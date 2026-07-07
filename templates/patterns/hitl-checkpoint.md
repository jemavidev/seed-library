# Pattern — hitl-checkpoint (human-in-the-loop interrupt)

## When to use
Before consequential, hard-to-reverse actions: production data migrations, publishing,
external side effects without cheap compensation, anything policy marks `confirm` or
`expert-review`. The work *up to* the action runs autonomously; the action itself waits.

## When not to use
- The action is cheaply reversible and policy allows it → notify-after is cheaper than
  interrupt-before.
- Approval would be rubber-stamped ("approve 200 file writes?") → gate the *batch intent*
  once, not each item; per-item gates train humans to click yes.

## Mechanics that matter
- **The verdict is a stance decision, not a boolean.** The gate presents `pending_action`
  (exact, human-readable, with its undo story) and yields to the runtime's approval mechanism
  — whatever stance the active policy assigns (`confirm`, `expert-review`). Three outcomes:
  approved, rejected, amended (human edits the intent; worker revises).
- **State freezes losslessly** at the gate: resume must not need re-derivation. Anything not
  in `work_product`/`pending_action` is lost by contract.
- **Timeout is explicit** and always fails safe (`abort`), never auto-approves.
- The gate node has no role_ref: it is runtime machinery, not an agent.

## Failure modes
- **Vague pending_action**: "apply changes?" is unanswerable. The gate item must name objects,
  counts, and the compensation plan.
- **Drift during the wait**: hours later the world moved. The executor re-validates
  preconditions after approval; stale preconditions send it back to the worker, not blindly on.

## Source attribution
Interrupt/checkpoint semantics from durable-workflow and state-graph practice; stance mapping
is runtime policy, kept out of core by design (hand-seeded 2026-07-07).
