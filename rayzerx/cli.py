"""Command line entrypoint for the first RayzerX bootstrap flow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .contracts import load_task_brief
from .orchestrator import run_first_flow


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the RayzerX local bootstrap flow.")
    parser.add_argument("task", type=Path, help="Path to a RayzerX task brief JSON file.")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("tmp/rayzerx/runs"),
        help="Directory where run reports will be written.",
    )
    args = parser.parse_args()

    task = load_task_brief(args.task)
    report = run_first_flow(task, args.out)
    print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
