"""Generate six original guided-lesson diagrams as PNG and SVG."""

from fractions import Fraction
from decimal import Decimal, localcontext
from math import comb
from pathlib import Path
import os

ROOT=Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT/".cache"/"matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


OUT=ROOT/"assets"/"figures"/"lessons-advanced"
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.size":11,"axes.grid":True,"grid.alpha":0.2,
                     "axes.spines.top":False,"axes.spines.right":False,"svg.fonttype":"none",
                     "svg.hashsalt":"guided-advanced"})
BLUE="#24628f"
ORANGE="#ad571e"
GREEN="#26714c"


def save(fig,name):
    fig.savefig(OUT/f"{name}.png",dpi=170,bbox_inches="tight")
    svg=OUT/f"{name}.svg"
    fig.savefig(svg,bbox_inches="tight",metadata={"Date":None})
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",
                   encoding="utf-8",newline="\n")
    plt.close(fig)
    print(f"Created {name}.png and {name}.svg")


fig,ax=plt.subplots(figsize=(8,4.9),constrained_layout=True)
p=np.linspace(0,.105,500)
posterior=lambda q:.9*q/(.9*q+.01*(1-q))
ax.plot(100*p,100*posterior(p),color=BLUE,linewidth=2.5)
ax.scatter([1,10],[100*10/21,100*10/11],color=ORANGE,s=65,zorder=3)
ax.annotate("Prevalence 1%; posterior 10/21",(1,100*10/21),xytext=(2.3,27),arrowprops={"arrowstyle":"->"})
ax.annotate("Prevalence 10%; posterior 10/11",(10,100*10/11),xytext=(4.4,71),arrowprops={"arrowstyle":"->"})
ax.set(xlabel="Defect prevalence (%)",ylabel="Probability of defect given alarm (%)",ylim=(0,100),
       title="Same test, different population: sensitivity 90%; false alarms 1%")
save(fig,"base-rates")


fig,axes=plt.subplots(1,2,figsize=(11.6,4.6),constrained_layout=True)
k=np.arange(9)
for prob,shift,color in [(.5,-.18,BLUE),(.75,.18,ORANGE)]:
    pmf=np.array([comb(8,int(j))*prob**j*(1-prob)**(8-j) for j in k])
    axes[0].bar(k+shift,pmf,width=.36,color=color,label=f"Fixed p = {prob}")
axes[0].set(xlabel="Random success count K",ylabel="P(K = k)",xticks=k,title="Sampling distributions: n = 8")
axes[0].legend()
pp=np.linspace(0,1,500)
like=lambda q:q**6*(1-q)**2
axes[1].plot(pp,like(pp)/like(.75),color=BLUE,linewidth=2.3)
axes[1].axvline(.75,color=ORANGE,linestyle="--",label="Maximum at p = 3/4")
axes[1].scatter([.5,.75],[like(.5)/like(.75),1],color=ORANGE,s=45)
axes[1].set(xlabel="Candidate parameter p",ylabel="Likelihood / maximum likelihood",title="Observed data fixed: K = 6, n = 8",ylim=(0,1.08))
axes[1].legend(loc="upper left",fontsize=9)
save(fig,"binomial-evidence")


fig,axes=plt.subplots(1,2,figsize=(11.6,4.7),constrained_layout=True)
delta=np.linspace(-.004,.004,300)
axes[0].plot(delta,1-delta/.01,color=BLUE,label="Exact x1")
axes[0].plot(delta,1+delta/.01,color=ORANGE,label="Exact x2")
axes[0].set(xlabel="Perturbation in second equation (dimensionless)",ylabel="Exact solution component",title="Data sensitivity: epsilon = 0.01")
axes[0].legend()
newton=[Fraction(1)]
for j in range(6):
    newton.append((newton[-1]+2/newton[-1])/2)
lo,hi=Fraction(1),Fraction(2)
bisect=[]
for j in range(7):
    mid=(lo+hi)/2
    bisect.append(mid)
    if mid*mid<2:
        lo=mid
    else:
        hi=mid
with localcontext() as ctx:
    ctx.prec=100
    root=Decimal(2).sqrt()
    err=lambda v:float(abs(Decimal(v.numerator)/Decimal(v.denominator)-root))
    en=np.array([err(v) for v in newton])
    eb=np.array([err(v) for v in bisect])
axes[1].semilogy(range(7),eb,"o-",color=BLUE,label="Bisection retained midpoint")
axes[1].semilogy(range(7),en,"o-",color=ORANGE,label="Newton from x0 = 1")
axes[1].set(xlabel="Iteration index k",ylabel="Absolute error from square root of two",title="Exact-arithmetic root errors; evaluated at 100 digits")
axes[1].legend(loc="lower left",fontsize=9)
save(fig,"conditioning-and-roots")


fig,axes=plt.subplots(1,2,figsize=(11.8,5.0),constrained_layout=True)
kk=np.arange(26)
for step,color in [(.25,BLUE),(.4,GREEN),(.49,ORANGE),(.6,"#8b367c")]:
    x1=2*(1-step)**kk
    x2=(1-4*step)**kk
    objective=(x1*x1+4*x2*x2)/2
    axes[0].semilogy(kk,objective,label=f"Step alpha = {step}",color=color,linewidth=2)
axes[0].set(xlabel="Iteration k",ylabel="Objective f(x_k)",title="Quadratic descent: eigenvalues 1 and 4")
axes[0].legend(fontsize=9)
gridx=np.linspace(-.2,2.6,350)
gridy=np.linspace(-.2,2.2,300)
X,Y=np.meshgrid(gridx,gridy)
cs=axes[1].contour(X,Y,(X-2)**2+2*(Y-1)**2,levels=[2/3,1,2,4,6],colors=BLUE)
axes[1].clabel(cs,inline=True,fontsize=9)
axes[1].add_patch(Polygon([[0,0],[2,0],[0,2]],facecolor="#dbeaf1",alpha=.65,edgecolor=ORANGE,linewidth=2))
axes[1].plot(4/3,2/3,"o",color="black",markersize=7)
axes[1].annotate("KKT optimum (4/3, 2/3)",(4/3,2/3),xytext=(.15,1.95),arrowprops={"arrowstyle":"->"},fontsize=10)
axes[1].plot(2,1,"x",color=ORANGE,markersize=8)
axes[1].text(1.54,1.15,"Unconstrained target",fontsize=9)
axes[1].set(xlabel="x",ylabel="y",title="Feasible triangle: x, y >= 0; x + y <= 2",xlim=(-.2,2.6),ylim=(-.2,2.2))
axes[1].set_aspect("equal",adjustable="box")
save(fig,"descent-and-constraints")


fig,axes=plt.subplots(1,2,figsize=(11.7,4.8),constrained_layout=True)
xx=np.linspace(0,1,600)
for n,color in [(1,"0.4"),(5,BLUE),(20,ORANGE),(100,GREEN)]:
    axes[0].plot(xx,xx**n,label=f"n = {n}",color=color,linewidth=2)
axes[0].set(xlabel="Position x",ylabel="f_n(x) = x^n",title="Pointwise limit is discontinuous at x = 1")
axes[0].legend(loc="upper left")
for n,color in [(4,BLUE),(8,ORANGE),(16,GREEN)]:
    axes[1].plot([0,1/n],[n,n],color=color,linewidth=2,label=f"n = {n}; area = 1")
    axes[1].vlines([0,1/n],0,n,color=color,linestyle=":",alpha=.5)
    axes[1].plot([0,1/n],[n,n],"o",markerfacecolor="white",markeredgecolor=color,markersize=5)
    axes[1].plot(1/n,0,"o",color=color,markersize=5)
axes[1].plot(0,0,"o",color="black",markersize=5,zorder=4)
axes[1].set(xlabel="Position x",ylabel="Spike height g_n(x)",title="Shrinking supports do not force integrals to vanish",xlim=(-.005,.3),ylim=(-.5,17.5))
axes[1].legend(loc="upper right",fontsize=9)
save(fig,"function-convergence")


fig,axes=plt.subplots(1,2,figsize=(11.7,4.7),constrained_layout=True)
xx=np.linspace(0,1,400)
axes[0].plot(xx,xx*xx,color="black",linewidth=2,label="Function x squared")
axes[0].plot(xx,xx-1/6,color=BLUE,linewidth=2,label="Projection x - 1/6")
axes[0].fill_between(xx,xx*xx,xx-1/6,color=ORANGE,alpha=.2,label="Residual gap")
axes[0].set(xlabel="x",ylabel="Function value",title="L2 best affine approximation; squared error 1/180")
axes[0].legend(loc="upper left",fontsize=9)
axes[1].axhline(0,color="0.4")
for n,color in [(2,BLUE),(6,ORANGE),(12,GREEN)]:
    axes[1].plot([n,n],[0,1],color=color,linewidth=2)
    axes[1].plot(n,1,"o",color=color,markersize=7,label=f"e_{n}; norm = 1")
axes[1].set(xlabel="Coordinate index j",ylabel="Component (e_n)_j",title="e_n tends weakly to zero; norm remains one",xlim=(.5,12.5),ylim=(-.05,1.5),xticks=range(1,13))
axes[1].legend(loc="upper center",fontsize=9,ncol=3)
save(fig,"projection-and-weak-convergence")
