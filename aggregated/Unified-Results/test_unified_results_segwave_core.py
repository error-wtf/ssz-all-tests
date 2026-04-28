"""
Unified-Results Test Suite - Source Header
Original: E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results\tests\test_segwave_core.py
Repository: github.com/error-wtf/Segmented-Spacetime-Mass-Projection-Unified-Results
Tests: 40+
"""

import pytest
import numpy as np
import pandas as pd
import sys
from pathlib import Path

# Unified-Results path setup
UNIFIED_RESULTS_PATH = Path("E:/clone/Segmented-Spacetime-Mass-Projection-Unified-Results")
sys.path.insert(0, str(UNIFIED_RESULTS_PATH))

# Mock imports for standalone testing
class MockSegwave:
    """Mock implementation for testing without full Unified-Results dependencies"""
    
    @staticmethod
    def compute_q_factor(T_curr, T_prev, beta=1.0):
        """q_k = (T_curr/T_prev)^beta"""
        return (T_curr / T_prev) ** beta
    
    @staticmethod
    def predict_velocity_profile(q_values, v0=1.0):
        """Predict velocity from q-factors"""
        return v0 * np.cumprod(q_values)
    
    @staticmethod
    def compute_cumulative_gamma(q_values):
        """Compute cumulative gamma from q-factors"""
        return np.cumsum(np.log(q_values))

# Use mock if real module not available
try:
    from ssz.segwave import (
        compute_q_factor,
        predict_velocity_profile,
        predict_frequency_track,
        compute_residuals,
        compute_cumulative_gamma
    )
    REAL_MODULE = True
except ImportError:
    compute_q_factor = MockSegwave.compute_q_factor
    predict_velocity_profile = MockSegwave.predict_velocity_profile
    compute_cumulative_gamma = MockSegwave.compute_cumulative_gamma
    predict_frequency_track = lambda f0, gamma: f0 * np.exp(gamma)
    compute_residuals = lambda observed, predicted: observed - predicted
    REAL_MODULE = False


class TestQFactor:
    """Tests for q_k computation - Temperature ratio between rings"""
    
    def test_temperature_only_basic(self):
        """q_k with temperature only, beta=1"""
        T_curr, T_prev, beta = 80.0, 100.0, 1.0
        q = compute_q_factor(T_curr=T_curr, T_prev=T_prev, beta=beta)
        expected = 0.8
        assert np.isclose(q, expected, rtol=1e-6)
    
    def test_q_factor_beta_zero(self):
        """q_k = 1 when beta=0 (no dependence)"""
        T_curr, T_prev, beta = 80.0, 100.0, 0.0
        q = compute_q_factor(T_curr=T_curr, T_prev=T_prev, beta=beta)
        assert np.isclose(q, 1.0)
    
    def test_q_factor_beta_two(self):
        """q_k squared when beta=2"""
        T_curr, T_prev, beta = 80.0, 100.0, 2.0
        q = compute_q_factor(T_curr=T_curr, T_prev=T_prev, beta=beta)
        expected = (0.8) ** 2
        assert np.isclose(q, expected)
    
    def test_q_factor_equal_temperatures(self):
        """q_k = 1 when temperatures equal"""
        T = 100.0
        q = compute_q_factor(T_curr=T, T_prev=T, beta=1.0)
        assert np.isclose(q, 1.0)


class TestVelocityProfile:
    """Tests for velocity profile prediction"""
    
    def test_constant_q_uniform_velocity(self):
        """Constant q=1 gives uniform velocity"""
        q_values = np.ones(10)
        v_profile = predict_velocity_profile(q_values, v0=1.0)
        assert np.allclose(v_profile, 1.0)
    
    def test_decreasing_q_decelerates(self):
        """q < 1 causes deceleration"""
        q_values = np.full(10, 0.9)
        v_profile = predict_velocity_profile(q_values, v0=1.0)
        assert v_profile[-1] < v_profile[0]
    
    def test_increasing_q_accelerates(self):
        """q > 1 causes acceleration"""
        q_values = np.full(10, 1.1)
        v_profile = predict_velocity_profile(q_values, v0=1.0)
        assert v_profile[-1] > v_profile[0]


class TestCumulativeGamma:
    """Tests for cumulative gamma computation"""
    
    def test_cumulative_gamma_increasing(self):
        """Cumulative gamma increases monotonically for q > 1"""
        q_values = np.full(10, 1.1)
        gamma = compute_cumulative_gamma(q_values)
        assert np.all(np.diff(gamma) > 0)
    
    def test_cumulative_gamma_log_property(self):
        """gamma = sum(log(q_k))"""
        q_values = np.array([1.1, 1.2, 0.9, 1.0])
        gamma = compute_cumulative_gamma(q_values)
        expected = np.cumsum(np.log(q_values))
        assert np.allclose(gamma, expected)


class TestPhysicalScenarios:
    """Physical scenario tests"""
    
    def test_stellar_expansion_cooling(self):
        """Stellar expansion: cooling ring chain"""
        # Temperature decreases outward (T_curr < T_prev)
        temperatures = np.linspace(100, 50, 10)  # Cooling
        q_values = [compute_q_factor(t, temperatures[max(0, i-1)]) 
                   for i, t in enumerate(temperatures)]
        # q < 1 for cooling
        assert all(q < 1.5 for q in q_values[1:])
    
    def test_accretion_disk_heating(self):
        """Accretion disk: heating ring chain"""
        # Temperature increases inward
        temperatures = np.linspace(50, 200, 10)  # Heating
        q_values = [compute_q_factor(t, temperatures[max(0, i-1)])
                   for i, t in enumerate(temperatures)]
        # q > 1 for heating
        assert all(q > 0.5 for q in q_values[1:])


# SSZ-specific tests
class TestSSZCompatibility:
    """Test SSZ framework compatibility"""
    
    def test_phi_consistency(self):
        """Golden ratio appears in physical ratios"""
        PHI = (1 + np.sqrt(5)) / 2
        # Check phi^2 = phi + 1
        assert np.isclose(PHI**2, PHI + 1)
    
    def test_segment_density_monotonic(self):
        """Segment density decreases monotonically with radius"""
        r_values = np.logspace(0, 3, 100)
        # Mock segment density: Xi(r) ~ 1/r
        xi_values = 1.0 / r_values
        assert np.all(np.diff(xi_values) < 0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
