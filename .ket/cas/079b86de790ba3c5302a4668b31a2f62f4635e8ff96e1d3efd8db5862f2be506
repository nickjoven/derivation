---
kind: proof
status: active
input_types: [3]
depends_on:
  - integers
  - mediant
  - fixed_point
  - parabola
  - circle_map
  - stern_brocot
  - arnold_tongue
  - rational_field_equation
  - continuum_limits
  - three_dimensions
  - lie_group_characterization
  - sl2r_manifold
  - proof_A_gravity
consequences: []
citations:
  - "Madelung, Quantentheorie in hydrodynamischer Form (Z. Phys. 40:322, 1927)"
  - "Schrödinger, Quantisierung als Eigenwertproblem (Ann. Phys. 79:361, 1926)"
  - "Guckenheimer & Holmes, Nonlinear Oscillations, §3.5 (saddle-node normal form)"
---

# Proof B: primitives to the Schrödinger equation and the Born rule

## Statement

Under the framework's axiomatic primitives and the topology
commitment [`sl2r_manifold`](sl2r_manifold.md), the continuum limit
of the [rational field equation](rational_field_equation.md) at
coupling $K < 1$ satisfies the Schrödinger equation

$$i \hbar\, \partial_t \Psi \;=\; -\frac{\hbar^2}{2m}\nabla^2 \Psi + V\Psi$$

for the unlocked fraction of the oscillator population, and the
probability of finding the system in the $k$-th locked attractor is

$$P_k \;=\; |\psi_k|^2.$$

The value of $\hbar$ is a derived diffusion coefficient of the
unlocked sector.  The potential $V$ and the mass $m$ are not fixed
by the proof.

## Chain

Six quantum-branch propositions Q1–Q6.  The spatial spine P1–P5 is
shared with [Proof A](proof_A_gravity.md); this proof cites it
rather than repeating.  The two chains diverge at P4 on the
coupling parameter $K$.

### Shared spine (P1–P5)

See [`proof_A_gravity`](proof_A_gravity.md).  The spine delivers the
circle phase space (P1), the mediant as the locking rule (P2), the
Stern-Brocot tree as configuration space (P3), the rational field
equation as a self-consistent population on the tree (P4), and the
$\mathrm{SL}(2, \mathbb{R})$ spatial manifold of dimension three (P5,
via [`sl2r_manifold`](sl2r_manifold.md)).

Proof A's P6 (Bianchi uniqueness) is consumed implicitly through
`sl2r_manifold`; it is not otherwise needed for the quantum branch.

The split is at P4: Proof A takes the $K = 1$ limit of P4; this
proof takes $K < 1$.

### Q1. Saddle-node normal form at tongue boundaries

*Uses: P3, [`parabola`](parabola.md),
[`arnold_tongue`](arnold_tongue.md).*

Each [Arnold tongue](arnold_tongue.md) terminates in a saddle-node
bifurcation.  Near the bifurcation the one-dimensional dynamics
reduce, by the standard normal-form theorem (Guckenheimer & Holmes
§3.5), to the [parabola](parabola.md) form

$$\dot x \;=\; \mu - x^2, \qquad \mu = \text{detuning from resonance}.$$

The basin width of the locked attractor scales as

$$\Delta \theta(\varepsilon) \;\propto\; \sqrt{\varepsilon}, \qquad \varepsilon = |\mu|.$$

The $\sqrt{\varepsilon}$ scaling is the content of the parabola
primitive; the normal form is exact, not perturbative.

### Q2. Born rule: $P = |\psi|^2$

*Uses: Q1.*

The probability of landing in the basin of the $k$-th locked
attractor is the basin measure in phase-amplitude space.  In two
dimensions the basin area scales as $(\Delta \theta_k)^2$.  By Q1
this is $\varepsilon_k$, which is the squared amplitude $|\psi_k|^2$
under the Madelung parameterization introduced at Q4:

$$P_k \;\propto\; (\Delta \theta_k)^2 \;\propto\; \varepsilon_k \;=\; |\psi_k|^2.$$

The exponent 2 is the degree of the parabola in the saddle-node
normal form.  It is geometric, not axiomatic.

### Q3. Subcritical regime: locked and unlocked fractions

*Uses: P4, [`continuum_limits`](continuum_limits.md).*

At coupling $K < 1$ the devil's staircase of
[Arnold tongues](arnold_tongue.md) leaves open intervals of the
$\Omega$-axis unoccupied.  The population $N^*$ of P4 splits into a
locked fraction $r \in (0, 1)$ (supported on tongues) and an
unlocked fraction $1 - r$ (supported on the complement).  The
self-consistency equation of P4 fixes $r$; only $r < 1$ is used
below.

The locked fraction carries the classical content (metric, Proof A
at $K = 1$); the unlocked fraction carries the quantum content
(Q4–Q5).

### Q4. Madelung variables for the unlocked fraction

*Uses: Q3, P5, [`continuum_limits`](continuum_limits.md).*

Identify within the unlocked sector:

- $\rho(x, t)$: number density of unlocked oscillators at spatial
  point $x$ (on the $\mathrm{SL}(2, \mathbb{R})$ manifold);
- $S(x, t)$: accumulated action of the unlocked drift.

Nearest-neighbor diffusive coupling on the Stern-Brocot tree yields,
in the continuum limit of P5, the Madelung equations

$$\partial_t \rho + \nabla \cdot\!\left(\rho\, \nabla S / m\right) \;=\; 0,$$

$$\partial_t S + \frac{|\nabla S|^2}{2m} + V - \frac{\hbar^2}{2m}\,\frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}} \;=\; 0.$$

The quantum potential $(\hbar^2 / 2m)\, \nabla^2 \sqrt{\rho} / \sqrt{\rho}$
arises from the Stern-Brocot renormalization flow of the per-level
variance of the unlocked sector.  This derivation is the substantive
lemma of [`continuum_limits`](continuum_limits.md) §Proof sketch for
the $K < 1$ branch.

The value of $\hbar$ appears as the diffusion coefficient of the
unlocked sector, set by the [parabola](parabola.md)-governed escape
rate from tongue boundaries.

### Q5. Schrödinger equation from Madelung

*Uses: Q4.*

**Named theorem (Madelung, 1927).**  Under the substitution
$\Psi = \sqrt{\rho}\, \exp(i S / \hbar)$, the Madelung system (Q4) is
algebraically equivalent to

$$i \hbar\, \partial_t \Psi \;=\; -\frac{\hbar^2}{2m}\nabla^2 \Psi + V \Psi.$$

The substitution is invertible modulo nodes of $\rho$.  The
Schrödinger equation is the Madelung system in polar coordinates.

### Q6. Assembly and uniqueness claims

*Uses: Q1–Q5.*

Three load-bearing claims close the chain:

1. **Madelung form.**  The pair of conservation laws on $(\rho, S)$
   (continuity from particle-count conservation, Hamilton–Jacobi
   from action conservation) is the minimal first-order pair
   consistent with both.  Any such pair is a Madelung system.
2. **Quantum potential from Stern-Brocot flow.**  The $\nabla^2
   \sqrt{\rho} / \sqrt{\rho}$ term is fixed by the per-level variance
   of the unlocked sector on the Stern-Brocot tree; see
   [`continuum_limits`](continuum_limits.md).  It is not a free
   parameter choice.
3. **Born rule exponent.**  The exponent 2 in $P = |\psi|^2$ is
   forced by the saddle-node normal form (Q1–Q2); it is the degree
   of the parabola.

The four standard postulates of quantum mechanics
(complex-amplitude state, $|\psi|^2$ probability rule, Schrödinger
evolution, conjugate-variable operators) are consequences of Q4–Q5
rather than independent inputs.

## Where the load sits

- **Q1**: the saddle-node normal form is a standard dynamical-systems
  result (Guckenheimer & Holmes).  The framework imports it through
  the [`parabola`](parabola.md) primitive.
- **Q2**: basin-measure computation; direct.
- **Q3**: $K < 1$ regime of the devil's staircase; standard.
- **Q4**: the Stern-Brocot RG derivation of the quantum potential.
  Substantive step; carried as a lemma of
  [`continuum_limits`](continuum_limits.md) §Proof sketch.
- **Q5**: Madelung (1927); external, cited.
- **Q6**: assembly of Q1–Q5; no new content.

The framework's novel content in Proof B is the same combination as
in Proof A (rational field equation, Stern-Brocot tree,
$\mathrm{SL}(2, \mathbb{R})$ manifold), taken at the subcritical
side of the same critical point.

## Input-type accounting

- Type 3 consumed at the shared P5 via
  [`sl2r_manifold`](sl2r_manifold.md).  No additional commitment.
- Types 1, 4, 5, 6 not consumed.  $\hbar$ is a derived constant (the
  diffusion coefficient of the unlocked sector); $m$ and $V$ are
  external to the proof chain.

## Corollaries

- The [`continuum_limits`](continuum_limits.md) theorem names both
  branches.  The $K = 1$ branch is Proof A; the $K < 1$ branch is
  proved here.
- The Born rule exponent 2 is the origin of the pending `born_rule`
  prediction entry.
- One rational field equation produces gravity at $K = 1$ and
  quantum mechanics at $K < 1$.  No second equation is introduced.
