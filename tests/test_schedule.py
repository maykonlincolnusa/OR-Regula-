from or_regula import review_schedule


def test_separates_overdue_and_due_soon_controls():
    controls = [{"id": "old", "owner": "compliance", "review_due": "2026-01-01"},
                {"id": "soon", "owner": "risk", "review_due": "2026-07-01"},
                {"id": "later", "owner": "risk", "review_due": "2027-12-01"}]
    result = review_schedule(controls, "2026-06-01", horizon_days=60)
    assert [item["control_id"] for item in result["overdue"]] == ["old"]
    assert [item["control_id"] for item in result["due_soon"]] == ["soon"]
