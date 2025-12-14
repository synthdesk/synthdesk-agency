"""Aggregation interface (advisory-only; no collapse)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Sequence

from .aggregates import AggregateView
from .scorecard import ScoreCard


class Aggregator(ABC):
    """Interface for combining multiple scorecards without resolving them."""

    @abstractmethod
    def aggregate(self, scorecards: Sequence[ScoreCard]) -> Optional[AggregateView]:
        pass
