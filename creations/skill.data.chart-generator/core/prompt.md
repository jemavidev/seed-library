---
name: chart-generator
description: Render JSON/CSV records into a labeled line/bar/scatter/pie/histogram chart file (SVG/PNG/HTML).
---

Use this skill to make numbers readable — after the analysis, not instead of it.

- Pick the form from the question: trend → line, comparison → bar, relationship → scatter,
  distribution → histogram. Pie only for parts-of-a-whole with few slices.
- One message per chart: if you need two ideas, make two charts.
- Missing data renders as gaps — leave them visible; do not pre-fill holes to make the line
  look continuous.
- On `unknown_field`, re-check the actual record keys from the error; don't guess variants.
