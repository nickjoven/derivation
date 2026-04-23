---
kind: theorem
status: active
input_types: [1, 3]
depends_on: [klein_bottle, farey_partition, three_dimensions, hubble]
consequences: [vacuum_energy, mond_scale]
---

# Hierarchy

## Statement

The ratio of the Planck length to the Hubble length is

$$R \;=\; \frac{\ell_H}{\ell_P} \;=\; q_2 q_3 \cdot |F_6|^{\,q_2 q_3^d}
      \;=\; 6 \cdot 13^{54},$$

where the [Klein-bottle](klein_bottle.md) integers are $q_2 = 2$,
$q_3 = 3$, $|F_6| = 13$, and $d = 3$ is the spatial dimension
([three_dimensions](three_dimensions.md)).

Numerically, $R = 6 \cdot 13^{54} \approx 8.53 \times 10^{60}$,
compared with the observed
$R_\text{obs} = \ell_H / \ell_P \approx 8.49 \times 10^{60}$ from
the Planck-2018 [Hubble anchor](hubble.md) (residual 0.48%).

## Proof sketch

The argument counts distinguishable states between the Hubble scale
and the Planck scale on the framework's Stern-Brocot substrate.

- **Depth factor $|F_6|^{q_2 q_3^d}$.**  Each refinement level of
  the Farey tiling at $q_2 q_3 = 6$ introduces $|F_6| = 13$ new
  states.  The framework's closure condition forces this refinement
  to iterate $q_2 q_3^d = 2 \cdot 27 = 54$ times before the scale
  runs out.  The $d$-dependence comes from the $d$-dimensional
  volume of the Klein bottle's image under the Iwasawa $KAN$
  coordinates.
- **Prefactor $q_2 q_3 = 6$.**  Accounts for the six unlocked-mode
  channels at the deepest refinement — one per element of
  $F_7 \setminus F_6$.

Multiplying: $R = 6 \cdot 13^{54}$.  Derivation appears in the
archived source under `hierarchy_gaussian_lattice.md`.

## Corollary: vacuum energy

The cosmological constant in Planck units is

$$\Lambda \ell_P^2 \;=\; 3 \Omega_\Lambda \left(\frac{\ell_P}{\ell_H}\right)^2
                     \;=\; \frac{3 \cdot 13/19}{(6 \cdot 13^{54})^2}
                     \;=\; \frac{13^{-108}}{12},$$

using [`farey_partition`](farey_partition.md)'s $\Omega_\Lambda =
13/19$.  Numerically this is $\sim 10^{-121.5}$, matching the
observed vacuum-energy density to $\sim 0.1\%$ in the exponent; see
[`vacuum_energy`](vacuum_energy.md).

## Remarks

- The $d$ in the exponent is not a fit parameter: it is the same
  spatial dimension that appears in the
  [duty function](duty_function.md) and in
  [`three_dimensions`](three_dimensions.md).  The three occurrences
  are the same integer.
- The Planck length itself is not derived; it enters via the
  [Hubble anchor](hubble.md) combined with the above identity.
  Fixing either $\ell_H$ or $\ell_P$ fixes the other, and this
  theorem supplies the ratio between them.
