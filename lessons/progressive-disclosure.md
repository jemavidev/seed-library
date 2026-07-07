# Lesson — progressive disclosure: inject the index, never the catalog

**Statement.** With a growing skill catalog, never load full skill bodies into an agent's context
up front. Keep only `name` + one-line `description` resident; load the full spec/prompt on
activation.

**Evidence (source).** The SKILL.md convention (agent-skills format): frontmatter stays in
context, the body is read on demand. Systems that inject full catalogs see context bloat, worse
tool selection, and higher cost as the catalog grows past a few dozen entries.

**How to apply.** Context assembly reads each creation's `core/prompt.md` frontmatter only.
The full `spec.md`/`prompt.md` body is injected only after the router/agent selects that skill.
Catalog growth should never change baseline context size by more than one line per skill.

**Valid at.** 2026-07-07.
