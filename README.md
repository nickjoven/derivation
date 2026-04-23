# derivation

A textbook-style reference for the synchronization-cost framework: axioms,
definitions, theorems, proofs, and verified predictions.  Forward-carrying
resolution of the [`harmonics`](https://github.com/nickjoven/harmonics) and
[`proslambenomenos`](https://github.com/nickjoven/proslambenomenos)
repositories, filtered to what would be taught.

## What's in here

- [`derivations/`](derivations/) — every entry is a self-contained
  teaching unit with a classification frontmatter.  Read any file
  top-to-bottom and you should be able to reproduce the result.
- [`INDEX.md`](INDEX.md) — generated index grouped by classification
  kind (axiom, definition, lemma, theorem, proof, prediction, open
  question).  Regenerate via `python3 scripts/build_index.py`.
- [`MANIFEST.yml`](MANIFEST.yml) — generated aggregate: dimensional
  anchors, scorecard of verified predictions, open questions.
  Regenerate via `python3 scripts/build_manifest.py`.

## What's not in here

Content that would not appear in a graduate textbook on the framework
is excluded by editorial policy — see [`CLAUDE.md`](CLAUDE.md) §Filter.
Specifically absent:

- Retracted hypotheses and the prose documenting their retraction.
- "Fitted" corrections without scale-consistent derivation.
- Class 1/Class 3 numerology per the prior repo's audit.
- Lab-notebook exploration not in service of a stated theorem.
- Any claim whose status is "conjecture" without a named testable
  resolution criterion.

For the lineage, see the archived source repos and the
[`99_history/`](99_history/) pointer.

## Classification

Every entry declares its kind in YAML frontmatter.  Seven kinds, three
statuses.

### Kinds

| Kind | Purpose |
|------|---------|
| `axiom` | Primitive or observational anchor.  No proof — stated as given. |
| `definition` | Named mathematical object used by later entries. |
| `lemma` | Intermediate result used in proofs.  Proved in file. |
| `theorem` | Result with a named structural or physical consequence. |
| `proof` | End-to-end chain of lemmas and theorems establishing a major claim. |
| `prediction` | Theorem whose value matches observation to a stated residual. |
| `open_question` | Framed problem with no current solution.  Must name its resolution criterion. |

### Statuses

| Status | Meaning |
|--------|---------|
| `active` | Canonical; currently in use by downstream entries. |
| `conjecture` | Stated, not proved.  Requires a resolution criterion in-file. |
| `archived` | Kept for provenance only.  No longer in the derivation chain. |

## Source chain

Every file traces back to exactly one set of roots:

- **Four axiomatic primitives**: integers, mediant, fixed-point, parabola.
- **Two observational anchors**: Hubble parameter $H_0$ (cosmological
  sector), electroweak scale $v_\mathrm{EW}$ (particle sector).

Dimensional inputs are these two anchors.  Everything else is a
dimensionless theorem, a bare mathematical identity, or a prediction
that follows from the above under a named deduction.

## License

[CC0 1.0 Universal](LICENSE) — no rights reserved.
