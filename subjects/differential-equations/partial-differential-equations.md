# Partial differential equations

**Topic ID:** PDE-01.  
**Classification:** Differential equations → partial equations and boundary problems.  
**Level:** Undergraduate through an introductory graduate bridge.  
**Content status:** Written compact reference chapter.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Differential equations: models, modes, and stability](../../lessons/analysis/differential-equations-and-stability.md)
<!-- guided-lessons:end -->

## Prerequisites

Use [multivariable calculus](../calculus/multivariable-and-vector-calculus.md), [ODEs](ordinary-differential-equations.md), and Fourier expansions. Diagnostic: for $u(x,t)=e^{-t}\sin x$, $u_t=-u$ and $u_{xx}=-u$, so $u_t=u_{xx}$. Checking a PDE also requires checking the initial and boundary data; the same equation supports many different physical problems.

## Definition

A **partial differential equation** relates a function of several variables to its partial derivatives. A classical solution has the derivatives required pointwise. A weak solution transfers derivatives onto smooth test functions through integration by parts, allowing less regular functions. A boundary problem is **well posed** in a chosen function space if a solution exists, is unique, and depends continuously on the data in specified norms. Stating the space and norms is part of the claim.

For $Au_{xx}+2Bu_{xy}+Cu_{yy}$ in two variables with real coefficients, the principal part is elliptic if $B^2-AC<0$, hyperbolic if it is positive, and parabolic if zero with a nonzero principal part. For variable coefficients this classification can change with position. Higher-dimensional classification uses the principal symbol rather than this two-variable shortcut.

## Intuitive explanation

Transport moves information along trajectories. Waves propagate disturbances at finite speed. Heat smooths disturbances through diffusion. Laplace's equation describes equilibrated fields whose interior values are constrained by surrounding values. Different information mechanisms explain why appropriate data differ: a wave needs displacement and velocity, heat needs an initial temperature, and an elliptic equilibrium normally takes boundary data without a separate time history.

![Heat equation modes decay at different rates](../../assets/figures/analysis/heat-modes.png)

The plotted exact solution is $u(x,t)=e^{-t}\sin x+\tfrac12e^{-4t}\sin(2x)$ for $0\le x\le\pi$, at $t=0,1/5,1$. It satisfies $u_t=u_{xx}$ with zero endpoint values in dimensionless coordinates. The second mode decays four times as fast in its exponential rate.

## Mathematical notation

$u_t=\partial u/\partial t$, $\Delta u=\sum_i u_{x_ix_i}$, and $\nabla u$ is the spatial gradient. $\Omega$ is an open spatial region, $n$ its outward normal, and $\varphi$ a smooth compactly supported test function. Dirichlet data prescribe $u$; Neumann data prescribe normal derivative or flux; Robin data prescribe a linear combination. $\delta$ denotes a Dirac distribution, defined by $\langle\delta,\varphi\rangle=\varphi(0)$, not an ordinary infinitely tall function.

## Fundamental properties

The model equations are

$$u_t+cu_x=0,\qquad u_{tt}=c^2u_{xx},\qquad u_t=\kappa\Delta u,\qquad\Delta u=0,$$

with transport/wave speed $c$, and diffusivity $\kappa>0$. Their data must match at corners when classical regularity is requested. For a bounded connected domain, a sufficiently regular harmonic function attains its maximum on the boundary unless constant; the maximum principle is cited without full proof. It yields uniqueness for Laplace's Dirichlet problem. Pure Neumann data determine a Poisson solution only up to an additive constant and require a compatibility condition from divergence theorem.

Forward heat evolution is smoothing. Backward recovery of the initial field amplifies high spatial modes by $e^{\kappa k^2t}$, so it is unstable in ordinary data norms. Small measurement error does not imply small reconstruction error. Hyperbolic problems instead have domains of dependence controlled by characteristic speeds. General existence and regularity theorems are equation- and space-dependent; no single theorem covers every nonlinear PDE.

## Important formulas and identities

For transport on the whole real line, $u(x,0)=f(x)$ gives $u(x,t)=f(x-ct)$. For the one-dimensional wave equation on the line with $u(x,0)=f(x)$ and $u_t(x,0)=g(x)$,

$$u(x,t)=\frac{f(x-ct)+f(x+ct)}2+\frac1{2c}\int_{x-ct}^{x+ct}g(s)\,ds,$$

assuming $c>0$ and sufficient smoothness. This is d'Alembert's formula and displays the dependence interval.

The whole-space heat kernel in $d$ dimensions is

$$G(x,t)=(4\pi\kappa t)^{-d/2}\exp[-|x|^2/(4\kappa t)],\qquad t>0.$$

For suitable initial data, $u(x,t)=(G(\cdot,t)*f)(x)$ solves heat evolution; $\int Gdx=1$ preserves total mass. A **fundamental solution** solves a unit point-source equation distributionally. A **Green function** additionally fits the domain and homogeneous boundary conditions. In three dimensions, for the convention $-\Delta\Phi=\delta$, $\Phi(x)=1/(4\pi|x|)$; the sign changes if the operator convention changes.

## Derivations and proofs

**Characteristics for transport.** Along $x(t)=x_0+ct$, the chain rule gives $d u(x(t),t)/dt=u_t+cu_x=0$. Thus $u$ is constant on each characteristic and equals $f(x_0)=f(x-ct)$. For nonconstant speed, one first solves the characteristic ODE; characteristics may cease to give a global single-valued classical solution in nonlinear problems.

**Heat separation.** For $0<x<L$ with $u(0,t)=u(L,t)=0$, put $u=X(x)T(t)$. Dividing by a nonzero product locally gives $T'/(\kappa T)=X''/X=-\lambda$. Nontrivial endpoint solutions require $\lambda_n=(n\pi/L)^2$, $X_n=\sin(n\pi x/L)$, and $T_n=e^{-\kappa\lambda_nt}$. Expansion of initial data yields

$$u(x,t)=\sum_{n=1}^\infty b_n e^{-\kappa(n\pi/L)^2t}\sin(n\pi x/L),\quad b_n=\frac2L\int_0^L f(x)\sin(n\pi x/L)dx.$$

For square-integrable $f$, this is understood through the eigenfunction completeness theorem, cited rather than proved; for positive time the exponential factors improve regularity. Termwise differentiation at time zero needs separate compatibility and convergence checks.

**Energy uniqueness.** If two smooth heat solutions share data, their difference $w$ has zero data. Multiplying $w_t=\kappa\Delta w$ by $w$, integrating, and using zero Dirichlet boundary values gives

$$\frac d{dt}\frac12\int_\Omega w^2dx=-\kappa\int_\Omega|\nabla w|^2dx\le0.$$

Since the initial energy is zero and energy is nonnegative, $w=0$. This proves uniqueness in this regularity class, not existence.

Weak formulations extend this calculation. For $-\Delta u=f$ and zero Dirichlet data, seek $u\in H_0^1(\Omega)$ satisfying $\int\nabla u\cdot\nabla v=\int fv$ for every $v\in H_0^1(\Omega)$. This is also the stationarity condition of $J(u)=\tfrac12\int|\nabla u|^2-\int fu$. Here $H_0^1$ is the closure of smooth compactly supported functions in the norm combining the square-integrals of the function and its first weak derivatives. On a bounded Lipschitz domain with $f\in L^2(\Omega)$, Poincaré and Lax–Milgram supply existence and uniqueness; these functional-analytic theorems are cited, not proved here. A distributional derivative is defined by $\langle\partial_i u,\varphi\rangle=-\langle u,\partial_i\varphi\rangle$; this makes integration by parts the definition rather than an informal manipulation.

## Worked examples

**1. Moving pulse.** Solve $u_t+2u_x=0$, $u(x,0)=e^{-x^2}$. Characteristics give $u=e^{-(x-2t)^2}$. Its peak lies at $x=2t$. Setting $z=x-2t$ gives $u_t=4ze^{-z^2}$ and $2u_x=-4ze^{-z^2}$, so the PDE residual is zero and the initial profile is recovered.

**2. Two heat modes.** On $[0,\pi]$, solve $u_t=u_{xx}$, zero endpoint data, $u(x,0)=\sin x+\tfrac12\sin2x$. Each sine is already an eigenfunction. Hence $u=e^{-t}\sin x+\tfrac12e^{-4t}\sin2x$. The second coefficient at $t=\log2$ is $1/32$, while the first is $1/2$. Direct differentiation checks the two rates independently.

**3. Steady conduction.** Solve $u''=0$ on $0<x<L$, $u(0)=T_0$, $u(L)=T_1$, where $L>0$. Integration gives $u=ax+b$; data give $b=T_0$, $a=(T_1-T_0)/L$. The temperature stays between the endpoint temperatures, consistent with the maximum principle. Constant conductivity produces constant heat flux $-k(T_1-T_0)/L$.

**4. A conservation-law shock.** For $u_t+(u^2/2)_x=0$, let initial states be $u_L=2$ for $x<0$ and $u_R=0$ for $x>0$. A discontinuity moving at speed $s$ obeys Rankine–Hugoniot: $s(u_L-u_R)=f(u_L)-f(u_R)$. Thus $s=1$. Characteristics have speeds two and zero and enter the shock from both sides, satisfying the entropy condition. Merely satisfying the weak equation would not select every physically admissible discontinuity.

## Practice problems

1. Classify $u_{xx}+u_{yy}=0$, $u_{xx}-u_{yy}=0$, and $u_{xx}=u_t$.
2. Solve the wave problem with $c=1$, $f(x)=\cos x$, $g(x)=0$ on the line.
3. For $-u''=1$ on $[0,1]$ with zero endpoint values, find $u$ and its maximum.
4. For Burgers' equation, explain why states $u_L=0$, $u_R=2$ require a rarefaction rather than the same entropy shock construction.

## Answers and explanations

1. They are elliptic, hyperbolic, and parabolic, respectively. In the last equation the principal second-order part is degenerate in the $(x,t)$ variables; the first-order time term carries the evolution.
2. D'Alembert gives $[\cos(x-t)+\cos(x+t)]/2=\cos x\cos t$. The initial velocity vanishes and $u_{tt}=u_{xx}$.
3. Integrating twice and imposing endpoints gives $u=x(1-x)/2$. Its derivative vanishes at $1/2$, where the maximum is $1/8$; nonnegativity agrees with the sign of $-u''$.
4. Characteristics spread rather than collide. The entropy solution for $t>0$ is $0$ for $x/t<0$, $x/t$ for $0\le x/t\le2$, and $2$ for $x/t>2$. Within the fan, substitution verifies $u_t+uu_x=0$.

## Common mistakes and misconceptions

Specifying both arbitrary boundary value and arbitrary normal derivative for an elliptic equation generally overdetermines it. Weak solutions need not be unique without an entropy condition for nonlinear conservation laws. Smoothness at positive heat time does not imply arbitrary initial data were smooth. A Fourier series solution must match the actual boundary conditions; sine and cosine bases are not interchangeable by appearance.

## Connections to other mathematics

[Real analysis](../analysis/real-analysis-and-measure.md) provides integral convergence and distributions. [Harmonic analysis](../harmonic-analysis/transforms-and-special-functions.md) diagonalizes constant-coefficient operators. Reaction–diffusion systems $u_t=D\Delta u+R(u)$ combine diffusion and local kinetics; linearizing and testing spatial eigenmodes can reveal growth of patterns even when homogeneous reaction dynamics are stable.

## Applications

For homogeneous material, $\rho c_pT_t=k\Delta T+q$ combines density $\rho$ in kg/m³, specific heat $c_p$ in J/(kg·K), conductivity $k$ in W/(m·K), and volumetric source $q$ in W/m³. Every term is W/m³. Dividing by $\rho c_p$ gives diffusivity $\kappa=k/(\rho c_p)$ in m²/s. The model requires a continuum scale and the chosen constitutive assumptions; interface conditions need separate treatment.

## Optional computational examples

[plot_analysis.py](../../scripts/plot_analysis.py) renders the exact two-mode heat solution. [verify_analysis.py](../../scripts/verify_analysis.py) checks transport, heat, wave, Poisson, and jump-condition residuals. These checks do not establish general well-posedness or numerical-method convergence.

## References and recommended reading

Sources and further study: Jiří Lebl, [Notes on Diffy Qs](https://www.jirka.org/diffyqs/), Fourier series/PDEs and characteristics; Niels Walet, [Partial Differential Equations](https://math.libretexts.org/Bookshelves/Differential_Equations/Partial_Differential_Equations_%28Walet%29), classical models and separation methods. Weak existence, entropy theory, and general regularity are introductory bridges with proofs omitted explicitly.

## Revision and mastery status

Written 2026-10-18. Scope includes all group 11 themes at reference level, with worked classical and weak-solution examples; it is not a full elliptic/parabolic/hyperbolic specialist course. Mastery requires choosing compatible data, checking dimensions, deriving a weak form, and distinguishing classical from entropy solutions. Learner assessment remains open.
