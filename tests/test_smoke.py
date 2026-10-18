import unittest

from or_regula import assess_coverage, project_info


class ProjectSmokeTest(unittest.TestCase):
    def test_project_metadata(self) -> None:
        self.assertEqual(project_info()["status"], "starter")

    def test_reports_requirement_gap(self) -> None:
        requirements = [{"id": "R1"}, {"id": "R2"}]
        controls = [{"id": "C1", "requirement_ids": ["R1"], "evidence_ids": ["E1"]}]
        result = assess_coverage(requirements, controls)
        self.assertEqual(result["gaps"], [{"requirement_id": "R2", "reason": "NO_CONTROL_WITH_EVIDENCE"}])



if __name__ == "__main__":
    unittest.main()

