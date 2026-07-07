# skill.core-utils.regex-data-extractor — spec

## What it does
Extracts structured tokens (emails, IPs, URLs, hashes, or a custom regex) from a text string or
a file, returning the deduplicated match list. Read-only, deterministic.

## When to use / when not
- **Use** to pull entities out of logs, dumps, or documents for downstream processing.
- **Don't use** for semantic extraction ("find the customer's complaint") — literal patterns
  only — nor for searching across many files (`file-search` first, extract from hits).

## Inputs / outputs
- In: exactly one of `text` / `input_path`; `extract` (`emails|ips|urls|hashes|custom`);
  `custom_pattern` (required iff `extract=custom`).
- Out: `{ matches: [string], count }` — deduplicated, input order preserved.

## Worked example
`{ "text": "contact ops@acme.io or admin@acme.io, ops@acme.io again", "input_path": null,
"extract": "emails", "custom_pattern": null }` →
`{ "matches": ["ops@acme.io", "admin@acme.io"], "count": 2 }`.

## Failure modes
- `invalid_pattern` — custom regex does not compile (not retryable).
- `no_input` — both `text` and `input_path` null, or both set (not retryable; ambiguity is
  rejected, not guessed).

## Constraints
Built-in patterns are documented, versioned constants — changing them is a breaking change.
`count` is post-deduplication.
