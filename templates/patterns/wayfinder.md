# Pattern — wayfinder (shared-map planning)

## When to use
A loose idea has arrived — too big for one agent session, and wrapped in fog: the way from
here to the **destination** isn't visible yet. Wayfinding charts that way as a shared map of
typed tickets on the tracker, then works them one per session until the route is clear. The
destination varies per effort — a spec to hand off, a decision to lock, a change made in
place — and naming it is the first act of charting, because it fixes the scope.

## When not to use
- The whole journey fits one session → no map; plain grilling or execution.
- The work is *execution* across sessions, not open decisions → `long-horizon-run`
  (checkpointed autonomy) or `context-handoff` (succession). Wayfinder produces decisions,
  not deliverables.
- The plan is already clear and only needs slicing → `tracer-bullet-decomposition`.

## Mechanics that matter
- **Plan, don't do.** Each ticket resolves a decision; the pull to just do the work is the
  signal you've reached the map's edge and it's time to hand off to implementation.
- **The map is an index, not a store.** One issue, low resolution: destination, a one-line
  gist per closed ticket (the detail lives in the ticket), the fog, and out-of-scope. Open
  tickets are found by query, never listed in the body.
- **Fog of war.** Chart only what you can see. The test for fog vs ticket: can you state the
  question precisely *now*? (Not: can you answer it now.) Sharp → ticket, even if blocked.
  Dim → one loose line in "not yet specified"; it graduates when the frontier reaches it.
- **The frontier** is the open, unblocked, unclaimed tickets. A session claims (assigns)
  before any work, so parallel sessions skip it. One resolution per session — the budget
  enforces it.
- **Typed tickets, typed autonomy.** research and (some) task tickets run AFK; grilling and
  prototype tickets are human-in-the-loop and only resolve through that live exchange — an
  agent answering its own grilling question has broken the pattern.
- **Out of scope never graduates.** Work past the destination gets one line and a closed
  ticket; it returns only if the destination is redrawn, as a fresh effort.

## Failure modes
- **Doing instead of deciding**: a resolution that ships an implementation has jumped the
  map; capture the decision, hand the doing to implementation tickets outside the map.
- **Pre-slicing the fog**: fog cut into ticket-sized pieces before it's specifiable creates
  tickets that get deleted; fog is coarser than a ticket by design.
- **Bare-id narration**: humans read names, not `#42`; every reference wraps the link in the
  ticket's title.

## Source attribution
Adapted from `mattpocock/skills` v1.1 `wayfinder` (MIT) — map/fog/frontier semantics and the
one-ticket-per-session rule; recast as a declarative graph with stance-typed interrupts
(hand-seeded 2026-07-10).
