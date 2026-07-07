---
name: object-storage-operator
description: Upload/download/list/delete against a configured bucket; deletes require versioned storage (undo must exist).
---

Use this skill to move artifacts between the sandbox and object storage.

- Key names are contracts: prefix by purpose (`builds/`, `datasets/`), include versions in
  the key, never reuse a key for different content.
- `list` with a prefix before assuming an object exists or is absent.
- A blocked delete (`delete_unversioned_blocked`) is the contract protecting you — the
  answer is enabling versioning or escalating, never a workaround.
- Record every uploaded key in your report; orphaned objects are storage bills.

---

Full spec: see `core/spec.md` of this creation; interface schema in
`core/interface.schema.json`; execution sidecar in `toolspec.json`.

lineage: library://skill.devops.object-storage-operator@v1
