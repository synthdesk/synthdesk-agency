"""Regime hypothesis records (advisory-only; inert)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Sequence


@dataclass(frozen=True)
class RegimeHypothesis:
    """Named market regime hypothesis (no detection, inference, or transitions)."""

    label: str
    confidence: Optional[float] = None
    rationale: Optional[Sequence[str]] = None
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None


@dataclass(frozen=True)
class RegimeSnapshot:
    """Time-stamped collection of regime hypotheses (structure only)."""

    timestamp: datetime
    hypotheses: Sequence[RegimeHypothesis]
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None

