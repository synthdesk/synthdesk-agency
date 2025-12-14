"""Temporal regime churn records (expressive, non-resolving)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from .temporal_regime_snapshot import TemporalRegimeSnapshot


@dataclass(frozen=True)
class RegimeChurn:
    """Describes how regime hypotheses evolve across time.

    Notes:
    - descriptive only
    - does not imply detection or transition
    - instability is information, not error
    """

    snapshots: Sequence[TemporalRegimeSnapshot]
    pattern: Optional[str] = None
    notes: Optional[Sequence[str]] = None

