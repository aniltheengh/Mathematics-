# Euclidean geometry: shape, measurement, and proof

**Topic ID:** GEO-EUC-001  
**Classification:** Geometry → Euclidean plane and solid geometry  
**Level:** Elementary through university revision; real Euclidean spaces.

[Home](../../README.md) · [Contents](../../CONTENTS.md) · [Coordinate geometry](coordinate-geometry/cartesian-plane.md)

## Prerequisites

Use arithmetic, ratios, elementary algebra, square roots, and angle measurement.
A point has position without size; a line extends indefinitely; a segment has
two endpoints. Those are mathematical idealizations, not claims that a physical
mark has zero width. All geometric lengths in one formula must use compatible units.

## Definition

**Definition.** Euclidean geometry studies incidence, distance, angle, and shape
under Euclidean axioms. Two distinct points determine a unique line. In a plane,
through a point outside a line there is exactly one parallel line. This parallel
postulate distinguishes Euclidean geometry from spherical and hyperbolic settings.
An angle is measured by the rotation between rays; a full turn is $2\pi$ radians.

**Congruence** means equality of shape and size under a rigid motion, possibly
including reflection. **Similarity** additionally allows a common positive
length scale. Equal area alone gives neither congruence nor similarity. A circle
is the boundary of points at a fixed positive distance from a center; its disk
includes the interior. A polygon has a closed chain of straight sides, and a
polyhedron has polygonal faces.

## Intuitive explanation

Synthetic geometry reasons using relationships between figures; coordinate
geometry assigns numbers to those same relationships. A perpendicular drawn
from a vertex turns a triangle into right triangles and exposes lengths and
areas. Similarity compares a whole shape rather than unrelated side ratios.
When a drawing suggests a right angle or equal sides, those properties must
come from the problem's hypotheses, a construction, or a proof.

## Mathematical notation

For triangle $ABC$, let $a,b,c>0$ be lengths opposite angles $A,B,C$.
Its area is $K$, semiperimeter $s=(a+b+c)/2$, and altitude to side $a$ is $h_a$.
A circle has radius $R>0$, diameter $2R$, circumference $L$, and disk area $S$.
For solids $V$ denotes volume and $S$ total surface area. Do not confuse the
vertex label $A$ with an area symbol; this chapter uses $K$ for triangle area.

## Fundamental properties

### Triangles and constructions

The Euclidean triangle angle sum is $A+B+C=\pi$. A nondegenerate triangle
exists for prescribed positive sides exactly when the strict triangle
inequalities hold: $a+b>c$, $b+c>a$, $c+a>b$. Equality gives a collapsed figure.
SSS, SAS, and ASA give congruence criteria; AAA specifies similarity, not size.
Two sides and a nonincluded angle can give an ambiguous case and are not a
general congruence rule. Two equal angles give triangle similarity.

The perpendicular bisectors meet at the circumcenter; angle bisectors meet at
the incenter. Medians meet at a centroid which divides each median in the ratio
$2:1$ from its vertex. Altitudes meet at the orthocenter. A circumcenter or
orthocenter can lie outside an obtuse triangle; the incenter remains inside.
Straightedge-and-compass constructions use an unmarked straightedge and compass;
an arbitrary angle cannot in general be trisected by those tools alone.

### Polygons and circles

For a simple Euclidean $n$-gon, $n\ge3$, interior angles sum to $(n-2)\pi$.
The sum does not assert each angle is equal. For a regular polygon each is
$(n-2)\pi/n$. A radius perpendicular to a chord bisects that chord. A tangent at
a circle point is perpendicular to its radius. An inscribed angle subtending a
specified arc has half the corresponding central angle; keep track of the arc
and orientation when the vertex changes sides.

Intersecting chords satisfy $PA\,PB=PC\,PD$ when two secants through an interior
point $P$ meet the same circle at $A,B$ and $C,D$. For an external point, the
secant-product form uses the near and far intersection distances on each ray;
a tangent gives the square of tangent length. These are forms of the power-of-a-point theorem.

### Solid geometry

Two intersecting nonparallel planes meet in a line. In three dimensions, lines
can be parallel, intersecting, or skew. A sphere is a surface, a ball its
interior together with boundary. A right circular cylinder or cone has its axis
perpendicular to its circular base. General oblique solids need perpendicular
height, not slant length, in volume formulas.

For a convex polyhedron, $V_e-E+F=2$, where $V_e$ counts vertices, $E$ edges,
and $F$ faces. This Euler formula also applies to suitable cell decompositions
of a topological sphere, but not to every surface: a torus has Euler
characteristic zero. The only convex regular polyhedra are the tetrahedron,
cube, octahedron, dodecahedron, and icosahedron.

## Important formulas and identities

For a right triangle with perpendicular legs $a,b$ and hypotenuse $c$,
$a^2+b^2=c^2$. More generally the cosine law is
$c^2=a^2+b^2-2ab\cos C$. The triangle area formulas are

$$
K=\tfrac12 a h_a=\tfrac12 ab\sin C
 =\sqrt{s(s-a)(s-b)(s-c)}.
$$

Heron's formula assumes a nondegenerate triangle; in limiting equality cases
the area is zero. For circle sectors use angle $\theta$ in radians:

$$
L=2\pi R,\qquad S=\pi R^2,\qquad
\text{arc length}=R\theta,\qquad \text{sector area}=\tfrac12R^2\theta.
$$

The sector formula takes $0\le\theta\le2\pi$ for a single ordinary sector.
For a regular $n$-gon with perimeter $P$ and apothem $r_a$, its area is $Pr_a/2$.

| Solid | Volume | Total surface area / condition |
| --- | --- | --- |
| Rectangular box, sides $a,b,c$ | $abc$ | $2(ab+bc+ca)$ |
| Prism, base area $B$, perpendicular height $h$ | $Bh$ | Depends on base and lateral geometry |
| Pyramid | $Bh/3$ | Depends on face slant heights |
| Right circular cylinder | $\pi R^2h$ | $2\pi Rh+2\pi R^2$ |
| Right circular cone | $\pi R^2h/3$ | $\pi R\sqrt{R^2+h^2}+\pi R^2$ |
| Ball / sphere | $4\pi R^3/3$ | $4\pi R^2$ |

All lengths here are positive. If a cone's slant height is $\ell$, then
$\ell^2=R^2+h^2$ only for a right circular cone.

## Derivations and proofs

### Triangle angle sum

Draw through vertex $C$ the line parallel to $AB$. Alternate interior angle
equalities copy angles $A$ and $B$ beside angle $C$ along the straight line.
Their sum is the straight angle $\pi$. This uses the Euclidean parallel
postulate; on a curved surface this proof's parallel-line step is not available.

### Pythagorean area argument

Arrange four congruent right triangles, each with legs $a,b$, inside a square
of side $a+b$, with their hypotenuses bounding the inner square of side $c$.
Its angles are right because the two acute triangle angles sum to $\pi/2$.
Subtracting triangle areas gives
$(a+b)^2=4(ab/2)+c^2$, hence $c^2=a^2+b^2$.
The converse also holds: if a triangle satisfies the squared-length identity
with $c$ largest, its included opposite angle is right, for example by the cosine law.

### Heron's formula

From the cosine law, $\cos C=(a^2+b^2-c^2)/(2ab)$. Since
$K=ab\sin C/2$ and $\sin C>0$ in a nondegenerate triangle,

$$
16K^2=4a^2b^2-(a^2+b^2-c^2)^2
=(a+b+c)(a+b-c)(a-b+c)(-a+b+c).
$$

The four factors are $2s,2(s-c),2(s-b),2(s-a)$. Divide by $16$ and take the
positive square root. The triangle inequalities ensure positivity.

### Similarity and volume

Uniform scaling by $k>0$ multiplies every length by $k$, each area by $k^2$,
and each volume by $k^3$. For a coordinate proof the transformations have
determinants $k^2$ and $k^3$. Consequently a scale model that halves every length
uses one eighth of the volume, not half. A pyramid's parallel cross-section at
distance $z$ from its apex has area $B(z/h)^2$; integrating from $0$ to $h$
gives $Bh/3$, explaining the volume factor rather than merely memorizing it.

## Worked examples

### A triangle without an altitude

For sides $13,14,15$ cm, $s=21$ cm. Heron's formula gives
$K=\sqrt{21\cdot8\cdot7\cdot6}=\sqrt{7056}=84$ cm².
The altitude to the $14$ cm side is $h=2K/14=12$ cm. Each term has the expected
dimension: four length factors under a square root give length squared.

### Circle chord

A chord of a circle of radius $5$ cm is $3$ cm from the center. Its half-length
$q$ forms a right triangle with the radius, so $q^2+3^2=5^2$ and $q=4$ cm.
The complete chord is $8$ cm. A center-to-chord distance exceeding $5$ cm
would not describe a real chord.

### An open cylindrical tank

For internal radius $R=1$ m and height $h=2$ m, capacity is $2\pi$ m³.
If the idealized tank has a side wall and bottom but no lid, its material area
is $2\pi Rh+\pi R^2=5\pi$ m². The closed-cylinder formula would incorrectly
add another $\pi$ m². Wall thickness and allowances are separate design inputs.

### A scale change

A similar part has all lengths enlarged by $3/2$. Its area multiplier is $9/4$
and volume multiplier $27/8$. If the original volume is $16$ cm³, the new
volume is $54$ cm³. Similarity requires the same factor along every direction.

## Practice problems

1. Can sides $2,3,6$ form a Euclidean triangle? Can $2,3,5$ form a nondegenerate one?
2. Find the area and altitude to side $10$ of a triangle with sides $6,8,10$.
3. A regular hexagon has circumradius $2$ cm. Find its perimeter and area exactly.
4. A right cone has radius $3$ m and height $4$ m. Find volume and total area.
5. A circle has radius $4$ cm. Find the arc length and area of a $\pi/3$ sector.
6. A convex polyhedron has $12$ vertices and $20$ faces. How many edges has it?

## Answers and explanations

1. No: $2+3<6$. The second triple has equality, so it is a collapsed segment
   with area zero, not a nondegenerate triangle.
2. It is right because $6^2+8^2=10^2$. Area $K=24$ square coordinate units;
   altitude to the hypotenuse $h=2K/10=24/5$ length units.
3. Six equilateral triangles of side $2$ give perimeter $12$ cm and total
   area $6(\sqrt3\,2^2/4)=6\sqrt3$ cm².
4. Slant length $5$ m. Volume $\pi(9)(4)/3=12\pi$ m³; lateral area $15\pi$
   m² and base area $9\pi$ m², totaling $24\pi$ m².
5. Arc length $4\pi/3$ cm; sector area $8\pi/3$ cm². Radians make both formulas valid.
6. Euler's relation gives $E=12+20-2=30$.

## Common mistakes and misconceptions

A perpendicular height is not generally a side or slant height. Diameter is
twice radius; using it as radius multiplies disk area by four. Area scales
quadratically and volume cubically. A sphere's surface area differs from a
disk's area. Separate open and closed surface boundaries in a material problem.
Do not transfer flat-plane angle sums to spherical triangles or assume a
convex-polyhedron identity applies to a solid with handles.

## Connections to other mathematics

[Coordinate geometry](coordinate-geometry/cartesian-plane.md) expresses these
properties as equations. [Conics](coordinate-geometry/conic-sections.md) extend
circles and loci. Determinants express signed area and volume; calculus derives
curved-body measurements from slices; topology explains Euler characteristic.
Proof methods distinguish a drawing from a universal geometric claim.

## Applications

Plate layouts, triangulated frames, vessel geometry, triangulated surveys, and
volume estimates all use these relationships. Choose a mathematical model before
calculating: a pipe elbow is neither a straight cylinder nor a cone, and a real
tank can include dished ends or internal structures. The formulas describe the
ideal geometry specified, not tolerances or structural adequacy.

## Optional computational examples

The [geometry checks](../../scripts/verify_geometry.py) verify Heron's example,
cone dimensions, and scaling factors exactly. Use coordinates or a geometric
construction to check whether a proposed triangle actually exists before asking
software to render it. A plotting package can display invalid assumptions without
recognizing their physical inconsistency.

## References and recommended reading

Euclid's *Elements* is a primary historical source for synthetic geometry; see
the [Clark University edition by D. E. Joyce](https://mathcs.clarku.edu/~djoyce/elements/).
For modern coordinate and measurement foundations see OpenStax,
[Prealgebra 2e](https://openstax.org/details/books/prealgebra-2e).
The statements here use modern real-coordinate assumptions; historical axioms
are not presented as a complete modern formal foundation.

## Revision and mastery status

Be able to identify a formula's required shape, distinguish length/area/volume,
prove one central identity, and check degeneracy and units. Solve all six
questions without notes, then explain why the open-tank area differs from the
closed-cylinder formula. Record your own evidence in the revision tracker.
