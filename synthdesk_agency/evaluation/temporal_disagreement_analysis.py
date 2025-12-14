"""Temporal disagreement analysis interface (advisory-only; no conclusions)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from .temporal_disagreement import TemporalDisagreementSeries


class TemporalDisagreementAnalyzer(ABC):
    """Interface for analyzing temporal disagreement evolution."""

    @abstractmethod
    def analyze(self, series: TemporalDisagreementSeries) -> Optional[dict]:
        pass

