# Logic, sets, and proof

**Topic ID:** FND-001  
**Classification:** Foundations → mathematical language, logic, and structures  
**Level:** Introductory, with clearly marked advanced bridges  
**Content status:** Written compact reference; advanced results explicitly cited without proof.  
**Learner mastery:** Unassessed.

## Prerequisites

Only integer arithmetic is needed for the main examples. A statement is something
that can be true or false; a question or command is not a statement. Diagnostic:
“Every even integer is positive” is false, because $-2$ is a counterexample.
“Find an even integer” is an instruction, so it has no truth value.

## Definition

A **proposition** has a truth value. A **predicate** $P(x)$ becomes a proposition
when a value is substituted or its variable is quantified. The universal statement
$\forall x\in S\,P(x)$ requires every element of $S$ to satisfy $P$; the
existential statement $\exists x\in S\,P(x)$ requires at least one witness.

A **set** is a collection of distinct elements. Write $x\in A$ for membership
and $A\subseteq B$ when every element of $A$ belongs to $B$. Equality means
mutual inclusion. The power set $\mathcal P(A)$ contains all subsets of $A$;
$A\times B$ contains ordered pairs $(a,b)$ with $a\in A,b\in B$.

A **relation** from $A$ to $B$ is a subset of $A\times B$. An equivalence
relation on $A$ is reflexive, symmetric, and transitive. Its class at $a$ is
$[a]=\{x\in A:x\sim a\}$. A partial order is reflexive, antisymmetric, and
transitive; a total order also compares every pair. Divisibility on positive
integers is a partial order, but $2$ and $3$ are incomparable.

A function $f:A\to B$ assigns exactly one value in $B$ to each member of $A$.
It is injective if equal outputs imply equal inputs, surjective if every member
of $B$ occurs, and bijective if both conditions hold. The inverse image
$f^{-1}(C)=\{a\in A:f(a)\in C\}$ is defined for every $C\subseteq B$, even
when an inverse function does not exist.

## Intuitive explanation

Logic controls what a claim promises. “For every input there is an output” allows
different outputs for different inputs; “there is an output for every input” may
instead assert one common output, depending on the quantifier order. A proof is
a finite chain of justified steps whose conclusion follows from its hypotheses.
Checking a million cases does not establish a statement about every integer.

Sets describe allowable objects, relations compare them, and functions describe
consistent assignments. These distinctions prevent treating a multivalued
relation such as $y^2=x$ as a real function without choosing a branch.

## Mathematical notation

Here $\neg,\land,\lor,\Rightarrow,\Leftrightarrow$ mean negation, conjunction,
inclusive disjunction, implication, and equivalence. $\varnothing$ is the empty
set, $A\setminus B$ is set difference, and $A^c$ is complement relative to a
declared universe. Composition is $(g\circ f)(x)=g(f(x))$, so $f$ acts first.
$|A|$ denotes cardinality. We use $\mathbb N=\{0,1,2,\ldots\}$.

## Fundamental properties

The truth table gives the full meaning of the basic connectives:

| $P$ | $Q$ | $P\land Q$ | $P\lor Q$ | $P\Rightarrow Q$ | $P\Leftrightarrow Q$ |
| --- | --- | --- | --- | --- | --- |
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | F | T | T | F |
| F | F | F | F | T | T |

An implication with false premise is true under this definition. It makes no
assertion that the premise actually occurs. Its contrapositive
$\neg Q\Rightarrow\neg P$ is equivalent, while its converse
$Q\Rightarrow P$ need not be.

Equivalence classes partition a set: two classes are either identical or
disjoint. A finite set has cardinality $n$ if it is in bijection with
$\{1,\ldots,n\}$. An infinite set is countably infinite when it is in bijection
with $\mathbb N$; “countable” includes finite sets here. The integers and
rationals are countable. A diagonal enumeration of integer pairs gives a list
of fractions, and deleting duplicates lists $\mathbb Q$.

**Advanced foundations.** In first-order logic a formal theory consists of a
language, axioms, and inference rules. A model interprets the symbols so the
axioms hold. Semantic validity is truth in every model; derivability is the
existence of a formal proof. The completeness theorem for first-order logic
equates these two notions for consequences of a theory. This does not say a
particular theory decides every sentence.

The first incompleteness theorem, in its consistency-based form, says a
consistent, effectively axiomatized theory containing enough elementary
arithmetic is incomplete. The second says such a theory cannot prove its own
standardly formalized consistency, under the usual derivability conditions.
These are cited deep theorems, not proved here. They do not imply that a
particular engineering calculation is undecidable. Computability is likewise
precise: a decision algorithm must halt on every allowed input. The halting
problem has no such algorithm for arbitrary programs.

## Important formulas and identities

De Morgan laws and quantifier negation are

$$
\neg(P\land Q)\Leftrightarrow\neg P\lor\neg Q,\qquad
(A\cup B)^c=A^c\cap B^c,
$$
$$
\neg\forall x\in S\,P(x)\Leftrightarrow\exists x\in S\,\neg P(x),\qquad
\neg\exists x\in S\,P(x)\Leftrightarrow\forall x\in S\,\neg P(x).
$$

For finite $A$, $|\mathcal P(A)|=2^{|A|}$, because each element is either selected
or omitted. The **axiom of choice** says that for any family of nonempty sets
$(A_i)_{i\in I}$ there is a function $c$ with $c(i)\in A_i$. It is equivalent,
over the other usual ZF axioms, to the well-ordering theorem and Zorn's lemma;
these equivalences are cited without proof. Finite choices need no such axiom.

**Advanced category language.** A category has objects, morphisms with specified
sources and targets, associative composition, and identity morphisms. In
$\mathbf{Set}$ objects are sets and morphisms are functions. A functor
$F:\mathcal C\to\mathcal D$ preserves identities and composition:

$$F(1_A)=1_{F(A)},\qquad F(g\circ f)=F(g)\circ F(f).$$

A natural transformation $\eta:F\Rightarrow G$ has components
$\eta_A:F(A)\to G(A)$ satisfying
$G(f)\circ\eta_A=\eta_B\circ F(f)$ for every $f:A\to B$.
For example, on sets let $F(A)=A$ and $G(A)=A\times A$, with
$G(f)(a,b)=(f(a),f(b))$. The diagonal $\eta_A(a)=(a,a)$ is natural since both
compositions send $a$ to $(f(a),f(a))$. This checks a structural compatibility,
not merely equality at a chosen numerical example.

## Derivations and proofs

**Proposition: $\mathcal P(A)$ is larger than $A$.** There is an injection
$a\mapsto\{a\}$. Suppose a surjection $f:A\to\mathcal P(A)$ existed and put
$D=\{a\in A:a\notin f(a)\}$. Surjectivity gives $f(d)=D$. Then
$d\in D\Leftrightarrow d\notin D$, a contradiction. Thus no such surjection
exists. In particular not all infinite sets have the same cardinality.

**Induction example.** For $n\ge1$,
$1+3+\cdots+(2n-1)=n^2$. The base case is $1=1$. If the sum through $2n-1$
equals $n^2$, adding the next term gives
$n^2+(2n+1)=(n+1)^2$. Induction proves the statement for every positive integer.
The induction hypothesis is an assumption inside the step, not the conclusion
assumed for all $n$.

## Worked examples

**1. Negating a quantified claim.** Negate “For every real $x$ there exists real
$y$ with $y>x$.” First write $\forall x\,\exists y\,(y>x)$. Change each
quantifier and negate the predicate: $\exists x\,\forall y\,(y\le x)$.
The original is true, with witness $y=x+1$; therefore its negation is false.

**2. Computing an inverse image.** Let $f:\mathbb R\to\mathbb R$ be $f(x)=x^2$.
For $C=[1,4]$, solve $1\le x^2\le4$. Both signs matter, giving
$f^{-1}(C)=[-2,-1]\cup[1,2]$. Substitution checks the endpoints. There is no
inverse function on all $\mathbb R$, because $f(1)=f(-1)$.

**3. Contrapositive and counterexample.** For integer $n$, prove that $n^2$ odd
implies $n$ odd. The contrapositive starts with $n=2k$; then
$n^2=4k^2=2(2k^2)$ is even. To disprove the different statement “$n^2$ even
implies $n$ divisible by $4$,” take $n=2$: its square is $4$, but $4\nmid2$.

## Practice problems

1. **FND-01:** List $\mathcal P(\{a,b\})$ and distinguish $a\in A$ from $\{a\}\subseteq A$.
2. **FND-02:** On integers, let $a\sim b$ mean $3\mid(a-b)$. Prove this is an equivalence relation and list its classes.
3. **FND-03:** Prove $f^{-1}(B\cap C)=f^{-1}(B)\cap f^{-1}(C)$.
4. **FND-04:** Prove $2^n\ge n+1$ for all $n\in\mathbb N$ by induction.
5. **FND-05:** Does $\forall x\in\mathbb R\,\exists y\in\mathbb R\,(x+y=0)$ imply $\exists y\,\forall x\,(x+y=0)$?

## Answers and explanations

1. The subsets are $\varnothing,\{a\},\{b\},\{a,b\}$. Membership concerns an element; inclusion concerns a set. Both displayed claims hold for $A=\{a,b\}$, but their meanings differ.
2. $a-a=0$ is divisible by $3$; if $3\mid a-b$, then $3\mid b-a$; if $3\mid a-b$ and $3\mid b-c$, add to get $3\mid a-c$. The three classes are $[0],[1],[2]$.
3. An input belongs to the left side exactly when its output belongs to both $B$ and $C$, exactly when it belongs to each inverse image. Equality follows element by element; injectivity is unnecessary.
4. At $n=0$, $1\ge1$. If $2^n\ge n+1$, then $2^{n+1}\ge2n+2\ge n+2$ because $n\ge0$.
5. No. The first uses $y=-x$. A common $y$ would have to be $0$ at $x=0$ and $-1$ at $x=1$, impossible.

## Common mistakes and misconceptions

A converse needs a separate proof. One counterexample refutes a universal claim,
but one confirming example proves only that instance. The empty set is a subset
of every set, while $\varnothing\in A$ depends on $A$. Negating $x>0$ gives
$x\le0$, with the equality case included. An unproved assertion is not made
true by calling it “obvious.”

## Connections to other mathematics

[Number theory](../number-theory/number-theory.md) uses divisibility relations and
induction. [Abstract algebra](../abstract-algebra/abstract-algebra.md) uses
equivalence classes to construct quotient structures. Limits in
[analysis](../analysis/functions-limits-and-series.md) depend critically on the
order of their quantifiers.

## Applications

An interlock specification “pump on implies valve open” is $P\Rightarrow V$.
The unsafe state is exactly $P\land\neg V$. Its converse would require the pump
to run whenever the valve opens, which is a different design requirement.
Logical verification checks a stated model; the physical equipment still has
failure modes outside a Boolean model.

## Optional computational examples

Truth tables can be enumerated for finitely many Boolean inputs. They verify
propositional identities, but do not prove arbitrary quantified number-theoretic
claims. No program is needed for this chapter.

## References and recommended reading

Verified reference routes: Richard Hammack, [*Book of Proof*, chapters “Sets,” “Logic,” “Relations,” “Functions,” and “Cardinality of Sets”](https://richardhammack.github.io/BookOfProof/), for further proof practice; Oscar Levin, [*Discrete Mathematics: An Open Introduction*](https://discrete.openmathbooks.org/dmoi4.html), logic and proof chapters. Tai-Danae Bradley's author explanation [“What is a Natural Transformation?”](https://www.math3ma.com/blog/what-is-a-natural-transformation) supports the naturality equation. The Lean community's [*Logic and Proof*, “Semantics of First Order Logic”](https://leanprover-community.github.io/logic_and_proof/semantics_of_first_order_logic.html) treats models and completeness; the [*Open Logic Text*, “Introduction to Incompleteness” and subsequent chapters](https://builds.openlogicproject.org/open-logic-complete.pdf) provides the formal incompleteness/computability route. Those advanced statements here are orientation, not local proofs or a completeness claim for this chapter.

## Revision and mastery status

Written 2026-10-18. Learner mastery remains unassessed. Demonstrate mastery by
negating nested quantifiers, choosing a valid proof method, and constructing an
inverse image without assuming an inverse function. Formal incompleteness proofs,
axiomatic set theory, and categorical limits remain deeper study topics.
