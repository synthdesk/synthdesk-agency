"""Rank options (stub; advisory-only)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class Ranker:
    """Stub ranker for advisory options."""

    def rank(self, options: Sequence[dict]) -> Optional[Sequence[dict]]:
        pass

