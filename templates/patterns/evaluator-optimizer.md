# Pattern — evaluator-optimizer (reflection / self-correction)

## When to use
When output quality is checkable by an evaluator that is *more objective than the generator*:
tests, linters, schema validation, rubric scoring. Ideal for code refactors, config
generation, structured writing against a rubric.

## When not to use
- No objective check exists → the loop converges on the evaluator's taste, burning budget for
  cosmetic churn.
- The check is cheap enough to inline → give the generator the tool directly; a second agent
  adds a hop without adding objectivity.

## Mechanics that matter
- The evaluator returns **typed findings** (what failed, where, why), not prose opinions —
  the generator fixes findings, it doesn't argue with essays.
- `attempts` lives in state, incremented by the generator node; both exit edges are explicit.
- Exhaustion is a first-class outcome: deliver the best draft *plus* the outstanding findings.
  A caller must be able to distinguish "passed" from "ran out of attempts".
- Evaluator skills should be read-only (analysis, tests); the generator owns all writes.

## Failure modes
- **Oscillation**: fix A breaks B, fix B breaks A. Findings history in `feedback` lets the
  generator detect the cycle and stop early.
- **Evaluator drift**: the evaluator invents new demands each round. Pin the evaluation
  criteria in the task_brief; the evaluator checks against them, not against inspiration.

## Source attribution
Canonical evaluator-optimizer workflow; typed-feedback discipline from structured-output
validation practice (hand-seeded 2026-07-07). See lesson `cyclic-patterns-declare-termination`.
