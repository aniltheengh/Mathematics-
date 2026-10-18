# Differential geometry and tensor mathematics

**Topic ID:** DG-001  
**Classification:** Differential geometry → manifolds → tensor fields  
**Level:** Upper undergraduate with advanced introductions  
**Content status:** Written compact reference; global theorems are cited rather than fully proved.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Conics II: tangents, normals, curvature, and reflection](../../lessons/geometry/conics-tangents-and-reflection.md)
<!-- guided-lessons:end -->

## Prerequisites

Multivariable calculus, linear maps, dual vectors, differential equations and [topology](../topology/topology.md) are needed. Diagnostic: polar coordinates satisfy $x=r\cos\theta$, $y=r\sin\theta$; a displacement in the angular coordinate has length $r\,d\theta$, not $d\theta$ metres. Coordinate components and physical measurements must be distinguished.

## Definition

A **smooth manifold** is a Hausdorff, second-countable topological manifold with an atlas of coordinate charts whose transition maps are smooth. The charts represent neighborhoods by open subsets of $\mathbb R^n$; they do not turn a curved surface into one global Cartesian coordinate system. At $p$, a **tangent vector** can be defined as a derivation on smooth functions, a linear map $v$ satisfying $v(fg)=f(p)v(g)+g(p)v(f)$. Tangent vectors form the vector space $T_pM$. Its dual $T_p^*M$ is the **cotangent space**.

A type-$(r,s)$ **tensor** at $p$ is a multilinear map taking $r$ covectors and $s$ vectors to a scalar. Its coordinate expression has $r$ upper and $s$ lower indices. A **tensor field** assigns such objects smoothly to points. Components change with coordinates; the underlying multilinear object does not. A Riemannian metric is a smooth positive-definite symmetric type-$(0,2)$ tensor $g$ that measures squared lengths.

## Intuitive explanation

Coordinates are labels, while tensors express operations independent of those labels. A physical displacement has different components in Cartesian and polar coordinates, but the squared length computed with the matching metric agrees. A connection tells us how vectors at neighboring points are compared. Curvature records the failure of parallel transport to return a vector unchanged around a sufficiently small loop.

![A circular helix of radius two and pitch parameter one, with a radius reference.](../../assets/figures/advanced/helix.png)

This curve has nonzero curvature and torsion. Its parameter is dimensionless; the displayed coordinates have length units. The equal axis scale avoids distorting its radius and rise.

## Mathematical notation

Coordinates are $x^1,\ldots,x^n$; repeated upper–lower index pairs are summed. $\partial_i=\partial/\partial x^i$ is a coordinate tangent basis and $dx^i$ its dual. $g_{ij}$ are metric components and $g^{ij}$ entries of the inverse matrix. $\nabla$ is a connection, $\Gamma^k_{ij}$ its coordinate coefficients, and $s$ arc length. For surfaces, $I$ and $II$ denote first and second fundamental forms. Curvature sign conventions differ across sources; the convention below is specified locally.

## Fundamental properties

For a regular curve $\mathbf r(t)\in\mathbb R^3$, meaning $\mathbf r'(t)\ne0$, speed is $v=\|\mathbf r'\|$, $ds=v\,dt$, and unit tangent $T=d\mathbf r/ds$. Where $dT/ds\ne0$, curvature is $\kappa=\|dT/ds\|$, principal normal $N=(dT/ds)/\kappa$ and binormal $B=T\times N$. Where the needed derivatives exist and $\mathbf r'\times\mathbf r''\ne0$,

$$\kappa=\frac{\|\mathbf r'\times\mathbf r''\|}{\|\mathbf r'\|^3},\qquad
\tau=\frac{\det(\mathbf r',\mathbf r'',\mathbf r''')}{\|\mathbf r'\times\mathbf r''\|^2}.$$

The Frenet equations are $T_s=\kappa N$, $N_s=-\kappa T+\tau B$ and $B_s=-\tau N$. If curvature vanishes, this Frenet frame can fail even though the curve remains smooth.

For a regular parametrized surface $\mathbf r(u,v)$, take $n=(\mathbf r_u\times\mathbf r_v)/\|\mathbf r_u\times\mathbf r_v\|$. The first fundamental form is $I=E\,du^2+2F\,du\,dv+G\,dv^2$, with $E=\mathbf r_u\cdot\mathbf r_u$, $F=\mathbf r_u\cdot\mathbf r_v$, $G=\mathbf r_v\cdot\mathbf r_v$. The second is $II=e\,du^2+2f\,du\,dv+g\,dv^2$, with $e=n\cdot\mathbf r_{uu}$, $f=n\cdot\mathbf r_{uv}$, $g=n\cdot\mathbf r_{vv}$. Principal curvatures are the eigenvalues of $I^{-1}II$ in this convention; reversing the normal reverses their signs but not their product.

## Important formulas and identities

Under $x\mapsto x'$, vector and covector components transform as

$$v'^i=\frac{\partial x'^i}{\partial x^j}v^j,\qquad
\alpha'_i=\frac{\partial x^j}{\partial x'^i}\alpha_j.$$

Their contraction $\alpha_i v^i$ is invariant by the chain rule. A metric lowers an index: $v_i=g_{ij}v^j$, and its inverse raises one: $v^i=g^{ij}v_j$. Raising an index is not simply moving its printed position. A type-$(1,1)$ tensor contracts to $T^i{}_i$, its coordinate-independent trace.

The **Levi-Civita connection** is the unique metric-compatible, torsion-free connection of a smooth Riemannian metric. Its coefficients are

$$\Gamma^k_{ij}=\tfrac12g^{k\ell}(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}).$$

For a vector field, $\nabla_i v^k=\partial_i v^k+\Gamma^k_{ij}v^j$; a covector has the opposite connection sign, $\nabla_i\alpha_j=\partial_i\alpha_j-\Gamma^k_{ij}\alpha_k$. Connection coefficients themselves are not tensor components. A geodesic parametrized affinely satisfies

$$\ddot x^k+\Gamma^k_{ij}\dot x^i\dot x^j=0.$$

Geodesics are locally stationary paths for energy; a long geodesic need not be globally shortest. With convention $R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z$, curvature is a type-$(1,3)$ tensor. Gaussian curvature of a surface is $K=(eg-f^2)/(EG-F^2)$; for a sphere of radius $R$, $K=1/R^2$, independent of coordinates. A cylinder has $K=0$ even though it bends in ambient space.

A **differential $k$-form** is an alternating covariant tensor field. The wedge product is alternating: $dx^i\wedge dx^j=-dx^j\wedge dx^i$. The exterior derivative obeys $d^2=0$. On an oriented smooth $n$-manifold with boundary and a smooth compactly supported $(n-1)$-form $\omega$,

$$\int_Md\omega=\int_{\partial M}\omega$$

with the induced boundary orientation. This general Stokes theorem unifies circulation and flux formulas; its full proof is deferred. Riemannian volume is $\sqrt{\det g}\,dx^1\cdots dx^n$ in an oriented chart with compatible orientation.

**Advanced geometries.** Riemannian geometry combines smooth structure and positive-definite metric. **Symplectic geometry** uses a closed nondegenerate two-form $\omega$, so its dimension is even. In coordinates $(q,p)$, $\omega=dq\wedge dp$ and the convention $\iota_{X_H}\omega=dH$ gives Hamilton equations $\dot q=H_p$, $\dot p=-H_q$. A **Lie group** is a smooth manifold whose multiplication and inversion are smooth. For rotations $SO(3)=\{R:R^TR=I,\det R=1\}$, tangent vectors at the identity are skew-symmetric matrices; the matrix commutator $[A,B]=AB-BA$ supplies the Lie algebra bracket. Rotations about distinct axes generally do not commute.

## Derivations and proofs

**Polar metric.** Differentiate $x=r\cos\theta$, $y=r\sin\theta$. Squaring and adding gives

$$dx^2+dy^2=dr^2+r^2d\theta^2,$$

because the mixed terms cancel and $\sin^2\theta+\cos^2\theta=1$. Thus $g=\operatorname{diag}(1,r^2)$ on $r>0$, $g^{-1}=\operatorname{diag}(1,r^{-2})$ and $\sqrt{\det g}=r$. Substituting into the connection formula gives $\Gamma^r_{\theta\theta}=-r$ and $\Gamma^\theta_{r\theta}=\Gamma^\theta_{\theta r}=1/r$, with other coefficients zero. These coefficients are nonzero in the flat Euclidean plane: nonzero connection coefficients alone do not imply curvature.

**Invariant contraction.** Multiply the transformation laws for $\alpha'_i$ and $v'^i$. The factor $(\partial x^j/\partial x'^i)(\partial x'^i/\partial x^k)=\delta^j_k$ by invertibility of the coordinate change, leaving $\alpha_jv^j$. This justifies the upper–lower summation convention geometrically.

## Worked examples

**1. A helix.** Let $\mathbf r(t)=(2\cos t,2\sin t,t)$. Then $\|\mathbf r'\|=\sqrt5$ and $\mathbf r'\times\mathbf r''=(2\sin t,-2\cos t,4)$, whose norm is $2\sqrt5$. Therefore $\kappa=2/5$. The triple product is $4$ and the cross-product norm squared is $20$, so $\tau=1/5$. If coordinates are metres, these have units $\mathrm m^{-1}$. One turn has arc length $2\pi\sqrt5\ \mathrm m$.

**2. Polar vector length.** At $r=3\ \mathrm m$, a tangent displacement with coordinate components $(dr,d\theta)=(0.2\ \mathrm m,0.1)$ has squared length $0.2^2+3^2(0.1)^2=0.13\ \mathrm m^2$. Its length is $\sqrt{13}/10\ \mathrm m$. Treating the coordinate pair as Cartesian would omit the factor $r^2$ and give the wrong units and magnitude.

**3. A great circle.** On a sphere, $g=R^2\operatorname{diag}(1,\sin^2\theta)$ in colatitude–longitude coordinates away from the poles. The equator $\theta=\pi/2$, $\phi=ct$ solves the geodesic equations: its radial-in-chart acceleration term involves $\sin\theta\cos\theta=0$. A non-equatorial latitude generally fails that equation, so circles on a sphere need not be geodesics.

**4. A form integral.** On the unit disk take $\omega=(-y\,dx+x\,dy)/2$. Then $d\omega=dx\wedge dy$. The counterclockwise boundary $(\cos t,\sin t)$ yields $\omega=dt/2$, so $\int_{\partial D}\omega=\pi$, equal to $\int_Ddx\,dy$. The orientation fixes the sign.

## Practice problems

1. Find curvature and torsion of a circle $(R\cos t,R\sin t,0)$, $R>0$.
2. In polar coordinates, lower the index of a vector with components $v^i=(a,b)$.
3. Why is longitude singular at a sphere's pole without the sphere itself being singular?
4. For $H=(p^2+q^2)/2$ with $\omega=dq\wedge dp$, find the Hamilton equations and show energy is constant.

## Answers and explanations

1. $\kappa=1/R$, $\tau=0$. The curve turns in a plane and its binormal is constant.
2. $v_i=(a,r^2b)$, since $v_i=g_{ij}v^j$. The coordinate basis for angular motion is not a unit basis.
3. All longitudes name the same pole; that chart loses invertibility there. Another chart describes a smooth neighborhood, so the defect belongs to coordinates.
4. $\dot q=p$, $\dot p=-q$. Then $dH/dt=q\dot q+p\dot p=qp-pq=0$. The motion stays on a constant-energy circle in phase space.

## Common mistakes and misconceptions

An array is not automatically a tensor; it needs the transformation law. Partial derivatives of vector components alone are not covariant derivatives in changing bases. A coordinate singularity need not be physical. Gaussian curvature and curve curvature are different objects. A geodesic can stop minimizing after sufficient extension, as a long great-circle arc demonstrates.

## Connections to other mathematics

[Topology](../topology/topology.md) supplies manifolds and global invariants. [Functional analysis](../functional-analysis/functional-analysis.md) supports differential operators on manifolds. [Modeling](../applied-mathematics/modeling.md) uses tensors for stress, strain and coordinate-invariant conservation.

## Applications

A stress tensor maps oriented surface normals to traction; changing axes changes its components while preserving the physical mapping. Surface geometry enters shell models and membrane curvature. Rigid-body orientation lives on $SO(3)$ rather than a flat three-dimensional coordinate box, explaining both noncommuting rotations and the need for coordinate care in robotics.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) generates the helix with equal geometric scale. [Checks](../../scripts/verify_advanced.py) verify its curvature and torsion, polar metric and connection coefficients, and the disk integral. General manifold theorems require proofs beyond these calculations.

## References and recommended reading

- David Tong, [*General Relativity*](https://www.damtp.cam.ac.uk/user/tong/gr.html), chapters “Introducing Differential Geometry” and “Introducing Riemannian Geometry”: tensors, forms, connections and curvature. The author supplies both PDF and HTML versions.
- MIT OpenCourseWare, [18.357 Interfacial Phenomena](https://ocw.mit.edu/courses/18-357-interfacial-phenomena-fall-2010/), curvature-pressure and surface notes: an applied follow-up.

## Revision and mastery status

Written 2026-10-18. The subject-map scope is covered at reference depth, with conventions and local calculations explicit. Full global Riemannian, symplectic and Lie-group theory remains further study. Mastery requires computing an invariant in two coordinate systems and identifying where a chosen chart is valid.
