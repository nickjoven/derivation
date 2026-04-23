"""
build_index.py

Scan derivations/*.md, parse the YAML frontmatter, emit INDEX.md
grouping entries by `kind` and tagging their `status`.

Usage:
    python3 scripts/build_index.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DERIV_DIR = ROOT / "derivations"
OUT_PATH = ROOT / "INDEX.md"

KIND_ORDER = [
    "axiom",
    "definition",
    "lemma",
    "theorem",
    "proof",
    "prediction",
    "open_question",
]

KIND_HEADINGS = {
    "axiom": "Axioms",
    "definition": "Definitions",
    "lemma": "Lemmas",
    "theorem": "Theorems",
    "proof": "Proof chains",
    "prediction": "Predictions",
    "open_question": "Open questions",
}


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
        "depends_on": meta.get("depends_on", []) or [],
        "consequences": meta.get("consequences", []) or [],
        "observables": meta.get("observables") or [],
    }


def render(entries: list[dict]) -> str:
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_kind[e["kind"]].append(e)
    for arr in by_kind.values():
        arr.sort(key=lambda e: e["stem"])

    lines = [
        "# Index",
        "",
        (
            "Generated view of every entry in `derivations/`, grouped by "
            f"classification.  Total entries: **{len(entries)}**.  Regenerate "
            "via `python3 scripts/build_index.py`."
        ),
        "",
    ]

    for kind in KIND_ORDER:
        items = by_kind.get(kind, [])
        if not items:
            continue
        heading = KIND_HEADINGS.get(kind, kind.title())
        lines.append(f"## {heading} ({len(items)})")
        lines.append("")
        lines.append("| Entry | Status | Depends on |")
        lines.append("|-------|--------|------------|")
        for e in items:
            deps = ", ".join(f"`{d}`" for d in e["depends_on"]) or "&mdash;"
            status = e["status"]
            status_cell = f"`{status}`" if status != "active" else "active"
            lines.append(
                f"| [{e['title']}](derivations/{e['stem']}.md) | {status_cell} | {deps} |"
            )
        lines.append("")

    # Catch-all for unrecognized kinds
    unknown = [k for k in by_kind if k not in KIND_ORDER]
    if unknown:
        lines.append("## Unclassified")
        lines.append("")
        for kind in sorted(unknown):
            for e in by_kind[kind]:
                lines.append(f"- `{e['stem']}` kind=`{kind}`")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    if not DERIV_DIR.exists():
        print(f"error: {DERIV_DIR} not found", file=sys.stderr)
        return 2
    paths = sorted(DERIV_DIR.glob("*.md"))
    if not paths:
        print(f"error: no .md files in {DERIV_DIR}", file=sys.stderr)
        return 2
    entries: list[dict] = []
    for p in paths:
        try:
            entries.append(parse_entry(p))
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 1
    OUT_PATH.write_text(render(entries))
    print(f"Wrote {OUT_PATH} ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
