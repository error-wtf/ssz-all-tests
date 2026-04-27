# -*- coding: utf-8 -*-
# =============================================================================
# SOURCE: ssz-metric-pure
# ORIGINAL PATH: E:\clone\ssz-metric-pure\tests\test_sparse_validators.py
# AGGREGATED: 2026-04-27T20:50:00
# =============================================================================

"""
SSZ Symbolic Sparse Validators

Tests metric compatibility (∇_α g_μν = 0)
and energy conservation along geodesics.
"""

import pytest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ssz_metric_pure.ssz_symbolic_sparse import (
    validator_nabla_g_zero,
    validator_energy_conservation
)

M_EARTH = 5.9722e24
M_SUN = 1.98847e30
G_SI = 6.67430e-11
C_SI = 299792458.0

NABLA_G_TOLERANCE = 1e-10
ENERGY_TOLERANCE = 1e-6


class TestMetricCompatibility:
    """Test ∇_α g_μν = 0 (metric compatibility)"""
    
    def test_nabla_g_earth_weak_field(self):
        """Metric compatibility for Earth (weak field)"""
        max_error = validator_nabla_g_zero(
            max_r_samples=5,
            r_min=6.4e6,
            r_max=6.4e9,
            M_val=M_EARTH,
            G_val=G_SI,
            c_val=C_SI
        )
        assert max_error < NABLA_G_TOLERANCE
    
    def test_nabla_g_sun_weak_field(self):
        """Metric compatibility for Sun (weak field)"""
        max_error = validator_nabla_g_zero(
            max_r_samples=5,
            r_min=6.96e8,
            r_max=6.96e11,
            M_val=M_SUN,
            G_val=G_SI,
            c_val=C_SI
        )
        assert max_error < NABLA_G_TOLERANCE


class TestEnergyConservation:
    """Test energy conservation along timelike geodesics"""
    
    def test_energy_earth_low_orbit(self):
        """Energy conservation for Earth low orbit"""
        drift = validator_energy_conservation(
            M_val=M_EARTH,
            G_val=G_SI,
            c_val=C_SI,
            r0=7.0e6,
            steps=5000,
            dlam=1e-3
        )
        assert drift < ENERGY_TOLERANCE
    
    def test_energy_sun_surface(self):
        """Energy conservation for Sun at surface"""
        drift = validator_energy_conservation(
            M_val=M_SUN,
            G_val=G_SI,
            c_val=C_SI,
            r0=7.0e8,
            steps=5000,
            dlam=1e-3
        )
        assert drift < ENERGY_TOLERANCE


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
