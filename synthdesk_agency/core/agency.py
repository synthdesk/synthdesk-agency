"""Top-level coordinator for the advisory-only agency engine (stub)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .context import AgencyContext
from .decision import Decision
from .trace import DecisionTrace
from ..policies.stack import PolicyStack


@dataclass(frozen=True)
class Agency:
    """Inert coordinator that produces advisory decisions from an input context."""

    policies: PolicyStack

    def evaluate(self, context: AgencyContext) -> Optional[Decision]:
        pass

    def explain(self, context: AgencyContext) -> DecisionTrace:
        """Produce an inert decision trace without executing logic."""
        return DecisionTrace(decision=None)
