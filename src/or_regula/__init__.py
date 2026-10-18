"""Starter package for OR Regula."""

from .coverage import assess_coverage

__version__ = "0.1.0"


def project_info() -> dict[str, str]:
    return {
        "name": "OR Regula",
        "focus": "Regulatory requirements mapped to controls and evidence",
        "status": "starter",
    }


__all__ = ["assess_coverage", "project_info"]

