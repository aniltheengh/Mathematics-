# Topology: continuity, shape and holes

**Topic ID:** TOP-001  
**Classification:** Topology → general topology → algebraic topology  
**Level:** Undergraduate with advanced introductions  
**Content status:** Written compact reference; algebraic-topology invariants are introduced with stated results.  
**Learner mastery:** Unassessed.

## Prerequisites

Sets, functions, inverse images, basic proof methods, and groups are useful. Limits and Euclidean continuity supply familiar examples but are not definitions of general topology. Diagnostic: if $f(x)=x^2$, then $f^{-1}((1,4))=(-2,-1)\cup(1,2)$; an inverse image does not require an inverse function. Advanced homology uses abelian groups and quotient constructions.

## Definition

A **topology** $\tau$ on a set $X$ is a collection of subsets called open sets, containing $\varnothing$ and $X$, closed under arbitrary unions and finite intersections. The pair $(X,\tau)$ is a **topological space**. A set is closed when its complement is open; it may be both open and closed, or neither. A **basis** $\mathcal B$ is a collection whose unions form all open sets: every point lies in a basis member, and if a point lies in two basis members, a third contains it and lies in their intersection.

A map $f:X\to Y$ is **continuous** when $f^{-1}(U)$ is open in $X$ for every open $U\subseteq Y$. A **homeomorphism** is a bijection continuous in both directions. Two spaces are homeomorphic if one can be represented by the other without changing this open-set structure. Equal shape in this sense does not imply equal length, angle, area or differentiable structure.

## Intuitive explanation

Topology isolates nearness and connectedness from measurement. Stretching a rubber circle changes lengths but preserves a loop; cutting it changes the space. This picture is useful for common surfaces, but open sets give the definition even when no drawing is available. The same underlying set can carry different topologies: in the discrete topology every subset is open, while in the indiscrete topology only the empty set and the whole space are open.

![A circle and its real-line covering parameter, showing points differing by integer shifts mapping to the same point.](../../assets/figures/advanced/topology-cover.png)

The map $p(t)=(\cos2\pi t,\sin2\pi t)$ wraps the real line around the circle. Marked values $0$, $1$ and $2$ all reach $(1,0)$, although their lifted positions on the line differ.

## Mathematical notation

$\overline A$ is closure, the intersection of all closed sets containing $A$. $A^\circ$ is interior, the union of open subsets contained in $A$. The boundary is $\partial A=\overline A\setminus A^\circ$. $S^1=\{(x,y):x^2+y^2=1\}$, $D^2=\{(x,y):x^2+y^2\le1\}$ and $I=[0,1]$. The notation $X/\!\sim$ denotes equivalence classes with the quotient topology. Group statements below concern chosen basepoints unless the space is explicitly path-connected and the resulting isomorphism type is being discussed.

## Fundamental properties

The **subspace topology** on $A\subseteq X$ consists of $A\cap U$ for open $U\subseteq X$. Thus $[0,1/2)$ is open relative to $[0,1]$ but not open in $\mathbb R$. The **product topology** on $X\times Y$ has basis $U\times V$ with both factors open. A map into a product is continuous exactly when its coordinate maps are continuous.

For a surjection $q:X\to Y$, the **quotient topology** declares $U\subseteq Y$ open exactly when $q^{-1}(U)$ is open. Identifying the endpoints of $[0,1]$ gives a circle. A construction that glues boundaries requires the quotient topology, rather than merely drawing the pieces touching.

A space is **$T_1$** if singleton sets are closed. It is **Hausdorff** if distinct points have disjoint open neighborhoods; Hausdorff implies $T_1$. A **regular $T_1$** space separates a point from a closed set by disjoint open neighborhoods, and a **normal $T_1$** space separates disjoint closed sets in the same way. Metric spaces satisfy these conditions. Topological spaces need not be Hausdorff: an indiscrete space with more than one point is a simple counterexample. Separation assumptions therefore belong in theorem statements.

A space is **compact** if every open cover has a finite subcover. A space is **connected** if it cannot be written as two disjoint nonempty open subsets. A path from $x$ to $y$ is a continuous map $\gamma:I\to X$ with those endpoints; path-connected implies connected, while the converse can fail. A familiar compactness theorem states that a subset of $\mathbb R^n$ is compact exactly when closed and bounded. This equivalence does not hold in every metric or topological space.

## Important formulas and identities

A **homotopy** between maps $f,g:X\to Y$ is a continuous $H:X\times I\to Y$ with $H(x,0)=f(x)$ and $H(x,1)=g(x)$. A homotopy equivalence has continuous maps each way whose compositions are homotopic to the respective identity. A deformation retraction contracts a space onto a subspace while keeping that subspace fixed. These notions preserve fewer details than homeomorphism: a solid disk is contractible to a point, but cannot be homeomorphic to a one-point space.

The **fundamental group** $\pi_1(X,x_0)$ consists of based loops modulo endpoint-fixed homotopy; multiplication concatenates loops, the identity is the constant loop and inversion reverses a loop. The interval and disk have trivial fundamental group. A standard theorem gives $\pi_1(S^1)\cong\mathbb Z$, recording winding number; the torus has $\pi_1(S^1\times S^1)\cong\mathbb Z^2$. These computations use lifting or other theorems, not visual inspection alone.

A **covering map** $p:\widetilde X\to X$ is a continuous surjection such that every point of $X$ has an open neighborhood $U$ whose preimage is a disjoint union of open sets, each mapped homeomorphically onto $U$. For locally suitable spaces, paths have unique lifts once the starting lift is fixed. The real-line cover of the circle turns winding into an endpoint difference of lifted paths. General covering classification requires connectedness and local hypotheses; it is not asserted for arbitrary spaces here.

For a chain complex of abelian groups and boundary maps,

$$\cdots\longrightarrow C_{n+1}\xrightarrow{\partial_{n+1}}C_n\xrightarrow{\partial_n}C_{n-1}\longrightarrow\cdots,\qquad\partial_n\partial_{n+1}=0,$$

the **homology group** is $H_n=\ker\partial_n/\operatorname{im}\partial_{n+1}$. Singular chains are finite formal integer sums of continuous simplex maps. Cycles have zero boundary, while boundaries arise from one dimension higher; the quotient counts cycles that do not fill. For a circle, $H_0\cong\mathbb Z$, $H_1\cong\mathbb Z$ and $H_n=0$ for $n\ge2$. Homology loses some information retained by the fundamental group because its groups are abelian.

**Cohomology** reverses the arrows using cochains $C^n=\operatorname{Hom}(C_n,G)$ with coefficient group $G$ and coboundary $\delta$. Then $H^n=\ker\delta_n/\operatorname{im}\delta_{n-1}$. With ring coefficients, a cup product adds multiplicative information; on an oriented torus, degree-one classes from its two circle directions have a nonzero degree-two product. This is an algebraic-topology result stated for orientation, not proved here.

A **topological $n$-manifold** is a Hausdorff, second-countable space locally homeomorphic to $\mathbb R^n$. A boundary version also allows half-space charts. A sphere is locally planar although not globally a plane. The torus is another two-manifold. Smooth atlases add differentiability and lead to [differential geometry](../differential-geometry/geometry-and-tensors.md).

## Derivations and proofs

**Theorem.** A continuous image of a compact space is compact. Let $(V_i)$ cover $f(X)$ by sets open in the image space. Their inverse images form an open cover of $X$. Compactness gives finitely many inverse images covering $X$, hence the corresponding finitely many $V_i$ cover $f(X)$.

**Theorem.** A continuous image of a connected space is connected. If the image split into disjoint nonempty relatively open sets, their inverse images would give the forbidden separation of the original space. In particular, connectedness is preserved by homeomorphisms.

These short proofs also show why continuity is formulated with inverse images. Deep computations of homotopy and homology groups require additional machinery and are referenced below.

## Worked examples

**1. An open interval and a line.** The map $f:(-1,1)\to\mathbb R$, $f(x)=x/(1-|x|)$, is a homeomorphism. It is continuous, strictly increasing, and tends to opposite infinities at the endpoints. Its inverse is $g(y)=y/(1+|y|)$, continuous on $\mathbb R$. Direct substitution checks both compositions. Boundedness is therefore not a topological invariant.

**2. Disk versus circle.** The homotopy $H(x,t)=(1-t)x$ contracts $D^2$ to its center; every intermediate point remains in the disk because its norm is at most one. The same formula does not contract $S^1$ within $S^1$, since intermediate norms are below one. The theorem $\pi_1(S^1)=\mathbb Z$ establishes that the circle cannot contract to a point.

**3. A punctured plane.** For $x\in\mathbb R^2\setminus\{0\}$ set $r(x)=x/\|x\|$. The homotopy $H(x,t)=((1-t)+t/\|x\|)x$ never passes through zero, starts at $x$, ends at $r(x)$ and fixes points of $S^1$. Thus the punctured plane deformation retracts onto $S^1$, so its fundamental group is $\mathbb Z$. A missing point changes the allowable contractions.

**4. A small homology calculation.** A triangle with its three edges but no filled face has three vertices and three oriented edges. A closed traversal is an edge cycle with zero boundary. There is no two-cell boundary to remove that cycle, giving $H_1\cong\mathbb Z$. Adding the filled triangle introduces a boundary equal to that cycle, making $H_1=0$. This elementary cellular computation agrees with the circle and disk results.

## Practice problems

1. In $\mathbb R$, find closure, interior and boundary of $[0,1)$.
2. Why cannot $[0,1]$ be homeomorphic to $\mathbb R$?
3. How many path components does $\mathbb R\setminus\{0\}$ have, and why?
4. For the circle cover $p(t)=(\cos2\pi t,\sin2\pi t)$, lift the loop $\gamma(s)=(\cos6\pi s,\sin6\pi s)$ starting at zero and find its winding number.

## Answers and explanations

1. Closure is $[0,1]$, interior $(0,1)$ and boundary $\{0,1\}$. Both endpoints touch the set and its complement in every neighborhood.
2. The interval is compact and the line is not. A homeomorphism is continuous, so its image would have to be compact, a contradiction.
3. Two, the negative and positive half-lines. Each is path-connected; a path between them would take the value zero by the intermediate value theorem.
4. The lift is $\widetilde\gamma(s)=3s$. Its endpoint difference is three, giving winding number three. Changing the initial lift to an integer shifts both endpoints but preserves the difference.

## Common mistakes and misconceptions

An open subset of a subspace need not be open in the ambient space. Continuous bijections need not have continuous inverses, although a continuous bijection from compact to Hausdorff is a homeomorphism. Connectedness does not always imply path-connectedness. A drawn hole is intuition; a stated invariant or explicit deformation supplies the mathematical argument. Compactness in infinite dimensions requires extra care.

## Connections to other mathematics

[Functional analysis](../functional-analysis/functional-analysis.md) uses weak topologies and compactness. [Differential geometry](../differential-geometry/geometry-and-tensors.md) adds smooth structure and metrics. The [subject map](../../CONTENTS.md) records links to real analysis and abstract algebra.

## Applications

An angular joint coordinate lives on a circle rather than an unrestricted line; a two-angle mechanism lives on a torus before collision restrictions are imposed. A path planner must stay in the collision-free configuration space. Different winding classes can constrain routes even if their endpoint coordinates match. Topological information complements length and energy calculations rather than replacing them.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) draws the covering map. [Checks](../../scripts/verify_advanced.py) verify the interval-map inverses on both sign branches, radial-retraction norms and triangle incidence ranks. Finite examples do not prove general classification theorems.

## References and recommended reading

- Allen Hatcher, [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html), chapters 0–3: homotopy, fundamental group, homology and cohomology. Its [contents](https://pi.math.cornell.edu/~hatcher/AT/at1-tc.html) identifies the relevant sections.
- Gerald Teschl, [*Topics in Linear and Nonlinear Functional Analysis*](https://www.mat.univie.ac.at/~gerald/ftp/book-fa/), appendix on metric and topological spaces: recommended further reading; the author page currently lists its contents and publication availability.

## Revision and mastery status

Written 2026-10-18. All topology subject-map entries are introduced explicitly, with elementary proofs and finite calculations. Complete algebraic-topology proofs and manifold classification are outside this reference scope. Mastery requires working with inverse images and explaining what a stated invariant can and cannot distinguish.
