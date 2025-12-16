"""Hourly mean structure for 60s candles.

Input: path to candle_60s.jsonl
Group candles by hour (UTC)
Print mean range and body per hour
Print mean tick_count per hour
"""

from __future__ import annotations

import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Tuple


sys.dont_write_bytecode = True


def _parse_ts(value: object) -> datetime:
    if not isinstance(value, str):
        raise TypeError("timestamp must be a string")
    s = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError("timestamp missing timezone")
    return dt.astimezone(timezone.utc)


def _iter_hour_ranges_bodies_ticks(path: Path) -> Iterator[Tuple[int, float, float, int]]:
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                ts_open = _parse_ts(rec["ts_open_utc"])
                o = float(rec["open"])
                h = float(rec["high"])
                l = float(rec["low"])
                c = float(rec["close"])
                ticks = int(rec["tick_count"])
                if h < l:
                    raise ValueError("high < low")
                candle_range = h - l
                candle_body = abs(c - o)
            except Exception as exc:
                print(f"WARNING: skipping malformed line {line_no}: {exc}")
                continue
            yield ts_open.hour, candle_range, candle_body, ticks


def _fmt(x: float) -> str:
    return f"{x:.10g}"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python analysis/candles/temporal_structure.py <candle_60s.jsonl>")
        return 1

    path = Path(argv[1])

    ranges_by_hour: list[list[float]] = [[] for _ in range(24)]
    bodies_by_hour: list[list[float]] = [[] for _ in range(24)]
    ticks_by_hour: list[list[int]] = [[] for _ in range(24)]

    try:
        for hour, r, b, t in _iter_hour_ranges_bodies_ticks(path):
            ranges_by_hour[hour].append(r)
            bodies_by_hour[hour].append(b)
            ticks_by_hour[hour].append(t)
    except OSError as exc:
        print(f"ERROR: cannot read file: {exc}")
        return 1

    print("hourly_mean_utc:")
    print("hour  n  mean_range  mean_body  mean_tick_count")
    for hour in range(24):
        if not ranges_by_hour[hour]:
            continue
        n = len(ranges_by_hour[hour])
        mean_range = statistics.fmean(ranges_by_hour[hour])
        mean_body = statistics.fmean(bodies_by_hour[hour])
        mean_ticks = statistics.fmean(ticks_by_hour[hour])
        print(f"{hour:02d}    {n}  {_fmt(mean_range)}  {_fmt(mean_body)}  {_fmt(mean_ticks)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
