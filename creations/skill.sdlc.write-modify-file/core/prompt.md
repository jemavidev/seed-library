---
name: write-modify-file
description: Create or modify one project file (full write or targeted patch), atomically, inside the sandbox.
---

Use this skill to apply a change you have already reasoned about.

- Read the current file first; never patch from memory of an older read.
- Prefer `mode: "patch"` with an exact, unique `patch_target`; use `mode: "write"` only for
  new files or intentional full rewrites.
- If `patch_target_not_found`, re-read the file and rebuild the patch — do not fall back to a
  full overwrite to "make it work".
- Keep one logical change per call so each write is independently reviewable and undoable.
