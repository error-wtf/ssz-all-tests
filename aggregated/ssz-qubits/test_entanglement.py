# -*- coding: utf-8 -*-
# =============================================================================
# SOURCE: ssz-qubits
# ORIGINAL PATH: E:\clone\ssz-qubits\tests\test_entanglement.py
# AGGREGATED: 2026-04-27T20:55:00
# =============================================================================

import numpy as np
import pytest
from ssz_qubits.core import Qubit, QubitPair, analyze_entangled_pair
from ssz_qubits.entanglement import (
    correction_interval, correction_gate, is_in_coherent_zone,
    characteristic_time_T_SSZ
)


class TestCharacteristicTime:
    """Test T_SSZ characteristic time calculations."""
    
    def test_T_SSZ_paper_value(self):
        """Paper B: T_SSZ ≈ 29 years for 1 mm separation."""
        T = characteristic_time_T_SSZ(1e-3)
        years = T / (365.25 * 24 * 3600)
        assert abs(years - 29) / 29 < 0.05
    
    def test_T_SSZ_scaling(self):
        """T_SSZ should scale inversely with height."""
        T_1mm = characteristic_time_T_SSZ(1e-3)
        T_10mm = characteristic_time_T_SSZ(10e-3)
        ratio = T_1mm / T_10mm
        assert abs(ratio - 10) / 10 < 0.01
    
    def test_T_SSZ_zero_height(self):
        """T_SSZ = inf when height difference is zero."""
        T = characteristic_time_T_SSZ(0)
        assert T == np.inf


class TestCorrectionInterval:
    """Test correction interval calculations."""
    
    def test_correction_interval_paper_value(self):
        """Paper B: N_corr ≈ 5.8e9 for 1 mm, eps = 1e-6."""
        phase_drift = 1.72e-16
        eps = 1e-6
        N = correction_interval(eps, phase_drift)
        expected = 5.8e9
        assert abs(N - expected) / expected < 0.1
    
    def test_correction_interval_zero_drift(self):
        """N_corr = inf when drift is zero."""
        N = correction_interval(1e-6, 0)
        assert N == np.inf


class TestCorrectionGate:
    """Test correction gate specification."""
    
    def test_correction_higher_A(self):
        """When A is higher, correct A with Rz(-phi)."""
        corr = correction_gate(1e-7, higher_qubit='A')
        assert corr['target_qubit'] == 'A'
        assert corr['rotation_angle'] == -1e-7
    
    def test_correction_higher_B(self):
        """When B is higher, correct B with Rz(+phi)."""
        corr = correction_gate(1e-7, higher_qubit='B')
        assert corr['target_qubit'] == 'B'
        assert corr['rotation_angle'] == 1e-7


class TestCoherentZone:
    """Test coherent zone membership."""
    
    def test_same_height_in_zone(self):
        """Qubits at same height are always in same zone."""
        q1 = Qubit(id='q1', x=0, y=0, z=0, gate_time=50e-9)
        q2 = Qubit(id='q2', x=1, y=0, z=0, gate_time=50e-9)
        pair = QubitPair(q1, q2)
        assert is_in_coherent_zone(pair, tolerance=1e-18)
    
    def test_small_separation_in_zone(self):
        """1 mm separation should be in 18 mm zone (eps=1e-18)."""
        q1 = Qubit(id='q1', x=0, y=0, z=0, gate_time=50e-9)
        q2 = Qubit(id='q2', x=0, y=0, z=1e-3, gate_time=50e-9)
        pair = QubitPair(q1, q2)
        assert is_in_coherent_zone(pair, tolerance=1e-18)
    
    def test_large_separation_out_of_zone(self):
        """100 mm separation should be outside 18 mm zone."""
        q1 = Qubit(id='q1', x=0, y=0, z=0, gate_time=50e-9)
        q2 = Qubit(id='q2', x=0, y=0, z=0.1, gate_time=50e-9)
        pair = QubitPair(q1, q2)
        assert not is_in_coherent_zone(pair, tolerance=1e-18)


class TestFullAnalysis:
    """Test complete entangled pair analysis."""
    
    def test_analysis_1mm(self):
        """Full analysis for 1 mm separation."""
        q1 = Qubit(id='q1', x=0, y=0, z=0, gate_time=50e-9)
        q2 = Qubit(id='q2', x=0, y=0, z=1e-3, gate_time=50e-9)
        pair = QubitPair(q1, q2)
        
        analysis = analyze_entangled_pair(pair, N_gates=10**9)
        
        assert abs(analysis.phase_drift_per_gate - 1.72e-16) / 1.72e-16 < 0.01
        assert abs(analysis.T_SSZ / (365.25*24*3600) - 29) / 29 < 0.05
        assert abs((1 - analysis.fidelity_after_N_gates) - 7.4e-15) / 7.4e-15 < 0.1
        assert analysis.in_coherent_zone == True


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
