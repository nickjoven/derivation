---
kind: definition
status: active
input_types: []
depends_on: [circle_map, parabola, farey_sequence]
consequences: [duty_function, born_rule]
citations:
  - "Arnold, Small denominators I (1961)"
  - "de Melo & van Strien, One-Dimensional Dynamics, Ch. I"
---

# Arnold tongue

## Definition

For the [circle map](circle_map.md) $f_{\Omega, K}$ at rational
rotation number $p/q \in F_n$, the **Arnold tongue** at $p/q$ is the
maximal connected region of the $(\Omega, K)$ parameter plane on
which the rotation number equals $p/q$:

$$T_{p/q} \;=\; \{(\Omega, K) : W(\Omega, K) = p/q\}.$$

Each $T_{p/q}$ is rooted at $(\Omega, K) = (p/q, 0)$ and opens upward
as $K$ increases.

## Geometry at the boundary

The lateral boundary of $T_{p/q}$ consists of two saddle-node curves,
where the stable and unstable periodic orbits of period $q$ coalesce.
At each boundary point the local dynamics are smoothly conjugate to
the [parabola](parabola.md) normal form $\dot x = \mu - x^2$, with
$\mu$ measuring the distance to the tongue edge in $\Omega$.

Consequently, the width of $T_{p/q}$ in the $\Omega$-direction at
fixed $K$ scales (for small $K$) as $K^q$, and at criticality
$K = 1$ the tongue width scales as

$$w(p/q) \;\sim\; \frac{1}{q^2}.$$

The $1/q^2$ scaling at $K = 1$ is the Gauss–Kuzmin measure on
[Farey rationals](farey_sequence.md), realized as Ford-circle
diameters.

## Role

- **Bifurcation universality.**  The saddle-node geometry at every
  tongue boundary gives the $\sqrt{\mu}$ escape law, which becomes
  the exponent 2 in the [Born rule](born_rule.md).
- **Duty-cycle basis.**  At $K = 1$ the fraction of the $\Omega$-axis
  occupied by $T_{p/q}$ is $1/q^2$; weighted by the orbit period $q$
  this gives the $1/q^3$ [duty function](duty_function.md), which
  is the empirical content of the duty-cycle basis for the
  cosmological partition.
- **Complete devil's staircase.**  At $K = 1$ the union of
  $\{T_{p/q}\}$ fills $[0, 1]$ up to a set of Lebesgue measure zero.
  The rotation number $W(\Omega, 1)$ is a Cantor function on this
  set — the **devil's staircase**.
