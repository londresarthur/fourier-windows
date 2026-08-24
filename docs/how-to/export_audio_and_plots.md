# 🛠️ Guia Prático: Exportação de Áudio e Gráficos Vetoriais

> **Quadrante Diátaxis:** How-To Guide (Orientado a Tarefas)  
> **Objetivo:** Ensinar a customizar gráficos para publicação científica e gerar arquivos de áudio WAV de alta fidelidade.

---

## 1. Exportar Gráficos de Alta Resolução

```python
import matplotlib.pyplot as plt
from fourier_toolbox import FourierEngine, plot_series, plot_spectrum

engine = FourierEngine(L=3.14159, N=20, expression_or_func=lambda x: x, mode='odd')

# 1. Gráfico no domínio do tempo com preenchimento de erro residual
fig1, ax1 = plot_series(engine, show_error=True)
fig1.savefig("sawtooth_time.svg", format="svg", bbox_inches="tight")

# 2. Espectro de coeficientes harmônicos
fig2, ax2 = plot_spectrum(engine, mode='coefficients')
fig2.savefig("sawtooth_spectrum.png", dpi=300, bbox_inches="tight")
```

---

## 2. Sintetizar Ondas Sonoras WAV

```python
from fourier_toolbox import FourierEngine, synthesize_wav
import numpy as np

# Função degrau bipolar (onda quadrada)
engine = FourierEngine(L=1.0, N=30, expression_or_func=lambda x: np.sign(x))

# Síntese na frequência fundamental de 440 Hz (Nota Lá4)
synthesize_wav(
    engine,
    output_path="onda_quadrada_440hz.wav",
    duration=3.0,
    sample_rate=44100,
    base_freq=440.0
)
```
