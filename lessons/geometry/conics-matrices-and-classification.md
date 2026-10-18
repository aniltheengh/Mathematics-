# Conics III: classify every real quadratic without guessing

**Lesson ID:** LES-GEO-03  
**Sequence:** Third guided conic lesson.  
**Prerequisites:** Completing squares, symmetric matrices, eigenvectors, and [conic geometry](conics-focus-to-equation.md).  
**Learning objectives:** Separate rotation from translation; classify rank-two and rank-one quadratics; identify empty and degenerate loci; recover exact geometric data; and explain which properties survive a change of coordinates.

[Lesson route](../README.md) · [Linear algebra reference](../../subjects/linear-algebra/linear-algebra.md) · [Conic reference](../../subjects/geometry/coordinate-geometry/conic-sections.md)

## Stage 1: expose the structure hidden in the coefficients

Write a real quadratic in two variables as

$$
f(x,y)=Ax^2+Bxy+Cy^2+Dx+Ey+F
=z^TQz+\ell^Tz+F,\quad
z=\begin{pmatrix}x\\y\end{pmatrix},
$$

where

$$
Q=\begin{pmatrix}A&B/2\\B/2&C\end{pmatrix},
\qquad \ell=\begin{pmatrix}D\\E\end{pmatrix}.
$$

Assume $Q\ne0$. The factor $1/2$ is necessary because a matrix
quadratic counts the two off-diagonal terms. Missing it changes the
eigenvalues and the curve.

Because $Q$ is real symmetric, it has an orthonormal eigenbasis.
Let $R$ have these eigenvectors as columns. If needed, reverse the sign
of one column so $\det R=1$. With $z=Rw$,

$$
f=\lambda_1u^2+\lambda_2v^2+(R^T\ell)^Tw+F,\quad w=(u,v)^T.
$$

This is a rotation of coordinates: it preserves distances, angles, area,
and the geometric eccentricity. The mixed quadratic term vanishes, but a
linear term generally remains. A rotation diagonalizes $Q$; it does
not automatically move a center to the origin.

The two elementary invariants are

$$
\lambda_1+\lambda_2=\operatorname{tr}Q=A+C,\qquad
\lambda_1\lambda_2=\det Q=AC-B^2/4.
$$

Thus the familiar discriminant $B^2-4AC=-4\det Q$ records
the signs and rank of the quadratic part. It says nothing by itself about
whether the level set $f=0$ has real points.

## Stage 2: remove the linear terms when a center exists

Translate $z=h+w$. Expansion gives

$$
f=w^TQw+(2Qh+\ell)^Tw+f(h).
$$

A center is any solution of $2Qh+\ell=0$. If $Q$ is invertible,
there is exactly one:

$$
h=-\tfrac12Q^{-1}\ell,\qquad
k=f(h)=F-\tfrac14\ell^TQ^{-1}\ell.
$$

Then rotate $w=R(u,v)^T$. The entire classification reduces to

$$
\lambda_1u^2+\lambda_2v^2=-k. \tag{1}
$$

This is the multivariable version of completing a square. The gradient
$2Qz+\ell$ vanishes at $h$, confirming that the same point is
the quadratic function's stationary point. It is a minimum for positive
definite $Q$, a maximum for negative definite $Q$, and a saddle for
indefinite $Q$. A conic center and a minimum need not be the same concept.

For positive definite $Q$, both eigenvalues are positive.
Equation (1) gives an ellipse if $k<0$, one point if $k=0$,
and the empty real set if $k>0$. If $Q$ is negative definite,
multiply the whole equation by $-1$ and use the same rule.
For indefinite $Q$, the eigenvalues have opposite signs:
$k\ne0$ gives a hyperbola, while $k=0$ gives two intersecting lines.

**Worked example 1: rotate and translate an ellipse.** Consider

$$
5x^2-6xy+5y^2-16x+16y+8=0.
$$

Here $Q=\begin{pmatrix}5&-3\\-3&5\end{pmatrix}$,
$\ell=(-16,16)^T$, and $h=(1,-1)^T$.
Indeed $2Qh+\ell=0$ and $k=-8$.
Choose the positively oriented eigenbasis
$r_1=(1,1)^T/\sqrt2$, $r_2=(-1,1)^T/\sqrt2$,
with eigenvalues $2,8$. Therefore

$$
\begin{pmatrix}x\\y\end{pmatrix}
=\begin{pmatrix}1\\-1\end{pmatrix}
+\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix},\qquad
\frac{u^2}{4}+v^2=1.
$$

The semiaxes are $a=2,b=1$, and the major direction is $r_1$.
The foci are
$(1,-1)\pm\sqrt{3/2}(1,1)$. The area is $2\pi$.
A graph can suggest the rotation; substitution into the original polynomial
verifies it exactly.

![A translated rotated ellipse, with orthonormal principal axes and foci, beside its diagonal equation in principal coordinates.](../../assets/figures/lessons-geometry/principal-axes.png)

## Stage 3: understand the rank-one case instead of dividing by zero

Suppose $\det Q=0$ and $Q\ne0$. The eigenvalues are
$\lambda\ne0$ and $0$. Choose orthonormal coordinates along their
eigenvectors and write

$$
f=\lambda u^2+\alpha u+\beta v+F.
$$

Complete the square in the direction that has a quadratic term:

$$
f=\lambda\left(u+\frac{\alpha}{2\lambda}\right)^2
+\beta v+\gamma,\qquad
\gamma=F-\frac{\alpha^2}{4\lambda}.
$$

If $\beta\ne0$, translate $U=u+\alpha/(2\lambda)$,
$V=v+\gamma/\beta$. The result is

$$
U^2=4pV,\qquad p=-\frac{\beta}{4\lambda}\ne0.
$$

This is a parabola. Its axis follows the null eigenvector, and it has no
center because $2Qh=-\ell$ cannot cancel the nonzero component
$\beta$ in that direction.

If $\beta=0$, no variable $v$ appears. The equation is
$\lambda U^2+\gamma=0$. It describes two distinct parallel
lines if $-\gamma/\lambda>0$, a single repeated line if
$\gamma=0$, and no real points if $-\gamma/\lambda<0$.
In the repeated-line case the polynomial gradient vanishes on the entire
line; the regular implicit-curve tangent theorem does not apply to that
particular defining polynomial. The geometric line still has its usual tangent.

**Worked example 2: a rotated parabola with exact focus.** Consider
$x^2+2xy+y^2-4x+4y=0$. Use
$u=(x+y)/\sqrt2$, $v=(-x+y)/\sqrt2$.
The equation becomes $2u^2+4\sqrt2v=0$, so
$u^2=-2\sqrt2v$ and $p=-1/\sqrt2$.
Its vertex is the origin. Its focus has principal coordinates
$(u,v)=(0,-1/\sqrt2)$, hence ordinary coordinates $(1/2,-1/2)$.
The directrix is $v=1/\sqrt2$, or $y-x=1$.
The perpendicular distance from the origin to that line is $1/\sqrt2$,
equal to the vertex-focus distance. This check uses a normalized line
distance; reading the line constant as the distance would be wrong.

![Rank-one quadratic parts can yield a parabola, parallel lines, a repeated line, or an empty set depending on the linear term and level.](../../assets/figures/lessons-geometry/rank-one-loci.png)

## Stage 4: track degeneracy with a three-by-three matrix

Introduce the symmetric homogeneous coefficient matrix

$$
H=\begin{pmatrix}
A&B/2&D/2\\
B/2&C&E/2\\
D/2&E/2&F
\end{pmatrix}.
$$

With the extra coordinate fixed to one,
$f(x,y)=(x,y,1)H(x,y,1)^T$.
An invertible affine change $z=Rw+h$ becomes an invertible
three-by-three matrix $T$, and $H$ transforms to $T^THT$.
Thus $\det H$ is multiplied by $(\det T)^2$, preserving whether
it is zero. It is a useful algebraic degeneracy test.

When $Q$ is invertible, elimination of the linear terms gives the identity

$$
\det H=\det Q\left(F-\tfrac14\ell^TQ^{-1}\ell\right)
=\det Q\,k.
$$

This follows by translating to the center, where the homogeneous matrix
is block diagonal with blocks $Q$ and $k$. For a centered
ellipse or hyperbola, $k=0$ is precisely the degenerate level.
For the rank-one diagonal form
$\lambda u^2+\alpha u+\beta v+F$,
expansion instead gives $\det H=-\lambda\beta^2/4$.
Hence a rank-one conic with $\det H\ne0$ is a parabola.

**The necessary qualification.** A nonsingular homogeneous matrix does not
guarantee real affine points: $x^2+y^2+1=0$ has
$\det H=1$ and no real locus. Its quadratic form is algebraically
nondegenerate, but its real affine set is empty. Keep “real existence”
separate from “algebraic degeneracy” in a classification table.

**Worked example 3: the same discriminant, three different loci.** The
equations $x^2+y^2-1=0$, $x^2+y^2=0$, and
$x^2+y^2+1=0$ all have $B^2-4AC=-4$.
Their real loci are respectively a circle, a point, and empty.
Their values of $k$ are $-1,0,1$. This is a direct counterexample
to the rule “negative discriminant means a real ellipse” without a level check.

## Stage 5: follow a whole family through its transitions

Consider $x^2+2txy+y^2=1$, $t\in\mathbb R$.
Its eigenvalues are $1+t$ along $(1,1)$ and $1-t$
along $(1,-1)$. When $|t|<1$, it is an ellipse.
At $t=1$ it becomes $(x+y)^2=1$, two parallel lines;
at $t=-1$ it becomes $(x-y)^2=1$.
For $|t|>1$, it is a hyperbola.

Notice that the transition does not pass through a parabola.
At the rank-one values the linear term along the null direction is zero,
so the rank-one classification gives parallel lines. Merely varying a
discriminant continuously through zero does not determine a parabola.
The semiaxis associated with the eigenvalue tending to zero grows without
bound as the transition is approached from inside $|t|<1$.

**Worked example 4: a saddle's zero level.** Translate
$xy+x-y-1=0$ using $x=1+u$, $y=-1+v$.
The polynomial becomes $uv=0$. Its locus is the two lines
$x=1$ and $y=-1$, meeting at its center. Direct factorization
$(x-1)(y+1)=0$ verifies the same result. A nonzero level
$uv=c$ would instead be a rectangular hyperbola. The zero-level
case explains what the matrix value $k=0$ means geometrically.

## Stage 6: decide which transformations preserve which facts

Translations and orthogonal transformations preserve all Euclidean data:
distances, angles, focal eccentricity, tangency, curvature, and area.
An arbitrary invertible linear map preserves collinearity, incidence, and
the number of branches, and multiplies areas by the absolute determinant.
It generally changes angles, lengths, circles, foci, and curvature.
For example $(u,v)\mapsto(au,bv)$ takes the unit circle to an
ellipse; its focal geometry must be recomputed in the new Euclidean metric.

This is why diagonalizing by an orthonormal eigenbasis is especially useful.
A general algebraic substitution may simplify an equation, but its
coordinates may not represent perpendicular equal-unit axes. The distinction
also appeared in the first lesson's sloping cone section.
Numerically, an eigenvalue close to zero is a conditioning issue:
small coefficient perturbations can change the apparent family.
Exact rank classification and tolerance-based numerical classification
are separate tasks.

## Stage 7: recover a hyperbola's geometry after rotation

**Worked example 5: opposite eigenvalue signs with exact focal data.**
For $2x^2+8xy+2y^2-12=0$, the center is the origin.
The quadratic matrix has eigenvalues $6$ and $-2$ along
$r_1=(1,1)/\sqrt2$ and $r_2=(-1,1)/\sqrt2$.
In the corresponding principal coordinates,

$$
6u^2-2v^2=12,\qquad \frac{u^2}{2}-\frac{v^2}{6}=1.
$$

The transverse semiaxis is $a=\sqrt2$, the conjugate parameter
is $b=\sqrt6$, and $c=\sqrt{a^2+b^2}=2\sqrt2$.
Thus the foci are $\pm c r_1=(\pm2,\pm2)$ with matching
signs, and the eccentricity is $c/a=2$. The asymptotes satisfy
$v=\pm\sqrt3u$, or
$-x+y=\pm\sqrt3(x+y)$ in the original coordinates.
These are directions through the center, not the conic itself, because the
original equation has a nonzero constant level.

To check a nonvertex point, choose $u=2$, $v=\sqrt6$.
Then $u^2/2-v^2/6=2-1=1$ and
$(x,y)=(\sqrt2-\sqrt3,\sqrt2+\sqrt3)$.
Its focal distances have absolute difference $2\sqrt2$ by the
hyperbola theorem proved in the first lesson. A direct substitution into the
original quadratic gives zero, independently checking the coordinate rotation.

If the right side were zero instead of twelve, the same eigenvectors and
eigenvalues would describe the pair of asymptote lines. This final comparison
is why the workflow always checks the level after identifying the quadratic
part. Signs, rank, and eigenvectors do substantial work, but the constant
determines which level of that quadratic function is being drawn.

## Practice problems

1. Classify $4x^2+9y^2-8x+36y+31=0$, giving all real geometric parameters that exist.
2. Classify $x^2-y^2-2x-4y-3=0$ and write its asymptotes.
3. Find the center and semiaxis lengths of $2x^2+2xy+2y^2=3$.
4. Classify $(x-y)^2+2x+2y=0$ and find its vertex and focus.
5. Give one rank-one equation for each case: parallel lines, a repeated line, and the empty real set.
6. Compute $\det H$ for $y^2-4px=0$, $p\ne0$, and explain why $\det Q=0$ does not mean a degenerate parabola.
7. For $x^2+2txy+y^2=1$, find the semiaxes at $t=1/2$ and the directions they follow.
8. Explain why scaling $x=2u,y=v$ turns a circle into an ellipse while a rotation cannot.

## Answers and explanations

1. Completion gives $4(x-1)^2+9(y+2)^2=9$.
   Center $(1,-2)$, horizontal $a=3/2$, vertical $b=1$,
   $c=\sqrt5/2$, eccentricity $\sqrt5/3$, foci
   $(1\pm\sqrt5/2,-2)$, and area $3\pi/2$.
2. The equation is $(x-1)^2-(y+2)^2=0$.
   It is a pair of intersecting lines $y+2=\pm(x-1)$,
   with center $(1,-2)$. These are the locus itself; a
   nondegenerate hyperbola would have those directions as asymptotes.
3. The center is $(0,0)$. Eigenvalues are $3$ along $(1,1)$
   and $1$ along $(1,-1)$, so squared semiaxes are $1,3$.
   The long direction is $(1,-1)/\sqrt2$.
4. With $u=(x-y)/\sqrt2$, $v=(x+y)/\sqrt2$,
   the equation is $2u^2+2\sqrt2v=0$, or $u^2=-\sqrt2v$.
   Vertex $(0,0)$ and $p=-1/(2\sqrt2)$ along $v$ give
   focus $(-1/4,-1/4)$. The sign of the axis direction is part of the answer.
5. Respectively $x^2=1$, $x^2=0$, $x^2=-1$.
   All have the same rank-one quadratic part; their levels differ.
6. $H=\begin{pmatrix}0&0&-2p\\0&1&0\\-2p&0&0\end{pmatrix}$
   has determinant $-4p^2\ne0$. The linear term along the null
   direction of $Q$ makes the parabola algebraically nondegenerate.
7. The eigenvalues are $3/2,1/2$, so the semiaxes are
   $\sqrt{2/3}$ along $(1,1)$ and $\sqrt2$ along $(1,-1)$.
   Use unit versions of these vectors when measuring actual displacements.
8. The map has matrix $\operatorname{diag}(2,1)$ and unequal singular values.
   It changes the unit circle to $x^2/4+y^2=1$.
   An orthogonal matrix preserves $x^2+y^2$ exactly, so a
   rotation keeps a circle a circle.

## Review and computational check

For an unfamiliar equation, use this order: form $Q$, find its rank and
signs, remove admissible linear terms, inspect the remaining level, and only
then label the locus. If it exists, recover lengths using an orthonormal
frame and transform centers, vertices, and foci back to the original axes.

The [linear algebra lesson](../analysis/linear-algebra-and-least-squares.md)
develops orthogonal coordinates and projection; the
[numerical lesson](../advanced/approximation-and-optimization.md) explains
conditioning. Consult the [conic reference's reading list](../../subjects/geometry/coordinate-geometry/conic-sections.md#references-and-recommended-reading)
for further textbook treatments. The geometry lesson verification script
checks substitutions, center equations, ranks, eigenvalues, determinants,
and the worked answers here. Those checks support the encoded cases; the
classification argument above supplies the general reasoning.
