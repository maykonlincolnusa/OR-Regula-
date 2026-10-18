import unittest

from or_regula import assess_coverage, project_info


class ProjectTest(unittest.TestCase):
    def setUp(self):
        self.requirement = {"id": "R1", "version": "2026-01", "jurisdiction": "TEST",
                            "source_url": "https://example.com/requirement"}
        self.evidence = {"id": "E1", "status": "APPROVED", "valid_from": "2026-01-01",
                         "expires_on": "2026-12-31"}
        self.control = {"id": "C1", "requirement_ids": ["R1"], "evidence_ids": ["E1"],
                        "requirement_versions": {"R1": "2026-01"}, "owner": "compliance",
                        "status": "APPROVED", "review_due": "2026-12-31"}

    def test_reports_valid_catalog_coverage(self):
        result = assess_coverage([self.requirement], [self.control], [self.evidence], "2026-06-01")
        self.assertEqual(result["covered"][0]["control_ids"], ["C1"])
        self.assertEqual(project_info()["status"], "reference-prototype")

    def test_expired_evidence_creates_gap(self):
        result = assess_coverage([self.requirement], [self.control], [self.evidence], "2027-01-01")
        self.assertEqual(result["gaps"][0]["requirement_id"], "R1")

    def test_rejects_unknown_requirement_reference(self):
        control = {**self.control, "requirement_ids": ["missing"]}
        with self.assertRaises(ValueError):
            assess_coverage([self.requirement], [control], [self.evidence], "2026-06-01")


if __name__ == "__main__":
    unittest.main()
