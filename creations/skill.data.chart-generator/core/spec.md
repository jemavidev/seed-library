# skill.data.chart-generator — spec

## What it does
Renders tabular data (JSON records inline or from a file) into a chart file — line, bar,
scatter, pie, or histogram — as SVG, PNG, or a self-contained HTML file. Local effect: writes
one artifact into the project.

## When to use / when not
- **Use** to make results legible to humans: trends in metrics, distributions from an
  analysis, report figures. Charts are the transparency tool for non-technical readers.
- **Don't use** to *analyze* (run `statistical-analyzer` first and chart its output) or for
  interactive dashboards (out of scope — one static artifact per call).

## Inputs / outputs
- In: exactly one of `data` (JSON array of records) / `input_path` (json/csv file);
  `chart_type`; `x` (field name); `y` (field names, one series each); `title`;
  `output_path`; `format` (`svg|png|html`).
- Out: `{ output_path, series_count, points }`.

## Worked example
`{ "data": "[{\"day\":\"Mon\",\"errors\":12},{\"day\":\"Tue\",\"errors\":7}]",
"input_path": null, "chart_type": "bar", "x": "day", "y": ["errors"],
"title": "Errors by day", "output_path": "reports/errors.svg", "format": "svg" }` →
`{ "output_path": "reports/errors.svg", "series_count": 1, "points": 2 }`.

## Failure modes
- `no_input` — zero or two data inputs (not retryable).
- `invalid_data` — input not parseable as records (not retryable).
- `unknown_field` — `x`/`y` name not present in the records (not retryable; the message
  lists available fields).
- `unsupported_chart` — chart_type/format combination not implemented (not retryable).

## Constraints
Charts never invent data: missing values render as gaps, not interpolations, unless the spec
of a future option says otherwise. Axis labels default to field names; a chart with an
unlabeled axis fails composition review, so the implementation always labels.
