# 📚 Documentação Técnica — Fourier Toolbox (Diátaxis)

Estrutura da documentação de acordo com os quatro quadrantes do framework **Diátaxis**:

```
docs/
├── tutorials/       # 🚀 Tutoriais práticos (getting started)
│   └── 01_quickstart.md
├── how-to/          # 🛠️ Guias "Como Fazer" (plotagem, áudio, exportação)
│   └── export_audio_and_plots.md
├── reference/       # 📖 Especificações completas de APIs e classes
│   └── api_reference.md
└── explanation/     # 💡 Fundamentação teórica, quadratura e convergência
    └── quadrature_and_convergence.md
```

---

### 1. [🚀 Tutoriais (`tutorials/`)](tutorials/)
- **[Primeiros Passos com o Fourier Toolbox](tutorials/01_quickstart.md)**: Instalação e primeiro cálculo com visualização gráfica e síntese de áudio em Python.

### 2. [🛠️ Guias Práticos (`how-to/`)](how-to/)
- **[Exportação de Áudio e Gráficos Vetoriais](how-to/export_audio_and_plots.md)**: Geração de figuras SVG/PNG de alta resolução e arquivos de áudio WAV de 44.1 kHz.

### 3. [📖 Referência Técnica (`reference/`)](reference/)
- **[Referência da API](reference/api_reference.md)**: Métodos e atributos da classe `FourierEngine` e funções auxiliares de plotagem e síntese.

### 4. [💡 Explicação & Teoria (`explanation/`)](explanation/)
- **[Quadratura Numérica e Convergência de Dirichlet](explanation/quadrature_and_convergence.md)**: Integração via Gauss-Legendre, convolução com Kernel de Dirichlet e overshoot de Gibbs.
