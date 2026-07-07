# hook.style-rules-injector — spec

## What it is
A pre-run context hook: collects the project's rule files (agent context files, editor rule
files, contribution guides) and injects the applicable subset into the agent's context before
work starts — so style/convention compliance comes from the project, not from per-agent
prompt copies.

## Trigger semantics (harness-neutral)
- **Trigger:** `pre-run` — fires when an agent session starts inside a project, and again if
  the working directory changes.
- **Input:** the working directory.
- **Effect:** contributes a context block `project-rules` assembled from discovered rule
  files; contributes nothing when none exist.

## Behavior rules
1. **Discovery order (nearest wins):** rule files closer to the files being worked on
   override repo-root ones; repo-root overrides user-global. Ties break toward the more
   specific file.
2. **Known sources:** agent context files (`AGENTS.md` and harness equivalents), editor rule
   files (e.g. `.cursorrules`, `.editorconfig` prose sections), `CONTRIBUTING.md` style
   sections. The source list is binding-configurable; the precedence rule is not.
3. **Budgeted:** the block is capped (default 1,500 tokens); over-budget content is
   summarized with a pointer to the full file rather than truncated mid-rule.
4. **Traceable:** each injected rule block cites its source file so an agent can quote where
   a convention came from.

## When to attach
Any profile that writes into a project (developers, composers). Read-only profiles benefit
too: reviewers should judge against the project's rules, not their own defaults.
