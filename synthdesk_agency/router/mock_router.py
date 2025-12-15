"""Mock router adapter for schema conformance and null-handling tests."""

from __future__ import annotations


def route(candidate_aggregate) -> dict:
    return {
        "aggregate_state": "indeterminate",
        "constraint_flags": {"mock_router_active"},
        "salience_tags": set(),
        "veto_applied": True,
        "audit_reference": None,
    }

