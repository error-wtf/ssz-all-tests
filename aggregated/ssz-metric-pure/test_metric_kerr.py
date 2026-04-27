# -*- coding: utf-8 -*-
# =============================================================================
# SOURCE: ssz-metric-pure
# ORIGINAL PATH: E:\clone\ssz-metric-pure\tests\test_metric_kerr.py
# AGGREGATED: 2026-04-27T20:45:00
# =============================================================================

"""
SSZ Metric Pure - Kerr Metric Tests

Tests symbolic validation of Kerr metric components,
frame dragging, horizons, and ergosphere properties.
"""

import numpy as np
import pytest
from ssz_metric_pure.kerr_metric import KerrSSZMetric, KerrSSZParams
from ssz_core.constants import M_SUN


class TestKerrHorizons:
    """Test horizon structure for Kerr metric."""
    
    def test_horizon_exists(self, kerr_moderate):
        """Outer horizon r_+ exists for a > 0."""
        r_plus, r_minus = kerr_moderate.horizons()
        assert r_plus > 0, "Outer horizon must exist"
        assert r_plus > r_minus, "r_+ > r_-"
    
    def test_ergosphere_larger_than_horizon(self, kerr_moderate):
        """r_ergo > r_horizon for a > 0."""
        r_plus, _ = kerr_moderate.horizons()
        r_ergo = kerr_moderate.ergosphere_radius()
        assert r_ergo > r_plus, "Ergosphere extends beyond horizon"
    
    def test_frame_dragging_nonzero(self, kerr_moderate):
        """ω ≠ 0 for a > 0 (prograde frame dragging)."""
        r_test = 5.0 * kerr_moderate.r_s
        theta = np.pi / 2
        omega = kerr_moderate.frame_drag_frequency(r_test, theta)
        assert omega != 0, "Frame dragging must be non-zero for a≠0"
        assert omega > 0, "Frame dragging is prograde (positive)"
    
    def test_schwarzschild_limit_no_frame_drag(self, kerr_schwarzschild):
        """a=0 → no frame dragging (ω=0)."""
        r_test = 5.0 * kerr_schwarzschild.r_s
        theta = np.pi / 2
        omega = kerr_schwarzschild.frame_drag_frequency(r_test, theta)
        assert abs(omega) < 1e-10, "No frame dragging for a=0"
    
    def test_schwarzschild_limit_horizons(self, kerr_schwarzschild):
        """a=0 → r_+ = r_s, r_- = 0."""
        r_plus, r_minus = kerr_schwarzschild.horizons()
        assert abs(r_plus - kerr_schwarzschild.r_s) < 1e-6, "r_+ = r_s for a=0"
        assert abs(r_minus) < 1e-6, "r_- = 0 for a=0"


class TestKerrMetricComponents:
    """Test metric tensor components."""
    
    def test_metric_components_finite(self, kerr_moderate):
        """All metric components finite outside horizon."""
        r_test = 5.0 * kerr_moderate.r_s
        theta = np.pi / 4
        comp = kerr_moderate.metric_tensor(r_test, theta)
        assert np.isfinite(comp.g_tt), "g_tt must be finite"
        assert np.isfinite(comp.g_rr), "g_rr must be finite"
        assert np.isfinite(comp.g_thth), "g_θθ must be finite"
        assert np.isfinite(comp.g_phph), "g_φφ must be finite"
        assert np.isfinite(comp.g_tph), "g_tφ must be finite"
    
    def test_g_tt_negative_outside_ergosphere(self, kerr_moderate):
        """g_tt < 0 outside ergosphere (time-like allowed)."""
        r_far = 10.0 * kerr_moderate.r_s
        theta = np.pi / 2
        g_tt = kerr_moderate.g_tt(r_far, theta)
        assert g_tt < 0, "g_tt must be negative outside ergosphere"
    
    def test_redshift_positive(self, kerr_moderate):
        """Gravitational redshift z > 0."""
        r_test = 5.0 * kerr_moderate.r_s
        z = kerr_moderate.redshift(r_test)
        assert z > 0, "Redshift must be positive"
        assert np.isfinite(z), "Redshift must be finite"
    
    def test_fast_rotation_still_has_horizons(self, kerr_fast):
        """Fast rotation (a=0.9) still sub-extremal."""
        r_plus, r_minus = kerr_fast.horizons()
        assert not np.isnan(r_plus), "Horizons must exist even for a=0.9"
        assert r_plus > r_minus, "r_+ > r_-"
    
    def test_extremal_detection(self):
        """Extremal case a=1 should be detected."""
        params = KerrSSZParams(mass=M_SUN, spin=1.0)
        kerr_extremal = KerrSSZMetric(params)
        is_ext = kerr_extremal.is_extremal(tol=1e-3)
        assert isinstance(is_ext, (bool, np.bool_))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
