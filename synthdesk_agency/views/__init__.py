"""Human-facing rendering surfaces (advisory-only; inert)."""

from .text_report import render_text_report

try:
    __all__
except NameError:
    __all__ = []

__all__ += ["render_text_report"]

