"""Offline simulation harness for replaying advisory contexts (stub)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Iterable, List, Sequence

from ..core.agency import Agency
from ..core.context import AgencyContext
from ..core.trace import DecisionTrace


@dataclass(frozen=True)
class ReplayResult:
    """Inert replay result containing decision traces."""

    traces: Sequence[DecisionTrace]


@dataclass(frozen=True)
class OfflineSimulationHarness:
    """Replays advisory contexts through an agency without side effects."""

    agency: Agency

    def replay(self, contexts: Iterable[AgencyContext]) -> ReplayResult:
        traces: List[DecisionTrace] = []
        for context in contexts:
            traces.append(self.agency.explain(context))
        return ReplayResult(traces=tuple(traces))
