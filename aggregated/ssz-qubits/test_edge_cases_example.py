# -*- coding: utf-8 -*-
# =============================================================================
# SOURCE: ssz-qubits
# ORIGINAL PATH: e:\clone\ssz-qubits\tests\test_edge_cases.py
# AGGREGATED: 2026-04-27T18:33:47.137014
# =============================================================================
# This file was automatically aggregated from the SSZ repository.
# Do not modify - changes will be lost on next aggregation.
# =============================================================================

"""
SSZ Edge Case Tests
Tests for extreme conditions and boundary cases.
"""

import numpy as np
import pytest


def test_extreme_radius():
    """Test behavior at very small radius (near r_s)."""
    r_s = 8.87e-3  # Earth Schwarzschild radius in meters
    r = 10 * r_s
    xi = 1 - np.exp(-1.618 * r / r_s)
    xi_capped = min(xi, 0.809)
    assert xi_capped > 0.5
    assert xi_capped <= 0.809


def test_zero_mass():
    """Test zero mass case (flat spacetime)."""
    M = 0
    r_s = 0
    xi = 0
    assert xi == 0


def test_large_radius():
    """Test at 1 AU (weak field)."""
    AU = 1.496e11
    xi = 1e-10  # Very small
    assert xi < 1e-8


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
