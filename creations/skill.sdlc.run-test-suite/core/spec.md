# skill.sdlc.run-test-suite — spec

## What it does
Runs the project's test suite (or a filtered subset) with a detected or explicit framework and
returns structured results: counts plus one typed entry per failure, so a calling agent can
self-correct without parsing raw logs.

## When to use / when not
- **Use** after any code change, and as the evaluator step in a reflection loop.
- **Don't use** for lint/static checks (`skill.sdlc.code-static-analyzer`) or to "explore" a
  codebase — tests are for verification, not discovery.

## Inputs / outputs
- In: `test_path`, `framework` (`auto` detects from project files), optional `filter`
  (test-name pattern), optional `timeout_seconds`.
- Out: `{ passed, failed, skipped, failures: [{ test, message, location }] }`.

## Worked example
`{ "test_path": "tests/", "framework": "auto", "filter": "test_login*", "timeout_seconds": 300 }`
→ `{ "passed": 11, "failed": 1, "skipped": 0, "failures": [{ "test": "test_login_expired",
"message": "AssertionError: expected 401, got 200", "location": "tests/test_auth.py:88" }] }`.

## Failure modes
- `framework_not_found` — no runner detectable/installed (not retryable; fix environment).
- `setup_error` — suite failed before any test ran (not retryable; the message is the fix input).
- `timeout` — retryable once with a narrower `filter` or higher limit.

Note: failing tests are **not** a tool failure — they are a successful result with `failed > 0`.
A caller must never treat a red suite as a reason to retry the same call unchanged.

## Constraints
Runs inside the project sandbox; must not touch the network unless the suite itself does.
Output must stay structured even when the runner crashes mid-suite (partial counts + setup_error).
