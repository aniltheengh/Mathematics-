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

## Conic sections

For centered coordinates $X=x-h$, $Y=y-k$, positive semiaxes $a,b$, and signed nonzero focal parameter $p$, the exact standard forms are:

| Curve | Standard equation | Conditions and derivation |
| --- | --- | --- |
| Ellipse | $X^2/a^2+Y^2/b^2=1$ | $a\ge b>0$, $c^2=a^2-b^2$, foci on the major axis; [chapter](../subjects/geometry/coordinate-geometry/conic-sections.md) |
| Hyperbola | $X^2/a^2-Y^2/b^2=1$ | $a,b>0$, $c^2=a^2+b^2$, transverse axis horizontal; [chapter](../subjects/geometry/coordinate-geometry/conic-sections.md) |
| Parabola | $Y^2=4pX$ | $p\ne0$, focus $(h+p,k)$, directrix $x=h-p$; [chapter](../subjects/geometry/coordinate-geometry/conic-sections.md) |
| General quadratic | $Ax^2+Bxy+Cy^2+Dx+Ey+F=0$ | $A,B,C$ not all zero; $B^2-4AC$ indicates family, not real existence; [chapter](../subjects/geometry/coordinate-geometry/conic-sections.md) |

## Formula directory across the book

Each chapter defines every symbol and supplies the applicable domain, exceptional cases, and derivations. These links are the canonical reference for the full formulas, not an unconditional formula sheet.

| Subject | Formula reference |
| --- | --- |
| Foundations and logic | [Logic, sets, and proof](../subjects/foundations/logic-and-proof.md#important-formulas-and-identities) |
| Arithmetic and number systems | [Arithmetic and number systems](../subjects/numbers/arithmetic-and-number-systems.md#important-formulas-and-identities) |
| Elementary algebra | [Elementary and intermediate algebra](../subjects/algebra/elementary-algebra.md#important-formulas-and-identities) |
| Geometry | [Euclidean geometry: shape, measurement, and proof](../subjects/geometry/euclidean-geometry.md#important-formulas-and-identities) |
| Geometry | [Cartesian plane: points, lines, and circles](../subjects/geometry/coordinate-geometry/cartesian-plane.md#formulas-and-conditions) |
| Geometry | [Conic sections: circles, ellipses, parabolas, and hyperbolas](../subjects/geometry/coordinate-geometry/conic-sections.md#important-formulas-and-identities) |
| Geometry | [Coordinate systems, transformations, and quadrics](../subjects/geometry/coordinate-geometry/coordinate-systems-and-transformations.md#important-formulas-and-identities) |
| Trigonometry | [Trigonometry and harmonic motion](../subjects/trigonometry/trigonometry.md#important-formulas-and-identities) |
| Functions, limits, and series | [Functions, limits, continuity, and series](../subjects/analysis/functions-limits-and-series.md#important-formulas-and-identities) |
| Linear and multilinear algebra | [Linear algebra and multilinear algebra](../subjects/linear-algebra/linear-algebra.md#important-formulas-and-identities) |
| Single-variable calculus | [Differential and integral calculus](../subjects/calculus/single-variable-calculus.md#important-formulas-and-identities) |
| Multivariable and vector calculus | [Multivariable and vector calculus](../subjects/calculus/multivariable-and-vector-calculus.md#important-formulas-and-identities) |
| Ordinary differential equations | [Ordinary differential equations and dynamical systems](../subjects/differential-equations/ordinary-differential-equations.md#important-formulas-and-identities) |
| Partial differential equations | [Partial differential equations](../subjects/differential-equations/partial-differential-equations.md#important-formulas-and-identities) |
| Discrete mathematics | [Discrete mathematics and combinatorics](../subjects/discrete/discrete-mathematics.md#important-formulas-and-identities) |
| Number theory | [Number theory: divisibility, congruences, and primes](../subjects/number-theory/number-theory.md#important-formulas-and-identities) |
| Abstract algebra | [Abstract algebra: groups, rings, fields, and structural methods](../subjects/abstract-algebra/abstract-algebra.md#important-formulas-and-identities) |
| Real analysis and measure | [Real analysis and measure theory](../subjects/analysis/real-analysis-and-measure.md#important-formulas-and-identities) |
| Complex analysis | [Complex analysis](../subjects/complex-analysis/complex-analysis.md#important-formulas-and-identities) |
| Probability and stochastic processes | [Probability and stochastic processes](../subjects/probability/probability-and-stochastic-processes.md#important-formulas-and-identities) |
| Statistics | [Statistics, inference and data analysis](../subjects/statistics/statistics.md#important-formulas-and-identities) |
| Numerical analysis | [Numerical analysis and scientific computation](../subjects/numerical-analysis/numerical-analysis.md#important-formulas-and-identities) |
| Optimization and control | [Optimization, operations research and control](../subjects/optimization/optimization-and-control.md#important-formulas-and-identities) |
| Topology | [Topology: continuity, shape and holes](../subjects/topology/topology.md#important-formulas-and-identities) |
| Differential geometry and tensors | [Differential geometry and tensor mathematics](../subjects/differential-geometry/geometry-and-tensors.md#important-formulas-and-identities) |
| Functional analysis | [Functional analysis and operator theory](../subjects/functional-analysis/functional-analysis.md#important-formulas-and-identities) |
| Transforms and special functions | [Harmonic analysis, transforms, and special functions](../subjects/harmonic-analysis/transforms-and-special-functions.md#important-formulas-and-identities) |
| Applied mathematics and modeling | [Applied mathematics and mathematical modeling](../subjects/applied-mathematics/modeling.md#important-formulas-and-identities) |
