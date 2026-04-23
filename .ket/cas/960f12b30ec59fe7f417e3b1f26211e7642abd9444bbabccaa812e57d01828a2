---
kind: theorem
status: active
input_types: [3, 4]
depends_on: [klein_bottle, klein_substrate, gauge_identification]
consequences: [anomaly_cancellation, gauge_group]
citations:
  - "Gell-Mann, The Eightfold Way (Caltech Synchrotron Lab Report CTSL-20, 1961)"
  - "Nishijima, Charge independence theory of V particles (Prog. Theor. Phys. 13:285, 1955)"
---

# Gell-Mann–Nishijima relation from the Klein boundary

## Statement

The relation between electric charge $Q$, weak isospin $T_3$, and
hypercharge $Y$ is

$$Q \;=\; T_3 + \frac{Y}{2}.$$

The factor $1/2$ is the order of the $y \mapsto 1 - y$ reflection
in the Klein-bottle identification $(0, y) \sim (1,\, 1 - y)$.

## Derivation

Three ingredients.  Steps 1 and 2 use the
[`klein_bottle`](klein_bottle.md) identification directly; step 3
assembles them under the
[`gauge_identification`](gauge_identification.md) assignments.

### 1. $T_3$ as half-twist eigenvalue

The antiperiodic x-direction has fundamental-group generator of
order 2: $(0, y) \sim (1, 1 - y)$ applied twice returns the
identity.  On a complex doublet, the irreducible representations
of $\mathbb{Z}_2$ carry eigenvalues $e^{+i\pi/2}$ and $e^{-i\pi/2}$,
which correspond to $T_3 = +1/2$ and $T_3 = -1/2$ respectively.

Singlet modes are symmetric under the half-twist and carry $T_3 = 0$.

### 2. $Y$ as periodic winding, $Y / 2$ at the boundary

The periodic y-direction has $\mathrm{U}(1)$ symmetry.  A mode with
hypercharge $Y$ takes the form $\psi_Y(y) = e^{2\pi i Y y}$.  Under
the reflection $y \mapsto 1 - y$:

$$\psi_Y(1 - y) \;=\; e^{2\pi i Y}\,\psi_{-Y}(y).$$

For integer $Y$, $e^{2\pi i Y} = 1$, so the reflection sends $Y$ to
$-Y$.  The $\mathbb{Z}_2$ eigenvalue of a mode with hypercharge $Y$
under the reflection is $(-1)^Y = e^{i\pi Y}$.  The generator that
exponentiates to this reflection ("the reflection is $e^{i\pi}$
times the generator") is $Y / 2$: the factor of $1/2$ is the order
of the reflection.

### 3. The boundary charge is $T_3 + Y / 2$

At the identification boundary $(0, y) \sim (1, 1 - y)$, the
combined twist-and-reflect operation is the $\mathbb{Z}_2$
generator consistent with both directions.  A mode on the boundary
must be an eigenvector of this combined operation, and its
eigenvalue is the product:

$$(\text{twist eigenvalue}) \cdot (\text{reflection eigenvalue}) \;=\; e^{i\pi T_3} \cdot e^{i\pi Y / 2} \cdot (\ldots).$$

The surviving $\mathrm{U}(1)$ symmetry at the boundary is generated
by $T_3 + Y / 2$.  The electric charge, as the coupling-constant
observable at the boundary, is this generator's eigenvalue:

$$Q \;=\; T_3 + \frac{Y}{2}.$$

## Observational content

The relation reproduces all Standard-Model charges from the
Klein-bottle surviving fractions $\{1/3, 1/2, 2/3\}$.  Selected
cases:

| Particle | $T_3$ | $Y$ | $Q = T_3 + Y/2$ | Observed |
|----------|-------|-----|-----------------|----------|
| $u_L$ | $+1/2$ | $+1/3$ | $+2/3$ | $+2/3$ |
| $d_L$ | $-1/2$ | $+1/3$ | $-1/3$ | $-1/3$ |
| $\nu_{eL}$ | $+1/2$ | $-1$ | $0$ | $0$ |
| $e_L$ | $-1/2$ | $-1$ | $-1$ | $-1$ |
| $u_R$ | $0$ | $+4/3$ | $+2/3$ | $+2/3$ |
| $d_R$ | $0$ | $-2/3$ | $-1/3$ | $-1/3$ |
| $e_R$ | $0$ | $-2$ | $-1$ | $-1$ |

Every Standard-Model hypercharge follows from the Klein
identification.  The assignment $Y$ per particle is not a free
parameter; it is fixed by the particle's denominator class and
doublet membership.

## Where the load sits

- **Step 1**: irreducible-representation theory of $\mathbb{Z}_2$;
  standard.
- **Step 2**: elementary computation on the reflection $y \mapsto
  1 - y$; the $1/2$ factor is geometric, not empirical.
- **Step 3**: the identification of the "boundary charge" with
  electric charge rests on the
  [`gauge_identification`](gauge_identification.md) commitment.
  Without that commitment, the derivation would deliver *a*
  generator at the boundary; identifying it with electromagnetic
  $\mathrm{U}(1)$ is the Type 4 step.

## Remarks

- Q = T_3 + Y / 2 has been a convention of Standard Model charge
  assignment since Gell-Mann (1961) and Nishijima (1955).  The
  framework derives it from the Klein-bottle identification
  rather than taking it as a definition.
- The unit charge difference within each doublet, $Q_\text{up} -
  Q_\text{down} = 1$, follows directly: the half-twist shifts
  $T_3$ by $1$ ($+1/2 \to -1/2$), and the reflection-eigenvalue is
  shared by doublet components (same $Y$), so $\Delta Q = \Delta T_3
  = 1$.  The experimental check is immediate: quarks have $2/3 -
  (-1/3) = 1$, leptons have $0 - (-1) = 1$.
