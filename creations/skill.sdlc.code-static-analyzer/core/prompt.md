---
name: code-static-analyzer
description: Run a linter/type-checker and get normalized, typed findings (rule, severity, file, line, message). Read-only.
---

Use this skill as the fast, cheap verification pass.

- Run it before and after editing: before to learn the baseline, after to confirm you added
  zero new findings.
- Judge your change by the *delta* in findings, not the absolute count — legacy noise is not
  yours to fix unless asked.
- Use `severity_threshold` to keep loops focused: gate on `error` first, then tighten.
- Feed each finding's `file:line` and `message` directly into the fix; do not paraphrase.
