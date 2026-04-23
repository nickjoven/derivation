---
kind: proof
status: active
input_types: [1, 3, 6]
depends_on:
  - integers
  - mediant
  - fixed_point
  - parabola
  - circle_map
  - stern_brocot
  - farey_sequence
  - arnold_tongue
  - rational_field_equation
  - continuum_limits
  - three_dimensions
  - lie_group_characterization
  - klein_bottle
  - hubble
  - sl2r_manifold
  - klein_substrate
  - golden_ratio
  - farey_partition
  - hierarchy
  - dark_energy
  - mond_scale
  - proof_A_gravity
consequences: []
citations:
  - "Milgrom, A modification of the Newtonian dynamics (Astrophys. J. 270:365, 1983)"
  - "Friedmann, Über die Krümmung des Raumes (Z. Phys. 10:377, 1922)"
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
---

# Proof C: the bridge

## Statement

Under the framework's axiomatic primitives, both topology
commitments ([`sl2r_manifold`](sl2r_manifold.md) and
[`klein_substrate`](klein_substrate.md)), the
[Hubble anchor](hubble.md), and the [golden ratio](golden_ratio.md)
as the relevant universal constant, the cosmological numbers

| Quantity | Predicted | Observed | Residual |
|----------|-----------|----------|----------|
| $\Omega_\Lambda$ | $13 / 19$ | $0.6847 \pm 0.0073$ | $0.07\sigma$ |
| $\ell_H / \ell_P$ | $6 \cdot 13^{54}$ | $\sim 8.49 \cdot 10^{60}$ | $0.48\%$ |
| $a_0$ | $c H_0 / (2\pi \sqrt{g_*(1 / \varphi)})$ | $\sim 1.2 \cdot 10^{-10}\,\mathrm{m\,s^{-2}}$ | $4\%$ |

follow without additional inputs, connecting the anchor chain of
cosmology to the structural content of Proof A (gravity) and
Proof B (quantum).

## Chain

Seven bridge propositions B1–B7.  The spatial spine P1–P5 is shared
with [Proof A](proof_A_gravity.md) and is cited rather than
repeated.

### Shared spine (P1–P5)

See [`proof_A_gravity`](proof_A_gravity.md).  Same five
propositions: circle, mediant, Stern-Brocot tree, rational field
equation, and the $\mathrm{SL}(2, \mathbb{R})$ spatial manifold of
dimension 3.

### B1. Antiperiodic boundary on the one-dimensional ring

*Uses: P1, P3.*

Impose antiperiodic boundary conditions on a finite ring of $N$
oscillators: $\theta(x + L) = \theta(x) + \pi$.  One traversal of
the ring shifts the phase by half a cycle.  This is a Möbius-strip
identification on the phase variable; periodic boundary conditions
would permit a trivial global synchronization, while the Möbius
half-twist forces non-trivial rational divisions of the phase.

The order parameter under the twist,

$$r_\text{Möbius} \;=\; \frac{1}{N}\sum_j e^{i\theta_j}\,(-1)^{q_j},$$

carries a parity factor $(-1)^{q_j}$ that distinguishes odd- from
even-denominator modes.

### B2. Klein bottle and the XOR filter

*Uses: B1, [`klein_bottle`](klein_bottle.md),
[`klein_substrate`](klein_substrate.md).*

Extending the antiperiodic condition from one ring to two, with the
second identification pairing reflection in one direction with
periodicity in the other, gives the [Klein bottle](klein_bottle.md).
Taking this quotient as the substrate for the mode structure is
the [`klein_substrate`](klein_substrate.md) topology commitment
(Type 3 input).

The combined twist-and-reflect operation implements an XOR parity
filter on mode pairs $(p_x, p_y)$:

$$p_x + p_y \;\equiv\; 1 \pmod 2.$$

Only modes with one odd and one even winding number survive.  On
the Stern-Brocot tree at low depth, the smallest coprime survivors
are $(q_2, q_3) = (2, 3)$.

### B3. Three occurrences of the integer 3

*Uses: B2, P5.*

The integer 3 appears in three distinct roles:

- $q_3 = 3$ from B2 (Klein XOR filter).
- $\dim \mathrm{SL}(2, \mathbb{R}) = 3$ from P5 and
  [`three_dimensions`](three_dimensions.md).
- The spatial dimension $d = 3$ of the continuum limit, from the
  same Lie-group identification.

These are the same integer.  The Klein quotient acts on a product
of two SL(2, R) factors, so the denominator class $q_3$ and the
Lie-group dimension share a common origin in the mediant-induced
group structure.  The observation is structural, not numerical.

### B4. Farey counts at $n = 6$ and $n = 7$

*Uses: B2, [`farey_sequence`](farey_sequence.md).*

The cardinality of the [Farey sequence](farey_sequence.md) $F_n$ is

$$|F_n| \;=\; 1 + \sum_{k = 1}^{n} \varphi_\text{Euler}(k).$$

At $n = q_2 q_3 = 6$: $|F_6| = 13$.  At $n = 7$ (the next
refinement, including the depth beyond the Klein cutoff):
$|F_7| = 19$.  Pure number theory, independent of the framework.

### B5. Dark-energy fraction $\Omega_\Lambda = 13 / 19$

*Uses: B2, B4, [`farey_partition`](farey_partition.md).*

The theorem [`farey_partition`](farey_partition.md) delivers the
partition $|F_7| = |F_6| + q_2 q_3 = 13 + 6 = 19$, with locked
modes identified as the cosmological-constant sector:

$$\Omega_\Lambda \;=\; \frac{|F_6|}{|F_7|} \;=\; \frac{13}{19} \;=\; 0.6842\ldots$$

The prediction with observable metadata is
[`dark_energy`](dark_energy.md); Planck 2018 agreement is
$0.07\sigma$.

### B6. Planck–Hubble hierarchy $R = 6 \cdot 13^{54}$

*Uses: B3, B4, B5, [`hierarchy`](hierarchy.md),
[`hubble`](hubble.md).*

The theorem [`hierarchy`](hierarchy.md) delivers

$$R \;=\; \frac{\ell_H}{\ell_P} \;=\; q_2 q_3 \cdot |F_6|^{q_2 q_3^d} \;=\; 6 \cdot 13^{54}.$$

The exponent $q_2 q_3^d = 2 \cdot 27 = 54$ is self-referential:
$d = 3 = q_3$ from B3, so the refinement depth is set by the
denominator class it refines toward.  Numerically $R \approx
8.53 \cdot 10^{60}$, against the observed $R_\text{obs} \approx
8.49 \cdot 10^{60}$ (residual $0.48\%$).  A standalone prediction
entry is pending; the numerical comparison is already in
`hierarchy` §Statement.

### B7. MOND scale $a_0$ from Kuramoto critical coupling

*Uses: B5, [`hierarchy`](hierarchy.md), [`hubble`](hubble.md),
[`golden_ratio`](golden_ratio.md), [`mond_scale`](mond_scale.md).*

The Friedmann equation gives the reference frequency $\nu_\Lambda =
c \sqrt{\Lambda / 3}$, and $\nu_\Lambda = H_0 \sqrt{\Omega_\Lambda}$
by B5.  The Kuramoto critical-coupling formula applied to the
unlocked sector's self-consistent frequency distribution, evaluated
at the devil's-staircase pivot $1 / \varphi$, yields

$$a_0 \;=\; \frac{c\, H_0}{2\pi \sqrt{g_*(1 / \varphi)}} \;\approx\; 1.25 \cdot 10^{-10}\,\mathrm{m\,s^{-2}}.$$

Observed: $\sim 1.2 \cdot 10^{-10}$ m/s² (McGaugh 2016); residual
$\sim 4\%$.  Full derivation and observable metadata are in
[`mond_scale`](mond_scale.md).

## The bridge in one diagram

$$\Lambda \;\xrightarrow[\text{Friedmann}]{c \sqrt{\,\cdot\,/ 3}}\; \nu_\Lambda \;\xrightarrow[\text{B5}]{/\sqrt{\Omega_\Lambda}}\; H_0 \;\xrightarrow[\text{B7}]{c / (2\pi \sqrt{g_*})}\; a_0$$

Three observed constants, one underlying frequency.  Arrows 1 and
the Hubble-to-acceleration conversion factor ($c$, $2\pi$) are
standard; arrows that cross sectors (B5 and the $g_*$ factor in
B7) are the framework's claims.

## Where the load sits

- **B1**: boundary-condition mechanics; direct.
- **B2**: the [`klein_substrate`](klein_substrate.md) topology
  commitment.  Type 3 input, distinct from the `sl2r_manifold`
  commitment of the gravitational sector.
- **B3**: structural observation; no new external load.
- **B4**: pure number theory (Euler's totient sum).
- **B5**: carried in [`farey_partition`](farey_partition.md).
  Prediction wrapped in [`dark_energy`](dark_energy.md).
- **B6**: carried in [`hierarchy`](hierarchy.md); uses the
  [Hubble anchor](hubble.md) for dimensional closure.
- **B7**: carried in [`mond_scale`](mond_scale.md).  The novel step
  is the identification of the unlocked-sector critical coupling
  with the MOND threshold acceleration; the $2\pi$ is
  angular-to-cyclic conversion, forced.

## Input-type accounting

- Type 1: [Hubble anchor](hubble.md).  Used at B6 and B7.
- Type 3: two commitments.
  [`sl2r_manifold`](sl2r_manifold.md) through the shared spine;
  [`klein_substrate`](klein_substrate.md) at B2.
- Type 6: [golden ratio](golden_ratio.md) at B7.
- No Type 4 identification: the sector-to-mode assignment that
  would make `klein_substrate`'s surviving-denominator content
  interpretable as physical sectors (13 ↔ vacuum, 5 ↔ dark matter,
  1 ↔ baryons) is pending; the structural prediction
  $\Omega_\Lambda = 13 / 19$ holds without that identification,
  since the locked-vs-unlocked split is purely combinatorial.

## Scope

- The proof closes the anchor chain for the cosmological
  observables that depend only on $\Omega_\Lambda$, the hierarchy
  ratio, and the MOND scale.  Matter-fraction predictions
  ($\Omega_\text{DM} = 5 / 19$, $\Omega_b = 1 / 19$) follow from
  the same Klein-XOR-plus-Farey machinery but await their own
  prediction entries.
- The $v / M_P$ gap (electroweak-to-Planck scale) is *not* closed
  by Proof C: it requires an identification input that no entry
  here supplies.  See the pending `v_over_MP_gap` open-question
  entry.
- Proofs A, B, and C share one rational field equation.  Proof A
  is the $K = 1$ limit; Proof B is the $K < 1$ limit; Proof C
  supplies the numerical constants that populate both.  Together
  they are not three proofs but three sides of one construction.
