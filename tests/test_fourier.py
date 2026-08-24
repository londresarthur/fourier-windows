"""
Unit tests for the fourier_toolbox package.
"""

import unittest
import numpy as np
from fourier_toolbox.core import FourierEngine
from fourier_toolbox.presets import get_presets


class TestFourierEngine(unittest.TestCase):

    def test_parity_symmetry(self):
        presets = get_presets()
        
        # Test even function (abs_x): bn should be 0
        p_even = presets['abs_x']
        engine_even = FourierEngine(p_even.L, 5, p_even.func, mode=p_even.mode)
        self.assertTrue(np.allclose(engine_even.bn, 0, atol=1e-5), "Even function should have bn=0")
        
        # Test odd function (x): an should be 0 (except maybe a0)
        p_odd = presets['x']
        engine_odd = FourierEngine(p_odd.L, 5, p_odd.func, mode=p_odd.mode)
        self.assertTrue(np.allclose(engine_odd.an, 0, atol=1e-5), "Odd function should have an=0")

    def test_basel_series(self):
        def abs_pi(x):
            return np.abs(x)
        
        engine = FourierEngine(np.pi, 50, abs_pi, mode='even')
        val_at_0 = engine.evaluate(0)
        self.assertTrue(np.isclose(val_at_0, 0, atol=0.05), "Basel series deduction at x=0 should converge to 0")

    def test_parseval_conservation(self):
        p = get_presets()['triangle']
        engine = FourierEngine(p.L, 10, p.func, mode=p.mode)
        
        pa = engine.parseval_analysis()
        
        # sum of energies <= E_orig (Bessel)
        self.assertTrue(np.all(pa['E_N_cum'] <= pa['E_orig'] + 1e-5), "Cumulative energy should be <= original energy")
        
        # converges as N increases
        self.assertTrue(pa['MSE'][-1] < pa['MSE'][0], "MSE should decrease with more terms")

    def test_dirichlet_jump_convergence(self):
        p_sign = get_presets()['sign_x']
        engine = FourierEngine(p_sign.L, 20, p_sign.func, mode='full')
        
        # For sign(x), jump at x=0 is from -1 to +1. Midpoint is 0.
        midpoint = engine.get_jump_midpoint(0)
        self.assertTrue(np.isclose(midpoint, 0, atol=1e-5), "Dirichlet jump midpoint for sign(x) at x=0 should be 0")
        
        val = engine.evaluate(0)
        self.assertTrue(np.isclose(val, 0, atol=1e-5), "Fourier series should converge to midpoint at jump")

        p_pulse = get_presets()['causal_pulse']
        engine2 = FourierEngine(p_pulse.L, 20, p_pulse.func, mode='full')
        midpoint2 = engine2.get_jump_midpoint(0)
        self.assertTrue(np.isclose(midpoint2, 0.5, atol=1e-5), "Dirichlet jump midpoint for causal pulse at x=0 should be 0.5")
        
        val2 = engine2.evaluate(0)
        self.assertTrue(np.isclose(val2, 0.5, atol=0.05), "Fourier series should converge to midpoint at jump (pulse)")


if __name__ == '__main__':
    unittest.main()
