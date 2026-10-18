# Functions, limits, continuity, and series

**Topic ID:** ANA-001  
**Classification:** Analysis → functions and convergence foundations  
**Level:** Precalculus through introductory analysis  
**Content status:** Written compact reference; deep existence theorems cited without proof.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Algebra and functions: preserve meaning through every transformation](../../lessons/foundations/algebra-and-functions.md)
<!-- guided-lessons:end -->

## Prerequisites

Use [algebra](../algebra/elementary-algebra.md),
[logical quantifiers](../foundations/logic-and-proof.md), and absolute value.
Diagnostic: $(x^2-1)/(x-1)=x+1$ for $x\ne1$, but the original quotient has
no value at $1$. A limit can describe nearby behavior without supplying a
missing function value.

## Definition

A function $f:D\to C$ has domain $D$, codomain $C$, and range
$f(D)=\{f(x):x\in D\}\subseteq C$. A real graph is
$\{(x,f(x)):x\in D\}\subseteq\mathbb R^2$. Composition $g\circ f$ requires
$f(x)$ to lie in the domain of $g$. A bijection has a two-sided inverse;
a noninjective function may have an inverse only after its domain is restricted.

A sequence $a_n$ converges to $L$ if, for every $\varepsilon>0$, there is an
integer $N$ such that $n\ge N$ implies $|a_n-L|<\varepsilon$.
The function limit $\lim_{x\to a}f(x)=L$ means that for every
$\varepsilon>0$ there is $\delta>0$ such that, for domain points,
$0<|x-a|<\delta$ implies $|f(x)-L|<\varepsilon$. The point $a$ must be
an accumulation point of the domain. Continuity at a domain point means the
same implication with $|f(x)-f(a)|<\varepsilon$, including $x=a$.

An infinite series $\sum_{n=0}^{\infty}a_n$ converges when its partial sums
$S_N=\sum_{n=0}^N a_n$ converge. A small term and a small tail sum are different
requirements. A power series is $\sum_{n=0}^{\infty}c_n(x-a)^n$.

## Intuitive explanation

A function is an input-output assignment; its graph is one representation.
A limit demands eventual closeness for every requested accuracy. The index
threshold may depend on the requested accuracy, but cannot depend on the
particular later index. This explains why a finite graph or table suggests a
limit yet cannot alone prove it.

For sequences of functions, pointwise convergence lets each input have its own
threshold. Uniform convergence requires one threshold that works over the whole
domain. Moving spikes or shrinking boundary layers can defeat uniform
convergence even when each fixed input behaves well.

## Mathematical notation

$\sup S$ and $\inf S$ are the least upper and greatest lower bounds.
A function is bounded on $D$ if $|f(x)|\le M$ there for some finite $M$.
$f(x)=O(g(x))$ near a specified limiting point means
$|f(x)|\le C|g(x)|$ eventually for some constant $C$;
$f(x)=o(g(x))$ means $f(x)/g(x)\to0$, where $g$ is eventually nonzero.
The limiting regime, such as $x\to0$ or $n\to\infty$, must be stated.
$\|h\|_\infty=\sup_{x\in D}|h(x)|$ when finite.

## Fundamental properties

Increasing means $x<y$ implies $f(x)\le f(y)$; strictly increasing uses a
strict conclusion. An even function obeys $f(-x)=f(x)$, an odd function
$f(-x)=-f(x)$, on a domain symmetric about zero. A period $T>0$ requires an invariant domain $D+T=D$ and
$f(x+T)=f(x)$ for every $x\in D$; checking only an empty overlap would not define periodicity.

Elementary real families include polynomials (all real inputs), rational
functions (denominator nonzero), $\sqrt x$ ($x\ge0$), $|x|$ (all real inputs),
$b^x$ ($b>0$), $\log_bx$ ($x>0,b>0,b\ne1$), and the trigonometric functions
on their domains. The transformed graph $y=A f(B(x-h))+k$, $B\ne0$,
shifts the original horizontally by $h$ and vertically by $k$, scales vertical
values by $A$ and horizontal distances by $1/|B|$, and reflects when the
corresponding multiplier is negative. A vertical asymptote describes unbounded
limiting behavior, not merely an excluded point.

Limits respect sums and products, and quotients when the denominator limit is
nonzero. The squeeze theorem says that $g\le f\le h$ near the point and equal
outer limits $L$ imply the same limit for $f$. A monotone bounded real sequence
converges; this uses completeness of $\mathbb R$.

**Intermediate value theorem, cited without proof.** A continuous
$f:[a,b]\to\mathbb R$ takes every value between $f(a)$ and $f(b)$.
**Extreme value theorem, cited without proof.** Such an $f$ attains both its
maximum and minimum. Closedness, boundedness of the interval, and continuity
matter: $f(x)=x$ on $(0,1)$ has neither extreme, and $1/x$ on $(0,1]$ is unbounded.

## Important formulas and identities

For $|r|<1$,

$$\sum_{n=0}^{\infty}r^n=\frac1{1-r},\qquad
\left|\frac1{1-r}-\sum_{n=0}^N r^n\right|
=\frac{|r|^{N+1}}{|1-r|}.$$

Convergence tools, each with its own hypotheses, include:

- If $\sum a_n$ converges, then $a_n\to0$; the converse is false.
- For $0\le a_n\le b_n$ eventually, convergence of $\sum b_n$ implies convergence of $\sum a_n$. Divergence of the smaller series forces divergence of the larger.
- The $p$-series $\sum_{n=1}^{\infty}1/n^p$ converges exactly when $p>1$.
- If $L=\lim|a_{n+1}/a_n|<1$ (eventually nonzero terms), the ratio test gives absolute convergence; $L>1$ gives divergence. At $L=1$ it decides nothing.
- The root test uses $L=\limsup |a_n|^{1/n}$ with the same strict alternatives.
- If $b_n\ge0$ decreases to zero, $\sum(-1)^n b_n$ converges and the error after a partial sum is bounded by the first omitted $b_n$.
- For a positive decreasing continuous $f$ on $[1,\infty)$, $\sum f(n)$ and $\int_1^\infty f(x)\,dx$ converge or diverge together.

These tests are cited here with geometric and alternating arguments illustrated
below; their full general proofs belong to real analysis. Absolute convergence
implies convergence over $\mathbb R$ and $\mathbb C$.

A power series has a radius $R\in[0,\infty]$: absolute convergence for
$|x-a|<R$ and divergence for $|x-a|>R$; endpoints require separate checks.
Inside the radius it may be differentiated and integrated term by term.

## Derivations and proofs

**Epsilon proof of a sequence limit.** For $a_n=(3n+1)/(n+2)$,
$|a_n-3|=5/(n+2)$. Given $\varepsilon>0$, choose an integer
$N>5/\varepsilon$. For $n\ge N$, the error is less than
$5/N<\varepsilon$. Thus $a_n\to3$. The proof supplies a threshold for every
accuracy, rather than extrapolating a table.

**Geometric convergence.** Finite summation gives
$(1-r)\sum_{n=0}^Nr^n=1-r^{N+1}$. If $|r|<1$, then $r^{N+1}\to0$,
so division by $1-r\ne0$ gives the infinite sum and exact remainder above.
At $r=1$ partial sums grow, and at $r=-1$ they oscillate; neither endpoint
inherits convergence.

**Uniform limit preserves continuity.** Suppose continuous $f_n:D\to\mathbb R$
converge uniformly to $f$. At a chosen $a\in D$ and accuracy $\varepsilon$,
select $n$ with $|f-f_n|<\varepsilon/3$ everywhere. Continuity of this fixed
$f_n$ gives $|f_n(x)-f_n(a)|<\varepsilon/3$ for $x$ close to $a$. Then
the triangle inequality bounds $|f(x)-f(a)|$ by three terms, each less than
$\varepsilon/3$. Hence $f$ is continuous.

Uniform convergence also permits exchange with a finite-interval integral for
Riemann-integrable $f_n$, because the integral error is at most
$(b-a)\|f_n-f\|_\infty$. Differentiation requires more: for continuously
differentiable $f_n$ on $[a,b]$, uniform convergence of $f_n'$ and convergence
of $f_n$ at one point imply convergence to a differentiable limit with the
expected derivative. Uniform convergence of $f_n$ alone is insufficient.

## Worked examples

**1. Domain and inverse.** Let $f(x)=\sqrt{x-2}$. Its real domain is
$[2,\infty)$ and range $[0,\infty)$. It is strictly increasing, so treating
the range as codomain gives an inverse. Solve $y=\sqrt{x-2}$ for $x$ to get
$f^{-1}(y)=y^2+2$, $y\ge0$. Both compositions give the appropriate identity;
extending the inverse formula to negative inputs would no longer invert $f$.

**2. A removable discontinuity.** For $x\ne2$,
$(x^2-4)/(x-2)=x+2$, so the limit at $2$ is $4$.
Defining the missing value to be $4$ makes the extension continuous.
Defining it as $9$ leaves a discontinuity despite the same nearby limit.

**3. Exact infinite sum.** Evaluate $\sum_{n=1}^{\infty}3/4^n$.
The first term is $3/4$ and ratio $1/4$, giving $(3/4)/(1-1/4)=1$.
After $N$ terms the sum is $1-4^{-N}$ and the error is exactly $4^{-N}$.
To make it less than $1/1000$, $N=5$ works since $4^5=1024>1000$.

**4. A power-series endpoint test.** For $\sum_{n=1}^{\infty}x^n/n$,
the ratio test gives convergence for $|x|<1$ and divergence for $|x|>1$.
At $x=1$ the harmonic series diverges; at $x=-1$ the alternating harmonic
series converges. Thus the real convergence interval is $[-1,1)$.
Endpoint convergence cannot be read from the radius alone.

**5. Pointwise versus uniform convergence.** On $[0,1]$, $f_n(x)=x^n$
tends to $0$ for $x<1$ and equals $1$ at $x=1$. The limit is discontinuous,
so the continuous functions cannot converge uniformly. More explicitly,
$\sup_{0\le x<1}x^n=1$ for every $n$. On $[0,q]$ with fixed $0<q<1$,
the uniform error is $q^n\to0$, so the restricted convergence is uniform.

![Powers x to n on the unit interval and geometric partial sums compared with one over one minus x on a restricted interval.](../../assets/figures/foundations/convergence.png)

The left panel displays a boundary layer near $1$; the right panel deliberately
uses $|x|\le3/4$, where the geometric tails have a uniform bound.

## Practice problems

1. **ANA-01:** Find the domain of $\ln(4-x^2)$ and state whether the function is even.
2. **ANA-02:** Prove $1/n\to0$ directly from the definition.
3. **ANA-03:** Determine convergence of $\sum 1/n^2$ and $\sum n/(n+1)$.
4. **ANA-04:** Show $x^2=o(x)$ as $x\to0$, but not as $x\to\infty$.
5. **ANA-05:** Prove geometric series converge uniformly on $[-q,q]$ for any fixed $0<q<1$.

## Answers and explanations

1. A real logarithm needs $4-x^2>0$, giving $(-2,2)$. Replacing $x$ by
$-x$ changes nothing, so it is even on this symmetric domain.
2. Given $\varepsilon>0$, choose an integer $N>1/\varepsilon$. Then for
$n\ge N$, $|1/n|\le1/N<\varepsilon$.
3. The first converges by the $p$-series test with $p=2$. The second
diverges because its terms approach $1$, violating the necessary zero-term test.
4. For $x\ne0$, $x^2/x=x$. This tends to $0$ at zero and is unbounded
as $x\to\infty$; the regime determines the statement.
5. For $|x|\le q$, the geometric remainder is at most
$q^{N+1}/(1-q)$, independent of $x$, and this bound tends to zero.

## Common mistakes and misconceptions

A function limit does not require a value at the limiting point. Boundedness
does not imply convergence: $(-1)^n$ is bounded. Terms tending to zero do not
guarantee a finite sum: the harmonic series is the standard counterexample.
The ratio test at $L=1$ is inconclusive, rather than a divergence test.
Moving a limit through a derivative or integral needs a stated theorem.

## Connections to other mathematics

The quantifiers are developed in [logic and proof](../foundations/logic-and-proof.md).
[Trigonometry](../trigonometry/trigonometry.md) supplies periodic examples.
Differential calculus, real analysis, and Fourier analysis build on these
convergence distinctions; their deeper topics are in the book's subject map.

## Applications

A repeated correction leaves one quarter of the previous displacement error.
If the initial error is $4\ \mathrm{mm}$, after $n$ corrections its magnitude
is $4(1/4)^n\ \mathrm{mm}$. This sequence converges to zero under the assumed
constant contraction factor. The exact threshold for a desired tolerance can
be computed as in the geometric example; physical noise may impose a separate
error floor absent from this ideal model.

## Optional computational examples

[plot_foundations.py](../../scripts/plot_foundations.py) regenerates the
convergence figure in PNG and SVG. Finite curves illustrate the behavior;
the supremum bound and epsilon argument establish the claims.

## References and recommended reading

Jiří Lebl, [*Basic Analysis*, author page and open editions](https://www.jirka.org/ra/), provides further study of sequences, series, continuity, and uniform convergence; its section “Pointwise and uniform convergence” is the reference route for the exchange-of-limit results. Richard Hammack, [*Book of Proof*, “Proofs in Calculus”](https://richardhammack.github.io/BookOfProof/), provides additional epsilon-proof practice. The present proofs and examples are original concise treatments, not substitutes for the full real-analysis development.

## Revision and mastery status

Written 2026-10-18; learner mastery unassessed. Explain every quantifier in a
limit and justify a series test, including its endpoint limitations. General
metric-space convergence, measure-theoretic limit theorems, and full proofs of
all convergence tests require the later analysis chapters.
