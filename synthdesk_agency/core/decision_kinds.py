"""Decision kind taxonomy (advisory-only)."""

from typing import Final, Tuple

DECISION_KINDS: Final[Tuple[str, ...]] = (
    "no_op",
    "bias_up",
    "bias_down",
    "stand_down",
    "conflict_detected",
    "insufficient_signal",
    "regime_uncertain",
)

