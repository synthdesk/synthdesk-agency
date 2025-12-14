"""Temporal analysis interface (advisory-only; no resolution)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Sequence

from .disagreement import TemporalDisagreement
from .snapshot import TemporalSnapshot


class TemporalAnalyzer(ABC):
    """Interface for analyzing advisory evolution across time."""

    @abstractmethod
    def analyze(
        self,
        snapshots: Sequence[TemporalSnapshot],
    ) -> Optional[TemporalDisagreement]:
        pass

