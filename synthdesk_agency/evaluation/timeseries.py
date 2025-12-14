"""Temporal sequences for advisory evaluation (no interpretation)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from .temporal import TemporalSnapshot


@dataclass(frozen=True)
class TemporalSeries:
    """Sequence of temporal advisory snapshots (structure only).

    Notes:
    - no assumptions about ordering enforcement
    - no trend detection
    - no statistics
    - just structure
    """

    snapshots: Sequence[TemporalSnapshot]
    notes: Optional[str] = None
