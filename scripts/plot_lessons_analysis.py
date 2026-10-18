"""Generate six reproducible guided-lesson diagrams from exact functions."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = ROOT / "assets" / "figures" / "lessons-analysis"
OUT.mkdir(parents=True, exist_ok=True)
C = ["#1464a0", "#d95728", "#24835e", "#884bb0"]
plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 14,
    "figure.facecolor": "#fcfdff",
    "axes.facecolor": "#fcfdff",
    "axes.grid": True,
    "grid.alpha": 0.2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "svg.hashsalt": "guided-analysis-2026",
})


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=175)
    svg = OUT / f"{name}.svg"
    fig.savefig(svg, metadata={"Date": None})
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())+"\n",
                   encoding="utf-8", newline="\n")
    plt.close(fig)
    print(f"Generated lessons-analysis/{name}.png and .svg")


def calculus():
    fig, ax = plt.subplots(figsize=(8, 7), layout="constrained")
    x = np.linspace(0, 2.1, 501)
    ax.plot(x, x*x, color=C[0], lw=2.5, label=r"$f(x)=x^2$")
    ax.plot(x, 1+2*(x-1), color="#232832", lw=2, ls="--",
            label="tangent: slope 2")
    for h, color in zip([1, 0.5, -0.5], C[1:]):
        ax.plot(x, 1+(2+h)*(x-1), lw=1.6, color=color,
                label=f"secant: h = {h:g}, slope = {2+h:g}")
        ax.scatter([1+h], [(1+h)**2], s=35, color=color, zorder=5)
    ax.scatter([1], [1], color="black", s=35, zorder=6)
    ax.set(title="Average slopes approaching a derivative",
           xlabel="x (dimensionless)", ylabel="y (dimensionless)",
           xlim=(0, 2.1), ylim=(-0.2, 4.4))
    ax.set_aspect("equal")
    ax.legend(fontsize=9, loc="upper left")
    save(fig, "calculus-secants")

    fig, ax = plt.subplots(figsize=(8.5, 5.5), layout="constrained")
    h = np.linspace(-0.5, 0.5, 1001)
    actual = np.abs(np.expm1(h)-h-h*h/2)
    bound = np.exp(0.5)*np.abs(h)**3/6
    ax.plot(h, actual, color=C[0], lw=2.4,
            label=r"actual: $|e^h-(1+h+h^2/2)|$")
    ax.plot(h, bound, color=C[1], lw=2, ls="--",
            label=r"bound: $e^{1/2}|h|^3/6$")
    ax.fill_between(h, actual, bound, color=C[1], alpha=0.1)
    ax.set(title="A Taylor error bound applies over an entire interval",
           xlabel="increment h (dimensionless)",
           ylabel="absolute error (dimensionless)")
    ax.legend()
    save(fig, "calculus-taylor-error")


def linear():
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained")
    time = np.array([0., 1., 2.])
    observed = np.array([1., 2., 2.])
    predicted = 7/6+time/2
    curve = np.linspace(-0.2, 2.2, 301)
    ax.plot(curve, 7/6+curve/2, color=C[0], lw=2,
            label=r"fit $7/6+t/2$")
    ax.scatter(time, observed, color=C[1], s=70, zorder=5,
               label="observations")
    ax.scatter(time, predicted, facecolors="white", edgecolors=C[0],
               s=55, zorder=4, label="predictions")
    for i, residual in enumerate(["-1/6", "1/3", "-1/6"]):
        ax.plot([time[i], time[i]], [predicted[i], observed[i]],
                color=C[2], lw=2.3)
        ax.text(time[i]+0.045, (predicted[i]+observed[i])/2, f"r = {residual}",
                fontsize=10, ha="left", va="center")
    ax.set(title="Exact least squares: prediction and residual",
           xlabel="t (dimensionless)", ylabel="measurement (dimensionless)",
           xlim=(-0.25, 2.6), ylim=(0.8, 2.5))
    ax.legend(loc="upper left")
    save(fig, "linear-regression")

    fig, ax = plt.subplots(figsize=(8, 5.8), layout="constrained")
    eps = np.logspace(-5, 0, 601)
    largest = (2+eps*eps+np.sqrt(4+eps**4))/2
    condition = largest/eps
    ax.loglog(eps, condition, color=C[0], lw=2.2,
              label=r"$\kappa_2(A_\varepsilon)=\lambda_+/\varepsilon$")
    ax.loglog(eps, condition**2, color=C[1], lw=2.2,
              label=r"$\kappa_2(A_\varepsilon^T A_\varepsilon)=\kappa_2(A_\varepsilon)^2$")
    ax.set(title="Normal equations square the condition number",
           xlabel=r"$\varepsilon$ (dimensionless)",
           ylabel="spectral condition number")
    ax.legend(fontsize=10)
    save(fig, "linear-conditioning")


def differential():
    fig, ax = plt.subplots(figsize=(9, 6.2), layout="constrained")
    tau = np.linspace(0, 14, 1201)
    for damping, color in zip([0, 0.3, 1, 2], C):
        if damping < 1:
            frequency = np.sqrt(1-damping*damping)
            response = 1-np.exp(-damping*tau)*(
                np.cos(frequency*tau)+damping/frequency*np.sin(frequency*tau))
        elif damping == 1:
            response = 1-(1+tau)*np.exp(-tau)
        else:
            root = np.sqrt(damping*damping-1)
            # Sum decaying modes avoids unnecessary exponential cancellation.
            r1, r2 = -damping+root, -damping-root
            response = 1+(r2*np.exp(r1*tau)-r1*np.exp(r2*tau))/(r1-r2)
        ax.plot(tau, response, lw=1.8, color=color,
                label=rf"$\zeta={damping:g}$")
    ax.axhline(1, color="#78818e", ls="--", lw=1, label="static value 1")
    ax.set(title="Step forcing with zero initial displacement and velocity",
           xlabel=r"normalized time $\tau=\omega_n t$",
           ylabel=r"normalized displacement $y=kx/F_0$")
    ax.legend(ncol=5, fontsize=10, loc="upper center", bbox_to_anchor=(0.5, -0.14))
    save(fig, "ode-step-response")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.4), layout="constrained")
    xi = np.linspace(0, 1, 601)
    for tau_value, color in zip([0, 0.02, 0.1], C):
        profile = np.exp(-np.pi**2*tau_value)*np.sin(np.pi*xi) + (
            0.5*np.exp(-4*np.pi**2*tau_value)*np.sin(2*np.pi*xi))
        axes[0].plot(xi, profile, lw=2, color=color,
                     label=rf"$\tau={tau_value:g}$")
    axes[0].set(title="Compatible two-mode initial profile",
                xlabel=r"normalized position $\xi=x/L$",
                ylabel="normalized temperature U")
    axes[0].legend()
    times = np.linspace(0, 0.2, 601)
    axes[1].semilogy(times, np.exp(-np.pi**2*times), color=C[0], lw=2,
                     label=r"mode 1: $e^{-\pi^2\tau}$")
    axes[1].semilogy(times, 0.5*np.exp(-4*np.pi**2*times), color=C[1], lw=2,
                     label=r"mode 2: $\frac{1}{2}e^{-4\pi^2\tau}$")
    axes[1].set(title="Higher spatial modes decay faster",
                xlabel=r"normalized time $\tau=\kappa t/L^2$",
                ylabel="modal amplitude (logarithmic scale)")
    axes[1].legend(fontsize=10)
    save(fig, "heat-mode-evolution")


if __name__ == "__main__":
    calculus()
    linear()
    differential()
