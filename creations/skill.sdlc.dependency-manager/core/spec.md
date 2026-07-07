# skill.sdlc.dependency-manager — spec

## What it does
Manages project dependencies through the project's own package manager (detected from
lockfiles): install, add, remove, update, or audit. Mutations are confined to the project
(manifest, lockfile, vendored packages); the registry is only ever read.

## When to use / when not
- **Use** to add a library a change needs, sync an environment (`install`), or check for known
  vulnerabilities (`audit`).
- **Don't use** to publish packages (out of scope; that is an external effect needing its own
  spec) or to edit manifests by hand — going through the manager keeps lockfiles consistent.

## Inputs / outputs
- In: `project_path`, `action` (`install|add|remove|update|audit`), optional `package`,
  optional `version` (exact or range; only with `add`/`update`).
- Out: `{ action, changed: [{ package, from, to }], vulnerabilities }` — `vulnerabilities`
  is populated by `audit`, null otherwise.

## Worked example
`{ "project_path": ".", "action": "add", "package": "httpx", "version": "^0.27" }` →
`{ "action": "add", "changed": [{ "package": "httpx", "from": null, "to": "0.27.2" }],
"vulnerabilities": null }`.

## Failure modes
- `resolution_conflict` — version constraints unsatisfiable (not retryable; the conflict list
  is the negotiation input).
- `registry_unreachable` — network problem (retryable with backoff).
- `unsupported_manager` — no recognizable manifest/lockfile (not retryable).

## Constraints
Never modify version pins beyond what the action names (`add httpx` must not bump unrelated
packages — use `update` explicitly for that). `audit` is read-only. Lockfile changes are the
undo surface: restoring manifest+lockfile reverses any action.
