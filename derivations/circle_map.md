---
kind: definition
status: active
input_types: []
depends_on: [integers, fixed_point]
consequences: [arnold_tongue, duty_function, rational_field_equation, continuum_limits]
citations:
  - "Arnold, Small denominators I (1961); standard reference: Guckenheimer & Holmes, §1.5"
---

# Circle map

## Definition

The **standard circle map** is the one-parameter family of maps
$f_{\Omega, K} : S^1 \to S^1$ defined by

$$\theta_{n+1} \;=\; \theta_n + \Omega - \frac{K}{2\pi}\,\sin(2\pi\,\theta_n)
  \pmod 1,$$

with bare frequency $\Omega \in [0, 1)$ and coupling strength
$K \in [0, 1]$.  The domain $S^1$ is $[0, 1]$ with endpoints
identified, i.e. the [fixed-point](fixed_point.md) closure
$\theta \equiv \theta + 1$ of the [integer](integers.md) translation.

## Rotation number

Each orbit has a well-defined rotation number

$$W(\Omega, K) \;=\; \lim_{n \to \infty} \frac{\theta_n - \theta_0}{n},$$

independent of the initial $\theta_0$ when the limit exists.  $W$ is
rational iff the orbit is periodic; it is $p/q$ iff
$f^{(q)}(\theta) = \theta + p$ has fixed points.

## Regimes

- **$K = 0$.**  Rigid rotation $\theta_{n+1} = \theta_n + \Omega$.
  $W(\Omega, 0) = \Omega$.
- **$0 < K < 1$.**  Mode-locking: $W$ is locally constant on open
  intervals of $\Omega$ at each rational value, forming
  [Arnold tongues](arnold_tongue.md).  The Lebesgue measure of the
  mode-locked set is strictly between $0$ and $1$.
- **$K = 1$.**  Critical coupling.  Tongues fill $[0, 1]$; the
  complement (unlocked orbits) has Lebesgue measure zero.  $f$ is
  still a homeomorphism but has a cubic inflection point at the
  origin.
- **$K > 1$.**  $f$ fails to be a homeomorphism; tongues overlap and
  orbits become chaotic.  The framework does not use this regime.

## Role

The circle map is the dynamical object on which every mode-locking
and bifurcation result in the framework rests.  In particular,
[continuum limits](continuum_limits.md) of the circle map yield the
Einstein field equations at $K = 1$ and the Schrödinger equation at
$K < 1$; see [Proof A](proof_A_gravity.md), [Proof B](proof_B_quantum.md).
