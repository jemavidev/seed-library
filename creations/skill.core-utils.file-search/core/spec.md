# skill.core-utils.file-search — spec

## What it does
Searches the project sandbox for files by name pattern or for lines matching a content pattern
(plain or regex), returning match locations with short excerpts. Read-only.

## When to use / when not
- **Use** to locate where something is defined/used before reading whole files, or to enumerate
  files by glob.
- **Don't use** to read full file bodies (use the read skill on the located file) or for
  semantic "find code that does X" questions — this is literal matching only.

## Inputs / outputs
- In: `pattern`, `path` (root to search under), `type` (`content` | `filename`), optional
  `regex` (default plain-text), optional `max_results`.
- Out: `{ matches: [{ file, line, excerpt }], truncated }` — for `filename` searches `line`
  is 0 and `excerpt` is the filename.

## Worked example
`{ "pattern": "def handle_upload", "path": "src/", "type": "content", "regex": null,
"max_results": 20 }` → `{ "matches": [{ "file": "src/uploads.py", "line": 42,
"excerpt": "def handle_upload(request):" }], "truncated": false }`.

## Failure modes
- `invalid_pattern` — regex does not compile (not retryable; fix the pattern).
- `path_not_found` — search root missing (not retryable).

Zero matches is a successful result (`matches: []`), not a failure — callers should broaden
the pattern deliberately, not loop.

## Constraints
Respects ignore files (`.gitignore` and equivalents) by default so vendored/generated trees
don't drown results. `truncated: true` means more matches exist than `max_results`.
