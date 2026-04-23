---
kind: theorem
status: active
input_types: []
depends_on: [circle_map, arnold_tongue, farey_sequence, three_dimensions]
consequences: [farey_partition, hierarchy]
---

# Duty function

## Statement

The **duty function** at critical coupling $K = 1$ is the fraction of
the [circle-map](circle_map.md) orbit time spent in the mode-locked
state at rotation number $p/q$:

$$\mathrm{duty}(q) \;=\; \frac{w(q)}{T(q)}
                      \;=\; \frac{1/q^2}{q}
                      \;=\; \frac{1}{q^3},$$

where $w(q)$ is the [Arnold-tongue](arnold_tongue.md) width and
$T(q) = q$ is the orbit period.  The exponent 3 in $1/q^3$ equals
$\dim \mathrm{SL}(2, \mathbb{R}) = d$, the spatial dimension
([three_dimensions](three_dimensions.md)).

## Proof

Two factors, each with a classical origin.

- **Tongue width $w(q) \sim 1/q^2$.**  At $K = 1$, the tongue at
  $p/q$ is tangent to the $\Omega$-axis at a Ford circle of diameter
  $1/q^2$ (Hardy & Wright, Ch. III; see [`farey_sequence`](farey_sequence.md)).
  Equivalently, the Gauss–Kuzmin measure on Farey rationals assigns
  weight $1/q^2$ to the cusp at $p/q$.  This contributes two of the
  three factors of $q$ in the exponent.
- **Orbit period $T(q) = q$.**  A $p/q$ mode-locked orbit closes
  after $q$ iterations of $f_{\Omega, 1}$.  This contributes the
  remaining factor of $q$.

Multiplying: duty $= (1/q^2)/q = 1/q^3$.  The two factors correspond
to the Iwasawa decomposition $KA / N$ split of $\mathrm{SL}(2,
\mathbb{R})$ — two "transverse" directions (positive roots, $n^2 - n
= 2$ for $n = 2$) and one "longitudinal" (rank, $n - 1 = 1$) — whose
sum is $n^2 - 1 = 3$.

## Remarks

- **General $n$.**  For the $\mathrm{SL}(n, \mathbb{R})$
  generalization, the same factorization gives
  $\mathrm{duty}(q) = 1/q^{n^2 - 1} = 1/q^{\dim \mathrm{SL}(n, \mathbb{R})}$.
  The framework uses $n = 2$.
- **Status with respect to the Standard Model.**  Downstream
  "duty-dictionary" identities derived from this function at the
  electroweak scale (in particular the cross-sector Weinberg-angle
  identity $\sin^2 \theta_W = q_2^3 / (q_2^3 + q_3^3) = 8/35$) do
  *not* port forward to this repository as predictions.  No
  scale-consistent derivation connecting the bare $K = 1$ values to
  observed $M_Z$-scale couplings exists in the framework; see the
  archived source for the audit.
- Duty-function ratios enter the cosmological partition
  (see [`farey_partition`](farey_partition.md)) as integer state
  counts, not as coupling values, and the cosmological derivation
  *does* port forward.
