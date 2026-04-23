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
        "input_types": meta.get("input_types", []) or [],
        "depends_on": meta.get("depends_on", []) or [],
        "observables": meta.get("observables") or [],
        "citations": meta.get("citations") or [],
    }


def _by_kind(entries: list[dict], kind: str) -> list[dict]:
    return sorted(
        (e for e in entries if e["kind"] == kind), key=lambda e: e["stem"]
    )


def main() -> int:
    if not DERIV_DIR.exists():
        print(f"error: {DERIV_DIR} not found", file=sys.stderr)
        return 2
    paths = sorted(DERIV_DIR.glob("*.md"))
    if not paths:
        print(f"error: no .md files in {DERIV_DIR}", file=sys.stderr)
        return 2

    entries = [parse_entry(p) for p in paths]

    primitives = _by_kind(entries, "axiom_primitive")
    anchors = _by_kind(entries, "amplitude_anchor")
    topology = _by_kind(entries, "topology_commitment")
    identifications = _by_kind(entries, "identification")
    phase_labels = _by_kind(entries, "phase_label")
    universal = _by_kind(entries, "universal_constant")
    predictions = _by_kind(entries, "prediction")
    open_questions = _by_kind(entries, "open_question")

    # Counts of entries that consume each input type (1..6)
    consumers: dict[int, list[str]] = {}
    for e in entries:
        for t in e["input_types"]:
            consumers.setdefault(t, []).append(e["stem"])
    consumers_summary = {
        f"type_{t}": sorted(consumers.get(t, [])) for t in range(1, 7)
    }

    def _short(e: dict) -> dict:
        return {"stem": e["stem"], "title": e["title"]}

    manifest = {
        "generated_by": "scripts/build_manifest.py",
        "entries_scanned": len(entries),
        "free_parameters": 0,
        "free_functions": 0,
        "inputs": {
            "dimensionful_anchors_count": len(anchors),
            "topology_commitments_count": len(topology),
            "identification_maps_count": len(identifications),
            "phase_labels_count": len(phase_labels),
            "universal_constants_count": len(universal),
            "axiom_primitives_count": len(primitives),
        },
        "anchors": [_short(a) for a in anchors],
        "topology_commitments": [_short(t) for t in topology],
        "identifications": [_short(i) for i in identifications],
        "phase_labels": [_short(p) for p in phase_labels],
        "universal_constants": [_short(u) for u in universal],
        "primitives": [_short(p) for p in primitives],
        "predictions": [
            {
                "stem": p["stem"],
                "title": p["title"],
                "input_types": p["input_types"],
                "observables": p["observables"],
            }
            for p in predictions
        ],
        "open_questions": [_short(q) for q in open_questions],
        "input_type_consumers": consumers_summary,
    }

    header = (
        "# MANIFEST.yml\n"
        "# Generated from derivations/*.md frontmatter.  Do not edit by hand --\n"
        "# edit the source entries and re-run scripts/build_manifest.py.\n"
        "# For the taxonomy of input types, see derivations/inputs_taxonomy.md.\n\n"
    )
    OUT_PATH.write_text(header + yaml.safe_dump(manifest, sort_keys=False))
    print(
        f"Wrote {OUT_PATH}: "
        f"{len(anchors)} anchors, {len(primitives)} primitives, "
        f"{len(topology)} topology, {len(identifications)} identifications, "
        f"{len(predictions)} predictions, {len(open_questions)} open questions"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
