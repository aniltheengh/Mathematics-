# Trigonometry and vectors: rotation, phase, and mechanical projections

**Lesson ID:** LES-FND-03  
**Level:** Trigonometry through introductory vector methods.  
**Lesson status:** Written guided lesson with exact mechanical calculations and reproducible diagrams.  
**Learner mastery:** Unassessed.

## Prerequisites

Use the Pythagorean theorem, exact fractions and radicals,
[trigonometry](../../subjects/trigonometry/trigonometry.md), and the first
definitions of [vectors and inner products](../../subjects/linear-algebra/linear-algebra.md).
This lesson uses real two-dimensional vectors with the ordinary Euclidean dot
product. Cartesian axes are perpendicular and have compatible scales. Angles
are radians unless a degree sign is shown. Mechanical examples declare their
units and describe idealized forces or displacements, not a complete design.

Diagnostic: $(3/5)^2+(4/5)^2=1$. Therefore $(3/5,4/5)$ is a unit vector.
Its components are not merely a ratio: their squared sum establishes its unit
length. A direction such as $(3,4)$ must be normalized before a dot product
is interpreted as a signed component along that direction.

## Learning objectives

You will explain why radians simplify arc length, read exact sine and cosine
values from a unit circle, derive addition formulas from rotations, combine
same-frequency motion into amplitude and phase, and separate a force into
parallel and perpendicular components with an independent orthogonality check.
The common idea is projection: trigonometric functions are the coordinate
projections of a rotating radius, and vector components generalize that operation.

## Stage 1: radians compare an arc with its radius

For a circular arc of signed length $s$ on radius $r>0$, define the radian
angle $\theta=s/r$. A full revolution has arc length $2\pi r$, hence angle
$2\pi$. Thus $180^\circ=\pi$ radians and
$\theta_{\mathrm{rad}}=(\pi/180)\theta_{\mathrm{deg}}$.

The ratio is dimensionless when arc length and radius use the same length
unit. The label “radian” still matters because it tells us which numerical
angle convention is being used. For radians, arc length is simply $s=r\theta$.
Substituting a degree value into that formula would introduce a factor error.

**Worked example 1: a rotating marker.** A marker on a wheel of radius
$0.4\ \mathrm m=2/5\ \mathrm m$ rotates by $150^\circ$.
First convert the angle: $150\pi/180=5\pi/6$. Its traveled circular distance is
$(2/5)(5\pi/6)=\pi/3\ \mathrm m$. The straight chord is a different length:
$2r\sin(\theta/2)=(4/5)\sin(5\pi/12)$ metres.
The arc follows the wheel while the chord connects the start and end positions.
They need not agree, even when they have the same length unit.

For a sector of angle $\theta\in[0,2\pi]$, the area is the same fraction
$\theta/(2\pi)$ of the full disk area $\pi r^2$, giving $r^2\theta/2$.
This derivation makes the radian condition visible rather than presenting
two unrelated formulas to memorize.

**Checkpoint.** A $90^\circ$ turn is $\pi/2$ radians. On radius
$2\ \mathrm m$, its arc is $\pi\ \mathrm m$, not $180\ \mathrm m$.

## Stage 2: a unit circle supplies signs and exact coordinates

The unit-circle point at angle $\theta$ is
$u(\theta)=(\cos\theta,\sin\theta)$. The Pythagorean theorem gives
$\cos^2\theta+\sin^2\theta=1$. Reflection across the horizontal axis gives
$\cos(-\theta)=\cos\theta$ and $\sin(-\theta)=-\sin\theta$.
A complete turn repeats the point, so both functions have period $2\pi$.

For a $45^\circ$ right triangle with unit hypotenuse, equal legs $a$ satisfy
$2a^2=1$, giving $a=\sqrt2/2$. Therefore
$u(\pi/4)=(\sqrt2/2,\sqrt2/2)$. Bisecting an equilateral triangle gives
$u(\pi/3)=(1/2,\sqrt3/2)$ and
$u(\pi/6)=(\sqrt3/2,1/2)$. Coordinates in other quadrants use the same
reference lengths with the signs determined by position.

For example $u(5\pi/6)=(-\sqrt3/2,1/2)$ lies to the left of the vertical
axis and above the horizontal axis. A positive square root alone cannot
decide the sign of a trigonometric value; the quadrant supplies that information.

The ratio $\tan\theta=\sin\theta/\cos\theta$ is defined only when the
horizontal component is nonzero. Its failure at $\pi/2$ describes a vertical
direction, not an infinite real output that can be substituted into ordinary
algebra. Solving a tangent equation must keep those excluded angles separate.

## Stage 3: derive angle addition from the action of a rotation

Let $e_1=(1,0)$ and $e_2=(0,1)$ be the standard unit basis vectors. A positive
rotation through $\alpha$ sends $e_1$ to
$(\cos\alpha,\sin\alpha)$. It sends the perpendicular vector $e_2$ to
$(-\sin\alpha,\cos\alpha)$, because the second direction is another quarter
turn counterclockwise. Rotations preserve linear combinations, so an arbitrary
vector $(x,y)=xe_1+ye_2$ becomes

$$R_\alpha(x,y)=
(x\cos\alpha-y\sin\alpha,\ x\sin\alpha+y\cos\alpha).$$

This is the matrix rule
$R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha\end{pmatrix}$.
Apply it to $u(\beta)=(\cos\beta,\sin\beta)$.
Geometrically the new direction is $\alpha+\beta$, so comparing coordinates gives

$$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta,$$
$$\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta.$$

Replacing $\beta$ by $-\beta$ and using evenness and oddness derives both
subtraction formulas. The signs follow the rotation operation; they need not
be learned as disconnected patterns. The assumption that a Euclidean rotation
is a linear map is the geometric fact used in this derivation.

![Unit-circle radii at beta equals pi over four and alpha plus beta equals five pi over twelve, with a pi over six rotation marked between them.](../../assets/figures/lessons-foundations/angle-addition.png)

**Worked example 2: obtain an unfamiliar exact angle.** Take
$\alpha=\pi/6$ and $\beta=\pi/4$. The angle is $5\pi/12=75^\circ$.
Substitute the known exact values into the addition formulas:

$$\cos\frac{5\pi}{12}
=\frac{\sqrt3}{2}\frac{\sqrt2}{2}
-\frac12\frac{\sqrt2}{2}
=\frac{\sqrt6-\sqrt2}{4},$$
$$\sin\frac{5\pi}{12}
=\frac12\frac{\sqrt2}{2}
+\frac{\sqrt3}{2}\frac{\sqrt2}{2}
=\frac{\sqrt6+\sqrt2}{4}.$$

Both values are positive, agreeing with quadrant I. Their squared sum is
$[(8-4\sqrt3)+(8+4\sqrt3)]/16=1$, an independent check. The cosine is
smaller than the sine because the angle is closer to the vertical axis.

## Stage 4: phase tells us where a sinusoid starts

A harmonic displacement can be written
$x(t)=A\cos(\omega t-\delta)$, where $A\ge0$ is amplitude,
$\omega>0$ is angular frequency, and $\delta$ is a phase angle. If $t$ is
seconds, $\omega$ is in radians per second and $T=2\pi/\omega$ is the period
in seconds. The first maximum at nonnegative time depends on the phase;
amplitude alone does not locate the peaks.

The addition formula gives

$$A\cos(\omega t-\delta)
=A\cos\delta\cos(\omega t)+A\sin\delta\sin(\omega t).$$

Thus $a\cos(\omega t)+b\sin(\omega t)$ has amplitude
$A=\sqrt{a^2+b^2}$. If $A>0$, choose a phase with
$\cos\delta=a/A$ and $\sin\delta=b/A$.
Using both equations selects the correct quadrant. The angle $\arctan(b/a)$
alone may choose the wrong quadrant, and is unavailable when $a=0$.
If $a=b=0$, the motion vanishes and phase has no unique physical meaning.

**Worked example 3: exact amplitude, phase, and timing.** Let
$x(t)=4\cos(3t)+3\sin(3t)$ millimetres, with $t$ in seconds.
Then $A=5\ \mathrm{mm}$, and choose the quadrant-I angle
$\delta=\arctan(3/4)$ so that $\cos\delta=4/5$ and $\sin\delta=3/5$.
The motion is $5\cos(3t-\delta)$ millimetres.
Its period is $2\pi/3\ \mathrm s$ and its first nonnegative maximum is at
$t=\delta/3$. At $t=0$, both forms give $4\ \mathrm{mm}$.
Differentiation gives initial velocity $9\ \mathrm{mm/s}$ in either form:
$15\sin\delta=9$. These checks verify the sign of the phase shift.

Phasors package the same geometry using complex numbers. With the convention
$x(t)=\operatorname{Re}(\widehat X e^{i\omega t})$, this example has
$\widehat X=4-3i$ millimetres, because the real part of
$(4-3i)(\cos3t+i\sin3t)$ is $4\cos3t+3\sin3t$.
Its argument is $-\delta$, consistent with $5e^{-i\delta}$.
Opposite exponential conventions change the sign convention, so state one
before importing a phasor formula. Fixed phasors combine signals at the same
frequency; different frequencies generally do not produce a single constant-amplitude sinusoid.

## Stage 5: project a mechanical vector onto a guide

For real vectors $v=(v_x,v_y)$ and $u=(u_x,u_y)$,
$v\cdot u=v_xu_x+v_yu_y$. If $u$ is a unit direction, the signed scalar
component along it is $v\cdot u$, and the parallel vector is
$v_\parallel=(v\cdot u)u$. The residual
$v_\perp=v-v_\parallel$ is perpendicular because

$$u\cdot v_\perp=u\cdot v-(v\cdot u)(u\cdot u)=0.$$

For a nonzero unnormalized direction $d$, the equivalent formula is
$v_\parallel=[(v\cdot d)/(d\cdot d)]d$. The denominator is a squared length;
omitting it changes both the vector and its units.

**Worked example 4: resolve a load.** A planar load is
$F=(6,8)\ \mathrm{kN}$. A straight guide has direction ratio $(4,3)$,
so its unit direction is $u=(4/5,3/5)$.
The signed load component along the guide is
$F\cdot u=24/5+24/5=48/5\ \mathrm{kN}$.
The corresponding vector and perpendicular remainder are

$$F_\parallel=\left(\frac{192}{25},\frac{144}{25}\right)\mathrm{kN},\qquad
F_\perp=\left(-\frac{42}{25},\frac{56}{25}\right)\mathrm{kN}.$$

Check the sum component by component: $(192-42)/25=6$ and
$(144+56)/25=8$. Check orthogonality:
$u\cdot F_\perp=(-168+168)/125=0$.
The magnitudes are $48/5$ and $14/5$ kN, and
$(48/5)^2+(14/5)^2=100=\|F\|^2$.
The three checks establish the decomposition without trusting a drawing's scale.

![A six comma eight kilonewton force split into its parallel component along the four comma three guide direction and a perpendicular residual.](../../assets/figures/lessons-foundations/mechanical-projection.png)

If a carriage displacement is $s=0.2u\ \mathrm m$, the ideal work done by this
constant load is $F\cdot s=(48/5)(1/5)=48/25\ \mathrm{kN\,m}=1920\ \mathrm J$.
The perpendicular component does no work along that displacement because its
dot product with $u$ is zero. This is a geometric force decomposition; actual
guide reactions, friction, and structural stresses require a separate model.

## Stage 6: explain why the projection is the closest parallel vector

The projection formula also solves a small optimization problem. Let $u$ be
a unit vector, write $s=v\cdot u$, and let $r=v-su$. We have already proved
$r\cdot u=0$. Every vector parallel to the guide can be written $cu$ for a
real scalar $c$. Its error relative to $v$ is
$v-cu=r+(s-c)u$. Expand the squared norm using the dot product:

$$\|v-cu\|^2=\|r\|^2+2(s-c)(r\cdot u)+(s-c)^2\|u\|^2
=\|r\|^2+(s-c)^2.$$

The square is nonnegative and vanishes exactly when $c=s$. Therefore $su$
is the unique closest parallel vector in Euclidean distance. This proof
explains why orthogonality is the condition behind least squares: once the
error is perpendicular to the allowable line, moving along that line can
only add a nonnegative squared contribution.

For the mechanical example, choosing the parallel component $c=10\ \mathrm{kN}$
instead of $48/5\ \mathrm{kN}$ would increase squared force error by
$(10-48/5)^2=4/25\ \mathrm{kN^2}$. Its residual would no longer be perpendicular
to the guide. Geometric optimality is useful when approximating a vector by
one available direction, while equilibrium calculations must additionally
satisfy the force and moment balance of the actual mechanism.

## Practice problems

1. **TV-01:** Convert $210^\circ$ to radians and give its exact unit-circle coordinates.
2. **TV-02:** A radius is $3/2\ \mathrm m$ and a rotation is $2\pi/3$. Find its arc length and sector area.
3. **TV-03:** Derive $\sin2\theta=2\sin\theta\cos\theta$ from an addition formula, and evaluate $\sin(\pi/3)$ by setting $\theta=\pi/6$.
4. **TV-04:** Use angle subtraction to find $\cos(\pi/12)$ exactly.
5. **TV-05:** Express $-3\cos(2t)+4\sin(2t)$ as $A\cos(2t-\delta)$ with $A\ge0$ and a correctly located phase.
6. **TV-06:** Find the projection of $v=(5,1)$ onto the line with direction $d=(1,2)$, and check the residual.
7. **TV-07:** A constant force is $(3,4)\ \mathrm N$ and displacement is $(2,-1)\ \mathrm m$. Find the work and explain why multiplying the two magnitudes gives another answer.
8. **TV-08:** Under $x(t)=\operatorname{Re}(\widehat X e^{i\omega t})$, find the phasor for $2\cos(\omega t)-5\sin(\omega t)$ and its magnitude.

## Answers and explanations

1. The angle is $7\pi/6$, with reference angle $\pi/6$ in quadrant III.
Both components are negative, giving $(-\sqrt3/2,-1/2)$.
2. The arc is $(3/2)(2\pi/3)=\pi\ \mathrm m$.
Sector area is $(1/2)(9/4)(2\pi/3)=3\pi/4\ \mathrm{m^2}$.
3. Substitute equal angles into
$\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$.
At $\theta=\pi/6$, the result is $2(1/2)(\sqrt3/2)=\sqrt3/2$.
4. Use $\pi/12=\pi/4-\pi/6$ and the cosine subtraction formula:
$\cos(\pi/12)=(\sqrt6+\sqrt2)/4$. The positive value near one agrees
with the small acute angle.
5. The amplitude is $5$. Choose $\delta\in(\pi/2,\pi)$ with
$\cos\delta=-3/5$ and $\sin\delta=4/5$, for example
$\delta=\pi-\arctan(4/3)$. The quadrant is essential; the principal arctangent
of $4/(-3)$ alone would choose the wrong direction.
6. $v\cdot d=7$ and $d\cdot d=5$, so
$p=(7/5,14/5)$ and $r=(18/5,-9/5)$. Then
$d\cdot r=18/5-18/5=0$ and $p+r=v$.
7. Work is $3\cdot2+4(-1)=2\ \mathrm J$.
The product of magnitudes is $5\sqrt5\ \mathrm J$; the missing cosine of
the angle between the vectors accounts for the difference. They are not parallel.
8. The phasor is $2+5i$, since its imaginary part contributes minus
$5\sin\omega t$ on taking the real part. Its magnitude is $\sqrt{29}$.
Substitution into the declared convention is the safest sign check.

## Reproducible diagrams and verification

[plot_lessons_foundations.py](../../scripts/plot_lessons_foundations.py)
generates both figures with equal scales for geometric coordinates.
[verify_lessons_foundations.py](../../scripts/verify_lessons_foundations.py)
checks the angle-addition values, rotation orthogonality, phase coefficients,
force reconstruction, residual orthogonality, magnitude identity, and work.
Exact identities establish the results; floating-point samples draw their shapes.

## References and further study

OpenStax, [*Precalculus 2e*, unit-circle, trigonometric-identity, and complex-polar entries](https://openstax.org/books/precalculus-2e/pages/index), is a reference route for additional practice. Gilbert Strang's [MIT OpenCourseWare 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) develops projections and orthogonality further. Use the [trigonometry reference](../../subjects/trigonometry/trigonometry.md) for triangle laws and periodic equations; use [linear algebra](../../subjects/linear-algebra/linear-algebra.md) for projections onto higher-dimensional subspaces. This lesson's derivations, examples, and figures are original.
