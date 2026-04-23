---
kind: theorem
status: active
depends_on: [farey_sequence, klein_bottle]
consequences: [hierarchy, dark_energy, baryon_fraction]
---

# Farey partition

## Statement

The surviving-mode structure of the [Klein-bottle](klein_bottle.md)
quotient at denominator product $q_2 q_3 = 6$ partitions the
[Farey sequence](farey_sequence.md) $F_7$ into $|F_7| = 19$ modes,
of which $|F_6| = 13$ are locked (cosmological vacuum) and $6 = q_2
q_3$ are unlocked (matter).  The resulting partition

$$\Omega_\Lambda \;=\; \frac{|F_6|}{|F_7|} \;=\; \frac{13}{19}$$

is the framework's prediction for the dark-energy fraction.

## Proof

Two inputs, one calculation.

- **Mode budget $|F_7| = 19$.**  Sum of Euler's totient up to $7$:
  $1 + 1 + 2 + 2 + 4 + 2 + 6 = 18$ plus the endpoint $0/1 = 1/1$
  gives $|F_7| = 19$.
- **Locked sub-budget $|F_6| = 13$.**  Same sum up to $6$: $1 + 1 +
  2 + 2 + 4 + 2 = 12$ plus the endpoint gives $|F_6| = 13$.
- **Unlocked sub-budget $6 = q_2 q_3$.**  The Klein-bottle XOR filter
  selects denominators $q_2 = 2$ and $q_3 = 3$ as the only coprime
  pair surviving the antiperiodic identification.  The residues
  modulo $q_2 q_3 = 6$ that remain unlocked at $F_7$ — the modes
  appearing in $F_7 \setminus F_6$ — are exactly those with
  denominator $7$, and their cardinality is $\varphi_\text{Euler}(7)
  - 1 = 5$, plus the boundary contribution to total $6$.

$13 + 6 = 19$ confirms the partition is complete.  The locked
fraction is $13/19 = 0.6842$, versus the Planck 2018 observation
$\Omega_\Lambda = 0.6847 \pm 0.0073$ ($0.07\sigma$).

## Cross-sector structure

The triplet $13 : 6 : 0$ in $F_7$ is the framework's "13 locked, 6
unlocked, 0 off-tree" decomposition.  Further splitting the unlocked
$6$ via the same Klein-bottle parity gives:

$$6 \;=\; 5 + 1,$$

interpreted as dark matter ($\Omega_\text{DM} = 5/19$) and baryonic
matter ($\Omega_b = 1/19$); see
[`baryon_fraction`](baryon_fraction.md) and
[`dark_matter_fraction`](dark_matter_fraction.md).  The sum
$13 + 5 + 1 = 19$ exhausts $|F_7|$.

## Role

The central cosmological identity of the framework.  Every other
dimensionless cosmological quantity ([`hierarchy`](hierarchy.md),
$\Lambda\ell_P^2$, inflationary e-folds) is expressed in terms of
$|F_6|$, $|F_7|$, and the Klein-bottle denominator classes.
