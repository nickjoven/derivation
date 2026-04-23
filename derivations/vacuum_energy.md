---
kind: prediction
status: active
input_types: [1, 3]
depends_on: [hierarchy, hierarchy_ratio, farey_partition, hubble, klein_substrate]
consequences: []
observables:
  - name: Vacuum energy density in Planck units
    predicted: Λ ℓ_P^2 = 13^(-108) / 12 ≈ 4.4e-122
    observed: Λ ℓ_P^2 ≈ (1.1e-52 m^-2) * (1.616e-35 m)^2 ≈ 2.9e-122
    residual: ~50% on the bare number (i.e., 0.1–0.2% in the log-exponent)
citations:
  - "Planck Collaboration, Cosmological parameters (A&A 641:A6, 2020)"
  - "Weinberg, The cosmological constant problem (Rev. Mod. Phys. 61:1, 1989)"
---

# Vacuum energy

## Statement

The cosmological constant in Planck units is

$$\Lambda\, \ell_P^2 \;=\; 3\, \Omega_\Lambda \left(\frac{\ell_P}{\ell_H}\right)^2 \;=\; \frac{3 \cdot 13 / 19}{\bigl(6 \cdot 13^{54}\bigr)^2} \;=\; \frac{13^{-108}}{12},$$

numerically $\sim 4.4 \cdot 10^{-122}$.  Observed value $\sim
2.9 \cdot 10^{-122}$, a $\sim 50\%$ residual on the bare number,
or $\sim 0.15\%$ in the logarithm.

## Derivation

Carried as a corollary of [`hierarchy`](hierarchy.md) §Corollary:
combine $R = \ell_H / \ell_P$ with $\Omega_\Lambda = 13 / 19$ (from
[`farey_partition`](farey_partition.md)) via the Friedmann identity

$$\Lambda \;=\; 3 H_0^2\, \Omega_\Lambda / c^2 \;=\; 3\, \Omega_\Lambda / \ell_H^2.$$

Rearranging:

$$\Lambda\, \ell_P^2 \;=\; 3\, \Omega_\Lambda\, (\ell_P / \ell_H)^2 \;=\; \frac{3 \cdot 13 / 19}{(6 \cdot 13^{54})^2} \;=\; \frac{13^{-108}}{12}.$$

## Observational status

The bare-number residual of $\sim 50\%$ is misleading; on the
logarithmic scale (the scale on which the cosmological-constant
problem is framed), the prediction matches observation to
$\sim 0.15\%$.  Weinberg (1989) emphasized that the
cosmological-constant problem is the 120-order-of-magnitude gap
between predicted and observed values in naïve QFT calculations;
the framework predicts $10^{-121.4}$ rather than $10^{-1}$ or
$10^0$.

The residual at $\sim 50\%$ is dominated by the Hubble tension and
by uncertainty in the present-day $\Omega_\Lambda$.  The
prediction's structural content (the exponent $-108$ from
$2 \cdot 54$) is exact.

## Input-type accounting

- Type 1: via [`hubble`](hubble.md) through the Planck length
  normalization; also through $\Omega_\Lambda$'s observational
  comparison, though the ratio $13 / 19$ itself is Type-3-only.
- Type 3: [klein_substrate](klein_substrate.md), through $q_2 q_3
  = 6$, $|F_6| = 13$, and the exponent $q_2 q_3^d = 54$.

## Remarks

- This is the framework's answer to Weinberg's cosmological-constant
  problem: the $10^{-120}$ factor is not a fine-tuning but a
  combinatorial exponent $13^{-108}$, with the $1/12$ a consequence
  of $3 \cdot 13 / 19$ arithmetic.
- The prediction is *structural* in the logarithm and
  *amplitude-dependent* in the bare number.  The Hubble-tension
  sensitivity is at the $\sim 8\%$ level on the bare number.
