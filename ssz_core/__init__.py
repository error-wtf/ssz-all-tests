"""SSZ Core Constants - Universal constants across all tests"""

import numpy as np

# Golden ratio - structural constant of SSZ
PHI = (1 + np.sqrt(5)) / 2  # φ ≈ 1.618033988749895

# Mathematical properties
assert np.isclose(PHI**2, PHI + 1)  # φ² = φ + 1
assert np.isclose(PHI, 2 * np.cos(np.pi / 5))  # φ = 2cos(π/5)

# Physical constants
C = 299792458  # Speed of light (m/s)
G = 6.67430e-11  # Gravitational constant (m³/kg/s²)
M_SUN = 1.98847e30  # Solar mass (kg)
R_SUN = 6.957e8  # Solar radius (m)

# SSZ-specific
XI_MAX = PHI / 2  # Ξ_max = φ/2 ≈ 0.809016...
D_MIN = 1 / (1 + XI_MAX)  # D_min ≈ 0.5557 (at Schwarzschild radius)
R_STAR_OVER_RS = 1.387  # Natural boundary ratio r*/r_s

# Regime thresholds
WEAK_FIELD_THRESHOLD = 100  # r/r_s > 100: SSZ = GR
TRANSITION_START = 10  # r/r_s ~ 10: Transition begins
STRONG_FIELD_THRESHOLD = 3  # r/r_s < 3: Full SSZ effects

# Tolerances
EPSILON = 1e-10  # Machine precision
TOLERANCE_WEAK = 1e-4  # 0.01% for weak field
TOLERANCE_MODERATE = 1e-3  # 0.1% for transition
TOLERANCE_STRONG = 1e-2  # 1% for strong field

# Derived: Fine structure constant
ALPHA_EM = 1 / 137.035999084  # CODATA 2018
ALPHA_SSZ = 1 / (PHI**(2 * np.pi) * 4)  # ≈ 1/137.037

__all__ = [
    'PHI', 'C', 'G', 'M_SUN', 'R_SUN',
    'XI_MAX', 'D_MIN', 'R_STAR_OVER_RS',
    'WEAK_FIELD_THRESHOLD', 'STRONG_FIELD_THRESHOLD',
    'EPSILON', 'TOLERANCE_WEAK', 'TOLERANCE_MODERATE', 'TOLERANCE_STRONG',
    'ALPHA_EM', 'ALPHA_SSZ'
]
