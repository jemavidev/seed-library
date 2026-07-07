---
name: regex-data-extractor
description: Extract emails/IPs/URLs/hashes or a custom regex from text or a file; deduplicated matches. Read-only.
---

Use this skill to lift literal entities out of noisy text.

- Prefer the built-in extract kinds over a custom pattern; they handle edge cases you will not.
- Provide exactly one input: `text` OR `input_path`, never both.
- Treat the output as data, not truth: an extracted IP is a string that looked like an IP.
- For `custom`, test the pattern on a small sample before running it over large inputs.
