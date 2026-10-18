# From base rates to evidence: a guided probability and inference lesson

**Lesson ID:** LES-ADV-001  
**Level:** Early university; calculus appears only in the likelihood derivation.  
**Prerequisites:** Fractions, sums, elementary derivatives, and the definitions in [probability](../../subjects/probability/probability-and-stochastic-processes.md).  
**Objectives:** Condition on evidence correctly; derive means and variances; distinguish a sampling law from a likelihood and a posterior; interpret a test and an interval under stated assumptions.  
**Status:** Written guided lesson; learner mastery remains unassessed.

Use this lesson with paper beside the screen. At each stage, identify what is fixed, what is random, and which probability distribution is being used. The reference chapter [Statistics, inference and data analysis](../../subjects/statistics/statistics.md) supplies a compact map of the larger subject. Here we stay with a few models long enough to derive their consequences. All measurements and data below are constructed teaching examples.

## Stage 1: turn an alarm into the right conditional probability

Suppose a test reports an alarm $A$ about a defective part $D$. Define prevalence $p=P(D)$, sensitivity $s=P(A\mid D)$, and false-alarm probability $f=P(A\mid D^c)$. These are three different inputs. Sensitivity asks about alarms among defective parts. The desired probability $P(D\mid A)$ asks about defects among alarmed parts. Reversing the conditioning changes the denominator.

Partition the alarm event into two disjoint cases: a defective part produces it, or a good part produces it. Multiplication of conditional probabilities gives

$$P(A\cap D)=sp,\qquad P(A\cap D^c)=f(1-p).$$

Therefore, provided $sp+f(1-p)>0$,

$$P(D\mid A)=\frac{sp}{sp+f(1-p)}.$$

The denominator is the probability of observing an alarm at all. This derivation needs the law of total probability, not an independence assumption between defect and alarm; those events are deliberately related.

**Worked example 1: count the alarmed parts.** Let $p=1/100$, $s=9/10$, and $f=1/100$. In a hypothetical population of $10,000$ parts with exactly the corresponding proportions, $100$ are defective, of which $90$ alarm. Of the $9,900$ good parts, $99$ alarm. Thus $189$ parts alarm and $90$ are defective, giving

$$P(D\mid A)=\frac{90}{189}=\frac{10}{21}\approx0.47619.$$

The same answer follows from the probability formula: $(9/1000)/(189/10000)=10/21$. The population counts visualize weights in the model; an actual random sample need not contain exactly these counts. Even a sensitive test can produce many false alarms when defects are rare.

![Posterior defect probability versus prevalence for sensitivity 0.9 and false-alarm probability 0.01; the points at prevalence 0.01 and 0.10 are marked.](../../assets/figures/lessons-advanced/base-rates.png)

If prevalence instead becomes $1/10$ while both test rates stay fixed, the posterior becomes $(9/100)/(9/100+9/1000)=10/11$. This is not a contradiction: the test is applied to a different population. Applying a rate from a factory screening population to a preselected batch can therefore give a misleading conclusion.

For $0<p<1$ and $f>0$, the odds form is especially useful:

$$\frac{P(D\mid A)}{P(D^c\mid A)}=\frac{s}{f}\frac{p}{1-p}.$$

The ratio $s/f$ multiplies prior odds. Two successive alarm likelihood ratios may be multiplied only when the required conditional joint model justifies it. Repeating the same sensor reading does not automatically create independent new evidence.

**Pause and explain:** Why is $0.9$ not the answer to the worked example? It is the probability of an alarm conditional on a defect, while the question conditions on an alarm. Writing both denominators in words is a reliable way to detect the reversal.

## Stage 2: derive expectation, variance and shared error

For a finite-valued random variable $X$, expectation is the probability-weighted average $EX=\sum_x xP(X=x)$. Variance is $\operatorname{Var}X=E[(X-EX)^2]$, requiring a finite second moment. Expanding the square gives

$$\operatorname{Var}X=E[X^2]-2(EX)^2+(EX)^2=E[X^2]-(EX)^2.$$

For an event indicator $I$, equal to one on success and zero otherwise, $I^2=I$. If $P(I=1)=p$, then $EI=p$ and $\operatorname{Var}I=p-p^2=p(1-p)$. This derivation explains the Bernoulli variance rather than treating it as a table entry.

Linearity gives $E(X+Y)=EX+EY$ without independence. Write centered variables $X_c=X-EX$ and $Y_c=Y-EY$. Expanding $(X_c+Y_c)^2$ gives

$$\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y),$$

where $\operatorname{Cov}(X,Y)=E[X_cY_c]$. Independence implies zero covariance when the second moments exist, but zero covariance need not imply independence. For example, a symmetric uniform $X$ on $[-1,1]$ has zero covariance with $X^2$, although the second variable is completely determined by the first.

For independent Bernoulli indicators $I_1,\ldots,I_n$ with common success probability $p$, the count $K=\sum I_i$ obeys

$$EK=np,\qquad\operatorname{Var}K=np(1-p),\qquad
E(K/n)=p,\quad\operatorname{Var}(K/n)=\frac{p(1-p)}n.$$

The factor $1/n$ comes from summing variances and dividing by $n^2$. Dependence can change that conclusion materially.

**Worked example 2: averaging sensors with a common disturbance.** Let readings be $X_i=\mu+Z+\varepsilon_i$. Assume $EZ=E\varepsilon_i=0$, $\operatorname{Var}Z=4\ \mathrm{mm^2}$, $\operatorname{Var}\varepsilon_i=1\ \mathrm{mm^2}$, and all noise variables are mutually independent. Then each reading has variance $5\ \mathrm{mm^2}$, but two different readings have covariance $4\ \mathrm{mm^2}$ because both include $Z$. For their average,

$$\operatorname{Var}\bar X=4+\frac1n\quad\text{in square millimetres}.$$

With four sensors the variance is $17/4$, not $5/4$. Averaging reduces independent noise but does not remove the common disturbance. The limiting standard deviation is $2\ \mathrm{mm}$, so claiming arbitrarily precise measurement by buying more identical sensors would overlook the model's shared error.

## Stage 3: distinguish the sampling law from the likelihood

Assume $n$ trials are independent, have the same fixed success probability $p$, and are classified correctly. Every specified success/failure sequence with $k$ successes has probability $p^k(1-p)^{n-k}$. There are $\binom nk$ such sequences, hence

$$P_p(K=k)=\binom nk p^k(1-p)^{n-k},\qquad k=0,\ldots,n.$$

This is the **sampling distribution**: fix $p$, and compare possible data counts $k$. Once a count $k$ is observed, the same expression viewed as a function of $p$ is the **likelihood**. It need not integrate to one over $p$; a likelihood ranks parameters by how much probability they assign to the observed data.

**Worked example 3: six successes in eight trials.** Observe $K=6$ with $n=8$. Apart from the constant $\binom86=28$, the likelihood is $p^6(1-p)^2$. For $0<p<1$, its log derivative is

$$\ell'(p)=\frac6p-\frac2{1-p}.$$

Setting it to zero gives $6(1-p)=2p$, hence $\hat p=3/4$. The second derivative is negative throughout the interior, and the likelihood is zero at both endpoints, proving this is the global maximum. Comparing $p=3/4$ against $p=1/2$ gives the likelihood ratio

$$\frac{L(3/4)}{L(1/2)}=\frac{729}{256}\approx2.84766.$$

This is evidence measured on a likelihood scale. It is not a posterior probability of either parameter, and it does not say future success is certain.

![Binomial sampling laws for eight trials at probabilities one half and three quarters, beside the likelihood curve for six observed successes.](../../assets/figures/lessons-advanced/binomial-evidence.png)

The figure separates the two questions: its left panel varies the random count while holding each parameter fixed; its right varies the parameter after fixing the observed count. Similar-looking formulas have different roles because different quantities are being varied.

## Stage 4: interpret tests, intervals and posterior probabilities

To test $H_0:p=1/2$ against a higher success probability using $K=6$, one possible predeclared statistic is the number of successes. Under the null,

$$P_{1/2}(K\ge6)=\frac{\binom86+\binom87+\binom88}{2^8}
=\frac{37}{256}\approx0.14453.$$

The upper-tail $p$-value is a probability of data at least this extreme under a fixed null model. It is not the probability that the null is true. A symmetric two-sided tail rule counts $K\le2$ or $K\ge6$, giving $37/128\approx0.28906$. Different test statistics and tail conventions must be specified before interpreting the number. Neither result establishes an engineering effect size or a causal improvement.

**Worked example 4: an exact upper bound after zero failures.** Inspect $n=10$ independent parts from a process with fixed unknown failure probability $p$, and observe no failures. Under the model, $P_p(K=0)=(1-p)^{10}$. A nonrandomized one-sided 95% exact binomial upper confidence limit after this outcome solves

$$ (1-p_U)^{10}=\frac1{20},\qquad p_U=1-20^{-1/10}\approx0.25887.$$

The calculation uses the exact binomial law rather than a normal approximation, which is poor at an observed proportion of zero. More generally the procedure defines $p_U(k)$ by $P_{p_U(k)}(K\le k)=0.05$ for $k<n$, with $p_U(n)=1$. Inverting these tail tests gives coverage at least 95%; discreteness can make it conservative. The reported bound does not assert that $p$ itself is random or that 95% of individual parts fall below a probability. It shows that ten failure-free trials still allow substantial failure probability.

A Bayesian calculation adds a prior distribution. With a uniform $\operatorname{Beta}(1,1)$ prior and the earlier six successes in eight trials, posterior density is proportional to $p^6(1-p)^2$, hence is $\operatorname{Beta}(7,3)$. Its normalized density is $252p^6(1-p)^2$ on $(0,1)$. Its mean is $7/10$, and exact integration gives

$$P(p>1/2\mid K=6)=\int_{1/2}^1 252p^6(1-p)^2\,dp=\frac{233}{256}.$$

This is a probability about the parameter under the stated prior and data model. It answers a different question from the null tail $37/256$. There is no inconsistency in the two numbers. Changing the prior changes the posterior, especially with only eight observations; assessing that sensitivity belongs to an honest Bayesian analysis.

## Practice problems

1. Keep sensitivity $0.9$ and false-alarm probability $0.01$. At what prevalence does an alarm make a defect and a good part equally probable?
2. A Bernoulli indicator has success probability $2/5$. Derive its expectation and variance using $I^2=I$.
3. Four independent readings have common variance $9\ \mathrm{mm^2}$. Find the variance and standard deviation of their average.
4. Two centered measurements each have variance $5$ and covariance $4$. Find the variance of their difference and explain the result.
5. For eight independent trials at $p=1/2$, calculate $P(K=6)$ and distinguish it from $P(K\ge6)$.
6. With $K=1$ success in four trials, maximize the binomial likelihood by differentiation and check the endpoints.
7. After zero failures in twenty independent trials, give the exact one-sided 95% upper failure-probability limit and compare it with the ten-trial result.
8. With a uniform prior and one success in two trials, obtain the posterior density and calculate $P(p>1/2\mid K=1)$ exactly.

## Answers and explanations

1. Set $0.9p=0.01(1-p)$, because posterior odds equal one when true- and false-alarm weights agree. Thus $p=1/91$. An alarm's interpretation changes continuously through this prevalence; sensitivity itself has not changed.
2. $EI=2/5$ and $E[I^2]=2/5$. Therefore $\operatorname{Var}I=2/5-(2/5)^2=6/25$.
3. Independence gives variance $4(9)/4^2=9/4\ \mathrm{mm^2}$ and standard deviation $3/2\ \mathrm{mm}$. Standard deviations are not added in place of variances.
4. The variance is $5+5-2(4)=2$. Common error cancels in a difference, even though it survives in an average. This conclusion uses the specified covariance.
5. Exactly six has probability $28/256=7/64$. At least six adds counts seven and eight, giving $37/256$. A single observed outcome's probability is generally smaller than the relevant tail probability.
6. $\ell'(p)=1/p-3/(1-p)=0$ gives $p=1/4$. The likelihood $4p(1-p)^3$ vanishes at zero and one, and its log second derivative is negative in the interior. Thus the stationary point is the unique global maximizer.
7. The limit is $1-20^{-1/20}\approx0.13911$, smaller than $0.25887$. More failure-free exposure tightens this model-based upper limit but does not prove a zero failure probability.
8. The likelihood is proportional to $p(1-p)$, so the posterior is $\operatorname{Beta}(2,2)$ with density $6p(1-p)$. Symmetry about $1/2$, or direct integration, gives posterior probability $1/2$ above $1/2$.

## What to retain and how to check it

Draw the conditioning event before substituting into Bayes' rule. Derive an indicator's variance before memorizing a binomial formula. Write which quantity varies when interpreting a sampling distribution or likelihood. A confidence interval's coverage, a null tail probability and a Bayesian posterior probability are separate statements with separate assumptions. All can be useful, but they cannot be exchanged by relabeling a percentage.

The original graphs are reproduced by [plot_lessons_advanced.py](../../scripts/plot_lessons_advanced.py); exact event arithmetic, likelihood derivatives, posterior integrals and interval formulas are checked in [verify_lessons_advanced.py](../../scripts/verify_lessons_advanced.py). Those checks verify the encoded examples, not the independence of real data. For further proofs see Pishro-Nik's [open probability textbook](https://www.probabilitycourse.com/) and NIST's [statistical methods handbook](https://www.itl.nist.gov/div898/handbook/). Next, change one probability in worked example 1, recompute the two alarm counts, and explain the changed posterior in a complete sentence.
