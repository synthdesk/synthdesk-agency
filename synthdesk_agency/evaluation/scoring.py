"""Scoring interface (advisory-only; no thresholds)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from abc import ABC, abstractmethod
from typing import Optional

from ..core.context import AgencyContext
from .scorecard import ScoreCard


class Scorer(ABC):
    """Interface for producing advisory scorecards."""

    @abstractmethod
    def score(self, context: AgencyContext) -> Optional[ScoreCard]:
        pass
