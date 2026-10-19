"""Deterministic control-review schedule built from a governed catalog."""
from datetime import timedelta

from .coverage import calendar_date
from .validation import integer, text, unique_rows


def review_schedule(controls, as_of, horizon_days=90):
    today = calendar_date(as_of, "as_of")
    integer(horizon_days, "horizon_days", 1, 3660)
    due, overdue = [], []
    for control in unique_rows(controls):
        owner = text(control.get("owner"), "control owner")
        review = calendar_date(control.get("review_due"), "review_due")
        item = {"control_id": control["id"], "owner": owner,
                "review_due": review.isoformat(), "days_until_due": (review - today).days}
        if review < today:
            overdue.append(item)
        elif review <= today + timedelta(days=horizon_days):
            due.append(item)
    def order(item):
        return item["review_due"], item["control_id"]

    return {"as_of": today.isoformat(), "horizon_days": horizon_days,
            "overdue": sorted(overdue, key=order), "due_soon": sorted(due, key=order)}
