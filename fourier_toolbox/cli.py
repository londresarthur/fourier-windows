import argparse
from .core import FourierEngine
from .presets import get_presets
from .plotting import plot_fourier_series, plot_spectrum
from .audio import synthesize_wav
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Fourier Toolbox CLI")
    parser.add_argument("--preset", type=str, required=True, help="Preset ID")
    parser.add_argument("-N", type=int, default=10, help="Number of terms")
    parser.add_argument("--plot", action="store_true", help="Show plots")
    parser.add_argument("--save-plot", type=str, help="Save plot to file")
    parser.add_argument("--audio", type=str, help="Save audio to wav file")
    parser.add_argument("--latex", action="store_true", help="Print LaTeX formula")
    
    args = parser.parse_args()
    
    presets = get_presets()
    if args.preset not in presets:
        print(f"Error: preset {args.preset} not found.")
        print(f"Available presets: {list(presets.keys())}")
        return
        
    p = presets[args.preset]
    engine = FourierEngine(p.L, args.N, p.func, mode=p.mode, preset_id=p.id)
    
    if args.latex:
        print("LaTeX representation:")
        print(engine.to_latex())
        
    if args.audio:
        synthesize_wav(engine, args.audio)
        print(f"Audio saved to {args.audio}")
        
    if args.plot or args.save_plot:
        fig, axs = plt.subplots(1, 2, figsize=(15, 6))
        plot_fourier_series(engine, ax=axs[0])
        plot_spectrum(engine, ax=axs[1])
        
        if args.save_plot:
            plt.savefig(args.save_plot)
            print(f"Plot saved to {args.save_plot}")
            
        if args.plot:
            plt.show()

if __name__ == "__main__":
    main()
