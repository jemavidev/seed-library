---
name: statistical-analyzer
description: Descriptive stats, correlation, hypothesis tests, distribution checks over records — always with n and caveats.
---

Use this skill before making any claim from data.

- Run `descriptive` first; test only what the descriptives make plausible.
- Report `n` and every `warnings` entry alongside any number you quote — a p-value stripped
  of its caveats is misinformation.
- Correlation is not causation: state relationships as associations unless the design
  supports more.
- On `insufficient_data`, the honest output is "not enough data to tell" — say exactly that.
