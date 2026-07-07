# skill.core-utils.data-transformer — spec

## What it does
Converts structured data between formats — JSON, YAML, CSV, and markdown tables — from inline
text or a file, returning the converted text or writing it to a target path.

## When to use / when not
- **Use** for mechanical format conversion: config translation, CSV→markdown for a report,
  YAML→JSON for a strict consumer.
- **Don't use** to *reshape* data (rename fields, aggregate rows) — conversion preserves
  structure 1:1; reshaping is reasoning work done before calling this.

## Inputs / outputs
- In: exactly one of `input` / `input_path`; `from` (`json|yaml|csv|auto`); `to`
  (`json|yaml|csv|markdown-table`); optional `output_path` (null returns text inline).
- Out: `{ output, output_path, records }` — `output` null when written to a file; `records` is
  rows for tabular data, top-level keys otherwise.

## Worked example
`{ "input": "[{\"name\":\"a\",\"n\":1}]", "input_path": null, "from": "json",
"to": "markdown-table", "output_path": null }` →
`{ "output": "| name | n |\n|---|---|\n| a | 1 |", "output_path": null, "records": 1 }`.

## Failure modes
- `parse_error` — input does not parse as `from` (not retryable; message carries line/column).
- `unsupported_conversion` — pair not implemented, e.g. deeply nested JSON → CSV
  (not retryable; flatten first).
- `no_input` — zero or two inputs given (not retryable).

## Constraints
Round-trip safety where formats allow: JSON→YAML→JSON must be identity. Lossy conversions
(nested→tabular) must fail rather than guess a flattening.
