"""Aggregation surfaces for advisory scores (no resolution)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from .disagreement import Disagreement
from .scorecard import ScoreCard


@dataclass(frozen=True)
class AggregateView:
    """Parallel view of advisory scores and their disagreements.

    Notes:
    - scorecards stay parallel
    - nothing is merged
    - nothing is averaged
    - nothing “wins”
    """

    scorecards: Sequence[ScoreCard]
    disagreement: Optional[Disagreement] = None
