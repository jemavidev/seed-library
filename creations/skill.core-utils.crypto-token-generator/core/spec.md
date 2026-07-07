# skill.core-utils.crypto-token-generator — spec

## What it does
Generates cryptographic values: random tokens (URL-safe), UUIDv4, SHA-256 digests of a given
input, or HMAC-SHA256 signatures using a key referenced from the environment. Pure computation,
no state.

## When to use / when not
- **Use** for session tokens, webhook signatures, content digests, correlation ids.
- **Don't use** for password hashing (needs a slow KDF — out of scope by design) or anything
  requiring key *management* (rotation, storage) — keys are only ever referenced, never handled.

## Inputs / outputs
- In: `kind` (`random-token|uuid|sha256-digest|hmac-sha256`), optional `length` (random-token,
  bytes of entropy), optional `input` (required for digest/hmac), optional `key_env` (name of
  the environment variable holding the HMAC key; required for hmac).
- Out: `{ value, kind }` — hex for digests/signatures, base64url for random tokens.

## Worked example
`{ "kind": "sha256-digest", "length": null, "input": "hello", "key_env": null }` →
`{ "value": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", "kind": "sha256-digest" }`.

## Failure modes
- `invalid_length` — outside 16–128 bytes (not retryable).
- `missing_input` — digest/hmac without `input` (not retryable).
- `missing_key` — hmac with unset/empty `key_env` variable (not retryable; a key value must
  never be passed inline as a workaround).

## Constraints
Randomness must come from a CSPRNG. The HMAC key never appears in inputs, outputs, or logs —
only its environment variable *name* crosses the interface.
