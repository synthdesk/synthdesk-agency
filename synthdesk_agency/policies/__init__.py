"""Policy interfaces and empty templates for advisory-only evaluation."""

from .base import Policy
from .stack import PolicyStack

__all__ = ["Policy", "PolicyStack"]
