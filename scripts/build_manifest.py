"""
build_manifest.py

Scan derivations/*.md, parse the YAML frontmatter, emit MANIFEST.yml
as a machine-readable aggregate: anchors, axiomatic primitives, the
prediction scorecard with observables, and open questions.

Usage:
    python3 scripts/build_manifest.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DERIV_DIR = ROOT / "derivations"
OUT_PATH = ROOT / "MANIFEST.yml"


FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


# Stems that count as observational anchors (vs mathematical axioms).
# These are the only entries whose `kind == axiom` represents a
# dimensional input rather than a mathematical primitive.
ANCHOR_STEMS = {"hubble", "vev"}


def parse_entry(path: Path) -> dict:
    text = path.read_text()
    m = FM_RE.match(text)
    if not m:
        raise ValueError(f"{path}: missing frontmatter")
    meta = yaml.safe_load(m.group(1)) or {}
    title_m = H1_RE.search(text, m.end())
    title = title_m.group(1).strip() if title_m else path.stem
    return {
        "stem": path.stem,
        "title": title,
        "kind": meta.get("kind", "unclassified"),
        "status": meta.get("status", "active"),
        "depends_on": meta.get("depends_on", []) or [],
        "observables": meta.get("observables") or [],
        "citations": meta.get("citations") or [],
    }


def main() -> int:
    if not DERIV_DIR.exists():
        print(f"error: {DERIV_DIR} not found", file=sys.stderr)
        return 2
    paths = sorted(DERIV_DIR.glob("*.md"))
    if not paths:
        print(f"error: no .md files in {DERIV_DIR}", file=sys.stderr)
        return 2

    entries = [parse_entry(p) for p in paths]

    anchors = [e for e in entries if e["kind"] == "axiom" and e["stem"] in ANCHOR_STEMS]
    primitives = [
        e for e in entries if e["kind"] == "axiom" and e["stem"] not in ANCHOR_STEMS
    ]
    predictions = [e for e in entries if e["kind"] == "prediction"]
    open_questions = [e for e in entries if e["kind"] == "open_question"]

    manifest = {
        "generated_by": "scripts/build_manifest.py",
        "entries_scanned": len(entries),
        "free_parameters": 0,
        "free_functions": 0,
        "dimensionful_inputs": len(anchors),
        "anchors": [
            {"stem": a["stem"], "title": a["title"]}
            for a in sorted(anchors, key=lambda e: e["stem"])
        ],
        "primitives": [
            {"stem": p["stem"], "title": p["title"]}
            for p in sorted(primitives, key=lambda e: e["stem"])
        ],
        "predictions": [
            {
                "stem": p["stem"],
                "title": p["title"],
                "observables": p["observables"],
            }
            for p in sorted(predictions, key=lambda e: e["stem"])
        ],
        "open_questions": [
            {"stem": q["stem"], "title": q["title"]}
            for q in sorted(open_questions, key=lambda e: e["stem"])
        ],
    }

    header = (
        "# MANIFEST.yml\n"
        "# Generated from derivations/*.md frontmatter.  Do not edit by hand —\n"
        "# edit the source entries and re-run scripts/build_manifest.py.\n\n"
    )
    OUT_PATH.write_text(header + yaml.safe_dump(manifest, sort_keys=False))
    print(
        f"Wrote {OUT_PATH}: "
        f"{len(anchors)} anchors, {len(primitives)} primitives, "
        f"{len(predictions)} predictions, {len(open_questions)} open questions"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
