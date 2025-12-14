"""Temporal disagreement records (expressive, non-resolving)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from .snapshot import TemporalSnapshot


@dataclass(frozen=True)
class TemporalDisagreement:
    """Represents divergence or instability across time.

    Notes:
    - descriptive only
    - does not imply error or action
    - does not resolve disagreement
    """

    snapshots: Sequence[TemporalSnapshot]
    pattern: Optional[str] = None
    notes: Optional[Sequence[str]] = None

