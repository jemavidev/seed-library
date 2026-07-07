---
name: document-parser
description: Convert PDF/DOCX/XLSX/HTML documents to markdown or plain text with structure preserved. Read-only.
---

Use this skill to get document content into workable text.

- For long paginated documents, extract in page ranges and stop when you have what you need —
  do not parse 200 pages for one clause.
- Check `metadata.pages_extracted` against `pages_total` before claiming you read the whole
  document.
- On `password_protected`, report it and stop; never attempt to bypass.
- Prefer `markdown` output when tables matter; `text` when you only need prose.
