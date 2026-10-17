# Coordinate geometry solutions

[Problems](../../exercises/geometry/coordinate-geometry.md) ·
[Chapter](../../subjects/geometry/coordinate-geometry/cartesian-plane.md)

All coordinates and lengths are in the exercise's orthonormal Euclidean frame.
Try each problem before reading its answer. Exact values appear before any decimals.

## CG-01 Distance and midpoint

$\Delta x=4-(-2)=6$ and $\Delta y=9-1=8$, so $d=\sqrt{36+64}=10$.
The midpoint is $M=((-2+4)/2,(1+9)/2)=(1,5)$.
Each half has changes of magnitudes $3,4$, hence length $5$.
[Return to CG-01](../../exercises/geometry/coordinate-geometry.md#cg-01-distance-and-midpoint)

## CG-02 A line through two points

$m=(6-(-2))/(5-1)=8/4=2$. Through $C$, $y+2=2(x-1)$, so
$y=2x-4$ or $2x-y-4=0$. Substitution gives $2(1)-(-2)-4=0$
and $2(5)-6-4=0$.
[Return to CG-02](../../exercises/geometry/coordinate-geometry.md#cg-02-a-line-through-two-points)

## CG-03 A vertical line

The horizontal coordinate is always $-3$, so $x=-3$. Its slope is undefined
because its horizontal change is zero. The perpendicular line through the given
point is horizontal: $y=5$, whose slope is zero.
[Return to CG-03](../../exercises/geometry/coordinate-geometry.md#cg-03-a-vertical-line)

## CG-04 Intersection

Adding the equations yields $3x=9$, hence $x=3$ and $y=2$. The point $(3,2)$
lies on both lines. Their slopes are $-2$ and $1$, so they are distinct and
not parallel. Equivalently, $D=2(-1)-1(1)=-3\ne0$. The intersection is unique.
[Return to CG-04](../../exercises/geometry/coordinate-geometry.md#cg-04-intersection)

## CG-05 Parallel or coincident

(a) Dividing $4x-2y=6$ by two gives $2x-y=3$, exactly the first line, so there
are infinitely many common points. (b) Dividing $4x-2y=7$ by two gives
$2x-y=7/2$, incompatible with $2x-y=3$; the lines are parallel and distinct.
Both comparisons have determinant $2(-2)-4(-1)=0$, which only checks the
normal coefficient pairs, not consistency of constant terms.
[Return to CG-05](../../exercises/geometry/coordinate-geometry.md#cg-05-parallel-or-coincident)

## CG-06 Completing the square

$x^2-6x=(x-3)^2-9$ and $y^2+4y=(y+2)^2-4$, giving
$(x-3)^2+(y+2)^2=25$. Center $(3,-2)$, radius $5$. At $y=-2$,
$(x-3)^2=25$, so intersections are $(-2,-2)$ and $(8,-2)$.
[Return to CG-06](../../exercises/geometry/coordinate-geometry.md#cg-06-completing-the-square)

## CG-07 A sloping line meets a circle

Substitute $y=x+1$:
$x^2+(x+1)^2=25$, so $2x^2+2x-24=0$ and
$(x+4)(x-3)=0$. The pairs are $(-4,-3)$ and $(3,4)$.
They satisfy the line because $-3=-4+1$ and $4=3+1$; their squared distances
from the origin are $16+9=25$ and $9+16=25$.
[Return to CG-07](../../exercises/geometry/coordinate-geometry.md#cg-07-a-sloping-line-meets-a-circle)

## CG-08 Perpendicular distance

$s=3(4)+4(1)-10=6$, $q=9+16=25$, and the distance is
$|6|/5=6/5$. The foot is $H=(4-18/25,1-24/25)=(82/25,1/25)$.
Membership: $3(82/25)+4(1/25)-10=0$. The displacement $P-H=(18/25,24/25)$
is parallel to the line normal $(3,4)$, proving perpendicularity. Its length
is $\sqrt{18^2+24^2}/25=30/25=6/5$.
[Return to CG-08](../../exercises/geometry/coordinate-geometry.md#cg-08-perpendicular-distance)

## CG-09 Plate coordinates in millimetres

The changes are $300$ mm and $400$ mm, giving spacing $500$ mm.
Squared distance is $250000$ mm². The midpoint is $(250,250)$ mm.
For a diameter, the center is its midpoint and the radius is half its length,
so the requested circle has center $(250,250)$ mm and radius $250$ mm.
Endpoint offsets from that center are $(-150,-200)$ mm and $(150,200)$ mm;
each has length $250$ mm, independently checking the circle.
[Return to CG-09](../../exercises/geometry/coordinate-geometry.md#cg-09-plate-coordinates-in-millimetres)

## CG-10 Degenerate cases

(a) Completing squares gives $(x+1)^2+(y-2)^2=0$. Both squares must vanish,
so the real locus is just $(-1,2)$. (b) The right-hand side becomes $-1$;
there are no real points because a sum of real squares is nonnegative.
For repeated endpoints $A=B$, the two-point line equation is $0=0$, which every
point satisfies. One point allows infinitely many lines through it and does not
specify a unique line.
[Return to CG-10](../../exercises/geometry/coordinate-geometry.md#cg-10-degenerate-cases)

## CG-11 An equidistant locus

Equate the two nonnegative distances and square:
$(x+2)^2+y^2=(x-4)^2+y^2$.
Expansion and cancellation give $4x+4=-8x+16$, hence $x=1$.
Every real $y$ is allowed. Conversely, every $(1,y)$ has squared distance
$9+y^2$ from either endpoint, so no solutions were added or lost. The locus is
the vertical perpendicular bisector through the midpoint $(1,0)$.
[Return to CG-11](../../exercises/geometry/coordinate-geometry.md#cg-11-an-equidistant-locus)

## CG-12 A line is longer than its segment

The infinite line is $y=0$, with perpendicular foot $(3,0)$ and distance $4$.
The foot lies outside the segment, whose points are $(t,0)$ for $0\le t\le1$.
Squared distance is $(3-t)^2+16$; as $t$ increases from zero to one, $3-t$
decreases from three to two and remains positive. Therefore its minimum occurs
at $t=1$, the endpoint $B$. The segment distance is
$\sqrt{(3-1)^2+4^2}=\sqrt{20}=2\sqrt5\approx4.4721$.
Restricting the available points cannot make the nearest distance smaller.
[Return to CG-12](../../exercises/geometry/coordinate-geometry.md#cg-12-a-line-is-longer-than-its-segment)
