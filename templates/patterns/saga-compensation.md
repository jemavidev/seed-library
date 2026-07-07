# Pattern — saga-compensation (compensated effect chain)

## When to use
Any flow with two or more external effects that must be all-or-nothing *in effect* even
though no transaction spans them: register webhook + announce + update document; create
issue + open PR + notify. The per-tool `compensate` declarations exist so this pattern can
compose them.

## When not to use
- One external effect → the tool's own compensation and the approval flow suffice.
- Effects on a single system that offers real transactions → use the transaction.
- Steps whose compensation is honestly weak (email) → a saga can't fix that; gate the send
  instead, or sequence it last so an unwind never needs to "unsend".

## Mechanics that matter
- **Compensation before effect**: step k+1 does not start until step k's compensation is
  registered in the log. A crash at any moment leaves a sweepable trail — this is the
  crash-safety property, and it is the whole pattern.
- **Load-time validation**: a saga containing a step without a declared compensation is
  rejected before anything runs (mirrors the ToolSpec rule: external effects carry
  `compensate` or don't run).
- **Unwind is newest-first** and compensations must be idempotent — an unwind interrupted
  and resumed must not double-revert.
- **Order steps by regret**: put the hardest-to-compensate effect *last* (email after
  webhook, not before), so most failures unwind cheaply.
- `partially_unwound` is a first-class outcome: a failed compensation stops the unwind and
  escalates with the log — silent best-effort cleanup is how orphans are born.

## Failure modes
- **Compensation drift**: the recorded compensation no longer matches reality (the resource
  changed since). Compensations re-validate their target before running; a mismatch
  escalates rather than deletes the wrong thing.
- **Saga sprawl**: ten-step sagas are unreviewable. Compose: a saga step may itself be a
  smaller gated flow.

## Source attribution
Saga pattern from distributed-transaction practice (compensating transactions,
durable-workflow engines); regret-ordering heuristic from operational experience
(hand-seeded 2026-07-07).
