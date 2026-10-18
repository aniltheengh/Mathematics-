"""Independent exact checks for advanced chapter examples, not theorem proofs."""

from itertools import product
from pathlib import Path
import json

import sympy as sp


checks = []


def check(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)


def zero(name, expression):
    check(name, sp.simplify(expression) == 0)


R = sp.Rational
x, y, t = sp.symbols("x y t", real=True)

# Probability: direct event arithmetic and exact moments, not simulated agreement.
alarm = R(95, 100)*R(2, 100) + R(4, 100)*R(98, 100)
zero("alarm probability", alarm-R(291, 5000))
zero("Bayes posterior", R(95, 100)*R(2, 100)/alarm-R(95, 291))
P = sp.Matrix([[R(9,10), R(1,10)], [R(2,5), R(3,5)]])
pi = sp.Matrix([[R(4,5), R(1,5)]])
check("Markov stationary law", pi*P == pi)
check("Markov row normalization", P*sp.ones(2,1) == sp.ones(2,1))
q = sp.symbols("q", positive=True)
zero("exponential waiting mean", sp.integrate(t*q*sp.exp(-q*t), (t, 0, sp.oo))-1/q)
zero("squared-uniform density normalization", sp.integrate(1/(2*sp.sqrt(x)), (x, 0, 1))-1)
zero("Bernoulli sample variance", R(1,4)*R(3,4)/100-R(3,1600))

# Statistics: normal equations, posterior integrals, likelihood derivatives.
data = [-2, -1, 0, 1, 2]
zero("sample variance", sum(sp.Integer(z)**2 for z in data)/4-R(5,2))
X = sp.Matrix([[1, 0], [1, 1], [1, 2]])
obs = sp.Matrix([1,2,2])
beta = (X.T*X).inv()*X.T*obs
check("calibration coefficients", beta == sp.Matrix([R(7,6), R(1,2)]))
res = obs-X*beta
check("calibration normal equations", X.T*res == sp.zeros(2,1))
zero("calibration squared residual", (res.T*res)[0]-R(1,6))
unnorm = x**2*(1-x)**8
zero("Beta posterior mean", sp.integrate(x*unnorm,(x,0,1))/sp.integrate(unnorm,(x,0,1))-R(1,4))
rate = sp.symbols("rate", positive=True)
zero("censored exponential MLE stationarity", (3/rate-1200).subs(rate,R(1,400)))
zero("AR1 stationary variance", 3/(1-R(1,2)**2)-4)

# Numerical analysis: independent exact substitutions and variational integrals.
zero("Newton iterate residual", R(577,408)**2-2-R(1,166464))
zero("trapezoid error", R(3,8)-sp.integrate(x*x,(x,0,1))-R(1,24))
zero("Simpson integral", (0+4*R(1,4)+1)/6-R(1,3))
A = sp.Matrix([[4,1],[1,3]])
check("linear system substitution", A*sp.Matrix([R(1,11),R(7,11)]) == sp.Matrix([1,2]))
check("symmetric system eigenvalues", set(A.eigenvals()) == {(7-sp.sqrt(5))/2,(7+sp.sqrt(5))/2})
stiffness = sp.integrate(4,(x,0,1))
load = sp.integrate(2*x,(x,0,R(1,2)))+sp.integrate(2*(1-x),(x,R(1,2),1))
zero("one-hat finite element coefficient", load/stiffness-R(1,8))
check("Euler unstable example", abs(1-10*R(1,4))>1)

# Optimization: KKT residual, exhaustive finite enumeration, control ranks.
gx = sp.Matrix([2*x-2,2*y-2])
check("quadratic KKT stationarity", gx.subs({x:1,y:1}) == sp.zeros(2,1))
check("integer allocation optimum", min((4*a+7*b,a,b) for a,b in product(range(8),range(6)) if 3*a+5*b>=10) == (14,0,2))
A = sp.Matrix([[0,1],[0,0]])
B = sp.Matrix([0,1])
C = sp.Matrix([[1,0]])
check("double integrator controllability", B.row_join(A*B).rank()==2)
check("double integrator observability", C.col_join(C*A).rank()==2)
check("feedback spectrum", set((A-B*sp.Matrix([[2,3]])).eigenvals())=={-1,-2})

# Topology: formulas and finite chain ranks, not assertions about arbitrary spaces.
yp = sp.symbols("yp", nonnegative=True)
yn = sp.symbols("yn", nonpositive=True)
xp = yp/(1+yp)
xn = yn/(1-yn)
zero("interval inverse positive branch", xp/(1-xp)-yp)
zero("interval inverse negative branch", xn/(1+xn)-yn)
a,b = sp.symbols("a b", real=True)
norm2=a*a+b*b
zero("radial retraction norm", (a/sp.sqrt(norm2))**2+(b/sp.sqrt(norm2))**2-1)
boundary1 = sp.Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
boundary2 = sp.Matrix([1,1,1])
check("triangle boundary squared zero", boundary1*boundary2==sp.zeros(3,1))
check("unfilled triangle H1 rank", 3-boundary1.rank()==1)
check("filled triangle H1 rank", 3-boundary1.rank()-boundary2.rank()==0)

# Geometry: differentiate the space curve and compute the metric from its map.
curve = sp.Matrix([2*sp.cos(t),2*sp.sin(t),t])
d1, d2, d3 = curve.diff(t), curve.diff(t,2), curve.diff(t,3)
cross = d1.cross(d2)
zero("helix curvature", sp.sqrt(cross.dot(cross))/sp.sqrt(d1.dot(d1))**3-R(2,5))
zero("helix torsion", sp.det(sp.Matrix.hstack(d1,d2,d3))/cross.dot(cross)-R(1,5))
r = sp.symbols("r", positive=True)
theta = sp.symbols("theta", real=True)
cart = sp.Matrix([r*sp.cos(theta),r*sp.sin(theta)])
J=cart.jacobian([r,theta])
g=sp.simplify(J.T*J)
check("polar metric", g==sp.diag(1,r*r))
ginv=g.inv()
coords=[r,theta]
gamma = [[[sp.simplify(sum(ginv[k,l]*(sp.diff(g[j,l],coords[i])+sp.diff(g[i,l],coords[j])-sp.diff(g[i,j],coords[l]))/2 for l in range(2))) for j in range(2)] for i in range(2)] for k in range(2)]
zero("polar radial Christoffel", gamma[0][1][1]+r)
zero("polar angular Christoffel", gamma[1][0][1]-1/r)
zero("polar displacement squared length", R(1,5)**2+9*R(1,10)**2-R(13,100))
zero("disk boundary form integral", sp.integrate(R(1,2),(t,0,2*sp.pi))-sp.pi)

# Functional analysis: exact projection and weak energy algebra.
projection=x-R(1,6)
residual=x*x-projection
zero("projection orthogonality constant", sp.integrate(residual,(x,0,1)))
zero("projection orthogonality linear", sp.integrate(x*residual,(x,0,1)))
zero("projection squared error", sp.integrate(residual**2,(x,0,1))-R(1,180))
zero("best constant squared error", sp.integrate((x-R(1,2))**2,(x,0,1))-R(1,12))
u=x*(1-x)
zero("weak solution differential check", -sp.diff(u,x,2)-2)
w=x*(1-x)*(2*x-1)
energy=lambda v:sp.integrate(sp.diff(v,x)**2/2-2*v,(x,0,1))
zero("weak energy identity for test variation", energy(u+w)-energy(u)-sp.integrate(sp.diff(w,x)**2/2,(x,0,1)))

# Modeling: units are documented in prose; equations and exact examples checked here.
ct=2*(1-sp.exp(-R(3,10)*t))
zero("tank solution differential equation", 10*sp.diff(ct,t)-(6-3*ct))
zero("tank initial condition", ct.subs(t,0))
check("tank steady solute balance", 2*3 == 2*2+R(1,10)*10*2)
z=sp.symbols("z")
poly=2*z*z+4*z+50
zero("oscillator root", poly.subs(z,-1+2*sp.sqrt(6)*sp.I))
p=sp.symbols("p")
zero("repetition code polynomial", 3*p*p*(1-p)+p**3-(3*p*p-2*p**3))
zero("repetition code numerical error", (3*p*p-2*p**3).subs(p,R(1,100))-R(149,500000))

report = {"status":"passed", "checks":len(checks), "names":checks,
          "limits":"Exact checks verify encoded examples, not global theorems or physical validation."}
print(json.dumps(report, indent=2))
target=Path(__file__).resolve().parents[1]/"assets"/"figures"/"advanced"/"verification.json"
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8",newline="\n")
