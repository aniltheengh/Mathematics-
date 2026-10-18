# Optimization, operations research and control

**Topic ID:** OPT-001  
**Classification:** Optimization → constrained decisions → dynamical control  
**Level:** Undergraduate reference with graduate introductions  
**Content status:** Written compact reference; major existence and duality results are stated, not exhaustively proved.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Approximation and optimization: decide what an error means](../../lessons/advanced/approximation-and-optimization.md)
<!-- guided-lessons:end -->

## Prerequisites

Derivatives, gradients, matrices, eigenvalues, ordinary differential equations and basic probability are needed. Diagnostic: minimizing $(x-3)^2$ over $x\le1$ gives $x=1$, even though the unconstrained derivative vanishes at $3$. Constraints can determine the optimum. Numerical implementation also needs [conditioning and stopping criteria](../numerical-analysis/numerical-analysis.md).

## Definition

An **optimization problem** minimizes an objective $f(x)$ over a feasible set $C$. A **global minimizer** is no worse than every feasible point; a **local minimizer** is no worse than sufficiently nearby feasible points. A set is **convex** if $\theta x+(1-\theta)y\in C$ for all $x,y\in C$ and $0\le\theta\le1$. A function is convex if

$$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y).$$

Strict convexity gives at most one minimizer; it does not itself ensure that a minimizer exists. Compactness of a nonempty feasible set with continuous objective is one sufficient existence condition. A coercive continuous objective on a closed nonempty subset of finite-dimensional space also attains a minimum.

## Intuitive explanation

Optimization makes a decision rule explicit: what can change, what is being minimized, and what must remain feasible. Control chooses inputs as time evolves, often using feedback from measurements. A mathematically optimal action is useful only relative to the stated model, objective, uncertainty and constraints. Minimizing pump energy while omitting required flow gives a trivial but useless result.

![Convex quadratic contours and the active inequality boundary, showing an optimum at one and one.](../../assets/figures/advanced/optimization.png)

The unconstrained center is $(0,0)$; the feasible region $x+y\ge2$ moves the closest feasible point to $(1,1)$.

## Mathematical notation

$x\in\mathbb R^n$ is a decision vector, $\nabla f$ its gradient, $H=\nabla^2f$ its Hessian, $g_i(x)\le0$ inequalities and $h_j(x)=0$ equalities. Multipliers for inequalities are $\lambda_i\ge0$ and equality multipliers $\nu_j\in\mathbb R$. For control, $z(t)$ is state, $u(t)$ input, and $y(t)$ measured output; $A,B,C$ are compatible constant matrices. Objective units must be consistent, or explicit weights must convert competing terms.

## Fundamental properties

For differentiable convex $f$ on a convex open domain,

$$f(y)\ge f(x)+\nabla f(x)^T(y-x).$$

Thus $\nabla f(x)=0$ implies a global minimum. For twice-differentiable $f$, a positive-semidefinite Hessian everywhere on a convex open domain is equivalent to convexity. At a smooth unconstrained local minimum, the gradient vanishes and the Hessian is positive semidefinite; the conditions are necessary but do not make every stationary point a minimum.

For equality constraints with linearly independent gradients, a smooth local optimizer satisfies $\nabla f+\sum_j\nu_j\nabla h_j=0$. This Lagrange condition expresses orthogonality to allowable tangent directions. Without constraint qualifications multipliers can fail to exist, even at an optimum.

## Important formulas and identities

For $L(x,\lambda,\nu)=f(x)+\sum_i\lambda_i g_i(x)+\sum_j\nu_j h_j(x)$, the **Karush–Kuhn–Tucker conditions** are stationarity $\nabla_xL=0$, primal feasibility, dual feasibility $\lambda_i\ge0$, and complementary slackness $\lambda_i g_i(x)=0$. Under appropriate qualifications they are necessary. For convex differentiable $f,g_i$ and affine $h_j$, a feasible KKT point is globally optimal. Slater's strict-feasibility condition is a standard sufficient condition for strong duality in this convex setting, subject to the usual finite-optimum assumptions.

The dual function $q(\lambda,\nu)=\inf_x L(x,\lambda,\nu)$ gives a lower bound on the primal minimum for $\lambda\ge0$. The dual maximizes this bound. A primal–dual gap provides an optimality certificate when feasibility is checked; an optimizer's success message alone is weaker evidence.

**Problem classes.** Linear programming has affine objective and constraints. Quadratic programming has a quadratic objective and affine constraints; it is convex when the quadratic matrix is positive semidefinite. Integer programming restricts some decisions to integers, creating discrete choices such as equipment counts. Nonlinear programming allows nonlinear objective or constraints and may have several local optima. Stochastic programming minimizes expectations or risk measures under an explicit probability model; a two-stage example chooses capacity now and pays uncertain recourse cost later. Scenario approximations require out-of-sample assessment.

**Algorithms.** Gradient descent uses $x_{k+1}=x_k-\alpha_k\nabla f(x_k)$. For convex functions with $L$-Lipschitz gradient, suitable steps such as $0<\alpha\le1/L$ ensure descent. Newton solves $H_kp_k=-\nabla f_k$ and sets $x_{k+1}=x_k+\alpha_kp_k$; an indefinite Hessian may require modification. Quasi-Newton methods build curvature approximations from successive gradients; BFGS preserves positive definiteness under a positive curvature condition. Line searches and constraint handling remain essential.

**Variations and optimal control.** For $J[x]=\int_a^b F(t,x,x')\,dt$ with fixed endpoints and sufficient smoothness, stationarity gives the Euler–Lagrange equation $F_x-d(F_{x'})/dt=0$. In control with $\dot z=f(z,u)$ and running cost $\ell$, the Hamiltonian $H=\ell+p^Tf$ yields the costate equation $\dot p=-H_z$ and a Hamiltonian-minimizing control under the hypotheses of the minimum principle. These are necessary conditions, not an automatic global certificate.

**Dynamic programming** uses the principle that an optimal continuation is optimal for its reached state. In a finite discounted Markov decision model,

$$V(s)=\min_a\left[c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')\right],\quad0\le\gamma<1.$$

Scheduling adds timing, resource and precedence constraints; a two-task precedence relation is $s_2\ge s_1+p_1$ for start times $s_i$ and duration $p_1$. Decision theory compares expected losses; game theory allows outcomes to depend on other decision makers. A Nash equilibrium allows no player to improve by a unilateral change, which need not maximize collective welfare.

For $\dot z=Az+Bu$, the **controllability matrix** $[B,AB,\ldots,A^{n-1}B]$ has full row rank exactly when every state can be reached in finite time for the unconstrained linear system. For $y=Cz$, the **observability matrix** $[C^T,(CA)^T,\ldots,(CA^{n-1})^T]^T$ has full column rank exactly when initial states can be distinguished from noiseless output histories. These rank tests do not include actuator limits or measurement noise.

A linear system $\dot z=Az$ is asymptotically stable when all eigenvalues have negative real part. A positive-definite $P$ satisfying $A^TP+PA=-Q$ for $Q>0$ gives the Lyapunov function $z^TPz$. A state observer $\dot{\hat z}=A\hat z+Bu+L(y-C\hat z)$ has error dynamics $\dot e=(A-LC)e$. Kalman estimation adds stochastic noise assumptions and minimizes mean-square error within its stated linear Gaussian setting.

## Derivations and proofs

**Convex KKT sufficiency.** At a feasible KKT point $x_*$, convexity gives $f(x)\ge f(x_*)+\nabla f(x_*)^T(x-x_*)$. Insert stationarity. For each convex $g_i$, $\nabla g_i(x_*)^T(x-x_*)\le g_i(x)-g_i(x_*)\le-g_i(x_*)$. Multiplying by $-\lambda_i$ and summing gives a nonnegative contribution because complementary slackness makes $\lambda_i g_i(x_*)=0$. Affine equality contributions vanish. Hence $f(x)\ge f(x_*)$ for every feasible $x$.

**Euler–Lagrange derivation.** Perturb a candidate by $x+\varepsilon\eta$, with $\eta(a)=\eta(b)=0$. Differentiation under the integral gives $\delta J=\int(F_x\eta+F_{x'}\eta')dt$. Integration by parts removes the endpoint term and gives $\delta J=\int[F_x-d(F_{x'})/dt]\eta\,dt$. The fundamental lemma yields the equation when the variation vanishes for all admissible smooth $\eta$.

## Worked examples

**1. A constrained quadratic.** Minimize $x^2+y^2$ with $x+y\ge2$. Use $g=2-x-y$. Stationarity gives $2x=\lambda$, $2y=\lambda$. The optimum cannot have $\lambda=0$, since the origin is infeasible. Complementary slackness gives $x+y=2$, hence $x=y=1$, $\lambda=2$. The objective is $2$, and $(x+y)^2\le2(x^2+y^2)$ independently proves the lower bound.

**2. Allocation with integers.** Units A and B deliver $3$ and $5$ units of flow and cost $4$ and $7$. Minimize $4a+7b$ for nonnegative integers with $3a+5b\ge10$. For $b=0$, the cheapest is $a=4$, cost $16$; for $b=1$, $a=2$, cost $15$; for $b=2$, $a=0$, cost $14$. Values $b\ge3$ cost at least $21$. Thus $(0,2)$ is optimal. The continuous relaxation has cost $40/3$, illustrating why rounding its solution needs a feasibility check.

**3. Double integrator.** Let $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $B=(0,1)^T$, $C=(1,0)$. The controllability matrix is $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and observability matrix the identity; both have rank two. Feedback $u=-2z_1-3z_2$ gives characteristic polynomial $s^2+3s+2=(s+1)(s+2)$, so the closed loop is asymptotically stable in this ideal linear model.

**4. A short variational problem.** Minimize $\int_0^1(x')^2dt$ with $x(0)=0$, $x(1)=1$. Euler–Lagrange gives $x''=0$, hence $x=t$. For any competitor $x=t+\eta$, $J=1+2\int\eta'+\int(\eta')^2=1+\int(\eta')^2\ge1$. The endpoint conditions make the middle term zero, proving global optimality.

## Practice problems

1. Is $f(x)=x^4$ strictly convex, and does $f''(0)=0$ rule out a strict minimum?
2. Minimize $(x-4)^2$ under $x\le1$; find the KKT multiplier.
3. For $A=\operatorname{diag}(-1,-2)$, $B=(1,0)^T$, is the system controllable?
4. A two-stage path costs $3$ then $5$, while an alternative costs $4$ then $2$. Which total cost does deterministic dynamic programming select?

## Answers and explanations

1. $x^4$ is strictly convex and has its unique strict minimum at zero. A positive-definite Hessian is sufficient for a strict local minimum, not necessary.
2. With $g=x-1$, stationarity is $2(x-4)+\lambda=0$. At $x=1$, $\lambda=6\ge0$; complementary slackness holds and convexity certifies the result.
3. No. $[B,AB]=\begin{pmatrix}1&-1\\0&0\end{pmatrix}$ has rank one. The second state is stable but cannot be actuated.
4. The alternatives total $8$ and $6$; choose $6$. The recursion compares the immediate cost plus the optimal remaining cost, not only the first edge.

## Common mistakes and misconceptions

Stationarity alone does not distinguish a saddle. KKT necessity needs qualifications. A nonlinear solver may find a local minimum, while a convex certificate can establish a global one. Controllability does not ensure acceptable bounded input, and observability does not ensure good estimation with noisy sensors. Objective weights encode choices and need stated units or normalization.

## Connections to other mathematics

[Numerical analysis](../numerical-analysis/numerical-analysis.md) supplies algorithms; [probability](../probability/probability-and-stochastic-processes.md) supplies uncertainty models; [modeling](../applied-mathematics/modeling.md) supplies physical objectives and state equations.

## Applications

Pump scheduling balances required delivery, storage limits, start costs and energy tariffs. A model can choose binary on/off states and continuous flows while enforcing mass balance. Feedback control updates these decisions from measured states. Actual implementation requires calibrated dynamics, actuator limits and an objective consistent with the plant's operating requirements.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) draws the quadratic feasible set. [Checks](../../scripts/verify_advanced.py) verify KKT equations, enumerate the small integer problem, and check control ranks and closed-loop eigenvalues independently.

## References and recommended reading

- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), chapters 2–5 and 9–11: convexity, duality and algorithms.
- Russ Tedrake, [*Underactuated Robotics*, dynamic programming](https://underactuated.mit.edu/dp.html) and [linear quadratic regulators](https://underactuated.mit.edu/lqr.html): control follow-up. Full proofs of the rank tests and minimum principle are outside this reference chapter.

## Revision and mastery status

Written 2026-10-18. The full subject-map scope is introduced mathematically; comprehensive operations research or optimal-control theory needs further study. Mastery requires specifying feasible decisions, checking sufficient optimality conditions, and distinguishing stability, controllability and observability.
