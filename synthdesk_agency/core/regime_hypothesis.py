"""Regime hypothesis record (advisory-only; descriptive)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class RegimeHypothesis:
    """Represents a hypothesized market regime.

    Notes:
    - does not imply detection
    - does not imply exclusivity
    - multiple hypotheses may coexist
    """

    name: str
    confidence: Optional[float] = None
    notes: Optional[Sequence[str]] = None

