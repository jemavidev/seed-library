# Pattern — triage (proposal state machine)

## When to use
A stream of incoming proposals needs a maintainer-controlled path from "arrived" to
"actionable or declined": external issues and PRs, and equally a self-improving system's own
suggestion queue — anything that *proposes* work someone must accept before it runs. Gives
the propose-never-auto-apply doctrine its vocabulary: every item ends holding exactly one
category (`bug` | `enhancement`) and one state (`needs-triage` → `needs-info` /
`ready-for-agent` / `ready-for-human` / `wontfix`).

## When not to use
- Work already accepted and specified → decomposition (`tracer-bullet-decomposition`) or
  execution; triage decides *whether*, not *how*.
- A single ad-hoc request from the owner in live conversation → just do the work; the state
  machine earns its cost on a queue, not a favor.

## Mechanics that matter
- **Redundancy first.** Before anything else, the gatherer searches for an existing
  implementation *by concept* (not the request's wording) and reads the rejection log. A hit
  short-circuits: already-built → point to where it lives; already-rejected → point to the
  logged reason. Cheapest triage is the one that doesn't happen.
- **Verify before grilling.** Reproduce the bug from the reporter's steps, or check the PR
  does what it claims, *before* investing conversation. Failure to reproduce is a strong
  `needs-info` signal; a confirmed verification makes a much stronger brief.
- **Rejections are knowledge** (see `lessons/rejections-are-knowledge.md`): `wontfix` may not
  close without a reason written to the rejection log — that log is what keeps the queue from
  refilling with ghosts.
- **The maintainer can override at any time**: an explicit "move it to X" skips the machine;
  the machine flags unusual transitions and asks, it never argues.
- **Provenance disclaimer**: everything the machine posts to a shared tracker is labeled as
  generated during triage.

## Failure modes
- **Two state roles at once** — the tell of a machine bypassed by hand; flag and ask, don't
  guess which is current.
- **Vague needs-info** — "please provide more info" returns nothing; questions must be
  specific enough that the reporter's answer changes the state.
- **Briefless ready-for-agent** — a state without its artifact; the brief is what makes the
  state true.

## Source attribution
Adapted from `mattpocock/skills` v1.1 `triage` + its out-of-scope knowledge-base convention
(MIT); recast as a declarative graph with the rejection log promoted to a first-class gate
(hand-seeded 2026-07-10).
