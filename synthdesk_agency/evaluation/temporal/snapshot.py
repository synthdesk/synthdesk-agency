"""Temporal snapshot of advisory aggregates (record only)."""

from __future__ import annotations

from dataclasses import dataclass

from ..aggregates import AggregateView


@dataclass(frozen=True)
class TemporalSnapshot:
    """Represents advisory state at a specific moment in time."""

    timestamp: str
    aggregate: AggregateView

