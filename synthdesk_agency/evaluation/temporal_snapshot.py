"""Temporal aggregate snapshot records (advisory-only; structure only)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .aggregates import AggregateView


@dataclass(frozen=True)
class TemporalAggregateSnapshot:
    """Snapshot binding a timestamp to an aggregate view (structure only)."""

    timestamp: datetime
    aggregate: AggregateView

