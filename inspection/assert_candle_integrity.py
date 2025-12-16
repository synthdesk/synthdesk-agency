"""Assert basic candle integrity invariants.

Checks:
- ts_open_utc is strictly increasing
- candles do not overlap
- asset and timeframe are consistent within the file
"""

import json
import sys
from datetime import datetime, timezone


def _parse_ts(value: object) -> datetime:
    if not isinstance(value, str):
        raise TypeError("timestamp must be a string")
    s = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        raise ValueError("timestamp missing timezone")
    return dt.astimezone(timezone.utc)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(
            "Usage: python inspection/assert_candle_integrity.py <candle_60s.jsonl>",
            file=sys.stderr,
        )
        return 1

    path = argv[1]

    prev_open = None
    prev_close = None
    asset = None
    timeframe = None
    seen = 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    rec = json.loads(line)

                    ts_open = _parse_ts(rec["ts_open_utc"])
                    ts_close = _parse_ts(rec["ts_close_utc"])
                    rec_asset = rec["asset"]
                    rec_tf = rec["timeframe"]
                except Exception as exc:
                    print(
                        f"WARNING: skipping malformed line {line_no}: {exc}",
                        file=sys.stderr,
                    )
                    continue

                if asset is None:
                    asset = rec_asset
                    timeframe = rec_tf
                else:
                    if rec_asset != asset:
                        print(
                            f"ERROR: asset mismatch at line {line_no}",
                            file=sys.stderr,
                        )
                        return 1
                    if rec_tf != timeframe:
                        print(
                            f"ERROR: timeframe mismatch at line {line_no}",
                            file=sys.stderr,
                        )
                        return 1

                if prev_open is not None:
                    if ts_open <= prev_open:
                        print(
                            f"ERROR: ts_open_utc not strictly increasing at line {line_no}",
                            file=sys.stderr,
                        )
                        return 1
                    if ts_open < prev_close:
                        print(
                            f"ERROR: candle overlap at line {line_no}",
                            file=sys.stderr,
                        )
                        return 1

                prev_open = ts_open
                prev_close = ts_close
                seen += 1

    except OSError as exc:
        print(f"ERROR: cannot read file: {exc}", file=sys.stderr)
        return 1

    if seen == 0:
        print("ERROR: no valid candle records found", file=sys.stderr)
        return 1

    print("OK: candle integrity verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
