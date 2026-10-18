# Approximation and optimization: decide what an error means

**Lesson ID:** LES-ADV-002  
**Level:** Undergraduate numerical mathematics.  
**Prerequisites:** Derivatives, Taylor expansion, vectors, symmetric matrices and eigenvalues. Read [numerical analysis](../../subjects/numerical-analysis/numerical-analysis.md) and [optimization and control](../../subjects/optimization/optimization-and-control.md) alongside this lesson.  
**Objectives:** Separate conditioning from algorithmic error; compare bracketing with Newton iteration; derive a descent step bound; analyze gradient descent by eigenvalues; certify a constrained quadratic using KKT conditions.  
**Status:** Written guided lesson; learner mastery remains unassessed.

A computer can return many digits for an inaccurate answer, and a mathematically correct solver can return a very sensitive answer to uncertain data. Before choosing an algorithm, name the exact problem, the approximation, the norm and the stopping condition. This lesson follows two connected tasks: solving an equation and minimizing a function. Their iterations may look similar, but their guarantees depend on different hypotheses.

## Stage 1: separate data sensitivity from arithmetic and approximation

Let the exact mathematical answer be $x=G(b)$ for data $b$. **Conditioning** asks how much $G(b)$ changes when the data change. **Forward error** compares an algorithm's output $\hat x$ with $G(b)$. **Backward error** asks whether $\hat x=G(b+\delta b)$ for a small perturbation. A backward-stable algorithm solves a nearby problem accurately; the nearby problem may still have a substantially different answer when the original problem is ill-conditioned.

**Worked example 1: a sensitive two-equation system.** Let $\varepsilon>0$ and solve

$$x_1+x_2=2,\qquad x_1+(1+\varepsilon)x_2=2+\varepsilon.$$

Subtracting the equations gives $\varepsilon x_2=\varepsilon$, so the exact answer is $(1,1)$. Now increase only the second right-hand side by $\delta$. The perturbed exact answer becomes

$$x_2=1+\frac\delta\varepsilon,\qquad x_1=1-\frac\delta\varepsilon.$$

At $\varepsilon=1/100$ and $\delta=1/1000$, the new answer is $(9/10,11/10)$. Both equations can be satisfied exactly, yet the state changes by ten percent in relative Euclidean norm. The relative data perturbation is only $|\delta|/\sqrt{4+(2+\varepsilon)^2}\approx0.00035267$. This amplification belongs to the equations. Reducing a solver's residual cannot eliminate uncertainty already present in the measured right-hand side.

For a nonsingular matrix $A$, the residual is $r=b-A\hat x$. Since $A(x-\hat x)=r$, one obtains $\|x-\hat x\|\le\|A^{-1}\|\|r\|$. A small residual implies a small error only when the inverse norm and scaling are controlled. Relative versions introduce the condition number $\kappa(A)=\|A\|\|A^{-1}\|$. The chosen norm and units matter; rescaling metres to millimetres changes the numerical representation without creating new physical information.

Now consider computing $g(\delta)=\sqrt{1+\delta}-1$ for a tiny nonzero $\delta>-1$. The exact identity

$$g(\delta)=\frac\delta{\sqrt{1+\delta}+1}$$

avoids subtracting two quantities close to one. The relative condition number with respect to $\delta$ is

$$\left|\frac{\delta g'(\delta)}{g(\delta)}\right|
=\frac{\sqrt{1+\delta}+1}{2\sqrt{1+\delta}}\longrightarrow1.$$

The problem is reasonably conditioned near zero, but an algorithm that rounds both nearly equal terms before subtracting can lose relative accuracy. That is an algorithmic issue. The rationalized formula demonstrates that sensitivity and cancellation are separate questions. At $\delta=0$, the exact answer is zero and relative error must be replaced by an absolute error statement.

## Stage 2: bracket a root before trusting a local iteration

Suppose a continuous real function satisfies $f(a)f(b)<0$. The intermediate value theorem guarantees at least one root in $(a,b)$. Bisection evaluates the midpoint and retains a subinterval with opposite endpoint signs, unless a root is found exactly. After $k$ halvings the retained interval has width $(b-a)/2^k$; its midpoint is within half this width of some root in the interval. This guarantee needs continuity and reliable sign evaluation. An apparent sign change across a pole does not establish a root.

Newton's formula

$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}$$

comes from setting the tangent approximation $f(x_k)+f'(x_k)(x-x_k)$ to zero. It requires $f'(x_k)\ne0$. Near a simple root with sufficient smoothness and a close initial guess, the error is typically quadratic. This is a local statement, unlike bisection's retained bracket. A practical safeguarded method can propose a Newton step and fall back to a bracket step when the proposal is unsafe or unhelpful.

A stopping rule should identify the error it controls. If a root $r$ and candidate $x$ lie in an interval where $|f'|\ge m>0$, the mean value theorem gives $|f(x)|=|f'(\xi)||x-r|$ for an intermediate $\xi$, hence $|x-r|\le|f(x)|/m$. Without a derivative lower bound, a small residual can correspond to a much larger root error. For $f(x)=x^3$, residual $10^{-9}$ at $x=10^{-3}$ accompanies root error $10^{-3}$. Stopping only when successive iterates differ little can also mistake floating-point stagnation for accuracy. A sensible report combines a scaled residual, an iterate-change test, and a retained bracket when one exists. The bracket establishes the existence of at least one root, but not uniqueness: uniqueness needs an additional argument such as strict monotonicity. At an exact endpoint root, return that endpoint before applying an opposite-sign requirement. These small cases make the difference between a method's textbook description and a reliable implementation.

**Worked example 2: approximate $\sqrt2$ exactly before rounding.** Set $f(x)=x^2-2$. The interval $[1,2]$ brackets its positive root. Newton simplifies to $x_{k+1}=(x_k+2/x_k)/2$. From $x_0=1$, the iterates are

$$x_1=\frac32,\qquad x_2=\frac{17}{12},\qquad x_3=\frac{577}{408}.$$

If $r=\sqrt2$ and $e_k=x_k-r$, direct algebra gives

$$e_{k+1}=\frac{(x_k-r)^2}{2x_k}=\frac{e_k^2}{2x_k}.$$

For positive $x_k$ the denominator is positive, so after the first step the iterate is at or above $r$. The error then decreases rapidly. For the last fraction,

$$x_3^2-2=\frac1{166464},\qquad
x_3-r=\frac1{166464(x_3+r)}.$$

These are exact polynomial residual and solution-error identities, respectively. They show explicitly why a residual and a root error are different quantities. Bisection converges more slowly but preserves a guaranteed interval; Newton's exceptional speed comes from curvature and a well-positioned iterate, not from iteration alone.

![A sensitive linear-system response to small data perturbations, beside exact-root errors of bisection and Newton for square root of two.](../../assets/figures/lessons-advanced/conditioning-and-roots.png)

**A failure worth calculating.** For $f(x)=x^3-2x+2$, starting Newton at zero gives $x_1=1$, since $f(0)=2$ and $f'(0)=-2$. At one, $f(1)=1$ and $f'(1)=1$, so $x_2=0$. The method cycles forever between zero and one, although the polynomial has a real root between $-2$ and $-1$. A small change in the starting point or a bracket safeguard changes the problem-solving strategy; claiming “Newton always converges” would conceal the failure.

## Stage 3: derive a step-size bound from smoothness

To minimize a differentiable $f:\mathbb R^n\to\mathbb R$, let $g=\nabla f(x)$. Assume the gradient is $L$-Lipschitz on the segment between $x$ and $x+p$, meaning $\|\nabla f(u)-\nabla f(v)\|\le L\|u-v\|$ there. The fundamental theorem applied along the segment gives

$$f(x+p)-f(x)=\int_0^1\nabla f(x+tp)^Tp\,dt.$$

Subtract $g^Tp$, apply Cauchy–Schwarz and the Lipschitz bound, and integrate $Lt\|p\|^2$. The result is the descent inequality

$$f(x+p)\le f(x)+g^Tp+\frac L2\|p\|^2.$$

Putting $p=-\alpha g$ yields

$$f(x-\alpha g)\le f(x)-\alpha\left(1-\frac{L\alpha}2\right)\|g\|^2.$$

Thus $0<\alpha<2/L$ guarantees a strict decrease when $g\ne0$, provided the same smoothness bound applies to the entire proposed segment. The convenient choice $\alpha=1/L$ gives a decrease of at least $\|g\|^2/(2L)$. This is a bound, not an exact formula for a general nonlinear objective. Local estimates that underestimate $L$ may not give safe global steps; line searches check actual progress.

## Stage 4: see gradient descent one eigenvector at a time

**Worked example 3: a quadratic with two scales.** Take

$$f(x)=\tfrac12(x_1^2+4x_2^2),\qquad H=\begin{pmatrix}1&0\\0&4\end{pmatrix}.$$

The unique minimizer is zero. Gradient descent gives $x_{k+1}=(I-\alpha H)x_k$, hence

$$x_{1,k}=(1-\alpha)^kx_{1,0},\qquad
x_{2,k}=(1-4\alpha)^kx_{2,0}.$$

Convergence from every starting point requires both multipliers to have magnitude less than one, so $0<\alpha<1/2$. At $\alpha=1/4$, the second coordinate becomes zero in one step, while the first shrinks by $3/4$ per step. At $\alpha=0.49$, the factors are $0.51$ and $-0.96$: the fast direction oscillates slowly toward zero. At $\alpha=0.6$, its factor is $-1.4$, so almost every trajectory diverges.

More generally a symmetric positive-definite Hessian has an orthonormal eigenbasis. In eigen-direction $i$, the error multiplier is $1-\alpha\lambda_i$. With smallest and largest eigenvalues $m,L>0$, the best constant worst-direction step for a quadratic is $\alpha_*=2/(m+L)$. It balances $1-\alpha m$ against $-(1-\alpha L)$ and gives contraction $(L-m)/(L+m)$. Here $\alpha_*=2/5$ and both coordinate magnitudes contract by $3/5$ per iteration. The objective contracts by $(3/5)^2=9/25$, since it is quadratic. This eigenanalysis explains the effect of a large condition ratio $L/m$: some directions then restrict the step while others advance slowly.

![Quadratic gradient-descent trajectories for several step sizes, and a constrained quadratic with its KKT optimum and active boundary.](../../assets/figures/lessons-advanced/descent-and-constraints.png)

## Stage 5: certify a constrained solution

**Worked example 4: a weighted target under a shared limit.** Minimize

$$f(x,y)=(x-2)^2+2(y-1)^2$$

subject to $x+y\le2$, $x\ge0$, $y\ge0$. The Hessian $\operatorname{diag}(2,4)$ is positive definite, so the objective is strictly convex. The feasible region is a nonempty compact triangle, so a minimizer exists and is unique. The unconstrained minimizer $(2,1)$ violates the shared limit.

Use inequalities $g_0=x+y-2$, $g_1=-x$, $g_2=-y$, with nonnegative multipliers $\lambda,\mu,\nu$. Stationarity is

$$2(x-2)+\lambda-\mu=0,\qquad4(y-1)+\lambda-\nu=0.$$

If both coordinates are positive, complementary slackness gives $\mu=\nu=0$. The shared bound must be active here, so $x+y=2$. Solving gives $\lambda=4/3$, $x=4/3$ and $y=2/3$. Both coordinates are indeed positive, checking the assumed active set. All multipliers are nonnegative and all KKT conditions hold; convexity makes them a global optimality certificate. Slater's condition also holds, for example at $(1/2,1/2)$, though sufficiency of a feasible convex KKT certificate does not require invoking it.

For an independent bound, put $a=x-2$, $b=y-1$. Feasibility implies $a+b\le-1$. Weighted Cauchy–Schwarz gives $(a+b)^2\le(1+1/2)(a^2+2b^2)$, hence $f\ge2/3$. Our point attains $4/9+2/9=2/3$. This second argument verifies the optimum without relying on solver output or a plotted contour.

## Practice problems

1. In the sensitive system, set $\varepsilon=1/1000$ and $\delta=1/10000$. Find the perturbed exact answer. What ratio controls the change?
2. Why does a sign change between $-1$ and $1$ fail to prove a zero for $f(x)=1/x$?
3. Starting with a bracket of width one, how many halvings guarantee the retained midpoint is within $1/1000$ of some root?
4. For $f(x)=x^2-9$, take one Newton step from $x_0=4$ and compute its exact polynomial residual.
5. If $L=6$ and $\|\nabla f(x)\|=2$, what decrease is guaranteed by $\alpha=1/L$ under the stated smoothness assumptions?
6. For $H=\operatorname{diag}(2,10)$, find the interval of constant steps that converges from every start and the best worst-direction step.
7. For the same Hessian and $\alpha=1/10$, what are the coordinate error multipliers? Explain why one direction still converges slowly.
8. Minimize $(x-3)^2+y^2$ subject to $x+y\le1$, with $x,y$ otherwise unrestricted. Find the KKT point and verify its objective value.

## Answers and explanations

1. The answer remains $(9/10,11/10)$ because $\delta/\varepsilon=1/10$. The absolute perturbations are smaller, but their ratio to the nearly singular coefficient is unchanged.
2. The function is not defined or continuous throughout the interval. The intermediate value theorem's continuity hypothesis fails; crossing a pole is not crossing a root.
3. The midpoint bound is $2^{-(k+1)}$. Require $2^{k+1}\ge1000$; $k=9$ suffices, since $2^{10}=1024$. State that the final answer is the midpoint of the retained interval to avoid an off-by-one convention.
4. The step is $(4+9/4)/2=25/8$. Its residual is $(25/8)^2-9=49/64$. The root error is $1/8$, so again residual and solution error differ.
5. The decrease is at least $\|g\|^2/(2L)=4/12=1/3$. This assertion requires the gradient Lipschitz bound on the step segment, not merely a Hessian value measured at its starting point.
6. Require $0<\alpha<2/10=1/5$. The balanced step is $2/(2+10)=1/6$, with worst-direction magnitude $2/3$.
7. The factors are $1-2/10=4/5$ and $1-10/10=0$. The high-curvature direction vanishes immediately; the lower-curvature direction shrinks by only 20% each iteration.
8. The unconstrained point $(3,0)$ is infeasible. Stationarity gives $2(x-3)+\lambda=0$ and $2y+\lambda=0$, while the active bound gives $x+y=1$. Thus $\lambda=2$, $x=2$, $y=-1$, and the objective is $2$. The feasible set here permits negative $y$; adding an unstated nonnegativity constraint would change the answer.

## Verification and further study

The graphs are reproduced by [plot_lessons_advanced.py](../../scripts/plot_lessons_advanced.py), and [verify_lessons_advanced.py](../../scripts/verify_lessons_advanced.py) checks exact sensitivity, root iterates, eigenmultipliers and KKT certificates. For fuller analysis see Driscoll and Braun's [*Fundamentals of Numerical Computation*](https://fncbook.com/) and Boyd and Vandenberghe's [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/). A useful final explanation is: “This residual is small in this norm; the problem's sensitivity is this large; therefore these digits have this limited support.” Write that explanation for worked example 1 before recording mastery.
