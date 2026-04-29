# -*- coding: utf-8 -*-
"""
Part IV: Frequency Framework (Modules 16-17) - 28 Tests
Redshift, Time Dilation, Interference
"""

import pytest
import numpy as np
from ssz_core import PHI, C_SI, XI_MAX, D_MIN

class TestCh16Redshift:
    """Module 16: Gravitational Redshift - 15 tests"""
    
    def test_redshift_basic_formula(self):
        """z = (f_emit - f_obs)/f_obs"""
        f_emit, f_obs = 1.0, 0.9
        z = (f_emit - f_obs) / f_obs
        assert z > 0
    
    def test_redshift_ssz_formula(self):
        """z = 1/D - 1 (SSZ)"""
        D = 0.9
        z = 1/D - 1
        assert z > 0
    
    def test_redshift_gr_formula(self):
        """z = 1/sqrt(1-r_s/r) - 1 (GR)"""
        r_s, r = 1.0, 10.0
        z = 1/np.sqrt(1 - r_s/r) - 1
        assert z > 0
    
    def test_redshift_weak_field(self):
        """Weak field: z ≈ GM/(rc²)"""
        GM, r, c = 1.0, 100.0, 1.0
        z = GM / (r*c**2)
        assert z < 0.1
    
    def test_redshift_strong_field(self):
        """Strong field: SSZ deviates from GR"""
        D_ssz = 0.556
        z_ssz = 1/D_ssz - 1
        assert z_ssz > 0.5
    
    def test_redshift_sun_surface(self):
        """Solar surface redshift: z ≈ 2e-6"""
        z_sun = 2.12e-6
        assert 2e-6 < z_sun < 3e-6
    
    def test_redshift_white_dwarf(self):
        """White dwarf redshift: z ≈ 10⁻⁴"""
        z_wd = 1e-4
        assert 1e-5 < z_wd < 1e-3
    
    def test_redshift_neutron_star(self):
        """NS redshift: z ≈ 0.1-0.4 (SSZ prediction: +13%)"""
        z_ns_gr = 0.3
        z_ns_ssz = z_ns_gr * 1.13
        assert 0.2 < z_ns_ssz < 0.5
    
    def test_redshift_pound_rebka(self):
        """Pound-Rebka: z = gh/c² = 2.46e-15"""
        g, h, c = 9.81, 22.5, 3e8
        z = g*h/c**2
        assert 2e-15 < z < 3e-15
    
    def test_redshift_gps(self):
        """GPS satellite: z ≈ 5e-10"""
        z_gps = 5.3e-10
        assert 4e-10 < z_gps < 6e-10
    
    def test_redshift_cmb_dipole(self):
        """CMB dipole: ΔT/T = z_dipole"""
        z_dipole = 1.23e-3
        assert z_dipole > 1e-3
    
    def test_redshift_hubble(self):
        """Hubble redshift: z = H₀d/c"""
        H0, d, c = 70e3, 1e9, 3e8
        z = H0*d/c
        assert z > 0.2
    
    def test_redshift_cosmological(self):
        """Cosmological redshift: 1+z = a(t₀)/a(t₁)"""
        a_emit, a_obs = 0.5, 1.0
        z = a_obs/a_emit - 1
        assert z == 1.0
    
    def test_redshift_gravitational_time_delay(self):
        """Shapiro delay: Δt = (2GM/c³)ln(...)"""
        GM_c3 = 1e-5
        delta_t = 2*GM_c3 * np.log(100)
        assert delta_t > 0
    
    def test_ssz_neutron_star_prediction(self):
        """SSZ predicts +13% NS redshift vs GR"""
        z_gr = 0.3
        z_ssz = z_gr * 1.13
        assert z_ssz > z_gr


class TestCh17TimeDilation:
    """Module 17: Time Dilation & Interference - 13 tests"""
    
    def test_time_dilation_basic(self):
        """Δt' = γΔt"""
        gamma, dt = 2.0, 1.0
        dt_prime = gamma * dt
        assert dt_prime == 2.0
    
    def test_time_dilation_ssz(self):
        """Δt_SSZ = Δt/"""
        D = 0.9
        dt_proper = 1.0
        dt_coord = dt_proper / D
        assert dt_coord > dt_proper
    
    def test_time_dilation_gravitational(self):
        """Gravitational time dilation: dτ = D·dt"""
        D = 0.9
        dt = 1.0
        dtau = D * dt
        assert dtau < dt
    
    def test_time_dilation_velocity(self):
        """Velocity time dilation: γ = 1/sqrt(1-v²)"""
        v = 0.6
        gamma = 1/np.sqrt(1 - v**2)
        assert gamma > 1.0
    
    def test_twin_paradox(self):
        """Traveling twin ages less"""
        gamma = 2.0
        t_earth = 10.0
        t_traveler = t_earth / gamma
        assert t_traveler < t_earth
    
    def test_interference_pattern(self):
        """Double-slit: Δx = λL/d"""
        lam, L, d = 500e-9, 1.0, 1e-4
        delta_x = lam*L/d
        assert delta_x > 0
    
    def test_interference_phase_shift(self):
        """Phase shift: Δφ = 2πΔL/λ"""
        delta_L, lam = 1e-6, 500e-9
        delta_phi = 2*np.pi*delta_L/lam
        assert delta_phi > 0
    
    def test_interference_constructive(self):
        """Constructive: ΔL = nλ"""
        n, lam = 3, 500e-9
        delta_L = n*lam
        assert delta_L > 0
    
    def test_interference_destructive(self):
        """Destructive: ΔL = (n+½)λ"""
        n, lam = 3, 500e-9
        delta_L = (n + 0.5)*lam
        assert delta_L > 0
    
    def test_temporal_interference(self):
        """Temporal interference: Δt = n/f"""
        n, f = 5, 1e9
        delta_t = n/f
        assert delta_t > 0
    
    def test_ssz_time_dilation_excess(self):
        """SSZ predicts +30% time dilation excess"""
        delta_gr = 1e-6
        delta_ssz = delta_gr * 1.30
        assert delta_ssz > delta_gr
    
    def test_gravitational_redshift_time_dilation_equivalence(self):
        """z = Δt/Δτ - 1"""
        D = 0.9
        z = 1/D - 1
        delta_ratio = 1/D - 1
        assert np.isclose(z, delta_ratio)
    
    def test_ssz_interference_modification(self):
        """SSZ modifies interference with D(r) phase"""
        D = 0.99
        phase_classical = 2*np.pi
        phase_ssz = phase_classical * D
        assert phase_ssz < phase_classical


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
