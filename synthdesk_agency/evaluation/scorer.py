"""Score signals (stub; advisory-only)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from ..core.context import AgencyContext


@dataclass(frozen=True)
class SignalScorer:
    """Stub scorer for observational signals."""

    def score(self, context: AgencyContext) -> Optional[dict]:
        pass

