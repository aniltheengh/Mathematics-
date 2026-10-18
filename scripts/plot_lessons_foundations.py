"""Generate six original guided-lesson figures as PNG and SVG.

Run from any working directory: python scripts/plot_lessons_foundations.py
Exact mathematical checks live in verify_lessons_foundations.py.
"""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

OUT = ROOT / "assets" / "figures" / "lessons-foundations"
plt.rcParams.update({"font.size": 11, "axes.titlesize": 14,
                     "figure.facecolor": "#fcfdff", "axes.facecolor": "#fcfdff",
                     "svg.hashsalt": "guided-foundations-2026"})
BLUE = "#155e75"
ORANGE = "#b25c22"
RED = "#ad3b56"
GREEN = "#26785a"


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=170)
    svg = OUT / f"{name}.svg"
    fig.savefig(svg, metadata={"Date": None})
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",
                   encoding="utf-8", newline="\n")
    plt.close(fig)
    print(f"Generated lessons-foundations/{name}.png and .svg")


def quantifier_witnesses():
    fig, ax = plt.subplots(figsize=(8.1, 6.4), layout="constrained")
    witness = np.eye(4, dtype=int)
    ax.imshow(witness, cmap=matplotlib.colors.ListedColormap(["#eaf0f4", BLUE]),
              vmin=0, vmax=1, interpolation="nearest")
    ax.set_xticks(range(4), ["y = 1", "y = 2", "y = 3", "y = 4"])
    ax.set_yticks(range(4), ["x = 0", "x = 1", "x = 2", "x = 3"])
    ax.set_xticks(np.arange(-.5, 4, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 4, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)
    for row in range(4):
        for col in range(4):
            ax.text(col, row, "witness" if row == col else "—",
                    color="white" if row == col else "#7c8791", ha="center", va="center")
    ax.set(title=r"Relation $y=x+1$ on $X=\{0,1,2,3\}$, $Y=\{1,2,3,4\}$",
           xlabel="Candidate witness y (dimensionless)", ylabel="Presented input x (dimensionless)")
    fig.supxlabel(r"Every row has a witness: $\forall x\,\exists y$ is true."
                  "\n" r"No column covers every row: $\exists y\,\forall x$ is false.", fontsize=11)
    save(fig, "quantifier-witnesses")


def induction_square_layers():
    fig, ax = plt.subplots(figsize=(8.4, 6.7), layout="constrained")
    colors = ["#285f75", "#507e91", "#93b3bf", "#d0e0e6", "#eda66b"]
    for row in range(5):
        for col in range(5):
            layer = max(row, col)
            ax.add_patch(Rectangle((col, row), 1, 1, facecolor=colors[layer],
                                   edgecolor="white", linewidth=1.6))
    for layer in range(5):
        ax.text(layer+.5, layer+.5, str(2*layer+1),
                ha="center", va="center", fontweight="bold",
                color="white" if layer < 2 else "#1f2937")
    ax.plot([0, 4, 4], [4, 4, 0], "--", color=BLUE, linewidth=2)
    ax.annotate("New outer L: 5 + 5 − 1 = 9 cells", (4.5, 2.5),
                xytext=(5.55, 3.0), ha="left", va="center",
                arrowprops={"arrowstyle": "->", "color": ORANGE}, fontsize=10)
    ax.text(5.55, 1.35, r"$5^2=4^2+9$" "\n\n" r"$1+3+5+7+9=25$", fontsize=12)
    ax.set(title="Induction: grow a square by one odd-sized layer",
           xlim=(-.15, 9.0), ylim=(-.15, 5.15), xlabel="Column (one cell per unit)", ylabel="Row (one cell per unit)")
    ax.set_xticks(range(6))
    ax.set_yticks(range(6))
    ax.set_aspect("equal")
    save(fig, "induction-square-layers")


def quadratic_levels():
    fig, ax = plt.subplots(figsize=(9.3, 5.7), layout="constrained")
    x = np.linspace(-.65, 4.65, 900)
    q = 2*(x-2)**2-3
    ax.plot(x, q, color=BLUE, linewidth=2.4, label=r"$q(x)=2(x-2)^2-3$")
    ax.axhline(5, color=ORANGE, linestyle="--", label="Level q = 5")
    ax.axhline(0, color="#87919a", linewidth=.9)
    ax.axvline(2, color="#87919a", linewidth=.9, linestyle=":")
    restricted = np.linspace(0, 4, 600)
    ax.fill_between(restricted, 2*(restricted-2)**2-3, 5, color="#cbe3eb", alpha=.7,
                    label=r"$q(x)\leq5$ occurs for $0\leq x\leq4$")
    ax.scatter([0, 4, 2], [5, 5, -3], color=RED, zorder=5)
    roots = [2-np.sqrt(6)/2, 2+np.sqrt(6)/2]
    ax.scatter(roots, [0, 0], color=GREEN, zorder=5)
    for root, text in zip(roots, [r"$2-\sqrt{6}/2$", r"$2+\sqrt{6}/2$"]):
        ax.annotate(text, (root, 0), xytext=(0, -25), textcoords="offset points", ha="center", color=GREEN,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9, "pad": 1.5})
    ax.annotate("Vertex (2, −3)", (2, -3), xytext=(25, 0), textcoords="offset points", va="center",
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9, "pad": 1.5})
    ax.set(title="Complete the square to read roots, a minimum, and a level set",
           xlabel="x (dimensionless)", ylabel="q(x) (dimensionless)", ylim=(-4.3, 11.7), xlim=(-.65, 4.65))
    ax.legend(loc="upper center", fontsize=10)
    ax.grid(alpha=.2)
    save(fig, "quadratic-levels")


def inverse_branches():
    fig, ax = plt.subplots(figsize=(7.7, 7), layout="constrained")
    source = np.linspace(0, 2.08, 500)
    target = np.linspace(0, 4.35, 500)
    ax.plot(source, source**2, color=BLUE, linewidth=2.4, label=r"$f(x)=x^2$, $x\geq0$")
    ax.plot(target, np.sqrt(target), color=ORANGE, linewidth=2.4,
            label=r"$f^{-1}(x)=\sqrt{x}$, $x\geq0$")
    ax.plot([0, 4.4], [0, 4.4], "--", color="#87919a", label="Reflection axis y = x")
    ax.plot([2, 4], [4, 2], ":", color=RED)
    ax.scatter([2, 4], [4, 2], color=RED, s=45, zorder=5)
    ax.annotate("(2, 4)", (2, 4), xytext=(10, 7), textcoords="offset points")
    ax.annotate("(4, 2)", (4, 2), xytext=(-15, -25), textcoords="offset points")
    ax.set(title="A restricted square branch has a single-valued inverse",
           xlabel="Input (dimensionless)", ylabel="Output (dimensionless)",
           xlim=(-.2, 4.5), ylim=(-.2, 4.5))
    ax.set_aspect("equal")
    ax.grid(alpha=.2)
    ax.legend(loc="upper left", fontsize=10)
    save(fig, "inverse-branches")


def angle_addition():
    fig, ax = plt.subplots(figsize=(8, 7), layout="constrained")
    t = np.linspace(0, 2*np.pi, 700)
    ax.plot(np.cos(t), np.sin(t), color="#98b9c4", linewidth=1.5)
    beta, alpha = np.pi/4, np.pi/6
    old = np.array([np.cos(beta), np.sin(beta)])
    new = np.array([np.cos(alpha+beta), np.sin(alpha+beta)])
    for point, color, label in [(old, BLUE, r"$u(\beta)$"), (new, RED, r"$u(\alpha+\beta)$")]:
        ax.annotate("", point, (0, 0), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.3})
        ax.scatter(*point, color=color, s=35, zorder=5, label=label)
    arc = np.linspace(beta, beta+alpha, 100)
    ax.plot(.55*np.cos(arc), .55*np.sin(arc), color=ORANGE, linewidth=2)
    ax.text(.52, .35, r"$\alpha=\pi/6$", color=ORANGE, ha="left")
    ax.annotate(r"$\beta=\pi/4$", old, xytext=(13, -16), textcoords="offset points", color=BLUE)
    ax.annotate(r"$\alpha+\beta=5\pi/12$", new, xytext=(-10, 18), textcoords="offset points", color=RED, ha="center")
    ax.text(-1.15, -.65, r"$R_\alpha u(\beta)=u(\alpha+\beta)$", fontsize=13,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9, "pad": 2})
    ax.text(-1.15, -.89, r"$u(5\pi/12)=\left(\frac{\sqrt{6}-\sqrt{2}}{4},\frac{\sqrt{6}+\sqrt{2}}{4}\right)$", fontsize=12,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9, "pad": 2})
    ax.axhline(0, color="#87919a", linewidth=.8)
    ax.axvline(0, color="#87919a", linewidth=.8)
    ax.set(title="Rotating a unit direction derives angle addition",
           xlabel="Horizontal component (dimensionless)", ylabel="Vertical component (dimensionless)",
           xlim=(-1.3, 1.35), ylim=(-1.15, 1.28))
    ax.set_aspect("equal")
    ax.grid(alpha=.18)
    save(fig, "angle-addition")


def mechanical_projection():
    fig, ax = plt.subplots(figsize=(8.5, 7.3), layout="constrained")
    force = np.array([6., 8.])
    parallel = np.array([192/25, 144/25])
    ax.plot([0, 10], [0, 7.5], "--", color="#8d98a2", linewidth=1.5,
            label="Guide direction u = (4/5, 3/5)")
    for point, color, label in [(force, BLUE, "F = (6, 8) kN"), (parallel, GREEN, r"$F_\parallel=(192/25,144/25)$ kN")]:
        ax.annotate("", point, (0, 0), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.7})
        ax.scatter(*point, color=color, s=45, zorder=5, label=label)
    ax.annotate("", force, parallel, arrowprops={"arrowstyle": "-|>", "color": ORANGE, "lw": 2.7})
    ax.plot([], [], color=ORANGE, linewidth=2.5, label=r"$F_\perp=(-42/25,56/25)$ kN")
    # A right-angle marker whose legs follow the exact orthogonal directions.
    u = np.array([4/5, 3/5])
    normal = np.array([-3/5, 4/5])
    marker = np.array([parallel-.35*u, parallel-.35*u+.35*normal, parallel+.35*normal])
    ax.plot(marker[:, 0], marker[:, 1], color="#4b5563", linewidth=1.2)
    ax.annotate("Total load", force, xytext=(-70, 12), textcoords="offset points", color=BLUE)
    ax.text(8.05, 5.25, r"$\|F_\parallel\|=48/5$ kN", color=GREEN)
    ax.text(4.25, 7.2, r"$\|F_\perp\|=14/5$ kN", color=ORANGE, ha="right")
    ax.set(title="Resolve a load along and perpendicular to a guide",
           xlabel="Horizontal force component (kN)", ylabel="Vertical force component (kN)",
           xlim=(-.6, 11.9), ylim=(-.5, 9.3))
    ax.set_aspect("equal")
    ax.grid(alpha=.2)
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "mechanical-projection")


if __name__ == "__main__":
    for make in [quantifier_witnesses, induction_square_layers, quadratic_levels,
                 inverse_branches, angle_addition, mechanical_projection]:
        make()
