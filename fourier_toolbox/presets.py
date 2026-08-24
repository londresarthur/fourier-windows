import numpy as np

class Preset:
    def __init__(self, id, name, func, L, mode='full', description=""):
        self.id = id
        self.name = name
        self.func = func
        self.L = L
        self.mode = mode
        self.description = description

def get_presets():
    presets = []
    
    # 1. abs(x)
    presets.append(Preset("abs_x", "|x|", lambda x: np.abs(x), 1.0, mode='even'))
    
    # 2. pi-x odd (Sawtooth)
    presets.append(Preset("pi_x_odd", "pi - x (odd)", lambda x: np.sign(x) * (np.pi - np.abs(x)), np.pi, mode='odd'))
    
    # 3. pi-x even (Triangle)
    presets.append(Preset("pi_x_even", "pi - |x| (even)", lambda x: np.pi - np.abs(x), np.pi, mode='even'))
    
    # 4. pi-x direct
    presets.append(Preset("pi_x_direct", "pi - x", lambda x: np.pi - x, np.pi, mode='full'))
    
    # 5. sign(x)
    presets.append(Preset("sign_x", "sign(x)", lambda x: np.sign(x), 1.0, mode='odd'))
    
    # 6. x
    presets.append(Preset("x", "x", lambda x: x, 1.0, mode='odd'))
    
    # 7. causal pulse (Heaviside step pulse)
    presets.append(Preset("causal_pulse", "Causal Pulse", lambda x: np.where((x >= 0) & (x < 0.5), 1.0, 0.0), 1.0, mode='full'))
    
    # 8. triangle
    presets.append(Preset("triangle", "Triangle", lambda x: 1 - np.abs(x), 1.0, mode='even'))
    
    # 9. exp(-abs(x))
    presets.append(Preset("exp_abs_x", "exp(-|x|)", lambda x: np.exp(-np.abs(x)), np.pi, mode='even'))
    
    # 10. rectified sine
    presets.append(Preset("rectified_sine", "Rectified Sine", lambda x: np.abs(np.sin(x)), np.pi, mode='even'))
    
    # 11. quadratic
    presets.append(Preset("quadratic", "x^2", lambda x: x**2, 1.0, mode='even'))

    return {p.id: p for p in presets}
