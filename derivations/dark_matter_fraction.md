---
kind: prediction
status: active
input_types: [3, 4]
depends_on: [klein_substrate, klein_bottle, farey_partition, gell_mann_nishijima]
consequences: [dm_baryon_ratio]
observables:
  - name: Dark-matter fraction Ω_DM
    predicted: 5 / 19 ≈ 0.2632
    observed: 0.265 ± 0.007 (Planck 2018)
    residual: ~0.2σ
citations:
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
---

# Dark-matter fraction

## Statement

$$\Omega_\text{DM} \;=\; \frac{5}{19} \;\approx\; 0.2632.$$

Planck 2018 reports $\Omega_\text{DM} = 0.265 \pm 0.007$; residual
$\sim 0.2\sigma$.

## Derivation

See [`farey_partition`](farey_partition.md) §Cross-sector structure.
The unlocked budget $|F_7| - |F_6| = \varphi(7) = 6$ splits as
$6 = 5 + 1$ under a mechanism that is *not* a quotient by a
$\mathbb{Z}_2 \times \mathbb{Z}_3$ action — that framing was a
placeholder.  The correct mechanism is the Klein-antipodal
$\mathbb{Z}_2$ representation theory combined with the EM-coupling
criterion from [`gell_mann_nishijima`](gell_mann_nishijima.md).
The full tabulation lives in [`baryon_fraction`](baryon_fraction.md)
§Derivation; the summary here is sufficient for the $5 / 19$
count.

### Mechanism (summary)

The Klein bottle has torsion $H_1(K^2; \mathbb{Z}) = \mathbb{Z}
\oplus \mathbb{Z}_2$ ([`klein_bottle`](klein_bottle.md)), so the
antipodal action $p \mapsto 6 - p$ on the six $q = 7$ numerators is
a non-trivial $\mathbb{Z}_2$ representation.  Each antipodal pair
$\{\psi_p, \psi_{6-p}\}$ decomposes into:

- a **symmetric** (Klein-singlet) eigenmode, single-valued around
  the Klein loop;
- an **antisymmetric** (sign-rep) eigenmode, monodromy $-1$ around
  the loop and therefore no single-valued global phase.

A mode is **baryonic** (carries net EM coupling) iff it is
simultaneously a Klein-singlet (so the post-EWSB $\mathrm{U}(1)_
\text{em}$ generator from [`gauge_identification`](gauge_identification.md)
has a well-defined eigenvalue on it) *and* has a numerator coprime
to $6$ (so it couples to both the $q_2 = 2$ and $q_3 = 3$ sectors;
see [`gell_mann_nishijima`](gell_mann_nishijima.md)).

Exactly one of the six modes satisfies both — the symmetric
combination of the coprime pair $\{1, 5\}$.  The remaining five
fail at least one condition and are dark.  Cardinality:

$$\Omega_\text{DM} = \frac{5}{19}, \qquad \Omega_b = \frac{1}{19}.$$

### What the five dark modes are

From the table in [`baryon_fraction`](baryon_fraction.md):

1. $\psi_1 - \psi_5$ (coprime pair, antisymmetric — fails the
   Klein-singlet criterion).
2. $\psi_2 + \psi_4$ (gcd-$2$ pair, symmetric — fails the
   coprime-to-$6$ criterion, $q_3$ sector absent).
3. $\psi_2 - \psi_4$ (gcd-$2$ pair, antisymmetric — fails both).
4. $\psi_3$ (self-paired — fails coprime-to-$6$, $q_2$ sector
   absent).
5. $\psi_6 \equiv \psi_0$ (self-paired — fails coprime-to-$6$,
   trivial sector).

All five have gravitational coupling (universal, from the
energy-density-sources-frequency identification of Proof A) but
no net EM coupling.  The $5$ is not one irreducible orbit under a
single group action — it is the count of eigenmodes that fail the
baryonic criterion, four of them accidentally sharing the
"no-cross-sector" obstruction and one failing the Klein-singlet
obstruction alone.

## Input-type accounting

- Type 3: [`klein_substrate`](klein_substrate.md) supplies the
  primary XOR filter *and* the $\mathbb{Z}_2$ torsion of
  $H_1(K^2; \mathbb{Z})$ that underwrites the antipodal
  representation theory.
- Type 4: [`gauge_identification`](gauge_identification.md) fixes
  which eigenmode carries EM charge, via the post-EWSB
  $\mathbb{Z}_2 \hookrightarrow \mathrm{U}(1)_\text{em}$ reading;
  [`gell_mann_nishijima`](gell_mann_nishijima.md) supplies the
  cross-sector criterion.
- No Type 1 amplitude consumed; the ratio is structural.

## Remarks

- The $5 + 1$ split is the framework's specific prediction for the
  dark-to-baryon decomposition.  A different topology commitment
  (for example $\mathbb{RP}^2$ instead of Klein) would not yield
  this secondary split: the Klein bottle's $\mathbb{Z}_2$ torsion
  is essential to make the antipodal representation non-trivial.
- Together with [`baryon_fraction`](baryon_fraction.md) and
  [`dark_energy`](dark_energy.md), the three sum to
  $13 / 19 + 5 / 19 + 1 / 19 = 1$, exhausting the total mode
  budget $|F_7| = 19$.
