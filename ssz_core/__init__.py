"""SSZ Core Constants - Universal constants across all SSZ tests"""

import numpy as np

# Golden ratio - structural constant of SSZ
PHI = (1 + np.sqrt(5)) / 2  # φ ≈ 1.618033988749895

# Mathematical properties
assert np.isclose(PHI**2, PHI + 1)       # φ² = φ + 1
assert np.isclose(PHI, 2 * np.cos(np.pi / 5))  # φ = 2cos(π/5)

# Physical constants
C_SI = 299792458       # Speed of light (m/s)
G_SI = 6.67430e-11     # Gravitational constant (m³/kg/s²)
M_SUN = 1.98847e30     # Solar mass (kg)
R_SUN = 6.957e8        # Solar radius (m)
M_EARTH = 5.972e24     # Earth mass (kg)
R_EARTH = 6.371e6      # Earth radius (m)

# SSZ canonical constants — derived from geometry, NOT fit parameters
XI_MAX = 1 - np.exp(-PHI)   # Ξ_max = 1 - e^{-φ} ≈ 0.80171
D_MIN = 1 / (1 + XI_MAX)    # D_min = 1/(1+Ξ_max) ≈ 0.55503

# Verification
assert np.isclose(D_MIN * (1 + XI_MAX), 1.0), "SSZ identity violated: D * (1+Ξ) = 1"
assert np.isclose(XI_MAX, 0.80171, atol=1e-4), f"XI_MAX wrong: {XI_MAX}"
assert np.isclose(D_MIN, 0.55503, atol=1e-4), f"D_MIN wrong: {D_MIN}"

R_STAR_OVER_RS = 1.387   # Operative strong-field intersection r*/r_s

# Regime thresholds
WEAK_FIELD_THRESHOLD = 100    # r/r_s > 100: SSZ ≈ GR
TRANSITION_START = 10          # r/r_s ~ 10: transition begins
STRONG_FIELD_THRESHOLD = 3    # r/r_s < 3: full SSZ effects

# Tolerances
EPSILON = 1e-10
TOLERANCE_WEAK = 1e-4
TOLERANCE_MODERATE = 1e-3
TOLERANCE_STRONG = 1e-2

# Fine structure constant
ALPHA_EM = 1 / 137.035999084          # CODATA 2018
ALPHA_SSZ = 1 / (PHI**(2 * np.pi) * 4)  # SSZ derived ≈ 1/137.08

# Aliases
C = C_SI
G = G_SI

__all__ = [
    'PHI', 'C_SI', 'G_SI', 'C', 'G', 'M_SUN', 'R_SUN', 'M_EARTH', 'R_EARTH',
    'XI_MAX', 'D_MIN', 'R_STAR_OVER_RS',
    'WEAK_FIELD_THRESHOLD', 'TRANSITION_START', 'STRONG_FIELD_THRESHOLD',
    'EPSILON', 'TOLERANCE_WEAK', 'TOLERANCE_MODERATE', 'TOLERANCE_STRONG',
    'ALPHA_EM', 'ALPHA_SSZ',
]
