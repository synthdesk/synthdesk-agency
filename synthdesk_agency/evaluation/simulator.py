"""Offline advisory simulator (stub; no execution)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

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
