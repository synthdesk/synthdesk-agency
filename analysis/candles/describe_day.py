"""Describe a day of 60s candles.

Input: path to candle_60s.jsonl
Print:
- total candles
- first ts_open_utc
- last ts_open_utc
- candles per hour (table)
- number of missing minutes inferred from gaps
- earliest hour observed
- latest hour observed
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator


sys.dont_write_bytecode = True


def _parse_ts(value: object) -> datetime:
    if not isinstance(value, str):
        raise TypeError("timestamp must be a string")
    s = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError("timestamp missing timezone")
    return dt.astimezone(timezone.utc)


def _iter_ts_open(path: Path) -> Iterator[datetime]:
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                ts_open = _parse_ts(rec["ts_open_utc"])
            except Exception as exc:
                print(f"WARNING: skipping malformed line {line_no}: {exc}")
                continue
            yield ts_open


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python analysis/candles/describe_day.py <candle_60s.jsonl>")
        return 1

    path = Path(argv[1])

    total = 0
    first_open: datetime | None = None
    last_open: datetime | None = None
    per_hour = [0] * 24
    opens: list[datetime] = []

    try:
        for ts_open in _iter_ts_open(path):
            per_hour[ts_open.hour] += 1
            opens.append(ts_open)
            total += 1
    except OSError as exc:
        print(f"ERROR: cannot read file: {exc}")
        return 1

    missing_minutes = 0
    earliest_hour: int | None = None
    latest_hour: int | None = None

    if opens:
        opens.sort()
        first_open = opens[0]
        last_open = opens[-1]
        earliest_hour = first_open.hour
        latest_hour = last_open.hour
        prev = opens[0]
        for curr in opens[1:]:
            delta_seconds = int((curr - prev).total_seconds())
            if delta_seconds >= 120:
                missing_minutes += (delta_seconds // 60) - 1
            prev = curr

    print(f"total_candles: {total}")
    print(f"first_ts_open_utc: {first_open.isoformat() if first_open else 'NA'}")
    print(f"last_ts_open_utc: {last_open.isoformat() if last_open else 'NA'}")
    print("candles_per_hour_utc:")
    print("hour  candles")
    for hour in range(24):
        print(f"{hour:02d}    {per_hour[hour]}")
    print(f"missing_minutes_inferred: {missing_minutes}")
    print(f"earliest_hour_observed_utc: {earliest_hour if earliest_hour is not None else 'NA'}")
    print(f"latest_hour_observed_utc: {latest_hour if latest_hour is not None else 'NA'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
