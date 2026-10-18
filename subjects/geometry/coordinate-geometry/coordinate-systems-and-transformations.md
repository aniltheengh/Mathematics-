# Coordinate systems, transformations, and quadrics

**Topic ID:** GEO-FRAME-001  
**Classification:** Geometry → coordinate, affine, and projective geometry  
**Level:** Intermediate algebra through university mathematics.

[Home](../../../README.md) · [Contents](../../../CONTENTS.md) · [Conics](conic-sections.md)

<!-- guided-lessons:start -->
**Study in depth:** [Conics III: classify every real quadratic without guessing](../../../lessons/geometry/conics-matrices-and-classification.md)
<!-- guided-lessons:end -->

## Prerequisites

Use trigonometry, vectors, matrices, and [Cartesian geometry](cartesian-plane.md).
Assume orthonormal Euclidean frames unless a different geometry is explicitly
introduced. Angles are radians. For spatial coordinates, all length components
use compatible units. Coordinate singularities are defects of a description,
not necessarily singularities of the geometric object being described.

## Definition

A **coordinate system** assigns numerical labels to positions. Cartesian,
polar, cylindrical, and spherical systems describe the same Euclidean space
with different labels. A **transformation of points** moves objects; a **change
of coordinates** relabels them. Their matrices can be inverses of one another,
which explains many apparent sign disagreements in rotation formulas.

An affine transformation is $\mathbf x'=M\mathbf x+\mathbf t$ for a matrix $M$
and translation $\mathbf t$. It is invertible exactly when $\det M\ne0$.
A projective point is a nonzero homogeneous coordinate vector modulo common
nonzero scaling. This makes parallelism a coordinate-dependent affine notion
within a larger projective setting.

## Intuitive explanation

Cartesian coordinates ask how far to move along fixed axes. Polar coordinates
ask how far and in what direction. Cylindrical coordinates add height to a
polar ground plane. Spherical coordinates use distance and two directions.
Choose the description that matches the symmetry: circular motion, axial flow,
or radial fields can become simpler. Simpler coordinates do not automatically
make coordinate increments into perpendicular lengths of equal scale.

## Mathematical notation

Cartesian coordinates are $(x,y)$ or $(x,y,z)$. In polar/cylindrical notation
$r\ge0$ is distance to the vertical axis and $\theta$ the azimuth. In spherical
notation $\rho\ge0$ is distance to the origin, $\phi\in[0,\pi]$ is the polar
angle from the **positive $z$ axis**, and $\theta\in[0,2\pi)$ the azimuth.
Other books interchange the angle names; the definition controls the formula.
A displacement vector is $\mathbf d$, a plane normal $\mathbf n\ne\mathbf0$,
and $t\in\mathbb R$ a line parameter.

## Fundamental properties

### Polar and spatial systems

Polar coordinates satisfy $x=r\cos\theta$, $y=r\sin\theta$. At $r>0$ recover
$r=\sqrt{x^2+y^2}$ and an angle by the quadrant-aware function
$\theta=\operatorname{atan2}(y,x)$, followed by any desired $2\pi$ adjustment.
The origin has no unique angle. Adding $2\pi k$, $k\in\mathbb Z$, changes the
label but not the point. With a signed-radius convention, $(-r,\theta+\pi)$
also describes the same point, but this chapter fixes nonnegative radius.

Cylindrical coordinates are $(r,\theta,z)$ with the same planar conversion.
Spherical conversion is

$$
x=\rho\sin\phi\cos\theta,\quad
y=\rho\sin\phi\sin\theta,\quad z=\rho\cos\phi.
$$

The inverse includes $\rho=\sqrt{x^2+y^2+z^2}$,
$\phi=\arccos(z/\rho)$ when $\rho>0$, and quadrant-aware azimuth when
$x^2+y^2>0$. At a pole the azimuth is indeterminate. Inverse formulas must
not divide by zero just to assign an arbitrary conventional angle.

### Lines, planes, and quadrics

A spatial line is $\mathbf x=\mathbf p+t\mathbf d$ with
$\mathbf d\ne\mathbf0$. A plane through $\mathbf p_0$ with normal
$\mathbf n\ne\mathbf0$ is $\mathbf n\cdot(\mathbf x-\mathbf p_0)=0$.
Two lines in space need not meet even when their directions are not parallel:
they can be skew. A **quadric** is a quadratic locus in three coordinates.
Diagonal examples in dimensionless coordinates, with $a,b,c>0$, include:

| Equation | Geometry |
| --- | --- |
| $x^2/a^2+y^2/b^2+z^2/c^2=1$ | Ellipsoid |
| $x^2/a^2+y^2/b^2-z^2/c^2=1$ | One-sheet hyperboloid |
| $z^2/c^2-x^2/a^2-y^2/b^2=1$ | Two-sheet hyperboloid |
| $z=x^2/a^2+y^2/b^2$ | Elliptic paraboloid |
| $z=x^2/a^2-y^2/b^2$ | Hyperbolic paraboloid, or saddle |
| $x^2/a^2+y^2/b^2-z^2/c^2=0$ | Elliptic double cone |
| $x^2+y^2=R^2$ | Circular cylinder, independent of $z$ |

For physical lengths, introduce appropriate dimensional scales before using the
paraboloid equations. Plane sections recover conics; degeneracies include pairs
of planes, lines, points, and empty sets.

### Affine and projective viewpoints

An invertible affine map preserves straightness, parallelism, and ratios along
one line. It need not preserve angles, lengths, area, circles, or perpendicularity.
An orthogonal map satisfies $M^TM=I$ and does preserve lengths; determinant
$+1$ is orientation-preserving, while determinant $-1$ reverses orientation.
A general projective transformation can send parallel affine lines to
intersecting ones; incidence is preserved where the map is defined.

Represent $(x,y)$ as $[x:y:1]$. Coordinates $[u:v:w]$ with $w\ne0$ correspond
to $(u/w,v/w)$; points with $w=0$ lie at infinity in the projective completion.
A nonsingular $3\times3$ homogeneous matrix induces a projective transformation.
Affine translation fits into this matrix model with last row $(0,0,1)$.

### Non-Euclidean settings

A spherical triangle has geodesic great-circle sides. On a sphere of radius
$R$, its area is $R^2(A+B+C-\pi)$ for an ordinary convex triangle, with
angles in radians. Angle sum exceeds $\pi$. In the hyperbolic plane of constant
curvature $-1/R^2$, triangle area is $R^2(\pi-A-B-C)$ and angle sum is smaller.
These formulas are consequences of the Gauss-Bonnet theorem, cited here rather
than proved. A coordinate change within the Euclidean plane cannot create
intrinsic curvature: a curved metric is a change of geometry, not merely labels.

## Important formulas and identities

The active counterclockwise rotation through $\alpha$ is

$$
R(\alpha)=\begin{pmatrix}\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha\end{pmatrix},\qquad
R^{-1}=R^T=R(-\alpha).
$$

If a new frame has old-coordinate origin $\mathbf o$ and columns of $R$ as its
axes, then old and new coordinates satisfy
$\mathbf x=\mathbf o+R\mathbf u$, so $\mathbf u=R^T(\mathbf x-\mathbf o)$.
This formula is for a passive frame change and explains the inverse rotation.

Euclidean line elements and volume/area factors are

$$
ds^2=dr^2+r^2d\theta^2\quad\text{(polar)},\qquad dA=r\,dr\,d\theta,
$$

$$
ds^2=dr^2+r^2d\theta^2+dz^2,\qquad dV=r\,dr\,d\theta\,dz,
$$

$$
ds^2=d\rho^2+\rho^2d\phi^2+\rho^2\sin^2\phi\,d\theta^2,
\qquad dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.
$$

For plane $\mathbf n\cdot\mathbf x=d$, the distance from $\mathbf p$ is
$|\mathbf n\cdot\mathbf p-d|/\|\mathbf n\|$.
For a line $\mathbf p_0+t\mathbf d$, its nearest point to $\mathbf p$ uses
$t=((\mathbf p-\mathbf p_0)\cdot\mathbf d)/(\mathbf d\cdot\mathbf d)$.
Constrain $0\le t\le1$ and clamp to this interval for a segment parameterized
by its endpoint difference; do not clamp for an infinite line.

## Derivations and proofs

### Polar metric and Jacobian

Differentiate $x=r\cos\theta$, $y=r\sin\theta$:
$dx=\cos\theta\,dr-r\sin\theta\,d\theta$ and
$dy=\sin\theta\,dr+r\cos\theta\,d\theta$. Squaring and adding cancels
mixed terms and yields $dx^2+dy^2=dr^2+r^2d\theta^2$. The determinant
$\partial(x,y)/\partial(r,\theta)=r$ gives the area factor for $r>0$.
The zero determinant at the origin is consistent with the lost angular label.
The same orthogonal-differential calculation gives the spherical metric above.

### Rotation preserves length

Trigonometric identities give $R^TR=I$. For every displacement $\mathbf v$,
$\|R\mathbf v\|^2=\mathbf v^TR^TR\mathbf v=\mathbf v^T\mathbf v$.
Translation cancels when taking coordinate differences. A shear lacks this
orthogonality, so straightness alone does not imply length preservation.

### Projective intersection at infinity

Affine lines $ax+by+c_1=0$ and $ax+by+c_2=0$, $c_1\ne c_2$, have homogeneous
equations $au+bv+c_iw=0$. Subtraction gives $w=0$. Their common projective
point is $[b:-a:0]$, the direction parallel to both lines. It is not an
ordinary finite Euclidean point; projective completion adds it explicitly.

## Worked examples

### Convert an exact point

For $(x,y)=(-\sqrt3,1)$, $r=2$, and the point is in quadrant II, so
$\theta=5\pi/6$. Using $\arctan(y/x)$ alone would choose an incorrect
quadrant. In spherical coordinates, $(1,1,\sqrt2)$ has $\rho=2$,
$\phi=\pi/4$, and $\theta=\pi/4$; substitution checks all three components.

### Change an engineering datum

Let a new frame's origin be $(10,20)$ mm in old coordinates and its axes rotated
counterclockwise by $\pi/2$. New coordinates $(3,4)$ mm correspond to
$\mathbf x=(10,20)+(-4,3)=(6,23)$ mm. Conversely, subtract the origin and
multiply by $R^T$ to recover $(3,4)$ mm. Adding origin coordinates before applying
the inverse rotation would be a different operation.

### A spatial intersection

Line $(x,y,z)=(1,0,2)+t(1,2,-1)$ meets plane $x+y+z=6$ when
$3+2t=6$, hence $t=3/2$ and point $(5/2,3,1/2)$. Substitution gives $6$.
If the line direction had zero dot product with the plane normal, there would
instead be no intersection or infinitely many, depending on the base point.

### A coordinate volume integral

A ball of radius $R$ has volume
$\int_0^{2\pi}\int_0^\pi\int_0^R\rho^2\sin\phi\,d\rho\,d\phi\,d\theta
=2\pi\cdot2\cdot R^3/3=4\pi R^3/3$. Omitting the Jacobian would integrate
coordinate labels rather than physical volume.

## Practice problems

1. Convert $(r,\theta)=(3,2\pi/3)$ to Cartesian coordinates.
2. Apply an active rotation of $\pi/2$ to $(2,-1)$. What passive coordinate
   change represents the same fixed point when the axes rotate by $\pi/2$?
3. Find the distance from $(1,2,3)$ to plane $2x-y+2z=1$.
4. Classify $x^2+y^2-z^2=1$ and its sections at $z=0$ and $z=\sqrt3$.
5. Does the shear $(x,y)\mapsto(x+2y,y)$ preserve area and length?
6. A spherical triangle on the unit sphere has three right angles. Find its area.

## Answers and explanations

1. $(-3/2,3\sqrt3/2)$, using exact unit-circle values.
2. Active result $(1,2)$. Passive coordinates use $R^T$ and give $(-1,-2)$.
   The inverse sign reflects that the point is fixed while the axes move.
3. Numerator $|2-2+6-1|=5$; normal length $\sqrt{4+1+4}=3$;
   distance $5/3$ length units.
4. A one-sheet hyperboloid; sections are circles $x^2+y^2=1$ and
   $x^2+y^2=4$, of radii $1$ and $2$.
5. Its matrix determinant is one, so area is preserved. It sends $(0,1)$
   to $(2,1)$, increasing its length from $1$ to $\sqrt5$; length is not preserved.
6. Spherical excess is $3\pi/2-\pi=\pi/2$, so area is $\pi/2$.
   Eight such octants cover the unit sphere of area $4\pi$.

## Common mistakes and misconceptions

State which spherical angle is polar, avoid dividing by radius at the origin,
and use quadrant-aware inverse angles. Do not use $\sqrt{(\Delta r)^2+
(\Delta\theta)^2}$ as a Euclidean distance. Distinguish active rotations from
passive frame changes and apply translations in the correct order. In three
dimensions, nonparallel lines need not intersect. A perspective image does not
preserve Euclidean lengths merely because its edges remain straight.

## Connections to other mathematics

[Conic classification](conic-sections.md) is the two-dimensional version of
diagonalizing quadratic forms. Multivariable calculus uses the metric and
Jacobian factors. Linear algebra supplies orthogonal maps and projections;
projective geometry describes perspective; differential geometry handles
intrinsic curved metrics. See the [book navigation](../../../INDEX.md).

## Applications

Coordinate frames occur in survey datums, pipe supports, robot joints, and CAD
assemblies. Cylindrical symmetry suits pipes and rotational parts; spherical
symmetry suits radial fields and ball geometry. Always identify the origin,
axis order, handedness, angle units, and measurement unit. A homogeneous
transformation combines position and rotation without mixing point coordinates
with displacement vectors: translations affect points, but cancel in differences.

## Optional computational examples

The [geometry script](../../../scripts/plot_geometry.py) plots polar coordinates
and representative quadric surfaces. The [exact checks](../../../scripts/verify_geometry.py)
verify rotation orthogonality, the polar Jacobian, the datum conversion, and
the line-plane intersection. Three-dimensional plots are projections onto a
screen, so labels and equations carry geometric information that perspective can distort.

![A polar point at radius 2 and angle pi/3, with its exact Cartesian components.](../../../assets/figures/geometry/polar-coordinates.png)

![An ellipsoid x²/4+y²/9+z²/16=1 and the saddle z=x²-y², shown as sampled surfaces with labeled axes.](../../../assets/figures/geometry/quadrics.png)

## References and recommended reading

OpenStax, *Calculus Volume 3*,
[Cylindrical and Spherical Coordinates](https://openstax.org/books/calculus-volume-3/pages/2-7-cylindrical-and-spherical-coordinates),
provides the coordinate conventions and standard transformations. For quadratic
forms and orthogonal changes of basis, see Gilbert Strang's
[MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/).
For curved metrics and the cited curvature-area connection see David Tong's
[General Relativity notes, chapters on differential and Riemannian geometry](https://davidtong.org/teaching/general-relativity/).
Projective statements here are derived directly in homogeneous coordinates.

## Revision and mastery status

Practice forward and inverse conversion, identify singular coordinates, transform
a point between frames, compute a plane distance, and distinguish the main
quadric families. Explain the Jacobian rather than memorizing it. Personal
mastery remains unassessed until you record actual independent work.
