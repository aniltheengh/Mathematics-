# Complex analysis

**Topic ID:** CA-01.  
**Classification:** Analysis → holomorphic functions and contour methods.  
**Level:** Undergraduate, with an advanced continuation bridge.  
**Content status:** Written compact reference chapter.  
**Learner mastery:** Unassessed.

## Prerequisites

Know real calculus, power series, and line integrals. Diagnostic: $(1+i)^2=2i$, $|1+i|=\sqrt2$, and one argument is $\pi/4$. Arguments differing by $2\pi k$, $k\in\mathbb Z$, represent the same direction. Treating the argument as globally single-valued creates false logarithm identities.

## Definition

A complex number is $z=x+iy$, where $x,y\in\mathbb R$ and $i^2=-1$. Its modulus is $|z|=\sqrt{x^2+y^2}$ and conjugate is $\bar z=x-iy$. A function on an open set is **holomorphic** if the complex derivative

$$f'(z)=\lim_{h\to0,\,h\in\mathbb C}\frac{f(z+h)-f(z)}h$$

exists at every point. The increment approaches from all complex directions. A function is **analytic** if it has a convergent local power series; a central theorem says holomorphic and analytic are equivalent. This equivalence is cited below, rather than assumed as a definition.

## Intuitive explanation

Complex differentiability requires a real two-dimensional map to behave locally like one complex multiplication: the same scaling and rotation in every direction. This rigidity makes an integral over a contour determine values throughout its interior. Singularities store information in Laurent coefficients; the coefficient of $(z-a)^{-1}$ controls a closed contour integral. Branches record which locally consistent value of a multivalued expression has been chosen.

![The image of a Cartesian grid under the square map](../../assets/figures/analysis/complex-square-map.png)

The exact map is $w=z^2$: $\operatorname{Re}w=x^2-y^2$, $\operatorname{Im}w=2xy$. Both panels use equal scales and dimensionless coordinates. The left panel restricts $1/4\le x\le3/2$, $-1\le y\le1$ so it avoids the critical point zero; the right shows the corresponding grid curves. At a regular crossing, perpendicular source lines remain perpendicular in the image.

## Mathematical notation

$\operatorname{Re}z=x$, $\operatorname{Im}z=y$, and $z=re^{i\theta}=r(\cos\theta+i\sin\theta)$ for $r>0$. $\operatorname{Res}(f,a)$ is the residue at $a$. Contours are oriented, piecewise continuously differentiable paths; positive orientation around a simple region is counterclockwise. The principal logarithm uses $-\pi<\operatorname{Arg}z<\pi$ on the slit plane $\mathbb C\setminus(-\infty,0]$, and $\operatorname{Log}z=\log|z|+i\operatorname{Arg}z$ there.

## Fundamental properties

Writing $f=u+iv$ with continuously differentiable real components, holomorphicity is equivalent to the **Cauchy–Riemann equations** $u_x=v_y$, $u_y=-v_x$. The regularity qualifier matters: equations holding at an isolated point alone do not establish neighborhood analyticity. For a holomorphic function, $f'=u_x+iv_x$. If second derivatives are continuous, differentiating the equations gives $\Delta u=\Delta v=0$, so real and imaginary parts are harmonic.

**Cauchy integral theorem, cited without full proof.** A holomorphic function on a simply connected open domain has integral zero around every closed contour in that domain. A hole containing a singularity can invalidate the conclusion. **Identity theorem, cited:** two holomorphic functions on a connected domain that agree on a set with an interior accumulation point agree everywhere in that domain. Equality merely on a sequence accumulating outside the domain is insufficient.

A holomorphic map with $f'(z_0)\ne0$ is locally conformal: it preserves oriented angles between smooth curves through $z_0$. It need not be globally one-to-one. A harmonic function locally has a harmonic conjugate on a disk, yielding a holomorphic function; a global conjugate can fail on a domain with holes. For example $\log|z|$ is harmonic off zero, but its conjugate angle cannot be chosen continuously around the whole punctured plane.

## Important formulas and identities

If $z\ne0$ has polar form $re^{i\theta}$, its $n$th roots, for integer $n\ge1$, are

$$r^{1/n}\exp\!\left(\frac{i(\theta+2\pi k)}n\right),\qquad k=0,\ldots,n-1.$$

For $f$ holomorphic on a neighborhood of a positively oriented simple contour and its interior, and $a$ inside,

$$f^{(n)}(a)=\frac{n!}{2\pi i}\oint\frac{f(z)}{(z-a)^{n+1}}dz.$$

This Cauchy formula gives the Taylor coefficients $f^{(n)}(a)/n!$ and bounds $|f^{(n)}(a)|\le n!M/R^n$ on a circle of radius $R$ with $|f|\le M$. Expanding the Cauchy kernel geometrically proves local power-series representation; this is the mechanism behind holomorphic implying analytic, with the uniform convergence justification part of the full theorem.

On an annulus, a holomorphic function has a **Laurent series** $\sum_{n=-\infty}^\infty c_n(z-a)^n$. At an isolated singularity, no negative terms means removable; finitely many negative terms means a pole; infinitely many means essential. The residue is $c_{-1}$. At a simple pole of $g/h$ where $h(a)=0$ and $h'(a)\ne0$, it equals $g(a)/h'(a)$. For a pole of order $m$,

$$\operatorname{Res}(f,a)=\frac1{(m-1)!}\left[\frac{d^{m-1}}{dz^{m-1}}((z-a)^m f(z))\right]_{z=a}.$$

The residue theorem gives $\oint_Cf(z)dz=2\pi i\sum_a\operatorname{Res}(f,a)$ for a positively oriented simple contour enclosing finitely many isolated singularities and no singularities on the contour, with holomorphicity elsewhere in its interior.

## Derivations and proofs

**Necessity of Cauchy–Riemann.** Approach the derivative along real increments: the limit is $u_x+iv_x$. Along imaginary increments it is $(u_y+iv_y)/i=v_y-iu_y$. Equating real and imaginary parts gives the equations. Conversely, real differentiability plus these equations makes the real linear derivative complex multiplication, so the required complex derivative exists. Continuous partial derivatives ensure the real differentiability used here.

**Integral of a simple reciprocal.** Parameterize $z=a+Re^{it}$, $0\le t\le2\pi$. Then $dz=iRe^{it}dt$, so $\oint dz/(z-a)=2\pi i$. Integrating $(z-a)^n$ similarly gives zero for every integer $n\ne-1$. Termwise integration of a uniformly convergent Laurent series on a circle therefore isolates exactly its residue. The general residue theorem additionally uses contour deformation/Cauchy theorem; that global step is cited.

**Branches and continuation.** On the slit plane, differentiating $\operatorname{Log}z$ gives $1/z$ and exponentiating recovers $z$. There is no holomorphic logarithm on all of $\mathbb C\setminus\{0\}$: such a logarithm would make $1/z$ a derivative and force its closed integral to zero, contradicting $2\pi i$. On the slit plane, a square root is $e^{\operatorname{Log}z/2}$; analytically continuing this local choice once around zero in the punctured plane changes its sign.

Analytic continuation extends local holomorphic formulas across overlapping disks, agreeing on overlaps by the identity theorem. The series $\sum_{n\ge0}z^n$ initially represents $1/(1-z)$ only for $|z|<1$; the rational expression continues the function to $\mathbb C\setminus\{1\}$. Continued values can depend on the path when branch points are present. A **Riemann surface** replaces such incompatible sheets by a space with local complex coordinates on which the function becomes single-valued. For $w^2=z$, use $w$ as a local coordinate near the branch point and projection $w\mapsto w^2$ to the $z$ plane; away from zero the projection has two sheets. This is a construction example, not a full theorem on continuation surfaces.

## Worked examples

**1. Cube roots.** Solve $z^3=8i$. Use $8i=8e^{i\pi/2}$. Roots have radius two and angles $\pi/6,5\pi/6,3\pi/2$, giving $\sqrt3+i$, $-\sqrt3+i$, and $-2i$. Cubing the last gives $8i$; the other two follow by multiplying a root by cube roots of unity. There are three distinct roots because the polynomial has degree three and these are distinct.

**2. A contour integral.** Calculate $\oint_{|z|=2} dz/[z(z-1)]$ counterclockwise. The simple poles are zero and one. Residues are $-1$ and $1$, respectively, so the integral is zero. Partial fractions $-1/z+1/(z-1)$ independently explain the cancellation: each reciprocal contributes the same $2\pi i$ with opposite coefficients.

**3. A real improper integral by residues.** For $\int_{-\infty}^\infty dx/(x^2+1)$, close in the upper half-plane. The sole upper pole is $i$, with residue $1/(2i)$. On a semicircle of radius $R>1$, the arc integral magnitude is at most $\pi R/(R^2-1)\to0$. Therefore the real integral is $2\pi i/(2i)=\pi$. The arc estimate is necessary; closing a contour does not automatically make its extra part vanish.

**4. Laurent regions.** For $f(z)=1/[z(z-1)]$, around zero with $0<|z|<1$, geometric expansion gives $f=-1/z-1-z-z^2-\cdots$. For $|z|>1$, it instead gives $f=z^{-2}+z^{-3}+\cdots$. These different annuli explain why their $z^{-1}$ coefficients differ; residues at a point use the local punctured neighborhood, not an arbitrary distant annulus.

## Practice problems

1. Is $f(z)=\bar z$ holomorphic anywhere?
2. Evaluate $\oint_{|z|=1}e^z/z^2\,dz$ counterclockwise.
3. Classify the isolated singularity of $e^{1/z}$ at zero and find its residue.
4. Evaluate the principal logarithm of $-i$ and explain why principal logarithms need not satisfy $\operatorname{Log}(zw)=\operatorname{Log}z+\operatorname{Log}w$.

## Answers and explanations

1. No. For $u=x,v=-y$, the equation $u_x=v_y$ would demand $1=-1$. Equivalently the directional difference quotients disagree everywhere.
2. Cauchy's derivative formula with $f=e^z$, $a=0$ gives $2\pi i f'(0)=2\pi i$.
3. Expansion $e^{1/z}=1+1/z+1/(2!z^2)+\cdots$ contains infinitely many negative powers, so the singularity is essential. The residue is one.
4. $\operatorname{Log}(-i)=-i\pi/2$. For instance $z=w=e^{3\pi i/4}$ are in the slit domain and $zw=-i$; the sum of their principal logs is $3\pi i/2$, differing from $-i\pi/2$ by $2\pi i$. Exponentiation erases that difference.

## Common mistakes and misconceptions

The identity $|z^2|=|z|^2$ is valid, but $z^2=|z|^2$ generally is not. Cauchy–Riemann equations are not merely two unrelated algebraic tests at isolated points. A singularity on a proposed contour invalidates the ordinary residue formula. A branch cut is a domain choice, not a physical discontinuity intrinsic to every possible representation.

## Connections to other mathematics

[Harmonic analysis](../harmonic-analysis/transforms-and-special-functions.md) uses complex exponentials and contour inversion. [PDEs](../differential-equations/partial-differential-equations.md) use harmonic functions for potential fields. Real two-dimensional conformality is explained by the Jacobian in [multivariable calculus](../calculus/multivariable-and-vector-calculus.md).

## Applications

In planar irrotational incompressible flow on a suitable domain, a complex potential combines a velocity potential and stream function as harmonic conjugates. The flow assumptions, boundary conditions, and derivative convention must be specified before interpreting $f'$. Phasors also encode sinusoidal amplitude and phase, but their physical quantity is recovered by taking the appropriate real part after multiplying by $e^{i\omega t}$.

## Optional computational examples

[plot_analysis.py](../../scripts/plot_analysis.py) maps the exact Cartesian grid under $z^2$. [verify_analysis.py](../../scripts/verify_analysis.py) checks roots, residues, Cauchy–Riemann derivatives, Laurent coefficients, and the real integral. A plotted grid illustrates local angle preservation but does not prove global conformality.

## References and recommended reading

Source and further study: Jiří Lebl, [Guide to Cultivating Complex Analysis](https://www.jirka.org/ca/), holomorphic functions, integration, power series, residues, and analytic continuation. The chapter supplies elementary derivations and distinguishes the unproved global complex-analysis theorems from those derivations.

## Revision and mastery status

Written 2026-10-18. Scope: a compact first complex-analysis reference with an explicit branches/surfaces introduction. Mastery requires checking holomorphicity with hypotheses, choosing a contour, bounding its added arcs, and declaring branches. No learner assessment has been entered.
