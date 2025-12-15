"""Temporal evaluation surfaces (advisory-only; structure only)."""

import os
import sys

from ... import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from .snapshot import TemporalSnapshot
from .regime_churn import RegimeChurn, RegimeChurnAnalyzer, TemporalRegimeSeries, TemporalRegimeSnapshot

__all__ = [
    "TemporalSnapshot",
    "TemporalRegimeSnapshot",
    "TemporalRegimeSeries",
    "RegimeChurn",
    "RegimeChurnAnalyzer",
]
