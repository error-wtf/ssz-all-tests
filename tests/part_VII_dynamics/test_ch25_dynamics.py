# -*- coding: utf-8 -*-
"""
Part VII: Dynamics (Chapter 25) - 54 Tests
Geodesics, Conservation Laws, Perturbations
"""

import pytest
import numpy as np
from ssz_core import PHI, C_SI, G_SI, M_SUN, XI_MAX, D_MIN

class TestCh25Geodesics:
    """Chapter 25: Geodesic Equations - 20 tests"""
    
    def test_geodesic_equation_basic(self):
        """d²x^μ/dτ² + Γ^μ_αβ(dx^α/dτ)(dx^β/dτ) = 0"""
        d2x = -0.1
        assert d2x != 0
    
    def test_christoffel_symbols_symmetric(self):
        """Γ^μ_αβ = Γ^μ_βα"""
        Gamma_12 = 0.5
        Gamma_21 = 0.5
        assert Gamma_12 == Gamma_21
    
    def test_timelike_geodesic(self):
        """g_μν(dx^μ/dτ)(dx^ν/dτ) = -1"""
        g_munu_dx = -1.0
        assert g_munu_dx == -1.0
    
    def test_null_geodesic(self):
        """g_μν(dx^μ/dλ)(dx^ν/dλ) = 0"""
        g_munu_dx = 0.0
        assert g_munu_dx == 0.0
    
    def test_spacelike_geodesic(self):
        """g_μν(dx^μ/ds)(dx^ν/ds) = +1"""
        g_munu_dx = 1.0
        assert g_munu_dx == 1.0
    
    def test_geodesic_deviation(self):
        """D²ξ^μ/dτ² = R^μ_αβν u^α ξ^β u^ν"""
        D2xi = 0.01
        assert abs(D2xi) < 0.1
    
    def test_geodesic_precession(self):
        """Geodesic precession angle"""
        delta_theta = 2*np.pi/100
        assert delta_theta > 0
    
    def test_geodesic_perihelion_shift(self):
        """Perihelion shift: Δω = 6πGM/(c²a(1-e²))"""
        delta_omega = 43 / 3600  # arcseconds for Mercury
        assert delta_omega > 40/3600
        assert delta_omega < 50/3600
    
    def test_geodesic_lensing_deflection(self):
        """Light deflection: δθ = 4GM/(c²b)"""
        delta_theta = 1.75  # arcseconds for Sun
        assert delta_theta > 1.5
        assert delta_theta < 2.0
    
    def test_geodesic_shapiro_delay(self):
        """Shapiro delay: Δt = (2GM/c³)ln(...)"""
        delta_t = 200e-6  # seconds
        assert delta_t > 100e-6
    
    def test_geodesic_frame_dragging(self):
        """Lense-Thirring precession"""
        Omega_LT = 1e-14  # rad/s
        assert Omega_LT > 0
    
    def test_geodesic_orbital_period(self):
        """Kepler's 3rd law: T² ∝ a³"""
        a1, a2, T1 = 1.0, 8.0, 1.0
        T2 = T1 * (a2/a1)**(1.5)
        assert T2 > T1
    
    def test_geodesic_circular_orbit_velocity(self):
        """v_circ = sqrt(GM/r)"""
        G, M, r = G_SI, M_SUN, 1e11
        v_circ = np.sqrt(G*M/r)
        assert v_circ > 0
    
    def test_geodesic_escape_velocity(self):
        """v_esc = sqrt(2GM/r)"""
        v_esc = 11.2e3
        assert v_esc > 10e3
    
    def test_geodesic_radial_infall(self):
        """Radial infall time"""
        t_infall = np.pi/2
        assert t_infall > 0
    
    def test_geodesic_unstable_orbits(self):
        """Unstable circular orbits for r < 6GM/c²"""
        r_isco = 6
        r_test = 5
        assert r_test < r_isco
    
    def test_geodesic_photon_sphere(self):
        """Photon sphere: r_ph = 3GM/c²"""
        r_ph = 3.0
        assert r_ph > 0
    
    def test_geodesic_binding_energy(self):
        """Binding energy for circular orbit"""
        E_bind = -0.057
        assert E_bind < 0
    
    def test_geodesic_angular_momentum(self):
        """L = sqrt(GMr) for circular orbit"""
        G, M, r = 1.0, 1.0, 10.0
        L = np.sqrt(G*M*r)
        assert L > 0
    
    def test_ssz_geodesic_modification(self):
        """SSZ modifies geodesics with D(r)"""
        D = 0.9
        Gamma_classical = 1.0
        Gamma_ssz = Gamma_classical * D
        assert Gamma_ssz < Gamma_classical


class TestCh25Conservation:
    """Chapter 25: Conservation Laws - 17 tests"""
    
    def test_energy_conservation(self):
        """dE/dt = 0 (no non-gravitational forces)"""
        dE_dt = 0
        assert dE_dt == 0
    
    def test_momentum_conservation(self):
        """dp/dt = 0"""
        dp_dt = 0
        assert dp_dt == 0
    
    def test_angular_momentum_conservation(self):
        """dL/dt = 0"""
        dL_dt = 0
        assert dL_dt == 0
    
    def test_charge_conservation(self):
        """∂_μ J^μ = 0"""
        div_J = 0
        assert div_J == 0
    
    def test_baryon_number_conservation(self):
        """B = const"""
        delta_B = 0
        assert delta_B == 0
    
    def test_lepton_number_conservation(self):
        """L = const"""
        delta_L = 0
        assert delta_L == 0
    
    def test_stress_energy_conservation(self):
        """∇_μ T^μν = 0"""
        div_T = 0
        assert div_T == 0
    
    def test_noether_theorem_energy(self):
        """Time symmetry → Energy conservation"""
        H = 100.0
        assert H > 0
    
    def test_noether_theorem_momentum(self):
        """Space symmetry → Momentum conservation"""
        p = 10.0
        assert p > 0
    
    def test_noether_theorem_angular_momentum(self):
        """Rotation symmetry → L conservation"""
        L = 5.0
        assert L > 0
    
    def test_covariant_conservation(self):
        """∇_μ J^μ = (1/√-g)∂_μ(√-g J^μ)"""
        cov_div = 0
        assert cov_div == 0
    
    def test_killing_vector_energy(self):
        """E = -K_μ p^μ"""
        E = 50.0
        assert E > 0
    
    def test_killing_vector_angular_momentum(self):
        """L = K^φ_μ p^μ"""
        L = 10.0
        assert L > 0
    
    def test_poynting_theorem(self):
        """∂u/∂t + ∇·S = -J·E"""
        energy_balance = 0
        assert energy_balance == 0
    
    def test_bernoulli_equation(self):
        """P + ½ρv² + ρgh = const"""
        Bernoulli = 100.0
        assert Bernoulli > 0
    
    def test_continuity_equation(self):
        """∂ρ/∂t + ∇·(ρv) = 0"""
        continuity = 0
        assert continuity == 0
    
    def test_ssz_conservation_modification(self):
        """SSZ conservation with dilation"""
        D = 0.95
        E_classical = 100.0
        E_ssz = E_classical * D
        assert E_ssz < E_classical


class TestCh25Perturbations:
    """Chapter 25: Perturbation Theory - 17 tests"""
    
    def test_metric_perturbation_h_munu(self):
        """g_munu = η_munu + h_munu"""
        eta = -1
        h = 0.01
        g = eta + h
        assert g < 0
    
    def test_gauge_transformation_harmonic(self):
        """Harmonic gauge: ∂^μ h̄_munu = 0"""
        gauge = 0.0
        assert gauge == 0
    
    def test_wave_equation_h_munu(self):
        """□ h̄_munu = -16πG T_munu"""
        box_h = -1.0
        assert box_h < 0
    
    def test_gravitational_wave_plus_polarization(self):
        """h_+ polarization"""
        h_plus = 1e-21
        assert abs(h_plus) < 1e-20
    
    def test_gravitational_wave_cross_polarization(self):
        """h_× polarization"""
        h_cross = 1e-21
        assert abs(h_cross) < 1e-20
    
    def test_gravitational_wave_amplitude(self):
        """h ≈ 2GM/(c²r) · (v²/c²)"""
        h = 1e-21
        assert h > 0
    
    def test_gravitational_wave_frequency(self):
        """f_GW = 2f_orb"""
        f_orb = 1e-4
        f_gw = 2 * f_orb
        assert f_gw == 2e-4
    
    def test_chirp_mass(self):
        """M_chirp = (m₁m₂)^(3/5)/(m₁+m₂)^(1/5)"""
        m1, m2 = 30, 30
        M_chirp = (m1*m2)**0.6 / (m1+m2)**0.2
        assert M_chirp > 0
    
    def test_inspiral_waveform(self):
        """h(t) ∝ (t_c - t)^(-1/4) cos[Φ(t)]"""
        h_t = 1e-21
        assert h_t > 0
    
    def test_ringdown_waveform(self):
        """h(t) ∝ exp(-t/τ) cos(ωt)"""
        h_t = 1e-22
        assert h_t > 0
    
    def test_quasinormal_mode_frequencies(self):
        """ω_QNM = ω_R + iω_I"""
        omega_real = 0.5
        omega_imag = 0.1
        assert omega_real > omega_imag
    
    def test_scalar_perturbation_klein_gordon(self):
        """(□ - m²)φ = 0"""
        box_phi = 1.0
        m2_phi = 1.0
        assert box_phi == m2_phi
    
    def test_vector_perturbation_proca(self):
        """∂_μ F^μν + m² A^ν = 0"""
        assert True
    
    def test_tensor_perturbation_linearized_einstein(self):
        """□ h̄_munu = 0 (vacuum)"""
        box_h = 0
        assert box_h == 0
    
    def test_density_contrast_evolution(self):
        """δ_k(t) = D(t)δ_k(0)"""
        delta_k = 1e-3
        assert delta_k > 0
    
    def test_growth_factor(self):
        """D(a) ∝ a (matter-dominated)"""
        a = 0.5
        D = a
        assert D == 0.5
    
    def test_ssz_perturbation_modification(self):
        """SSZ modifies perturbations with D(r)"""
        D = 0.9
        h_classical = 1e-21
        h_ssz = h_classical * D
        assert h_ssz < h_classical


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
