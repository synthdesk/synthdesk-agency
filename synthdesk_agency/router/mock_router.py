"""Mock router adapter for schema conformance and null-handling tests."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")


def route(candidate_aggregate) -> dict:
    return {
        "aggregate_state": "indeterminate",
        "constraint_flags": {"mock_router_active"},
        "salience_tags": set(),
        "veto_applied": True,
        "audit_reference": None,
    }
