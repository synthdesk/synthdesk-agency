"""Distribution summary for 60s candles.

Input: path to candle_60s.jsonl
Compute:
- range = high - low
- body = abs(close - open)
- upper wick
- lower wick
Print:
- count
- min / mean / max for each metric
- p50 / p90 / p99 percentiles
"""

from __future__ import annotations

import json
import math
import statistics
import sys
from pathlib import Path
from typing import Iterable, Iterator, Tuple


sys.dont_write_bytecode = True


def _iter_metrics(path: Path) -> Iterator[Tuple[float, float, float, float]]:
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                o = float(rec["open"])
                h = float(rec["high"])
                l = float(rec["low"])
                c = float(rec["close"])
                if h < l:
                    raise ValueError("high < low")
                candle_range = h - l
                candle_body = abs(c - o)
                upper_wick = h - max(o, c)
                lower_wick = min(o, c) - l
                if upper_wick < 0:
                    raise ValueError("high < max(open, close)")
                if lower_wick < 0:
                    raise ValueError("low > min(open, close)")
            except Exception as exc:
                print(f"WARNING: skipping malformed line {line_no}: {exc}")
                continue
            yield candle_range, candle_body, upper_wick, lower_wick


def _percentile_sorted(sorted_values: list[float], p: float) -> float:
    if not sorted_values:
        raise ValueError("empty sample")
    if p <= 0:
        return sorted_values[0]
    if p >= 1:
        return sorted_values[-1]
    n = len(sorted_values)
    if n == 1:
        return sorted_values[0]
    pos = p * (n - 1)
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return sorted_values[lo]
    frac = pos - lo
    return sorted_values[lo] * (1 - frac) + sorted_values[hi] * frac


def _fmt(x: float) -> str:
    return f"{x:.10g}"


def _summarize(values: Iterable[float]) -> tuple[float, float, float, float, float, float]:
    data = list(values)
    if not data:
        raise ValueError("no valid records")
    data.sort()
    vmin = data[0]
    vmax = data[-1]
    mean = statistics.fmean(data)
    p50 = _percentile_sorted(data, 0.50)
    p90 = _percentile_sorted(data, 0.90)
    p99 = _percentile_sorted(data, 0.99)
    return vmin, mean, vmax, p50, p90, p99


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python analysis/candles/distribution.py <candle_60s.jsonl>")
        return 1

    path = Path(argv[1])
    ranges: list[float] = []
    bodies: list[float] = []
    upper_wicks: list[float] = []
    lower_wicks: list[float] = []

    try:
        for r, b, uw, lw in _iter_metrics(path):
            ranges.append(r)
            bodies.append(b)
            upper_wicks.append(uw)
            lower_wicks.append(lw)
    except OSError as exc:
        print(f"ERROR: cannot read file: {exc}")
        return 1

    if not ranges:
        print("count: 0")
        for name in ["range", "body", "upper_wick", "lower_wick"]:
            print(f"{name}:")
            print("  min:  NA")
            print("  mean: NA")
            print("  max:  NA")
            print("  p50:  NA")
            print("  p90:  NA")
            print("  p99:  NA")
        return 0

    print(f"count: {len(ranges)}")

    r_min, r_mean, r_max, r_p50, r_p90, r_p99 = _summarize(ranges)
    b_min, b_mean, b_max, b_p50, b_p90, b_p99 = _summarize(bodies)
    uw_min, uw_mean, uw_max, uw_p50, uw_p90, uw_p99 = _summarize(upper_wicks)
    lw_min, lw_mean, lw_max, lw_p50, lw_p90, lw_p99 = _summarize(lower_wicks)

    print("range:")
    print(f"  min:  {_fmt(r_min)}")
    print(f"  mean: {_fmt(r_mean)}")
    print(f"  max:  {_fmt(r_max)}")
    print(f"  p50:  {_fmt(r_p50)}")
    print(f"  p90:  {_fmt(r_p90)}")
    print(f"  p99:  {_fmt(r_p99)}")
    print("body:")
    print(f"  min:  {_fmt(b_min)}")
    print(f"  mean: {_fmt(b_mean)}")
    print(f"  max:  {_fmt(b_max)}")
    print(f"  p50:  {_fmt(b_p50)}")
    print(f"  p90:  {_fmt(b_p90)}")
    print(f"  p99:  {_fmt(b_p99)}")
    print("upper_wick:")
    print(f"  min:  {_fmt(uw_min)}")
    print(f"  mean: {_fmt(uw_mean)}")
    print(f"  max:  {_fmt(uw_max)}")
    print(f"  p50:  {_fmt(uw_p50)}")
    print(f"  p90:  {_fmt(uw_p90)}")
    print(f"  p99:  {_fmt(uw_p99)}")
    print("lower_wick:")
    print(f"  min:  {_fmt(lw_min)}")
    print(f"  mean: {_fmt(lw_mean)}")
    print(f"  max:  {_fmt(lw_max)}")
    print(f"  p50:  {_fmt(lw_p50)}")
    print(f"  p90:  {_fmt(lw_p90)}")
    print(f"  p99:  {_fmt(lw_p99)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
