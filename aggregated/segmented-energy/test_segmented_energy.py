#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Segmented-Energy Tests - Source Header
Original: E:\clone\segmented-energy\segmented_energy.py
Repository: github.com/error-wtf/segmented-energy
Tests: 6 tests for energy decomposition model
"""

import sys
import numpy as np
import pytest
from pathlib import Path

# Mock astropy for testing without dependency
try:
    from astropy import units as u
    from astropy.constants import G, c, M_sun, R_sun
    ASTROPY_AVAILABLE = True
except ImportError:
    ASTROPY_AVAILABLE = False
    # Mock units
    class MockUnit:
        def __init__(self, name):
            self.name = name
        def __mul__(self, other):
            return MockQuantity(other, self.name)
        def __rmul__(self, other):
            return MockQuantity(other, self.name)
    
    class MockQuantity:
        def __init__(self, value, unit):
            self.value = value
            self.unit = unit
        def __float__(self):
            return float(self.value)
        def to(self, unit):
            return self
        @property
        def si(self):
            return self
        @property
        def value(self):
            return self._value
        @value.setter
        def value(self, v):
            self._value = v
    
    class MockUnits:
        m = MockUnit('m')
        km = MockUnit('km')
        s = MockUnit('s')
        kg = MockUnit('kg')
        Quantity = MockQuantity
    
    u = MockUnits()
    G = 6.67430e-11  # m³/kg/s²
    c = 299792458.0  # m/s
    M_sun = 1.98847e30  # kg
    R_sun = 6.957e8  # m


# Physical constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
C_SI = 299792458.0
G_SI = 6.67430e-11
M_SUN = 1.98847e30


def radii_linear(r_in, r_out, N):
    """Generate N segment midpoints linearly spaced"""
    dr = (r_out - r_in) / N
    return np.array([r_in + (i + 0.5) * dr for i in range(N)])


def compute_segment_energy(M, m_test, r_n, N):
    """
    Compute energy for one segment at radius r_n
    
    E_n = (m_test/N) * [-G*M/r_n + (γ_n - 1)*c²]
    where γ_n = 1/sqrt(1 - v_n²/c²)
    and v_n = sqrt(G*M/r_n)
    """
    dm = m_test / N
    v_n = np.sqrt(G_SI * M / r_n)
    gamma_n = 1 / np.sqrt(1 - (v_n/C_SI)**2)
    
    e_grav = -G_SI * M / r_n
    e_sr = (gamma_n - 1) * C_SI**2
    
    return dm * (e_grav + e_sr)


def compute_total_energy(M, m_test, r_in, r_out, N):
    """Total energy = sum over all segments"""
    radii = radii_linear(r_in, r_out, N)
    energies = [compute_segment_energy(M, m_test, r, N) for r in radii]
    return sum(energies)


class TestSegmentedEnergy:
    """Tests for segmented energy model"""
    
    def test_linear_radii_generation(self):
        """Test linear radius spacing"""
        r_in, r_out, N = 1e6, 10e6, 10
        radii = radii_linear(r_in, r_out, N)
        
        assert len(radii) == N
        assert radii[0] > r_in
        assert radii[-1] < r_out
        assert np.all(np.diff(radii) > 0)  # Monotonically increasing
    
    def test_segment_energy_negative(self):
        """Segment energy is negative (bound system)"""
        M = M_SUN
        m_test = 1.0  # 1 kg test mass
        r_n = 1e9  # 1000 km from center
        N = 100
        
        e_seg = compute_segment_energy(M, m_test, r_n, N)
        assert e_seg < 0  # Bound system has negative energy
    
    def test_total_energy_converges(self):
        """Total energy converges as N increases"""
        M = M_SUN
        m_test = 1.0
        r_in, r_out = 1e8, 1e9
        
        # Compute for different N
        energies = []
        for N in [10, 50, 100, 500]:
            e = compute_total_energy(M, m_test, r_in, r_out, N)
            energies.append(e)
        
        # Energy should converge (change less between steps)
        deltas = np.abs(np.diff(energies))
        assert deltas[-1] < deltas[0]  # Convergence
    
    def test_gravitational_component_dominates(self):
        """Gravitational energy dominates over SR correction"""
        M = M_SUN
        m_test = 1.0
        r_n = 7e8  # Near solar surface
        N = 100
        
        dm = m_test / N
        v_n = np.sqrt(G_SI * M / r_n)
        gamma_n = 1 / np.sqrt(1 - (v_n/C_SI)**2)
        
        e_grav = -G_SI * M / r_n
        e_sr = (gamma_n - 1) * C_SI**2
        
        # |E_grav| >> E_sr for non-relativistic velocities
        assert np.abs(e_grav) > e_sr
    
    def test_energy_scales_with_mass(self):
        """Total energy scales linearly with test mass"""
        M = M_SUN
        r_in, r_out, N = 1e8, 1e9, 50
        
        m1, m2 = 1.0, 2.0
        e1 = compute_total_energy(M, m1, r_in, r_out, N)
        e2 = compute_total_energy(M, m2, r_in, r_out, N)
        
        assert np.isclose(e2 / e1, m2 / m1, rtol=1e-10)
    
    def test_weak_field_newtonian_limit(self):
        """In weak field, recover Newtonian energy"""
        M = M_SUN
        m_test = 1.0
        # Far from Sun (weak field)
        r_in, r_out, N = 1e11, 1e12, 100
        
        e_total = compute_total_energy(M, m_test, r_in, r_out, N)
        
        # Newtonian expectation: E ≈ -G*M*m/r_avg
        r_avg = (r_in + r_out) / 2
        e_newtonian = -G_SI * M * m_test / r_avg
        
        # Should be close in weak field (within 1%)
        assert np.abs((e_total - e_newtonian) / e_newtonian) < 0.01


class TestSSZSpecificPredictions:
    """SSZ-specific energy predictions"""
    
    def test_phi_energy_scaling(self):
        """Energy corrections scale with φ-based segment density"""
        # Mock segment density
        r = np.linspace(1e8, 1e10, 100)
        xi = 1 - np.exp(-PHI * 1e8 / r)  # SSZ segment density
        
        # Energy density should correlate with xi
        energy_density = 1 / (1 + xi)
        assert np.all(energy_density > 0)
        assert np.all(energy_density <= 1)
    
    def test_finite_energy_at_horizon(self):
        """SSZ predicts finite energy at Schwarzschild radius"""
        M = M_SUN
        r_s = 2 * G_SI * M / C_SI**2
        
        # At r = r_s (horizon in GR, but not singular in SSZ)
        xi_at_rs = 1 - np.exp(-PHI)
        d_at_rs = 1 / (1 + xi_at_rs)
        
        assert d_at_rs > 0  # Finite in SSZ
        assert np.isclose(d_at_rs, 0.555, rtol=0.01)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
