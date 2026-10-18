"""Reproduce original reference figures for advanced chapters (PNG and SVG)."""

from pathlib import Path
from math import factorial

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "figures" / "advanced"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.22,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none"})


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=170, bbox_inches="tight")
    svg = OUT / f"{name}.svg"
    fig.savefig(svg, bbox_inches="tight", metadata={"Date": None})
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
                   encoding="utf-8", newline="\n")
    plt.close(fig)
    print(f"Created {name}.png and {name}.svg")


fig, axes = plt.subplots(1, 2, figsize=(11, 4.1), constrained_layout=True)
k = np.arange(10)
mass = np.array([np.exp(-2) * 2.0**int(j) / factorial(int(j)) for j in k])
axes[0].bar(k, mass, color="#24628f")
axes[0].set(xlabel="Fault count n (dimensionless)", ylabel="P(N = n)",
            title="Poisson count: expected count = 2", xticks=k)
t = np.linspace(0, 20, 400)
axes[1].plot(t, np.exp(-0.2*t), color="#af5b20", linewidth=2.5)
axes[1].axvline(5, color="0.4", linestyle="--", label="Mean waiting time = 5 h")
axes[1].set(xlabel="Waiting time t (h)", ylabel="P(T > t)",
            title="Exponential survival: rate = 0.2 / h", ylim=(0, 1.03))
axes[1].legend()
save(fig, "probability")


fig, ax = plt.subplots(figsize=(7.4, 4.4), constrained_layout=True)
x = np.array([0., 1., 2.])
y = np.array([1., 2., 2.])
xx = np.linspace(-0.15, 2.2, 200)
ax.plot(xx, 7/6 + xx/2, color="#24628f", label="Least squares: y = 7/6 + x/2")
ax.scatter(x, y, color="#af5b20", s=60, zorder=3, label="Observed data")
for xi, yi in zip(x, y):
    ax.plot([xi, xi], [yi, 7/6+xi/2], color="#af5b20", linestyle="--")
ax.set(xlabel="Input x (dimensionless)", ylabel="Response y (dimensionless)",
       title="An affine calibration and its residuals")
ax.legend(loc="upper left")
save(fig, "regression")


fig, ax = plt.subplots(figsize=(7.4, 4.5), constrained_layout=True)
t = np.linspace(0, 4, 500)
ax.plot(t, np.exp(-2*t), color="black", linewidth=2, label="Exact: exp(-2t)")
for step, color in [(0.2, "#24628f"), (0.8, "#af5b20")]:
    tn = np.arange(round(4/step)+1)*step
    yn = (1-2*step)**np.arange(tn.size)
    ax.plot(tn, yn, "o-", color=color, markersize=4, label=f"Euler step h = {step}")
ax.set(xlabel="Time t (s)", ylabel="Normalized state y (dimensionless)",
       title="Stable time steps can still give poor physical behavior")
ax.legend()
save(fig, "numerical-decay")


fig, ax = plt.subplots(figsize=(6.5, 5.3), constrained_layout=True)
g = np.linspace(-0.5, 3, 350)
X, Y = np.meshgrid(g, g)
ax.contourf(X, Y, (X+Y >= 2).astype(float), levels=[0.5, 1.5], colors=["#e4eff4"])
cs = ax.contour(X, Y, X**2+Y**2, levels=[0.5, 1, 2, 4, 6, 9], colors="#24628f")
ax.clabel(cs, inline=True, fontsize=9)
ax.plot(g, 2-g, color="#af5b20", linewidth=2, label="Constraint boundary: x + y = 2")
ax.plot(1, 1, "o", color="black", markersize=7)
ax.annotate("Minimum (1, 1); objective = 2", (1, 1), xytext=(0.0, 2.6),
            arrowprops={"arrowstyle": "->"})
ax.text(1.8, 2.5, "Feasible region", color="#24628f")
ax.set(xlabel="x (dimensionless)", ylabel="y (dimensionless)",
       title="Quadratic contours with an active constraint", xlim=(-0.5, 3), ylim=(-0.5, 3))
ax.set_aspect("equal", adjustable="box")
ax.legend(loc="lower left", fontsize=9)
save(fig, "optimization")


fig, axes = plt.subplots(1, 2, figsize=(10, 4.1), constrained_layout=True)
tt = np.linspace(0, 2*np.pi, 400)
axes[0].plot(np.cos(tt), np.sin(tt), color="#24628f", linewidth=2)
axes[0].plot(1, 0, "o", color="#af5b20", markersize=8)
axes[0].annotate("p(0) = p(1) = p(2)", (1, 0), xytext=(-0.9, 1.25),
                 arrowprops={"arrowstyle": "->"})
axes[0].set(xlabel="cos(2 pi t)", ylabel="sin(2 pi t)", title="Circle S1",
            xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
axes[0].set_aspect("equal")
axes[1].axhline(0, color="#24628f", linewidth=2)
axes[1].scatter([0, 1, 2], [0, 0, 0], color="#af5b20", s=60, zorder=3)
for j in [0, 1, 2]:
    axes[1].text(j, 0.08, str(j), ha="center")
axes[1].set(xlabel="Covering parameter t (dimensionless)", yticks=[],
            title="Distinct lifts on the real line", xlim=(-0.4, 2.4), ylim=(-0.6, 0.6))
axes[1].text(1, -0.3, "Integer shifts have the same image", ha="center")
save(fig, "topology-cover")


fig = plt.figure(figsize=(6.7, 6.0), layout="constrained")
ax = fig.add_subplot(projection="3d")
t = np.linspace(0, 2*np.pi, 400)
ax.plot(2*np.cos(t), 2*np.sin(t), t, color="#24628f", linewidth=2.6)
ax.plot([0, 2], [0, 0], [0, 0], "--", color="#af5b20", label="Radius = 2 m")
ax.set(xlabel="x (m)", ylabel="y (m)", zlabel="z (m)", title="Helix: (2 cos t, 2 sin t, t)",
       xlim=(-2.5, 2.5), ylim=(-2.5, 2.5), zlim=(0, 2*np.pi))
ax.set_box_aspect((5, 5, 2*np.pi))
ax.legend(loc="upper left")
save(fig, "helix")


fig, ax = plt.subplots(figsize=(7.4, 4.4), constrained_layout=True)
x = np.linspace(0, 1, 400)
f = x*x
p = x-1/6
ax.plot(x, f, color="black", linewidth=2, label="Function: x squared")
ax.plot(x, p, color="#24628f", linewidth=2, label="L2 affine projection: x - 1/6")
ax.fill_between(x, f, p, alpha=0.2, color="#af5b20", label="Signed residual gap")
ax.set(xlabel="x (dimensionless)", ylabel="Function value (dimensionless)",
       title="Projection minimizes integrated squared error")
ax.legend(loc="upper left")
save(fig, "function-projection")


fig, ax = plt.subplots(figsize=(7.4, 4.5), constrained_layout=True)
tau = np.linspace(0, 5, 400)
for da, color in [(0, "black"), (0.5, "#24628f"), (2, "#af5b20")]:
    c = (1-np.exp(-(1+da)*tau))/(1+da)
    ax.plot(tau, c, color=color, linewidth=2.3, label=f"Da = {da}; equilibrium = {1/(1+da):.3g}")
ax.set(xlabel="Dimensionless time tau = Qt / V", ylabel="Dimensionless concentration C = c / c_in",
       title="Mixed-tank response from clean initial liquid", ylim=(0, 1.05))
ax.legend(loc="lower right")
save(fig, "tank-model")
