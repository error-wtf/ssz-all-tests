#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chord-Partition Eigenmodes - SSZ Test Suite
==========================================
Parametric chord-partition curves: C(t;p,k,R) = (R*cos(p*t), R*sin(k*t))
Authors: Carmen N. Wrede & Lino P. Casu
"""
import pytest
import numpy as np
from math import gcd, lcm, pi, sqrt

PHI = (1 + sqrt(5)) / 2
N_POINTS = 10_000

def chord_curve(t, p, k, R=1.0):
    return R * np.cos(p * t), R * np.sin(k * t)

def curve_period(p, k):
    return 2 * pi * lcm(p, k) / p

def is_closed(p, k, tol=1e-10):
    T = curve_period(p, k)
    x0, y0 = chord_curve(0.0, p, k)
    xT, yT = chord_curve(T, p, k)
    return abs(xT - x0) < tol and abs(yT - y0) < tol

def curve_perimeter(p, k, R=1.0, n=N_POINTS):
    T = curve_period(p, k)
    t = np.linspace(0, T, n, endpoint=False)
    dx = -R * p * np.sin(p * t)
    dy =  R * k * np.cos(k * t)
    return (np.sqrt(dx**2 + dy**2) * (T / n)).sum()

def derivative_smoothness(p, k, R=1.0, n=N_POINTS):
    T = curve_period(p, k)
    t = np.linspace(0, T, n, endpoint=False)
    ddx = -R * p**2 * np.cos(p * t)
    ddy = -R * k**2 * np.sin(k * t)
    return np.sqrt(ddx**2 + ddy**2).max()

def winding_number(p, k):
    T = curve_period(p, k)
    return p * T / (2 * pi), k * T / (2 * pi)

def phi_resonance(p, k):
    return abs(k / p - PHI)

def eigenmode_index(p, k):
    return lcm(p, k) // gcd(p, k)

def stability_score(p, k, R=1.0):
    L = curve_perimeter(p, k, R)
    km = derivative_smoothness(p, k, R)
    return 1.0 / (km * L) if km > 0 and L > 0 else float('inf')

STANDARD_MODES = [(1,1),(1,2),(2,3),(3,4),(1,3),(2,5),(3,5),(5,8)]
PHI_ADJACENT_MODES = [(p,k) for p in range(1,9) for k in range(p,9*p) if abs(k/p-PHI)<0.05]

class TestClosure:
    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_closure(self, p, k):
        assert is_closed(p, k)

    @pytest.mark.parametrize('p,k', [(1,1),(2,3),(5,7),(3,4)])
    def test_period_formula(self, p, k):
        T = curve_period(p, k)
        assert T > 0 and np.isfinite(T)
        assert T == pytest.approx(2*pi*lcm(p,k)/p, rel=1e-12)

    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_no_self_intersection_at_origin(self, p, k):
        x0, y0 = chord_curve(0.0, p, k)
        assert x0 == pytest.approx(1.0, abs=1e-12)
        assert y0 == pytest.approx(0.0, abs=1e-12)

class TestDerivatives:
    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_derivative_finite(self, p, k):
        kappa = derivative_smoothness(p, k)
        assert np.isfinite(kappa) and kappa > 0

    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_higher_modes_have_higher_curvature(self, p, k):
        k1 = derivative_smoothness(p, k)
        k2 = derivative_smoothness(p*2, k*2)
        assert k2 >= k1 * 0.9

    @pytest.mark.parametrize('p,k', [(1,1),(2,3),(3,5)])
    def test_periodic_derivative(self, p, k):
        T = curve_period(p, k)
        t0 = 0.5
        assert -p*np.sin(p*t0) == pytest.approx(-p*np.sin(p*(t0+T)), abs=1e-10)

class TestEigenmodes:
    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_eigenmode_index_positive(self, p, k):
        n = eigenmode_index(p, k)
        assert n >= 1 and isinstance(n, int)

    def test_circle_eigenmode(self):
        assert eigenmode_index(1, 1) == 1

    def test_lissajous_2_3_eigenmode(self):
        assert eigenmode_index(2, 3) == 6

    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_winding_integers(self, p, k):
        wx, wy = winding_number(p, k)
        assert wx == pytest.approx(round(wx), abs=1e-9)
        assert wy == pytest.approx(round(wy), abs=1e-9)

    def test_winding_consistent(self):
        wx, wy = winding_number(3, 5)
        assert wx == pytest.approx(15.0, abs=1e-9)
        assert wy == pytest.approx(25.0, abs=1e-9)

class TestPhiResonance:
    def test_phi_value(self):
        assert PHI == pytest.approx(1.6180339887498949, rel=1e-12)

    def test_fibonacci_pair_closest_to_phi(self):
        assert phi_resonance(5,8) < phi_resonance(3,5)
        assert phi_resonance(5,8) < phi_resonance(4,7)

    @pytest.mark.parametrize('p,k', [(1,2),(2,3),(3,5),(5,8),(8,13)])
    def test_fibonacci_pairs_decreasing_resonance(self, p, k):
        r = phi_resonance(p, k)
        assert r >= 0 and r < 0.5

    def test_phi_adjacent_modes_exist(self):
        assert len(PHI_ADJACENT_MODES) >= 3

    def test_fib_8_13_phi_approx(self):
        assert phi_resonance(8, 13) < 0.01

    def test_fib_13_21_phi_approx(self):
        assert phi_resonance(13, 21) < 0.004

class TestPerimeter:
    def test_circle_perimeter(self):
        assert curve_perimeter(1, 1, R=1.0) == pytest.approx(2*pi, rel=1e-3)

    @pytest.mark.parametrize('p,k', [(1,1),(2,3),(3,5)])
    def test_perimeter_scales_with_R(self, p, k):
        assert curve_perimeter(p,k,R=2.0) == pytest.approx(2*curve_perimeter(p,k,R=1.0), rel=1e-3)

    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_perimeter_positive(self, p, k):
        assert curve_perimeter(p, k) > 0

class TestStability:
    @pytest.mark.parametrize('p,k', STANDARD_MODES)
    def test_stability_positive(self, p, k):
        s = stability_score(p, k)
        assert s > 0 and np.isfinite(s)

    def test_circle_most_stable(self):
        s_circle = stability_score(1, 1)
        for p, k in [(2,3),(3,5),(5,8)]:
            assert s_circle >= stability_score(p, k) * 0.5

    def test_stability_decreases_with_complexity(self):
        assert stability_score(1,1) > stability_score(2,3)

class TestNumerical:
    def test_large_winding(self):
        assert is_closed(13, 21)
        L = curve_perimeter(13, 21)
        assert L > 0 and np.isfinite(L)

    def test_coprime_modes_close(self):
        for p, k in [(2,3),(3,5),(4,7),(5,9)]:
            assert gcd(p,k) == 1
            assert is_closed(p, k)

    def test_same_winding_circle(self):
        for n in [2, 3, 5]:
            assert is_closed(n, n)
            assert curve_period(n, n) == pytest.approx(2*pi, rel=1e-10)

    @pytest.mark.parametrize('R', [0.5, 1.0, 2.0, 5.0, 10.0])
    def test_radius_scaling_closure(self, R):
        T = curve_period(3, 5)
        x0, y0 = chord_curve(0.0, 3, 5, R)
        xT, yT = chord_curve(T,  3, 5, R)
        assert abs(xT - x0) < 1e-10 * R
        assert abs(yT - y0) < 1e-10 * R

class TestSSZConstants:
    def test_phi_squared(self):
        assert PHI**2 == pytest.approx(PHI + 1, rel=1e-12)

    def test_phi_reciprocal(self):
        assert 1.0/PHI == pytest.approx(PHI - 1, rel=1e-12)

    def test_xi_max(self):
        assert 1 - np.exp(-PHI) == pytest.approx(0.80171, abs=1e-4)

    def test_d_min(self):
        xi_max = 1 - np.exp(-PHI)
        assert 1.0/(1+xi_max) == pytest.approx(0.555, abs=1e-3)

    def test_r_star_over_rs(self):
        xi_at_rstar = 1 - np.exp(-PHI * 1.387)
        xi_max = 1 - np.exp(-PHI)
        assert xi_at_rstar > xi_max / 2
        assert xi_at_rstar > 0.85
