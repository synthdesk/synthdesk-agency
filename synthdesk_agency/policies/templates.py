"""Empty policy shells (stubs; no business logic)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .base import Policy
from ..core.context import AgencyContext
from ..core.decision import Decision


@dataclass(frozen=True)
class NoOpPolicy(Policy):
    """Policy that returns no decision (inert default)."""

    def evaluate(self, context: AgencyContext) -> Optional[Decision]:
        return None

