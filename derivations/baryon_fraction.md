---
kind: prediction
status: active
input_types: [3, 4]
depends_on: [klein_substrate, klein_bottle, farey_partition, gell_mann_nishijima]
consequences: [dm_baryon_ratio]
observables:
  - name: Baryon fraction Ω_b
    predicted: 1 / 19 ≈ 0.05263
    observed: 0.0493 ± 0.0003 (Planck 2018)
    residual: ~6.7% (~11σ)
citations:
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
---

# Baryon fraction

## Statement

$$\Omega_b \;=\; \frac{1}{19} \;\approx\; 0.05263.$$

Planck 2018 reports $\Omega_b = 0.0493 \pm 0.0003$; residual
$\sim 6.7\%$ in the bare number, about $11\sigma$ given the
tight Planck error bar.

The quoted Planck uncertainty is the one on $\Omega_b$ derived
from the combination $\Omega_b h^2 = 0.02237 \pm 0.00015$, which
is measured directly from the CMB acoustic peak heights and is
*independent of $H_0$*.  Using a looser $\Omega_b$ uncertainty
that folds in $H_0$ tension (for example, Planck's full
marginalized $\pm 0.0006$) understates the tension by a factor
of two; the $\Omega_b h^2$-based error $\pm 0.0003$ is the
correct one to use against a structural $1/19$ prediction,
because the prediction has no $H_0$ dependence either.

## Derivation

See [`farey_partition`](farey_partition.md) §Cross-sector
structure and [`dark_matter_fraction`](dark_matter_fraction.md).
At depth $q_\max = q_2 q_3 + 1 = 7$, the unlocked budget is
$|F_7| - |F_6| = \varphi(7) = 6$, indexed by numerators
$p \in \{1, 2, 3, 4, 5, 6\}$ of the $q = 7$ class $\{p / 7\}$.

The split $6 = 5 + 1$ is **not** a quotient by a $\mathbb{Z}_2
\times \mathbb{Z}_3$ action on the six modes; that framing was a
placeholder.  The correct mechanism has two structural ingredients,
both rooted in the Klein substrate.

### 1. Klein-antipodal $\mathbb{Z}_2$ representation theory

The Klein bottle has torsion $H_1(K^2; \mathbb{Z}) = \mathbb{Z}
\oplus \mathbb{Z}_2$ ([`klein_bottle`](klein_bottle.md)).  The
$\mathbb{Z}_2$ factor makes the antipodal action $k \mapsto 6 - k$
on the $\mathbb{Z}_6$ residues of $p \in \{1, \ldots, 6\}$ a
*non-trivial* $\mathbb{Z}_2$ representation on the field bundle.
Antipodally-paired modes $\{\psi_p, \psi_{6-p}\}$ decompose into
two one-dimensional irreducible $\mathbb{Z}_2$ representations:

- **Symmetric**: $\psi_p + \psi_{6-p}$, trivial $\mathbb{Z}_2$
  representation (single-valued around the Klein loop).
- **Antisymmetric**: $\psi_p - \psi_{6-p}$, sign $\mathbb{Z}_2$
  representation (picks up monodromy $-1$ around the loop, no
  single-valued global phase).

The antipodal identification does *not* merge the pair; it
decomposes the two-dimensional pair-space into two one-dimensional
irreducibles.  The four antipodal classes of $\{1, \ldots, 6\}$:

| Class | Type | $\gcd$ with $6$ | Sectors present |
|-------|------|-----------------|-----------------|
| $\{1, 5\}$ | coprime-to-$6$ | $1$ | $q_2$ and $q_3$ (cross-sector) |
| $\{2, 4\}$ | $\gcd = 2$ | $2$ | $q_2$ only |
| $\{3\}$ | self-paired | $3$ | $q_3$ only |
| $\{6\} \equiv \{0\}$ | self-paired | $6$ | trivial sector |

### 2. EM-coupling criterion

[`gell_mann_nishijima`](gell_mann_nishijima.md) fixes
electromagnetic coupling as the $\mathrm{U}(1)_\text{em}$ generator
$Q = T_3 + Y / 2$ at the Klein identification boundary.  A mode
carries net EM coupling iff:

(a) it is a **Klein-singlet** (symmetric combination of an
antipodal pair, or self-paired fixed mode) — i.e., it has a
single-valued global phase around the Klein loop, which is the
condition for definite charge under the $\mathrm{U}(1)_\text{em}$
generator inherited from the post-EWSB $\mathbb{Z}_2
\hookrightarrow \mathrm{U}(1)_\text{em}$ reading of
[`gauge_identification`](gauge_identification.md); AND

(b) its numerator $p$ is **coprime to $6$**, so the mode
participates in *both* the $q_2$ and $q_3$ sectors, which is the
cross-sector requirement for $\alpha_\text{em} = \alpha_2
\sin^2\theta_W$-type couplings to be non-zero.

### 3. The baryonic count is one

Applying (a) and (b) to the six matter modes:

| Mode | Klein-singlet? (a) | Coprime to $6$? (b) | Baryonic? |
|------|--------------------|---------------------|-----------|
| $\psi_1 + \psi_5$ | yes | yes | **yes** |
| $\psi_1 - \psi_5$ | no (sign rep) | yes | no |
| $\psi_2 + \psi_4$ | yes | no | no |
| $\psi_2 - \psi_4$ | no (sign rep) | no | no |
| $\psi_3$ | yes (self-paired) | no | no |
| $\psi_6$ | yes (self-paired) | no | no |

Exactly one mode — the symmetric combination of the coprime pair
$\{1, 5\}$ — satisfies both conditions.  The remaining five are
dark (no net EM coupling, gravitational coupling only).  Combined
with the $13$-mode dark-energy sector from
[`farey_partition`](farey_partition.md):

$$\Omega_\Lambda : \Omega_\text{DM} : \Omega_b = 13 : 5 : 1
\quad\text{over}\quad |F_7| = 19.$$

The baryonic count $\Omega_b = 1 / 19$ is forced by the Klein
$\mathbb{Z}_2$ torsion plus the EM-coupling criterion; no free
parameters.

## Observational status

The dark-energy and dark-matter fractions sit near observation
($\Omega_\Lambda$ at $0.07\sigma$, $\Omega_\text{DM}$ at
$\sim 0.2\sigma$).  The baryon fraction residual is the outlier:

- **Predicted**: $1 / 19 = 0.05263$.
- **Observed (Planck 2018, $\Omega_b h^2$-based)**: $0.0493 \pm
  0.0003$.
- **Residual**: $\sim 6.7\%$, $\sim 11\sigma$.

Three framings of the residual remain live; none is currently
resolved in this repo.

1. **Boundary-weight correction.**  The Farey depth may act as
   $w^* \sim 0.83$ rather than as a sharp integer; this reduces
   the baryon count below $1 / 19$.  Load sits in the boundary-weight
   analysis in harmonics (`boundary_weight_correction.md`), not yet
   ported here.
2. **Identification audit.**  The assignment of the singleton
   coprime-symmetric mode to baryons specifically (rather than to,
   say, a spectator sector) is an identification-level commitment.
   It is flagged in the open question
   [`baryon_sector_identification`](baryon_sector_identification.md).
3. **Radiation budget.**  Planck's $\Omega_b \approx 0.0493$ does
   not include $\Omega_\gamma + \Omega_\nu \sim 10^{-4}$.  The
   radiation budget does not close the $6.7\%$ gap.

## Remarks

- The $\sim 11\sigma$ formal residual is the largest in the
  current predictions scorecard and is tracked in
  [`baryon_sector_identification`](baryon_sector_identification.md).
- The structural prediction — that of the six unlocked modes,
  exactly one is Klein-singlet AND coprime-to-$6$, giving the
  $\{5, 1\}$ decomposition — is exact and depends on no anchors.
- The partner prediction $\Omega_\text{DM} = 5 / 19$ in
  [`dark_matter_fraction`](dark_matter_fraction.md) uses the
  same eigenmode decomposition; the $5$ is the count of modes
  that fail condition (a), condition (b), or both.
