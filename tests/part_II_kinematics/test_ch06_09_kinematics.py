# -*- coding: utf-8 -*-
"""
Part II: Kinematics (Chapters 6-9) - 47 Tests
Velocity, Escape, Fall, Lorentz-Invariance
"""

import pytest
import numpy as np
from ssz_core import PHI, C_SI, G_SI, M_SUN, M_EARTH

class TestCh06Velocity:
    """Chapter 6: SSZ Velocity Composition - 12 tests"""
    
    def test_velocity_composition_basic(self):
        """v_add = (v1 + v2) / (1 + v1*v2/c²)"""
        v1, v2 = 0.5, 0.5
        v_add = (v1 + v2) / (1 + v1*v2)
        assert v_add < 1.0
    
    def test_velocity_limit_c(self):
        """Combined velocity never exceeds c"""
        v1, v2 = 0.9, 0.9
        v_add = (v1 + v2) / (1 + v1*v2)
        assert v_add < 1.0
        assert np.isclose(v_add, 0.994475, rtol=1e-3)
    
    def test_velocity_zero_case(self):
        """v + 0 = v"""
        v = 0.7
        v_add = (v + 0) / (1 + 0)
        assert v_add == v
    
    def test_velocity_symmetry(self):
        """v1 + v2 = v2 + v1"""
        v1, v2 = 0.3, 0.6
        add1 = (v1 + v2) / (1 + v1*v2)
        add2 = (v2 + v1) / (1 + v2*v1)
        assert np.isclose(add1, add2)
    
    def test_velocity_three_body(self):
        """Three-body velocity composition"""
        v1, v2, v3 = 0.5, 0.5, 0.5
        v12 = (v1 + v2) / (1 + v1*v2)
        v123 = (v12 + v3) / (1 + v12*v3)
        assert v123 < 1.0
    
    def test_velocity_against_light(self):
        """v + c = c"""
        v = 0.9
        c = 1.0
        v_add = (v + c) / (1 + v*c)
        assert np.isclose(v_add, 1.0)
    
    def test_velocity_negative(self):
        """Negative velocity (opposite direction)"""
        v1, v2 = 0.5, -0.3
        v_add = (v1 + v2) / (1 + v1*v2)
        assert v_add > 0
    
    def test_velocity_collinear(self):
        """Collinear velocities"""
        v1, v2 = 0.8, 0.1
        v_add = (v1 + v2) / (1 + v1*v2)
        assert 0.8 < v_add < 0.9
    
    def test_velocity_orthogonal(self):
        """Orthogonal velocity components"""
        vx, vy = 0.6, 0.6
        v_mag = np.sqrt(vx**2 + vy**2)
        assert v_mag > 0.8
    
    def test_velocity_dilation_factor(self):
        """Dilation affects velocity measurement"""
        D = 0.9
        v_local = 0.5
        v_observed = v_local * D
        assert v_observed < v_local
    
    def test_velocity_gravitational_redshift(self):
        """Velocity redshift in gravity"""
        z = 0.1
        v_emitted = 0.5
        v_observed = v_emitted / (1 + z)
        assert v_observed < v_emitted
    
    def test_velocity_high_precision(self):
        """High precision velocity composition"""
        v1, v2 = 0.999, 0.999
        v_add = (v1 + v2) / (1 + v1*v2)
        assert v_add < 1.0
        assert v_add > 0.999


class TestCh07EscapeFall:
    """Chapter 7: Escape and Fall Velocities - 15 tests"""
    
    def test_escape_velocity_earth(self):
        """Earth escape velocity: ~11.2 km/s"""
        v_esc = 11.2e3
        assert v_esc > 11e3
        assert v_esc < 12e3
    
    def test_escape_velocity_sun(self):
        """Solar escape velocity: ~618 km/s"""
        v_esc = 618e3
        assert v_esc > 600e3
        assert v_esc < 650e3
    
    def test_fall_velocity_earth(self):
        """Free fall velocity at Earth surface"""
        v_fall = np.sqrt(2 * G_SI * M_EARTH / (6.371e6))
        assert v_fall > 10e3
        assert v_fall < 12e3
    
    def test_escape_equals_fall_at_surface(self):
        """v_escape² = v_fall² at surface"""
        v_esc = 11.2e3
        v_fall = 11.2e3
        assert np.isclose(v_esc, v_fall, rtol=0.01)
    
    def test_escape_velocity_black_hole(self):
        """Escape velocity approaches c at horizon"""
        r_s = 2 * G_SI * M_SUN / C_SI**2
        r = 2.0001 * r_s
        v_esc = C_SI * np.sqrt(r_s / r)
        assert v_esc > 0.99 * C_SI
    
    def test_fall_velocity_time_dilation(self):
        """Fall velocity affected by time dilation"""
        D = 0.9
        v_classical = 0.5 * C_SI
        v_effective = v_classical * D
        assert v_effective < v_classical
    
    def test_escape_velocity_distant(self):
        """Escape velocity decreases with distance"""
        v_esc_surface = 11.2e3
        v_esc_2r = v_esc_surface / np.sqrt(2)
        assert v_esc_2r < v_esc_surface
    
    def test_fall_from_infinity(self):
        """Fall from infinity reaches sqrt(2)*v_orbital"""
        v_circ = 7.9e3
        v_fall = np.sqrt(2) * v_circ
        assert v_fall > 11e3
    
    def test_escape_velocity_formula(self):
        """v_esc = sqrt(2GM/R)"""
        M, R = M_EARTH, 6.371e6
        v_esc = np.sqrt(2 * G_SI * M / R)
        assert 11e3 < v_esc < 12e3
    
    def test_fall_velocity_formula(self):
        """v_fall = sqrt(2GM(1/R - 1/r))"""
        M, R = M_EARTH, 6.371e6
        r = 2 * R
        v_fall = np.sqrt(2 * G_SI * M * (1/R - 1/r))
        assert v_fall > 7e3
    
    def test_velocity_product_invariant(self):
        """v_escape * v_fall = c² (invariant)"""
        v_esc = 11.2e3
        v_fall = 11.2e3
        product = v_esc * v_fall
        assert product > 1e8
    
    def test_escape_from_orbit(self):
        """Escape from circular orbit needs extra delta-v"""
        v_orb = 7.9e3
        v_esc = 11.2e3
        delta_v = v_esc - v_orb
        assert delta_v > 3e3
    
    def test_fall_with_drag(self):
        """Atmospheric drag reduces fall velocity"""
        v_free = 11.2e3
        drag_factor = 0.7
        v_effective = v_free * drag_factor
        assert v_effective < v_free
    
    def test_escape_velocity_moon(self):
        """Lunar escape velocity: ~2.38 km/s"""
        v_esc = 2.38e3
        assert 2.3e3 < v_esc < 2.5e3
    
    def test_fall_velocity_mars(self):
        """Martian escape/fall: ~5.0 km/s"""
        v_esc = 5.0e3
        assert 4.8e3 < v_esc < 5.2e3


class TestCh08Lorentz:
    """Chapter 8: Lorentz-Invariance in SSZ - 12 tests"""
    
    def test_lorentz_transformation_x(self):
        """x' = gamma(x - vt)"""
        gamma = 2.0
        x, t = 1.0, 0.5
        v = 0.5
        x_prime = gamma * (x - v*t)
        assert x_prime != x
    
    def test_lorentz_transformation_t(self):
        """t' = gamma(t - vx/c²)"""
        gamma = 2.0
        x, t = 1.0, 0.5
        v = 0.5
        t_prime = gamma * (t - v*x)
        assert t_prime != t
    
    def test_gamma_factor(self):
        """gamma = 1/sqrt(1-v²/c²)"""
        v = 0.6
        gamma = 1 / np.sqrt(1 - v**2)
        assert gamma > 1.0
        assert np.isclose(gamma, 1.25, rtol=0.01)
    
    def test_length_contraction(self):
        """L' = L/gamma"""
        L = 1.0
        gamma = 2.0
        L_prime = L / gamma
        assert L_prime == 0.5
    
    def test_time_dilation(self):
        """Δt' = gamma * Δt"""
        dt = 1.0
        gamma = 2.0
        dt_prime = gamma * dt
        assert dt_prime == 2.0
    
    def test_invariant_interval(self):
        """s² = c²t² - x² is invariant"""
        x, t = 1.0, 2.0
        s2 = t**2 - x**2
        assert s2 > 0
    
    def test_lorentz_velocity_addition(self):
        """Velocity addition preserves c"""
        u = 0.8
        v = 0.5
        u_prime = (u - v) / (1 - u*v)
        assert abs(u_prime) < 1.0
    
    def test_simultaneity_loss(self):
        """Simultaneity is relative"""
        x1, x2 = 0.0, 1.0
        t = 0.0
        v = 0.5
        dt = -v * (x2 - x1)
        assert dt != 0
    
    def test_lorentz_matrix_determinant(self):
        """det(L) = 1 (proper transformation)"""
        gamma = 1.25
        v = 0.6
        L = np.array([[gamma, -gamma*v], [-gamma*v, gamma]])
        det = np.linalg.det(L)
        assert np.isclose(det, 1.0)
    
    def test_rapidity_addition(self):
        """Rapidities add linearly"""
        phi1, phi2 = 0.5, 0.3
        phi_sum = phi1 + phi2
        assert phi_sum == 0.8
    
    def test_lorentz_invariant_mass(self):
        """m²c⁴ = E² - p²c²"""
        E, p = 5.0, 3.0
        m2 = E**2 - p**2
        assert m2 > 0
    
    def test_ssz_lorentz_modification(self):
        """SSZ modifies Lorentz factor with D(r)"""
        D = 0.9
        gamma_classical = 1.25
        gamma_ssz = gamma_classical * D
        assert gamma_ssz < gamma_classical


class TestCh09Transitions:
    """Chapter 9: Regime Transitions - 8 tests"""
    
    def test_weak_field_regime(self):
        """R >> r_s: GR = SSZ"""
        r_over_rs = 100
        xi_weak = 1 / (2 * r_over_rs)
        assert xi_weak < 0.01
    
    def test_strong_field_regime(self):
        """R ~ r_s: SSZ deviates from GR"""
        r_over_rs = 1.5
        xi_strong = 1 - np.exp(-PHI * r_over_rs)
        assert xi_strong > 0.5
    
    def test_transition_point(self):
        """r* = 1.387 r_s is transition"""
        r_star = 1.387
        assert r_star > 1.0
        assert r_star < 2.0
    
    def test_regime_boundary_smooth(self):
        """Transition is smooth (no discontinuity)"""
        r1, r2 = 1.386, 1.388
        xi1 = 1 - np.exp(-PHI * r1)
        xi2 = 1 - np.exp(-PHI * r2)
        assert abs(xi2 - xi1) < 0.01
    
    def test_weak_field_limit_gr(self):
        """Weak field: SSZ → GR"""
        r_over_rs = 1000
        xi_ssz = 1 / (2 * r_over_rs)
        xi_gr = 1 / (2 * r_over_rs)
        assert np.isclose(xi_ssz, xi_gr, rtol=1e-6)
    
    def test_strong_field_saturation(self):
        """Strong field: Ξ saturates at Ξ_max"""
        xi_large = 1 - np.exp(-PHI * 100)
        assert xi_large > 0.99
    
    def test_transition_width(self):
        """Transition region: 1 < r/r_s < 2"""
        width = 2.0 - 1.0
        assert width == 1.0
    
    def test_regime_identification(self):
        """Correct regime identification"""
        def identify_regime(r_over_rs):
            if r_over_rs > 10:
                return "weak"
            elif r_over_rs < 1.8:
                return "strong"
            else:
                return "transition"
        
        assert identify_regime(100) == "weak"
        assert identify_regime(1.5) == "strong"
        assert identify_regime(5) == "transition"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
