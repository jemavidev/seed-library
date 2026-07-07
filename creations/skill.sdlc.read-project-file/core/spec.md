# skill.sdlc.read-project-file — spec

## What it does
Reads the content of a single file inside the active project sandbox and returns it as text,
with truncation metadata. Read-only: never touches the filesystem state.

## When to use / when not
- **Use** to inspect source files, configs, or docs before proposing or applying a change.
- **Don't use** for pattern searches across many files (use `skill.core-utils.file-search`),
  for binary/office documents (use `skill.core-utils.document-parser`), or for files outside
  the project sandbox (out of scope by contract — the call must fail).

## Inputs / outputs
- In: `file_path` (project-relative), optional `encoding` (default `utf-8`), optional
  `max_bytes` cap.
- Out: `{ content, truncated, size_bytes }` — `truncated: true` means `content` was cut at
  `max_bytes` and the caller should re-read with a range or raise the cap deliberately.

## Worked example
Request `{ "file_path": "src/app/routes.py", "encoding": null, "max_bytes": 65536 }` →
`{ "content": "from ...", "truncated": false, "size_bytes": 4102 }`.

## Failure modes
- `not_found` — path does not exist (not retryable; check the path, don't loop).
- `access_denied` — path resolves outside the sandbox or lacks read permission (not retryable).
- `too_large` — file exceeds the hard ceiling even for truncated reads (not retryable).
- `binary_file` — content is not decodable text; caller should switch to the document parser.

## Constraints
Path traversal (`..`, symlinks escaping the sandbox) must be rejected as `access_denied`,
never silently resolved.
