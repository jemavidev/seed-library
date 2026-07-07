# Pattern — prompt-chaining (sequential pipeline)

## When to use
When a task decomposes into *fixed, known-in-advance* stages where each stage is simpler than
the whole: draft → review-gate → refine → package; extract → transform → load; outline →
write → format.

## When not to use
- Stages aren't known up front → orchestrator-workers (dynamic decomposition).
- Stages are independent of each other → parallelization is cheaper and faster.
- Only one transformation → a single call; a chain of one is overhead.

## Mechanics that matter
- **Typed stage contracts**: each stage declares an output schema; the next stage consumes
  exactly that. A stage that needs data two stages back reads it from `stage_outputs`, not by
  re-asking.
- **Gates stop, they don't fix**: a gate node validates and either passes control or ends the
  chain with typed failures. Fixing belongs to an evaluator-optimizer loop embedded at that
  stage if needed.
- Stage count is instantiation-specific; the invariant is linearity + typed handoffs + gates
  after the stages most likely to go wrong.

## Failure modes
- **Error amplification**: a subtly wrong stage-1 output degrades every later stage — this is
  why the gate sits early, not at the end.
- **Context smuggling**: stages passing prose blobs instead of schema-shaped data reintroduce
  ambiguity the pattern exists to remove.

## Source attribution
Canonical prompt-chaining workflow; typed handoffs from state-graph practice
(hand-seeded 2026-07-07).
