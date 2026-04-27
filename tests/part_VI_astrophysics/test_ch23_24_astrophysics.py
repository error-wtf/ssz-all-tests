import pytest
import numpy as np
from ssz_core import PHI, C_SI, G_SI, M_SUN, XI_MAX, D_MIN

class TestCh23CompactObjects:
    def test_schwarzschild_radius(self):
        G, M, c = G_SI, M_SUN, C_SI
        r_s = 2*G*M/c**2
        assert r_s > 0

class TestCh24Accretion:
    def test_accretion_luminosity(self):
        G, M, M_dot, R = 6.67e-11, M_SUN, 1e-9, 1e7
        L_acc = G*M*M_dot/(2*R)
        assert L_acc > 0