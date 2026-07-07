# skill.devops.k8s-operator — spec

## What it does
Operates workloads on a configured orchestration cluster: apply manifests, watch rollout
status, scale, roll back to a previous revision, delete resources. Every mutating action is
anchored to the revision history the orchestrator already keeps — which is what makes
rollback a first-class compensation.

## When to use / when not
- **Use** for deploying and operating orchestrated workloads whose manifests live in the
  project.
- **Don't use** for cluster administration (nodes, RBAC, namespaces — deliberately out of
  scope) or for building images (`container-operator` feeds this skill).

## Inputs / outputs
- In: `cluster_ref`, `action` (`apply|status|scale|rollback|delete`), `manifest_path`
  (apply), `resource_ref` (kind/name for the rest), `replicas` (scale), `revision`
  (rollback target; null = previous).
- Out: `{ action, resource_ref, revision, state }` — `state` for apply/status reflects
  rollout readiness, not just acceptance.

## Worked example
`{ "cluster_ref": "staging", "action": "apply", "manifest_path": "deploy/api.yaml",
"resource_ref": null, "replicas": null, "revision": null }` →
`{ "action": "apply", "resource_ref": "deployment/api", "revision": "12",
"state": "rolled-out" }`.

## Failure modes
- `cluster_unreachable` (retryable) · `manifest_invalid` (not retryable, diagnostics attached)
- `resource_not_found` (not retryable) · `rollout_failed` — applied but never became ready;
  the failing pods' conditions are the evidence (not retryable as-is; usually followed by
  `rollback`).

## Reversibility
`apply` ↔ `rollback(revision)`; `scale` ↔ scale back to the recorded prior count; `delete` ↔
re-`apply` of the manifest **as long as the manifest is versioned in the project** — deleting
a resource whose manifest is not in version control is refused (`manifest_unversioned`).
`status` is effect-free. An apply is not done until the rollout is ready or has failed —
"accepted by the API" is not a result.
