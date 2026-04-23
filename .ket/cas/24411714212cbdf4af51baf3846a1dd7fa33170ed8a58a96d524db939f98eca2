---
kind: theorem
status: active
input_types: []
depends_on: [three_dimensions, klein_bottle, lie_group_characterization]
consequences: [proof_A_gravity]
---

# Minkowski signature

## Statement

Complexifying the spatial group $\mathrm{SL}(2, \mathbb{R})$
([three_dimensions](three_dimensions.md)) gives $\mathrm{SL}(2,
\mathbb{C})$, whose universal cover is a double cover of the
identity component of the Lorentz group $\mathrm{SO}^+(3, 1)$.  The
framework's spacetime thus carries signature $(3, 1)$ (three spatial,
one temporal).

## Proof

Write $\mathrm{SL}(2, \mathbb{C})$ as the set of $2 \times 2$ complex
matrices with $\det = 1$.  Its real dimension is
$2 \cdot (4) - 2 = 6$, matching the dimension of $\mathrm{SO}(3, 1)$.

The standard Möbius action of $\mathrm{SL}(2, \mathbb{C})$ on
$\mathbb{CP}^1 \cong S^2$ extends to an action on the forward null
cone in $\mathbb{R}^{3, 1}$, and this descends to a group homomorphism

$$\mathrm{SL}(2, \mathbb{C}) \;\twoheadrightarrow\; \mathrm{SO}^+(3, 1)$$

with kernel $\{\pm I\}$.  Explicitly, a four-vector
$(t, x, y, z) \in \mathbb{R}^{3, 1}$ corresponds to the Hermitian matrix

$$X \;=\; \begin{pmatrix} t + z & x - i y \\ x + i y & t - z \end{pmatrix},$$

with $\det X = t^2 - x^2 - y^2 - z^2$, and the action $X \mapsto g X
g^\dagger$ for $g \in \mathrm{SL}(2, \mathbb{C})$ preserves the
determinant, hence the Minkowski interval.

The real form of $\mathrm{SL}(2, \mathbb{C})$ under the involution
fixing $\mathrm{SL}(2, \mathbb{R})$ singles out the three spatial
boosts as imaginary-time extensions of the real $\mathrm{SL}(2,
\mathbb{R})$ generators; the surviving fourth direction is the time
axis.  Signature $(3, 1)$ is the content of this real-form
decomposition.

## Role

- Locks the spacetime signature for the continuum limit at
  [$K = 1$](continuum_limits.md).  The ADM decomposition assumes
  Lorentzian signature; here that assumption is a theorem.
- Consistent with the [Klein-bottle](klein_bottle.md) orbit
  decomposition under $r \mapsto 1 - r$: three pair orbits (spatial
  directions) plus one fixed point (time), for $n = 4$ in $F_n$.

## Remarks

- The same $\mathrm{SL}(2, \mathbb{C})$ appears in twistor theory
  and in spinor formulations of general relativity; the framework's
  use of it is consistent with those references.  No new geometric
  construction is introduced here.
