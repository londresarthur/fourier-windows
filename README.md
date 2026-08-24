# 🪟 Fourier Windows (Desktop & Python Suite)

Suíte científica nativa para Windows e biblioteca Python dedicada à análise de **Séries e Transformadas de Fourier**, integração numérica de alta precisão (Quadratura de Gauss-Legendre), plotagem de alta resolução com Matplotlib e síntese acústica WAV.

> **Nota de Ecossistema:** Este repositório é a versão dedicada para **Windows / Desktop**. O projeto Android móvel reside separadamente no repositório `fourier-toolbox`.

---

## 📦 Instalação no Windows

```powershell
# Clonar o repositório
git clone https://github.com/londresarthur/fourier-windows.git
cd fourier-windows

# Instalar em modo de desenvolvimento
pip install -e .
```

---

## 🚀 Uso em Scripts Python

```python
import numpy as np
from fourier_toolbox import FourierEngine, plot_series, synthesize_wav

# 1. Inicializar motor de cálculo com L=pi e N=15
engine = FourierEngine(
    L=np.pi,
    N=15,
    expression_or_func=lambda x: np.abs(x),
    mode='even'
)

# 2. Obter coeficientes e relatório de Parseval
print(f"Termo Médio (DC) a0 = {engine.a0:.4f}")
parseval = engine.parseval_analysis()
print(f"Conservação de Energia: {parseval['conservation_ratio'] * 100:.2f}%")

# 3. Gerar figura e exportar áudio WAV
fig, ax = plot_series(engine, show_error=True)
fig.savefig("fourier_series.png", dpi=300)

synthesize_wav(engine, "saida.wav", duration=2.0, base_freq=220.0)
```

---

## 💻 CLI do Windows (Prompt / PowerShell)

```powershell
# Linha de comando para análise de Fourier no Windows
fourier-windows --preset abs_x -N 15 --latex

# Plotar onda e exportar áudio WAV
fourier-windows --preset square_wave -N 30 --save-plot onda.png --audio som.wav
```

---

## 📚 Documentação (Framework Diátaxis)

- **[🚀 Tutoriais](docs/tutorials/)**: Primeiros passos práticos no Windows
- **[🛠️ Guias How-To](docs/how-to/)**: Exportação de áudio WAV e gráficos SVG/PNG
- **[📖 Referência](docs/reference/)**: Especificação de APIs e classes
- **[💡 Explicação](docs/explanation/)**: Teoria matemática de quadratura e Dirichlet

---

## 🧪 Testes Unitários

```powershell
python -m unittest discover -s tests
```
