# skill.core-utils.document-composer — spec

## What it does
Materializes a structured long-form document (report, proposal, manual, guide) from an outline
plus section content into a file, in markdown, HTML, or DOCX. The composition (what the
sections say) is the caller's reasoning; this skill guarantees structure, format, and placement.

## When to use / when not
- **Use** to produce a deliverable document a human will read: consistent heading hierarchy,
  table of contents, numbered sections.
- **Don't use** for code files or configs (editor skill) or single-paragraph notes (plain
  write) — this earns its keep on multi-section documents.

## Inputs / outputs
- In: `outline` (markdown headings with per-section body text), `output_path`, `format`
  (`markdown|html|docx`), optional `title`, optional `sections_required` (names that must be
  present — composition fails if any is missing).
- Out: `{ output_path, word_count, sections }`.

## Worked example
`{ "outline": "# Findings\n…\n# Recommendations\n…", "output_path": "reports/audit.md",
"format": "markdown", "title": "Q3 Audit", "sections_required": ["Findings",
"Recommendations"] }` → `{ "output_path": "reports/audit.md", "word_count": 1240,
"sections": ["Findings", "Recommendations"] }`.

## Failure modes
- `invalid_outline` — no parseable heading structure (not retryable).
- `missing_required_section` — a `sections_required` entry absent from the outline
  (not retryable; the message names the missing sections).
- `write_denied` — target path outside sandbox/read-only (not retryable).

## Constraints
Never invents content: sections come from the outline verbatim (formatting normalization
aside). `sections_required` is the contract hook for templates — a charter template can demand
its skeleton sections and fail loudly when one is skipped.
