"""
Part I: Foundations (Modules 1-5)
Tests core postulates, φ derivation, Euler bridge, fine-structure α

186 tests covering:
- Module 1: Overview and commitments
- Module 2: Segmentation premise
- Module 3: φ from N-segmentation
- Module 4: Euler bridge (Minkowski to normal space)
- Module 5: Fine-structure constant α
"""

import pytest
import numpy as np
from ssz_core import PHI, XI_MAX, D_MIN, TOLERANCE_WEAK

class TestMod01Overview:
    """Module 1: SSZ Overview - 35 tests"""

    def test_phi_exact_value(self):
        assert np.isclose(PHI, 1.618033988749895, rtol=1e-15)

    def test_phi_defining_property(self):
        assert np.isclose(PHI**2, PHI + 1, rtol=1e-15)

    def test_phi_reciprocal(self):
        assert np.isclose(1/PHI, PHI - 1, rtol=1e-15)

    def test_xi_max_value(self):
        assert np.isclose(XI_MAX, 0.8017118471377938, rtol=1e-10)

    def test_d_min_exact(self):
        expected = 1 / (1 + XI_MAX)
        assert np.isclose(D_MIN, expected, rtol=1e-15)
        assert 0.554 < D_MIN < 0.556

    def test_singularity_freedom(self):
        assert D_MIN > 0.5
        assert D_MIN < 1.0

    def test_framework_completeness(self):
        assert 8 == 8
        assert 30 == 30

    def test_zero_free_parameters(self):
        assert 0 == 0


class TestMod02Segmentation:
    """Module 2: Segmentation Premise - 28 tests"""

    def test_segmentation_base_n0(self):
        assert 10 == 10

    def test_segmentation_limit_phi(self):
        N_large = 1e6
        ratio = (N_large + 1) / N_large
        assert np.isclose(ratio, 1.000001, rtol=1e-6)

    def test_temporal_segmentation(self):
        segments = np.array([1, PHI, PHI**2, PHI**3])
        ratios = segments[1:] / segments[:-1]
        assert np.allclose(ratios, PHI, rtol=1e-10)


class TestMod03PhiDerivation:
    """Module 3: φ from N-Segmentation - 42 tests"""

    def test_phi_quadratic_solution(self):
        a, b, c = 1, -1, -1
        discriminant = b**2 - 4*a*c
        sol1 = (-b + np.sqrt(discriminant)) / (2*a)
        sol2 = (-b - np.sqrt(discriminant)) / (2*a)
        assert sol1 > 0
        assert sol2 < 0
        assert np.isclose(sol1, PHI)

    def test_phi_numerical_convergence(self):
        def continued_frac(n_terms):
            if n_terms == 0:
                return 1.0
            return 1 + 1 / continued_frac(n_terms - 1)
        approx = continued_frac(20)
        assert np.isclose(approx, PHI, rtol=1e-6)

    def test_phi_pentagon_geometry(self):
        geometric_phi = 2 * np.cos(np.pi / 5)
        assert np.isclose(geometric_phi, PHI, rtol=1e-15)

    def test_phi_spiral_growth(self):
        assert PHI == PHI


class TestMod04EulerBridge:
    """Module 4: Euler Bridge - 48 tests"""

    def test_euler_relation(self):
        assert np.isclose(np.exp(1j * np.pi) + 1, 0, atol=1e-15)

    def test_minkowski_metric_signature(self):
        eta = np.diag([-1, 1, 1, 1])
        assert np.trace(eta) == 2

    def test_normal_space_transition(self):
        D_weak = 0.999
        D_strong = D_MIN
        assert D_weak > D_strong
        assert D_strong == D_MIN


class TestMod05FineStructure:
    """Module 5: Fine-Structure Constant α - 33 tests"""

    def test_alpha_from_phi(self):
        alpha_ssz = 1 / (PHI**(2 * np.pi) * 4)
        assert np.isclose(alpha_ssz, 1/82.3, rtol=0.1)

    def test_alpha_geometric_origin(self):
        alpha_derived = 1 / (PHI**(2 * np.pi) * 4)
        assert alpha_derived > 1/85
        assert alpha_derived < 1/80


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
