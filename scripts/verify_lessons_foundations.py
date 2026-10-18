"""Exact checks for three guided lessons; not a general proof checker.

Run: python scripts/verify_lessons_foundations.py
Checks encoded equations, examples, figure equations, and delivery structure.
"""

from fractions import Fraction
from pathlib import Path
import re

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def equal(name, actual, expected=0):
    difference = actual - expected
    values = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
    require(name, all(sp.simplify(sp.expand_trig(v)) == 0 for v in values))


x, r, s, a, b = sp.symbols("x r s a b", real=True)
k = sp.symbols("k", integer=True)
n = sp.symbols("n", integer=True, positive=True)
u = sp.symbols("u", nonnegative=True)

# Proof lesson: finite witness statements and identities behind general proofs.
matrix = [[int(y == x0+1) for y in range(1, 5)] for x0 in range(4)]
require("every input has its witness", all(sum(row) == 1 for row in matrix))
require("no common witness", not any(all(matrix[i][j] for i in range(4)) for j in range(4)))
equal("sum of odd integers", (2*r+1)+(2*s+1), 2*(r+s+1))
equal("even integer square", (2*k)**2, 2*(2*k*k))
equal("odd integer square", (2*k+1)**2, 2*(2*k*k+2*k)+1)
equal("nonmultiple of three remainder one", (3*k+1)**2, 3*(3*k*k+2*k)+1)
equal("nonmultiple of three remainder two", (3*k+2)**2, 3*(3*k*k+4*k+1)+1)
equal("sum odd integers", sp.summation(2*k-1, (k, 1, n)), n*n)
equal("induction odd link", k*k+2*k+1, (k+1)**2)
equal("geometric layer count", n*n-(n-1)**2, 2*n-1)
for layer in range(1, 6):
    count = sum(max(i, j)+1 == layer for i in range(5) for j in range(5))
    require(f"square diagram layer {layer}", count == 2*layer-1)
require("prime polynomial counterexample", 41**2+41+41 == 41*43)
equal("sum integers induction link", k*(k+1)/2+k+1, (k+1)*(k+2)/2)
require("false divisibility converse", 2**2 % 4 == 0 and 2 % 4 != 0)
equal("rational addition identity", sp.Rational(2, 3)+sp.Rational(5, 7), sp.Rational(29, 21))

# Algebra lesson: original expressions, level sets, domains, and inverse branches.
equal("factor with hole", x*x-4, (x-2)*(x+2))
require("hole excludes reduced equation candidate", (sp.Integer(2)-2) == 0)
q = 2*x*x-8*x+5
equal("completed-square identity", q, 2*(x-2)**2-3)
equal("quadratic vertex value", q.subs(x, 2), -3)
for root in [2-sp.sqrt(6)/2, 2+sp.sqrt(6)/2]:
    equal("quadratic exact root", q.subs(x, root))
for endpoint in [0, 4]:
    equal("level-five endpoints", q.subs(x, endpoint), 5)
for value, expected in [(-3, 4), (0, sp.Rational(-1, 2)), (2, sp.Rational(1, 4))]:
    equal("rational inequality sign representative", ((x-1)/(x+2)).subs(x, value), expected)
equal("composition log-square-root", sp.log(sp.sqrt(u+1)), sp.log(u+1)/2)
equal("inverse square nonnegative branch", sp.sqrt(u*u), u)
equal("square after square-root", sp.sqrt(u)**2, u)
root = sp.sqrt(13)
equal("logarithmic candidate product", (root-2)*(root+2), 9)
require("logarithm positive inputs", root-2 > 0 and root+2 > 0)
equal("exercise completed square", 3*x*x+6*x-2, 3*(x+1)**2-5)
for root in [-1-sp.sqrt(15)/3, -1+sp.sqrt(15)/3]:
    equal("exercise quadratic root", 3*root*root+6*root-2)
equal("inverse shifted branch", 1+sp.sqrt(((1+u)-1)**2), 1+u)
equal("log exercise product", (sp.Integer(3)-1)*(sp.Integer(3)+1), 8)
equal("mechanical area completed square", x*(6-x), 9-(x-3)**2)
for endpoint in [2, 4]:
    equal("mechanical area constraint endpoints", (x*(6-x)).subs(x, endpoint), 8)

# Trigonometry/vector lesson: exact rotation, harmonic and mechanical checks.
alpha, beta = sp.pi/6, sp.pi/4
rotation = sp.Matrix([[sp.cos(alpha), -sp.sin(alpha)], [sp.sin(alpha), sp.cos(alpha)]])
direction = sp.Matrix([sp.cos(beta), sp.sin(beta)])
equal("rotation preserves inner product", rotation.T*rotation, sp.eye(2))
equal("rotation angle addition", rotation*direction,
      sp.Matrix([sp.cos(alpha+beta), sp.sin(alpha+beta)]))
c75 = (sp.sqrt(6)-sp.sqrt(2))/4
s75 = (sp.sqrt(6)+sp.sqrt(2))/4
equal("cosine seventy-five", sp.cos(5*sp.pi/12), c75)
equal("sine seventy-five", sp.sin(5*sp.pi/12), s75)
equal("unit direction squared length", c75*c75+s75*s75, 1)
equal("wheel radian conversion", 150*sp.pi/180, 5*sp.pi/6)
equal("wheel arc", sp.Rational(2, 5)*5*sp.pi/6, sp.pi/3)
delta = sp.atan(sp.Rational(3, 4))
equal("phase cosine coefficient", 5*sp.cos(delta), 4)
equal("phase sine coefficient", 5*sp.sin(delta), 3)
equal("initial velocity phase", 15*sp.sin(delta), 9)
force = sp.Matrix([6, 8])
guide = sp.Matrix([sp.Rational(4, 5), sp.Rational(3, 5)])
parallel = sp.Matrix([sp.Rational(192, 25), sp.Rational(144, 25)])
residual = sp.Matrix([sp.Rational(-42, 25), sp.Rational(56, 25)])
equal("unit guide", guide.dot(guide), 1)
equal("signed projection component", force.dot(guide), sp.Rational(48, 5))
equal("parallel vector formula", force.dot(guide)*guide, parallel)
equal("force reconstruction", parallel+residual, force)
equal("perpendicular residual", guide.dot(residual))
equal("perpendicular magnitude", residual.dot(residual), sp.Rational(14, 5)**2)
equal("Pythagorean force check", parallel.dot(parallel)+residual.dot(residual), force.dot(force))
equal("work in kilonewton metres", force.dot(guide/5), sp.Rational(48, 25))
equal("work in joules", 1000*sp.Rational(48, 25), 1920)
trial_error = force-x*guide
equal("projection uniquely minimizes squared error", trial_error.dot(trial_error),
      residual.dot(residual)+(sp.Rational(48, 5)-x)**2)
equal("trial load squared error increment", (10-sp.Rational(48, 5))**2, sp.Rational(4, 25))
equal("exercise arc", sp.Rational(3, 2)*2*sp.pi/3, sp.pi)
equal("exercise sector", sp.Rational(1, 2)*sp.Rational(9, 4)*2*sp.pi/3, 3*sp.pi/4)
equal("double angle", sp.sin(2*x), 2*sp.sin(x)*sp.cos(x))
equal("exercise cosine fifteen", sp.cos(sp.pi/12), (sp.sqrt(6)+sp.sqrt(2))/4)
exercise_projection = sp.Matrix([sp.Rational(7, 5), sp.Rational(14, 5)])
exercise_residual = sp.Matrix([sp.Rational(18, 5), sp.Rational(-9, 5)])
equal("exercise projection reconstruction", exercise_projection+exercise_residual, sp.Matrix([5, 1]))
equal("exercise projection residual", sp.Matrix([1, 2]).dot(exercise_residual))
equal("exercise work", sp.Matrix([3, 4]).dot(sp.Matrix([2, -1])), 2)
equal("phasor real-part convention", sp.re((2+5*sp.I)*(sp.cos(x)+sp.I*sp.sin(x))), 2*sp.cos(x)-5*sp.sin(x))

# Deliverable structure and figures; the word count is not a mathematical proof.
for name in ["proof-workshop", "algebra-and-functions", "trigonometry-and-vectors"]:
    path = ROOT / "lessons" / "foundations" / f"{name}.md"
    text = path.read_text(encoding="utf-8")
    words = len(text.split())
    require(f"substantial lesson {name}", words >= 1800)
    require(f"lesson stages {name}", len(re.findall(r"^## Stage ", text, re.M)) >= 4)
    practice = text.split("## Practice problems\n", 1)[1].split("## Answers and explanations", 1)[0]
    require(f"eight practice questions {name}", len(re.findall(r"^\d+\. \*\*", practice, re.M)) >= 8)
    print(f"{name}: {words} whitespace words; eight explained practice questions.")

for name in ["quantifier-witnesses", "induction-square-layers", "quadratic-levels",
             "inverse-branches", "angle-addition", "mechanical-projection"]:
    for suffix in ["png", "svg"]:
        path = ROOT / "assets" / "figures" / "lessons-foundations" / f"{name}.{suffix}"
        require(f"figure artifact {name}.{suffix}", path.exists() and path.stat().st_size > 1000)

print(f"PASS: {len(CHECKS)} exact mathematics, figure-artifact, and lesson-structure checks.")
print("Limits: not a formal proof checker; symbolic checks apply only to encoded expressions and assumptions.")
