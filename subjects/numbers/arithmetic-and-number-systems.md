# Arithmetic and number systems

**Topic ID:** NUM-001  
**Classification:** Numbers → arithmetic, representation, and measurement  
**Level:** Elementary foundations to introductory complex arithmetic  
**Content status:** Written compact reference.  
**Learner mastery:** Unassessed.

## Prerequisites

Read a number line and multiply whole numbers. Diagnostic: $3+4\times2=11$,
while $(3+4)\times2=14$. Parentheses determine the intended grouping; multiplication
precedes addition in an unparenthesized expression.

## Definition

The natural numbers are $\mathbb N=\{0,1,2,\ldots\}$; integers
$\mathbb Z$ also include negative whole numbers. Rational numbers are fractions
$a/b$ with $a,b\in\mathbb Z$ and $b\ne0$, identifying fractions with the same
value. The real numbers $\mathbb R$ include the rationals and irrational limits
such as $\sqrt2$; they form a complete ordered field. Complex numbers are
$z=a+bi$, with $a,b\in\mathbb R$ and $i^2=-1$. Thus
$\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q\subseteq\mathbb R\subseteq\mathbb C$.

In base ten the digit $d_k$ in position $k$ contributes $d_k10^k$. For example
$304.07=3\cdot10^2+4\cdot10^0+7\cdot10^{-2}$. In any integer base
$b\ge2$, allowed digits are $0,\ldots,b-1$, and positions contribute powers of $b$.
The numeral is a representation; its value does not depend on the chosen base.

A ratio compares two quantities by division; a proportion asserts equality of
ratios. A percentage $p\%$ means $p/100$. A unit expresses the scale of a measured
quantity. A dimension describes its physical kind, such as length $L$, time $T$,
or mass $M$.

## Intuitive explanation

The number systems successively allow operations that would otherwise fail:
integers allow unrestricted subtraction, rationals allow division by nonzero
integers, reals provide limits of convergent rational approximations, and complex
numbers allow roots of every nonconstant polynomial. The last statement is the
fundamental theorem of algebra, cited here without proof. Larger systems do not
remove the restriction on division by zero.

Exact arithmetic preserves a mathematical value, while measurement arithmetic
tracks uncertainty. Writing a length as $2.000\ \mathrm m$ communicates a
measurement resolution that the exact integer $2$ alone does not specify.

## Mathematical notation

$|x|$ is absolute value for real $x$; for complex $z=a+bi$,
$|z|=\sqrt{a^2+b^2}$. The conjugate is $\overline z=a-bi$.
$a\mid b$ means $b=ak$ for some integer $k$. We choose
$\gcd(a,b)\ge0$ and $\operatorname{lcm}(a,b)\ge0$. Interval brackets include
an endpoint, parentheses exclude it: $[a,b)=\{x:a\le x<b\}$.
$\approx$ marks an approximation, while $=$ means exact equality.

## Fundamental properties

Addition and multiplication are associative and commutative on $\mathbb R$ and
$\mathbb C$; multiplication distributes over addition. Subtraction and division
are generally neither associative nor commutative. Compute operations of equal
priority from left to right: $12/3\times2=8$. Powers precede an unparenthesized
minus: $-3^2=-9$, whereas $(-3)^2=9$.

A positive integer $p>1$ is prime if its positive divisors are only $1,p$.
Every integer $n>1$ factors uniquely as a product of primes up to order
(fundamental theorem of arithmetic, cited without its full uniqueness proof).
If $a=\prod p^{\alpha_p}$ and $b=\prod p^{\beta_p}$ are positive,
the gcd uses $\min(\alpha_p,\beta_p)$ and the lcm uses the maximum.

An inequality may be multiplied by a positive number without reversal; a
negative multiplier reverses it. Absolute value is a distance from zero:
$|x|\ge0$, $|xy|=|x||y|$, and $|x+y|\le|x|+|y|$.
There is no order on $\mathbb C$ compatible with the ordered-field rules:
if there were, the square $i^2=-1$ would have to be nonnegative.

## Important formulas and identities

For $b,d\ne0$,

$$\frac ab+\frac cd=\frac{ad+bc}{bd},\quad
\frac ab\frac cd=\frac{ac}{bd},\quad
\frac{a/b}{c/d}=\frac{ad}{bc}\quad(c\ne0).$$

With positive real $a,b$ and real exponents,

$$a^ma^n=a^{m+n},\quad (a^m)^n=a^{mn},\quad (ab)^m=a^mb^m.$$

Integer exponent rules extend to nonzero negative bases when defined; general
real-exponent rules require positive bases. For $a\ne0$, $a^0=1$ and
$a^{-n}=1/a^n$. The real principal square root is nonnegative, so
$\sqrt{x^2}=|x|$. For nonnegative $a,b$, $\sqrt{ab}=\sqrt a\sqrt b$.
There is no general rule $\sqrt{a+b}=\sqrt a+\sqrt b$.

Scientific notation is $c\times10^k$ with $1\le|c|<10$ for nonzero values.
A measured result $q$ with true value $q_*$ has absolute error
$|q-q_*|$ and relative error $|q-q_*|/|q_*|$ when $q_*\ne0$.
For rounding to the nearest step $h$, the absolute rounding error is at most
$h/2$; a specified tie-breaking rule handles exact halfway cases.

## Derivations and proofs

**Why common denominators work.** Multiplying numerator and denominator by
the same nonzero number changes no value, because $d/d=1$. Therefore
$a/b=ad/(bd)$ and $c/d=bc/(bd)$; adding equal-sized fractional parts gives
$(ad+bc)/(bd)$. A zero denominator has no such interpretation.

**Why $\sqrt2$ is irrational.** Suppose $\sqrt2=a/b$ in lowest terms, with
positive integers $a,b$. Squaring gives $a^2=2b^2$. An odd integer has an odd
square, so $a$ is even: $a=2k$. Substitution gives $b^2=2k^2$, hence $b$ is
also even. That contradicts lowest terms. Thus $\sqrt2\notin\mathbb Q$.

**Error propagation for a product.** If $q=xy$, $\tilde x=x+\delta x$, and
$\tilde y=y+\delta y$, then exactly

$$\tilde x\tilde y-xy=y\delta x+x\delta y+\delta x\delta y.$$

Consequently the absolute error is at most
$|y||\delta x|+|x||\delta y|+|\delta x\delta y|$. Dropping the last term is a
first-order approximation, justified only when the input errors are small.

## Worked examples

**1. Fraction, ratio, and percentage.** A tank holds $240\ \mathrm L$ and is
$3/8$ full. Multiply to obtain $90\ \mathrm L$. This is
$100(3/8)\%=37.5\%$ of capacity. Adding $30\ \mathrm L$ gives
$120/240=1/2=50\%$. The increase is $12.5$ percentage points and
$(30/90)100\%=100/3\%$ relative to the original volume; these describe different
comparisons.

**2. Gcd and lcm.** For $84=2^2\cdot3\cdot7$ and
$126=2\cdot3^2\cdot7$, take minimum prime exponents to get
$\gcd(84,126)=42$ and maximum exponents to get
$\operatorname{lcm}(84,126)=252$. Check $42\cdot252=84\cdot126=10584$.
The fraction $84/126$ reduces to $2/3$ by division by $42$.

**3. Complex division.** Compute $(3+2i)/(1-i)$. Multiply numerator and
denominator by $1+i$: the numerator is $1+5i$, and the denominator is $2$.
Thus the result is $1/2+(5/2)i$. Multiplying this result by $1-i$ recovers
$3+2i$, independently checking the division.

**4. Units and scale.** A drawing at scale $1:50$ shows $36\ \mathrm{mm}$.
Actual length is $50\cdot36=1800\ \mathrm{mm}=1.8\ \mathrm m$.
An actual square area scales by $50^2$, not by $50$. If the drawn length is
rounded to the nearest $1\ \mathrm{mm}$, actual rounding uncertainty is at
most $25\ \mathrm{mm}$, before other drawing or manufacturing errors.

## Practice problems

1. **NUM-01:** Evaluate $-2^4+3(5-1)$ and $\frac56-\frac7{15}$ exactly.
2. **NUM-02:** Solve $|2x-3|\le5$ and express the answer as an interval.
3. **NUM-03:** Simplify $\sqrt{72}$ and rationalize $3/\sqrt6$.
4. **NUM-04:** A $2.40\ \mathrm m$ length has a possible error of $0.01\ \mathrm m$. State the relative error bound and convert the data to millimetres.
5. **NUM-05:** Convert binary $1011.01_2$ to a rational decimal value; explain why $1/10$ has no terminating binary expansion.

## Answers and explanations

1. Power first gives $-16+12=-4$. A common denominator $30$ gives
$25/30-14/30=11/30$.
2. Since $|u|\le5$ means $-5\le u\le5$, get
$-2\le2x\le8$ and therefore $x\in[-1,4]$.
3. $72=36\cdot2$ gives $6\sqrt2$. Multiplying the second expression by
$\sqrt6/\sqrt6$ gives $\sqrt6/2$; its square is $3/2$, matching $9/6$.
4. Relative to the reported nominal length, $0.01/2.40=1/240$, or
$5/12\%$. The same data are $2400\pm10\ \mathrm{mm}$. If a bound relative to
the unknown true length is required, use its minimum $2.39\ \mathrm m$,
giving $1/239$. The reference value must be stated.
5. $8+2+1+1/4=45/4=11.25$. A terminating base-two fraction has reduced
denominator a power of $2$, whereas $1/10$ retains a factor $5$.

## Common mistakes and misconceptions

Adding numerators and denominators separately is invalid: $1/2+1/3=5/6$, not
$2/5$. Percentage change depends on the reference quantity. Negative exponents
mean reciprocals, not negative values. Significant figures are a reporting
convention, not an uncertainty model: carry guard digits during calculation and
round the final value to a resolution supported by the data. Exact counts and
defined unit conversions do not introduce measurement uncertainty.

## Connections to other mathematics

[Elementary algebra](../algebra/elementary-algebra.md) extends arithmetic laws to
unknown quantities. [Number theory](../number-theory/number-theory.md) develops
prime factorization and congruences. [Analysis](../analysis/functions-limits-and-series.md)
explains limits and real completeness; [abstract algebra](../abstract-algebra/abstract-algebra.md)
abstracts the field operations.

## Applications

Dimensional consistency is a necessary check on a physical formula. If speed
$v=L/T$ and time $t=T$, then $vt$ has dimension $L$, while $v+t$ is not a valid
sum. With $v=3\ \mathrm{m/s}$ and $t=8\ \mathrm s$, distance at constant speed
is $24\ \mathrm m$. Matching dimensions alone does not prove the assumed
constant-speed model describes the motion.

## Optional computational examples

Binary floating-point stores finitely many representable numbers, so a decimal
fraction may be approximated. Exact rational arithmetic would store $1/10$ as
an integer numerator and denominator. The symbolic explanations in this chapter
require no software; numerical representation is a property of the chosen
arithmetic, not of the real number itself.

## References and recommended reading

OpenStax, [*Precalculus 2e*, “Complex Numbers” and the supporting algebra review](https://openstax.org/books/precalculus-2e/pages/3-1-complex-numbers), provides practice with real and complex arithmetic. Richard Hammack, [*Book of Proof*, “Sets That Are Number Systems”](https://richardhammack.github.io/BookOfProof/), is further reading on the logical distinction between number systems. These links identify reference routes; the computations and measurement examples above are original.

## Revision and mastery status

Written 2026-10-18; learner mastery unassessed. Demonstrate mastery by preserving
exact fractions, checking domains, propagating units, and separating rounding
from measurement error. Constructing the reals from Cauchy sequences or Dedekind
cuts is beyond this compact chapter.
