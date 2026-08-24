import numpy as np
import matplotlib.pyplot as plt

def plot_series(engine, ax=None, num_points=1000, title="Fourier Series Approximation"):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        
    x = np.linspace(-engine.L, engine.L, num_points)
    y_orig = engine.func(x)
    y_approx = engine.evaluate(x)
    
    ax.plot(x, y_orig, 'k-', lw=2, label="f(x)")
    ax.plot(x, y_approx, 'r--', lw=2, label=f"S_{engine.N}(x)")
    
    ax.fill_between(x, y_orig, y_approx, color='gray', alpha=0.3, label="Error")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)
    return ax

def plot_spectrum(engine, mode='coefficients', ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        
    n_vals = np.arange(engine.N + 1)
    
    if mode == 'coefficients':
        ax.stem(n_vals, engine.cn, basefmt=" ", use_line_collection=True)
        ax.set_ylabel("Magnitude $c_n$")
        ax.set_title("Harmonic Spectrum")
    elif mode == 'energy':
        e_n = engine.cn**2
        e_n[0] = (engine.a0/2)**2 * 2  # DC energy
        ax.stem(n_vals, e_n, basefmt=" ", use_line_collection=True)
        ax.set_ylabel("Energy")
        ax.set_title("Energy Spectrum")
    elif mode == 'convergence':
        pa = engine.parseval_analysis()
        ax.plot(n_vals, pa['E_N_cum'], 'b-', marker='o', label="Cumulative Energy")
        ax.axhline(pa['E_orig'], color='r', linestyle='--', label="Original Energy")
        ax.set_ylabel("Cumulative Energy")
        ax.set_title("Parseval Energy Convergence")
        ax.legend()
        
    ax.set_xlabel("n")
    ax.grid(True)
    return ax

def plot_parseval_convergence(engine, ax=None):
    return plot_spectrum(engine, mode='convergence', ax=ax)
