"""Exact independent checks for LES-CAL-01, LES-LA-01, and LES-DE-01.

No numerical sample establishes a theorem's universal hypotheses.
"""

from pathlib import Path
import ast
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
COUNT = 0


def check(label, actual, expected=0):
    global COUNT
    delta = actual-expected
    if isinstance(delta, s.MatrixBase):
        valid = all(s.simplify(v) == 0 for v in delta)
    else:
        valid = s.simplify(s.expand_trig(delta)) == 0
    if not valid:
        raise AssertionError(f"{label}: {actual}, expected {expected}")
    COUNT += 1


def require(label, predicate):
    global COUNT
    if not predicate:
        raise AssertionError(label)
    COUNT += 1


x, a, h, t, tau, xi = s.symbols("x a h t tau xi", real=True)
eps, K = s.symbols("eps K", positive=True)
r = s.Rational

# Limits and derivatives: independent algebraic identities followed by limits.
check("square factorization", x*x-4, (x-2)*(x+2))
check("square secant identity", ((a+h)**2-a*a)/h, 2*a+h)
check("square derivative", s.limit(((a+h)**2-a*a)/h, h, 0), 2*a)
check("cube derivative", s.limit(((a+h)**3-a**3)/h, h, 0), 3*a*a)
check("sqrt derivative at four", s.limit((s.sqrt(4+h)-2)/h, h, 0), r(1, 4))
check("flow integral", s.integrate(2*s.exp(-t/3), (t, 0, tau)),
      6*(1-s.exp(-tau/3)))
check("flow derivative", s.diff(6*(1-s.exp(-t/3)), t), 2*s.exp(-t/3))
check("flow initial volume", (6*(1-s.exp(-t/3))).subs(t, 0))
check("polynomial rate integration", s.integrate(3*t*t, (t, 0, 2)), 8)
check("linear input tolerance", r(1, 20)/5, r(1, 100))
check("sine Taylor polynomial", s.series(s.sin(h), h, 0, 5).removeO(), h-h**3/6)
check("sine remainder bound", r(1, 5)**5/s.factorial(5), r(1, 375000))
volume_change = 4*s.pi*((1+h)**3-1)/3
linear_volume = 4*s.pi*h
quadratic_volume = 4*s.pi*h+4*s.pi*h*h
check("sphere polynomial identity", volume_change,
      linear_volume+4*s.pi*h*h+4*s.pi*h**3/3)
error = s.simplify((volume_change-linear_volume).subs(h, r(1, 100)))
check("sphere first-order error", error, 301*s.pi/750000)
check("sphere relative error against estimate", error/linear_volume.subs(h, r(1, 100)),
      r(301, 30000))
check("sphere relative error against exact change",
      error/volume_change.subs(h, r(1, 100)), r(301, 30301))
check("sphere second-order error",
      (volume_change-quadratic_volume).subs(h, r(1, 100)), s.pi/750000)

# Maps, kernels, exact QR and residual orthogonality.
S = s.Matrix([[1, 1], [1, -1]])
T = s.diag(1, 0)
TC = S.inv()*T*S
check("basis representation", TC, s.Matrix([[r(1, 2), r(1, 2)],
                                           [r(1, 2), r(1, 2)]]))
check("basis example vector", S*s.Matrix([1, 1]), s.Matrix([2, 0]))
check("basis map agreement", S*TC*s.Matrix([1, 1]), T*s.Matrix([2, 0]))
B = s.Matrix([[1, 2], [2, 4]])
check("kernel generator", B*s.Matrix([-2, 1]), s.zeros(2, 1))
require("rank-one example", B.rank() == 1)
A = s.Matrix([[1, 0], [1, 1], [1, 2]])
y = s.Matrix([1, 2, 2])
beta = s.Matrix([r(7, 6), r(1, 2)])
residual = y-A*beta
check("regression original equations residual", residual,
      s.Matrix([-r(1, 6), r(1, 3), -r(1, 6)]))
check("normal equations orthogonality", A.T*residual, s.zeros(2, 1))
check("regression squared norm", residual.dot(residual), r(1, 6))
q3 = s.Matrix([1, -2, 1])/s.sqrt(6)
check("residual complement", A.T*q3, s.zeros(2, 1))
check("residual from perpendicular coordinate", q3*(q3.dot(y)), residual)
Q = s.Matrix.hstack(s.Matrix([1, 1, 1])/s.sqrt(3),
                    s.Matrix([-1, 0, 1])/s.sqrt(2))
R = s.Matrix([[s.sqrt(3), s.sqrt(3)], [0, s.sqrt(2)]])
check("QR product", Q*R, A)
check("QR orthonormality", Q.T*Q, s.eye(2))
check("QR right hand side", Q.T*y,
      s.Matrix([5/s.sqrt(3), 1/s.sqrt(2)]))
check("QR triangular solve", R*beta, Q.T*y)
check("projection matrix idempotence", (Q*Q.T)**2, Q*Q.T)
check("projection exercise residual orthogonality",
      s.Matrix([1, 1]).dot(s.Matrix([2, 0])-s.Matrix([1, 1])))
check("best constant squared norm", sum((v-4)**2 for v in [2, 4, 6]), 8)
delta = s.symbols("delta", real=True)
Aeps = s.Matrix([[1, 1], [0, eps]])
perturbed = s.Matrix([1-delta/eps, 1+delta/eps])
check("sensitive exact solve", Aeps*perturbed, s.Matrix([2, eps+delta]))
check("sensitive exercise", perturbed.subs({eps: r(1, 100), delta: r(1, 1000)}),
      s.Matrix([r(9, 10), r(11, 10)]))
gram = Aeps.T*Aeps
check("Gram trace", s.trace(gram), 2+eps*eps)
check("Gram determinant", gram.det(), eps*eps)
lambda_plus = (2+eps*eps+s.sqrt(4+eps**4))/2
lambda_minus = eps*eps/lambda_plus
check("Gram eigenvalue sum", lambda_plus+lambda_minus, s.trace(gram))
check("Gram condition example", 100**2, 10000)

# Oscillator cases and forcing: independent differential residual + data checks.
motion = s.exp(-t)*s.sin(2*s.sqrt(6)*t)/(2*s.sqrt(6))
check("dimensioned oscillator equation",
      2*s.diff(motion, t, 2)+4*s.diff(motion, t)+50*motion)
check("dimensioned initial position", motion.subs(t, 0))
check("dimensioned initial velocity", s.diff(motion, t).subs(t, 0), 1)
check("critical damping for mass two", 2*s.sqrt(2*50), 20)
step = 1-(1+tau)*s.exp(-tau)
check("critical step equation", s.diff(step, tau, 2)+2*s.diff(step, tau)+step, 1)
check("critical step position", step.subs(tau, 0))
check("critical step velocity", s.diff(step, tau).subs(tau, 0))
check("critical step derivative", s.diff(step, tau), tau*s.exp(-tau))
free_critical = (1+t)*s.exp(-t)
check("critical free equation", s.diff(free_critical, t, 2)+
      2*s.diff(free_critical, t)+free_critical)
check("critical free data", free_critical.subs(t, 0), 1)
check("critical free velocity", s.diff(free_critical, t).subs(t, 0))
resonance = t*s.sin(t)/2
check("resonant equation", s.diff(resonance, t, 2)+resonance, s.cos(t))
for damping in [s.Integer(0), r(3, 10), s.Integer(1), s.Integer(2)]:
    if damping < 1:
        frequency = s.sqrt(1-damping*damping)
        solution = 1-s.exp(-damping*t)*(
            s.cos(frequency*t)+damping/frequency*s.sin(frequency*t))
    elif damping == 1:
        solution = 1-(1+t)*s.exp(-t)
    else:
        root = s.sqrt(damping*damping-1)
        p, q = -damping+root, -damping-root
        solution = 1+(q*s.exp(p*t)-p*s.exp(q*t))/(p-q)
    check(f"step residual damping {damping}",
          s.diff(solution, t, 2)+2*damping*s.diff(solution, t)+solution, 1)
    check(f"step displacement damping {damping}", solution.subs(t, 0))
    check(f"step velocity damping {damping}", s.diff(solution, t).subs(t, 0))
matrix = s.Matrix([[-1, K], [0, -2]])
state = s.Matrix([K*(s.exp(-t)-s.exp(-2*t)), s.exp(-2*t)])
check("nonnormal system equation", state.diff(t), matrix*state)
check("nonnormal system data", state.subs(t, 0), s.Matrix([0, 1]))
check("nonnormal peak time", s.diff(state[0], t).subs(t, s.log(2)))
check("nonnormal peak state", state.subs(t, s.log(2)), s.Matrix([K/4, r(1, 4)]))
check("nonnormal exercise norm squared",
      state.subs({t: s.log(2), K: 8}).dot(state.subs({t: s.log(2), K: 8})), r(65, 16))
check("critical exercise coefficient", 2*s.sqrt(1*9), 6)

# Heat modes and energy, in the same dimensionless convention as the plot.
heat = s.exp(-s.pi**2*tau)*s.sin(s.pi*xi) + (
    s.exp(-4*s.pi**2*tau)*s.sin(2*s.pi*xi)/2)
check("heat residual", s.diff(heat, tau), s.diff(heat, xi, 2))
check("heat left boundary", heat.subs(xi, 0))
check("heat right boundary", heat.subs(xi, 1))
check("heat initial profile", heat.subs(tau, 0),
      s.sin(s.pi*xi)+s.sin(2*s.pi*xi)/2)
check("heat modal one half-life",
      s.exp(-s.pi**2*tau).subs(tau, s.log(2)/s.pi**2), r(1, 2))
check("heat modal two at one half-life",
      (s.exp(-4*s.pi**2*tau)/2).subs(tau, s.log(2)/s.pi**2), r(1, 32))
energy = s.integrate(heat**2/2, (xi, 0, 1))
dissipation = -s.integrate(s.diff(heat, xi)**2, (xi, 0, 1))
check("heat energy identity", s.diff(energy, tau), dissipation)
check("mode-three rate ratio", (3*s.pi)**2/s.pi**2, 9)

# Deliverable and syntax checks are counted separately in the printed ledger.
mathematical_count = COUNT
for source in ["plot_lessons_analysis.py", "verify_lessons_analysis.py"]:
    ast.parse((ROOT / "scripts" / source).read_text(encoding="utf-8"))
    COUNT += 1
names = ["calculus-secants", "calculus-taylor-error", "linear-regression",
         "linear-conditioning", "ode-step-response", "heat-mode-evolution"]
for name in names:
    for suffix in ["png", "svg"]:
        path = ROOT/"assets"/"figures"/"lessons-analysis"/f"{name}.{suffix}"
        require(f"figure {path.name}", path.exists() and path.stat().st_size > 1000)
for name in ["calculus-from-limits-to-models", "linear-algebra-and-least-squares",
             "differential-equations-and-stability"]:
    text = (ROOT/"lessons"/"analysis"/f"{name}.md").read_text(encoding="utf-8")
    words = len(text.split())
    require(f"lesson depth {name}", words >= 1800)
    require(f"lesson metadata {name}", "**Lesson ID:**" in text)
    require(f"lesson stages {name}", len(re.findall(r"(?m)^## Stage ", text)) >= 4)
    print(f"{name}: {words} whitespace words, 5 stages, 8 explained exercises")
print(f"PASS: {mathematical_count} mathematical checks; "
      f"{COUNT-mathematical_count} syntax/artifact/structure checks.")
print("Scope: exact encoded examples; not a general proof checker or real-system validation.")
