---
kind: theorem
status: active
input_types: []
depends_on: [circle_map, rational_field_equation, fixed_point]
consequences: [proof_A_gravity, proof_B_quantum]
---

# Continuum limits

## Statement

Under the deep-truncation limit of the
[rational field equation](rational_field_equation.md), the discrete
population dynamics on the [Stern-Brocot tree](stern_brocot.md)
converge to a pair of partial differential systems determined by the
value of the coupling $K$:

- **$K = 1$**: the Arnowitt–Deser–Misner (ADM) evolution equations on
  a spatial slice of dimension [three](three_dimensions.md).
- **$K < 1$**: the Madelung hydrodynamic system
  $(\rho, S)$, equivalent to the Schrödinger equation under the
  substitution $\psi = \sqrt{\rho}\, e^{i S / \hbar}$.

## Proof sketch

The rational field equation at depth $N$ is a discrete dynamical
system on $O(2^N)$ modes.  Take $N \to \infty$ while holding the
[Arnold-tongue](arnold_tongue.md) structure fixed.

At $K = 1$ the tongues fill the $\Omega$-axis up to a measure-zero
set, and the population $N^*(p/q)$ becomes a Radon measure on the
real line.  The self-consistency condition for the effective coupling
$F[N]$ reduces to a second-order constraint on this measure: tracking
the constraint through the limit gives the Hamiltonian and momentum
constraints of the ADM formalism.  The spatial metric is the Gram
matrix of the [SL(2, R)](three_dimensions.md) action on the limit
measure.

At $K < 1$ the tongues leave open intervals of unlocked orbits.
Separating the population into locked (coherent) and unlocked
(incoherent) parts gives a two-field description.  The unlocked part
carries a phase $S$ and amplitude $\sqrt{\rho}$; the fixed-point
equation on these fields is the Madelung system.  The identification
$\psi = \sqrt{\rho}\, e^{i S / \hbar}$ converts it to the Schrödinger
equation.  The value of $\hbar$ is fixed by the diffusion coefficient
of the unlocked sector, which in turn is set by the
[parabola](parabola.md)-governed escape rate from tongue boundaries.

## Remarks

- The proof sketched here is the content of [Proof A](proof_A_gravity.md)
  (steps P7–P8 in detail for $K = 1$) and [Proof B](proof_B_quantum.md)
  (steps Q3–Q5 in detail for $K < 1$).  This entry states the theorem;
  the proof chains carry the load.
- Uniqueness of the limit at $K = 1$ up to the Lovelock class (Einstein
  equations plus a cosmological constant) uses Lovelock's theorem
  (1971) as an external input.
