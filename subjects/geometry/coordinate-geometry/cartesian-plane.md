# Cartesian plane: points, lines, and circles

**Topic ID:** GEO-CG-001  
**Classification:** Geometry → analytic geometry → Cartesian coordinate geometry  
**Level:** Elementary to early university revision  
**Content status:** Written; see the [verification record](../../../docs/verification.md).  
**Learner mastery:** Unassessed; record your evidence in the [tracker](../../../learning/progress.csv).

[Home](../../../README.md) · [Navigation](../../../INDEX.md) · [Geometry](../overview.md)

This chapter translates positions into equations and equations back into shapes.
Its scope is two-dimensional Euclidean geometry: points, segment lengths,
midpoints, straight lines, their intersections, circles, and distances to lines.
Continue with [conic sections](conic-sections.md) for ellipses, parabolas, and
hyperbolas, or [coordinate systems](coordinate-systems-and-transformations.md)
for polar, spatial, and projective descriptions.

## Prerequisites

You need signed real numbers, fractions, squaring, square roots, substitution,
linear equations, simultaneous equations, and the Pythagorean theorem. Completing
the square is explained locally below. No calculus, vectors course, or programming
is required. Review prerequisite subjects in the [subject plan](../../../CONTENTS.md)
using the [reading guide](../../../references/README.md) when needed.

**Quick check:** Can you solve $3x=9$, simplify $\sqrt{36+64}$, and expand
$(x-2)^2$? The answers are $x=3$, $10$, and $x^2-4x+4$.

## Definitions and domain

**Assumption.** Work in a flat Euclidean plane with perpendicular coordinate axes,
a common origin, and the same unit of length along each axis. The axes' unit
directions are orthogonal and have unit length: this is an **orthonormal Cartesian
frame**. Coordinates are real. Unless a physical unit is specified, a length is
reported in coordinate units.

**Definition — Cartesian point.** A point $P=(x,y)$ is specified by the signed
coordinate $x$ along the first axis and $y$ along the second. The plane is
$\mathbb{R}^2=\{(x,y):x,y\in\mathbb{R}\}$. An ordered pair matters: $(2,5)$
and $(5,2)$ generally locate different points.

**Definition — displacement.** For $A=(x_1,y_1)$ and $B=(x_2,y_2)$, define
$\Delta x=x_2-x_1$ and $\Delta y=y_2-y_1$. These signed changes are not the
nonnegative length between the points.

**Definition — line.** A line is a set of points satisfying
$ax+by+c=0$, where $a,b,c\in\mathbb{R}$ and $(a,b)\ne(0,0)$.
Multiplying all three coefficients by the same nonzero constant gives the same line.

**Definition — segment and midpoint.** The closed segment from $A$ to $B$ consists
of $(x_1+t\Delta x,y_1+t\Delta y)$ for $0\le t\le1$. Its midpoint has $t=1/2$.
If $A=B$, the segment is a single point and has length zero.

**Definition — circle.** A circle with center $C=(h,k)$ and radius $r>0$ is the
set of points at Euclidean distance $r$ from $C$. A radius of zero describes a
single point, treated here as a degenerate case rather than a circle.

**Definition — locus.** A locus is the set of all points satisfying a stated
condition, such as having a fixed distance from a center.

## Intuition

A coordinate frame is a measuring convention. The pair $(x,y)$ records where
you stand relative to its origin and directions. An equation such as $y=2x+1$
selects every position whose coordinates obey a rule. A geometric problem can
therefore become an algebra problem, and its answer must still make geometric sense.

For distance, imagine horizontal and vertical legs of a right triangle joining
two points. For a midpoint, move halfway through both coordinate changes.
For a circle, hold a compass opening fixed while turning about its center.
These are useful pictures; the proofs below supply the arguments.

![Points A(1,2), B(7,10), and midpoint M(4,6); a right triangle has legs 6 and 8 and hypotenuse 10.](../../../assets/figures/distance-midpoint.png)

Figure 1. Equal horizontal and vertical scales preserve geometric lengths and
angles. The dashed legs measure displacement components, not an alternative
definition of straight-line distance.

## Notation

| Symbol | Meaning and restrictions |
| --- | --- |
| $A=(x_1,y_1)$, $B=(x_2,y_2)$ | Fixed points with real coordinates |
| $P=(x,y)$ | A variable or specified point, as stated locally |
| $\Delta x$, $\Delta y$ | Signed coordinate changes from $A$ to $B$ |
| $d(A,B)$ | Nonnegative Euclidean distance |
| $M$ | Midpoint of a segment |
| $m$, $\beta$ | Slope and vertical intercept of a nonvertical line |
| $a,b,c$ | Implicit line coefficients, with $a^2+b^2>0$ |
| $h,k,r$ | Circle center coordinates and positive radius |
| $t$ | Real parameter; $0\le t\le1$ for a segment |
| $\approx$ | Approximate equality after rounding |

The symbol $b$ in an implicit line coefficient is not the vertical intercept;
this chapter uses $\beta$ for that intercept. See the [general notation guide](../../../indexes/notation.md).

## Fundamental properties

1. Distances are nonnegative, symmetric, and zero exactly when the points coincide.
2. A common translation or rigid rotation of the frame preserves distances.
   An unequal rescaling of axes generally does not preserve the simple sum-of-squares formula.
3. Two **distinct** points determine exactly one line. One point alone does not.
4. Every nonvertical line can be written $y=mx+\beta$. A vertical line $x=q$
   cannot be written this way for a real finite slope.
5. Two distinct lines are parallel or have exactly one intersection. Equivalent
   line equations describe a coincident line with infinitely many shared points.
6. A circle is symmetric about every line through its center. Its equation is
   unchanged by a rigid rotation about its center.

The length assertions follow from Euclidean geometry. The algebraic line
assertions are justified by the forms and determinant test below.

## Formulas and conditions

### Distance and midpoint

For all $A,B\in\mathbb{R}^2$ in the assumed frame,

$$
d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2},\qquad
M=\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right).
$$

The square root is the nonnegative root. Both formulas include $A=B$.
If coordinates are millimetres, distance is millimetres and squared distance is
square millimetres.

### Lines

If $x_2\ne x_1$, the slope and point-slope form are

$$
m=\frac{y_2-y_1}{x_2-x_1},\qquad y-y_1=m(x-x_1).
$$

If $x_2=x_1$ and $y_2\ne y_1$, the line is $x=x_1$. A form covering both
vertical and nonvertical lines through distinct $A,B$ is

$$
(y_2-y_1)(x-x_1)-(x_2-x_1)(y-y_1)=0.
$$

If $A=B$, this reduces to $0=0$ and does **not** determine a line.
For $ax+by+c=0$ with $b\ne0$, $m=-a/b$ and $\beta=-c/b$.

For two valid lines $a_1x+b_1y+c_1=0$ and $a_2x+b_2y+c_2=0$, define
$D=a_1b_2-a_2b_1$. If $D\ne0$, their unique intersection is

$$
x=\frac{b_1c_2-b_2c_1}{D},\qquad
y=\frac{c_1a_2-c_2a_1}{D}.
$$

If $D=0$, check whether the full coefficient triples are proportional.
Proportional triples give the same line; otherwise the lines are parallel and
distinct. This test includes vertical lines.

Two valid implicit lines are perpendicular exactly when
$a_1a_2+b_1b_2=0$. For two nonvertical lines this becomes $m_1m_2=-1$.
A horizontal line and a vertical line are perpendicular, though the slope product
cannot be formed. Equal slopes indicate parallel or coincident nonvertical lines.

### Circles

For $r>0$, the circle equation is

$$
(x-h)^2+(y-k)^2=r^2.
$$

If $u,v,w$ are real constants, completing the square in
$x^2+y^2+ux+vy+w=0$ gives center $(-u/2,-v/2)$ and

$$
r^2=\frac{u^2+v^2}{4}-w.
$$

A positive value gives a circle; zero gives a point; a negative value gives no
real points. Unequal coefficients of $x^2,y^2$ or a nonzero $xy$ term require
additional conic analysis; this recognition rule does not cover them.

### Perpendicular distance to a line

For $P=(x_0,y_0)$ and a valid line $L:ax+by+c=0$,

$$
d(P,L)=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}.
$$

The foot $H$ of the perpendicular from $P$ to $L$ is

$$
H=\left(x_0-\frac{a(ax_0+by_0+c)}{a^2+b^2},\quad
y_0-\frac{b(ax_0+by_0+c)}{a^2+b^2}\right).
$$

This is distance to an **infinite line**. For distance to a finite segment, check
whether the foot lies between its endpoints; otherwise use the nearer endpoint.

## Derivations and proofs

### Distance proof

**Theorem.** The distance formula above holds in an orthonormal Cartesian frame.

**Proof.** If both coordinate changes are nonzero, a right triangle with leg
lengths $|\Delta x|$ and $|\Delta y|$ has hypotenuse $d(A,B)$. The Pythagorean
theorem gives $d(A,B)^2=(\Delta x)^2+(\Delta y)^2$. Length is nonnegative,
so take the nonnegative square root. If either change is zero, the segment lies
along an axis and the formula reduces to that leg's absolute length. If both
are zero, it gives zero. Symmetry follows because reversing the endpoints
changes each difference's sign without changing its square. The sum of squares
is zero exactly when both differences are zero. This proves the stated cases.

### Midpoint proof

**Proposition.** The coordinate average is the midpoint, including a zero-length segment.

**Proof.** A point at parameter $t$ on the segment has displacement
$(t\Delta x,t\Delta y)$ from $A$. At $t=1/2$, its coordinates are the stated
averages. Its displacement to $B$ has the same components, so each half has
length $d(A,B)/2$. For distinct endpoints, a segment point at parameter $t$
has distances $t\,d(A,B)$ and $(1-t)d(A,B)$ from the endpoints. Equality forces
$t=1/2$. For coincident endpoints, the segment is the one point $A=B$.

### Line forms and intersection derivation

**Derivation.** Along a nonvertical straight line, similar right triangles give
a constant ratio of vertical to horizontal displacement. Calling that ratio $m$
gives $y-y_1=m(x-x_1)$. Substitute $m=\Delta y/\Delta x$ and multiply by
$\Delta x$ to obtain the two-point implicit form. If $\Delta x=0$ but
$\Delta y\ne0$, that implicit form instead yields $x=x_1$.

For the intersection, eliminate $y$ from the two implicit equations:
$Dx=b_1c_2-b_2c_1$. Eliminating $x$ gives
$Dy=c_1a_2-c_2a_1$. Division is valid when $D\ne0$. If $D=0$, the nonzero
normal coefficient pairs are proportional, so equations have either the same
solution set or no common point according to their constant terms.

**Perpendicularity justification.** A direction along $ax+by+c=0$ is $(-b,a)$:
adding a multiple of it does not change $ax+by+c$. The dot product of two such
directions is $a_1a_2+b_1b_2$. In an orthonormal frame a zero dot product means
perpendicular directions. Here a dot product of pairs $(p,q)$ and $(s,t)$ means
$ps+qt$; its angle interpretation is a later linear algebra topic. For
nonvertical lines, directions $(1,m_1)$ and $(1,m_2)$ give $1+m_1m_2=0$.

### Circle derivation

**Derivation.** By definition, $d((x,y),(h,k))=r$. Both sides are nonnegative,
so squaring is equivalent to $(x-h)^2+(y-k)^2=r^2$.

For the expanded form, $x^2+ux=(x+u/2)^2-u^2/4$, and similarly for $y$.
Thus

$$
(x+u/2)^2+(y+v/2)^2=(u^2+v^2)/4-w.
$$

A sum of real squares cannot be negative. If it is zero, each square is zero.
This explains all three signs of the right-hand side, not just the usual circle case.

### Point-to-line distance proof

**Theorem.** The stated foot lies on the line and minimizes distance from $P$.

**Proof.** Set $s=ax_0+by_0+c$ and $q=a^2+b^2>0$. The proposed foot is
$H=(x_0-as/q,y_0-bs/q)$. Substitution gives $aH_x+bH_y+c=s-qs/q=0$.
The displacement from $H$ to $P$ is $(as/q,bs/q)$.

For any other line point $Q=(u,v)$, the displacement from $H$ to $Q$ has zero
dot product with $(a,b)$ because $a(u-H_x)+b(v-H_y)=0$. Hence $HP$ is perpendicular
to $HQ$. The Pythagorean theorem gives
$d(P,Q)^2=d(P,H)^2+d(H,Q)^2\ge d(P,H)^2$, so $H$ is nearest, uniquely.
Finally,

$$
d(P,H)=\sqrt{(as/q)^2+(bs/q)^2}=\frac{|s|}{\sqrt q}.
$$

If $s=0$, then $P=H$ already lies on the line, and the same conclusion holds.

## Worked examples

### Distance and midpoint example

Let $A=(1,2)$ and $B=(7,10)$ in coordinate units.

1. Changes: $\Delta x=7-1=6$ and $\Delta y=10-2=8$.
2. Length: $d(A,B)=\sqrt{6^2+8^2}=\sqrt{100}=10$.
3. Midpoint: $M=((1+7)/2,(2+10)/2)=(4,6)$.
4. Check: $d(A,M)=\sqrt{3^2+4^2}=5=d(M,B)$.

Adding $6+8=14$ would measure an axis-aligned route, not the straight segment.

### Line through two points example

Using the same distinct points, $\Delta x=6\ne0$, so
$m=8/6=4/3$. Point-slope form is $y-2=(4/3)(x-1)$.
Multiply by three and collect terms to obtain $4x-3y+2=0$.
Check endpoints: $4(1)-3(2)+2=0$ and $4(7)-3(10)+2=0$.
The line through $A$ perpendicular to it has slope $-3/4$ and equation
$y-2=-(3/4)(x-1)$.

For $U=(3,-2)$ and $V=(3,5)$, the horizontal change is zero; the line is $x=3$.
Its slope is undefined, not a real number called infinity.

### Two-line intersection example

Find the intersection of $2x+y=8$ and $x-y=1$.
Adding gives $3x=9$, hence $x=3$. Substituting in $x-y=1$ gives $y=2$.
Check: $2(3)+2=8$ and $3-2=1$. With coefficients $(2,1,-8)$ and $(1,-1,-1)$,
$D=-3\ne0$, agreeing that the intersection is unique.

### Circle and intersection example

Given $x^2+y^2-4x+2y-4=0$, group terms and complete squares:

$$
(x-2)^2-4+(y+1)^2-1-4=0,
\qquad (x-2)^2+(y+1)^2=9.
$$

The center is $(2,-1)$ and the radius is $3$, not $9$.
To intersect it with the horizontal line $y=-1$, substitute to get
$(x-2)^2=9$. Therefore $x=2\pm3$, and the intersection points are
$(-1,-1)$ and $(5,-1)$. Both lie three units from the center.

![Circle centered at (2,-1) with radius 3; the line y=-1 meets it at (-1,-1) and (5,-1).](../../../assets/figures/circle-intersections.png)

### Perpendicular distance example

Find the distance from $P=(4,1)$ to $L:3x+4y-10=0$.
Here $s=3(4)+4(1)-10=6$ and $q=3^2+4^2=25$.
Thus $d(P,L)=6/5=1.2$ coordinate units, an exact terminating decimal.
The foot is

$$
H=(4-18/25,1-24/25)=(82/25,1/25).
$$

Check line membership:
$3(82/25)+4(1/25)-10=(246+4-250)/25=0$.
Check length: $d(P,H)=\sqrt{(18/25)^2+(24/25)^2}=30/25=6/5$.

![Point P(4,1), its perpendicular foot H(82/25,1/25), and the line 3x+4y-10=0; distance is 6/5.](../../../assets/figures/point-line-distance.png)

## Practice problems

Before looking at answers, try the [12 problems](../../../exercises/geometry/coordinate-geometry.md).
They progress from basic calculation to degeneracy, loci, and segment-versus-line
reasoning. Start with CG-01, CG-03, and CG-06 if time is limited.

**One-minute self-assessment:** Why does the distance formula use squares? Why
does a vertical line need a different slope description? What condition turns
the expanded circle equation into an empty real locus?

## Answers and explanations

The [solution set](../../../solutions/geometry/coordinate-geometry.md) gives steps,
exact results, and checks for all 12 problems.

For the self-assessment: squaring combines perpendicular components through the
Pythagorean theorem and removes displacement signs; a vertical line has zero
horizontal change so its slope quotient is undefined; a negative completed-square
right-hand side is impossible over the real numbers.

## Common mistakes

| Mistake | Correction |
| --- | --- |
| Reversing only one coordinate subtraction | Use a consistent endpoint order; squaring hides some sign errors in distance but not slope |
| Taking $\sqrt{p^2+q^2}=p+q$ | Squaring a sum adds a cross term; the equality is generally false |
| Calling vertical slope zero | Zero slope is horizontal; vertical slope is undefined |
| Using $m_1m_2=-1$ with a vertical line | Use horizontal/vertical reasoning or implicit coefficients |
| Assuming $D=0$ always means distinct parallel lines | Check coincident equations too |
| Reading radius from $r^2$ | Take the positive square root for a nondegenerate circle |
| Ignoring negative or zero squared radius | Distinguish a circle, one point, and an empty locus |
| Treating a plot as proof | Substitute or reason exactly; pixels can conceal errors |
| Measuring a line clearance as segment clearance | Check the foot lies on the finite segment |
| Applying distance to incompatible axes | Use a physical frame with compatible units and a common length scale |

## Connections

- **Algebra:** simultaneous equations become intersections of loci.
- **Linear algebra:** displacements are vectors; distance is a norm, and the
  perpendicular foot is an orthogonal projection.
- **Calculus:** a nonvertical line has constant derivative equal to its slope;
  tangent lines extend this local idea to curves.
- **Optimization:** the nearest-point proof minimizes a squared distance.
- **Complex numbers:** $(x,y)$ corresponds to $x+iy$, with $i^2=-1$; Euclidean
  distance becomes the modulus of a difference.
- **Differential geometry:** changing coordinates on curved surfaces requires
  more than the flat-plane sum of coordinate squares.

Read the chapters on [linear algebra](../../linear-algebra/linear-algebra.md),
[calculus](../../calculus/single-variable-calculus.md),
[optimization](../../optimization/optimization-and-control.md), and
[differential geometry](../../differential-geometry/geometry-and-tensors.md)
for these extensions. [Geometry overview](../overview.md) explains the
relationship between coordinate and analytic geometry.

## Applications

For a flat plate, coordinates can locate holes, midpoints can locate a symmetry
center, and point-to-line distance can give a nominal perpendicular offset.
State the datum, axis directions, and units before calculating.

**Dimensioned example.** Let two hole centers be $A=(100,50)$ mm and
$B=(400,450)$ mm in a common plate frame. Their center-to-center spacing is
$\sqrt{300^2+400^2}=500$ mm. Their midpoint is $(250,250)$ mm. A circle whose
diameter joins them has center $(250,250)$ mm and radius $250$ mm.
In the coordinate equation $(x-250)^2+(y-250)^2=250^2$, $x,y$ denote numerical
coordinates measured in mm, so both sides represent squared lengths in mm².

This model treats the plate as flat and positions as exact nominal values.
Measurement uncertainty and manufacturing tolerances need additional information;
they are not supplied by the coordinate formulas.

## Optional computational examples

Open the [executed notebook](../../../notebooks/coordinate-geometry.ipynb) to
change endpoints, inspect plots, and verify a line-circle intersection in SymPy.
Run [the plotting script](../../../scripts/plot_coordinate_geometry.py) to
regenerate all chapter figures. Computation is optional and does not carry any
part of the chapter's mathematical argument.

The notebook uses floating-point arithmetic for plots and exact symbolic values
for algebra. A drawn circle is sampled at finitely many angles; the equation
describes every point on the ideal circle.

## References and recommended reading

- Jay Abramson and contributors, *College Algebra 2e*, OpenStax,
  [Section 2.1: The Rectangular Coordinate Systems and Graphs](https://openstax.org/books/college-algebra-2e/pages/2-1-the-rectangular-coordinate-systems-and-graphs),
  for coordinate pairs, distance, and midpoint.
- OpenStax, *College Algebra 2e*,
  [Section 4.1: Linear Functions](https://openstax.org/books/college-algebra-2e/pages/4-1-linear-functions),
  for slope and nonvertical line models.
- Gilbert Strang, MIT OpenCourseWare,
  [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/),
  for the later vector and projection viewpoint.

All proofs and examples here are written for this chapter. The sources provide
background and further study, not a claim that this wording is theirs. Source
records and scope are in [the bibliography](../../../references/README.md).

## Revision and mastery status

**Personal status:** `not-started` until you assess yourself; a written chapter
does not imply you have mastered it. Use the [revision guide](../../../learning/revision-guide.md).

You are ready to mark this topic `independent` when, without notes, you can derive
distance from Pythagoras, handle a vertical line, solve a line intersection,
complete a square, and explain the line-versus-segment distinction. Solve CG-01,
CG-03, CG-06, CG-08, and CG-12 and record any errors. Revisit a new problem later
to check retention rather than memorizing the supplied answers.
