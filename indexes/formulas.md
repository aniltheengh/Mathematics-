# Formula index

[Home](../README.md) · [Notation](notation.md) · [Proofs](proofs.md)

Only formulas documented in written chapters appear here. Each entry links to
its assumptions, symbols, and derivation. This is a lookup aid, not a substitute
for checking the hypotheses. Use the [formula template](../templates/formula-template.md)
when a result needs a longer independent reference entry.

## Coordinate geometry

Assume an orthonormal Cartesian frame in the real Euclidean plane and the same
length unit on both axes. Let $A=(x_1,y_1)$, $B=(x_2,y_2)$,
$\Delta x=x_2-x_1$, $\Delta y=y_2-y_1$, and $P=(x_0,y_0)$.
For a line, $a,b,c$ are real with $a^2+b^2>0$. A circle has center $(h,k)$
and radius $r>0$. For an expanded circle, $u,v,w$ are real coefficients.

| ID | Result | Formula | Conditions and source |
| --- | --- | --- | --- |
| GEO-F01 | Distance | $d(A,B)=\sqrt{(\Delta x)^2+(\Delta y)^2}$ | All points; [statement](../subjects/geometry/coordinate-geometry/cartesian-plane.md#distance-and-midpoint), [proof](../subjects/geometry/coordinate-geometry/cartesian-plane.md#distance-proof) |
| GEO-F02 | Midpoint | $M=((x_1+x_2)/2,(y_1+y_2)/2)$ | Includes coincident endpoints; [proof](../subjects/geometry/coordinate-geometry/cartesian-plane.md#midpoint-proof) |
| GEO-F03 | Slope and point-slope line | $m=\Delta y/\Delta x$, $y-y_1=m(x-x_1)$ | $\Delta x\ne0$; [line forms](../subjects/geometry/coordinate-geometry/cartesian-plane.md#lines) |
| GEO-F04 | Two-point implicit line | $\Delta y(x-x_1)-\Delta x(y-y_1)=0$ | $A\ne B$; includes vertical lines; [derivation](../subjects/geometry/coordinate-geometry/cartesian-plane.md#line-forms-and-intersection-derivation) |
| GEO-F05 | Circle | $(x-h)^2+(y-k)^2=r^2$ | $r>0$; [derivation](../subjects/geometry/coordinate-geometry/cartesian-plane.md#circle-derivation) |
| GEO-F06 | Expanded circle | Center $(-u/2,-v/2)$; $r^2=(u^2+v^2)/4-w$ | Equation $x^2+y^2+ux+vy+w=0$; classify sign of $r^2$; [conditions](../subjects/geometry/coordinate-geometry/cartesian-plane.md#circles) |
| GEO-F07 | Point-to-line distance | $d(P,L)=\lvert ax_0+by_0+c\rvert/\sqrt{a^2+b^2}$ | Infinite line $L:ax+by+c=0$; [proof](../subjects/geometry/coordinate-geometry/cartesian-plane.md#point-to-line-distance-proof) |
| GEO-F08 | Unique line intersection | $x=(b_1c_2-b_2c_1)/D$, $y=(c_1a_2-c_2a_1)/D$ | Two valid lines, $D=a_1b_2-a_2b_1\ne0$; [definition of coefficients and derivation](../subjects/geometry/coordinate-geometry/cartesian-plane.md#line-forms-and-intersection-derivation) |

Lengths inherit the coordinate unit. Squared lengths inherit its square. Slope
is dimensionless when both coordinates use the same unit. The implicit-line
coefficients may be rescaled together without changing geometric distance.

**Related result:** the [perpendicular foot](../subjects/geometry/coordinate-geometry/cartesian-plane.md#perpendicular-distance-to-a-line)
is useful for checking whether the nearest line point lies on a finite segment.
