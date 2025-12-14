"""Policy stack container (advisory-only; inert)."""

from dataclasses import dataclass
from typing import Sequence

from .base import Policy


@dataclass(frozen=True)
class PolicyStack:
    """Ordered collection of advisory policies."""

    policies: Sequence[Policy]
