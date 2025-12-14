"""Registry of known regime hypothesis names (vocabulary only).

Notes:
- not exhaustive
- inclusion does not imply detection, priority, or truth
"""

from typing import Final, Tuple

KNOWN_REGIMES: Final[Tuple[str, ...]] = (
    "trend_expansion",
    "range_compression",
    "volatility_expansion",
    "volatility_compression",
    "liquidity_vacuum",
    "mean_reversion_dominant",
)
