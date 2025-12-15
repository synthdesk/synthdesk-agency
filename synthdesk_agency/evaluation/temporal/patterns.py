"""Named temporal disagreement patterns (vocabulary only)."""

import os
import sys

from ... import ADVISORY_MODE

if ADVISORY_MODE and "PYTEST_CURRENT_TEST" not in os.environ and "pytest" not in sys.modules:
    raise RuntimeError("agency modules are advisory-only and must not be executed")

from typing import Final, Tuple


TEMPORAL_PATTERNS: Final[Tuple[str, ...]] = (
    "confidence_oscillation",
    "regime_flip_flop",
    "agreement_decay",
    "agreement_lock_in",
    "model_divergence_acceleration",
)
