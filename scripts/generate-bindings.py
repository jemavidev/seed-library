#!/usr/bin/env python3
"""Regenerate derived files for every creation, from its own source of truth.

Derived artifacts (never hand-edit these; edit `core/` and rerun):
  - `_meta.json`            for every creation
  - `bindings/claude-code/SKILL.md`  for every skill

Source of truth read: `core/prompt.md` frontmatter (name/description/goal),
`core/spec.md` (fallback description for hooks), and `toolspec.json` (capabilities).

Durability: stdlib-only, path-relative to this file, and **provenance-preserving** —
an existing `lineage` / `libraryShare` in `_meta.json` is kept as-is; only genuinely new
creations get the defaults below. So regeneration refreshes name/description/capabilities
from `core/` without ever stomping an asset's history. Idempotent: rerunning produces no diff.

Usage: python3 scripts/generate-bindings.py   (from anywhere)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CREATIONS = ROOT / "creations"

# Defaults applied ONLY to creations that have no _meta.json yet.
DEFAULT_LINEAGE = "hand-seeded@2026-07-07"
DEFAULT_SHARE = "candidate"


def parse_frontmatter(text: str):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        return {}, text
    fm, key = {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z_]+:", line):
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
        elif key and line.strip().startswith("- "):
            fm.setdefault(key + "_list", []).append(line.strip()[2:])
    return fm, m.group(2)


def hook_description(spec_text: str) -> str:
    m = re.search(r"## What it is\n(.+?)(?:\n\n|\n##)", spec_text, re.S)
    if not m:
        return ""
    return " ".join(m.group(1).split()).split(". ")[0].rstrip(".") + "."


def load_json(p: Path):
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def main():
    count = 0
    for creation in sorted(CREATIONS.iterdir()):
        if not creation.is_dir():
            continue
        cid = creation.name
        kind = cid.split(".")[0]
        toolspec = load_json(creation / "toolspec.json")

        name, description, body = cid.split(".", 1)[1], "", ""
        prompt_path = creation / "core" / "prompt.md"
        if prompt_path.exists():
            fm, body = parse_frontmatter(prompt_path.read_text())
            name = fm.get("name", name)
            description = fm.get("description", fm.get("goal", ""))
        elif (creation / "core" / "spec.md").exists():
            description = hook_description((creation / "core" / "spec.md").read_text())

        # Preserve provenance if the asset already exists.
        prior = load_json(creation / "_meta.json")
        meta = {
            "id": cid,
            "kind": kind,
            "name": name,
            "description": description,
            "lineage": prior.get("lineage", DEFAULT_LINEAGE),
            "capabilities": toolspec.get("capabilities", []),
            "libraryShare": prior.get("libraryShare", DEFAULT_SHARE),
        }
        (creation / "_meta.json").write_text(json.dumps(meta, indent=2) + "\n")

        if kind == "skill":
            skill_md = (
                f"---\nname: {name}\ndescription: {description}\n---\n\n"
                f"{body.strip()}\n\n"
                f"---\n\n"
                f"Full spec: see `core/spec.md` of this creation; interface schema in\n"
                f"`core/interface.schema.json`; execution sidecar in `toolspec.json`.\n\n"
                f"lineage: library://{cid}@v1\n"
            )
            out = creation / "bindings" / "claude-code" / "SKILL.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(skill_md)
        count += 1
    print(f"generate-bindings: refreshed {count} creations")


if __name__ == "__main__":
    main()
