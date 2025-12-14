"""Abstract policy interface (advisory-only; no execution paths)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from ..core.context import AgencyContext
from ..core.decision import Decision


class Policy(ABC):
    """Interface for transforming an input context into an advisory decision."""

    @abstractmethod
    def evaluate(self, context: AgencyContext) -> Optional[Decision]:
        pass

