---
kind: prediction
status: active
input_types: [3, 4]
depends_on: [klein_substrate, gauge_identification, klein_bottle]
consequences: []
observables:
  - name: Standard Model gauge group
    predicted: SU(3) × SU(2)_L × U(1)_Y
    observed: SU(3)_c × SU(2)_L × U(1)_Y (Standard Model, verified in every precision test since the 1970s)
    residual: exact at the level of group identity
citations:
  - "Cartan, Sur la structure des groupes de transformations finis et continus (Nony, 1894)"
  - "Utiyama, Invariant theoretical interpretation of interaction (Phys. Rev. 101:1597, 1956)"
  - "Glashow, Partial-symmetries of weak interactions (Nucl. Phys. 22:579, 1961)"
---

# Standard Model gauge group

## Statement

The Standard Model gauge group

$$G_\text{SM} \;=\; \mathrm{SU}(3) \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$$

is the unique compact Lie group consistent with four conditions:

1. Center $\mathbb{Z}_2 \times \mathbb{Z}_3$, realized as a direct
   product (not cyclic $\mathbb{Z}_6$).
2. Minimum rank given the center.
3. Confinement pattern matching the Klein XOR asymmetry
   (q = 3 confined, q = 2 open).
4. Triangle-anomaly cancellation for the Klein-bottle charges
   $\{1/3, 1/2, 2/3\}$.

## Derivation sketch

Three external results, no free parameters.

### Step 1. Center from the Klein substrate

The [`klein_substrate`](klein_substrate.md) commitment gives a
structure group whose center is $\mathbb{Z}_2 \times \mathbb{Z}_3$:
the $\mathbb{Z}_2$ factor acts on $q_2$-denominator modes, the
$\mathbb{Z}_3$ factor on $q_3$-denominator modes, and the two
factors act on disjoint mode classes (so they compose as a direct
product, not as cyclic $\mathbb{Z}_6$).  The
[`gauge_identification`](gauge_identification.md) entry carries the
commitment that these centers belong to the gauge sector.

### Step 2. Cartan classification picks SU(3) × SU(2)

**Named theorem (Cartan, 1894).**  Every simple compact Lie group
has a center listed in the Cartan classification.  Groups whose
center contains $\mathbb{Z}_3$ are $\mathrm{SU}(3)$ and $E_6$;
groups whose center contains $\mathbb{Z}_2$ are $\mathrm{SU}(2)$,
$\mathrm{SO}(2n + 1)$, $\mathrm{Sp}(2n)$, and $E_7$.

Minimum rank given the center:

- $\mathbb{Z}_3$: $\mathrm{SU}(3)$ at rank 2; next option $E_6$ at
  rank 6.
- $\mathbb{Z}_2$: $\mathrm{SU}(2)$ at rank 1; next options all at
  rank $\geq 2$.

The Klein substrate supplies one denominator class per center
factor (one for $q_2$, one for $q_3$).  Higher-rank gauge groups
would require additional Cartan generators that the topology does
not provide.

Note: $\mathrm{SU}(6)$ has cyclic center $\mathbb{Z}_6 \cong
\mathbb{Z}_2 \times \mathbb{Z}_3$ as abstract groups, but its
center acts on a single $6$-dimensional fundamental.  The Klein
substrate's two independent denominator classes select the
*direct-product* realization over the *cyclic* one, ruling out
$\mathrm{SU}(6)$.

### Step 3. The $\mathrm{U}(1)$ factor

The periodic y-direction of the Klein bottle carries an unbroken
$\mathrm{U}(1)$ isometry.  That a $\mathrm{U}(1)$ exists is
topological; its identification as hypercharge $\mathrm{U}(1)_Y$
is the [`gauge_identification`](gauge_identification.md)
commitment, validated a posteriori by the anomaly-cancellation
conditions ([`anomaly_cancellation`](anomaly_cancellation.md)).

### Step 4. Yang-Mills dynamics (Utiyama 1956)

For completeness: once the gauge group is fixed, Utiyama's theorem
(1956) plus the requirement of second-order equations of motion
(Ostrogradsky stability) selects the Yang-Mills Lagrangian
$-\frac{1}{4 g^2}\,\mathrm{Tr}\, F_{\mu\nu} F^{\mu\nu}$ uniquely,
up to the topological Pontryagin term and a cosmological-constant-
like piece (both non-dynamical in four dimensions).  The resulting
equations of motion are $D_\mu F^{\mu\nu} = J^\nu$.  Full derivation
is carried in the archived harmonics entry
`gauge_sector_lovelock.md`; a standalone theorem entry for
Yang-Mills is pending in this repository.

## Observational status

The Standard Model gauge group has been verified in every
precision test of electroweak and strong interactions since the
1970s.  The group identity — SU(3) × SU(2)_L × U(1)_Y — is not in
dispute; it is the null hypothesis against which extensions
(grand unification, extra $\mathrm{U}(1)$s, hidden sectors) are
compared.

The three gauge couplings $g_1$, $g_2$, $g_3$ are *not* predicted
by the framework (one dimensionful scale remains, consistent with
the Lovelock parallel where $G$ is not fixed either).  Their ratios
to observed values involve tongue-width arithmetic whose numerical
status is catalogued carefully in the archived harmonics entry
`sinw_fixed_point.md`.

## Input-type accounting

- Type 3: [`klein_substrate`](klein_substrate.md) supplies the
  center $\mathbb{Z}_2 \times \mathbb{Z}_3$ and the confinement
  asymmetry.
- Type 4: [`gauge_identification`](gauge_identification.md) makes
  the q_2-to-SU(2), q_3-to-SU(3), periodic-to-U(1)_Y assignments
  explicit.
- No Type 1, 5, 6 consumed for the group *identity*.  One
  dimensionful scale (equivalently, $v$ or $g$) is not predicted;
  that is the framework's remaining Type 1 input in the gauge
  sector.

## Remarks

- "Exact at the level of group identity" means the prediction is
  a discrete group specification, not a continuous number.  Any
  experimental discovery of a new gauge boson not in the SM
  spectrum would falsify the claim.
- The parallel with Lovelock (Proof A §P8) is structural: in both
  sectors, a classification theorem applied to
  topology-supplied premises yields a unique dynamics.
