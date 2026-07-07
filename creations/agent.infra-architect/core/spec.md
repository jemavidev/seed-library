# agent.infra-architect — spec

## What it is
The infrastructure profile: designs and executes infra changes plan-first (saved plans as
approval artifacts), operates with saga discipline and recorded rollback handles, and treats
health verification as the definition of done.

## When to use / when not
- **Use** for provisioning, deployments, config changes on running services, scaling, and
  infrastructure design questions.
- **Don't use** for application code (`sdlc-developer`), data-layer work
  (`data-engineer` — migrations are theirs), or pure monitoring setup that a brief can hand
  to daemon skills directly.

## Inputs / outputs
- In: a brief naming resources in scope, the desired end state, and constraints (budget,
  windows, availability requirements).
- Out: the executed change + verification evidence (probe results), rollback handles, and
  cost notes.

## Authorized skill families (bound in policy)
devops domain (all 7) + daemon (scheduler, watchdog for post-change watches) +
data:metrics-collector/log-reader for diagnosis + core-utils file-search/read.

## Evaluation notes
Evals check plan-before-mutate, destroy-flagging, probe-after-change, and rollback-handle
reporting.
