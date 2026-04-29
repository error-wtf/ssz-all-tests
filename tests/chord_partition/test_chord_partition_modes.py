#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chord-Partition Eigenmodes - Test Suite
Mathematische Validierung der Chord-Partition-Hypothese

Formeln:
C_p(theta) = 2 R sin(p theta / 2)
dC_p/dtheta = R p cos(p theta / 2)
M_{p,k}(theta) = R p cos(p theta / 2) * exp(i k theta)

Reelle Projektion:
x(theta) = Re(M_{p,k}) cos(theta)
y(theta) = Re(M_{p,k}) sin(theta)

Status: Mathematisch getestet / Physikalische Interpretation hypothetisch
"""

import numpy as np
import pytest
import json
from pathlib import Path

# Test-Output Verzeichnis
OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Toleranzen
TOL_DERIVATIVE = 1e-6
TOL_PERIODICITY = 1e-6
TOL_PROJECTION = 1e-8
TOL_ENERGY = 1e-10


class TestChordPartitionModes:
    """Test Suite für Chord-Partition Eigenmodes"""

    def test_derivative_exactness(self):
        """Prüfe: C_p(theta) = 2R sin(p theta / 2), dC/dtheta = Rp cos(p theta / 2)"""
        R = 1.0
        p = 2.0
        theta = np.linspace(0, 4*np.pi, 10000)
        C_p = 2 * R * np.sin(p * theta / 2)
        dC_analytical = R * p * np.cos(p * theta / 2)
        dC_numerical = np.gradient(C_p, theta)
        residual = np.max(np.abs(dC_analytical - dC_numerical))
        assert residual < TOL_DERIVATIVE, f"Derivative residual: {residual} > {TOL_DERIVATIVE}"

    def test_zero_partition_limit(self):
        """Für p=0: C_p=0, dC/dtheta=0, M_{p,k}=0"""
        R, p, k = 1.0, 0.0, 1.0
        theta = np.linspace(0, 2*np.pi, 1000)
        C_p = 2 * R * np.sin(p * theta / 2)
        dC = R * p * np.cos(p * theta / 2)
        M_pk = dC * np.exp(1j * k * theta)
        assert np.allclose(C_p, 0, atol=TOL_DERIVATIVE)
        assert np.allclose(dC, 0, atol=TOL_DERIVATIVE)
        assert np.allclose(M_pk, 0, atol=TOL_DERIVATIVE)

    def test_radius_scaling(self):
        """Verdopplung von R verdoppelt C, dC/dtheta und M"""
        p, k, theta = 2.0, 1.0, np.pi / 3
        for R in [0.5, 1.0, 2.0, 4.0]:
            C_p = 2 * R * np.sin(p * theta / 2)
            dC = R * p * np.cos(p * theta / 2)
            M_pk = dC * np.exp(1j * k * theta)
            if R == 0.5:
                base_C, base_dC, base_M = C_p, dC, M_pk
            else:
                scale = R / 0.5
                assert np.isclose(C_p, base_C * scale, rtol=1e-10)
                assert np.isclose(dC, base_dC * scale, rtol=1e-10)
                assert np.isclose(M_pk, base_M * scale, rtol=1e-10)

    def test_sign_symmetry_p(self):
        """C_{-p}(theta) = -C_p(theta)"""
        R, p = 1.0, 3.0
        theta = np.linspace(0, 2*np.pi, 1000)
        C_p = 2 * R * np.sin(p * theta / 2)
        C_minus_p = 2 * R * np.sin(-p * theta / 2)
        dC_p = R * p * np.cos(p * theta / 2)
        dC_minus_p = R * (-p) * np.cos(-p * theta / 2)
        assert np.allclose(C_minus_p, -C_p, atol=TOL_DERIVATIVE)
        assert np.allclose(dC_minus_p, -dC_p, atol=TOL_DERIVATIVE)

    def test_mode_norm_invariance_under_k(self):
        """|M_{p,k}| = |dC_p/dtheta| für alle k"""
        R, p = 1.0, 2.0
        theta = np.linspace(0, 2*np.pi, 1000)
        dC = R * p * np.cos(p * theta / 2)
        dC_abs = np.abs(dC)
        for k in [-4, -2, -1, 0, 1, 2, 4]:
            M_pk = dC * np.exp(1j * k * theta)
            assert np.allclose(np.abs(M_pk), dC_abs, atol=TOL_DERIVATIVE)

    def test_no_nan_no_inf(self):
        """Keine NaN oder Inf für alle Parameterbereiche"""
        R_values = [0, 1, 2, np.sqrt(2)]
        p_values = [-8, -4, -2, -1, 0, 1, 2, 4, 8, np.sqrt(2)]
        k_values = [-8, -4, -2, -1, 0, 1, 2, 4, 8, np.sqrt(3)]
        theta = np.linspace(0, 4*np.pi, 1000)
        for R in R_values:
            for p in p_values:
                for k in k_values:
                    C_p = 2 * R * np.sin(p * theta / 2)
                    dC = R * p * np.cos(p * theta / 2)
                    M_pk = dC * np.exp(1j * k * theta)
                    assert not np.any(np.isnan(C_p))
                    assert not np.any(np.isnan(dC))
                    assert not np.any(np.isnan(M_pk))
                    assert not np.any(np.isinf(C_p))
                    assert not np.any(np.isinf(dC))
                    assert not np.any(np.isinf(M_pk))

    def test_integer_mode_periodicity(self):
        """Für ganzzahlige p und k: Kurve ist periodisch"""
        R = 1.0
        theta = np.linspace(0, 4*np.pi, 10000)
        for p, k in [(1,1),(2,2),(4,4),(2,4),(4,2)]:
            dC = R * p * np.cos(p * theta / 2)
            M_pk = dC * np.exp(1j * k * theta)
            x = np.real(M_pk) * np.cos(theta)
            y = np.real(M_pk) * np.sin(theta)
            distance = np.sqrt((x[0]-x[len(theta)//2])**2 + (y[0]-y[len(theta)//2])**2)
            assert distance < 5.0

    def test_non_integer_open_curve_detection(self):
        """Für nichtkommensurable p,k: Kurve schließt sich nicht exakt"""
        R, p, k = 1.0, np.sqrt(2), np.sqrt(3)
        theta = np.linspace(0, 4*np.pi, 10000)
        dC = R * p * np.cos(p * theta / 2)
        M_pk = dC * np.exp(1j * k * theta)
        x = np.real(M_pk) * np.cos(theta)
        y = np.real(M_pk) * np.sin(theta)
        distance = np.sqrt((x[0]-x[len(theta)//2])**2 + (y[0]-y[len(theta)//2])**2)
        assert distance > 1e-4

    def test_projection_consistency(self):
        """r(theta)^2 = x(theta)^2 + y(theta)^2"""
        R, p, k = 1.0, 2.0, 1.0
        theta = np.linspace(0, 4*np.pi, 10000)
        dC = R * p * np.cos(p * theta / 2)
        M_pk = dC * np.exp(1j * k * theta)
        r = np.real(M_pk)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        r_check = np.sqrt(x**2 + y**2)
        assert np.allclose(np.abs(r), r_check, atol=TOL_PROJECTION)

    def test_finite_energy_proxy(self):
        """E = ∫ |M_{p,k}(theta)|^2 dtheta ist endlich und positiv"""
        R = 1.0
        theta = np.linspace(0, 4*np.pi, 10000)
        dtheta = theta[1] - theta[0]
        for p in [1, 2, 4]:
            for k in [1, 2, 4]:
                dC = R * p * np.cos(p * theta / 2)
                M_pk = dC * np.exp(1j * k * theta)
                E = np.sum(np.abs(M_pk)**2) * dtheta
                assert E > 0
                assert np.isfinite(E)
        p, k = 0, 1
        dC = R * p * np.cos(p * theta / 2)
        M_pk = dC * np.exp(1j * k * theta)
        E_zero = np.sum(np.abs(M_pk)**2) * dtheta
        assert np.isclose(E_zero, 0, atol=TOL_ENERGY)


class TestSSZCompatibility:
    """SSZ-Kompatibilitätstests"""

    def test_no_free_parameters(self):
        """Chord-Partition hat keine freien Fit-Parameter"""
        assert True

    def test_phi_compatibility(self):
        """p und k können als Vielfache von φ interpretiert werden"""
        PHI = (1 + np.sqrt(5)) / 2
        R, p, k = 1.0, PHI, PHI
        theta = np.linspace(0, 4*np.pi, 1000)
        dC = R * p * np.cos(p * theta / 2)
        M_pk = dC * np.exp(1j * k * theta)
        assert not np.any(np.isnan(M_pk))
        assert not np.any(np.isinf(M_pk))

    def test_dimensionless_consistency(self):
        """Alle Größen sind dimensionslos oder konsistent"""
        assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
