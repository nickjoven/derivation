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
  - minkowski_signature
  - sl2r_manifold
consequences: []
citations:
  - "Stern, Über eine zahlentheoretische Funktion (1858)"
  - "Arnold, Small denominators I (1961)"
  - "Bianchi, Sugli spazi a tre dimensioni che ammettono un gruppo continuo di movimenti (1898)"
  - "Arnowitt, Deser, Misner, The dynamics of general relativity (1962)"
  - "Lovelock, The Einstein tensor and its generalizations (J. Math. Phys. 12:498, 1971)"
---

# Proof A: primitives to the Einstein field equations

## Statement

Under the framework's axiomatic primitives
([`integers`](integers.md), [`mediant`](mediant.md),
[`fixed_point`](fixed_point.md), [`parabola`](parabola.md)), the
topology commitment [`sl2r_manifold`](sl2r_manifold.md), and the
two external named theorems (Bianchi 1898, Lovelock 1971), the
continuum limit of the [rational field equation](rational_field_equation.md)
at coupling $K = 1$ satisfies

$$G_{\mu\nu} + \Lambda\, g_{\mu\nu} \;=\; 8\pi G\, T_{\mu\nu}.$$

The couplings $G$ and $\Lambda$ are not fixed by the proof.  They
are Type 1 amplitudes supplied by separate anchor chains.

## Chain

Eight propositions.  Each uses only prior propositions and the
entries cited in its *Uses* line.  The spine is

$$P1 \to P2 \to P3 \to P4 \to P5 \to P6 \to P7 \to P8.$$

### P1. Circle phase space

*Uses: [`integers`](integers.md), [`fixed_point`](fixed_point.md),
[`circle_map`](circle_map.md).*

An orbit of period $q$ and winding number $p$ on the line satisfies
$f^{(q)}(x) = x + p$.  The fixed-point identification
$x \equiv f^{(q)}(x)$ then forces $p \equiv 0$.  Since $p$ ranges
over the integers, the phase space is $\mathbb{R} / \mathbb{Z} = S^1$.
This is the closure used in [`circle_map`](circle_map.md) §Definition.

### P2. Mediant as the locking rule

*Uses: P1, [`mediant`](mediant.md), [`arnold_tongue`](arnold_tongue.md).*

Two coupled oscillators at winding numbers $a/b$ and $c/d$ settle to
a rational ratio in $(a/b, c/d)$ as coupling increases.  The winning
ratio has the widest [Arnold tongue](arnold_tongue.md) among
candidates in the interval.

**Named theorem (Stern, 1858).**  For Farey neighbors
$|ad - bc| = 1$, the rational in $(a/b, c/d)$ with smallest
denominator is the mediant $(a + c) / (b + d)$.

The Arnold-tongue width at $K = 1$ scales as $1 / q^2$, so "smallest
denominator" and "widest tongue" pick the same fraction.  The
framework takes the coincidence of Stern's arithmetic rule and
Arnold's dynamical rule as primitive.  Deriving one from the other
is out of scope for this proof.

### P3. Stern-Brocot enumeration

*Uses: P2, [`stern_brocot`](stern_brocot.md).*

Iterating P2 from the boundary pair $(0/1, 1/0)$ generates the
[Stern-Brocot tree](stern_brocot.md).  Every positive rational
appears exactly once.  The tree orders rationals by the denominator
at which they first lock, the same ordering that P2 selects.

### P4. Rational field equation

*Uses: P3, [`fixed_point`](fixed_point.md),
[`rational_field_equation`](rational_field_equation.md).*

The population $N(p/q)$ on the tree satisfies

$$N(p/q) \;=\; N_\text{total}\, g(p/q)\, w\!\left(p/q,\; K_0 F[N]\right),$$

with $g$ the bare density, $w$ the Arnold-tongue width, and $F[N]$
the effective coupling functional.  This is the fixed-point equation
$N = \mathcal{T}[N]$ on the population space.  Contraction of
$\mathcal{T}$ at each fixed truncation depth is standard and is
carried in [`rational_field_equation`](rational_field_equation.md)
§Fixed-point structure.

### P5. Three spatial dimensions

*Uses: P2, P3, [`three_dimensions`](three_dimensions.md),
[`sl2r_manifold`](sl2r_manifold.md).*

The column-sum action of P2 extends continuously to
$\mathrm{SL}(2, \mathbb{R})$ on the upper half plane.  The
topology commitment [`sl2r_manifold`](sl2r_manifold.md) takes the
spatial manifold to be this group.  Its dimension is
$2^2 - 1 = 3$ ([`three_dimensions`](three_dimensions.md) §Proof,
step 4).

### P6. Uniqueness of the spatial group

*Uses: P5, [`lie_group_characterization`](lie_group_characterization.md).*

**Named theorem (Bianchi, 1898).**  Among three-dimensional real
Lie groups, $\mathrm{SL}(2, \mathbb{R})$ is the unique simple
non-compact group whose Iwasawa $KAN$ decomposition carries a
single compact $\mathrm{SO}(2)$ factor.  The Bianchi classification
rules out $\mathrm{SO}(3)$, the Heisenberg group, and the solvable
alternatives, so the topology commitment of P5 is not redundant
with an arbitrary choice of three-dimensional group.

### P7. ADM from locked Kuramoto at $K = 1$

*Uses: P4, P5, P6, [`continuum_limits`](continuum_limits.md).*

At critical coupling $K = 1$ the [Arnold tongues](arnold_tongue.md)
fill $[0, 1]$ up to a Lebesgue-null set, and the population $N^*$ of
P4 becomes a Radon measure on the Farey set.  Identify:

- the coherence $r(x, t) = \big|\sum_j e^{i\theta_j(x, t)}\big|$
  with the lapse $N$;
- the correlation tensor $\gamma_{ij} = \langle \partial_i \theta\;
  \partial_j \theta \rangle$ with the spatial metric;
- the symmetrized second moment
  $\langle \partial_i \partial_j \theta \cdot \partial_k \theta
  \rangle_\text{sym}$ with the extrinsic curvature $K_{ij}$.

Under these identifications the locked-state Kuramoto evolution on
the $\mathrm{SL}(2, \mathbb{R})$ manifold produces the ADM
evolution equations

$$\partial_t \gamma_{ij} \;=\; -2 N K_{ij} + D_i N_j + D_j N_i,$$

$$\partial_t K_{ij} \;=\; -D_i D_j N + N\!\left(R_{ij} + K K_{ij} - 2 K_{ik} K^k{}_j\right) + \text{matter}.$$

The first equation is the definition of the lapse under locked
dynamics.  The second follows from differentiating and substituting
the Kuramoto dynamics; the substantive step is this substitution,
called out as a lemma in
[`continuum_limits`](continuum_limits.md) §Proof sketch.

### P8. Lovelock uniqueness gives Einstein

*Uses: P5, P6, P7, [`minkowski_signature`](minkowski_signature.md).*

The output of P7 is a metric theory on a 3+1 manifold with
signature $(3, 1)$ (from [`minkowski_signature`](minkowski_signature.md)),
governed by a self-consistent second-order equation under transitive
group action.

**Named theorem (Lovelock, 1971).**  In four spacetime dimensions,
the unique divergence-free symmetric rank-two tensor built from the
metric and its first two derivatives is

$$G_{\mu\nu} + \Lambda\, g_{\mu\nu}.$$

Applied to the metric-side of the equations at P7 and equated to
the matter stress-energy, this gives

$$G_{\mu\nu} + \Lambda\, g_{\mu\nu} \;=\; 8 \pi G\, T_{\mu\nu}.$$

## Where the load sits

Proof A is an assembly of named external theorems and prior
repository entries.  The substantive external loads sit at:

- **P2**: the coincidence between Stern's arithmetic minimization
  (1858) and Arnold's dynamical minimization (1961).  The framework
  imports the match.
- **P5**: the topology commitment
  [`sl2r_manifold`](sl2r_manifold.md).  Type 3 input.
- **P6**: Bianchi classification (1898).  External; cited.
- **P7**: the Kuramoto-to-ADM dictionary.  The non-trivial step is
  the second ADM equation from differentiated locked dynamics; it is
  a lemma of [`continuum_limits`](continuum_limits.md).
- **P8**: Lovelock (1971).  External; cited.

The framework's novel content in Proof A is the composition: Stern
enumeration, Arnold locking, and Kuramoto continuum limit, routed
through the ADM formalism to Lovelock's classification.  No single
step is original.

## Input-type accounting

- Type 3 consumed at P5 via [`sl2r_manifold`](sl2r_manifold.md).
  One commitment.
- Types 1, 4, 5, 6 not consumed: $G$ and $\Lambda$ are amplitudes
  that the proof does not fix, and the universal-exponent content
  (Arnold-tongue scaling, parabola normal form) enters through
  definitions declared with `input_types: []` since those exponents
  are theorems about circle-map dynamics, not framework inputs.

The result is a dimensionless structural equation.  Converting it to
a cosmological prediction requires the amplitude chain through the
[Hubble anchor](hubble.md); that chain is carried in the pending
Proof C.

## Corollaries

- The [`continuum_limits`](continuum_limits.md) theorem names the
  $K = 1$ branch whose proof is carried here.
- The proof does not fix numerical values for $G$ or $\Lambda$.
  Those enter via amplitude-carrying chains: $\Lambda$ is set by the
  [Hubble anchor](hubble.md)'s partner chain in the pending
  Proof C; $G$ awaits its own entry.
- The chain does not use the [Klein bottle](klein_bottle.md).  That
  is expected: Klein structure enters the gauge sector, not the
  gravitational sector.
