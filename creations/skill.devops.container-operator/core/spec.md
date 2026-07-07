# skill.devops.container-operator — spec

## What it does
Operates the container lifecycle against the configured container runtime: build an image
from a context, run/stop/remove containers, read container logs, push an image to a
configured registry. One action per call. The runtime and registry are bindings.

## When to use / when not
- **Use** to build and run project services locally, inspect their logs, and publish images
  a deployment will consume.
- **Don't use** for orchestrated workloads (`k8s-operator` owns those) or as a shell
  substitute — if the need is "run a command", that is not a container lifecycle operation.

## Inputs / outputs
- In: `action` (`build|run|stop|logs|remove|push`), `image` (name:tag), `container_ref`,
  `context_path` (build), `registry_ref` (push — configured registry name), `args`
  (action-specific: ports, env refs, build args).
- Out: `{ action, container_ref, image, output }`.

## Worked example
`{ "action": "build", "image": "api:1.4.2", "container_ref": null,
"context_path": "services/api", "registry_ref": null, "args": null }` →
`{ "action": "build", "container_ref": null, "image": "api:1.4.2", "output": "sha256:…" }`.

## Failure modes
- `build_failed` — with the build log tail as evidence (not retryable until inputs change)
- `image_not_found` / `container_not_found` (not retryable)
- `registry_auth_failed` (not retryable) · `runtime_unreachable` (retryable)
- `port_in_use` — run collision (not retryable; pick another port deliberately).

## Reversibility
`run` ↔ `stop`+`remove`; `build` is local (image removable); `push` is the publication —
compensated by deleting the pushed tag where the registry allows, and otherwise treated as
permanent (never overwrite a pushed tag to "fix" it; push a new tag). Secrets enter builds
and runs only as env references, never baked into images.
