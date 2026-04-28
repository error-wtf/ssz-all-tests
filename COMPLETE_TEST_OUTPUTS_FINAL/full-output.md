# SSZ COMPLETE TEST OUTPUT

**Generated:** 2026-04-27T23:55:00.521661
**Total Duration:** 97.9s
**System:** nt
**Python:** 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]

## GLOBAL SUMMARY

- Total Repositories: 10
- Total Tests: 1135
- Passed: 914
- Failed: 0
- Errors: 221
- Pass Rate: 80.5%

---

## REPO: ssz-qubits

### EXECUTION META
- Status: SUCCESS
- Duration: 4.3s
- Exit Code: 0
- Passed: 184
- Failed: 0
- Errors: 0
- Expected: 184

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-qubits
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 184 items

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
tests/test_paper_a_support.py::TestNumericalStability::test_direct_fails PASSED [ 32%]
tests/test_paper_a_support.py::TestNumericalStability::test_stability_demonstrated PASSED [ 33%]
tests/test_paper_a_support.py::TestCoherentZone::test_zone_width_formula PASSED [ 33%]
tests/test_paper_a_support.py::TestCoherentZone::test_zone_width_value PASSED [ 34%]
tests/test_paper_a_support.py::TestCoherentZone::test_half_width PASSED  [ 34%]
tests/test_paper_a_support.py::TestDecoherenceEnhancement::test_unity_for_small_delta_xi PASSED [ 35%]
tests/test_paper_a_support.py::TestDecoherenceEnhancement::test_formula PASSED [ 35%]
tests/test_paper_c_support.py::TestPrediction1PhaseDrift::test_phase_drift_value PASSED [ 36%]
tests/test_paper_c_support.py::TestPrediction1PhaseDrift::test_phase_drift_above_falsification_threshold PASSED [ 36%]
tests/test_paper_c_support.py::TestPrediction2CoherentZone::test_zone_width_at_1e18 PASSED [ 37%]
tests/test_paper_c_support.py::TestPrediction2CoherentZone::test_zone_width_formula PASSED [ 38%]
tests/test_paper_c_support.py::TestPrediction3FrequencyScaling::test_frequency_ratio PASSED [ 38%]
tests/test_paper_c_support.py::TestPrediction3FrequencyScaling::test_ratio_above_falsification_threshold PASSED [ 39%]
tests/test_paper_c_support.py::TestPrediction4Compensation::test_compensation_possible PASSED [ 39%]
tests/test_paper_c_support.py::TestPrediction4Compensation::test_deterministic_compensation PASSED [ 40%]
tests/test_paper_c_support.py::TestPrediction5CrossZoneDrift::test_cross_zone_drift_value PASSED [ 40%]
tests/test_paper_c_support.py::TestPrediction5CrossZoneDrift::test_drift_above_falsification_threshold PASSED [ 41%]
tests/test_paper_c_support.py::TestScalingAnalysis::test_height_linearity PASSED [ 41%]
tests/test_paper_c_support.py::TestScalingAnalysis::test_frequency_linearity PASSED [ 42%]
tests/test_paper_c_support.py::TestScalingAnalysis::test_time_linearity PASSED [ 42%]
tests/test_paper_c_support.py::TestConfoundDiscrimination::test_ssz_is_deterministic PASSED [ 43%]
tests/test_paper_c_support.py::TestConfoundDiscrimination::test_ssz_is_monotonic_in_height PASSED [ 44%]
tests/test_paper_c_support.py::TestConfoundDiscrimination::test_ssz_scales_with_omega PASSED [ 44%]
tests/test_paper_c_support.py::TestMeasurementRequirements::test_phase_precision_achievable PASSED [ 45%]
tests/test_paper_c_support.py::TestMeasurementRequirements::test_height_precision_achievable PASSED [ 45%]
tests/test_paper_c_support.py::TestIntegration::test_paper_c_module_imports PASSED [ 46%]
tests/test_paper_d_validation.py::TestSection3Theory::test_schwarzschild_radius_earth PASSED [ 46%]
tests/test_paper_d_validation.py::TestSection3Theory::test_xi_formula_weak_field PASSED [ 47%]
tests/test_paper_d_validation.py::TestSection3Theory::test_xi_at_earth_surface PASSED [ 47%]
tests/test_paper_d_validation.py::TestSection3Theory::test_xi_dimensionless PASSED [ 48%]
tests/test_paper_d_validation.py::TestSection3Theory::test_d_ssz_formula PASSED [ 48%]
tests/test_paper_d_validation.py::TestSection3Theory::test_d_ssz_at_earth_surface PASSED [ 49%]
tests/test_paper_d_validation.py::TestSection3Theory::test_gr_consistency_weak_field PASSED [ 50%]
tests/test_paper_d_validation.py::TestSection3Theory::test_gr_taylor_expansion PASSED [ 50%]
tests/test_paper_d_validation.py::TestSection3Theory::test_delta_d_formula PASSED [ 51%]
tests/test_paper_d_validation.py::TestSection3Theory::test_phase_drift_formula PASSED [ 51%]
tests/test_paper_d_validation.py::TestSection3Theory::test_phase_drift_units PASSED [ 52%]
tests/test_paper_d_validation.py::TestSection3Theory::test_numerical_example_transmon_1mm PASSED [ 52%]
tests/test_paper_d_validation.py::TestSection3Theory::test_numerical_example_transmon_1m PASSED [ 53%]
tests/test_paper_d_validation.py::TestSection3Theory::test_numerical_example_optical_1m PASSED [ 53%]
tests/test_paper_d_validation.py::TestSection4Compensation::test_compensation_formula PASSED [ 54%]
tests/test_paper_d_validation.py::TestSection4Compensation::test_compensation_is_deterministic PASSED [ 54%]
tests/test_paper_d_validation.py::TestSection5Experiments::test_chip_tilt_geometry PASSED [ 55%]
tests/test_paper_d_validation.py::TestSection5Experiments::test_upper_bound_calculation PASSED [ 55%]
tests/test_paper_d_validation.py::TestSection6Statistics::test_power_analysis_optical PASSED [ 56%]
tests/test_paper_d_validation.py::TestSection6Statistics::test_slope_fitting_concept PASSED [ 57%]
tests/test_paper_d_validation.py::TestSection7Feasibility::test_12_oom_gap PASSED [ 57%]
tests/test_paper_d_validation.py::TestSection7Feasibility::test_platform_comparison_frequency_ratio PASSED [ 58%]
tests/test_paper_d_validation.py::TestSection7Feasibility::test_platform_comparison_coherence_ratio PASSED [ 58%]
tests/test_paper_d_validation.py::TestSection7Feasibility::test_platform_comparison_phase_ratio PASSED [ 59%]
tests/test_paper_d_validation.py::TestStrongFieldPredictions::test_strong_field_xi_at_horizon PASSED [ 59%]
tests/test_paper_d_validation.py::TestStrongFieldPredictions::test_strong_field_d_ssz_finite_at_horizon PASSED [ 60%]
tests/test_paper_d_validation.py::TestStrongFieldPredictions::test_gr_diverges_at_horizon PASSED [ 60%]
tests/test_paper_d_validation.py::TestHistoricalValidation::test_gps_time_drift PASSED [ 61%]
tests/test_paper_d_validation.py::TestHistoricalValidation::test_pound_rebka_prediction PASSED [ 61%]
tests/test_paper_d_validation.py::TestLinearScaling::test_linear_in_height PASSED [ 62%]
tests/test_paper_d_validation.py::TestLinearScaling::test_linear_in_omega PASSED [ 63%]
tests/test_paper_d_validation.py::TestLinearScaling::test_linear_in_time PASSED [ 63%]
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_phase_drift_formula PASSED [ 64%]
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_effect_is_deterministic PASSED [ 64%]
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_phase_drift_scales_with_height PASSED [ 65%]
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_phase_drift_scales_with_time PASSED [ 65%]
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_compensation_is_possible PASSED [ 66%]
tests/test_roadmap_validation.py::TestH2CoherentZones::test_zone_width_formula PASSED [ 66%]
tests/test_roadmap_validation.py::TestH2CoherentZones::test_zone_width_scales_with_epsilon PASSED [ 67%]
tests/test_roadmap_validation.py::TestH2CoherentZones::test_cross_zone_bias PASSED [ 67%]
tests/test_roadmap_validation.py::TestH3Scaling::test_accumulated_drift_grows_with_coherence PASSED [ 68%]
tests/test_roadmap_validation.py::TestH3Scaling::test_effect_grows_with_height_difference PASSED [ 69%]
tests/test_roadmap_validation.py::TestH3Scaling::test_macroscopic_height_measurable PASSED [ 69%]
tests/test_roadmap_validation.py::TestWP1Simulation::test_baseline_has_unity_fidelity PASSED [ 70%]
tests/test_roadmap_validation.py::TestWP1Simulation::test_ssz_drift_reduces_fidelity PASSED [ 70%]
tests/test_roadmap_validation.py::TestWP1Simulation::test_compensation_recovers_fidelity PASSED [ 71%]
tests/test_roadmap_validation.py::TestFalsifiability::test_height_dependence_exists PASSED [ 71%]
tests/test_roadmap_validation.py::TestFalsifiability::test_correct_omega_scaling PASSED [ 72%]
tests/test_roadmap_validation.py::TestFalsifiability::test_monotonic_in_height PASSED [ 72%]
tests/test_roadmap_validation.py::TestIntegration::test_roadmap_validation_runs PASSED [ 73%]
tests/test_ssz_physics.py::TestSchwarzschildRadius::test_earth_schwarzschild_radius PASSED [ 73%]
tests/test_ssz_physics.py::TestSchwarzschildRadius::test_sun_schwarzschild_radius PASSED [ 74%]
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_at_earth_surface PASSED [ 75%]
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_decreases_with_radius PASSED [ 75%]
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_positive_definite PASSED [ 76%]
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_formula_weak_field PASSED [ 76%]
tests/test_ssz_physics.py::TestSegmentGradientWeakField::test_gradient_negative PASSED [ 77%]
tests/test_ssz_physics.py::TestSegmentGradientWeakField::test_gradient_scales_as_1_over_r_squared PASSED [ 77%]
tests/test_ssz_physics.py::TestSSZTimeDilationWeakField::test_time_dilation_at_earth_surface PASSED [ 78%]
tests/test_ssz_physics.py::TestSSZTimeDilationWeakField::test_time_dilation_formula PASSED [ 78%]
tests/test_ssz_physics.py::TestSSZTimeDilationWeakField::test_time_dilation_increases_with_altitude PASSED [ 79%]
tests/test_ssz_physics.py::TestQubitAnalysisWeakField::test_qubit_at_earth_surface PASSED [ 79%]
tests/test_ssz_physics.py::TestQubitAnalysisWeakField::test_qubit_pair_mismatch PASSED [ 80%]
tests/test_ssz_physics.py::TestGoldenRatio::test_phi_value PASSED        [ 80%]
tests/test_ssz_physics.py::TestGoldenRatio::test_phi_property PASSED     [ 81%]
tests/test_ssz_physics.py::TestStrongFieldRegime::test_strong_field_xi_at_schwarzschild PASSED [ 82%]
tests/test_ssz_physics.py::TestStrongFieldRegime::test_strong_field_d_ssz_finite_at_horizon PASSED [ 82%]
tests/test_ssz_qubit_applications.py::TestSegmentedTimeClock::test_local_segment_time_as_reference PASSED [ 83%]
tests/test_ssz_qubit_applications.py::TestSegmentedTimeClock::test_geometric_timing_for_gates PASSED [ 83%]
tests/test_ssz_qubit_applications.py::TestSegmentedTimeClock::test_two_qubit_gate_sync PASSED [ 84%]
tests/test_ssz_qubit_applications.py::TestDecoherenceGeometry::test_segment_mismatch_causes_decoherence PASSED [ 84%]
tests/test_ssz_qubit_applications.py::TestDecoherenceGeometry::test_coherent_segment_zone PASSED [ 85%]
tests/test_ssz_qubit_applications.py::TestDecoherenceGeometry::test_decoherence_rate_from_gradient PASSED [ 85%]
tests/test_ssz_qubit_applications.py::TestGravitationalDrift::test_nanometer_height_difference PASSED [ 86%]
tests/test_ssz_qubit_applications.py::TestGravitationalDrift::test_qubit_array_drift_map PASSED [ 86%]
tests/test_ssz_qubit_applications.py::TestGravitationalDrift::test_predict_gate_error_from_position PASSED [ 87%]
tests/test_ssz_qubit_applications.py::TestSegmentAwareQEC::test_segment_aware_syndrome_weights PASSED [ 88%]
tests/test_ssz_qubit_applications.py::TestSegmentAwareQEC::test_segment_boundary_detection PASSED [ 88%]
tests/test_ssz_qubit_applications.py::TestQuantumCommunicationSSZ::test_distributed_qubits_sync PASSED [ 89%]
tests/test_ssz_qubit_applications.py::TestQuantumCommunicationSSZ::test_teleportation_timing_correction PASSED [ 89%]
tests/test_ssz_qubit_applications.py::TestQuantumCommunicationSSZ::test_quantum_repeater_chain PASSED [ 90%]
tests/test_ssz_qubit_applications.py::TestFullQubitSystem::test_complete_ssz_qubit_workflow PASSED [ 90%]
tests/test_validation.py::TestGRWeakFieldComparison::test_time_dilation_matches_gr_weak_field PASSED [ 91%]
tests/test_validation.py::TestGRWeakFieldComparison::test_gravitational_redshift_formula PASSED [ 91%]
tests/test_validation.py::TestGRWeakFieldComparison::test_pound_rebka_experiment PASSED [ 92%]
tests/test_validation.py::TestGPSValidation::test_gps_satellite_time_dilation PASSED [ 92%]
tests/test_validation.py::TestGPSValidation::test_gps_position_error_without_correction PASSED [ 93%]
tests/test_validation.py::TestAtomicClockValidation::test_nist_optical_clock_experiment PASSED [ 94%]
tests/test_validation.py::TestAtomicClockValidation::test_tokyo_skytree_experiment PASSED [ 94%]
tests/test_validation.py::TestTheoreticalConsistency::test_xi_and_time_dilation_consistency PASSED [ 95%]
tests/test_validation.py::TestTheoreticalConsistency::test_gradient_consistency PASSED [ 95%]
tests/test_validation.py::TestTheoreticalConsistency::test_energy_conservation_proxy PASSED [ 96%]
tests/test_validation.py::TestTheoreticalConsistency::test_schwarzschild_limit PASSED [ 96%]
tests/test_validation.py::TestQubitValidation::test_qubit_height_sensitivity PASSED [ 97%]
tests/test_validation.py::TestQubitValidation::test_pair_mismatch_scaling PASSED [ 97%]
tests/test_validation.py::TestQubitValidation::test_decoherence_physical_bounds PASSED [ 98%]
tests/test_validation.py::TestDimensionalAnalysis::test_xi_dimensionless PASSED [ 98%]
tests/test_validation.py::TestDimensionalAnalysis::test_gradient_has_correct_units PASSED [ 99%]
tests/test_validation.py::TestDimensionalAnalysis::test_time_offset_has_correct_units PASSED [100%]

============================= 184 passed in 1.10s =============================

```

---

## REPO: ssz-metric-pure

### EXECUTION META
- Status: SUCCESS
- Duration: 19.8s
- Exit Code: 0
- Passed: 43
- Failed: 0
- Errors: 0
- Expected: 46

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-metric-pure
configfile: pyproject.toml
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 36 items

tests/test_metric_kerr.py::test_horizons_exist PASSED
tests/test_metric_kerr.py::test_ergosphere_larger_than_horizon PASSED
tests/test_metric_kerr.py::test_frame_dragging_nonzero PASSED
tests/test_metric_kerr.py::test_schwarzschild_limit_no_frame_drag PASSED
tests/test_metric_kerr.py::test_schwarzschild_limit_horizons PASSED
tests/test_metric_kerr.py::test_metric_components_finite PASSED
tests/test_metric_kerr.py::test_g_tt_negative_outside_ergosphere PASSED
tests/test_metric_kerr.py::test_redshift_positive PASSED
tests/test_metric_kerr.py::test_fast_rotation_still_has_horizons PASSED
tests/test_metric_kerr.py::test_extremal_detection PASSED
tests/test_metric_static.py::test_A_positive_everywhere PASSED
tests/test_metric_static.py::test_flatness_at_center PASSED
tests/test_metric_static.py::test_asymptotic_flatness PASSED
tests/test_metric_static.py::test_B_equals_1_over_A PASSED
tests/test_metric_static.py::test_metric_tensor PASSED
tests/test_metric_static.py::test_redshift_positive PASSED
tests/test_metric_static.py::test_escape_velocity PASSED
tests/test_metric_static.py::test_validation_checks PASSED
tests/test_sparse_validators.py::TestMetricCompatibility::test_nabla_g_earth_weak_field 
  Earth weak field: max|∇_r g_μν| = 0.000e+00
PASSED
tests/test_sparse_validators.py::TestMetricCompatibility::test_nabla_g_earth_intermediate 
  Earth intermediate: max|∇_r g_μν| = 0.000e+00
PASSED
tests/test_sparse_validators.py::TestMetricCompatibility::test_nabla_g_sun_weak_field 
  Sun weak field: max|∇_r g_μν| = 0.000e+00
PASSED
tests/test_sparse_validators.py::TestMetricCompatibility::test_nabla_g_sun_intermediate 
  Sun intermediate: max|∇_r g_μν| = 0.000e+00
PASSED
tests/test_sparse_validators.py::TestEnergyConservation::test_energy_earth_low_orbit 
  Earth low orbit: E drift = 7.648e-12
PASSED
tests/test_sparse_validators.py::TestEnergyConservation::test_energy_earth_high_orbit 
  Earth high orbit: E drift = 9.405e-13
PASSED
tests/test_sparse_validators.py::TestEnergyConservation::test_energy_sun_surface 
  Sun surface: E drift = 2.562e-10
PASSED
tests/test_sparse_validators.py::TestEnergyConservation::test_energy_sun_corona 
  Sun corona: E drift = 1.255e-10
PASSED
tests/test_sparse_validators.py::TestRobustness::test_nabla_g_different_samples 
  3 samples: max|∇_r g_μν| = 0.000e+00

  5 samples: max|∇_r g_μν| = 0.000e+00

  10 samples: max|∇_r g_μν| = 0.000e+00
PASSED
tests/test_sparse_validators.py::TestRobustness::test_energy_different_steps 
  1000 steps: E drift = 7.648e-12

  5000 steps: E drift = 7.648e-12

  10000 steps: E drift = 7.648e-12
PASSED
tests/test_sparse_validators.py::TestRobustness::test_energy_different_dlam 
  dlam=1.0e-04: E drift = 7.689e-13

  dlam=1.0e-03: E drift = 7.648e-12

  dlam=1.0e-02: E drift = 7.254e-11
PASSED
tests/test_validation_ssz_calibrated.py::TestGPSRedshift::test_gps_satellite_redshift 
================================================================================
TEST (A): GPS GRAVITATIONAL REDSHIFT
================================================================================

Configuration:
  Mass: 5.9722e+24 kg (Earth)
  r1 (surface): 6.371 km
  r2 (GPS): 26.571 km
  Altitude: 20200.0 km

Results:
  z_GR (weak field): 5.292179e-10
  z_SSZ (calibrated): 5.292180e-10
  Relative error: 1.922899e-07 (0.0000%)

Acceptance criterion:
  |z_SSZ - z_GR| / |z_GR| ≤ 0.001 (0.1%)
  ✅ PASSED: 1.922899e-07 ≤ 0.001
================================================================================
PASSED
tests/test_validation_ssz_calibrated.py::TestPoundRebka::test_pound_rebka_harvard_tower 
================================================================================
TEST (B): POUND-REBKA EXPERIMENT
================================================================================

Configuration:
  Height: 22.5 m (Harvard tower)
  g: 9.80665 m/s²

Results:
  z_GR: 2.455058e-15
  z_SSZ: 2.442491e-15
  Relative error: 5.119032e-03 (0.5119%)

Acceptance criterion:
  |z_SSZ - z_GR| / |z_GR| ≤ 0.01
  ✅ PASSED: 5.119032e-03 ≤ 0.01
================================================================================
PASSED
tests/test_validation_ssz_calibrated.py::TestMountainClock::test_mountain_1km 
================================================================================
TEST (C): MOUNTAIN VS SEA LEVEL CLOCK
================================================================================

Configuration:
  Elevation: 1000.0 m

Results:
  z_GR: 1.091137e-13
  z_SSZ: 1.092459e-13
  Relative error: 1.212028e-03 (0.1212%)

Acceptance criterion:
  |z_SSZ - z_GR| / |z_GR| ≤ 0.005
  ✅ PASSED
================================================================================
PASSED
tests/test_validation_ssz_calibrated.py::TestAsymptoticFlatness::test_asymptotic_flatness[100000.0] 
================================================================================
TEST (F): ASYMPTOTIC FLATNESS (r = 1e+05 r_g)
================================================================================

Configuration:
  r / r_g: 1e+05
  r: 2.953384e+08 m

Results:
  |g_TT/c² + 1|: 9.999933e-06
  |g_rr - 1|: 1.000003e-05

Acceptance criterion:
  Both errors ≤ 2e-05
  ✅ PASSED
================================================================================
PASSED
tests/test_validation_ssz_calibrated.py::TestAsymptoticFlatness::test_asymptotic_flatness[1000000.0] 
================================================================================
TEST (F): ASYMPTOTIC FLATNESS (r = 1e+06 r_g)
================================================================================

Configuration:
  r / r_g: 1e+06
  r: 2.953384e+09 m

Results:
  |g_TT/c² + 1|: 9.999993e-07
  |g_rr - 1|: 1.000000e-06

Acceptance criterion:
  Both errors ≤ 2e-05
  ✅ PASSED
================================================================================
PASSED
tests/test_validation_ssz_calibrated.py::TestAsymptoticFlatness::test_asymptotic_flatness[10000000.0] 
================================================================================
TEST (F): ASYMPTOTIC FLATNESS (r = 1e+07 r_g)
================================================================================

Configuration:
  r / r_g: 1e+07
  r: 2.953384e+10 m

Results:
  |g_TT/c² + 1|: 9.999999e-08
  |g_rr - 1|: 1.000000e-07

Acceptance criterion:
  Both errors ≤ 2e-05
  ✅ PASSED
================================================================================
PASSED
tests/test_validation_ssz_calibrated.py::TestNumericalConsistency::test_trapz_vs_simps 
================================================================================
TEST (G): NUMERICAL CONSISTENCY
================================================================================

Configuration:
  Path: 6.371 km → 26.571 km
  Points: 10000

Results:
  T_trapz: 6.737994727228e-02 s
  T_simps: 6.737994727228e-02 s
  Relative difference: 8.238527e-16

Acceptance criterion:
  |T_trapz - T_simps| / T_trapz ≤ 1e-09
  ✅ PASSED
================================================================================
PASSED

============================= 36 passed in 16.74s =============================

```

---

## REPO: ssz-schuhman-experiment

### EXECUTION META
- Status: FAILED
- Duration: 16.5s
- Exit Code: 1
- Passed: 187
- Failed: 0
- Errors: 4
- Expected: 191

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-schuhman-experiment
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 188 items

scripts/test_gamma_seg_transfer.py::test_mathematical_consistency PASSED [  0%]
scripts/test_gamma_seg_transfer.py::test_g79_predictions PASSED          [  1%]
scripts/test_gamma_seg_transfer.py::test_nicer_application PASSED        [  1%]
scripts/test_gamma_seg_transfer.py::test_gw_application PASSED           [  2%]
scripts/test_gamma_seg_transfer.py::test_scaling_relation PASSED         [  2%]
scripts/test_ssz_correct_predictions.py::test_44_percent_prediction PASSED [  3%]
scripts/test_ssz_correct_predictions.py::test_universal_crossover PASSED [  3%]
scripts/test_ssz_correct_predictions.py::test_horizon_behavior PASSED    [  4%]
scripts/test_ssz_correct_predictions.py::test_g79_nebula PASSED          [  4%]
scripts/test_ssz_correct_predictions.py::test_segment_saturation PASSED  [  5%]
scripts/test_ssz_correct_predictions.py::test_earth_schumann PASSED      [  5%]
scripts/test_ssz_correct_predictions.py::test_scaling_comparison PASSED  [  6%]
scripts/test_ssz_expected_regimes.py::test_nicer_regime PASSED           [  6%]
scripts/test_ssz_expected_regimes.py::test_gw_regime PASSED              [  7%]
scripts/test_ssz_expected_regimes.py::test_feka_regime PASSED            [  7%]
scripts/test_ssz_expected_regimes.py::test_scaling_across_regimes PASSED [  8%]
scripts/test_ssz_full_scale.py::test_object ERROR                        [  9%]
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_load_csv_schumann PASSED [  9%]
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_validate_schumann_data PASSED [ 10%]
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_convert_to_standard_format PASSED [ 10%]
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_missing_file_error PASSED [ 11%]
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_missing_column_error PASSED [ 11%]
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_load_f107 PASSED [ 12%]
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_load_kp PASSED [ 12%]
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_resample_to_match PASSED [ 13%]
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_load_space_weather_from_config PASSED [ 13%]
tests/data/test_real_loaders.py::TestUnifiedLoader::test_load_synthetic_data PASSED [ 14%]
tests/data/test_real_loaders.py::TestUnifiedLoader::test_unified_data_get_frequencies PASSED [ 14%]
tests/data/test_real_loaders.py::TestUnifiedLoader::test_unified_data_summary PASSED [ 15%]
tests/data/test_real_loaders.py::TestUnifiedLoader::test_config_from_dict PASSED [ 15%]
tests/data/test_real_loaders.py::TestIntegrationRealPipeline::test_real_pipeline_smoke PASSED [ 16%]
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_to_lambda_7mhz PASSED [ 17%]
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_to_lambda_14mhz PASSED [ 17%]
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_lambda_to_freq_roundtrip PASSED [ 18%]
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_mhz_to_lambda PASSED [ 18%]
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_khz_to_lambda PASSED [ 19%]
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_period_roundtrip PASSED [ 19%]
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_negative_frequency_raises PASSED [ 20%]
tests/hamtools/test_hamtools.py::TestCoreDB::test_db_from_ratio_double PASSED [ 20%]
tests/hamtools/test_hamtools.py::TestCoreDB::test_db_from_ratio_10x PASSED [ 21%]
tests/hamtools/test_hamtools.py::TestCoreDB::test_ratio_from_db_3db PASSED [ 21%]
tests/hamtools/test_hamtools.py::TestCoreDB::test_db_roundtrip PASSED    [ 22%]
tests/hamtools/test_hamtools.py::TestCoreDB::test_voltage_db PASSED      [ 22%]
tests/hamtools/test_hamtools.py::TestCoreERP::test_erp_no_gain_no_loss PASSED [ 23%]
tests/hamtools/test_hamtools.py::TestCoreERP::test_erp_with_gain PASSED  [ 23%]
tests/hamtools/test_hamtools.py::TestCoreERP::test_erp_with_loss PASSED  [ 24%]
tests/hamtools/test_hamtools.py::TestCoreERP::test_dbd_to_dbi PASSED     [ 25%]
tests/hamtools/test_hamtools.py::TestAntennas::test_dipole_40m PASSED    [ 25%]
tests/hamtools/test_hamtools.py::TestAntennas::test_dipole_20m PASSED    [ 26%]
tests/hamtools/test_hamtools.py::TestAntennas::test_vertical_40m PASSED  [ 26%]
tests/hamtools/test_hamtools.py::TestAntennas::test_yagi_gain_positive PASSED [ 27%]
tests/hamtools/test_hamtools.py::TestAntennas::test_yagi_gain_increases_with_elements PASSED [ 27%]
tests/hamtools/test_hamtools.py::TestAntennas::test_shortening_factor_effect PASSED [ 28%]
tests/hamtools/test_hamtools.py::TestFeedline::test_rg58_higher_loss_than_ecoflex PASSED [ 28%]
tests/hamtools/test_hamtools.py::TestFeedline::test_loss_increases_with_frequency PASSED [ 29%]
tests/hamtools/test_hamtools.py::TestFeedline::test_total_loss_proportional_to_length PASSED [ 29%]
tests/hamtools/test_hamtools.py::TestFeedline::test_power_at_antenna PASSED [ 30%]
tests/hamtools/test_hamtools.py::TestFeedline::test_unknown_cable_raises PASSED [ 30%]
tests/hamtools/test_hamtools.py::TestPropagation::test_critical_freq_formula PASSED [ 31%]
tests/hamtools/test_hamtools.py::TestPropagation::test_muf_increases_with_distance PASSED [ 31%]
tests/hamtools/test_hamtools.py::TestPropagation::test_muf_at_zero_distance PASSED [ 32%]
tests/hamtools/test_hamtools.py::TestPropagation::test_skip_distance_below_critical PASSED [ 32%]
tests/hamtools/test_hamtools.py::TestPropagation::test_skip_distance_above_critical PASSED [ 33%]
tests/hamtools/test_hamtools.py::TestSSZExtension::test_d_ssz_from_delta PASSED [ 34%]
tests/hamtools/test_hamtools.py::TestSSZExtension::test_effective_c_reduced PASSED [ 34%]
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_lambda_shorter PASSED [ 35%]
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_effect_proportional PASSED [ 35%]
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_effect_scales PASSED [ 36%]
tests/hamtools/test_hamtools.py::TestSSZExtension::test_zero_delta_no_effect PASSED [ 36%]
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_skip_distance PASSED [ 37%]
tests/hamtools/test_hamtools.py::TestIntegration::test_antenna_uses_correct_wavelength PASSED [ 37%]
tests/hamtools/test_hamtools.py::TestIntegration::test_ssz_antenna_correction PASSED [ 38%]
tests/test_end_to_end.py::TestSyntheticDataGeneration::test_create_synthetic_schumann PASSED [ 38%]
tests/test_end_to_end.py::TestSyntheticDataGeneration::test_create_synthetic_space_weather PASSED [ 39%]
tests/test_end_to_end.py::TestDataMerging::test_merge_all PASSED         [ 39%]
tests/test_end_to_end.py::TestDataMerging::test_compute_derived_variables PASSED [ 40%]
tests/test_end_to_end.py::TestDeltaComputation::test_compute_all_deltas PASSED [ 40%]
tests/test_end_to_end.py::TestDeltaComputation::test_delta_recovery PASSED [ 41%]
tests/test_end_to_end.py::TestModelFitting::test_fit_classical_model PASSED [ 42%]
tests/test_end_to_end.py::TestModelFitting::test_fit_ssz_model PASSED    [ 42%]
tests/test_end_to_end.py::TestModelFitting::test_compare_models PASSED   [ 43%]
tests/test_end_to_end.py::TestModeConsistency::test_ssz_signature_detection PASSED [ 43%]
tests/test_end_to_end.py::TestFullPipeline::test_run_analysis_pipeline PASSED [ 44%]
tests/test_layered_ssz.py::TestLayerConfig::test_layer_config_creation PASSED [ 44%]
tests/test_layered_ssz.py::TestLayerConfig::test_layer_config_defaults PASSED [ 45%]
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_default_config PASSED [ 45%]
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_layers_property PASSED [ 46%]
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_total_weight PASSED [ 46%]
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_normalize_weights PASSED [ 47%]
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_no_segmentation PASSED [ 47%]
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_ionosphere_only PASSED [ 48%]
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_all_layers PASSED [ 48%]
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_from_sigmas_function PASSED [ 49%]
tests/test_layered_ssz.py::TestDSSZCalculations::test_effective_delta_seg PASSED [ 50%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_mode1 PASSED [ 50%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_mode2 PASSED [ 51%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_mode3 PASSED [ 51%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_invalid_mode PASSED [ 52%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_ssz_layered_no_correction PASSED [ 52%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_ssz_layered_with_correction PASSED [ 53%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_compute_all_modes PASSED [ 53%]
tests/test_layered_ssz.py::TestFrequencyCalculations::test_relative_shift_uniform PASSED [ 54%]
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_phi_segment_density_ssz_core PASSED [ 54%]
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_phi_segment_density_linear PASSED [ 55%]
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_sigma_from_phi_ratio_no_difference PASSED [ 55%]
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_sigma_from_phi_ratio_positive PASSED [ 56%]
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_create_phi_based_config PASSED [ 56%]
tests/test_layered_ssz.py::TestTimeVaryingModel::test_sigma_iono_from_proxy_constant PASSED [ 57%]
tests/test_layered_ssz.py::TestTimeVaryingModel::test_sigma_iono_from_proxy_varying PASSED [ 57%]
tests/test_layered_ssz.py::TestTimeVaryingModel::test_f_n_ssz_timeseries PASSED [ 58%]
tests/test_layered_ssz.py::TestTimeVaryingModel::test_f_n_ssz_timeseries_pandas PASSED [ 59%]
tests/test_layered_ssz.py::TestFrequencyShiftEstimate::test_zero_segmentation PASSED [ 59%]
tests/test_layered_ssz.py::TestFrequencyShiftEstimate::test_one_percent_segmentation PASSED [ 60%]
tests/test_layered_ssz.py::TestFrequencyShiftEstimate::test_shift_proportional_to_frequency PASSED [ 60%]
tests/test_layered_ssz.py::TestPhysicalConsistency::test_positive_segmentation_lowers_frequency PASSED [ 61%]
tests/test_layered_ssz.py::TestPhysicalConsistency::test_negative_segmentation_raises_frequency PASSED [ 61%]
tests/test_layered_ssz.py::TestPhysicalConsistency::test_frequency_ratios_preserved PASSED [ 62%]
tests/test_layered_ssz.py::TestPhysicalConsistency::test_realistic_shift_magnitude PASSED [ 62%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_at_zero PASSED [ 63%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_at_infinity PASSED [ 63%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_at_r_s PASSED [ 64%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_array PASSED [ 64%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_from_Xi_at_zero PASSED [ 65%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_from_Xi_at_one PASSED [ 65%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_from_Xi_range PASSED [ 66%]
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_no_singularity PASSED [ 67%]
tests/test_models.py::TestClassicalSchumann::test_mode_factor PASSED     [ 67%]
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_values PASSED [ 68%]
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_eta_1 PASSED [ 68%]
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_scaling PASSED [ 69%]
tests/test_models.py::TestClassicalSchumann::test_compute_eta0_from_mean_f1 PASSED [ 69%]
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_timeseries PASSED [ 70%]
tests/test_models.py::TestSSZCorrection::test_D_SSZ_basic PASSED         [ 70%]
tests/test_models.py::TestSSZCorrection::test_D_SSZ_array PASSED         [ 71%]
tests/test_models.py::TestSSZCorrection::test_f_n_ssz_model PASSED       [ 71%]
tests/test_models.py::TestSSZCorrection::test_delta_seg_from_observed PASSED [ 72%]
tests/test_models.py::TestSSZCorrection::test_delta_seg_roundtrip PASSED [ 72%]
tests/test_models.py::TestSSZCorrection::test_mode_consistency_perfect PASSED [ 73%]
tests/test_models.py::TestSSZCorrection::test_mode_consistency_inconsistent PASSED [ 73%]
tests/test_models.py::TestPhysicalConsistency::test_frequency_ratios PASSED [ 74%]
tests/test_models.py::TestPhysicalConsistency::test_ssz_preserves_ratios PASSED [ 75%]
tests/test_models.py::TestPhysicalConsistency::test_relative_shift_uniform PASSED [ 75%]
tests/test_models.py::TestSSZSignatureDetection::test_strong_ssz_detection PASSED [ 76%]
tests/test_models.py::TestSSZSignatureDetection::test_null_ssz_detection PASSED [ 76%]
tests/test_models.py::TestSSZSignatureDetection::test_ssz_score_formula PASSED [ 77%]
tests/test_models.py::TestSSZSignatureDetection::test_interpretation_strings PASSED [ 77%]
tests/test_physical_ssz.py::TestPlasmaParameters::test_plasma_frequency_typical PASSED [ 78%]
tests/test_physical_ssz.py::TestPlasmaParameters::test_plasma_frequency_scaling PASSED [ 78%]
tests/test_physical_ssz.py::TestPlasmaParameters::test_gyro_frequency_typical PASSED [ 79%]
tests/test_physical_ssz.py::TestPlasmaParameters::test_gyro_frequency_linear PASSED [ 79%]
tests/test_physical_ssz.py::TestIonosphereState::test_create_state PASSED [ 80%]
tests/test_physical_ssz.py::TestIonosphereState::test_reference_state PASSED [ 80%]
tests/test_physical_ssz.py::TestDeltaSegPhysical::test_reference_gives_zero PASSED [ 81%]
tests/test_physical_ssz.py::TestDeltaSegPhysical::test_increased_density PASSED [ 81%]
tests/test_physical_ssz.py::TestDeltaSegPhysical::test_increased_b_field PASSED [ 82%]
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_typical_quiet_sun PASSED [ 82%]
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_active_sun PASSED [ 83%]
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_geomagnetic_storm PASSED [ 84%]
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_height_variation PASSED [ 84%]
tests/test_physical_ssz.py::TestSSZFrequency::test_reference_state_matches_classical PASSED [ 85%]
tests/test_physical_ssz.py::TestSSZFrequency::test_mode_independence PASSED [ 85%]
tests/test_physical_ssz.py::TestPredictions::test_predict_signature_returns_dict PASSED [ 86%]
tests/test_physical_ssz.py::TestPredictions::test_grid_shape PASSED      [ 86%]
tests/test_physical_ssz.py::TestPredictions::test_range_is_finite PASSED [ 87%]
tests/test_physical_ssz.py::TestPhysicalParams::test_default_params PASSED [ 87%]
tests/test_physical_ssz.py::TestPhysicalParams::test_custom_params PASSED [ 88%]
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_extended_default PASSED [ 88%]
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_extended_height_effect PASSED [ 89%]
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_with_latitude PASSED [ 89%]
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_diurnal PASSED [ 90%]
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_extended_mode_ratios PASSED [ 90%]
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_invalid_parameters PASSED [ 91%]
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_load_synthetic_data PASSED [ 92%]
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_schema_validation PASSED [ 92%]
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_synthetic_data_has_true_delta_seg PASSED [ 93%]
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_get_frequency_dict PASSED [ 93%]
tests/test_t1_t4_implementation.py::TestT2Pipeline::test_pipeline_default_config PASSED [ 94%]
tests/test_t1_t4_implementation.py::TestT2Pipeline::test_pipeline_result_summary PASSED [ 94%]
tests/test_t1_t4_implementation.py::TestT2Pipeline::test_quick_analysis PASSED [ 95%]
tests/test_t1_t4_implementation.py::TestT3RealDataHooks::test_real_data_loader_not_implemented PASSED [ 95%]
tests/test_t1_t4_implementation.py::TestT3RealDataHooks::test_load_from_csv_path PASSED [ 96%]
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_compute_relative_shifts PASSED [ 96%]
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_check_mode_independence_ssz PASSED [ 97%]
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_check_mode_independence_dispersive PASSED [ 97%]
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_delta_seg_with_confidence PASSED [ 98%]
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_detect_dispersion_pattern PASSED [ 98%]
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_generate_diagnostic_report PASSED [ 99%]
tests/test_t1_t4_implementation.py::TestIntegration::test_full_workflow PASSED [100%]

=================================== ERRORS ====================================
________________________ ERROR at setup of test_object ________________________
file e:\clone\ssz-schuhman-experiment\scripts\test_ssz_full_scale.py, line 142
  def test_object(obj: AstroObject) -> dict:
E       fixture 'obj' not found
>       available fixtures: _session_faker, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, doctest_namespace, faker, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, subtests, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

e:\clone\ssz-schuhman-experiment\scripts\test_ssz_full_scale.py:142
============================== warnings summary ===============================
scripts/test_gamma_seg_transfer.py::test_mathematical_consistency
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_gamma_seg_transfer.py::test_mathematical_consistency returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_gamma_seg_transfer.py::test_g79_predictions
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_gamma_seg_transfer.py::test_g79_predictions returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_gamma_seg_transfer.py::test_nicer_application
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_gamma_seg_transfer.py::test_nicer_application returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_gamma_seg_transfer.py::test_gw_application
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_gamma_seg_transfer.py::test_gw_application returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_gamma_seg_transfer.py::test_scaling_relation
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_gamma_seg_transfer.py::test_scaling_relation returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_correct_predictions.py::test_44_percent_prediction
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_correct_predictions.py::test_44_percent_prediction returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_correct_predictions.py::test_universal_crossover
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_correct_predictions.py::test_universal_crossover returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_correct_predictions.py::test_horizon_behavior
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_correct_predictions.py::test_horizon_behavior returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_correct_predictions.py::test_g79_nebula
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_correct_predictions.py::test_g79_nebula returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_correct_predictions.py::test_segment_saturation
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_correct_predictions.py::test_segment_saturation returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_correct_predictions.py::test_earth_schumann
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_correct_predictions.py::test_earth_schumann returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_correct_predictions.py::test_scaling_comparison
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_correct_predictions.py::test_scaling_comparison returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_expected_regimes.py::test_nicer_regime
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_expected_regimes.py::test_nicer_regime returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_expected_regimes.py::test_gw_regime
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_expected_regimes.py::test_gw_regime returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_expected_regimes.py::test_feka_regime
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_expected_regimes.py::test_feka_regime returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

scripts/test_ssz_expected_regimes.py::test_scaling_across_regimes
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but scripts/test_ssz_expected_regimes.py::test_scaling_across_regimes returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_end_to_end.py::TestFullPipeline::test_run_analysis_pipeline
  E:\clone\ssz-schuhman-experiment\ssz_schumann\analysis\compute_deltas.py:163: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "timestamp": datetime.utcnow().isoformat(),

tests/test_models.py::TestSSZCorrection::test_mode_consistency_inconsistent
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\numpy\lib\_function_base_impl.py:2922: RuntimeWarning: invalid value encountered in divide
    c /= stddev[:, None]

tests/test_models.py::TestSSZCorrection::test_mode_consistency_inconsistent
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\numpy\lib\_function_base_impl.py:2923: RuntimeWarning: invalid value encountered in divide
    c /= stddev[None, :]

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
ERROR scripts/test_ssz_full_scale.py::test_object
================= 187 passed, 19 warnings, 1 error in 13.40s ==================

```

---

## REPO: ssz-lagrange

### EXECUTION META
- Status: FAILED
- Duration: 10.4s
- Exit Code: 3
- Passed: 0
- Failed: 0
- Errors: 100
- Expected: 54

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-lagrange
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... 
=================================================================
TEST 1: SSZ-Grundwerte bei r_s
=================================================================
  [PASS] Xi(r_s)=0.802
         0.801712
  [PASS] D(r_s)=0.555
         0.555028
  [PASS] D*s=1
         1.000000000000000
  [PASS] D(r_s)>0 kein Horizont
         D=0.555028

=================================================================
TEST 2: GPS-Satellit
=================================================================
  [PASS] SSZ=GR
         SSZ:5.292002e-10 GR:5.292002e-10
  [PASS] df/f~5.3e-10
         5.2920e-10

=================================================================
TEST 3: Pound-Rebka (22.5m)
=================================================================
  [PASS] ~2.46e-15
         2.4425e-15

=================================================================
TEST 4: Merkur-Periheldrehung
=================================================================
  [PASS] ~42.98 arcsec/Jh
         42.99"/Jh

=================================================================
TEST 5: S2-Stern (Sgr A*)
=================================================================
  [PASS] ~12.1 arcmin
         11.9'

=================================================================
TEST 6: Cassini Shapiro-Delay
=================================================================
  [PASS] 200-300us
         283.4us

=================================================================
TEST 7: Lichtablenkung Sonne
=================================================================
  [PASS] ~1.75 arcsec
         1.7516"

=================================================================
TEST 8: V_eff Endlichkeit
=================================================================
  [PASS] SSZ V_eff(r_s) endlich
         0.806636
  [PASS] Schw V_eff(r_s)=0
         0.000000
  [PASS] Weak field <1%
         Abw:9.85e-03

=================================================================
TEST 9: Photonensphäre
=================================================================
  [PASS] SSZ<GR (kompakter)
         SSZ:1.100 GR:1.500
  [PASS] Schw~1.5
         1.5002

=================================================================
TEST 10: ISCO
=================================================================
  [PASS] Schw ISCO=3r_s (analytisch)
         r_ISCO=3.000 r_s (6M)
  [PASS] SSZ ISCO gefunden
         r~1.65 r_s
  [PASS] Schw ISCO~3.0
         3.17

=================================================================
TEST 11: Geodäten-Erhaltung (Kreisbahn r=50r_s)
=================================================================
  [PASS] Energie erhalten dE/E<1e-4
         dE/E=0.00e+00
  [PASS] Drehimpuls erhalten dL/L<1e-4
         dL/L=0.00e+00
  [PASS] Kreisbahn stabil dr/r<5%
         dr/r=0.00e+00

=================================================================
TEST 12: Weak-Field g_tt
=================================================================
  [PASS] r=100: <1e-4
         Abw:7.53e-05
  [PASS] r=1000: <1e-4
         Abw:7.50e-07
  [PASS] r=10000: <1e-4
         Abw:7.50e-09

=================================================================
TEST 13: PPN gamma=beta=1
=================================================================
  [PASS] gamma=1
         alpha=2r_s/b -> gamma=1
  [PASS] beta=1
         Perihel=GR -> beta=1

=================================================================
TEST 14: Gravity Probe A
=================================================================
  [PASS] SSZ=GR <0.01%
         4.252079e-10 vs 4.252079e-10

=================================================================
TEST 15: Energiebedingungen
=================================================================
  [PASS] WEC rho>0 bei 2r_s
         1.3423e-02
  [PASS] WEC rho>0 bei r*
         1.9838e-02

=================================================================
TEST 16: SSZ-Kerr: Delta_SSZ > 0 (Kap.14)
=================================================================
  [PASS] Cygnus X-1: Delta_SSZ > 0 ueberall
         min=9.8636e+08, Kerr Horizont=True
  [PASS] M87*: Delta_SSZ > 0 ueberall
         min=7.5579e+25, Kerr Horizont=True
  [PASS] Sgr A*: Delta_SSZ > 0 ueberall
         min=9.7686e+18, Kerr Horizont=True
  [PASS] GW150914 rem.: Delta_SSZ > 0 ueberall
         min=3.8483e+09, Kerr Horizont=True

=================================================================
TEST 17: SSZ-Kerr: Keine Ergosphaere (Kap.14)
=================================================================
  [PASS] Cygnus X-1: g_tt < 0 ueberall (keine Ergo.)
         min(g_tt)=-0.613737
  [PASS] M87*: g_tt < 0 ueberall (keine Ergo.)
         min(g_tt)=-0.613737

=================================================================
TEST 18: Spin-Orbit-Praezession (Kap.14)
=================================================================
  [PASS] GPB Spin-Orbit SSZ=GR
         D^2 - (1-rs/r) = 2.22e-16
  [PASS] Geodaet. Praez. ~6606 mas/yr
         6638.1 mas/yr (Messung: 6601.8+-18.3)

=================================================================
TEST 19: Frame-Dragging / Lense-Thirring (Kap.15)
=================================================================
  [PASS] LT-Praez. ~39 mas/yr
         41.1 mas/yr (GPB: 37.2+-7.2)
  [PASS] SSZ-Korrektur vernachlaessigbar
         D^2/s^2 - 1 = -2.53e-09
  [PASS] Frame-Dragging endlich bei r_s
         1-D(rs)^2 = 0.691944

=================================================================
TEST 20: Quantenkorrekturen (Kap.16)
=================================================================
  [PASS] Hawking T(10 M_sun) ~ 6e-9 K
         T_H = 6.1687e-09 K
  [PASS] T_SSZ endlich
         T_SSZ = 8.6884e-10 K
  [PASS] T_SSZ < T_Hawking
         T_SSZ/T_H = 0.141
  [PASS] S_SSZ > S_BH (groesserer Horizont)
         S_SSZ/S_BH = 2.544, (r*/r_s)^2 = 2.544
  [PASS] S_SSZ ~ 2.5 * S_BH
         Faktor 2.544

=================================================================
TEST 21: Kosmologie / Friedmann (Kap.17)
=================================================================
  [PASS] Xi_lokal << 1 (Schwachfeld)
         Xi = 4.79e-08
  [PASS] BBN: dH/H < 1e-8
         dH/H ~ 1.00e-10
  [PASS] w_Xi ~ -1 (de Sitter)
         w = -0.999993
  [PASS] H_0 = 67.4 km/s/Mpc (Eingabe)
         H_0 = 67.4 km/s/Mpc

=================================================================
TEST 22: 3+1 Zerlegung / Hamilton-Constraint (Kap.18)
=================================================================
  [PASS] R^(3) analytisch = metrisch
         max rel err = 4.43e-14
  [PASS] Lapse alpha > 0 ueberall
         min(alpha) = 0.967742
  [PASS] CFL stabil: alpha(r_s) endlich
         alpha(r_s) = 0.5550 (GR: 0 -> instabil)
  [PASS] Konformer Faktor endlich
         phi-Range: [0.9081, 1.7665]

=================================================================
ERGEBNIS: 54/54 PASS, 0 FAIL
=================================================================
ALLE TESTS BESTANDEN
collected 0 items
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 318, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 371, in _main
INTERNALERROR>     config.hook.pytest_collection(session=session)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\logging.py", line 788, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\warnings.py", line 98, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\config\__init__.py", line 1403, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 382, in pytest_collection
INTERNALERROR>     session.perform_collect()
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 857, in perform_collect
INTERNALERROR>     self.items.extend(self.genitems(node))
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 1023, in genitems
INTERNALERROR>     yield from self.genitems(subnode)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 1020, in genitems
INTERNALERROR>     rep, duplicate = self._collect_one_node(node, handle_dupes)
INTERNALERROR>                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 883, in _collect_one_node
INTERNALERROR>     rep = collect_one_node(node)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 576, in collect_one_node
INTERNALERROR>     rep: CollectReport = ihook.pytest_make_collect_report(collector=collector)
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\capture.py", line 880, in pytest_make_collect_report
INTERNALERROR>     rep = yield
INTERNALERROR>           ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 400, in pytest_make_collect_report
INTERNALERROR>     call = CallInfo.from_call(
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 353, in from_call
INTERNALERROR>     result: TResult | None = func()
INTERNALERROR>                              ^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 398, in collect
INTERNALERROR>     return list(collector.collect())
INTERNALERROR>                 ^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 563, in collect
INTERNALERROR>     self._register_setup_module_fixture()
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 576, in _register_setup_module_fixture
INTERNALERROR>     self.obj, ("setUpModule", "setup_module")
INTERNALERROR>     ^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 289, in obj
INTERNALERROR>     self._obj = obj = self._getobj()
INTERNALERROR>                       ^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 560, in _getobj
INTERNALERROR>     return importtestmodule(self.path, self.config)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 507, in importtestmodule
INTERNALERROR>     mod = import_path(
INTERNALERROR>           ^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\pathlib.py", line 587, in import_path
INTERNALERROR>     importlib.import_module(module_name)
INTERNALERROR>   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py", line 90, in import_module
INTERNALERROR>     return _bootstrap._gcd_import(name[level:], package, level)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\assertion\rewrite.py", line 197, in exec_module
INTERNALERROR>     exec(co, module.__dict__)
INTERNALERROR>   File "E:\clone\ssz-lagrange\test_lagrange_ssz.py", line 395, in <module>
INTERNALERROR>     sys.exit(0 if F==0 else 1)
INTERNALERROR> SystemExit: 0

============================ no tests ran in 8.09s ============================

```

### STDERR (RAW)

```
mainloop: caught unexpected SystemExit!

```

---

## REPO: segmented-calculation-suite

### EXECUTION META
- Status: SUCCESS
- Duration: 7.6s
- Exit Code: 0
- Passed: 158
- Failed: 0
- Errors: 0
- Expected: 158

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\segmented-calculation-suite
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 158 items

segcalc/tests/test_invariants.py::TestSSZInvariants::test_dual_velocity_product_is_c_squared PASSED [  0%]
segcalc/tests/test_invariants.py::TestSSZInvariants::test_xi_plus_d_bounded PASSED [  1%]
segcalc/tests/test_invariants.py::TestSSZInvariants::test_d_ssz_from_xi_relation PASSED [  1%]
segcalc/tests/test_invariants.py::TestSSZInvariants::test_ssz_finite_at_horizon PASSED [  2%]
segcalc/tests/test_invariants.py::TestSSZInvariants::test_xi_at_horizon_is_finite PASSED [  3%]
segcalc/tests/test_invariants.py::TestRedshiftInvariants::test_z_from_d_relation PASSED [  3%]
segcalc/tests/test_invariants.py::TestRedshiftInvariants::test_weak_field_redshift_approximation PASSED [  4%]
segcalc/tests/test_invariants.py::TestGeometricInvariants::test_natural_boundary_ratio PASSED [  5%]
segcalc/tests/test_invariants.py::TestGeometricInvariants::test_phi_squared_relation PASSED [  5%]
segcalc/tests/test_invariants.py::TestGeometricInvariants::test_phi_reciprocal_relation PASSED [  6%]
segcalc/tests/test_invariants.py::TestDatasetInvariants::test_calculate_all_preserves_order PASSED [  6%]
segcalc/tests/test_invariants.py::TestDatasetInvariants::test_calculate_all_handles_nan PASSED [  7%]
segcalc/tests/test_invariants.py::TestDatasetInvariants::test_ssz_vs_gr_consistency PASSED [  8%]
segcalc/tests/test_invariants.py::TestNumericalInvariants::test_xi_monotonic_in_weak_field PASSED [  8%]
segcalc/tests/test_invariants.py::TestNumericalInvariants::test_d_monotonic_in_weak_field PASSED [  9%]
segcalc/tests/test_invariants.py::TestNumericalInvariants::test_results_reproducible PASSED [ 10%]
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_phi_precision PASSED [ 10%]
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_schwarzschild_radius_scaling PASSED [ 11%]
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_weak_field_limit PASSED [ 12%]
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_strong_field_limit PASSED [ 12%]
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_blend_continuity PASSED [ 13%]
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_auto_regime_selection PASSED [ 13%]
segcalc/tests/test_physics.py::TestPhysicalLimits::test_no_singularities PASSED [ 14%]
segcalc/tests/test_physics.py::TestPhysicalLimits::test_gr_singularity_at_horizon PASSED [ 15%]
segcalc/tests/test_physics.py::TestPhysicalLimits::test_dual_velocity_invariance PASSED [ 15%]
segcalc/tests/test_physics.py::TestPhysicalLimits::test_time_dilation_bounds PASSED [ 16%]
segcalc/tests/test_physics.py::TestNumericalPrecision::test_mass_range_stability PASSED [ 17%]
segcalc/tests/test_physics.py::TestNumericalPrecision::test_extreme_radii PASSED [ 17%]
segcalc/tests/test_physics.py::TestNumericalPrecision::test_calculate_single_consistency PASSED [ 18%]
segcalc/tests/test_physics.py::TestRegimeClassification::test_photon_sphere_regime PASSED [ 18%]
segcalc/tests/test_physics.py::TestRegimeClassification::test_weak_field_regime PASSED [ 19%]
segcalc/tests/test_physics.py::TestRegimeClassification::test_neutron_star_regime PASSED [ 20%]
segcalc/tests/test_ssz_physics.py::TestConstants::test_golden_ratio PASSED [ 20%]
segcalc/tests/test_ssz_physics.py::TestConstants::test_regime_boundaries PASSED [ 21%]
segcalc/tests/test_ssz_physics.py::TestConstants::test_intersection_point PASSED [ 22%]
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_weak_field_earth PASSED [ 22%]
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_strong_field_horizon PASSED [ 23%]
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_strong_field_zero PASSED [ 24%]
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_blend_zone_continuity PASSED [ 24%]
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_auto_selects_weak_for_earth PASSED [ 25%]
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_D_ssz_at_horizon PASSED [ 25%]
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_D_gr_at_horizon PASSED [ 26%]
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_D_ssz_never_zero PASSED [ 27%]
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_weak_field_agreement PASSED [ 27%]
segcalc/tests/test_ssz_physics.py::TestGPSValidation::test_gps_time_correction PASSED [ 28%]
segcalc/tests/test_ssz_physics.py::TestPoundRebka::test_pound_rebka_redshift PASSED [ 29%]
segcalc/tests/test_ssz_physics.py::TestNeutronStarPredictions::test_psr_j0740_regime PASSED [ 29%]
segcalc/tests/test_ssz_physics.py::TestNeutronStarPredictions::test_ssz_predicts_higher_redshift PASSED [ 30%]
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_power_law_parameters PASSED [ 31%]
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_sun_energy_normalization PASSED [ 31%]
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_neutron_star_energy PASSED [ 32%]
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_power_law_scaling PASSED [ 32%]
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_geom_hint_finite PASSED [ 33%]
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_geom_hint_uses_phi PASSED [ 34%]
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_ssz_geom_hint_mode PASSED [ 34%]
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_ssz_geom_hint_disabled_weak_field PASSED [ 35%]
segcalc/tests/test_ssz_physics.py::TestUniversalIntersection::test_intersection_mass_independent PASSED [ 36%]
test_golden_validation.py::test_golden_dataset_exists PASSED             [ 36%]
test_golden_validation.py::test_golden_win_rate PASSED                   [ 37%]
test_golden_validation.py::test_golden_regime_distribution PASSED        [ 37%]
test_golden_validation.py::test_golden_columns PASSED                    [ 38%]
test_tie_regression.py::test_tie_on_equal_residuals PASSED               [ 39%]
test_tie_regression.py::test_ssz_closer_consistent_with_winner PASSED    [ 39%]
test_tie_regression.py::test_no_winner_without_observation PASSED        [ 40%]
test_tie_regression.py::test_winner_deterministic PASSED                 [ 41%]
test_tie_regression.py::test_regime_has_numeric_trigger PASSED           [ 41%]
test_weak_field_contract.py::test_sun_weak_field PASSED                  [ 42%]
test_weak_field_contract.py::test_earth_orbit_weak_field PASSED          [ 43%]
test_weak_field_contract.py::test_gps_satellite_weak_field PASSED        [ 43%]
test_weak_field_contract.py::test_neutron_star_strong_field PASSED       [ 44%]
tests/test_experimental_validation.py::TestPoundRebka::test_pound_rebka_redshift PASSED [ 44%]
tests/test_experimental_validation.py::TestGPSValidation::test_gps_gravitational_time_dilation PASSED [ 45%]
tests/test_experimental_validation.py::TestGPSValidation::test_gps_position_error_without_correction PASSED [ 46%]
tests/test_experimental_validation.py::TestNISTOpticalClock::test_nist_33cm_height_difference PASSED [ 46%]
tests/test_experimental_validation.py::TestTokyoSkytree::test_skytree_450m PASSED [ 47%]
tests/test_experimental_validation.py::TestWeakFieldContract::test_earth_surface_ssz_equals_gr PASSED [ 48%]
tests/test_experimental_validation.py::TestWeakFieldContract::test_solar_system_weak_field PASSED [ 48%]
tests/test_experimental_validation.py::TestTheoreticalConsistency::test_d_ssz_equals_one_over_one_plus_xi PASSED [ 49%]
tests/test_experimental_validation.py::TestTheoreticalConsistency::test_xi_at_horizon PASSED [ 50%]
tests/test_experimental_validation.py::TestTheoreticalConsistency::test_d_ssz_finite_at_horizon PASSED [ 50%]
tests/test_geodesics.py::TestNullGeodesics::test_light_cone_closing_positive PASSED [ 51%]
tests/test_geodesics.py::TestNullGeodesics::test_null_geodesic_dr_dT_bounded PASSED [ 51%]
tests/test_geodesics.py::TestNullGeodesics::test_light_travel_time_exceeds_flat_space PASSED [ 52%]
tests/test_geodesics.py::TestEffectivePotential::test_effective_potential_bounded PASSED [ 53%]
tests/test_geodesics.py::TestEffectivePotential::test_effective_potential_equals_c2_sech2 PASSED [ 53%]
tests/test_geodesics.py::TestAsymptoticLimits::test_metric_smooth_everywhere PASSED [ 54%]
tests/test_geodesics.py::TestAsymptoticLimits::test_no_horizon_singularity PASSED [ 55%]
tests/test_geodesics.py::TestTimelikeGeodesics::test_timelike_geodesic_returns_arrays PASSED [ 55%]
tests/test_geodesics.py::TestTimelikeGeodesics::test_timelike_geodesic_integrates PASSED [ 56%]
tests/test_geodesics.py::TestMetricFunctions::test_phi_gravitational_positive PASSED [ 56%]
tests/test_geodesics.py::TestMetricFunctions::test_gamma_ge_one PASSED   [ 57%]
tests/test_geodesics.py::TestMetricFunctions::test_beta_bounded PASSED   [ 58%]
tests/test_geodesics.py::TestMetricFunctions::test_sech2_bounded PASSED  [ 58%]
tests/test_geodesics.py::TestConsistency::test_gamma_squared_times_sech2_equals_one PASSED [ 59%]
tests/test_geodesics.py::TestConsistency::test_null_geodesic_path_consistency PASSED [ 60%]
tests/test_invariants_hard.py::TestWeakFieldContract::test_sun_weak_field_z_ssz_equals_z_gr PASSED [ 60%]
tests/test_invariants_hard.py::TestWeakFieldContract::test_earth_weak_field_z_ssz_equals_z_gr PASSED [ 61%]
tests/test_invariants_hard.py::TestWeakFieldContract::test_delta_m_is_zero_in_weak_field PASSED [ 62%]
tests/test_invariants_hard.py::TestForbiddenFormula::test_z_ssz_is_not_one_over_d_minus_one PASSED [ 62%]
tests/test_invariants_hard.py::TestWinnerLogic::test_winner_is_deterministic PASSED [ 63%]
tests/test_invariants_hard.py::TestWinnerLogic::test_eps_based_tie_handling PASSED [ 63%]
tests/test_invariants_hard.py::TestGoldenDatasetMatch::test_golden_dataset_46_of_47 PASSED [ 64%]
tests/test_invariants_hard.py::TestGoldenDatasetMatch::test_single_gr_win_is_3c279 PASSED [ 65%]
tests/test_invariants_hard.py::TestXiFormulas::test_xi_weak_formula PASSED [ 65%]
tests/test_invariants_hard.py::TestXiFormulas::test_xi_strong_formula PASSED [ 66%]
tests/test_invariants_hard.py::TestXiFormulas::test_xi_at_horizon_value PASSED [ 67%]
tests/test_invariants_hard.py::TestHorizonFinite::test_d_ssz_finite_at_horizon PASSED [ 67%]
tests/test_invariants_hard.py::TestHorizonFinite::test_d_gr_zero_at_horizon PASSED [ 68%]
tests/test_invariants_hard.py::TestRegimeBoundaries::test_weak_regime_above_10_rs PASSED [ 68%]
tests/test_invariants_hard.py::TestRegimeBoundaries::test_photon_sphere_regime PASSED [ 69%]
tests/test_qubit.py::TestQubitDataclass::test_qubit_creation PASSED      [ 70%]
tests/test_qubit.py::TestQubitDataclass::test_qubit_position PASSED      [ 70%]
tests/test_qubit.py::TestQubitDataclass::test_qubit_radius PASSED        [ 71%]
tests/test_qubit.py::TestQubitDataclass::test_qubit_pair_separation PASSED [ 72%]
tests/test_qubit.py::TestQubitDataclass::test_qubit_pair_height_difference PASSED [ 72%]
tests/test_qubit.py::TestSegmentDensity::test_xi_weak_field_formula PASSED [ 73%]
tests/test_qubit.py::TestSegmentDensity::test_xi_strong_field_formula PASSED [ 74%]
tests/test_qubit.py::TestSegmentDensity::test_xi_positive_definite PASSED [ 74%]
tests/test_qubit.py::TestSegmentDensity::test_xi_gradient_negative_weak_field PASSED [ 75%]
tests/test_qubit.py::TestTimeDilation::test_d_ssz_equals_one_over_one_plus_xi PASSED [ 75%]
tests/test_qubit.py::TestTimeDilation::test_d_ssz_less_than_one PASSED   [ 76%]
tests/test_qubit.py::TestTimeDilation::test_time_dilation_difference_sign PASSED [ 77%]
tests/test_qubit.py::TestQubitAnalysis::test_analyze_qubit_returns_segment_analysis PASSED [ 77%]
tests/test_qubit.py::TestQubitAnalysis::test_pair_mismatch_zero_for_same_height PASSED [ 78%]
tests/test_qubit.py::TestQubitAnalysis::test_pair_mismatch_increases_with_height_diff PASSED [ 79%]
tests/test_qubit.py::TestGateTiming::test_gate_timing_correction_at_reference PASSED [ 79%]
tests/test_qubit.py::TestGateTiming::test_two_qubit_gate_timing_returns_dict PASSED [ 80%]
tests/test_qubit.py::TestDecoherence::test_decoherence_rate_positive PASSED [ 81%]
tests/test_qubit.py::TestDecoherence::test_effective_T2_less_than_base PASSED [ 81%]
tests/test_qubit.py::TestDecoherence::test_effective_T2_nearly_equals_base PASSED [ 82%]
tests/test_qubit.py::TestSegmentCoherentZones::test_zone_formula PASSED  [ 82%]
tests/test_qubit.py::TestHawkingTemperature::test_hawking_temp_solar_mass PASSED [ 83%]
tests/test_qubit.py::TestHawkingTemperature::test_hawking_temp_inverse_mass PASSED [ 84%]
tests/test_qubit.py::TestHawkingTemperature::test_ssz_hawking_temp_finite PASSED [ 84%]
tests/test_qubit.py::TestHawkingTemperature::test_ssz_hawking_temp_less_than_classical PASSED [ 85%]
tests/test_qubit.py::TestHawkingTemperature::test_evaporation_time_solar_mass PASSED [ 86%]
tests/test_qubit.py::TestHawkingTemperature::test_radiation_power_positive PASSED [ 86%]
tests/test_qubit.py::TestUtilityFunctions::test_height_to_time_offset_sign PASSED [ 87%]
tests/test_qubit.py::TestUtilityFunctions::test_time_difference_per_second_positive PASSED [ 87%]
tests/test_regime_classification.py::TestRegimeClassification::test_very_close_regime PASSED [ 88%]
tests/test_regime_classification.py::TestRegimeClassification::test_blended_regime PASSED [ 89%]
tests/test_regime_classification.py::TestRegimeClassification::test_photon_sphere_regime PASSED [ 89%]
tests/test_regime_classification.py::TestRegimeClassification::test_strong_regime PASSED [ 90%]
tests/test_regime_classification.py::TestRegimeClassification::test_weak_regime PASSED [ 91%]
tests/test_regime_classification.py::TestRegimeClassification::test_boundary_values PASSED [ 91%]
tests/test_regime_classification.py::TestRegimeClassification::test_constants_values PASSED [ 92%]
tests/test_regime_classification.py::TestRegimeClassification::test_simple_regime_classification PASSED [ 93%]
tests/test_regime_classification.py::TestRegimeClassification::test_zero_schwarzschild_radius PASSED [ 93%]
tests/test_regime_classification.py::TestRegimeClassification::test_negative_schwarzschild_radius PASSED [ 94%]
tests/test_regime_classification.py::TestLegacyContextAwareness::test_segcalc_does_not_use_legacy_90_110 PASSED [ 94%]
tests/test_regime_classification.py::TestLegacyContextAwareness::test_segcalc_weak_boundary_is_10 PASSED [ 95%]
tests/test_ui_canonicalization.py::TestUICanonicalRegimes::test_get_regime_uses_canonical_thresholds PASSED [ 96%]
tests/test_ui_canonicalization.py::TestUICanonicalRegimes::test_no_legacy_90_110_in_constants PASSED [ 96%]
tests/test_ui_canonicalization.py::TestUICanonicalRegimes::test_regime_names_are_canonical PASSED [ 97%]
tests/test_ui_canonicalization.py::TestUIWinnerLogic::test_winner_requires_real_z_obs PASSED [ 98%]
tests/test_ui_canonicalization.py::TestNoLegacyStrings::test_app_py_no_legacy_90_110_in_ui_text PASSED [ 98%]
tests/test_ui_canonicalization.py::TestNoLegacyStrings::test_reference_tab_shows_canonical_boundaries PASSED [ 99%]
tests/test_ui_canonicalization.py::TestRegimeColorMapping::test_regime_colors_defined_for_all_canonical_regimes PASSED [100%]

============================= 158 passed in 4.71s =============================

```

---

## REPO: ssz-lensing

### EXECUTION META
- Status: SUCCESS
- Duration: 11.8s
- Exit Code: 0
- Passed: 279
- Failed: 0
- Errors: 0
- Expected: 279

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-lensing
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 279 items

tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_determined_standard PASSED [  0%]
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_overdetermined PASSED [  0%]
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_underdetermined_high_mmax PASSED [  1%]
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_rescue_with_source PASSED [  1%]
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_ill_conditioned PASSED [  1%]
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_phase_degeneracy PASSED [  2%]
tests/test_comprehensive_analysis.py::TestPathConsistency::test_path_a_b_consistency PASSED [  2%]
tests/test_comprehensive_analysis.py::TestPathConsistency::test_regime_matches_dof PASSED [  2%]
tests/test_datahub.py::TestSnapshotValidation::test_quad_snapshot_valid PASSED [  3%]
tests/test_datahub.py::TestSnapshotValidation::test_ring_snapshot_valid PASSED [  3%]
tests/test_datahub.py::TestSnapshotValidation::test_all_snapshots_valid PASSED [  3%]
tests/test_datahub.py::TestQuadSnapshot::test_load_quad_positions PASSED [  4%]
tests/test_datahub.py::TestQuadSnapshot::test_quad_has_redshifts PASSED  [  4%]
tests/test_datahub.py::TestQuadSnapshot::test_quad_no_nan PASSED         [  5%]
tests/test_datahub.py::TestQuadSnapshot::test_quad_no_inf PASSED         [  5%]
tests/test_datahub.py::TestQuadSnapshot::test_quad_has_theta_E PASSED    [  5%]
tests/test_datahub.py::TestRingSnapshot::test_load_ring_positions PASSED [  6%]
tests/test_datahub.py::TestRingSnapshot::test_ring_has_redshifts PASSED  [  6%]
tests/test_datahub.py::TestRingSnapshot::test_ring_no_nan PASSED         [  6%]
tests/test_datahub.py::TestRingSnapshot::test_ring_no_inf PASSED         [  7%]
tests/test_datahub.py::TestFallbackByMode::test_quad_mode PASSED         [  7%]
tests/test_datahub.py::TestFallbackByMode::test_ring_mode PASSED         [  7%]
tests/test_datahub.py::TestFallbackByMode::test_arc_mode PASSED          [  8%]
tests/test_datahub.py::TestFallbackByMode::test_invalid_mode_raises PASSED [  8%]
tests/test_datahub.py::TestDataQuality::test_quad_all_fields_from_source PASSED [  8%]
tests/test_datahub.py::TestDataQuality::test_ring_all_fields_from_source PASSED [  9%]
tests/test_datahub.py::TestDataQuality::test_available_datasets PASSED   [  9%]
tests/test_datahub.py::TestNoDefaultsNoNull::test_quad_complete_numeric PASSED [ 10%]
tests/test_datahub.py::TestNoDefaultsNoNull::test_ring_complete_numeric PASSED [ 10%]
tests/test_dual_path.py::TestSharedForwardModel::test_reduced_deflection_basic PASSED [ 10%]
tests/test_dual_path.py::TestSharedForwardModel::test_lens_equation_zero_residual PASSED [ 11%]
tests/test_dual_path.py::TestPathA_Algebraic::test_algebraic_solver_basic PASSED [ 11%]
tests/test_dual_path.py::TestPathA_Algebraic::test_phase_is_output_not_input PASSED [ 11%]
tests/test_dual_path.py::TestPathB_PhaseScan::test_scan_is_labeled PASSED [ 12%]
tests/test_dual_path.py::TestPathB_PhaseScan::test_scan_finds_candidates PASSED [ 12%]
tests/test_dual_path.py::TestCrossCheck::test_dual_path_runs_both PASSED [ 12%]
tests/test_dual_path.py::TestCrossCheck::test_cross_check_reports_consistency PASSED [ 13%]
tests/test_extended_model.py::test_profiles PASSED                       [ 13%]
tests/test_extended_model.py::test_external_shear PASSED                 [ 13%]
tests/test_extended_model.py::test_higher_multipoles PASSED              [ 14%]
tests/test_extended_model.py::test_synthetic_recovery PASSED             [ 14%]
tests/test_extended_model.py::test_model_with_shear PASSED               [ 15%]
tests/test_extended_model.py::test_real_lens_data PASSED                 [ 15%]
tests/test_extended_model.py::test_comparison PASSED                     [ 15%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_assert_finite_valid PASSED [ 16%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_assert_finite_nan_raises PASSED [ 16%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_assert_finite_inf_raises PASSED [ 16%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_sanitize_no_nan_converts_nan_to_none PASSED [ 17%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_validate_no_nan_finds_issues PASSED [ 17%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_divide_zero PASSED [ 17%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_divide_valid PASSED [ 18%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_sqrt_negative PASSED [ 18%]
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_sqrt_valid PASSED [ 18%]
tests/test_fallback_no_nan.py::TestFallbackQuad::test_load_quad_images_no_nan PASSED [ 19%]
tests/test_fallback_no_nan.py::TestFallbackQuad::test_load_quad_has_4_images PASSED [ 19%]
tests/test_fallback_no_nan.py::TestFallbackQuad::test_quad_has_redshift_info PASSED [ 20%]
tests/test_fallback_no_nan.py::TestFallbackQuad::test_quad_positions_finite PASSED [ 20%]
tests/test_fallback_no_nan.py::TestFallbackRing::test_load_ring_no_nan PASSED [ 20%]
tests/test_fallback_no_nan.py::TestFallbackRing::test_ring_has_multiple_points PASSED [ 21%]
tests/test_fallback_no_nan.py::TestFallbackRing::test_ring_has_redshift_info PASSED [ 21%]
tests/test_fallback_no_nan.py::TestFallbackRing::test_ring_positions_finite PASSED [ 21%]
tests/test_fallback_no_nan.py::TestFallbackByMode::test_load_quad_by_mode PASSED [ 22%]
tests/test_fallback_no_nan.py::TestFallbackByMode::test_load_ring_by_mode PASSED [ 22%]
tests/test_fallback_no_nan.py::TestFallbackByMode::test_invalid_mode_raises PASSED [ 22%]
tests/test_fallback_no_nan.py::TestAllFallbackDatasets::test_all_datasets_no_nan PASSED [ 23%]
tests/test_fallback_no_nan.py::TestAllFallbackDatasets::test_fallback_text_parseable PASSED [ 23%]
tests/test_lensing_run.py::TestNoNaNOutputs::test_cross_no_nan PASSED    [ 24%]
tests/test_lensing_run.py::TestNoNaNOutputs::test_ring_no_nan PASSED     [ 24%]
tests/test_lensing_run.py::TestCircleLabeling::test_sky_circle_is_theta_E PASSED [ 24%]
tests/test_lensing_run.py::TestCircleLabeling::test_lens_circle_is_b_E PASSED [ 25%]
tests/test_lensing_run.py::TestRotationPreservesRadii::test_rotation_invariant_radii PASSED [ 25%]
tests/test_lensing_run.py::TestGRSSZShiftConsistency::test_shift_equals_xi PASSED [ 25%]
tests/test_lensing_run.py::TestGRSSZShiftConsistency::test_xi_is_small_but_nonzero PASSED [ 26%]
tests/test_lensing_run.py::TestFallbackDatasetsLoad::test_cross_dataset_loads PASSED [ 26%]
tests/test_lensing_run.py::TestFallbackDatasetsLoad::test_ring_dataset_loads PASSED [ 26%]
tests/test_lensing_run.py::TestFallbackDatasetsLoad::test_no_fake_zeros PASSED [ 27%]
tests/test_lensing_run.py::TestPhysicalConsistency::test_distances_positive PASSED [ 27%]
tests/test_lensing_run.py::TestPhysicalConsistency::test_mass_reasonable PASSED [ 27%]
tests/test_lensing_run.py::TestPhysicalConsistency::test_schwarzschild_radius_small PASSED [ 28%]
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_gauge_no_nan PASSED [ 28%]
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_alpha_rsg_vs_ppn PASSED [ 29%]
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_delay_monotonic_vs_b PASSED [ 29%]
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_xi_to_zero_limit PASSED [ 29%]
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_phase_delay_relation PASSED [ 30%]
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_gauge_insets_render_data PASSED [ 30%]
tests/test_linear_model.py::test_dof_analysis PASSED                     [ 30%]
tests/test_linear_model.py::test_synthetic_recovery PASSED               [ 31%]
tests/test_linear_model.py::test_real_lens_data PASSED                   [ 31%]
tests/test_linear_model.py::test_comparison_with_extended PASSED         [ 31%]
tests/test_minimal_exact.py::TestLinearSolver::test_simple_2x2 PASSED    [ 32%]
tests/test_minimal_exact.py::TestLinearSolver::test_identity PASSED      [ 32%]
tests/test_minimal_exact.py::TestLinearSolver::test_singular_matrix PASSED [ 32%]
tests/test_minimal_exact.py::TestLinearSolver::test_near_singular PASSED [ 33%]
tests/test_minimal_exact.py::TestRootSolver::test_bisection_linear PASSED [ 33%]
tests/test_minimal_exact.py::TestRootSolver::test_bisection_quadratic PASSED [ 34%]
tests/test_minimal_exact.py::TestRootSolver::test_bisection_trig PASSED  [ 34%]
tests/test_minimal_exact.py::TestRootSolver::test_find_all_roots PASSED  [ 34%]
tests/test_minimal_exact.py::TestExactRecovery::test_standard_cross PASSED [ 35%]
tests/test_minimal_exact.py::TestExactRecovery::test_symmetric_cross PASSED [ 35%]
tests/test_minimal_exact.py::TestExactRecovery::test_asymmetric_cross PASSED [ 35%]
tests/test_minimal_exact.py::TestExactRecovery::test_varying_theta_E PASSED [ 36%]
tests/test_minimal_exact.py::TestMatrixRank::test_full_rank PASSED       [ 36%]
tests/test_minimal_exact.py::TestMatrixRank::test_rank_deficient PASSED  [ 36%]
tests/test_minimal_exact.py::TestMatrixRank::test_rectangular PASSED     [ 37%]
tests/test_model_zoo.py::test_m2_allowed PASSED                          [ 37%]
tests/test_model_zoo.py::test_m2_shear_m3_forbidden PASSED               [ 37%]
tests/test_model_zoo.py::test_arc_points_rescue PASSED                   [ 38%]
tests/test_model_zoo.py::test_multi_source_rescue PASSED                 [ 38%]
tests/test_model_zoo.py::test_shear_recovery PASSED                      [ 39%]
tests/test_model_zoo.py::test_m3_recovery PASSED                         [ 39%]
tests/test_model_zoo.py::test_zoo_comparison PASSED                      [ 39%]
tests/test_multi_source.py::TestDOFGatekeeper::test_overdetermined_allowed PASSED [ 40%]
tests/test_multi_source.py::TestDOFGatekeeper::test_exactly_determined_allowed PASSED [ 40%]
tests/test_multi_source.py::TestDOFGatekeeper::test_underdetermined_forbidden PASSED [ 40%]
tests/test_multi_source.py::TestDOFGatekeeper::test_max_params_single_source PASSED [ 41%]
tests/test_multi_source.py::TestDOFGatekeeper::test_max_params_two_sources PASSED [ 41%]
tests/test_multi_source.py::TestMultiSourceParams::test_phase_derived_from_components PASSED [ 41%]
tests/test_multi_source.py::TestMultiSourceParams::test_shear_phase_derived PASSED [ 42%]
tests/test_multi_source.py::TestMultiSourceBuilder::test_unknowns_single_source_m2 PASSED [ 42%]
tests/test_multi_source.py::TestMultiSourceBuilder::test_unknowns_two_sources_with_shear PASSED [ 43%]
tests/test_multi_source.py::TestMultiSourceBuilder::test_dof_blocks_underdetermined PASSED [ 43%]
tests/test_multi_source.py::TestMultiSourceRecovery::test_single_source_recovery PASSED [ 43%]
tests/test_multi_source.py::TestMultiSourceRecovery::test_two_source_shared_lens PASSED [ 44%]
tests/test_multi_source.py::TestMultiSourceRecovery::test_phase_is_output_not_input PASSED [ 44%]
tests/test_multi_source.py::TestDOFAnalysis::test_analyze_single_source PASSED [ 44%]
tests/test_multi_source.py::TestDOFAnalysis::test_analyze_forbidden_config PASSED [ 45%]
tests/test_multi_source.py::TestDOFAnalysis::test_analyze_multi_source_enables_more PASSED [ 45%]
tests/test_multipole_consistency.py::TestDoFCounting::test_minimal_model_4_images PASSED [ 45%]
tests/test_multipole_consistency.py::TestDoFCounting::test_underdetermined PASSED [ 46%]
tests/test_multipole_consistency.py::TestDoFCounting::test_multipole_m3 PASSED [ 46%]
tests/test_multipole_consistency.py::TestDoFCounting::test_image_multiplicity_quad PASSED [ 46%]
tests/test_multipole_consistency.py::TestMultipoleConsistency::test_m2_matches_minimal PASSED [ 47%]
tests/test_multipole_consistency.py::TestMultipoleConsistency::test_multipole_residuals PASSED [ 47%]
tests/test_multipole_consistency.py::TestMultipoleConsistency::test_phase_periodicity PASSED [ 48%]
tests/test_multipole_consistency.py::TestNumericalStability::test_small_quadrupole PASSED [ 48%]
tests/test_multipole_consistency.py::TestNumericalStability::test_large_offset PASSED [ 48%]
tests/test_multipole_consistency.py::TestNumericalStability::test_matrix_conditioning PASSED [ 49%]
tests/test_no_null_contract.py::TestIsNullOrNaN::test_none_is_null PASSED [ 49%]
tests/test_no_null_contract.py::TestIsNullOrNaN::test_nan_is_null PASSED [ 49%]
tests/test_no_null_contract.py::TestIsNullOrNaN::test_inf_is_null PASSED [ 50%]
tests/test_no_null_contract.py::TestIsNullOrNaN::test_empty_string_is_null PASSED [ 50%]
tests/test_no_null_contract.py::TestIsNullOrNaN::test_valid_number_not_null PASSED [ 50%]
tests/test_no_null_contract.py::TestIsNullOrNaN::test_valid_string_not_null PASSED [ 51%]
tests/test_no_null_contract.py::TestDictValidation::test_valid_dict_passes PASSED [ 51%]
tests/test_no_null_contract.py::TestDictValidation::test_null_detected PASSED [ 51%]
tests/test_no_null_contract.py::TestDictValidation::test_nested_null_detected PASSED [ 52%]
tests/test_no_null_contract.py::TestDictValidation::test_list_null_detected PASSED [ 52%]
tests/test_no_null_contract.py::TestDefaultSigma::test_quad_sigma_positive PASSED [ 53%]
tests/test_no_null_contract.py::TestDefaultSigma::test_ring_sigma_positive PASSED [ 53%]
tests/test_no_null_contract.py::TestDefaultSigma::test_single_point_fallback PASSED [ 53%]
tests/test_no_null_contract.py::TestFillUncertainties::test_all_defaults PASSED [ 54%]
tests/test_no_null_contract.py::TestFillUncertainties::test_partial_input PASSED [ 54%]
tests/test_no_null_contract.py::TestFullNumericPoints::test_creates_all_fields PASSED [ 54%]
tests/test_no_null_contract.py::TestFullNumericPoints::test_to_dict_no_null PASSED [ 55%]
tests/test_no_null_contract.py::TestNormalizedDistances::test_all_values_present PASSED [ 55%]
tests/test_no_null_contract.py::TestEstimates::test_center_estimate PASSED [ 55%]
tests/test_no_null_contract.py::TestEstimates::test_theta_E_estimate PASSED [ 56%]
tests/test_no_null_contract.py::TestAssertNoNullNoNaN::test_valid_dict_passes PASSED [ 56%]
tests/test_no_null_contract.py::TestAssertNoNullNoNaN::test_null_raises PASSED [ 56%]
tests/test_no_null_contract.py::TestAssertNoNullNoNaN::test_nan_raises PASSED [ 57%]
tests/test_no_null_contract.py::TestProvenanceSummary::test_counts_flags PASSED [ 57%]
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_quad_fallback_complete PASSED [ 58%]
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_ring_fallback_complete PASSED [ 58%]
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_quad_full_numeric_output PASSED [ 58%]
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_ring_full_numeric_output PASSED [ 59%]
tests/test_no_null_contract.py::TestUserMinimalInput::test_4_points_no_uncertainties PASSED [ 59%]
tests/test_q2237_diagnostic.py::test_q2237_model_comparison PASSED       [ 59%]
tests/test_q2237_diagnostic.py::test_q2237_forbidden_info PASSED         [ 60%]
tests/test_q2237_diagnostic.py::test_q2237_full_report PASSED            [ 60%]
tests/test_radial_scaling_gauge.py::test_scaling_factor_definition PASSED [ 60%]
tests/test_radial_scaling_gauge.py::test_scaling_weak_field_limit PASSED [ 61%]
tests/test_radial_scaling_gauge.py::test_time_dilation_relation PASSED   [ 61%]
tests/test_radial_scaling_gauge.py::test_effective_wavenumber PASSED     [ 62%]
tests/test_radial_scaling_gauge.py::test_local_light_speed_invariant PASSED [ 62%]
tests/test_radial_scaling_gauge.py::test_shapiro_delay_cassini PASSED    [ 62%]
tests/test_radial_scaling_gauge.py::test_shapiro_delay_solar_grazing PASSED [ 63%]
tests/test_radial_scaling_gauge.py::test_shapiro_xi_vs_ppn_factor PASSED [ 63%]
tests/test_radial_scaling_gauge.py::test_solar_limb_deflection PASSED    [ 63%]
tests/test_radial_scaling_gauge.py::test_deflection_xi_vs_ppn_factor PASSED [ 64%]
tests/test_radial_scaling_gauge.py::test_gaia_deflection_precision PASSED [ 64%]
tests/test_radial_scaling_gauge.py::test_wkb_phase_scaling PASSED        [ 64%]
tests/test_radial_scaling_gauge.py::test_interferometer_phase_difference PASSED [ 65%]
tests/test_radial_scaling_gauge.py::test_frame_consistency_loop_closure PASSED [ 65%]
tests/test_radial_scaling_gauge.py::test_coordinate_independence PASSED  [ 65%]
tests/test_radial_scaling_gauge.py::test_pound_rebka_experiment PASSED   [ 66%]
tests/test_radial_scaling_gauge.py::test_gps_time_drift PASSED           [ 66%]
tests/test_radial_scaling_gauge.py::test_tokyo_skytree_clocks PASSED     [ 67%]
tests/test_real_data.py::test_synthetic_exact PASSED                     [ 67%]
tests/test_real_data.py::test_synthetic_random PASSED                    [ 67%]
tests/test_real_data.py::test_real_data PASSED                           [ 68%]
tests/test_real_data.py::test_noise_sensitivity PASSED                   [ 68%]
tests/test_real_inversion.py::TestMorphologyClassifier::test_quad_classification PASSED [ 68%]
tests/test_real_inversion.py::TestMorphologyClassifier::test_ring_classification PASSED [ 69%]
tests/test_real_inversion.py::TestMorphologyClassifier::test_double_classification PASSED [ 69%]
tests/test_real_inversion.py::TestMorphologyClassifier::test_criteria_are_explicit PASSED [ 69%]
tests/test_real_inversion.py::TestSourceConsistency::test_consistent_sources PASSED [ 70%]
tests/test_real_inversion.py::TestQuadInversion::test_synthetic_recovery PASSED [ 70%]
tests/test_real_inversion.py::TestQuadInversion::test_model_comparison PASSED [ 70%]
tests/test_real_inversion.py::TestLinearSystem::test_system_dimensions PASSED [ 71%]
tests/test_real_inversion.py::TestLinearSystem::test_overdetermined_system PASSED [ 71%]
tests/test_regime_explorer.py::test_regime_determined PASSED             [ 72%]
tests/test_regime_explorer.py::test_regime_overdetermined PASSED         [ 72%]
tests/test_regime_explorer.py::test_regime_underdetermined PASSED        [ 72%]
tests/test_regime_explorer.py::test_regime_ill_conditioned PASSED        [ 73%]
tests/test_regime_explorer.py::test_underdetermined_multiple_solutions PASSED [ 73%]
tests/test_regime_explorer.py::test_underdetermined_param_ranges PASSED  [ 73%]
tests/test_regime_explorer.py::test_underdetermined_non_identifiable PASSED [ 74%]
tests/test_regime_explorer.py::test_high_mmax_underdetermined PASSED     [ 74%]
tests/test_regime_explorer.py::test_dof_rescue_multisource PASSED        [ 74%]
tests/test_regime_explorer.py::test_recommendations_change PASSED        [ 75%]
tests/test_ui_state.py::TestDatasetState::test_empty_state PASSED        [ 75%]
tests/test_ui_state.py::TestDatasetState::test_to_dict PASSED            [ 75%]
tests/test_ui_state.py::TestDatasetState::test_from_dict PASSED          [ 76%]
tests/test_ui_state.py::TestParseUserPoints::test_parse_quad PASSED      [ 76%]
tests/test_ui_state.py::TestParseUserPoints::test_parse_ring PASSED      [ 77%]
tests/test_ui_state.py::TestParseUserPoints::test_wrong_count_quad PASSED [ 77%]
tests/test_ui_state.py::TestParseUserPoints::test_invalid_line PASSED    [ 77%]
tests/test_ui_state.py::TestBuildUserDataset::test_build_quad PASSED     [ 78%]
tests/test_ui_state.py::TestBuildUserDataset::test_build_with_redshifts PASSED [ 78%]
tests/test_ui_state.py::TestLoadFallbackDataset::test_load_quad PASSED   [ 78%]
tests/test_ui_state.py::TestLoadFallbackDataset::test_load_ring PASSED   [ 79%]
tests/test_ui_state.py::TestValidateDataset::test_valid_quad PASSED      [ 79%]
tests/test_ui_state.py::TestValidateDataset::test_empty_fails PASSED     [ 79%]
tests/test_ui_state.py::TestValidateDataset::test_wrong_mode_count PASSED [ 80%]
tests/test_ui_state.py::TestValidateDataset::test_nan_fails PASSED       [ 80%]
tests/test_ui_state.py::TestValidationReport::test_valid_report PASSED   [ 81%]
tests/test_ui_state.py::TestValidationReport::test_invalid_report PASSED [ 81%]
tests/test_ui_state.py::TestDatasetSummary::test_summary_valid PASSED    [ 81%]
tests/test_ui_state.py::TestDatasetSummary::test_summary_invalid PASSED  [ 82%]
tests/test_ui_state.py::TestRunState::test_default PASSED                [ 82%]
tests/test_ui_state.py::TestRunState::test_to_from_dict PASSED           [ 82%]
tests/test_validation_lab.py::test_UT1 PASSED                            [ 83%]
tests/test_validation_lab.py::test_UT2 PASSED                            [ 83%]
tests/test_validation_lab.py::test_UT3 PASSED                            [ 83%]
tests/test_validation_lab.py::test_ST1 PASSED                            [ 84%]
tests/test_validation_lab.py::test_ST2 PASSED                            [ 84%]
tests/test_validation_lab.py::test_ST3 PASSED                            [ 84%]
tests/test_validation_lab.py::test_CM1 PASSED                            [ 85%]
tests/test_validation_lab.py::test_RB1 PASSED                            [ 85%]
tests/test_validation_lab.py::test_RB2 PASSED                            [ 86%]
tests/test_validation_module.py::test_image_validation PASSED            [ 86%]
tests/test_validation_module.py::test_dof_analysis PASSED                [ 86%]
tests/test_validation_module.py::test_result_interpretation PASSED       [ 87%]
tests/test_validation_module.py::test_model_comparison PASSED            [ 87%]
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_shear_data_shear_wins PASSED [ 87%]
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_m3_data_m3_wins PASSED [ 88%]
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_full_model_forbidden_without_extras PASSED [ 88%]
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_report_shows_derivation PASSED [ 88%]
tests/zoo/test_derivation_chain.py::TestForbiddenToAllowed::test_arc_points_rescue_full_model PASSED [ 89%]
tests/zoo/test_derivation_chain.py::TestForbiddenToAllowed::test_multi_source_rescue_full_model PASSED [ 89%]
tests/zoo/test_derivation_chain.py::TestRegression::test_basic_m2_still_works PASSED [ 89%]
tests/zoo/test_derivation_chain.py::TestRegression::test_bundle_backward_compatible PASSED [ 90%]
tests/zoo/test_geometry.py::TestTriadScene::test_create_standard_scene PASSED [ 90%]
tests/zoo/test_geometry.py::TestTriadScene::test_scene_distances PASSED  [ 91%]
tests/zoo/test_geometry.py::TestTriadScene::test_add_multiple_sources PASSED [ 91%]
tests/zoo/test_geometry.py::TestProjection::test_project_single_source PASSED [ 91%]
tests/zoo/test_geometry.py::TestProjection::test_projection_tracer PASSED [ 92%]
tests/zoo/test_geometry.py::TestProjection::test_forward_backward_consistency PASSED [ 92%]
tests/zoo/test_geometry.py::TestSerialization::test_to_dict_and_back PASSED [ 92%]
tests/zoo/test_geometry.py::TestSerialization::test_json_roundtrip PASSED [ 93%]
tests/zoo/test_geometry.py::TestVisualization::test_visualizer_smoke_test PASSED [ 93%]
tests/zoo/test_geometry.py::TestVisualization::test_ascii_scene_output PASSED [ 93%]
tests/zoo/test_m4_extension.py::TestM4Models::test_derivation_chain_includes_m4 PASSED [ 94%]
tests/zoo/test_m4_extension.py::TestM4Models::test_m4_data_m4_model_works PASSED [ 94%]
tests/zoo/test_m4_extension.py::TestM4Models::test_full_chain_report PASSED [ 94%]
tests/zoo/test_m4_extension.py::TestRealDataPipeline::test_list_available_systems PASSED [ 95%]
tests/zoo/test_m4_extension.py::TestRealDataPipeline::test_load_q2237 PASSED [ 95%]
tests/zoo/test_m4_extension.py::TestRealDataPipeline::test_q2237_derivation_chain PASSED [ 96%]
tests/zoo/test_m4_extension.py::TestArtifacts::test_save_artifacts PASSED [ 96%]
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_perfect_ring_classified_as_ring PASSED [ 96%]
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_shear_ring_detected PASSED [ 97%]
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_quad_classified_as_quad PASSED [ 97%]
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_ring_to_cross_transition PASSED [ 97%]
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_perfect_ring_fit PASSED [ 98%]
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_perturbed_ring_detects_m2 PASSED [ 98%]
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_m4_perturbation_detected PASSED [ 98%]
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_off_center_ring PASSED [ 99%]
tests/zoo/test_ring_morphology.py::TestCenterEstimation::test_estimate_ring_center PASSED [ 99%]
tests/zoo/test_ring_morphology.py::TestCenterEstimation::test_estimate_ring_radius PASSED [100%]

============================== warnings summary ===============================
tests\test_radial_scaling_gauge.py:134
  E:\clone\ssz-lensing\tests\test_radial_scaling_gauge.py:134: PytestCollectionWarning: cannot collect test class 'TestResult' because it has a __init__ constructor (from: tests/test_radial_scaling_gauge.py)
    @dataclass

tests\test_regime_explorer.py:32
  E:\clone\ssz-lensing\tests\test_regime_explorer.py:32: PytestCollectionWarning: cannot collect test class 'TestResult' because it has a __init__ constructor (from: tests/test_regime_explorer.py)
    @dataclass

tests/test_extended_model.py::test_profiles
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_profiles returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_external_shear
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_external_shear returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_higher_multipoles
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_higher_multipoles returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_synthetic_recovery
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_synthetic_recovery returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_model_with_shear
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_model_with_shear returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_real_lens_data
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_real_lens_data returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_comparison
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_comparison returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_linear_model.py::test_dof_analysis
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_linear_model.py::test_dof_analysis returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_linear_model.py::test_synthetic_recovery
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_linear_model.py::test_synthetic_recovery returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_linear_model.py::test_real_lens_data
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_linear_model.py::test_real_lens_data returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_linear_model.py::test_comparison_with_extended
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_linear_model.py::test_comparison_with_extended returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_scaling_factor_definition
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_scaling_factor_definition returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_scaling_weak_field_limit
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_scaling_weak_field_limit returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_time_dilation_relation
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_time_dilation_relation returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_effective_wavenumber
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_effective_wavenumber returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_local_light_speed_invariant
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_local_light_speed_invariant returned <class 'list'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_shapiro_delay_cassini
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_shapiro_delay_cassini returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_shapiro_delay_solar_grazing
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_shapiro_delay_solar_grazing returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_shapiro_xi_vs_ppn_factor
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_shapiro_xi_vs_ppn_factor returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_solar_limb_deflection
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_solar_limb_deflection returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_deflection_xi_vs_ppn_factor
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_deflection_xi_vs_ppn_factor returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_gaia_deflection_precision
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_gaia_deflection_precision returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_wkb_phase_scaling
tests/test_radial_scaling_gauge.py::test_interferometer_phase_difference
tests/test_radial_scaling_gauge.py::test_interferometer_phase_difference
  E:\clone\ssz-lensing\tests\test_radial_scaling_gauge.py:256: DeprecationWarning: `trapz` is deprecated. Use `trapezoid` instead, or one of the numerical integration functions in `scipy.integrate`.
    return k * np.trapz(s_vals, dx=dr)

tests/test_radial_scaling_gauge.py::test_wkb_phase_scaling
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_wkb_phase_scaling returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_interferometer_phase_difference
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_interferometer_phase_difference returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_frame_consistency_loop_closure
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_frame_consistency_loop_closure returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_coordinate_independence
  E:\clone\ssz-lensing\tests\test_radial_scaling_gauge.py:783: DeprecationWarning: `trapz` is deprecated. Use `trapezoid` instead, or one of the numerical integration functions in `scipy.integrate`.
    rho = np.trapz(s_vals, r_vals)

tests/test_radial_scaling_gauge.py::test_coordinate_independence
  E:\clone\ssz-lensing\tests\test_radial_scaling_gauge.py:789: DeprecationWarning: `trapz` is deprecated. Use `trapezoid` instead, or one of the numerical integration functions in `scipy.integrate`.
    rho_2 = np.trapz(s_vals_2, r_vals_2)

tests/test_radial_scaling_gauge.py::test_coordinate_independence
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_coordinate_independence returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_pound_rebka_experiment
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_pound_rebka_experiment returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_gps_time_drift
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_gps_time_drift returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_radial_scaling_gauge.py::test_tokyo_skytree_clocks
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_radial_scaling_gauge.py::test_tokyo_skytree_clocks returned <class 'test_radial_scaling_gauge.TestResult'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_real_data.py::test_synthetic_exact
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_real_data.py::test_synthetic_exact returned <class 'tuple'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_real_data.py::test_synthetic_random
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_real_data.py::test_synthetic_random returned <class 'tuple'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_real_data.py::test_real_data
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_real_data.py::test_real_data returned <class 'tuple'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_real_data.py::test_noise_sensitivity
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_real_data.py::test_noise_sensitivity returned <class 'tuple'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_regime_determined
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_regime_determined returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_regime_overdetermined
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_regime_overdetermined returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_regime_underdetermined
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_regime_underdetermined returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_regime_ill_conditioned
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_regime_ill_conditioned returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_underdetermined_multiple_solutions
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_underdetermined_multiple_solutions returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_underdetermined_param_ranges
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_underdetermined_param_ranges returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_underdetermined_non_identifiable
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_underdetermined_non_identifiable returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_high_mmax_underdetermined
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_high_mmax_underdetermined returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_dof_rescue_multisource
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_dof_rescue_multisource returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_regime_explorer.py::test_recommendations_change
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_recommendations_change returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_UT1
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_UT1 returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_UT2
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_UT2 returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_UT3
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_UT3 returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_ST1
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_ST1 returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_ST2
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_ST2 returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_ST3
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_ST3 returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_CM1
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_CM1 returned <class 'numpy.bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_RB1
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_RB1 returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_lab.py::test_RB2
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_lab.py::test_RB2 returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_module.py::test_image_validation
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_module.py::test_image_validation returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_module.py::test_dof_analysis
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_module.py::test_dof_analysis returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_module.py::test_result_interpretation
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_module.py::test_result_interpretation returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_validation_module.py::test_model_comparison
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_validation_module.py::test_model_comparison returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================== 279 passed, 63 warnings in 9.23s =======================

```

---

## REPO: Unified-Results

### EXECUTION META
- Status: FAILED
- Duration: 7.4s
- Exit Code: 1
- Passed: 0
- Failed: 0
- Errors: 0
- Expected: 139

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results
configfile: pyproject.toml
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 54 items

============================ no tests ran in 4.35s ============================

```

### STDERR (RAW)

```
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pytest\__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\config\__init__.py", line 223, in console_main
    code = main()
           ^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\config\__init__.py", line 199, in main
    ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 167, in _multicall
    raise exception
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 365, in pytest_cmdline_main
    return wrap_session(config, _main)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 360, in wrap_session
    config._ensure_unconfigure()
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\config\__init__.py", line 1171, in _ensure_unconfigure
    self._cleanup_stack.close()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\contextlib.py", line 618, in close
    self.__exit__(None, None, None)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\contextlib.py", line 610, in __exit__
    raise exc_details[1]
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\contextlib.py", line 595, in __exit__
    if cb(*exc_details):
       ^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\contextlib.py", line 478, in _exit_wrapper
    callback(*args, **kwds)
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\capture.py", line 778, in stop_global_capturing
    self._global_capturing.pop_outerr_to_orig()
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\capture.py", line 659, in pop_outerr_to_orig
    out, err = self.readouterr()
               ^^^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\capture.py", line 706, in readouterr
    out = self.out.snap() if self.out else ""
          ^^^^^^^^^^^^^^^
  File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\capture.py", line 591, in snap
    self.tmpfile.seek(0)
ValueError: I/O operation on closed file.

```

---

## REPO: ssz-trajectories

### EXECUTION META
- Status: SUCCESS
- Duration: 3.6s
- Exit Code: 0
- Passed: 63
- Failed: 0
- Errors: 0
- Expected: 63

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-trajectories
configfile: pyproject.toml
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 63 items

tests/test_analysis.py::TestAnalyzeOrbit::test_small_b_jumps PASSED      [  1%]
tests/test_analysis.py::TestAnalyzeOrbit::test_b50_jumps PASSED          [  3%]
tests/test_analysis.py::TestAnalyzeOrbit::test_b80_jumps PASSED          [  4%]
tests/test_analysis.py::TestAnalyzeOrbit::test_large_b_no_jumps PASSED   [  6%]
tests/test_analysis.py::TestAnalyzeOrbit::test_phi_total_positive PASSED [  7%]
tests/test_analysis.py::TestAnalyzeOrbit::test_r_range PASSED            [  9%]
tests/test_analysis.py::TestDeflection::test_is_dphi_minus_pi PASSED     [ 11%]
tests/test_analysis.py::TestDeflection::test_positive_deep_orbit PASSED  [ 12%]
tests/test_analysis.py::TestDeflection::test_increases_below_barrier PASSED [ 14%]
tests/test_analysis.py::TestBridgeIdentity::test_exact_at_all_radii PASSED [ 15%]
tests/test_analysis.py::TestBridgeIdentity::test_components PASSED       [ 17%]
tests/test_analysis.py::TestProperLength::test_finite_to_boundary PASSED [ 19%]
tests/test_analysis.py::TestProperLength::test_positive PASSED           [ 20%]
tests/test_analysis.py::TestTortoise::test_finite_no_horizon PASSED      [ 22%]
tests/test_embedding.py::TestXLocal::test_at_rs_strong PASSED            [ 23%]
tests/test_embedding.py::TestXLocal::test_far_field_weak PASSED          [ 25%]
tests/test_embedding.py::TestXLocal::test_monotone_decreasing_outward_blend PASSED [ 26%]
tests/test_embedding.py::TestNLevel::test_N1_at_rs PASSED                [ 28%]
tests/test_embedding.py::TestNLevel::test_N0_far PASSED                  [ 30%]
tests/test_embedding.py::TestEpsilon::test_range PASSED                  [ 31%]
tests/test_embedding.py::TestCountJumps::test_no_jumps PASSED            [ 33%]
tests/test_embedding.py::TestCountJumps::test_one_jump PASSED            [ 34%]
tests/test_embedding.py::TestCountJumps::test_two_jumps PASSED           [ 36%]
tests/test_embedding.py::TestCountJumps::test_empty PASSED               [ 38%]
tests/test_embedding.py::TestCountJumps::test_single PASSED              [ 39%]
tests/test_integrator.py::TestRK4Scalar::test_exponential_decay PASSED   [ 41%]
tests/test_integrator.py::TestRK4Scalar::test_linear_growth PASSED       [ 42%]
tests/test_integrator.py::TestTrapz::test_constant PASSED                [ 44%]
tests/test_integrator.py::TestTrapz::test_linear PASSED                  [ 46%]
tests/test_integrator.py::TestTrapz::test_reversed_limits PASSED         [ 47%]
tests/test_integrator.py::TestNullRadial::test_outgoing_monotone PASSED  [ 49%]
tests/test_integrator.py::TestNullRadial::test_ingoing_monotone PASSED   [ 50%]
tests/test_integrator.py::TestNullRadial::test_speed_bounded PASSED      [ 52%]
tests/test_integrator.py::TestTimeLikeInfall::test_monotone_decrease PASSED [ 53%]
tests/test_integrator.py::TestTimeLikeInfall::test_reaches_boundary PASSED [ 55%]
tests/test_integrator.py::TestNullGeodesic::test_small_b_two_jumps PASSED [ 57%]
tests/test_integrator.py::TestNullGeodesic::test_large_b_no_jumps PASSED [ 58%]
tests/test_integrator.py::TestNullGeodesic::test_turning_point PASSED    [ 60%]
tests/test_integrator.py::TestNullGeodesic::test_phi_increases PASSED    [ 61%]
tests/test_integrator.py::TestTurningPoint::test_exists_for_small_b PASSED [ 63%]
tests/test_integrator.py::TestTurningPoint::test_turning_point_condition PASSED [ 65%]
tests/test_xi.py::TestXiStrong::test_zero_radius PASSED                  [ 66%]
tests/test_xi.py::TestXiStrong::test_negative_radius PASSED              [ 68%]
tests/test_xi.py::TestXiStrong::test_at_rs PASSED                        [ 69%]
tests/test_xi.py::TestXiStrong::test_monotone_increasing PASSED          [ 71%]
tests/test_xi.py::TestXiStrong::test_asymptotic_to_one PASSED            [ 73%]
tests/test_xi.py::TestXiStrong::test_positive PASSED                     [ 74%]
tests/test_xi.py::TestXiWeak::test_at_large_r PASSED                     [ 76%]
tests/test_xi.py::TestXiWeak::test_inversely_proportional PASSED         [ 77%]
tests/test_xi.py::TestXiWeak::test_zero_radius PASSED                    [ 79%]
tests/test_xi.py::TestXiHard::test_strong_regime PASSED                  [ 80%]
tests/test_xi.py::TestXiHard::test_weak_regime PASSED                    [ 82%]
tests/test_xi.py::TestXiHard::test_discontinuity_at_100 PASSED           [ 84%]
tests/test_xi.py::TestXiBlend::test_pure_strong PASSED                   [ 85%]
tests/test_xi.py::TestXiBlend::test_pure_weak PASSED                     [ 87%]
tests/test_xi.py::TestXiBlend::test_smooth_in_blend PASSED               [ 88%]
tests/test_xi.py::TestXiBlend::test_c2_continuity PASSED                 [ 90%]
tests/test_xi.py::TestXiBlend::test_monotone_decreasing_in_blend PASSED  [ 92%]
tests/test_xi.py::TestMetricD::test_D_at_rs PASSED                       [ 93%]
tests/test_xi.py::TestMetricD::test_D_range PASSED                       [ 95%]
tests/test_xi.py::TestMetricD::test_s_inverse_of_D PASSED                [ 96%]
tests/test_xi.py::TestDDerivative::test_positive_in_strong PASSED        [ 98%]
tests/test_xi.py::TestDDerivative::test_finite PASSED                    [100%]

============================= 63 passed in 0.88s ==============================

```

---

## REPO: segmented-energy

### EXECUTION META
- Status: FAILED
- Duration: 4.7s
- Exit Code: 2
- Passed: 0
- Failed: 0
- Errors: 7
- Expected: 6

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\segmented-energy
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 0 items / 3 errors

=================================== ERRORS ====================================
___________________ ERROR collecting FINAL_PERFECT_TEST.py ____________________
ImportError while importing test module 'E:\clone\segmented-energy\FINAL_PERFECT_TEST.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FINAL_PERFECT_TEST.py:27: in <module>
    from astropy import units as u
E   ModuleNotFoundError: No module named 'astropy'
________________ ERROR collecting test_on_complete_dataset.py _________________
ImportError while importing test module 'E:\clone\segmented-energy\test_on_complete_dataset.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_on_complete_dataset.py:17: in <module>
    from astropy import units as u
E   ModuleNotFoundError: No module named 'astropy'
________________ ERROR collecting test_ssz_complete_dataset.py ________________
ImportError while importing test module 'E:\clone\segmented-energy\test_ssz_complete_dataset.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_ssz_complete_dataset.py:17: in <module>
    from astropy import units as u
E   ModuleNotFoundError: No module named 'astropy'
=========================== short test summary info ===========================
ERROR FINAL_PERFECT_TEST.py
ERROR test_on_complete_dataset.py
ERROR test_ssz_complete_dataset.py
!!!!!!!!!!!!!!!!!!! Interrupted: 3 errors during collection !!!!!!!!!!!!!!!!!!!
============================== 3 errors in 2.27s ==============================

```

---

## REPO: g79-cygnus-test

### EXECUTION META
- Status: FAILED
- Duration: 11.8s
- Exit Code: 3
- Passed: 0
- Failed: 0
- Errors: 110
- Expected: 5

### STDOUT (RAW)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\g79-cygnus-test
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... ERROR: No module named 'astroquery'
collected 3 items
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "E:\clone\g79-cygnus-test\scripts\test_irsa_catalogs.py", line 16, in <module>
INTERNALERROR>     from astroquery.ipac.irsa import Irsa
INTERNALERROR> ModuleNotFoundError: No module named 'astroquery'
INTERNALERROR> 
INTERNALERROR> During handling of the above exception, another exception occurred:
INTERNALERROR> 
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 318, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 371, in _main
INTERNALERROR>     config.hook.pytest_collection(session=session)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\logging.py", line 788, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\warnings.py", line 98, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\config\__init__.py", line 1403, in pytest_collection
INTERNALERROR>     return (yield)
INTERNALERROR>             ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 382, in pytest_collection
INTERNALERROR>     session.perform_collect()
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 857, in perform_collect
INTERNALERROR>     self.items.extend(self.genitems(node))
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 1023, in genitems
INTERNALERROR>     yield from self.genitems(subnode)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 1023, in genitems
INTERNALERROR>     yield from self.genitems(subnode)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 1020, in genitems
INTERNALERROR>     rep, duplicate = self._collect_one_node(node, handle_dupes)
INTERNALERROR>                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\main.py", line 883, in _collect_one_node
INTERNALERROR>     rep = collect_one_node(node)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 576, in collect_one_node
INTERNALERROR>     rep: CollectReport = ihook.pytest_make_collect_report(collector=collector)
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\capture.py", line 880, in pytest_make_collect_report
INTERNALERROR>     rep = yield
INTERNALERROR>           ^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pluggy\_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 400, in pytest_make_collect_report
INTERNALERROR>     call = CallInfo.from_call(
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 353, in from_call
INTERNALERROR>     result: TResult | None = func()
INTERNALERROR>                              ^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\runner.py", line 398, in collect
INTERNALERROR>     return list(collector.collect())
INTERNALERROR>                 ^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 563, in collect
INTERNALERROR>     self._register_setup_module_fixture()
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 576, in _register_setup_module_fixture
INTERNALERROR>     self.obj, ("setUpModule", "setup_module")
INTERNALERROR>     ^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 289, in obj
INTERNALERROR>     self._obj = obj = self._getobj()
INTERNALERROR>                       ^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 560, in _getobj
INTERNALERROR>     return importtestmodule(self.path, self.config)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py", line 507, in importtestmodule
INTERNALERROR>     mod = import_path(
INTERNALERROR>           ^^^^^^^^^^^^
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\pathlib.py", line 587, in import_path
INTERNALERROR>     importlib.import_module(module_name)
INTERNALERROR>   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py", line 90, in import_module
INTERNALERROR>     return _bootstrap._gcd_import(name[level:], package, level)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
INTERNALERROR>   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
INTERNALERROR>   File "C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\assertion\rewrite.py", line 197, in exec_module
INTERNALERROR>     exec(co, module.__dict__)
INTERNALERROR>   File "E:\clone\g79-cygnus-test\scripts\test_irsa_catalogs.py", line 21, in <module>
INTERNALERROR>     sys.exit(1)
INTERNALERROR> SystemExit: 1

============================= 1 warning in 9.06s ==============================

```

### STDERR (RAW)

```
mainloop: caught unexpected SystemExit!

```

