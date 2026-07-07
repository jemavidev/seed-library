# Context pack — project-rules

The convention for project-level rule files that agents must respect: which files count,
how precedence works, and how the set compiles into one flat context block.

## The convention

1. **Rule files** live in the project tree as plain markdown: an agent context file at the
   repo root (`AGENTS.md` or the harness's equivalent), optional per-directory context files,
   plus style sections in `CONTRIBUTING.md` and editor rule files where present.
2. **Nearest wins.** A rule file closer to the files being changed overrides a repo-root
   rule on conflict; repo-root overrides user-global defaults. Precedence is by path depth,
   never by file kind.
3. **Compilable.** The whole set must flatten into a single markdown block (the
   `block:project-rules` referenced by `default-agent-context`), each rule annotated with its
   source file. `hook.style-rules-injector` is the mechanical implementation of this compile.
4. **Human-first.** Rule files are written for people; agents consume them as-is. No
   agent-only syntax: if a human contributor would not read it, it does not belong in a rule
   file.

## Design rules
- Keep the root file short (a screen); push detail into per-directory files where it applies.
- Rules that are really *policies* (approval stances, budgets) belong in runtime policy, not
  in rule files — rule files describe how work should look, not who may do it.

## How to instantiate
Copy `example.json` to declare the sources and compile budget for a project; validation:
`config.schema.json`.
