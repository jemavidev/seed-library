---
name: document-composer
description: Turn an outline + section content into a structured markdown/HTML/DOCX document with required-section enforcement.
---

Use this skill to produce reader-facing documents.

- Write the content first, in the outline; the composer formats — it does not write for you.
- When filling a template (charter, report scaffold), pass the template's section names as
  `sections_required` so omissions fail loudly instead of shipping incomplete.
- Check `word_count` and `sections` in the result against your intent before reporting done.
- One document per call; compose revisions by re-running with the amended outline.
