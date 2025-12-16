"""
Descriptive candle-level regime classifier v1.

Consumes 60s candles for a single asset/day and emits a coarse regime
classification with evidence. No decisions, no signals.
"""

import json
import sys
from datetime import datetime
from statistics import mean

CLASSIFIER_VERSION = "v1.0.0"
EPS = 1e-9


def _parse_ts(s: str) -> datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return datetime.fromisoformat(s)


def _percentile(values, p):
    values = sorted(values)
    if not values:
        return 0.0
    k = int(round((p / 100) * (len(values) - 1)))
    return values[k]


def main(argv):
    if len(argv) != 2:
        print(
            "Usage: python analysis/regimes/classify_day_v1.py <candle_60s.jsonl>",
            file=sys.stderr,
        )
        return 1

    path = argv[1]

    ranges = []
    bodies = []
    directions = []
    candles = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                c = json.loads(line)
                o = float(c["open"])
                h = float(c["high"])
                l = float(c["low"])
                cl = float(c["close"])
                ts = _parse_ts(c["ts_open_utc"])
            except Exception:
                continue

            r = h - l
            b = abs(cl - o)
            d = cl - o

            ranges.append(r)
            bodies.append(b)
            directions.append(d)
            candles.append((ts, o, cl, r))

    if not candles:
        print("ERROR: no valid candles", file=sys.stderr)
        return 1

    asset = json.loads(open(path).readline())["asset"]
    day = candles[0][0].strftime("%Y-%m-%d")

    mean_range = mean(ranges)
    p50 = _percentile(ranges, 50)
    p90 = _percentile(ranges, 90)
    body_ratio = mean(b / max(r, EPS) for b, r in zip(bodies, ranges))
    up_frac = sum(1 for d in directions if d > 0) / len(directions)

    vol_ratio = p90 / max(p50, EPS)
    if vol_ratio < 1.5:
        vol_regime = "low"
    elif vol_ratio < 2.5:
        vol_regime = "medium"
    else:
        vol_regime = "high"

    n = len(candles)
    early = candles[: n // 3]
    late = candles[-n // 3 :]

    early_mean = mean(c[3] for c in early)
    late_mean = mean(c[3] for c in late)
    delta = late_mean - early_mean

    if delta > 0.1 * mean_range:
        structure = "expanding"
    elif delta < -0.1 * mean_range:
        structure = "compressing"
    else:
        structure = "flat"

    first_open = candles[0][1]
    last_close = candles[-1][2]
    net_move = last_close - first_open
    total_range = sum(ranges)

    if net_move > 0.2 * total_range:
        trend = "bullish"
    elif net_move < -0.2 * total_range:
        trend = "bearish"
    else:
        trend = "neutral"

    out = {
        "day": day,
        "asset": asset,
        "volatility_regime": vol_regime,
        "structure": structure,
        "trend_bias": trend,
        "evidence": {
            "mean_range": round(mean_range, 4),
            "range_p50": round(p50, 4),
            "range_p90": round(p90, 4),
            "body_to_range_ratio": round(body_ratio, 4),
            "up_fraction": round(up_frac, 4),
            "early_mean_range": round(early_mean, 4),
            "late_mean_range": round(late_mean, 4),
        },
        "classifier_version": CLASSIFIER_VERSION,
    }

    print(json.dumps(out, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

