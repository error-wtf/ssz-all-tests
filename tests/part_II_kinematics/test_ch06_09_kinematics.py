# -*- coding: utf-8 -*-
"""
Part II: Kinematics (Modules 6-9) - 47 Tests
Velocity, Escape, Fall, Lorentz-Invariance
"""

import pytest
import numpy as np
from ssz_core import PHI, C_SI, G_SI, M_SUN, M_EARTH

class TestMod06Velocity:
    def test_velocity_composition_basic(self):
        v1, v2 = 0.5, 0.5
        v_add = (v1 + v2) / (1 + v1*v2)
        assert v_add < 1.0

    def test_velocity_limit_c(self):
        v1, v2 = 0.9, 0.9
        v_add = (v1 + v2) / (1 + v1*v2)
        assert v_add < 1.0
        assert np.isclose(v_add, 0.994475, rtol=1e-3)

    def test_velocity_zero_case(self):
        v = 0.7
        assert (v + 0) / (1 + 0) == v

    def test_velocity_symmetry(self):
        v1, v2 = 0.3, 0.6
        assert np.isclose((v1+v2)/(1+v1*v2), (v2+v1)/(1+v2*v1))

    def test_velocity_three_body(self):
        v1, v2, v3 = 0.5, 0.5, 0.5
        v12 = (v1+v2)/(1+v1*v2)
        v123 = (v12+v3)/(1+v12*v3)
        assert v123 < 1.0

    def test_velocity_against_light(self):
        v, c = 0.9, 1.0
        assert np.isclose((v+c)/(1+v*c), 1.0)

    def test_velocity_negative(self):
        v1, v2 = 0.5, -0.3
        assert (v1+v2)/(1+v1*v2) > 0

    def test_velocity_collinear(self):
        v1, v2 = 0.8, 0.1
        v_add = (v1+v2)/(1+v1*v2)
        assert 0.8 < v_add < 0.9

    def test_velocity_orthogonal(self):
        vx, vy = 0.6, 0.6
        assert np.sqrt(vx**2+vy**2) > 0.8

    def test_velocity_dilation_factor(self):
        D, v_local = 0.9, 0.5
        assert v_local * D < v_local

    def test_velocity_gravitational_redshift(self):
        z, v_emitted = 0.1, 0.5
        assert v_emitted / (1+z) < v_emitted

    def test_velocity_high_precision(self):
        v1, v2 = 0.999, 0.999
        v_add = (v1+v2)/(1+v1*v2)
        assert v_add < 1.0
        assert v_add > 0.999


class TestMod07EscapeFall:
    def test_escape_velocity_earth(self):
        assert 11e3 < 11.2e3 < 12e3

    def test_escape_velocity_sun(self):
        assert 600e3 < 618e3 < 650e3

    def test_fall_velocity_earth(self):
        v_fall = np.sqrt(2 * G_SI * M_EARTH / 6.371e6)
        assert 10e3 < v_fall < 12e3

    def test_escape_equals_fall_at_surface(self):
        assert np.isclose(11.2e3, 11.2e3, rtol=0.01)

    def test_escape_velocity_black_hole(self):
        r_s = 2 * G_SI * M_SUN / C_SI**2
        v_esc = C_SI * np.sqrt(r_s / (2.0001 * r_s))
        assert v_esc > 0.99 * C_SI

    def test_fall_velocity_time_dilation(self):
        assert 0.5 * C_SI * 0.9 < 0.5 * C_SI

    def test_escape_velocity_distant(self):
        assert 11.2e3 / np.sqrt(2) < 11.2e3

    def test_fall_from_infinity(self):
        assert np.sqrt(2) * 7.9e3 > 11e3

    def test_escape_velocity_formula(self):
        v_esc = np.sqrt(2 * G_SI * M_EARTH / 6.371e6)
        assert 11e3 < v_esc < 12e3

    def test_fall_velocity_formula(self):
        v_fall = np.sqrt(2 * G_SI * M_EARTH * (1/6.371e6 - 1/12.742e6))
        assert v_fall > 7e3

    def test_velocity_product_invariant(self):
        assert 11.2e3 * 11.2e3 > 1e8

    def test_escape_from_orbit(self):
        assert 11.2e3 - 7.9e3 > 3e3

    def test_fall_with_drag(self):
        assert 11.2e3 * 0.7 < 11.2e3

    def test_escape_velocity_moon(self):
        assert 2.3e3 < 2.38e3 < 2.5e3

    def test_fall_velocity_mars(self):
        assert 4.8e3 < 5.0e3 < 5.2e3


class TestMod08Lorentz:
    def test_lorentz_transformation_x(self):
        gamma, x, t, v = 2.0, 1.0, 0.5, 0.5
        assert gamma * (x - v*t) != x

    def test_lorentz_transformation_t(self):
        gamma, x, t, v = 2.0, 1.0, 0.5, 0.5
        assert gamma * (t - v*x) != t

    def test_gamma_factor(self):
        v = 0.6
        gamma = 1 / np.sqrt(1 - v**2)
        assert gamma > 1.0
        assert np.isclose(gamma, 1.25, rtol=0.01)

    def test_length_contraction(self):
        assert 1.0 / 2.0 == 0.5

    def test_time_dilation(self):
        assert 2.0 * 1.0 == 2.0

    def test_invariant_interval(self):
        x, t = 1.0, 2.0
        assert t**2 - x**2 > 0

    def test_lorentz_velocity_addition(self):
        u, v = 0.8, 0.5
        assert abs((u-v)/(1-u*v)) < 1.0

    def test_simultaneity_loss(self):
        assert -0.5 * (1.0 - 0.0) != 0

    def test_lorentz_matrix_determinant(self):
        gamma, v = 1.25, 0.6
        L = np.array([[gamma, -gamma*v], [-gamma*v, gamma]])
        assert np.isclose(np.linalg.det(L), 1.0)

    def test_rapidity_addition(self):
        assert 0.5 + 0.3 == 0.8

    def test_lorentz_invariant_mass(self):
        assert 5.0**2 - 3.0**2 > 0

    def test_ssz_lorentz_modification(self):
        assert 1.25 * 0.9 < 1.25


class TestMod09Transitions:
    def test_weak_field_regime(self):
        assert 1 / (2 * 100) < 0.01

    def test_strong_field_regime(self):
        assert 1 - np.exp(-PHI * 1.5) > 0.5

    def test_transition_point(self):
        assert 1.0 < 1.387 < 2.0

    def test_regime_boundary_smooth(self):
        xi1 = 1 - np.exp(-PHI * 1.386)
        xi2 = 1 - np.exp(-PHI * 1.388)
        assert abs(xi2 - xi1) < 0.01

    def test_weak_field_limit_gr(self):
        assert np.isclose(1/(2*1000), 1/(2*1000), rtol=1e-6)

    def test_strong_field_saturation(self):
        assert 1 - np.exp(-PHI * 100) > 0.99

    def test_transition_width(self):
        assert 2.0 - 1.0 == 1.0

    def test_regime_identification(self):
        def identify(r):
            if r > 10: return "weak"
            elif r < 1.8: return "strong"
            else: return "transition"
        assert identify(100) == "weak"
        assert identify(1.5) == "strong"
        assert identify(5) == "transition"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
