---
kind: prediction
status: active
input_types: [3]
depends_on: [klein_substrate, farey_partition]
consequences: [dm_baryon_ratio]
observables:
  - name: Baryon fraction Ω_b
    predicted: 1 / 19 ≈ 0.05263
    observed: 0.0493 ± 0.0006 (Planck 2018)
    residual: ~5% (~5.6σ)
citations:
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
---

# Baryon fraction

## Statement

$$\Omega_b \;=\; \frac{1}{19} \;\approx\; 0.05263.$$

Planck 2018 reports $\Omega_b = 0.0493 \pm 0.0006$; residual
$\sim 5\%$ in the bare number, about $5.6\sigma$ given the
tight Planck error bar.

## Derivation

See [`farey_partition`](farey_partition.md) §Cross-sector structure
and [`dark_matter_fraction`](dark_matter_fraction.md).  The
secondary $\mathbb{Z}_2 \times \mathbb{Z}_3$ split of the six
unlocked modes yields $6 = 5 + 1$; the singleton is identified
with the baryonic sector, giving $\Omega_b = 1 / 19$.

## Observational status

Unlike $\Omega_\Lambda = 13 / 19$ ($0.07\sigma$) and
$\Omega_\text{DM} = 5 / 19$ ($\sim 0.2\sigma$), the
$\Omega_b$ prediction has a visible tension with Planck 2018.
Two sources of the residual are plausible:

1. **Identification ambiguity.**  The assignment of the singleton
   orbit to baryons (rather than, for example, a spectator
   cosmological sector) is an identification-level commitment that
   has not been formally entered (no
   [`baryon_identification`](baryon_identification.md) yet).  The
   structural prediction is $\{5, 1\}$; which physical sector gets
   which is a separate Type 4 input.
2. **Baryon-photon-neutrino structure.**  The framework predicts
   baryons but does not distinguish baryons from photons and
   neutrinos at this level.  Planck's
   $\Omega_b \approx 0.0493$ does not include radiation; a fairer
   comparison would sum baryons with the radiation budget
   ($\Omega_\gamma + \Omega_\nu \sim 10^{-4}$), which does not
   close the gap.

The $5\%$ residual is noted here without claim of resolution.
The structural piece — that the singleton mode has fraction
$1 / 19$ — is exact.

## Remarks

- The $5.6\sigma$ formal residual against Planck is the largest
  residual in the current predictions scorecard.  It is a candidate
  for the `anchor_audit` open-question entry.
- The symmetry with [`dark_matter_fraction`](dark_matter_fraction.md)
  is intact: the $5$ and the $1$ are the two orbits of the
  secondary parity.  The question is which orbit is which physical
  sector.
