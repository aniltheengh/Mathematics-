# Statistics, inference and data analysis

**Topic ID:** STAT-001  
**Classification:** Statistics → inference → statistical models  
**Level:** Undergraduate reference with advanced introductions  
**Content status:** Written compact reference.  
**Learner mastery:** Unassessed.

<!-- guided-lessons:start -->
**Study in depth:** [From base rates to evidence: a guided probability and inference lesson](../../lessons/advanced/probability-and-inference.md)
<!-- guided-lessons:end -->

## Prerequisites

Understand means, algebra, probability distributions, logarithms and basic matrices. Diagnostic: observations $2,4,6$ have mean $4$, but their sample variance is $(4+0+4)/2=4$, since an estimated mean uses one degree of freedom. [Probability](../probability/probability-and-stochastic-processes.md) supplies the stochastic language. Calculus is needed for likelihood optimization.

## Definition

A **statistical model** is a family of data distributions $\{P_\theta:\theta\in\Theta\}$ with unknown parameter $\theta$. A **statistic** is a function of observed data; an **estimator** is a statistic used to infer a parameter. An **estimate** is its realized numerical value. A **sampling design** specifies how observations enter the study. Random sampling supports population inference; randomized assignment supports causal comparison under the experiment's assumptions. Neither automatically removes missing-data bias, interference or measurement error.

Descriptive statistics summarize observed values. For data $x_1,\ldots,x_n$, the mean is $\bar x=n^{-1}\sum x_i$, the sample variance is $s^2=\sum(x_i-\bar x)^2/(n-1)$ for $n>1$, and the median splits the ordered sample. A box plot exposes spread and outliers; a scatter plot displays association; a time plot exposes drift hidden by a histogram. Choose displays before fitting complicated models.

## Intuitive explanation

Inference asks how much a result would change if the study were repeated under the same design. The distribution of individual measurements and the distribution of an estimated mean are different objects. A narrow interval for the mean can coexist with wide part-to-part variation. A model makes such questions answerable by stating which variation is included and which assumptions connect the sample to the intended population.

![Three calibration measurements, fitted least-squares line, and vertical residuals.](../../assets/figures/advanced/regression.png)

Here the residuals sum to zero because the line includes an intercept. The figure shows fit geometry; three points alone cannot establish reliable predictive performance.

## Mathematical notation

$X_i$ denotes a random observation and $x_i$ its observed value. $\theta$ is a parameter, $\hat\theta$ an estimator, $L(\theta;x)$ a likelihood, and $\ell=\log L$. $\alpha$ is a chosen type-I error level, $\beta_{\mathrm{II}}$ a type-II error probability, and $1-\beta_{\mathrm{II}}$ power. Bold $X$ below denotes a design matrix, not a scalar measurement. Covariance matrices have squared measurement units in their diagonal entries.

## Fundamental properties

**Bias** is $E_\theta\hat\theta-\theta$. **Consistency** means $\hat\theta_n\to\theta$ in probability as sample size grows. Mean-square error decomposes as $\operatorname{MSE}(\hat\theta)=\operatorname{Var}\hat\theta+\operatorname{Bias}(\hat\theta)^2$. An unbiased estimator need not minimize MSE.

A **confidence interval procedure** $C(X)$ has level $1-\alpha$ if $P_\theta(\theta\in C(X))\ge1-\alpha$ throughout the stated model. After observation, frequentist coverage refers to the procedure's repetitions, not a posterior probability assigned to the fixed parameter. For independent normal observations with unknown variance,

$$\bar X\pm t_{1-\alpha/2,n-1}\frac S{\sqrt n}$$

has exact coverage, where $t_{q,\nu}$ is a Student-$t$ quantile. With nonnormal data it may be approximate, and strong dependence invalidates the usual standard error.

A **hypothesis test** rejects a null model in a prechosen rejection region. A $p$-value is a null-model tail probability for a statistic at least as extreme as observed, not $P(H_0\mid x)$. Report effect sizes in physical units as well as significance. Power depends on a specified alternative, sample size and noise. For $m$ tests, Bonferroni thresholds $\alpha/m$ bound the probability of at least one false rejection by $\alpha$, without requiring independence.

## Important formulas and identities

For independent observations with density or mass $f_\theta$, $L(\theta;x)=\prod_i f_\theta(x_i)$. A maximum-likelihood estimator maximizes this function over its allowed parameter space. A Bayesian posterior is

$$p(\theta\mid x)=\frac{p(x\mid\theta)p(\theta)}{\int p(x\mid u)p(u)\,du},$$

provided the denominator is finite and positive. Priors express a model choice and require sensitivity assessment; a credible interval is a posterior probability statement.

In linear regression, $y=X\beta+\varepsilon$ with $E\varepsilon=0$ and $\operatorname{Cov}\varepsilon=\sigma^2I$. If $X$ has full column rank, $\hat\beta=(X^TX)^{-1}X^Ty$ and $\operatorname{Cov}\hat\beta=\sigma^2(X^TX)^{-1}$. Normal errors additionally give the usual exact $t$ and $F$ procedures. **ANOVA** decomposes sums of squares to compare nested linear models; it is not a license to assume normality or equal variance from the name of the method.

A **generalized linear model** specifies an exponential-family response and a link $g(E[Y\mid x])=x^T\beta$. Logistic regression uses $\log(p/(1-p))=x^T\beta$ for binary data; Poisson regression often uses $\log\lambda=x^T\beta$ for counts. Response variance is then tied to the chosen family rather than constant by default.

For a stationary AR(1) time series $X_t=\phi X_{t-1}+\varepsilon_t$, $|\phi|<1$, independent zero-mean innovations of variance $\sigma_\varepsilon^2$ give $\operatorname{Var}X_t=\sigma_\varepsilon^2/(1-\phi^2)$ and autocorrelation $\phi^{|h|}$. **Multivariate statistics** studies joint vectors: principal components are covariance eigenvectors ordered by variance. Variable scaling matters because changing units changes unstandardized PCA.

**Statistical learning** estimates predictive relationships. Fit preprocessing only on training data, choose tuning parameters with validation or cross-validation, and reserve test data for a final performance estimate. For dependent time data, preserve temporal order; random shuffling can leak future information. Penalized regression, such as minimizing $\|y-X\beta\|^2+\lambda\|\beta\|^2$, trades fit against coefficient size.

## Derivations and proofs

**Least-squares normal equations.** Let $Q(\beta)=\|y-X\beta\|^2$. Differentiation gives $\nabla Q=-2X^T(y-X\beta)$. At a minimizer, $X^TX\hat\beta=X^Ty$. Full column rank makes $X^TX$ positive definite, hence the minimizer is unique. Moreover $X^T\hat\varepsilon=0$, so the residual is perpendicular to every fitted column. This establishes the fit; it does not establish the stochastic error model.

**MSE decomposition.** Write $\hat\theta-\theta=(\hat\theta-E\hat\theta)+(E\hat\theta-\theta)$. On squaring and taking expectations, the cross term is zero. The two remaining terms are variance and squared bias.

## Worked examples

**1. A mean interval.** Independent normal pipe-diameter errors, in millimetres, are $-2,-1,0,1,2$. Thus $n=5$, $\bar x=0$, $s^2=10/4=5/2$. A 95% interval is $0\pm t_{0.975,4}/\sqrt2\approx\pm1.963\ \mathrm{mm}$, using $t_{0.975,4}\approx2.77645$. The interval estimates mean error, not a tolerance range containing 95% of manufactured diameters.

**2. Calibration line.** For $(x,y)=(0,1),(1,2),(2,2)$, means are $\bar x=1$ and $\bar y=5/3$. The slope is $\sum(x_i-\bar x)(y_i-\bar y)/\sum(x_i-\bar x)^2=1/2$, and the intercept is $7/6$. Predictions are $7/6,5/3,13/6$; residuals $-1/6,1/3,-1/6$ sum to zero and have squared sum $1/6$. Independent substitution checks the calculation.

**3. Bayesian defect fraction.** A uniform $\operatorname{Beta}(1,1)$ prior and binomial observations of two defects in ten parts give posterior $\operatorname{Beta}(3,9)$ because the likelihood contributes $p^2(1-p)^8$. The posterior mean is $3/12=1/4$, while the maximum-likelihood estimate is $2/10=1/5$. The difference is the finite-sample influence of the stated prior.

**4. Survival and censoring.** With exponential lifetimes at constant hazard $\lambda$, three observed failures over total exposure $T=1200\ \mathrm h$, including right-censored exposure, give likelihood proportional to $\lambda^3e^{-1200\lambda}$. Its log derivative is $3/\lambda-1200$, giving $\hat\lambda=1/400\ \mathrm h^{-1}$. The estimated mean lifetime is $400\ \mathrm h$. Independent censoring and constant hazard are essential assumptions.

## Practice problems

1. Why does repeatedly measuring one part not automatically estimate variation across a production population?
2. For Bernoulli observations $1,0,1,1$, find the likelihood maximizer.
3. Ten null hypotheses are tested at a familywise level $0.05$ using Bonferroni. What individual threshold is used?
4. An AR(1) model has $\phi=1/2$ and innovation variance $3$. Find its stationary variance and lag-two autocorrelation.

## Answers and explanations

1. Repeated readings primarily measure instrument repeatability conditional on that part. Population variation needs independently sampled parts and a design separating measurement and part effects.
2. $L(p)=p^3(1-p)$. For $0<p<1$, $\ell'(p)=3/p-1/(1-p)=0$ gives $p=3/4$; the endpoints have zero likelihood, so this is the maximum.
3. Use $0.005$. The union bound gives $P(\text{any false rejection})\le\sum_{j=1}^{10}0.005=0.05$.
4. The variance is $3/(1-1/4)=4$ and lag-two correlation $(1/2)^2=1/4$. Serial dependence means four observations generally contain less information than four independent observations with the same marginal variance.

## Common mistakes and misconceptions

Statistical significance does not measure engineering importance. Failure to reject does not prove equality. Correlation alone does not establish causation. Selecting the best result after many unreported trials changes the effective multiplicity. A bootstrap resamples from an empirical model; it cannot repair an unrepresentative sample by itself. MCMC output is dependent and requires convergence and effective-sample-size checks.

## Connections to other mathematics

[Optimization](../optimization/optimization-and-control.md) supplies fitting methods; [probability](../probability/probability-and-stochastic-processes.md) supplies sampling distributions; [modeling](../applied-mathematics/modeling.md) separates parameter uncertainty from model discrepancy.

## Applications

In experimental design, randomization limits allocation bias, replication estimates variation, and blocking removes known nuisance variation. A factorial experiment estimates interactions that changing one factor at a time can miss. Survival analysis uses $S(t)=P(T>t)$ and hazard $h(t)=f(t)/S(t)$ when a density exists; right censoring records survival beyond an observation time rather than a failure at that time. Reliability claims require stated operating conditions.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) generates the calibration graph. [Checks](../../scripts/verify_advanced.py) verify normal equations, sums of squares, conjugate-posterior moments and censored-likelihood optimization. Computational inference may use quadrature, bootstrap or MCMC, but these algorithms approximate a stated model rather than supply its scientific justification.

## References and recommended reading

- NIST/SEMATECH, [*e-Handbook*, confidence limits for the mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm): exact interval assumptions and coverage interpretation.
- NIST/SEMATECH, [tests for a process mean](https://www.itl.nist.gov/div898/handbook/prc/section2/prc22.htm): test-statistic conventions.
- Pishro-Nik, [open textbook](https://www.probabilitycourse.com/), mathematical statistics chapters: likelihood and Bayesian foundations. Original data and examples here are constructed for teaching.

## Revision and mastery status

Written 2026-10-18. This chapter treats every statistics subject-map bullet at reference depth, not every model's full inferential theory. Mastery requires identifying the sampling unit, stating a model, fitting it, checking residual structure and interpreting an interval in the correct framework.
