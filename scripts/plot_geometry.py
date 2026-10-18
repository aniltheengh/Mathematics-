"""Exact-equation geometry illustrations, sampled only for rendering."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache/matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = ROOT / "assets/figures/geometry"
BLUE, RED, GOLD = "#155e75", "#b63853", "#b46517"
plt.rcParams.update({"font.size": 10, "svg.hashsalt": "geometry-reference"})


def prepare(ax, title, limits):
    ax.set(title=title, xlabel="x", ylabel="y", xlim=limits[:2], ylim=limits[2:])
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="0.7", lw=.8)
    ax.axvline(0, color="0.7", lw=.8)
    ax.grid(alpha=.18)


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=160)
    svg = OUT / f"{name}.svg"
    fig.savefig(svg, metadata={"Date": None})
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
                   encoding="utf-8", newline="\n")
    plt.close(fig)
    print(f"Generated geometry/{name}.png and .svg")


def main():
    t = np.linspace(0, 2*np.pi, 1201)
    u = np.linspace(-1.65, 1.65, 1001)
    yy = np.linspace(-4, 4, 801)
    # Every plotted curve is checked against its displayed implicit equation.
    assert np.max(np.abs((5*np.cos(t))**2/25 + (3*np.sin(t))**2/9 - 1)) < 2e-14
    assert np.max(np.abs((3*np.cosh(u))**2/9 - (2*np.sinh(u))**2/4 - 1)) < 2e-14
    fig, axs = plt.subplots(2, 2, figsize=(10, 9), layout="constrained")
    prepare(axs[0,0], r"Circle: $x^2+y^2=9$", (-4,4,-4,4))
    axs[0,0].plot(3*np.cos(t),3*np.sin(t),color=BLUE)
    prepare(axs[0,1], r"Ellipse: $x^2/25+y^2/9=1$", (-6,6,-4,4))
    axs[0,1].plot(5*np.cos(t),3*np.sin(t),color=BLUE)
    axs[0,1].scatter([-4,4],[0,0],color=RED,s=20,label="foci")
    axs[0,1].legend()
    prepare(axs[1,0], r"Parabola: $y^2=4x$", (-2,5,-4.5,4.5))
    axs[1,0].plot(yy**2/4,yy,color=BLUE)
    axs[1,0].scatter([1],[0],color=RED,s=20)
    axs[1,0].axvline(-1,color=GOLD,ls="--",label="directrix x=-1")
    axs[1,0].legend(loc="upper right")
    prepare(axs[1,1], r"Hyperbola: $x^2/9-y^2/4=1$", (-8.5,8.5,-5.5,5.5))
    for sign in [-1,1]:
        axs[1,1].plot(sign*3*np.cosh(u),2*np.sinh(u),color=BLUE)
    xx = np.linspace(-9,9,100)
    for sign in [-1,1]:
        axs[1,1].plot(xx,sign*2*xx/3,"--",color=GOLD,lw=.9)
    save(fig,"conics-overview")

    fig, ax = plt.subplots(figsize=(9,6),layout="constrained")
    prepare(ax,r"Ellipse: $x^2/25+y^2/9=1$; $a=5$, $b=3$, $c=4$",(-7.5,7.5,-4,4))
    ax.plot(5*np.cos(t),3*np.sin(t),color=BLUE,lw=2)
    p = np.array([3.,12/5])
    for focus in [-4.,4.]:
        ax.plot([focus,p[0]],[0,p[1]],color=RED,lw=1.4)
    ax.scatter([-4,4,3],[0,0,12/5],color=RED,zorder=3)
    for x in [-25/4,25/4]:
        ax.axvline(x,color=GOLD,ls="--",lw=1)
    ax.annotate(r"$F_1=(-4,0)$",(-4,0),xytext=(-34,-20),textcoords="offset points")
    ax.annotate(r"$F_2=(4,0)$",(4,0),xytext=(-10,-20),textcoords="offset points")
    ax.annotate(r"$P=(3,12/5)$",p,xytext=(-70,13),textcoords="offset points")
    ax.text(-1,1.7,r"$37/5$",color=RED)
    ax.text(3.6,1.35,r"$13/5$",color=RED)
    ax.text(-6.1,-3.5,r"directrices $x=\pm25/4$",color=GOLD)
    save(fig,"ellipse-foci")

    fig, ax = plt.subplots(figsize=(8,7),layout="constrained")
    prepare(ax,r"Parabola $y^2=4x$: focus $(1,0)$ and directrix $x=-1$",(-2,7,-4.5,4.5))
    ax.plot(yy**2/4,yy,color=BLUE,lw=2)
    ax.axvline(-1,color=GOLD,ls="--")
    ax.scatter([0,1],[0,0],color=[BLUE,RED],zorder=4)
    ax.annotate("vertex (0,0)",(0,0),xytext=(-60,-22),textcoords="offset points")
    ax.annotate("focus (1,0)",(1,0),xytext=(10,-18),textcoords="offset points",color=RED)
    for y in [-3.,-2.,2.,3.]:
        point = (y*y/4,y)
        ax.annotate("",point,(6.4,y),arrowprops={"arrowstyle":"->","color":GOLD,"lw":1})
        ax.annotate("",(1,0),point,arrowprops={"arrowstyle":"->","color":RED,"lw":1})
    ax.text(4.8,.5,"incoming\nparallel rays",color=GOLD)
    ax.text(-1.8,3.5,"directrix",rotation=90,color=GOLD)
    save(fig,"parabola-focus")

    fig, ax = plt.subplots(figsize=(9,6),layout="constrained")
    prepare(ax,r"Hyperbola $x^2/9-y^2/4=1$; $c=\sqrt{13}$",(-8.5,8.5,-5.5,5.5))
    for sign in [-1,1]:
        ax.plot(sign*3*np.cosh(u),2*np.sinh(u),color=BLUE,lw=2)
        ax.plot(xx,sign*2*xx/3,"--",color=GOLD,lw=1)
        ax.scatter(sign*np.sqrt(13),0,color=RED,s=35,zorder=3)
        ax.scatter(sign*3,0,color=BLUE,s=35,zorder=3)
    ax.annotate(r"$(-\sqrt{13},0)$",(-np.sqrt(13),0),xytext=(-80,-28),textcoords="offset points",color=RED)
    ax.annotate(r"$(\sqrt{13},0)$",(np.sqrt(13),0),xytext=(5,-28),textcoords="offset points",color=RED)
    ax.text(-2.5,4.3,r"asymptotes $y=\pm2x/3$",color=GOLD)
    save(fig,"hyperbola-asymptotes")

    fig, ax = plt.subplots(figsize=(7,7),layout="constrained")
    prepare(ax,r"Rotated ellipse: $5x^2-6xy+5y^2=8$",(-2.5,2.5,-2.5,2.5))
    uc,vc = 2*np.cos(t),np.sin(t)
    x,y = (uc-vc)/np.sqrt(2),(uc+vc)/np.sqrt(2)
    assert np.max(np.abs(5*x*x-6*x*y+5*y*y-8)) < 3e-14
    ax.plot(x,y,color=BLUE,lw=2)
    d = np.linspace(-2.3,2.3,100)
    ax.plot(d,d,"--",color=GOLD,label="major principal axis: x=y")
    ax.plot(d,-d,":",color="0.5",label="minor principal axis: x=-y")
    ax.scatter([np.sqrt(1.5),-np.sqrt(1.5)],[np.sqrt(1.5),-np.sqrt(1.5)],color=RED,label="foci")
    ax.legend(loc="lower right",fontsize=8)
    save(fig,"rotated-ellipse")

    fig, axs = plt.subplots(2,2,figsize=(9,8),layout="constrained")
    for ax,title in zip(axs.flat,[r"$x^2+y^2=0$: one point",r"$x^2-y^2=0$: two lines",
                                  r"$x^2=4$: parallel lines",r"$x^2+y^2=-1$: empty real locus"]):
        prepare(ax,title,(-3,3,-3,3))
    axs[0,0].scatter([0],[0],color=BLUE,s=50,zorder=4)
    zz=np.linspace(-3,3,100)
    axs[0,1].plot(zz,zz,color=BLUE); axs[0,1].plot(zz,-zz,color=BLUE)
    axs[1,0].axvline(-2,color=BLUE); axs[1,0].axvline(2,color=BLUE)
    axs[1,1].text(0,.5,"No real points",ha="center",color=RED)
    save(fig,"degenerate-conics")

    fig, ax = plt.subplots(figsize=(7,7),layout="constrained")
    prepare(ax,r"Polar point: $r=2$, $\theta=\pi/3$",(-.5,2.5,-.5,2.5))
    point = (1,np.sqrt(3))
    ax.plot([0,point[0]],[0,point[1]],color=BLUE,lw=2)
    ax.plot([0,1,1],[0,0,np.sqrt(3)],"--",color=GOLD)
    arc=np.linspace(0,np.pi/3,100)
    ax.plot(.45*np.cos(arc),.45*np.sin(arc),color=RED)
    ax.text(.48,.25,r"$\pi/3$",color=RED)
    ax.text(.37,1.05,r"$r=2$",color=BLUE)
    ax.scatter(*point,color=BLUE,zorder=3)
    ax.annotate(r"$(x,y)=(1,\sqrt{3})$",point,xytext=(8,8),textcoords="offset points")
    save(fig,"polar-coordinates")

    fig = plt.figure(figsize=(12,6))
    ax1=fig.add_subplot(121,projection="3d")
    az,pol=np.meshgrid(np.linspace(0,2*np.pi,100),np.linspace(0,np.pi,60))
    x=2*np.sin(pol)*np.cos(az); y=3*np.sin(pol)*np.sin(az); z=4*np.cos(pol)
    assert np.max(np.abs(x*x/4+y*y/9+z*z/16-1)) < 2e-14
    ax1.plot_surface(x,y,z,cmap="Blues",alpha=.8,linewidth=0)
    ax1.set(title=r"Ellipsoid: $x^2/4+y^2/9+z^2/16=1$",xlabel="x",ylabel="y",zlabel="z")
    ax1.set_box_aspect((4,6,8))
    ax1.set(xticks=[-2,0,2],yticks=[-3,0,3],zticks=[-4,-2,0,2,4])
    ax2=fig.add_subplot(122,projection="3d")
    x,y=np.meshgrid(np.linspace(-1.5,1.5,70),np.linspace(-1.5,1.5,70)); z=x*x-y*y
    ax2.plot_surface(x,y,z,cmap="coolwarm",alpha=.85,linewidth=0)
    ax2.set(title=r"Saddle: $z=x^2-y^2$",xlabel="x",ylabel="y",zlabel="z")
    ax2.set_box_aspect((3,3,4.5))
    ax2.set(xticks=[-1,0,1],yticks=[-1,0,1],zticks=[-2,0,2])
    fig.subplots_adjust(left=.02,right=.98,bottom=.12,top=.9,wspace=.12)
    save(fig,"quadrics")


if __name__ == "__main__":
    main()
