"""Temporal snapshot of regime hypotheses (record only)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .regime_hypothesis import RegimeHypothesis


@dataclass(frozen=True)
class TemporalRegimeSnapshot:
    """Represents regime hypotheses at a specific moment in time."""

    timestamp: str
    regimes: Sequence[RegimeHypothesis]

