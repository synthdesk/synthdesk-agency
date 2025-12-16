"""Assert tick observation monotonicity.

Invariant: within a `tick_observation.jsonl` file, for each `asset`, `ts_utc` must
be strictly increasing in file order.
"""

import json
import sys
from datetime import datetime


def _parse_ts(s: str) -> datetime:
    if not isinstance(s, str):
        raise TypeError("ts_utc must be a string")
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError("ts_utc missing timezone offset")
    return dt


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python inspection/assert_tick_integrity.py <tick_observation.jsonl>")
        return 2

    path = argv[1]
    last_dt: dict[str, datetime] = {}
    last_s: dict[str, str] = {}

    with open(path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                asset = rec["asset"]
                ts_s = rec["ts_utc"]
                if not isinstance(asset, str):
                    raise TypeError("asset must be a string")
                ts_dt = _parse_ts(ts_s)
            except Exception as exc:
                print(f"ERROR: invalid record at line {line_no}: {exc}")
                return 1

            prev_dt = last_dt.get(asset)
            if prev_dt is not None and not (ts_dt > prev_dt):
                print(
                    f"ERROR: non-monotonic ts_utc for asset={asset} at line {line_no}: "
                    f"prev={last_s[asset]} curr={ts_s}"
                )
                return 1

            last_dt[asset] = ts_dt
            last_s[asset] = ts_s

    print("OK: tick monotonicity verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
