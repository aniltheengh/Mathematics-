# Linear algebra and multilinear algebra

**Topic ID:** LA-01.  
**Classification:** Linear algebra → finite-dimensional spaces and multilinear constructions.  
**Level:** Undergraduate, with an advanced bridge.  
**Content status:** Written compact reference chapter.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [Linear maps, bases, and least squares](../../lessons/analysis/linear-algebra-and-least-squares.md)
<!-- guided-lessons:end -->

## Prerequisites

Use real and complex arithmetic, simultaneous equations, and functions. Diagnostic: solve $x+y=3$, $x-y=1$; the answer is $(2,1)$. A vector is an object that can be added and scaled; its coordinates depend on a chosen basis. This distinction is essential before tensors. Geometric coordinates are introduced in the [Cartesian plane chapter](../geometry/coordinate-geometry/cartesian-plane.md).

## Definition

A **vector space** over a field $\mathbb F$ is a set with addition and scalar multiplication satisfying the usual associative, commutative, distributive, identity, and inverse axioms. Here $\mathbb F=\mathbb R$ or $\mathbb C$, and spaces are finite-dimensional unless stated otherwise. A **linear map** $T:V\to W$ satisfies $T(au+bv)=aT(u)+bT(v)$. A matrix represents such a map after choosing ordered bases. Its columns are the output coordinates of the input basis vectors.

A list spans $V$ when every vector is a linear combination of that list. It is independent when a zero linear combination forces every coefficient to vanish. A **basis** is an independent spanning list, and its length is the dimension.

## Intuitive explanation

Vectors record compatible quantities, such as spatial displacements. A matrix mixes those components predictably. Elimination asks whether prescribed outputs can be produced; eigenvectors identify directions whose lines are preserved; singular values measure stretch along perpendicular input directions. These are different questions, so their preferred factorizations differ. A projection keeps the part explainable by a subspace and places the unexplained part perpendicular to it.

![Projection of b=(2,1) onto span(1,1), with perpendicular residual](../../assets/figures/analysis/linear-projection.png)

The diagram uses dimensionless coordinates, equal axis scales, $b=(2,1)$, $p=(3/2,3/2)$, and $r=b-p=(1/2,-1/2)$. The right angle represents the exact identity $p\cdot r=0$.

## Mathematical notation

$A\in\mathbb F^{m\times n}$ has $m$ rows and $n$ columns; $A^*$ is conjugate transpose, $A^T$ ordinary transpose. Our complex inner product is $\langle u,v\rangle=u^*v$, conjugate-linear in its first argument. Write $\ker T=\{v:T(v)=0\}$ and $\operatorname{im}T=\{T(v):v\in V\}$. The Euclidean norm is $\|v\|=\sqrt{v^*v}$. The identity matrix is $I$. A dual vector $\phi\in V^*$ is a linear scalar-valued function on $V$.

## Fundamental properties

**Rank–nullity theorem.** If $T:V\to W$ is linear and $\dim V=n$, then $\dim\ker T+\dim\operatorname{im}T=n$. A proof extends a basis of the kernel to a basis of $V$; the images of the added vectors form a basis of the range. Thus a system $Ax=b$ has a solution precisely when $b$ lies in the column space; a solution is unique precisely when $\ker A=\{0\}$.

Elementary row operations preserve solution sets when applied to both sides of an augmented system. Pivot columns count rank; nonpivot variables parameterize the null space. For a square matrix, invertibility, full rank, nonzero determinant, and absence of the eigenvalue zero are equivalent.

**Finite-dimensional spectral theorem, cited without full proof.** A Hermitian matrix $A=A^*$ has an orthonormal eigenbasis and real eigenvalues. Consequently $A$ is positive definite, meaning $x^*Ax>0$ for every $x\ne0$, exactly when all its eigenvalues are positive. A general matrix can have complex eigenvalues or too few eigenvectors for diagonalization; the matrix $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ is one example.

## Important formulas and identities

For a full-column-rank matrix $A$, the least-squares solution and projection are

$$\widehat x=(A^*A)^{-1}A^*b,\qquad P=A(A^*A)^{-1}A^*,\qquad P^2=P=P^*.$$

These formulas explain the mathematics; QR or SVD is preferable in numerical work because forming $A^*A$ squares the spectral condition number. Every matrix has an **SVD**, $A=U\Sigma V^*$, with unitary $U,V$ and nonnegative diagonal singular values. The positive singular values are square roots of the nonzero eigenvalues of $A^*A$. Their number is the rank. If $A$ is $m$ by $n$, form the $n$ by $m$ matrix $\Sigma^+$ by transposing the rectangular diagonal shape, replacing each positive singular value by its reciprocal and leaving zeros unchanged. Then the Moore–Penrose inverse is $A^+=V\Sigma^+U^*$; $A^+b$ is the minimum-norm least-squares solution, including rank-deficient cases.

If $[v]_B=S[v]_C$ for bases $B,C$ of one space, then $[T]_C=S^{-1}[T]_BS$. The determinant measures signed volume scaling over $\mathbb R$, is multiplicative, and changes sign under a row swap. A real symmetric quadratic form is $q(x)=x^TAx$; rotating to orthonormal eigenvectors gives $q=\sum_i\lambda_i z_i^2$.

## Derivations and proofs

**Projection and the normal equations.** Minimize $\|b-Ax\|^2$. If $\widehat x$ satisfies $A^*(b-A\widehat x)=0$, put $r=b-A\widehat x$. For every $h$,

$$\|b-A(\widehat x+h)\|^2=\|r\|^2+\|Ah\|^2,$$

because the cross term is $-2\operatorname{Re}(h^*A^*r)=0$. Hence $\widehat x$ is a minimizer. Conversely, variation along every real and imaginary coordinate forces the same orthogonality condition. Full column rank makes $A^*A$ invertible and the minimizer unique. Without it, the fitted vector remains unique, although coefficient vectors need not.

For completeness, multilinear constructions retain this distinction between objects and coordinates. A **bilinear form** $B:V\times V\to\mathbb F$ is linear in each input separately; over $\mathbb C$ an inner product is sesquilinear instead. In a basis, $B(u,v)=u^TMv$. A basis change gives $M_C=S^TM_BS$, a congruence rather than a similarity.

The tensor product $V\otimes W$ is generated by symbols $v\otimes w$ with bilinearity relations. Its defining universal property says that every bilinear $B:V\times W\to X$ factors uniquely through a linear map $V\otimes W\to X$. If bases are $e_i,f_j$, the $e_i\otimes f_j$ form a basis, so the dimension is $(\dim V)(\dim W)$. Not every tensor is a single product: $e_1\otimes f_1+e_2\otimes f_2$ has rank two in these two-dimensional spaces.

Exterior algebra additionally imposes $v\wedge v=0$, yielding $u\wedge v=-v\wedge u$. The basis elements of $\Lambda^kV$ have strictly increasing indices, giving dimension $\binom nk$. A nonzero top-degree element chooses an orientation. Under a linear map its coefficient changes by the determinant, explaining why negative determinant reverses orientation and zero determinant collapses volume.

## Worked examples

**1. Elimination and solution structure.** Solve $x+2y=5$, $2x+4y=10$. Subtract twice the first row from the second to obtain $0=0$. Set $y=t$; then $x=5-2t$. Thus the rank is one, the nullity is one, and all solutions are $(5,0)+t(-2,1)$. Substitution verifies both equations. Replacing the second right side by $11$ gives $0=1$, hence no solution.

**2. Least-squares line.** Fit $a+bt$ to measurements $(t,y)=(0,1),(1,2),(2,2)$ with equal weights. The normal equations are

$$\begin{pmatrix}3&3\\3&5\end{pmatrix}\binom ab=\binom57.$$

Eliminating $a$ gives $2b=1$, so $b=1/2$ and $a=7/6$. The residual is $(-1/6,1/3,-1/6)$, whose dot products with $(1,1,1)$ and $(0,1,2)$ are both zero. Its squared norm is $1/6$, an independent orthogonality check.

**3. Eigenvalues and a quadratic form.** Let $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. Its characteristic polynomial is $(2-\lambda)^2-1$, giving $3,1$. Unit eigenvectors are $(1,1)/\sqrt2$ and $(1,-1)/\sqrt2$. Therefore $2x^2+2xy+2y^2=3z_1^2+z_2^2>0$ away from the origin. As a direct check, the same form equals $(x+y)^2+x^2+y^2$.

## Practice problems

1. Are $(1,2)$ and $(2,4)$ a basis of $\mathbb R^2$?
2. Project $(3,0)$ onto the line spanned by $(1,2)$.
3. Find the singular values and rank of $\operatorname{diag}(3,-2,0)$.
4. For $u=(1,2)$, $v=(3,1)$, calculate $u\wedge v$ and explain its orientation.

## Answers and explanations

1. No: the second is twice the first, so their span has dimension one.
2. The scalar coefficient is $u^Tb/(u^Tu)=3/5$. Thus $p=(3/5,6/5)$ and $r=(12/5,-6/5)$; $u\cdot r=0$ checks the result.
3. $A^TA=\operatorname{diag}(9,4,0)$, so the singular values are $3,2,0$ and the rank is two. The negative entry is a reflection, not a negative stretch magnitude.
4. Bilinearity and antisymmetry give $u\wedge v=(1\cdot1-2\cdot3)e_1\wedge e_2=-5e_1\wedge e_2$. The signed parallelogram area is $-5$, reversing the standard orientation.

## Common mistakes and misconceptions

Matrix multiplication generally does not commute. A zero determinant says a square map loses dimension; it does not say every entry vanishes. Eigenvectors from distinct eigenvalues are independent, but orthogonality needs a condition such as Hermitian symmetry. A change in vector coordinates is not a physical deformation. Tensor components require a declared basis and transform with their slots; an arbitrary rectangular table is not automatically a coordinate-free tensor.

## Connections to other mathematics

The [multivariable chapter](../calculus/multivariable-and-vector-calculus.md) uses Jacobians as linear maps. The [ODE chapter](../differential-equations/ordinary-differential-equations.md) uses eigenvalues for evolution. The [subject map](../../CONTENTS.md) locates infinite-dimensional spectral theory and differential geometry.

## Applications

For a spring network, $Ku=f$ relates displacement $u$ in metres to force $f$ in newtons; stiffness entries have units N/m. Positive definiteness after supports are imposed means positive elastic energy $u^TKu/2$. A free rigid translation can create a null vector, so a singular stiffness matrix may reveal missing constraints rather than a numerical error. Least squares also estimates sensor calibration, provided residual weighting matches measurement uncertainty.

## Optional computational examples

Run [plot_analysis.py](../../scripts/plot_analysis.py) for the projection figure and [verify_analysis.py](../../scripts/verify_analysis.py) for exact rational elimination, least-squares residuals, spectra, and wedge determinants. Symbolic checks validate these expressions; they do not prove every theorem in the chapter.

## References and recommended reading

Source and further study: Gilbert Strang, [MIT OpenCourseWare 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/), materials on the four subspaces, projections, eigenvalues, and SVD. The multilinear definitions here are an introductory construction; a full tensor algebra course requires additional study.

## Revision and mastery status

Written 2026-10-18. Scope: finite-dimensional reference with a substantive multilinear bridge, not an exhaustive algebra text. Mastery requires explaining rank–nullity, checking a residual, diagonalizing a symmetric matrix, and distinguishing a tensor from its components. No learner assessment or next-review date has been recorded.
