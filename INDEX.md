# Index

Generated view of every entry in `derivations/`, grouped by classification.  Total entries: **23**.  Regenerate via `python3 scripts/build_index.py`.

## Axiomatic primitives (mathematical) (4)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Fixed point](derivations/fixed_point.md) | active | &mdash; | &mdash; |
| [Integers](derivations/integers.md) | active | &mdash; | &mdash; |
| [Mediant](derivations/mediant.md) | active | &mdash; | `integers` |
| [Parabola](derivations/parabola.md) | active | &mdash; | &mdash; |

## Amplitude anchors (Type 1, observational) (2)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Hubble anchor](derivations/hubble.md) | active | &mdash; | &mdash; |
| [Electroweak vacuum anchor](derivations/vev.md) | active | &mdash; | &mdash; |

## Topology commitments (Type 3) (1)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [SL(2, R) manifold commitment](derivations/sl2r_manifold.md) | active | 3 | `three_dimensions`, `lie_group_characterization` |

## Definitions (7)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Arnold tongue](derivations/arnold_tongue.md) | active | &mdash; | `circle_map`, `parabola`, `farey_sequence` |
| [Circle map](derivations/circle_map.md) | active | &mdash; | `integers`, `fixed_point` |
| [Farey sequence](derivations/farey_sequence.md) | active | &mdash; | `integers`, `mediant`, `stern_brocot` |
| [Inputs taxonomy](derivations/inputs_taxonomy.md) | active | &mdash; | &mdash; |
| [Klein bottle](derivations/klein_bottle.md) | active | &mdash; | `integers`, `fixed_point`, `three_dimensions` |
| [Rational field equation](derivations/rational_field_equation.md) | active | &mdash; | `integers`, `fixed_point`, `stern_brocot`, `arnold_tongue` |
| [Stern-Brocot tree](derivations/stern_brocot.md) | active | &mdash; | `integers`, `mediant` |

## Theorems (7)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Continuum limits](derivations/continuum_limits.md) | active | &mdash; | `circle_map`, `rational_field_equation`, `fixed_point` |
| [Duty function](derivations/duty_function.md) | active | &mdash; | `circle_map`, `arnold_tongue`, `farey_sequence`, `three_dimensions` |
| [Farey partition](derivations/farey_partition.md) | active | 3 | `farey_sequence`, `klein_bottle` |
| [Hierarchy](derivations/hierarchy.md) | active | 1, 3 | `klein_bottle`, `farey_partition`, `three_dimensions`, `hubble` |
| [Lie group characterization](derivations/lie_group_characterization.md) | active | &mdash; | `mediant`, `three_dimensions` |
| [Minkowski signature](derivations/minkowski_signature.md) | active | &mdash; | `three_dimensions`, `klein_bottle`, `lie_group_characterization` |
| [Three dimensions](derivations/three_dimensions.md) | active | &mdash; | `integers`, `mediant`, `fixed_point` |

## Proof chains (2)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Proof A: primitives to the Einstein field equations](derivations/proof_A_gravity.md) | active | 3 | `integers`, `mediant`, `fixed_point`, `parabola`, `circle_map`, `stern_brocot`, `arnold_tongue`, `rational_field_equation`, `continuum_limits`, `three_dimensions`, `lie_group_characterization`, `minkowski_signature`, `sl2r_manifold` |
| [Proof B: primitives to the Schrödinger equation and the Born rule](derivations/proof_B_quantum.md) | active | 3 | `integers`, `mediant`, `fixed_point`, `parabola`, `circle_map`, `stern_brocot`, `arnold_tongue`, `rational_field_equation`, `continuum_limits`, `three_dimensions`, `lie_group_characterization`, `sl2r_manifold`, `proof_A_gravity` |

