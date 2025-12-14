"""Decision trace records (advisory-only; inert)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from .decision import Decision


@dataclass(frozen=True)
class DecisionTrace:
    """Explainability record describing how a decision was formed."""

    decision: Optional[Decision]
    considered_policies: Optional[Sequence[str]] = None
    notes: Optional[Sequence[str]] = None

