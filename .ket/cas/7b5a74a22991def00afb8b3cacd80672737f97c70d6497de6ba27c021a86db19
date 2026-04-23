---
kind: universal_constant
status: active
input_types: [6]
depends_on: []
consequences: [mond_scale]
citations:
  - "Hardy & Wright, An Introduction to the Theory of Numbers, §11.8"
  - "Shenker, Scaling behavior in a map of a circle onto itself (Physica 5D, 1982)"
  - "Feigenbaum, Kadanoff, Shenker, Quasiperiodicity in dissipative systems (Physica 5D, 1982)"
---

# Golden ratio

## Constant

The golden ratio is the positive root of $x^2 - x - 1 = 0$:

$$\varphi \;=\; \frac{1 + \sqrt 5}{2} \;=\; 1.61803\ldots$$

The reciprocal $1 / \varphi = \varphi - 1 \approx 0.618\ldots$ has
continued-fraction expansion $[0;\, 1, 1, 1, \ldots]$; every
partial quotient is $1$.

## Universal role in circle-map dynamics

In one-dimensional [circle-map](circle_map.md) dynamics, the
rotation number $1 / \varphi$ is the accumulation point of the
[Stern-Brocot](stern_brocot.md) deep structure.  By the
Gauss–Kuzmin distribution, $1 / \varphi$ is the "most generic"
irrational in a precise measure-theoretic sense.

Shenker (1982) established that at the critical coupling $K = 1$,
the scaling of rotation-number plateaus near $1 / \varphi$ obeys
universal exponents independent of the specific one-parameter
family of circle maps.  Feigenbaum–Kadanoff–Shenker (1982)
completed the list of universal constants.  These constants belong
to circle-map dynamics as a class, not to any particular family.

## Why Type 6

The golden ratio appears in the framework as a property of the
universal dynamics of one-dimensional circle maps, not as a
framework input.  Any family of circle maps at critical coupling
exhibits golden-ratio-related universal constants: the value is
inherited, not chosen.

The framework consumes $\varphi$ at:

- [`mond_scale`](mond_scale.md) via the evaluation
  $g_*(1 / \varphi) \approx 0.697$ of the self-consistent
  frequency distribution at the devil's-staircase pivot.
- Pending: the spectral-tilt prediction $n_s - 1 \propto
  \log \varphi$ (see harmonics `n_efolds` derivation); the
  MacKay universal exponent $\delta_\text{MacKay}$ in quasiperiodic
  breakdown, which enters any prediction depending on torus
  decoherence.

## Remarks

- $\varphi$ and $\sqrt 5$ are not claims to be derived; they are
  imported mathematical facts about $x^2 - x - 1 = 0$.  Listing
  them as `universal_constant` entries is bookkeeping, so every
  prediction that consumes them can declare Type 6 honestly.
- Two standard notations: $\varphi = [1;\, 1, 1, 1, \ldots]$ and
  $1 / \varphi = [0;\, 1, 1, 1, \ldots]$.  The reciprocal form is
  what appears at the devil's-staircase pivot.
- The $\sqrt 5$ in the spectral-tilt chain is another Type 6
  constant that will land when the spectral-tilt prediction is
  ported.  Whether it needs its own entry or can be covered under
  `golden_ratio` is a book-keeping decision to be made then.
