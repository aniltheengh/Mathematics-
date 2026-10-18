"""Regenerate exact-equation teaching figures and check foundation examples.

Run from any directory: python scripts/plot_foundations.py
For the mathematical checks only: python scripts/plot_foundations.py --check-only
The checks verify encoded identities/examples, not all prose or deep theorems.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, lcm
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))
OUT = ROOT / "assets" / "figures" / "foundations"


def verify_mathematics() -> int:
    """Check exact arithmetic and identities independent of rendered pixels."""
    import sympy as sp

    passed: list[str] = []

    def check(name: str, condition: object) -> None:
        if not bool(condition):
            raise AssertionError(name)
        passed.append(name)

    x, n, t = sp.symbols("x n t", real=True)
    # Arithmetic and number representation.
    check("tank initial", Fraction(3, 8) * 240 == 90)
    check("percentage-point change", Fraction(100 * 30, 240) == Fraction(25, 2))
    check("relative percentage change", Fraction(100 * 30, 90) == Fraction(100, 3))
    check("gcd and lcm", (gcd(84, 126), lcm(84, 126)) == (42, 252))
    check("complex quotient", sp.simplify((3 + 2 * sp.I) / (1 - sp.I) - (1 + 5 * sp.I) / 2) == 0)
    check("fraction subtraction", Fraction(5, 6) - Fraction(7, 15) == Fraction(11, 30))
    check("inequality endpoints", [2 * a - 3 for a in (-1, 4)] == [-5, 5])
    check("radical simplification", sp.sqrt(72) == 6 * sp.sqrt(2))
    check("rationalization", sp.simplify(3 / sp.sqrt(6) - sp.sqrt(6) / 2) == 0)
    check("binary fraction", 8 + 2 + 1 + Fraction(1, 4) == Fraction(45, 4))
    # Algebra: domains still require the prose restrictions.
    check("rational factorization", sp.expand((x - 1) * (x + 1)) == x**2 - 1)
    check("radical candidates", sp.solve(x**2 - x - 2, x) == [-1, 2])
    check("radical original root", sp.sqrt(2 + 2) == 2)
    check("quadratic inequality factors", sp.expand((2 * x + 1) * (x - 3)) == 2 * x**2 - 5 * x - 3)
    check("log domain candidate", sp.log(2, 2) + sp.log(4, 2) == 3)
    check("simultaneous system", sp.solve([2*x + sp.Symbol('y') - 7, x - sp.Symbol('y') - 2]) == {x: 3, sp.Symbol('y'): 1})
    check("cubic factorization", sp.expand(x * (x - 2) * (x + 2)) == x**3 - 4*x)
    check("completed square", sp.expand(2 * (x - 2)**2 + 3) == 2*x**2 - 8*x + 11)
    check("arithmetic sum", sum(3*k - 1 for k in range(1, 21)) == 610)
    check("finite geometric sum", sum(2**k for k in range(6)) == 63)
    check("exponential equation", 9**3 == 27**2 == 729)
    check("binomial coefficient", sp.expand((2+x)**5).coeff(x, 3) == 40)
    # Trigonometry, including both exact labels used in plots.
    check("unit-circle point x", sp.cos(sp.pi/3) == sp.Rational(1, 2))
    check("unit-circle point y", sp.sin(sp.pi/3) == sp.sqrt(3)/2)
    check("cosine-law side", 5**2 + 8**2 - 2*5*8*sp.cos(sp.pi/3) == 49)
    check("triangle area", sp.Rational(1, 2)*5*8*sp.sin(sp.pi/3) == 10*sp.sqrt(3))
    check("sine equation branches", sp.sin(sp.pi/6) == sp.sin(5*sp.pi/6) == sp.Rational(1, 2))
    check("harmonic amplitude", 3**2 + 4**2 == 5**2)
    check("exact angle sine", sp.sin(3*sp.pi/4) == sp.sqrt(2)/2)
    check("exact angle cosine", sp.cos(3*sp.pi/4) == -sp.sqrt(2)/2)
    check("arc length", 6*sp.pi/3 == 2*sp.pi)
    check("sector area", sp.Rational(1, 2)*36*sp.pi/3 == 6*sp.pi)
    check("SSA sine", Fraction(8, 2*5) == Fraction(4, 5))
    check("angle difference", sp.simplify(sp.sin(sp.pi/12) - (sp.sqrt(6)-sp.sqrt(2))/4) == 0)
    # Sequences, series, and discrete examples.
    check("sequence exact error", sp.simplify((3*n+1)/(n+2) - 3 + 5/(n+2)) == 0)
    check("geometric exact sum", sp.summation(3 / sp.Integer(4)**sp.Symbol('k'), (sp.Symbol('k'), 1, sp.oo)) == 1)
    check("geometric tolerance", Fraction(1, 4**5) < Fraction(1, 1000))
    check("distinct code count", 9*9*8*7 == 4536)
    check("code count independent", 10*9*8*7 - 9*8*7 == 4536)
    check("hypergeometric probability", Fraction(comb(5, 2)*comb(3, 1), comb(8, 3)) == Fraction(15, 28))
    check("inclusion exclusion", 40 - (23 + 19 - 8) == 6)
    a = lambda k: (5 * 3**k - 1) // 2
    check("recurrence initial", a(0) == 2)
    check("recurrence values", all(a(k) == 3*a(k-1) + 1 for k in range(1, 15)))
    blocks = [tuple(map(int, s)) for s in ("123", "145", "167", "246", "257", "347", "356")]
    pairs = [tuple(sorted(pair)) for block in blocks for pair in combinations(block, 2)]
    check("Fano all pairs once", len(pairs) == len(set(pairs)) == comb(7, 2))
    check("Fano replication", all(sum(v in block for block in blocks) == 3 for v in range(1, 8)))
    # Number theory arithmetic.
    check("Bezout 252 198", gcd(252, 198) == 4*252 - 5*198 == 18)
    check("inverse 7 modulo 10", 7*3 % 10 == 1)
    check("Diophantine family", sp.expand(84*(-1+5*t)+30*(3-14*t)) == 6)
    check("CRT three residues", [23 % m for m in (3, 5, 7)] == [2, 3, 2])
    check("quadratic residue", 5**2 % 11 == 3)
    check("sqrt2 rational error", sp.simplify((sp.Rational(17, 12)-sp.sqrt(2)) - 1/(144*(sp.sqrt(2)+sp.Rational(17, 12)))) == 0)
    check("RSA encrypt", pow(7, 3, 55) == 13)
    check("RSA decrypt", pow(13, 27, 55) == 7)
    check("inverse 11 modulo 26", 11*19 % 26 == 1)
    check("divisor functions", (sp.totient(36), sp.divisor_count(36), sp.divisor_sigma(36)) == (12, 9, 91))
    check("noncoprime CRT", [9 % m for m in (4, 6)] == [1, 3])
    check("square residues modulo seven", {k*k % 7 for k in range(7)} == {0, 1, 2, 4})
    check("continued fraction", sp.continued_fraction(sp.Rational(43, 19)) == [2, 3, 1, 4])
    # Structural algebra: exact polynomial remainders and matrices.
    f = x*x + x + 1
    check("F4 irreducibility", [int(f.subs(x, k)) % 2 for k in (0, 1)] == [1, 1])
    check("F4 inverse", sp.rem(x*(x+1), f, domain=sp.GF(2)) == 1)
    check("F4 square", sp.rem((1+x)**2, f, domain=sp.GF(2)) == x)
    check("F4 cube", sp.rem(x**3, f, domain=sp.GF(2)) == 1)
    check("C2 representation", sp.diag(1, -1)**2 == sp.eye(2))
    check("cyclic additive order", [(8*k) % 12 for k in range(4)] == [0, 8, 4, 0])
    check("parabola kernel", sp.expand((sp.Symbol('y')-x*x).subs({sp.Symbol('y'):t*t, x:t})) == 0)
    print(f"Passed {len(passed)} exact checks for the eight foundation chapters.")
    return len(passed)


def make_figures() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 14,
                         "figure.facecolor": "#fbfcff", "axes.facecolor": "#fbfcff",
                         "svg.hashsalt": "mathematics-foundations"})
    OUT.mkdir(parents=True, exist_ok=True)

    def save(fig: object, name: str) -> None:
        fig.savefig(OUT / f"{name}.png", dpi=160)
        svg = OUT / f"{name}.svg"
        fig.savefig(svg, metadata={"Date": None})
        svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8", newline="\n")
        plt.close(fig)
        print(f"Generated assets/figures/foundations/{name}.png and .svg")

    fig, ax = plt.subplots(figsize=(7.2, 6.4), layout="constrained")
    angle = np.linspace(0, 2*np.pi, 721)
    ax.plot(np.cos(angle), np.sin(angle), color="#155e75", linewidth=2.3)
    point = (0.5, np.sqrt(3)/2)
    ax.plot([0, point[0]], [0, point[1]], color="#b63853", linewidth=2.1)
    ax.plot([point[0], point[0], 0], [0, point[1], point[1]], "--", color="#96713a", linewidth=1.2)
    arc = np.linspace(0, np.pi/3, 100)
    ax.plot(.25*np.cos(arc), .25*np.sin(arc), color="#b63853")
    ax.text(.29, .13, r"$\theta=\pi/3$", color="#b63853")
    ax.scatter(*point, s=58, color="#b63853", zorder=4)
    ax.annotate(r"$P=(1/2,\sqrt{3}/2)$", point, xytext=(13, 13), textcoords="offset points")
    ax.text(.23, -.14, r"$\cos\theta=1/2$", ha="center", fontsize=10)
    ax.text(-.10, 1.10, r"$\sin\theta=\sqrt{3}/2$", ha="right", fontsize=10)
    ax.axhline(0, color="#6b7280", linewidth=.8)
    ax.axvline(0, color="#6b7280", linewidth=.8)
    ax.set(title="Unit-circle definition of sine and cosine", xlabel="x (dimensionless)", ylabel="y (dimensionless)", xlim=(-1.3, 1.55), ylim=(-1.2, 1.25))
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=.22)
    save(fig, "unit-circle")

    fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
    time = np.linspace(0, 2*np.pi, 1400)
    displacement = 3*np.cos(2*time) + 4*np.sin(2*time)
    ax.plot(time, displacement, color="#155e75", linewidth=2.3,
            label=r"$x(t)=3\cos(2t)+4\sin(2t)$")
    for level in (-5, 5):
        ax.axhline(level, color="#b63853", linestyle="--", linewidth=1.1)
    ax.axhline(0, color="#6b7280", linewidth=.8)
    peak = np.arctan2(4, 3)/2
    ax.scatter([0, peak, peak+np.pi], [3, 5, 5], color="#b63853", zorder=4)
    ax.annotate("x(0) = 3 mm", (0, 3), xytext=(16, -25), textcoords="offset points")
    ax.annotate("", (peak, -5.65), (peak+np.pi, -5.65), arrowprops={"arrowstyle": "<->", "color": "#96713a"})
    ax.text(peak+np.pi/2, -6.25, r"One period $T=\pi\ \mathrm{s}$", ha="center")
    ax.text(5.9, 5.3, "+5 mm", color="#b63853", ha="right")
    ax.set(title="Same-frequency components combine to amplitude 5 mm",
           xlabel="Time t (s)", ylabel="Displacement x (mm)", xlim=(0, 2*np.pi), ylim=(-6.7, 6.15))
    ax.set_xticks(np.arange(5)*np.pi/2, ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.grid(alpha=.22)
    ax.legend(loc="lower right", bbox_to_anchor=(1, .18))
    save(fig, "harmonic-motion")

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.1), layout="constrained")
    grid = np.linspace(0, 1, 1201)
    for exponent in (1, 2, 5, 20, 100):
        axes[0].plot(grid, grid**exponent, label=f"n = {exponent}", linewidth=1.6)
    axes[0].plot([0, .995], [0, 0], color="#111827", linewidth=2.8)
    axes[0].scatter([1], [0], facecolors="white", edgecolors="#111827", s=45, zorder=5)
    axes[0].scatter([1], [1], color="#111827", s=40, zorder=5)
    axes[0].set(title=r"$f_n(x)=x^n$: pointwise, not uniform on $[0,1]$",
                xlabel="x (dimensionless)", ylabel="Function value (dimensionless)", xlim=(0, 1.025), ylim=(-.045, 1.06))
    axes[0].legend(loc="upper left")
    axes[0].grid(alpha=.22)
    grid = np.linspace(-.75, .75, 801)
    axes[1].plot(grid, 1/(1-grid), color="#111827", linewidth=2.6, label=r"$1/(1-x)$")
    for last in (0, 1, 3, 9):
        partial = sum(grid**k for k in range(last+1))
        axes[1].plot(grid, partial, linewidth=1.5, label=f"Partial sum, N = {last}")
    axes[1].set(title=r"Geometric sums: uniform on $[-3/4,3/4]$",
                xlabel="x (dimensionless)", ylabel="Function value (dimensionless)", xlim=(-.75, .75), ylim=(.3, 4.2))
    axes[1].legend(loc="upper left", fontsize=9)
    axes[1].grid(alpha=.22)
    save(fig, "convergence")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    verify_mathematics()
    if not args.check_only:
        make_figures()
