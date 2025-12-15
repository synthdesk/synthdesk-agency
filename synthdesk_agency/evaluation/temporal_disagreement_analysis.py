"""Temporal disagreement analysis interface (advisory-only; no conclusions)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from abc import ABC, abstractmethod
from typing import Optional

from .temporal_disagreement import TemporalDisagreementSeries


class TemporalDisagreementAnalyzer(ABC):
    """Interface for analyzing temporal disagreement evolution."""

    @abstractmethod
    def analyze(self, series: TemporalDisagreementSeries) -> Optional[dict]:
        pass
