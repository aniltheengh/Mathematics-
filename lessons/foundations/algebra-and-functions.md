# Algebra and functions: preserve meaning through every transformation

**Lesson ID:** LES-FND-02  
**Level:** Algebra through precalculus.  
**Lesson status:** Written guided lesson with exact results and reproducible diagrams.  
**Learner mastery:** Unassessed.

## Prerequisites

Use [fractions and radicals](../../subjects/numbers/arithmetic-and-number-systems.md),
[elementary algebra](../../subjects/algebra/elementary-algebra.md), and the
meaning of a real function's domain. All variables in this lesson are real
unless stated otherwise. A square root means the nonnegative principal root.
A real logarithm requires a positive argument, and its base satisfies $b>0$,
$b\ne1$. We keep exact radicals until an approximation is explicitly requested.

Diagnostic: $(x-2)^2=x^2-4x+4$, but $\sqrt{(x-2)^2}=|x-2|$.
The absolute value is essential when $x<2$. If you can expand the first expression
and check the second at $x=0$, you have the arithmetic needed to begin.

## Learning objectives

You will track domains before simplifying, derive and use completed-square
form, solve inequalities while respecting signs and endpoints, compose
functions in the correct order, construct an inverse by choosing a branch,
and solve a logarithmic equation without accepting a false root. The broader
goal is to recognize which transformations preserve equivalence and which
only produce candidates.

Keep a small “allowed inputs” line beside each calculation. Update it whenever
you encounter a denominator, square root, logarithm, or restricted inverse.
This habit makes many apparently mysterious algebra errors visible at the
moment they occur.

## Stage 1: a formula has a domain before it has a graph

A function is more than a formula. Its declared domain tells us which inputs
are allowed, and its codomain tells us what outputs are being considered.
The range is the set of outputs actually reached. Two equal-looking formulas
can describe different functions if their domains differ.

**Worked example 1: simplify without filling a hole.** Consider

$$f(x)=\frac{x^2-4}{x-2}.$$

The denominator requires $x\ne2$. Factor $x^2-4=(x-2)(x+2)$ and cancel
on that domain, obtaining $f(x)=x+2$ for $x\ne2$.
The graph follows a line except for the missing point $(2,4)$. The continuous
function $g(x)=x+2$ on all $\mathbb R$ is an extension of $f$, rather than
the very same function with the same domain. Substituting $x=2$ into the
original expression still gives division by zero.

Now solve $f(x)=4$. The reduced equation gives $x=2$, but this value is
excluded, so the original equation has no solution. This is a particularly
useful example because the familiar straight-line simplification produces
a candidate exactly where the original formula is unavailable.

For a square root such as $\sqrt{5-2x}$, require $5-2x\ge0$, giving
$x\le5/2$. For $\ln(5-2x)$, require the stricter $5-2x>0$, giving $x<5/2$.
The difference at one endpoint changes both the domain and possible solutions.

**Checkpoint.** What is the domain of $1/\sqrt{5-2x}$? The root must be real
and also nonzero, so $x<5/2$. Apply all restrictions together, not only the
first one noticed.

## Stage 2: complete the square and expose a quadratic's structure

Factored form reveals roots, expanded form reveals coefficients, and completed
square form reveals a vertex and an extremum. These are representations of
the same polynomial, useful for different questions.

For $a\ne0$, factor $a$ out of the quadratic and linear terms:

$$ax^2+bx+c=a\left(x^2+\frac ba x\right)+c.$$

The coefficient needed inside a square is $b/(2a)$, because
$(x+h)^2=x^2+2hx+h^2$. Add and subtract its square inside the brackets:

$$ax^2+bx+c
=a\left(x+\frac b{2a}\right)^2+c-\frac{b^2}{4a}.$$

No input values were lost: this is an identity for every real $x$.
The sign of $a$ determines whether the square opens upward or downward.
For $a>0$ its smallest contribution is zero, while for $a<0$ its largest
contribution is zero.

**Worked example 2: one quadratic, three questions.** Let
$q(x)=2x^2-8x+5$. Factor the leading coefficient from the first two terms,
then complete the square:

$$q(x)=2(x^2-4x)+5=2[(x-2)^2-4]+5=2(x-2)^2-3.$$

Its minimum is $-3$ at $x=2$, since $(x-2)^2\ge0$. For its zeros, solve
$(x-2)^2=3/2$, so
$x=2\pm\sqrt{3/2}=2\pm\sqrt6/2$. Both values are real and both must be kept.
For the level inequality $q(x)\le5$, solve
$2(x-2)^2-3\le5$, then $(x-2)^2\le4$, hence $|x-2|\le2$ and
$0\le x\le4$. Substitution at both endpoints gives exactly $q=5$.

![Quadratic two times x minus two squared minus three, with its vertex, exact roots, and the level five whose sublevel interval runs from zero to four.](../../assets/figures/lessons-foundations/quadratic-levels.png)

The level line and shaded sublevel region represent the same inequality as
the algebra. The exact root labels come from the square-root calculation,
not from reading rounded coordinates off a graph.

The completed square also derives the quadratic formula. Setting the general
identity to zero gives
$(x+b/(2a))^2=(b^2-4ac)/(4a^2)$. A real solution requires
$b^2-4ac\ge0$. Taking both signs and simplifying the unordered pair yields
$x=(-b\pm\sqrt{b^2-4ac})/(2a)$. If the discriminant is zero, the two signs
name one repeated root, rather than two distinct roots.

## Stage 3: solve inequalities with sign information intact

Adding the same quantity to both sides preserves an inequality. Multiplication
by a positive number preserves its direction; multiplication by a negative
number reverses it. When the multiplier depends on $x$, its sign may change,
so cross multiplication cannot be used without a sign analysis.

**Worked example 3: a rational inequality.** Solve

$$\frac{x-1}{x+2}\ge0.$$

First exclude $x=-2$. The numerator changes sign at $1$ and the denominator
changes sign at $-2$. These values divide the real line into three intervals:

| Interval | Sign of $x-1$ | Sign of $x+2$ | Sign of quotient |
| --- | --- | --- | --- |
| $(-\infty,-2)$ | negative | negative | positive |
| $(-2,1)$ | negative | positive | negative |
| $(1,\infty)$ | positive | positive | positive |

The desired nonnegative values occur on the first and third intervals.
Include $x=1$, where the quotient is zero; exclude $x=-2$, where it is
undefined. Thus the answer is $(-\infty,-2)\cup[1,\infty)$.
Check representatives $-3,0,2$: their quotient values are $4,-1/2,1/4$,
confirming the three signs independently.

Absolute value inequalities encode distances. For $c\ge0$,
$|u|\le c$ means $-c\le u\le c$, whereas $|u|>c$ means
$u<-c$ or $u>c$. These are an intersection and a union, respectively.
For $c<0$, $|u|\le c$ has no solution because absolute values are nonnegative.
Checking the sign of the threshold first prevents a meaningless interval.

Squaring inequalities also needs care. For nonnegative $a,b$, $a\le b$
is equivalent to $a^2\le b^2$. Over all real numbers this fails: $-3<2$
but $9>4$. Establish sign conditions before applying a monotone operation.

## Stage 4: composition means passing through two domains

For $(g\circ f)(x)=g(f(x))$, first $x$ must lie in the domain of $f$.
Then $f(x)$ must lie in the domain of $g$. The exact composition domain is
$\{x\in\operatorname{dom}f:f(x)\in\operatorname{dom}g\}$.
The order matters because an output suitable for one next operation may not
be suitable for another.

**Worked example 4: square root and logarithm.** Set
$f(x)=\sqrt{x-1}$ on $[1,\infty)$ and $g(u)=\ln u$ on $(0,\infty)$.
For $g\circ f$, the inner root must be strictly positive, giving $x>1$.
Then $g(f(x))=\ln\sqrt{x-1}=\tfrac12\ln(x-1)$.
For $f\circ g$, the logarithm must be at least $1$, so $x\ge e$.
Its formula is $\sqrt{\ln x-1}$. The functions have different formulas and
different domains; neither order can be inferred from the names alone.

Composition makes physical units useful as a type check. A sensor calibration
may turn a voltage into a displacement, after which a geometry formula turns
that displacement into an area. Feeding the original voltage directly into
the area formula would violate the meaning of the input even if software
accepted the numerical value.

## Stage 5: an inverse undoes a chosen one-to-one assignment

An inverse function exists when the original map is a bijection between its
declared domain and codomain. If a formula repeats values, restrict its domain
to a branch on which values are not repeated, and choose its range as codomain.
Changing a domain is a mathematical choice that must be stated.

**Worked example 5: choose a square branch.** The formula $x^2$ on all reals
has $f(2)=f(-2)=4$, so no inverse can decide which input to recover from $4$.
Restrict to $f:[0,\infty)\to[0,\infty)$, $f(x)=x^2$.
This map is one-to-one and reaches each nonnegative output. Its inverse is
$g(y)=\sqrt y$. For $x\ge0$, $g(f(x))=\sqrt{x^2}=x$; for $y\ge0$,
$f(g(y))=(\sqrt y)^2=y$. These two checks identify the correct domains.

![The nonnegative square branch and its square-root inverse reflected in the line y equals x, with exact points two comma four and four comma two.](../../assets/figures/lessons-foundations/inverse-branches.png)

The reflection swaps input and output, so $(2,4)$ becomes $(4,2)$.
If instead we restricted $x^2$ to $(-\infty,0]$, the inverse would be
$-\sqrt y$. The negative branch is equally legitimate when declared, but
combining both branches would make the inverse multivalued.

**Worked example 6: logarithms and exact roots.** Solve
$\log_3(x-2)+\log_3(x+2)=2$. Both arguments must be positive, hence $x>2$.
The product rule gives $\log_3(x^2-4)=2$, then $x^2-4=9$.
The algebraic candidates are $x=\pm\sqrt{13}$. Only $\sqrt{13}$ satisfies
$x>2$, since $13>4$. Its original two positive arguments have product $9$,
so their logarithms sum to $\log_39=2$. The negative candidate fails the
original domain and must be discarded.

The product law requires positive factors for real logarithms. Although
$(-1)(-1)=1$, writing $\ln(-1)+\ln(-1)=\ln1$ is unavailable in real
arithmetic. A formal product with a positive result does not retroactively
make each logarithm meaningful.

## Practice problems

1. **AF-01:** Find the real domain of $\sqrt{x+3}/(x-1)$.
2. **AF-02:** Solve $(x^2-9)/(x-3)=6$ on its original domain.
3. **AF-03:** Complete the square in $3x^2+6x-2$, and give its minimum and both exact roots.
4. **AF-04:** Solve $(x+1)/(x-2)<0$ with correct endpoint inclusion.
5. **AF-05:** Solve $|2x-5|\le3$ and explain its distance interpretation.
6. **AF-06:** For $f(x)=x+2$ and $g(x)=1/x$, find both compositions and their domains.
7. **AF-07:** Restrict $f(x)=(x-1)^2+2$ to $x\ge1$ and find its inverse, including both maps' domains and ranges.
8. **AF-08:** Solve $\ln(x-1)+\ln(x+1)=\ln8$ exactly and check the original domain.

## Answers and explanations

1. The root needs $x\ge-3$ and the denominator needs $x\ne1$.
Together the domain is $[-3,1)\cup(1,\infty)$. The value $-3$ is allowed
because a zero numerator is harmless when the denominator is nonzero.
2. The original restriction is $x\ne3$. Cancellation gives $x+3=6$, whose
only candidate is the excluded value $3$. Therefore the solution set is empty.
3. $3(x+1)^2-5$ has minimum $-5$ at $x=-1$.
The zeros satisfy $(x+1)^2=5/3$, so $x=-1\pm\sqrt{15}/3$.
Substituting the squared relation into the completed square verifies both.
4. Critical values are $-1$ and $2$. The quotient is negative only between
them, so $x\in(-1,2)$. Strict inequality excludes the numerator zero, while
the denominator zero is excluded independently of strictness.
5. The double inequality $-3\le2x-5\le3$ gives $1\le x\le4$.
Equivalently $|x-5/2|\le3/2$: the input is within distance $3/2$ of $5/2$.
6. $(g\circ f)(x)=1/(x+2)$ on $\mathbb R\setminus\{-2\}$.
$(f\circ g)(x)=1/x+2$ on $\mathbb R\setminus\{0\}$.
Each exclusion belongs to the stage at which its denominator is evaluated.
7. The original domain is $[1,\infty)$ and range is $[2,\infty)$.
Solving $y=(x-1)^2+2$ with $x-1\ge0$ gives $x=1+\sqrt{y-2}$.
The inverse therefore has domain $[2,\infty)$ and range $[1,\infty)$.
8. The original arguments require $x>1$. Combining logs gives
$x^2-1=8$, hence candidates $\pm3$. Only $3$ is allowed, and
$\ln2+\ln4=\ln8$ checks it.

## Transfer to a mechanical design calculation

Suppose a rectangular opening has perimeter $12\ \mathrm m$ and positive
sides $w$ and $6-w$ metres. Its area is
$A=9-(w-3)^2$ square metres when numerical $w$ is expressed in metres,
with $0<w<6$. The maximum area is $9\ \mathrm{m^2}$ at $w=3\ \mathrm m$.
Requiring at least $8\ \mathrm{m^2}$ gives $(w-3)^2\le1$, hence
$2\le w\le4$ metres. Completing the square supplies the optimum and the
allowable interval in one calculation. The model describes the opening only;
wall thickness, stress, and fabrication constraints would add conditions.

## Reproducible diagrams and verification

[plot_lessons_foundations.py](../../scripts/plot_lessons_foundations.py) plots
the exact quadratic and inverse pair. [verify_lessons_foundations.py](../../scripts/verify_lessons_foundations.py)
checks factorizations, completed squares, radical roots, representative signs,
composition formulas, and inverse identities on their declared branches.
A sampled curve illustrates the solution; the algebra establishes its exact
endpoints and excluded values.

## References and further study

OpenStax, [*Precalculus 2e*, function, transformation, and logarithm entries](https://openstax.org/books/precalculus-2e/pages/index), is a reference route for additional exercises. Use the [functions and limits reference](../../subjects/analysis/functions-limits-and-series.md) to continue from a missing value to a removable discontinuity, and the [algebra reference](../../subjects/algebra/elementary-algebra.md) for finite sums and the binomial theorem. This lesson's derivations, examples, and figures are original.
