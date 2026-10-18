# Calculus from limits to models

**Lesson ID:** LES-CAL-01.  
**Prerequisites:** Algebraic manipulation, functions, inequalities, basic trigonometry in radians, and units.  
**Objectives:** Turn a tolerance into a limit proof; derive a derivative; connect accumulation and rate; construct an approximation with a justified error bound.  
**Status:** Written guided lesson; learner mastery unassessed.

Use the [single-variable reference](../../subjects/calculus/single-variable-calculus.md) for a compact formula lookup and [real analysis](../../subjects/analysis/real-analysis-and-measure.md) for the surrounding rigorous theory. This lesson develops one connected argument: a model predicts a value; a tolerance states what accuracy is required; a limit justifies a local approximation; differentiation and integration then connect local rates to accumulated quantities. The examples are deliberately exact until the final interpretation.

## Stage 1: a limit is a tolerance promise

Suppose a sensor computes the square of a dimensionless input. Near input two, the expected output is four. Saying $x^2\to4$ as $x\to2$ means something operational: for every requested output tolerance $\varepsilon>0$, we can supply an input tolerance $\delta>0$ such that

$$0<|x-2|<\delta\quad\Longrightarrow\quad|x^2-4|<\varepsilon.$$

The order matters. A user chooses the output tolerance first; our input guarantee must then work for every input in that neighborhood. Checking three inputs, or drawing a smooth-looking curve, cannot establish that universal promise.

**Worked example 1: construct the guarantee.** Factor the error:

$$|x^2-4|=|x-2||x+2|.$$

The second factor is not constant, so first impose $|x-2|<1$. Then $1<x<3$, hence $|x+2|<5$. Therefore choosing

$$\delta=\min\{1,\varepsilon/5\}$$

gives $|x^2-4|<5\delta\le\varepsilon$. The proof has two jobs: restrict the changing factor, then control the factor that vanishes. This bound is convenient rather than the largest possible allowable tolerance.

For a requested output error below $1/100$, it suffices to keep the input error below $1/500$. The calculation uses dimensionless inputs. If $x$ were a length in metres, then $x^2$ would have units m² and numerical tolerances would need those units or a dimensionless rescaling. An epsilon is a positive tolerance in the output's units, while delta belongs to the input's units.

Continuity at two adds the statement $f(2)=4$. A limit alone concerns neighboring values and need not equal the assigned value at the point. For example, assigning $f(2)=9$ while keeping $f(x)=x^2$ elsewhere leaves the same limit but breaks continuity. This distinction will matter when we differentiate an accumulated integral: continuity at the point is a precise hypothesis, not a decorative word.

Pause and predict: if the required output tolerance is halved, our sufficient input tolerance also halves once $\varepsilon<5$. That proportionality comes from the local slope scale. The next stage makes the scale exact in the limit.

## Stage 2: derive a rate before using differentiation rules

An average rate between $a$ and $a+h$ is

$$\frac{f(a+h)-f(a)}h,\qquad h\ne0.$$

The derivative is the finite two-sided limit of these quotients as $h\to0$. We do not evaluate the original quotient at $h=0$. Instead, algebra can produce an equivalent expression for nonzero $h$, whose limit is accessible.

**Worked example 2: the square function.** With $f(x)=x^2$,

$$\frac{(a+h)^2-a^2}{h}
=\frac{2ah+h^2}{h}=2a+h\qquad(h\ne0).$$

Given any desired slope error $\eta>0$, taking $0<|h|<\eta$ gives $|(2a+h)-2a|<\eta$. Thus the derivative is $2a$. At $a=1$, secant slopes for $h=1,1/2,1/4,-1/2$ are exactly $3,5/2,9/4,3/2$; all approach the tangent slope two as the interval shrinks from either side.

![Secant lines approaching the tangent to the square function](../../assets/figures/lessons-analysis/calculus-secants.png)

The exact curve is $y=x^2$ and the tangent at $(1,1)$ is $y=1+2(x-1)$. Secants use $h=1,1/2,-1/2$ and hence slopes $2+h$. Equal axis scales make the angles interpretable; both coordinates are dimensionless.

The same expansion gives a stronger statement than the derivative's value:

$$f(a+h)=f(a)+2ah+h^2.$$

The local linear estimate omits the exact error $h^2$. The error divided by $|h|$ tends to zero, which is the meaning of a first-order approximation. A nonzero error is therefore compatible with a perfectly correct derivative.

**Worked example 3: a square root with a domain condition.** Let $f(x)=\sqrt x$ at $a>0$. Choose $h$ small enough that $a+h>0$. Rationalizing the difference quotient gives

$$\frac{\sqrt{a+h}-\sqrt a}{h}
=\frac1{\sqrt{a+h}+\sqrt a}
\longrightarrow\frac1{2\sqrt a}.$$

At $a=4$, the tangent estimate is $\sqrt{4+h}\approx2+h/4$. The assumption $a>0$ ensures a positive denominator and a two-sided domain neighborhood. At zero, the right quotient is $1/\sqrt h$, which becomes unbounded, so there is no finite derivative there. Copying the interior formula to the endpoint would conceal both issues.

Differentiability implies continuity because $f(a+h)-f(a)$ is the quotient multiplied by $h$: a finite quotient limit times a vanishing increment gives zero. Continuity does not imply differentiability. For $|x|$ at zero, the right quotient is one and the left quotient minus one. The failure is visible in the definition, even before any rule is memorized.

## Stage 3: accumulating a rate and recovering it

Let $q(t)$ be a continuous volume-flow rate on a closed time interval, measured in m³/s. A Riemann sum $\sum q(\xi_i)\Delta t_i$ approximates the volume crossing a section. As the largest time step shrinks, its limit is the integral. Define accumulated volume

$$V(t)=\int_0^t q(s)\,ds.$$

The first fundamental theorem of calculus states $V'(t)=q(t)$ at interior points where $q$ is continuous. To see why, write

$$\frac{V(t+h)-V(t)}h-q(t)
=\frac1h\int_t^{t+h}[q(s)-q(t)]\,ds.$$

Its magnitude is bounded by the largest variation of $q$ over that short interval. Continuity makes this bound tend to zero from either side. This is the proof's entire mechanism: an average of almost constant values is almost that constant. If the rate jumps, the ordinary two-sided derivative of accumulation at that exact time may fail.

The second fundamental theorem states that if $F'=q$ on the interval, with the regularity needed to integrate $q$, then $\int_a^bq=F(b)-F(a)$. One proof compares $F$ with the accumulation function: their difference has derivative zero, so the mean value theorem makes it constant. The mean value theorem requires continuity on the closed interval and differentiability in its interior.

**Worked example 4: decaying flow.** Let

$$q(t)=2e^{-t/3}\ {\rm m^3/s},\qquad t\ge0,$$

where the three in the exponent represents a time scale of three seconds. Then

$$V(t)=6(1-e^{-t/3})\ {\rm m^3}.$$

At three seconds the delivered volume is $6(1-e^{-1})$ m³, approximately $3.793$ m³. Differentiation returns the stated rate, and $V(0)=0$ checks the initial accumulation. Since $0<q(t)\le2$ over this interval, the volume is between zero and six cubic metres; the exact answer passes that independent magnitude check.

Notice that the limiting total volume is six cubic metres even though the flow remains positive at every finite time. A positive rate need not imply unbounded accumulation; its integral can converge. Conversely, integrating a discontinuous model does not automatically smooth every feature into an everywhere-differentiable curve. At a step change in flow, accumulated volume is continuous but has a corner.

## Stage 4: approximation needs an error statement

The derivative gives a tangent approximation. Repeated derivatives give a Taylor polynomial. If $f$ has $n+1$ continuous derivatives on the interval joining $a$ and $a+h$, Taylor's theorem gives

$$f(a+h)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}h^k
+\frac{f^{(n+1)}(\xi)}{(n+1)!}h^{n+1}$$

for an intermediate $\xi$. Therefore a bound $|f^{(n+1)}|\le M$ on that whole interval gives an error at most $M|h|^{n+1}/(n+1)!$. Knowing a derivative's value at the center alone cannot supply the whole-interval bound.

For $e^h$ about zero, the quadratic polynomial is $1+h+h^2/2$. On $|h|\le1/2$, its remainder has magnitude at most $e^{1/2}|h|^3/6$. This is an upper bound, not the actual error. The actual error can be smaller and its sign changes with the sign of $h$.

![Actual exponential Taylor error and a uniform cubic upper bound](../../assets/figures/lessons-analysis/calculus-taylor-error.png)

The graph shows $|e^h-(1+h+h^2/2)|$ and $e^{1/2}|h|^3/6$ for $-1/2\le h\le1/2$. The error is computed from the exact functions before floating-point evaluation. The bound is established by Taylor's theorem, rather than inferred from the plotted samples.

## Stage 5: translate local error into engineering meaning

**Worked example 5: radius tolerance and spherical volume.** A sphere has nominal radius $r_0=1$ m with radius increment $h=1/100$ m. The exact volume change is

$$\Delta V=\frac{4\pi}3[(r_0+h)^3-r_0^3]
=4\pi r_0^2h+4\pi r_0h^2+\frac{4\pi}3h^3.$$

The first-order estimate is $4\pi/100=\pi/25$ m³. Its omitted error is

$$4\pi/10000+4\pi/(3\,000\,000)
=301\pi/750000\ {\rm m^3}.$$

The relative error measured against the first-order estimate is $301/30000$, about $1.0033\%$. If measured against the exact change, it is $301/30301$, about $0.9934\%$. Declaring the denominator prevents two correct calculations from seeming contradictory.

For a tolerance $|h|\le1/100$ m, an absolute first-order remainder bound is

$$|\Delta V-4\pi r_0^2h|
\le4\pi r_0h^2+\frac{4\pi}3|h|^3.$$

Both terms have units m³. The derivative has units m², so multiplying it by the radius error gives a volume error. A second-order approximation keeps the $h^2$ term and leaves only the cubic term. More terms improve this polynomial model exactly; they do not address whether the actual object is spherical or whether the radius measurement is biased.

## Practice problems

1. For $f(x)=3x-1$ at $x=2$, construct a delta for any output tolerance $\varepsilon>0$.
2. For the square-function proof at two, what sufficient delta corresponds to $\varepsilon=1/20$? Is it claimed to be optimal?
3. Derive the derivative of $x^3$ at an arbitrary real $a$ from the difference quotient.
4. Does $f(x)=|x-2|$ have a derivative at two? Show the two quotients.
5. If $q(t)=3t^2$ m³/s for the numerical time $t$ in seconds, find accumulation from zero to two seconds, with consistent coefficient units.
6. Let $q(t)=0$ for $t<1$ and $q(t)=2$ for $t>1$. Is its accumulation from zero differentiable at one?
7. Bound the error of replacing $\sin h$ by $h-h^3/6$ for $|h|\le1/5$.
8. For the sphere example, find the exact error after retaining the quadratic correction.

## Answers and explanations

1. The error is $|3x-6|=3|x-2|$. Choose $\delta=\varepsilon/3$. No auxiliary neighborhood is necessary because the other factor is constant.
2. $\delta=\min(1,1/100)=1/100$. It is a sufficient bound. A different estimate of $|x+2|$ could enlarge it; a limit proof needs a valid guarantee rather than the largest one.
3. For $h\ne0$, the quotient is $3a^2+3ah+h^2$, whose limit is $3a^2$. The discarded terms tend to zero for each fixed $a$.
4. No. The quotient is $|h|/h$, which equals one for positive $h$ and minus one for negative $h$. Each one-sided derivative exists, but they disagree.
5. The coefficient has units m³/s³ when $t$ carries seconds. Integrating gives $V(t)=t^3$ with that coefficient's corresponding units, so $V(2\ {\rm s})=8$ m³. More transparently, write $q=3(t/(1\ {\rm s}))^2$ m³/s before integrating.
6. Accumulation is zero up to one and $2(t-1)$ afterward, in the chosen compatible units. Left derivative zero and right derivative two disagree. The single assigned value of $q(1)$ cannot repair that corner.
7. Apply Taylor through degree four: the $h^4$ coefficient is zero and the fifth derivative of sine has magnitude at most one. The error is at most $|h|^5/120\le1/375000$. Using degree three alone gives a weaker valid fourth-order bound; including the zero coefficient sharpens it.
8. The remaining error is exactly $4\pi h^3/3=\pi/750000$ m³ for the positive increment. For a signed tolerance, use its absolute value in the error bound.

## Verification and further study

[Plot source](../../scripts/plot_lessons_analysis.py) generates both diagrams; [exact checks](../../scripts/verify_lessons_analysis.py) verify quotients, integrals, polynomial remainders, and exercise arithmetic. Computation checks the encoded expressions, while the tolerance and theorem arguments supply the general justification.

Further study: Strang and Herman, OpenStax [Calculus Volume 1](https://openstax.org/details/books/calculus-volume-1), limits, derivatives, and fundamental theorem; [Calculus Volume 2](https://openstax.org/details/books/calculus-volume-2), Taylor polynomials and remainder estimates. These are sources for the underlying theorems; the teaching sequence and examples here are original.

Written 2026-10-18. To demonstrate mastery, give an input guarantee for a requested output tolerance, derive one derivative without a rule, recover a rate from an accumulation, and state both the approximation and its error units. Learner assessment and a review date require actual study evidence.
