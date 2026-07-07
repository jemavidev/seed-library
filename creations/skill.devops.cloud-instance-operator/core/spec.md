# skill.devops.cloud-instance-operator — spec

## What it does
Manages compute instances on a configured cloud provider: provision, start, stop, reboot,
terminate, and status. Provider-neutral interface — the concrete cloud (and its instance
types, regions, images) is a binding resolved through `provider_ref`.

## When to use / when not
- **Use** to provision or control the lifecycle of VMs/instances a project owns.
- **Don't use** for containers (`container-operator`/`k8s-operator`), managed services
  (databases, queues — future dedicated skills), or bulk fleet operations (compose this
  skill under `parallelization` with per-shard budgets instead).

## Inputs / outputs
- In: `provider_ref`, `action` (`provision|start|stop|reboot|terminate|status`),
  `instance_ref` (existing instance), `instance_spec` (provision only: `{ type, region,
  image_ref, tags }` — every provisioned instance must carry an owner/purpose tag).
- Out: `{ action, instance_ref, state, details }`.

## Worked example
`{ "provider_ref": "main-cloud", "action": "provision", "instance_ref": null,
"instance_spec": { "type": "small", "region": "us-east", "image_ref": "base-linux",
"tags": { "owner": "project-x", "purpose": "staging" } } }` →
`{ "action": "provision", "instance_ref": "i-0abc12", "state": "running", "details": "…" }`.

## Failure modes
- `auth_failed` (not retryable) · `instance_not_found` (not retryable)
- `quota_exceeded` — account limits (not retryable; a request to raise quota is a human
  decision) · `spec_invalid` (not retryable, message names the invalid field)
- `provider_unreachable` (retryable with backoff).

## Reversibility
`provision` ↔ `terminate`; `start` ↔ `stop`; `reboot` is self-inverse in effect. **Terminate
destroys instance-local data and has no undo** — it is the action policies should hold at
`expert-review`, and it must never run against an instance whose tags this skill did not
create unless explicitly briefed. `status` is effect-free.
