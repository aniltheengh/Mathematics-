# Elementary and intermediate algebra

**Topic ID:** ALG-001  
**Classification:** Algebra → expressions, equations, inequalities, and sequences  
**Level:** Elementary to precalculus  
**Content status:** Written compact reference.  
**Learner mastery:** Unassessed.

## Prerequisites

Use [signed arithmetic, fractions, radicals, and number systems](../numbers/arithmetic-and-number-systems.md).
Diagnostic: $2(x+3)=2x+6$, and $(x+3)^2=x^2+6x+9$. Distribution applies to
each term; squaring a sum includes its cross term. Unless stated otherwise,
unknowns and coefficients in this chapter are real numbers.

## Definition

An **expression** denotes a value once its variables are assigned. An
**identity** holds for every assignment in its stated domain; an **equation**
asks which assignments make two expressions equal. An equation's solution set
may be empty, finite, or infinite. Equivalent equations have the same solution
set. A one-way implication during calculation may introduce candidates that
must later be checked.

A polynomial is a finite sum $p(x)=a_nx^n+\cdots+a_1x+a_0$, with nonnegative
integer exponents; if $a_n\ne0$, its degree is $n$. A rational expression is a
quotient of polynomials, defined where its denominator is nonzero. Canceling
a common factor simplifies values on the original domain but does not restore
excluded points.

A sequence $(a_n)$ assigns a number to each index. An arithmetic progression
has constant difference $d$; a geometric progression has constant multiplier
$r$. A recurrence specifies later terms from earlier ones and needs initial
values to select a particular sequence.

## Intuitive explanation

Solving an equation means preserving or carefully tracking the allowed values.
Adding the same expression to both sides is reversible. Multiplying by a
nonzero expression is reversible on its nonzero domain. Squaring loses sign
information, and multiplication by an expression that can vanish may lose or
gain cases. Domain bookkeeping is part of the solution, not a final cosmetic
check.

Factoring changes a sum into a product so the zero-product property can expose
roots. Completing the square changes a quadratic into a translated square so
its vertex, minimum, and roots can be read from one form.

## Mathematical notation

$\Delta=b^2-4ac$ denotes the quadratic discriminant; $\log_b x$ is the real
logarithm with $b>0,b\ne1,x>0$. The natural logarithm is $\ln x=\log_e x$.
$\sum_{k=1}^n a_k$ means a finite sum. $n!$ is the product from $1$ to $n$,
with $0!=1$. The binomial coefficient is
$\binom nk=n!/[k!(n-k)!]$ for integers $0\le k\le n$.

## Fundamental properties

Polynomial addition combines equal powers, and multiplication distributes.
Polynomial division by nonzero $d(x)$ gives unique $q,r$ with
$p=dq+r$ and $\deg r<\deg d$ (or $r=0$). In particular division by $x-c$
leaves remainder $p(c)$, so $p(c)=0$ exactly when $x-c$ is a factor.

A two-equation system
$ax+by=e$, $cx+dy=f$ has a unique solution when
$ad-bc\ne0$. When the determinant is zero, equations may be inconsistent or
dependent; substitution distinguishes these cases. For example $x+y=1$ and
$2x+2y=3$ have no common solution, while replacing $3$ by $2$ gives a whole line.

For a quadratic $ax^2+bx+c=0$ with $a\ne0$, the sign of $\Delta$ determines
two distinct real roots, one repeated real root, or no real roots. In the last
case complex roots exist and are conjugates. For real $u,v$ and $c>0$,
$u<v\Leftrightarrow cu<cv$; for $c<0$, the inequality reverses.

Real exponentials $b^x$ are one-to-one for $b>0,b\ne1$, increasing if $b>1$
and decreasing if $0<b<1$. Their inverse logarithms have the same monotonicity.
These facts justify applying a logarithm to an equality of positive quantities.

## Important formulas and identities

Common exact factorizations are

$$a^2-b^2=(a-b)(a+b),\quad
a^3-b^3=(a-b)(a^2+ab+b^2),$$
$$a^3+b^3=(a+b)(a^2-ab+b^2),\qquad
(a+b)^n=\sum_{k=0}^n\binom nk a^{n-k}b^k.$$

The binomial theorem is for nonnegative integer $n$ here. General noninteger
binomial expansions are infinite series with convergence conditions.

For $a\ne0$,

$$ax^2+bx+c=a\left(x+\frac b{2a}\right)^2-\frac{\Delta}{4a},\qquad
x=\frac{-b\pm\sqrt\Delta}{2a}.$$

For positive $u,v$ and admissible logarithm base,

$$\log_b(uv)=\log_bu+\log_bv,\quad
\log_b(u^t)=t\log_bu,\quad
\log_bu=\frac{\ln u}{\ln b}.$$

Arithmetic and geometric finite sums, with $n\ge1$, are

$$a_n=a_1+(n-1)d,\quad S_n=\frac n2[2a_1+(n-1)d],$$
$$a_n=a_1r^{n-1},\quad S_n=a_1\frac{1-r^n}{1-r}\quad(r\ne1).$$

When $r=1$, $S_n=na_1$. Useful inequalities include
$|u+v|\le|u|+|v|$ and $(u+v)^2\le2(u^2+v^2)$ for real $u,v$.
For $u,v\ge0$, $\sqrt{uv}\le(u+v)/2$, with equality exactly when $u=v$.

## Derivations and proofs

**Quadratic formula.** Divide by $a\ne0$, move $c/a$, and add
$(b/(2a))^2$ to both sides. This gives
$(x+b/(2a))^2=\Delta/(4a^2)$. Taking both square-root signs and simplifying
the unordered pair yields $x=(-b\pm\sqrt\Delta)/(2a)$. For $\Delta<0$,
there is no real square root; in $\mathbb C$ write
$\sqrt\Delta=i\sqrt{-\Delta}$.

**Geometric sum.** Put $S=a_1+a_1r+\cdots+a_1r^{n-1}$. Subtract $rS$
from $S$ to cancel the middle terms, yielding
$(1-r)S=a_1(1-r^n)$. Divide only when $r\ne1$; handle $r=1$ directly.

**Arithmetic–geometric mean inequality for two numbers.** Since
$(\sqrt u-\sqrt v)^2\ge0$, expansion gives
$u+v\ge2\sqrt{uv}$. Equality requires $\sqrt u=\sqrt v$, hence $u=v$.
Nonnegativity is essential to this real square-root proof.

## Worked examples

**1. A rational equation with an excluded value.** Solve
$\frac{x^2-1}{x-1}=3$. First impose $x\ne1$. Factor the numerator and cancel
to obtain $x+1=3$, hence $x=2$. Substitution in the original gives $3$.
The reduced formula $x+1$ is defined at $1$, but the original expression is not.

**2. A radical equation and an extraneous root.** Solve
$\sqrt{x+2}=x$. The left side is nonnegative, so $x\ge0$.
Squaring gives $x+2=x^2$, or $(x-2)(x+1)=0$. Candidates are $2,-1$.
Only $2$ satisfies the domain and original equation: $\sqrt4=2$.
For $-1$, the original sides are $1$ and $-1$.

**3. A quadratic inequality.** Solve $2x^2-5x-3\le0$.
Factor $(2x+1)(x-3)$. Roots are $-1/2$ and $3$. Test intervals: both factors
are negative to the left, their signs differ between roots, and both are
positive to the right. The solution is $[-1/2,3]$, including both zero values.

**4. A logarithmic equation.** Solve $\log_2(x-1)+\log_2(x+1)=3$.
The domain is $x>1$. Combine logarithms to get $\log_2(x^2-1)=3$, so
$x^2-1=8$ and $x=\pm3$. The domain selects $x=3$.
Check $\log_22+\log_24=1+2=3$.

**5. A simultaneous system.** Solve $2x+y=7$, $x-y=2$.
Add equations to obtain $3x=9$, so $x=3$ and then $y=1$.
Substitution verifies both equations; the nonzero determinant $-3$ guarantees
that another solution cannot exist.

## Practice problems

1. **ALG-01:** Factor $x^3-4x$ and find all real zeros.
2. **ALG-02:** Solve $|3x-2|>4$.
3. **ALG-03:** Find the exact minimum of $2x^2-8x+11$.
4. **ALG-04:** Find $\sum_{k=1}^{20}(3k-1)$ and $\sum_{k=0}^{5}2^k$.
5. **ALG-05:** Solve $9^x=27^{x-1}$ exactly and check by substitution.
6. **ALG-06:** Find the coefficient of $x^3$ in $(2+x)^5$.

## Answers and explanations

1. Factor $x(x^2-4)=x(x-2)(x+2)$. A product of real numbers is zero exactly
when a factor is zero, giving $-2,0,2$.
2. $3x-2>4$ or $3x-2<-4$, hence $x>2$ or $x<-2/3$. Strict inequalities
exclude the boundary values.
3. Complete the square: $2(x-2)^2+3$. A square is nonnegative, so the minimum
is $3$, attained at $x=2$.
4. First and last arithmetic terms are $2$ and $59$, so the sum is
$20(2+59)/2=610$. The geometric sum is $(2^6-1)/(2-1)=63$.
5. Rewrite in base $3$: $3^{2x}=3^{3x-3}$. Injectivity gives $x=3$;
both original sides are $729$.
6. Choose three $x$ factors and two $2$ factors. The coefficient is
$\binom53 2^2=40$. This counts the ten distinct selections rather than
assuming a single product term.

## Common mistakes and misconceptions

$\log(u+v)$ is generally not $\log u+\log v$. Dividing by $x$ may discard
$x=0$; split into cases first. Cross multiplication requires both original
denominators nonzero. An identity after cancellation does not supply values
at a hole. For inequalities involving a variable denominator, use a sign chart
or split its positive and negative cases before multiplying.

## Connections to other mathematics

[Functions and limits](../analysis/functions-limits-and-series.md) interpret
rational holes and asymptotes. [Trigonometry](../trigonometry/trigonometry.md)
adds periodic equations. Polynomial rings receive a structural treatment in
[abstract algebra](../abstract-algebra/abstract-algebra.md).

## Applications

For a uniform rectangular plate of fixed perimeter $4\ \mathrm m$, side lengths
$x$ and $2-x$ metres give area $A=x(2-x)=1-(x-1)^2$ square metres, with
$0<x<2$. Its maximum is exactly $1\ \mathrm{m^2}$ at $x=1\ \mathrm m$.
The algebra includes the physical domain; a negative “side” is not admissible.

## Optional computational examples

Symbolic expansion can check a proposed identity by reducing the difference
to zero. A numerical root solver supplies candidates and tolerances, not a proof
that all roots have been found. All answers above can be checked exactly by hand.

## References and recommended reading

OpenStax, [*Precalculus 2e*, “Exponential and Logarithmic Functions”](https://openstax.org/books/precalculus-2e/pages/4-key-concepts), and [“Sequences, Probability, and Counting Theory”](https://openstax.org/books/precalculus-2e/pages/11-key-concepts), are verified reference routes for further examples. Richard Hammack, [*Book of Proof*, “Counting”](https://richardhammack.github.io/BookOfProof/), supplies a proof-oriented route to the binomial theorem. Full general polynomial solvability belongs to advanced algebra.

## Revision and mastery status

Written 2026-10-18; learner mastery unassessed. A satisfactory self-check includes
one excluded-denominator example, one extraneous-root example, and a finite-sum
derivation. General high-degree equations and systematic inequality theory
receive only their foundational tools here.
