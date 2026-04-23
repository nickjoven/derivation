---
kind: prediction
status: active
input_types: [1, 3]
depends_on: [hierarchy, klein_substrate, farey_partition, hubble, three_dimensions]
consequences: []
observables:
  - name: Planck-to-Hubble length ratio R
    predicted: q_2 * q_3 * |F_6|^(q_2 * q_3^d) = 6 * 13^54 ≈ 8.533e60
    observed: ~8.49e60 (Planck 2018 ℓ_H; ℓ_P from G, ℏ, c)
    residual: ~0.48%
citations:
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
---

# Planck-to-Hubble hierarchy

## Statement

The ratio of Hubble length to Planck length is

$$R \;=\; \frac{\ell_H}{\ell_P} \;=\; q_2 q_3 \cdot |F_6|^{q_2 q_3^d} \;=\; 6 \cdot 13^{54} \;\approx\; 8.533 \cdot 10^{60},$$

against observed $R_\text{obs} \approx 8.49 \cdot 10^{60}$; residual
$\sim 0.48\%$.

## Derivation

Carried by [`hierarchy`](hierarchy.md) §Proof sketch.  The
refinement exponent $q_2 q_3^d = 2 \cdot 27 = 54$ uses the
self-referential identity $d = q_3 = 3$
([Proof C](proof_C_bridge.md) §B3).

## Observational status

Hubble length from the Planck 2018 reduced Hubble constant
$H_0 = 67.4 \pm 0.5\,\mathrm{km\,s^{-1}\,Mpc^{-1}}$ gives
$\ell_H = c / H_0 \approx 1.37 \cdot 10^{26}\,\mathrm{m}$.  Planck
length from $G$, $\hbar$, $c$ gives $\ell_P \approx 1.616 \cdot
10^{-35}\,\mathrm{m}$.  The ratio is $\sim 8.49 \cdot 10^{60}$.

The Hubble-tension ambiguity (SH0ES $H_0 \approx 73.0$ vs Planck
$H_0 \approx 67.4$) shifts $\ell_H$ by $\sim 8\%$, which propagates
to $R$ at the same level.  The $0.48\%$ residual quoted here uses
the Planck value.

## Input-type accounting

- Type 1: [Hubble anchor](hubble.md), through $\ell_H$.  The
  Planck length $\ell_P$ enters via the derived $G$.  Either
  choice of $H_0$ (Planck vs SH0ES) maps to a consistent $R$ via
  this relation.
- Type 3: [klein_substrate](klein_substrate.md) at $q_2 = 2$,
  $q_3 = 3$, $|F_6| = 13$; [sl2r_manifold](sl2r_manifold.md) at
  $d = 3$.

## Remarks

- The prediction is dimensionally consistent: $R$ is dimensionless,
  built from four integers ($q_2$, $q_3$, $|F_6|$, $d$) already
  determined by the topology commitments.  The only observational
  input is the normalization setting $\ell_H$ and $\ell_P$ —
  hence Type 1.
- The $0.48\%$ residual is small relative to the $8\%$
  Hubble-tension spread.  Resolution of the tension is required
  before a tighter bound on residual can be quoted.
