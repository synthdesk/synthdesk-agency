"""Offline simulation records (advisory-only; inert)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

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
