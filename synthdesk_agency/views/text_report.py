"""Human-readable text report renderer for AgencySnapshot (advisory-only)."""

from __future__ import annotations

from typing import List, Sequence

from ..core.agency_snapshot import AgencySnapshot


def render_text_report(
    snapshot: AgencySnapshot,
) -> Sequence[str]:
    lines: List[str] = []

    lines.append("agency snapshot (advisory-only; descriptive)")

    lines.append("context:")
    if snapshot.context is None:
        lines.append("- absent")
    else:
        lines.append("- present")
        lines.append(f"- reported: {snapshot.context!r}")

    lines.append("decisions:")
    if snapshot.decisions is None:
        lines.append("- absent")
    else:
        lines.append("- present (no endorsement; no execution implied)")
        for decision in snapshot.decisions:
            lines.append(f"- reported: {decision!r}")

    lines.append("scorecards:")
    if snapshot.scorecards is None:
        lines.append("- absent")
    else:
        lines.append("- present (parallel; no ordering implied)")
        for scorecard in snapshot.scorecards:
            lines.append(f"- reported: {scorecard!r}")

    lines.append("disagreement:")
    if snapshot.disagreement is None:
        lines.append("- absent")
    else:
        lines.append("- present (information; no resolution implied)")
        lines.append(f"- reported: {snapshot.disagreement!r}")

    lines.append("aggregate view:")
    if snapshot.aggregate_view is None:
        lines.append("- absent")
    else:
        lines.append("- present (parallel; no resolution implied)")
        lines.append(f"- reported: {snapshot.aggregate_view!r}")

    lines.append("temporal view:")
    if snapshot.temporal_view is None:
        lines.append("- absent")
    else:
        lines.append("- present (reported; no resolution implied)")
        lines.append(f"- reported: {snapshot.temporal_view!r}")

    lines.append("regime churn:")
    if snapshot.regime_churn is None:
        lines.append("- absent")
    else:
        lines.append("- present (descriptive; no transition implied)")
        lines.append(f"- reported: {snapshot.regime_churn!r}")

    lines.append("notes:")
    if snapshot.notes is None:
        lines.append("- absent")
    else:
        lines.append("- present")
        for note in snapshot.notes:
            lines.append(f"- {note}")

    return lines

