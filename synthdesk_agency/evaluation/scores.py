"""Advisory score records (expressive, non-vetoing)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Score:
    """Continuous advisory score for a signal or decision."""

    value: float
    confidence: Optional[float] = None
    label: Optional[str] = None
    notes: Optional[str] = None
