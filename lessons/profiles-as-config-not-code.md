# Lesson — agent profiles are config, not code

**Statement.** An agent's identity (role, goal, constraints, authorized tools) lives in
versioned, human-readable config (markdown/YAML), separate from any runtime code that
instantiates it.

**Evidence (source).** Role-based crew frameworks keep `role/goal/backstory` in YAML files and
task definitions likewise; teams iterate on agent behavior via config diffs, review them like
prose, and swap runtimes without rewriting identities. Profiles embedded in code get edited
rarely and reviewed never.

**How to apply.** Each profile is a creation whose `core/prompt.md` is the complete system
prompt (usable verbatim as a `system` parameter anywhere), with role/goal/constraints in
frontmatter. Runtime-specific policy (tool allowlists, approval stances) attaches in a binding,
so the identity stays portable.

**Valid at.** 2026-07-07.
