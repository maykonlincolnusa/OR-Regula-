"""Map regulatory requirements to implemented controls and evidence."""

from __future__ import annotations


def assess_coverage(
    requirements: list[dict[str, object]], controls: list[dict[str, object]]
) -> dict[str, list[dict[str, object]]]:
    linked: dict[str, list[dict[str, object]]] = {}
    for control in controls:
        for requirement_id in control.get("requirement_ids", []):
            linked.setdefault(str(requirement_id), []).append(control)

    covered = []
    gaps = []
    for requirement in requirements:
        requirement_id = str(requirement["id"])
        valid_controls = [control for control in linked.get(requirement_id, []) if control.get("evidence_ids")]
        if valid_controls:
            covered.append({"requirement_id": requirement_id, "control_ids": [str(c["id"]) for c in valid_controls]})
        else:
            gaps.append({"requirement_id": requirement_id, "reason": "NO_CONTROL_WITH_EVIDENCE"})
    return {"covered": covered, "gaps": gaps}

