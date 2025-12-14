"""Scoring interface (advisory-only; no thresholds)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from ..core.context import AgencyContext
from .scorecard import ScoreCard


class Scorer(ABC):
    """Interface for producing advisory scorecards."""

    @abstractmethod
    def score(self, context: AgencyContext) -> Optional[ScoreCard]:
        pass
