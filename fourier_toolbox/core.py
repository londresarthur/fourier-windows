import numpy as np
from scipy.integrate import fixed_quad

class FourierEngine:
    def __init__(self, L, N, expression_or_func, mode='full', preset_id=None):
        self.L = float(L)
        self.N = int(N)
        self.func = expression_or_func
        self.mode = mode
        self.preset_id = preset_id
        
        self.a0 = 0.0
        self.an = np.zeros(N + 1)
        self.bn = np.zeros(N + 1)
        self.cn = np.zeros(N + 1)
        self.phases = np.zeros(N + 1)
        
        self._calculate_coefficients()

    def _calculate_coefficients(self):
        # Calculate a0
        # a0 = (1/L) * int_{-L}^{L} f(x) dx
        def integrand_a0(x):
            return self.func(x)
        val, _ = fixed_quad(integrand_a0, -self.L, self.L, n=500)
        self.a0 = val / self.L
        self.an[0] = self.a0 / 2
        self.cn[0] = abs(self.an[0])

        for n in range(1, self.N + 1):
            def integrand_an(x):
                return self.func(x) * np.cos(n * np.pi * x / self.L)
            
            def integrand_bn(x):
                return self.func(x) * np.sin(n * np.pi * x / self.L)

            if self.mode in ['full', 'even']:
                val_a, _ = fixed_quad(integrand_an, -self.L, self.L, n=500)
                self.an[n] = val_a / self.L
            else:
                self.an[n] = 0.0
                
            if self.mode in ['full', 'odd']:
                val_b, _ = fixed_quad(integrand_bn, -self.L, self.L, n=500)
                self.bn[n] = val_b / self.L
            else:
                self.bn[n] = 0.0

            self.cn[n] = np.sqrt(self.an[n]**2 + self.bn[n]**2)
            self.phases[n] = np.arctan2(-self.bn[n], self.an[n])

    def evaluate(self, x):
        res = np.full_like(x, self.a0 / 2, dtype=np.float64)
        for n in range(1, self.N + 1):
            res += self.an[n] * np.cos(n * np.pi * x / self.L)
            res += self.bn[n] * np.sin(n * np.pi * x / self.L)
        return res

    def harmonic(self, x, n):
        if n == 0:
            return np.full_like(x, self.a0 / 2, dtype=np.float64)
        return self.an[n] * np.cos(n * np.pi * x / self.L) + self.bn[n] * np.sin(n * np.pi * x / self.L)
        
    def dirichlet_kernel(self, t):
        # D_N(t) = sin((N+1/2) * pi * t / L) / (2 * L * sin(pi * t / (2*L)))
        # using L scaling appropriately. Often D_N(x) = sin((N+0.5)x)/sin(0.5x)
        # We'll use the normalized form on [-L, L]
        t = np.asarray(t)
        arg = np.pi * t / self.L
        num = np.sin((self.N + 0.5) * arg)
        den = np.sin(0.5 * arg)
        with np.errstate(divide='ignore', invalid='ignore'):
            res = num / den
        res[den == 0] = 2 * self.N + 1
        return res / (2 * self.L)

    def parseval_analysis(self):
        def integrand_e(x):
            return self.func(x)**2
        
        e_orig, _ = fixed_quad(integrand_e, -self.L, self.L, n=500)
        e_orig = e_orig / self.L
        
        e_n_cum = np.zeros(self.N + 1)
        e_n_cum[0] = (self.a0 / 2)**2 * 2
        for n in range(1, self.N + 1):
            e_n_cum[n] = e_n_cum[n-1] + (self.an[n]**2 + self.bn[n]**2)
            
        mse = e_orig - e_n_cum
        mse[mse < 0] = 0
        
        return {
            'E_orig': e_orig,
            'E_N': e_n_cum[-1],
            'E_N_cum': e_n_cum,
            'MSE': mse
        }

    def get_jump_midpoint(self, x0, epsilon=1e-5):
        val_left = self.func(x0 - epsilon)
        val_right = self.func(x0 + epsilon)
        return (val_left + val_right) / 2

    def to_latex(self, max_terms=5):
        terms = []
        if abs(self.a0/2) > 1e-10:
            terms.append(f"{self.a0/2:.4g}")
        for n in range(1, min(self.N, max_terms) + 1):
            if abs(self.an[n]) > 1e-10:
                terms.append(f"{self.an[n]:.4g} \\cos(\\frac{{{n}\\pi x}}{{{self.L}}})")
            if abs(self.bn[n]) > 1e-10:
                terms.append(f"{self.bn[n]:.4g} \\sin(\\frac{{{n}\\pi x}}{{{self.L}}})")
        if self.N > max_terms:
            terms.append("\\dots")
        
        return "S_N(x) = " + " + ".join(terms).replace("+ -", "- ")

    def generate_epicycles(self, t):
        # Generates phasor positions at time t for epicycle drawing
        # phasors in complex plane: c_n * e^{i * (n * pi * t / L + phase)}
        # but using Euler coeffs properly
        points = [0j]
        # a0/2 term
        points.append(points[-1] + self.an[0])
        
        # We need to sort by magnitude for nicer epicycles
        idx = np.argsort(self.cn[1:])[::-1] + 1
        for n in idx:
            if self.cn[n] > 1e-10:
                # complex coefficient representation for a_n and b_n
                # (an - i bn)/2 * e^{i n w t} + (an + i bn)/2 * e^{-i n w t}
                # For plotting epicycles as continuous spinning circles:
                w = n * np.pi * t / self.L
                c = complex(self.an[n], -self.bn[n]) * np.exp(1j * w)
                points.append(points[-1] + c)
        return points
