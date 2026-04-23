---
kind: prediction
status: active
input_types: [3]
depends_on: [parabola, arnold_tongue, proof_B_quantum]
consequences: []
observables:
  - name: Born-rule exponent in P = |ψ|^α
    predicted: α = 2
    observed: α = 2 (two-slit interference, Bell tests, quantum tomography; no deviation detected)
    residual: exact
citations:
  - "Sinha et al., Ruling out multi-order interference in quantum mechanics (Science 329:418, 2010)"
  - "Born, Zur Quantenmechanik der Stoßvorgänge (Z. Phys. 37:863, 1926)"
---

# Born rule

## Statement

The probability of finding a quantum system in the $k$-th
eigenstate of an observable is the squared amplitude:

$$P_k \;=\; |\psi_k|^2.$$

The exponent $2$ is the degree of the saddle-node normal form at
the boundary of an [Arnold tongue](arnold_tongue.md), i.e. the
exponent of the [parabola](parabola.md) primitive.

## Derivation

Carried by [Proof B](proof_B_quantum.md) at Q2.  The basin width
of the $k$-th locked attractor scales as $\Delta\theta_k \propto
\sqrt{\varepsilon_k}$ (Q1, parabola normal form); the basin area
in two dimensions is therefore $(\Delta\theta_k)^2 \propto
\varepsilon_k = |\psi_k|^2$.  The exponent is geometric, not a
postulate of the theory.

## Observational status

- **Two-slit interference**: exponent 2 is the form the
  interference visibility depends on amplitude.  Deviations would
  show up as residual three-path correlations in the
  multi-slit-interference test; Sinha et al. (2010) bounded the
  Sorkin third-order correlator at $\lesssim 10^{-2}$ relative to
  the second-order, consistent with exactly 2.
- **Bell tests**: the quantum-mechanical $\cos^2$ correlation
  pattern (derived from $|\psi|^2$) has been confirmed at the
  $10^{-4}$ level in loophole-free Bell tests.
- **Quantum state tomography**: full-state reconstruction assuming
  the Born rule recovers predicted expectation values to high
  precision in every benchmarked platform.

No confirmed deviation from exponent 2 has been reported.

## Where the load sits

The exponent is forced by the saddle-node normal form (standard
dynamical-systems theorem; see Guckenheimer & Holmes §3.5).  No
framework-specific input is needed beyond the
[parabola](parabola.md) primitive.  The novel content is the
identification of the quantum amplitude with the basin-width
parameter of the unlocked sector (Proof B Q4), not the exponent
itself.

## Remarks

- Born (1926) introduced the rule as a postulate.  The framework
  derives it rather than assumes it; this is the proximate reason
  Proof B is one of the two structural proof chains.
- Proposals of $|\psi|^{2 + \delta}$ with small $\delta$ (generalized
  Born rules) are incompatible with the framework to the extent
  that the parabola normal form is exact at the saddle-node, which
  it is at all scales reached by circle-map dynamics.
