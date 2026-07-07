# Pattern — orchestrator-workers (dynamic decomposition)

## When to use
When the subtasks cannot be known before looking at the objective: "audit this system",
"prepare this launch", "research this market". The orchestrator reads the objective, invents
a subtask list, picks a profile per subtask, and integrates.

## When not to use
- Subtasks are known and fixed → prompt-chaining (cheaper, more predictable).
- Subtasks are uniform shards of one operation → parallelization.
- The request is a classification problem → routing.

## Mechanics that matter
- **Subtask briefs are contracts**: each carries its own goal, constraints, and expected
  output form — a worker never sees the whole objective unless its brief includes it.
- **Heterogeneous workers**: unlike map-reduce, each subtask can bind a different profile
  (`profile_ref`), which is the entire point of decomposing.
- **One re-plan, not many**: the integrator may send the orchestrator back exactly
  `max_iterations - 1` times with named gaps. Unlimited re-planning is scope creep with a
  budget attached.
- Failed subtasks integrate as typed gaps — the final output states what is missing and why.

## Failure modes
- **Decomposition sprawl**: 15 micro-subtasks where 4 would do. Cap via
  `max_concurrent_subtasks` and instruct the orchestrator to decompose to *independently
  answerable* units, not to-do granularity.
- **Integration by concatenation**: the integrator's job is synthesis (conflicts resolved,
  redundancy removed), not stapling worker outputs together.

## Source attribution
Canonical orchestrator-workers workflow; subtask-brief discipline from supervisor handoff
practice (hand-seeded 2026-07-07).
