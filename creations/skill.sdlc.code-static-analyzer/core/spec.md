# skill.sdlc.code-static-analyzer — spec

## What it does
Runs a static analyzer (linter, type checker, or rule scanner) over a path and returns
normalized findings — one typed entry per issue — regardless of which underlying analyzer ran.
Read-only.

## When to use / when not
- **Use** as the cheap first evaluator in a review/reflection loop (before tests), and to
  audit unfamiliar code.
- **Don't use** to auto-fix (fixing belongs to the editor skill, driven by these findings) or
  as a substitute for tests — static analysis proves absence of *patterns*, not presence of
  *behavior*.

## Inputs / outputs
- In: `target_path`, `analyzer` (`auto` picks from project config), optional
  `severity_threshold` (drop findings below it).
- Out: `{ findings: [{ rule, severity, file, line, message }], summary: { error, warning, info } }`.

## Worked example
`{ "target_path": "src/", "analyzer": "auto", "severity_threshold": "warning" }` →
`{ "findings": [{ "rule": "F401", "severity": "warning", "file": "src/app.py", "line": 3,
"message": "'os' imported but unused" }], "summary": { "error": 0, "warning": 1, "info": 0 } }`.

## Failure modes
- `analyzer_not_found` — requested/detected analyzer unavailable (not retryable).
- `parse_error` — target code unparseable; the finding itself explains where (not retryable).

Findings (even hundreds) are a successful result. Zero findings with `summary` all-zero is
also a successful result — never a reason to re-run.

## Constraints
Normalization is the contract: callers must never need to know which analyzer produced a
finding. Analyzer-specific rule ids stay in `rule` verbatim for traceability.
