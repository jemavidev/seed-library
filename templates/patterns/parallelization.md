# Pattern — parallelization (map-reduce)

## When to use
Divisible work where shards don't depend on each other: audit N files, evaluate M candidates,
summarize K documents, scan a fleet. Also the *voting* variant: same input to several workers,
reducer aggregates for confidence.

## When not to use
- Shards share evolving state → they're not shards; use a pipeline.
- Fewer than ~3 shards → concurrency overhead eats the win.
- The reduce step needs deep judgment over huge combined output → reduce hierarchically
  (reduce shards of results) instead of one mega-reduce.

## Mechanics that matter
- **The join must not hang**: every shard resolves to a result *or a typed failure* within its
  budget; the reducer consolidates both kinds and reports coverage ("38/40 shards clean, 2
  failed: …").
- **Per-shard budget** is total budget divided across shards, capped by
  `max_concurrent_shards` — fan-out without per-shard caps is the fastest way to burn a
  whole budget on one runaway shard.
- Workers are identical instances of one profile; if shards need *different* specialists,
  that's routing composed inside orchestrator-workers, not map-reduce.

## Failure modes
- **Straggler shard**: one shard 10× slower blocks the reduce. Time-box shards; a timeout is a
  typed failure entry.
- **Reducer bias**: reducer trusts the first/most verbose shard. Give the reducer a fixed
  consolidation rubric (coverage, then severity, then dedupe).

## Source attribution
Canonical parallelization (sectioning + voting) workflow; join semantics from concurrent
workflow-engine practice (hand-seeded 2026-07-07).
