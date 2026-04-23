# Index

Generated view of every entry in `derivations/`, grouped by classification.  Total entries: **46**.  Regenerate via `python3 scripts/build_index.py`.

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

## Topology commitments (Type 3) (2)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Klein-quotient substrate commitment](derivations/klein_substrate.md) | active | 3 | `klein_bottle`, `sl2r_manifold` |
| [SL(2, R) manifold commitment](derivations/sl2r_manifold.md) | active | 3 | `three_dimensions`, `lie_group_characterization` |

## Identification maps (Type 4) (1)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Gauge-sector identification](derivations/gauge_identification.md) | active | 4 | `klein_substrate`, `klein_bottle`, `farey_partition`, `sl2r_manifold` |

## Universal constants (Type 6, inherited) (1)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Golden ratio](derivations/golden_ratio.md) | active | 6 | &mdash; |

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

## Theorems (9)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Continuum limits](derivations/continuum_limits.md) | active | &mdash; | `circle_map`, `rational_field_equation`, `fixed_point` |
| [Duty function](derivations/duty_function.md) | active | &mdash; | `circle_map`, `arnold_tongue`, `farey_sequence`, `three_dimensions` |
| [Farey partition](derivations/farey_partition.md) | active | 3 | `farey_sequence`, `klein_bottle`, `klein_substrate` |
| [Gell-Mann–Nishijima relation from the Klein boundary](derivations/gell_mann_nishijima.md) | active | 3, 4 | `klein_bottle`, `klein_substrate`, `gauge_identification` |
| [Hierarchy](derivations/hierarchy.md) | active | 1, 3 | `klein_bottle`, `klein_substrate`, `farey_partition`, `three_dimensions`, `hubble` |
| [Lie group characterization](derivations/lie_group_characterization.md) | active | &mdash; | `mediant`, `three_dimensions` |
| [Minkowski signature](derivations/minkowski_signature.md) | active | &mdash; | `three_dimensions`, `klein_bottle`, `lie_group_characterization` |
| [Three dimensions](derivations/three_dimensions.md) | active | &mdash; | `integers`, `mediant`, `fixed_point` |
| [Yang-Mills dynamics from Utiyama uniqueness](derivations/yang_mills.md) | active | 3, 4 | `gauge_group`, `gauge_identification`, `klein_substrate`, `minkowski_signature`, `three_dimensions` |

## Proof chains (3)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Proof A: primitives to the Einstein field equations](derivations/proof_A_gravity.md) | active | 3 | `integers`, `mediant`, `fixed_point`, `parabola`, `circle_map`, `stern_brocot`, `arnold_tongue`, `rational_field_equation`, `continuum_limits`, `three_dimensions`, `lie_group_characterization`, `minkowski_signature`, `sl2r_manifold` |
| [Proof B: primitives to the Schrödinger equation and the Born rule](derivations/proof_B_quantum.md) | active | 3 | `integers`, `mediant`, `fixed_point`, `parabola`, `circle_map`, `stern_brocot`, `arnold_tongue`, `rational_field_equation`, `continuum_limits`, `three_dimensions`, `lie_group_characterization`, `sl2r_manifold`, `proof_A_gravity` |
| [Proof C: the bridge](derivations/proof_C_bridge.md) | active | 1, 3, 6 | `integers`, `mediant`, `fixed_point`, `parabola`, `circle_map`, `stern_brocot`, `farey_sequence`, `arnold_tongue`, `rational_field_equation`, `continuum_limits`, `three_dimensions`, `lie_group_characterization`, `klein_bottle`, `hubble`, `sl2r_manifold`, `klein_substrate`, `golden_ratio`, `farey_partition`, `hierarchy`, `dark_energy`, `mond_scale`, `proof_A_gravity` |

## Predictions (13)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Anomaly cancellation](derivations/anomaly_cancellation.md) | active | 3, 4 | `klein_substrate`, `gauge_identification`, `gell_mann_nishijima`, `gauge_group` |
| [Baryon fraction](derivations/baryon_fraction.md) | active | 3, 4 | `klein_substrate`, `klein_bottle`, `farey_partition`, `gell_mann_nishijima` |
| [Born rule](derivations/born_rule.md) | active | 3 | `parabola`, `arnold_tongue`, `proof_B_quantum` |
| [Dark-energy fraction](derivations/dark_energy.md) | active | 3 | `klein_substrate`, `farey_partition`, `farey_sequence` |
| [Dark-matter fraction](derivations/dark_matter_fraction.md) | active | 3, 4 | `klein_substrate`, `klein_bottle`, `farey_partition`, `gell_mann_nishijima` |
| [Dark-matter to baryon ratio](derivations/dm_baryon_ratio.md) | active | 3 | `dark_matter_fraction`, `baryon_fraction`, `klein_substrate`, `farey_partition` |
| [Standard Model gauge group](derivations/gauge_group.md) | active | 3, 4 | `klein_substrate`, `gauge_identification`, `klein_bottle` |
| [Planck-to-Hubble hierarchy](derivations/hierarchy_ratio.md) | active | 1, 3 | `hierarchy`, `klein_substrate`, `farey_partition`, `hubble`, `three_dimensions` |
| [Lorentz symmetry](derivations/lorentz_symmetry.md) | active | 3 | `three_dimensions`, `minkowski_signature`, `sl2r_manifold`, `lie_group_characterization` |
| [MOND acceleration scale](derivations/mond_scale.md) | active | 1, 3, 6 | `hubble`, `klein_substrate`, `farey_partition`, `hierarchy`, `golden_ratio`, `rational_field_equation`, `continuum_limits` |
| [Spatial dimension](derivations/spatial_dimension.md) | active | 3 | `three_dimensions`, `sl2r_manifold`, `lie_group_characterization` |
| [Heisenberg uncertainty](derivations/uncertainty.md) | active | 3 | `proof_B_quantum`, `continuum_limits`, `rational_field_equation`, `parabola` |
| [Vacuum energy](derivations/vacuum_energy.md) | active | 1, 3 | `hierarchy`, `hierarchy_ratio`, `farey_partition`, `hubble`, `klein_substrate` |

## Open questions (4)

| Entry | Status | Input types | Depends on |
|-------|--------|-------------|------------|
| [Anchor audit](derivations/anchor_audit.md) | `conjecture` | 1 | `hubble`, `vev`, `inputs_taxonomy` |
| [Cosmological-sector identification for the {5, 1} orbits](derivations/baryon_sector_identification.md) | `conjecture` | 4 | `farey_partition`, `klein_substrate`, `baryon_fraction`, `dark_matter_fraction`, `gauge_identification` |
| [Can the topology commitments be forced?](derivations/topology_forcing.md) | `conjecture` | 3 | `sl2r_manifold`, `klein_substrate`, `inputs_taxonomy` |
| [The electroweak-to-Planck gap](derivations/v_over_MP_gap.md) | `conjecture` | 1 | `hubble`, `vev`, `hierarchy`, `hierarchy_ratio` |

