---
kind: prediction
status: active
input_types: [3]
depends_on: [klein_substrate, farey_partition]
consequences: [dm_baryon_ratio]
observables:
  - name: Dark-matter fraction Ω_DM
    predicted: 5 / 19 ≈ 0.2632
    observed: 0.265 ± 0.007 (Planck 2018)
    residual: ~0.2σ
citations:
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
---

# Dark-matter fraction

## Statement

$$\Omega_\text{DM} \;=\; \frac{5}{19} \;\approx\; 0.2632.$$

Planck 2018 reports $\Omega_\text{DM} = 0.265 \pm 0.007$; residual
$\sim 0.2\sigma$.

## Derivation

See [`farey_partition`](farey_partition.md) §Cross-sector structure.
The unlocked budget $|F_7| - |F_6| = 6 = q_2 q_3$ splits further
under the Klein-XOR parity refinement into $6 = 5 + 1$, giving

$$\Omega_\text{DM} \;=\; \frac{5}{19}, \qquad \Omega_b \;=\; \frac{1}{19}.$$

The split arises because the six unlocked modes decompose by a
secondary parity ($\mathbb{Z}_2 \times \mathbb{Z}_3$ action of the
Klein surviving modes) into a five-element orbit and a singleton.

## Input-type accounting

- Type 3: [klein_substrate](klein_substrate.md) supplies the
  primary XOR filter; the secondary $\mathbb{Z}_2 \times
  \mathbb{Z}_3$ refinement is a downstream consequence of the
  same commitment, not an independent Type 3 input.
- No Type 1 amplitude consumed; the ratio is structural.

## Remarks

- The $5 + 1$ split is the framework's specific prediction for the
  dark-to-baryon decomposition.  A different topology commitment
  (for example $\mathbb{RP}^2$ instead of Klein) would not yield
  this secondary split.
- Together with [`baryon_fraction`](baryon_fraction.md) and
  [`dark_energy`](dark_energy.md), the three sum to
  $13 / 19 + 5 / 19 + 1 / 19 = 1$, exhausting the total mode
  budget $|F_7| = 19$.
