"""Disagreement records (expressive, non-resolving)."""

from __future__ import annotations

import os
import sys

from .. import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from dataclasses import dataclass
from typing import Mapping, Optional

from .scores import Score


@dataclass(frozen=True)
class Disagreement:
    """Represents divergence between multiple advisory scores.

    Notes:
    - magnitude is descriptive, not decisive
    - disagreement is information, not error
    """

    scores: Mapping[str, Score]
    magnitude: Optional[float] = None
    notes: Optional[str] = None
