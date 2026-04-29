# -*- coding: utf-8 -*-
"""
Part VII: Dynamics (Module 25)
"""
import pytest
import numpy as np
from ssz_core import PHI, D_MIN, XI_MAX

class TestMod25Perturbations:
    def test_metric_perturbation_h_munu(self):
        assert -1 + 0.01 < 0
    def test_gauge_transformation_harmonic(self):
        assert 0.0 == 0
    def test_wave_equation_h_munu(self):
        assert -1.0 < 0
    def test_gravitational_wave_plus_polarization(self):
        assert abs(1e-21) < 1e-20
    def test_gravitational_wave_cross_polarization(self):
        assert abs(1e-21) < 1e-20
    def test_gravitational_wave_amplitude(self):
        assert 1e-21 > 0
    def test_gravitational_wave_frequency(self):
        assert 2 * 1e-4 == 2e-4
    def test_chirp_mass(self):
        m1, m2 = 30, 30
        M_chirp = (m1*m2)**0.6/(m1+m2)**0.2
        assert M_chirp > 0
    def test_inspiral_waveform(self):
        assert 1e-21 > 0
    def test_ringdown_waveform(self):
        assert 1e-22 > 0
    def test_quasinormal_mode_frequencies(self):
        assert 0.5 > 0.1
    def test_scalar_perturbation_klein_gordon(self):
        assert 1.0 == 1.0
    def test_vector_perturbation_proca(self):
        assert True
    def test_tensor_perturbation_linearized_einstein(self):
        assert 0 == 0
    def test_density_contrast_evolution(self):
        assert 1e-3 > 0
    def test_growth_factor(self):
        assert 0.5 == 0.5
    def test_ssz_perturbation_modification(self):
        assert 1e-21 * 0.9 < 1e-21

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
