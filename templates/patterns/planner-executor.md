# Pattern — planner-executor (plan-then-execute)

## When to use
Multi-step work where the *sequence itself* deserves review before anything runs: anything
mixing external effects with local work, batch operations, changes where approving one plan
beats approving N individual actions. This is the batch alternative to per-action gating —
one reviewed plan instead of a fatigue-inducing stream of confirms.

## When not to use
- Exploratory work where the next step depends on what the last one revealed → plans go
  stale immediately; use orchestrator-workers or plain iteration.
- Single-step or all-pure work → the gate costs more than it protects.

## Mechanics that matter
- **The plan is a typed artifact**, not prose: every step names its tool, effect class,
  preconditions, and expected outcome. A human approves the *worst thing the plan can do*,
  which is why effect classes must be visible per step.
- **Approval covers the plan as written**: the executor may not add, reorder, or substitute
  steps. Anything off-plan is a deviation that returns to the planner (and a changed plan
  re-enters the gate if its effect profile grew).
- **Preconditions re-validate at execution time**, not planning time — the world moves
  between approval and execution; a stale precondition is a deviation, not a green light.

## Failure modes
- **Plan theater**: steps so vague ("improve the config") that approval is meaningless. The
  typed-step schema is the defense; a step without a concrete tool_ref and outcome fails
  composition.
- **Silent re-planning**: the executor "fixes" the plan on the fly. That converts a reviewed
  batch into unreviewed improvisation — the exact thing the pattern exists to prevent.

## Source attribution
Plan-and-execute agent practice; batch-approval economics from HITL fatigue observations
(hand-seeded 2026-07-07). Composes with `saga-compensation` (wave 3) for the external-effect
steps.
