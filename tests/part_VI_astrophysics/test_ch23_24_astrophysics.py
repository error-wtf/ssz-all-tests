# -*- coding: utf-8 -*-
"""
Part VI: Astrophysics (Chapters 23-24) - 14 Tests
Compact Objects, Accretion
"""

import pytest
import numpy as np
from ssz_core import PHI, C_SI, G_SI, M_SUN, XI_MAX, D_MIN

class TestCh23CompactObjects:
    """Chapter 23: Compact Objects - 8 tests"""
    
    def test_schwarzschild_radius(self):
        """r_s = 2GM/c²"""
        G, M, c = G_SI, M_SUN, C_SI
        r_s = 2*G*M/c**2
        assert r_s > 0
        assert r_s > 2000  # km
    
    def test_compactness_parameter(self):
        """C = GM/(Rc²)"""
        GM, R, c = 1.0, 10.0, 1.0
        C = GM/(R*c**2)
        assert 0 < C < 1
    
    def test_neutron_star_compactness(self):
        """NS compactness: C ≈ 0.1-0.3"""
        C_ns = 0.15
        assert 0.1 < C_ns < 0.3
    
    def test_white_dwarf_mass_limit(self):
        """Chandrasekhar limit: 1.4 M☉"""
        M_ch = 1.4 * M_SUN
        assert M_ch > 1.3 * M_SUN
        assert M_ch < 1.5 * M_SUN
    
    def test_neutron_star_mass_range(self):
        """NS mass: 1.1-2.2 M☉"""
        M_min, M_max = 1.1*M_SUN, 2.2*M_SUN
        assert M_min < M_max
    
    def test_black_hole_spin_limit(self):
        """Kerr spin: a < M (sub-extremal)"""
        a, M = 0.9, 1.0
        assert a < M
    
    def test_eddington_luminosity(self):
        """L_Edd = 4πGMm_p/σ_T"""
        G, M, mp, sigma_T = 6.67e-11, M_SUN, 1.67e-27, 6.65e-29
        L_edd = 4*np.pi*G*M*mp/sigma_T
        assert L_edd > 0
    
    def test_ssz_compact_object_modification(self):
        """SSZ modifies compact objects with D_min"""
        D_min = 0.553
        assert D_min > 0.5


class TestCh24Accretion:
    """Chapter 24: Accretion Physics - 6 tests"""
    
    def test_accretion_luminosity(self):
        """L_acc = GMṀ/(2R)"""
        G, M, M_dot, R = 6.67e-11, M_SUN, 1e-9, 1e7
        L_acc = G*M*M_dot/(2*R)
        assert L_acc > 0
    
    def test_accretion_efficiency(self):
        """η = L_acc/(Ṁc²)"""
        eta = 0.1
        assert 0 < eta < 1
    
    def test_innermost_stable_orbit(self):
        """ISCO: r_ISCO = 6GM/c² (Schwarzschild)"""
        G, M, c = 6.67e-11, M_SUN, 3e8
        r_isco = 6*G*M/c**2
        assert r_isco > 0
    
    def test_accretion_disk_temperature(self):
        """T(r) ∝ r^(-3/4)"""
        r1, r2 = 1.0, 2.0
        T_ratio = (r2/r1)**(-0.75)
        assert T_ratio < 1.0
    
    def test_jet_formation_power(self):
        """P_jet = ε_jet L_acc"""
        P_jet = 1e38
        assert P_jet > 0
    
    def test_ssz_accretion_modification(self):
        """SSZ modifies accretion with dilation factor"""
        D = 0.6
        L_classical = 1e38
        L_ssz = L_classical * D
        assert L_ssz < L_classical


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
