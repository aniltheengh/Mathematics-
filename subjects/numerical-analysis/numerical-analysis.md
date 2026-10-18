# Numerical analysis and scientific computation

**Topic ID:** NLA-001  
**Classification:** Numerical analysis → approximation → reliable computation  
**Level:** Undergraduate with advanced method introductions  
**Content status:** Written compact reference.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Approximation and optimization: decide what an error means](../../lessons/advanced/approximation-and-optimization.md)
<!-- guided-lessons:end -->

## Prerequisites

Calculus, matrix algebra and elementary differential equations are needed. Diagnostic: the exact derivative of $x^2$ at $x=2$ is $4$; its forward difference with step $h$ is $4+h$. The discrepancy is a mathematical approximation error even with exact arithmetic. [Modeling](../applied-mathematics/modeling.md) explains the separate error of replacing physics by equations.

## Definition

A **numerical method** constructs a finite computation approximating a mathematical answer. **Conditioning** measures the sensitivity of the exact problem to input perturbations; **stability** concerns the algorithm's response to rounding or perturbations during computation. **Forward error** compares the computed answer with the exact answer. **Backward error** asks how much the input must change for the computed answer to be exact for that altered problem. A small residual is evidence about the equations satisfied, and need not imply a small solution error in an ill-conditioned problem.

In normalized binary floating-point arithmetic, a nonzero represented number has the form $\pm(1.b_1\ldots b_{p-1})_2\,2^e$ within a finite exponent range. Under round-to-nearest and excluding overflow and underflow, elementary arithmetic is modeled by $\operatorname{fl}(a\circ b)=(a\circ b)(1+\delta)$ with $|\delta|\le u$, the unit roundoff. Subnormal numbers near zero require a different relative-error qualification. More digits in output do not create more reliable digits.

## Intuitive explanation

Approximation balances several error sources. A finer mesh usually reduces discretization error, but costs memory and may increase accumulated roundoff. Subtracting nearby computed quantities can expose their existing errors. An adaptive method spends effort where an error indicator is large; the indicator must estimate the relevant error rather than merely repeat the same approximation twice.

![Forward Euler approximations to exponential decay at two time steps, alongside the exact solution.](../../assets/figures/advanced/numerical-decay.png)

The graph uses $y'=-2y$, $y(0)=1$. A step of $0.2$ resolves the decay more closely than $0.8$; the latter is stable but alternates sign and is physically unsuitable for a positive concentration.

## Mathematical notation

$h>0$ is a mesh or step size, $u$ unit roundoff, $\|\cdot\|$ a specified vector or induced matrix norm, and $\kappa(A)=\|A\|\|A^{-1}\|$ for nonsingular $A$. $O(h^p)$ means bounded in magnitude by $Ch^p$ for sufficiently small $h$, with $C$ independent of $h$. Constants can depend on the problem and on the time interval; asymptotic order alone does not determine actual accuracy.

## Fundamental properties

For a differentiable scalar function away from zeros, the relative local condition number is $|xf'(x)/f(x)|$. Thus subtraction $f(x)=x-a$ becomes relatively ill-conditioned near $a$, although its absolute sensitivity is one. For a linear system $Ax=b$, relative errors can be amplified by $\kappa(A)$. Scaling units can improve a representation but cannot manufacture information missing in measurements.

**Convergence** means an approximation approaches the target as resolution increases. **Consistency** means the discrete equations approximate the differential equation locally. **Stability** controls amplification of perturbations. For suitable well-posed linear initial-value problems and consistent linear discretizations, a stability-equivalence theorem connects stability and convergence; this is not a universal theorem for arbitrary nonlinear algorithms.

## Important formulas and identities

**Roots.** Bisection for continuous $f$ with opposite endpoint signs halves a bracket each iteration; after $k$ halvings its length is $(b-a)/2^k$. Newton's iteration $x_{k+1}=x_k-f(x_k)/f'(x_k)$ requires a nonzero derivative at each iterate. Near a simple root, sufficient smoothness and a close initial guess give local quadratic convergence. A multiple root or poor initial guess changes that conclusion.

**Interpolation and approximation.** Distinct nodes $x_i$ determine a unique polynomial of degree at most $n$ through $n+1$ values. For $f\in C^{n+1}$ and $x$ in the node interval,

$$f(x)-p_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n(x-x_i)$$

for a suitable $\xi$ in that interval. High degree at equally spaced nodes can oscillate badly; piecewise polynomials or well-chosen nodes often work better. Least-squares approximation instead minimizes a residual norm and need not interpolate every value.

**Differentiation and quadrature.** Taylor expansion gives $(f(x+h)-f(x-h))/(2h)=f'(x)+O(h^2)$ for sufficient smoothness. Roundoff scales roughly as $u/h$ in this difference, so taking $h$ arbitrarily small is unwise. Composite trapezoidal quadrature has error bounded by $(b-a)h^2\max|f''|/12$ for a uniform mesh. Composite Simpson quadrature with an even number of subintervals has error bounded by $(b-a)h^4\max|f^{(4)}|/180$. Adaptive quadrature compares embedded rules and subdivides until an estimated absolute-plus-relative tolerance is met; singularities and cancellation need explicit treatment.

**Linear algebra.** Pivoted LU is a general direct solver; Cholesky uses symmetry and positive definiteness. QR is preferable to explicitly forming normal equations in sensitive least-squares problems because $\kappa_2(X^TX)=\kappa_2(X)^2$ for full-column-rank $X$. Jacobi and Gauss–Seidel are stationary iterations; convergence depends on the iteration matrix's spectral radius. Conjugate gradients require a symmetric positive-definite matrix, while GMRES addresses general nonsymmetric systems. Krylov iteration should monitor residuals and use an appropriate preconditioner.

For an eigenpair approximation $(\hat\lambda,v)$, the residual is $Av-\hat\lambda v$. Power iteration seeks a strictly dominant magnitude eigenvalue provided the initial vector has a nonzero component in its eigendirection and suitable diagonalizability assumptions hold. QR and symmetric tridiagonal methods support fuller spectra. A tiny residual is especially interpretable for normal matrices; nonnormal spectra can be highly sensitive.

**Differential equations.** Forward Euler is $y_{n+1}=y_n+hf(t_n,y_n)$, with global order one for sufficiently smooth Lipschitz problems on a fixed interval. For $y'=\lambda y$, absolute stability requires $|1+h\lambda|\le1$. Backward Euler solves $y_{n+1}=y_n+hf(t_{n+1},y_{n+1})$ and handles stiff decay well, at the cost of an implicit solve. Runge–Kutta methods use multiple slope samples; tolerances control local error estimates rather than directly certifying global physical accuracy.

For heat diffusion $u_t=\alpha u_{xx}$, the explicit centered scheme is

$$u_j^{n+1}=u_j^n+r(u_{j-1}^n-2u_j^n+u_{j+1}^n),\qquad r=\alpha\Delta t/(\Delta x)^2.$$

In the standard one-dimensional setting $0\le r\le1/2$ ensures stability. **Finite differences** approximate derivatives at nodes; **finite volumes** balance conserved fluxes across cell boundaries; **finite elements** approximate a weak formulation in piecewise basis functions; **spectral methods** use global modes and can converge rapidly for smooth solutions. Shocks reduce smoothness, making conservative fluxes and suitable limiting particularly important.

## Derivations and proofs

**Euler stability.** Applying Euler to $y'=\lambda y$ gives $y_n=(1+h\lambda)^ny_0$. Perturbations obey the same recurrence, so their magnitudes stay bounded precisely when $|1+h\lambda|\le1$. For real $\lambda<0$, this becomes $0\le h\le-2/\lambda$. At the endpoint the numerical solution may oscillate without decay, so strict inequality is generally preferable.

**Centered difference.** Expand $f(x\pm h)=f(x)\pm hf'(x)+h^2f''(x)/2\pm h^3f'''(x)/6+O(h^4)$ under sufficient smoothness. Subtraction cancels even powers; division by $2h$ leaves $f'(x)+h^2f'''(x)/6+O(h^3)$. Stronger smoothness gives the familiar higher-order remainder. This is truncation analysis, not a roundoff bound.

## Worked examples

**1. A square root.** To solve $x^2-2=0$, Newton gives $x_{k+1}=(x_k+2/x_k)/2$. Starting at $x_0=3/2$ gives $x_1=17/12$ and $x_2=577/408$. Its polynomial residual $x_2^2-2$ is $1/166464$, because $577^2-2(408)^2=1$. Positive iterates remain above $\sqrt2$; $x_2-\sqrt2=(x_2^2-2)/(x_2+\sqrt2)$ checks the small error independently.

**2. Numerical integration.** For $f(x)=x^2$ on $[0,1]$, trapezoidal quadrature with two intervals gives $T=(1/2)[0/2+(1/2)^2+1/2]=3/8$. The exact integral is $1/3$, so the error is $1/24$. The error bound with $h=1/2$ and $\max|f''|=2$ is also $1/24$. Simpson gives $[f(0)+4f(1/2)+f(1)]/6=1/3$ exactly.

**3. A small linear system.** For $A=\begin{pmatrix}4&1\\1&3\end{pmatrix}$ and $b=(1,2)^T$, elimination gives $x=(1/11,7/11)^T$. Substitution checks $Ax=b$. The positive leading minors $4$ and $11$ prove positive definiteness, permitting Cholesky or conjugate gradients. The exact eigenvalues $(7\pm\sqrt5)/2$ are both positive.

**4. A finite-element weak solve.** For $-u''=1$ on $[0,1]$ with zero endpoint values, use the single hat function $\phi$ equal to $2x$ up to $1/2$ and $2(1-x)$ after. Set $u_h=c\phi$. The weak equation gives $c\int(\phi')^2=\int\phi$, hence $4c=1/2$ and $c=1/8$. The approximation matches the exact midpoint value of $u=x(1-x)/2$; it differs between the nodes.

## Practice problems

1. How many bisection halvings reduce a bracket of length one to at most $1/1024$?
2. Is Euler stable for $y'=-10y$ with $h=1/4$?
3. Evaluate the centered difference of $x^3$ at $x=1$ and explain its error.
4. For explicit heat diffusion with $\alpha=2$, $\Delta x=0.1$, what upper bound on $\Delta t$ follows from $r\le1/2$ in compatible units?

## Answers and explanations

1. Ten, since $2^{-10}=1/1024$. A midpoint error bound is half the current bracket length.
2. No: the amplification factor is $1-10/4=-3/2$, whose magnitude exceeds one. The exact solution decays while the numerical solution grows in magnitude.
3. $[(1+h)^3-(1-h)^3]/(2h)=3+h^2$. The derivative is $3$, so the exact truncation error is $h^2$.
4. $\Delta t\le(\Delta x)^2/(2\alpha)=0.0025$. If length is metres and $\alpha$ is square metres per second, time is seconds.

## Common mistakes and misconceptions

Converged iterations can solve a wrong model accurately. A relative tolerance alone is problematic near zero. Computing an inverse explicitly is usually unnecessary for solving a system. Uncontrolled mesh refinement may violate a time-step stability condition. Reporting one Monte Carlo run without sampling uncertainty hides numerical probability error.

## Connections to other mathematics

[Optimization](../optimization/optimization-and-control.md) extends root-finding ideas to gradients. [Functional analysis](../functional-analysis/functional-analysis.md) supports weak PDE formulations. [Probability](../probability/probability-and-stochastic-processes.md) gives Monte Carlo standard errors.

## Applications

Monte Carlo estimates $Ef(X)$ by an independent sample mean, with standard error $s/\sqrt N$ when the variance is finite. For a reliable engineering calculation, record mesh, tolerances, units, solver, version and convergence evidence. Compare against an exact solution or a manufactured solution before using a new PDE implementation. This is verification; comparison with independent physical observations is validation.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) reproduces the Euler comparison. [Checks](../../scripts/verify_advanced.py) use exact arithmetic for root residuals, quadrature, finite elements and the linear solve. Seeded random examples are reproducible, but a seed does not prove unbiasedness or adequate sampling.

## References and recommended reading

- Tobin A. Driscoll and Richard J. Braun, [*Fundamentals of Numerical Computation*](https://fncbook.com/), chapters on linear systems, nonlinear roots, initial-value and boundary-value problems.
- Their [floating-point chapter](https://fncbook.com/floating-point/) gives the representation and rounding model in detail. These are further-reading references; the derivations and examples here are original.

## Revision and mastery status

Written 2026-10-18. Every numerical subject-map entry has an explicit method or equation; full implementation and convergence theory of all methods are beyond this compact chapter. Mastery includes distinguishing conditioning from stability and demonstrating convergence against a known answer.
