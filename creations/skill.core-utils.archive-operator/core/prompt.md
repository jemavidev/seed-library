---
name: archive-operator
description: Create, list, or extract zip/tar.gz archives inside the sandbox; zip-slip-safe, all-or-nothing extraction.
---

Use this skill for packing and unpacking bundles.

- `list` before `extract` when the archive came from anywhere external — check the entries
  look sane before touching the filesystem.
- On `path_escape_blocked`, stop and report: the archive attempted to write outside its
  target and must be treated as hostile, not re-tried with a different destination.
- Compress with explicit `paths`; never "everything" by default.
- Note `output_path` in your report so the artifact is findable.
