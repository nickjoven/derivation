---
kind: open_question
status: conjecture
input_types: [1]
depends_on: [hubble, vev, inputs_taxonomy]
consequences: []
---

# Anchor audit

## Statement

The framework carries two Type 1 amplitude anchors:
[`hubble`](hubble.md) ($H_0 \approx 67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}$,
Planck 2018) and [`vev`](vev.md) ($v_\text{EW} \approx 246\,
\mathrm{GeV}$).  The six-type input taxonomy
([`inputs_taxonomy`](inputs_taxonomy.md)) specifies that Type 1
anchors set the dimensional scale within one sector each, with no
derivable content across sectors.

**Question.**  Given the framework's structural ratios (Type 2,
derived from Types 3, 4, 5, 6), is the pair of anchors
$\{H_0, v_\text{EW}\}$ *self-consistent* at the $\mathcal{O}(1)$
level within the framework?  That is, do the dimensionless ratios
predicted in the cosmological and particle sectors match each
other's predictions when both anchors are held fixed?

## Resolution criterion

The question is resolved if a table can be assembled with the
following structure:

| Structural ratio | Prediction using $H_0$ only | Prediction using $v_\text{EW}$ only | Overlap check |
|------------------|-----------------------------|-------------------------------------|---------------|
| (each observable amplitude, converted to the common Planck-scale reference) | (Hubble-anchored derivation) | (vev-anchored derivation) | (match within stated residual?) |

and the overlap check passes at the $\mathcal{O}(1)$ level for
every observable that both anchors reach.  "Passes" means the two
anchor-based predictions of a single observable agree with each
other to within the Hubble-tension spread ($\sim 8\%$) or tighter.

If the overlap check fails on any observable, the question resolves
in the negative direction: one (or both) anchors is miscalibrated
or mis-identified with its physical sector.

## Status

Conjectural.  The audit has not been performed end-to-end in this
repository.  Informally:

- Cosmological observables ($\Omega_\Lambda$, $R$, $a_0$, $\Lambda
  \ell_P^2$) use $H_0$ via [`hubble`](hubble.md); residuals are
  $0.07\sigma$, $0.48\%$, $4\%$, and $\sim 50\%$ on the bare
  number of $\Lambda \ell_P^2$ (or $\sim 0.15\%$ in the log).
- Particle-sector observables that have been attempted in the
  archived harmonics content (gauge-coupling ratios, Higgs-vev
  ratios) use $v_\text{EW}$ via [`vev`](vev.md); the
  harmonics-era fits do not currently port here because the
  honest-null audit demoted them below teaching threshold.

The audit question has two parts:

1. **Internal consistency.**  Given the two anchors, do the
   observables in each sector agree with observation to within
   each anchor's uncertainty?  *Cosmological sector: yes (see
   predictions above).  Particle sector: not yet audited in this
   repository.*
2. **Cross-sector consistency.**  Are there observables that can
   be predicted from both anchors independently, and do the two
   predictions agree?  *Planck-to-Hubble ratio is one candidate
   ([`hierarchy_ratio`](hierarchy_ratio.md) uses only $H_0$; a
   parallel derivation from $v_\text{EW}$ is unconstructed).*

Both parts are open.

## Relation to other open questions

- [`v_over_MP_gap`](v_over_MP_gap.md) asks whether the two anchors
  are *independent* (a strong, derivation-level question).
  `anchor_audit` asks whether they are *consistent* (a weaker,
  verification-level question).  Resolution of `v_over_MP_gap` in
  direction (1) or (2) would also resolve `anchor_audit`
  automatically; resolution of `anchor_audit` alone would not
  resolve `v_over_MP_gap`.
- The $\sim 5.6\sigma$ residual on [`baryon_fraction`](baryon_fraction.md)
  is not an anchor issue per se (the baryon fraction is
  dimensionless), but any resolution via re-examining the
  cosmological-sector identification would feed back into this
  audit.

## Why this matters

The audit's purpose is to put a concrete, teachable bound on the
framework's internal coherence.  A successful audit says: given
the two anchors, the framework is self-consistent across sectors
to within stated residuals.  A failed audit says: at least one
anchor is misplaced.

## Input-type accounting

- Type 1 declared because the question is about Type 1 anchors'
  mutual consistency.  No Type 3, 4, 5, or 6 inputs are consumed
  by the question itself.
