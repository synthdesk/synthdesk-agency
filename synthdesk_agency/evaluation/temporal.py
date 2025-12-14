"""Temporal advisory records (regime-sensitive, non-resolving)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .disagreement import Disagreement
from .scorecard import ScoreCard


@dataclass(frozen=True)
class TemporalSnapshot:
    """Snapshot of advisory evaluation at a point in time."""

    timestamp: datetime
    scorecard: Optional[ScoreCard] = None
    disagreement: Optional[Disagreement] = None
