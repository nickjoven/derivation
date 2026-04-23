# CLAUDE.md

Authoring rules for `derivation/`.  This repo is a textbook, not a lab
notebook.  The filter below is strict by design.

## Filter

**If it wouldn't be taught, it doesn't go here.**

Before adding content, ask:

1. Is there a named conclusion this entry establishes, with a proof
   or a named citation?  If no — not yet.
2. Does it depend only on other entries in this repo (or explicit
   external citations)?  If it depends on a lab-notebook fragment
   elsewhere — first port that fragment here as its own entry, or
   inline it.
3. Is there any retracted / fitted / coincidental claim in the draft?
   Remove it before commit.  Retractions belong in the source repos'
   git history, not in this textbook.
4. Does the entry have a classification and a status in frontmatter?
   If no — assign both before commit.

An entry that passes all four is teachable.  If any fail, reshape or
archive.

## Frontmatter schema

Every file in `derivations/` starts with:

```yaml
---
kind: axiom_primitive
    | amplitude_anchor
    | topology_commitment
    | identification
    | phase_label
    | universal_constant
    | definition
    | lemma
    | theorem
    | proof
    | prediction
    | open_question
status: active | conjecture | archived
input_types: [1, 3, 4]            # which of the six input types this
                                  # entry consumes (see inputs_taxonomy.md).
                                  # Empty list means pure mathematics —
                                  # no physical input consumed.
depends_on: [file_a, file_b]      # other entries, by stem (no .md)
consequences: [file_c]            # optional reverse pointer
observables:                      # present iff kind == prediction
  - name: <name>
    predicted: <value or expression>
    observed: <value ± error>
    residual: <string>
citations:                        # external references (optional)
  - <arxiv id, DOI, or canonical URL>
---
```

### Kinds

Six kinds for *inputs* to the framework (see
[`derivations/inputs_taxonomy.md`](derivations/inputs_taxonomy.md)):

| Kind | Input type | Role |
|------|------------|------|
| `axiom_primitive` | (pre-type) | Mathematical primitive: integers, mediant, fixed-point, parabola.  Not a physical input; foundational math. |
| `amplitude_anchor` | 1 | Observational scale anchor: `hubble`, `vev`.  Two total. |
| `topology_commitment` | 3 | Ontological commitment: which mathematical object the substrate is (Klein quotient vs torus vs …). |
| `identification` | 4 | Sector-to-mode assignment: which physical observable corresponds to which mode class. |
| `phase_label` | 5 | Parity, torsion, orientation labels on the topology. |
| `universal_constant` | 6 | Inherited from universal dynamics (KAM, golden torus): $\varphi$, $\sqrt 5$, $\delta_\text{MacKay}$, $\lambda_\text{unlock}$. |

Six kinds for *derived content*:

| Kind | Role |
|------|------|
| `definition` | Named mathematical object used by later entries. |
| `lemma` | Intermediate result used in proofs. |
| `theorem` | Result with a named structural or physical consequence. |
| `proof` | End-to-end chain assembling lemmas and theorems into a major claim. |
| `prediction` | Theorem whose value matches observation to a stated residual. |
| `open_question` | Framed problem with no current solution.  Must name its resolution criterion. |

Frontmatter is machine-readable: `scripts/build_index.py` and
`scripts/build_manifest.py` both parse it.  A typo in frontmatter will
produce a validation error; the generators do not silently fix.

## Adding a new entry

1. Write `derivations/<stem>.md` with frontmatter and the body (see
   `derivations/three_dimensions.md` for the canonical example).
2. Run `python3 scripts/build_index.py` — refreshes `INDEX.md`.
3. If the entry is a `prediction` or changes anchors/primitives, run
   `python3 scripts/build_manifest.py` — refreshes `MANIFEST.yml`.
4. Commit all three together: the new entry, `INDEX.md`, `MANIFEST.yml`.

## Source-chain integrity

- Every `theorem`, `proof`, and `prediction` must trace by
  `depends_on` back to the axiomatic roots
  (`integers`, `mediant`, `fixed_point`, `parabola`) or anchor
  entries (`hubble`, `vev`).
- `open_question` entries do *not* need a closed chain, but must
  state their resolution criterion in a dedicated section.
- Circular deps are rejected by the index builder.

## Input-type crossings

Every derivation declares, in `input_types`, which of the six
meta-types it consumes.  If an entry's `input_types` is a strict
*superset* of the union of its dependencies' `input_types`, the
entry is introducing a new input — it must name the mechanism
(a `topology_commitment`, `identification`, `phase_label`, or
`amplitude_anchor` entry) that supplies the new input.  Algebraic
manipulation alone does not introduce a new input type.

This is the formalization of the rule that the
[inputs taxonomy](derivations/inputs_taxonomy.md) makes explicit:
pitch (Type 2) cannot be derived from other pitches;  amplitude
(Type 1) cannot be derived from pitches or scores.  Type-crossings
need named mechanisms.

## Substrate

`.ket/` will be seeded with the current canonical state once the
port is stable.  The forward-carrying substrate uses BLAKE3 CIDs,
per the `ket` binary at `/home/njoven/AI/sandbox/ket/target/release/ket`.
Cross-repo references into legacy `harmonics` / `proslambenomenos`
content go via `ket import` of foreign-CID bundles, not by
duplication of text.

## Style

- Dry prose.  No "this is remarkable," no "strikingly."  If a result
  is significant, the reader can tell from the derivation.
- One theorem per file.  One proof chain per `proof_*.md`.
- Inline math via `$…$`, display via `$$…$$`.  KaTeX renders both
  on the Pages deploy.
- No em dashes.  Avoid ambiguity between structural dashes and
  prose punctuation.
- No narrative filler at the top of a file.  The first substantive
  content after frontmatter is `## Statement` (for theorems) or
  `## Definition` (for definitions) or `## Axiom` (for primitives).
