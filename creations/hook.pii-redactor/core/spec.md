# hook.pii-redactor — spec

## What it is
A pre-external hook: scans every outbound payload (message bodies, email content, issue/PR
bodies, document edits, HTTP request bodies) for secrets and personal data before the effect
executes. Masks or blocks per category policy, and never silently alters meaning.

## Trigger semantics (harness-neutral)
- **Trigger:** `pre-tool`, scoped to invocations whose tool declares `effects: external`.
- **Input:** the outbound payload fields + the redaction policy in force.
- **Effect:** pass-through when clean; on detection, apply the category's action —
  `mask` (replace with a typed placeholder like `[REDACTED:api-key]`) or `block` (refuse the
  send with a typed failure naming the category and location). Every detection is recorded.

## Detection categories (each with its own default action)
- **Secrets** — API keys, tokens, private keys, connection strings, high-entropy credential
  shapes → default `block` (a secret in an outbound payload is an incident, not a typo).
- **Personal identifiers** — email addresses, phone numbers, government-id patterns,
  payment-card numbers (checksum-validated) → default `mask`, allowlist-aware (a support
  flow legitimately emails a customer's own address).
- **Internal markers** — hostnames/paths/refs matching the configured internal namespace →
  default `mask` outside configured internal channels.

## Behavior rules
1. **Masking is visible:** the sender sees what was masked and why before the payload goes
   out; a send whose meaning breaks under masking should be blocked instead (policy flag).
2. **Fail closed:** if the redactor itself errors, the external effect does not run.
3. **Allowlists are named and versioned** — per channel and per category, never global.
4. **Detections feed the audit record**, including masked previews, category, and action.

## When to attach
Globally on external effects; `agent.integrations-operator` assumes it is present.
