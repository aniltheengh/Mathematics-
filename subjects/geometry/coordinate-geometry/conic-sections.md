# Conic sections: circles, ellipses, parabolas, and hyperbolas

**Topic ID:** GEO-CONIC-001  
**Classification:** Geometry → analytic geometry → conic sections  
**Level:** Algebra through early university mathematics  
**Content status:** Written; symbolic and graphical checks accompany this chapter.  
**Learner mastery:** Unassessed.

[Home](../../../README.md) · [Contents](../../../CONTENTS.md) · [Cartesian plane](cartesian-plane.md)

## Prerequisites

Review [distance, lines, and completing squares](cartesian-plane.md), quadratic
equations, square roots, and basic trigonometry. The matrix classification is an
extension; the elementary standard forms do not require a matrix course.
Coordinates below are real, the plane is Euclidean, and the axes are orthonormal
with the same length unit. A conic's equation is exact; its drawn curve is a finite
sampling of that equation.

## Definition

**Definition.** A real plane conic is the locus of a quadratic equation

$$
Ax^2+Bxy+Cy^2+Dx+Ey+F=0,
$$

where the real coefficients $A,B,C$ are not all zero. Such a locus can be a
circle, ellipse, parabola, hyperbola, or a degenerate set such as lines, a point,
or the empty set. A plane cutting a double circular cone gives the familiar
nondegenerate shapes; passing through its vertex can produce degeneracy.

**Focal definitions.** A circle has a constant distance from one center. An
ellipse has a constant **sum** of distances from two foci. A hyperbola has a
constant **absolute difference** of distances from two foci. A parabola has equal
distances from one focus and one line called a directrix. These conditions are
geometric: translating or rotating the frame changes the equation but preserves
the curve's lengths and angles.

## Intuitive explanation

An ellipse is the boundary traced by a taut string around two fixed pins. A
hyperbola compares which focus is nearer, with a fixed difference in distances.
A parabola balances point-distance against line-distance. A circle is the
equal-distance boundary around one point. The distinction concerns the defining
constraint, not how stretched a curve appears on a screen.

![Four exact example loci: circle, ellipse, parabola, and hyperbola, each drawn with equal coordinate scales.](../../../assets/figures/geometry/conics-overview.png)

The parabola is not half an ellipse, and the two branches of a hyperbola are not
connected across the gap. An unequal plotting scale can conceal these facts.

## Mathematical notation

Write $X=x-h$ and $Y=y-k$ for coordinates relative to a center or vertex $(h,k)$.
For an ellipse, $a\ge b>0$ are the major and minor semiaxis lengths and
$c=\sqrt{a^2-b^2}$ is focal distance. For a hyperbola, $a,b>0$ are transverse
and conjugate semiaxis parameters and $c=\sqrt{a^2+b^2}$. Thus the symbol $c$
has the same geometric role but a different relation in the two families.
For a parabola, $p\ne0$ is a **signed** focal parameter. Eccentricity is $e$;
$t$ and $u$ are real parameters. All angles are in radians.

## Fundamental properties

### Circle

$X^2+Y^2=r^2$ with $r>0$ has center $(h,k)$ and radius $r$. A circle is an
ellipse with $a=b=r$, coincident foci, and $e=0$. Its circumference is $2\pi r$
and its enclosed area is $\pi r^2$.

### Ellipse

For horizontal major axis,

$$
\frac{X^2}{a^2}+\frac{Y^2}{b^2}=1,\qquad a\ge b>0.
$$

Its major vertices are $(h\pm a,k)$, minor vertices $(h,k\pm b)$, and foci
$(h\pm c,k)$, where $c^2=a^2-b^2$. Every point satisfies
$d(P,F_1)+d(P,F_2)=2a$. Its eccentricity is $e=c/a\in[0,1)$ and area is
$\pi ab$. For $a>b$, directrices are $x=h\pm a/e$. A circle has no finite
directrix under this formula: dividing by $e=0$ is invalid.

For a vertical major axis interchange $X$ and $Y$: $X^2/b^2+Y^2/a^2=1$,
with foci $(h,k\pm c)$ and directrices $y=k\pm a/e$.

### Parabola

$$
Y^2=4pX,\qquad p\ne0
$$

has vertex $(h,k)$, focus $(h+p,k)$, directrix $x=h-p$, and axis $y=k$.
It opens right for $p>0$ and left for $p<0$. Its eccentricity is $1$.
The corresponding vertical form $X^2=4pY$ has focus $(h,k+p)$ and directrix
$y=k-p$. A parabola has no finite center or semimajor axis. Its latus rectum,
the chord through the focus perpendicular to its axis, has length $4|p|$.

### Hyperbola

$$
\frac{X^2}{a^2}-\frac{Y^2}{b^2}=1,\qquad a,b>0
$$

has vertices $(h\pm a,k)$, foci $(h\pm c,k)$ with $c^2=a^2+b^2$, and
$|d(P,F_1)-d(P,F_2)|=2a$. Its asymptotes are $Y=\pm(b/a)X$,
eccentricity $e=c/a>1$, and directrices $x=h\pm a/e$. For a vertical transverse
axis, use $Y^2/a^2-X^2/b^2=1$ and asymptotes $Y=\pm(a/b)X$.
The parameter $b$ is not a vertical intercept: this horizontal hyperbola never
meets $X=0$.

## Important formulas and identities

### Exact parameterizations

| Curve | Parameterization | Domain |
| --- | --- | --- |
| Circle | $X=r\cos t$, $Y=r\sin t$ | $0\le t<2\pi$ |
| Ellipse | $X=a\cos t$, $Y=b\sin t$ | $0\le t<2\pi$ |
| Horizontal parabola | $X=pt^2$, $Y=2pt$ | $t\in\mathbb R$, $p\ne0$ |
| Right hyperbola branch | $X=a\cosh u$, $Y=b\sinh u$ | $u\in\mathbb R$ |
| Left hyperbola branch | $X=-a\cosh u$, $Y=b\sinh u$ | $u\in\mathbb R$ |

Here $\cosh u=(e^u+e^{-u})/2$ and $\sinh u=(e^u-e^{-u})/2$, so
$\cosh^2u-\sinh^2u=1$. Ellipse parameter $t$ is generally **not** the polar
angle of its radius vector. These parameterizations are particularly reliable
for graphs because they avoid square-root branch omissions.

### Tangents

At a point $(x_0,y_0)$ **on** the respective curve, let $X_0=x_0-h$,
$Y_0=y_0-k$. Tangents are

$$
\frac{X_0X}{a^2}+\frac{Y_0Y}{b^2}=1\quad\text{(ellipse)},
\qquad
\frac{X_0X}{a^2}-\frac{Y_0Y}{b^2}=1\quad\text{(hyperbola)},
$$

$$
Y_0Y=2p(X+X_0)\quad\text{for }Y^2=4pX.
$$

The point must satisfy the conic equation; substituting an arbitrary external
point into these formulas does not give its tangent. For a line-conic
intersection, substitute a parameterization of the line into the conic. The
resulting quadratic discriminant distinguishes two, one, or zero real roots
when the quadratic coefficient is nonzero; degenerate reductions require
separate checking.

### Focus-directrix and polar description

For a focus $F$ and directrix $L$, $d(P,F)=e\,d(P,L)$ gives an ellipse for
$0<e<1$, parabola for $e=1$, and hyperbola for $e>1$. Place the focus at the
polar origin and the directrix at $x=d>0$, with polar radius $r\ge0$ and angle
$\theta$. The full condition is

$$
r=e|r\cos\theta-d|.
$$

On the side $r\cos\theta<d$, it becomes

$$
r=\frac{ed}{1+e\cos\theta},\qquad 1+e\cos\theta>0.
$$

For $e>1$, the other side gives $r=ed/(e\cos\theta-1)$ where
$e\cos\theta>1$. This explicit sign distinction matters when using only
nonnegative radii; some books use signed radii to combine branches differently.
The numerator $ed$ is often called the semilatus rectum for this orientation.

### Rotation and general quadratic classification

Under $x=h+u\cos\alpha-v\sin\alpha$ and
$y=k+u\sin\alpha+v\cos\alpha$, the mixed quadratic coefficient becomes
$(C-A)\sin2\alpha+B\cos2\alpha$. Choose a rotation making it zero. If
$A\ne C$, $\tan2\alpha=B/(A-C)$ is useful, but angles require quadrant care;
if $A=C$ and $B\ne0$, a rotation by $\pi/4$ works.

The symmetric quadratic matrix and coefficient vector are

$$
Q=\begin{pmatrix}A&B/2\\B/2&C\end{pmatrix},\qquad
\mathbf d=\begin{pmatrix}D\\E\end{pmatrix}.
$$

An orthogonal eigenbasis diagonalizes $Q$. If $Q$ is invertible, the center is
$-Q^{-1}\mathbf d/2$; then complete squares in principal coordinates.
The invariant $B^2-4AC=-4\det Q$ indicates a **family**, not real existence:

| Sign | Possible real loci after further checking |
| --- | --- |
| Negative | Ellipse/circle, one point, or empty set |
| Positive | Hyperbola or two intersecting lines |
| Zero | Parabola, parallel lines, double line, or empty set |

The homogeneous determinant
$\det\begin{pmatrix}A&B/2&D/2\\B/2&C&E/2\\D/2&E/2&F\end{pmatrix}$
vanishes for algebraic degeneracy. A nonzero determinant alone does not guarantee
real points: $x^2+y^2+1=0$ is nondegenerate algebraically but empty over $\mathbb R$.

![Degenerate real loci: one point for x²+y²=0, intersecting lines for x²-y²=0, parallel lines for x²=4, and no real points for x²+y²=-1.](../../../assets/figures/geometry/degenerate-conics.png)

## Derivations and proofs

### Parabola from equal distances

Put the vertex at the origin, focus $(p,0)$, directrix $x=-p$, with $p\ne0$.
The definition is $\sqrt{(x-p)^2+y^2}=|x+p|$. Both sides are nonnegative, so
squaring is reversible. Expanding and cancelling gives $y^2=4px$. Conversely,
that equation implies equality of the squared nonnegative distances, hence of
the distances. No extraneous real points are introduced.

### Ellipse focal sum

For $x=a\cos t$, $y=b\sin t$, and $c^2=a^2-b^2$,

$$
(x-c)^2+y^2=(a-c\cos t)^2,\qquad
(x+c)^2+y^2=(a+c\cos t)^2.
$$

Since $a>c\ge0$, both square roots are positive and their sum is $2a$.
Conversely, from $d_++d_-=2a$ and $d_-^2-d_+^2=4cx$, obtain
$d_+=a-cx/a$. Substitution into $d_+^2=(x-c)^2+y^2$ gives
$x^2/a^2+y^2/b^2=1$. The standard form also forces $|x|\le a$, ensuring the
distance expressions used in the reverse argument remain nonnegative.

### Hyperbola focal difference

For the right branch $x=a\cosh u$, $y=b\sinh u$, with $c^2=a^2+b^2$,
direct expansion gives distances to $(-c,0)$ and $(c,0)$ equal to
$c\cosh u+a$ and $c\cosh u-a$. These are positive since $c>a$. Their difference
is $2a$. Reflection gives the other branch and the absolute difference condition.
Conversely, separating the sign of the distance difference and eliminating the
two roots yields $x^2/a^2-y^2/b^2=1$; the appropriate branch has $x\ge a$ or
$x\le-a$. The parameterization covers both complete branches, since every
$x\ge a$ is $a\cosh u$ for an appropriate magnitude of $u$ and either sign of $y$.

### Tangent and area derivations

For the ellipse function $f(X,Y)=X^2/a^2+Y^2/b^2-1$, its nonzero normal at
$(X_0,Y_0)$ is $(2X_0/a^2,2Y_0/b^2)$. The line normal equation, using
$f(X_0,Y_0)=0$, simplifies to the stated tangent. Replacing the plus by minus
gives the hyperbola formula. For the parabola, the normal of $Y^2-4pX$ is
$(-4p,2Y)$, which never vanishes when $p\ne0$; its line equation gives the
parabola tangent even at its vertex, where a slope calculation would divide by zero.

The linear scaling $(s,t)\mapsto(as,bt)$ sends the unit disk to the ellipse's
interior and multiplies areas by determinant $ab>0$. Its area is therefore
$ab\pi$. This is also a direct application of the change-of-variables theorem.

## Worked examples

### Complete an ellipse square

For $9x^2+4y^2-36x+8y+4=0$, complete each square:
$9(x-2)^2+4(y+1)^2=36$. Dividing by $36$ gives
$(x-2)^2/4+(y+1)^2/9=1$. The major axis is vertical, center $(2,-1)$,
$a=3$, $b=2$, $c=\sqrt5$. Foci are $(2,-1\pm\sqrt5)$, major vertices
$(2,2)$ and $(2,-4)$, and area $6\pi$. The eccentricity is $\sqrt5/3$.

### Locate a parabola's focus

For $y^2-6y-8x+17=0$, $(y-3)^2=8(x-1)$. Thus $4p=8$ and $p=2$:
vertex $(1,3)$, focus $(3,3)$, directrix $x=-1$, opening right. At $(3,7)$,
both squared focus-distance and squared directrix-distance are $16$, checking
the construction.

### Hyperbola and tangent

For $x^2/9-y^2/4=1$, $a=3$, $b=2$, $c=\sqrt{13}$ and asymptotes
$y=\pm2x/3$. The point $(5,8/3)$ is on it because $25/9-16/9=1$.
The tangent is $5x/9-(8/3)y/4=1$, or $5x-6y=9$. Substitution of the point
gives $25-16=9$. The slope is $5/6$, agreeing with implicit differentiation
$y'=4x/(9y)$ there.

### A rotated ellipse

For $5x^2-6xy+5y^2=8$, set
$x=(u-v)/\sqrt2$ and $y=(u+v)/\sqrt2$. Expansion gives
$2u^2+8v^2=8$, hence $u^2/4+v^2=1$. The semiaxes are $2,1$, area $2\pi$,
and its major axis lies along $x=y$. The vertices are $(\pm\sqrt2,\pm\sqrt2)$
with paired signs. The foci are $(\pm\sqrt{3/2},\pm\sqrt{3/2})$.

![The rotated ellipse 5x²-6xy+5y²=8 with principal axes u and v; the major axis is x=y.](../../../assets/figures/geometry/rotated-ellipse.png)

### Intersect an ellipse and a line

For $x^2/25+y^2/9=1$ and $y=12/5$, substitution gives
$x^2/25=1-16/25=9/25$, so $x=\pm3$. At $P=(3,12/5)$, distances to foci
$(4,0)$ and $(-4,0)$ are $13/5$ and $37/5$, summing to $10=2a$.
The exact radicals simplify because $1+(12/5)^2=169/25$ and
$49+(12/5)^2=1369/25$.

![Ellipse x²/25+y²/9=1, foci at plus and minus 4, and point (3,12/5) with exact focal distances 13/5 and 37/5.](../../../assets/figures/geometry/ellipse-foci.png)

## Practice problems

1. For $(x+1)^2/16+(y-2)^2/9=1$, find center, vertices, foci, eccentricity,
   directrices, and area.
2. For $(x-2)^2=-12(y+1)$, find vertex, focus, directrix, and opening direction.
3. Rewrite $4x^2-9y^2-16x-18y-29=0$ in standard form and find its asymptotes.
4. Find the tangent to $y^2=8x$ at $(2,4)$; check the line's intersection multiplicity.
5. Classify $x^2+y^2=0$, $x^2-y^2=0$, $x^2=4$, and $x^2+y^2=-1$ over the reals.
6. For $e=1/2$ and directrix $x=6$, find the focus-origin polar equation and its
   radius at $\theta=\pi/2$.
7. Derive the equation of the locus having focus $(2,0)$, directrix $x=-2$,
   and eccentricity one.
8. A symmetric parabola has full aperture width $4$ m and depth $1$ m. Find its
   focal distance from the vertex and write its equation with horizontal axis.

## Answers and explanations

1. Center $(-1,2)$; $a=4,b=3,c=\sqrt7$. Major vertices $(-5,2),(3,2)$;
   minor vertices $(-1,-1),(-1,5)$; foci $(-1\pm\sqrt7,2)$;
   $e=\sqrt7/4$; directrices $x=-1\pm16/\sqrt7$; area $12\pi$.
2. $4p=-12$, so $p=-3$. Vertex $(2,-1)$, focus $(2,-4)$, directrix $y=2$;
   the parabola opens downward, not left, because the squared coordinate is $x$.
3. Completing squares yields $4(x-2)^2-9(y+1)^2=36$, hence
   $(x-2)^2/9-(y+1)^2/4=1$. Asymptotes: $y+1=\pm(2/3)(x-2)$.
4. $p=2$ and the tangent formula gives $4y=4(x+2)$, or $y=x+2$.
   Substitution into $y^2=8x$ gives $(x+2)^2=8x$, hence $(x-2)^2=0$;
   there is one real contact point, a double root.
5. Respectively: one point $(0,0)$; lines $y=x$ and $y=-x$; parallel lines
   $x=2$ and $x=-2$; empty real set. The discriminant alone cannot distinguish all these.
6. $r=3/(1+\tfrac12\cos\theta)$, always positive; at $\pi/2$, $r=3$.
7. $\sqrt{(x-2)^2+y^2}=|x+2|$; reversible squaring gives $y^2=8x$.
8. With $y^2=4px$, the rim has $(x,|y|)=(1,2)$ in metres, so
   $4=4p$ and $p=1$ m. In numerical metre coordinates the equation is $y^2=4x$;
   dimensionally its coefficient $4p$ is a length.

## Common mistakes and misconceptions

Never use $c^2=a^2+b^2$ for an ellipse or $c^2=a^2-b^2$ for a hyperbola.
Read $a^2,b^2$ from denominators only after normalizing the right side to one.
For ellipses $a$ denotes the larger semiaxis; for hyperbolas $a$ belongs to the
positive transverse term regardless of relative denominator size. A parabola's
coefficient is $4p$, not $p$. The hyperbola's asymptotes pass through its center,
and their slopes depend on orientation. Always retain both hyperbola branches
and both square-root signs when solving for intersections.

![Hyperbola x²/9-y²/4=1 with both branches, vertices, foci and its two asymptotes.](../../../assets/figures/geometry/hyperbola-asymptotes.png)

## Connections to other mathematics

Quadratic forms and orthogonal diagonalization explain rotations. Gradients
give tangents and normals. Coordinate changes give ellipse area. Polar conics
connect geometry to orbital models; inverse-square central-force motion produces
conic trajectories under the usual ideal two-body assumptions. Projective geometry
unifies nondegenerate conics; affine maps preserve their algebraic family while
not generally preserving lengths or eccentricity. See the [subject navigation](../../../INDEX.md).

## Applications

The aperture calculation above is useful for an ideal parabolic reflector's
cross-section. Parallel rays reflect through its focus in geometric optics;
this statement assumes a perfectly reflecting exact parabola and no diffraction.
A parabola of revolution gives a dish, while extruding the planar parabola gives
a trough. Elliptic trajectories and elliptical cross-sections, hyperbolic
time-difference loci, and quadratic machine-tool profiles are other uses.

![Parabola y²=4x, focus (1,0), directrix x=-1, and ideal horizontal incoming rays reflected toward the focus.](../../../assets/figures/geometry/parabola-focus.png)

## Optional computational examples

[The geometry plotting script](../../../scripts/plot_geometry.py) uses the exact
parameterizations above and separate hyperbola branches. The [verification script](../../../scripts/verify_geometry.py)
substitutes parameters into equations, checks focus distances, diagonalizes the
rotated quadratic, and verifies the tangent's repeated root. Finite-precision
samples illustrate exact loci; they are not new definitions of the curves.

## References and recommended reading

Primary reading: OpenStax, *College Algebra 2e*,
[ellipses](https://openstax.org/books/college-algebra-2e/pages/8-1-the-ellipse),
[hyperbolas](https://openstax.org/books/college-algebra-2e/pages/8-2-the-hyperbola),
and [parabolas](https://openstax.org/books/college-algebra-2e/pages/8-3-the-parabola).
For rotated equations, see OpenStax, *Algebra and Trigonometry 2e*,
[Rotation of Axes](https://openstax.org/books/algebra-and-trigonometry-2e/pages/12-4-rotation-of-axes).
The explanations, parameter checks, examples, and exercises here are original.

## Revision and mastery status

You should be able to identify orientation, complete squares, distinguish all
four families, find foci/directrices, draw axes and asymptotes, check a tangent,
and reject an empty real locus. Attempt problems 1–8 without notes, then change
one numerical parameter and check the resulting curve by substitution. This
chapter's existence does not assign personal mastery; use the revision tracker.
