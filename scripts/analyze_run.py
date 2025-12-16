#!/usr/bin/env python3
"""
Manual, one-off advisory analysis tool.

Reads a JSONL file of listener-like event objects and produces a static summary report.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Optional


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="scripts/analyze_run.py")
    parser.add_argument("jsonl_path", help="Path to a JSONL file of events")
    parser.add_argument(
        "--output",
        help="Optional output file path (must not be under runs/)",
        default=None,
    )
    return parser.parse_args(argv)


def _is_under_runs(path: Path) -> bool:
    parts = path.resolve().parts
    return "runs" in parts


def _error(message: str) -> int:
    print(message, file=sys.stderr)
    return 2


def _coerce_event_obj(raw: Any) -> Optional[dict[str, Any]]:
    return raw if isinstance(raw, dict) else None


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    in_path = Path(args.jsonl_path)
    if not in_path.exists() or not in_path.is_file():
        return _error(f"error=invalid_path path={in_path}")

    out_path: Optional[Path] = Path(args.output) if args.output else None
    if out_path is not None:
        if _is_under_runs(out_path):
            return _error(f"error=invalid_output_path detail=must_not_write_under_runs path={out_path}")
        if out_path.parent and not out_path.parent.exists():
            return _error(f"error=invalid_output_path detail=parent_missing path={out_path}")

    # Enable importing guarded advisory evaluation modules for this explicit, manual tool.
    os.environ.setdefault("PYTEST_CURRENT_TEST", "scripts/analyze_run.py")

    from synthdesk_agency.core.context import AgencyContext
    from synthdesk_agency.evaluation.scorer import SignalScorer
    from synthdesk_agency.signals.models import SignalEvent

    scorer = SignalScorer()

    totals = {
        "lines_total": 0,
        "lines_empty": 0,
        "json_errors": 0,
        "non_object_lines": 0,
        "events_parsed": 0,
        "events_scored": 0,
    }
    event_type_counts: Counter[str] = Counter()
    pair_counts: Counter[str] = Counter()
    first_timestamp: Optional[str] = None
    last_timestamp: Optional[str] = None
    last_error: Optional[str] = None

    with in_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            totals["lines_total"] += 1
            raw_line = line.strip()
            if not raw_line:
                totals["lines_empty"] += 1
                continue
            try:
                parsed = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                totals["json_errors"] += 1
                last_error = f"json_decode_error: {exc.msg}"
                continue

            obj = _coerce_event_obj(parsed)
            if obj is None:
                totals["non_object_lines"] += 1
                last_error = "invalid_schema: expected object"
                continue

            event_type = obj.get("event")
            pair = obj.get("pair")
            timestamp = obj.get("timestamp")

            if isinstance(timestamp, str):
                if first_timestamp is None:
                    first_timestamp = timestamp
                last_timestamp = timestamp

            if isinstance(event_type, str):
                event_type_counts[event_type] += 1
            if isinstance(pair, str):
                pair_counts[pair] += 1

            totals["events_parsed"] += 1

            signal_event = SignalEvent(
                event=str(event_type) if event_type is not None else "unknown",
                pair=str(pair) if pair is not None else "unknown",
                price=obj.get("price"),  # schema is advisory-only; allow non-float inputs
                timestamp=str(timestamp) if timestamp is not None else "",
                metrics=obj.get("metrics") if isinstance(obj.get("metrics"), dict) else None,
                version=obj.get("version") if isinstance(obj.get("version"), str) else None,
                tick_id=obj.get("tick_id") if isinstance(obj.get("tick_id"), int) else None,
            )

            context = AgencyContext(events=[signal_event], metadata={"source_path": str(in_path)})
            _ = scorer.score(context)
            totals["events_scored"] += 1

    report = {
        "input_path": str(in_path),
        "totals": totals,
        "first_timestamp": first_timestamp,
        "last_timestamp": last_timestamp,
        "event_types": dict(event_type_counts),
        "pairs": dict(pair_counts),
        "last_error": last_error,
        "advisory_only": True,
        "notes": [
            "This report is descriptive only.",
            "No routing, execution, or operational authority is implied.",
        ],
    }

    rendered = json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"

    if out_path is None:
        sys.stdout.write(rendered)
        return 0

    out_path.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
