#!/usr/bin/env python
"""
Extract the builds used in Github CI, so that we can run them locally
"""

from pathlib import Path

import yaml


def main() -> None:
    """Print the list of PlatformIO environments used for CI builds."""

    workflow = Path(__file__).resolve().parent / ".github" / "workflows" / "test-builds.yml"

    with workflow.open() as f:
        github_configuration = yaml.safe_load(f)

    jobs = github_configuration.get("jobs", {})
    test_builds = jobs.get("test_builds", {})
    strategy = test_builds.get("strategy", {})
    matrix = strategy.get("matrix", {})
    test_platforms = matrix.get("test-platform", [])

    print(" ".join(test_platforms))


if __name__ == "__main__":
    main()
