# skill.saas.workspace-document-operator — spec

## What it does
Reads and edits documents in a hosted workspace suite (collaborative docs/sheets — the suite
is a binding): read content, append, replace a named range, or create a document. Hosted docs
keep revision history, which is exactly what makes edits compensable.

## When to use / when not
- **Use** to publish reports into the team's shared space, maintain living documents, or
  read collaborative content as input.
- **Don't use** for local documents (`document-composer`) or for permission/sharing
  management (out of scope; sharing state is configured by humans).

## Inputs / outputs
- In: `document_ref` (configured document name or suite id), `action`
  (`read|append|replace-range|create`), `content`, `range_ref` (named range/section for
  replace-range), `title` (for create).
- Out: `{ action, document_ref, revision_id }` — plus `content` on `read`. `revision_id` is
  the compensation anchor: keep it.

## Worked example
`{ "document_ref": "weekly-status", "action": "append", "content": "## Week 27\n…",
"range_ref": null, "title": null }` →
`{ "action": "append", "document_ref": "weekly-status", "revision_id": "r-2214", "content": null }`.

## Failure modes
- `document_not_found` (not retryable) · `permission_denied` (not retryable)
- `range_not_found` (not retryable) · `conflict` — concurrent edit collision (retryable once
  after re-read) · `auth_failed` (not retryable).

## Constraints
`read` is effect-free; the mutating actions are external effects on shared state that
colleagues see immediately — content passes redaction first. Compensation restores the
pre-edit revision (`revision_id`), which reverts the content but not colleagues' memory of
it: write accordingly.
