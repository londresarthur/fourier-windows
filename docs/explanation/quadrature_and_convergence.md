# 💡 Explicação Teórica: Quadratura Numérica e Convergência de Dirichlet

> **Quadrante Diátaxis:** Explanation (Orientado ao Entendimento e Teoria)

---

## 1. Quadratura Numérica de Gauss-Legendre

Os coeficientes de Euler-Fourier contínuos são definidos pelas integrais:

$$
a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)dx
$$

$$
b_n = \frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)dx
$$

O `fourier_toolbox` aproxima essas integrais via Quadratura Gaussiana com pesos e nós ótimos:

$$
\int_{-1}^1 g(u)\,du \approx \sum_{i=1}^M w_i \, g(u_i)
$$

Essa abordagem integra exatamente polinômios de grau até $2M - 1$, oferecendo precisão exponencial para funções suaves comparada à regra dos trapézios ou soma de Riemann simples.

---

## 2. O Kernel de Dirichlet e o Fenômeno de Gibbs

A soma truncada de Fourier pode ser expressa como a convolução da função original com o **Kernel de Dirichlet $D_N(t)$**:

$$
S_N(x) = \frac{1}{2\pi} \int_{-\pi}^\pi f(x - t) D_N(t)\,dt
$$

onde:

$$
D_N(t) = 1 + 2\sum_{n=1}^N \cos(nt) = \frac{\sin\left((N + 1/2)t\right)}{\sin(t/2)}
$$

Nas descontinuidades de primeira espécie (saltos), as oscilações laterais do kernel produzem um overshoot assintótico invariante de aproximadamente $8{,}949\%$ da altura do salto:

$$
\lim_{N \to \infty} \max_{x} S_N(x) = \frac{f(x^+) + f(x^-)}{2} + \frac{f(x^+) - f(x^-)}{\pi} \int_0^\pi \frac{\sin(u)}{u}\,du
$$
