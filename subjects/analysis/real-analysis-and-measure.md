# Real analysis and measure theory

**Topic ID:** RA-01.  
**Classification:** Analysis → rigorous limits, measure, and integration.  
**Level:** Undergraduate analysis through a graduate introduction.  
**Content status:** Written compact reference chapter.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Spaces and convergence: what does it mean to get close?](../../lessons/advanced/spaces-and-convergence.md)
<!-- guided-lessons:end -->

## Prerequisites

Know sets, quantifiers, sequences, and [calculus](../calculus/single-variable-calculus.md). Diagnostic: to prove $1/n\to0$, given $\varepsilon>0$, choose an integer $N>1/\varepsilon$; then $n\ge N$ implies $|1/n|<\varepsilon$. The integer is chosen after the tolerance and works for every later term. Reversing those quantifiers changes the statement.

## Definition

A real sequence $a_n$ **converges** to $L$ when for every $\varepsilon>0$ some $N$ satisfies $|a_n-L|<\varepsilon$ for every $n\ge N$. A sequence is **Cauchy** when its sufficiently late pairs are arbitrarily close. The real numbers are complete: every Cauchy sequence of reals converges to a real number. Equivalently, every nonempty real set bounded above has a least upper bound, its supremum. The infimum is the greatest lower bound. Neither bound must belong to the set.

A **metric** $d$ on $X$ is nonnegative, symmetric, zero exactly for identical points, and satisfies the triangle inequality. Completeness is always relative to the chosen metric. The rationals with ordinary distance are incomplete, since rational approximations to $\sqrt2$ are Cauchy without a rational limit.

## Intuitive explanation

Analysis makes approximation promises precise. Completeness says an increasingly consistent approximation has somewhere to land. Compactness makes local information controllable by finitely many pieces. Measure assigns size to sets, including sets too irregular for elementary area formulas. Lebesgue integration accumulates values by measurable level sets and tolerates changes on sets of measure zero, which is crucial for probability and weak differential equations.

![Pointwise but not uniform convergence of x to the power n](../../assets/figures/analysis/pointwise-convergence.png)

The exact functions are $f_n(x)=x^n$ on $[0,1]$, for $n=1,2,5,20$. The pointwise limit is zero for $0\le x<1$ and one at $x=1$, shown with separate endpoint markers. No line is drawn across the limit's discontinuity. All quantities are dimensionless.

## Mathematical notation

$\sup A$ and $\inf A$ are bounds, $\limsup a_n=\lim_N\sup_{n\ge N}a_n$, and $\mathbf1_E$ is the indicator of a set. $\mathcal A$ denotes a sigma-algebra, $\mu$ a measure, and $\int f\,d\mu$ its integral. A property holds **almost everywhere** if it fails only on a measurable null set. Functions in $L^p$ are equivalence classes modulo equality almost everywhere, with $\|f\|_p=(\int|f|^p)^{1/p}$ for $1\le p<\infty$.

## Fundamental properties

A subset is **compact** if every open cover has a finite subcover. In metric spaces this is equivalent to sequential compactness; in $\mathbb R^n$ it is equivalent to being closed and bounded. These equivalences are cited without proof and do not extend unchanged to arbitrary spaces. A complete bounded metric space need not be compact: completeness plus total boundedness is the correct criterion. A space is **connected** if it cannot be split into two nonempty separated open pieces; connected subsets of $\mathbb R$ are intervals.

Continuous maps preserve compactness and connectedness. Hence a continuous real function on a nonempty compact set attains a maximum and minimum; on an interval it takes every intermediate value. These conclusions need their hypotheses: $f(x)=x$ on $(0,1)$ attains neither endpoint bound. On a compact metric domain, continuity implies uniform continuity, meaning one input tolerance works over the entire domain.

An absolutely convergent series of real or complex numbers converges, and rearrangement preserves its sum. Conditional convergence does not have this stability. A function sequence converges **uniformly** when $\sup_x|f_n(x)-f(x)|\to0$. Uniform limits of continuous functions are continuous. For integrable functions on a finite interval, uniform convergence permits passing the limit through the integral. Passing a limit through derivatives needs stronger conditions, such as uniform convergence of derivatives and convergence at one base point.

## Important formulas and identities

A **sigma-algebra** contains the whole space and is closed under complements and countable unions. A **measure** is a map $\mu:\mathcal A\to[0,\infty]$ with $\mu(\varnothing)=0$ and countable additivity on disjoint sets. Lebesgue measure gives an interval its length. A real-valued function is measurable when inverse images of open sets are measurable.

For a nonnegative simple function $s=\sum_{j=1}^k a_j\mathbf1_{E_j}$ with disjoint measurable sets and $a_j\ge0$,

$$\int s\,d\mu=\sum_j a_j\mu(E_j).$$

For nonnegative measurable $f$, define its integral as the supremum of those simple-function integrals with $0\le s\le f$. For signed $f$, write $f=f^+-f^-$; a finite Lebesgue integral requires $\int|f|<\infty$. One must not subtract two infinite integrals.

**Convergence theorems, cited without full proofs.** If $0\le f_n\uparrow f$ almost everywhere, monotone convergence gives $\int f_n\uparrow\int f$. Fatou gives $\int\liminf f_n\le\liminf\int f_n$ for nonnegative measurable functions. Dominated convergence gives $\int f_n\to\int f$ when $f_n\to f$ almost everywhere and $|f_n|\le g$ for one integrable $g$ independent of $n$.

For sigma-finite measure spaces, **Tonelli** allows iterated integration of nonnegative measurable $f$ even if the answer is infinite. **Fubini** permits exchanging iterated integrals for absolutely integrable signed or complex $f$. Without these hypotheses, an iterated answer may depend on order or fail to define an integral.

## Derivations and proofs

**Monotone bounded sequences converge.** Suppose $a_n$ is increasing and bounded above, and let $L=\sup\{a_n:n\ge1\}$. Given $\varepsilon>0$, $L-\varepsilon$ is not an upper bound, so some $a_N>L-\varepsilon$. For $n\ge N$, $L-\varepsilon<a_N\le a_n\le L$, proving convergence to $L$. The supremum property supplies the actual limit rather than only plausible closeness.

**Uniform continuity on a compact metric space.** If a continuous $f$ were not uniformly continuous, some $\varepsilon_0>0$ and sequences $x_n,y_n$ would satisfy $d(x_n,y_n)\to0$ but $|f(x_n)-f(y_n)|\ge\varepsilon_0$. Compactness gives a subsequence $x_{n_k}\to x$. The triangle inequality makes $y_{n_k}\to x$ as well, and continuity forces their image difference to zero, a contradiction. This proof uses the cited sequential characterization of compactness.

A function has **bounded variation** on $[a,b]$ if $\sup_P\sum_i|f(x_i)-f(x_{i-1})|<\infty$, the supremum over finite partitions. Monotone functions have bounded variation; a difference of two increasing functions characterizes real BV functions. The latter decomposition is a cited theorem. BV functions may have jumps, so their derivatives are naturally finite signed measures rather than merely ordinary functions. In distribution language, $\langle Df,\varphi\rangle=-\int f\varphi'$. For the Heaviside step $H(x)=0$ when $x<0$ and one when $x>0$,

$$\langle DH,\varphi\rangle=-\int_0^\infty\varphi'(x)dx=\varphi(0),$$

so $DH=\delta_0$. The value assigned to $H(0)$ does not change its associated distribution. This is a proof of the jump's distributional derivative, not a claim that $H$ has a classical derivative at zero.

## Worked examples

**1. Supremum without maximum.** Let $A=\{1-1/n:n=1,2,\ldots\}$. Every member is below one. Given $\varepsilon>0$, choose $n>1/\varepsilon$, giving $1-1/n>1-\varepsilon$. Hence any candidate upper bound below one fails, so $\sup A=1$. Since one is absent, there is no maximum. The infimum and minimum are both zero, attained at $n=1$.

**2. Pointwise versus uniform convergence.** On $[0,1]$, $x^n\to0$ for $x<1$ and stays one at $x=1$. The limit is discontinuous while every $f_n$ is continuous, already disproving uniform convergence. Directly, $\sup_{x\in[0,1)}x^n=1$, so the supremum error is one for every $n$. On $[0,a]$ for a fixed $0\le a<1$, the error is at most $a^n\to0$, so convergence there is uniform.

**3. Dominated integration.** Set $f_n(x)=x^n$ on $[0,1]$. Although convergence is not uniform, $|f_n|\le1$, an integrable bound, and the pointwise limit is zero almost everywhere. Dominated convergence gives integral limit zero. Exact integration gives $\int_0^1x^n dx=1/(n+1)$, confirming it. Now $g_n=n\mathbf1_{(0,1/n)}$ also tends to zero almost everywhere, but $\int g_n=1$; no common integrable dominator can exist, so applying the theorem would be invalid.

**4. Tonelli product.** For $a,b>0$, let $f(x,y)=e^{-ax-by}$ on $[0,\infty)^2$. Nonnegativity permits Tonelli. Separate the integrals to obtain $(1/a)(1/b)=1/(ab)$. The finite result also proves absolute integrability, justifying Fubini afterward. Positivity of both parameters is essential.

## Practice problems

1. Find $\inf(0,2)$ and say whether it is a minimum.
2. Is the metric space $(0,1)$ with ordinary distance complete? Give a sequence.
3. Compute the Lebesgue integral of the rational-number indicator on $[0,1]$, and compare Riemann integrability.
4. Find the distributional derivative of $|x|$ and its second derivative on $\mathbb R$.

## Answers and explanations

1. The infimum is zero, but it is not a minimum because zero is not in the open interval.
2. No. $x_n=1/(n+1)$ is Cauchy and converges in $\mathbb R$ to zero, which is absent from the space.
3. The rationals are countable and each singleton has measure zero, so their indicator is zero almost everywhere and its Lebesgue integral is zero. Every interval contains both rationals and irrationals; lower Riemann sums are zero and upper sums one, so it is not Riemann integrable.
4. The first derivative is $\operatorname{sgn}x$ distributionally, with no delta since $|x|$ has no jump. The sign function has a jump of size two at zero, so $D^2|x|=2\delta_0$. Integration by parts on the two half-lines verifies both statements.

## Common mistakes and misconceptions

Bounded does not mean convergent: $(-1)^n$ is bounded. Pointwise convergence gives a tolerance index depending on position; uniform convergence forbids that dependence. Almost everywhere equality does not mean equality at every point. A nonnegative function can have integral zero while being nonzero on a null set. A distributional delta is not manipulated by assigning it an ordinary value at its source.

## Connections to other mathematics

[PDE weak solutions](../differential-equations/partial-differential-equations.md) use distributional derivatives. [Harmonic analysis](../harmonic-analysis/transforms-and-special-functions.md) uses $L^2$ convergence instead of demanding pointwise convergence everywhere. Compactness and continuity also connect to topology in the [subject map](../../CONTENTS.md).

## Applications

A probability measure has total mass one, and expectation is a Lebesgue integral. Dominated convergence can justify taking limits through expected values when one common integrable bound exists. In mechanics, a concentrated load is represented by a measure or distribution; its integral gives finite total force even though no ordinary bounded force density represents the idealized point source.

## Optional computational examples

[plot_analysis.py](../../scripts/plot_analysis.py) draws pointwise convergence without joining the discontinuous limit. [verify_analysis.py](../../scripts/verify_analysis.py) checks exact power integrals and moving-spike integrals. Quantifier proofs and measure-theoretic hypotheses are reviewed mathematically, not certified by sampling.

## References and recommended reading

Sources and further study: Jiří Lebl, [Basic Analysis](https://www.jirka.org/ra/), real numbers, sequences, functions, integration, function sequences, and metric spaces; Terence Tao, [An Introduction to Measure Theory](https://terrytao.wordpress.com/books/an-introduction-to-measure-theory/), author page with open text and errata. The measure convergence and product-measure theorems are stated precisely; their full proofs are beyond this compact chapter.

## Revision and mastery status

Written 2026-10-18. Scope: rigorous introductory analysis and a working measure/distribution bridge covering the group 15 themes. Mastery requires writing an epsilon proof, distinguishing compactness from completeness, selecting a valid convergence theorem, and interpreting a weak derivative. Learner assessment remains unrecorded.
