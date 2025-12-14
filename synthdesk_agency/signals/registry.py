"""Known signal types (names only)."""

from __future__ import annotations

from typing import Final, Tuple

KNOWN_SIGNAL_TYPES: Final[Tuple[str, ...]] = (
    "breakout",
    "vol_spike",
    "mr_touch",
)

