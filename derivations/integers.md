---
kind: axiom
status: active
depends_on: []
consequences: [mediant, fixed_point, circle_map]
---

# Integers

## Axiom

The set $\mathbb{Z}$ of integers is taken as given.  Cycle counts,
winding numbers, and denominator classes in the framework are all
integer-valued.

## Role

Integers supply countability to every later construction:

- Cycle counts $p$ in $p/q$ rotation numbers of the [circle map](circle_map.md).
- Denominators $q$ in Farey sequences and [Stern-Brocot](stern_brocot.md)
  enumeration.
- Winding numbers distinguishing topologically inequivalent maps on
  $S^1$.

No primitive below the integers is invoked.  In particular, the
continuum is not assumed: it enters only through the
[continuum limit](continuum_limits.md) of rational constructions as
denominators grow without bound.
