"""Public API for OR Regula."""

from .coverage import assess_coverage
from .schedule import review_schedule

__version__ = "0.3.0"


def project_info() -> dict[str, str]:
    return {
        "name": "OR Regula",
        "focus": "Regulatory requirements mapped to controls and evidence",
        "status": "reference-prototype",
    }


__all__ = ["assess_coverage", "project_info", "review_schedule"]

