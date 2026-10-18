# Functional analysis and operator theory

**Topic ID:** FA-001  
**Classification:** Analysis → function spaces → linear operators  
**Level:** Upper undergraduate to graduate introduction  
**Content status:** Written compact reference; major Banach-space theorems are stated with hypotheses and references.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Spaces and convergence: what does it mean to get close?](../../lessons/advanced/spaces-and-convergence.md)
<!-- guided-lessons:end -->

## Prerequisites

Linear algebra, rigorous convergence, integrals, and metric-space completeness are needed. Lebesgue integration supports $L^p$ spaces. Diagnostic: in $\ell^2$, the coordinate vectors $e_n$ all have norm one and pairwise distance $\sqrt2$, so boundedness does not imply a norm-convergent subsequence. This sharply distinguishes infinite-dimensional geometry from finite-dimensional Euclidean space. [Topology](../topology/topology.md) supplies compactness and continuity language.

## Definition

A **normed space** is a real or complex vector space $X$ with $\|x\|\ge0$, equality exactly at zero, absolute homogeneity $\|\alpha x\|=|\alpha|\|x\|$, and the triangle inequality. A **Banach space** is complete in the induced metric: every Cauchy sequence converges in the space. A **bounded linear operator** $T:X\to Y$ satisfies $\|Tx\|\le C\|x\|$ for some finite $C$; its operator norm is $\|T\|=\sup_{\|x\|\le1}\|Tx\|$. For linear maps between normed spaces, boundedness is equivalent to continuity.

A **Hilbert space** is complete in the norm from an inner product. Throughout this book the complex inner product is conjugate-linear in its first argument and linear in its second, so $\langle u,v\rangle=u^*v$ in finite-dimensional coordinates. The **continuous dual** $X^*$ is the space of bounded scalar-valued linear functionals on $X$. An algebraic linear functional may be discontinuous in infinite dimensions, so the word “continuous” matters.

## Intuitive explanation

A function can be treated as a vector whose coordinates are infinitely many mode amplitudes. Norms specify what counts as a small error: a supremum norm controls the largest pointwise error, while an $L^2$ norm controls integrated squared error. Completeness ensures an improving Cauchy sequence has a limit within the space where the problem is posed. The choice of space is therefore part of the mathematical model, not decorative notation.

![A function x squared and its orthogonal linear approximation, with signed residual shading.](../../assets/figures/advanced/function-projection.png)

The projection is $x-1/6$ on $[0,1]$ with the unweighted $L^2$ inner product. Its residual is orthogonal to both $1$ and $x$, rather than zero at every point.

## Mathematical notation

$C[a,b]$ denotes continuous functions with $\|f\|_\infty=\max|f|$, a Banach space. $L^p(\Omega)$ consists of equivalence classes equal almost everywhere with $\int|f|^p<\infty$ for $1\le p<\infty$; its norm is $(\int|f|^p)^{1/p}$. $L^\infty$ uses essential supremum. $\ell^2$ is the space of square-summable sequences. $H$ denotes a Hilbert space, $M^\perp$ an orthogonal complement, $T^*$ an adjoint, and $\rightharpoonup$ weak convergence. No pointwise value is intrinsically defined for an arbitrary $L^p$ equivalence class.

## Fundamental properties

**Projection theorem, stated.** For a closed subspace $M$ of a Hilbert space and $x\in H$, there is a unique $m\in M$ minimizing $\|x-m\|$. The residual $x-m$ is orthogonal to $M$. Closedness is necessary: projecting onto an incomplete collection can give an unattained infimum.

An orthonormal sequence $(e_n)$ satisfies $\langle e_n,e_m\rangle=\delta_{nm}$. Bessel's inequality is $\sum_n|\langle e_n,x\rangle|^2\le\|x\|^2$. A complete orthonormal basis gives $x=\sum_n\langle e_n,x\rangle e_n$ in norm and Parseval's identity $\|x\|^2=\sum_n|\langle e_n,x\rangle|^2$. The word basis here refers to norm-convergent series, not a finite linear combination as with a Hamel basis.

The **Riesz representation theorem** for a Hilbert space says every bounded linear functional has the form $\ell(x)=\langle y,x\rangle$ for a unique $y\in H$, with $\|\ell\|=\|y\|$. It does not say the dual of every Banach space is naturally the same as the space itself.

## Important formulas and identities

**Hahn–Banach, norm-preserving form.** A bounded linear functional on a linear subspace of a real or complex normed space extends to the whole space with the same norm. In particular, for nonzero $x\in X$ there exists $\ell\in X^*$ with $\|\ell\|=1$ and $\ell(x)=\|x\|$. The proof is not reproduced here; its extension argument is deeper than finite-dimensional elimination.

**Weak convergence** $x_n\rightharpoonup x$ means $\ell(x_n)\to\ell(x)$ for every $\ell\in X^*$. Norm convergence implies weak convergence. The converse fails: $e_n\rightharpoonup0$ in $\ell^2$, because for each fixed $y\in\ell^2$, $\langle y,e_n\rangle=\overline{y_n}\to0$, yet $\|e_n\|=1$. Weakly convergent sequences are norm-bounded. Reflexive Banach spaces have weak compactness properties that support existence proofs in variational problems; these results require functional-analytic theorems rather than pointwise reasoning.

Three major Banach-space results share the completeness hypothesis:

- **Uniform boundedness:** if $X$ is Banach and a family $T_i:X\to Y$ of bounded linear operators is pointwise bounded, $\sup_i\|T_ix\|<\infty$ for every $x$, then $\sup_i\|T_i\|<\infty$.
- **Open mapping:** a bounded surjective linear map between Banach spaces maps open sets to open sets. A bounded bijection consequently has bounded inverse.
- **Closed graph:** a linear map defined on all of a Banach space with values in another Banach space is bounded if its graph is closed in the product space.

These are sourced theorems, not consequences of checking a few vectors. For an unbounded differential operator, its domain is usually a proper dense subspace, so the closed graph statement above cannot be used to declare it bounded on all of $L^2$.

An operator is **compact** if it maps bounded sets to relatively compact sets. Bounded finite-rank operators are compact; the identity on an infinite-dimensional Hilbert space is not. A bounded operator on a Hilbert space is **self-adjoint** when $T=T^*$, where $\langle Tx,y\rangle=\langle x,T^*y\rangle$. A compact self-adjoint operator has real nonzero eigenvalues of finite multiplicity, possible accumulation only at zero, and an orthonormal eigenbasis for the closure of its range together with its kernel. Equivalently one can choose a full orthonormal eigenbasis in a separable Hilbert space. The proof is deferred.

The **spectrum** $\sigma(T)$ consists of scalars $\lambda$ for which $T-\lambda I$ has no bounded everywhere-defined inverse. In infinite dimensions, spectral values need not be eigenvalues. For example, on $L^2[0,1]$, $(Tf)(x)=xf(x)$ has spectrum $[0,1]$ and no eigenvalues: a nonzero eigenfunction would have to be supported on a singleton of measure zero. The general bounded self-adjoint spectral theorem uses projection-valued measures rather than assuming a discrete eigenvector expansion.

## Derivations and proofs

**Projection characterization.** If $m\in M$ minimizes $\|x-m\|$, then for any $v\in M$ the real quadratic $\|x-m-tv\|^2$ has its minimum at $t=0$. Differentiation gives $\operatorname{Re}\langle x-m,v\rangle=0$. In the complex case, repeat with $iv$ to get the imaginary part zero. Conversely, orthogonality gives $\|x-z\|^2=\|x-m\|^2+\|m-z\|^2$ for every $z\in M$, proving minimality and uniqueness. Existence for closed $M$ follows from a minimizing Cauchy sequence using the parallelogram identity; that standard argument is not fully expanded here.

**Weak formulation.** For $-u''=f$ on $(0,1)$ with zero endpoints, multiply by a smooth test function $v$ vanishing at the endpoints and integrate by parts. This gives

$$\int_0^1u'v'\,dx=\int_0^1fv\,dx.$$

The equation needs only first weak derivatives, so it extends beyond twice-classically-differentiable candidates. A **weak derivative** $g$ of $u$ satisfies $\int u\varphi'=-\int g\varphi$ for every smooth compactly supported $\varphi$. The Sobolev space $H^1$ contains $L^2$ functions with first weak derivatives in $L^2$, and $H_0^1$ is the closure of compactly supported smooth functions in the $H^1$ norm. On this interval it enforces zero trace. The Lax–Milgram theorem gives a unique weak solution when the bilinear form is bounded and coercive and the right-hand functional is bounded on a Hilbert space; it is cited rather than proved.

## Worked examples

**1. Best constant.** Approximate $f(x)=x$ on $[0,1]$ by a constant $c$ in $L^2$. Orthogonality to $1$ gives $\int_0^1(x-c)dx=0$, hence $c=1/2$. The squared error is $\int_0^1(x-1/2)^2dx=1/12$. The minimax constant happens also to be $1/2$, but that agreement is specific to this symmetric example.

**2. Best affine function.** Approximate $x^2$ by $a+bx$. Normal equations are $a+b/2=1/3$ and $a/2+b/3=1/4$. Solving gives $a=-1/6$, $b=1$. The residual $x^2-x+1/6$ integrates to zero both alone and multiplied by $x$; its squared norm is $1/180$. This checks the orthogonality and the exact error independently.

**3. A compact diagonal operator.** On $\ell^2$, define $T(x_1,x_2,\ldots)=(x_1,x_2/2,x_3/3,\ldots)$. It is bounded self-adjoint with norm one and eigenvalues $1/n$. Truncating after $N$ coordinates gives finite-rank $T_N$ with $\|T-T_N\|=1/(N+1)\to0$, proving compactness using norm limits of compact operators. Zero lies in the spectrum because the inverse would multiply coordinate $n$ by $n$ and is unbounded, but zero is not an eigenvalue.

**4. A weak solution.** For $f=2$, $u(x)=x(1-x)$ has zero endpoints and $-u''=2$. Integration by parts verifies $\int u'v'=2\int v$ for every $v\in H_0^1$. Its energy $J(v)=\frac12\int(v')^2-2\int v$ is minimized uniquely at $u$: setting $v=u+w$ and using the weak equation gives $J(u+w)-J(u)=\frac12\int(w')^2\ge0$.

## Practice problems

1. Show $\ell(f)=\int_0^1f(x)dx$ is bounded on $L^2[0,1]$ and find its norm.
2. Does $e_n$ converge strongly to zero in $\ell^2$? Does it converge weakly?
3. Find the $L^2[0,1]$ projection of $x^2$ onto constants.
4. Why is point evaluation $f\mapsto f(0)$ not a well-defined functional on all of $L^2[0,1]$?

## Answers and explanations

1. Cauchy–Schwarz gives $|\ell(f)|\le\|f\|_2\|1\|_2=\|f\|_2$. Equality at $f=1$ shows norm one.
2. It is weakly zero because every fixed $\ell^2$ coordinate sequence tends to zero. It is not strongly zero because its norm is constantly one.
3. The constant is the average $\int_0^1x^2dx=1/3$; the residual is orthogonal to $1$.
4. An $L^2$ element is an almost-everywhere equivalence class. Changing a representative at the single point zero preserves that element while changing the proposed value. Additional regularity or a different space is required.

## Common mistakes and misconceptions

Bounded sets are not generally compact in infinite dimensions. Weak convergence is weaker than norm convergence. An eigenfunction expansion needs the operator hypotheses that support it. Derivatives need a specified domain. An $L^2$ error does not uniformly bound pointwise error; a narrow spike can have small integral norm and a large peak.

## Connections to other mathematics

[Numerical analysis](../numerical-analysis/numerical-analysis.md) uses projection in finite elements. [Probability](../probability/probability-and-stochastic-processes.md) uses $L^2$ and conditional expectation. [Differential geometry](../differential-geometry/geometry-and-tensors.md) supplies differential operators on manifolds.

## Applications

Elastic energy, diffusion and vibration models are posed in function spaces that encode finite energy and boundary traces. A finite-element method chooses a finite-dimensional subspace and solves the weak equation there. The functional setting states what the approximation converges to and which boundary conditions have actually been imposed.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) shows the affine projection. [Checks](../../scripts/verify_advanced.py) verify the exact orthogonality equations, squared errors and energy identity. The infinite-dimensional theorems are supported by the references, not certified by a finite matrix computation.

## References and recommended reading

- Casey Rodriguez, MIT OpenCourseWare [18.102 lecture notes and readings](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/): Banach spaces, Hilbert spaces and spectral theory.
- Gerald Teschl, [*Topics in Linear and Nonlinear Functional Analysis*](https://www.mat.univie.ac.at/~gerald/ftp/book-fa/), chapters on Hilbert spaces, compact operators and major Banach-space theorems: further reading; publication availability is described on the author page.

## Revision and mastery status

Written 2026-10-18. Every functional-analysis subject-map bullet has definitions, hypotheses and examples at reference depth. Complete proofs of Hahn–Banach, Baire-category consequences, spectral and Lax–Milgram theorems require a full course. Mastery requires naming the space, norm, domain and topology in a claimed convergence statement.
