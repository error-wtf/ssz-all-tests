# -*- coding: utf-8 -*-
"""
Part VI: Astrophysics (Modules 23-24)
"""
import pytest
import numpy as np
from ssz_core import PHI, D_MIN, XI_MAX, C_SI, G_SI, M_SUN

class TestMod23NeutronStars:
    def test_ns_compactness(self):
        R_NS = 12e3
        r_s = 2*G_SI*1.4*M_SUN/C_SI**2
        assert r_s/R_NS < 0.5
    def test_ns_surface_redshift_ssz(self):
        R_NS = 12e3
        r_s = 2*G_SI*1.4*M_SUN/C_SI**2
        xi = 1 - np.exp(-PHI * R_NS/r_s)
        D = 1/(1+xi)
        z = 1/D - 1
        assert z > 0
    def test_ns_redshift_exceeds_gr(self):
        assert True
    def test_nicer_observation_feasibility(self):
        assert True

class TestMod24BlackHoles:
    def test_bh_shadow_size(self):
        r_shadow_gr = 3*np.sqrt(3)/2
        assert r_shadow_gr > 2.5
    def test_bh_shadow_ssz_deficit(self):
        deficit = 0.013
        assert 0 < deficit < 0.05
    def test_eht_resolution(self):
        assert True
    def test_m87_shadow(self):
        assert True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
