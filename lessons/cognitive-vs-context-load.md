# Lesson — cognitive load vs context load (and the router that pays it down)

**Statement.** Every asset in a growing library is paid for in one of two currencies, and the
choice is a design decision, not an accident:

- **Context load** — the asset's description sits in the working window *every turn* so the
  agent can reach for it unprompted (model-invoked). It costs tokens continuously; it scales
  badly as the catalog grows.
- **Cognitive load** — the description is stripped from the window; the asset fires only when
  *named* (user-invoked). It costs zero tokens, but now some index — a human, or a routing
  agent — has to remember it exists and when to reach for it.

Most durable, high-value assets are user-invoked, so **cognitive load is the pressure a large
library is built to manage.** When user-invoked assets multiply past what any single index can
hold, the cure is a **router**: one asset that names the others and states when to reach for
each, turning an unnavigable pile into a graph with a single entry node.

**Evidence (source).** Distilled from the authoring doctrine of `mattpocock/skills` (MIT) —
its `writing-great-skills` reference and `ask-matt` router. The same two-load framing explains
why SeeD keeps only `name` + one-line `description` resident (see [[progressive-disclosure]])
and why a catalog past a few dozen entries needs [[seed-library-seeding|a librarian]].

**How to apply.**
- Default new skills to user-invoked (zero standing context cost); promote to model-invoked
  only when the agent must reach for it *without being told* and the description earns its
  permanent window rent.
- The moment the catalog can't be held in one head, a router asset is not optional — it is the
  thing that keeps the accumulated knowledge reachable. A self-evolving library that adds
  assets forever needs a router that **cannot rot**: generate its index from asset metadata,
  never hand-maintain the list.
- Judge every "should this be its own asset?" decision by which load it spends and whether the
  router can still route to it.

**Valid at.** 2026-07-07.
