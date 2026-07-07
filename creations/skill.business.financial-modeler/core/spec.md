# skill.business.financial-modeler — spec

## What it does
Runs standard financial computations: net present value, internal rate of return, loan
amortization, break-even analysis, and simple multi-period projections. Pure arithmetic with
explicit assumptions — it computes; it does not advise.

## When to use / when not
- **Use** to put numbers under a business-idea charter: "at what volume does this break
  even?", "what does this loan actually cost?", "is cash flow A worth more than B at rate r?"
- **Don't use** for accounting/tax filings (jurisdiction-specific, out of scope), portfolio
  or investment advice (never in scope), or statistics over data (`statistical-analyzer`).

## Inputs / outputs
- In: `analysis` (`npv|irr|amortization|break-even|projection`), `inputs` (per-analysis
  documented object — e.g. npv: `{ rate, cash_flows[] }`; break-even: `{ fixed_costs,
  unit_price, unit_variable_cost }`), `currency` (label only; no conversion).
- Out: `{ analysis, results, assumptions, warnings }` — `assumptions` restates what the math
  took as given (rate constant, flows end-of-period); `warnings` flags fragility (IRR with
  multiple sign changes, break-even beyond plausible volume).

## Worked example
`{ "analysis": "break-even", "inputs": { "fixed_costs": 1200, "unit_price": 15,
"unit_variable_cost": 7 }, "currency": "USD" }` →
`{ "analysis": "break-even", "results": { "units": 150, "revenue": 2250 },
"assumptions": ["price and variable cost constant across volume"], "warnings": [] }`.

## Failure modes
- `missing_input` — the analysis's required fields absent (not retryable; message lists them)
- `invalid_inputs` — e.g. negative price, empty cash flows (not retryable)
- `no_solution` — e.g. IRR undefined for the flows given (not retryable; that *is* the answer).

## Constraints
Results always travel with their `assumptions` — a number stripped of what it assumed is how
spreadsheet fictions get made. Ranges beat false precision: projections output low/base/high
when the inputs carry ranges. No investment advice, ever: the skill computes consequences of
stated inputs, full stop.
