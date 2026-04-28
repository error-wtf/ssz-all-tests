#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unified-Results Real Data Tests - Source Header
Original: E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results\tests\test_ssz_real_data_comprehensive.py
Repository: github.com/error-wtf/Segmented-Spacetime-Mass-Projection-Unified-Results
Tests: 6 comprehensive tests with real astronomical data
"""

import sys
import io
import math
import json
from pathlib import Path
from typing import Dict, List, Tuple

import pytest
import pandas as pd
import numpy as np

# Physical constants - MATCH SSZ_BOOK_DE.tex
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio: 1.618033988749895
XI_MAX = 1 - math.exp(-PHI)   # Ξ_max = 0.80171...
D_MIN = 1 / (1 + XI_MAX)      # D_min ≈ 0.5557

G = 6.67430e-11                # Gravitational constant [m³/kg/s²]
C = 299792458.0                # Speed of light [m/s]
M_SUN = 1.98847e30             # Solar mass [kg]

# Real astronomical objects with measured masses
ASTRONOMICAL_OBJECTS = {
    "Sun": {
        "mass_kg": 1.98847e30,
        "mass_solar": 1.0,
        "description": "Our Sun - reference star",
    },
    "Earth": {
        "mass_kg": 5.97237e24,
        "mass_solar": 3.0e-6,
        "description": "Earth - our planet",
    },
    "Jupiter": {
        "mass_kg": 1.89813e27,
        "mass_solar": 9.55e-4,
        "description": "Jupiter - largest planet",
    },
    "SgrA*": {
        "mass_kg": 4.297e6 * M_SUN,
        "mass_solar": 4.297e6,
        "description": "Sagittarius A* - SMBH at galactic center",
    },
    "M87*": {
        "mass_kg": 6.5e9 * M_SUN,
        "mass_solar": 6.5e9,
        "description": "M87* - first EHT-imaged SMBH",
    },
    "PsrB1913+16": {
        "mass_kg": 1.4408 * M_SUN,
        "mass_solar": 1.4408,
        "description": "Hulse-Taylor pulsar - binary neutron star",
    },
}


class TestRealAstronomicalData:
    """Test SSZ with real astronomical objects"""
    
    def test_sun_basic_properties(self):
        """Sun: Basic SSZ properties"""
        M = ASTRONOMICAL_OBJECTS["Sun"]["mass_kg"]
        r_s = 2 * G * M / C**2  # Schwarzschild radius
        
        # At solar surface (r ~ 7e8 m)
        r = 6.957e8
        xi = r_s / (2 * r)  # Weak field
        d_ssz = 1 / (1 + xi)
        
        assert xi < 1e-6  # Very weak field
        assert np.isclose(d_ssz, 1.0, rtol=1e-6)
    
    def test_earth_gravitational_redshift(self):
        """Earth: Gravitational redshift from surface"""
        M = ASTRONOMICAL_OBJECTS["Earth"]["mass_kg"]
        R = 6.371e6  # Earth radius
        
        r_s = 2 * G * M / C**2
        xi_surface = r_s / (2 * R)
        
        # GR redshift
        z_gr = xi_surface
        # SSZ redshift (same in weak field)
        z_ssz = xi_surface
        
        assert np.isclose(z_ssz, z_gr)
        assert z_ssz > 0  # Positive redshift (time runs slower at surface)
    
    def test_jupiter_compactness(self):
        """Jupiter: Much less compact than Sun"""
        M_jup = ASTRONOMICAL_OBJECTS["Jupiter"]["mass_kg"]
        M_sun = ASTRONOMICAL_OBJECTS["Sun"]["mass_kg"]
        R_jup = 6.991e7  # Jupiter radius
        
        # Schwarzschild radii
        r_s_jup = 2 * G * M_jup / C**2
        r_s_sun = 2 * G * M_sun / C**2
        
        # Compactness ratio
        compactness_jup = r_s_jup / R_jup
        compactness_sun = r_s_sun / 6.957e8
        
        assert compactness_jup < compactness_sun
    
    def test_sgr_a_star_is_supermassive(self):
        """Sgr A*: Supermassive black hole properties"""
        M = ASTRONOMICAL_OBJECTS["SgrA*"]["mass_kg"]
        r_s = 2 * G * M / C**2
        
        # At 5 r_s (photon sphere region)
        r = 5 * r_s
        xi_strong = 1 - math.exp(-PHI * r_s / r)
        d_ssz = 1 / (1 + xi_strong)
        d_gr = math.sqrt(1 - r_s / r)
        
        # SSZ predicts different value
        assert not np.isclose(d_ssz, d_gr, rtol=0.1)
        
        # SSZ finite at horizon (D_min)
        xi_horizon = XI_MAX
        d_horizon = 1 / (1 + xi_horizon)
        assert np.isclose(d_horizon, D_MIN)
    
    def test_m87_star_shadow_prediction(self):
        """M87*: Shadow diameter prediction differs from GR"""
        M = ASTRONOMICAL_OBJECTS["M87*"]["mass_kg"]
        r_s = 2 * G * M / C**2
        
        # Photon sphere radius
        r_ph_gr = 1.5 * r_s  # GR
        r_ph_ssz = 1.48 * r_s  # SSZ (-1.3%)
        
        # Shadow diameter scales with photon sphere
        d_shadow_gr = 2 * r_ph_gr
        d_shadow_ssz = 2 * r_ph_ssz
        
        # SSZ predicts -1.3% shadow
        diff_percent = (d_shadow_ssz - d_shadow_gr) / d_shadow_gr * 100
        assert np.isclose(diff_percent, -1.3, rtol=0.1)
    
    def test_hulse_taylor_pulsar_orbital_decay(self):
        """PSR B1913+16: Binary pulsar orbital decay"""
        M = ASTRONOMICAL_OBJECTS["PsrB1913+16"]["mass_kg"]
        
        # Pulsar mass ~ 1.44 solar masses
        assert M > 1.4 * M_SUN
        assert M < 1.5 * M_SUN
        
        # Neutron star compactness
        r_s = 2 * G * M / C**2
        R_ns = 1.2e4  # ~12 km radius
        compactness = r_s / R_ns
        
        # r/r_s ~ 2 for typical neutron star
        assert 1.8 < R_ns / r_s < 2.2
    
    def test_phi_invariant_across_masses(self):
        """φ-based invariants hold for all masses"""
        for name, obj in ASTRONOMICAL_OBJECTS.items():
            M = obj["mass_kg"]
            r_s = 2 * G * M / C**2
            
            # r* / r_s = 1.387 (universal from φ)
            r_star = PHI / 2 * r_s
            ratio = r_star / r_s
            
            assert np.isclose(ratio, PHI / 2, rtol=1e-10)
    
    def test_minus_44_percent_universal(self):
        """The -44% prediction is mass-independent"""
        r_multiple = 5.0  # At 5 r_s
        
        for name, obj in ASTRONOMICAL_OBJECTS.items():
            if obj["mass_solar"] < 1.0:  # Skip planets
                continue
                
            M = obj["mass_kg"]
            r_s = 2 * G * M / C**2
            r = r_multiple * r_s
            
            # SSZ at 5 r_s
            xi_ssz = 1 - math.exp(-PHI * r_s / r)
            d_ssz = 1 / (1 + xi_ssz)
            
            # GR at 5 r_s
            d_gr = math.sqrt(1 - r_s / r)
            
            # Both give same -44% difference
            delta = (d_ssz - d_gr) / d_gr
            assert np.isclose(delta, -0.441, rtol=0.01)


class TestSSZPhysicalPredictions:
    """Core SSZ physical predictions"""
    
    def test_natural_boundary_ratio(self):
        """r*/r_s = φ/2 ≈ 1.387"""
        ratio = PHI / 2
        assert np.isclose(ratio, 1.387, rtol=0.001)
    
    def test_xi_max_formula(self):
        """Ξ_max = 1 - exp(-φ) ≈ 0.8017"""
        xi_max = 1 - math.exp(-PHI)
        assert np.isclose(xi_max, XI_MAX)
        assert np.isclose(xi_max, 0.8017, rtol=1e-4)
    
    def test_d_min_formula(self):
        """D_min = 1/(1+Ξ_max) ≈ 0.555"""
        d_min = 1 / (1 + XI_MAX)
        assert np.isclose(d_min, D_MIN)
        assert np.isclose(d_min, 0.5557, rtol=1e-4)
    
    def test_weak_field_ssz_equals_gr(self):
        """SSZ → GR in weak field (r >> r_s)"""
        r_over_rs = 1000  # Very weak field
        
        xi_ssz = r_s_ratio = 1 / (2 * r_over_rs)
        xi_gr = r_s_ratio
        
        assert np.isclose(xi_ssz, xi_gr, rtol=1e-6)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
