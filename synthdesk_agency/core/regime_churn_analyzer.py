"""Interface for describing regime instability across time (advisory-only)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Sequence

from .regime_churn import RegimeChurn
from .temporal_regime_snapshot import TemporalRegimeSnapshot


class RegimeChurnAnalyzer(ABC):
    """Interface for analyzing regime hypothesis evolution."""

    @abstractmethod
    def analyze(
        self,
        snapshots: Sequence[TemporalRegimeSnapshot],
    ) -> Optional[RegimeChurn]:
        pass

