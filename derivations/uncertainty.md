---
kind: prediction
status: active
input_types: [3]
depends_on: [proof_B_quantum, continuum_limits, rational_field_equation, parabola]
consequences: []
observables:
  - name: Heisenberg uncertainty relation for position and momentum
    predicted: Δx · Δp ≥ ℏ / 2
    observed: Δx · Δp ≥ ℏ / 2 (verified in single-photon interferometry, electron diffraction, cold-atom interferometry; no deviation observed to current precision)
    residual: exact
citations:
  - "Heisenberg, Über den anschaulichen Inhalt der quantentheoretischen Kinematik (Z. Phys. 43:172, 1927)"
  - "Kennard, Zur Quantenmechanik einfacher Bewegungstypen (Z. Phys. 44:326, 1927)"
---

# Heisenberg uncertainty

## Statement

For a quantum state, the product of position and momentum
variances satisfies

$$\Delta x \cdot \Delta p \;\geq\; \frac{\hbar}{2}.$$

This follows from the framework's Schrödinger evolution
([`proof_B_quantum`](proof_B_quantum.md)) and the Madelung
parameterization $\Psi = \sqrt{\rho}\, e^{i S / \hbar}$: the
canonical commutation relation $[\hat x, \hat p] = i\hbar$ is an
algebraic consequence of the polar-coordinate transform.

## Derivation

Carried by [Proof B](proof_B_quantum.md) through Q4 (Madelung
variables) and Q5 (Schrödinger from Madelung).  Four steps; the
first three are Proof B, the fourth is Robertson's (1929)
derivation of the general uncertainty bound from a commutator.

1. **Madelung parameters (Q4).**  The unlocked-sector continuum
   limit defines $(\rho, S)$ with the Madelung equations.
2. **Polar-to-complex transform (Q5).**  $\Psi = \sqrt{\rho}\,
   e^{i S / \hbar}$ converts Madelung to Schrödinger.  The phase
   variable $S$ plays the role of the action conjugate to $\rho$.
3. **Canonical commutator.**  On Schrödinger wavefunctions,
   $[\hat x, \hat p] = i\hbar$ is the algebraic identity
   $\hat p = -i\hbar \partial_x$ applied to $\hat x$ eigenstates.
   In the Madelung picture this is the Poisson-bracket structure
   of the $(\rho, S)$ hydrodynamic system; the quantum commutator
   is its canonical quantization.
4. **Robertson (1929) bound.**  For any two Hermitian operators
   $\hat A$, $\hat B$ with $[\hat A, \hat B] = i \hat C$, the
   variance product satisfies $\Delta A \cdot \Delta B \geq
   |\langle \hat C \rangle| / 2$.  Specializing to $\hat A = \hat x$,
   $\hat B = \hat p$, $\hat C = \hbar$ gives the uncertainty
   relation.

The role of the [parabola](parabola.md) primitive (and thus of
[`continuum_limits`](continuum_limits.md)) is that it fixes the
diffusion coefficient $\hbar$ of the unlocked sector; without that
step, $\hbar$ would be a free parameter on the right-hand side.

## Observational status

The relation is exact in all regimes where non-relativistic
quantum mechanics applies.  Every precision measurement to date
is consistent, including:

- **Single-photon interferometry**: position and transverse
  momentum variances satisfy the bound within instrumental
  resolution.
- **Electron diffraction**: two-slit and three-slit Sinha-style
  tests (see [`born_rule`](born_rule.md)) also confirm the
  position-momentum product bound at the quantum-optical level.
- **Cold-atom interferometry**: state-of-the-art atom
  interferometers directly test the relation at the level of
  the underlying canonical structure; no deviation has been
  reported.

## Where the load sits

The non-trivial work is in delivering $\hbar$ as a *derived*
diffusion coefficient (Proof B Q4), not as a free parameter.  The
uncertainty bound itself is a corollary of any canonical
commutator and Robertson's bound.

## Input-type accounting

- Type 3 consumed via [`proof_B_quantum`](proof_B_quantum.md)
  (which uses [`sl2r_manifold`](sl2r_manifold.md)).
- No Type 1 amplitude consumed: the bound is amplitude-independent,
  and $\hbar$ appears on both sides.
- No Type 4, 5, 6 consumed.

## Remarks

- The framework does not predict a generalized-uncertainty
  modification (e.g. $\Delta x \cdot \Delta p \geq \hbar/2 +
  \ell_P^2 \Delta p^2$, from candidate Planck-scale corrections).
  Any experimental detection of such a modification would require
  amending Proof B's Q4 derivation of the diffusion coefficient.
- The $\hbar / 2$ lower bound is saturated by Gaussian wave
  packets, consistent with the saddle-node normal form of
  [Proof B §Q1](proof_B_quantum.md): near the tongue boundary, the
  basin measure is Gaussian to leading order in $\varepsilon$.
