"""Score aggregation container (advisory-only)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional, Sequence

from .scores import Score


@dataclass(frozen=True)
class ScoreCard:
    """Collection of advisory scores."""

    scores: Mapping[str, Score]
    summary: Optional[str] = None
    notes: Optional[Sequence[str]] = None

