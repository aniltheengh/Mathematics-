# Linear maps, bases, and least squares

**Lesson ID:** LES-LA-01.  
**Prerequisites:** Simultaneous linear equations, vectors, dot products, square roots, and basic functions.  
**Objectives:** Distinguish a map from its matrix; explain rank and nullity; derive a projection; solve one regression exactly by normal equations and QR; identify why an exact fit can still be sensitive.  
**Status:** Written guided lesson; learner mastery unassessed.

The [linear algebra reference](../../subjects/linear-algebra/linear-algebra.md) collects the main definitions and formulas. Here we follow one measurement problem far enough to discover why those formulas have their particular form. Three observations will produce two coefficients, a one-dimensional residual, an orthogonal factorization, and an explicit uncertainty question. These are different views of the same calculation.

All vectors in the main derivation are real. For a complex extension, use the book's convention $\langle u,v\rangle=u^*v$, conjugate-linear first and linear second. Replace ordinary transposes in the orthogonality statements with conjugate transposes.

## Stage 1: a map exists before its coordinates

Consider the physical operation that projects a planar displacement onto the horizontal axis. In Cartesian coordinates its matrix is

$$T_B=\begin{pmatrix}1&0\\0&0\end{pmatrix}.$$

This table is a representation, not the whole definition of the operation. Let a new basis be $c_1=(1,1)$ and $c_2=(1,-1)$, and let

$$S=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad[v]_B=S[v]_C.$$

Columns of $S$ express the new basis vectors in the old coordinates. To operate on new coordinates, first convert to old coordinates, apply the map, and convert back. Thus

$$T_C=S^{-1}T_BS=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

**Worked example 1: follow a vector through the change.** The displacement $v=(2,0)$ has new coordinates $(1,1)$ because $c_1+c_2=(2,0)$. The new matrix sends $(1,1)$ to itself. Converting back gives $(2,0)$, agreeing with the physical horizontal projection. The matrices differ, while the operation and output vector agree. Checking only whether matrix entries remain unchanged would ask the wrong question.

A basis is an independent spanning list, so every vector has unique coordinates. Independence ensures uniqueness: if two coordinate lists represent the same vector, subtracting them produces a zero combination and forces every coefficient difference to zero. Spanning ensures existence. Removing either condition destroys one of these guarantees.

## Stage 2: rank asks what can be explained

Suppose observations $y_i$ are modeled by $a+bt_i$, with unknown intercept $a$ and slope $b$. For measurements at $t=0,1,2$, write

$$A=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad
\beta=\binom ab,\qquad y=\begin{pmatrix}1\\2\\2\end{pmatrix}.$$

The map $\beta\mapsto A\beta$ takes a two-component coefficient vector to a three-component prediction vector. Its columns span the possible prediction patterns. They are independent, so the rank is two and the coefficient null space is zero. Every representable prediction has a unique coefficient pair.

Yet the map is not onto $\mathbb R^3$: two independent columns can span at most a plane. In fact no straight line passes through all three observations. The first two require $a=1,b=1$, predicting three rather than two at the last time. This inconsistency is a mathematical property of the stated exact equations, not an algorithm failure.

Rank–nullity says $\dim\ker A+\operatorname{rank}A=2$ because the input space has dimension two. It does not say the nullity is the output dimension minus rank. The output-space complement has dimension $3-2=1$ and corresponds instead to $\ker A^T$ under the Euclidean inner product.

**Worked example 2: an unidentifiable coefficient.** If all measurement times are zero, the second column vanishes. Predictions become $(a,a,a)$ and every vector $(0,b)$ belongs to the null space. Any slope fits the same predictions. Repeating more measurements at the same time may improve the intercept estimate under a noise model, but it cannot identify the slope. Designing varied input values is part of making a fit informative.

## Stage 3: derive projection from an error decomposition

Choose coefficients to minimize the sum of squared residuals

$$Q(\beta)=\|y-A\beta\|^2.$$

The Euclidean norm treats each observation with equal weight and compatible units. It does not automatically follow that this weighting matches instrument uncertainty. With different measurement variances, a weighted norm may be appropriate; the stochastic assumptions must justify that choice.

Let a candidate fit be $p=A\widehat\beta$, with residual $r=y-p$. For any coefficient change $h$,

$$\|y-A(\widehat\beta+h)\|^2
=\|r\|^2-2r^TAh+\|Ah\|^2.$$

If $A^Tr=0$, the middle term vanishes. Every alternative then has squared error $\|r\|^2+\|Ah\|^2\ge\|r\|^2$. This proves minimality by a Pythagorean identity. Conversely, if some component of $A^Tr$ is nonzero, a sufficiently small change along that coefficient direction decreases the objective, so the candidate cannot minimize it.

Therefore the normal equations are

$$A^TA\widehat\beta=A^Ty.$$

If columns are independent, $h^TA^TAh=\|Ah\|^2>0$ for every nonzero $h$, so $A^TA$ is positive definite and invertible. This proves uniqueness of coefficients. Even when columns are dependent, the fitted prediction is still the unique orthogonal projection onto the column space, while its coefficient representation can be nonunique.

**Worked example 3: exact regression.** For the three observations,

$$A^TA=\begin{pmatrix}3&3\\3&5\end{pmatrix},
\qquad A^Ty=\binom57.$$

The equations are $3a+3b=5$ and $3a+5b=7$. Subtraction gives $b=1/2$, then $a=7/6$. Predictions and residuals are

$$p=\begin{pmatrix}7/6\\5/3\\13/6\end{pmatrix},
\qquad r=\begin{pmatrix}-1/6\\1/3\\-1/6\end{pmatrix}.$$

Check both orthogonality conditions: residuals sum to zero, and the time-weighted sum is $0(-1/6)+1(1/3)+2(-1/6)=0$. The squared error is $1/36+1/9+1/36=1/6$. These conditions check the fitted result independently of the elimination steps.

There is exactly one perpendicular residual direction in this example. A unit vector in it is $q_3=(1,-2,1)^T/\sqrt6$, since its dot products with both columns of $A$ vanish. The scalar residual coordinate is $q_3^Ty=-1/\sqrt6$, so $r=q_3(q_3^Ty)=(-1,2,-1)^T/6$. Squaring that coordinate immediately recovers the minimum error $1/6$. This is the three-dimensional Pythagorean picture behind the algebra.

For a positive-definite weight matrix $W$, minimizing $r^TWr$ instead gives $A^TW(y-A\widehat\beta)=0$. Factor $W=C^TC$ to see it as ordinary least squares for transformed data $Cy$ and matrix $CA$. If weights represent inverse measurement variances, the objective is dimensionless. Correlated errors can require nondiagonal weights. The geometric minimization itself needs no normal-distribution assumption; confidence intervals for its coefficients require a separate probability model and its corresponding hypotheses.

![Three observations and their exact least-squares affine fit](../../assets/figures/lessons-analysis/linear-regression.png)

The line is exactly $a+bt=7/6+t/2$. Vertical segments are observed-minus-predicted residuals in the plotted $(t,y)$ plane. Orthogonality in the derivation refers to three-dimensional observation space, where $r$ is perpendicular to both columns of $A$; the vertical segments are not perpendicular distances to the plotted line. The distinction prevents a common confusion between ordinary least squares and orthogonal-distance fitting.

## Stage 4: QR finds the same fit through perpendicular coordinates

The normal equations are ideal for deriving the condition, but their direct floating-point implementation can lose accuracy on sensitive problems. Factor $A=QR$, where columns of $Q$ are orthonormal and $R$ is square upper triangular for a full-column-rank thin factorization. The column space is unchanged, while the basis is now perpendicular.

For our matrix, normalize the first column:

$$q_1=\frac1{\sqrt3}(1,1,1)^T.$$

Its dot product with the second column is $\sqrt3$. Subtract that component: $(0,1,2)^T-(1,1,1)^T=(-1,0,1)^T$. Normalize to get $q_2=(-1,0,1)^T/\sqrt2$. Therefore

$$R=\begin{pmatrix}\sqrt3&\sqrt3\\0&\sqrt2\end{pmatrix},
\qquad Q^Ty=\binom{5/\sqrt3}{1/\sqrt2}.$$

Solving $R\widehat\beta=Q^Ty$ by back substitution gives $b=1/2$ then $a=7/6$, matching the normal-equation result.

Why does this work? Complete $Q$ to an orthogonal basis $[Q,Q_\perp]$ of observation space. Orthogonal transformations preserve the Euclidean norm, so

$$\|y-A\beta\|^2
=\|Q^Ty-R\beta\|^2+\|Q_\perp^Ty\|^2.$$

The second term does not depend on coefficients. Because $R$ is invertible, the first can be made exactly zero by the triangular solve. The remaining component is the unavoidable residual. This derivation also shows that QR does not magically make inconsistent data exactly representable.

The hand calculation used Gram–Schmidt to expose the geometry. Reliable software commonly uses Householder QR, or carefully implemented modified Gram–Schmidt when appropriate, because naive Gram–Schmidt can lose orthogonality. An SVD is particularly useful when deciding effective rank or finding a minimum-norm solution in a rank-deficient problem.

## Stage 5: separate problem sensitivity from algorithm stability

Consider the nearly dependent matrix

$$A_\varepsilon=\begin{pmatrix}1&1\\0&\varepsilon\end{pmatrix},
\qquad0<\varepsilon\le1.$$

It has exact rank two for every positive $\varepsilon$. Nevertheless, the second row carries only a small distinction between the two coefficient effects.

**Worked example 4: a zero residual with uncertain coefficients.** Data $y=(2,\varepsilon)^T$ give coefficients $(1,1)^T$. Perturb only the second observation by $\delta$; exact solution of the perturbed equations gives

$$\beta_2=1+\delta/\varepsilon,\qquad
\beta_1=1-\delta/\varepsilon.$$

For $\varepsilon=1/1000$ and $\delta=1/10000$, the data change is small but each coefficient changes by $1/10$. Both fits have zero residual for their own data. A residual measures agreement with the supplied equations; it does not establish insensitivity to uncertain measurements.

For the spectral norm, the condition number is $\kappa_2(A)=\sigma_{\max}/\sigma_{\min}$. Let $\lambda_+$ be the larger eigenvalue of $A_\varepsilon^TA_\varepsilon$:

$$\lambda_+=\frac{2+\varepsilon^2+\sqrt{4+\varepsilon^4}}2.$$

Its determinant is $\varepsilon^2$, so the other eigenvalue is $\lambda_-=\varepsilon^2/\lambda_+$. Consequently

$$\kappa_2(A_\varepsilon)=\lambda_+/\varepsilon,\qquad
\kappa_2(A_\varepsilon^TA_\varepsilon)=\kappa_2(A_\varepsilon)^2.$$

Computing the small eigenvalue by the determinant relation avoids subtracting nearly equal floating-point numbers. Forming normal equations squares the condition number; QR avoids that squaring, but cannot remove the underlying sensitivity of the original measurement problem.

![Condition numbers of a matrix with nearly dependent columns and its Gram matrix](../../assets/figures/lessons-analysis/linear-conditioning.png)

The curves use the exact expressions above for $10^{-5}\le\varepsilon\le1$, plotted on logarithmic axes. Parameter and condition numbers are dimensionless. The graph measures sensitivity in the stated coordinates; rescaling dimensional variables changes their numerical representation and must be justified by physical units and measurement uncertainty.

## Practice problems

1. Why must the two columns of a change-of-basis matrix be independent?
2. Find the kernel and rank of $B=\begin{pmatrix}1&2\\2&4\end{pmatrix}$.
3. Project $y=(2,0)$ onto the line spanned by $u=(1,1)$.
4. For observations $2,4,6$, find the least-squares constant and squared residual norm.
5. Explain why equal-weight regression residuals sum to zero when an intercept column is present.
6. Check the QR factorization above by multiplying $QR$; why is $Q^TQ=I$ enough for a thin factorization even though $QQ^T\ne I$?
7. In the sensitive example, take $\varepsilon=1/100$, $\delta=1/1000$. Find both perturbed coefficients.
8. If $\kappa_2(A)=100$, what is $\kappa_2(A^TA)$ for full column rank? Does choosing QR make the original condition number one?

## Answers and explanations

1. A basis must give unique coordinates. Dependent columns create a nonzero vector $h$ with $Sh=0$, so two coordinate lists differing by $h$ represent the same vector. The conversion matrix would not be invertible.
2. The second row is twice the first, so rank is one. The equation $x+2y=0$ gives kernel $\{t(-2,1):t\in\mathbb R\}$. Its dimension plus rank is two, matching the input dimension.
3. The coefficient is $u^Ty/(u^Tu)=2/2=1$, so the projection is $(1,1)$ and residual $(1,-1)$. Their dot product is zero, which confirms the minimizer.
4. The constant is the average four, giving residual $(-2,0,2)$ and squared norm eight. Orthogonality to $(1,1,1)$ explains why the mean is selected.
5. The first normal equation is the dot product of the all-ones column with the residual. It sets that sum to zero. Without an intercept, this particular orthogonality condition need not appear.
6. The first column is $\sqrt3q_1=(1,1,1)^T$; the second is $\sqrt3q_1+\sqrt2q_2=(0,1,2)^T$. The columns of $Q$ are unit and perpendicular, so $Q^TQ=I_2$. But $QQ^T$ projects $\mathbb R^3$ onto a plane and cannot equal the three-dimensional identity.
7. The ratio $\delta/\varepsilon=1/10$ gives $(\beta_1,\beta_2)=(9/10,11/10)$. Their sum remains two, and $\varepsilon\beta_2=\varepsilon+\delta$ checks the second equation.
8. The Gram condition number is $10000$. QR chooses perpendicular coordinates for computation and avoids that squaring; it does not change the inherent condition number of the given input-output map.

## Verification and further study

[Exact checks](../../scripts/verify_lessons_analysis.py) verify basis conversion, kernel vectors, regression residuals, QR products, and perturbation identities. [Plot source](../../scripts/plot_lessons_analysis.py) generates the graphs from the stated equations. These checks do not justify a particular statistical noise model.

Further study: Gilbert Strang, [MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/), projections, orthogonal matrices, and least squares; Driscoll and Braun, [Fundamentals of Numerical Computation](https://fncbook.com/), conditioning and stable least-squares methods. The hand examples and derivations here are original.

Written 2026-10-18. Mastery requires explaining the four different spaces involved—coefficient input, prediction range, coefficient null space, and residual complement—and checking a computed fit by an independent orthogonality test. No learner assessment has been recorded.
