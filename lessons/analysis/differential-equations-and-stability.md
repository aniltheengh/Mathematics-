# Differential equations: models, modes, and stability

**Lesson ID:** LES-DE-01.  
**Prerequisites:** Derivatives and integrals, complex quadratic roots, matrices, eigenvectors, and sine functions.  
**Objectives:** Derive a forced oscillator from a balance law; solve all damping cases; distinguish asymptotic decay from transient amplification; derive heat eigenmodes and check initial and boundary data.  
**Status:** Written guided lesson; learner mastery unassessed.

Use the [ODE reference](../../subjects/differential-equations/ordinary-differential-equations.md) and [PDE reference](../../subjects/differential-equations/partial-differential-equations.md) for compact lookup. This lesson builds a connection between two apparently different models: a vibrating mass has finitely many modes after a lumped approximation, while a conducting rod has infinitely many spatial modes. In both, eigenvalues determine how modal amplitudes evolve. What the eigenvalues do not determine by themselves is equally important.

All physical constants below carry units before any numerical normalization. A formula involving $e^{-t}$ assumes either dimensionless time or a decay coefficient with reciprocal-time units. The graphs explicitly use dimensionless variables so comparisons between damping choices do not mix incompatible scales.

## Stage 1: derive the equation from forces

Consider one translating mass attached to a linear spring and viscous damper. Let $x(t)$ be displacement from static equilibrium, measured in metres, with positive displacement and external force in the same direction. The spring force is $-kx$, the damper force $-cx'$, and the applied force is $F(t)$. Newton's law gives

$$mx''=F(t)-cx'-kx,\qquad
mx''+cx'+kx=F(t).$$

Here $m>0$ is in kg, $c\ge0$ in N·s/m, and $k>0$ in N/m. Every term has units newtons. The model assumes small enough deformation for a linear stiffness, a lumped moving mass, and damping proportional to velocity. Dry friction or large-deflection spring behavior would require a different force law.

A second-order equation needs two initial data, displacement $x(0)=x_0$ and velocity $x'(0)=v_0$. Substituting a proposed function into the differential equation alone does not ensure it is the required motion. Continuous forcing gives a unique global classical solution for this linear constant-coefficient initial value problem; a step force is handled piecewise with continuity of displacement and velocity when no impulse is present. An ideal impulse instead changes momentum and must be modeled as distributional forcing.

Introduce natural angular frequency and damping ratio:

$$\omega_n=\sqrt{k/m},\qquad
\zeta=\frac{c}{2\sqrt{km}},\qquad \tau=\omega_nt.$$

For a nonzero reference force $F_0>0$, use displacement scale $F_0/k$ and set $y=kx/F_0$. With $F=F_0f(\tau)$ the equation becomes

$$y_{\tau\tau}+2\zeta y_\tau+y=f(\tau).$$

This derivation exposes the dimensionless parameter controlling the shape of the response. Two systems with different masses and springs can have the same normalized response while evolving at different physical time and displacement scales.

## Stage 2: solve free motion and understand repeated roots

For $F=0$, try $x=e^{rt}$. It never vanishes, so division gives $mr^2+cr+k=0$, with roots

$$r=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}.$$

For $0\le\zeta<1$, write $\omega_d=\omega_n\sqrt{1-\zeta^2}$, giving

$$x=e^{-\zeta\omega_nt}(A\cos\omega_dt+B\sin\omega_dt).$$

For $\zeta>1$, two distinct negative real roots give $Ae^{r_1t}+Be^{r_2t}$. At $\zeta=1$ the repeated root is $-\omega_n$, and the independent solutions are $e^{-\omega_nt}$ and $te^{-\omega_nt}$. Simply writing two constants times the same exponential would supply only one degree of freedom and fail to meet arbitrary initial data.

To derive the repeated-root factor rather than memorize it, let $x=e^{-\omega_nt}v(t)$ in the critically damped equation. Direct substitution reduces it to $v''=0$. Thus $v=A+Bt$, explaining the second solution. In every damped case with $c>0$, both modes decay; in the undamped case $c=0$, oscillation persists without decay.

**Worked example 1: an underdamped mass.** Take $m=2$ kg, $c=4$ N·s/m, $k=50$ N/m, $x(0)=0$, and $x'(0)=1$ m/s. Then $\omega_n=5$ rad/s, $\zeta=1/5$, and $\omega_d=2\sqrt6$ rad/s. The initial displacement makes $A=0$. Differentiating at zero gives $B\omega_d=1$ m/s, so

$$x(t)=\frac{e^{-t}\sin(2\sqrt6\,t)}{2\sqrt6}\ {\rm m},$$

when numerical time is in seconds. The envelope decays at one s⁻¹. Substituting into $2x''+4x'+50x=0$ verifies the equation; initial velocity checks the coefficient separately. The critical damping coefficient for this mass and stiffness would be $2\sqrt{mk}=20$ N·s/m, not the stated four.

Energy gives an independent stability argument. Define $E=mx'^2/2+kx^2/2$. Multiplying the unforced equation by velocity yields

$$E'=x'(mx''+kx)=-cx'^2\le0.$$

At a turning point the derivative can be zero even when $c>0$. Thus nonincreasing energy does not mean a strictly negative derivative at every instant. With positive stiffness and mass, energy controls both displacement and velocity, which makes this a useful physical norm for the model.

## Stage 3: forcing chooses the sustained part

For constant force $F_0$, the static displacement is $x_s=F_0/k$. Substituting $x=x_s+z$ leaves the free equation for $z$. Initial conditions determine which transient must be added to that steady displacement.

**Worked example 2: a critically damped step.** In dimensionless variables solve

$$y''+2y'+y=1,\qquad y(0)=y'(0)=0.$$

Take particular solution one and homogeneous part $(A+B\tau)e^{-\tau}$. The first initial condition gives $A=-1$; differentiating gives $y'(0)=B-A$, so $B=-1$. Hence

$$y(\tau)=1-(1+\tau)e^{-\tau},\qquad y'=\tau e^{-\tau}.$$

The response is monotone for $\tau\ge0$, starts at zero, and tends to one. The nonnegative derivative is a proof of monotonicity, whereas a sampled plot only suggests it.

![Normalized step responses for four damping ratios](../../assets/figures/lessons-analysis/ode-step-response.png)

Every curve solves $y''+2\zeta y'+y=1$ with zero initial displacement and velocity, for $\zeta=0,3/10,1,2$. The steady value is one. The undamped curve $1-\cos\tau$ never settles; positive damping removes its sustained free oscillation. The overdamped curve's slow mode can take longer to approach equilibrium than the critically damped response for this normalization.

For harmonic forcing $F_0\cos\omega t$, substitute the real part of $Xe^{i\omega t}$. Algebra gives

$$X=\frac{F_0}{k-m\omega^2+ic\omega},\qquad
|X|=\frac{F_0}{\sqrt{(k-m\omega^2)^2+c^2\omega^2}}.$$

For $c>0$ and $\omega>0$, the denominator cannot vanish, so this periodic particular response is finite. The actual initial-value solution also includes transients. With zero damping and $\omega=\omega_n$, the ordinary trial overlaps the homogeneous solution and fails; a time factor is needed.

**Worked example 3: ideal resonance.** For $y''+y=\cos t$, zero initial data, try $y_p=at\sin t$. Differentiation gives $y_p''+y_p=2a\cos t$, so $a=1/2$. Both initial conditions already vanish, giving $y=t\sin t/2$. The growing envelope is an exact conclusion of this undamped model. It does not predict unlimited real motion once material nonlinearities, limits, and damping become relevant.

## Stage 4: systems, eigenvalues, and transient growth

Set the oscillator state to $z=(x,v)^T$ with $v=x'$. Then

$$z'=\begin{pmatrix}0&1\\-k/m&-c/m\end{pmatrix}z
+\binom0{F/m}.$$

For a general constant matrix $A$, the solution of $z'=Az$ is $e^{At}z_0$. A finite-dimensional continuous-time linear system is asymptotically stable exactly when every eigenvalue has strictly negative real part. If the matrix is defective, polynomial time factors can occur, but a fixed polynomial times a strictly decaying exponential still tends to zero.

For a smooth nonlinear system near an equilibrium, eigenvalues of the Jacobian with negative real parts imply local asymptotic stability; a positive real part implies instability. If an eigenvalue has zero real part, linearization may be inconclusive. These are local nonlinear theorems, and their hypotheses are stronger than merely having a matrix written on a page.

**Worked example 4: stable eigenvalues with large transient growth.** In dimensionless coordinates let

$$A=\begin{pmatrix}-1&K\\0&-2\end{pmatrix},\qquad K>0,\qquad
z(0)=\binom01.$$

The second component is $z_2=e^{-2t}$. Solving the first by an integrating factor gives

$$z_1=K(e^{-t}-e^{-2t}).$$

Both eigenvalues are negative, so the state ultimately decays. Nevertheless $z_1$ peaks when $-e^{-t}+2e^{-2t}=0$, namely at $t=\log2$, where $z_1=K/4$. With $K=100$, a unit-norm initial state produces a first component of 25 before decaying. Negative eigenvalues guarantee asymptotic behavior, not monotonic decay of the Euclidean norm.

The matrix is nonnormal when $K\ne0$, meaning $AA^T\ne A^TA$. Its eigenvectors need not be perpendicular, allowing interacting decaying modes to produce temporary growth. A physically scaled energy norm may tell a different story from an arbitrary component norm. Before interpreting amplification, state what norm measures the relevant quantity and whether its components have compatible units.

## Stage 5: the same modal idea in heat diffusion

Consider a rod $0<x<L$ with diffusivity $\kappa>0$ and temperature relative to a fixed endpoint temperature denoted by $u(x,t)$. Assume constant properties and one-dimensional conduction without internal sources:

$$u_t=\kappa u_{xx},\qquad u(0,t)=u(L,t)=0,\qquad u(x,0)=f(x).$$

The initial profile is part of the problem. Zero boundary values for positive time do not mean the initial interior is zero. For a solution continuous at the corners, $f(0)=f(L)=0$ is required. Weaker $L^2$ initial data can violate pointwise corner matching while still defining a heat evolution that is smooth for positive time; the solution concept must be named.

Put $u=X(x)T(t)$ where the product is nonzero locally. Dividing gives $T'/(\kappa T)=X''/X=-\lambda$. The endpoint conditions select

$$X_n=\sin(n\pi x/L),\qquad\lambda_n=(n\pi/L)^2,\qquad
T_n=e^{-\kappa\lambda_nt},\quad n=1,2,\ldots.$$

Each spatial eigenfunction has its own decay rate. Expanding a square-integrable initial profile in the complete sine basis yields a solution in the $L^2$ sense at time zero and a smooth solution for positive time. Completeness and convergence are cited spectral results; separation alone does not prove them.

**Worked example 5: two compatible modes.** Use dimensionless position $\xi=x/L$, time $\tau=\kappa t/L^2$, and initial profile

$$U(\xi,0)=\sin(\pi\xi)+\tfrac12\sin(2\pi\xi).$$

Then

$$U(\xi,\tau)=e^{-\pi^2\tau}\sin(\pi\xi)
+\tfrac12e^{-4\pi^2\tau}\sin(2\pi\xi).$$

The endpoints are zero at every time, and substituting $\tau=0$ recovers the initial data. Direct differentiation gives $U_\tau=U_{\xi\xi}$. At $\tau=\log2/\pi^2$, the first amplitude is $1/2$ and the second is $1/32$. The shape becomes increasingly like the first mode because the second decays faster.

![Heat profiles and their exact modal coefficient decay](../../assets/figures/lessons-analysis/heat-mode-evolution.png)

The left panel shows the exact two-mode profiles at $\tau=0,1/50,1/10$ on $0\le\xi\le1$. The right shows amplitudes $e^{-\pi^2\tau}$ and $\tfrac12e^{-4\pi^2\tau}$ on a logarithmic vertical axis. These are rates in dimensionless time; physical rates multiply by $\kappa/L^2$. Doubling rod length multiplies each modal decay time by four when diffusivity is fixed.

Heat energy confirms decay without tracking every mode. For a smooth zero-endpoint solution, multiply by $u$ and integrate:

$$\frac d{dt}\frac12\int_0^L u^2dx
=\kappa\int_0^Luu_{xx}dx
=-\kappa\int_0^Lu_x^2dx.$$

The boundary term vanishes because $u=0$ there. Applying this identity to the difference of two solutions with the same data proves uniqueness in this regularity class. It does not prove existence; the sine expansion or an appropriate weak-existence theorem supplies that separate step.

## Practice problems

1. For $m=1$, $k=9$, find the critical damping coefficient and the undamped angular frequency, using compatible SI units.
2. Solve $y''+2y'+y=0$ with $y(0)=1$, $y'(0)=0$.
3. In the critically damped step example, verify the equation directly from the stated $y'$.
4. Why does a constant particular solution fail for $y''+y=\cos t$? What feature of resonance requires a factor of time?
5. For the nonnormal example with $K=8$, find the state at $t=\log2$. Does its norm exceed the initial norm?
6. Are eigenvalues $-1$ and zero sufficient for asymptotic stability of a linear system? Give a diagonal counterexample.
7. For a rod, find the ratio of mode-three decay rate to mode-one decay rate. How does doubling $L$ change both?
8. With zero endpoint temperature, can the initial profile $f(x)=1$ on the entire closed interval produce a solution continuous at both initial corners? What weaker interpretation remains possible?

## Answers and explanations

1. $\omega_n=\sqrt{k/m}=3$ rad/s and $c_{\rm crit}=2\sqrt{mk}=6$ N·s/m. The coefficient's units differ from the angular frequency's units even when both involve the same square root.
2. Write $y=(A+Bt)e^{-t}$. Initial displacement gives $A=1$ and derivative at zero gives $B-A=0$, hence $y=(1+t)e^{-t}$. Its derivative is $-te^{-t}$.
3. From $y'=\tau e^{-\tau}$, $y''=(1-\tau)e^{-\tau}$. Thus $y''+2y'+y=[1-\tau+2\tau-(1+\tau)]e^{-\tau}+1=1$; the initial data also follow directly.
4. A constant has no oscillation and cannot reproduce $\cos t$. More specifically, a trial $A\cos t+B\sin t$ lies entirely in the homogeneous solution space, so applying $D^2+1$ gives zero. Multiplication by time escapes that kernel and produces the required forcing.
5. $z_1=8/4=2$ and $z_2=1/4$. Its Euclidean norm is $\sqrt{4+1/16}=\sqrt{65}/4>1$. Both components nevertheless tend to zero at late time.
6. No. For $A=\operatorname{diag}(-1,0)$, an initial second component remains constant. Asymptotic stability requires decay of every sufficiently small initial state; a zero eigenvalue defeats it here.
7. Rates are proportional to $n^2$, so the ratio is nine. Each rate scales as $1/L^2$, so doubling length divides both rates by four and leaves their ratio unchanged.
8. No: continuity would require the initial endpoint values one to match the prescribed boundary values zero. Treating the constant as an $L^2$ interior initial profile still yields a valid weak/mild heat evolution for positive time, without claiming corner continuity.

## Verification and further study

[Exact checks](../../scripts/verify_lessons_analysis.py) test oscillator residuals and initial data, matrix exponentials, nonnormal amplification, and heat modes. [Plot source](../../scripts/plot_lessons_analysis.py) regenerates both diagrams from closed-form functions. These computations do not validate a real mechanical or thermal model.

Further study: Jiří Lebl, [Notes on Diffy Qs](https://www.jirka.org/diffyqs/), higher-order equations, systems, Fourier series, and PDEs; [linear algebra reference](../../subjects/linear-algebra/linear-algebra.md) for eigenvectors and spectral decompositions. General nonlinear stability and heat-space convergence results are cited rather than fully proved in this lesson.

Written 2026-10-18. Mastery requires deriving the force balance with units, selecting a root case, checking two initial data, distinguishing transient from asymptotic behavior, and checking a heat solution against all its data. Learner assessment remains open.
