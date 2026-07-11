#!/usr/bin/env python3
"""Validate the library. Exits non-zero (and prints findings) on any failure.

Checks:
  1. Core-neutrality — nothing under any `creations/*/core/` may name a harness, a model, or
     a framework. `core/` declares capabilities only; harness glue lives in `bindings/`.
     (This is the hard rule from the SeeD portable-assets design, enforced here as a lint.)
  2. JSON / JSONL validity — every `.json` parses; every non-blank `.jsonl` line parses.
  3. Skill contract presence — every `skill.*` creation carries `toolspec.json`,
     `core/interface.schema.json`, and declares an `effects` class.
  4. Lifecycle — every creation `_meta.json` and every `*.pattern.json` carries a valid
     `status` (incubating | active | deprecated | retired); `deprecated` requires
     `superseded_by`. Packs, charters and frontier policies carry a `> Status:` line in
     their markdown; lessons carry a dated `**Valid at.**` line (invalidated, never deleted).

Durability: stdlib-only, path-relative. Run in CI or before any commit.
Usage: python3 scripts/validate.py   (from anywhere)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CREATIONS = ROOT / "creations"

# Words that couple an asset to a runtime/model/framework — banned under core/.
NEUTRALITY = re.compile(
    r"\b(pi|seed|claude|gpt|gpt-\d|gemini|opus|sonnet|haiku|anthropic|openai|"
    r"langgraph|langchain|crewai|autogen|composio|letta|mem0|"
    r"terraform|kubernetes|docker|aws|gcp|azure|nginx|redis|postgres|weaviate)\b",
    re.IGNORECASE,
)


def check_neutrality():
    findings = []
    for core in CREATIONS.glob("*/core"):
        for f in core.rglob("*"):
            if not f.is_file():
                continue
            for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
                for m in NEUTRALITY.finditer(line):
                    findings.append(f"{f.relative_to(ROOT)}:{i}: banned '{m.group(0)}' under core/")
    return findings


def check_json():
    findings = []
    for p in ROOT.rglob("*.json"):
        if ".git" in p.parts:
            continue
        try:
            json.loads(p.read_text())
        except Exception as e:
            findings.append(f"{p.relative_to(ROOT)}: invalid JSON: {e}")
    for p in ROOT.rglob("*.jsonl"):
        if ".git" in p.parts:
            continue
        for i, line in enumerate(p.read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
            except Exception as e:
                findings.append(f"{p.relative_to(ROOT)}:{i}: invalid JSONL: {e}")
    return findings


def check_skill_contracts():
    findings = []
    for d in CREATIONS.glob("skill.*"):
        if not d.is_dir():
            continue
        rel = d.relative_to(ROOT)
        if not (d / "toolspec.json").exists():
            findings.append(f"{rel}: missing toolspec.json")
        if not (d / "core" / "interface.schema.json").exists():
            findings.append(f"{rel}: missing core/interface.schema.json")
        ts = d / "toolspec.json"
        if ts.exists():
            try:
                if "effects" not in json.loads(ts.read_text()):
                    findings.append(f"{rel}: toolspec.json declares no effects class")
            except Exception:
                pass  # JSON validity already reported above
    return findings


VALID_STATUS = {"incubating", "active", "deprecated", "retired"}
STATUS_LINE = re.compile(r"^> Status: ([a-z-]+)(.*)$", re.M)


def check_lifecycle():
    findings = []

    def check_status_obj(rel, data):
        s = data.get("status")
        if s not in VALID_STATUS:
            findings.append(f"{rel}: status '{s}' not in {sorted(VALID_STATUS)}")
        elif s == "deprecated" and not data.get("superseded_by"):
            findings.append(f"{rel}: deprecated without superseded_by")

    for d in sorted(CREATIONS.iterdir()):
        meta_p = d / "_meta.json"
        if d.is_dir() and meta_p.exists():
            try:
                check_status_obj(meta_p.relative_to(ROOT), json.loads(meta_p.read_text()))
            except Exception:
                pass  # JSON validity already reported above

    for f in sorted((ROOT / "templates" / "patterns").glob("*.pattern.json")):
        try:
            check_status_obj(f.relative_to(ROOT), json.loads(f.read_text()))
        except Exception:
            pass

    md_assets = (list((ROOT / "templates" / "context-packs").glob("*/pack.md"))
                 + list((ROOT / "templates" / "charters").glob("*.md"))
                 + list((ROOT / "templates" / "frontier-policies").glob("*.md")))
    for f in sorted(md_assets):
        rel = f.relative_to(ROOT)
        m = STATUS_LINE.search(f.read_text(errors="ignore"))
        if not m:
            findings.append(f"{rel}: missing '> Status:' line")
        elif m.group(1) not in VALID_STATUS:
            findings.append(f"{rel}: status '{m.group(1)}' not in {sorted(VALID_STATUS)}")
        elif m.group(1) == "deprecated" and "superseded by" not in m.group(2):
            findings.append(f"{rel}: deprecated without 'superseded by <ref>' on the Status line")

    for f in sorted((ROOT / "lessons").glob("*.md")):
        if "**Valid at.**" not in f.read_text(errors="ignore"):
            findings.append(f"{f.relative_to(ROOT)}: missing dated '**Valid at.**' line")

    return findings


def main():
    groups = {
        "core-neutrality": check_neutrality(),
        "json-validity": check_json(),
        "skill-contracts": check_skill_contracts(),
        "lifecycle": check_lifecycle(),
    }
    total = sum(len(v) for v in groups.values())
    for name, findings in groups.items():
        if findings:
            print(f"FAIL {name}: {len(findings)} finding(s)")
            for f in findings:
                print(f"  - {f}")
        else:
            print(f"OK   {name}")
    if total:
        print(f"\nvalidate: {total} finding(s)")
        sys.exit(1)
    print("\nvalidate: all checks passed")


if __name__ == "__main__":
    main()
