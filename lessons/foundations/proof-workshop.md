# Proof workshop: turn a claim into a justified argument

**Lesson ID:** LES-FND-01  
**Level:** First course in mathematical reasoning.  
**Lesson status:** Written guided lesson with exact examples and reproducible diagrams.  
**Learner mastery:** Unassessed; completing a reading is different from demonstrating a proof.

## Prerequisites

You need integer arithmetic, fractions, squares, and the meaning of an even or
odd integer. An even integer is $2k$ for some $k\in\mathbb Z$; an odd integer
is $2k+1$. Read the compact [logic and proof reference](../../subjects/foundations/logic-and-proof.md)
when a symbol is unfamiliar. All integer variables in this lesson range over
$\mathbb Z$ unless another domain is declared. We use
$\mathbb N=\{0,1,2,\ldots\}$; induction statements will specify their initial index.

Before starting, explain why $-6$ is even. Its required witness is $k=-3$,
because $-6=2(-3)$. “Even” describes divisibility, not sign. This small example
shows the central habit of proof: connect a claim to its exact definition.

## Learning objectives

By the end you should be able to translate a sentence into quantified form,
negate it without losing an equality case, select direct or contrapositive
reasoning, write a complete induction argument, and reject a false claim with
a valid counterexample. You should also explain why checking finitely many
values cannot prove an unrestricted assertion about integers.

Work through the stages in order. At each checkpoint, cover the explanation,
write one or two sentences yourself, and compare the logical structure rather
than only the final answer.

## Stage 1: identify the promise and the domain

The sentence “Every square is nonnegative” needs a domain. For real $x$,
$x^2\ge0$ is true. For complex $x$ there is no compatible real ordering of all
complex numbers, so the same ordered statement does not have its usual meaning.
A missing domain can turn an apparently simple assertion into an ambiguous one.

The notation $\forall x\in S\,P(x)$ promises the property for every member of
$S$. One failing member refutes it. The notation $\exists x\in S\,P(x)$ promises
at least one witness; giving a witness and checking it proves the statement.
It does not promise uniqueness. To prove uniqueness, show that any two witnesses
must be equal.

Compare these real-number statements:

$$\forall x\in\mathbb R\;\exists y\in\mathbb R:\ y>x,$$
$$\exists y\in\mathbb R\;\forall x\in\mathbb R:\ y>x.$$

The first is true: after an arbitrary $x$ is presented, choose $y=x+1$.
The choice depends on $x$. The second is false: if a common $y$ were proposed,
the input $x=y$ would demand $y>y$. The order of the quantifiers controls what
information you may use when selecting a witness.

![A finite witness grid for y equals x plus one, with one marked witness in every row and no column covering every row.](../../assets/figures/lessons-foundations/quantifier-witnesses.png)

This finite example uses $X=\{0,1,2,3\}$ and $Y=\{1,2,3,4\}$ with relation
$y=x+1$. Each row has a witness, so $\forall x\in X\,\exists y\in Y$ is true.
No single column works for all rows, so $\exists y\in Y\,\forall x\in X$ is
false. The grid proves this finite instance by exhaustive inspection; the
preceding argument handles the separate, infinite real-number example.

**Checkpoint.** Does “every bolt has an assigned hole” imply that all bolts use
one common hole? No. The assignment may depend on the bolt. This is a logical
analogy, not a claim about an actual mechanical fit.

## Stage 2: negate the whole assertion

Negating a universal statement produces an existential statement with the
property negated. Negating an existential statement produces a universal
statement with the property negated:

$$\neg\forall x\,P(x)\ \Longleftrightarrow\ \exists x\,\neg P(x),\qquad
\neg\exists x\,P(x)\ \Longleftrightarrow\ \forall x\,\neg P(x).$$

The negation of $x>2$ is $x\le2$, not $x<2$. The boundary matters. The negation
of “$x$ is in both $A$ and $B$” is “$x$ is outside at least one of them,” so
$\neg(P\land Q)$ is $\neg P\lor\neg Q$. Here “or” is inclusive.

**Worked example 1: a complete nested negation.** The claim is
“Every real number has a larger integer.” Write it as
$\forall x\in\mathbb R\,\exists n\in\mathbb Z:(n>x)$.
First switch the outer universal quantifier to an existential one. Then switch
the inner existential quantifier to a universal one. Finally negate the
inequality. The result is

$$\exists x\in\mathbb R\;\forall n\in\mathbb Z:\ n\le x.$$

This says some real number bounds all integers above. The original statement
is the Archimedean property of the reals; it is assumed here as a standard
property, not derived merely by listing large integers. The negation gives the
precise failure that would be needed to refute it.

An implication $P\Rightarrow Q$ fails exactly when $P$ holds and $Q$ fails.
Therefore its negation is $P\land\neg Q$. “If a number is divisible by four,
then it is even” would be refuted by an integer divisible by four that is odd.
An even integer not divisible by four refutes the converse, a different statement.

## Stage 3: build a direct proof from definitions

A direct proof starts with the stated hypotheses and follows justified steps
to the conclusion. Begin with an arbitrary object satisfying the hypotheses.
“Arbitrary” matters: it allows the final conclusion to apply to every object
in the declared domain, rather than only to one selected example.

**Worked example 2: the sum of two odd integers is even.** Let $a,b$ be odd
integers. By definition, there are integers $r,s$ with
$a=2r+1$ and $b=2s+1$. Add the expressions:

$$a+b=2r+1+2s+1=2(r+s+1).$$

Since integers are closed under addition, $r+s+1$ is an integer. Thus $a+b$
has the form twice an integer and is even. This last sentence links the
calculation back to the definition; stopping at the factorization leaves the
logical connection unstated.

**Worked example 3: a rational closure proof.** Suppose $a,b$ are rational.
Write $a=m/n$ and $b=p/q$, with integers $m,n,p,q$ and $n,q\ne0$.
Then

$$a+b=\frac{mq+pn}{nq}.$$

The numerator is an integer, the denominator is an integer, and $nq\ne0$.
Therefore the sum is rational. The nonzero denominator is a required part of
the proof. For division, one would also need $b\ne0$; rational closure under
addition does not authorize division by zero.

When a proof splits into cases, justify that the cases cover every possibility.
Every integer is even or odd, so a parity split is exhaustive. Splitting real
numbers into positive and negative cases omits zero unless it is handled separately.

## Stage 4: use the contrapositive when the failure is simpler

The implication $P\Rightarrow Q$ is logically equivalent to
$\neg Q\Rightarrow\neg P$. Both fail only when $P$ is true and $Q$ is false.
This is the contrapositive. The converse $Q\Rightarrow P$ is generally not
equivalent and needs a separate proof.

**Worked example 4: an odd square has an odd integer root.** For integer $n$,
prove that if $n^2$ is odd, then $n$ is odd. Prove the contrapositive instead:
if $n$ is even, then $n^2$ is even. Write $n=2k$. Then
$n^2=4k^2=2(2k^2)$, with $2k^2\in\mathbb Z$. This proves the contrapositive
and hence the original implication. It does not assume the original conclusion.

There is also a residue version. If $3\nmid n$, division by three gives
$n=3k+1$ or $n=3k+2$. Squaring gives residues $1$ in either case:
$(3k+1)^2=3(3k^2+2k)+1$ and
$(3k+2)^2=3(3k^2+4k+1)+1$.
Thus $3\nmid n^2$. By contrapositive, $3\mid n^2$ implies $3\mid n$.
The argument depends on the specific remainder possibilities; it is not a
license to cancel divisibility for every composite number.

A contradiction proof temporarily assumes the negation of the desired result
and derives an impossibility. The [arithmetic chapter](../../subjects/numbers/arithmetic-and-number-systems.md)
proves irrationality of $\sqrt2$ this way. Keep the temporary assumption visible
so the reader can distinguish it from an established fact.

## Stage 5: induction proves an infinite chain with a justified link

To prove $P(n)$ for all integers $n\ge n_0$, first establish $P(n_0)$.
Then prove that for every $k\ge n_0$, assuming $P(k)$ permits deduction of
$P(k+1)$. The induction principle supplies the passage through all indices.
Checking the first few cases is useful for detecting mistakes, but it does not
replace either the base case or the general link.

**Worked example 5: sum of the first odd numbers.** For $n\ge1$, define
$S_n=1+3+\cdots+(2n-1)$. We claim $S_n=n^2$.
At $n=1$, both sides are $1$. Now fix an arbitrary $k\ge1$ and assume
$S_k=k^2$. The next odd number is $2(k+1)-1=2k+1$. Therefore

$$S_{k+1}=S_k+(2k+1)=k^2+2k+1=(k+1)^2.$$

The first equality is the definition of the sum; the second uses the induction
hypothesis; the third is algebra. The base case and induction step prove the
claim for every $n\ge1$.

![A five by five square partitioned into successive L-shaped layers containing one, three, five, seven, and nine cells.](../../assets/figures/lessons-foundations/induction-square-layers.png)

The picture shows the geometric link: enlarging a $k$ by $k$ square to a
$(k+1)$ by $(k+1)$ square adds one row and one column, with the corner counted
only once. The added count is $(k+1)+(k+1)-1=2k+1$. The displayed five-layer
case illustrates the general counting argument; the algebraic induction proves
all positive indices.

**Counterexample discipline.** The tempting claim $n^2+n+41$ is prime for every
$n\in\mathbb N$ survives many small tests. At $n=41$, its value is
$41(41+1+1)=41\cdot43$, which is composite. A counterexample must satisfy
the hypothesis and violate the conclusion. A value outside the declared domain
does not refute a theorem about that domain.

## Practice problems

1. **PW-01:** Negate $\forall x\in\mathbb R\,\exists y\in\mathbb R:(y^2>x)$.
2. **PW-02:** Determine the truth of $\exists y\in\mathbb R\,\forall x\in\mathbb R:(y^2>x)$ and justify it.
3. **PW-03:** Prove directly that the product of an even integer and any integer is even.
4. **PW-04:** Prove by contrapositive that $n^2$ even implies $n$ even.
5. **PW-05:** Disprove the assertion that $n^2$ divisible by four implies $n$ divisible by four.
6. **PW-06:** Prove $\sum_{j=1}^n j=n(n+1)/2$ for $n\ge1$ by induction.
7. **PW-07:** Prove $2^n\ge n+1$ for every $n\in\mathbb N$ and identify where $n\ge0$ is used.
8. **PW-08:** A proposed proof says: “Assume $1+\cdots+n=n(n+1)/2$. Then the statement is true. It is also true at $n=1$.” Explain what step is missing.

## Answers and explanations

1. The negation is $\exists x\in\mathbb R\,\forall y\in\mathbb R:(y^2\le x)$.
Both quantifiers switch and the strict inequality gains its equality case.
The original is true: choose $y=\sqrt{|x|+1}$, whose square exceeds $x$.
2. It is false. For any proposed $y$, choose $x=y^2$, giving the false
requirement $y^2>y^2$. A different $y$ for each $x$ would answer another claim.
3. Let $a=2k$ and $b\in\mathbb Z$. Then $ab=2(kb)$, with $kb\in\mathbb Z$.
Thus the product is even by definition, including when either factor is zero
or negative.
4. The contrapositive says odd $n$ has odd $n^2$. For $n=2k+1$,
$n^2=4k^2+4k+1=2(2k^2+2k)+1$, which is odd. This establishes the original
implication; it does not use its converse as an assumption.
5. Take $n=2$. Its square $4$ is divisible by four, but $2$ is not.
The example meets the integer domain and the hypothesis, so one instance
suffices to disprove the universal claim.
6. At $n=1$, $1=1(2)/2$. Assuming the formula at $k$, add $k+1$:
$k(k+1)/2+(k+1)=(k+1)(k+2)/2$. This is exactly the claimed expression at
$k+1$, completing the induction.
7. At $n=0$, $1\ge1$. If $2^k\ge k+1$, then
$2^{k+1}\ge2k+2\ge k+2$. The last comparison uses $k\ge0$.
The index range is part of the reasoning, not an optional label.
8. The argument never derives the formula at $n+1$ from the formula at $n$.
Assuming a statement and restating it proves only an implication from itself
to itself. The base case cannot repair a missing induction link.

## A final proof-writing check

Before marking your own argument complete, identify its domain, its temporary
assumptions, the definition used to enter the calculation, and the definition
used to recognize the conclusion. For induction, point to the exact line where
the hypothesis is used. For a counterexample, check both hypothesis and failure.
For an existence claim, state the witness and substitute it. These checks make
a short proof clearer without replacing reasoning with a list of formal words.

## Reproducible diagrams and verification

[plot_lessons_foundations.py](../../scripts/plot_lessons_foundations.py) creates
both diagrams in PNG and SVG. [verify_lessons_foundations.py](../../scripts/verify_lessons_foundations.py)
checks the finite witness matrix, odd-layer counts, and encoded algebraic
identities. Those checks certify the encoded examples; the quantified proofs
above establish their stated infinite families.

## References and further study

Richard Hammack, [*Book of Proof*, “Logic,” “Direct Proof,” “Contrapositive Proof,” and “Mathematical Induction”](https://richardhammack.github.io/BookOfProof/), provides further exercises. Oscar Levin, [*Discrete Mathematics: An Open Introduction*](https://discrete.openmathbooks.org/dmoi4.html), connects proof methods to graphs and counting. This lesson's examples, wording, and figures are original. For a next application, try a divisibility proof in the [number theory reference](../../subjects/number-theory/number-theory.md).
