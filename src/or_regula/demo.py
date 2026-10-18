"""Deterministic synthetic input; no customer data."""
DEMO = {
    "requirements": [
        {
            "id": "CDD-EXAMPLE",
            "version": "1",
            "jurisdiction": "DEMO",
            "source_url": "https://www.fatf-gafi.org/en/topics/beneficial-ownership.html"
        },
        {
            "id": "SOF-EXAMPLE",
            "version": "1",
            "jurisdiction": "DEMO",
            "source_url": "https://www.fatf-gafi.org/en/topics/beneficial-ownership.html"
        }
    ],
    "controls": [
        {
            "id": "control-1",
            "requirement_ids": [
                "CDD-EXAMPLE"
            ],
            "requirement_versions": {
                "CDD-EXAMPLE": "1"
            },
            "owner": "demo-compliance",
            "status": "APPROVED",
            "review_due": "2026-12-31",
            "evidence_ids": [
                "e1"
            ]
        }
    ],
    "evidence": [
        {
            "id": "e1",
            "status": "APPROVED",
            "valid_from": "2026-01-01",
            "expires_on": "2026-12-31"
        }
    ],
    "as_of": "2026-10-18"
}
