# skill.devops.object-storage-operator — spec

## What it does
Moves objects between the project sandbox and a configured object store (bucket): upload,
download, list, delete. Provider-neutral; the store, its region, and its versioning policy
are bindings resolved through `storage_ref`.

## When to use / when not
- **Use** to publish build artifacts, fetch datasets, back up deliverables, or enumerate
  what a bucket holds.
- **Don't use** as a working filesystem (objects are not files; latency and semantics
  differ) or for serving content to users (that is infrastructure design, not an operation).

## Inputs / outputs
- In: `storage_ref`, `action` (`upload|download|list|delete`), `key` (object key),
  `local_path` (sandbox side for upload/download), `prefix` (list filter).
- Out: `{ action, key, keys, size_bytes }` — `keys` populated by `list`.

## Worked example
`{ "storage_ref": "artifacts", "action": "upload", "key": "builds/api-1.4.2.tar.gz",
"local_path": "out/api-1.4.2.tar.gz", "prefix": null }` →
`{ "action": "upload", "key": "builds/api-1.4.2.tar.gz", "keys": null, "size_bytes": 8388608 }`.

## Failure modes
- `storage_unreachable` (retryable) · `auth_failed` (not retryable)
- `key_not_found` (not retryable) · `quota_exceeded` (not retryable)
- `delete_unversioned_blocked` — delete against a store without versioning enabled
  (not retryable **by design**: an unversioned delete has no undo, so the skill refuses it;
  policy may override only via the approval flow).

## Reversibility
`upload` ↔ `delete(key)`; `delete` ↔ restore of the prior version — which only exists on
versioned stores, hence the `delete_unversioned_blocked` rule. `list`/`download` are
effect-free reads. Keys are recorded per call so a sweep can reconcile orphaned uploads.
