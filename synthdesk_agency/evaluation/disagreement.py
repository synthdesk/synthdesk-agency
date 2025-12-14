"""Disagreement records (expressive, non-resolving)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional

from .scores import Score


@dataclass(frozen=True)
class Disagreement:
    """Represents divergence between multiple advisory scores.

    Notes:
    - magnitude is descriptive, not decisive
    - disagreement is information, not error
    """

    scores: Mapping[str, Score]
    magnitude: Optional[float] = None
    notes: Optional[str] = None
