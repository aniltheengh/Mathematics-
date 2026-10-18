"""Independent exact checks for worked calculations in eight analysis chapters.

These checks verify encoded examples, not every theorem or its hypotheses.
Run: python scripts/verify_analysis.py
"""

from pathlib import Path
import re

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
COUNT = 0


def equal(name, actual, expected=0):
    global COUNT
    difference = actual - expected
    if isinstance(difference, sp.MatrixBase):
        correct = all(sp.simplify(value) == 0 for value in difference)
    else:
        correct = sp.simplify(sp.expand_trig(difference)) == 0
    if not correct:
        raise AssertionError(f"{name}: actual {actual}; expected {expected}")
    COUNT += 1


def require(name, condition):
    global COUNT
    if not condition:
        raise AssertionError(name)
    COUNT += 1


x, y, z, t, w = sp.symbols("x y z t w", real=True)
a, b = sp.symbols("a b", positive=True)
r = sp.Rational
pi = sp.pi

# LA: substitute into the original equations and test orthogonality rather
# than only recomputing formulas by the same procedure used in the prose.
equal("dependent system first row", (5-2*t)+2*t, 5)
equal("dependent system second row", 2*(5-2*t)+4*t, 10)
A = sp.Matrix([[1, 0], [1, 1], [1, 2]])
measurements = sp.Matrix([1, 2, 2])
fit = sp.Matrix([r(7, 6), r(1, 2)])
residual = measurements-A*fit
equal("line fit residual", residual, sp.Matrix([-r(1, 6), r(1, 3), -r(1, 6)]))
equal("line fit orthogonality", A.T*residual, sp.zeros(2, 1))
equal("line fit squared residual", residual.dot(residual), r(1, 6))
matrix = sp.Matrix([[2, 1], [1, 2]])
for value, vector in [(3, sp.Matrix([1, 1])), (1, sp.Matrix([1, -1]))]:
    equal(f"eigenpair {value}", matrix*vector, value*vector)
equal("quadratic independent decomposition", 2*x*x+2*x*y+2*y*y,
      (x+y)**2+x*x+y*y)
proj = sp.Matrix([r(3, 5), r(6, 5)])
equal("projection orthogonality", sp.Matrix([1, 2]).dot(sp.Matrix([3, 0])-proj))
equal("wedge determinant", sp.Matrix([[1, 3], [2, 1]]).det(), -5)
require("SVD squares", sp.diag(3, -2, 0).T*sp.diag(3, -2, 0) == sp.diag(9, 4, 0))

# Calculus: derivative residuals, independent integration, extrema, and units
# represented in prose rather than a symbolic units package.
equal("cubic critical point negative", sp.diff(x**3-3*x, x).subs(x, -1))
equal("cubic critical point positive", sp.diff(x**3-3*x, x).subs(x, 1))
equal("log integral", sp.integrate(x*sp.log(1+x), (x, 0, 1)), r(1, 4))
equal("sphere rate", (4*pi*x*x*r(3, 100)).subs(x, 2), 12*pi/25)
equal("cardioid area", sp.integrate((1+sp.cos(t))**2/2, (t, 0, 2*pi)), 3*pi/2)
equal("log chain derivative", sp.diff(sp.log(1+x*x), x), 2*x/(1+x*x))
equal("substitution integral", sp.integrate(2*x*sp.exp(x*x), (x, 0, 1)), sp.E-1)
equal("Taylor polynomial", 1+r(1, 10)+r(1, 200), r(221, 200))
require("Taylor bound", float(sp.exp(r(1, 10))/6000) < 1/5000)
equal("spring work", sp.integrate(200*x, (x, 0, r(1, 10))), 1)
arc_antiderivative = (x*sp.sqrt(1+x*x)+sp.log(x+sp.sqrt(1+x*x)))/2
equal("arc length antiderivative", sp.diff(arc_antiderivative, x), sp.sqrt(1+x*x))
equal("parabola arc length", arc_antiderivative.subs(x, 1)-arc_antiderivative.subs(x, 0),
      (sp.sqrt(2)+sp.log(1+sp.sqrt(2)))/2)

# Multivariable/vector calculus.
line_f = (1+3*t/5)**2+2*(1+4*t/5)**2
equal("directional expansion", line_f, 3+r(22, 5)*t+r(41, 25)*t*t)
equal("directional derivative", sp.diff(line_f, t).subs(t, 0), r(22, 5))
equal("disk integral", sp.integrate(2*pi*x**3, (x, 0, 2)), 8*pi)
circle = sp.Matrix([sp.cos(t), sp.sin(t), 0])
field = sp.Matrix([-sp.sin(t), sp.cos(t), 0])
equal("direct circulation", sp.integrate(field.dot(circle.diff(t)), (t, 0, 2*pi)), 2*pi)
equal("implicit tangent derivative", (-(2*x+y)/(x+2*y)).subs({x: 1, y: 1}), -1)
equal("minimum completing squares", x*x+2*y*y-2*x+4*y,
      (x-1)**2+2*(y+1)**2-3)
equal("spherical unit volume",
      sp.integrate(x*x, (x, 0, 1))*sp.integrate(sp.sin(t), (t, 0, pi))*2*pi,
      4*pi/3)
equal("sphere radius two flux", 3*(4*pi*2**3/3), 32*pi)

# ODE examples and initial/boundary data.
response = 3-2*sp.exp(-2*t)
equal("linear ODE", sp.diff(response, t)+2*response, 6)
equal("linear ODE data", response.subs(t, 0), 1)
resonant = t*sp.sin(t)/2
equal("resonance differential equation", sp.diff(resonant, t, 2)+resonant, sp.cos(t))
equal("resonance position", resonant.subs(t, 0))
equal("resonance velocity", sp.diff(resonant, t).subs(t, 0))
system = sp.Matrix([(sp.exp(-t)+sp.exp(-3*t))/2,
                    (sp.exp(-t)-sp.exp(-3*t))/2])
equal("system residual", system.diff(t), sp.Matrix([[-2, 1], [1, -2]])*system)
equal("system data", system.subs(t, 0), sp.Matrix([1, 0]))
equal("blowup ODE", sp.diff(1/(1-t), t), (1/(1-t))**2)
equal("exact equation x derivative", sp.diff(x*x+x*y+y*y, x), 2*x+y)
equal("exact equation y derivative", sp.diff(x*x+x*y+y*y, y), x+2*y)
n = sp.symbols("n", integer=True, positive=True)
equal("boundary eigenfunction", -sp.diff(sp.sin(n*x), x, 2), n*n*sp.sin(n*x))
equal("boundary eigenfunction at pi", sp.sin(n*pi))
damped = sp.exp(-t)*sp.sin(2*t)/2
equal("dimensioned oscillator residual", sp.diff(damped, t, 2)+2*sp.diff(damped, t)+5*damped)
equal("dimensioned oscillator initial velocity", sp.diff(damped, t).subs(t, 0), 1)
logistic = 1/(1+(1/r(1, 5)-1)*sp.exp(-t))
equal("logistic exact field", sp.diff(logistic, t), logistic*(1-logistic))

# PDE: check derivatives directly, then independent data and conservation jump.
transport = sp.exp(-(x-2*t)**2)
equal("transport PDE", sp.diff(transport, t)+2*sp.diff(transport, x))
equal("transport initial profile", transport.subs(t, 0), sp.exp(-x*x))
heat = sp.exp(-t)*sp.sin(x)+sp.exp(-4*t)*sp.sin(2*x)/2
equal("heat PDE", sp.diff(heat, t), sp.diff(heat, x, 2))
equal("heat left boundary", heat.subs(x, 0))
equal("heat right boundary", heat.subs(x, pi))
equal("heat second coefficient at log2", (sp.exp(-4*t)/2).subs(t, sp.log(2)), r(1, 32))
wave = sp.cos(x)*sp.cos(t)
equal("wave PDE", sp.diff(wave, t, 2), sp.diff(wave, x, 2))
equal("wave initial velocity", sp.diff(wave, t).subs(t, 0))
poisson = x*(1-x)/2
equal("Poisson source", -sp.diff(poisson, x, 2), 1)
equal("Poisson maximum", poisson.subs(x, r(1, 2)), r(1, 8))
equal("shock conservation", 1*(2-0), (sp.Integer(2)**2-0**2)/2)
equal("rarefaction PDE inside fan", sp.diff(x/t, t)+(x/t)*sp.diff(x/t, x))

# Real analysis: exact integrals provide checks independent of convergence
# theorem assertions; no sample grid is used as a proof of uniform convergence.
equal("power integral", sp.integrate(x**n, (x, 0, 1)), 1/(n+1))
equal("spike integral", sp.integrate(n, (x, 0, 1/n)), 1)
equal("Tonelli separated integral",
      sp.integrate(sp.exp(-a*x), (x, 0, sp.oo)) *
      sp.integrate(sp.exp(-b*y), (y, 0, sp.oo)), 1/(a*b))

# Complex analysis: use an independent complex symbol (not the real x above).
q = sp.symbols("q")
for root in [sp.sqrt(3)+sp.I, -sp.sqrt(3)+sp.I, -2*sp.I]:
    equal("cube root", root**3, 8*sp.I)
equal("rational residue zero", sp.residue(1/(q*(q-1)), q, 0), -1)
equal("rational residue one", sp.residue(1/(q*(q-1)), q, 1), 1)
equal("real integral", sp.integrate(1/(x*x+1), (x, -sp.oo, sp.oo)), pi)
equal("Cauchy derivative residue", sp.residue(sp.exp(q)/q**2, q, 0), 1)
# SymPy's residue routine does not support this essential singularity.
# The coefficient of q^-1 is the coefficient of w in exp(w), w=1/q.
equal("essential residue from reciprocal-variable series",
      sp.series(sp.exp(q), q, 0, 3).removeO().coeff(q, 1), 1)
equal("square map CR first", sp.diff(x*x-y*y, x), sp.diff(2*x*y, y))
equal("square map CR second", sp.diff(x*x-y*y, y), -sp.diff(2*x*y, x))
equal("local Laurent leading terms",
      sp.series(1/(q*(q-1)), q, 0, 3).removeO(), -1/q-1-q-q*q)

# Harmonic analysis: coefficient quadrature, direct convolution, special
# values and differential identities.
for k in [1, 2, 3, 5]:
    equal(f"sawtooth sine coefficient {k}",
          sp.integrate(x*sp.sin(k*x), (x, -pi, pi))/pi,
          2*sp.Integer(-1)**(k+1)/k)
equal("causal convolution", sp.integrate(sp.exp(-(t-x)), (x, 0, t)), 1-sp.exp(-t))
equal("beta integral", sp.integrate(sp.sqrt(x*(1-x)), (x, 0, 1)), pi/8)
equal("Gamma five", sp.gamma(5), 24)
equal("Beta two three", sp.gamma(2)*sp.gamma(3)/sp.gamma(5), r(1, 12))
equal("Bessel first three terms", sp.series(sp.besselj(0, x), x, 0, 6).removeO(),
      1-x*x/4+x**4/64)
equal("Bessel equation", x*x*sp.diff(sp.besselj(0, x), x, 2) +
      x*sp.diff(sp.besselj(0, x), x)+x*x*sp.besselj(0, x))
equal("Legendre P2 norm",
      sp.integrate(((3*x*x-1)/2)**2, (x, -1, 1)), r(2, 5))
eps = sp.symbols("eps", positive=True)
layer = sp.exp(-t/eps)
equal("boundary layer residual", eps*sp.diff(layer, t)+layer)
equal("boundary layer initial data", layer.subs(t, 0), 1)
for index in range(20):
    equal(f"sampling alias at n={index}",
          sp.cos(2*pi*7*index/10), sp.cos(2*pi*3*index/10))

# File-presence checks ensure chapter image links have deliverable artifacts.
names = ["linear-projection", "taylor-exponential", "gradient-contours",
         "ode-evolution", "heat-modes", "pointwise-convergence",
         "complex-square-map", "fourier-sawtooth", "boundary-layer"]
for name in names:
    for suffix in ["png", "svg"]:
        path = ROOT / "assets" / "figures" / "analysis" / f"{name}.{suffix}"
        require(f"figure artifact {path.name}", path.exists() and path.stat().st_size > 1000)

chapters = [
    "linear-algebra/linear-algebra.md",
    "calculus/single-variable-calculus.md",
    "calculus/multivariable-and-vector-calculus.md",
    "differential-equations/ordinary-differential-equations.md",
    "differential-equations/partial-differential-equations.md",
    "analysis/real-analysis-and-measure.md",
    "complex-analysis/complex-analysis.md",
    "harmonic-analysis/transforms-and-special-functions.md",
]
for chapter in chapters:
    text = (ROOT / "subjects" / chapter).read_text(encoding="utf-8")
    sections = re.findall(r"(?m)^## ", text)
    require(f"16 template sections {chapter}", len(sections) == 16)
    print(f"{chapter}: {len(text.split())} whitespace words; {len(sections)} sections")

print(f"PASS: {COUNT} exact mathematical, sampling, figure, and structure checks.")
print("Limits: not a proof checker; does not certify every stated theorem, source, or modeling assumption.")
