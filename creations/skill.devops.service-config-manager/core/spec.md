# skill.devops.service-config-manager — spec

## What it does
Manages a running service's configuration (web server, reverse proxy, message broker — the
concrete service is a binding) in strict two-phase form: `validate` checks a candidate config
and returns diagnostics; `apply` installs **only a validated candidate** and reloads;
`rollback` restores a kept prior version. The service keeps its last N config versions.

## When to use / when not
- **Use** to change how a running service behaves: routes, limits, upstreams, TLS settings.
- **Don't use** for application config files inside a project (plain file edit under version
  control) or for declaratively-managed infrastructure (`iac-operator` owns that state).

## Inputs / outputs
- In: `service_ref`, `action` (`validate|apply|rollback`), `config_path` (the candidate,
  validate/apply), `version_ref` (rollback target; apply also *returns* one).
- Out: `{ action, valid, version_ref, diagnostics }`.

## Worked example
`{ "service_ref": "edge-proxy", "action": "validate", "config_path": "conf/edge.conf",
"version_ref": null }` → `{ "action": "validate", "valid": true, "version_ref": null,
"diagnostics": [] }` — then `apply` the same path, which returns `version_ref: "cfg-31"`.

## Failure modes
- `config_invalid` — validation diagnostics attached, nothing touched (not retryable as-is)
- `apply_unvalidated` — apply of a candidate that wasn't validated in this flow (not
  retryable; the two-phase contract)
- `reload_failed` — config installed but the service rejected the live reload; **auto-reverts
  to the prior version** and reports it (not retryable without change)
- `service_unreachable` (retryable) · `version_not_found` (not retryable).

## Reversibility
`apply` ↔ `rollback(version_ref)` against the kept history. The auto-revert on
`reload_failed` means a bad apply can degrade service for seconds, not minutes — which is
also why `apply` on production services still deserves a `confirm` stance.
