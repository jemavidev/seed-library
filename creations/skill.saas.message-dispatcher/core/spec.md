# skill.saas.message-dispatcher — spec

## What it does
Sends one message to a configured channel — chat (team messenger, community server, personal
messenger) or email-as-channel — and returns the delivery receipt. External effect: a sent
message reaches humans and cannot be truly unsent everywhere.

## When to use / when not
- **Use** for notifications, reports, approval requests (the transport under
  `hook.hitl-notifier`), and status updates to configured destinations.
- **Don't use** for transactional email with attachments/recipient lists (`email-operator`)
  or for arbitrary recipients — destinations come from configuration, not free-form input.

## Inputs / outputs
- In: `channel_ref` (configured destination name), `body`, `subject` (channels that support
  it), `thread_ref` (reply threading where supported), `format` (`text|markdown`).
- Out: `{ message_id, channel_ref, delivered_at }`.

## Worked example
`{ "channel_ref": "ops-alerts", "body": "Deploy 1.4.2 needs approval: …", "subject": null,
"thread_ref": null, "format": "markdown" }` →
`{ "message_id": "m-88412", "channel_ref": "ops-alerts", "delivered_at": "2026-07-07T15:00:41Z" }`.

## Failure modes
- `channel_not_configured` (not retryable) · `recipient_invalid` (not retryable)
- `delivery_failed` (retryable) · `rate_limited` (retryable after window)
- `body_too_large` (not retryable; summarize with a pointer instead).

## Constraints
Outbound content should pass redaction (`hook.pii-redactor`) before sending — a message is a
publication. Retraction support varies by channel: compensation retracts where the channel
allows (`message_id`) and otherwise posts a correction; assume the recipient saw the original
either way.
