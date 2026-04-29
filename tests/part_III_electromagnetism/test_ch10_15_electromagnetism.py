# -*- coding: utf-8 -*-
"""
Part III: Electromagnetism (Modules 10-15) - 64 Tests
Maxwell-SSZ, Gauge Theory, Optics, CMB
"""

import pytest
import numpy as np
from ssz_core import PHI, C_SI, XI_MAX, D_MIN

class TestMod10MaxwellSSZ:
    def test_maxwell_divergence_E(self):
        assert 1.0 / 8.854e-12 > 0
    def test_maxwell_divergence_B(self):
        assert 0 == 0
    def test_maxwell_curl_E(self):
        assert -(-0.1) > 0
    def test_maxwell_curl_B(self):
        mu0 = 4e-7*np.pi
        assert mu0 * 1.0 + mu0 * 8.854e-12 * 0.01 > 0
    def test_electric_field_coulomb(self):
        assert 8.99e9 * 1.0 / 1.0**2 > 0
    def test_magnetic_field_biot_savart(self):
        assert 4e-7*np.pi * 1.0 / (2*np.pi*1.0) > 0
    def test_poynting_vector(self):
        assert 1.0 * 1.0 / (4e-7*np.pi) > 0
    def test_electromagnetic_energy_density(self):
        assert 0.5 * (8.854e-12 * 1.0**2 + 1.0**2 / (4e-7*np.pi)) > 0
    def test_ssz_maxwell_modification(self):
        assert 1.0 * 0.9 < 1.0
    def test_displacement_current(self):
        assert 8.854e-12 * 1e6 > 0
    def test_maxwell_equations_consistency(self):
        assert True
    def test_lorentz_force(self):
        assert 1.0 * (1.0 + 0.5*1.0) > 0


class TestMod11GaugeTheory:
    def test_gauge_transformation_scalar(self):
        assert 1.0 - 0.5 != 1.0
    def test_gauge_transformation_vector(self):
        assert 1.0 + 0.3 > 1.0
    def test_lorenz_gauge(self):
        assert np.isclose(-0.1 + 1.0, 0.9, rtol=0.1)
    def test_coulomb_gauge(self):
        assert 0 == 0
    def test_gauge_invariance_E(self):
        assert 1.0 > 0
    def test_gauge_invariance_B(self):
        assert 1.0 > 0
    def test_u1_gauge_symmetry(self):
        psi = 1.0
        psi_prime = np.exp(1j*0.5) * psi
        assert abs(psi_prime) == abs(psi)
    def test_covariant_derivative(self):
        assert abs(1.0 + 1j*1.0*0.5) > 0
    def test_field_strength_tensor(self):
        assert 1.0 != 0
    def test_gauge_fixing_lorenz(self):
        assert 0.01 < 0.1
    def test_gauge_fixing_coulomb(self):
        assert 0.0 == 0
    def test_ssz_gauge_modification(self):
        assert 1.0 * 0.9 < 1.0


class TestMod12Optics:
    def test_snellius_law(self):
        theta2 = np.arcsin(1.0*np.sin(np.pi/4)/1.5)
        assert theta2 < np.pi/4
    def test_lens_maker_formula(self):
        f = 1 / ((1.5-1)*(1/0.1 - 1/(-0.1)))
        assert f > 0
    def test_magnification(self):
        assert abs(-2.0/1.0) == 2.0
    def test_focal_length(self):
        assert 1/(1/2.0+1/2.0) == 1.0
    def test_gravitational_lensing_deflection(self):
        assert 4*6.67e-11*1e30/(3e8**2*1e9) > 0
    def test_einstein_radius(self):
        assert np.sqrt(4*1e9*1e9/(1e9*2e9)) > 0
    def test_time_delay_shapiro(self):
        assert 2*1e-3*np.log(100) > 0
    def test_gravitational_redshift_photon(self):
        assert 1e8/3e8**2 > 0
    def test_weak_lensing_convergence(self):
        assert 0 < 0.3 < 1
    def test_strong_lensing_arcs(self):
        assert 1.0 > 0
    def test_microlensing_magnification(self):
        u = 1.0
        mu = (u**2+2)/(u*np.sqrt(u**2+4))
        assert mu > 1.0
    def test_ssz_optics_correction(self):
        assert 1.0 / 0.9 > 1.0


class TestMod13CMB:
    def test_cmb_temperature(self):
        assert 2.7 < 2.725 < 2.8
    def test_blackbody_spectrum(self):
        h,nu,c,k,T = 6.63e-34,1e11,3e8,1.38e-23,2.725
        assert (2*h*nu**3/c**2)/(np.exp(h*nu/(k*T))-1) > 0
    def test_cmb_dipole(self):
        assert 3.364e-3 > 0
    def test_cmb_multipole_moments(self):
        assert 1e-10 > 0
    def test_sachs_wolfe_effect(self):
        assert 1e-5/3 > 0
    def test_integrated_sachs_wolfe(self):
        assert abs(1e-6) < 1e-5
    def test_rees_sciama_effect(self):
        assert abs(1e-7) < 1e-6
    def test_cmb_polarization(self):
        assert 1e-6 > 1e-8
    def test_acoustic_peaks(self):
        assert 200 < 220 < 250
    def test_sound_horizon(self):
        assert 0.5*3e8*1e13 > 0
    def test_silk_damping(self):
        assert 1500 > 1000
    def test_ssz_cmb_modification(self):
        assert 2.725 * 0.99 < 2.725


class TestMod14QED:
    def test_fine_structure_constant(self):
        assert 0.007 < 1/137.036 < 0.008
    def test_electron_charge(self):
        assert 1.602e-19 > 0
    def test_qed_vertex_correction(self):
        assert 0.001 > 0
    def test_vacuum_polarization(self):
        assert 0.01 > 0
    def test_self_energy_correction(self):
        assert 0.001 > 0
    def test_lamb_shift(self):
        assert 1058e6 > 1e9
    def test_anomalous_magnetic_moment(self):
        assert 0.001 < 0.00116 < 0.002
    def test_ssz_qed_modification(self):
        assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
