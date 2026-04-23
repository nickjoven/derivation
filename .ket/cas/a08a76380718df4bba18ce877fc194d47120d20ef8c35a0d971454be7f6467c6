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

Content present (44 entries):

- 4 axiomatic primitives (mathematical).
- 2 amplitude anchors (observational, Type 1 of the inputs taxonomy).
- 2 topology commitments (Type 3): `sl2r_manifold` (gravitational
  substrate) and `klein_substrate` (cosmological and gauge
  substrate).
- 1 identification (Type 4): `gauge_identification`.
- 1 universal constant (Type 6): `golden_ratio`.
- 7 definitions.
- 8 theorems.
- 3 proof chains: `proof_A_gravity` (primitives → Einstein),
  `proof_B_quantum` (primitives → Schrödinger + Born), `proof_C_bridge`
  (Λ → a₀ via Kuramoto critical coupling).
- 12 predictions with observable metadata: `dark_energy`,
  `mond_scale`, `spatial_dimension`, `lorentz_symmetry`, `born_rule`,
  `hierarchy_ratio`, `vacuum_energy`, `dark_matter_fraction`,
  `baryon_fraction`, `dm_baryon_ratio`, `gauge_group`,
  `anomaly_cancellation`.
- 4 open questions with explicit resolution criteria:
  `v_over_MP_gap`, `anchor_audit`, `baryon_sector_identification`,
  `topology_forcing`.
- 1 foundations document (`inputs_taxonomy.md`) — the six-type input
  scheme.

Schema-ready but unpopulated: `phase_label`.  (Consumer pending; no
prediction currently needs an explicit Type 5 entry.)

## What's next

Ordered queue, one commit per item unless noted:

1. Remaining predictions with new Type 6 infrastructure:
   - `strong_cp` (θ = 0 from Pin+(3) non-orientability)
   - `n_efolds`, `spectral_tilt` (need the MacKay exponent δ and
     possibly √5 as companion Type 6 constants)
   - `uncertainty` (ℏ from Proof B's Q4 diffusion coefficient)
   - Yang–Mills dynamics as a standalone theorem (Utiyama 1956).
2. Cosmological-sector identification entry (if
   `baryon_sector_identification` open question resolves in
   direction (1) or (2)).  Would formalize the {13, 5, 1} ↔
   {vacuum, DM, baryons} assignment.
3. Proslambenomenos extras: `kuramoto_einstein_mapping`,
   `lyapunov_uniqueness`, `renzos_rule_from_kuramoto`.  Port only
   what survives the filter.
4. Substrate seeding: `ket --home .ket init`, `ket put` each entry,
   `ket dag create` lineage.  Import foreign CIDs from harmonics
   for entries with prior substrate history.
5. Pages workflow (optional, defer).

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
