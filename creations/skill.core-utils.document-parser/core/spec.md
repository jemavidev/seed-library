# skill.core-utils.document-parser — spec

## What it does
Converts a non-plain-text document (PDF, DOCX, XLSX, CSV with odd encodings, HTML) into
markdown or plain text, preserving structure (headings, tables, lists) where the format allows.
Read-only.

## When to use / when not
- **Use** when a read attempt reported `binary_file`, or the input is an office/PDF document
  whose *content* is needed for reasoning.
- **Don't use** on source code or plain text (read directly), or when layout fidelity matters
  more than content (this extracts, it does not render).

## Inputs / outputs
- In: `input_path`, `output_format` (`markdown` | `text`), optional `pages` (range string like
  `"1-5"`, for paginated formats).
- Out: `{ content, metadata: { format, pages_total, pages_extracted, tables } }`.

## Worked example
`{ "input_path": "docs/contract.pdf", "output_format": "markdown", "pages": "1-3" }` →
`{ "content": "# Service Agreement\n...", "metadata": { "format": "pdf", "pages_total": 12,
"pages_extracted": 3, "tables": 1 } }`.

## Failure modes
- `unsupported_format` — extension/content not handled (not retryable).
- `corrupt_file` — parseable format, unreadable file (not retryable).
- `password_protected` — encrypted document; surface to a human, never brute-force.

## Constraints
Extraction must be deterministic for the same input. Tables become markdown tables when
`output_format=markdown`; anything untranslatable degrades to text, never silently dropped.
