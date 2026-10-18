# Ordinary differential equations and dynamical systems

**Topic ID:** ODE-01.  
**Classification:** Differential equations → ordinary equations and dynamics.  
**Level:** Undergraduate, with an advanced dynamics bridge.  
**Content status:** Written compact reference chapter.  
**Learner mastery:** Unassessed.

## Prerequisites

Use [calculus](../calculus/single-variable-calculus.md), complex roots, and [linear algebra](../linear-algebra/linear-algebra.md). Diagnostic: $y=Ce^{-2t}$ satisfies $y'+2y=0$ for every constant $C$. An initial value selects one member, so $y(0)=3$ selects $C=3$. Always check both the equation and the data; satisfying only one is insufficient.

## Definition

An **ordinary differential equation** relates an unknown function of one independent variable to its derivatives. Its order is the highest derivative present. An **initial value problem** specifies values at one point, usually $y(t_0)$ for a first-order system. A **boundary value problem** specifies conditions at different points. A solution is a sufficiently differentiable function satisfying the equation and data on a declared interval; formulas beyond a singularity need not belong to the same solution.

A first-order autonomous system is $x'=f(x)$, with no explicit time dependence. An equilibrium satisfies $f(x_*)=0$. Its stability concerns nearby solutions, not merely the value of the derivative at the equilibrium.

## Intuitive explanation

A model supplies a rate law; solving reconstructs the evolution. Initial data choose the trajectory, while boundary data may select special parameters or may be incompatible. A phase portrait shows the direction and geometry of motion without choosing a specific clock reading. Linearization measures behavior near an equilibrium, but nonlinear terms can decide cases in which the linear part predicts no decay or growth.

![Damped displacement and logistic solutions](../../assets/figures/analysis/ode-evolution.png)

Left: exact solution $x(t)=e^{-t}\sin(2t)/2$ m of $x''+2x'+5x=0$ with $x(0)=0$ m and $x'(0)=1$ m/s, with coefficient units understood as s⁻¹ and s⁻². Right: dimensionless logistic solutions $y(t)=1/[1+(1/y_0-1)e^{-t}]$ for $y_0=1/5,1/2,2$, using dimensionless time.

## Mathematical notation

A prime denotes $d/dt$ except in spatial boundary problems. $I$ is an identity matrix, $e^{At}=\sum_{k=0}^\infty(At)^k/k!$, and $\mathcal L\{f\}(s)=\int_0^\infty e^{-st}f(t)dt$ when convergent. In a mechanical model, $m,c,k$ denote mass, viscous damping, and stiffness. A phase state for second-order motion is $(x,v)$ with $v=x'$; axis units can therefore differ, so a phase plot is not a geometric length diagram.

## Fundamental properties

**Local existence and uniqueness theorem, cited without proof.** If $f(t,y)$ is continuous near $(t_0,y_0)$ and locally Lipschitz in $y$, an initial value problem $y'=f(t,y)$, $y(t_0)=y_0$ has a unique local solution. Continuity alone can give existence but not uniqueness: $y'=\sqrt{|y|}$, $y(0)=0$ admits a zero solution and delayed departures. Local existence does not promise existence for all future time; $y'=y^2$, $y(0)=1$ blows up at $t=1$.

For $y'=g(y)$, equilibria are zeros of $g$. On intervals where $g\ne0$, separation gives $\int dy/g(y)=t+C$, while equilibrium solutions must be retained separately. A linear equation $y'+p(t)y=q(t)$ has integrating factor $\mu=e^{\int pdt}$. An exact equation $M(x,y)dx+N(x,y)dy=0$ comes from a potential $\Phi$ with $\Phi_x=M$, $\Phi_y=N$; $M_y=N_x$ is a local test with the appropriate domain conditions.

## Important formulas and identities

For continuous matrix $A(t)$ and forcing, systems have a fundamental matrix representation. In the constant-coefficient case,

$$x(t)=e^{A(t-t_0)}x_0+\int_{t_0}^t e^{A(t-s)}b(s)\,ds.$$

For $ay''+by'+cy=0$, $a\ne0$, characteristic roots solve $ar^2+br+c=0$. Distinct roots give $C_1e^{r_1t}+C_2e^{r_2t}$; a repeated root gives $(C_1+C_2t)e^{rt}$. Complex conjugate roots $\alpha\pm i\beta$ give real combinations $e^{\alpha t}(C_1\cos\beta t+C_2\sin\beta t)$. Resonant forcing requires a factor of $t$ in a trial particular solution when its ordinary trial overlaps a homogeneous solution.

For functions of exponential order with appropriate regularity,

$$\mathcal L\{y'\}=sY-y(0),\qquad \mathcal L\{y''\}=s^2Y-sy(0)-y'(0).$$

Transforming an initial value problem produces an algebraic equation, but inversion must retain the region where the transform converges. A power-series solution $y=\sum a_n(t-t_0)^n$ gives recurrences after coefficient matching, valid inside a convergence interval justified by coefficient regularity. Near regular singular points, a Frobenius form $(t-t_0)^r\sum a_n(t-t_0)^n$ introduces an indicial equation; repeated roots can require logarithms.

## Derivations and proofs

**Integrating factor.** If $\mu'=p\mu$, the product rule gives $(\mu y)'=\mu(y'+py)=\mu q$. Integrating yields

$$y(t)=\frac{\mu(t_0)y_0+\int_{t_0}^t\mu(s)q(s)ds}{\mu(t)}.$$

An exponential integrating factor never vanishes, so division is valid wherever $p$ is continuous. This also proves uniqueness within that interval by subtracting two solutions.

**Energy decay.** For $mx''+cx'+kx=0$ with $m,k>0$, $c\ge0$, define $E=mx'^2/2+kx^2/2$. Then $E'=x'(mx''+kx)=-cx'^2\le0$. This proves nonincreasing energy; by itself it does not claim strict decrease at every instant or establish every asymptotic result.

For a smooth autonomous system, the Jacobian $Df(x_*)$ determines linearized evolution. Eigenvalues with strictly negative real parts imply local asymptotic stability; a positive real part implies instability. These nonlinear stability theorems are cited, not proved. Purely imaginary or zero-real-part eigenvalues are inconclusive. The scalar family $x'=\mu x-x^3$ has one equilibrium at zero for $\mu<0$, and three at $0,\pm\sqrt\mu$ for $\mu>0$: a supercritical pitchfork bifurcation. Signs of $f'$ show zero loses stability and the two new equilibria are stable.

A periodic orbit is a closed nonconstant trajectory; its transverse stability is measured by a return map or Floquet multipliers. For smooth autonomous planar flows, the Poincaré–Bendixson theorem strongly restricts compact limit sets without equilibria; it rules out the usual strange-attractor chaos in that setting. Three-dimensional autonomous flows, or periodically forced lower-dimensional systems, can exhibit chaos, meaning more than a complicated-looking trace: sensitive dependence requires a mathematical criterion such as a positive Lyapunov exponent in a specified invariant setting. These advanced results are stated with scope, not proved here.

For a regular **Sturm–Liouville problem**,

$$-(p y')'+qy=\lambda wy,\qquad p,w>0,$$

on a finite interval with real regular coefficients and separated self-adjoint boundary conditions, eigenvalues are real and distinct-eigenvalue eigenfunctions are orthogonal in $\langle f,g\rangle_w=\int f g wdx$. Subtracting the two eigen-equations after cross multiplication and integrating leaves a boundary term; the self-adjoint conditions make it zero, hence $(\lambda-\mu)\int wy_\lambda y_\mu=0$. Completeness is a deeper theorem and is not proved here.

## Worked examples

**1. Linear forced response.** Solve $y'+2y=6$, $y(0)=1$. Multiplying by $e^{2t}$ gives $(e^{2t}y)'=6e^{2t}$. Integrating gives $y=3+Ce^{-2t}$, and the initial condition gives $C=-2$. Thus $y=3-2e^{-2t}$. Substitution gives $y'+2y=4e^{-2t}+6-4e^{-2t}=6$.

**2. Resonance.** Solve $y''+y=\cos t$, $y(0)=y'(0)=0$. The homogeneous terms are $\cos t,\sin t$, so use $y_p=at\sin t$. Differentiation gives $y_p''+y_p=2a\cos t$, hence $a=1/2$. Both initial values vanish, yielding $y=t\sin t/2$. Its envelope grows linearly because this ideal model has no damping; this is not the response of every real oscillator.

**3. Stable coupled system.** Let $x'=Ax$, $A=\begin{pmatrix}-2&1\\1&-2\end{pmatrix}$ and $x(0)=(1,0)$. Eigenpairs are $(-1,(1,1))$ and $(-3,(1,-1))$. Decompose the initial state as half of each eigenvector. Then $x_1=(e^{-t}+e^{-3t})/2$ and $x_2=(e^{-t}-e^{-3t})/2$. Differentiation checks both equations; both modes decay, proving global asymptotic stability for this linear system.

**4. Boundary spectrum.** Solve $-y''=\lambda y$, $y(0)=y(\pi)=0$, for nonzero $y$. For $\lambda=0$ linear solutions are forced to zero; for $\lambda<0$ hyperbolic solutions are also trivial. For $\lambda>0$, $y=B\sin(\sqrt\lambda x)$ and $\sin(\sqrt\lambda\pi)=0$. Thus $\lambda_n=n^2$, $y_n=\sin(nx)$, $n=1,2,\ldots$.

## Practice problems

1. Solve $y'=3y$, $y(0)=2$.
2. Solve $y'=y^2$, $y(0)=1$, and state the maximal interval containing zero.
3. Classify $y=0$ and $y=1$ for $y'=y(1-y)$.
4. Solve $(2x+y)dx+(x+2y)dy=0$ implicitly.

## Answers and explanations

1. Separation or the linear formula gives $y=2e^{3t}$; this exists for every real $t$.
2. Separation gives $-1/y=t+C$, so $y=1/(1-t)$ on $(-\infty,1)$. The pole prevents continuation through one as a finite classical solution.
3. For $g(y)=y-y^2$, $g'(0)=1>0$ gives instability and $g'(1)=-1<0$ gives local asymptotic stability. A sign-line analysis confirms motion toward one for positive initial data.
4. Cross partials are both one. Integrate $\Phi_x=2x+y$ to obtain $\Phi=x^2+xy+h(y)$. Matching $\Phi_y=x+2y$ gives $h=y^2$, so $x^2+xy+y^2=C$ is the implicit family.

## Common mistakes and misconceptions

Dividing by $y$ loses the equilibrium $y=0$. A general solution need not be valid across every denominator zero. Complex characteristic roots produce real sine and cosine solutions when coefficients and data are real. A boundary value problem need not have a unique solution even when an associated initial value problem does. An eigenvalue plot alone does not classify a nonlinear nonhyperbolic equilibrium.

## Connections to other mathematics

[Transforms and special functions](../harmonic-analysis/transforms-and-special-functions.md) supply Laplace inversion and Bessel equations. [PDEs](partial-differential-equations.md) reduce through separation to Sturm–Liouville problems. Linear algebra turns coupled equations into independent modes when diagonalization is available.

## Applications

For $m=1$ kg, $c=2$ N·s/m, $k=5$ N/m, free displacement satisfies $x''+2x'+5x=0$ after dividing by mass. With $x(0)=0$ m and velocity $1$ m/s, $x=e^{-t}\sin(2t)/2$ m when time is measured in seconds. The decay rate is $1$ s⁻¹ and damped angular frequency $2$ rad/s. A lumped model assumes small motion, linear springs, and viscous damping.

## Optional computational examples

[plot_analysis.py](../../scripts/plot_analysis.py) plots exact free-motion and logistic solutions. [verify_analysis.py](../../scripts/verify_analysis.py) checks differential residuals, initial data, eigenmodes, and boundary eigenfunctions. Numerical integration of one trajectory is not a proof of stability or chaos.

## References and recommended reading

Source and further study: Jiří Lebl, [Notes on Diffy Qs](https://www.jirka.org/diffyqs/), first-order equations, higher-order equations, systems, eigenvalue problems, Laplace transforms, power-series methods, and nonlinear systems. Deep dynamics and Sturm–Liouville completeness need a longer specialist treatment; the chapter distinguishes their statements from its explicit proofs.

## Revision and mastery status

Written 2026-10-18. Scope: core solution methods plus mathematically explicit introductions to dynamics and spectral boundary problems. Mastery requires selecting a method, checking data and interval of existence, explaining energy decay, and recognizing when linearization is inconclusive. Learner mastery remains unassessed.
