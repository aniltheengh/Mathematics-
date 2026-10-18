# Number theory: divisibility, congruences, and primes

**Topic ID:** NTH-001  
**Classification:** Number theory → elementary methods and advanced bridges  
**Level:** Introductory university, with algebraic and analytic orientation  
**Content status:** Written compact reference; advanced theorems labeled.  
**Learner mastery:** Unassessed.

## Prerequisites

Use [integer arithmetic and prime factorization](../numbers/arithmetic-and-number-systems.md)
and [proof methods](../foundations/logic-and-proof.md). Diagnostic:
$17=3\cdot5+2$, so the remainder of $17$ on division by $5$ is $2$.
A divisibility statement $a\mid b$ asserts an integer multiplier, not merely
that the real quotient exists.

## Definition

For integers $a,b$ and positive modulus $m$, the congruence
$a\equiv b\pmod m$ means $m\mid(a-b)$. It is an equivalence relation, and
the residue classes form $\mathbb Z/m\mathbb Z$. A residue is a **unit**
when it has a multiplicative inverse modulo $m$; this occurs exactly when
$\gcd(a,m)=1$.

A Diophantine equation asks for integer solutions. Euler's totient
$\varphi(n)$ counts residues in $\{1,\ldots,n\}$ coprime to $n$.
The divisor functions $\tau(n)$ and $\sigma(n)$ count positive divisors and
sum them, respectively. An arithmetic function has positive integer inputs;
it is multiplicative if $f(ab)=f(a)f(b)$ for coprime $a,b$.

For an odd prime $p$, a nonzero residue $a$ is a quadratic residue if
$x^2\equiv a\pmod p$ has a solution. The Legendre symbol
$(a/p)$ is $0$ if $p\mid a$, $1$ for a nonzero square residue, and $-1$
otherwise. A finite simple continued fraction is
$[a_0;a_1,\ldots,a_k]=a_0+1/(a_1+1/(\cdots+1/a_k))$, with the usual
positive integer later entries. Initial truncations are its convergents.

## Intuitive explanation

Modular arithmetic identifies integers differing by whole turns around a
clock, but its algebra depends on the modulus. Every nonzero residue is
invertible modulo a prime; this fails for composite moduli. For example
$2\cdot3\equiv0\pmod6$ even though neither factor is zero modulo $6$.

The Euclidean algorithm replaces a large divisibility problem by a smaller
one without changing its common divisors. Continued fractions reuse the same
division-with-remainder idea to produce efficient rational approximations.
Algebraic number theory enlarges the number system, while analytic number
theory studies integer patterns through limits, sums, and complex functions.

## Mathematical notation

$\gcd(a,b)$ is positive unless both inputs are zero. A prime factorization
is written $n=\prod_{p\mid n}p^{\alpha_p}$. $\pi(x)$ counts primes at most
the real number $x$; it is distinct from the geometric constant $\pi$.
$f(x)\sim g(x)$ as $x\to\infty$ means their ratio tends to $1$.
A number field $K$ is a finite extension of $\mathbb Q$, and
$\mathcal O_K$ denotes its ring of algebraic integers.

## Fundamental properties

**Euclidean algorithm.** If $a=bq+r$, then $\gcd(a,b)=\gcd(b,r)$.
Repeated division ends at a zero remainder; the last nonzero remainder is the
gcd. Back substitution gives **Bézout's identity**
$ua+vb=\gcd(a,b)$ for some integers $u,v$.
Consequently $ax+by=c$ is solvable in integers exactly when
$\gcd(a,b)\mid c$. When $a,b\ne0$, one solution $(x_0,y_0)$ generates all
solutions $x=x_0+(b/d)t$, $y=y_0-(a/d)t$, $t\in\mathbb Z$, with $d=\gcd(a,b)$.

**Chinese remainder theorem.** For pairwise coprime positive moduli
$m_1,\ldots,m_k$, any specified residues determine one class modulo
$M=\prod m_i$. With two noncoprime moduli, the two congruences are compatible
exactly when their residues agree modulo the gcd; the combined modulus is
then the lcm. The unrestricted pairwise-coprime theorem must not be applied
blindly to overlapping moduli.

**Fermat and Euler theorems.** For prime $p$ and $p\nmid a$,
$a^{p-1}\equiv1\pmod p$. More generally $a^{\varphi(n)}\equiv1\pmod n$
when $\gcd(a,n)=1$. Fermat's theorem also implies $a^p\equiv a\pmod p$
without a coprimality assumption. Its converse is false: a composite number
can pass a particular Fermat congruence.

## Important formulas and identities

Prime factorization gives

$$\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right),\quad
\tau(n)=\prod_{p\mid n}(\alpha_p+1),\quad
\sigma(n)=\prod_{p\mid n}\frac{p^{\alpha_p+1}-1}{p-1}.$$

For distinct odd primes $p,q$, quadratic reciprocity and its supplements are

$$\left(\frac pq\right)\left(\frac qp\right)
=(-1)^{(p-1)(q-1)/4},$$
$$\left(\frac{-1}p\right)=(-1)^{(p-1)/2},\qquad
\left(\frac2p\right)=(-1)^{(p^2-1)/8}.$$

These are deep elementary theorems cited without proof. Euler's criterion
$a^{(p-1)/2}\equiv(a/p)\pmod p$ gives a computational test for odd prime $p$
and $p\nmid a$.

If $p_k/q_k=[a_0;\ldots,a_k]$, put
$p_{-2}=0,p_{-1}=1,q_{-2}=1,q_{-1}=0$. Then
$p_k=a_kp_{k-1}+p_{k-2}$ and $q_k=a_kq_{k-1}+q_{k-2}$.
For irrational $\alpha$ its convergents satisfy
$|\alpha-p_k/q_k|<1/q_k^2$ (cited approximation theorem).

**Analytic bridge.** For complex $s$ with $\operatorname{Re}s>1$,

$$\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}
=\prod_{p\ \mathrm{prime}}(1-p^{-s})^{-1}.$$

Absolute convergence justifies expansion of the product into integers through
unique factorization. Analytic continuation extends $\zeta$ meromorphically
with a simple pole at $1$; the original series does not converge everywhere
the continuation is defined. The prime number theorem says
$\pi(x)\sim x/\ln x$; this deep asymptotic theorem is cited, not proved here.

**Algebraic bridge.** An algebraic integer satisfies a monic polynomial with
integer coefficients. For $K=\mathbb Q(i)$, $\mathcal O_K=\mathbb Z[i]$,
and the norm is $N(a+bi)=a^2+b^2$. A rational prime can split:
$5=(2+i)(2-i)$. Unique factorization of elements fails in some number fields,
where ideal factorization supplies a more stable language. A nonzero ideal
of the full ring of integers factors uniquely into prime ideals (cited
Dedekind-domain theorem); an arbitrary subring need not have this property.

## Derivations and proofs

**Gcd invariance.** A common divisor of $a,b$ divides $a-qb=r$. Conversely,
a common divisor of $b,r$ divides $qb+r=a$. Thus the sets of common divisors
coincide. The decreasing nonnegative remainders guarantee termination.

**Linear Diophantine criterion.** Assume $a,b$ are not both zero, so $d=\gcd(a,b)>0$. If both are zero, $ax+by=c$ has every integer pair as a solution when $c=0$, and none otherwise. For the nonzero-coefficient case, any common divisor of $a,b$ divides
$ax+by$, so $d\mid c$ is necessary. If $d\mid c$, multiply
$ua+vb=d$ by $c/d$ to construct a solution, proving sufficiency.

**Euler's theorem.** Multiplication by a unit $a$ permutes the finite list
of units $u_1,\ldots,u_{\varphi(n)}$ modulo $n$. Multiply all congruences:
$a^{\varphi(n)}\prod u_i\equiv\prod u_i$. The product of units is invertible,
so it can be canceled, yielding the result. Canceling nonunits would not be
valid in this argument.

## Worked examples

**1. Gcd and a modular inverse.** Divide $252=198+54$,
$198=3\cdot54+36$, $54=36+18$, and $36=2\cdot18$.
Thus $d=18=4\cdot252-5\cdot198$. For an inverse example,
$1=3\cdot7-2\cdot10$, so $7^{-1}\equiv3\pmod{10}$.
Check $7\cdot3=21\equiv1$.

**2. Integer solutions.** Solve $84x+30y=6$. Since
$6=3\cdot30-84$, take $x_0=-1,y_0=3$.
All solutions are $x=-1+5t$, $y=3-14t$. Substitution gives
$84(-1+5t)+30(3-14t)=6$ for every integer $t$.

**3. Chinese remainders.** Solve $x\equiv2\pmod3$,
$x\equiv3\pmod5$, $x\equiv2\pmod7$.
Write $x=2+3k$. The second congruence gives $3k\equiv1\pmod5$, hence
$k\equiv2\pmod5$ and $x=8+15t$. The third gives $1+t\equiv2\pmod7$,
so $x=23+105u$. Direct reduction of $23$ gives the three requested residues.

**4. Reciprocity and approximation.** Since $11\equiv3\pmod4$ and
$3\equiv3\pmod4$, reciprocity gives $(3/11)=-(11/3)$.
Now $11\equiv2\pmod3$, a nonsquare, so $(3/11)=1$.
Check $5^2\equiv3\pmod{11}$. Separately,
$\sqrt2=[1;2,2,\ldots]$ has convergent $17/12$, with exact error

$$\left|\sqrt2-\frac{17}{12}\right|
=\frac1{144(\sqrt2+17/12)}<\frac1{144}.$$

The rationalizing identity checks both the approximation and its bound.

**5. Small RSA arithmetic.** Let $p=5,q=11,n=55$, so
$\varphi(n)=40$. Choose $e=3$ and $d=27$ because $ed=81\equiv1\pmod{40}$.
For message $m=7$, encryption gives $c=7^3\bmod55=13$; decryption gives
$13^{27}\bmod55=7$. Euler's theorem establishes recovery here because
$\gcd(7,55)=1$. This deliberately tiny arithmetic example illustrates the
congruences; it is not a secure cryptographic construction.

## Practice problems

1. **NTH-01:** Find the inverse of $11$ modulo $26$, if it exists.
2. **NTH-02:** Decide whether $12x+18y=5$ has integer solutions.
3. **NTH-03:** Compute $\varphi(36),\tau(36),\sigma(36)$.
4. **NTH-04:** Solve $x\equiv1\pmod4$, $x\equiv3\pmod6$.
5. **NTH-05:** Find all square residues modulo $7$, including zero.
6. **NTH-06:** Find the continued-fraction expansion of $43/19$ and its last two convergents.

## Answers and explanations

1. $11\cdot19=209=8\cdot26+1$, so the inverse is $19\pmod{26}$.
It exists because the gcd is $1$.
2. No: $\gcd(12,18)=6$ does not divide $5$. A real solution would not
answer the integer question.
3. Since $36=2^2\cdot3^2$, the values are
$36(1/2)(2/3)=12$, $(2+1)(2+1)=9$, and $(1+2+4)(1+3+9)=91$.
4. The residues agree modulo $2$, so compatibility holds. Testing
$1,5,9$ modulo $12$ finds $9\equiv3\pmod6$. Thus $x\equiv9\pmod{12}$;
the combined modulus is the lcm, not $24$.
5. Squaring $0,1,2,3$ gives $0,1,4,2$; negatives repeat these values.
The set is $\{0,1,2,4\}$.
6. Euclidean divisions give $43=2\cdot19+5$, $19=3\cdot5+4$,
$5=4+1$, $4=4\cdot1$. Thus $[2;3,1,4]$; the penultimate convergent is
$9/4$ and the final one is $43/19$. Reversing the nesting checks the fraction.

## Common mistakes and misconceptions

Cancellation modulo $m$ requires an invertible factor or a changed modulus.
For example $2x\equiv2\pmod6$ implies $x\equiv1\pmod3$, not necessarily
$x\equiv1\pmod6$. A large exponent does not justify Euler reduction when
the base is not coprime to the modulus. An asymptotic prime count is not an
exact formula for each finite $x$.

## Connections to other mathematics

[Abstract algebra](../abstract-algebra/abstract-algebra.md) explains units,
finite fields, and field extensions. [Discrete mathematics](../discrete/discrete-mathematics.md)
uses remainders for finite states and counting. The zeta function connects
prime factorization to [series and convergence](../analysis/functions-limits-and-series.md).

## Applications

Two ideal cyclic maintenance schedules repeat every $12$ and $18$ days.
Starting together, they next coincide after $\operatorname{lcm}(12,18)=36$
days. If their starting offsets differ, compatibility becomes a congruence
condition modulo $\gcd(12,18)=6$. Dates and operational exceptions require
information beyond this integer periodic model.

## Optional computational examples

Repeated squaring computes modular powers without constructing the full
integer power. It repeatedly squares the base modulo $n$ and multiplies only
for the $1$ bits of the exponent. Exact integer arithmetic is essential; a
floating-point approximation followed by rounding need not preserve residues.

## References and recommended reading

William Stein, [*Elementary Number Theory: Primes, Congruences, and Secrets*, author page](https://wstein.org/ent/), is the reference route for congruences, continued fractions, and cryptographic examples. J. S. Milne, [*Algebraic Number Theory*, “Rings of Integers” and “Dedekind Domains; Factorization”](https://www.jmilne.org/math/CourseNotes/ant.html), supports the advanced ideal-theoretic orientation. NIST, [DLMF §25.2, “Definition and Expansions”](https://dlmf.nist.gov/25.2), states the zeta series/product domain and continuation. Quadratic reciprocity and the prime number theorem are cited without their long proofs.

## Revision and mastery status

Written 2026-10-18; learner mastery unassessed. Give a Bézout certificate,
check congruence compatibility, and state the coprimality condition of Euler's
theorem. Full reciprocity proofs, prime distribution estimates, class groups,
and cryptographic protocol design are deeper subjects beyond this chapter.
