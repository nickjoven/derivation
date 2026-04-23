---
kind: topology_commitment
status: active
input_types: [3]
depends_on: [klein_bottle, sl2r_manifold]
consequences: [farey_partition, hierarchy, proof_C_bridge, dark_energy, mond_scale]
---

# Klein-quotient substrate commitment

## Commitment

The framework's cosmological and gauge mode content lives on the
quotient of a product of two [SL(2, R) manifold](sl2r_manifold.md)
factors by the antiperiodic half-twist of the
[Klein bottle](klein_bottle.md):

$$X_\text{Klein} \;=\; \bigl(\mathrm{SL}(2, \mathbb{R}) \times \mathrm{SL}(2, \mathbb{R})\bigr) \big/ \mathbb{Z}_2^\text{twist}.$$

The $\mathbb{Z}_2$ action is the half-twist
$(x, y) \sim (-x,\, 1 - y)$ on one factor (see
[`klein_bottle`](klein_bottle.md) §Definition).

## Relation to the repository

- [`klein_bottle`](klein_bottle.md) gives the quotient as a
  mathematical definition.  It does not commit the framework to
  using that quotient for physics; this entry does.
- [`sl2r_manifold`](sl2r_manifold.md) is the Type 3 input for the
  gravity chain (Proof A).  Klein lives on top of it, supplying a
  distinct Type 3 input for the cosmological and gauge sectors.
- [`farey_partition`](farey_partition.md) and
  [`hierarchy`](hierarchy.md) consume this commitment as the Type 3
  input that supplies $q_2 = 2$, $q_3 = 3$, $|F_6| = 13$,
  $|F_7| = 19$.  Their frontmatter now depends on this entry.

## Alternatives

- **Torus $T^2$ (orientable).**  Every denominator class survives
  the identification.  No non-trivial mode filter; no Farey
  partition at $q_2 q_3 = 6$.
- **Real projective plane $\mathbb{RP}^2$.**  Non-orientable but
  with a single reflection direction.  Rejected because the gauge
  sector's $\mathbb{Z}_2 \times \mathbb{Z}_3 = \mathbb{Z}_6$ center
  requires two independent reflections.
- **Sphere $S^2$.**  Trivial $\pi_1$; no mode-locking structure of
  the Farey type.

The rejections are commitments, not derivations from the
framework's primitives.

## Surviving integer content

Under the Klein XOR filter on mode pairs $(p_x, p_y)$,

$$p_x + p_y \;\equiv\; 1 \pmod 2,$$

the lowest-depth coprime survivors are:

| Symbol | Value | Origin |
|--------|-------|--------|
| $q_2$ | $2$ | smallest denominator class surviving XOR |
| $q_3$ | $3$ | smallest $q$ coprime to $q_2$ also surviving |
| $|F_6|$ | $13$ | [Farey count](farey_sequence.md) at $q_2 q_3 = 6$ |
| $|F_7|$ | $19$ | Farey count at $q_2 q_3 + 1$ |
| $d$ | $3$ | spatial dimension, consistent with $q_3$ |

These integers drive the cosmological predictions of Proof C
(Ω_Λ = 13/19, R = 6 · 13^54) and the matter-fraction predictions
(Ω_DM = 5/19, Ω_b = 1/19).

## Running count

After this entry the framework carries two Type 3 commitments:

1. [`sl2r_manifold`](sl2r_manifold.md) — the spatial manifold for
   the gravitational chain.
2. This entry — the Klein quotient for the gauge and cosmological
   content.

The two are independent; neither derives from the other.  Whether a
more primitive requirement (for example the existence of fermions,
which live in spinor bundles unavailable on orientable surfaces)
forces one from the other remains open.

## Remarks

- The commitment is ontological rather than derived.  Naming
  non-orientability as the physical selection rule is the
  substantive content: the framework cannot distinguish Klein-vs-torus
  from its primitives alone.
- The "half-twist of the product of two $\mathrm{SL}(2, \mathbb{R})$
  factors" construction was developed in the harmonics repo; only
  its substrate commitment ports forward here.
