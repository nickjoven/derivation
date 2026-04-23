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

Content present (20 entries):

- 4 axiomatic primitives (mathematical).
- 2 amplitude anchors (observational, Type 1 of the inputs taxonomy).
- 6 definitions.
- 7 theorems.
- 1 foundations document (`inputs_taxonomy.md`) — the six-type input
  scheme (amplitude / ratio / topology / identification / phase /
  universal), with the musical analogy and the composition rules.

Schema-ready but unpopulated:
`topology_commitment`, `identification`, `phase_label`,
`universal_constant`.  These will be populated as proofs and
predictions that consume them are ported.

## What's next

Ordered queue, one commit per item unless noted:

1. `proof_A_gravity.md` — 8-proposition Einstein chain.
2. `proof_B_quantum.md` — 6-proposition Schrödinger + Born chain,
   shares P1–P5 with A.
3. `proof_C_bridge.md` — 7-proposition Λ → a₀ chain
   (proslambenomenos source).
4. First `identification` entry (gauge sector-to-mode mapping).
5. Predictions layer (~15 entries).
6. Open questions (at least `v_over_MP_gap`, `anchor_audit`).
7. Proslambenomenos-specific lemmas (Kuramoto–Einstein mapping,
   Lyapunov uniqueness, Renzo's Rule).
8. Substrate seeding in `.ket/`.
9. Pages workflow (optional, defer).

## Register

Dry, not over-reaching.  Illustrative analogies OK; selling the
result is not.  Every theorem names where its proof load sits and
cites external uniqueness results when invoked.  Retracted material
from `harmonics` (Class 1 / Class 3 numerology, fitted corrections
like `+8/F_10²`, `+1/228`) stays in harmonics's git history and does
not port here.

The exemplar is `derivations/three_dimensions.md`.  Match its
register on every new entry.

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
