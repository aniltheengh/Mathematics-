# Probability and stochastic processes

**Topic ID:** PROB-001  
**Classification:** Probability → random variables → stochastic processes  
**Level:** Undergraduate reference with graduate introductions  
**Content status:** Written compact reference; advanced results stated with hypotheses, not fully proved.  
**Learner mastery:** Unassessed.

## Prerequisites

Sets, functions, finite sums, derivatives and integrals are needed; measure theory is needed for the rigorous process results. Diagnostic: if $P(A)=1/3$, what is $P(A^c)$? It is $2/3$, since the disjoint events exhaust the sample space. Probability measures mathematical uncertainty; the choice of model must still be justified by data or a physical argument.

## Definition

A **probability space** $(\Omega,\mathcal F,P)$ comprises outcomes $\Omega$, a sigma-algebra $\mathcal F$ of measurable events, and a countably additive measure with $P(\Omega)=1$. Countable additivity says $P(\bigcup_i A_i)=\sum_iP(A_i)$ for pairwise disjoint measurable events. A **random variable** is a measurable map $X:\Omega\to\mathbb R$. Its cumulative distribution function is $F_X(x)=P(X\le x)$, not the value of $X$ in one experiment.

For $P(B)>0$, conditional probability is $P(A\mid B)=P(A\cap B)/P(B)$. Events are independent if $P(A\cap B)=P(A)P(B)$; pairwise independence of a family need not imply joint independence. A discrete variable has mass function $p_X(x)=P(X=x)$. An absolutely continuous variable has density $f_X\ge0$ satisfying $P(X\in A)=\int_A f_X(x)\,dx$. Mixed distributions also exist: a valve may have a positive probability of zero leakage and a continuous distribution of positive leakage.

## Intuitive explanation

Probability assigns consistent weights to possible outcomes. Conditioning removes outcomes incompatible with observed information and renormalizes the remaining weights. A stochastic process is a time-indexed collection of random variables; its joint laws describe how uncertainty at different times fits together. A histogram of a single variable therefore cannot identify the dependence of an entire process.

![Poisson probability masses at rate-time product two, and exponential survival at rate 0.2 per hour.](../../assets/figures/advanced/probability.png)

The left graph concerns integer counts. The right concerns continuous waiting time. Their horizontal axes and probability conventions differ deliberately.

## Mathematical notation

$E[X]$ denotes expectation when $E|X|<\infty$; $\operatorname{Var}(X)=E[(X-EX)^2]$ requires a finite second moment. $\operatorname{Cov}(X,Y)=E[(X-EX)(Y-EY)]$. $\mathcal F_t$ records information available by time $t$; a filtration satisfies $\mathcal F_s\subseteq\mathcal F_t$ for $s\le t$. Rates $\lambda$ have inverse-time units. $N(\mu,\sigma^2)$ denotes a normal law, and $\Rightarrow$ denotes convergence in distribution.

## Fundamental properties

Expectation is linear without independence. For square-integrable variables,

$$\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y).$$

Independence implies zero covariance when the moments exist; the converse fails, for example $X$ uniform on $[-1,1]$ and $Y=X^2$. A joint density yields $f_X(x)=\int f_{X,Y}(x,y)\,dy$ and, where $f_X(x)>0$, $f_{Y\mid X}(y\mid x)=f_{X,Y}(x,y)/f_X(x)$.

**Conditional expectation** $E[X\mid\mathcal G]$ is the $\mathcal G$-measurable integrable variable $Z$ satisfying $E[Z1_A]=E[X1_A]$ for all $A\in\mathcal G$, determined almost surely. When $X\in L^2$, it gives the best mean-square predictor among $\mathcal G$-measurable square-integrable variables. The tower rule says $E[E[X\mid\mathcal G]]=EX$.

**Limit theorems, stated without full proofs.** For independent identically distributed integrable $X_i$, the strong law gives $n^{-1}\sum_{i=1}^nX_i\to EX_1$ almost surely. If also $0<\sigma^2=\operatorname{Var}X_1<\infty$, the central limit theorem gives $\sqrt n(\bar X_n-\mu)/\sigma\Rightarrow N(0,1)$. These are asymptotic results; neither supplies a universal finite-sample error bound, and infinite-variance data require other arguments.

## Important formulas and identities

Bayes' rule for a finite partition $(H_i)$ with $P(B)>0$ is

$$P(H_j\mid B)=\frac{P(B\mid H_j)P(H_j)}{\sum_iP(B\mid H_i)P(H_i)}.$$

For a differentiable monotone transformation $Y=g(X)$ whose derivative is nonzero, $f_Y(y)=f_X(g^{-1}(y))|(g^{-1})'(y)|$ on the transformed support. Multiple inverse branches contribute a sum. In several dimensions, the corresponding factor is the absolute determinant of the inverse Jacobian.

The total-variance identity is

$$\operatorname{Var}X=E[\operatorname{Var}(X\mid\mathcal G)]+\operatorname{Var}(E[X\mid\mathcal G]).$$

A discrete-time **Markov chain** satisfies $P(X_{n+1}=j\mid X_0,\ldots,X_n)=P_{X_nj}$. Rows of $P$ sum to one. A stationary row distribution obeys $\pi P=\pi$. A **Poisson process** of rate $\lambda>0$ starts at zero, has independent stationary increments and $N(t)-N(s)\sim\operatorname{Poisson}(\lambda(t-s))$. Its waiting times are independent exponentials of rate $\lambda$.

A **martingale** $M_t$ is adapted, integrable and obeys $E[M_t\mid\mathcal F_s]=M_s$ for $s\le t$. Standard **Brownian motion** $W_t$ has continuous paths, $W_0=0$, independent increments, and $W_t-W_s\sim N(0,t-s)$. Its continuous paths are almost surely nowhere differentiable; ordinary velocity is unavailable.

For an Itô equation $dX_t=a(t,X_t)dt+b(t,X_t)dW_t$ and $f\in C^{1,2}$, Itô's formula is

$$df(t,X_t)=\left(f_t+af_x+\tfrac12b^2f_{xx}\right)dt+bf_x\,dW_t.$$

The stochastic integral is defined by a mean-square limit for adapted square-integrable integrands, then extended under appropriate local conditions. Global Lipschitz and linear-growth conditions on $a,b$ are standard sufficient hypotheses for a unique strong solution with square-integrable initial data. These existence and Itô results are cited, not proved here.

## Derivations and proofs

**Proposition.** The total-variance identity holds for $X\in L^2$. Put $m=E[X\mid\mathcal G]$ and write $X-EX=(X-m)+(m-EX)$. Square and take expectations. The cross term vanishes because $E[X-m\mid\mathcal G]=0$ and $m-EX$ is measurable with respect to $\mathcal G$. The first squared term is the expected conditional variance, and the second is $\operatorname{Var}m$. No independence assumption is needed.

**Poisson waiting-time derivation.** If $T$ is the first arrival, $\{T>t\}=\{N(t)=0\}$, hence $P(T>t)=e^{-\lambda t}$ for $t\ge0$. Differentiating the CDF gives $f_T(t)=\lambda e^{-\lambda t}$. Integrating by parts yields $ET=1/\lambda$.

## Worked examples

**1. Alarm and base rate.** A component is defective with probability $0.02$. An alarm detects a defect with probability $0.95$ and triggers on a good component with probability $0.04$. Then $P(A)=0.95(0.02)+0.04(0.98)=0.0582$. Bayes gives $P(D\mid A)=0.019/0.0582=95/291\approx0.32646$. The numerator is less than the total alarm probability, and the posterior is below the detector sensitivity because good components are common.

**2. Maintenance counts.** Independent faults arrive at rate $0.2\ \mathrm h^{-1}$. In ten hours $N\sim\operatorname{Poisson}(2)$, so $P(N\ge1)=1-e^{-2}\approx0.86466$, while $P(N=2)=2e^{-2}$. The expected first waiting time is $5\ \mathrm h$. A real wear-out process need not have a constant rate, so this model specifically excludes aging effects.

**3. Two operating states.** Let $P=\begin{pmatrix}0.9&0.1\\0.4&0.6\end{pmatrix}$. Write $\pi=(p,1-p)$. Solving $p=0.9p+0.4(1-p)$ gives $p=4/5$. Thus $\pi=(4/5,1/5)$; direct multiplication checks stationarity. Starting in state one gives one-step distribution $(0.9,0.1)$, which is different from equilibrium.

**4. Stochastic exponential.** For $dX=\mu Xdt+\sigma XdW$ with $X_0>0$, applying Itô's rule to $\log X$ gives $d\log X=(\mu-\sigma^2/2)dt+\sigma dW$. Thus $X_t=X_0e^{(\mu-\sigma^2/2)t+\sigma W_t}$. Checking by Itô's formula recovers both coefficients; omitting the half-variance term would give the wrong drift.

## Practice problems

1. Can two disjoint events of positive probability be independent? Explain.
2. If $X$ is uniform on $[0,1]$ and $Y=X^2$, find $F_Y$ and $f_Y$.
3. Independent Bernoulli variables have success probability $1/4$. Find the mean and variance of their average over $100$ trials.
4. Show directly that $N(t)-\lambda t$ is a martingale for the Poisson process's natural filtration.

## Answers and explanations

1. No. Their intersection has probability zero, but the product of their positive probabilities is positive.
2. For $0\le y\le1$, $P(Y\le y)=P(X\le\sqrt y)=\sqrt y$. Thus $f_Y(y)=1/(2\sqrt y)$ for $0<y<1$, and zero outside. The endpoint singularity is integrable and the density integrates to one.
3. Linearity gives $E\bar X=1/4$. Independence gives $\operatorname{Var}\bar X=(1/4)(3/4)/100=3/1600$; its standard deviation is $\sqrt3/40$.
4. For $s<t$, the increment has conditional mean $\lambda(t-s)$ because it is independent of past information. Therefore $E[N(t)-\lambda t\mid\mathcal F_s]=N(s)-\lambda s$; integrability follows from $EN(t)=\lambda t$.

## Common mistakes and misconceptions

A density value can exceed one; its integral is the probability. $P(X=x)=0$ for a continuous distribution does not make the outcome impossible in the logical sense. Zero correlation is weaker than independence. Multiplying failure probabilities assumes independence. A law of large numbers does not force the next toss to correct an earlier imbalance. Optional stopping for martingales requires conditions; a stopping strategy alone does not guarantee preservation of expectation.

## Connections to other mathematics

[Statistics](../statistics/statistics.md) infers unknown model parameters; [numerical analysis](../numerical-analysis/numerical-analysis.md) approximates expectations; [functional analysis](../functional-analysis/functional-analysis.md) explains conditional expectation as projection. The [subject map](../../CONTENTS.md) records measure theory prerequisites.

## Applications

Reliability, noisy sensors, queues and random forcing use distinct process models. State the time unit and test whether stationarity and independence are defensible. Brownian forcing is an idealization at a chosen time scale, not a microscopic description of every physical disturbance.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) reproduces the displayed mass and survival curves. [Checks](../../scripts/verify_advanced.py) verify alarm fractions, Markov stationarity, waiting-time moments and transformed-density normalization; they do not prove the limit theorems or SDE existence results.

## References and recommended reading

- Hossein Pishro-Nik, [*Introduction to Probability, Statistics, and Random Processes*](https://www.probabilitycourse.com/), chapters on conditional probability, joint variables, limit theorems and random processes: source for further proofs.
- MIT OpenCourseWare, [18.S096 lecture notes](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/lecture-notes/), stochastic processes and Itô calculus: advanced follow-up. The original examples here are independent teaching examples.

## Revision and mastery status

Written 2026-10-18. Scope covers the subject-map entries at reference depth; it is not a complete measure-theoretic probability course. Mastery requires explaining conditioning, deriving a transformed law and distinguishing a process's marginal law from its dependence structure. Deep convergence and stochastic-calculus theorems remain sourced results.
