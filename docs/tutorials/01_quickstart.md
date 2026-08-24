# 🚀 Tutorial: Primeiros Passos com o Fourier Toolbox

> **Quadrante Diátaxis:** Tutorial (Orientado ao Aprendizado)  
> **Objetivo:** Guiar o desenvolvedor pelo primeiro cálculo numérico, plotagem e síntese de Séries de Fourier em Python.

---

## 1. Instalação em Modo Editável

No terminal dentro do repositório `fourier-toolbox`:

```bash
pip install -e .
```

---

## 2. Primeiro Script em Python

Crie um script `exemplo.py` com o seguinte conteúdo:

```python
import numpy as np
from fourier_toolbox import FourierEngine, plot_series, synthesize_wav

# 1. Definir uma função alvo f(x) = |x| no intervalo [-pi, pi]
def f(x):
    return np.abs(x)

# 2. Inicializar o motor de cálculo com L=pi e N=10 harmônicos
engine = FourierEngine(L=np.pi, N=10, expression_or_func=f, mode='even')

# 3. Exibir coeficientes calculados
print(f"a0 = {engine.a0:.4f}")
for n in range(1, 6):
    print(f"a_{n} = {engine.an[n]:.4f}, b_{n} = {engine.bn[n]:.4f}")

# 4. Gerar e exibir gráfico de convergência
fig, ax = plot_series(engine, show_error=True)
fig.savefig("fourier_abs_x.png", dpi=300)

# 5. Sintetizar áudio WAV da onda
synthesize_wav(engine, "fourier_abs_x.wav", duration=2.0, base_freq=220.0)
print("Áudio exportado com sucesso para fourier_abs_x.wav!")
```

Execute o script:

```bash
python exemplo.py
```

---

## 3. Uso Direto via Linha de Comando (CLI)

O pacote oferece uma interface CLI completa:

```bash
# Calcular e exibir série de Fourier do preset abs_x com 15 harmônicos
python -m fourier_toolbox --preset abs_x -N 15 --latex

# Gerar gráfico e exportar áudio WAV
python -m fourier_toolbox --preset square_wave -N 25 --save-plot square.png --audio square.wav
```
