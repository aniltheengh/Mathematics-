# Multivariable and vector calculus

**Topic ID:** MVC-01.  
**Classification:** Analysis → several variables and vector fields.  
**Level:** Undergraduate.  
**Content status:** Written compact reference chapter.  
**Learner mastery:** Unassessed.

## Prerequisites

Use [single-variable calculus](single-variable-calculus.md), vectors, matrices, and [linear maps](../linear-algebra/linear-algebra.md). Diagnostic: for $f(x,y)=x^2+3y$, holding $y$ fixed gives $f_x=2x$ and holding $x$ fixed gives $f_y=3$. Partial derivatives describe selected directions; by themselves they do not guarantee a good linear approximation in every direction.

## Definition

A function $f:U\subseteq\mathbb R^n\to\mathbb R^m$, with $U$ open, is **differentiable** at $a$ if a linear map $Df(a)$ satisfies

$$f(a+h)=f(a)+Df(a)h+o(\|h\|).$$

Its matrix is the **Jacobian**, $J_{ij}=\partial f_i/\partial x_j$. For scalar $f$, the gradient $\nabla f$ is the column of partial derivatives, representing $Df$ through the Euclidean inner product. A **vector field** assigns a vector $F(x)$ to each point. Its line integral $\int_C F\cdot dr$ accumulates its tangential component along an oriented curve.

## Intuitive explanation

A surface can rise differently along different directions. Differentiability says a single tangent plane explains all small displacements at once. The gradient points toward greatest first-order increase per unit distance in a Euclidean coordinate system. A divergence measures local outward flux density; a curl measures local circulation density. Integral theorems turn a sum over a boundary into a sum over the enclosed region, provided orientations and regularity match.

![Contours of a quadratic potential and its gradient](../../assets/figures/analysis/gradient-contours.png)

The exact potential is $f(x,y)=x^2+2y^2$, and arrows show $\nabla f=(2x,4y)$. Coordinates and potential are dimensionless. Arrows are drawn from exact component formulas; their displayed lengths use a stated plotting scale rather than implying a new vector field.

## Mathematical notation

$D_uf=\nabla f\cdot u$ assumes a unit direction $\|u\|=1$ and differentiability. The Hessian $H_f$ has entries $f_{x_ix_j}$; it is symmetric if second partial derivatives are continuous. For $F=(P,Q,R)$, $\nabla\cdot F=P_x+Q_y+R_z$ and $\nabla\times F=(R_y-Q_z,P_z-R_x,Q_x-P_y)$. The measure $dV$ denotes volume and $dS$ surface area; $n$ is a chosen unit normal. A positive planar boundary orientation is counterclockwise with the region on the left.

## Fundamental properties

Continuity means $\|f(x)-f(a)\|\to0$ whenever $\|x-a\|\to0$, independently of path. Different path limits disprove a limit; matching a few paths cannot prove it. For instance $xy/(x^2+y^2)$ tends to zero on either axis but to $1/2$ on $y=x$, so its limit at zero fails.

The chain rule is $D(g\circ f)(a)=Dg(f(a))Df(a)$. **Inverse function theorem, cited without proof:** if $f$ is continuously differentiable near $a$ and $\det Df(a)\ne0$, it has a continuously differentiable local inverse with derivative $(Df(a))^{-1}$. **Implicit function theorem, cited without proof:** for continuously differentiable $F(x,y)$ with invertible derivative in the $y$ variables at a zero, one can solve locally for a differentiable $y=g(x)$ and $Dg=-F_y^{-1}F_x$. These are local results, not global injectivity claims.

At an interior differentiable local extremum, $\nabla f=0$. A positive-definite Hessian gives a strict local minimum and a negative-definite Hessian a strict local maximum. An indefinite Hessian gives a saddle. A semidefinite Hessian alone is inconclusive, as $x^4+y^4$ and $x^4-y^4$ illustrate.

For a smooth equality constraint $g(x)=c$ with $\nabla g\ne0$, a constrained stationary point satisfies $\nabla f=\lambda\nabla g$: every tangent displacement must annihilate the derivative of $f$, so its gradient is normal to the constraint. This necessary condition does not prove a minimum and can miss singular constraint points where the gradient vanishes. On a compact closed region, global extrema exist for continuous $f$; check interior stationary points and all relevant boundary pieces, including corners. Comparing their actual values is the final step.

## Important formulas and identities

For an injective smooth coordinate change $x=\Phi(u)$ with nonsingular derivative, up to suitable boundaries,

$$\int_{\Phi(D)} f(x)\,dx=\int_D f(\Phi(u))|\det D\Phi(u)|\,du.$$

Polar area is $dA=r\,dr\,d\theta$ for $r\ge0$; cylindrical volume is $r\,dr\,d\theta\,dz$; spherical volume is $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$, with $\rho\ge0$ and polar angle $0\le\phi\le\pi$. The absolute determinant is required for volume; orientation-sensitive integrals retain its sign.

For a piecewise smooth parameterized path $r(t)$,

$$\int_C F\cdot dr=\int_a^b F(r(t))\cdot r'(t)dt.$$

For a smooth surface parameterization $r(u,v)$, flux is $\iint F(r)\cdot(r_u\times r_v)\,du\,dv$; scalar area integration uses $\|r_u\times r_v\|$. A conservative field $F=\nabla\varphi$ has path integral $\varphi(B)-\varphi(A)$. A continuously differentiable curl-free field is conservative on a simply connected open domain, but this conclusion can fail around a hole.

## Derivations and proofs

**Fundamental theorem for line integrals.** If $F=\nabla\varphi$ and the path is piecewise continuously differentiable, the ordinary chain rule gives

$$\frac d{dt}\varphi(r(t))=\nabla\varphi(r(t))\cdot r'(t).$$

Integrating on every smooth piece and cancelling internal endpoints yields $\int_C F\cdot dr=\varphi(r(b))-\varphi(r(a))$. This proves path independence for gradient fields.

**Green's theorem for a rectangle.** Suppose $P,Q$ have continuous first partial derivatives on the rectangle $D=[a,b]\times[c,d]$. The two horizontal edge integrals of $P\,dx$ sum to $\int_a^b[P(x,c)-P(x,d)]dx=-\iint_D P_y\,dA$. The two vertical edge integrals of $Q\,dy$ sum to $\int_c^d[Q(b,y)-Q(a,y)]dy=\iint_DQ_x\,dA$. Adding proves $\oint_{\partial D}Pdx+Qdy=\iint_D(Q_x-P_y)dA$. The general piecewise smooth-domain theorem follows by approximation under suitable regularity; that extension is cited, not proved here.

The three standard boundary theorems, under piecewise smooth boundaries and continuously differentiable fields on a neighborhood of the region, are

$$\oint_{\partial D}(Pdx+Qdy)=\iint_D(Q_x-P_y)dA,$$
$$\iint_{\partial V}F\cdot n\,dS=\iiint_V\nabla\cdot F\,dV,$$
$$\oint_{\partial S}F\cdot dr=\iint_S(\nabla\times F)\cdot n\,dS.$$

The second uses outward normals; the third uses the right-hand orientation. Their general proofs are omitted. In differential forms language, a $k$-form is an alternating multilinear function on $k$ tangent vectors, with coefficient functions varying over position. The exterior derivative $d$ raises degree and satisfies $d^2=0$. The unified theorem is $\int_Md\omega=\int_{\partial M}\omega$ for a smooth compact oriented manifold with boundary and a sufficiently smooth form. For example, $d(Pdx+Qdy)=(Q_x-P_y)dx\wedge dy$, recovering Green's theorem. The geometry of forms is developed further in the subject map's differential geometry branch.

## Worked examples

**1. Direction and sensitivity.** For $f=x^2+2y^2$, at $(1,1)$ the gradient is $(2,4)$. In the direction $(3,4)$, first normalize: $u=(3/5,4/5)$. Then $D_uf=22/5$. Along $r(t)=(1,1)+tu$, expand exactly: $f(r(t))=3+(22/5)t+(41/25)t^2$. Its derivative at zero confirms the directional calculation.

**2. Polar change of variables.** Integrate $x^2+y^2$ over the disk $x^2+y^2\le4$. Polar coordinates give $\int_0^{2\pi}\int_0^2r^2r\,dr\,d\theta=8\pi$. The mean value over the disk is $8\pi/(4\pi)=2$, between its minimum zero and maximum four. Omitting the extra $r$ would fail the area scaling.

**3. Circulation checked two ways.** Set $F=(-y,x,0)$ and take the unit circle counterclockwise in $z=0$. Parameterize $r=(\cos t,\sin t,0)$, $0\le t\le2\pi$. Then $F(r)=r'$ and $F\cdot r'=1$, giving $2\pi$. Independently $\nabla\times F=(0,0,2)$, so flux through the upward unit disk is $2\pi$ by Stokes.

**4. An implicit curve.** For $x^2+xy+y^2=3$ near $(1,1)$, $F_y=x+2y=3\ne0$. Thus $y'=-(2x+y)/(x+2y)$, giving $-1$ there. The tangent is $x+y=2$. The normal $(3,3)$ agrees with the gradient of the defining function.

## Practice problems

1. Find and classify the critical point of $x^2+2y^2-2x+4y$.
2. Compute the volume of the unit ball using spherical coordinates.
3. Calculate outward flux of $F=(x,y,z)$ through the sphere of radius two.
4. Explain why $F=(-y/(x^2+y^2),x/(x^2+y^2))$ is not conservative on $\mathbb R^2\setminus\{0\}$ even though its scalar curl vanishes there.

## Answers and explanations

1. Solving $(2x-2,4y+4)=0$ gives $(1,-1)$. Completing squares gives $(x-1)^2+2(y+1)^2-3$, proving a global minimum of $-3$.
2. $\int_0^{2\pi}\int_0^\pi\int_0^1\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=4\pi/3$. The factor $\sin\phi$ accounts for shrinking latitude circles.
3. Divergence is three and the enclosed volume is $32\pi/3$, so flux is $32\pi$. Directly, $F\cdot n=2$ and sphere area is $16\pi$.
4. On the unit circle the integrand is one under the usual angle parameter, hence circulation is $2\pi$. A gradient would have zero closed-path integral. The punctured domain's hole invalidates the simply connected hypothesis.

## Common mistakes and misconceptions

Directional derivatives require unit vectors to represent rate per unit distance. Existing partial derivatives need not imply differentiability. Volume Jacobians use an absolute value; oriented flux does not replace a normal with its magnitude. Reversing a curve's orientation changes circulation's sign. Applying divergence theorem across a singularity without excluding it can produce a false zero flux.

## Connections to other mathematics

[Linear algebra](../linear-algebra/linear-algebra.md) supplies Hessian definiteness and Jacobian invertibility. [PDEs](../differential-equations/partial-differential-equations.md) use divergence to express conservation. [Real analysis](../analysis/real-analysis-and-measure.md) supplies conditions for iterated integration and exchange of limits.

## Applications

If $T(x,y,z)$ is temperature in kelvins and position in metres, $\nabla T$ has units K/m. Isotropic conduction uses $q=-k\nabla T$, with conductivity $k$ in W/(m·K), giving heat flux $q$ in W/m². Divergence theorem converts net outward heat flow to a volume integral; a heat source and stored energy then enter the balance. The minus sign follows flow toward lower temperature, not an orientation convention.

## Optional computational examples

[plot_analysis.py](../../scripts/plot_analysis.py) draws gradient contours. [verify_analysis.py](../../scripts/verify_analysis.py) checks the directional expansion, disk integral, implicit derivative, circulation, and flux using exact expressions. A grid cannot test all paths in a multivariable limit.

## References and recommended reading

Source and further study: Gilbert Strang and Edwin Herman, OpenStax [Calculus Volume 3](https://openstax.org/details/books/calculus-volume-3), partial derivatives, multiple integration, and vector calculus. For rigorous local inverse results, Jiří Lebl, [Basic Analysis, Volume II](https://www.jirka.org/ra/), several-variable differentiation. General manifold Stokes is stated as an advanced theorem, not proved here.

## Revision and mastery status

Written 2026-10-18. Scope: a compact reference through the classical integral theorems, with a differential-forms bridge. Mastery requires checking a total derivative, selecting integration coordinates, and declaring orientations before applying a boundary theorem. No assessment has yet been recorded.
