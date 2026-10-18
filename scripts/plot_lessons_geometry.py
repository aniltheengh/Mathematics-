"""Six reproducible illustrations for the guided conic sequence."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache/matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = ROOT / "assets/figures/lessons-geometry"
BLUE, RED, GOLD = "#155e75", "#b63853", "#b46517"
plt.rcParams.update({"font.size": 10, "svg.hashsalt": "guided-conics"})


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / (name + ".png"), dpi=160)
    svg = OUT / (name + ".svg")
    fig.savefig(svg, metadata={"Date": None})
    svg.write_text("\n".join(s.rstrip() for s in svg.read_text(encoding="utf-8").splitlines()) + "\n",
                   encoding="utf-8", newline="\n")
    plt.close(fig)
    print("Generated lessons-geometry/" + name + ".png and .svg")


def axes(ax, title, limits, labels=("x", "y")):
    ax.set(title=title, xlabel=labels[0], ylabel=labels[1],
           xlim=limits[:2], ylim=limits[2:])
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color=".75", lw=.7)
    ax.axvline(0, color=".75", lw=.7)
    ax.grid(alpha=.18)


def arrow(ax, start, end, color):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 1.6})


def main():
    t = np.linspace(0, 2*np.pi, 1201)
    fig, axs = plt.subplots(1, 3, figsize=(15, 5), layout="constrained")
    for ax, e, limits in zip(axs, [.5, 1., 1.5],
                            [(-4.2, 4.2, -3.5, 3.5), (-4.2, 7, -6, 6), (-18, 8, -9, 9)]):
        axes(ax, rf"$|P|=e\,|x+3|$, $e={e:g}$", limits)
        if e < 1:
            x, y = 1+2*np.cos(t), np.sqrt(3)*np.sin(t)
            ax.plot(x, y, color=BLUE, lw=2)
        elif e == 1:
            y = np.linspace(-6, 6, 1001)
            x = y*y/6-1.5
            ax.plot(x, y, color=BLUE, lw=2)
        else:
            u = np.linspace(-1.5, 1.5, 1001)
            for sign in [-1, 1]:
                x, y = -5.4+sign*3.6*np.cosh(u), 4.5/np.sqrt(1.25)*np.sinh(u)
                assert np.max(np.abs(x*x+y*y-e*e*(x+3)**2)) < 1e-11
                ax.plot(x, y, color=BLUE, lw=2)
        ax.axvline(-3, color=GOLD, ls="--", label="directrix x=-3")
        ax.scatter([0], [0], color=RED, zorder=4, label="focus (0,0)")
        ax.legend(fontsize=8, loc="upper right")
    save(fig, "eccentricity-family")

    fig = plt.figure(figsize=(12, 11), layout="constrained")
    theta = np.linspace(0, 2*np.pi, 45)
    radius = np.linspace(0, 5.5, 20)
    rr, tt = np.meshgrid(radius, theta)
    xx, yy = rr*np.cos(tt), rr*np.sin(tt)
    for i, (m, label) in enumerate([(0, "circle"), (.6, "ellipse"), (1, "parabola"), (1.5, "hyperbola")]):
        ax = fig.add_subplot(2, 2, i+1, projection="3d")
        for sign in [-1, 1]:
            ax.plot_wireframe(xx, yy, sign*rr, rstride=5, cstride=4,
                              color="#607d8b", alpha=.13, lw=.5)
        px, py = np.meshgrid(np.linspace(-3.2, 3.2, 6), np.linspace(-3.2, 3.2, 6))
        ax.plot_surface(px, py, m*px+1, color=GOLD, alpha=.13, shade=False)
        curves = []
        if m < 1:
            q = 1-m*m
            curves.append((m/q+np.cos(t)/q, np.sin(t)/np.sqrt(q)))
        elif m == 1:
            y = np.linspace(-2.6, 2.6, 801)
            curves.append(((y*y-1)/2, y))
        else:
            q = m*m-1
            u = np.linspace(-1.75, 1.75, 801)
            for sign in [-1, 1]:
                curves.append((-m/q+sign*np.cosh(u)/q, np.sinh(u)/np.sqrt(q)))
        for x, y in curves:
            z = m*x+1
            assert np.max(np.abs(z*z-x*x-y*y)) < 1e-12
            ax.plot(x, y, z, color=RED, lw=2.5)
        ax.set(title=rf"{label}: $z={m:g}x+1$", xlabel="x", ylabel="y", zlabel="z",
               xlim=(-5.5, 5.5), ylim=(-5.5, 5.5), zlim=(-5.5, 5.5))
        ax.set_box_aspect((1, 1, 1))
        ax.view_init(elev=25, azim=-115)
    fig.suptitle(r"Exact intersections with the double cone $z^2=x^2+y^2$", fontsize=15)
    save(fig, "cone-sections")

    fig, axs = plt.subplots(1, 3, figsize=(15, 6), layout="constrained")
    for ax, k, title in zip(axs, [2, 3*np.sqrt(2), 5],
                            [r"$k=2$: $\Delta>0$", r"$k=3\sqrt{2}$: $\Delta=0$", r"$k=5$: $\Delta<0$"]):
        axes(ax, title, (-6.5, 6.5, -4, 8))
        ax.plot(5*np.cos(t), 3*np.sin(t), color=BLUE, lw=2)
        x = np.linspace(-7, 7, 200)
        ax.plot(x, .6*x+k, color=RED, label=r"$y=3x/5+k$")
        roots = np.roots([1/25+.6**2/9, 2*.6*k/9, k*k/9-1])
        if k == 2:
            ax.scatter(roots, .6*roots+k, color=RED, zorder=4)
        elif k < 5:
            x0 = -.6*k*25/18
            ax.scatter([x0], [.6*x0+k], color=RED, zorder=4)
        ax.text(-5.9, -3.5, r"$x^2/25+y^2/9=1$", color=BLUE)
        ax.legend(loc="upper left", fontsize=9)
    save(fig, "tangency-discriminant")

    fig, axs = plt.subplots(1, 2, figsize=(13, 6), layout="constrained")
    ax = axs[0]
    axes(ax, "Ellipse: focus to focus", (-5.8, 5.8, -3.8, 4))
    ax.plot(5*np.cos(t), 3*np.sin(t), color=BLUE)
    p = np.array([3, 12/5])
    n = np.array([9, 20])/np.sqrt(481)
    tangent = np.array([20, -9])/np.sqrt(481)
    arrow(ax, (-4, 0), p, GOLD)
    arrow(ax, p, (4, 0), RED)
    ax.plot(*(np.array([p-1.1*n, p+1.1*n]).T), color="purple", ls="--", label="normal")
    ax.plot(*(np.array([p-1.5*tangent, p+1.5*tangent]).T), color=".3", label="tangent")
    ax.scatter([-4, 4, 3], [0, 0, 12/5], color=BLUE, zorder=5)
    for xy, label, offset in [((-4, 0), r"$F_-$", (-5, -22)), ((4, 0), r"$F_+$", (0, -22)),
                              ((3, 12/5), r"$P=(3,12/5)$", (-110, 40))]:
        ax.annotate(label, xy, xytext=offset, textcoords="offset points")
    ax.legend(loc="lower left", fontsize=9)
    ax = axs[1]
    axes(ax, r"Parabola $y^2=4x$: parallel ray to focus", (-1, 5.5, -3.5, 4))
    y = np.linspace(-3.3, 3.3, 501)
    ax.plot(y*y/4, y, color=BLUE)
    p = np.array([1., 2.])
    n = np.array([-1., 1.])/np.sqrt(2)
    tangent = np.array([1., 1.])/np.sqrt(2)
    arrow(ax, (5, 2), p, GOLD)
    arrow(ax, p, (1, 0), RED)
    ax.plot(*(np.array([p-n, p+n]).T), color="purple", ls="--")
    ax.plot(*(np.array([p-tangent, p+tangent]).T), color=".3")
    ax.scatter([1, 1], [2, 0], color=BLUE, zorder=5)
    ax.annotate("P=(1,2)", (1, 2), xytext=(-70, 12), textcoords="offset points")
    ax.annotate("F=(1,0)", (1, 0), xytext=(10, -20), textcoords="offset points")
    ax.text(2.7, 2.25, "incoming direction (-1,0)", fontsize=9, color=GOLD)
    save(fig, "reflection-vectors")

    fig, axs = plt.subplots(1, 2, figsize=(12, 6), layout="constrained")
    u, v = 2*np.cos(t), np.sin(t)
    x, y = 1+(u-v)/np.sqrt(2), -1+(u+v)/np.sqrt(2)
    assert np.max(np.abs(5*x*x-6*x*y+5*y*y-16*x+16*y+8)) < 1e-13
    axes(axs[0], r"$5x^2-6xy+5y^2-16x+16y+8=0$", (-2, 4, -4, 2))
    axs[0].plot(x, y, color=BLUE, lw=2)
    center = np.array([1., -1.])
    for direction, label in [(np.array([1., 1.])/np.sqrt(2), "u"), (np.array([-1., 1.])/np.sqrt(2), "v")]:
        endpoints = np.array([center-2.5*direction, center+2.5*direction])
        axs[0].plot(*endpoints.T, color=GOLD, ls="--")
        axs[0].text(*(center+2.6*direction), label, color=GOLD)
    axs[0].scatter([1], [-1], color=BLUE, label="center (1,-1)")
    f = np.sqrt(1.5)
    axs[0].scatter([1-f, 1+f], [-1-f, -1+f], color=RED, label="foci")
    axs[0].legend(loc="lower right", fontsize=9)
    axes(axs[1], r"Principal coordinates: $u^2/4+v^2=1$", (-3, 3, -3, 3), ("u", "v"))
    axs[1].plot(u, v, color=BLUE, lw=2)
    axs[1].scatter([-np.sqrt(3), np.sqrt(3)], [0, 0], color=RED, label=r"foci $(\pm\sqrt{3},0)$")
    axs[1].legend(loc="lower left", fontsize=9)
    save(fig, "principal-axes")

    fig, axs = plt.subplots(2, 2, figsize=(10, 9), layout="constrained")
    titles = [r"$y^2=4x$: parabola", r"$x^2=1$: two parallel lines",
              r"$x^2=0$: one repeated line", r"$x^2+1=0$: empty real set"]
    for ax, title in zip(axs.flat, titles):
        axes(ax, title, (-3, 3, -3, 3))
    y = np.linspace(-3, 3, 501)
    axs[0, 0].plot(y*y/4, y, color=BLUE, lw=2)
    for sign in [-1, 1]:
        axs[0, 1].axvline(sign, color=BLUE, lw=2)
    axs[1, 0].axvline(0, color=BLUE, lw=2)
    axs[1, 1].text(0, 0, "No real points", ha="center", va="center",
                   bbox={"facecolor": "white", "edgecolor": "none"}, color=RED)
    save(fig, "rank-one-loci")


if __name__ == "__main__":
    main()
