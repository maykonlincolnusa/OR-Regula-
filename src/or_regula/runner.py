"""Validated boundary used by the CLI and HTTP adapter."""
from .coverage import assess_coverage
from .schedule import review_schedule


def run(payload):
    if not isinstance(payload, dict) or set(payload) - set(["requirements","controls","evidence","as_of","action","horizon_days"]):
        raise ValueError("request must be an object containing only documented fields")
    if payload.get("action") == "schedule":
        return review_schedule(payload.get("controls"), payload.get("as_of"),
                               payload.get("horizon_days", 90))
    if payload.get("action", "coverage") != "coverage" or "horizon_days" in payload:
        raise ValueError("unknown action or unexpected schedule option")
    return assess_coverage(payload.get('requirements'), payload.get('controls'), payload.get('evidence'), payload.get('as_of'))
