"""Offline advisory simulator (stub; no execution)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from ..core.agency import Agency
from ..core.context import AgencyContext
from .simulation import SimulationReport, SimulationResult


@dataclass(frozen=True)
class Simulator:
    """Replay container for advisory-only evaluation."""

    agency: Agency

    def replay(self, contexts: Sequence[AgencyContext]) -> SimulationReport:
        """Replay contexts through the agency explainability surface."""
        results = [
            SimulationResult(
                context=context,
                trace=self.agency.explain(context),
            )
            for context in contexts
        ]
        return SimulationReport(results=results)

