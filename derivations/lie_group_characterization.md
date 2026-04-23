---
kind: theorem
status: active
depends_on: [mediant, three_dimensions]
consequences: [three_dimensions, minkowski_signature]
citations:
  - "Bianchi, Sugli spazi a tre dimensioni che ammettono un gruppo continuo di movimenti (1898)"
---

# Lie group characterization

## Statement

Among connected three-dimensional real Lie groups, $\mathrm{SL}(2,
\mathbb{R})$ is the unique simple non-compact group whose Iwasawa
decomposition admits a single compact $\mathrm{SO}(2)$ factor.

## Proof (sketch)

The Bianchi classification (1898) enumerates three-dimensional Lie
algebras over $\mathbb{R}$ up to isomorphism:

- **Abelian**: $\mathbb{R}^3$ (Bianchi type I).
- **Nilpotent**: Heisenberg (type II).
- **Solvable, non-nilpotent**: types III–VII.
- **Semisimple**: types VIII ($\mathfrak{sl}(2, \mathbb{R})$) and IX
  ($\mathfrak{so}(3) = \mathfrak{su}(2)$).

The compact case is type IX ($\mathrm{SO}(3)$ or $\mathrm{SU}(2)$);
the non-compact semisimple case is type VIII.  Only the type VIII
group, $\mathrm{SL}(2, \mathbb{R})$ (or its cover), carries the
Iwasawa decomposition $KAN$ with a single $\mathrm{SO}(2)$ compact
factor, a one-parameter boost subgroup $A$, and a unipotent subgroup
$N$.

The Heisenberg and solvable cases fail the semisimplicity required
for the [mediant](mediant.md) action to extend transitively to
matrix multiplication with determinant one; $\mathrm{SO}(3)$ fails
the non-compactness required for the hyperbolic geometry of the
Farey tiling.  Thus $\mathrm{SL}(2, \mathbb{R})$ is singled out.

## Role

This theorem is the external input invoked in step 3 of
[`three_dimensions`](three_dimensions.md): it is what makes
"the Lie group whose Iwasawa decomposition matches the circle-map
kinematics" well-defined and unique.

## Remarks

- The Iwasawa $KAN$ factors also supply the three spatial directions
  of the framework: compact rotation ($K$), radial boost ($A$), and
  translation ($N$).  The interpretation of these as
  Lorentzian-signature factors is developed in
  [`minkowski_signature`](minkowski_signature.md).
