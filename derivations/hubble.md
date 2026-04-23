---
kind: axiom
status: active
depends_on: []
consequences: [hierarchy, mond_scale, vacuum_energy]
citations:
  - "Planck 2018 results. VI. Cosmological parameters (A&A 641, A6, 2020)"
---

# Hubble anchor

## Axiom (observational)

The cosmological sector takes one dimensional input: the present-day
expansion rate of the universe,

$$H_0 \;=\; 67.4 \pm 0.5 \ \mathrm{km\,s^{-1}\,Mpc^{-1}}
       \;=\; 2.184 \times 10^{-18} \ \mathrm{s^{-1}},$$

from Planck 2018.  Equivalently, by the Friedmann equation for flat
$\Lambda$CDM, $\Lambda = 3\,\Omega_\Lambda H_0^2 / c^2$ and the Hubble
radius $\ell_H = c/H_0$ may be substituted without loss of information.

No attempt to derive $H_0$ from the framework's mathematical
primitives has succeeded; this entry states it as given.  The
[`v/M_P` open question](v_over_mp_gap.md) is the specific structural
gap whose closure would reduce the anchor count to one.

## Covers

Given $H_0$, the framework expresses the following as dimensionless
identities or simple consequences:

- $\Lambda$: via $\Omega_\Lambda = 13/19$ from the
  [Farey partition](farey_partition.md).
- $\ell_P$, $t_P$, $M_P$ (in natural units): via the
  [hierarchy theorem](hierarchy.md) $R = 6 \cdot 13^{54}$.
- $a_0$ (MOND scale): via the [$\Lambda \to a_0$ bridge](proof_C_bridge.md).
- Cosmic-timeline scales: by standard cosmology from $H_0$ and
  $\Omega_\Lambda$.

## Status

Observational anchor.  Independent of the particle-sector anchor
[`vev`](vev.md).  Anchor count is two; see the
[anchor audit](anchor_audit.md) for why it does not yet close to one.
