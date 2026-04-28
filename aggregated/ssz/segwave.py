# -*- coding: utf-8 -*-
"""
Mock ssz.segwave Modul für Unified-Results Tests
"""

import numpy as np

def compute_q_factor(beta, temperature=0):
    """Compute Q-factor for given beta and temperature"""
    base_q = 1.0 / (1.0 - beta**2 + 1e-10)
    temp_correction = 1.0 - temperature * 0.01
    return base_q * temp_correction

def velocity_profile(r, r0=1.0, v_max=1.0):
    """Velocity profile function"""
    return v_max * np.tanh(r / r0)

def cumulative_gamma(beta_values):
    """Cumulative gamma factor"""
    return np.cumsum(1.0 / np.sqrt(1.0 - beta_values**2 + 1e-10))

# Konstanten
PHI = (1 + np.sqrt(5)) / 2
XI_MAX = 1 - np.exp(-PHI)
D_MIN = 1 / (1 + XI_MAX)
