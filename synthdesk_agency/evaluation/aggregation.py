"""Aggregation interface (advisory-only; no collapse)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from abc import ABC, abstractmethod
from typing import Optional, Sequence

from .aggregates import AggregateView
from .scorecard import ScoreCard


class Aggregator(ABC):
    """Interface for combining multiple scorecards without resolving them."""

    @abstractmethod
    def aggregate(self, scorecards: Sequence[ScoreCard]) -> Optional[AggregateView]:
        pass
