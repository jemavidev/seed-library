---
name: read-project-file
description: Read one project file as text, safely inside the sandbox, with truncation metadata. Read-only.
---

Use this skill to inspect a file before reasoning about it or editing it.

- Always read a file before proposing a modification to it.
- Pass a project-relative path; never attempt absolute paths outside the project.
- If the result has `truncated: true`, do not assume you saw the whole file — re-read with a
  higher `max_bytes` only if the remainder is actually needed.
- On `binary_file`, switch to the document-parser skill instead of retrying.
- On `not_found`, verify the path with a file search instead of guessing variants blindly.
