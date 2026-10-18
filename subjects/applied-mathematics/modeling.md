# Applied mathematics and mathematical modeling

**Topic ID:** APP-001  
**Classification:** Applied mathematics → conservation → modeling and evidence  
**Level:** Undergraduate engineering reference with advanced introductions  
**Content status:** Written compact reference.  
**Learner mastery:** Unassessed.

## Prerequisites

Units, calculus, linear algebra and differential equations are needed. [Statistics](../statistics/statistics.md) and [probability](../probability/probability-and-stochastic-processes.md) support uncertain data. Diagnostic: if $Q=2\ \mathrm{m^3/h}$ flows into a tank of fixed volume $10\ \mathrm{m^3}$ and the same flow exits, the hydraulic residence scale is $V/Q=5\ \mathrm h$. A time scale is not automatically a complete mixing model; the physical assumptions still matter.

## Definition

A **mathematical model** is an explicit collection of variables, equations, parameters, assumptions and input/output rules representing selected aspects of a system for a stated purpose. A **state** contains the information required by the model to predict future evolution from specified inputs. A parameter is held fixed within a modeled run; an input varies according to an imposed rule or measured history. A continuum model treats material as fields in space and time, appropriate only when the chosen scale is large enough relative to unresolved microscopic structure.

**Verification** asks whether equations and algorithms have been solved correctly. **Validation** compares predictions with independent observations for an intended use. **Calibration** estimates parameters from observations. A calibrated model can still fail validation, and a numerically converged model can still omit important physics. **Identifiability** concerns whether distinct parameter values can be distinguished from available outputs; structural identifiability is an ideal mathematical question, while practical identifiability also depends on data quality and excitation.

## Intuitive explanation

Model building is an accounting exercise followed by a test. Decide what crosses a boundary, what accumulates, and what is produced or consumed. Add constitutive relations that connect fluxes to fields, such as stress to strain or diffusive flux to concentration gradient. Choose scales to reveal dominant terms. Then test predictions against evidence that was not used to choose the parameters.

![Dimensionless concentration trajectories for a mixed tank at several reaction-to-flow ratios.](../../assets/figures/advanced/tank-model.png)

The curves start with clean liquid and approach $1/(1+\mathrm{Da})$ for dimensionless concentration. Flow and first-order reaction compete through the Damköhler number $\mathrm{Da}=kV/Q$.

## Mathematical notation

$t$ is time, $x$ position, $\rho$ mass density, $v$ velocity, $\sigma$ Cauchy stress, $b$ body force per unit mass, and $\varepsilon$ small strain. $V$ is volume, $Q$ volume flow rate, $c$ concentration and $k$ reaction rate. A superscript star denotes a dimensionless variable only where explicitly introduced. $\nabla\cdot$ is divergence and $D/Dt=\partial_t+v\cdot\nabla$ the material derivative. Use a fixed unit system before adding quantities.

## Fundamental properties

For conserved scalar density $u$, flux $J$ and source $s$, balance on a fixed control volume $\Omega$ gives

$$\frac d{dt}\int_\Omega u\,dV=-\int_{\partial\Omega}J\cdot n\,dA+\int_\Omega s\,dV.$$

With sufficient smoothness and arbitrary control volumes, the divergence theorem gives $u_t+\nabla\cdot J=s$. A constitutive law such as $J=-D\nabla u$ turns conservation into diffusion. Conservation supplies structure; it does not determine $D$ or guarantee that a Fickian law is suitable.

**Dimensional homogeneity** requires every term in an equation to have compatible units. Nondimensionalization writes $x=Lx^*$, $t=Tt^*$ and scales dependent fields. It reduces parameters to dimensionless groups and reveals ratios of effects. For $n$ dimensional variables whose dimension matrix has rank $r$, Buckingham's dimensional theorem gives $n-r$ independent dimensionless products under its dimensional assumptions. Geometric similarity alone does not ensure dynamic similarity; the relevant groups and boundary conditions must also match.

## Important formulas and identities

**Continuum mechanics.** Mass and momentum balance are

$$\partial_t\rho+\nabla\cdot(\rho v)=0,\qquad \rho\frac{Dv}{Dt}=\nabla\cdot\sigma+\rho b.$$

For an incompressible Newtonian fluid of constant viscosity $\mu$, $\nabla\cdot v=0$ and $\sigma=-pI+2\mu D$, with $D=(\nabla v+\nabla v^T)/2$. This gives $\rho(v_t+v\cdot\nabla v)=-\nabla p+\mu\nabla^2v+\rho b$ for constant $\mu$. The Reynolds number $\mathrm{Re}=\rho UL/\mu$ compares inertia to viscous stress. Small $\mathrm{Re}$ motivates a creeping-flow approximation when the remaining scales and forcing are consistent.

For small-displacement isotropic linear elasticity, $\varepsilon=(\nabla u+\nabla u^T)/2$ and $\sigma=\lambda\operatorname{tr}(\varepsilon)I+2G\varepsilon$, where $u$ is displacement and $\lambda,G$ are Lamé moduli. This constitutive law assumes small strain and linear elastic response; plasticity and finite deformation need other laws. Boundary data distinguish prescribed displacement from traction $\sigma n$.

**Signals and vibrations.** A mass–spring–damper satisfies $m\ddot x+c\dot x+kx=F(t)$ for positive $m,k$ and nonnegative $c$. Natural angular frequency is $\omega_n=\sqrt{k/m}$ and damping ratio $\zeta=c/(2\sqrt{km})$. Under zero initial conditions the transfer function from force to displacement is $H(s)=1/(ms^2+cs+k)$. A wave field can satisfy $u_{tt}=a^2u_{xx}$ with propagation speed $a$; initial displacement, initial velocity and boundary data complete the problem. Different physical models can share the same equation while assigning different units to $u$.

**Variational mechanics and fields.** Hamilton's principle makes the action $S[q]=\int(T-V)dt$ stationary with fixed endpoint configurations. The Euler–Lagrange equation is $d(\partial L/\partial\dot q)/dt-\partial L/\partial q=0$. A field energy $E[u]=\int[\frac12a|\nabla u|^2-fu]dV$ has stationary equation $-\nabla\cdot(a\nabla u)=f$ with boundary terms determining natural conditions. Stationarity is not always a minimum, especially for action in time.

**Inverse problems.** Forward problems compute observations from parameters, $y=G(\theta)$. Inverse problems infer $\theta$ from $y$. A common regularized fit minimizes $\|G(\theta)-y\|_W^2+\alpha R(\theta)$, with an explicit noise weighting and penalty. Regularization adds assumptions and trades variance against bias. Nonuniqueness, unstable inversion and model discrepancy must be distinguished from numerical solver error.

**Information and computation.** For discrete probabilities $p_i$, entropy in bits is $H=-\sum_i p_i\log_2p_i$, with $0\log_20=0$. Mutual information $I(X;Y)=\sum_{x,y}p(x,y)\log_2[p(x,y)/(p(x)p(y))]$ measures statistical dependence. A binary block code adds redundant bits; a minimum Hamming distance $d_{\min}$ permits detection of up to $d_{\min}-1$ bit errors and correction of up to $\lfloor(d_{\min}-1)/2\rfloor$ under nearest-codeword decoding. Algorithmic complexity, finite precision and conditioning constrain computation even when an exact mathematical expression exists.

**Extensions.** Logistic population growth $\dot N=rN(1-N/K)$ represents density-limited growth, not every biological mechanism. An SIR model uses $\dot S=-\beta SI/N$, $\dot I=\beta SI/N-\gamma I$, $\dot R=\gamma I$ under a closed, well-mixed population assumption. In a financial diffusion $dS=\mu Sdt+\sigma SdW$, $\mu$ and $\sigma$ describe a chosen stochastic model rather than guaranteed returns. A network's incidence matrix $B$ expresses flow balance $Bq=s$; a graph Laplacian $L=BB^T$ supports diffusion $\dot x=-Lx$ and consensus. Each extension needs domain-specific validation.

## Derivations and proofs

**Mixed reacting tank.** Assume constant volume $V$, equal inflow and outflow $Q$, perfect mixing, constant inlet concentration $c_{\mathrm{in}}>0$ and first-order consumption $kVc$. Solute balance gives

$$V\dot c=Qc_{\mathrm{in}}-Qc-kVc.$$

Set $c=c_{\mathrm{in}}C$ and $t=(V/Q)\tau$, with $V,Q>0$. Division by $Qc_{\mathrm{in}}$ yields

$$\frac{dC}{d\tau}=1-(1+\mathrm{Da})C,\qquad\mathrm{Da}=kV/Q.$$

The integrating-factor solution is $C(\tau)=1/(1+\mathrm{Da})+[C(0)-1/(1+\mathrm{Da})]e^{-(1+\mathrm{Da})\tau}$. For $k\ge0$ the steady state is stable. This derivation checks mass balance, units and limiting cases; it does not establish perfect mixing in a particular tank.

**Energy dissipation.** Multiply the unforced mass–spring–damper equation by $\dot x$. Then $d[m\dot x^2/2+kx^2/2]/dt=-c\dot x^2\le0$. Damping dissipates modeled mechanical energy. The proof also supplies a check on numerical simulations: sustained unforced growth with $c>0$ demands investigation.

## Worked examples

**1. A treatment tank.** Let $V=10\ \mathrm{m^3}$, $Q=2\ \mathrm{m^3/h}$, $k=0.1\ \mathrm h^{-1}$, $c_{\mathrm{in}}=3\ \mathrm{kg/m^3}$ and $c(0)=0$. Then $\mathrm{Da}=1/2$, steady concentration is $2\ \mathrm{kg/m^3}$, and $c(t)=2(1-e^{-0.3t})$ when $t$ is in hours. At steady state the inlet solute flow is $6\ \mathrm{kg/h}$, outlet $4$ and reaction loss $2$, checking the balance exactly.

**2. A vibration scale.** For $m=2\ \mathrm{kg}$, $k=50\ \mathrm{N/m}$ and $c=4\ \mathrm{N\,s/m}$, $\omega_n=5\ \mathrm{rad/s}$ and $\zeta=1/5$. The underdamped frequency is $\omega_d=\omega_n\sqrt{1-\zeta^2}=2\sqrt6\ \mathrm{rad/s}$. The free-motion envelope decays as $e^{-ct/(2m)}=e^{-t}$, with time in seconds. Substitution into the characteristic polynomial gives roots $-1\pm2\sqrt6\,i$.

**3. Identifiability.** Suppose a measured steady flow obeys $y=(ab)\Delta p$ with unknown positive $a,b$. One or many measurements at different known $\Delta p$ identify only the product $ab$. Replacing $(a,b)$ by $(ra,b/r)$ for any $r>0$ preserves every prediction. An additional observable or justified prior relation is required to separate the parameters; more repetitions of the same type of measurement cannot remove structural nonidentifiability.

**4. A repetition code.** Code one bit as $000$ or $111$. Their Hamming distance is three, so one corrupted bit is correctable by majority vote. With independent bit-error probability $p$, decoding error is $3p^2(1-p)+p^3=3p^2-2p^3$. At $p=0.01$, this is $0.000298$. The gain costs three transmitted bits per information bit and depends on independent-error assumptions.

## Practice problems

1. Check the dimensions of $\rho U^2$ and $\mu U/L$ and interpret their ratio.
2. For the mixed tank with $k=0$, find steady concentration and the time to reach half of it from zero.
3. A model predicts $y=ax+b$. Why cannot one exact observation uniquely identify both $a$ and $b$?
4. A positive random flow $Q$ has small standard deviation $\sigma_Q$. Linearize $\tau=V/Q$ at $Q_0>0$ and estimate its standard deviation when $V$ is exact.

## Answers and explanations

1. Both are stresses, $\mathrm{kg/(m\,s^2)}$. Their ratio is $\rho UL/\mu=\mathrm{Re}$, comparing inertia and viscosity at the chosen scales.
2. The steady concentration is $c_{\mathrm{in}}$. Since $c/c_{\mathrm{in}}=1-e^{-Qt/V}$, setting it to $1/2$ gives $t=(V/Q)\log2$.
3. One equation $ax_1+b=y_1$ describes a line of parameter pairs. Two distinct input values can identify both in the noiseless affine model, provided their difference is nonzero.
4. $\tau\approx V/Q_0-(V/Q_0^2)(Q-Q_0)$, so $\sigma_\tau\approx V\sigma_Q/Q_0^2$. This first-order uncertainty estimate assumes fluctuations are small relative to $Q_0$ and fails near zero flow.

## Common mistakes and misconceptions

Matching units is necessary but does not prove a physical equation. Fitting and validating on the same data overstates predictive evidence. Parameter uncertainty is not the same as omitted-physics discrepancy. More mesh points improve discretization only when the method is consistent and stable. A visually accurate curve can conceal nonidentifiable parameters and poor extrapolation.

## Connections to other mathematics

[Optimization](../optimization/optimization-and-control.md) supports design and inverse fitting. [Numerical analysis](../numerical-analysis/numerical-analysis.md) supplies discretization and verification. [Statistics](../statistics/statistics.md) supports experiments, inference and uncertainty. [Differential geometry](../differential-geometry/geometry-and-tensors.md) clarifies coordinate-invariant tensor fields.

## Applications

A useful engineering model records the intended decision, control volume, assumptions, units, boundary and initial conditions, parameter provenance and evidence limits. Uncertainty quantification propagates measured variation or distributions through the model; sensitivity analysis identifies influential inputs. Compare numerical error, parameter uncertainty and independent validation residuals before interpreting a prediction as design evidence.

## Optional computational examples

[Plot source](../../scripts/plot_advanced.py) generates the nondimensional tank curves. [Checks](../../scripts/verify_advanced.py) verify tank balances and solution, oscillator roots and repetition-code probabilities. These are equation-level checks, not validation of a real treatment plant.

## References and recommended reading

- David Tong, [*Dynamics and Relativity*](https://www.damtp.cam.ac.uk/user/tong/relativity.html), dimensional analysis and forces chapters: scale reasoning and mechanics.
- John W. M. Bush, MIT OpenCourseWare [18.357 Interfacial Phenomena](https://ocw.mit.edu/courses/18-357-interfacial-phenomena-fall-2010/): examples connecting continuum laws, scales and experiments.
- Russ Tedrake, [*Underactuated Robotics*](https://underactuated.mit.edu/), model systems and system-identification discussions: further applied reading. All numerical examples here are original.

## Revision and mastery status

Written 2026-10-18. Every modeling subject-map bullet is introduced with a concrete equation or example, including optional biology, finance and networks. This is a mathematical reference rather than a validated engineering design handbook. Mastery requires deriving a balance, checking dimensions, identifying assumptions and separating verification from independent validation.
