---
kind: axiom
status: active
depends_on: []
consequences: [circle_map, rational_field_equation]
---

# Fixed point

## Axiom

A **fixed point** of a map $f: X \to X$ is a point $x \in X$ such that

$$x = f(x).$$

Self-consistency — the requirement that a dynamical law's solution is
a fixed point of the law itself — is taken as primitive in the
framework, alongside the integers, the [mediant](mediant.md), and the
[parabola](parabola.md).

## Role

Three uses:

- **Topology of phase space.** Integer cycle counts combined with a
  fixed-point closure collapse the line to the circle $S^1$: the
  identification $p \equiv 0$ (period $2\pi$) is the fixed-point
  condition on the translation $x \mapsto x + 2\pi$.
- **Dynamics.** The [circle map](circle_map.md)
  $\theta_{n+1} = f(\theta_n)$ is iterated; mode-locking is the
  existence of a periodic fixed point of $f^{(q)}$.
- **Self-consistent field equations.** The
  [rational field equation](rational_field_equation.md) populates
  Stern-Brocot denominators by the requirement that the population
  distribution $N$ satisfies $N = F[N]$ for a stated functional $F$.

The fixed-point axiom enters every proof chain at the step where
closure is needed.
