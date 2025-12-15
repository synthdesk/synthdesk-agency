"""Temporal regime churn records and interface (advisory-only; descriptive)."""

from __future__ import annotations

import os
import sys

from ... import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Sequence

from ...core.regime_hypothesis import RegimeHypothesis


@dataclass(frozen=True)
class TemporalRegimeSnapshot:
    """Snapshot of regime hypotheses at a point in time.

    Notes:
    - hypotheses are descriptive, not resolved
    - multiple hypotheses may coexist
    - ordering does not imply priority
    - does not imply detection or transition truth
    """

    timestamp: str
    regimes: Sequence[RegimeHypothesis]
    notes: Optional[Sequence[str]] = None


@dataclass(frozen=True)
class TemporalRegimeSeries:
    """Sequence of regime snapshots (structure only).

    Notes:
    - no assumptions about ordering enforcement
    - no deltas, trends, or statistics
    - no transitions, thresholds, or alerts
    - just structure
    """

    snapshots: Sequence[TemporalRegimeSnapshot]
    notes: Optional[Sequence[str]] = None


@dataclass(frozen=True)
class RegimeChurn:
    """Descriptive record of how regime hypotheses evolve over time.

    Notes:
    - descriptive only
    - does not resolve disagreement or transitions
    - does not imply action or execution
    """

    series: TemporalRegimeSeries
    description: Optional[str] = None
    notes: Optional[Sequence[str]] = None


class RegimeChurnAnalyzer(ABC):
    """Interface for describing regime churn (no detection, no resolution)."""

    @abstractmethod
    def analyze(self, series: TemporalRegimeSeries) -> Optional[RegimeChurn]:
        pass
