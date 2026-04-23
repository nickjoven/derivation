---
kind: open_question
status: conjecture
input_types: [1]
depends_on: [hubble, vev, hierarchy, hierarchy_ratio]
consequences: []
citations:
  - "Weinberg, The cosmological constant problem (Rev. Mod. Phys. 61:1, 1989)"
  - "Dine, Fischler, Srednicki, A simple solution to the strong CP problem with a harmless axion (Phys. Lett. B 104:199, 1981)"
---

# The electroweak-to-Planck gap

## Statement

The two amplitude anchors [`hubble`](hubble.md) ($H_0$,
cosmological register) and [`vev`](vev.md) ($v_\text{EW} \approx
246\,\mathrm{GeV}$, particle register) carry independent
dimensionful content in different sectors.  Their ratio is

$$\frac{v_\text{EW}}{M_P} \;\approx\; \frac{246\,\mathrm{GeV}}{1.22 \cdot 10^{19}\,\mathrm{GeV}} \;\approx\; 2 \cdot 10^{-17},$$

and

$$\frac{H_0}{M_P} \;\approx\; \frac{1.4 \cdot 10^{-33}\,\mathrm{eV}}{1.22 \cdot 10^{28}\,\mathrm{eV}} \;\approx\; 10^{-61}.$$

The second ratio is delivered by
[`hierarchy_ratio`](hierarchy_ratio.md) as $1 / R = 1 / (6 \cdot
13^{54})$.  The first ratio is *not* delivered by any entry in this
repository.

**Question.**  Is the electroweak-to-Planck ratio derivable from the
framework's primitives + topology commitments + identifications, or
is it a genuine second Type 1 input in the particle sector?

## Resolution criterion

The question is *resolved* if any of the following is demonstrated:

1. **Derivation side.**  A derivation that produces $v_\text{EW} /
   M_P$ in terms of integers from the Klein substrate and one
   chosen amplitude anchor (either $H_0$ or $M_P$ — not both), with
   no free parameters and residual $\lesssim 10\%$.
2. **Anchor-reduction side.**  An identification
   ($\texttt{kind: identification}$) that fixes one of $\{H_0,
   v_\text{EW}\}$ in terms of the other and a structural ratio
   from `klein_substrate`, reducing the framework's Type 1 input
   count from 2 to 1.
3. **Independence proof.**  A proof (not just an enumeration) that
   the Type 1 input count cannot be reduced below 2 without
   introducing new primitives, confirming the conjecture that
   $v_\text{EW}$ and $H_0$ are genuinely independent anchors.

Any of (1), (2), (3) closes the open question.

## Status

Conjectural.  Two lines of attack are visible and unresolved:

- **Condensate scale.**  The electroweak scale is a vacuum
  condensate of the $\mathrm{SU}(2) \times \mathrm{U}(1)$ sector.
  Whether the condensate scale is set by a Kuramoto-type fixed
  point on the Klein substrate — and whether that fixed point has
  a dimensionless ratio to the Planck scale — is not settled.
  The harmonics-era attempt (`sinw_fixed_point.py`) found that
  tongue-width ratios do not reach $v / M_P$ at any $K \in [0.93,
  0.99]$, ruling out the simplest running scenario.  That is a
  negative result, not a resolution.
- **Proslambenomenos extension.**  The chain
  $\Lambda \to \nu_\Lambda \to H_0 \to a_0$ (see
  [Proof C](proof_C_bridge.md) §B7) links the cosmological anchor
  to a physical acceleration scale via the Kuramoto critical
  coupling.  A parallel chain for the particle sector — linking
  $v_\text{EW}$ to some dimensionless tongue-width ratio via the
  same critical-coupling mechanism — would resolve the question by
  construction (2) above.  Status: unconstructed.

## Why this matters

- If (1) or (2) resolves, the framework's independent-input count
  drops from 2 Type 1 amplitudes to 1, giving a total of
  $1 + 2 + 1 + 1 = 5$ inputs (one amplitude, two topologies, one
  identification, one universal constant).
- If (3) resolves, the count stays at $2 + 2 + 1 + 1 = 6$ but the
  question is closed.
- A resolution of this question is the canonical candidate for
  "removing the electroweak-to-Planck hierarchy" from the list of
  unexplained ratios in the Standard Model.  Its status is open.

## Relation to other open questions

- [`anchor_audit`](anchor_audit.md) asks the reverse question: can
  the two anchors be audited against each other for consistency,
  regardless of whether they can be reduced to one.  `v_over_MP_gap`
  is more ambitious than `anchor_audit`; both could be partially
  resolved even while the other remains open.
- The `baryon_sector_identification` question (pending entry) is
  narrower: it concerns the {5, 1}-orbit assignment in the
  19-element mode budget, not the amplitude hierarchy itself.

## Input-type accounting

- Type 1 declared because the question is about a ratio of two
  Type 1 amplitudes.  No Type 3, 4, 5, or 6 inputs are consumed by
  the question itself; they may be consumed by any eventual
  resolution.
