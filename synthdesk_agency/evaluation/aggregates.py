"""Aggregation surfaces for advisory scores (no resolution)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Optional, Sequence

from .disagreement import Disagreement
from .scorecard import ScoreCard


@dataclass(frozen=True)
class AggregateView:
    """Parallel view of advisory scores and their disagreements.

    Notes:
    - scorecards stay parallel
    - nothing is merged
    - nothing is averaged
    - nothing “wins”
    """

    scorecards: Sequence[ScoreCard]
    disagreement: Optional[Disagreement] = None
