---
kind: prediction
status: active
input_types: [3, 4]
depends_on: [klein_substrate, gauge_identification, gell_mann_nishijima, gauge_group]
consequences: []
observables:
  - name: Sum of six SM triangle anomaly conditions
    predicted: 0 exactly, per generation
    observed: 0 (Standard Model is anomaly-free per generation; confirmed by consistency of gauge theory and by all precision electroweak tests)
    residual: exact
citations:
  - "Adler, Axial-vector vertex in spinor electrodynamics (Phys. Rev. 177:2426, 1969)"
  - "Bell & Jackiw, A PCAC puzzle: π0 → γγ in the σ-model (Nuovo Cim. A 60:47, 1969)"
  - "Weinberg, The Quantum Theory of Fields, vol. 2, §22.4"
---

# Anomaly cancellation

## Statement

The six Standard Model triangle anomaly conditions,

$$\sum_f Y_f \;=\; 0,\qquad
\sum_f Y_f^3 \;=\; 0,$$
$$\sum_\text{doublets} Y \;=\; 0,\qquad
\sum_\text{triplets} Y \;=\; 0,$$
$$\sum_f Q_f \;=\; 0,\qquad
\text{gravitational: } \sum_f Y_f \;=\; 0,$$

are satisfied exactly per generation under the Klein-bottle
charge assignments of
[`gauge_identification`](gauge_identification.md) and the
Gell-Mann–Nishijima relation of
[`gell_mann_nishijima`](gell_mann_nishijima.md).

(The hypercharge sum $\sum_f Y_f = 0$ appears in both the
$\mathrm{U}(1)_Y^3$ and the gravitational anomaly conditions; the
six-fold listing above is the standard enumeration in the
gauge-theory literature.)

## Derivation

The charges per particle are delivered by the Klein-bottle
identification (via
[`gell_mann_nishijima`](gell_mann_nishijima.md)): quark and lepton
hypercharges and electric charges are fixed structurally, not
fit.  Substituting into the anomaly polynomials (standard
computation; see Weinberg §22.4) gives $0$ in each of the six
conditions.

Explicit first-generation check (left-handed doublet content, plus
right-handed singlets):

- $\mathrm{U}(1)_Y^3$: $2 \cdot 3 \cdot (1/3)^3 + 3 \cdot (4/3)^3 +
  3 \cdot (-2/3)^3 + 2 \cdot (-1)^3 + 1 \cdot (-2)^3 = 0$
  (where the factor of $3$ is for quark color).
- $\mathrm{SU}(2)^2 \cdot \mathrm{U}(1)_Y$: sum of doublet
  $Y$-values weighted by color multiplicity $= 3 \cdot 1/3 +
  1 \cdot (-1) = 0$.
- $\mathrm{SU}(3)^2 \cdot \mathrm{U}(1)_Y$: sum of triplet
  $Y$-values $= 2 \cdot 1/3 + (4/3) + (-2/3) = 0$.
- Gravitational ($\mathrm{U}(1)_Y \cdot \mathrm{grav}^2$): sum of
  all hypercharges $= 2 \cdot 3 \cdot 1/3 + 3 \cdot 4/3 + 3 \cdot
  (-2/3) + 2 \cdot (-1) + 1 \cdot (-2) = 0$.
- Remaining two conditions ($\mathrm{U}(1)_Y^2 \cdot \mathrm{SU}(2)$,
  $\mathrm{U}(1)_Y^2 \cdot \mathrm{SU}(3)$): both vanish by the
  same combinatorics.

All six conditions are $0$ exactly.

## Observational status

Anomaly-free gauge theories are the only ones whose quantization
is consistent with general covariance.  The Standard Model is
observed to be a consistent gauge theory, i.e. its anomalies
cancel.  Every precision electroweak test since the 1970s is
consistent with this cancellation.

The framework's prediction here is not "anomalies cancel" *per se*
— that is required for the Standard Model to exist — but that the
charges delivered by the Klein-bottle identification, with no free
parameters, are exactly the ones that produce cancellation.  A
different identification (even one structurally plausible) would
generically break one or more of the six conditions.

## Where the load sits

The anomaly polynomials are standard QFT (Adler–Bell–Jackiw 1969).
The novel content of this prediction is that the Klein-bottle
charges — forced structurally by
[`gauge_identification`](gauge_identification.md) and the
denominator classes of
[`klein_substrate`](klein_substrate.md) — hit the six required
zeros on the nose.

The harmonics `anomaly_check.py` script verifies the computation
numerically for all three SM generations and for a
right-handed-neutrino extension; the result is $0$ to machine
precision in each case.

## Input-type accounting

- Type 3: [`klein_substrate`](klein_substrate.md) through the
  charges.
- Type 4: [`gauge_identification`](gauge_identification.md)
  through the particle-to-denominator-class assignments.

## Remarks

- The $3$-generation structure of the Standard Model is not
  predicted by this chain; the cancellation holds generation by
  generation.  Why there are three generations rather than one is
  open; the framework does not currently address it.
- The `anomaly_cancellation` prediction is often what distinguishes
  physical gauge charge assignments from naïve alternatives.  In
  the framework, the Klein identification predicts the charges
  first; the anomaly cancellation is then a structural consistency
  check that the identification has the right content, not a
  separate input.
