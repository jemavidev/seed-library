#!/usr/bin/env python3
"""Rebuild the library's derived artifacts and validate — one reproducible command.

Runs, in order:
  1. generate-bindings.py  — refresh every _meta.json + skill SKILL.md from core/
  2. build-catalog.py      — regenerate CATALOG.md from asset metadata
  3. validate.py           — core-neutrality, JSON/JSONL validity, skill contracts

Exits non-zero if validation fails. Run this after adding or renaming any asset, and in CI.
Durability: stdlib-only, no third-party deps, path-relative — a fresh clone rebuilds with just
`python3 scripts/build.py`. This is what keeps the library self-maintaining if SeeD vanishes.
"""
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
STEPS = ["generate-bindings.py", "build-catalog.py", "validate.py"]


def main():
    for step in STEPS:
        print(f"\n=== {step} ===")
        result = subprocess.run([sys.executable, str(SCRIPTS / step)])
        if result.returncode != 0:
            print(f"\nbuild: FAILED at {step}")
            sys.exit(result.returncode)
    print("\nbuild: OK — derived artifacts regenerated and validated")


if __name__ == "__main__":
    main()
