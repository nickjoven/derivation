---
kind: definition
status: active
depends_on: [integers, mediant, stern_brocot]
consequences: [farey_partition, arnold_tongue, duty_function]
citations:
  - "Hardy & Wright, An Introduction to the Theory of Numbers, Ch. III"
---

# Farey sequence

## Definition

The **Farey sequence of order $n$**, denoted $F_n$, is the set of
irreducible fractions in $[0, 1]$ with denominator at most $n$,
ordered by value:

$$F_n \;=\; \left\{\, p/q \in [0, 1] \;:\; \gcd(p, q) = 1,\;
                                          1 \leq q \leq n \,\right\}
       \cup \{\,0/1,\, 1/1\,\}.$$

The first few:

$$F_1 = \{0/1,\, 1/1\}, \quad
  F_2 = \{0/1,\, 1/2,\, 1/1\}, \quad
  F_3 = \{0/1,\, 1/3,\, 1/2,\, 2/3,\, 1/1\}.$$

## Key properties

- **Mediant closure.**  If $p/q$ and $p'/q'$ are consecutive in
  $F_n$, then $pq' - p'q = -1$ (Farey neighbors), and the [mediant](mediant.md)
  $(p + p')/(q + q')$ is the first fraction to appear *between* them
  in some later $F_m$.
- **Cardinality.**  $|F_n| = 1 + \sum_{k=1}^{n} \varphi_{\text{Euler}}(k)$,
  where $\varphi_{\text{Euler}}$ is Euler's totient.  For $n = 6$ this
  gives $|F_6| = 13$, the central integer in the framework's dark
  energy partition; see [`farey_partition`](farey_partition.md).
- **Gauss–Kuzmin distribution.**  The density of rationals in $F_n$
  near $p/q$ scales as $1/q^2$.  This is the measure-theoretic origin
  of the $1/q^2$ factor in the [Arnold tongue](arnold_tongue.md)
  width and — via the period factor $q$ from
  [circle map](circle_map.md) orbits — the $1/q^3$
  [duty function](duty_function.md) at $K = 1$.

## Role

Farey sequences index the mode-locked resonances of the circle map
at a given denominator cutoff.  The framework's Klein-bottle
partition selects the specific sequence $F_6$ (thirteen rationals) to
build the cosmological sector.
