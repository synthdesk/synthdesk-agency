"""Advisory score records (expressive, non-vetoing)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Score:
    """Continuous advisory score for a signal or decision."""

    value: float
    confidence: Optional[float] = None
    label: Optional[str] = None
    notes: Optional[str] = None

