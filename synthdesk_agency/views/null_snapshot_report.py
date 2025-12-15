"""Read-only renderer for router epistemic snapshots with explicit veto visibility."""

from __future__ import annotations


def render_null_snapshot(epistemic_snapshot: dict) -> str:
    veto_applied = epistemic_snapshot.get("veto_applied")
    aggregate_state = epistemic_snapshot.get("aggregate_state")
    constraint_flags = epistemic_snapshot.get("constraint_flags")
    audit_reference = epistemic_snapshot.get("audit_reference")

    lines: list[str] = [
        "router veto active",
        "",
        f"veto_applied: {veto_applied!r}",
        "no action is permitted.",
        "output is descriptive only.",
        "",
        f"aggregate_state: {aggregate_state!r}",
        f"audit_reference: {audit_reference!r}",
        "",
        "constraint_flags (unordered):",
    ]

    if isinstance(constraint_flags, (set, frozenset, list, tuple)):
        for flag in constraint_flags:
            lines.append(f"- {flag!r}" if not isinstance(flag, str) else f"- {flag}")
    else:
        lines.append(f"- {constraint_flags!r}")

    return "\n".join(lines)

