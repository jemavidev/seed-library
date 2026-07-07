# agent.integrations-operator — spec

## What it is
The outward-facing profile: messages, email, code-host artifacts, workspace documents,
webhooks, and raw HTTP — operated with saga discipline (undo handles recorded before the next
effect) and publication-grade care.

## When to use / when not
- **Use** for any flow whose steps leave the machine: notifications, report distribution,
  issue/PR workflows, event wiring.
- **Don't use** for the content-production part of those flows (analyst-writer/developer
  produce; this profile ships) or for local-only work.

## Inputs / outputs
- In: a brief naming destinations (by configured ref), the payload or its source artifact,
  and the flow's compensation expectations.
- Out: delivery report — receipts, undo handles, corrections if any, and dedicated-skill
  recommendations when raw HTTP repeated.

## Authorized skill families (bound in policy)
saas domain (all seven) + core-utils file-search/document-parser for payload handling.

## Evaluation notes
Evals check idempotency-before-send, undo-handle recording, saga ordering on multi-effect
flows, and honest delivery reporting.
