# Trigonometry and harmonic motion

**Topic ID:** TRI-001  
**Classification:** Trigonometry → angles, triangles, periodic functions, phasors  
**Level:** Elementary to precalculus, with a complex-number bridge  
**Content status:** Written compact reference, with reproducible figures.  
**Learner mastery:** Unassessed.

## Prerequisites

Use [algebra](../algebra/elementary-algebra.md), square roots, and the
Pythagorean theorem. Diagnostic: a right triangle with perpendicular sides $5$
and $12$ has hypotenuse $13$, since $5^2+12^2=169$. An angle must carry a
declared convention: degrees and radians have different numerical values.

## Definition

An angle measured in **radians** is $\theta=s/r$, where $s$ is signed arc
length on a circle of radius $r>0$. One revolution is $2\pi$ radians or
$360^\circ$. Positive angles rotate counterclockwise in the usual Cartesian
plane. Angles differing by $2\pi k$, $k\in\mathbb Z$, have the same terminal ray.

On the unit circle the point reached by angle $\theta$ is
$(\cos\theta,\sin\theta)$. Thus sine and cosine are defined for every real
angle, including those outside a right triangle. Define
$\tan\theta=\sin\theta/\cos\theta$ when $\cos\theta\ne0$;
$\sec\theta=1/\cos\theta$, $\csc\theta=1/\sin\theta$, and
$\cot\theta=\cos\theta/\sin\theta$ on their respective nonzero domains.

For an acute angle in a right triangle these definitions give opposite over
hypotenuse, adjacent over hypotenuse, and opposite over adjacent for sine,
cosine, and tangent. “Opposite” and “adjacent” depend on the chosen angle.

## Intuitive explanation

Cosine and sine are the horizontal and vertical projections of a rotating unit
radius. Their bounded periodic graphs come from repeating the same rotation.
Tangent compares vertical to horizontal projection, so it becomes unbounded
when the horizontal projection approaches zero. The functions are related but
their domains and periods differ.

![Unit circle with the exact point (one half, square root of three over two) at angle pi over three.](../../assets/figures/foundations/unit-circle.png)

The figure uses equal axis scales. The labeled point is exactly
$(1/2,\sqrt3/2)$ at $\theta=\pi/3$, not a value inferred from pixel position.

## Mathematical notation

Angles in formulas are radians unless a degree sign appears. For a triangle,
$A,B,C\in(0,\pi)$ denote its interior angles, and $a,b,c>0$ are the opposite
side lengths, measured in one common length unit. $R$ is circumradius.
For oscillations, $t$ is time in seconds, $\omega$ is angular frequency in
$\mathrm{rad/s}$, $\phi$ is phase in radians, and $A_0\ge0$ is amplitude.

## Fundamental properties

Sine and cosine have period $2\pi$ and range $[-1,1]$. Sine is odd and cosine
is even. Tangent has period $\pi$, is odd, and is undefined at
$\pi/2+k\pi$. On $(-\pi/2,\pi/2)$ it takes every real value once.

Inverse trigonometric functions require restricted branches:
$\arcsin:[-1,1]\to[-\pi/2,\pi/2]$,
$\arccos:[-1,1]\to[0,\pi]$, and
$\arctan:\mathbb R\to(-\pi/2,\pi/2)$.
Thus $\arcsin(\sin(5\pi/6))=\pi/6$, not $5\pi/6$.

An ordinary Euclidean triangle satisfies $A+B+C=\pi$ and strict triangle
inequalities. The side-side-angle data can produce zero, one, or two triangles;
an inverse sine alone does not settle the ambiguity. In the equality case of a
triangle inequality the figure degenerates to collinear points.

## Important formulas and identities

The unit circle yields $\sin^2\theta+\cos^2\theta=1$. Dividing by a
nonzero $\cos^2\theta$ gives $1+\tan^2\theta=\sec^2\theta$.

$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta,$$
$$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta.$$

Consequently
$\sin2\theta=2\sin\theta\cos\theta$,
$\cos2\theta=1-2\sin^2\theta=2\cos^2\theta-1$, and
$\sin^2(\theta/2)=(1-\cos\theta)/2$. A half-angle square root needs a sign
chosen from the angle's quadrant.

For $r>0$ and central angle $0\le\theta\le2\pi$,
arc length is $s=r\theta$ and sector area is $r^2\theta/2$.
For a nondegenerate triangle,

$$\frac a{\sin A}=\frac b{\sin B}=\frac c{\sin C}=2R,\qquad
c^2=a^2+b^2-2ab\cos C,\qquad K=\frac12ab\sin C.$$

Harmonic motion is $x(t)=x_0+A_0\cos(\omega t+\phi)$.
For $\omega>0$, its period is $T=2\pi/\omega$ and frequency is $1/T$.
The complex representation is
$x(t)-x_0=\operatorname{Re}(\widehat X e^{i\omega t})$ with
$\widehat X=A_0e^{i\phi}$ and $e^{i\theta}=\cos\theta+i\sin\theta$.
Euler's identity is cited here; it can be derived from the convergent power
series for the exponential, sine, and cosine.

## Derivations and proofs

**Cosine addition formula from rotations.** A plane rotation through $\alpha$
has matrix

$$R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha\end{pmatrix}.$$

Apply it to $(\cos\beta,\sin\beta)$. Rotation adds the directed angles, so
the first coordinate of the product is both $\cos(\alpha+\beta)$ and
$\cos\alpha\cos\beta-\sin\alpha\sin\beta$. The second coordinate gives
the sine formula. This geometric argument assumes the standard Euclidean
rotation operation and does not depend on a diagram's measured accuracy.

**Cosine law.** Put the vertex of angle $C$ at the origin, one adjacent vertex
at $(a,0)$, and the other at $(b\cos C,b\sin C)$.
The opposite squared length is
$(a-b\cos C)^2+(b\sin C)^2=a^2+b^2-2ab\cos C$.
This also handles obtuse $C$, for which the cosine is negative.

## Worked examples

**1. Exact oblique triangle.** Let sides adjacent to angle $C=60^\circ$ be
$a=5\ \mathrm m$, $b=8\ \mathrm m$. By the cosine law,
$c^2=25+64-80(1/2)=49$, so $c=7\ \mathrm m$.
Its area is $K=(1/2)5\cdot8\cdot(\sqrt3/2)=10\sqrt3\ \mathrm{m^2}$.
The side inequalities $5+7>8$, $5+8>7$, and $7+8>5$ check nondegeneracy.

**2. All solutions of an equation.** Solve $2\sin x=1$ on the real line.
First $\sin x=1/2$. The unit circle gives angles $\pi/6$ and $5\pi/6$
in one revolution. Therefore $x=\pi/6+2k\pi$ or
$x=5\pi/6+2k\pi$, $k\in\mathbb Z$. Restricting to $[0,2\pi)$ keeps only
those two values; a calculator's principal inverse supplies only the first.

**3. An inequality.** Solve $\cos x\ge\sqrt2/2$ on $[-\pi,\pi]$.
Equality occurs at $\pm\pi/4$. The horizontal coordinate on the unit circle
is at least $\sqrt2/2$ between these angles, so the solution is
$[-\pi/4,\pi/4]$. Testing $x=0$ gives $1$, while testing $x=\pi/2$ gives $0$,
confirming the selected interval.

**4. Combining same-frequency signals.** Let
$x(t)=3\cos(2t)+4\sin(2t)$ millimetres, with $t$ in seconds.
Choose $\delta\in(0,\pi/2)$ with $\cos\delta=3/5$, $\sin\delta=4/5$.
Expanding $5\cos(2t-\delta)$ recovers the two terms. Hence amplitude is
$5\ \mathrm{mm}$, phase is $-\delta=-\arctan(4/3)$, and period is
$\pi\ \mathrm s$. At $t=0$ both formulas give $3\ \mathrm{mm}$.

![Harmonic displacement 3 cos(2t) plus 4 sin(2t), with amplitude five millimetres and period pi seconds.](../../assets/figures/foundations/harmonic-motion.png)

## Practice problems

1. **TRI-01:** Convert $135^\circ$ to radians and find its exact sine and cosine.
2. **TRI-02:** Find the arc length and sector area for radius $6\ \mathrm{cm}$ and angle $\pi/3$.
3. **TRI-03:** Solve $\tan x=-1$ for all real $x$.
4. **TRI-04:** Triangle data are $A=30^\circ$, $a=5$, $b=8$. Find $\sin B$, all possible angles $B$, and the number of triangles.
5. **TRI-05:** Evaluate $\sin(\pi/12)$ exactly using an angle difference.

## Answers and explanations

1. Multiply by $\pi/180$: $3\pi/4$. The reference angle is $\pi/4$ in
quadrant II, so sine is $\sqrt2/2$ and cosine is $-\sqrt2/2$.
2. $s=6(\pi/3)=2\pi\ \mathrm{cm}$ and
$K=36(\pi/3)/2=6\pi\ \mathrm{cm^2}$. Areas require squared length units.
3. One solution is $-\pi/4$ and the tangent period is $\pi$, so
$x=-\pi/4+k\pi$, $k\in\mathbb Z$; none is a tangent pole.
4. The sine law gives one sine value $\sin B=8\sin(30^\circ)/5=4/5$.
There are two possible angles, $B_1=\arcsin(4/5)$ and $B_2=\pi-B_1$.
Both satisfy $A+B<\pi$: in the second case this follows from
$B_1>\pi/6$. Thus there are two triangles, with the same sine value.
5. Use $\pi/12=\pi/4-\pi/6$. The sine difference formula gives
$\sqrt6/4-\sqrt2/4=(\sqrt6-\sqrt2)/4$, positive in quadrant I.

## Common mistakes and misconceptions

Radians are required in $s=r\theta$ and the standard calculus derivatives.
The notation $\sin^{-1}x$ usually denotes arcsine, while $1/\sin x$ is
cosecant; use unambiguous notation. Dividing an equation by $\sin x$ can lose
solutions at its zeros. A phasor combination with fixed complex amplitudes
assumes a common frequency; different frequencies generally do not combine
into one sinusoid with a constant amplitude and phase.

## Connections to other mathematics

[Complex arithmetic](../numbers/arithmetic-and-number-systems.md) makes phasors
compact. [Functions and series](../analysis/functions-limits-and-series.md)
clarify periodicity and infinite trigonometric expansions. Triangle formulas
support coordinate geometry, surveying, and subsequent conic parametrizations.

## Applications

A straight pipe rises $2\ \mathrm m$ over a horizontal run $5\ \mathrm m$.
Its inclination is $\arctan(2/5)$ and length is $\sqrt{29}\ \mathrm m$.
The slope is $2/5$, a dimensionless ratio, while the angle has a radian value;
they are not interchangeable except under a stated small-angle approximation.
Real pipe routing also has fittings and clearances outside this line-segment model.

## Optional computational examples

Run [plot_foundations.py](../../scripts/plot_foundations.py) to regenerate the
unit-circle and harmonic PNG/SVG figures. The exact expressions in the text
define their geometry; sampled curves are visual aids. The script labels the
axis units, uses equal scales for the circle, and checks the marked angle.

## References and recommended reading

OpenStax, [*Precalculus 2e*, index entries for “Angles,” “Unit Circle,” “Trigonometric Identities,” “Trigonometric Equations,” and “Polar Form of Complex Numbers”](https://openstax.org/books/precalculus-2e/pages/index), provides a verified route to these sections. The formulas and numerical examples above are developed independently here. Deriving Euler's identity from power series is a natural next topic.

## Revision and mastery status

Written 2026-10-18; learner mastery unassessed. Reconstruct an exact-angle value,
solve a periodic equation with all branches, and explain the sine-law ambiguity
before recording mastery. General spherical trigonometry is beyond this chapter.
