import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from rayzerx.contracts import TaskBrief
from rayzerx.orchestrator import run_first_flow


class RayzerXFlowTest(unittest.TestCase):
    def test_first_flow_runs_without_provider_calls(self) -> None:
        task = TaskBrief(
            title="Bootstrap",
            description="Run the first RayzerX flow.",
            requested_by="test",
            acceptance_criteria=["No paid model calls", "Structured report"],
        )

        with TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            report = run_first_flow(task, output_dir)

            self.assertEqual(report.status, "passed")
            self.assertEqual(
                [result.agent_role for result in report.results],
                ["planner", "researcher", "tester", "reviewer", "documenter"],
            )
            self.assertTrue(
                all(
                    record.provider == "local"
                    for result in report.results
                    for record in result.usage
                )
            )
            self.assertTrue((output_dir / "latest-handoff.md").exists())


if __name__ == "__main__":
    unittest.main()
