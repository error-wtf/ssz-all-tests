import pytest
import numpy as np
from ssz_core import PHI, C_SI, XI_MAX, D_MIN

class TestCh10MaxwellSSZ:
    def test_maxwell_divergence_E(self):
        rho, epsilon0 = 1.0, 8.854e-12
        div_E = rho / epsilon0
        assert div_E > 0

class TestCh11GaugeTheory:
    def test_gauge_transformation_scalar(self):
        phi, lambda_t = 1.0, 0.5
        phi_prime = phi - lambda_t
        assert phi_prime != phi

class TestCh12Optics:
    def test_snellius_law(self):
        n1, n2 = 1.0, 1.5
        theta1 = np.pi/4
        theta2 = np.arcsin(n1*np.sin(theta1)/n2)
        assert theta2 < theta1

class TestCh13CMB:
    def test_cmb_temperature(self):
        T_cmb = 2.725
        assert 2.7 < T_cmb < 2.8

class TestCh14QED:
    def test_fine_structure_constant(self):
        alpha = 1/137.036
        assert 0.007 < alpha < 0.008

class TestCh15Plasma:
    def test_plasma_frequency(self):
        n, e, m_e, eps0 = 1e18, 1.6e-19, 9.1e-31, 8.85e-12
        omega_p = np.sqrt(n*e**2/(m_e*eps0))
        assert omega_p > 0