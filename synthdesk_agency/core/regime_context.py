"""Associates an advisory context with regime hypotheses."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from .regime_hypothesis import RegimeHypothesis


@dataclass(frozen=True)
class RegimeContext:
    """Regime hypotheses associated with a given advisory context.

    Notes:
    - hypotheses are descriptive, not resolved
    - multiple hypotheses may coexist
    - ordering does not imply priority
    """

    regimes: Sequence[RegimeHypothesis]
    notes: Optional[Sequence[str]] = None
