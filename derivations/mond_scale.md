---
kind: prediction
status: active
input_types: [1, 3, 6]
depends_on:
  - hubble
  - klein_substrate
  - farey_partition
  - hierarchy
  - golden_ratio
  - rational_field_equation
  - continuum_limits
consequences: []
observables:
  - name: MOND acceleration scale a_0
    predicted: c * H_0 / (2 * pi * sqrt(g_*(1/varphi))) ≈ 1.25e-10 m/s^2
    observed: 1.2e-10 m/s^2 ± 0.1e-10 (McGaugh et al. 2016)
    residual: ~4% relative to observed central value
citations:
  - "Milgrom, A modification of the Newtonian dynamics (Astrophys. J. 270:365, 1983)"
  - "McGaugh, Lelli, Schombert, Radial Acceleration Relation in Rotationally Supported Galaxies (Phys. Rev. Lett. 117:201101, 2016)"
  - "Strogatz, From Kuramoto to Crawford (Physica D 143:1, 2000)"
---

# MOND acceleration scale

## Statement

The MOND acceleration scale is

$$a_0 \;=\; \frac{c\, H_0}{2\pi \sqrt{g_*(1 / \varphi)}},$$

where $c$ is the speed of light, $H_0$ is the Hubble parameter,
$\varphi$ is the [golden ratio](golden_ratio.md), and
$g_*(1 / \varphi) \approx 0.697$ is the self-consistent frequency
distribution of the unlocked oscillator population of the
[rational field equation](rational_field_equation.md) at the
devil's-staircase pivot.

Numerically

$$a_0 \;\approx\; 1.25 \cdot 10^{-10}\,\mathrm{m\,s^{-2}},$$

against the observed $a_0 \approx 1.2 \cdot 10^{-10}\,
\mathrm{m\,s^{-2}}$ (McGaugh 2016): residual $\sim 4\%$.

## Derivation

Three steps.  Steps 1 and 2 are standard cosmology.  Step 3 is the
framework's input.

### 1. Friedmann: $\Lambda \to \nu_\Lambda$

The cosmological constant sets a reference frequency via the
Friedmann equation,

$$\nu_\Lambda \;=\; c \sqrt{\Lambda / 3},$$

the de Sitter limit of the Hubble rate.

### 2. Present Hubble rate

At the present epoch
$H_0 = \nu_\Lambda / \sqrt{\Omega_\Lambda}$, with $\Omega_\Lambda =
13 / 19$ supplied by [`farey_partition`](farey_partition.md).
Equivalently, $\nu_\Lambda = H_0 \sqrt{\Omega_\Lambda}$.

### 3. Kuramoto critical coupling: $H_0 \to a_0$

At mean-field Kuramoto synchronization, the critical coupling for a
population with frequency distribution $g(\omega)$ is

$$K_c \;=\; \frac{2}{\pi\, g(0)}.$$

For the unlocked sector of the
[rational field equation](rational_field_equation.md), the
self-consistent distribution $g_*(\omega)$ takes its value at the
devil's-staircase pivot $\omega_\text{pivot} = \omega_\text{ref} /
\varphi$, giving $g_*(1 / \varphi) \approx 0.697$.  (The pivot value
is inherited from universal circle-map dynamics at $K = 1$; see
[`continuum_limits`](continuum_limits.md) and
[`golden_ratio`](golden_ratio.md).)

The Kuramoto desynchronization acceleration scale is

$$a_0 \;=\; \frac{c\, H_0}{2\pi \sqrt{g_*(1 / \varphi)}}.$$

With $c = 2.998 \cdot 10^8\,\mathrm{m\,s^{-1}}$,
$H_0 = 2.17 \cdot 10^{-18}\,\mathrm{s^{-1}}$:

$$a_0 \;\approx\; \frac{(2.998 \cdot 10^8)\,(2.17 \cdot 10^{-18})}
                       {2\pi \sqrt{0.697}}
     \;\approx\; 1.25 \cdot 10^{-10}\,\mathrm{m\,s^{-2}}.$$

## Where the load sits

- **Step 1**: standard cosmology.  No framework content.
- **Step 2**: $\Omega_\Lambda = 13 / 19$ from
  [`farey_partition`](farey_partition.md).  Framework content.
- **Step 3**: two load-bearing claims, one external and one
  internal.
  - *External*: the Kuramoto critical-coupling formula $K_c =
    2 / (\pi\, g(0))$ (standard Kuramoto theory; Strogatz 2000
    reviews it).
  - *Internal*: evaluation of the self-consistent distribution at
    $1 / \varphi$.  Rests on the devil's-staircase pivot at
    $K = 1$; cited as inherited from circle-map universality.

## Residual

The $4\%$ residual between $1.25 \cdot 10^{-10}$ and the observed
$\sim 1.2 \cdot 10^{-10}$ is within the systematic uncertainty of
the McGaugh 2016 radial-acceleration-relation fit.  The bare
$c H_0 / (2\pi) \approx 1.04 \cdot 10^{-10}$ (without the $g_*$
factor) has $\sim 13\%$ residual; the $\sqrt{g_*}$ correction
drops it to $\sim 4\%$.  Sign of the correction is fixed by
$g_* < 1$, not fit.

## Scope

- The value of $a_0$ is derived.  The MOND phenomenology at
  $a \ll a_0$ (flat rotation curves, radial-acceleration relation)
  is not claimed to be derived here.  The dynamics below $a_0$ are
  governed by the rational field equation's continuum limit;
  deriving the MOND interpolation function from the framework's
  oscillator dynamics is a pending open item.
- The choice of Planck $H_0$ versus local $H_0$ shifts the
  prediction by $\sim 9\%$, comparable to the residual itself.
  The Hubble-tension ambiguity propagates here.

## Input-type accounting

- Type 1: the [Hubble anchor](hubble.md).
- Type 3: via [`klein_substrate`](klein_substrate.md), through the
  $\Omega_\Lambda = 13 / 19$ chain.
- Type 6: the [golden ratio](golden_ratio.md) at the
  devil's-staircase pivot.

No Type 4 identification is consumed: the assignment "unlocked
sector frequency distribution $=$ vacuum oscillation distribution"
is not introduced as an identification input; it is the content
of the Kuramoto-to-cosmology mapping sketched at step 3.
