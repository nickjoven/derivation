---
kind: prediction
status: active
input_types: [3]
depends_on: [klein_substrate, farey_partition, farey_sequence]
consequences: []
observables:
  - name: Dark-energy fraction Ω_Λ
    predicted: "|F_6| / |F_7| = 13 / 19 = 0.684211..."
    observed: 0.6847 ± 0.0073 (Planck 2018)
    residual: 0.07σ
citations:
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
---

# Dark-energy fraction

## Statement

$$\Omega_\Lambda \;=\; \frac{|F_6|}{|F_7|} \;=\; \frac{13}{19} \;=\; 0.684211\ldots$$

Planck 2018 reports $\Omega_\Lambda = 0.6847 \pm 0.0073$: residual
$0.07\sigma$.

## Derivation

Proof carried by [`farey_partition`](farey_partition.md).  The
[`klein_substrate`](klein_substrate.md) Type 3 input supplies the
denominator classes $q_2 = 2$ and $q_3 = 3$.  The
[Farey counts](farey_sequence.md) at $q_2 q_3 = 6$ and $q_2 q_3 + 1
= 7$ are pure number theory (Euler totient sums):

$$|F_6| = 13, \qquad |F_7| = 19.$$

The locked-unlocked partition $|F_7| = |F_6| + q_2 q_3$ identifies
the locked subset as the cosmological-constant sector, giving the
ratio $|F_6| / |F_7|$.

No Type 1 amplitude is consumed: $\Omega_\Lambda$ is dimensionless,
structural, and independent of the Hubble anchor or any other
observational scale.

## Remarks

- The prediction is exact at the level of the partition.  The
  residual with observation is dominated by the Planck 2018
  cosmological-parameters error bar, not by framework uncertainty.
- This is the framework's central cosmological claim.  The
  cross-sector split $6 = 5 + 1$ (within `farey_partition`) gives
  $\Omega_\text{DM} = 5 / 19$ and $\Omega_b = 1 / 19$, pending
  their own prediction entries.
- The prediction is Type 3 only: it consumes no amplitude.  It is
  therefore independent of the Hubble-tension ambiguity affecting
  [`mond_scale`](mond_scale.md) and other amplitude-dependent
  predictions.
