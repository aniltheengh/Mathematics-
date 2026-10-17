"""Regenerate the chapter's three diagrams. Run from any working directory."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 14,
    "svg.hashsalt": "mathematics-encyclopedia",
    "figure.facecolor": "#fbfcff",
    "axes.facecolor": "#fbfcff",
})
OUT = ROOT / "assets" / "figures"


def axes(title, xlim, ylim):
    fig, ax = plt.subplots(figsize=(7.5, 7), layout="constrained")
    ax.set(title=title, xlabel="x (coordinate units)", ylabel="y (coordinate units)",
           xlim=xlim, ylim=ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="#9ca3af", linewidth=0.9)
    ax.axvline(0, color="#9ca3af", linewidth=0.9)
    ax.grid(alpha=0.22)
    return fig, ax


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=160)
    svg = OUT / f"{name}.svg"
    fig.savefig(svg, metadata={"Date": None})
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
                   encoding="utf-8", newline="\n")
    plt.close(fig)
    print(f"Generated assets/figures/{name}.png and .svg")


def main():
    fig, ax = axes("Distance and midpoint", (-1, 10), (-1, 12))
    ax.plot([1, 7], [2, 10], color="#155e75", linewidth=2.5)
    ax.plot([1, 7, 7], [2, 2, 10], "--", color="#c27021", linewidth=1.7)
    ax.scatter([1, 7, 4], [2, 10, 6], color=["#155e75", "#155e75", "#b63853"], s=65, zorder=4)
    for xy, label, offset in [((1, 2), "A (1, 2)", (-2, -22)),
                              ((7, 10), "B (7, 10)", (10, 4)),
                              ((4, 6), "M (4, 6)", (-88, 8))]:
        ax.annotate(label, xy, xytext=offset, textcoords="offset points")
    ax.text(4, 1.3, r"$\Delta x=6$", ha="center", color="#92500f")
    ax.text(7.3, 5.4, r"$\Delta y=8$", color="#92500f")
    ax.text(2.1, 8.7, r"$d=\sqrt{6^2+8^2}=10$", color="#155e75")
    ax.plot([6.6, 6.6, 7], [2, 2.4, 2.4], color="#c27021", linewidth=1)
    save(fig, "distance-midpoint")

    fig, ax = axes("A circle and a line", (-3, 7), (-6, 4))
    theta = np.linspace(0, 2 * np.pi, 721)
    ax.plot(2 + 3 * np.cos(theta), -1 + 3 * np.sin(theta), color="#155e75", linewidth=2.5,
            label=r"$(x-2)^2+(y+1)^2=9$")
    ax.axhline(-1, color="#c27021", linestyle="--", label=r"$y=-1$")
    ax.scatter([2, -1, 5], [-1, -1, -1], s=55, color="#b63853", zorder=4)
    for xy, label, offset in [((2, -1), "C (2, -1)", (-30, -24)),
                              ((-1, -1), "(-1, -1)", (-45, 12)),
                              ((5, -1), "(5, -1)", (5, 12))]:
        ax.annotate(label, xy, xytext=offset, textcoords="offset points")
    ax.text(3.5, -1.6, "r = 3", ha="center", color="#155e75")
    ax.legend(loc="lower center", framealpha=0.95)
    save(fig, "circle-intersections")

    fig, ax = axes("Perpendicular distance to a line", (-0.5, 6), (-2.5, 4))
    x = np.linspace(-0.5, 6, 200)
    ax.plot(x, (10 - 3 * x) / 4, color="#155e75", linewidth=2.5,
            label=r"$3x+4y-10=0$")
    h = np.array([82 / 25, 1 / 25])
    p = np.array([4.0, 1.0])
    ax.plot([h[0], p[0]], [h[1], p[1]], color="#b63853", linewidth=2.5)
    ax.scatter([h[0], p[0]], [h[1], p[1]], color="#b63853", s=60, zorder=4)
    ax.annotate("P (4, 1)", p, xytext=(12, 10), textcoords="offset points")
    ax.annotate("H (82/25, 1/25)", h, xytext=(-130, -30), textcoords="offset points")
    ax.text(4.15, 0.15, r"$d=6/5=1.2$", color="#b63853")
    # Small right-angle marker uses unit tangent (4,-3)/5 and normal (3,4)/5.
    tangent = np.array([4.0, -3.0]) / 5
    normal = np.array([3.0, 4.0]) / 5
    corner = np.array([h + 0.18 * tangent,
                       h + 0.18 * (tangent + normal), h + 0.18 * normal])
    ax.plot(corner[:, 0], corner[:, 1], color="#b63853", linewidth=1)
    ax.legend(loc="upper right")
    save(fig, "point-line-distance")


if __name__ == "__main__":
    main()
