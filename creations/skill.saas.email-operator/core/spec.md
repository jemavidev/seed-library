# skill.saas.email-operator — spec

## What it does
Sends transactional email through a configured provider: explicit recipient lists, subject,
body, attachments from the project sandbox. External effect of the strongest kind — email
cannot be unsent, so policy should treat this as effectively uncompensated.

## When to use / when not
- **Use** for deliberate, individually-addressed mail: reports to stakeholders, generated
  documents, account notifications.
- **Don't use** for channel notifications (`message-dispatcher` with an email channel is the
  lighter tool) and never for bulk/marketing sends — recipient lists beyond a configured cap
  are rejected by design.

## Inputs / outputs
- In: `to` (explicit list), `subject`, `body`, `from_ref` (configured sender identity),
  `cc`, `attachments` (project paths).
- Out: `{ message_id, accepted: [addresses], rejected: [addresses] }` — partial acceptance is
  a normal result; report it, don't retry the accepted ones.

## Worked example
`{ "to": ["owner@acme.io"], "subject": "Q3 audit report", "body": "Attached…",
"from_ref": "reports", "cc": null, "attachments": ["reports/audit.pdf"] }` →
`{ "message_id": "e-3311", "accepted": ["owner@acme.io"], "rejected": [] }`.

## Failure modes
- `provider_unreachable` (retryable) · `quota_exceeded` (retryable after window)
- `invalid_recipient` — malformed address (not retryable)
- `attachment_too_large` / `attachment_not_found` (not retryable)
- `recipient_cap_exceeded` — list larger than the configured cap (not retryable by design).

## Constraints
Body and attachments must pass redaction before sending. The only compensation email supports
is a follow-up correction — which is why approval policies should gate this skill at
`expert-review` or stricter under anything but the most permissive policy.
