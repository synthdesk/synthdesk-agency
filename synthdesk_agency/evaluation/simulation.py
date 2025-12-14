"""Offline simulation records (advisory-only; inert)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from ..core.context import AgencyContext
from ..core.trace import DecisionTrace


@dataclass(frozen=True)
class SimulationResult:
    """Result of replaying a single advisory context."""

    context: AgencyContext
    trace: DecisionTrace


@dataclass(frozen=True)
class SimulationReport:
    """Collection of simulation results."""

    results: Sequence[SimulationResult]
    metadata: Optional[dict] = None

