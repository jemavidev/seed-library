# Context pack — spec-template

> Status: active

The canonical anatomy of a **spec**: the document that fixes *what* will be built and *which
decisions were made*, produced by synthesis (from a finished conversation, a wayfinder map, a
grilled charter) — never by interviewing during writing. A spec is a specification, not an
executable: it feeds decomposition and generation, it doesn't run.

## The anatomy

1. **Problem Statement** — the problem from the user's perspective.
2. **Solution** — the solution from the user's perspective.
3. **User Stories** — a long, numbered, deliberately exhaustive list:
   `As an <actor>, I want <feature>, so that <benefit>`. Coverage beats elegance here.
4. **Implementation Decisions** — the decisions that were made: modules built/modified and
   their interfaces, architectural calls, schema changes, API contracts. Decisions, not
   design prose.
5. **Testing Decisions** — what makes a good test here (external behaviour, never
   implementation details), which modules get tested, prior art to imitate.
6. **Out of Scope** — what this spec consciously excludes.
7. **Further Notes** — anything load-bearing that fits nowhere above.

## Rules

- **No file paths, no code snippets** — they go stale faster than the spec. The one
  exception: a prototype-validated snippet that encodes a decision more precisely than prose
  can (a state machine, a schema, a type shape), trimmed to the decision-rich part and marked
  with its origin.
- **Domain vocabulary throughout** — the project glossary's terms (see the `domain-glossary`
  pack), never synonyms of them.
- **Sections may be empty, never absent** — an empty "Out of Scope" is a visible statement;
  a missing one is a hole.
- Downstream: a finished spec decomposes via the `tracer-bullet-decomposition` pattern; the
  spec is the parent artifact tickets point back to, and decomposition never edits it.

## How to instantiate

Copy `example.json` to declare the section set and snippet policy for a project; validation:
`config.schema.json`.
