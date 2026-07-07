# skill.core-utils.archive-operator — spec

## What it does
Creates, extracts, or lists archives (zip, tar.gz) within the project sandbox. `list` is
read-only; `compress`/`extract` change local files only.

## When to use / when not
- **Use** to package build artifacts, unpack a received bundle, or inspect an archive's
  contents before extracting.
- **Don't use** to move data out of the sandbox (packaging for an upload is fine; the upload
  itself is a different, external-effect skill).

## Inputs / outputs
- In: `action` (`compress|extract|list`), `archive_path`, `paths` (sources; required for
  `compress`), `format` (`zip|tar.gz|auto`), optional `dest_path` (extract target; default
  alongside archive).
- Out: `{ action, entries, output_path }` — `entries` lists members touched/found.

## Worked example
`{ "action": "list", "archive_path": "incoming/bundle.zip", "paths": null, "format": "auto",
"dest_path": null }` → `{ "action": "list", "entries": ["src/app.py", "README.md"],
"output_path": null }`.

## Failure modes
- `corrupt_archive` (not retryable) · `unsupported_format` (not retryable)
- `path_escape_blocked` — an entry resolves outside `dest_path` ("zip-slip"); extraction
  aborts entirely, nothing partial remains (not retryable, and the archive should be treated
  as hostile).

## Constraints
Always `list` before `extract` on archives from outside the project. Extraction is
all-or-nothing: a blocked entry rolls back everything already extracted. Symlinks inside
archives are materialized as plain files or skipped — never followed.
