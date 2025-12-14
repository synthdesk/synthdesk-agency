"""Score weighting records (advisory-only; inert)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class Weight:
    """Named weight record used for scoring/aggregation (record only)."""

    name: str
    weight: Optional[float] = None
    enabled: Optional[bool] = None
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None


@dataclass(frozen=True)
class WeightSet:
    """Collection of named weights."""

    weights: Sequence[Weight]
    notes: Optional[Sequence[str]] = None
    metadata: Optional[dict] = None

