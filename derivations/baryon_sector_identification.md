---
kind: open_question
status: conjecture
input_types: [4]
depends_on: [farey_partition, klein_substrate, baryon_fraction, dark_matter_fraction, gauge_identification]
consequences: []
---

# Cosmological-sector identification for the {5, 1} orbits

## Statement

The Klein XOR secondary split $6 = 5 + 1$ of the unlocked mode
budget (see [`dark_matter_fraction`](dark_matter_fraction.md),
[`baryon_fraction`](baryon_fraction.md)) produces two orbits
in the Farey-19 decomposition:

- a 5-orbit, currently identified with dark matter
  ($\Omega_\text{DM} = 5/19 \approx 0.263$, residual $\sim 0.2
  \sigma$);
- a 1-singleton, currently identified with baryonic matter
  ($\Omega_b = 1/19 \approx 0.0526$, residual $\sim 5.6 \sigma$).

The large $\sim 5.6\sigma$ tension on $\Omega_b$ versus the
$0.2\sigma$ agreement on $\Omega_\text{DM}$ is asymmetric: the
structural split $\{5, 1\}$ is exact, but the assignment of which
orbit to which cosmological sector is a Type 4 identification that
has not been entered formally.

**Question.**  Is the singleton orbit properly identified with
baryonic matter, or with a spectator cosmological sector (e.g.
relic radiation beyond the Standard Model, or a dark-sector
subcomponent distinct from the 5-orbit dark matter)?

## Resolution criterion

The question is resolved if any of the following is demonstrated:

1. **Confirmation.**  A Klein-substrate derivation of an
   additional Standard-Model-sector quantum number (lepton number,
   baryon number, or a related charge) that distinguishes the
   singleton from the 5-orbit, with an explicit mechanism forcing
   the singleton to be baryons.  The resulting $\Omega_b = 1/19$
   prediction would then be structural; the $\sim 5\%$ residual
   with Planck would be the genuine framework error and require
   separate accounting.
2. **Reassignment.**  A demonstration that the singleton orbit is
   better identified with a non-baryonic sector (for example, the
   cosmic-neutrino background contribution to $\Omega_\nu$, or a
   relic axion background), closing the baryon-fraction tension
   by revising the identification rather than the ratio.  The
   baryon fraction in this case becomes either unpredicted or
   predicted via a different structural route.
3. **Null result.**  A demonstration that the Klein substrate's
   structural split is not sufficient to determine the cosmological
   sector assignment, and that the assignment is *irreducibly* a
   Type 4 identification input that must be fit.  This would close
   the question as "the singleton's identification is a free
   Type 4 input" and require explicit acknowledgement in
   [`gauge_identification`](gauge_identification.md) that two
   identifications are needed (gauge + cosmological), not one.

## Status

Conjectural and narrow.  The issue does not affect the
dark-energy fraction $\Omega_\Lambda = 13/19$ (which uses only the
$\{13, 6\}$ split, not the secondary $\{5, 1\}$), and does not
affect the gravitational or quantum chains (Proofs A and B).
Its resolution would close the largest residual in the current
scorecard.

The companion identification entry
[`gauge_identification`](gauge_identification.md) covers the
Klein-to-gauge map.  A parallel
[`cosmological_identification`](cosmological_identification.md)
entry (currently absent) would cover the Klein-to-cosmology map
and would be the natural place to settle this question if (1) or
(2) above is attempted.

## Why this matters

The baryon-fraction tension is the framework's most visible
numerical embarrassment.  Resolving it either gives a cleaner
prediction (under (1)), a revision of the identification (under
(2)), or an honest acknowledgement of an additional Type 4 input
(under (3)).  Any of the three improves the framework's claims of
inputs.

## Input-type accounting

- Type 4 declared because the question is about whether the
  assignment is a forced structural identification or a free
  identification input.  No amplitude, topology, phase-label, or
  universal-constant input is consumed.
