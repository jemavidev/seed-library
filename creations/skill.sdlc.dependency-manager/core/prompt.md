---
name: dependency-manager
description: Add/remove/update/install/audit project dependencies via the project's own package manager; changes stay in manifest+lockfile.
---

Use this skill instead of editing manifests by hand.

- Before `add`, check the dependency isn't already present (an `install` + import may suffice).
- Pin deliberately: pass `version` when the project pins, leave null to follow project policy.
- After any mutation, run the test suite — a dependency change is a code change.
- On `resolution_conflict`, present the conflicting constraints; do not loosen pins on your own.
- `audit` findings are ranked input for a human or a security profile, not an automatic
  license to mass-upgrade.
