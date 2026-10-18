# Discrete mathematics and combinatorics

**Topic ID:** DIS-001  
**Classification:** Discrete mathematics → counting, graphs, algorithms, designs  
**Level:** Introductory university, with advanced theorem statements  
**Content status:** Written compact reference.  
**Learner mastery:** Unassessed.

## Prerequisites

Use [sets, functions, and induction](../foundations/logic-and-proof.md) and
[finite sums](../algebra/elementary-algebra.md). Diagnostic: choosing three
distinct ordered items from five gives $5\cdot4\cdot3=60$, while choosing an
unordered set gives $\binom53=10$. Order is mathematical data, not a matter of
how a result happens to be written.

## Definition

Combinatorics studies finite and discrete arrangements. A permutation orders
distinct objects; a combination selects an unordered subset. A graph
$G=(V,E)$ consists here of a finite vertex set and unordered edges joining
distinct vertices, with no repeated edges, unless a directed or weighted graph
is explicitly specified. The degree $\deg v$ counts incident edges.

A path visits successive adjacent vertices without repetition. A graph is
connected if every pair of vertices has a path between them. A cycle returns
to its initial vertex with no other repeated vertex. A tree is connected and
has no cycles. A proper vertex coloring assigns different colors to adjacent
vertices; the least required number is the chromatic number $\chi(G)$.

A matching is a collection of edges sharing no endpoints. A directed flow
network has a source $s$, sink $t$, and nonnegative edge capacities; an allowed
flow obeys capacity bounds and conserves inflow and outflow at other vertices.
A deterministic finite-state model has a finite state set $Q$, input alphabet
$\Sigma$, and transition function $\delta:Q\times\Sigma\to Q$.

## Intuitive explanation

Counting starts by deciding what makes two outcomes different, then arranging
decisions without double counting. Graphs retain which objects are connected
while discarding irrelevant geometric placement. Crossed edges in a drawing
need not meet as vertices. Algorithms operate on these structures, and a proof
of correctness explains why their answer follows for every allowed input.

A generating function packages a sequence as coefficients. Multiplying such
expressions combines choices through coefficient convolution; it does not
require evaluating an infinite numerical sum when interpreted formally.

## Mathematical notation

$n=|V|$, $m=|E|$, $N(S)$ is the set of neighbors of a vertex subset $S$ in the
opposite part of a bipartite graph, and $\lfloor x\rfloor$ is the greatest
integer at most $x$. $[x^k]F(x)$ means the coefficient of $x^k$.
$T(n)=O(g(n))$ is an eventual upper bound by a constant multiple, and
$T(n)=\Theta(g(n))$ means both upper and lower bounds of that type for
positive comparison functions. Specify the input encoding and basic operation
before interpreting a complexity claim.

## Fundamental properties

The product rule multiplies numbers of sequential choices when each stage has
the stated number of options. The sum rule adds counts of disjoint alternatives.
For overlapping alternatives use inclusion–exclusion. The pigeonhole principle
says that placing $N$ objects in $k\ge1$ boxes forces some box to contain at
least $\lceil N/k\rceil$ objects.

Every tree on $n\ge1$ vertices has $n-1$ edges and a unique path between each
pair. A graph is bipartite exactly when it has no odd cycle (cited theorem).
Breadth-first search finds minimum-edge paths in an unweighted graph in
$O(n+m)$ time with adjacency lists. With positive weighted distances, counting
edges no longer measures path length; Dijkstra's method requires nonnegative
edge weights.

**Matching theorem, cited without proof.** A finite bipartite graph with parts
$A,B$ has a matching covering all of $A$ exactly when
$|N(S)|\ge|S|$ for every $S\subseteq A$ (Hall's theorem).
**Flow theorem, cited without proof.** Maximum flow value equals minimum
source–sink cut capacity. With integral capacities there is an integral maximum
flow. This is an existence statement; a particular choice of augmenting paths
also needs a termination argument and complexity analysis.

Extremal combinatorics asks how large a structure can be under a forbidden
configuration. Mantel's theorem (cited without proof) says a triangle-free simple
graph has at most $\lfloor n^2/4\rfloor$ edges; a balanced complete bipartite
graph attains the bound. This is stronger than checking a few sparse examples.

## Important formulas and identities

For integers $0\le r\le n$,

$$P(n,r)=\frac{n!}{(n-r)!},\quad
\binom nr=\frac{n!}{r!(n-r)!},\quad
\binom nr=\binom{n-1}{r-1}+\binom{n-1}r.$$

The Pascal equality requires $n\ge1$; define $\binom{m}{k}=0$ for $k<0$ or $k>m$ when $m\ge0$ to include its boundary cases. The factorial formula has the range stated above.

For finite sets,

$$|A\cup B|=|A|+|B|-|A\cap B|,$$
$$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|
+|A\cap B\cap C|.$$

The graph handshake identity is $\sum_{v\in V}\deg v=2m$.
For Fibonacci numbers $F_0=0,F_1=1,F_n=F_{n-1}+F_{n-2}$, the formal
generating function is

$$F(x)=\sum_{n\ge0}F_nx^n=\frac{x}{1-x-x^2}.$$

Boolean algebra uses $0,1$ with AND, OR, and NOT. In Boolean notation
$p\land(p\lor q)=p$ (absorption) and
$\neg(p\land q)=\neg p\lor\neg q$. As arithmetic on bits,
$p\land q=pq$ and $p\lor q=p+q-pq$; ordinary addition alone is not OR.

In a $2$-$(v,k,\lambda)$ block design there are $v$ points, $b$ blocks each
of size $k$, and each pair of points occurs in exactly $\lambda$ blocks.
If every point occurs in $r$ blocks, double counting yields
$bk=vr$ and $r(k-1)=\lambda(v-1)$.

## Derivations and proofs

**Handshake identity.** Count incidences $(v,e)$ with $v$ an endpoint of $e$.
Summing by vertex gives $\sum\deg v$; summing by edge gives $2m$. Thus the
number of vertices of odd degree is even, since their odd contributions must
sum to an even total.

**Tree edge count.** A tree with one vertex has zero edges. A finite tree with
at least two vertices has a leaf: take a longest path; an endpoint cannot have
another neighbor outside the path without lengthening it, or inside it without
creating a cycle. Delete a leaf and its one edge. The remaining graph is still
a tree. Induction gives $n-2$ remaining edges, hence $n-1$ originally.

**Fibonacci generating function.** Multiply the recurrence by $x^n$ and sum
formally for $n\ge2$. The left side is $F(x)-x$, and the right side is
$xF(x)+x^2F(x)$. Therefore $(1-x-x^2)F(x)=x$. Its constant denominator
coefficient is $1$, so formal power-series inversion is valid; no analytic
convergence assumption is being hidden.

## Worked examples

**1. Counting restricted codes.** A length-four code uses distinct decimal
digits and must not start with zero. There are $9$ first choices, then $9,8,7$
remaining choices, so $9\cdot9\cdot8\cdot7=4536$ codes.
Independent check: all distinct-digit strings number $10\cdot9\cdot8\cdot7$;
subtract those starting in zero, $9\cdot8\cdot7$, to get the same answer.

**2. A graph coloring.** In cycle $C_5$ with edges
$12,23,34,45,51$, alternating two colors around the cycle makes vertices
$5$ and $1$ have the same color, so two colors fail. A third color on vertex
$5$ resolves the conflict. Thus $\chi(C_5)=3$. Its five degree-two vertices
give total degree $10=2\cdot5$, checking its edge count.

**3. A flow and its optimality certificate.** Directed edges have capacities
$s\to a:3$, $s\to b:2$, $a\to b:1$, $a\to t:2$, $b\to t:3$.
Send $2$ along $s,a,t$, $2$ along $s,b,t$, and $1$ along $s,a,b,t$.
The total is $5$ and all capacities and conservation equations hold.
The cut separating $s$ alone has capacity $3+2=5$, so no flow can exceed $5$.
The constructed flow is therefore maximum, without relying only on an algorithm's output.

**4. A finite-state parity detector.** Let states $E,O$ record even or odd
numbers of $1$ bits seen. A $0$ leaves the state unchanged; a $1$ toggles it.
Starting in $E$, input $1011$ follows $E,O,O,E,O$ and ends in $O$.
The invariant is “the state records parity of the processed prefix.” It holds
initially and each transition preserves it, proving correctness for any length.

**5. Combinatorial probability.** A box has $5$ red and $3$ blue distinguishable
balls. A uniformly random unordered sample of $3$ without replacement has
$\binom83=56$ equally likely outcomes. Exactly two red occurs in
$\binom52\binom31=30$ outcomes, so the probability is $15/28$.
Multiplying independent draw probabilities would need adjustment because
without-replacement draws are dependent.

## Practice problems

1. **DIS-01:** Of $40$ learners, $23$ study algebra, $19$ geometry, and $8$ both. How many study neither?
2. **DIS-02:** Show that among $13$ integers two have the same remainder modulo $12$.
3. **DIS-03:** Solve $a_0=2$, $a_n=3a_{n-1}+1$ exactly.
4. **DIS-04:** Can a simple graph have exactly three vertices of odd degree? Justify.
5. **DIS-05:** Verify the design parameters of the blocks $123,145,167,246,257,347,356$ on seven points.
6. **DIS-06:** A loop adds integers from $1$ to $n$. Give a correctness invariant and the number of additions.

## Answers and explanations

1. The union has $23+19-8=34$ learners, so $40-34=6$ study neither.
The overlap must be subtracted because it was counted twice.
2. There are only twelve possible remainders, the boxes in the pigeonhole
principle. Thirteen inputs force a repeated box; distinct integers are not needed.
3. Set $b_n=a_n+1/2$. Then $b_n=3b_{n-1}$ and $b_0=5/2$,
so $a_n=(5\cdot3^n-1)/2$. Substitution checks both recurrence and initial value.
4. No: the handshake identity forces an even number of odd-degree vertices.
5. There are $b=7$ blocks of size $k=3$; each point occurs $r=3$ times.
Listing the three pairs per block shows each of the $\binom72=21$ pairs
occurs once, so $\lambda=1$. Check $bk=vr=21$ and $r(k-1)=6=v-1$.
6. After processing $k$ numbers the accumulated sum is $k(k+1)/2$.
The next addition of $k+1$ gives $(k+1)(k+2)/2$, preserving the invariant.
There are exactly $n$ additions if the sum starts at zero, hence $\Theta(n)$
arithmetic operations. Bit-operation cost also depends on operand sizes.

## Common mistakes and misconceptions

Dividing by $r!$ requires each unordered object to have exactly $r!$ ordered
representations. A walk may repeat vertices while a path, by this convention,
does not. A greedy choice is not automatically optimal: a greedy edge selection
can block a larger matching. Hall's condition ranges over all subsets, not only
single vertices. Complexity in arithmetic operations differs from bit complexity.

## Connections to other mathematics

[Number theory](../number-theory/number-theory.md) supplies modular states.
[Abstract algebra](../abstract-algebra/abstract-algebra.md) studies permutations
and finite fields used in designs. Generating functions connect to
[series](../analysis/functions-limits-and-series.md), with a distinction between
formal and convergent interpretations.

## Applications

Scheduling independent maintenance tasks on shared resources can be modeled by
a conflict graph: vertices are tasks, edges indicate tasks that cannot run
together, and colors represent time slots. This model assumes equal task
durations and pairwise conflicts. Unequal durations, precedence, and resource
capacities require a richer discrete optimization model. A minimum spanning
tree instead minimizes total connection weight over all spanning trees;
Kruskal's algorithm is justified by the cut-exchange property, not by graph
coloring or shortest-path arguments.

## Optional computational examples

Small designs, matchings, and paths can be checked by exhaustive enumeration.
An exhaustive search verifies only the encoded finite instance. The induction
and double-counting proofs explain whole families without software.

## References and recommended reading

Oscar Levin, [*Discrete Mathematics: An Open Introduction*, fourth edition](https://discrete.openmathbooks.org/dmoi4.html), provides proof-oriented graph, counting, and sequence exercises. Its [“Generating Functions” section](https://discrete.openmathbooks.org/dmoi4/sec_addtops-genfun.html?embed=) is a verified further-reading route. Richard Stanley, [*Algebraic Combinatorics: Walks, Trees, Tableaux, and More*, author page](https://math.mit.edu/~rstan/algcomb/), is advanced reading beyond this chapter. The deeper matching, flow, and extremal theorems have been labeled rather than presented as locally proved.

## Revision and mastery status

Written 2026-10-18; learner mastery unassessed. Supply a counting model, one
graph invariant, and an algorithm invariant before recording mastery. Full
matching/flow proofs, asymptotic enumeration, general design construction, and
integer-programming theory are beyond this compact treatment.
