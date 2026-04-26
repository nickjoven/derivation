# Session handoff

Operational notes for picking up this repo after a session boundary.
If you're reading this in Claude Code, the richer per-file memory at
`~/.claude/projects/-home-njoven-AI-sandbox-derivation/memory/` has
already been loaded.  This file is the git-native summary for
everyone else.

## Where things stand

The repo was seeded on 2026-04-23 as the forward-carrying resolution
of [`harmonics`](https://github.com/nickjoven/harmonics) and
[`proslambenomenos`](https://github.com/nickjoven/proslambenomenos),
under the editorial filter "if it wouldn't be taught, it doesn't go
here" (see `CLAUDE.md`).

Content present (46 entries):

- 4 axiomatic primitives (mathematical).
- 2 amplitude anchors (observational, Type 1 of the inputs taxonomy).
- 2 topology commitments (Type 3): `sl2r_manifold` (gravitational
  substrate) and `klein_substrate` (cosmological and gauge
  substrate).
- 1 identification (Type 4): `gauge_identification`.
- 1 universal constant (Type 6): `golden_ratio`.
- 7 definitions.
- 9 theorems (now includes `yang_mills`: D_μ F^μν = J^ν from
  Utiyama 1956).
- 3 proof chains: `proof_A_gravity` (primitives → Einstein),
  `proof_B_quantum` (primitives → Schrödinger + Born), `proof_C_bridge`
  (Λ → a₀ via Kuramoto critical coupling).
- 13 predictions with observable metadata: `dark_energy`,
  `mond_scale`, `spatial_dimension`, `lorentz_symmetry`, `born_rule`,
  `hierarchy_ratio`, `vacuum_energy`, `dark_matter_fraction`,
  `baryon_fraction`, `dm_baryon_ratio`, `gauge_group`,
  `anomaly_cancellation`, `uncertainty`.
- 4 open questions with explicit resolution criteria:
  `v_over_MP_gap`, `anchor_audit`, `baryon_sector_identification`,
  `topology_forcing`.
- 1 foundations document (`inputs_taxonomy.md`) — the six-type input
  scheme.
- Content-addressed substrate: `.ket/` with 46 DAG nodes, CAS of
  ~51 blobs, tracked in git (Dolt index `.ket/ket.db/` is
  gitignored and rebuilds via `ket repair`).

Schema-ready but unpopulated: `phase_label`.  (Consumer pending; no
prediction currently needs an explicit Type 5 entry.)

## What's next

Ordered queue, one commit per item unless noted:

1. Proslambenomenos extras that survive the filter:
   `kuramoto_einstein_mapping` (ADM ↔ Kuramoto dictionary, porting
   as a theorem supporting Proof A's P7), `lyapunov_uniqueness`
   (dissipation argument, possibly a lemma for `continuum_limits`).
   `renzos_rule_from_kuramoto` is likely filter-blocked — the
   Renzo-rule claim was Class-4 conjectural in the harmonics
   audit and has no closed derivation.
2. Cosmological-sector identification entry, contingent on
   `baryon_sector_identification` open question resolving in
   direction (1) or (2).  Would formalize the {13, 5, 1} ↔
   {vacuum, DM, baryons} assignment and convert the ~11σ
   baryon-fraction residual into either a structural prediction
   or a revised identification.  Direction (1) is now under
   upstream activity in harmonics: a w_+ = 13/14 recognize-mode
   closure at q = 14 is recorded in the open-question entry's
   "Upstream activity" section with three named interpretive
   caveats; closing those caveats is what would lift it to a
   textbook prediction.
3. Pages workflow (optional, defer).
4. Cross-repo CID imports from harmonics for entries whose
   structural content was stabilized there first
   (farey_partition, hierarchy, klein_bottle).

## Filter-blocked (do not port)

Three predictions from the original queue hit the filter and are
not portable without new source material:

- **`spectral_tilt`**: the harmonics source is explicitly
  superseded (original cost-function approach produces wrong-sign
  running; the reframed approach does not close to a numerical
  prediction).  Port only if a reframed closed-form emerges.
- **`n_efolds`**: no standalone derivation in harmonics; references
  are scattered across framework_status.md and numerology_inventory.md.
  Port only if a standalone derivation is written upstream.
- **`strong_cp`**: the θ = 0 claim rests on a Pin+(3) non-orientability
  + vanishing-eta-invariant argument referenced only in the
  remark "D45" of `gauge_sector_lovelock.md`.  No derivation file
  exists.  Port only if someone writes the derivation; otherwise
  this belongs in an open-question entry, not a prediction.

These three are not pending; they are blocked by the "if it
wouldn't be taught, it doesn't go here" filter.

## Register, once more

Dry, not over-reaching.  Illustrative analogies OK; selling the
result is not.  Every theorem names where its proof load sits and
cites external uniqueness results when invoked.  Retracted material
from `harmonics` (Class 1 / Class 3 numerology, fitted corrections
like `+8/F_10²`, `+1/228`) stays in harmonics's git history and does
not port here.

The exemplars are `derivations/three_dimensions.md` (theorem),
`derivations/proof_A_gravity.md` (proof), and
`derivations/dark_energy.md` (prediction).

## How to resume

```sh
cd /home/njoven/AI/sandbox/derivation
git pull
python3 scripts/build_index.py       # verify generators clean
python3 scripts/build_manifest.py
# then pick item 1 from the "What's next" list above and port it
```

If a Catbus packet was handed off, consume it first; otherwise
`CLAUDE.md` + `derivations/inputs_taxonomy.md` + this file are the
minimum orientation.

## Pointers to source

- Harmonics: `/home/njoven/AI/sandbox/harmonics` (`main` branch,
  CAS 83 entries, 0 corrupt).  Honest-null audit commits on `main`
  ending at `163513d` (PR #72).
- Proslambenomenos: `/home/njoven/AI/sandbox/proslambenomenos`.
- Four open PRs in harmonics (#73, #74, #75 — plus an abandoned
  item 4) are informational, not blocking; decide per-PR whether to
  land or close independently of work here.
