"""Temporal analysis interface (advisory-only; no conclusions)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from .timeseries import TemporalSeries


class TemporalAnalyzer(ABC):
    """Interface for analyzing temporal advisory evolution."""

    @abstractmethod
    def analyze(self, series: TemporalSeries) -> Optional[dict]:
        pass

