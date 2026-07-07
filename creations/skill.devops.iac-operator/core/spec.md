# skill.devops.iac-operator — spec

## What it does
Drives infrastructure-as-code: `plan` computes the change set and saves it as an immutable
artifact; `apply` executes **only a previously saved plan** (never "whatever the config says
now"); `destroy` tears down managed resources. The IaC engine is a binding.

## When to use / when not
- **Use** for declarative infrastructure changes: provision/modify/retire resources whose
  desired state lives in versioned config.
- **Don't use** for one-off instance operations (`cloud-instance-operator`) or config edits
  on running services (`service-config-manager`). If it isn't in the IaC config, this skill
  doesn't touch it.

## Inputs / outputs
- In: `working_dir` (the IaC config root), `action` (`plan|apply|destroy`), `var_refs`
  (variable values by env reference), `target` (optional resource scope), `plan_ref`
  (**required for apply** — the saved plan to execute).
- Out: `{ action, plan_ref, changes: { add, change, destroy }, output }`.

## Worked example
`{ "working_dir": "infra/", "action": "plan", "var_refs": { "region": "IAC_REGION" },
"target": null, "plan_ref": null }` →
`{ "action": "plan", "plan_ref": "plan-8842", "changes": { "add": 3, "change": 1,
"destroy": 0 }, "output": "…" }` — then `apply` with `plan_ref: "plan-8842"`.

## Failure modes
- `apply_without_plan` — apply lacking a `plan_ref` (not retryable; the two-phase contract)
- `plan_stale` — the world drifted since the plan was saved; re-plan (not retryable as-is)
- `config_invalid` (not retryable) · `state_locked` (retryable with backoff)
- `provider_auth_failed` (not retryable) · `partial_apply` — some resources changed before
  failure; the output names them (not retryable automatically).

## Reversibility
The saved plan is the approval artifact (same discipline as `db-migration-runner`): a human
gates exactly what will run, including the `destroy` count. Compensation for `apply` is
applying the recorded prior state; `destroy` of stateful resources loses their data — plans
whose `destroy > 0` deserve `expert-review`.
