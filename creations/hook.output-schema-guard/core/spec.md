# hook.output-schema-guard — spec

## What it is
A post-output hook: whenever an agent step declares an expected output schema, this hook
validates the actual output against it before the result is accepted downstream. On failure it
returns the typed validation errors to the producing agent for one bounded retry round.

## Trigger semantics (harness-neutral)
- **Trigger:** `post-output` — fires after an agent/step produces a result that a consumer
  will parse (structured handoffs, pattern state writes, tool-bound arguments).
- **Input:** the produced output + the JSON Schema the consumer declared.
- **Effect:** pass-through on valid; on invalid, emit
  `{ valid: false, errors: [{ path, message }] }` back to the producer with the retry budget.

## Behavior rules
1. Validation is strict: unknown properties are errors (see lesson `strict-schemas-always`).
2. Retry is bounded (default 2) and always carries the error list — a retry without the errors
   is a coin flip, not a correction.
3. After the retry budget, the failure propagates as a typed step failure; the hook never
   "fixes" output itself and never lets invalid output through quietly.
4. The hook logs schema-failure counts per producer — chronic failers are a signal the
   producer's instructions and the consumer's schema have drifted apart.

## When to attach
Between pattern stages (`prompt-chaining` gates), on `evaluator-optimizer` feedback payloads,
and on any structured deliverable a workflow consumes mechanically.
