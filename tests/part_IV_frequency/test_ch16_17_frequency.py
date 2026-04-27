import pytest
import numpy as np
from ssz_core import PHI, C_SI, XI_MAX, D_MIN

class TestCh16Redshift:
    def test_redshift_basic_formula(self):
        f_emit, f_obs = 1.0, 0.9
        z = (f_emit - f_obs) / f_obs
        assert z > 0

class TestCh17TimeDilation:
    def test_time_dilation_basic(self):
        gamma, dt = 2.0, 1.0
        dt_prime = gamma * dt
        assert dt_prime == 2.0