# skill.data.statistical-analyzer — spec

## What it does
Runs a named statistical analysis over tabular records: descriptive summaries, correlation,
two-sample hypothesis tests, or distribution fitting — returning typed results with sample
sizes and explicit caveats. Pure computation.

## When to use / when not
- **Use** to summarize a dataset honestly, test whether two groups differ, or check how two
  variables relate — before drawing any conclusion from data.
- **Don't use** for forecasting/modeling (out of scope by design) or on data you haven't
  looked at structurally (`db-query`/`data-transformer` first).

## Inputs / outputs
- In: exactly one of `data` (JSON records) / `input_path`; `analysis`
  (`descriptive|correlation|hypothesis-test|distribution`); `columns` (fields involved);
  `options` (per-analysis knobs: `group_by`, `test`, `confidence`).
- Out: `{ analysis, results, n, warnings }` — `results` shape depends on `analysis` and is
  documented per case in the eval fixtures; `warnings` carries method caveats (small n,
  skew, ties).

## Worked example
`{ "data": null, "input_path": "data/times.csv", "analysis": "hypothesis-test",
"columns": ["duration_ms"], "options": { "group_by": "variant", "test": "mann-whitney",
"confidence": 0.95 } }` → `{ "analysis": "hypothesis-test", "results": { "test":
"mann-whitney", "p_value": 0.031, "effect_size": 0.22, "groups": ["a", "b"] }, "n": 412,
"warnings": ["group sizes unbalanced (356 vs 56)"] }`.

## Failure modes
- `no_input` (not retryable) · `invalid_data` (not retryable)
- `unknown_column` (not retryable; message lists available columns)
- `insufficient_data` — n below the method's minimum (not retryable; the answer is "not
  enough data", which is a finding, not an error to engineer around).

## Constraints
Every result carries `n` and applicable `warnings` — a p-value without its caveats must not
leave this skill. The analysis never drops rows silently: exclusions (nulls, non-numeric)
are counted in `warnings`.
