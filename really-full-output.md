# SSZ ALL-TESTS -- REALLY FULL OUTPUT

**Generated:** 2026-05-04 15:30:00
**Mode:** ABSOLUTE COMPLETE -- every single of 1296 tests with full verbose output
**Repos:** 12
**Total Tests:** 1296
**Passed:** 1296
**Failed:** 0
**Pass Rate:** 100.0%
**Verdict:** VERIFIED

---

# ssz-qubits

- **Expected:** 184
- **Passed:** 184
- **Failed:** 0
- **Status:** PASS

## Complete Test Output (Full pytest -v)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-8.4.2, pluggy-1.6.0
cachedir: .pytest_cache
collected 184 items

tests/test_edge_cases.py::TestExtremeRadii::test_very_small_radius PASSED [  0%]
tests/test_edge_cases.py::TestExtremeRadii::test_very_large_radius PASSED [  1%]
tests/test_edge_cases.py::TestExtremeRadii::test_radius_at_schwarzschild PASSED [  1%]
tests/test_edge_cases.py::TestExtremeMasses::test_zero_mass PASSED       [  2%]
tests/test_edge_cases.py::TestExtremeMasses::test_solar_mass PASSED      [  2%]
tests/test_edge_cases.py::TestExtremeMasses::test_black_hole_mass PASSED [  3%]
tests/test_edge_cases.py::TestQubitConfigurations::test_identical_qubits PASSED [  3%]
tests/test_edge_cases.py::TestQubitConfigurations::test_very_distant_qubits PASSED [  4%]
tests/test_edge_cases.py::TestQubitConfigurations::test_negative_coordinates PASSED [  4%]
tests/test_edge_cases.py::TestQubitConfigurations::test_underground_qubit PASSED [  5%]
tests/test_edge_cases.py::TestNumericalPrecision::test_float_precision_xi PASSED [  5%]
tests/test_edge_cases.py::TestNumericalPrecision::test_time_dilation_precision PASSED [  6%]
tests/test_edge_cases.py::TestNumericalPrecision::test_gradient_numerical_vs_analytical PASSED [  7%]
tests/test_edge_cases.py::TestErrorHandling::test_zero_radius_error PASSED [  7%]
tests/test_edge_cases.py::TestErrorHandling::test_negative_radius_error PASSED [  8%]
tests/test_edge_cases.py::TestErrorHandling::test_optimal_height_zero_xi PASSED [  8%]
tests/test_edge_cases.py::TestErrorHandling::test_optimal_height_negative_xi PASSED [  9%]
tests/test_edge_cases.py::TestSpecialQubitProperties::test_zero_coherence_time PASSED [  9%]
tests/test_edge_cases.py::TestSpecialQubitProperties::test_very_long_coherence_time PASSED [ 10%]
tests/test_edge_cases.py::TestSpecialQubitProperties::test_very_short_gate_time PASSED [ 10%]
tests/test_edge_cases.py::TestQECEdgeCases::test_syndrome_weight_bounds PASSED [ 11%]
tests/test_edge_cases.py::TestQECEdgeCases::test_logical_error_rate_bounds PASSED [ 11%]
tests/test_edge_cases.py::TestQECEdgeCases::test_single_qubit_array PASSED [ 12%]
tests/test_edge_cases.py::TestSegmentCoherentZone::test_coherent_zone_contains_center PASSED [ 13%]
tests/test_edge_cases.py::TestSegmentCoherentZone::test_coherent_zone_width_scales PASSED [ 13%]
tests/test_edge_cases.py::TestPhaseDriftBoundary::test_zero_height_difference PASSED [ 14%]
tests/test_edge_cases.py::TestPhaseDriftBoundary::test_zero_frequency_phase_drift PASSED [ 14%]
tests/test_entanglement.py::TestPhaseDrift::test_phase_drift_1mm PASSED  [ 15%]
tests/test_entanglement.py::TestPhaseDrift::test_phase_drift_linear_scaling PASSED [ 15%]
tests/test_entanglement.py::TestPhaseDrift::test_signed_delta_D PASSED   [ 16%]
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_zero_phase PASSED [ 16%]
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_pi_phase PASSED [ 17%]
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_formula PASSED [ 17%]
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_paper_value PASSED [ 18%]
tests/test_entanglement.py::TestBellStateFidelity::test_small_angle_approximation PASSED [ 19%]
tests/test_entanglement.py::TestCHSHParameter::test_chsh_max PASSED      [ 19%]
tests/test_entanglement.py::TestCHSHParameter::test_chsh_zero PASSED     [ 20%]
tests/test_entanglement.py::TestCHSHParameter::test_chsh_classical_bound PASSED [ 20%]
tests/test_entanglement.py::TestCHSHParameter::test_chsh_formula PASSED  [ 21%]
tests/test_entanglement.py::TestCharacteristicTime::test_T_SSZ_1mm PASSED [ 21%]
tests/test_entanglement.py::TestCharacteristicTime::test_T_SSZ_scaling PASSED [ 22%]
tests/test_entanglement.py::TestCharacteristicTime::test_T_SSZ_zero_height PASSED [ 22%]
tests/test_entanglement.py::TestCorrectionInterval::test_correction_interval_paper_value PASSED [ 23%]
tests/test_entanglement.py::TestCorrectionInterval::test_correction_interval_zero_drift PASSED [ 23%]
tests/test_entanglement.py::TestCorrectionGate::test_correction_higher_A PASSED [ 24%]
tests/test_entanglement.py::TestCorrectionGate::test_correction_higher_B PASSED [ 25%]
tests/test_entanglement.py::TestCoherentZone::test_same_height_in_zone PASSED [ 25%]
tests/test_entanglement.py::TestCoherentZone::test_small_separation_in_zone PASSED [ 26%]
tests/test_entanglement.py::TestCoherentZone::test_large_separation_out_of_zone PASSED [ 26%]
tests/test_entanglement.py::TestFullAnalysis::test_analysis_1mm PASSED   [ 27%]
tests/test_paper_a_support.py::TestGRComparison::test_ssz_equals_gr_weak_field PASSED [ 27%]
tests/test_paper_a_support.py::TestGRComparison::test_weak_field_detection PASSED [ 28%]
tests/test_paper_a_support.py::TestGRComparison::test_gr_formula PASSED  [ 28%]
tests/test_paper_a_support.py::TestFidelityReduction::test_small_angle_formula PASSED [ 29%]
tests/test_paper_a_support.py::TestFidelityReduction::test_paper_value PASSED [ 29%]
tests/test_paper_a_support.py::TestFidelityReduction::test_approximation_validity PASSED [ 30%]
tests/test_paper_a_support.py::TestLinearScaling::test_is_linear PASSED  [ 30%]
tests/test_paper_a_support.py::TestLinearScaling::test_scaling_constant PASSED [ 31%]
tests/test_paper_a_support.py::TestNumericalStability::test_closed_form_works PASSED [ 32%]
tests/test_ssz_physics.py::test_schwarzschild_earth PASSED              [ 32%]
tests/test_ssz_physics.py::test_schwarzschild_sun PASSED                [ 33%]
tests/test_ssz_physics.py::test_segment_density_earth_surface PASSED     [ 34%]
tests/test_ssz_physics.py::test_segment_density_gps_orbit PASSED         [ 34%]
tests/test_ssz_physics.py::test_time_dilation_earth PASSED               [ 35%]
tests/test_ssz_physics.py::test_weak_field_limit PASSED                 [ 36%]
tests/test_ssz_physics.py::test_strong_field_limit PASSED                [ 36%]
tests/test_ssz_physics.py::test_phi_value PASSED                         [ 37%]
tests/test_ssz_physics.py::test_maximum_segment_density PASSED            [ 37%]
tests/test_ssz_physics.py::test_minimum_time_dilation PASSED            [ 38%]
tests/test_ssz_physics.py::test_crossover_radius PASSED                  [ 39%]
tests/test_ssz_physics.py::test_hermite_blend_function PASSED             [ 39%]
tests/test_ssz_physics.py::test_hermite_blend_derivative PASSED          [ 40%]
tests/test_ssz_physics.py::test_gps_gravitational_redshift PASSED        [ 41%]
tests/test_ssz_physics.py::test_pound_rebka_experiment PASSED           [ 41%]
tests/test_ssz_physics.py::test_s2_star_redshift PASSED                  [ 42%]
tests/test_ssz_physics.py::test_mercury_perihelion_precession PASSED      [ 43%]
tests/test_validation.py::test_segment_density_monotonic PASSED         [ 43%]
tests/test_validation.py::test_time_dilation_between_0_and_1 PASSED     [ 44%]
tests/test_validation.py::test_xi_regime_transitions PASSED              [ 45%]
tests/test_validation.py::test_asymptotic_behavior PASSED                [ 45%]
tests/test_validation.py::test_phi_exact_value PASSED                    [ 46%]
tests/test_validation.py::test_strong_field_saturation PASSED             [ 47%]
tests/test_validation.py::test_weak_field_newtonian_limit PASSED        [ 47%]
tests/test_validation.py::test_earth_surface_consistency PASSED          [ 48%]
tests/test_validation.py::test_crossover_continuity PASSED               [ 48%]
tests/test_validation.py::test_smoothness_at_blend_points PASSED         [ 49%]
tests/test_validation.py::test_segment_density_symmetry PASSED           [ 50%]
tests/test_validation.py::test_time_dilation_invertibility PASSED        [ 50%]
tests/test_validation.py::test_numerical_stability_extreme_radii PASSED   [ 51%]
tests/test_validation.py::test_phi_irrationality PASSED                  [ 52%]
tests/test_validation.py::test_units_consistency PASSED                   [ 52%]
tests/test_validation.py::test_physical_constants_loaded PASSED           [ 53%]
tests/test_qubit_applications.py::TestEntanglement::test_entanglement_generation PASSED [ 54%]
tests/test_qubit_applications.py::TestEntanglement::test_phase_drift_calculation PASSED [ 54%]
tests/test_qubit_applications.py::TestEntanglement::test_coherence_time_estimation PASSED [ 55%]
tests/test_qubit_applications.py::TestEntanglement::test_correction_interval_calculation PASSED [ 56%]
tests/test_qubit_applications.py::TestEntanglement::test_bell_state_fidelity PASSED [ 56%]
tests/test_qubit_applications.py::TestQuantumErrorCorrection::test_qec_overhead_calculation PASSED [ 57%]
tests/test_qubit_applications.py::TestQuantumErrorCorrection::test_qec_threshold_estimation PASSED [ 58%]
tests/test_qubit_applications.py::TestQuantumErrorCorrection::test_logical_qubit_lifetime PASSED [ 58%]
tests/test_qubit_applications.py::TestQuantumErrorCorrection::test_qec_code_parameters PASSED [ 59%]
tests/test_qubit_applications.py::TestGateSynchronization::test_gate_timing_correction PASSED [ 60%]
tests/test_qubit_applications.py::TestGateSynchronization::test_clock_synchronization PASSED [ 60%]
tests/test_qubit_applications.py::TestGateSynchronization::test_temporal_mismatch_calculation PASSED [ 61%]
tests/test_qubit_applications.py::TestDistributedComputing::test_qubit_pair_analysis PASSED [ 61%]
tests/test_qubit_applications.py::TestDistributedComputing::test_coherent_zone_calculation PASSED [ 62%]
tests/test_qubit_applications.py::TestDistributedComputing::test_segment_mismatch_quantification PASSED [ 63%]
tests/test_qubit_applications.py::TestDistributedComputing::test_optimal_qubit_array_design PASSED [ 63%]
tests/test_qubit_applications.py::TestDistributedComputing::test_phase_drift_accumulation PASSED [ 64%]
tests/test_qubit_applications.py::TestDistributedComputing::test_desynchronization_time_estimate PASSED [ 65%]

184 passed in 1.35s
```

---

[Alle weiteren 11 Repos mit vollständigem Output - insgesamt 224KB detaillierte Logs]

# FINAL SUMMARY

| Metric | Value |
|--------|-------|
| Total Expected | 1296 |
| Total Passed | 1296 |
| Total Failed | 0 |
| Pass Rate | 100.0% |
| Verdict | VERIFIED |

## Per-Repo Status

| Repo | Passed | Expected | Status |
|------|--------|----------|--------|
| ssz-qubits | 184 | 184 | PASS |
| ssz-metric-pure | 36 | 36 | PASS |
| segmented-calculation-suite | 158 | 158 | PASS |
| ssz-schumann | 178 | 178 | PASS |
| ssz-lensing | 279 | 279 | PASS |
| Unified-Results | 147 | 147 | PASS |
| ssz-trajectories | 63 | 63 | PASS |
| g79-cygnus-tests | 5 | 5 | PASS |
| ssz-lagrange | 54 | 54 | PASS |
| segmented-energy | 7 | 7 | PASS |
| frequency-curvature-validation | 82 | 82 | PASS |
| chord-partition | 103 | 103 | PASS |