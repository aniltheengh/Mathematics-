# Conics II: tangents, normals, curvature, and reflection

**Lesson ID:** LES-GEO-02  
**Sequence:** Second of three guided conic lessons.  
**Prerequisites:** [Focal geometry](conics-focus-to-equation.md), dot products, differentiation, and the chain rule.  
**Learning objectives:** Derive tangents three ways; use a discriminant to count intersections; prove ideal reflection laws using vectors; and compute local curvature with its units.

[Lesson route](../README.md) · [Conic reference](../../subjects/geometry/coordinate-geometry/conic-sections.md) · [Next: quadratic matrices](conics-matrices-and-classification.md)

## Stage 1: a tangent is a local direction

Let a smooth curve have a differentiable parameterization $P(t)=(x(t),y(t))$.
If $P'(t_0)\ne0$, the tangent line at $P_0=P(t_0)$ is
$P_0+sP'(t_0)$, $s\in\mathbb R$. The statement concerns a
first-order approximation: $P(t_0+h)=P_0+hP'(t_0)+o(h)$.
The tangent need not remain close to the curve far from $P_0$.

If the same curve is given by $f(x,y)=0$ and
$\nabla f(P_0)\ne0$, the chain rule gives
$\nabla f(P_0)\cdot P'(t_0)=0$. Thus

$$
\nabla f(P_0)\cdot(P-P_0)=0 \tag{1}
$$

is its tangent line. A normal line is
$P_0+s\nabla f(P_0)$. The gradient need not have unit length:
its direction is what matters. Dividing by its norm gives a unit normal,
and replacing that normal by its negative does not change either line.

For an ellipse $f=x^2/a^2+y^2/b^2-1$ at
$P_0=(x_0,y_0)$, (1) is

$$
\frac{x_0x}{a^2}+\frac{y_0y}{b^2}=1. \tag{2}
$$

The equality on the right uses the fact that $P_0$ is on the ellipse.
For $y^2=4px$, use $f=y^2-4px$ to get
$y_0y=2p(x+x_0)$. For
$x^2/a^2-y^2/b^2=1$, the tangent is
$x_0x/a^2-y_0y/b^2=1$. The sign in each formula comes
from the defining quadratic, not from a rule based on the curve's appearance.

**Worked example 1: tangent and normal to an ellipse.** At
$P=(3,12/5)$ on $x^2/25+y^2/9=1$, the gradient is
$(6/25,8/15)$. Equation (2), multiplied by $75$, is
$9x+20y=75$. A tangent direction is $(20,-9)$.
Their dot product is $24/5-24/5=0$. The normal line is
$P+s(9,20)$, whose slope is $20/9$. This normal does not
generally pass through the ellipse center; a radial line and a normal line
agree everywhere only for a circle.

## Stage 2: intersection algebra explains tangency

Substitute a nonvertical line $y=mx+k$ into the ellipse:

$$
\left(\frac1{a^2}+\frac{m^2}{b^2}\right)x^2
+\frac{2mk}{b^2}x+\left(\frac{k^2}{b^2}-1\right)=0.
$$

The leading coefficient is positive. Its discriminant simplifies to

$$
\Delta=\frac{4(a^2m^2+b^2-k^2)}{a^2b^2}.
$$

Therefore there are two intersections when $k^2<a^2m^2+b^2$,
one repeated intersection when equality holds, and no real intersection when
$k^2>a^2m^2+b^2$. A repeated root encodes the same tangency that
the gradient described locally. Vertical lines require direct substitution:
$x=\pm a$ are tangents and $|x|<a$ gives two intersections.
They are not missing because no finite slope $m$ represents them.

![Parallel lines with two, one, and zero intersections with a fixed ellipse; the discriminant changes sign at the tangent.](../../assets/figures/lessons-geometry/tangency-discriminant.png)

**Worked example 2: tangent lines from an outside point.** Find the tangents
through $Q=(0,5)$ to $x^2/25+y^2/9=1$.
Every nonvertical line through $Q$ has $k=5$. Tangency requires
$25=25m^2+9$, so $m=\pm4/5$.
The lines are $y=5\pm4x/5$. The repeated-root formula gives
$x_0=-mka^2/(b^2+m^2a^2)=-5m$, and
$y_0=9/5$. Thus their contacts are $(\mp4,9/5)$.
Substitution verifies both the ellipse and each tangent equation.
The vertical line through $Q$ is $x=0$, which is a secant, so
there are precisely two tangents.

A useful independent check is Cauchy-Schwarz. On the ellipse,
$(x/a,y/b)$ has norm one. Hence the maximum of
$ux+vy$ is $\sqrt{a^2u^2+b^2v^2}$, attained at

$$
(x,y)=\frac{(a^2u,b^2v)}{\sqrt{a^2u^2+b^2v^2}}
$$

when $(u,v)\ne(0,0)$. This proves the supporting-line statement
for all directions, including vertical tangents, without a slope convention.

## Stage 3: prove the reflection rule with unit vectors

For a unit incident direction $d$ and a unit normal $n$, ideal specular
reflection reverses the normal component and preserves the tangential one:

$$
d_{\rm out}=d-2(d\cdot n)n. \tag{3}
$$

Decompose $d=(d\cdot n)n+[d-(d\cdot n)n]$ to see why.
The squared norm is unchanged because the two components are perpendicular.
Formula (3) also works with $-n$. It describes geometric rays on an ideal
smooth reflecting boundary; it does not model diffraction, roughness,
absorption, or a manufactured surface's tolerances.

For an ellipse let $u=(P-F_-)/|P-F_-|$ and
$v=(P-F_+)/|P-F_+|$. Differentiating the constant-distance-sum
function gives a normal proportional to $u+v$. Because the ellipse
is nondegenerate, $u+v\ne0$ on its boundary.
An incident ray from $F_-$ has direction $d=u$.
Choose $n=(u+v)/|u+v|$. Since
$|u+v|^2=2(1+u\cdot v)$, equation (3) gives

$$
d_{\rm out}
=u-\frac{2(1+u\cdot v)}{2(1+u\cdot v)}(u+v)
=-v.
$$

The reflected ray points from $P$ toward $F_+$. This proves
the familiar focal reflection property, including its direction; merely
drawing equal-looking angles would not establish it.

**Worked example 3: check an exact reflected ray.** At the same
$P=(3,12/5)$ with foci $(-4,0),(4,0)$,

$$
u=(35/37,12/37),\qquad v=(-5/13,12/13).
$$

Their sum has direction $(9,20)$, so
$n=(9,20)/\sqrt{481}$. Substituting in (3) gives
$d_{\rm out}=(5/13,-12/13)=-v$. Its norm is one.
The endpoint $(4,0)$ lies on the outgoing ray, a stronger check than
testing only a perpendicularity relation.

For the right-opening parabola $y^2=4px$, $p>0$, use the
distance definition $g(P)=|P-F|-(x+p)=0$, $F=(p,0)$.
If $u=(P-F)/|P-F|$, then $\nabla g=u-e_x$.
Incoming parallel rays travel in direction $d=-e_x$, so this
normal is proportional to $u+d$. The same calculation as above
gives $d_{\rm out}=-u$, toward the focus.
This includes the vertex, where $u=-e_x=d$ and the normal is nonzero.

![Vector constructions for ellipse and parabola reflection: the normal follows the gradient, and each outgoing arrow points to the stated focus.](../../assets/figures/lessons-geometry/reflection-vectors.png)

For a hyperbola, differentiating a signed focal distance difference gives
a normal proportional to $u-v$. An incident ray from one focus
reflects in direction $v$, away from the other focus. Its backward
extension points to that other focus. This distinction between an actual
ray and its extension explains why the ellipse's statement cannot be
copied word for word to a hyperbola.

## Stage 4: quantify the curve's local bending

For a regular twice-differentiable plane parameterization, the nonnegative
curvature is

$$
\kappa(t)=\frac{|x'y''-y'x''|}{(x'^2+y'^2)^{3/2}}.
$$

To understand the formula, let $T=P'/|P'|$ and arclength satisfy
$ds/dt=|P'|$. Curvature is $|dT/ds|$: the change of tangent
direction per unit distance. Computing $dT/dt$ and removing its
component parallel to $T$ gives the displayed determinant expression.
Its reciprocal $\rho=1/\kappa$, where $\kappa>0$, is the
radius of the osculating circle. Curvature has units inverse length;
radius has units length. A tangent supplies first-order information;
curvature supplies a second-order measure of the same curve.

For $P(t)=(a\cos t,b\sin t)$,

$$
\kappa(t)=\frac{ab}{(a^2\sin^2t+b^2\cos^2t)^{3/2}}.
$$

At a major-axis vertex $t=0$, $\rho=b^2/a$.
At a minor-axis vertex $t=\pi/2$, $\rho=a^2/b$.
For $a>b$, the ends of the long axis bend more sharply. For $a=b=R$,
both give $\rho=R$, as a circle should.

For a parabola parameterized by $P(t)=(pt^2,2pt)$, $p\ne0$,

$$
\kappa(t)=\frac{1}{2|p|(1+t^2)^{3/2}}.
$$

The vertex has curvature $1/(2|p|)$, while the curve becomes
flatter as $|t|$ grows. Parameter $t$ here is dimensionless; it
is not automatically time. Multiplying both coordinate lengths by $L>0$
divides curvature by $L$, another useful dimensional check.

**Worked example 4: a local machining radius.** For an ellipse with
$a=5$ mm and $b=3$ mm, the major vertex has
$\rho=9/5$ mm, while the minor vertex has $\rho=25/3$ mm.
These are local geometric radii. They do not by themselves establish cutter
clearance or an acceptable machining process; the osculating circle matches
position, tangent, and curvature at one point.

## Stage 5: use parameterization to avoid lost vertical cases

For $y^2=4px$, write $P(t)=(pt^2,2pt)$. The tangent simplifies to
$ty=x+pt^2$. It remains valid at $t=0$, where it is $x=0$.
A normal direction is $(-1,t)$, so the normal line can be written

$$
(x,y)=(pt^2,2pt)+s(-1,t).
$$

For a specified point $Q=(X,Y)$ to lie on this normal, elimination of
$s$ gives

$$
pt^3+(2p-X)t-Y=0. \tag{4}
$$

This cubic can have one, two, or three distinct real roots. With only simple
roots the number is one or three; a double root and a simple root give two
distinct contacts. For example, $p=1$, $Q=(5,2)$ gives
$t^3-3t-2=(t-2)(t+1)^2$, with contacts at $t=2,-1$.
A point can therefore
have more than one normal to a parabola; “the normal from a point” is
ambiguous until its contact point is fixed. At $Q=(3,0)$ and $p=1$,
(4) is $t(t^2-1)=0$, giving three contacts:
$(0,0),(1,2),(1,-2)$. At repeated roots the number of distinct
normals changes. The cubic concerns normals, not tangent contacts.

## Stage 6: connect tangent contacts and chord midpoints

Write an ellipse as $X^TDX=1$, where
$D=\operatorname{diag}(1/a^2,1/b^2)$. The tangent at a contact
$P$ is $P^TDX=1$. If an external point $Q$ lies on that
tangent, then $P^TDQ=1$. Consequently both contacts of tangents
from $Q$ lie on the single line $Q^TDX=1$, called the
polar of $Q$. In worked example 2, $Q=(0,5)$ makes this line
$5y/9=1$, recovering the chord of contact $y=9/5$ directly.

To count contacts rigorously, transform $Z=D^{1/2}P$ and
$W=D^{1/2}Q$. Contacts satisfy $|Z|=1$ and $W\cdot Z=1$.
A line at distance $1/|W|$ from the unit circle's center has
two, one, or zero intersections according as $|W|>1$, $|W|=1$,
or $|W|<1$. Thus outside points have two tangents, boundary
points one, and inside points none. This proof includes every direction.

Now consider a chord with midpoint $M$ and nonzero direction $d$.
Substitute $X=M+sd$ into the ellipse equation. Its quadratic in
$s$ has linear coefficient $2M^TDd$. The two endpoints have
opposite parameters precisely when this coefficient vanishes:
$M^TDd=0$. Therefore midpoints of parallel chords lie on a
diameter through the center. They are generally not on the Euclidean
perpendicular to $d$: the matrix $D$ changes that direction.
For a horizontal chord, $d=(1,0)$ forces $M_x=0$, as symmetry
predicts. This links a tangent calculation, a midpoint property, and a
linear-algebra change of metric in one argument.

## Practice problems

1. Find the tangent and normal lines at $(3,0)$ on $x^2/9+y^2/4=1$.
2. Find both tangents of slope $1$ to $x^2/25+y^2/9=1$ and their contact points.
3. Prove directly from (3) that $|d_{\rm out}|=|d|$ for any vector $d$ and unit $n$.
4. At $(1,2)$ on $y^2=4x$, find a unit normal and reflect $d=(-1,0)$.
5. For $a=4,b=2$, calculate the ellipse's maximum and minimum curvature and the points where they occur.
6. Show that the normal line to an ellipse through a point with $x_0y_0\ne0$ passes through the center only if $a=b$.
7. Use (4) for $p=1$ to count the distinct normals through $(2,0)$ and explain the repeated root.
8. For the right branch of $x^2/9-y^2/16=1$, prove that its tangent at the vertex is vertical without dividing by $y$.

## Answers and explanations

1. The gradient is $(2/3,0)$. The tangent is $x=3$ and the normal is $y=0$.
2. $k=\pm\sqrt{34}$. For a chosen $k$, the contact is
   $(-25/k,9/k)$; substitution gives $y=x+k$. The opposite
   sign of $k$ gives the opposite contact.
3. Expanding yields
   $|d-2(d\cdot n)n|^2=|d|^2-4(d\cdot n)^2+4(d\cdot n)^2=|d|^2$.
   The argument does not require $d$ itself to be unit.
4. The gradient direction is $(-1,1)$, so use
   $n=(-1,1)/\sqrt2$. Reflection gives $(0,-1)$,
   toward the focus $(1,0)$.
5. With $a>b$, the denominator in $\kappa$ is smallest at
   $t=0,\pi$ and largest at $t=\pi/2,3\pi/2$.
   Thus $\kappa_{\max}=a/b^2=1$ at $(\pm4,0)$,
   and $\kappa_{\min}=b/a^2=1/8$ at $(0,\pm2)$,
   in inverse units of the semiaxes.
6. A center-passing normal requires $(x_0/a^2,y_0/b^2)$
   parallel to $(x_0,y_0)$. Nonzero coordinates force
   $1/a^2=1/b^2$. The excluded axis vertices do have radial
   normals even when $a\ne b$.
7. Equation (4) becomes $t^3=0$, with only one distinct root,
   $t=0$. The root has multiplicity three, so counting algebraic
   multiplicity as three distinct geometric normals would be incorrect.
8. For $f=x^2/9-y^2/16-1$, $\nabla f(3,0)=(2/3,0)$
   is nonzero. Its orthogonal tangent is $x=3$. Alternatively
   $(x,y)=(3\cosh u,4\sinh u)$ has derivative $(0,4)$ at $u=0$.

## Review and references

Return to the [conic reference](../../subjects/geometry/coordinate-geometry/conic-sections.md)
for the standard equations and its textbook reading list. The
[differential geometry chapter](../../subjects/differential-geometry/geometry-and-tensors.md)
connects this curvature to curves in space. The
[calculus lesson](../analysis/calculus-from-limits-to-models.md)
develops the first-order approximation used at the start.

Generate and check the figures with the geometry lesson scripts. For mastery,
derive the reflection formula and apply it at a point you choose; do not infer
reflection solely from the plotted arrows. Then solve a normal-contact cubic
and distinguish root multiplicity from the number of contact points.
