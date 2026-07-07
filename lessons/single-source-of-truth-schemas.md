# Lesson — one source of truth per schema; bindings are derived

**Statement.** A skill's interface is defined exactly once (`core/interface.schema.json`).
Every other representation — harness wrappers, tool-calling declarations, docs tables — is
generated from it, never hand-written in parallel.

**Evidence (source).** Decorator-style tool frameworks derive the calling schema from one typed
signature; ecosystems that maintain hand-written duplicates (schema in code + schema in docs +
schema in wrapper) reliably drift, and drift surfaces as runtime argument errors that no single
file review can catch.

**How to apply.** Bindings reference or regenerate from core (`$ref` where the format allows).
If a binding needs information core lacks, extend core once — do not fork the schema into the
binding. Regenerating all bindings must be a safe, idempotent operation.

**Valid at.** 2026-07-07.
