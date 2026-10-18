"""Regenerate exact-function analysis figures in PNG and SVG.

Run from any working directory: python scripts/plot_analysis.py
No numerical differential-equation solution is used for these figures.
"""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = ROOT / "assets" / "figures" / "analysis"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.2,
    "figure.facecolor": "#fcfdff",
    "axes.facecolor": "#fcfdff",
    "svg.hashsalt": "mathematics-analysis-2026",
})
COLORS = ["#1261a0", "#d65324", "#22845c", "#8a4baf", "#a87310"]


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=170)
    svg = OUT / f"{name}.svg"
    fig.savefig(svg, metadata={"Date": None})
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
                   encoding="utf-8", newline="\n")
    plt.close(fig)
    print(f"Generated analysis/{name}.png and .svg")


def single(title, xlabel, ylabel, figsize=(8, 5.5)):
    fig, ax = plt.subplots(figsize=figsize, layout="constrained")
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    return fig, ax


def projection():
    fig, ax = single("Orthogonal projection onto a line",
                     "x (dimensionless)", "y (dimensionless)", (7, 6.5))
    ax.plot([-0.3, 2.7], [-0.3, 2.7], color="#8993a0", label="span(1, 1)")
    b = np.array([2., 1.])
    p = np.array([1.5, 1.5])
    for vector, color, label in [(b, COLORS[0], "b = (2, 1)"),
                                  (p, COLORS[2], "p = (3/2, 3/2)")]:
        ax.annotate("", xy=vector, xytext=(0, 0),
                    arrowprops={"arrowstyle": "-|>", "lw": 2.4, "color": color})
        ax.scatter(*vector, color=color, label=label, zorder=4)
    ax.annotate("", xy=b, xytext=p,
                arrowprops={"arrowstyle": "-|>", "lw": 2.4, "color": COLORS[1]})
    ax.plot([], [], color=COLORS[1], label="residual = (1/2, -1/2)")
    d = 0.15 / np.sqrt(2)
    ax.plot([p[0]-d, p[0], p[0]+d], [p[1]-d, p[1]-2*d, p[1]-d],
            color="#495261")
    ax.set(xlim=(-0.3, 2.7), ylim=(-0.3, 2.7))
    ax.set_aspect("equal")
    ax.legend(loc="upper left", fontsize=10)
    save(fig, "linear-projection")


def taylor():
    x = np.linspace(-1, 1, 600)
    fig, ax = single("Taylor approximation about x = 0",
                     "x (dimensionless)", "function value (dimensionless)")
    for y, label, color in [(np.exp(x), r"$e^x$", COLORS[0]),
                             (1+x, r"$1+x$", COLORS[1]),
                             (1+x+x*x/2, r"$1+x+x^2/2$", COLORS[2])]:
        ax.plot(x, y, lw=2, label=label, color=color)
    ax.scatter([0], [1], color="black", s=25, zorder=5)
    ax.legend()
    save(fig, "taylor-exponential")


def gradient():
    q = np.linspace(-2, 2, 301)
    x, y = np.meshgrid(q, q)
    fig, ax = single(r"Potential $f=x^2+2y^2$ and gradient $(2x,4y)$",
                     "x (dimensionless)", "y (dimensionless)", (7.5, 7))
    contours = ax.contour(x, y, x*x+2*y*y, levels=[0.5, 1, 2, 4, 6, 8],
                          colors=COLORS[0], linewidths=1.2)
    ax.clabel(contours, inline=True, fontsize=10)
    sample = np.linspace(-1.6, 1.6, 9)
    sx, sy = np.meshgrid(sample, sample)
    ax.quiver(sx, sy, 2*sx, 4*sy, color=COLORS[1], angles="xy",
              scale_units="xy", scale=12, width=0.004)
    ax.text(0.02, 0.02, "Arrow display: 1/12 of exact component length",
            transform=ax.transAxes, fontsize=9,
            bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "none"})
    ax.set_aspect("equal")
    save(fig, "gradient-contours")


def ode():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), layout="constrained")
    t = np.linspace(0, 7, 900)
    axes[0].plot(t, np.exp(-t)*np.sin(2*t)/2, color=COLORS[0], lw=2,
                 label=r"$x=e^{-t}\sin(2t)/2$")
    axes[0].plot(t, np.exp(-t)/2, color="#8993a0", ls="--", lw=1)
    axes[0].plot(t, -np.exp(-t)/2, color="#8993a0", ls="--", lw=1,
                 label=r"envelopes $\pm e^{-t}/2$")
    axes[0].set(title="Damped free displacement", xlabel="t (s)", ylabel="x (m)")
    axes[0].legend(fontsize=9)
    for initial, color in zip([0.2, 0.5, 2.0], COLORS):
        y = 1/(1+(1/initial-1)*np.exp(-t))
        axes[1].plot(t, y, lw=2, color=color, label=f"y(0) = {initial:g}")
    axes[1].axhline(1, color="#8993a0", lw=1, ls="--", label="equilibrium y = 1")
    axes[1].set(title=r"Logistic equation $y'=y(1-y)$",
                xlabel="t (dimensionless)", ylabel="y (dimensionless)")
    axes[1].legend(fontsize=9)
    save(fig, "ode-evolution")


def heat():
    x = np.linspace(0, np.pi, 601)
    fig, ax = single("Heat diffusion: higher modes decay faster",
                     "x (dimensionless)", "u (dimensionless)")
    for t, color in zip([0, 0.2, 1.0], COLORS):
        u = np.exp(-t)*np.sin(x)+0.5*np.exp(-4*t)*np.sin(2*x)
        ax.plot(x, u, lw=2, color=color, label=f"t = {t:g}")
    ax.set_xticks([0, np.pi/2, np.pi], ["0", r"$\pi/2$", r"$\pi$"])
    ax.set_ylim(-0.04, 1.55)
    ax.text(0.5, 0.97, r"$u=e^{-t}\sin x+\frac{1}{2}e^{-4t}\sin(2x)$",
            transform=ax.transAxes, ha="center", va="top")
    ax.legend(loc="center right")
    save(fig, "heat-modes")


def convergence():
    x = np.linspace(0, 1, 701)
    fig, ax = single(r"Pointwise convergence of $x^n$ on $[0,1]$",
                     "x (dimensionless)", "function value (dimensionless)")
    for n, color in zip([1, 2, 5, 20], COLORS):
        ax.plot(x, x**n, color=color, lw=1.8, label=f"n = {n}")
    ax.plot([0, 1], [0, 0], color="#22272f", lw=2, ls="--",
            label="limit: 0 for x < 1; 1 at x = 1")
    ax.scatter([1], [0], s=60, facecolors="#fcfdff", edgecolors="#22272f",
               zorder=8)
    ax.scatter([1], [1], s=35, color="#22272f", zorder=8)
    ax.set(xlim=(-0.02, 1.02), ylim=(-0.04, 1.07))
    ax.legend(fontsize=9)
    save(fig, "pointwise-convergence")


def complex_map():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.6), layout="constrained")
    xs = np.linspace(0.25, 1.5, 7)
    ys = np.linspace(-1, 1, 9)
    for x in xs:
        z = x+1j*np.linspace(-1, 1, 401)
        for ax, points in [(axes[0], z), (axes[1], z*z)]:
            ax.plot(points.real, points.imag, color=COLORS[0], lw=1.3)
    for y in ys:
        z = np.linspace(0.25, 1.5, 401)+1j*y
        for ax, points in [(axes[0], z), (axes[1], z*z)]:
            ax.plot(points.real, points.imag, color=COLORS[1], lw=1.3)
    axes[0].set(title="Cartesian grid in z plane", xlabel="Re z", ylabel="Im z")
    axes[1].set(title=r"Exact image under $w=z^2$", xlabel="Re w", ylabel="Im w")
    for ax in axes:
        ax.set_aspect("equal")
    save(fig, "complex-square-map")


def fourier():
    x = np.linspace(-np.pi, np.pi, 1601)
    fig, ax = single("Sawtooth Fourier sums and jump behavior",
                     "phase x (radians)", "function value (dimensionless)")
    # Target's open endpoints are distinct from the Fourier value at the jump.
    ax.plot(x[1:-1], x[1:-1], color="#22272f", lw=2, label="target x (interior)")
    ax.scatter([-np.pi, np.pi], [-np.pi, np.pi], s=45,
               facecolors="#fcfdff", edgecolors="#22272f", zorder=8)
    for nmax, color in zip([1, 5, 25], COLORS):
        n = np.arange(1, nmax+1)[:, None]
        s = (2*(-1.)**(n+1)*np.sin(n*x)/n).sum(axis=0)
        ax.plot(x, s, lw=1.4, color=color, label=f"N = {nmax}")
    ax.scatter([-np.pi, np.pi], [0, 0], color="#22272f", s=30, zorder=8,
               label="Fourier limit at jumps = 0")
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
                  [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    ax.legend(fontsize=9, loc="upper left")
    save(fig, "fourier-sawtooth")


def boundary_layer():
    t = np.linspace(0, 1, 1001)
    fig, ax = single(r"Initial layer: $\varepsilon y'+y=0$, $y(0)=1$",
                     "t (dimensionless)", "y (dimensionless)")
    for eps, color in zip([0.3, 0.1, 0.03], COLORS):
        ax.plot(t, np.exp(-t/eps), lw=2, color=color,
                label=rf"$\varepsilon={eps:g}$")
    ax.axhline(0, color="#22272f", ls="--", label="outer solution y = 0")
    ax.legend()
    save(fig, "boundary-layer")


if __name__ == "__main__":
    for plot in [projection, taylor, gradient, ode, heat, convergence,
                 complex_map, fourier, boundary_layer]:
        plot()
