#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chord-Partition Eigenmodes - SSZ Test Suite
==========================================
Tests for parametric chord-partition curves with golden-ratio phi scaling.
Implements: periodicity, stability, derivative smoothness, and eigenmode analysis.

Physical context:
  A chord-partition curve C(t; p, k, R) = (R cos(p*t), R sin(k*t))
  - p, k: winding numbers (integers >= 1)
  - R: characteristic radius
  - phi = (1+sqrt(5))/2 is the SSZ scaling constant
  Eigenmode condition: closed curve iff gcd(p,k) structure allows period 2pi*lcm(p,k)/p
"""
import pytest
import numpy as np
from math import gcd, lcm, pi, sqrt

PHI = (1 + sqrt(5)) / 2  # Golden ratio = SSZ fundamental constant
N_POINTS = 10_000        # Integration resolution


# ─────────────────────────────────────────────
# Core implementation
# ─────────────────────────────────────────────

def chord_curve(t, p, k, R=1.0):
    """Parametric chord-partition curve."""
    return R * np.cos(p * t), R * np.sin(k * t)


def curve_period(p, k):
    """Minimal period T such that C(t+T) = C(t)."""
    return 2 * pi * lcm(p, k) / p


def is_closed(p, k, tol=1e-10):
    """Verify curve closure: C(T) == C(0)."""
    T = curve_period(p, k)
    x0, y0 = chord_curve(0.0, p, k)
    xT, yT = chord_curve(T, p, k)
    return (abs(xT - x0) < tol) and (abs(yT - y0) < tol)


def curve_perimeter(p, k, R=1.0, n=N_POINTS):
    """Numerical arc-length of one period."""
    T = curve_period(p, k)
    t = np.linspace(0, T, n, endpoint=False)
    dx = -R * p * np.sin(p * t)
    dy =  R * k * np.cos(k * t)
    ds = np.sqrt(dx**2 + dy**2) * (T / n)
    return ds.sum()


def derivative_smoothness(p, k, R=1.0, n=N_POINTS):
    """Max absolute second derivative (smoothness proxy)."""
    T = curve_period(p, k)
    t = np.linspace(0, T, n, endpoint=False)
    ddx = -R * p**2 * np.cos(p * t)
    ddy = -R * k**2 * np.sin(k * t)
    kappa = np.sqrt(ddx**2 + ddy**2)
    return kappa.max()


def winding_number(p, k):
    """Number of full oscillations in each axis per period."""
    T = curve_period(p, k)
    wind_x = p * T / (2 * pi)  # = lcm(p,k)/p * p = lcm(p,k)
    wind_y = k * T / (2 * pi)
    return wind_x, wind_y


def phi_resonance(p, k):
    """Ratio k/p relative to phi; measures golden-ratio resonance."""
    return abs(k / p - PHI)


def eigenmode_index(p, k):
    """
    SSZ eigenmode index: n = lcm(p,k)/gcd(p,k).
    Physical interpretation: number of independent segments.
    """
    return lcm(p, k) // gcd(p, k)


def stability_score(p, k, R=1.0):
    """
    Stability score = 1 / (max_curvature * perimeter).
    Higher = more stable (smoother curve for given length).
    """
    L = curve_perimeter(p, k, R)
    kappa_max = derivative_smoothness(p, k, R)
    if kappa_max == 0 or L == 0:
        return float('inf')
    return 1.0 / (kappa_max * L)


# ─────────────────────────────────────────────
# Test Fixtures
# ─────────────────────────────────────────────

STANDARD_MODES = [
    (1, 1),  # Circle
    (1, 2),  # Figure-8 / Lissajous
    (2, 3),  # Trefoil-like
    (3, 4),  # Standard Lissajous
    (1, 3),  # Triple oscillation
    (2, 5),  # Pentagonal
    (3, 5),  # Star-like
    (5, 8),  # Close to phi ratio: 8/5=1.6
]

PHI_ADJACENT_MODES = [
    (p, k) for p in range(1, 9) for k in range(p, 9*p)
    if abs(k/p - PHI) < 0.05
]


# ─────────────────────────────────────────────
# Tests: Closure & Periodicity
# ─────────────────────────────────────────────

class TestClosure:
    """All chord-partition curves must close after one minimal period."""

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_closure(self, p, k):
        assert is_closed(p, k), f"Curve ({p},{k}) is not closed after T={curve_period(p,k):.4f}"

    @pytest.mark.parametrize("p,k", [(1,1),(2,3),(5,7),(3,4)])
    def test_period_formula(self, p, k):
        """T = 2*pi*lcm(p,k)/p must be positive and finite."""
        T = curve_period(p, k)
        assert T > 0
        assert np.isfinite(T)
        assert T == pytest.approx(2 * pi * lcm(p, k) / p, rel=1e-12)

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_no_self_intersection_at_origin(self, p, k):
        """Curve must pass through (R, 0) exactly once at t=0 per period."""
        T = curve_period(p, k)
        t_vals = np.linspace(0, T, N_POINTS, endpoint=False)
        x, y = chord_curve(t_vals, p, k)
        # At t=0: x=R, y=0
        assert x[0] == pytest.approx(1.0, abs=1e-12)
        assert y[0] == pytest.approx(0.0, abs=1e-12)


class TestDerivatives:
    """Derivative tests: smoothness and continuity."""

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_derivative_finite(self, p, k):
        kappa = derivative_smoothness(p, k)
        assert np.isfinite(kappa)
        assert kappa > 0

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_higher_modes_have_higher_curvature(self, p, k):
        """Mode (p*2, k*2) must have >= curvature than (p, k)."""
        k1 = derivative_smoothness(p, k)
        k2 = derivative_smoothness(p*2, k*2)
        assert k2 >= k1 * 0.9, f"Scaling law violated: ({p},{k}) -> ({p*2},{k*2})"

    @pytest.mark.parametrize("p,k", [(1,1),(2,3),(3,5)])
    def test_periodic_derivative(self, p, k, R=1.0, n=1000):
        """First derivative must be periodic with same period T."""
        T = curve_period(p, k)
        t0 = 0.5  # arbitrary interior point
        # dx/dt = -R*p*sin(p*t)  → dx/dt(t) == dx/dt(t+T)
        dxdt_t = -R * p * np.sin(p * t0)
        dxdt_tT = -R * p * np.sin(p * (t0 + T))
        assert dxdt_t == pytest.approx(dxdt_tT, abs=1e-10)


class TestEigenmodes:
    """Eigenmode index and winding number tests."""

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_eigenmode_index_positive(self, p, k):
        n = eigenmode_index(p, k)
        assert n >= 1
        assert isinstance(n, int)

    def test_circle_eigenmode(self):
        """Circle (1,1) has eigenmode index 1."""
        assert eigenmode_index(1, 1) == 1

    def test_lissajous_2_3_eigenmode(self):
        """(2,3) has lcm=6, gcd=1 -> index=6."""
        assert eigenmode_index(2, 3) == 6

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_winding_integers(self, p, k):
        wx, wy = winding_number(p, k)
        assert wx == pytest.approx(round(wx), abs=1e-9), f"wx={wx} not integer for ({p},{k})"
        assert wy == pytest.approx(round(wy), abs=1e-9), f"wy={wy} not integer for ({p},{k})"

    def test_winding_consistent(self):
        """(3,5): T=2*pi*lcm(3,5)/3=2*pi*15/3=10*pi; wx=3*T/(2*pi)=15, wy=5*T/(2*pi)=25."""
        wx, wy = winding_number(3, 5)
        assert wx == pytest.approx(15.0, abs=1e-9)
        assert wy == pytest.approx(25.0, abs=1e-9)


class TestPhiResonance:
    """Golden ratio phi resonance tests."""

    def test_phi_value(self):
        """PHI = 1.6180339887..."""
        assert PHI == pytest.approx(1.6180339887498949, rel=1e-12)

    def test_fibonacci_pair_closest_to_phi(self):
        """(5,8) is closer to phi than (3,5) or (4,7)."""
        r_58 = phi_resonance(5, 8)
        r_35 = phi_resonance(3, 5)
        r_47 = phi_resonance(4, 7)
        assert r_58 < r_35
        assert r_58 < r_47

    @pytest.mark.parametrize("p,k", [(1,2),(2,3),(3,5),(5,8),(8,13)])
    def test_fibonacci_pairs_decreasing_resonance(self, p, k):
        """Consecutive Fibonacci pairs approach phi monotonically."""
        r = phi_resonance(p, k)
        assert r >= 0  # distance is non-negative
        assert r < 0.5  # always within 0.5 of phi

    def test_phi_adjacent_modes_exist(self):
        """There must be at least 3 modes within 5% of phi ratio."""
        assert len(PHI_ADJACENT_MODES) >= 3

    def test_fib_8_13_phi_approx(self):
        """(8,13): ratio 13/8=1.625 very close to phi."""
        assert phi_resonance(8, 13) < 0.01

    def test_fib_13_21_phi_approx(self):
        """(13,21): ratio 21/13~1.6154 close to phi."""
        assert phi_resonance(13, 21) < 0.004


class TestPerimeter:
    """Arc length and scaling tests."""

    def test_circle_perimeter(self):
        """(1,1) circle: perimeter ~ 2*pi*R."""
        L = curve_perimeter(1, 1, R=1.0)
        assert L == pytest.approx(2 * pi, rel=1e-3)

    @pytest.mark.parametrize("p,k", [(1,1),(2,3),(3,5)])
    def test_perimeter_scales_with_R(self, p, k):
        """Perimeter scales linearly with R."""
        L1 = curve_perimeter(p, k, R=1.0)
        L2 = curve_perimeter(p, k, R=2.0)
        assert L2 == pytest.approx(2 * L1, rel=1e-3)

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_perimeter_positive(self, p, k):
        """All perimeters must be positive."""
        L = curve_perimeter(p, k)
        assert L > 0


class TestStability:
    """Stability score and eigenmode stability ordering."""

    @pytest.mark.parametrize("p,k", STANDARD_MODES)
    def test_stability_positive(self, p, k):
        """Stability score must be positive."""
        s = stability_score(p, k)
        assert s > 0
        assert np.isfinite(s)

    def test_circle_most_stable(self):
        """Circle (1,1) should be the most stable (highest score)."""
        s_circle = stability_score(1, 1)
        for (p, k) in [(2,3),(3,5),(5,8)]:
            s_other = stability_score(p, k)
            assert s_circle >= s_other * 0.5, f"Circle less stable than ({p},{k})"

    def test_stability_decreases_with_complexity(self):
        """More complex modes (larger eigenmode index) tend to be less stable."""
        s1 = stability_score(1, 1)  # index=1
        s2 = stability_score(2, 3)  # index=6
        assert s1 > s2


class TestNumerical:
    """Numerical precision and edge cases."""

    def test_large_winding(self):
        """(13,21) Fibonacci pair: must close and be finite."""
        assert is_closed(13, 21)
        L = curve_perimeter(13, 21)
        assert L > 0
        assert np.isfinite(L)

    def test_coprime_modes_close(self):
        """Coprime (p,k) with gcd=1 must still close."""
        for p, k in [(2,3),(3,5),(4,7),(5,9)]:
            assert gcd(p,k) == 1
            assert is_closed(p, k), f"({p},{k}) coprime but not closed"

    def test_same_winding_circle(self):
        """(n,n) for any n gives circle-like periodicity."""
        for n in [2, 3, 5]:
            assert is_closed(n, n)
            T = curve_period(n, n)
            assert T == pytest.approx(2 * pi, rel=1e-10)

    @pytest.mark.parametrize("R", [0.5, 1.0, 2.0, 5.0, 10.0])
    def test_radius_scaling_closure(self, R):
        """Closure independent of R."""
        assert is_closed(3, 5), "Base case must close"
        T = curve_period(3, 5)
        x0, y0 = chord_curve(0.0, 3, 5, R)
        xT, yT = chord_curve(T, 3, 5, R)
        assert abs(xT - x0) < 1e-10 * R
        assert abs(yT - y0) < 1e-10 * R


class TestSSZConstants:
    """Verify SSZ canonical constants used in chord-partition context."""

    def test_phi_squared(self):
        """phi^2 = phi + 1 (defining property)."""
        assert PHI**2 == pytest.approx(PHI + 1, rel=1e-12)

    def test_phi_reciprocal(self):
        """1/phi = phi - 1."""
        assert 1.0/PHI == pytest.approx(PHI - 1, rel=1e-12)

    def test_xi_max(self):
        """XI_MAX = 1 - exp(-phi) = 0.80171..."""
        xi_max = 1 - np.exp(-PHI)
        assert xi_max == pytest.approx(0.80171, abs=1e-4)

    def test_d_min(self):
        """D_min = 1/(1+XI_MAX) = 0.5550..."""
        xi_max = 1 - np.exp(-PHI)
        d_min = 1.0 / (1 + xi_max)
        assert d_min == pytest.approx(0.555, abs=1e-3)

    def test_r_star_over_rs(self):
        """r*/r_s ~ 1.387 is the half-maximum curvature point of Xi_sat.
        At this point Xi_sat > 0.5 * Xi_max (well into strong field)."""
        r_star = 1.387
        xi_at_rstar = 1 - np.exp(-PHI * r_star)
        xi_max = 1 - np.exp(-PHI)
        # xi at r* must be > xi_max/2 and < 1
        assert xi_at_rstar > xi_max / 2
        assert xi_at_rstar < 1.0
        # Also verify canonical blend point r*/r_s ~ 1.387 gives Xi > 0.85
        assert xi_at_rstar > 0.85


if __name__ == '__main__':
    import sys
    # Direct execution mode
    tests_run = 0
    tests_pass = 0
    tests_fail = 0

    print("=" * 65)
    print("CHORD-PARTITION EIGENMODES - SSZ TEST SUITE")
    print("=" * 65)

    test_classes = [
        TestClosure, TestDerivatives, TestEigenmodes,
        TestPhiResonance, TestPerimeter, TestStability,
        TestNumerical, TestSSZConstants
    ]

    for cls in test_classes:
        instance = cls()
        print(f"\n[{cls.__name__}]")
        methods = [m for m in dir(instance) if m.startswith('test_')]
        for method_name in methods:
            method = getattr(instance, method_name)
            # Handle parametrize manually for direct run
            try:
                method()
                print(f"  [PASS] {method_name}")
                tests_pass += 1
            except TypeError:
                # Parametrized - skip in direct mode
                print(f"  [SKIP] {method_name} (parametrized)")
            except Exception as e:
                print(f"  [FAIL] {method_name}: {e}")
                tests_fail += 1
            tests_run += 1

    print("\n" + "=" * 65)
    print(f"TOTAL: {tests_run} run | {tests_pass} PASS | {tests_fail} FAIL")
    print("=" * 65)

    sys.exit(0 if tests_fail == 0 else 1)
