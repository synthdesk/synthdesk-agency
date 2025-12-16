"""
Run candle analysis scripts for a given day and persist stdout as artifacts.
"""

import subprocess
import sys
from pathlib import Path


sys.dont_write_bytecode = True


ANALYSES = [
    ("describe_day", "analysis/candles/describe_day.py"),
    ("distribution", "analysis/candles/distribution.py"),
    ("temporal_structure", "analysis/candles/temporal_structure.py"),
]


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(
            "Usage: python tools/run_candle_analysis_day.py <candle_60s.jsonl> <YYYY-MM-DD>",
            file=sys.stderr,
        )
        return 1

    candle_path = Path(argv[1])
    day = argv[2]

    out_dir = Path("artifacts") / "analysis" / day
    out_dir.mkdir(parents=True, exist_ok=True)

    for name, script in ANALYSES:
        out_path = out_dir / f"{name}.txt"
        proc = subprocess.run(
            [sys.executable, script, str(candle_path)],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            if proc.stdout:
                print(proc.stdout, file=sys.stderr, end="")
            if proc.stderr:
                print(proc.stderr, file=sys.stderr, end="")
            return proc.returncode

        out_path.write_text(proc.stdout, encoding="utf-8")
        print(f"WROTE {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

