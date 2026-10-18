# Conics I: from a geometric constraint to an equation

**Lesson ID:** LES-GEO-01  
**Sequence:** First of three guided conic lessons.  
**Prerequisites:** Distance between points, completing a square, quadratic equations, and radians.  
**Learning objectives:** Derive conic equations from distance constraints; recover geometric data from coefficients; distinguish the two hyperbola branches; and explain how a plane section and a focal definition describe the same family.

[Lesson route](../README.md) · [Conic reference](../../subjects/geometry/coordinate-geometry/conic-sections.md) · [Next: tangents and reflection](conics-tangents-and-reflection.md)

## How to use this lesson

Work through the stages in order with paper beside the diagram. Before squaring
an equation, record the signs of both sides. After deriving a quadratic, return
to the original distance statement and check that the quadratic has introduced
no extra points. This habit matters beyond conics: squaring removes sign
information, and a symbolic rearrangement alone does not prove equivalence.

All coordinates are real and orthonormal. Distances and semiaxes have a common
length unit. An eccentricity is dimensionless. Plots sample exact equations;
their finite line segments do not define the loci.

## Stage 1: construct a parabola from equal distances

Place a focus at $F=(p,0)$ and a directrix at $x=-p$, with $p>0$.
For a possible point $P=(x,y)$, the perpendicular foot on the directrix is
$D=(-p,y)$. Equality of the two distances means

$$
\sqrt{(x-p)^2+y^2}=|x+p|.
$$

Both sides are nonnegative, so squaring is reversible. Expanding and cancelling
$x^2+p^2$ gives $y^2=4px$. Conversely this quadratic forces $x\ge0$.
Hence $x+p>0$, and substituting into the squared equality recovers the
original distances. We have proved both directions.

The vertex is $(0,0)$, not the focus. Setting $x=p$ gives $y=\pm2p$:
the chord through the focus perpendicular to the axis has length $4p$.
If $p<0$, the same distance algebra is valid and the parabola opens left.
In that case the chord length is $4|p|$, while $p$ remains signed.

**Worked example 1: recover a physical dimension.** Suppose a cross-section of
a reflector has vertex at the origin, opens upward, and has rim points
$(\pm3,2)$ metres. Write $x^2=4py$. Substitution gives $9=8p$, so
$p=9/8$ m. The focus is $1.125$ m above the vertex. This is an exact
geometric result for the assumed parabola; the finite rim width determines the
aperture, not a different focal law. A focus is not generally halfway between
the vertex and the rim.

## Stage 2: use one focus and one directrix for the whole family

Fix $F=(0,0)$, directrix $x=-d$, $d>0$, and a number $e>0$.
The focus-directrix condition is

$$
\sqrt{x^2+y^2}=e|x+d|.
$$

Squaring is again reversible because the two sides are nonnegative:

$$
(1-e^2)x^2+y^2-2e^2dx-e^2d^2=0. \tag{1}
$$

For $0<e<1$, completing a square yields

$$
\frac{(x-h)^2}{a^2}+\frac{y^2}{b^2}=1,\qquad
h=\frac{e^2d}{1-e^2},\quad
a=\frac{ed}{1-e^2},\quad b=\frac{ed}{\sqrt{1-e^2}}.
$$

Here $c=ae=h$. Thus the left focus $h-c=0$ is the focus we started
with, and $h-a/e=-d$ is the prescribed directrix. For $e=1$,
(1) becomes $y^2=2dx+d^2=2d(x+d/2)$. Its vertex is
$(-d/2,0)$, and its signed focal parameter is $p=d/2$.

For $e>1$, put $q=e^2-1>0$. Equation (1) becomes

$$
\frac{(x-h)^2}{a^2}-\frac{y^2}{b^2}=1,\qquad
h=-\frac{e^2d}{q},\quad a=\frac{ed}{q},\quad
b=\frac{ed}{\sqrt q}.
$$

Now $c=ae=e^2d/q$, and the right focus $h+c=0$ is the
original focus. The absolute distance to the directrix is essential: this
single quadratic contains both hyperbola branches.

![The same focus and directrix with eccentricities one half, one, and three halves; each panel uses equal coordinate scales.](../../assets/figures/lessons-geometry/eccentricity-family.png)

**A useful limitation.** Keeping $d$ fixed while $e\to1$ does not keep
the ellipse center or semimajor axis bounded. It keeps the focus and directrix
fixed. Equation (1) then approaches a parabola on bounded coordinate windows.
These are different statements. A circle has $e=0$ in its two-focus
description, but substituting $e=0$ with a finite fixed directrix into this
construction produces only the focus. A circle is a limiting focal case with
the directrix receding appropriately.

**Worked example 2: do the completion, not just the classification.** Let
$e=1/2$ and $d=3$. Equation (1), multiplied by four, is
$3x^2+4y^2-6x-9=0$. Therefore
$3(x-1)^2+4y^2=12$, or
$(x-1)^2/4+y^2/3=1$. It has center $(1,0)$,
$a=2$, $b=\sqrt3$, and foci $(0,0),(2,0)$.
The associated left directrix is $x=1-a/e=-3$.
The vertex nearer that directrix is $(-1,0)$: its distances are
$1$ to the focus and $2$ to the directrix, as required.

## Stage 3: derive the ellipse's constant distance sum

Choose $a>c>0$, foci $F_-=(-c,0)$, $F_+=(c,0)$, and write
$r_\pm=|P-F_\pm|$. Assume $r_-+r_+=2a$.
Because
$r_-^2-r_+^2=4cx$, multiplying sum and difference gives

$$
r_--r_+=\frac{2cx}{a},\qquad
r_-=a+\frac{cx}{a},\qquad r_+=a-\frac{cx}{a}.
$$

Square the expression for $r_+$ and compare it with
$(x-c)^2+y^2$. The terms linear in $x$ cancel:

$$
x^2+y^2+c^2=a^2+\frac{c^2x^2}{a^2}.
$$

Set $b^2=a^2-c^2>0$. Rearranging gives
$x^2/a^2+y^2/b^2=1$.

For the converse, the standard equation forces $|x|\le a$, and thus
$a\pm cx/a\ge a-c>0$. Squaring shows that these expressions
are the respective distances, with the positive signs justified. Their sum is
$2a$. The sign argument finishes the equivalence that a one-way expansion
would leave incomplete. If $c=0$, the same result reduces to a circle.
If $c=a$, the minor semiaxis vanishes and the distance-sum locus is the
line segment joining the foci; it is not a nondegenerate ellipse.

**Worked example 3: one point, two checks.** On
$x^2/25+y^2/9=1$, take $P=(3,12/5)$.
The foci are $(-4,0),(4,0)$. The distances are $37/5$
and $13/5$, whose sum is $10=2a$. For the right focus and its
directrix $x=25/4$, the point-to-line distance is $13/4$.
The ratio $(13/5)/(13/4)=4/5$ equals $e=c/a$.
The sum and ratio descriptions give the same ellipse but use different data.

## Stage 4: derive the hyperbola and keep both branches

Let $c>a>0$, and use the same focal coordinates. On the right branch,
$r_--r_+=2a$. Combining this with
$r_-^2-r_+^2=4cx$ gives

$$
r_-+r_+=\frac{2cx}{a},\quad
r_-=\frac{cx}{a}+a,\quad r_+=\frac{cx}{a}-a.
$$

The sum is positive, so $x>0$. Squaring either distance and setting
$b^2=c^2-a^2>0$ gives $x^2/a^2-y^2/b^2=1$.
On that quadratic's right branch $x\ge a$, so
$cx/a-a\ge c-a>0$, making the converse valid.
On the left branch $x\le-a$, the roles of the two distances reverse.
Consequently the full locus is
$|r_--r_+|=2a$, with both branches included.

The assumptions $a<c$ also follow from the reverse triangle inequality:
$|r_--r_+|\le |F_--F_+|=2c$. Equality $a=c$
is a degenerate limiting case, not a hyperbola with positive $b$.
For $|x|$ large,
$y/x\to\pm b/a$, which explains the asymptote slopes rather than
merely listing them. The error between the upper right branch and its
asymptote decreases like a constant divided by $x$, since

$$
\frac{b}{a}x-b\sqrt{x^2/a^2-1}
=\frac{b}{x/a+\sqrt{x^2/a^2-1}}\quad(x\ge a).
$$

**Worked example 4: a time-difference locus.** Two ideal receivers are at
$(\pm5,0)$ km. A signal travels at a constant speed $v$ km/s,
and the absolute difference in arrival times is $6/v$ s. The difference
in path lengths is $6$ km. Thus $a=3$, $c=5$,
$b=4$, and the location locus is $x^2/9-y^2/16=1$.
Without the sign of the time difference, neither branch can be discarded.
This assumes straight paths, simultaneous emission, and a common speed.

## Stage 5: connect the loci to cutting a cone

For the double cone $z^2=x^2+y^2$, intersect the plane
$z=mx+1$, $m\ge0$. Substitution gives the plane curve

$$
(1-m^2)x^2+y^2-2mx-1=0. \tag{2}
$$

It is an ellipse for $0\le m<1$, a parabola for $m=1$,
and a hyperbola for $m>1$. At $m=0$ the section is a circle.
The plane never passes through the vertex, so these sections are
nondegenerate. A plane through the vertex requires a separate degeneracy check.

Equation (2) is expressed using the ambient $x,y$ coordinates. These are
not orthonormal coordinates for measuring lengths within a sloping plane:
along a change $dx$, $dz=m\,dx$, so the squared line element is
$(1+m^2)dx^2+dy^2$. For actual in-plane semiaxes, first complete
the square in $x$ and then use the scaled horizontal coordinate
$s=\sqrt{1+m^2}(x-m/(1-m^2))$ when $m\ne1$.
Classification survives the projection, but eccentricity and lengths must
use the plane's Euclidean metric.

![A double cone cut by four planes; highlighted intersections are computed from the cone and plane equations, with the slope-one plane producing a parabola.](../../assets/figures/lessons-geometry/cone-sections.png)

**Checkpoint.** For $m=1/2$, (2) becomes
$(3/4)(x-2/3)^2+y^2=4/3$.
After converting to the plane coordinate $s=\sqrt5(x-2/3)/2$,
the squared semiaxes are $20/9$ and $4/3$. Reading them
directly from the unscaled $x,y$ equation would give the wrong lengths.

## Stage 6: choose a parameter that covers the intended points

An implicit equation describes a whole set at once. A parameterization gives a
way to move through that set, but its domain determines which points it reaches.
For an ellipse, $(x,y)=(a\cos t,b\sin t)$, $0\le t<2\pi$,
traces the boundary once. The parameter is an auxiliary angle on the unit
circle before stretching; it is generally not the physical angle of the
ellipse point measured from its center.

There is also an exact rational parameterization. Intersect the unit circle
with the line $v=t(u+1)$ through $(-1,0)$. Substitution gives
$(u+1)[(1+t^2)u+t^2-1]=0$. The second intersection is

$$
u=\frac{1-t^2}{1+t^2},\qquad v=\frac{2t}{1+t^2}.
$$

Multiplying coordinates by $a,b$ gives an ellipse point for every real
$t$. It reaches every boundary point except $(-a,0)$; that point
is obtained as a limit when $|t|\to\infty$. A complete description
must explicitly include it. For $a=5,b=3,t=1/2$, this gives
$(3,12/5)$ with no trigonometric approximation.

For a parabola, $(x,y)=(pt^2,2pt)$ with $t\in\mathbb R$
does cover every point, since $t=y/(2p)$ is uniquely recoverable.
For a hyperbola use $(a\cosh t,b\sinh t)$ for the right branch
and $(-a\cosh t,b\sinh t)$ for the left. The identity
$\cosh^2t-\sinh^2t=1$ verifies the equation, and monotonicity of
$\sinh$ supplies every possible ordinate on each branch.
A single right-branch formula does not represent the entire hyperbola.

## Practice problems

1. Derive the equation for focus $(0,-2)$ and directrix $y=2$. Find its latus rectum length.
2. With focus at the origin, directrix $x=-3$, and $e=2$, find the center, standard equation, and other focus.
3. An ellipse has foci $(\pm3,0)$ and distance sum $10$. Find its equation and both directrices.
4. A hyperbola has foci $(0,\pm5)$ and absolute distance difference $8$. Find its equation and asymptotes.
5. Starting from a circle of radius $R>0$, explain why a finite directrix with eccentricity zero cannot define the circle.
6. For focus at the origin and directrix $x=-d$, use $x=r\cos\theta$, $r\ge0$, to derive both possible polar branches.
7. For the cone section $z=x/2+1$, find the actual in-plane eccentricity from the checkpoint semiaxes.
8. Show that a point whose distances to $(\pm c,0)$, $c>0$, sum to $2c$ lies on the segment between the foci.

## Answers and explanations

1. Equality $\sqrt{x^2+(y+2)^2}=|y-2|$ gives
   $x^2=-8y$. Here $p=-2$, vertex $(0,0)$, and latus rectum length $8$.
2. $x^2+y^2=4(x+3)^2$ gives
   $(x+4)^2/4-y^2/12=1$. The center is $(-4,0)$,
   $a=2$, $c=4$, and the other focus is $(-8,0)$.
3. $a=5,c=3,b=4$, so $x^2/25+y^2/16=1$.
   Since $e=3/5$, the directrices are $x=\pm25/3$.
4. $a=4,c=5,b=3$, with transverse axis vertical:
   $y^2/16-x^2/9=1$, and $y=\pm4x/3$.
5. With a finite directrix, $e\,d(P,\text{line})=0$ when $e=0$,
   so equality forces $P=F$. For the ellipse's circle limit at fixed radius,
   $a/e\to\infty$; the directrix cannot remain finite.
6. The equation is $r=e|r\cos\theta+d|$. On the side
   $x>-d$, $r=ed/(1-e\cos\theta)$ with positive denominator.
   On $x<-d$, $r=-ed/(1+e\cos\theta)$, possible only when
   $1+e\cos\theta<0$. The second region occurs only for $e>1$.
   There are no finite locus points on the directrix.
7. $a^2=20/9,b^2=4/3$, so $e^2=1-b^2/a^2=2/5$
   and $e=\sqrt{2/5}$. This differs from the projected curve's
   apparent eccentricity.
8. The triangle inequality is an equality:
   $|F_--P|+|P-F_+|=|F_--F_+|$. Equality requires the two
   displacement vectors along the path to point in the same direction,
   so $P$ is on the joining segment. Conversely every segment point
   has the required sum.

## Further connections and review

The next lesson differentiates these distance constraints to obtain optical
reflection laws. The [matrix lesson](conics-matrices-and-classification.md)
explains why the discriminant alone cannot establish that a real conic exists.
For further reading, the [conic reference chapter](../../subjects/geometry/coordinate-geometry/conic-sections.md#references-and-recommended-reading)
collects textbook sources. These derivations are written out here rather than
requiring an external source to supply a missing algebraic step.

Generate the diagrams with
<code>python scripts/plot_lessons_geometry.py</code>; run
<code>python scripts/verify_lessons_geometry.py</code> for the encoded exact
examples. Before marking this lesson independent, derive the ellipse and
hyperbola converses without checking the page and explain why the plane
section needs a metric correction.
