# Harmonic analysis, transforms, and special functions

**Topic ID:** HA-01.  
**Classification:** Analysis → oscillations, transforms, and asymptotic methods.  
**Level:** Undergraduate through an advanced methods bridge.  
**Content status:** Written compact reference chapter.  
**Learner mastery:** Unassessed.

## Prerequisites

Use integration, infinite series, complex exponentials, [ODEs](../differential-equations/ordinary-differential-equations.md), and orthogonality. Diagnostic: $\int_{-\pi}^\pi\sin x\cos x\,dx=0$ by oddness. The integral is an inner product: it says the two functions have no component in each other's direction under this particular interval and weight.

## Definition

**Harmonic analysis** studies representations using oscillatory building blocks. A Fourier series decomposes a periodic function into harmonics. A Fourier transform represents nonperiodic behavior by a continuum of frequencies. Other transforms choose kernels adapted to growth, causality, or discrete time. A **special function** is a named function with a well-studied defining equation, series, or integral, such as the gamma or Bessel function. Naming a solution does not remove the need to state its parameter range and normalization.

## Intuitive explanation

A transform changes the coordinate system of a function. Differentiation becomes multiplication in frequency, so a differential equation may become algebraic. Orthogonal polynomials perform a similar decomposition on finite intervals with weights. Wavelets localize scale and position, helping describe transients whose timing a global Fourier amplitude does not reveal. Asymptotic methods ask which terms control a limit, including cases where a small coefficient multiplies the highest derivative and cannot safely be discarded near a boundary.

![Finite Fourier sums of the sawtooth function](../../assets/figures/analysis/fourier-sawtooth.png)

For $-\pi<x<\pi$, the target is $f(x)=x$ extended periodically. Exact finite sums are $S_N(x)=2\sum_{n=1}^N(-1)^{n+1}\sin(nx)/n$ for $N=1,5,25$. The target jump is not joined across the endpoints; at the jump the Fourier limit is the midpoint zero. Both axes are dimensionless, with $x$ interpreted as a radian phase.

## Mathematical notation

Our angular-frequency convention is

$$\widehat f(\omega)=\int_{\mathbb R}f(t)e^{-i\omega t}dt,\qquad f(t)=\frac1{2\pi}\int_{\mathbb R}\widehat f(\omega)e^{i\omega t}d\omega$$

when inversion conditions hold, for example for Schwartz functions. Angular frequency $\omega$ in rad/s equals $2\pi\nu$ for frequency $\nu$ in Hz. Convolution is $(f*g)(t)=\int f(\tau)g(t-\tau)d\tau$. $\mathcal L$ denotes a one-sided Laplace transform; the bilateral Z transform is $X(z)=\sum_{n\in\mathbb Z}x[n]z^{-n}$ with its region of convergence included. $f\sim g$ means $f/g\to1$ in the stated limit, not equality.

## Fundamental properties

For $f\in L^2[-\pi,\pi]$, the trigonometric system is complete and its Fourier partial sums converge in $L^2$ to $f$. Pointwise convergence is a separate assertion. For a periodic piecewise continuously differentiable function, the series converges at each point to the average of the one-sided limits. Near a jump, Gibbs oscillation does not vanish in peak relative height although its affected interval narrows. These convergence theorems are cited without full proofs.

The Fourier transform initially defined by an absolutely convergent integral for $L^1$ functions extends to $L^2$ with Plancherel identity $\int|f|^2dt=(1/2\pi)\int|\widehat f|^2d\omega$. For rapidly decreasing smooth functions, $\widehat{f'}=i\omega\widehat f$ and $\widehat{f*g}=\widehat f\,\widehat g$. Distribution theory extends these formulas beyond integrable functions: under this normalization $\widehat1=2\pi\delta$ and $\widehat\delta=1$. These are distribution identities, not ordinary convergent integrals of a constant.

## Important formulas and identities

For a $2\pi$-periodic function,

$$f\sim\frac{a_0}2+\sum_{n\ge1}(a_n\cos nx+b_n\sin nx),\quad a_n=\frac1\pi\int_{-\pi}^\pi f\cos nx\,dx,\quad b_n=\frac1\pi\int_{-\pi}^\pi f\sin nx\,dx.$$

For $a>0$, $\widehat{e^{-at^2}}=\sqrt{\pi/a}\,e^{-\omega^2/(4a)}$. The Laplace transform of $e^{at}$ is $1/(s-a)$ for $\operatorname{Re}s>\operatorname{Re}a$. For the causal sequence $x[n]=a^n$ when $n\ge0$ and zero otherwise, $X(z)=1/(1-az^{-1})$ for $|z|>|a|$. The rational expression without its convergence region does not uniquely specify a bilateral sequence.

For a causal linear time-invariant system with zero initial state, output satisfies $y=h*u$, and transfer function $H(s)=Y(s)/U(s)=\mathcal Lh(s)$ where transforms exist. Initial-state contributions require separate terms. The Z-domain version uses discrete convolution and obeys the same distinction.

For $\operatorname{Re}z>0$,

$$\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}dt,\qquad\Gamma(z+1)=z\Gamma(z).$$

For $a,b>0$, $B(a,b)=\int_0^1t^{a-1}(1-t)^{b-1}dt=\Gamma(a)\Gamma(b)/\Gamma(a+b)$. The recurrence gives $\Gamma(n+1)=n!$ for nonnegative integers. Analytic continuation extends gamma away from its poles at nonpositive integers; its integral definition alone does not apply there.

## Derivations and proofs

**Sawtooth coefficients.** For $f(x)=x$ on $(-\pi,\pi)$, oddness makes $a_0=a_n=0$. Integration by parts gives

$$b_n=\frac2\pi\int_0^\pi x\sin(nx)dx=\frac{2(-1)^{n+1}}n.$$

The boundary term supplies the coefficient; the remaining sine term vanishes at both endpoints. The cited pointwise theorem identifies the interior sum with $x$ and the jump sum with zero.

**Gamma recurrence and beta relation.** Integrating $\Gamma(z+1)$ by parts gives $[-t^ze^{-t}]_0^\infty+z\Gamma(z)$; for $\operatorname{Re}z>0$ both endpoint terms vanish. For positive $a,b$, multiply the two gamma integrals and change variables $x=ru$, $y=r(1-u)$, where $r>0$, $0<u<1$, and the Jacobian is $r$. The product becomes $\Gamma(a+b)B(a,b)$. Nonnegative integrands justify the product integration and change of order, proving the relation.

Orthogonal polynomials are orthogonal under a specified weighted integral. **Legendre polynomials** satisfy $[(1-x^2)P_n']'+n(n+1)P_n=0$ on $[-1,1]$ and normalization $P_n(1)=1$. Their orthogonality is $\int_{-1}^1P_mP_n dx=2\delta_{mn}/(2n+1)$. First examples are $P_0=1$, $P_1=x$, $P_2=(3x^2-1)/2$. **Bessel's equation** is $x^2y''+xy'+(x^2-\nu^2)y=0$. For integer order zero, its regular solution is

$$J_0(x)=\sum_{k=0}^\infty\frac{(-1)^k(x^2/4)^k}{(k!)^2}.$$

Substitution into the equation determines the recurrence. The independent solution $Y_0$ is singular at zero, so regularity at the origin in a circular membrane problem selects $J_0$. Boundary zeros of Bessel functions then determine allowable radial frequencies; ordinary sine modes would encode the wrong radial operator.

For a wavelet $\psi$ with zero mean, translated and dilated copies are $\psi_{a,b}(t)=|a|^{-1/2}\psi((t-b)/a)$, $a\ne0$. The Haar mother is one on $[0,1/2)$, minus one on $[1/2,1)$, and zero elsewhere; its zero mean detects differences between adjacent averages. A short-time Fourier transform instead multiplies by a shifted window before Fourier transformation, giving a time-frequency description whose resolution depends on window width. The uncertainty principle constrains joint concentration, so arbitrarily precise time and frequency localization are unavailable simultaneously.

## Worked examples

**1. Convolution response.** For $h(t)=e^{-t}$ and input $u(t)=1$, both causal, $y(t)=\int_0^te^{-(t-\tau)}d\tau=1-e^{-t}$ for $t\ge0$. It satisfies $y'+y=1$, $y(0)=0$. The transform calculation agrees: $Y=1/[s(s+1)]=1/s-1/(s+1)$ for $\operatorname{Re}s>0$.

**2. A beta integral.** Evaluate $\int_0^1\sqrt{x(1-x)}dx$. It is $B(3/2,3/2)$. With $\Gamma(1/2)=\sqrt\pi$, the recurrence gives $\Gamma(3/2)=\sqrt\pi/2$ and $\Gamma(3)=2$, so the answer is $\pi/8$. Independently, the substitution $x=(1+u)/2$ turns the integral into one quarter of the area under the unit upper semicircle, again $\pi/8$.

**3. Sampling and aliasing.** Sample a $7$ Hz cosine at $10$ samples/s: $x[n]=\cos(2\pi7n/10)$. Since cosine is even and integer multiples of $2\pi n$ do not change it, this equals $\cos(2\pi3n/10)$. Thus the samples cannot distinguish seven Hz from three Hz. Ideal reconstruction of a bandlimited signal with no frequencies above $B$ Hz requires sampling rate greater than $2B$ Hz, plus the ideal reconstruction assumptions; an antialias filter is needed when a physical signal is not truly bandlimited.

**4. Singular perturbation.** Solve $\varepsilon y'+y=0$, $y(0)=1$, $\varepsilon>0$. Exactly $y=e^{-t/\varepsilon}$. For every fixed $t>0$, $y\to0$ as $\varepsilon\to0$, so the reduced outer equation is $y=0$. It cannot satisfy the initial value. Introduce inner variable $\tau=t/\varepsilon$, giving $dy/d\tau+y=0$ and inner solution $e^{-\tau}$. The layer has thickness of order $\varepsilon$; dropping the derivative was invalid there.

![Exact initial-layer solutions for three small parameters](../../assets/figures/analysis/boundary-layer.png)

The curves are exactly $e^{-t/\varepsilon}$ for $\varepsilon=3/10,1/10,3/100$, with dimensionless $t$ and $y$. Each meets the initial condition one, while the outer approximation zero does not. The rapidly changing interval shrinks as the parameter decreases.

## Practice problems

1. Find Fourier coefficients of $f(x)=3+2\cos2x-\sin3x$.
2. Find the Z transform and convergence region of the causal sequence $(1/2)^n$.
3. Compute $\Gamma(5)$ and $B(2,3)$.
4. Find the first three nonzero terms of $J_0(x)$, and state an asymptotic meaning of this truncation near zero.

## Answers and explanations

1. Orthogonality gives $a_0=6$, $a_2=2$, $b_3=-1$, with all other coefficients zero. The factor one half in the constant term matters.
2. The geometric series gives $X(z)=1/[1-(1/2)z^{-1}]$, convergent for $|z|>1/2$; the exterior region encodes causality here.
3. $\Gamma(5)=4!=24$. The beta relation gives $B(2,3)=1!2!/4!=1/12$; direct polynomial integration of $x(1-x)^2$ checks it.
4. $J_0(x)=1-x^2/4+x^4/64+O(x^6)$ as $x\to0$. The big-O statement bounds the omitted error by a constant times $|x|^6$ in a neighborhood; it does not assert the truncation is exact.

## Common mistakes and misconceptions

Fourier transform normalizations move factors of $2\pi$; declare one before using a table. Frequency in Hz differs from angular frequency. A transfer function assumes zero initial state. Pointwise convergence and $L^2$ convergence are different promises. An asymptotic expansion need not converge as its number of terms grows; its definition instead controls errors as the parameter approaches its stated limit.

## Connections to other mathematics

[Complex analysis](../complex-analysis/complex-analysis.md) supports contour inversion. [PDEs](../differential-equations/partial-differential-equations.md) use eigenfunction expansions. [Real analysis](../analysis/real-analysis-and-measure.md) explains $L^2$ and distributional transforms. For small-parameter algebraic equations, regular perturbation expands $y=y_0+\varepsilon y_1+\cdots$ and matches orders, but only an error argument establishes its validity over a chosen domain.

## Applications

Vibration analysis decomposes displacement into frequencies; the transform of displacement in metres has units metre-seconds under the stated time transform. Circular pipe acoustics and membranes lead to Bessel radial modes. Sensor sampling must relate the analog bandwidth to sample rate. Wavelets can isolate brief faults, while a global spectrum alone may conceal when a transient occurred. The physical model and window choice determine what conclusions the analysis supports.

## Optional computational examples

[plot_analysis.py](../../scripts/plot_analysis.py) draws exact finite Fourier sums and a boundary-layer comparison. [verify_analysis.py](../../scripts/verify_analysis.py) checks coefficients, convolution, transforms, special-function values, aliasing identities, and perturbation residuals. Truncated sums are explicitly labeled approximations to the infinite representation.

## References and recommended reading

Sources and further study: NIST [DLMF §1.14, Integral Transforms](https://dlmf.nist.gov/1.14), with normalization conventions checked against those stated here; [DLMF Chapter 10, Bessel Functions](https://dlmf.nist.gov/10), for equations and expansions; Jiří Lebl, [Notes on Diffy Qs](https://www.jirka.org/diffyqs/), Fourier series, Laplace transforms, and eigenfunction methods. Wavelet completeness, Plancherel, and sampling reconstruction are advanced results stated without full proofs.

## Revision and mastery status

Written 2026-10-18. Scope: a compact transforms and methods reference covering all group 24 themes, with explicit definitions and representative calculations. Mastery requires stating conventions, checking convergence regions, distinguishing exact and asymptotic expressions, and explaining aliasing. Learner mastery remains unassessed.
