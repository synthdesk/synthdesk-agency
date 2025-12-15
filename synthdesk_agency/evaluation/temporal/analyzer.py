"""Temporal analysis interface (advisory-only; no resolution)."""

from __future__ import annotations

import os
import sys

from ... import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from abc import ABC, abstractmethod
from typing import Optional, Sequence

from .disagreement import TemporalDisagreement
from .snapshot import TemporalSnapshot


class TemporalAnalyzer(ABC):
    """Interface for analyzing advisory evolution across time."""

    @abstractmethod
    def analyze(
        self,
        snapshots: Sequence[TemporalSnapshot],
    ) -> Optional[TemporalDisagreement]:
        pass
