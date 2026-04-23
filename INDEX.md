# Index

Generated view of every entry in `derivations/`, grouped by classification.  Total entries: **19**.  Regenerate via `python3 scripts/build_index.py`.

## Axioms (mathematical primitives) (4)

| Entry | Status | Depends on |
|-------|--------|------------|
| [Fixed point](derivations/fixed_point.md) | active | &mdash; |
| [Integers](derivations/integers.md) | active | &mdash; |
| [Mediant](derivations/mediant.md) | active | `integers` |
| [Parabola](derivations/parabola.md) | active | &mdash; |

## Anchors (observational inputs) (2)

| Entry | Status | Depends on |
|-------|--------|------------|
| [Hubble anchor](derivations/hubble.md) | active | &mdash; |
| [Electroweak vacuum anchor](derivations/vev.md) | active | &mdash; |

## Definitions (6)

| Entry | Status | Depends on |
|-------|--------|------------|
| [Arnold tongue](derivations/arnold_tongue.md) | active | `circle_map`, `parabola`, `farey_sequence` |
| [Circle map](derivations/circle_map.md) | active | `integers`, `fixed_point` |
| [Farey sequence](derivations/farey_sequence.md) | active | `integers`, `mediant`, `stern_brocot` |
| [Klein bottle](derivations/klein_bottle.md) | active | `integers`, `fixed_point`, `three_dimensions` |
| [Rational field equation](derivations/rational_field_equation.md) | active | `integers`, `fixed_point`, `stern_brocot`, `arnold_tongue` |
| [Stern-Brocot tree](derivations/stern_brocot.md) | active | `integers`, `mediant` |

## Theorems (7)

| Entry | Status | Depends on |
|-------|--------|------------|
| [Continuum limits](derivations/continuum_limits.md) | active | `circle_map`, `rational_field_equation`, `fixed_point` |
| [Duty function](derivations/duty_function.md) | active | `circle_map`, `arnold_tongue`, `farey_sequence`, `three_dimensions` |
| [Farey partition](derivations/farey_partition.md) | active | `farey_sequence`, `klein_bottle` |
| [Hierarchy](derivations/hierarchy.md) | active | `klein_bottle`, `farey_partition`, `three_dimensions`, `hubble` |
| [Lie group characterization](derivations/lie_group_characterization.md) | active | `mediant`, `three_dimensions` |
| [Minkowski signature](derivations/minkowski_signature.md) | active | `three_dimensions`, `klein_bottle`, `lie_group_characterization` |
| [Three dimensions](derivations/three_dimensions.md) | active | `integers`, `mediant`, `fixed_point` |

