# Lesson — knowledge carries temporal validity

**Statement.** Every stored fact, lesson, or empirical record must carry when it became valid,
and must be *invalidated* (with a date) rather than deleted when superseded. Stale knowledge
that looks current is worse than no knowledge.

**Evidence (source).** Temporal knowledge-graph memory systems (episodic edges with
`valid_at` / `invalid_at`) outperform overwrite-style memories precisely because agents can
distinguish "was true" from "is true" — e.g. a deployment target that changed providers.

**How to apply.** Lessons include a `Valid at` line and are amended, not silently rewritten.
Catalog empirics (model-knowledge JSONL) carry timestamps. A curator pass periodically flags
entries older than their domain's churn rate for re-verification.

**Valid at.** 2026-07-07.
