---
kind: theorem
status: active
input_types: [3, 4]
depends_on: [gauge_group, gauge_identification, klein_substrate, minkowski_signature, three_dimensions]
consequences: [anomaly_cancellation]
citations:
  - "Utiyama, Invariant theoretical interpretation of interaction (Phys. Rev. 101:1597, 1956)"
  - "Ostrogradsky, Mémoires sur les équations différentielles (Mém. Acad. St. Pét. 1850)"
  - "Yang & Mills, Conservation of isotopic spin and isotopic gauge invariance (Phys. Rev. 96:191, 1954)"
---

# Yang-Mills dynamics from Utiyama uniqueness

## Statement

For the gauge group $G_\text{SM} = \mathrm{SU}(3) \times
\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ delivered by
[`gauge_group`](gauge_group.md), on the Minkowski-signature
four-manifold supplied by [`minkowski_signature`](minkowski_signature.md),
the unique gauge-invariant Lorentz-invariant Lagrangian with
second-order equations of motion is

$$\mathcal{L}_\text{YM} \;=\; -\frac{1}{4 g^2}\, \mathrm{Tr}\, F_{\mu\nu} F^{\mu\nu},$$

with equations of motion

$$D_\mu F^{\mu\nu} \;=\; J^\nu.$$

## Proof

Three external theorems plus the topology-supplied premises.

### 1. Utiyama (1956): Lagrangian reduces to $F_{\mu\nu}$

Let $P$ be a principal $G$-bundle over a Lorentzian 4-manifold $M$,
$A$ a connection on $P$ with curvature $F = dA + A \wedge A$.
Utiyama's theorem states that a Lagrangian density $\mathcal{L}$
satisfying

(i) locality in $A$ and its first derivatives,
(ii) gauge invariance (under $G$-valued gauge transformations
$A \mapsto g^{-1} A g + g^{-1} dg$), and
(iii) Lorentz invariance,

takes the form $\mathcal{L} = \mathcal{L}(F_{\mu\nu})$.  Non-covariant
dependence on $A$ would violate (ii); the covariant combination is
exactly $F_{\mu\nu}$.

### 2. Second-order restriction: at most quadratic in $F$

For the Euler-Lagrange equations to be at most second-order in
$A$ (equivalently, first-order in $F$), the Lagrangian $\mathcal{L}(F)$
can be at most quadratic in $F$.  Higher powers produce equations
of higher order in $A$.

The most general Lorentz-invariant quadratic expression built from
a Lie-algebra-valued two-form $F_{\mu\nu}$ is

$$\mathcal{L} \;=\; a \cdot \mathrm{Tr}\, F_{\mu\nu} F^{\mu\nu}
                 + b \cdot \mathrm{Tr}\, F_{\mu\nu} \tilde F^{\mu\nu}
                 + c,$$

where $\tilde F^{\mu\nu} = \frac{1}{2} \varepsilon^{\mu\nu\rho\sigma}
F_{\rho\sigma}$ is the Hodge dual.

### 3. Ostrogradsky stability rules out higher orders

The requirement of second-order equations is not a preference but a
consistency requirement.  Ostrogradsky's theorem (1850) establishes
that a non-degenerate Lagrangian of order higher than two has a
Hamiltonian unbounded below and an unstable ground state.  Terms
like $\mathrm{Tr}\, F^4$, $\mathrm{Tr}\, (D F)^2$, and similar would
produce such dynamics and are excluded.

### 4. Topological and trivial terms drop

Of the three remaining quadratic terms:

- $\mathrm{Tr}\, F_{\mu\nu} F^{\mu\nu}$: dynamical.  Produces
  Yang-Mills equations $D_\mu F^{\mu\nu} = J^\nu$.
- $\mathrm{Tr}\, F_{\mu\nu} \tilde F^{\mu\nu}$: the Pontryagin
  density.  This is a total derivative:
  $\mathrm{Tr}\, F \wedge F = d\, \mathrm{Tr}\, (A \wedge dA +
  \tfrac{2}{3} A \wedge A \wedge A)$.  It does not contribute to
  classical equations of motion.
- $c$: a constant.  Does not generate gauge dynamics (a
  gauge-invariant constant on a principal bundle is trivial).

Discarding the topological and trivial terms leaves

$$\mathcal{L}_\text{YM} \;=\; -\frac{1}{4 g^2}\, \mathrm{Tr}\, F_{\mu\nu} F^{\mu\nu},$$

with overall sign and normalization fixed by positivity of the
kinetic energy and the standard field-strength normalization.

## Where the load sits

- **Utiyama (1956)**: external.  Reduces a gauge-invariant
  Lagrangian to $\mathcal{L}(F)$.
- **Ostrogradsky (1850)**: external.  Excludes higher-order
  equations of motion.
- **Topological term**: $F \tilde F$ drops classically.  At the
  quantum level it contributes as the $\theta$-angle; vanishing
  $\theta$ is a separate claim carried (pending) by a strong-CP
  prediction entry.
- **Normalization $1/g^2$**: not fixed by this theorem; $g$ is the
  gauge coupling, one dimensionful parameter per factor of the
  gauge group.  This parallels the Lovelock-Einstein situation
  (Proof A §P8), where $G$ is similarly undetermined.

## Parallel with Proof A

| Step | Gravity (Proof A §P8) | Gauge (this theorem) |
|------|----------------------|----------------------|
| Configuration | Metric $g_{\mu\nu}$ | Connection $A_\mu$ |
| Bundle | Lorentzian 4-manifold | Principal $G$-bundle over same |
| Symmetry | General covariance | Gauge invariance |
| Order restriction | Second-order in $g$ | Second-order in $A$ |
| Uniqueness theorem | Lovelock (1971) | Utiyama (1956) + quadratic |
| Unique output | $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ | $D_\mu F^{\mu\nu} = J^\nu$ |
| Undetermined constant | Newton's $G$ | Gauge coupling $g$ |
| Topological term | Gauss-Bonnet (trivial in 4D) | Pontryagin (θ-term) |

The two derivations have identical logical shape.

## Input-type accounting

- Type 3: inherited from [`gauge_group`](gauge_group.md) (via
  [`klein_substrate`](klein_substrate.md)).
- Type 4: inherited from [`gauge_group`](gauge_group.md) (via
  [`gauge_identification`](gauge_identification.md)).

No new Type 1, 5, or 6 consumed.  The coupling $g$ is
undetermined by the theorem, consistent with the framework's
Type 1 accounting (particle sector anchored by
[`vev`](vev.md), but only one amplitude per sector).

## Remarks

- This theorem closes the gauge half of the framework's dynamical
  content.  Together with Proof A (gravity) and Proof B (quantum),
  the three equations $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G
  T_{\mu\nu}$, $i\hbar \partial_t \Psi = H \Psi$, and
  $D_\mu F^{\mu\nu} = J^\nu$ are all unique outputs given the
  framework's topology commitments plus three external classification
  theorems (Lovelock, Madelung, Utiyama).
- A standalone proof chain "Proof D: primitives to Yang-Mills" is
  plausible but not ported: it would recapitulate the chain through
  Klein substrate, center identification, Cartan classification,
  Utiyama, and end here.  At this level, the theorem is
  structurally a co-consequence of Proof A's P8 argument applied
  to the gauge sector.
