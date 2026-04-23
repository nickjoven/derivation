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
  kind (axiom, anchor, definition, lemma, theorem, proof, prediction,
  open question).  Regenerate via `python3 scripts/build_index.py`.
- [`MANIFEST.yml`](MANIFEST.yml) — generated aggregate: dimensional
  anchors, axiomatic primitives, predictions with observables, open
  questions.  Regenerate via `python3 scripts/build_manifest.py`.

## Recommended reading order

The material is layered.  A new reader should traverse it in this
order:

1. **Axioms (4).**  The irreducible primitives.
   [`integers`](derivations/integers.md),
   [`mediant`](derivations/mediant.md),
   [`fixed_point`](derivations/fixed_point.md),
   [`parabola`](derivations/parabola.md).
2. **Anchors (2).**  The observational inputs, one per sector.
   [`hubble`](derivations/hubble.md) (cosmological),
   [`vev`](derivations/vev.md) (particle).
3. **Definitions.**  Named mathematical objects built from the axioms:
   [`circle_map`](derivations/circle_map.md),
   [`stern_brocot`](derivations/stern_brocot.md),
   [`farey_sequence`](derivations/farey_sequence.md),
   [`arnold_tongue`](derivations/arnold_tongue.md),
   [`klein_bottle`](derivations/klein_bottle.md),
   [`rational_field_equation`](derivations/rational_field_equation.md).
4. **Theorems.**  Results with structural consequence:
   [`three_dimensions`](derivations/three_dimensions.md),
   [`lie_group_characterization`](derivations/lie_group_characterization.md),
   [`minkowski_signature`](derivations/minkowski_signature.md),
   [`continuum_limits`](derivations/continuum_limits.md),
   [`duty_function`](derivations/duty_function.md),
   [`farey_partition`](derivations/farey_partition.md),
   [`hierarchy`](derivations/hierarchy.md).
5. **Proof chains.**  End-to-end: primitives → Einstein, primitives →
   Schrödinger, anchors → cosmological observables.  (Pending port.)
6. **Predictions.**  Verified theorems matching observation to a
   stated residual.  (Pending port.)
7. **Open questions.**  Framed problems with explicit resolution
   criteria.  (Pending port.)

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
