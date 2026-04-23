---
kind: identification
status: active
input_types: [4]
depends_on: [klein_substrate, klein_bottle, farey_partition, sl2r_manifold]
consequences: [gauge_group, gell_mann_nishijima, anomaly_cancellation]
---

# Gauge-sector identification

## Commitment

The [`klein_substrate`](klein_substrate.md)'s surviving-mode
structure is identified with the Standard Model's gauge and matter
content by the following assignments:

| Klein-substrate feature | Physical sector |
|-------------------------|-----------------|
| Antiperiodic direction (x, half-twist of order 2) | Weak isospin $\mathrm{SU}(2)_L$ |
| Periodic direction (y, $\mathrm{U}(1)$ isometry) | Hypercharge $\mathrm{U}(1)_Y$ |
| Denominator class $q_3 = 3$ | Color $\mathrm{SU}(3)$ |
| Half-twist eigenvalues $\pm 1/2$ | Weak isospin $T_3 = \pm 1/2$ doublet |
| Reflection $y \mapsto 1 - y$ (order 2) | Generates $Y / 2$ at the identification boundary |
| Surviving fractions $\{1/3, 1/2, 2/3\}$ | Electric-charge magnitudes |

The assignments are *partial*: the Klein topology forces the
denominator classes $q_2 = 2$ and $q_3 = 3$ and fixes the
surviving-mode table.  Which physical sector maps to each feature
is the framework's free content at this level.

## Forced vs free

**Forced by [`klein_substrate`](klein_substrate.md):**

- The structure-group center is $\mathbb{Z}_2 \times \mathbb{Z}_3$,
  realized as a direct product (not cyclic $\mathbb{Z}_6$), because
  the Klein XOR separates the two denominator classes into
  independent GCD-residue classes.
- The surviving fractions are $\{1/3, 1/2, 2/3\}$.
- The antiperiodic direction carries a $\mathbb{Z}_2$ twist of
  order 2; the periodic direction carries a $\mathrm{U}(1)$
  isometry.

**Free (this entry's content):**

- The antiperiodic direction is identified with the weak isospin
  sector rather than (say) color or a hidden gauge factor.
- The periodic direction is identified with hypercharge rather
  than with, e.g., $B - L$ or a spectator $\mathrm{U}(1)$.
- $q_3 = 3$ is identified with color $\mathrm{SU}(3)$ rather than
  (say) generation index.

## Consequences

Under the assignments above:

- The Standard Model gauge group is
  $\mathrm{SU}(3) \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$.
  See [`gauge_group`](gauge_group.md) for the prediction statement
  and uniqueness (Cartan 1894 + rank argument +
  anomaly-cancellation check).
- The Gell-Mann–Nishijima relation
  $Q = T_3 + Y / 2$ follows from the Klein-bottle identification
  boundary; the $1 / 2$ is the order of the $y \mapsto 1 - y$
  reflection.  See [`gell_mann_nishijima`](gell_mann_nishijima.md).
- All six Standard Model triangle anomalies cancel within each
  generation.  See [`anomaly_cancellation`](anomaly_cancellation.md).

## Alternative identifications (distinguishable, rejected)

- **$q_2 \leftrightarrow \mathrm{SU}(3)$, $q_3 \leftrightarrow
  \mathrm{SU}(2)_L$.**  Fails Cartan's classification of centers:
  $\mathrm{SU}(3)$'s center is $\mathbb{Z}_3$ and
  $\mathrm{SU}(2)$'s is $\mathbb{Z}_2$, so swapping the
  assignments swaps the centers and breaks the match.
- **Periodic direction $\leftrightarrow$ color.**  Inconsistent with
  color confinement: the periodic direction is unbroken at all
  scales, while color confines; the topology is continuous and the
  physics is confining, which is the opposite.
- **Swapping $Y$ and $T_3$.**  Fails the $Q = T_3 + Y / 2$ relation:
  the reflection's order-2 action fixes the factor $1/2$ on the
  reflection-charged variable, not on the half-twist eigenvalue.

The rejections are structural.

## Running count of framework inputs

Before this entry: 2 amplitudes (Type 1: Hubble + vev), 2 topology
commitments (Type 3: sl2r_manifold + klein_substrate), 0
identifications, 1 universal constant (Type 6: golden_ratio).

After this entry: same plus 1 identification (Type 4).

The independent-input count is therefore $2 + 2 + 1 + 1 = 6$, of
which $6 = 2 + 2 + 1 + 1$ are the listed content (2 amplitudes, 2
topologies, 1 identification, 1 universal constant).  This is the
framework's full input budget at the current depth.

## Remarks

- The $13$-subset ↔ cosmological vacuum, $5$-subset ↔ dark matter,
  $1$-subset ↔ baryons assignments (used in
  [`dark_energy`](dark_energy.md),
  [`dark_matter_fraction`](dark_matter_fraction.md),
  [`baryon_fraction`](baryon_fraction.md)) are a *separate*
  identification.  They operate on the 19-element mode budget
  $|F_7|$, not on the gauge-denominator set $\{q_2, q_3\}$.  A
  companion identification entry for the cosmological-sector
  assignment is pending, and its absence is the reason the
  baryon-fraction residual at $\sim 5\sigma$ is flagged rather
  than resolved.
- The electroweak-to-Planck hierarchy $v / M_P$ requires a
  *third* identification (the assignment of the $\mathrm{vev}$
  anchor to the weak-sector scale).  That identification is
  implicit in the [`vev`](vev.md) anchor but not yet promoted to
  an explicit entry.
