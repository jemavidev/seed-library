# skill.sdlc.write-modify-file — spec

## What it does
Creates or modifies one file inside the project sandbox. Two modes: `write` (create or fully
overwrite) and `patch` (apply a targeted replacement to an existing file). Effect is local to
the project and is expected to run under a checkpoint/undo regime.

## When to use / when not
- **Use** to materialize a reviewed change: new source file, config edit, doc update.
- **Don't use** to move/delete files (different operation, different reversibility story),
  nor for bulk multi-file rewrites — those should be decomposed so each write is reviewable.
- **Patch over write** whenever the file exists: a patch that fails to match is a loud,
  safe signal; a blind overwrite silently destroys concurrent edits.

## Inputs / outputs
- In: `file_path`, `content` (full body for `write`, replacement block for `patch`),
  `mode`, optional `patch_target` (exact text to replace; required when `mode=patch`),
  optional `create_dirs`.
- Out: `{ bytes_written, created }` — `created: true` means the file did not exist before.

## Worked example
`{ "file_path": "src/views.py", "content": "def health(request): ...", "mode": "patch",
"patch_target": "def health(request):\n    pass", "create_dirs": null }` →
`{ "bytes_written": 214, "created": false }`.

## Failure modes
- `access_denied` — outside sandbox / read-only path (not retryable).
- `patch_target_not_found` — `patch_target` text absent or ambiguous (not retryable; re-read
  the file, recompute the patch).
- `missing_patch_target` — `mode=patch` without `patch_target` (not retryable).
- `disk_full` — retryable after cleanup.

## Constraints
Writes must be atomic (temp file + rename) so an interrupted call never leaves a half-written
file. `write` mode on an existing file must be an explicit, logged overwrite.
