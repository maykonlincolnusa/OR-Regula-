"""Evidence freshness and approval checks against a user-supplied control catalog."""
from __future__ import annotations

from datetime import date

from .validation import identifiers, text, unique_rows


def calendar_date(value, field):
    try:
        return date.fromisoformat(value)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"{field} must be an ISO calendar date") from exc


def assess_coverage(requirements, controls, evidence=None, as_of=None):
    today = calendar_date(as_of, "as_of")
    requirements = unique_rows(requirements)
    controls = unique_rows(controls)
    evidence = unique_rows(evidence if evidence is not None else [])
    requirement_map = {r["id"]: r for r in requirements}
    evidence_map = {e["id"]: e for e in evidence}
    for requirement in requirements:
        text(requirement.get("version"), "requirement version")
        text(requirement.get("jurisdiction"), "jurisdiction")
        source = text(requirement.get("source_url"), "source_url")
        if not source.startswith("https://"):
            raise ValueError("source_url must use HTTPS")
    for item in evidence:
        text(item.get("status"), "evidence status")
        valid_from = calendar_date(item.get("valid_from"), "valid_from")
        expires = calendar_date(item.get("expires_on"), "expires_on")
        if valid_from > expires:
            raise ValueError("evidence validity period is reversed")
    linked = {}
    for control in controls:
        refs = identifiers(control.get("requirement_ids"), "requirement_ids")
        ids = identifiers(control.get("evidence_ids"), "evidence_ids")
        if not set(refs).issubset(requirement_map):
            raise ValueError("control references an unknown requirement")
        if not set(ids).issubset(evidence_map):
            raise ValueError("control references unknown evidence")
        text(control.get("owner"), "control owner")
        text(control.get("status"), "control status")
        calendar_date(control.get("review_due"), "review_due")
        versions = control.get("requirement_versions")
        if not isinstance(versions, dict):
            raise ValueError("requirement_versions must be an object")
        for ref in refs:
            linked.setdefault(ref, []).append(control)
    covered, gaps = [], []
    for requirement in sorted(requirements, key=lambda r: r["id"]):
        valid = []
        for control in linked.get(requirement["id"], []):
            if control["status"] != "APPROVED" or calendar_date(control["review_due"], "review_due") < today:
                continue
            if control["requirement_versions"].get(requirement["id"]) != requirement["version"]:
                continue
            refs = control["evidence_ids"]
            if refs and all(evidence_map[key]["status"] == "APPROVED"
                            and calendar_date(evidence_map[key]["valid_from"], "valid_from") <= today
                            <= calendar_date(evidence_map[key]["expires_on"], "expires_on") for key in refs):
                valid.append(control["id"])
        if valid:
            covered.append({"requirement_id": requirement["id"], "control_ids": sorted(valid)})
        else:
            gaps.append({"requirement_id": requirement["id"],
                         "reason": "NO_APPROVED_CURRENT_CONTROL_WITH_VALID_EVIDENCE"})
    return {"covered": covered, "gaps": gaps, "as_of": today.isoformat(),
            "assessment": "CATALOG_COVERAGE_ONLY", "rule_version": "2.0"}

