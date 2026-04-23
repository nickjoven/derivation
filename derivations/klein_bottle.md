---
kind: definition
status: active
depends_on: [integers, fixed_point, three_dimensions]
consequences: [minkowski_signature, farey_partition, hierarchy, duty_function]
---

# Klein bottle

## Definition

The **Klein bottle** $K^2$ is the closed non-orientable surface
obtained as the quotient of the unit square $[0, 1]^2$ by the
identifications

$$(x, 0) \sim (x, 1), \qquad (0, y) \sim (1,\, 1 - y).$$

The first identification makes $y$ periodic; the second makes $x$
periodic up to an orientation-reversing flip in $y$ ("antiperiodic
with a half-twist").  Equivalently, $K^2$ is the quotient of the
2-torus $T^2 = S^1 \times S^1$ by a free $\mathbb{Z}_2$-action
reversing orientation in one factor.

## Role in the framework

The framework uses the Klein-bottle identification on the product
space of two [SL(2, R)](three_dimensions.md) factors.  The
antiperiodic half-twist selects denominator classes $(q_2, q_3) =
(2, 3)$ via an XOR filter on the mode structure: modes surviving the
identification must be invariant under the half-twist, which in
denominator coordinates is a parity condition that only $q = 2$ and
$q = 3$ satisfy simultaneously.

The surviving integer content of $K^2$ is:

| Symbol | Value | Source |
|--------|-------|--------|
| $q_2$ | $2$ | smallest denominator class surviving XOR |
| $q_3$ | $3$ | smallest $q$ coprime to $q_2$ also surviving |
| $|F_6|$ | $13$ | [Farey count](farey_sequence.md) at $q_2 q_3 = 6$ |
| $|F_7|$ | $19$ | Farey count at $q_2 q_3 + 1$; total mode budget |
| $d$ | $3$ | spatial dimension, from [`three_dimensions`](three_dimensions.md) |

These integers propagate into every cosmological and gauge-sector
theorem; see [`farey_partition`](farey_partition.md),
[`hierarchy`](hierarchy.md), and the gauge-sector derivations.

## Remarks

- **Non-orientability is not a cosmetic choice.**  The half-twist is
  what forces the discrete $\mathbb{Z}_2 \times \mathbb{Z}_3 =
  \mathbb{Z}_6$ center appearing in the gauge sector; an orientable
  (torus) identification would preserve a different mode set and
  give a different gauge structure.
- **Signature.**  The antiperiodic identification induces the
  involution $r \mapsto 1 - r$ on the Farey set, whose orbit
  decomposition matches the signature $(3, 1)$ of Minkowski space;
  see [`minkowski_signature`](minkowski_signature.md).
