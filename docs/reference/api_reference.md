# 📖 Referência da API: `fourier_toolbox`

> **Quadrante Diátaxis:** Reference (Orientado à Informação Técnica)

---

## 1. Classe `FourierEngine`

```python
FourierEngine(L, N, expression_or_func, mode='full', preset_id=None)
```

### Atributos

| Atributo | Tipo | Descrição |
| :--- | :--- | :--- |
| `a0` | `float` | Coeficiente DC médio da função. |
| `an` | `np.ndarray` | Array $(N+1)$ com os coeficientes dos cossenos ($a_0/2$ no índice 0). |
| `bn` | `np.ndarray` | Array $(N+1)$ com os coeficientes dos senos ($b_0 = 0$). |
| `cn` | `np.ndarray` | Array $(N+1)$ das magnitudes complexas $\sqrt{a_n^2 + b_n^2}$. |
| `phases` | `np.ndarray` | Array $(N+1)$ dos ângulos de fase $-\text{atan2}(b_n, a_n)$. |

### Métodos

- `evaluate(x)`: Avalia $S_N(x)$ para um escalar ou array NumPy $x$.
- `harmonic(x, n)`: Avalia o $n$-ésimo termo harmônico isolado $h_n(x)$.
- `parseval_analysis()`: Retorna dicionário com `E_orig`, `E_N_cum`, `MSE` e `conservation_ratio`.
- `dirichlet_kernel(t)`: Retorna o kernel de Dirichlet $D_N(t) = \frac{\sin((N + 1/2)t)}{\sin(t/2)}$.
- `to_latex(max_terms=6)`: Retorna a string LaTeX formatada da série truncada.

---

## 2. Funções do Módulo

- `get_presets()`: Retorna catálogo dos presets canônicos disponíveis.
- `plot_series(engine, x_range=None, num_points=1000, show_error=True)`: Plota $f(x)$ vs $S_N(x)$.
- `plot_spectrum(engine, mode='coefficients')`: Plota espectro de magnitude ou convergência de Parseval.
- `synthesize_wav(engine, output_path, duration=2.0, sample_rate=44100, base_freq=220.0)`: Exporta arquivo `.wav`.
