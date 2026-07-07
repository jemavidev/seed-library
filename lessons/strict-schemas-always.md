# Lesson — strict schemas, always

**Statement.** Every tool/skill interface schema must set `additionalProperties: false` and list
every property in `required`; optionality is expressed as `"type": ["string", "null"]`, never by
omission from `required`.

**Evidence (source).** OpenAI structured-outputs/function-calling strict mode and MCP practice:
models invent parameters when schemas are loose, and loose schemas silently accept those
inventions. Strictness turns hallucinated arguments into validation errors at the boundary
instead of wrong behavior downstream.

**How to apply.** Validation gates should reject any `interface.schema.json` that is missing
`additionalProperties: false` or whose `required` array does not cover all declared properties.
When a parameter is genuinely optional, declare the null-union type and document the default.

**Valid at.** 2026-07-07 — revisit if schema dialects change (current: JSON Schema 2020-12).
