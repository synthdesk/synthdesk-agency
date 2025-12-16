# FROZEN — candle_builder_v1.py
# builder_version: v1.0.0
# status: immutable
# any changes require a new builder version (v2+)

"""
Passive 60s candle builder v1.

Transforms tick_observation.jsonl into closed 60-second OHLC candles.
Deterministic, replayable, read-only input, append-only output.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

BUILDER_VERSION = "v1.0.0"
TIMEFRAME_SECONDS = 60
TIMEFRAME_LABEL = "60s"
OUT_FILENAME = "candle_60s.jsonl"
RUNS_ROOT = Path("runs")


def _parse_ts(value: object) -> datetime:
    if not isinstance(value, str):
        raise TypeError("ts_utc must be a string")
    s = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError("ts_utc missing timezone")
    return dt.astimezone(timezone.utc)


def _bucket_start(ts: datetime) -> datetime:
    epoch = int(ts.timestamp())
    bucket = (epoch // TIMEFRAME_SECONDS) * TIMEFRAME_SECONDS
    return datetime.fromtimestamp(bucket, tz=timezone.utc)


def _bucket_close(bucket_open: datetime) -> datetime:
    return bucket_open + timedelta(seconds=TIMEFRAME_SECONDS) - timedelta(microseconds=1)


def _read_last_emitted_bucket(path: Path) -> Optional[datetime]:
    if not path.exists():
        return None
    try:
        with path.open("rb") as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
            if size == 0:
                return None
            offset = min(size, 4096)
            f.seek(-offset, os.SEEK_END)
            lines = f.read().decode("utf-8", errors="ignore").splitlines()
            for line in reversed(lines):
                if line.strip():
                    rec = json.loads(line)
                    ts_open = rec.get("ts_open_utc")
                    if ts_open is None:
                        return None
                    return _parse_ts(ts_open)
    except Exception:
        return None
    return None


@dataclass
class _CandleState:
    bucket_open: datetime
    open: float
    high: float
    low: float
    close: float
    tick_count: int = 1
    sources: set[str] = field(default_factory=set)


def _out_path(target_date: str, asset: str) -> Path:
    return RUNS_ROOT / target_date / asset / OUT_FILENAME


def _emit_candle(target_date: str, asset: str, state: _CandleState) -> None:
    out_path = _out_path(target_date, asset)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "ts_open_utc": state.bucket_open.isoformat(),
        "ts_close_utc": _bucket_close(state.bucket_open).isoformat(),
        "asset": asset,
        "timeframe": TIMEFRAME_LABEL,
        "open": state.open,
        "high": state.high,
        "low": state.low,
        "close": state.close,
        "tick_count": state.tick_count,
        "source_set": sorted(state.sources),
        "builder_version": BUILDER_VERSION,
    }

    with out_path.open("a", encoding="utf-8") as out:
        out.write(json.dumps(record) + "\n")


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(
            "Usage: python builders/candle_builder_v1.py <tick_observation.jsonl> <YYYY-MM-DD> [ASSET]",
            file=sys.stderr,
        )
        return 1

    tick_path = Path(argv[1])
    target_date = argv[2]
    asset_filter = argv[3] if len(argv) >= 4 else None

    state_by_asset: dict[str, _CandleState] = {}
    last_emitted_bucket_by_asset: dict[str, Optional[datetime]] = {}

    try:
        with tick_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    rec = json.loads(line)
                    asset = rec["asset"]
                    price = float(rec["price"])
                    source = rec.get("source")
                    ts = _parse_ts(rec["ts_utc"])
                except Exception:
                    continue

                if not isinstance(asset, str):
                    continue

                if asset_filter and asset != asset_filter:
                    continue

                if ts.strftime("%Y-%m-%d") != target_date:
                    continue

                bucket = _bucket_start(ts)
                if asset not in last_emitted_bucket_by_asset:
                    last_emitted_bucket_by_asset[asset] = _read_last_emitted_bucket(
                        _out_path(target_date, asset)
                    )

                last_emitted_bucket = last_emitted_bucket_by_asset[asset]
                if last_emitted_bucket is not None and bucket <= last_emitted_bucket:
                    continue

                state = state_by_asset.get(asset)
                if state is None:
                    state = _CandleState(
                        bucket_open=bucket,
                        open=price,
                        high=price,
                        low=price,
                        close=price,
                    )
                    if isinstance(source, str) and source:
                        state.sources.add(source)
                    state_by_asset[asset] = state
                    continue

                if bucket < state.bucket_open:
                    continue

                if bucket == state.bucket_open:
                    state.high = max(state.high, price)
                    state.low = min(state.low, price)
                    state.close = price
                    state.tick_count += 1
                    if isinstance(source, str) and source:
                        state.sources.add(source)
                    continue

                # Bucket rollover: previous bucket is now known-closed for this asset.
                _emit_candle(target_date, asset, state)
                last_emitted_bucket_by_asset[asset] = state.bucket_open
                next_state = _CandleState(
                    bucket_open=bucket,
                    open=price,
                    high=price,
                    low=price,
                    close=price,
                )
                if isinstance(source, str) and source:
                    next_state.sources.add(source)
                state_by_asset[asset] = next_state

    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
