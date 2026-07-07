---
name: run-test-suite
description: Run tests (auto-detected framework) and get structured pass/fail results with per-failure messages and locations.
---

Use this skill to verify changes and to drive fix loops.

- Run the narrowest suite that covers the change first (use `filter`), then the full suite
  before declaring done.
- A result with `failed > 0` is information, not an error: read each `failures[]` entry and fix
  the cause — never rerun unchanged hoping for green.
- On `setup_error`, the suite never ran: fix the environment/import problem before touching
  test logic.
- Report results honestly, including skips.
