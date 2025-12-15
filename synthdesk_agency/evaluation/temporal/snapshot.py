"""Temporal snapshot of advisory aggregates (record only)."""

from __future__ import annotations

import os
import sys

from ... import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass

from ..aggregates import AggregateView


@dataclass(frozen=True)
class TemporalSnapshot:
    """Represents advisory state at a specific moment in time."""

    timestamp: str
    aggregate: AggregateView
