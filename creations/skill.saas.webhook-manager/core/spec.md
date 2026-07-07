# skill.saas.webhook-manager — spec

## What it does
Registers, removes, or lists webhook subscriptions on a configured external provider, so
events from that provider can reach the runtime's trigger system. The provider is a binding.

## When to use / when not
- **Use** to wire an event source ("notify on new issue", "on payment failed") into
  automated flows, and to clean subscriptions up afterwards.
- **Don't use** to *receive* or process events (that is the trigger system's job) or against
  providers not present in configuration.

## Inputs / outputs
- In: `provider_ref`, `action` (`register|remove|list`), `url` (the receiving endpoint;
  register only), `events` (event type names; register only), `webhook_id` (remove only).
- Out: `{ action, webhook_id, active, events }`.

## Worked example
`{ "provider_ref": "code-host", "action": "register",
"url": "https://runtime.example.com/hooks/inbound", "events": ["issues.opened"],
"webhook_id": null }` → `{ "action": "register", "webhook_id": "wh-morrow-17",
"active": true, "events": ["issues.opened"] }`.

## Failure modes
- `provider_unreachable` (retryable) · `auth_failed` (not retryable)
- `invalid_url` — non-https or not an allowed receiving endpoint (not retryable)
- `webhook_not_found` (not retryable) · `event_unsupported` (not retryable; the message
  lists the provider's supported events).

## Constraints
Receiving URLs must belong to the runtime's configured inbound endpoints — registering an
arbitrary third-party URL as receiver is an exfiltration channel and must fail as
`invalid_url`. Register is exactly compensated by remove(`webhook_id`); every registration is
recorded so orphaned webhooks can be swept.
