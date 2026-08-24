# 🐍 Fourier Toolbox

Biblioteca Python modular para computação científica, análise de **Séries e Transformadas de Fourier**, integração numérica por quadratura de Gauss-Legendre, visualização gráfica de alta resolução e síntese de áudio harmônico.

---

## 📦 Instalação

```bash
# Instalação direta do repositório local
git clone https://github.com/londresarthur/fourier-toolbox.git
cd fourier-toolbox
pip install -e .
```

---

## 🚀 Uso Rápido em Python

```python
import numpy as np
from fourier_toolbox import FourierEngine, plot_series, synthesize_wav

# 1. Definir função periódica e ordem harmônica
engine = FourierEngine(
    L=np.pi,
    N=15,
    expression_or_func=lambda x: np.abs(x),
    mode='even'
)

# 2. Avaliar aproximação S_N(x) e Parseval
print(f"a0 = {engine.a0:.4f}")
parseval = engine.parseval_analysis()
print(f"Conservação de Energia: {parseval['conservation_ratio'] * 100:.2f}%")

# 3. Gerar figura e exportar áudio WAV
fig, ax = plot_series(engine, show_error=True)
fig.savefig("fourier_series.png", dpi=300)

synthesize_wav(engine, "saida.wav", duration=2.0, base_freq=220.0)
```

---

## 💻 Interface de Linha de Comando (CLI)

```bash
# Calcular coeficientes do preset |x| e imprimir fórmula LaTeX
python -m fourier_toolbox --preset abs_x -N 15 --latex

# Gerar gráfico vetorial e exportar síntese de áudio
python -m fourier_toolbox --preset square_wave -N 30 --save-plot onda_quadrada.png --audio onda_quadrada.wav
```

---

## 📚 Documentação

A documentação segue o framework [Diátaxis](https://diataxis.fr/):
- **[🚀 Tutoriais](docs/tutorials/)**: Primeiros passos práticos
- **[🛠️ Guias How-To](docs/how-to/)**: Receitas de exportação e customização
- **[📖 Referência](docs/reference/)**: Especificações técnicas da API
- **[💡 Explicação](docs/explanation/)**: Teoria matemática de quadratura e Dirichlet

---

## 🧪 Testes Unitários

```bash
python -m unittest discover -s tests
```
