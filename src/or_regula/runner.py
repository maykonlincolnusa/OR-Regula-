"""Validated boundary used by the CLI and HTTP adapter."""
from .coverage import assess_coverage


def run(payload):
    if not isinstance(payload, dict) or set(payload) - set(["requirements","controls","evidence","as_of"]):
        raise ValueError("request must be an object containing only documented fields")
    return assess_coverage(payload.get('requirements'), payload.get('controls'), payload.get('evidence'), payload.get('as_of'))
