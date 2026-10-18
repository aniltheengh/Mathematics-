"""Exact checks of the guided lessons' examples; not proofs of general theorems."""

from math import comb
from pathlib import Path
import json
import sympy as sp


checks=[]
R=sp.Rational


def check(name,condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)


def zero(name,value):
    check(name,sp.simplify(value)==0)


p=sp.symbols("p",real=True)
x,y,t=sp.symbols("x y t",real=True)

# Bayes and inference: exact counts, derivatives, tails, posterior integrals.
posterior=lambda prior:R(9,10)*prior/(R(9,10)*prior+R(1,100)*(1-prior))
zero("alarm posterior low prevalence",posterior(R(1,100))-R(10,21))
zero("alarm posterior higher prevalence",posterior(R(1,10))-R(10,11))
zero("alarm equal posterior threshold",posterior(R(1,91))-R(1,2))
zero("Bernoulli variance exercise",R(2,5)-R(2,5)**2-R(6,25))
zero("independent average variance",4*9/16-R(9,4))
zero("common disturbance average variance",4+R(1,4)-R(17,4))
check("difference covariance cancellation",5+5-2*4==2)
like=p**6*(1-p)**2
zero("binomial MLE derivative",sp.diff(like,p).subs(p,R(3,4)))
check("binomial MLE log curvature",(sp.diff(6*sp.log(p)+2*sp.log(1-p),p,2).subs(p,R(3,4)))<0)
zero("likelihood ratio",like.subs(p,R(3,4))/like.subs(p,R(1,2))-R(729,256))
zero("binomial exact six",R(comb(8,6),2**8)-R(7,64))
zero("binomial upper tail",sum(R(comb(8,k),256) for k in range(6,9))-R(37,256))
zero("binomial symmetric tails",sum(R(comb(8,k),256) for k in [0,1,2,6,7,8])-R(37,128))
up10=1-sp.Integer(20)**(-R(1,10))
up20=1-sp.Integer(20)**(-R(1,20))
zero("zero-failure confidence equation",(1-up10)**10-R(1,20))
check("ten-trial interval rounded endpoint",.25886<float(up10)<.25888)
check("twenty-trial interval rounded endpoint",.13910<float(up20)<.13912)
density=252*p**6*(1-p)**2
zero("Beta73 posterior normalization",sp.integrate(density,(p,0,1))-1)
zero("Beta73 posterior mean",sp.integrate(p*density,(p,0,1))-R(7,10))
zero("Beta73 posterior threshold probability",sp.integrate(density,(p,R(1,2),1))-R(233,256))
zero("one-in-four MLE derivative",sp.diff(p*(1-p)**3,p).subs(p,R(1,4)))
zero("Beta22 threshold probability",sp.integrate(6*p*(1-p),(p,R(1,2),1))-R(1,2))

# Conditioning, roots, descent and KKT: use algebraic residuals and exact spectra.
eps=R(1,100)
delta=R(1,1000)
A=sp.Matrix([[1,1],[1,1+eps]])
b=sp.Matrix([2,2+eps+delta])
check("sensitive exact solve",A*sp.Matrix([R(9,10),R(11,10)])==b)
d=sp.symbols("d",positive=True)
zero("rationalized cancellation formula",(sp.sqrt(1+d)-1)-d/(sp.sqrt(1+d)+1))
check("Newton exact rational iterates",[(R(1)+2)/2,(R(3,2)+2/R(3,2))/2,(R(17,12)+2/R(17,12))/2]==[R(3,2),R(17,12),R(577,408)])
zero("Newton polynomial residual",R(577,408)**2-2-R(1,166464))
xx=sp.symbols("xx",positive=True)
zero("Newton exact quadratic error recurrence",(xx+2/xx)/2-sp.sqrt(2)-(xx-sp.sqrt(2))**2/(2*xx))
f=x**3-2*x+2
newton=lambda z:sp.simplify(z-f.subs(x,z)/sp.diff(f,x).subs(x,z))
check("Newton two-cycle",newton(0)==1 and newton(1)==0)
check("bisection midpoint exercise",R(1,2)**10<R(1,1000) and R(1,2)**9>R(1,1000))
zero("sqrt9 Newton step",(4+R(9,4))/2-R(25,8))
zero("sqrt9 polynomial residual",R(25,8)**2-9-R(49,64))
zero("Taylor step decrease exercise",4/(2*sp.Integer(6))-R(1,3))
check("quadratic balanced eigenfactors",[1-R(2,5)*v for v in [1,4]]==[R(3,5),-R(3,5)])
zero("quadratic objective contraction",R(3,5)**2-R(9,25))
check("unstable quadratic step",abs(1-R(3,5)*4)>1)
zero("second Hessian optimal step",2/(sp.Integer(2)+10)-R(1,6))
obj=(x-2)**2+2*(y-1)**2
lam=R(4,3)
point={x:R(4,3),y:R(2,3)}
zero("KKT gradient x",(sp.diff(obj,x)+lam).subs(point))
zero("KKT gradient y",(sp.diff(obj,y)+lam).subs(point))
zero("KKT active shared bound",(x+y-2).subs(point))
check("KKT positive coordinates and multiplier",all(v>0 for v in [point[x],point[y],lam]))
zero("KKT objective certificate",obj.subs(point)-R(2,3))
obj2=(x-3)**2+y*y
zero("KKT exercise objective",obj2.subs({x:2,y:-1})-2)
check("KKT exercise stationarity",[sp.diff(obj2,z).subs({x:2,y:-1})+2 for z in [x,y]]==[0,0])

# Norms and projections: integration and complex Gram algebra.
n=sp.symbols("n",integer=True,positive=True)
zero("power L1 norm",sp.integrate(x**n,(x,0,1))-1/(n+1))
zero("power L2 squared norm",sp.integrate(x**(2*n),(x,0,1))-1/(2*n+1))
zero("constant area spike",sp.integrate(n,(x,0,1/n))-1)
zero("spike squared L2 norm",sp.integrate(n*n,(x,0,1/n))-n)
zero("square-root spike L1 norm",sp.integrate(sp.sqrt(n),(x,0,1/n))-1/sp.sqrt(n))
zero("square-root spike L2 squared norm",sp.integrate(n,(x,0,1/n))-1)
G=sp.Matrix([[1,R(1,2)],[R(1,2),R(1,3)]])
zero("affine Gram determinant",G.det()-R(1,12))
coeff=G.inv()*sp.Matrix([R(1,3),R(1,4)])
check("affine projection coefficients",coeff==sp.Matrix([-R(1,6),1]))
r=x*x-x+R(1,6)
zero("affine residual orthogonal to one",sp.integrate(r,(x,0,1)))
zero("affine residual orthogonal to x",sp.integrate(x*r,(x,0,1)))
zero("affine squared L2 error",sp.integrate(r*r,(x,0,1))-R(1,180))
zero("constant squared L2 error",sp.integrate((x*x-R(1,3))**2,(x,0,1))-R(4,45))
zero("ramp squared L2 error",sp.integrate((1-n*t)**2,(t,0,1/n))-1/(3*n))
e=sp.Matrix([1,sp.I])/sp.sqrt(2)
v=sp.Matrix([1,0])
inner=lambda u,v:(sp.conjugate(u).T*v)[0]
proj=sp.simplify(inner(e,v)*e)
check("complex projection coordinates",proj==sp.Matrix([R(1,2),sp.I/2]))
zero("complex residual orthogonality",inner(e,v-proj))
zero("coordinate counterexample fixed functional",sp.conjugate(1/n)*n-1)

report={"status":"passed","checks":len(checks),"names":checks,
        "limits":"Exact checks cover encoded examples and exercises, not general theorem proofs or real-data independence."}
out=Path(__file__).resolve().parents[1]/"assets"/"figures"/"lessons-advanced"/"verification.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(report,indent=2))
