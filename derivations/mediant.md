---
kind: axiom
status: active
depends_on: [integers]
consequences: [stern_brocot, farey_sequence, three_dimensions]
---

# Mediant

## Axiom

For two fractions $a/b$ and $c/d$ with $b, d > 0$, the **mediant** is

$$\frac{a}{b} \oplus \frac{c}{d} \;:=\; \frac{a + c}{b + d}.$$

The mediant is not ordinary addition of fractions.  It is the
column-sum of the matrix

$$M = \begin{pmatrix} a & c \\ b & d \end{pmatrix},$$

and the operation $\oplus$ is the unique binary operation on positive
fractions satisfying (i) strict intermediacy between its operands and
(ii) Farey-neighbor preservation: if $|ad - bc| = 1$ then both
$(a/b, a \oplus c/d)$ and $(a \oplus c/d, c/d)$ are Farey neighbors.

## Role

The mediant generates the [Stern-Brocot tree](stern_brocot.md) by
iteration: starting from the boundary pair $(0/1, 1/0)$, every
positive rational appears exactly once as the mediant of its
predecessors.

Under the continuum limit, the action on pairs $(a/b, c/d)$ extends
to $\mathrm{SL}(2,\mathbb{Z}) \to \mathrm{SL}(2,\mathbb{R})$ acting
on the upper half plane.  This extension is what supplies the
[three-dimensional](three_dimensions.md) spatial structure of the
framework.
