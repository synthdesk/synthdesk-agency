"""Regime hypothesis records (advisory-only; descriptive)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class RegimeHypothesis:
    """Named hypothesis representing a latent market state.

    Notes:
    - descriptive, not assertive
    - may coexist with other hypotheses
    - does not imply detection or truth
    """

    name: str
    description: Optional[str] = None
    indicators: Optional[Sequence[str]] = None
    notes: Optional[Sequence[str]] = None

