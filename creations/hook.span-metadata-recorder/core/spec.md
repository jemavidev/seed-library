# hook.span-metadata-recorder — spec

## What it is
A post-tool hook that **enriches** the runtime's existing per-invocation access event with
observability metadata — latency, token usage, retry count, result size — so cost and
performance questions are answerable from the one canonical record. It never creates a
parallel log.

## Trigger semantics (harness-neutral)
- **Trigger:** `post-tool` — after every tool invocation completes (success or typed failure).
- **Input:** the invocation's identifiers plus its timing/usage measurements.
- **Effect:** appends a `span` object onto the invocation's existing access event:
  `{ latency_ms, tokens_in, tokens_out, retries, result_bytes, failure_code }`.

## Behavior rules
1. **Enrich, never duplicate:** the access event is the single record; this hook adds fields
   to it. If no access event exists for the invocation, that is a runtime bug to surface —
   not a reason for this hook to write its own file.
2. **Measure, don't sample** at this layer: every invocation gets a span; aggregation and
   sampling are downstream consumers' choices.
3. **Fail open:** a recording failure logs a warning and never blocks or delays the tool
   result — observability must not become a point of failure.
4. **No payload capture:** sizes and counts only; bodies/arguments stay out of the span (the
   event already references them under its own access rules).

## When to attach
Globally — this hook is the feed for spend threshold alerts, latency regressions, and
retry-storm detection.
