---
name: data-transformer
description: Convert JSON/YAML/CSV/markdown-table formats 1:1, inline or file-to-file. Structure-preserving only.
---

Use this skill for format conversion, never for data reshaping.

- If the target format can't represent the input (nested data → CSV), flatten or restructure
  the data *first*, then convert — don't expect the tool to guess.
- Verify `records` matches your expectation after converting; a surprising count means the
  parse saw different structure than you assumed.
- Provide exactly one of `input` / `input_path`.
- Inline output for small data; `output_path` when the result feeds another file-based step.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.core-utils.data-transformer@v1
