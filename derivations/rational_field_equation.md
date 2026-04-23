---
kind: definition
status: active
depends_on: [integers, fixed_point, stern_brocot, arnold_tongue]
consequences: [continuum_limits, proof_A_gravity, proof_B_quantum]
---

# Rational field equation

## Definition

The **rational field equation** is the self-consistency condition on
a population $N : \mathbb{Q}_+ \to \mathbb{R}_{\geq 0}$ indexed by the
nodes of the [Stern-Brocot tree](stern_brocot.md):

$$N(p/q) \;=\; N_\text{total} \cdot g(p/q) \cdot w\!\left(p/q,\; K_0 F[N]\right),$$

where

- $N_\text{total} = \sum_{p/q} N(p/q)$ is the total population,
- $g : \mathbb{Q}_+ \to [0, 1]$ is the bare density (a normalized
  weight; for the Gauss–Kuzmin measure on rationals, $g(p/q) \propto
  1/q^2$),
- $w(p/q, K)$ is the [Arnold-tongue](arnold_tongue.md) width at
  $p/q$ for coupling $K$,
- $K_0$ is a coupling amplitude,
- $F[N]$ is a functional of the population returning an effective
  coupling.

The equation is solved at a fixed Stern-Brocot depth truncation;
increasing the depth is the approach to the continuum limit.

## Fixed-point structure

By the [fixed-point](fixed_point.md) axiom, a solution $N^*$ of the
rational field equation is a fixed point of the right-hand-side map
$\mathcal{T}[N] = N_\text{total} g \cdot w(\cdot, K_0 F[N])$.  For the
framework's chosen $g$, $w$, and $F$ this map is a contraction on a
suitable function space at each fixed truncation depth, so $N^*$
exists and is unique per depth.

## Role

The rational field equation is the common ancestor of both proof
chains:

- At $K = 1$, the [continuum limit](continuum_limits.md) of the
  equation produces the ADM evolution equations, from which
  [Proof A](proof_A_gravity.md) derives the Einstein field equations.
- At $K < 1$, the same continuum limit produces the Madelung
  hydrodynamic system, from which [Proof B](proof_B_quantum.md)
  derives the Schrödinger equation.

No other equation is imposed on the framework; the rational field
equation plus the four axioms is the full dynamical content.
