---
kind: definition
status: active
input_types: []
depends_on: []
consequences: [integers, mediant, fixed_point, parabola, hubble, vev]
---

# Inputs taxonomy

## Definition

The framework's content decomposes into six types of input.  A
derivation is legitimate iff it does not *create* an input type from
nothing — crossings between types require a named mechanism.

| Type | Name | Example | Source |
|------|------|---------|--------|
| 1 | Scale / amplitude | $H_0$, $v_\mathrm{EW}$ | Observation |
| 2 | Dimensionless ratio / pitch | $\Omega_\Lambda / \Omega_m = 13/6$, generation mass ratios | Derived from 3 + 4 ($+$ 5, 6) |
| 3 | Topology / structure | Klein-quotient substrate | Ontological commitment |
| 4 | Identification map | $q_2 \leftrightarrow U(1)_Y$, $q_3 \leftrightarrow \mathrm{SU}(2)_L$ | Framework's specific claim |
| 5 | Phase / orientation label | $\mathbb{Z}_2$ torsion, $(-1)^\ell$ sign flip | Sub-labeling of Type 4 |
| 6 | Universal exponent | $\varphi$, $\sqrt 5$, $\delta_\text{MacKay}$, $\lambda_\text{unlock}$ | Inherited from universal dynamics (KAM, golden torus) |

## Type details

### Type 1 — Scale / amplitude

Observational.  Two registers, one per sector:
[`hubble`](hubble.md) for the cosmological register,
[`vev`](vev.md) for the particle register.  These carry no
dimensionless content derivable from combinatorial structure; they
set the physical intensity of each sector.  Analogous to the volume
knobs on two different instruments.

### Type 2 — Dimensionless ratios

Structural, scale-invariant.  $\Omega_\Lambda = 13/19$, $R = 6 \cdot
13^{54}$, $\Lambda \ell_P^2 = 13^{-108}/12$, $\Omega_b = 1/19$, $d =
3$.  Every ratio derives from some combination of Types 3, 4, 5, 6;
no ratio derives from other ratios alone.  Analogous to pitch
intervals: they follow from the instrument and the score, not from
other intervals.

### Type 3 — Topology

A commitment to which mathematical object the substrate is.  The
framework commits to the [Klein bottle](klein_bottle.md) quotient.
Alternatives (torus, sphere, $\mathbb{RP}^2$, …) would yield
different surviving modes under the XOR filter and therefore
different Type 2 ratios.

Whether this commitment can be *forced* (e.g. by the existence of
fermions, which requires non-orientability) is an open question; the
framework carries the commitment as an axiom for now.

### Type 4 — Identification map

The framework's novel content.  The Klein-bottle quotient forces the
denominator classes $q_2 = 2$ and $q_3 = 3$ to be the surviving
classes; it does *not* force the assignment

$$q_2 \leftrightarrow U(1)_Y, \qquad q_3 \leftrightarrow \mathrm{SU}(2)_L.$$

That assignment is a separate commitment.  Similarly for the
13-mode subset $\leftrightarrow$ vacuum sector, 5-mode subset
$\leftrightarrow$ dark matter, 1-mode subset $\leftrightarrow$
baryonic matter (see [`farey_partition`](farey_partition.md)).
Identification is *partially* forced by topology (*which* classes
survive) and *partially* free (*which sector* gets mapped to each
class).

### Type 5 — Phase / orientation label

Qualitative information about monodromy, sign structure, and
spin-statistics.  Not a continuous parameter.  Examples: the
$\mathbb{Z}_2$ torsion in $H_1(K^2)$, the $(-1)^\ell$ sign flip in
spherical harmonics, the antipodal symmetric/antisymmetric split.

Type 5 is fine-grained *within* Type 4: the topology
(Type 3) guarantees the existence of the $\mathbb{Z}_2$ torsion, but
the *labeling* of which physical fermion gets the $+$ eigenvalue and
which gets $-$ is an identification choice below the sector level.

### Type 6 — Universal exponents

Mathematical constants inherited from universal dynamics of the
oscillator class.  The golden ratio $\varphi$ and $\sqrt 5$ appear in
the spectral tilt via self-similarity of the devil's staircase at
$1/\varphi$.  The MacKay fixed-point exponent $\delta \approx 1.6279$
appears in quasiperiodicity breakdown.  $\lambda_\text{unlock}$ is
the Lyapunov exponent of the unlocked sector at $K = 1$.

These are not framework-derived — they are properties of
one-dimensional circle-map dynamics, carried in by the choice of
oscillator class.  "Zero free parameters" is compatible with their
presence because they are not *free*: they are mathematical
constants, not fit values.

## Rules of composition

A legitimate derivation respects these compositions:

- Types 3, 4, 5, 6 $\to$ Type 2.  Topology plus identification plus
  phase labels plus universal exponents give dimensionless ratios.
- Type 1 fixes the dimensional scale within one sector.  It does not
  generate Type 2 ratios; it does not carry into the other sector.
- Types 3, 4, 5, 6 are orthogonal to Type 1.  Ratios do not pin
  amplitudes.
- **Type 2 does not derive from Type 2.**  Algebraic manipulation of
  ratios to produce a new ratio is *not* a legitimate derivation
  without introducing a new Type 3, 4, or 5 input.  This is the rule
  that several historical audit-failures violated (additive fitted
  corrections to $\sin^2 \theta_W$, $\lambda_H$, etc.).

## Running count of inputs

Given topology (Type 3) and identification (Type 4) as independent
commitments, and two amplitudes (Type 1) as observational anchors:

- **Type 1**: 2 (firm — observational).
- **Type 3**: 1 Klein commitment; possibly forced to 0 by "fermions
  must exist," unresolved.
- **Type 4**: 1 identification map (partially constrained by Type 3,
  partially free).
- **Type 5**: sub-labeling of Type 4; not counted separately.
- **Type 6**: 0 (mathematical constants, not framework inputs).

Running count: **3 to 4 independent inputs**, depending on whether
the Klein commitment is forced.  Not 0, not 2.

## Scope of the framework

The framework is a specific realization on a Klein-quotient
mode-locked substrate.  Its content is:

- a topology commitment (Type 3),
- an identification map (Type 4, with Type 5 sub-labels),
- inherited universal oscillator structure (Type 6),
- two amplitude anchors (Type 1),

yielding a collection of dimensionless ratios (Type 2) that match
observation.  Asking a Type 2 ratio to close to fewer inputs is
asking algebra to substitute for topology or identification.  Asking
a Type 1 amplitude to derive from Type 2 ratios is asking pitch to
set loudness.

## Remarks

- The six-type scheme is the meta-schema for every subsequent entry.
  Each entry declares its `input_types` in frontmatter.  Entries with
  non-empty `input_types` must have a dependency of matching
  `kind` supplying each type (an `amplitude_anchor` for Type 1, a
  `topology_commitment` for Type 3, etc.).
- This entry is a `kind: definition` because it *defines* the
  taxonomy used by the rest of the repository.  It does not prove
  anything; it fixes conventions.
