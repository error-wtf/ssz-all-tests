# SSZ COMPLETE FULL OUTPUT - ALL REPOS, ALL TESTS, NO TRUNCATION

**Generated:** 2026-04-28T00:02:35.234157
**Total Duration:** 152.9s
**System:** nt
**Python:** 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
**Command:** `pytest -v -s --tb=long --capture=no`

================================================================================
GLOBAL SUMMARY
================================================================================

- Total Repositories: 10
- Successful: 6
- Failed/Error: 4

================================================================================
REPO: ssz-qubits
Status: SUCCESS
Exit Code: 0
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-qubits
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 184 items

tests/test_edge_cases.py::TestExtremeRadii::test_very_small_radius 
======================================================================
EDGE CASE: Very Small Radius (near r_s)
======================================================================
r_s (Earth) = 8.869806e-03 m
r = 10 * r_s = 8.869806e-02 m
Xi = 1.000000
D_SSZ = 0.500000

Physical Interpretation:
  -> Near r_s: strong field regime
  -> Xi becomes significant (not << 1)
  -> D_SSZ deviates significantly from 1
======================================================================
PASSED
tests/test_edge_cases.py::TestExtremeRadii::test_very_large_radius 
======================================================================
EDGE CASE: Very Large Radius (1 AU)
======================================================================
r = 1 AU = 1.496e+11 m
Xi = 2.964507e-14
D_SSZ = 0.999999999999970
1 - D_SSZ = 2.975398e-14

Physical Interpretation:
  -> At 1 AU from Earth: essentially flat spacetime
  -> SSZ effects from Earth are negligible
======================================================================
PASSED
tests/test_edge_cases.py::TestExtremeRadii::test_radius_at_schwarzschild 
======================================================================
EDGE CASE: Exactly at Schwarzschild Radius
======================================================================
r = r_s = 8.869806e-03 m
Xi = 0.801712
D_SSZ = 0.555028

Physical Interpretation:
  -> At r = r_s: Xi = 0.5 (strong field)
  -> D_SSZ = 2/3 (significant time dilation)
  -> Note: This is inside Earth! (unphysical for Earth)
======================================================================
PASSED
tests/test_edge_cases.py::TestExtremeMasses::test_zero_mass 
======================================================================
EDGE CASE: Zero Mass (Flat Spacetime)
======================================================================
M = 0 kg
r_s = 0.0 m
Xi = 0.0

Physical Interpretation:
  -> Zero mass = flat spacetime
  -> No gravitational effects
======================================================================
PASSED
tests/test_edge_cases.py::TestExtremeMasses::test_solar_mass 
======================================================================
EDGE CASE: Solar Mass
======================================================================
M = M_Sun = 1.989e+30 kg
r = 1 AU = 1.496e+11 m
Xi = 9.873418e-09
D_SSZ = 0.999999990126582

Physical Interpretation:
  -> At Earth's orbit: weak field from Sun
  -> GPS must correct for this solar effect
======================================================================
PASSED
tests/test_edge_cases.py::TestExtremeMasses::test_black_hole_mass 
======================================================================
EDGE CASE: Stellar Black Hole (10 M_Sun)
======================================================================
M = 10 M_Sun = 1.989e+31 kg
r_s = 29.541 km
r = 100 r_s = 2954.127 km
Xi = 1.000000
D_SSZ = 0.500000

Physical Interpretation:
  -> Even at 100 r_s from black hole: measurable SSZ effects
  -> Qubits near black holes would experience strong effects
======================================================================
PASSED
tests/test_edge_cases.py::TestQubitConfigurations::test_identical_qubits 
======================================================================
EDGE CASE: Identical Qubit Positions
======================================================================
Both qubits at same position
Separation: 0.0 m
Delta Xi: 0.0
Delta D_SSZ: 0.0

Physical Interpretation:
  -> Identical positions = no SSZ mismatch
  -> Perfect segment coherence (unrealistic but valid)
======================================================================
PASSED
tests/test_edge_cases.py::TestQubitConfigurations::test_very_distant_qubits 
======================================================================
EDGE CASE: Very Distant Qubits (1 km separation)
======================================================================
Separation: 1000.0 m
Height difference: 0 m
Delta Xi: 0.000000e+00

Physical Interpretation:
  -> Horizontal separation doesn't change Xi (same height)
  -> Only vertical (radial) separation matters for SSZ
======================================================================
PASSED
tests/test_edge_cases.py::TestQubitConfigurations::test_negative_coordinates 
======================================================================
EDGE CASE: Negative Coordinates
======================================================================
Q1 position: (-0.001, -0.001, 0.001)
Q2 position: (0.001, 0.001, 0.001)
Q1 Xi: 6.961078e-10
Q2 Xi: 6.961078e-10
Separation: 2.828 mm

Physical Interpretation:
  -> x,y coordinates don't affect Xi (only z/height matters)
  -> Negative coordinates are valid
======================================================================
PASSED
tests/test_edge_cases.py::TestQubitConfigurations::test_underground_qubit 
======================================================================
EDGE CASE: Underground Qubit (z < 0)
======================================================================
Qubit at z = -100 m (underground)
R from Earth center: 6.370900 Mm
Xi: 6.961187e-10
D_SSZ: 0.999999999303881

Physical Interpretation:
  -> Underground: closer to Earth center
  -> Higher Xi = stronger gravitational effect
  -> Time runs slower underground
======================================================================
PASSED
tests/test_edge_cases.py::TestNumericalPrecision::test_float_precision_xi 
======================================================================
EDGE CASE: Float Precision in Xi
======================================================================
r1 = 6.371000000000000e+06 m
r2 = 6.371001000000000e+06 m
Delta r = 1.000000e+00 m
Xi1 = 6.961078186654634e-10
Xi2 = 6.961077094035407e-10
Delta Xi = 1.092619227390696e-16

Physical Interpretation:
  -> Float64 can resolve meter-scale differences in Xi
  -> Important for precision qubit positioning
======================================================================
PASSED
tests/test_edge_cases.py::TestNumericalPrecision::test_time_dilation_precision 
======================================================================
EDGE CASE: Time Dilation Precision
======================================================================
D_SSZ = 0.99999999930389216196
1 - D_SSZ = 6.96107838038528825564e-10

Physical Interpretation:
  -> Float64 has enough precision for Earth-surface SSZ
  -> Can measure ~10^-10 deviations from unity
======================================================================
PASSED
tests/test_edge_cases.py::TestNumericalPrecision::test_gradient_numerical_vs_analytical 
======================================================================
EDGE CASE: Gradient Numerical vs Analytical
======================================================================
Analytical gradient: -1.0926193983e-16 /m
Numerical gradient: -1.0926193985e-16 /m
Relative error: 1.833127e-10

Physical Interpretation:
  -> Analytical and numerical gradients agree
  -> Validates the gradient formula
======================================================================
PASSED
tests/test_edge_cases.py::TestErrorHandling::test_zero_radius_error 
======================================================================
EDGE CASE: Zero Radius Error
======================================================================
Error message: Radius must be positive, got r=0

Physical Interpretation:
  -> r=0 is a singularity, correctly rejected
======================================================================
PASSED
tests/test_edge_cases.py::TestErrorHandling::test_negative_radius_error 
======================================================================
EDGE CASE: Negative Radius Error
======================================================================
Error message: Radius must be positive, got r=-1000

Physical Interpretation:
  -> Negative radius is unphysical, correctly rejected
======================================================================
PASSED
tests/test_edge_cases.py::TestErrorHandling::test_optimal_height_zero_xi 
======================================================================
EDGE CASE: Optimal Height for Xi=0
======================================================================
Error message: Target Xi must be positive

Physical Interpretation:
  -> Xi=0 requires infinite distance (unphysical)
======================================================================
PASSED
tests/test_edge_cases.py::TestErrorHandling::test_optimal_height_negative_xi 
======================================================================
EDGE CASE: Optimal Height for Xi<0
======================================================================
Error message: Target Xi must be positive

Physical Interpretation:
  -> Negative Xi is unphysical (no negative curvature)
======================================================================
PASSED
tests/test_edge_cases.py::TestSpecialQubitProperties::test_zero_coherence_time 
======================================================================
EDGE CASE: Zero Coherence Time
======================================================================
Error (expected): float division by zero

Physical Interpretation:
  -> T2=0 means instant decoherence (infinite rate)
======================================================================
PASSED
tests/test_edge_cases.py::TestSpecialQubitProperties::test_very_long_coherence_time 
======================================================================
EDGE CASE: Very Long Coherence Time (1 second)
======================================================================
Base T2: 1.0 s
SSZ decoherence rate: 1.000000e+00 /s
Effective T2: 1.000000 s

Physical Interpretation:
  -> Even with 1s T2, SSZ effects are present
  -> Long-lived qubits accumulate more SSZ phase drift
======================================================================
PASSED
tests/test_edge_cases.py::TestSpecialQubitProperties::test_very_short_gate_time 
======================================================================
EDGE CASE: Very Short Gate Time (1 ps)
======================================================================
Gate time: 1 ps
Optimal gate time: 1.000000 ps
Timing asymmetry: 0.000000e+00

Physical Interpretation:
  -> Ultra-fast gates have less time for SSZ drift
  -> But timing precision requirements increase
======================================================================
PASSED
tests/test_edge_cases.py::TestQECEdgeCases::test_syndrome_weight_bounds 
======================================================================
EDGE CASE: Syndrome Weight Bounds
======================================================================
h=  -1000m: X-weight=1.000000, Z-weight=1.000000
h=      0m: X-weight=1.000000, Z-weight=1.000000
h=   1000m: X-weight=1.000000, Z-weight=1.000000
h=  10000m: X-weight=1.000000, Z-weight=1.000000
h= 100000m: X-weight=1.000000, Z-weight=1.000000

Physical Interpretation:
  -> Syndrome weights always in [0,1] regardless of position
======================================================================
PASSED
tests/test_edge_cases.py::TestQECEdgeCases::test_logical_error_rate_bounds 
======================================================================
EDGE CASE: Logical Error Rate Bounds
======================================================================
p=1e-04, d=3: p_L=1.000000e-04
p=1e-04, d=5: p_L=1.000000e-06
p=1e-04, d=7: p_L=1.000000e-08
p=1e-03, d=3: p_L=1.000000e-02
p=1e-03, d=5: p_L=1.000000e-03
p=1e-03, d=7: p_L=1.000000e-04
p=1e-02, d=3: p_L=1.000000e+00
p=1e-02, d=5: p_L=1.000000e+00
p=1e-02, d=7: p_L=1.000000e+00
p=1e-01, d=3: p_L=1.000000e+00
p=1e-01, d=5: p_L=1.000000e+00
p=1e-01, d=7: p_L=1.000000e+00

Physical Interpretation:
  -> Logical error rate always valid probability
  -> Higher distance = lower logical error (below threshold)
======================================================================
PASSED
tests/test_edge_cases.py::TestQECEdgeCases::test_single_qubit_array 
======================================================================
EDGE CASE: Single Qubit Array
======================================================================
Number of qubits: 1
Xi mean: 6.961078e-10
Xi std: 0.0
Uniformity: 1.0

Physical Interpretation:
  -> Single qubit: trivially uniform
======================================================================
PASSED
tests/test_edge_cases.py::TestSegmentCoherentZone::test_coherent_zone_contains_center 
======================================================================
EDGE CASE: Coherent Zone Contains Center
======================================================================
Center height: 100 m
Coherent zone: [90.847395, 109.152605] m
Zone width: 18.305210 m

Physical Interpretation:
  -> Coherent zone is symmetric around center
  -> Width depends on allowed Xi variation
======================================================================
PASSED
tests/test_edge_cases.py::TestSegmentCoherentZone::test_coherent_zone_width_scales 
======================================================================
EDGE CASE: Coherent Zone Width Scaling
======================================================================
Max Xi variation: 1e-17 -> Zone width: 0.183046 m
Max Xi variation: 1e-16 -> Zone width: 1.830464 m
Max Xi variation: 1e-15 -> Zone width: 18.304636 m
Max Xi variation: 1e-14 -> Zone width: 183.046357 m

Physical Interpretation:
  -> Tighter Xi tolerance = narrower coherent zone
  -> Trade-off between precision and usable volume
======================================================================
PASSED
tests/test_edge_cases.py::TestPhaseDriftBoundary::test_zero_height_difference PASSED
tests/test_edge_cases.py::TestPhaseDriftBoundary::test_zero_frequency_phase_drift PASSED
tests/test_entanglement.py::TestPhaseDrift::test_phase_drift_1mm PASSED
tests/test_entanglement.py::TestPhaseDrift::test_phase_drift_linear_scaling PASSED
tests/test_entanglement.py::TestPhaseDrift::test_signed_delta_D PASSED
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_zero_phase PASSED
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_pi_phase PASSED
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_formula PASSED
tests/test_entanglement.py::TestBellStateFidelity::test_fidelity_paper_value PASSED
tests/test_entanglement.py::TestBellStateFidelity::test_small_angle_approximation PASSED
tests/test_entanglement.py::TestCHSHParameter::test_chsh_max PASSED
tests/test_entanglement.py::TestCHSHParameter::test_chsh_zero PASSED
tests/test_entanglement.py::TestCHSHParameter::test_chsh_classical_bound PASSED
tests/test_entanglement.py::TestCHSHParameter::test_chsh_formula PASSED
tests/test_entanglement.py::TestCharacteristicTime::test_T_SSZ_1mm PASSED
tests/test_entanglement.py::TestCharacteristicTime::test_T_SSZ_scaling PASSED
tests/test_entanglement.py::TestCharacteristicTime::test_T_SSZ_zero_height PASSED
tests/test_entanglement.py::TestCorrectionInterval::test_correction_interval_paper_value PASSED
tests/test_entanglement.py::TestCorrectionInterval::test_correction_interval_zero_drift PASSED
tests/test_entanglement.py::TestCorrectionGate::test_correction_higher_A PASSED
tests/test_entanglement.py::TestCorrectionGate::test_correction_higher_B PASSED
tests/test_entanglement.py::TestCoherentZone::test_same_height_in_zone PASSED
tests/test_entanglement.py::TestCoherentZone::test_small_separation_in_zone PASSED
tests/test_entanglement.py::TestCoherentZone::test_large_separation_out_of_zone PASSED
tests/test_entanglement.py::TestFullAnalysis::test_analysis_1mm PASSED
tests/test_paper_a_support.py::TestGRComparison::test_ssz_equals_gr_weak_field PASSED
tests/test_paper_a_support.py::TestGRComparison::test_weak_field_detection PASSED
tests/test_paper_a_support.py::TestGRComparison::test_gr_formula PASSED
tests/test_paper_a_support.py::TestFidelityReduction::test_small_angle_formula PASSED
tests/test_paper_a_support.py::TestFidelityReduction::test_paper_value PASSED
tests/test_paper_a_support.py::TestFidelityReduction::test_approximation_validity PASSED
tests/test_paper_a_support.py::TestLinearScaling::test_is_linear PASSED
tests/test_paper_a_support.py::TestLinearScaling::test_scaling_constant PASSED
tests/test_paper_a_support.py::TestNumericalStability::test_closed_form_works PASSED
tests/test_paper_a_support.py::TestNumericalStability::test_direct_fails PASSED
tests/test_paper_a_support.py::TestNumericalStability::test_stability_demonstrated PASSED
tests/test_paper_a_support.py::TestCoherentZone::test_zone_width_formula PASSED
tests/test_paper_a_support.py::TestCoherentZone::test_zone_width_value PASSED
tests/test_paper_a_support.py::TestCoherentZone::test_half_width PASSED
tests/test_paper_a_support.py::TestDecoherenceEnhancement::test_unity_for_small_delta_xi PASSED
tests/test_paper_a_support.py::TestDecoherenceEnhancement::test_formula PASSED
tests/test_paper_c_support.py::TestPrediction1PhaseDrift::test_phase_drift_value PASSED
tests/test_paper_c_support.py::TestPrediction1PhaseDrift::test_phase_drift_above_falsification_threshold PASSED
tests/test_paper_c_support.py::TestPrediction2CoherentZone::test_zone_width_at_1e18 PASSED
tests/test_paper_c_support.py::TestPrediction2CoherentZone::test_zone_width_formula PASSED
tests/test_paper_c_support.py::TestPrediction3FrequencyScaling::test_frequency_ratio PASSED
tests/test_paper_c_support.py::TestPrediction3FrequencyScaling::test_ratio_above_falsification_threshold PASSED
tests/test_paper_c_support.py::TestPrediction4Compensation::test_compensation_possible PASSED
tests/test_paper_c_support.py::TestPrediction4Compensation::test_deterministic_compensation PASSED
tests/test_paper_c_support.py::TestPrediction5CrossZoneDrift::test_cross_zone_drift_value PASSED
tests/test_paper_c_support.py::TestPrediction5CrossZoneDrift::test_drift_above_falsification_threshold PASSED
tests/test_paper_c_support.py::TestScalingAnalysis::test_height_linearity PASSED
tests/test_paper_c_support.py::TestScalingAnalysis::test_frequency_linearity PASSED
tests/test_paper_c_support.py::TestScalingAnalysis::test_time_linearity PASSED
tests/test_paper_c_support.py::TestConfoundDiscrimination::test_ssz_is_deterministic PASSED
tests/test_paper_c_support.py::TestConfoundDiscrimination::test_ssz_is_monotonic_in_height PASSED
tests/test_paper_c_support.py::TestConfoundDiscrimination::test_ssz_scales_with_omega PASSED
tests/test_paper_c_support.py::TestMeasurementRequirements::test_phase_precision_achievable PASSED
tests/test_paper_c_support.py::TestMeasurementRequirements::test_height_precision_achievable PASSED
tests/test_paper_c_support.py::TestIntegration::test_paper_c_module_imports PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_schwarzschild_radius_earth [PASS] r_s(Earth) = 8.869806e-03 m (paper: 8.870e-03 m)
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_xi_formula_weak_field [PASS] Xi formula: r_s/(2r) = 6.961078e-10
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_xi_at_earth_surface [PASS] Xi(Earth surface) = 6.961078e-10 (paper: 6.96e-10)
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_xi_dimensionless [PASS] Xi is dimensionless: 6.961078e-10
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_d_ssz_formula [PASS] D_SSZ formula: 1/(1+Xi) = 0.999999999304
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_d_ssz_at_earth_surface [PASS] D_SSZ(Earth) = 0.999999999304 (paper: 0.999999999304)
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_gr_consistency_weak_field [PASS] GR consistency: D_SSZ=0.999999999304, D_GR=0.999999999304
       Relative difference: 0.00e+00
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_gr_taylor_expansion [PASS] Taylor expansion valid: error < 1e-9
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_delta_d_formula [PASS] Delta_D formula: 1.092619e-16 (impl: 1.092619e-16)
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_phase_drift_formula [PASS] Phase drift formula: 3.43e-10 rad
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_phase_drift_units [PASS] Phase drift units: 3.141593e-10 rad
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_numerical_example_transmon_1mm [PASS] Transmon 1mm: 6.87e-13 rad (paper: 6.87e-13)
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_numerical_example_transmon_1m [PASS] Transmon 1m: 6.87e-10 rad (paper: 6.87e-10)
PASSED
tests/test_paper_d_validation.py::TestSection3Theory::test_numerical_example_optical_1m [PASS] Optical 1m: 0.59 rad (paper: 0.59)
PASSED
tests/test_paper_d_validation.py::TestSection4Compensation::test_compensation_formula [PASS] Compensation cancels drift: 0.00e+00
PASSED
tests/test_paper_d_validation.py::TestSection4Compensation::test_compensation_is_deterministic [PASS] Drift is deterministic: 100 identical results
PASSED
tests/test_paper_d_validation.py::TestSection5Experiments::test_chip_tilt_geometry [PASS] Chip tilt 5deg: delta_h = 1.74 mm
[PASS] Chip tilt 10deg: delta_h = 3.47 mm
PASSED
tests/test_paper_d_validation.py::TestSection5Experiments::test_upper_bound_calculation [PASS] Upper bound: sigma_averaged=3.2e-05, sigma_slope=9.0e-03 rad/m
PASSED
tests/test_paper_d_validation.py::TestSection6Statistics::test_power_analysis_optical [PASS] Power analysis: N_required ~ 1 for 3-sigma (paper: ~25 conservative)
PASSED
tests/test_paper_d_validation.py::TestSection6Statistics::test_slope_fitting_concept [PASS] Slope fitting: alpha_fit = 5.89e-01, alpha_ssz = 5.89e-01
PASSED
tests/test_paper_d_validation.py::TestSection7Feasibility::test_12_oom_gap [PASS] Gap = 10^12.2 (paper: ~10^12)
PASSED
tests/test_paper_d_validation.py::TestSection7Feasibility::test_platform_comparison_frequency_ratio [PASS] Frequency ratio: 8.6e+04
PASSED
tests/test_paper_d_validation.py::TestSection7Feasibility::test_platform_comparison_coherence_ratio [PASS] Coherence ratio: 1e+04
PASSED
tests/test_paper_d_validation.py::TestSection7Feasibility::test_platform_comparison_phase_ratio [PASS] Phase ratio: 8.6e+08
PASSED
tests/test_paper_d_validation.py::TestStrongFieldPredictions::test_strong_field_xi_at_horizon [PASS] Xi(r_s) = 0.802 (strong field)
PASSED
tests/test_paper_d_validation.py::TestStrongFieldPredictions::test_strong_field_d_ssz_finite_at_horizon [PASS] D_SSZ(r_s) = 0.555 (finite, not 0 like GR)
PASSED
tests/test_paper_d_validation.py::TestStrongFieldPredictions::test_gr_diverges_at_horizon [PASS] D_GR(r_s) = 0.0 (singularity)
PASSED
tests/test_paper_d_validation.py::TestHistoricalValidation::test_gps_time_drift [PASS] GPS drift: 45.7 us/day
PASSED
tests/test_paper_d_validation.py::TestHistoricalValidation::test_pound_rebka_prediction [PASS] Pound-Rebka: 2.46e-15 (theory: 2.46e-15)
PASSED
tests/test_paper_d_validation.py::TestLinearScaling::test_linear_in_height [PASS] Linear in height: phi/h = 6.87e-10 rad/m
PASSED
tests/test_paper_d_validation.py::TestLinearScaling::test_linear_in_omega [PASS] Linear in omega: phi/omega = 2.19e-20 s
PASSED
tests/test_paper_d_validation.py::TestLinearScaling::test_linear_in_time [PASS] Linear in time: phi/t = 6.87e-06 rad/s
PASSED
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_phase_drift_formula PASSED
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_effect_is_deterministic PASSED
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_phase_drift_scales_with_height PASSED
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_phase_drift_scales_with_time PASSED
tests/test_roadmap_validation.py::TestH1DeterministicPhaseBias::test_compensation_is_possible PASSED
tests/test_roadmap_validation.py::TestH2CoherentZones::test_zone_width_formula PASSED
tests/test_roadmap_validation.py::TestH2CoherentZones::test_zone_width_scales_with_epsilon PASSED
tests/test_roadmap_validation.py::TestH2CoherentZones::test_cross_zone_bias PASSED
tests/test_roadmap_validation.py::TestH3Scaling::test_accumulated_drift_grows_with_coherence PASSED
tests/test_roadmap_validation.py::TestH3Scaling::test_effect_grows_with_height_difference PASSED
tests/test_roadmap_validation.py::TestH3Scaling::test_macroscopic_height_measurable PASSED
tests/test_roadmap_validation.py::TestWP1Simulation::test_baseline_has_unity_fidelity PASSED
tests/test_roadmap_validation.py::TestWP1Simulation::test_ssz_drift_reduces_fidelity PASSED
tests/test_roadmap_validation.py::TestWP1Simulation::test_compensation_recovers_fidelity PASSED
tests/test_roadmap_validation.py::TestFalsifiability::test_height_dependence_exists PASSED
tests/test_roadmap_validation.py::TestFalsifiability::test_correct_omega_scaling PASSED
tests/test_roadmap_validation.py::TestFalsifiability::test_monotonic_in_height PASSED
tests/test_roadmap_validation.py::TestIntegration::test_roadmap_validation_runs PASSED
tests/test_ssz_physics.py::TestSchwarzschildRadius::test_earth_schwarzschild_radius 
======================================================================
TEST: Earth Schwarzschild Radius
======================================================================
Calculated r_s = 8.869806 mm
Expected r_s = 8.869806 mm

Physical Interpretation:
  -> Earth's r_s is tiny: ~8.87 mm
  -> r_s/R_Earth = 1.39e-09
======================================================================
PASSED
tests/test_ssz_physics.py::TestSchwarzschildRadius::test_sun_schwarzschild_radius 
======================================================================
TEST: Sun Schwarzschild Radius
======================================================================
Calculated r_s = 2.954 km
======================================================================
PASSED
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_at_earth_surface 
======================================================================
TEST: Xi at Earth Surface (Weak Field)
======================================================================
Xi(R_Earth) = 6.961078e-10
Expected ~ 7e-10 (weak field)

Physical Interpretation:
  -> Xi << 1 confirms Earth's surface is in weak-field regime
  -> SSZ effects are small but measurable with precision instruments
======================================================================
PASSED
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_decreases_with_radius 
======================================================================
TEST: Xi Decreases with Radius (1/r scaling)
======================================================================
Xi(R) = 6.961078e-10
Xi(2R) = 3.480539e-10
Xi(R)/Xi(2R) = 2.000000

Physical Interpretation:
  -> Xi = r_s/(2r) falls off as 1/r
  -> Doubling distance halves segment density
======================================================================
PASSED
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_positive_definite 
======================================================================
TEST: Xi Positive Definite
======================================================================
     Radius [m] |              Xi
-----------------------------------
       1.00e+03 |    4.434903e-06
       1.00e+06 |    4.434903e-09
       6.37e+06 |    6.961078e-10
       1.00e+09 |    4.434903e-12
       1.00e+12 |    4.434903e-15
======================================================================
PASSED
tests/test_ssz_physics.py::TestSegmentDensityWeakField::test_xi_formula_weak_field 
======================================================================
TEST: Xi Formula Verification (Weak Field)
======================================================================
Xi (function) = 6.9599857387e-10
r_s/(2r) = 6.9599857387e-10
======================================================================
PASSED
tests/test_ssz_physics.py::TestSegmentGradientWeakField::test_gradient_negative 
======================================================================
TEST: Gradient is Negative (Weak Field)
======================================================================
dXi/dr at Earth surface = -1.092619e-16 /m

Physical Interpretation:
  -> Xi DECREASES with r (weak field)
  -> Moving away from mass reduces segment density
======================================================================
PASSED
tests/test_ssz_physics.py::TestSegmentGradientWeakField::test_gradient_scales_as_1_over_r_squared 
======================================================================
TEST: Gradient 1/r^2 Scaling
======================================================================
|dXi/dr|(R) = 1.092619e-16 /m
|dXi/dr|(2R) = 2.731548e-17 /m
Ratio = 4.000000
Expected (2R/R)^2 = 4.0
======================================================================
PASSED
tests/test_ssz_physics.py::TestSSZTimeDilationWeakField::test_time_dilation_at_earth_surface 
======================================================================
TEST: D_SSZ at Earth Surface
======================================================================
D_SSZ(R_Earth) = 0.999999999303892
Deviation from 1 = 6.961078e-10

Physical Interpretation:
  -> D_SSZ ~ 1 - Xi ~ 0.9999999993
  -> Time runs ~0.7 nanoseconds slower per second
======================================================================
PASSED
tests/test_ssz_physics.py::TestSSZTimeDilationWeakField::test_time_dilation_formula 
======================================================================
TEST: D_SSZ Formula Verification
======================================================================
Xi = 6.959986e-10
D_SSZ (function) = 0.999999999304001
1/(1+Xi) = 0.999999999304001
======================================================================
PASSED
tests/test_ssz_physics.py::TestSSZTimeDilationWeakField::test_time_dilation_increases_with_altitude 
======================================================================
TEST: Time Dilation Altitude Dependence
======================================================================
  Height [m] |                D_SSZ
----------------------------------------
           0 |    0.999999999303892
         100 |    0.999999999303903
        1000 |    0.999999999304001
       10000 |    0.999999999304983

Physical Interpretation:
  -> Time runs FASTER at higher altitude
  -> This is the gravitational time dilation effect
======================================================================
PASSED
tests/test_ssz_physics.py::TestQubitAnalysisWeakField::test_qubit_at_earth_surface 
======================================================================
TEST: Qubit at Earth Surface
======================================================================
Position: z = 0 m (sea level)
Xi = 6.961078e-10
D_SSZ = 0.999999999303892
dXi/dr = -1.092619e-16

Physical Interpretation:
  -> Earth surface is in weak-field regime
  -> Xi ~ 7e-10, D_SSZ ~ 0.9999999993
======================================================================
PASSED
tests/test_ssz_physics.py::TestQubitAnalysisWeakField::test_qubit_pair_mismatch 
======================================================================
TEST: Qubit Pair Segment Mismatch
======================================================================
Height difference: 1000 m
Delta Xi: 1.092448e-13
Delta D_SSZ: 1.092459e-13

Physical Interpretation:
  -> Height difference causes segment mismatch
  -> This affects two-qubit gate fidelity
======================================================================
PASSED
tests/test_ssz_physics.py::TestGoldenRatio::test_phi_value 
======================================================================
TEST: Golden Ratio Value
======================================================================
PHI (constant) = 1.618033988749895
(1+sqrt(5))/2 = 1.618033988749895
======================================================================
PASSED
tests/test_ssz_physics.py::TestGoldenRatio::test_phi_property 
======================================================================
TEST: Golden Ratio Property
======================================================================
phi^2 = 2.618033988749895
phi + 1 = 2.618033988749895
======================================================================
PASSED
tests/test_ssz_physics.py::TestStrongFieldRegime::test_strong_field_xi_at_schwarzschild 
======================================================================
TEST: Xi at Schwarzschild Radius (Strong Field)
======================================================================
Xi(r_s) = 0.801712
Expected ~ 0.8 (from 1 - exp(-phi))

Physical Interpretation:
  -> Strong field uses saturation formula
  -> Xi ~ 0.8 at Schwarzschild radius
======================================================================
PASSED
tests/test_ssz_physics.py::TestStrongFieldRegime::test_strong_field_d_ssz_finite_at_horizon 
======================================================================
TEST: D_SSZ Finite at Horizon (Strong Field)
======================================================================
D_SSZ(r_s) = 0.555028
Expected ~ 0.555

Physical Interpretation:
  -> GR: D_GR(r_s) = 0 (singularity!)
  -> SSZ: D_SSZ(r_s) ~ 0.555 (FINITE!)
  -> SSZ resolves event horizon singularity
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestSegmentedTimeClock::test_local_segment_time_as_reference 
======================================================================
TEST: Lokale Segmentzeit als Qubit-Referenzuhr
======================================================================
Qubit 1: h = 0 m, Xi = 6.961078186654634e-10
Qubit 2: h = 1.0 m, Xi = 6.961077094035407e-10
Delta Xi = 1.092619e-16

** SSZ-ANWENDUNG **
-> Xi(r) definiert lokale 'Segmentzeit'
-> Keine externe Synchronisation nötig!
-> Timing ist GEOMETRISCH festgelegt
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestSegmentedTimeClock::test_geometric_timing_for_gates 
======================================================================
TEST: Geometrisches Gate-Timing
======================================================================
Nominale Gate-Zeit: 50.000 ns
D_SSZ = 0.999999999303892
Korrigierte Gate-Zeit: 50.000000034805389 ns
Korrektur: 34.805391 as (Attosekunden)

** SSZ-ANWENDUNG **
-> Gate-Timing aus D_SSZ berechnet
-> Weniger Fehler bei Zwei-Qubit-Gates
-> Weniger Drift in Superposition
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestSegmentedTimeClock::test_two_qubit_gate_sync 
======================================================================
TEST: Zwei-Qubit-Gate SSZ-Synchronisation
======================================================================
Höhendifferenz: 10.000 mm
Optimale Gate-Zeit: 50.000000 ns
Timing-Asymmetrie: 0.000000e+00
Max Fidelity-Verlust: 0.000000e+00

** SSZ-ANWENDUNG **
-> SSZ berechnet optimales gemeinsames Timing
-> Timing-Asymmetrie wird kompensiert
-> Gate-Fidelity wird maximiert
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestDecoherenceGeometry::test_segment_mismatch_causes_decoherence 
======================================================================
TEST: Segment-Mismatch verursacht Decoherence
======================================================================
 Höhendiff [mm] |        Delta Xi |   Decoherence-Faktor
-------------------------------------------------------
          0.000 |    0.000000e+00 |             1.000000
          1.000 |    1.092620e-19 |             1.000000
         10.000 |    1.092619e-18 |             1.000000
        100.000 |    1.092619e-17 |             1.000000
       1000.000 |    1.092619e-16 |             1.000000

** SSZ-ERKENNTNIS **
-> Decoherence ist NICHT nur thermisches Rauschen!
-> Qubits in verschiedenen Segmenten = verschiedene Zeit
-> Sie decoherieren weil sie METRIKVERSCHOBEN sind
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestDecoherenceGeometry::test_coherent_segment_zone 
======================================================================
TEST: Geometrisch kohärente Segmentzonen
======================================================================
Referenzhöhe: 0 m
Ziel-Xi: 6.961078186654634e-10
Toleranz: 1e-18
Kohärente Zone: 0.000 um bis 18304.636 um
Zonenbreite: 18304.636 um

** SSZ-LÖSUNG **
-> Platziere Qubits in kohärenten Segmentzonen!
-> Nicht nur nach Abstand oder Kühlung optimieren
-> GEOMETRISCHE Kohärenz ist der Schlüssel
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestDecoherenceGeometry::test_decoherence_rate_from_gradient 
======================================================================
TEST: Decoherence-Rate aus Segment-Gradient
======================================================================
|dXi/dr|: 1.092619e-16 /m
SSZ Decoherence Rate: 1.000000e+04 /s
Intrinsische T2: 100.0 us
Effektive T2: 100.000 us

** SSZ-PHYSIK **
-> Decoherence-Rate proportional zu |dXi/dr| * L_qubit
-> Größere Qubits = mehr Segment-Variation = mehr Decoherence
-> SSZ erklärt 'unerklärliche' Decoherence-Quellen!
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestGravitationalDrift::test_nanometer_height_difference 
======================================================================
TEST: Nanometer-Höhenunterschiede
======================================================================
 Höhendiff [nm] |             Delta Xi |          Delta D_SSZ
------------------------------------------------------------
              1 |         1.033976e-25 |         0.000000e+00
             10 |         1.137373e-24 |         0.000000e+00
            100 |         1.085675e-23 |         0.000000e+00
           1000 |         1.092912e-22 |         0.000000e+00

** SSZ-PRÄZISION **
-> Xi(r) ist punktgenau berechenbar!
-> Selbst Nanometer-Unterschiede sind vorhersagbar
-> Keine 'unvorhersehbaren' Gate Errors mehr
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestGravitationalDrift::test_qubit_array_drift_map 
======================================================================
TEST: Qubit-Array Drift-Map
======================================================================
Qubit-Array (3x3):
   ID |     z [um] |                   Xi |                D_SSZ
------------------------------------------------------------
  Q00 |     -700.0 | 6.961078187419467e-10 |    0.999999999303892
  Q01 |     -500.0 | 6.961078187200943e-10 |    0.999999999303892
  Q02 |     -300.0 | 6.961078186982420e-10 |    0.999999999303892
  Q10 |     -200.0 | 6.961078186873158e-10 |    0.999999999303892
  Q11 |        0.0 | 6.961078186654634e-10 |    0.999999999303892
  Q12 |      200.0 | 6.961078186436110e-10 |    0.999999999303892
  Q20 |      300.0 | 6.961078186326847e-10 |    0.999999999303892
  Q21 |      500.0 | 6.961078186108324e-10 |    0.999999999303892
  Q22 |      700.0 | 6.961078185889800e-10 |    0.999999999303892

Array-Uniformität:
  Xi Range: 1.529667e-19
  Xi Std: 4.804214e-20
  Uniformitäts-Score: 1.000000

** SSZ-ANWENDUNG **
-> Komplette Drift-Map des Arrays berechenbar
-> Identifiziere problematische Qubit-Positionen
-> Optimiere Array-Layout für minimale Drift
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestGravitationalDrift::test_predict_gate_error_from_position 
======================================================================
TEST: Gate-Error-Vorhersage aus Position
======================================================================
Qubit 1: z = 0.0 mm
Qubit 2: z = 1.5 mm
Höhendifferenz: 1.5 mm

SSZ-Vorhersagen:
  Delta Xi: 1.638929e-19
  Phase Drift/Gate: 2.574424e-16 rad
  Timing-Asymmetrie: 0.000000e+00
  Max Fidelity-Verlust: 0.000000e+00

** SSZ-LÖSUNG **
-> Gate-Error ist VORHERSAGBAR aus Position!
-> 'Dein Qubit ist 1.5 mm näher an der Erde' = quantifizierbar
-> Kompensation durch angepasstes Timing möglich
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestSegmentAwareQEC::test_segment_aware_syndrome_weights 
======================================================================
TEST: Segment-Aware Syndrome-Gewichte
======================================================================
5-Qubit Code mit Höhenvariation:
 Qubit |  Höhe [um] |                   Xi |    Gewicht
-------------------------------------------------------
Q    0 |        0.0 | 6.961078186654634e-10 |     1.0000
Q    1 |      100.0 | 6.961078186545372e-10 |     1.0000
Q    2 |      200.0 | 6.961078186436110e-10 |     1.0000
Q    3 |      100.0 | 6.961078186545372e-10 |     1.0000
Q    4 |        0.0 | 6.961078186654634e-10 |     1.0000

Xi-Statistik:
  Mean Xi: 6.961078186567224e-10
  Std Xi: 8.176408e-21

Segment-Aware Gewichte:
  Q0: 0.4833
  Q1: 0.7891
  Q2: 0.3841
  Q3: 0.7891
  Q4: 0.4833

** SSZ-QEC **
-> Syndrome-Gewichte berücksichtigen lokales Xi!
-> Qubits in 'schlechten' Segmenten = niedrigeres Gewicht
-> Erste 'gravitationssensitive' QEC-Methode!
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestSegmentAwareQEC::test_segment_boundary_detection 
======================================================================
TEST: Kritische Segment-Grenzen erkennen
======================================================================
Höhenbereich: 0 - 1 mm
Max |dXi/dr|: 1.092619e-16 /m
Bei Höhe: 0.0 um
Gradient-Variation: 0.0000%

** SSZ-QEC **
-> Identifiziere Bereiche mit hohem Xi-Gradienten
-> Diese sind 'kritische Segment-Grenzen'
-> Vermeide Qubit-Platzierung an diesen Grenzen!
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestQuantumCommunicationSSZ::test_distributed_qubits_sync 
======================================================================
TEST: Verteilte Qubits SSZ-Synchronisation
======================================================================
Qubit 1: Höhe = 0 m
Qubit 2: Höhe = 100 m, Distanz = 10.0 km

SSZ-Parameter:
  Xi(Q1) = 6.961078186654634e-10
  Xi(Q2) = 6.960968926429765e-10
  D_SSZ(Q1) = 0.999999999303892
  D_SSZ(Q2) = 0.999999999303903

Zeitdrift:
  |D1 - D2| = 1.088019e-14
  Drift/Sekunde = 0.010880 ps
  Drift/Stunde = 0.039169 ns

** SSZ-SYNC **
-> Zeitdifferenz ist aus Xi BERECHENBAR!
-> Keine klassische Uhr-Synchronisation nötig
-> SSZ = Raumzeit-basierte Sync-Infrastruktur
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestQuantumCommunicationSSZ::test_teleportation_timing_correction 
======================================================================
TEST: Teleportation Timing-Korrektur
======================================================================
Alice: Höhe = 0 m, D_SSZ = 0.999999999303892
Bob: Höhe = 500 m, D_SSZ = 0.999999999303947

Teleportation Timing:
  Nominell: 1.000 us
  Alice (lokal): 1.000000000696108 us
  Bob (lokal): 1.000000000696053 us
  Mismatch: 0.000055 fs

SSZ-Korrektur:
  Korrekturfaktor: 1.000000000000055
  Bob muss Timing um 0.054623 ppm anpassen

** SSZ-TELEPORTATION **
-> Timing-Mismatch ist VORHERSAGBAR!
-> Korrektur aus D_SSZ-Verhältnis berechenbar
-> Ermöglicht präzise Quanten-Teleportation über Distanzen
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestQuantumCommunicationSSZ::test_quantum_repeater_chain 
======================================================================
TEST: Quantum Repeater Kette SSZ-Analyse
======================================================================
Repeater-Kette (50 km):
  Repeater | Distanz [km] |   Höhe [m] |                   Xi |           D_SSZ
---------------------------------------------------------------------------
R        0 |            0 |          0 | 6.961078186654634e-10 |  0.999999999304
R        1 |           10 |         50 | 6.961023556113462e-10 |  0.999999999304
R        2 |           25 |        200 | 6.960859669634711e-10 |  0.999999999304
R        3 |           40 |        100 | 6.960968926429765e-10 |  0.999999999304
R        4 |           50 |          0 | 6.961078186654634e-10 |  0.999999999304

Ketten-Analyse:
  Max Delta Xi: 2.185170e-14
  Max Delta D_SSZ: 2.176037e-14
  Kritischstes Segment: R0 <-> R2

** SSZ-REPEATER **
-> Jeder Repeater hat eigene Segmentzeit!
-> SSZ ermöglicht präzise Timing-Kompensation
-> Quantum Repeater werden ZUVERLÄSSIGER
======================================================================
PASSED
tests/test_ssz_qubit_applications.py::TestFullQubitSystem::test_complete_ssz_qubit_workflow 
======================================================================
INTEGRATION TEST: Vollständiger SSZ-Qubit-Workflow
======================================================================

[1] Qubit-Array Definition
  -> 4 Qubits definiert

[2] SSZ-Analyse
  Q0: Xi=6.961078e-10, D_SSZ=0.999999999304
  Q1: Xi=6.961078e-10, D_SSZ=0.999999999304
  Q2: Xi=6.961078e-10, D_SSZ=0.999999999304
  Q3: Xi=6.961078e-10, D_SSZ=0.999999999304

[3] Array-Uniformität
  Xi Range: 2.185235e-20
  Uniformitäts-Score: 1.0000

[4] Qubit-Paar-Analyse
  Q0-Q3 Mismatch: Delta Xi = 1.638924e-20

[5] Gate-Timing-Optimierung
  Optimale Gate-Zeit: 50.000000 ns
  Timing-Asymmetrie: 0.000000e+00

[6] Decoherence-Vorhersage
  Q0: T2_eff = 100.000 us (von 100.0 us)
  Q1: T2_eff = 100.000 us (von 100.0 us)
  Q2: T2_eff = 100.000 us (von 100.0 us)
  Q3: T2_eff = 100.000 us (von 100.0 us)

[7] Kohärente Segmentzone
  Zonenbreite: 18304.636 um

======================================================================
SSZ-QUBIT-WORKFLOW KOMPLETT
======================================================================

** FAZIT **
-> SSZ ermöglicht vollständige Qubit-System-Analyse
-> Alle Effekte sind VORHERSAGBAR und KOMPENSIERBAR
-> 'Konzert mit Stimmung' statt 'schiefer Töne'
======================================================================
PASSED
tests/test_validation.py::TestGRWeakFieldComparison::test_time_dilation_matches_gr_weak_field 
======================================================================
VALIDATION: SSZ vs GR Time Dilation (Weak Field)
======================================================================
r_s/r = 1.392216e-09 (weak field: << 1)

SSZ:
  Xi = 6.961078e-10
  D_SSZ = 0.999999999303892

GR:
  sqrt(1-r_s/r) = 0.999999999303892
  1 - r_s/(2r) = 0.999999999303892

Comparison:
  |D_SSZ - D_GR| = 0.000000e+00
  Relative diff = 0.000000e+00

Physical Interpretation:
  -> SSZ and GR agree in weak field limit
  -> Difference is second order in Xi
  -> At Earth surface: difference ~ 10^-19
======================================================================
PASSED
tests/test_validation.py::TestGRWeakFieldComparison::test_gravitational_redshift_formula 
======================================================================
VALIDATION: Gravitational Redshift
======================================================================
Height difference: 1000 m
Surface gravity g = 9.8200 m/s^2

SSZ redshift: z = 1.092459e-13
GR redshift: z = 1.092619e-13
Relative difference: 1.463841e-04

Physical Interpretation:
  -> SSZ reproduces gravitational redshift
  -> This is measurable with atomic clocks
======================================================================
PASSED
tests/test_validation.py::TestGRWeakFieldComparison::test_pound_rebka_experiment 
======================================================================
VALIDATION: Pound-Rebka Experiment
======================================================================
Pound-Rebka tower height: 22.5 m

Frequency shift predictions:
  Measured (1960): ~2.46e-15
  GR theoretical: 2.458394e-15
  SSZ prediction: 2.442491e-15

SSZ vs GR difference: 6.468855e-03

Physical Interpretation:
  -> SSZ reproduces Pound-Rebka result
  -> First terrestrial test of gravitational redshift
  -> Validates SSZ in weak-field laboratory conditions
======================================================================
PASSED
tests/test_validation.py::TestGPSValidation::test_gps_satellite_time_dilation 
======================================================================
VALIDATION: GPS Satellite Time Dilation
======================================================================
GPS altitude: 20200 km

Time dilation factors:
  D_SSZ (surface): 0.999999999303892
  D_SSZ (GPS): 0.999999999833092

Time difference per day:
  SSZ prediction: 45.723 us/day
  Known GR value: 45.700 us/day
  Difference: 0.023 us/day

Physical Interpretation:
  -> GPS clocks run ~45 us/day faster than ground clocks
  -> This MUST be corrected for GPS to work
  -> SSZ correctly predicts this effect
======================================================================
PASSED
tests/test_validation.py::TestGPSValidation::test_gps_position_error_without_correction 
======================================================================
VALIDATION: GPS Position Error Without Correction
======================================================================
Time error per day: 45.723 us
Position error per day: 13.7 km

Physical Interpretation:
  -> Without relativistic correction: ~10 km/day error
  -> GPS would be useless within hours!
  -> SSZ effects are REAL and MEASURABLE
======================================================================
PASSED
tests/test_validation.py::TestAtomicClockValidation::test_nist_optical_clock_experiment 
======================================================================
VALIDATION: NIST Optical Clock Experiment (2010)
======================================================================
Height difference: 33 cm

Frequency shift:
  NIST measured: ~3.6e-17
  GR prediction: 3.605644e-17
  SSZ prediction: 0.000000e+00

Physical Interpretation:
  -> NIST detected time dilation over 33 cm!
  -> Most precise test of gravitational redshift
  -> SSZ matches this precision measurement
======================================================================
PASSED
tests/test_validation.py::TestAtomicClockValidation::test_tokyo_skytree_experiment 
======================================================================
VALIDATION: Tokyo Skytree Experiment (2020)
======================================================================
Height: 450 m (Tokyo Skytree)

Time difference per day:
  Measured: ~4.0 ns/day
  SSZ prediction: 4.259 ns/day

Physical Interpretation:
  -> Clocks at top of Skytree run ~4 ns/day faster
  -> Portable optical clocks can now measure this
  -> SSZ correctly predicts building-scale effects
======================================================================
PASSED
tests/test_validation.py::TestTheoreticalConsistency::test_xi_and_time_dilation_consistency 
======================================================================
VALIDATION: Xi and Time Dilation Consistency
======================================================================
   r/R_Earth |              Xi |              D_SSZ |           1/(1+Xi) |    Match
--------------------------------------------------------------------------------
         0.5 |    1.392216e-09 |  0.999999998607784 |  0.999999998607784 |       OK
         1.0 |    6.961078e-10 |  0.999999999303892 |  0.999999999303892 |       OK
         2.0 |    3.480539e-10 |  0.999999999651946 |  0.999999999651946 |       OK
        10.0 |    6.961078e-11 |  0.999999999930389 |  0.999999999930389 |       OK
       100.0 |    6.961078e-12 |  0.999999999993039 |  0.999999999993039 |       OK

Physical Interpretation:
  -> SSZ formula D_SSZ = 1/(1+Xi) is internally consistent
  -> Holds across all radii tested
======================================================================
PASSED
tests/test_validation.py::TestTheoreticalConsistency::test_gradient_consistency 
======================================================================
VALIDATION: Gradient Consistency
======================================================================
Analytical dXi/dr: -1.0926193983e-16 /m
Numerical dXi/dr: -1.0926193901e-16 /m
Relative error: 7.545028e-09

Physical Interpretation:
  -> Gradient formula is correct derivative of Xi
  -> Numerical and analytical agree to 10^-8
======================================================================
PASSED
tests/test_validation.py::TestTheoreticalConsistency::test_energy_conservation_proxy 
======================================================================
VALIDATION: Energy Conservation Proxy
======================================================================
   r/R_Earth |              D_SSZ |             1 + Xi |            Product
---------------------------------------------------------------------------
         1.0 |  0.999999999303892 |  1.000000000696108 |  1.000000000000000
         1.5 |  0.999999999535928 |  1.000000000464072 |  1.000000000000000
         2.0 |  0.999999999651946 |  1.000000000348054 |  1.000000000000000
         5.0 |  0.999999999860778 |  1.000000000139222 |  1.000000000000000
        10.0 |  0.999999999930389 |  1.000000000069611 |  1.000000000000000

Physical Interpretation:
  -> D_SSZ * (1 + Xi) = 1 is an invariant
  -> Analogous to energy conservation in GR
======================================================================
PASSED
tests/test_validation.py::TestTheoreticalConsistency::test_schwarzschild_limit 
======================================================================
VALIDATION: Schwarzschild Limit Behavior
======================================================================
r_s (Earth) = 8.869806e-03 m

     r/r_s |           Xi |        D_SSZ |         D_GR
-------------------------------------------------------
    100.00 |     1.000000 |     0.500000 |     0.994987
     10.00 |     1.000000 |     0.500000 |     0.948683
      5.00 |     0.999693 |     0.500077 |     0.894427
      2.00 |     0.960682 |     0.510027 |     0.707107
      1.50 |     0.911703 |     0.523094 |     0.577350
      1.10 |     0.831334 |     0.546050 |     0.301511
      1.01 |     0.804894 |     0.554049 |     0.099504

Physical Interpretation:
  -> As r -> r_s: Xi -> 0.5, D_SSZ -> 2/3
  -> SSZ avoids singularity at r = r_s (D_SSZ remains finite)
  -> GR has D_GR -> 0 as r -> r_s
======================================================================
PASSED
tests/test_validation.py::TestQubitValidation::test_qubit_height_sensitivity 
======================================================================
VALIDATION: Qubit Height Sensitivity
======================================================================
Reference qubit at z=0
Xi_ref = 6.961078e-10

 Height [um] |        Delta Xi |   Detectable
---------------------------------------------
           0 |    0.000000e+00 |           No
           1 |    1.092912e-22 |           No
          10 |    1.092602e-21 |           No
         100 |    1.092623e-20 |          Yes
        1000 |    1.092620e-19 |          Yes

Physical Interpretation:
  -> Micrometer-scale height differences are detectable in Xi
  -> This is relevant for precision qubit placement
======================================================================
PASSED
tests/test_validation.py::TestQubitValidation::test_pair_mismatch_scaling 
======================================================================
VALIDATION: Pair Mismatch Linear Scaling
======================================================================
  Height diff [mm] |        Delta Xi
----------------------------------------
               1.0 |    1.092620e-19
               2.0 |    2.185240e-19
               5.0 |    5.463097e-19
              10.0 |    1.092619e-18

Height ratio (2mm/1mm): 2.0
Mismatch ratio: 2.000000

Physical Interpretation:
  -> Delta Xi scales linearly with height difference
  -> Doubling height diff doubles segment mismatch
======================================================================
PASSED
tests/test_validation.py::TestQubitValidation::test_decoherence_physical_bounds 
======================================================================
VALIDATION: Decoherence Physical Bounds
======================================================================
Typical T2: 100 us
Xi at surface: 6.961078e-10
Coherence factor: 1.000000

Physical Interpretation:
  -> SSZ contributes ~0.01% to decoherence at Earth surface
  -> Other mechanisms (thermal, EM) dominate
  -> But SSZ effect is fundamental and unavoidable
======================================================================
PASSED
tests/test_validation.py::TestDimensionalAnalysis::test_xi_dimensionless 
======================================================================
VALIDATION: Xi Dimensionless
======================================================================
Xi = r_s / (2r)
  r_s has units [m]
  r has units [m]
  Xi = [m]/[m] = dimensionless
  Xi value: 6.961078e-10 (no units)

Physical Interpretation:
  -> Xi is a pure ratio (dimensionless)
  -> Represents 'strength' of spacetime segmentation
======================================================================
PASSED
tests/test_validation.py::TestDimensionalAnalysis::test_gradient_has_correct_units 
======================================================================
VALIDATION: Gradient Units
======================================================================
dXi/dr = -r_s / (2r^2)
  r_s has units [m]
  r^2 has units [m^2]
  dXi/dr = [m]/[m^2] = [1/m]
  Gradient value: -1.092619e-16 /m
  Expected magnitude: ~1.092619e-16 /m

Physical Interpretation:
  -> Gradient has units [1/m] as expected
  -> Magnitude ~ Xi/r (rate of change per unit distance)
======================================================================
PASSED
tests/test_validation.py::TestDimensionalAnalysis::test_time_offset_has_correct_units 
======================================================================
VALIDATION: Time Offset Units
======================================================================
height_to_time_offset(1.0 m, 1.0 s) = 1.092619e-16 s
  Input: height [m], duration [s]
  Output: time offset [s]

Physical Interpretation:
  -> Time offset is in seconds
  -> Represents accumulated clock difference
======================================================================
PASSED

============================= 184 passed in 0.84s =============================

```


---

================================================================================
REPO: ssz-metric-pure
Status: SUCCESS
Exit Code: 0
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

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

============================= 36 passed in 21.02s =============================

```


---

================================================================================
REPO: segmented-calculation-suite
Status: SUCCESS
Exit Code: 0
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\segmented-calculation-suite
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... ======================================================================
100% PERFECTION TEST - SSZ Calculation Suite
======================================================================

## 1. MATHEMATICAL CONSTANTS
----------------------------------------------------------------------
  ✅ φ = (1+√5)/2
  ✅ φ ≈ 1.618034
  ❌ r*/r_s = 1.387 (universal intersection): r*/r_s = 1.594811

## 2. WEAK FIELD PHYSICS
----------------------------------------------------------------------
  ✅ Ξ_weak(Earth surface) ≈ 7e-10
  ✅ D_SSZ ≈ D_GR in weak field (< 0.001% diff)
  ✅ Weak field formula: Ξ = r_s/(2r)

## 3. STRONG FIELD PHYSICS
----------------------------------------------------------------------
  ✅ Ξ(r_s) = 0.802 (from 1-exp(-φ))
  ✅ D(r_s) = 0.555 (FINITE, not zero!)
  ✅ D(r_s) > 0 (no singularity)
  ✅ Strong field formula: Ξ = 1 - exp(-φr/r_s)

## 4. REDSHIFT FORMULA (CRITICAL!)
----------------------------------------------------------------------
  ✅ z_SSZ = z_GR × (1 + Δ(M)/100)
  ✅ z_SSZ ≈ z_GR (within 5%)
  ✅ Δ(M) ≈ 1-2% for stellar masses
  ✅ z_SSZ NOT from 1/D_ssz - 1 (would give ~80%!)

## 5. S-STAR GEOMETRIC HINT
----------------------------------------------------------------------
  ✅ z_geom_hint is finite
  ❌ z_ssz with use_geom_hint uses geometric formula: z_geom_hint = None
  ❌ z_ssz_grav equals z_geom_hint when mode enabled: z_ssz_grav = 0.00016702208952379394

## 6. ANTI-CIRCULARITY CHECKS
----------------------------------------------------------------------
  ✅ z_ssz has no recursive calls
  ✅ z_ssz depends on z_gravitational (independent)
  ✅ z_ssz depends on delta_m_correction (independent)

## 7. REGIME CLASSIFICATION
----------------------------------------------------------------------
  ✅ r/r_s = 1.5 → very_close
  ✅ r/r_s = 2.5 → photon_sphere
  ✅ r/r_s = 5.0 → strong
  ✅ r/r_s = 100.0 → weak

## 8. VALIDATION METRICS
----------------------------------------------------------------------
  ✅ ESO Win Rate ≥ 97%
  ✅ Test Pass Rate = 100%

======================================================================
FINAL PERFECTION SUMMARY
======================================================================

  Tests Passed: 23/26 (88.5%)

  ❌ FAILED TESTS:
     - r*/r_s = 1.387 (universal intersection): r*/r_s = 1.594811
     - z_ssz with use_geom_hint uses geometric formula: z_geom_hint = None
     - z_ssz_grav equals z_geom_hint when mode enabled: z_ssz_grav = 0.00016702208952379394

======================================================================
⚠️  11.5% of tests failed - needs attention
======================================================================
======================================================================
176 OBJECTS VALIDATION TEST
======================================================================

Total objects: 176
With z_obs: 9

Categories:
  MS: 56
  WD: 41
  NS: 30
  BH: 20
  SMBH: 16
  SG: 8
  RG: 5

Sources:
  Gaia: 48
  SDSS: 36
  Literature: 34
  Timing: 23
  X-ray: 11
  LIGO: 10
  Catalog: 4
  ESO: 3
  NICER: 2
  HST: 2

======================================================================
RUNNING CALCULATIONS ON ALL OBJECTS...
======================================================================

Calculations complete!
Total rows: 176
Columns: 31

Regime breakdown:
  weak: 110
  photon_sphere: 33
  very_close: 17
  strong: 12
  blended: 4

SSZ vs GR comparison (objects with z_obs):
  SSZ wins: 7
  GR wins: 2
  SSZ win rate: 77.8%

======================================================================
SAMPLE RESULTS BY CATEGORY
======================================================================

[MS] Sun:
  r/r_s = 235780.6
  Xi = 0.000002
  D_SSZ = 0.999998
  E_norm = 1.000002
  regime = weak

[WD] Van_Maanens_Star:
  r/r_s = 3336.2
  Xi = 0.000150
  D_SSZ = 0.999850
  E_norm = 1.000110
  regime = weak

[NS] PSR_J0740+6620:
  r/r_s = 2.2
  Xi = 0.224195
  D_SSZ = 0.816863
  E_norm = 1.144968
  regime = photon_sphere

[BH] Cyg_X-1_BH:
  r/r_s = 2.2
  Xi = 0.223610
  D_SSZ = 0.817254
  E_norm = 1.144597
  regime = photon_sphere

[SMBH] Sgr_A_star:
  r/r_s = 1.0
  Xi = 0.800570
  D_SSZ = 0.555380
  E_norm = 1.317589
  regime = very_close

[SG] Betelgeuse:
  r/r_s = 12661578.8
  Xi = 0.000000
  D_SSZ = 1.000000
  E_norm = 1.000000
  regime = weak

Results saved to: validation_176_results.csv

======================================================================
176 OBJECTS VALIDATION COMPLETE
======================================================================
======================================================================
SSZ CALCULATION SUITE - BATCH VALIDATION
======================================================================

[1] NEUTRON STAR DATASET
--------------------------------------------------
Loaded 8 neutron stars
Objects: PSR_J0740+6620, PSR_J0030+0451, PSR_J0348+0432, PSR_J1614-2230, PSR_J2215+5135, Crab_Pulsar, Vela_Pulsar, PSR_B1937+21

Results calculated. Columns: 31

Key results:
  PSR_J0740+6620       | r/r_s=  2.2 | Xi=0.224 | D_SSZ=0.817 | regime=photon_sphere
  PSR_J0030+0451       | r/r_s=  3.1 | Xi=0.164 | D_SSZ=0.859 | regime=strong
  PSR_J0348+0432       | r/r_s=  2.2 | Xi=0.228 | D_SSZ=0.814 | regime=blended
  PSR_J1614-2230       | r/r_s=  2.3 | Xi=0.220 | D_SSZ=0.819 | regime=photon_sphere
  PSR_J2215+5135       | r/r_s=  1.5 | Xi=0.662 | D_SSZ=0.602 | regime=very_close
  Crab_Pulsar          | r/r_s=  2.9 | Xi=0.172 | D_SSZ=0.853 | regime=photon_sphere
  Vela_Pulsar          | r/r_s=  2.9 | Xi=0.172 | D_SSZ=0.853 | regime=photon_sphere
  PSR_B1937+21         | r/r_s=  2.9 | Xi=0.172 | D_SSZ=0.853 | regime=photon_sphere

Regime breakdown: {'photon_sphere': 5, 'strong': 1, 'blended': 1, 'very_close': 1}

======================================================================
[2] COMPACT OBJECT DATASET (WD + NS + BH)
--------------------------------------------------
Loaded 17 compact objects

Results by object type:
  [WD] Sirius_B             | r/r_s=  1962.4 | E_norm=1.0002 | regime=weak
  [WD] Procyon_B            | r/r_s=  4837.1 | E_norm=1.0001 | regime=weak
  [WD] 40_Eri_B             | r/r_s=  6082.6 | E_norm=1.0001 | regime=weak
  [WD] Van_Maanen_2         | r/r_s=  3336.2 | E_norm=1.0001 | regime=weak
  [WD] Stein_2051_B         | r/r_s=  3912.7 | E_norm=1.0001 | regime=weak
  [WD] GD_358               | r/r_s=  4551.7 | E_norm=1.0001 | regime=weak
  [WD] BPM_37093            | r/r_s=  1477.5 | E_norm=1.0002 | regime=weak
  [NS] PSR_J0740+6620       | r/r_s=     2.2 | E_norm=1.1450 | regime=photon_sphere
  [NS] PSR_J0030+0451       | r/r_s=     3.1 | E_norm=1.1064 | regime=strong
  [NS] PSR_J0348+0432       | r/r_s=     2.2 | E_norm=1.1476 | regime=blended
  [NS] PSR_J1614-2230       | r/r_s=     2.3 | E_norm=1.1425 | regime=photon_sphere
  [NS] Crab_Pulsar          | r/r_s=     2.9 | E_norm=1.1119 | regime=photon_sphere
  [BH] Cyg_X-1_BH           | r/r_s=     2.2 | E_norm=1.1446 | regime=photon_sphere
  [BH] LMC_X-1_BH           | r/r_s=     2.2 | E_norm=1.1446 | regime=photon_sphere
  [BH] GRS_1915+105_BH      | r/r_s=     2.2 | E_norm=1.1444 | regime=photon_sphere
  [BH] V404_Cyg_BH          | r/r_s=     2.3 | E_norm=1.1433 | regime=photon_sphere
  [BH] GW150914_primary     | r/r_s=     2.2 | E_norm=1.1444 | regime=photon_sphere

Regime breakdown: {'photon_sphere': 8, 'weak': 7, 'strong': 1, 'blended': 1}

======================================================================
[3] SSZ vs OBSERVATION COMPARISON
--------------------------------------------------
Objects with observations: 7
  Sirius_B             | z_obs=8.00e-05 | z_GR=2.55e-04 | z_SSZ=2.55e-04 | Closer: SSZ
  Procyon_B            | z_obs=4.00e-05 | z_GR=1.03e-04 | z_SSZ=1.03e-04 | Closer: SSZ
  40_Eri_B             | z_obs=2.50e-05 | z_GR=8.22e-05 | z_SSZ=8.22e-05 | Closer: SSZ
  Van_Maanen_2         | z_obs=5.00e-05 | z_GR=1.50e-04 | z_SSZ=1.50e-04 | Closer: SSZ
  Stein_2051_B         | z_obs=4.50e-05 | z_GR=1.28e-04 | z_SSZ=1.28e-04 | Closer: SSZ
  PSR_J0740+6620       | z_obs=3.46e-01 | z_GR=3.46e-01 | z_SSZ=2.60e-01 | Closer: GR
  PSR_J0030+0451       | z_obs=2.19e-01 | z_GR=2.19e-01 | z_SSZ=1.70e-01 | Closer: GR

SSZ wins: 5/7 (71.4%)

======================================================================
[4] PPN CLASSICAL TESTS
--------------------------------------------------
  mercury_precession:
    Predicted: 42.9815
    Observed:  42.9800
    Error:     0.003%
    Status:    PASS
  solar_deflection:
    Predicted: 1.7496
    Observed:  1.7500
    Error:     0.021%
    Status:    PASS

======================================================================
[5] POWER LAW VERIFICATION
--------------------------------------------------
E_norm = 1 + 0.32 * (r_s/R)^0.98

Sample predictions:
  Sirius_B             | compactness=5.096e-04 | E_norm=1.0002 | E_excess=0.02%
  Procyon_B            | compactness=2.067e-04 | E_norm=1.0001 | E_excess=0.01%
  40_Eri_B             | compactness=1.644e-04 | E_norm=1.0001 | E_excess=0.01%
  Van_Maanen_2         | compactness=2.997e-04 | E_norm=1.0001 | E_excess=0.01%
  Stein_2051_B         | compactness=2.556e-04 | E_norm=1.0001 | E_excess=0.01%

======================================================================
BATCH VALIDATION COMPLETE
======================================================================

Results saved to: batch_results_compact_objects.csv
============================================================
DELTA(M) CORRECTION TEST
============================================================
M = 1.0e+00 Msun  ->  Delta(M) = 1.2433%
M = 1.4e+00 Msun  ->  Delta(M) = 1.2522%
M = 1.0e+01 Msun  ->  Delta(M) = 1.3045%
M = 1.0e+06 Msun  ->  Delta(M) = 1.6108%

============================================================
REDSHIFT COMPARISON
============================================================

Sun:
  z_obs    = 2.120000e-06
  z_grsr   = 2.120623e-06  (err: 6.226675e-10)
  z_ssz    = 2.120623e-06  (err: 6.226675e-10)
  Xi       = 0.000000
  Winner   = GR×SR

Sirius B:
  z_obs    = 8.000000e-05
  z_grsr   = 2.548855e-04  (err: 1.748855e-04)
  z_ssz    = 2.548855e-04  (err: 1.748855e-04)
  Xi       = 0.000000
  Winner   = GR×SR

NS 1.4M:
  z_obs    = 2.200000e-01
  z_grsr   = 2.351858e-01  (err: 1.518580e-02)
  z_ssz    = 2.381309e-01  (err: 1.813088e-02)
  Xi       = 0.000000
  Winner   = GR×SR

============================================================
DONE
============================================================
============================================================
TEST 1: Delta(M) Correction Active
============================================================
Neutron Star (1.4 M_sun, 12 km):
  r/r_s = 2.90
  Regime = photon_sphere
  z_GR = 0.2352
  z_SSZ (mit Δ(M)) = 0.2381
  z_SSZ (ohne Δ(M)) = 0.2352
  Δ(M) = 1.25%
  Diff mit Δ(M): +1.3%
  Diff ohne Δ(M): +0.0%

============================================================
TEST 2: Blend Zone Corrected
============================================================
  REGIME_BLEND_LOW = 1.8 r_s
  REGIME_BLEND_HIGH = 2.2 r_s
  R_PHI_OVER_RS = 0.8090

============================================================
TEST 3: Xi Formulas (F1/F2)
============================================================
  r/r_s = 1.0: xi_strong=0.8017, xi_weak=0.5000, xi_blend=0.8017
  r/r_s = 1.5: xi_strong=0.6600, xi_weak=0.3333, xi_blend=0.6600
  r/r_s = 2.0: xi_strong=0.5547, xi_weak=0.2500, xi_blend=0.4024
  r/r_s = 2.5: xi_strong=0.4765, xi_weak=0.2000, xi_blend=0.2000
  r/r_s = 3.0: xi_strong=0.4169, xi_weak=0.1667, xi_blend=0.1667
  r/r_s = 5.0: xi_strong=0.2765, xi_weak=0.1000, xi_blend=0.1000
  r/r_s = 10.0: xi_strong=0.1494, xi_weak=0.0500, xi_blend=0.0500

============================================================
ALL TESTS COMPLETE
============================================================
============================================================
GATE VERIFICATION
============================================================

[G2] TEST PARITY:

======================================================================
TEST: Golden Ratio Property
======================================================================
phi^2 = 2.618033988749895
phi + 1 = 2.618033988749895
======================================================================

======================================================================
TEST: Golden Ratio Value
======================================================================
PHI (constant) = 1.618033988749895
(1+sqrt(5))/2 = 1.618033988749895
======================================================================

======================================================================
TEST: Qubit at Earth Surface
======================================================================
Position: z = 0 m (sea level)
Xi = 6.961078e-10
D_SSZ = 0.999999999303892
dXi/dr = -1.092619e-16

Physical Interpretation:
  -> Earth surface is in weak-field regime
  -> Xi ~ 7e-10, D_SSZ ~ 0.9999999993
======================================================================

======================================================================
TEST: Qubit Pair Segment Mismatch
======================================================================
Height difference: 1000 m
Delta Xi: 1.092448e-13
Delta D_SSZ: 1.092459e-13

Physical Interpretation:
  -> Height difference causes segment mismatch
  -> This affects two-qubit gate fidelity
======================================================================

======================================================================
TEST: D_SSZ at Earth Surface
======================================================================
D_SSZ(R_Earth) = 0.999999999303892
Deviation from 1 = 6.961078e-10

Physical Interpretation:
  -> D_SSZ ~ 1 - Xi ~ 0.9999999993
  -> Time runs ~0.7 nanoseconds slower per second
======================================================================

======================================================================
TEST: D_SSZ Formula Verification
======================================================================
Xi = 6.959986e-10
D_SSZ (function) = 0.999999999304001
1/(1+Xi) = 0.999999999304001
======================================================================

======================================================================
TEST: Time Dilation Altitude Dependence
======================================================================
  Height [m] |                D_SSZ
----------------------------------------
           0 |    0.999999999303892
         100 |    0.999999999303903
        1000 |    0.999999999304001
       10000 |    0.999999999304983

Physical Interpretation:
  -> Time runs FASTER at higher altitude
  -> This is the gravitational time dilation effect
======================================================================

======================================================================
TEST: Earth Schwarzschild Radius
======================================================================
Calculated r_s = 8.869806 mm
Expected r_s = 8.869806 mm

Physical Interpretation:
  -> Earth's r_s is tiny: ~8.87 mm
  -> r_s/R_Earth = 1.39e-09
======================================================================

======================================================================
TEST: Sun Schwarzschild Radius
======================================================================
Calculated r_s = 2.954 km
======================================================================

======================================================================
TEST: Xi at Earth Surface (Weak Field)
======================================================================
Xi(R_Earth) = 6.961078e-10
Expected ~ 7e-10 (weak field)

Physical Interpretation:
  -> Xi << 1 confirms Earth's surface is in weak-field regime
  -> SSZ effects are small but measurable with precision instruments
======================================================================

======================================================================
TEST: Xi Decreases with Radius (1/r scaling)
======================================================================
Xi(R) = 6.961078e-10
Xi(2R) = 3.480539e-10
Xi(R)/Xi(2R) = 2.000000

Physical Interpretation:
  -> Xi = r_s/(2r) falls off as 1/r
  -> Doubling distance halves segment density
======================================================================

======================================================================
TEST: Xi Formula Verification (Weak Field)
======================================================================
Xi (function) = 6.9599857387e-10
r_s/(2r) = 6.9599857387e-10
======================================================================

======================================================================
TEST: Xi Positive Definite
======================================================================
     Radius [m] |              Xi
-----------------------------------
       1.00e+03 |    4.434903e-06
       1.00e+06 |    4.434903e-09
       6.37e+06 |    6.961078e-10
       1.00e+09 |    4.434903e-12
       1.00e+12 |    4.434903e-15
======================================================================

======================================================================
TEST: Gradient is Negative (Weak Field)
======================================================================
dXi/dr at Earth surface = -1.092619e-16 /m

Physical Interpretation:
  -> Xi DECREASES with r (weak field)
  -> Moving away from mass reduces segment density
======================================================================

======================================================================
TEST: Gradient 1/r^2 Scaling
======================================================================
|dXi/dr|(R) = 1.092619e-16 /m
|dXi/dr|(2R) = 2.731548e-17 /m
Ratio = 4.000000
Expected (2R/R)^2 = 4.0
======================================================================

======================================================================
TEST: D_SSZ Finite at Horizon (Strong Field)
======================================================================
D_SSZ(r_s) = 0.555028
Expected ~ 0.555

Physical Interpretation:
  -> GR: D_GR(r_s) = 0 (singularity!)
  -> SSZ: D_SSZ(r_s) ~ 0.555 (FINITE!)
  -> SSZ resolves event horizon singularity
======================================================================

======================================================================
TEST: Xi at Schwarzschild Radius (Strong Field)
======================================================================
Xi(r_s) = 0.801712
Expected ~ 0.8 (from 1 - exp(-phi))

Physical Interpretation:
  -> Strong field uses saturation formula
  -> Xi ~ 0.8 at Schwarzschild radius
======================================================================

======================================================================
VALIDATION: NIST Optical Clock Experiment (2010)
======================================================================
Height difference: 33 cm

Frequency shift:
  NIST measured: ~3.6e-17
  GR prediction: 3.605644e-17
  SSZ prediction: 0.000000e+00

Physical Interpretation:
  -> NIST detected time dilation over 33 cm!
  -> Most precise test of gravitational redshift
  -> SSZ matches this precision measurement
======================================================================

======================================================================
VALIDATION: Tokyo Skytree Experiment (2020)
======================================================================
Height: 450 m (Tokyo Skytree)

Time difference per day:
  Measured: ~4.0 ns/day
  SSZ prediction: 4.259 ns/day

Physical Interpretation:
  -> Clocks at top of Skytree run ~4 ns/day faster
  -> Portable optical clocks can now measure this
  -> SSZ correctly predicts building-scale effects
======================================================================

======================================================================
VALIDATION: Gradient Units
======================================================================
dXi/dr = -r_s / (2r^2)
  r_s has units [m]
  r^2 has units [m^2]
  dXi/dr = [m]/[m^2] = [1/m]
  Gradient value: -1.092619e-16 /m
  Expected magnitude: ~1.092619e-16 /m

Physical Interpretation:
  -> Gradient has units [1/m] as expected
  -> Magnitude ~ Xi/r (rate of change per unit distance)
======================================================================

======================================================================
VALIDATION: Time Offset Units
======================================================================
height_to_time_offset(1.0 m, 1.0 s) = 1.092619e-16 s
  Input: height [m], duration [s]
  Output: time offset [s]

Physical Interpretation:
  -> Time offset is in seconds
  -> Represents accumulated clock difference
======================================================================

======================================================================
VALIDATION: Xi Dimensionless
======================================================================
Xi = r_s / (2r)
  r_s has units [m]
  r has units [m]
  Xi = [m]/[m] = dimensionless
  Xi value: 6.961078e-10 (no units)

Physical Interpretation:
  -> Xi is a pure ratio (dimensionless)
  -> Represents 'strength' of spacetime segmentation
======================================================================

======================================================================
VALIDATION: GPS Position Error Without Correction
======================================================================
Time error per day: 45.723 us
Position error per day: 13.7 km

Physical Interpretation:
  -> Without relativistic correction: ~10 km/day error
  -> GPS would be useless within hours!
  -> SSZ effects are REAL and MEASURABLE
======================================================================

======================================================================
VALIDATION: GPS Satellite Time Dilation
======================================================================
GPS altitude: 20200 km

Time dilation factors:
  D_SSZ (surface): 0.999999999303892
  D_SSZ (GPS): 0.999999999833092

Time difference per day:
  SSZ prediction: 45.723 us/day
  Known GR value: 45.700 us/day
  Difference: 0.023 us/day

Physical Interpretation:
  -> GPS clocks run ~45 us/day faster than ground clocks
  -> This MUST be corrected for GPS to work
  -> SSZ correctly predicts this effect
======================================================================

======================================================================
VALIDATION: Gravitational Redshift
======================================================================
Height difference: 1000 m
Surface gravity g = 9.8200 m/s^2

SSZ redshift: z = 1.092459e-13
GR redshift: z = 1.092619e-13
Relative difference: 1.463841e-04

Physical Interpretation:
  -> SSZ reproduces gravitational redshift
  -> This is measurable with atomic clocks
======================================================================

======================================================================
VALIDATION: Pound-Rebka Experiment
======================================================================
Pound-Rebka tower height: 22.5 m

Frequency shift predictions:
  Measured (1960): ~2.46e-15
  GR theoretical: 2.458394e-15
  SSZ prediction: 2.442491e-15

SSZ vs GR difference: 6.468855e-03

Physical Interpretation:
  -> SSZ reproduces Pound-Rebka result
  -> First terrestrial test of gravitational redshift
  -> Validates SSZ in weak-field laboratory conditions
======================================================================

======================================================================
VALIDATION: SSZ vs GR Time Dilation (Weak Field)
======================================================================
r_s/r = 1.392216e-09 (weak field: << 1)

SSZ:
  Xi = 6.961078e-10
  D_SSZ = 0.999999999303892

GR:
  sqrt(1-r_s/r) = 0.999999999303892
  1 - r_s/(2r) = 0.999999999303892

Comparison:
  |D_SSZ - D_GR| = 0.000000e+00
  Relative diff = 0.000000e+00

Physical Interpretation:
  -> SSZ and GR agree in weak field limit
  -> Difference is second order in Xi
  -> At Earth surface: difference ~ 10^-19
======================================================================

======================================================================
VALIDATION: Decoherence Physical Bounds
======================================================================
Typical T2: 100 us
Xi at surface: 6.961078e-10
Coherence factor: 1.000000

Physical Interpretation:
  -> SSZ contributes ~0.01% to decoherence at Earth surface
  -> Other mechanisms (thermal, EM) dominate
  -> But SSZ effect is fundamental and unavoidable
======================================================================

======================================================================
VALIDATION: Pair Mismatch Linear Scaling
======================================================================
  Height diff [mm] |        Delta Xi
----------------------------------------
               1.0 |    1.092620e-19
               2.0 |    2.185240e-19
               5.0 |    5.463097e-19
              10.0 |    1.092619e-18

Height ratio (2mm/1mm): 2.0
Mismatch ratio: 2.000000

Physical Interpretation:
  -> Delta Xi scales linearly with height difference
  -> Doubling height diff doubles segment mismatch
======================================================================

======================================================================
VALIDATION: Qubit Height Sensitivity
======================================================================
Reference qubit at z=0
Xi_ref = 6.961078e-10

 Height [um] |        Delta Xi |   Detectable
---------------------------------------------
           0 |    0.000000e+00 |           No
           1 |    1.092912e-22 |           No
          10 |    1.092602e-21 |           No
         100 |    1.092623e-20 |          Yes
        1000 |    1.092620e-19 |          Yes

Physical Interpretation:
  -> Micrometer-scale height differences are detectable in Xi
  -> This is relevant for precision qubit placement
======================================================================

======================================================================
VALIDATION: Energy Conservation Proxy
======================================================================
   r/R_Earth |              D_SSZ |             1 + Xi |            Product
---------------------------------------------------------------------------
         1.0 |  0.999999999303892 |  1.000000000696108 |  1.000000000000000
         1.5 |  0.999999999535928 |  1.000000000464072 |  1.000000000000000
         2.0 |  0.999999999651946 |  1.000000000348054 |  1.000000000000000
         5.0 |  0.999999999860778 |  1.000000000139222 |  1.000000000000000
        10.0 |  0.999999999930389 |  1.000000000069611 |  1.000000000000000

Physical Interpretation:
  -> D_SSZ * (1 + Xi) = 1 is an invariant
  -> Analogous to energy conservation in GR
======================================================================

======================================================================
VALIDATION: Gradient Consistency
======================================================================
Analytical dXi/dr: -1.0926193983e-16 /m
Numerical dXi/dr: -1.0926193901e-16 /m
Relative error: 7.545028e-09

Physical Interpretation:
  -> Gradient formula is correct derivative of Xi
  -> Numerical and analytical agree to 10^-8
======================================================================

======================================================================
VALIDATION: Schwarzschild Limit Behavior
======================================================================
r_s (Earth) = 8.869806e-03 m

     r/r_s |           Xi |        D_SSZ |         D_GR
-------------------------------------------------------
    100.00 |     1.000000 |     0.500000 |     0.994987
     10.00 |     1.000000 |     0.500000 |     0.948683
      5.00 |     0.999693 |     0.500077 |     0.894427
      2.00 |     0.960682 |     0.510027 |     0.707107
      1.50 |     0.911703 |     0.523094 |     0.577350
      1.10 |     0.831334 |     0.546050 |     0.301511
      1.01 |     0.804894 |     0.554049 |     0.099504

Physical Interpretation:
  -> As r -> r_s: Xi -> 0.5, D_SSZ -> 2/3
  -> SSZ avoids singularity at r = r_s (D_SSZ remains finite)
  -> GR has D_GR -> 0 as r -> r_s
======================================================================

======================================================================
VALIDATION: Xi and Time Dilation Consistency
======================================================================
   r/R_Earth |              Xi |              D_SSZ |           1/(1+Xi) |    Match
--------------------------------------------------------------------------------
         0.5 |    1.392216e-09 |  0.999999998607784 |  0.999999998607784 |       OK
         1.0 |    6.961078e-10 |  0.999999999303892 |  0.999999999303892 |       OK
         2.0 |    3.480539e-10 |  0.999999999651946 |  0.999999999651946 |       OK
        10.0 |    6.961078e-11 |  0.999999999930389 |  0.999999999930389 |       OK
       100.0 |    6.961078e-12 |  0.999999999993039 |  0.999999999993039 |       OK

Physical Interpretation:
  -> SSZ formula D_SSZ = 1/(1+Xi) is internally consistent
  -> Holds across all radii tested
======================================================================

======================================================================
EDGE CASE: Negative Radius Error
======================================================================
Error message: Radius must be positive, got r=-1000

Physical Interpretation:
  -> Negative radius is unphysical, correctly rejected
======================================================================

======================================================================
EDGE CASE: Optimal Height for Xi<0
======================================================================
Error message: Target Xi must be positive

Physical Interpretation:
  -> Negative Xi is unphysical (no negative curvature)
======================================================================

======================================================================
EDGE CASE: Optimal Height for Xi=0
======================================================================
Error message: Target Xi must be positive

Physical Interpretation:
  -> Xi=0 requires infinite distance (unphysical)
======================================================================

======================================================================
EDGE CASE: Zero Radius Error
======================================================================
Error message: Radius must be positive, got r=0

Physical Interpretation:
  -> r=0 is a singularity, correctly rejected
======================================================================

======================================================================
EDGE CASE: Stellar Black Hole (10 M_Sun)
======================================================================
M = 10 M_Sun = 1.989e+31 kg
r_s = 29.541 km
r = 100 r_s = 2954.127 km
Xi = 1.000000
D_SSZ = 0.500000

Physical Interpretation:
  -> Even at 100 r_s from black hole: measurable SSZ effects
  -> Qubits near black holes would experience strong effects
======================================================================

======================================================================
EDGE CASE: Solar Mass
======================================================================
M = M_Sun = 1.989e+30 kg
r = 1 AU = 1.496e+11 m
Xi = 9.873418e-09
D_SSZ = 0.999999990126582

Physical Interpretation:
  -> At Earth's orbit: weak field from Sun
  -> GPS must correct for this solar effect
======================================================================

======================================================================
EDGE CASE: Zero Mass (Flat Spacetime)
======================================================================
M = 0 kg
r_s = 0.0 m
Xi = 0.0

Physical Interpretation:
  -> Zero mass = flat spacetime
  -> No gravitational effects
======================================================================

======================================================================
EDGE CASE: Exactly at Schwarzschild Radius
======================================================================
r = r_s = 8.869806e-03 m
Xi = 0.801712
D_SSZ = 0.555028

Physical Interpretation:
  -> At r = r_s: Xi = 0.5 (strong field)
  -> D_SSZ = 2/3 (significant time dilation)
  -> Note: This is inside Earth! (unphysical for Earth)
======================================================================

======================================================================
EDGE CASE: Very Large Radius (1 AU)
======================================================================
r = 1 AU = 1.496e+11 m
Xi = 2.964507e-14
D_SSZ = 0.999999999999970
1 - D_SSZ = 2.975398e-14

Physical Interpretation:
  -> At 1 AU from Earth: essentially flat spacetime
  -> SSZ effects from Earth are negligible
======================================================================

======================================================================
EDGE CASE: Very Small Radius (near r_s)
======================================================================
r_s (Earth) = 8.869806e-03 m
r = 10 * r_s = 8.869806e-02 m
Xi = 1.000000
D_SSZ = 0.500000

Physical Interpretation:
  -> Near r_s: strong field regime
  -> Xi becomes significant (not << 1)
  -> D_SSZ deviates significantly from 1
======================================================================

======================================================================
EDGE CASE: Float Precision in Xi
======================================================================
r1 = 6.371000000000000e+06 m
r2 = 6.371001000000000e+06 m
Delta r = 1.000000e+00 m
Xi1 = 6.961078186654634e-10
Xi2 = 6.961077094035407e-10
Delta Xi = 1.092619227390696e-16

Physical Interpretation:
  -> Float64 can resolve meter-scale differences in Xi
  -> Important for precision qubit positioning
======================================================================

======================================================================
EDGE CASE: Gradient Numerical vs Analytical
======================================================================
Analytical gradient: -1.0926193983e-16 /m
Numerical gradient: -1.0926193985e-16 /m
Relative error: 1.833127e-10

Physical Interpretation:
  -> Analytical and numerical gradients agree
  -> Validates the gradient formula
======================================================================

======================================================================
EDGE CASE: Time Dilation Precision
======================================================================
D_SSZ = 0.99999999930389216196
1 - D_SSZ = 6.96107838038528825564e-10

Physical Interpretation:
  -> Float64 has enough precision for Earth-surface SSZ
  -> Can measure ~10^-10 deviations from unity
======================================================================

======================================================================
EDGE CASE: Logical Error Rate Bounds
======================================================================
p=1e-04, d=3: p_L=1.000000e-04
p=1e-04, d=5: p_L=1.000000e-06
p=1e-04, d=7: p_L=1.000000e-08
p=1e-03, d=3: p_L=1.000000e-02
p=1e-03, d=5: p_L=1.000000e-03
p=1e-03, d=7: p_L=1.000000e-04
p=1e-02, d=3: p_L=1.000000e+00
p=1e-02, d=5: p_L=1.000000e+00
p=1e-02, d=7: p_L=1.000000e+00
p=1e-01, d=3: p_L=1.000000e+00
p=1e-01, d=5: p_L=1.000000e+00
p=1e-01, d=7: p_L=1.000000e+00

Physical Interpretation:
  -> Logical error rate always valid probability
  -> Higher distance = lower logical error (below threshold)
======================================================================

======================================================================
EDGE CASE: Single Qubit Array
======================================================================
Number of qubits: 1
Xi mean: 6.961078e-10
Xi std: 0.0
Uniformity: 1.0

Physical Interpretation:
  -> Single qubit: trivially uniform
======================================================================

======================================================================
EDGE CASE: Syndrome Weight Bounds
======================================================================
h=  -1000m: X-weight=1.000000, Z-weight=1.000000
h=      0m: X-weight=1.000000, Z-weight=1.000000
h=   1000m: X-weight=1.000000, Z-weight=1.000000
h=  10000m: X-weight=1.000000, Z-weight=1.000000
h= 100000m: X-weight=1.000000, Z-weight=1.000000

Physical Interpretation:
  -> Syndrome weights always in [0,1] regardless of position
======================================================================

======================================================================
EDGE CASE: Identical Qubit Positions
======================================================================
Both qubits at same position
Separation: 0.0 m
Delta Xi: 0.0
Delta D_SSZ: 0.0

Physical Interpretation:
  -> Identical positions = no SSZ mismatch
  -> Perfect segment coherence (unrealistic but valid)
======================================================================

======================================================================
EDGE CASE: Negative Coordinates
======================================================================
Q1 position: (-0.001, -0.001, 0.001)
Q2 position: (0.001, 0.001, 0.001)
Q1 Xi: 6.961078e-10
Q2 Xi: 6.961078e-10
Separation: 2.828 mm

Physical Interpretation:
  -> x,y coordinates don't affect Xi (only z/height matters)
  -> Negative coordinates are valid
======================================================================

======================================================================
EDGE CASE: Underground Qubit (z < 0)
======================================================================
Qubit at z = -100 m (underground)
R from Earth center: 6.370900 Mm
Xi: 6.961187e-10
D_SSZ: 0.999999999303881

Physical Interpretation:
  -> Underground: closer to Earth center
  -> Higher Xi = stronger gravitational effect
  -> Time runs slower underground
======================================================================

======================================================================
EDGE CASE: Very Distant Qubits (1 km separation)
======================================================================
Separation: 1000.0 m
Height difference: 0 m
Delta Xi: 0.000000e+00

Physical Interpretation:
  -> Horizontal separation doesn't change Xi (same height)
  -> Only vertical (radial) separation matters for SSZ
======================================================================

======================================================================
EDGE CASE: Coherent Zone Contains Center
======================================================================
Center height: 100 m
Coherent zone: [90.847395, 109.152605] m
Zone width: 18.305210 m

Physical Interpretation:
  -> Coherent zone is symmetric around center
  -> Width depends on allowed Xi variation
======================================================================

======================================================================
EDGE CASE: Coherent Zone Width Scaling
======================================================================
Max Xi variation: 1e-17 -> Zone width: 0.183046 m
Max Xi variation: 1e-16 -> Zone width: 1.830464 m
Max Xi variation: 1e-15 -> Zone width: 18.304636 m
Max Xi variation: 1e-14 -> Zone width: 183.046357 m

Physical Interpretation:
  -> Tighter Xi tolerance = narrower coherent zone
  -> Trade-off between precision and usable volume
======================================================================

======================================================================
EDGE CASE: Very Long Coherence Time (1 second)
======================================================================
Base T2: 1.0 s
SSZ decoherence rate: 1.000000e+00 /s
Effective T2: 1.000000 s

Physical Interpretation:
  -> Even with 1s T2, SSZ effects are present
  -> Long-lived qubits accumulate more SSZ phase drift
======================================================================

======================================================================
EDGE CASE: Very Short Gate Time (1 ps)
======================================================================
Gate time: 1 ps
Optimal gate time: 1.000000 ps
Timing asymmetry: 0.000000e+00

Physical Interpretation:
  -> Ultra-fast gates have less time for SSZ drift
  -> But timing precision requirements increase
======================================================================

======================================================================
EDGE CASE: Zero Coherence Time
======================================================================
Error (expected): float division by zero

Physical Interpretation:
  -> T2=0 means instant decoherence (infinite rate)
======================================================================
  Total: 61, Passed: 61, Failed: 0
  STATUS: GREEN

[G3] PLOT PARITY:
  Working: 7/7
  STATUS: GREEN

[GOLDEN RUNS]:
  Sun:    regime=weak, D_ssz=0.9999978794
  NS:     regime=blended, D_ssz=0.8140930826
  Sgr A*: regime=very_close, D_ssz=0.6273499727

[G6] WEAK/STRONG SPEC:
  Sun (r/r_s=235780.6): weak OK
  NS (r/r_s=2.19): blended FAIL
  STATUS: RED

============================================================
GATE SUMMARY
============================================================
  G1 TRACEABILITY: GREEN
  G2 TEST PARITY: GREEN
  G3 PLOT PARITY: GREEN
  G4 UI PARITY: GREEN
  G5 ONLINE REPRO: GREEN
  G6 WEAK/STRONG: RED
============================================================
OVERALL: SOME GATES RED
======================================================================
SSZ PHYSICS VALIDATION TESTS
======================================================================

[TEST 1] Xi Weak Field Formula
  r_s (Earth) = 8.869806e-03 m
  Xi calculated = 6.9610781867e-10
  Xi expected   = 6.9610781867e-10
  PASS

[TEST 2] D_SSZ = 1/(1+Xi)
  D_SSZ calculated = 0.999999999303892
  D_SSZ expected   = 0.999999999303892
  PASS

[TEST 3] Invariant: D_SSZ * (1 + Xi) = 1
  D_SSZ * (1 + Xi) = 1.000000000000000
  PASS

[TEST 4] GPS Satellite Time Dilation
  D_SSZ (surface) = 0.999999999303892
  D_SSZ (GPS)     = 0.999999999833092
  Time diff/day   = 45.723 us
  Expected        = 45.7 us
  Error           = 0.023 us
  PASS (within 1%)

[TEST 5] Pound-Rebka Experiment
  Height = 22.5 m
  z_SSZ   = 2.442491e-15
  z_GR    = 2.458394e-15
  Measured= 2.46e-15
  PASS (SSZ matches GR in weak field)

[TEST 6] Strong Field: D_SSZ finite at r_s
  r_s (BH) = 29533.394 m
  Xi(r_s)  = 0.801712
  D_SSZ(r_s) = 0.555028
  Expected ~ 0.555
  PASS (SSZ is singularity-free!)

[TEST 7] Weak Field: SSZ matches GR
   r/R_Earth |              D_SSZ |               D_GR |         Diff
  -----------------------------------------------------------------
         1.0 |  0.999999999303892 |  0.999999999303892 |     0.00e+00
         2.0 |  0.999999999651946 |  0.999999999651946 |     1.11e-16
        10.0 |  0.999999999930389 |  0.999999999930389 |     0.00e+00
       100.0 |  0.999999999993039 |  0.999999999993039 |     0.00e+00
  PASS

======================================================================
ALL 7 PHYSICS TESTS PASSED
======================================================================

Key Results:
- Xi = r_s/(2r) in weak field VERIFIED
- D_SSZ = 1/(1+Xi) VERIFIED
- D_SSZ * (1+Xi) = 1 INVARIANT VERIFIED
- GPS ~45.7 us/day VALIDATED
- Pound-Rebka 2.46e-15 VALIDATED
- D_SSZ(r_s) = 0.555 FINITE (no singularity!)
- SSZ matches GR in weak field to O(Xi^2)

=== FULL PIPELINE TEST ===
1. Template loaded: 4 objects
   Columns: ['name', 'M_Msun', 'R_km', 'v_kms', 'z_obs', 'source']
2. Validation: True
3. Normalized: 0 warnings
4. Run created: 20260428_000035
   Run folder: test_reports\20260428_000035
5. Input saved: True
6. Calculated: 4 results
   Columns: ['name', 'M_Msun', 'R_km', 'v_kms', 'r_s_m', 'r_s_km', 'r_over_rs', 'Xi']...
7. Summary:
   - Total objects: 4
   - With observations: 3
   - SSZ wins: 3
   - SSZ win rate: 100.0%
8. Results saved: True
9. Report saved: True
10. Files in run folder:
    - data_input.csv: 232 bytes
    - params.json: 344 bytes
    - plots/
    - report.md: 1245 bytes
    - results.csv: 2246 bytes

=== ALL TESTS PASSED ===
======================================================================
RUN ARTIFACT GENERATION TEST
======================================================================

[1] Loading data...
    Validation: VALID
    Rows: 8
    Normalized with 0 warnings

[2] Creating run...
    Run ID: 20260428_000035

[3] Saving input data...

[4] Running calculations...
    Calculated 8 objects
    Regimes: {'photon_sphere': 5, 'strong': 1, 'blended': 1, 'very_close': 1}

[5] Saving results...

[6] Generating report...

[7] Verifying artifacts...
    Run directory: test_artifacts\20260428_000035
    Artifacts created:
      - data_input.csv (434 bytes)
      - params.json (344 bytes)
      - plots (0 bytes)
      - report.md (1267 bytes)
      - results.csv (4189 bytes)

[8] Report preview:
    # SSZ Calculation Report
    
    **Run ID:** `20260428_000035`
    **Timestamp:** 2026-04-28T00:00:35.544932
    **Git Hash:** `f208cd5`
    
    ---
    
    ## Parameters
    
    | Parameter | Value |
    |-----------|-------|
    | Ï† (phi) | 1.618033988749895 |
    | Î¾(r_s) | 0.8017 (computed) |
    | Xi Mode | auto |
    | Weak Regime | r/r_s > 110.0 |
    | Strong Regime | r/r_s < 90.0 |
    
    ### Physical Constants (CODATA 2018)
    
    ... (35 more lines)

======================================================================
ARTIFACT GENERATION COMPLETE
======================================================================

All 4 required artifacts present!
======================================================================
SSZ Win Rate Analysis - Weak and Strong Field
======================================================================
PSR J0030+0451       | regime=strong       | z_obs=0.220000 | z_gr=0.219094 | z_ssz=0.221840 | GR
PSR J0348+0432       | regime=blended      | z_obs=0.280000 | z_gr=0.356603 | z_ssz=0.361103 | GR
PSR J0740+6620       | regime=photon_sphere | z_obs=0.260000 | z_gr=0.346431 | z_ssz=0.350805 | GR
PSR J1614-2230       | regime=photon_sphere | z_obs=0.270000 | z_gr=0.345400 | z_ssz=0.349756 | GR
Sirius B             | regime=weak         | z_obs=0.000089 | z_gr=0.000260 | z_ssz=0.000260 | GR
Procyon B            | regime=weak         | z_obs=0.000035 | z_gr=0.000108 | z_ssz=0.000108 | GR
40 Eri B             | regime=weak         | z_obs=0.000023 | z_gr=0.000082 | z_ssz=0.000082 | GR
Sun                  | regime=weak         | z_obs=0.000002 | z_gr=0.000002 | z_ssz=0.000002 | GR
----------------------------------------------------------------------
Weak Field:   0/4 = 0.0%
Strong Field: 0/4 = 0.0%
TOTAL:        0/8 = 0.0%
======================================================================

Delta(M) correction values:
         1.0 M_sun: delta_m = 1.2433%
         1.4 M_sun: delta_m = 1.2522%
         2.0 M_sun: delta_m = 1.2617%
        10.0 M_sun: delta_m = 1.3045%
   1000000.0 M_sun: delta_m = 1.6108%
collected 158 items

segcalc/tests/test_invariants.py::TestSSZInvariants::test_dual_velocity_product_is_c_squared PASSED
segcalc/tests/test_invariants.py::TestSSZInvariants::test_xi_plus_d_bounded PASSED
segcalc/tests/test_invariants.py::TestSSZInvariants::test_d_ssz_from_xi_relation PASSED
segcalc/tests/test_invariants.py::TestSSZInvariants::test_ssz_finite_at_horizon PASSED
segcalc/tests/test_invariants.py::TestSSZInvariants::test_xi_at_horizon_is_finite PASSED
segcalc/tests/test_invariants.py::TestRedshiftInvariants::test_z_from_d_relation PASSED
segcalc/tests/test_invariants.py::TestRedshiftInvariants::test_weak_field_redshift_approximation PASSED
segcalc/tests/test_invariants.py::TestGeometricInvariants::test_natural_boundary_ratio PASSED
segcalc/tests/test_invariants.py::TestGeometricInvariants::test_phi_squared_relation PASSED
segcalc/tests/test_invariants.py::TestGeometricInvariants::test_phi_reciprocal_relation PASSED
segcalc/tests/test_invariants.py::TestDatasetInvariants::test_calculate_all_preserves_order PASSED
segcalc/tests/test_invariants.py::TestDatasetInvariants::test_calculate_all_handles_nan PASSED
segcalc/tests/test_invariants.py::TestDatasetInvariants::test_ssz_vs_gr_consistency PASSED
segcalc/tests/test_invariants.py::TestNumericalInvariants::test_xi_monotonic_in_weak_field PASSED
segcalc/tests/test_invariants.py::TestNumericalInvariants::test_d_monotonic_in_weak_field PASSED
segcalc/tests/test_invariants.py::TestNumericalInvariants::test_results_reproducible PASSED
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_phi_precision PASSED
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_schwarzschild_radius_scaling PASSED
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_weak_field_limit PASSED
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_strong_field_limit PASSED
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_blend_continuity PASSED
segcalc/tests/test_physics.py::TestMathematicalConsistency::test_xi_auto_regime_selection PASSED
segcalc/tests/test_physics.py::TestPhysicalLimits::test_no_singularities PASSED
segcalc/tests/test_physics.py::TestPhysicalLimits::test_gr_singularity_at_horizon PASSED
segcalc/tests/test_physics.py::TestPhysicalLimits::test_dual_velocity_invariance PASSED
segcalc/tests/test_physics.py::TestPhysicalLimits::test_time_dilation_bounds PASSED
segcalc/tests/test_physics.py::TestNumericalPrecision::test_mass_range_stability PASSED
segcalc/tests/test_physics.py::TestNumericalPrecision::test_extreme_radii PASSED
segcalc/tests/test_physics.py::TestNumericalPrecision::test_calculate_single_consistency PASSED
segcalc/tests/test_physics.py::TestRegimeClassification::test_photon_sphere_regime PASSED
segcalc/tests/test_physics.py::TestRegimeClassification::test_weak_field_regime PASSED
segcalc/tests/test_physics.py::TestRegimeClassification::test_neutron_star_regime PASSED
segcalc/tests/test_ssz_physics.py::TestConstants::test_golden_ratio PASSED
segcalc/tests/test_ssz_physics.py::TestConstants::test_regime_boundaries PASSED
segcalc/tests/test_ssz_physics.py::TestConstants::test_intersection_point PASSED
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_weak_field_earth PASSED
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_strong_field_horizon PASSED
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_strong_field_zero PASSED
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_blend_zone_continuity PASSED
segcalc/tests/test_ssz_physics.py::TestXiRegimes::test_auto_selects_weak_for_earth PASSED
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_D_ssz_at_horizon PASSED
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_D_gr_at_horizon PASSED
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_D_ssz_never_zero PASSED
segcalc/tests/test_ssz_physics.py::TestTimeDilation::test_weak_field_agreement PASSED
segcalc/tests/test_ssz_physics.py::TestGPSValidation::test_gps_time_correction PASSED
segcalc/tests/test_ssz_physics.py::TestPoundRebka::test_pound_rebka_redshift PASSED
segcalc/tests/test_ssz_physics.py::TestNeutronStarPredictions::test_psr_j0740_regime PASSED
segcalc/tests/test_ssz_physics.py::TestNeutronStarPredictions::test_ssz_predicts_higher_redshift PASSED
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_power_law_parameters PASSED
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_sun_energy_normalization PASSED
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_neutron_star_energy PASSED
segcalc/tests/test_ssz_physics.py::TestPowerLaw::test_power_law_scaling PASSED
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_geom_hint_finite PASSED
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_geom_hint_uses_phi PASSED
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_ssz_geom_hint_mode PASSED
segcalc/tests/test_ssz_physics.py::TestGeomHint::test_ssz_geom_hint_disabled_weak_field PASSED
segcalc/tests/test_ssz_physics.py::TestUniversalIntersection::test_intersection_mass_independent PASSED
test_golden_validation.py::test_golden_dataset_exists PASSED
test_golden_validation.py::test_golden_win_rate 
=== GOLDEN VALIDATION ===
Dataset: unified_results.csv
Total objects: 47
SSZ wins: 46
Win rate: 97.9%
Contract expects: 97.9%
Source: full-output.md L6150: ESO Spectroscopy 46/47 = 97.9%
✅ PASS: Win rate matches Contract
PASSED
test_golden_validation.py::test_golden_regime_distribution 
=== REGIME DISTRIBUTION ===
regime
Strong Field                     24
Strong Field + High Velocity     12
Photon Sphere + High Velocity     6
Photon Sphere                     5
Name: count, dtype: int64

Photon Sphere objects: 11
Strong Field objects: 36
Photon Sphere SSZ win rate: 100.0%
PASSED
test_golden_validation.py::test_golden_columns ✅ All required columns present: ['case', 'regime', 'z_obs', 'z_grsr', 'z_seg', 'winner']
PASSED
test_tie_regression.py::test_tie_on_equal_residuals z_ssz=1.4981516226e-01, z_grsr=1.9126483570e-01, z_mid=1.7053999898e-01
res_ssz=2.0724836722e-02, res_grsr=2.0724836722e-02
winner=TIE
PASSED
test_tie_regression.py::test_ssz_closer_consistent_with_winner PASSED
test_tie_regression.py::test_no_winner_without_observation PASSED
test_tie_regression.py::test_winner_deterministic PASSED
test_tie_regression.py::test_regime_has_numeric_trigger Neutron Star: r_s=4.1347 km, r/r_s=2.90
regime=photon_sphere
PASSED
test_weak_field_contract.py::test_sun_weak_field Sun: r_s = 2.9533 km, R = 696000 km
r/r_s = 235665 (should be >> 10 = weak field)
regime = weak
z_gr = 2.1216586070e-06
z_ssz_grav = 2.1216586070e-06
delta_m_pct = 0.000000
[PASS] Sun weak field: SSZ = GR (no Delta(M))
PASSED
test_weak_field_contract.py::test_earth_orbit_weak_field 
Earth orbit: r_s = 2.9533 km, R = 149.6 million km
r/r_s = 50654524 (should be >> 10 = weak field)
regime = weak
z_gr = 9.8707868545e-09
z_ssz_grav = 9.8707868545e-09
delta_m_pct = 0.000000
[PASS] Earth orbit weak field: SSZ = GR (no Delta(M))
PASSED
test_weak_field_contract.py::test_gps_satellite_weak_field 
GPS: r_s = 8.869806 mm, R = 26600 km
r/r_s = 3.00e+09 (should be >> 10 = weak field)
regime = weak
z_gr = 1.6672574432e-10
z_ssz_grav = 1.6672574432e-10
delta_m_pct = 0.000000
[PASS] GPS weak field: SSZ = GR (no Delta(M))
PASSED
test_weak_field_contract.py::test_neutron_star_strong_field 
Neutron Star: r_s = 4.1347 km, R = 12 km
r/r_s = 2.90 (should be < 10 = strong field)
regime = photon_sphere
z_gr = 2.3518580046e-01
z_ssz_grav = 2.3813087851e-01
delta_m_pct = 1.252235
[PASS] NS strong field: Delta(M) = 1.25% applied
PASSED
tests/test_experimental_validation.py::TestPoundRebka::test_pound_rebka_redshift 
============================================================
POUND-REBKA EXPERIMENT (1960)
============================================================
Tower height: 22.5 m
Measured:     Df/f ~ 2.46e-15
GR theory:    Df/f = 2.458394e-15
SSZ predict:  Df/f = 2.442491e-15
SSZ vs GR:    6.47e-03 rel diff
PASSED
tests/test_experimental_validation.py::TestGPSValidation::test_gps_gravitational_time_dilation 
============================================================
GPS SATELLITE TIME DILATION
============================================================
GPS altitude:     20200 km
D_SSZ (surface):  0.999999999303892
D_SSZ (GPS):      0.999999999833092
SSZ prediction:   45.723 μs/day
Known GR value:   45.700 μs/day
Difference:       0.023 μs/day
PASSED
tests/test_experimental_validation.py::TestGPSValidation::test_gps_position_error_without_correction 
============================================================
GPS POSITION ERROR WITHOUT CORRECTION
============================================================
Time error:     45.723 μs/day
Position error: 13.7 km/day
PASSED
tests/test_experimental_validation.py::TestNISTOpticalClock::test_nist_33cm_height_difference 
============================================================
NIST OPTICAL CLOCK EXPERIMENT (2010)
============================================================
Height diff:  33 cm
Measured:     Df/f ~ 3.6e-17
GR theory:    Df/f = 3.605644e-17
SSZ predict:  Df/f = 0.000000e+00
PASSED
tests/test_experimental_validation.py::TestTokyoSkytree::test_skytree_450m 
============================================================
TOKYO SKYTREE EXPERIMENT (2020)
============================================================
Height:       450 m
Measured:     ~4.0 ns/day
SSZ predict:  4.259 ns/day
PASSED
tests/test_experimental_validation.py::TestWeakFieldContract::test_earth_surface_ssz_equals_gr 
============================================================
WEAK FIELD CONTRACT: SSZ = GR
============================================================
r_s/r = 1.392216e-09 (weak field: << 1)
Xi = 6.961078e-10
D_SSZ = 0.999999999303892
D_GR  = 0.999999999303892
|D_SSZ - D_GR| = 0.000000e+00
PASSED
tests/test_experimental_validation.py::TestWeakFieldContract::test_solar_system_weak_field 
============================================================
SOLAR SYSTEM WEAK FIELD CHECK
============================================================
Object               |           r/r_s |    Weak?
--------------------------------------------------
Earth surface        |        7.18e+08 |      Yes
GPS orbit            |        3.00e+09 |      Yes
Moon orbit           |        4.33e+10 |      Yes
Sun surface          |        2.36e+05 |      Yes
PASSED
tests/test_experimental_validation.py::TestTheoreticalConsistency::test_d_ssz_equals_one_over_one_plus_xi 
============================================================
CONSISTENCY: D_SSZ = 1/(1+Xi)
============================================================
PASSED
tests/test_experimental_validation.py::TestTheoreticalConsistency::test_xi_at_horizon 
============================================================
Xi AT SCHWARZSCHILD RADIUS
============================================================
Xi(r_s) = 1 - e^(-phi) = 0.801712
xi_strong(r_s, r_s) = 0.801712
PASSED
tests/test_experimental_validation.py::TestTheoreticalConsistency::test_d_ssz_finite_at_horizon 
============================================================
D_SSZ AT HORIZON (NO SINGULARITY!)
============================================================
D_SSZ(r_s) = 1/(1 + Xi(r_s)) = 0.555028
Expected: 0.555028
D_GR(r_s) = 0 (singularity)
PASSED
tests/test_geodesics.py::TestNullGeodesics::test_light_cone_closing_positive 
============================================================
LIGHT CONE CLOSING (phi-Spiral)
============================================================
r/r_s      Closing %      
------------------------------
100        99.96          
50         99.85          
20         99.10          
10         96.75          
5          89.48          
2          64.00          
1          36.00          
PASSED
tests/test_geodesics.py::TestNullGeodesics::test_null_geodesic_dr_dT_bounded PASSED
tests/test_geodesics.py::TestNullGeodesics::test_light_travel_time_exceeds_flat_space 
============================================================
LIGHT TRAVEL TIME
============================================================
r_start: 5.0 r_s
r_end:   20.0 r_s
T (SSZ): 7.499581e-03 s
T (flat): 1.477692e-04 s
Excess:   4975.20%
PASSED
tests/test_geodesics.py::TestEffectivePotential::test_effective_potential_bounded 
============================================================
EFFECTIVE POTENTIAL
============================================================
r/r_s      V_eff/c^2      
------------------------------
0.5        0.852071       
1.0        0.640000       
2.0        0.360000       
5.0        0.105186       
10.0       0.032518       
100.0      0.000392       
PASSED
tests/test_geodesics.py::TestEffectivePotential::test_effective_potential_equals_c2_sech2 PASSED
tests/test_geodesics.py::TestAsymptoticLimits::test_metric_smooth_everywhere 
============================================================
PHI-SPIRAL METRIC (smooth, no singularities)
============================================================
r/r_s      gamma           g_TT/c^2       
--------------------------------------------------
0.5        1.083333        -8.520710e-01  
1.0        1.250000        -6.400000e-01  
2.0        1.666667        -3.600000e-01  
5.0        3.083333        -1.051863e-01  
10.0       5.545455        -3.251814e-02  
100.0      50.504950       -3.920416e-04  
PASSED
tests/test_geodesics.py::TestAsymptoticLimits::test_no_horizon_singularity 
============================================================
AT r = r_s (Schwarzschild horizon)
============================================================
gamma(r_s) = 1.250000 (Schwarzschild: infinite)
V_eff(r_s) = 5.752033e+16 (finite!)
PASSED
tests/test_geodesics.py::TestTimelikeGeodesics::test_timelike_geodesic_returns_arrays PASSED
tests/test_geodesics.py::TestTimelikeGeodesics::test_timelike_geodesic_integrates 
============================================================
TIMELIKE GEODESIC INTEGRATION
============================================================
Start:    r0 = 5.0 r_s
Energy:   E/c = 0.9c
Steps:    5000
Final r:  456700.900 r_s
PASSED
tests/test_geodesics.py::TestMetricFunctions::test_phi_gravitational_positive PASSED
tests/test_geodesics.py::TestMetricFunctions::test_gamma_ge_one PASSED
tests/test_geodesics.py::TestMetricFunctions::test_beta_bounded PASSED
tests/test_geodesics.py::TestMetricFunctions::test_sech2_bounded PASSED
tests/test_geodesics.py::TestConsistency::test_gamma_squared_times_sech2_equals_one PASSED
tests/test_geodesics.py::TestConsistency::test_null_geodesic_path_consistency PASSED
tests/test_invariants_hard.py::TestWeakFieldContract::test_sun_weak_field_z_ssz_equals_z_gr PASSED
tests/test_invariants_hard.py::TestWeakFieldContract::test_earth_weak_field_z_ssz_equals_z_gr PASSED
tests/test_invariants_hard.py::TestWeakFieldContract::test_delta_m_is_zero_in_weak_field PASSED
tests/test_invariants_hard.py::TestForbiddenFormula::test_z_ssz_is_not_one_over_d_minus_one PASSED
tests/test_invariants_hard.py::TestWinnerLogic::test_winner_is_deterministic PASSED
tests/test_invariants_hard.py::TestWinnerLogic::test_eps_based_tie_handling PASSED
tests/test_invariants_hard.py::TestGoldenDatasetMatch::test_golden_dataset_46_of_47 PASSED
tests/test_invariants_hard.py::TestGoldenDatasetMatch::test_single_gr_win_is_3c279 PASSED
tests/test_invariants_hard.py::TestXiFormulas::test_xi_weak_formula PASSED
tests/test_invariants_hard.py::TestXiFormulas::test_xi_strong_formula PASSED
tests/test_invariants_hard.py::TestXiFormulas::test_xi_at_horizon_value PASSED
tests/test_invariants_hard.py::TestHorizonFinite::test_d_ssz_finite_at_horizon PASSED
tests/test_invariants_hard.py::TestHorizonFinite::test_d_gr_zero_at_horizon PASSED
tests/test_invariants_hard.py::TestRegimeBoundaries::test_weak_regime_above_10_rs PASSED
tests/test_invariants_hard.py::TestRegimeBoundaries::test_photon_sphere_regime PASSED
tests/test_qubit.py::TestQubitDataclass::test_qubit_creation PASSED
tests/test_qubit.py::TestQubitDataclass::test_qubit_position PASSED
tests/test_qubit.py::TestQubitDataclass::test_qubit_radius PASSED
tests/test_qubit.py::TestQubitDataclass::test_qubit_pair_separation PASSED
tests/test_qubit.py::TestQubitDataclass::test_qubit_pair_height_difference PASSED
tests/test_qubit.py::TestSegmentDensity::test_xi_weak_field_formula PASSED
tests/test_qubit.py::TestSegmentDensity::test_xi_strong_field_formula PASSED
tests/test_qubit.py::TestSegmentDensity::test_xi_positive_definite PASSED
tests/test_qubit.py::TestSegmentDensity::test_xi_gradient_negative_weak_field PASSED
tests/test_qubit.py::TestTimeDilation::test_d_ssz_equals_one_over_one_plus_xi PASSED
tests/test_qubit.py::TestTimeDilation::test_d_ssz_less_than_one PASSED
tests/test_qubit.py::TestTimeDilation::test_time_dilation_difference_sign PASSED
tests/test_qubit.py::TestQubitAnalysis::test_analyze_qubit_returns_segment_analysis PASSED
tests/test_qubit.py::TestQubitAnalysis::test_pair_mismatch_zero_for_same_height PASSED
tests/test_qubit.py::TestQubitAnalysis::test_pair_mismatch_increases_with_height_diff PASSED
tests/test_qubit.py::TestGateTiming::test_gate_timing_correction_at_reference PASSED
tests/test_qubit.py::TestGateTiming::test_two_qubit_gate_timing_returns_dict PASSED
tests/test_qubit.py::TestDecoherence::test_decoherence_rate_positive PASSED
tests/test_qubit.py::TestDecoherence::test_effective_T2_less_than_base PASSED
tests/test_qubit.py::TestDecoherence::test_effective_T2_nearly_equals_base PASSED
tests/test_qubit.py::TestSegmentCoherentZones::test_zone_formula PASSED
tests/test_qubit.py::TestHawkingTemperature::test_hawking_temp_solar_mass PASSED
tests/test_qubit.py::TestHawkingTemperature::test_hawking_temp_inverse_mass PASSED
tests/test_qubit.py::TestHawkingTemperature::test_ssz_hawking_temp_finite PASSED
tests/test_qubit.py::TestHawkingTemperature::test_ssz_hawking_temp_less_than_classical PASSED
tests/test_qubit.py::TestHawkingTemperature::test_evaporation_time_solar_mass PASSED
tests/test_qubit.py::TestHawkingTemperature::test_radiation_power_positive PASSED
tests/test_qubit.py::TestUtilityFunctions::test_height_to_time_offset_sign PASSED
tests/test_qubit.py::TestUtilityFunctions::test_time_difference_per_second_positive PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_very_close_regime PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_blended_regime PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_photon_sphere_regime PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_strong_regime PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_weak_regime PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_boundary_values PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_constants_values PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_simple_regime_classification PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_zero_schwarzschild_radius PASSED
tests/test_regime_classification.py::TestRegimeClassification::test_negative_schwarzschild_radius PASSED
tests/test_regime_classification.py::TestLegacyContextAwareness::test_segcalc_does_not_use_legacy_90_110 PASSED
tests/test_regime_classification.py::TestLegacyContextAwareness::test_segcalc_weak_boundary_is_10 PASSED
tests/test_ui_canonicalization.py::TestUICanonicalRegimes::test_get_regime_uses_canonical_thresholds PASSED
tests/test_ui_canonicalization.py::TestUICanonicalRegimes::test_no_legacy_90_110_in_constants PASSED
tests/test_ui_canonicalization.py::TestUICanonicalRegimes::test_regime_names_are_canonical PASSED
tests/test_ui_canonicalization.py::TestUIWinnerLogic::test_winner_requires_real_z_obs PASSED
tests/test_ui_canonicalization.py::TestNoLegacyStrings::test_app_py_no_legacy_90_110_in_ui_text PASSED
tests/test_ui_canonicalization.py::TestNoLegacyStrings::test_reference_tab_shows_canonical_boundaries PASSED
tests/test_ui_canonicalization.py::TestRegimeColorMapping::test_regime_colors_defined_for_all_canonical_regimes PASSED

============================= 158 passed in 4.58s =============================

```


---

================================================================================
REPO: ssz-schuhman-experiment
Status: FAILED
Exit Code: 1
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-schuhman-experiment
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 188 items

scripts/test_gamma_seg_transfer.py::test_mathematical_consistency ======================================================================
TEST 1: Mathematical Consistency of gamma_seg
======================================================================


--- Small alpha (Earth-like): alpha=1e-09, r_c=1.00e+06 m ---
  gamma(0) = 0.9999999990, expected = 0.9999999990, OK = True
  gamma(3*r_c) = 1.0000000000, expected ~ 1, OK = True
  delta_f/f = -0.000000 (-0.0000%)
  Delta_v/v = 0.000000 (0.0000%)
  z = 0.000000
  z ~ alpha check: z=0.0000, alpha=0.0000, ratio=1.00

--- Medium alpha (G79-like): alpha=0.12, r_c=5.86e+16 m ---
  gamma(0) = 0.8800000000, expected = 0.8800000000, OK = True
  gamma(3*r_c) = 0.9999851908, expected ~ 1, OK = True
  delta_f/f = -0.120000 (-12.0000%)
  Delta_v/v = 0.066004 (6.6004%)
  z = 0.136364
  z ~ alpha check: z=0.1364, alpha=0.1200, ratio=1.14

--- Large alpha (NS-like): alpha=0.25, r_c=1.20e+04 m ---
  gamma(0) = 0.7500000000, expected = 0.7500000000, OK = True
  gamma(3*r_c) = 0.9999691475, expected ~ 1, OK = True
  delta_f/f = -0.250000 (-25.0000%)
  Delta_v/v = 0.154701 (15.4701%)
  z = 0.333333
  z ~ alpha check: z=0.3333, alpha=0.2500, ratio=1.33

--- Very large alpha (BH-like): alpha=0.5, r_c=1.00e+05 m ---
  gamma(0) = 0.5000000000, expected = 0.5000000000, OK = True
  gamma(3*r_c) = 0.9999382951, expected ~ 1, OK = True
  delta_f/f = -0.500000 (-50.0000%)
  Delta_v/v = 0.414214 (41.4214%)
  z = 1.000000

======================================================================
TEST 1 RESULT: PASSED
======================================================================
PASSED
scripts/test_gamma_seg_transfer.py::test_g79_predictions 
======================================================================
TEST 2: G79 Nebula Predictions
======================================================================

Parameters: alpha = 0.12, r_c = 1.9 pc

Predictions at center:
  gamma_seg = 0.8800
  delta_f/f = -12.0%
  Delta_v/v = 6.6%

Checks:
  gamma = 1 - alpha = 0.8800, computed = 0.8800, OK = True
  delta_f/f = gamma - 1 = -0.1200, computed = -0.1200, OK = True

Temperature shell prediction:
  r = 0 pc: T = 440 K
  r = 1 pc: T = 455 K
  r = 2 pc: T = 480 K
  r = 3 pc: T = 495 K

Velocity excess prediction:
  For v0 = 50 km/s: Delta_v = 3.3 km/s
  Observed: ~5 km/s (consistent!)

======================================================================
TEST 2 RESULT: PASSED
======================================================================
PASSED
scripts/test_gamma_seg_transfer.py::test_nicer_application 
======================================================================
TEST 3: NICER Pulsar Application
======================================================================

Pulsar: J0740+6620
Mass: 2.08 M_sun
Radius: 12.39 km

Compactness:
  Computed: 0.247955
  Expected: 0.247955
  OK: True

GR surface redshift:
  Computed: 0.408466
  Expected: 0.408466
  OK: True

SSZ test:
  If z_obs = z_GR + 10%:
    delta_seg = 0.1000 (10.0%)
    This would indicate SSZ effect!

  Current NICER precision: ~17%
  -> Can constrain |delta_seg| < 17%

======================================================================
TEST 3 RESULT: PASSED
======================================================================
PASSED
scripts/test_gamma_seg_transfer.py::test_gw_application 
======================================================================
TEST 4: GW Ringdown Application
======================================================================

Event: GW150914
Final mass: 63.1 M_sun
Final spin: 0.69

QNM frequency (GR):
  f_QNM = 271.7 Hz

Comparison with observation:
  f_QNM (GR) = 271.7 Hz
  f_QNM (obs) = 251 +/- 8 Hz
  delta_seg = -0.0762 (-7.6%)
  delta_seg_err = 0.0294 (2.9%)

SSZ interpretation:
  f_SSZ = f_GR * (1 + delta_seg)
  Same structure as G79: nu' = nu_0 * gamma_seg

  Deviation from GR: 2.6 sigma
  Consistent with GR (< 3 sigma): True

======================================================================
TEST 4 RESULT: PASSED (framework works, interpretation ongoing)
======================================================================
PASSED
scripts/test_gamma_seg_transfer.py::test_scaling_relation 
======================================================================
TEST 5: Scaling Relation
======================================================================

Hypothesis: alpha ~ GM/(Rc^2)

Regime               alpha (theory)  delta_f/f (obs) Consistent? 
--------------------------------------------------------------
Earth                0.0000          < 0.5%          True
G79 Nebula           0.1200          DETECTED        True
Neutron Star         0.2500          < 17.0%         True
Black Hole           0.5000          < 26.0%         True

Interpretation:
  - Earth: alpha ~ 10^-9, effect invisible (< 0.5%)
  - G79: alpha ~ 0.12, effect DETECTED (~12%)
  - NS/BH: alpha ~ 0.2-0.5, strong effects expected

The scaling is CONSISTENT with SSZ theory!

======================================================================
TEST 5 RESULT: PASSED
======================================================================
PASSED
scripts/test_ssz_correct_predictions.py::test_44_percent_prediction ======================================================================
TEST 1: The -44% Prediction at r = 5*r_s
======================================================================

Parameters:
  M = 2.0 M_sun
  r_s = 5.91 km
  r = 5*r_s = 29.54 km
  Xi_max = 1.0
  phi = 1.618034

Results:
  Xi(5*r_s) = 0.9997
  D_GR(5*r_s) = 0.8944
  D_SSZ(5*r_s) = 1/(1+Xi) = 0.5001
  Delta = -44.1%

Expected: Delta ~ -44%
Actual: Delta = -44.1%

TEST RESULT: PASSED
PASSED
scripts/test_ssz_correct_predictions.py::test_universal_crossover 
======================================================================
TEST 2: Universal Crossover
======================================================================

Parameters:
  M = 10.0 M_sun
  r_s = 29.54 km
  Xi_max = 1.0

Results:
  r* / r_s = 1.386562
  Xi(r*) = 0.893914
  D_GR(r*) = 0.528007
  D_SSZ(r*) = 0.528007
  Expected r*/r_s ~ 1.387

Crossover at r* = 1.3866 * r_s
TEST RESULT: PASSED
PASSED
scripts/test_ssz_correct_predictions.py::test_horizon_behavior 
======================================================================
TEST 3: Horizon Behavior (No Singularity)
======================================================================

At r = r_s (horizon):
  Xi(r_s) = 0.8017
  D_GR(r_s) = 0.0000 (SINGULARITY - time stops!)
  D_SSZ(r_s) = 1/(1+Xi) = 0.5550 (FINITE - time continues!)

At r = 1.01*r_s (just outside):
  D_GR = 0.0995
  D_SSZ = 0.5540

SSZ time dilation is FINITE at horizon: 0.5550
TEST RESULT: PASSED
PASSED
scripts/test_ssz_correct_predictions.py::test_g79_nebula 
======================================================================
TEST 4: G79.29+0.46 Nebula Predictions
======================================================================

Parameters:
  alpha = 0.12
  r_c = 1.9 pc
  r = 0.5 pc

Results:
  gamma_seg = 0.8880
  z_temporal = 0.1120 (expected ~0.12)
  Xi (coherence) = 1.1261
  T_local = 213 K (from T_ext = 240 K)
  Delta_v = 1.3 km/s (expected ~5 km/s)

z_temporal ~ 0.12: 0.1120
TEST RESULT: PASSED
PASSED
scripts/test_ssz_correct_predictions.py::test_segment_saturation 
======================================================================
TEST 5: Segment Saturation
======================================================================

Xi_max = 1.0
Xi(r) = Xi_max * (1 - exp(-phi * r / r_s))

Xi(r) at various radii:
  r = 0.5*r_s: Xi = 0.5547, D_SSZ = 0.6432, D_GR = 0.0000
  r = 1.0*r_s: Xi = 0.8017, D_SSZ = 0.5550, D_GR = 0.0000
  r = 2.0*r_s: Xi = 0.9607, D_SSZ = 0.5100, D_GR = 0.7071
  r = 5.0*r_s: Xi = 0.9997, D_SSZ = 0.5001, D_GR = 0.8944
  r = 10.0*r_s: Xi = 1.0000, D_SSZ = 0.5000, D_GR = 0.9487
  r = 100.0*r_s: Xi = 1.0000, D_SSZ = 0.5000, D_GR = 0.9950

Xi(100*r_s) = 1.0000 <= Xi_max = 1.0
D_SSZ(r_s) = 0.5550 > 0 (no singularity!)
TEST RESULT: PASSED
PASSED
scripts/test_ssz_correct_predictions.py::test_earth_schumann 
======================================================================
TEST 6: Earth/Schumann - NULL TEST
======================================================================

Earth Parameters:
  M_earth = 5.972e+24 kg
  R_earth = 6371.0 km
  r_s (Earth) = 8.870 mm (!)
  Compactness GM/(Rc^2) = 6.96e-10

At Earth Surface (WEAK-FIELD LIMIT):
  r / r_s = 7.18e+08 (very far from horizon!)
  Xi(R_earth) = alpha * r_s / (2r) = 6.96e-10
  D_GR = 0.9999999993
  D_SSZ = 1/(1+Xi) = 0.9999999993
  Delta = 0.00e+00%

Schumann Resonance Implications:
  f_Schumann ~ 7.83 Hz
  SSZ frequency shift: delta_f/f ~ 6.96e-10
  Absolute shift: delta_f ~ 5.45e-09 Hz
  This is UNDETECTABLE (< measurement precision)!

Comparison with observations:
  Observed Schumann variations: ~0.1-0.5 Hz (ionospheric)
  SSZ prediction: ~5.45e-09 Hz
  Ratio: SSZ / observed ~ 5.45e-08

NULL TEST: Xi_earth = 6.96e-10 << 1
SSZ effect is 6.96e-10, which is UNDETECTABLE!
This is WHY Schumann shows no SSZ signal!
TEST RESULT: PASSED
PASSED
scripts/test_ssz_correct_predictions.py::test_scaling_comparison 
======================================================================
TEST 7: Scaling Comparison Across Regimes
======================================================================

Regime                    GM/(Rc^2)    Xi           D_SSZ      D_GR       Delta     
-------------------------------------------------------------------------------------
Earth (Schumann)          6.96e-10     6.96e-10     1.000000   1.000000   0.00e+00  %
Sun                       2.12e-06     2.12e-06     0.999998   0.999998   6.76e-10  %
White Dwarf               2.11e-04     2.11e-04     0.999789   0.999789   6.68e-06  %
Neutron Star              2.46e-01     9.63e-01     0.509525   0.712506   -2.85e+01 %
Stellar BH (10 M_sun)     1.00e-01     1.00e+00     0.500077   0.894427   -4.41e+01 %
SMBH (Sgr A*)             1.00e-01     1.00e+00     0.500077   0.894427   -4.41e+01 %

KEY INSIGHT:
  - Weak field (Earth, Sun, WD): Xi ~ r_s/r ~ GM/(Rc^2) << 1
  - Strong field (NS, BH): Xi ~ 1, Delta ~ -44%
  - SSZ effect scales with gravitational potential!

Earth Xi = 6.96e-10 < 10^-6: True
BH Delta = -44.1% ~ -44%: True
TEST RESULT: PASSED
PASSED
scripts/test_ssz_expected_regimes.py::test_nicer_regime ======================================================================
TEST: NICER NEUTRON STAR REGIME
======================================================================

Testing: z_SSZ = z_GR * (1 + delta_seg)
Expected: alpha ~ GM/(Rc^2) ~ 0.15-0.25

--- PSR J0030+0451 ---
  M = 1.440 (+0.15/-0.14) M_sun
  R = 13.02 (+1.24/-1.06) km
  Ref: Miller+2019 ApJL 887, L24
  Compactness: 0.1634 +/- 0.0231
  z_GR: 0.2187 +/- 0.0417
  SSZ expected delta_seg: 0.1953 (19.5%)
  Current precision allows: |delta_seg| < 0.1908 (19.1%)
  SSZ detectable with current precision? True

--- PSR J0740+6620 ---
  M = 2.080 (+0.07/-0.07) M_sun
  R = 12.39 (+1.3/-0.98) km
  Ref: Riley+2021 ApJL 918, L27
  Compactness: 0.2480 +/- 0.0273
  z_GR: 0.4085 +/- 0.0763
  SSZ expected delta_seg: 0.3297 (33.0%)
  Current precision allows: |delta_seg| < 0.1869 (18.7%)
  SSZ detectable with current precision? True

--- PSR J0437-4715 ---
  M = 1.418 (+0.037/-0.037) M_sun
  R = 11.36 (+0.95/-0.63) km
  Ref: Choudhury+2024
  Compactness: 0.1844 +/- 0.0162
  z_GR: 0.2586 +/- 0.0322
  SSZ expected delta_seg: 0.2260 (22.6%)
  Current precision allows: |delta_seg| < 0.1245 (12.5%)
  SSZ detectable with current precision? True

SUMMARY:
--------------------------------------------------
  PSR J0030+0451: delta_seg ~ 20%, limit < 19% -> DETECTABLE
  PSR J0740+6620: delta_seg ~ 33%, limit < 19% -> DETECTABLE
  PSR J0437-4715: delta_seg ~ 23%, limit < 12% -> DETECTABLE

CONCLUSION:
  Average expected SSZ: 25%
  Average current limit: 17%
  -> SSZ SHOULD BE DETECTABLE if alpha ~ compactness!
PASSED
scripts/test_ssz_expected_regimes.py::test_gw_regime 
======================================================================
TEST: GW RINGDOWN REGIME
======================================================================

Testing: f_SSZ = f_GR * (1 + delta_seg)
Expected: alpha ~ 0.5 at horizon

--- GW150914 ---
  M_final = 62.2 +/- 3.7 M_sun
  a_final = 0.68 +/- 0.05
  Ref: Abbott+2016 PRL 116, 061102
  f_QNM (GR): 273.5 +/- 16.3 Hz
  f_ring (obs): 251.0 +/- 8.0 Hz
  delta_seg (inferred): -0.0823 +/- 0.0619 (-8.2% +/- 6.2%)
  Deviation from GR: 1.3 sigma
  SSZ expected (alpha=0.5): delta_seg ~ 100%

--- GW170104 ---
  M_final = 48.9 +/- 4.0 M_sun
  a_final = 0.66 +/- 0.08
  Ref: Abbott+2017 PRL 118, 221101
  f_QNM (GR): 342.7 +/- 28.0 Hz
  f_ring: Not measured

--- GW170814 ---
  M_final = 53.4 +/- 3.3 M_sun
  a_final = 0.72 +/- 0.05
  Ref: Abbott+2017 PRL 119, 141101
  f_QNM (GR): 328.9 +/- 20.3 Hz
  f_ring: Not measured

--- GW190521 ---
  M_final = 142.0 +/- 16.0 M_sun
  a_final = 0.72 +/- 0.09
  Ref: Abbott+2020 PRL 125, 101102
  f_QNM (GR): 123.7 +/- 13.9 Hz
  f_ring (obs): 63.0 +/- 5.0 Hz
  delta_seg (inferred): -0.4907 +/- 0.0702 (-49.1% +/- 7.0%)
  Deviation from GR: 7.0 sigma
  SSZ expected (alpha=0.5): delta_seg ~ 100%

SUMMARY:
--------------------------------------------------
  GW150914: delta_seg = -8.2% +/- 6.2% (1.3 sigma)
  GW190521: delta_seg = -49.1% +/- 7.0% (7.0 sigma)

  Combined: delta_seg = -26.1% +/- 4.6%

CONCLUSION:
  Observed deviation: -26.1%
  SSZ expected (alpha=0.5): ~100%
  -> Observed << Expected, suggesting alpha << 0.5 at ringdown
PASSED
scripts/test_ssz_expected_regimes.py::test_feka_regime 
======================================================================
TEST: Fe-Ka X-RAY LINE REGIME
======================================================================

Testing: E_obs = E_rest * g_SSZ where g_SSZ = g_GR * (1 + delta_seg)
Expected: alpha ~ 0.3-0.5 at ISCO

--- MCG-6-30-15 (Seyfert 1) ---
  M = 2.90e+06 M_sun
  a = 0.989
  Ref: Tanaka+1995, Fabian+2002
  r_ISCO = 1.47 r_g
  g_ISCO (GR) = 0.642
  E_line (GR at ISCO) = 4.11 keV
  E_line (obs peak) = 6.40 +/- 0.10 keV
  Line width (FWHM) = 1.80 keV
  Note: Broad line - peak from outer disk, red wing from ISCO
  Red wing minimum (GR): ~4.1 keV
  Red wing minimum (obs): ~4.6 keV
  Rough delta: 12%

--- 1H0707-495 (NLS1) ---
  M = 2.00e+06 M_sun
  a = 0.980
  Ref: Fabian+2009
  r_ISCO = 1.61 r_g
  g_ISCO (GR) = 0.684
  E_line (GR at ISCO) = 4.38 keV
  E_line (obs peak) = 6.40 +/- 0.20 keV
  Line width (FWHM) = 2.50 keV
  Note: Broad line - peak from outer disk, red wing from ISCO
  Red wing minimum (GR): ~4.4 keV
  Red wing minimum (obs): ~3.9 keV
  Rough delta: -11%

--- Cyg X-1 (HMXB) ---
  M = 2.12e+01 M_sun
  a = 0.998
  Ref: Tomsick+2014, Duro+2011
  r_ISCO = 1.24 r_g
  g_ISCO (GR) = 0.571
  E_line (GR at ISCO) = 3.65 keV
  E_line (obs peak) = 6.40 +/- 0.10 keV
  Line width (FWHM) = 0.80 keV
  Note: Broad line - peak from outer disk, red wing from ISCO
  Red wing minimum (GR): ~3.7 keV
  Red wing minimum (obs): ~5.6 keV
  Rough delta: 53%

--- GRS 1915+105 (LMXB) ---
  M = 1.24e+01 M_sun
  a = 0.980
  Ref: Miller+2013
  r_ISCO = 1.61 r_g
  g_ISCO (GR) = 0.684
  E_line (GR at ISCO) = 4.38 keV
  E_line (obs peak) = 6.40 +/- 0.15 keV
  Line width (FWHM) = 1.20 keV
  Note: Broad line - peak from outer disk, red wing from ISCO
  Red wing minimum (GR): ~4.4 keV
  Red wing minimum (obs): ~5.2 keV
  Rough delta: 19%

SUMMARY:
--------------------------------------------------
  Fe-Ka lines require FULL spectral modeling (relxill)
  Simple peak comparison is NOT sufficient for SSZ test
  The broad line profile encodes information about:
    - Disk geometry
    - Emissivity profile
    - GR effects (redshift, beaming, light bending)

CONCLUSION:
  Fe-Ka is the MOST COMPLEX regime for SSZ testing
  Requires: relxill + SSZ modification to g-factor
  Current data: Consistent with GR Kerr metric
PASSED
scripts/test_ssz_expected_regimes.py::test_scaling_across_regimes 
======================================================================
TEST: SCALING ACROSS ALL REGIMES
======================================================================

Hypothesis: delta_seg ~ alpha ~ GM/(Rc^2)

Regime               GM/(Rc^2)    delta_obs    Type           
------------------------------------------------------------
Earth (Schumann)     7.00e-10     < 0.5%       upper_bound    
G79 Nebula           0.120        12.0% +/- 2.0% detection      
NICER (avg)          0.199        < 17.0%      upper_bound    
GW Ringdown          0.500        28.7%        measurement    

SCALING ANALYSIS:
--------------------------------------------------
  If delta_seg = alpha (linear scaling):
    Earth (Schumann): expected 7.00e-08%, limit < 0.5%
    G79 Nebula: expected 12.0%, observed 12.0%, ratio = 1.00
    NICER (avg): expected 1.99e+01%, limit < 17.0%

CONCLUSION:
  - G79: delta ~ alpha (SSZ detected!)
  - Earth: delta << alpha (below detection, as expected)
  - NS: delta < 17% at alpha ~ 20% (consistent with GR or small SSZ)
  - BH: delta ~ 20% at alpha ~ 50% (smaller than expected)

  -> SSZ effects appear to be SMALLER than naive alpha ~ GM/(Rc^2)
  -> Or: SSZ has different functional form in strong fields
PASSED
scripts/test_ssz_full_scale.py::test_object ERROR
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_load_csv_schumann PASSED
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_validate_schumann_data PASSED
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_convert_to_standard_format PASSED
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_missing_file_error PASSED
tests/data/test_real_loaders.py::TestRealSchumannLoader::test_missing_column_error PASSED
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_load_f107 PASSED
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_load_kp PASSED
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_resample_to_match PASSED
tests/data/test_real_loaders.py::TestRealSpaceWeatherLoader::test_load_space_weather_from_config PASSED
tests/data/test_real_loaders.py::TestUnifiedLoader::test_load_synthetic_data PASSED
tests/data/test_real_loaders.py::TestUnifiedLoader::test_unified_data_get_frequencies PASSED
tests/data/test_real_loaders.py::TestUnifiedLoader::test_unified_data_summary PASSED
tests/data/test_real_loaders.py::TestUnifiedLoader::test_config_from_dict PASSED
tests/data/test_real_loaders.py::TestIntegrationRealPipeline::test_real_pipeline_smoke PASSED
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_to_lambda_7mhz PASSED
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_to_lambda_14mhz PASSED
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_lambda_to_freq_roundtrip PASSED
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_mhz_to_lambda PASSED
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_freq_khz_to_lambda PASSED
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_period_roundtrip PASSED
tests/hamtools/test_hamtools.py::TestCoreFrequency::test_negative_frequency_raises PASSED
tests/hamtools/test_hamtools.py::TestCoreDB::test_db_from_ratio_double PASSED
tests/hamtools/test_hamtools.py::TestCoreDB::test_db_from_ratio_10x PASSED
tests/hamtools/test_hamtools.py::TestCoreDB::test_ratio_from_db_3db PASSED
tests/hamtools/test_hamtools.py::TestCoreDB::test_db_roundtrip PASSED
tests/hamtools/test_hamtools.py::TestCoreDB::test_voltage_db PASSED
tests/hamtools/test_hamtools.py::TestCoreERP::test_erp_no_gain_no_loss PASSED
tests/hamtools/test_hamtools.py::TestCoreERP::test_erp_with_gain PASSED
tests/hamtools/test_hamtools.py::TestCoreERP::test_erp_with_loss PASSED
tests/hamtools/test_hamtools.py::TestCoreERP::test_dbd_to_dbi PASSED
tests/hamtools/test_hamtools.py::TestAntennas::test_dipole_40m PASSED
tests/hamtools/test_hamtools.py::TestAntennas::test_dipole_20m PASSED
tests/hamtools/test_hamtools.py::TestAntennas::test_vertical_40m PASSED
tests/hamtools/test_hamtools.py::TestAntennas::test_yagi_gain_positive PASSED
tests/hamtools/test_hamtools.py::TestAntennas::test_yagi_gain_increases_with_elements PASSED
tests/hamtools/test_hamtools.py::TestAntennas::test_shortening_factor_effect PASSED
tests/hamtools/test_hamtools.py::TestFeedline::test_rg58_higher_loss_than_ecoflex PASSED
tests/hamtools/test_hamtools.py::TestFeedline::test_loss_increases_with_frequency PASSED
tests/hamtools/test_hamtools.py::TestFeedline::test_total_loss_proportional_to_length PASSED
tests/hamtools/test_hamtools.py::TestFeedline::test_power_at_antenna PASSED
tests/hamtools/test_hamtools.py::TestFeedline::test_unknown_cable_raises PASSED
tests/hamtools/test_hamtools.py::TestPropagation::test_critical_freq_formula PASSED
tests/hamtools/test_hamtools.py::TestPropagation::test_muf_increases_with_distance PASSED
tests/hamtools/test_hamtools.py::TestPropagation::test_muf_at_zero_distance PASSED
tests/hamtools/test_hamtools.py::TestPropagation::test_skip_distance_below_critical PASSED
tests/hamtools/test_hamtools.py::TestPropagation::test_skip_distance_above_critical PASSED
tests/hamtools/test_hamtools.py::TestSSZExtension::test_d_ssz_from_delta PASSED
tests/hamtools/test_hamtools.py::TestSSZExtension::test_effective_c_reduced PASSED
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_lambda_shorter PASSED
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_effect_proportional PASSED
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_effect_scales PASSED
tests/hamtools/test_hamtools.py::TestSSZExtension::test_zero_delta_no_effect PASSED
tests/hamtools/test_hamtools.py::TestSSZExtension::test_ssz_skip_distance PASSED
tests/hamtools/test_hamtools.py::TestIntegration::test_antenna_uses_correct_wavelength PASSED
tests/hamtools/test_hamtools.py::TestIntegration::test_ssz_antenna_correction PASSED
tests/test_end_to_end.py::TestSyntheticDataGeneration::test_create_synthetic_schumann PASSED
tests/test_end_to_end.py::TestSyntheticDataGeneration::test_create_synthetic_space_weather PASSED
tests/test_end_to_end.py::TestDataMerging::test_merge_all PASSED
tests/test_end_to_end.py::TestDataMerging::test_compute_derived_variables PASSED
tests/test_end_to_end.py::TestDeltaComputation::test_compute_all_deltas PASSED
tests/test_end_to_end.py::TestDeltaComputation::test_delta_recovery PASSED
tests/test_end_to_end.py::TestModelFitting::test_fit_classical_model PASSED
tests/test_end_to_end.py::TestModelFitting::test_fit_ssz_model PASSED
tests/test_end_to_end.py::TestModelFitting::test_compare_models PASSED
tests/test_end_to_end.py::TestModeConsistency::test_ssz_signature_detection PASSED
tests/test_end_to_end.py::TestFullPipeline::test_run_analysis_pipeline PASSED
tests/test_layered_ssz.py::TestLayerConfig::test_layer_config_creation PASSED
tests/test_layered_ssz.py::TestLayerConfig::test_layer_config_defaults PASSED
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_default_config PASSED
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_layers_property PASSED
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_total_weight PASSED
tests/test_layered_ssz.py::TestLayeredSSZConfig::test_normalize_weights PASSED
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_no_segmentation PASSED
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_ionosphere_only PASSED
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_all_layers PASSED
tests/test_layered_ssz.py::TestDSSZCalculations::test_D_SSZ_from_sigmas_function PASSED
tests/test_layered_ssz.py::TestDSSZCalculations::test_effective_delta_seg PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_mode1 PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_mode2 PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_mode3 PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_classical_invalid_mode PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_ssz_layered_no_correction PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_f_n_ssz_layered_with_correction PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_compute_all_modes PASSED
tests/test_layered_ssz.py::TestFrequencyCalculations::test_relative_shift_uniform PASSED
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_phi_segment_density_ssz_core PASSED
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_phi_segment_density_linear PASSED
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_sigma_from_phi_ratio_no_difference PASSED
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_sigma_from_phi_ratio_positive PASSED
tests/test_layered_ssz.py::TestPhiBasedSegmentation::test_create_phi_based_config PASSED
tests/test_layered_ssz.py::TestTimeVaryingModel::test_sigma_iono_from_proxy_constant PASSED
tests/test_layered_ssz.py::TestTimeVaryingModel::test_sigma_iono_from_proxy_varying PASSED
tests/test_layered_ssz.py::TestTimeVaryingModel::test_f_n_ssz_timeseries PASSED
tests/test_layered_ssz.py::TestTimeVaryingModel::test_f_n_ssz_timeseries_pandas PASSED
tests/test_layered_ssz.py::TestFrequencyShiftEstimate::test_zero_segmentation PASSED
tests/test_layered_ssz.py::TestFrequencyShiftEstimate::test_one_percent_segmentation PASSED
tests/test_layered_ssz.py::TestFrequencyShiftEstimate::test_shift_proportional_to_frequency PASSED
tests/test_layered_ssz.py::TestPhysicalConsistency::test_positive_segmentation_lowers_frequency PASSED
tests/test_layered_ssz.py::TestPhysicalConsistency::test_negative_segmentation_raises_frequency PASSED
tests/test_layered_ssz.py::TestPhysicalConsistency::test_frequency_ratios_preserved PASSED
tests/test_layered_ssz.py::TestPhysicalConsistency::test_realistic_shift_magnitude PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_at_zero PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_at_infinity PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_at_r_s PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_Xi_ssz_array PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_from_Xi_at_zero PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_from_Xi_at_one PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_from_Xi_range PASSED
tests/test_layered_ssz.py::TestCoreSSZFormulas::test_D_SSZ_no_singularity PASSED
tests/test_models.py::TestClassicalSchumann::test_mode_factor PASSED
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_values PASSED
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_eta_1 PASSED
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_scaling PASSED
tests/test_models.py::TestClassicalSchumann::test_compute_eta0_from_mean_f1 PASSED
tests/test_models.py::TestClassicalSchumann::test_f_n_classical_timeseries PASSED
tests/test_models.py::TestSSZCorrection::test_D_SSZ_basic PASSED
tests/test_models.py::TestSSZCorrection::test_D_SSZ_array PASSED
tests/test_models.py::TestSSZCorrection::test_f_n_ssz_model PASSED
tests/test_models.py::TestSSZCorrection::test_delta_seg_from_observed PASSED
tests/test_models.py::TestSSZCorrection::test_delta_seg_roundtrip PASSED
tests/test_models.py::TestSSZCorrection::test_mode_consistency_perfect PASSED
tests/test_models.py::TestSSZCorrection::test_mode_consistency_inconsistent PASSED
tests/test_models.py::TestPhysicalConsistency::test_frequency_ratios PASSED
tests/test_models.py::TestPhysicalConsistency::test_ssz_preserves_ratios PASSED
tests/test_models.py::TestPhysicalConsistency::test_relative_shift_uniform PASSED
tests/test_models.py::TestSSZSignatureDetection::test_strong_ssz_detection PASSED
tests/test_models.py::TestSSZSignatureDetection::test_null_ssz_detection PASSED
tests/test_models.py::TestSSZSignatureDetection::test_ssz_score_formula PASSED
tests/test_models.py::TestSSZSignatureDetection::test_interpretation_strings PASSED
tests/test_physical_ssz.py::TestPlasmaParameters::test_plasma_frequency_typical PASSED
tests/test_physical_ssz.py::TestPlasmaParameters::test_plasma_frequency_scaling PASSED
tests/test_physical_ssz.py::TestPlasmaParameters::test_gyro_frequency_typical PASSED
tests/test_physical_ssz.py::TestPlasmaParameters::test_gyro_frequency_linear PASSED
tests/test_physical_ssz.py::TestIonosphereState::test_create_state PASSED
tests/test_physical_ssz.py::TestIonosphereState::test_reference_state PASSED
tests/test_physical_ssz.py::TestDeltaSegPhysical::test_reference_gives_zero PASSED
tests/test_physical_ssz.py::TestDeltaSegPhysical::test_increased_density PASSED
tests/test_physical_ssz.py::TestDeltaSegPhysical::test_increased_b_field PASSED
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_typical_quiet_sun PASSED
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_active_sun PASSED
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_geomagnetic_storm PASSED
tests/test_physical_ssz.py::TestDeltaSegFromProxies::test_height_variation PASSED
tests/test_physical_ssz.py::TestSSZFrequency::test_reference_state_matches_classical PASSED
tests/test_physical_ssz.py::TestSSZFrequency::test_mode_independence PASSED
tests/test_physical_ssz.py::TestPredictions::test_predict_signature_returns_dict PASSED
tests/test_physical_ssz.py::TestPredictions::test_grid_shape PASSED
tests/test_physical_ssz.py::TestPredictions::test_range_is_finite PASSED
tests/test_physical_ssz.py::TestPhysicalParams::test_default_params PASSED
tests/test_physical_ssz.py::TestPhysicalParams::test_custom_params PASSED
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_extended_default PASSED
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_extended_height_effect PASSED
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_with_latitude PASSED
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_f_n_classical_diurnal PASSED
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_extended_mode_ratios PASSED
tests/test_t1_t4_implementation.py::TestT1ExtendedClassical::test_invalid_parameters PASSED
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_load_synthetic_data PASSED
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_schema_validation PASSED
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_synthetic_data_has_true_delta_seg PASSED
tests/test_t1_t4_implementation.py::TestT2DataLoader::test_get_frequency_dict PASSED
tests/test_t1_t4_implementation.py::TestT2Pipeline::test_pipeline_default_config PASSED
tests/test_t1_t4_implementation.py::TestT2Pipeline::test_pipeline_result_summary PASSED
tests/test_t1_t4_implementation.py::TestT2Pipeline::test_quick_analysis PASSED
tests/test_t1_t4_implementation.py::TestT3RealDataHooks::test_real_data_loader_not_implemented PASSED
tests/test_t1_t4_implementation.py::TestT3RealDataHooks::test_load_from_csv_path PASSED
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_compute_relative_shifts PASSED
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_check_mode_independence_ssz PASSED
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_check_mode_independence_dispersive PASSED
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_delta_seg_with_confidence PASSED
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_detect_dispersion_pattern PASSED
tests/test_t1_t4_implementation.py::TestT4Diagnostics::test_generate_diagnostic_report PASSED
tests/test_t1_t4_implementation.py::TestIntegration::test_full_workflow PASSED

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
================= 187 passed, 19 warnings, 1 error in 15.53s ==================

```


---

================================================================================
REPO: ssz-lagrange
Status: FAILED
Exit Code: 3
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

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

============================ no tests ran in 9.74s ============================

```

## STDERR (COMPLETE - NO TRUNCATION)

```
mainloop: caught unexpected SystemExit!

```


---

================================================================================
REPO: ssz-lensing
Status: SUCCESS
Exit Code: 0
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-lensing
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... ======================================================================
 EXTENDED LENS MODEL - COMPREHENSIVE TEST SUITE
======================================================================

Python: 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
NumPy:  2.0.2
collected 279 items

tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_determined_standard [Scan/Hypothesis Test mode (nonlinear search)]

[Scenario 1: Determined Standard]
  Path A residual: 0.100000
  Path B residual: 0.050000
  theta_E recovered: A=0.9823
PASSED
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_overdetermined [Scan/Hypothesis Test mode (nonlinear search)]

[Scenario 2: Overdetermined]
  Path A residual: 0.100000 (model check)
  Path B residual: 0.075000
  DOF info: DOF: OVERDETERMINED: +9 redundancy, 16C vs 7P
PASSED
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_underdetermined_high_mmax 
[Scenario 3: Underdetermined (high m_max)]
  Constraints: 8, Params: 12
  Regime: underdetermined
  Nullspace: 4 dimensions
  Path C notes: Nullspace: 4D, Solutions: 2
  Non-identifiable: ['theta_E', 'a_3', 'a_4', 'b_2', 'b_3']...
PASSED
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_rescue_with_source 
[Scenario 4: DOF Rescue]
  1 source: 8C vs 10P -> underdetermined
  2 sources: 16C vs 12P -> overdetermined
  Nullspace: 2 -> 0
PASSED
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_ill_conditioned 
[Scenario 5: Ill-Conditioned]
  Condition number: 1.00e+12
  Regime: ill_conditioned
  Recommendation: Run sensitivity analysis (perturb data, observe param changes)
PASSED
tests/test_comprehensive_analysis.py::TestScenarioSuite::test_scenario_phase_degeneracy [Scan/Hypothesis Test mode (nonlinear search)]

[Scenario 6: Phase Degeneracy]
  Phase points scanned: 10
  Min residual: 0.050000
  Points within 20%: 10
  Degeneracy hints: 2
PASSED
tests/test_comprehensive_analysis.py::TestPathConsistency::test_path_a_b_consistency [Scan/Hypothesis Test mode (nonlinear search)]

[Consistency: Path A vs B]
  theta_E (A): 0.982322
  theta_E (B): 1.000000
  Difference: 0.017678
PASSED
tests/test_comprehensive_analysis.py::TestPathConsistency::test_regime_matches_dof 
[Consistency: Regime vs DOF]
  8C vs 8P: determined (expected: determined)
  12C vs 8P: overdetermined (expected: overdetermined)
  6C vs 10P: underdetermined (expected: underdetermined)
PASSED
tests/test_datahub.py::TestSnapshotValidation::test_quad_snapshot_valid PASSED
tests/test_datahub.py::TestSnapshotValidation::test_ring_snapshot_valid PASSED
tests/test_datahub.py::TestSnapshotValidation::test_all_snapshots_valid PASSED
tests/test_datahub.py::TestQuadSnapshot::test_load_quad_positions PASSED
tests/test_datahub.py::TestQuadSnapshot::test_quad_has_redshifts PASSED
tests/test_datahub.py::TestQuadSnapshot::test_quad_no_nan PASSED
tests/test_datahub.py::TestQuadSnapshot::test_quad_no_inf PASSED
tests/test_datahub.py::TestQuadSnapshot::test_quad_has_theta_E PASSED
tests/test_datahub.py::TestRingSnapshot::test_load_ring_positions PASSED
tests/test_datahub.py::TestRingSnapshot::test_ring_has_redshifts PASSED
tests/test_datahub.py::TestRingSnapshot::test_ring_no_nan PASSED
tests/test_datahub.py::TestRingSnapshot::test_ring_no_inf PASSED
tests/test_datahub.py::TestFallbackByMode::test_quad_mode PASSED
tests/test_datahub.py::TestFallbackByMode::test_ring_mode PASSED
tests/test_datahub.py::TestFallbackByMode::test_arc_mode PASSED
tests/test_datahub.py::TestFallbackByMode::test_invalid_mode_raises PASSED
tests/test_datahub.py::TestDataQuality::test_quad_all_fields_from_source PASSED
tests/test_datahub.py::TestDataQuality::test_ring_all_fields_from_source PASSED
tests/test_datahub.py::TestDataQuality::test_available_datasets PASSED
tests/test_datahub.py::TestNoDefaultsNoNull::test_quad_complete_numeric PASSED
tests/test_datahub.py::TestNoDefaultsNoNull::test_ring_complete_numeric PASSED
tests/test_dual_path.py::TestSharedForwardModel::test_reduced_deflection_basic PASSED
tests/test_dual_path.py::TestSharedForwardModel::test_lens_equation_zero_residual PASSED
tests/test_dual_path.py::TestPathA_Algebraic::test_algebraic_solver_basic PASSED
tests/test_dual_path.py::TestPathA_Algebraic::test_phase_is_output_not_input PASSED
tests/test_dual_path.py::TestPathB_PhaseScan::test_scan_is_labeled PASSED
tests/test_dual_path.py::TestPathB_PhaseScan::test_scan_finds_candidates [Scan/Hypothesis Test mode (nonlinear search)]
PASSED
tests/test_dual_path.py::TestCrossCheck::test_dual_path_runs_both ============================================================
PATH A: Algebraic Components (No-Fit, CANONICAL)
============================================================
  theta_E = 2.020331
  Derived phi_2 = -0.7854 rad
  Max residual = 1.78e-15
  Status: PASS

============================================================
PATH B: Phase Scan Mode (Hypothesis Test)
============================================================
[Scan/Hypothesis Test mode (nonlinear search)]
WARNING: Scan phase (0.000) differs from algebraic (-0.785) by 0.785 rad
  Best phi_2 = 0.0000 rad
  Best residual = 5.54e-02
  DEGENERACY: 16 scan points within 10% of minimum
  HINT: 2-fold symmetry detected in residuals

----------------------------------------
CROSS-CHECK: Scan vs Algebraic
----------------------------------------
  Algebraic phi_2: -0.7854 rad
  Scan phi_2:      0.0000 rad
  Difference:      0.7854 rad
  Consistent:      NO
PASSED
tests/test_dual_path.py::TestCrossCheck::test_cross_check_reports_consistency ============================================================
PATH A: Algebraic Components (No-Fit, CANONICAL)
============================================================
  theta_E = 2.020331
  Derived phi_2 = -0.7854 rad
  Max residual = 1.78e-15
  Status: PASS

============================================================
PATH B: Phase Scan Mode (Hypothesis Test)
============================================================
[Scan/Hypothesis Test mode (nonlinear search)]
WARNING: Scan phase (0.000) differs from algebraic (-0.785) by 0.785 rad
  Best phi_2 = 0.0000 rad
  Best residual = 5.54e-02
  DEGENERACY: 32 scan points within 10% of minimum
  HINT: 2-fold symmetry detected in residuals

----------------------------------------
CROSS-CHECK: Scan vs Algebraic
----------------------------------------
  Algebraic phi_2: -0.7854 rad
  Scan phi_2:      0.0000 rad
  Difference:      0.7854 rad
  Consistent:      NO
PASSED
tests/test_extended_model.py::test_profiles 
======================================================================
 TEST 1: Radial Profile Functions
======================================================================

1a. SIS Profile (eta=2)
  theta=0.5: kappa=1.0000, alpha=1.0000
  theta=1.0: kappa=0.5000, alpha=1.0000
  theta=2.0: kappa=0.2500, alpha=1.0000

1b. Power-law Profile (variable eta)
  eta=1.5: kappa(theta_E)=0.7500, alpha(theta_E)=1.0000
  eta=2.0: kappa(theta_E)=0.5000, alpha(theta_E)=1.0000
  eta=2.5: kappa(theta_E)=0.2500, alpha(theta_E)=1.0000

1c. Cored Profile (r_core=0.1)
  theta=0.01: kappa_singular=inf, kappa_cored=4.9752
  theta=0.10: kappa_singular=5.00, kappa_cored=3.5355
  theta=1.00: kappa_singular=0.50, kappa_cored=0.4975

1d. Hermite C² Blending
  x=0.00: h(x)=0.0000
  x=0.25: h(x)=0.1035
  x=0.50: h(x)=0.5000
  x=0.75: h(x)=0.8965
  x=1.00: h(x)=1.0000

  [PASS] Profile functions work correctly
PASSED
tests/test_extended_model.py::test_external_shear 
======================================================================
 TEST 2: External Shear
======================================================================

  Shear: gamma=0.1, phi_gamma=30 deg
  (1.0, 0.0) -> alpha_shear = (0.0500, 0.0866)
  (0.0, 1.0) -> alpha_shear = (0.0866, -0.0500)
  (1.0, 1.0) -> alpha_shear = (0.1366, 0.0366)

  [PASS] External shear deflection correct
PASSED
tests/test_extended_model.py::test_higher_multipoles 
======================================================================
 TEST 3: Higher Multipoles (m=3, m=4)
======================================================================

3a. Octupole (m=3)
  phi=  0 deg: alpha_3 = (+0.0500, +0.0000)
  phi= 60 deg: alpha_3 = (-0.0250, -0.0433)
  phi=120 deg: alpha_3 = (-0.0250, +0.0433)
  phi=180 deg: alpha_3 = (+0.0500, +0.0000)

3b. Hexadecapole (m=4)
  phi=  0 deg: alpha_4 = (+0.0300, +0.0000)
  phi= 45 deg: alpha_4 = (-0.0212, -0.0212)
  phi= 90 deg: alpha_4 = (-0.0000, +0.0300)
  phi=135 deg: alpha_4 = (+0.0212, -0.0212)

  [PASS] Higher multipoles work correctly
PASSED
tests/test_extended_model.py::test_synthetic_recovery 
======================================================================
 TEST 4: Synthetic Data Parameter Recovery
======================================================================

True parameters:
  beta = (0.0500, 0.0300)
  theta_E = 1.0000
  a_2 = 0.0800, b_2 = 0.1200
  phi_2 = 25.0 deg

Generated 4 images:
  Image 1: (-0.707498, +0.436511) r=0.8313, phi=+148.3 deg
  Image 2: (+0.645968, -0.590471) r=0.8752, phi=-42.4 deg
  Image 3: (+0.751787, +0.933516) r=1.1986, phi=+51.2 deg
  Image 4: (-0.616692, -0.899615) r=1.0907, phi=-124.4 deg

Recovered parameters:
  beta = (0.0500, 0.0300)
  theta_E = 1.0000
  a_2 = -0.1147, b_2 = 0.0874
  phi_2 = 161.8 deg

Residuals:
  max|res| = 9.46e-14
  RMS      = 5.91e-14

  [PASS] Exact parameter recovery achieved
PASSED
tests/test_extended_model.py::test_model_with_shear 
======================================================================
 TEST 5: Model with External Shear
======================================================================

Model: Extended Model (m_max=2, eta=2.00+shear)
Unknowns: ['beta_x', 'beta_y', 'theta_E', 'gamma_ext', 'phi_gamma_ext', 'a_2', 'b_2', 'phi_2']
Nonlinear: ['phi_gamma_ext', 'phi_2']
Linear: ['beta_x', 'beta_y', 'theta_E', 'gamma_ext', 'a_2', 'b_2']

Total deflection at (0.8, 0.6):
  alpha = (0.8158, 0.7759)

  [PASS] Shear model structure correct
PASSED
tests/test_extended_model.py::test_real_lens_data 
======================================================================
 TEST 6: Real Lens Data with Extended Model
======================================================================

--------------------------------------------------
  Lens: Q2237+0305
  Note: Einstein Cross - bar structure (needs m=3)
--------------------------------------------------

  m_max=2: max|res|=0.0687 arcsec

  m_max=3: max|res|=0.0164 arcsec
           theta_E=0.913

  m_max=4: No solution found

  m=2+shear: max|res|=0.0498, gamma=0.4458

--------------------------------------------------
  Lens: HE0435-1223
  Note: Quad lens - good for m=2
--------------------------------------------------

  m_max=2: max|res|=0.0669 arcsec

  m_max=3: max|res|=0.0290 arcsec
           theta_E=1.193

  m_max=4: No solution found

  m=2+shear: max|res|=0.0214, gamma=0.6679

  [PASS] Real lens inversion completed
PASSED
tests/test_extended_model.py::test_comparison 
======================================================================
 TEST 7: Original vs Extended Model Comparison
======================================================================

Test images:
  1: (+0.95, +0.30)
  2: (-0.35, +0.92)
  3: (-0.88, -0.45)
  4: (+0.42, -0.90)

--- Original MultipoleModel (m=2) ---
  Skipped (import error: attempted relative import beyond top-level package)

--- Extended Model (m=2, no shear) ---
  max|res| = 0.0028
  theta_E = 0.9904

--- Extended Model (m=4, with shear) ---
  No solution

  [PASS] Model comparison completed
PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_assert_finite_valid PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_assert_finite_nan_raises PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_assert_finite_inf_raises PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_sanitize_no_nan_converts_nan_to_none PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_validate_no_nan_finds_issues PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_divide_zero PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_divide_valid PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_sqrt_negative PASSED
tests/test_fallback_no_nan.py::TestNoNaNUtilities::test_safe_sqrt_valid PASSED
tests/test_fallback_no_nan.py::TestFallbackQuad::test_load_quad_images_no_nan PASSED
tests/test_fallback_no_nan.py::TestFallbackQuad::test_load_quad_has_4_images PASSED
tests/test_fallback_no_nan.py::TestFallbackQuad::test_quad_has_redshift_info PASSED
tests/test_fallback_no_nan.py::TestFallbackQuad::test_quad_positions_finite PASSED
tests/test_fallback_no_nan.py::TestFallbackRing::test_load_ring_no_nan PASSED
tests/test_fallback_no_nan.py::TestFallbackRing::test_ring_has_multiple_points PASSED
tests/test_fallback_no_nan.py::TestFallbackRing::test_ring_has_redshift_info PASSED
tests/test_fallback_no_nan.py::TestFallbackRing::test_ring_positions_finite PASSED
tests/test_fallback_no_nan.py::TestFallbackByMode::test_load_quad_by_mode PASSED
tests/test_fallback_no_nan.py::TestFallbackByMode::test_load_ring_by_mode PASSED
tests/test_fallback_no_nan.py::TestFallbackByMode::test_invalid_mode_raises PASSED
tests/test_fallback_no_nan.py::TestAllFallbackDatasets::test_all_datasets_no_nan PASSED
tests/test_fallback_no_nan.py::TestAllFallbackDatasets::test_fallback_text_parseable PASSED
tests/test_lensing_run.py::TestNoNaNOutputs::test_cross_no_nan PASSED
tests/test_lensing_run.py::TestNoNaNOutputs::test_ring_no_nan PASSED
tests/test_lensing_run.py::TestCircleLabeling::test_sky_circle_is_theta_E PASSED
tests/test_lensing_run.py::TestCircleLabeling::test_lens_circle_is_b_E PASSED
tests/test_lensing_run.py::TestRotationPreservesRadii::test_rotation_invariant_radii PASSED
tests/test_lensing_run.py::TestGRSSZShiftConsistency::test_shift_equals_xi PASSED
tests/test_lensing_run.py::TestGRSSZShiftConsistency::test_xi_is_small_but_nonzero PASSED
tests/test_lensing_run.py::TestFallbackDatasetsLoad::test_cross_dataset_loads PASSED
tests/test_lensing_run.py::TestFallbackDatasetsLoad::test_ring_dataset_loads PASSED
tests/test_lensing_run.py::TestFallbackDatasetsLoad::test_no_fake_zeros PASSED
tests/test_lensing_run.py::TestPhysicalConsistency::test_distances_positive PASSED
tests/test_lensing_run.py::TestPhysicalConsistency::test_mass_reasonable PASSED
tests/test_lensing_run.py::TestPhysicalConsistency::test_schwarzschild_radius_small PASSED
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_gauge_no_nan PASSED
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_alpha_rsg_vs_ppn PASSED
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_delay_monotonic_vs_b PASSED
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_xi_to_zero_limit PASSED
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_phase_delay_relation PASSED
tests/test_lensing_run.py::TestCarmenPaperIntegrals::test_gauge_insets_render_data PASSED
tests/test_linear_model.py::test_dof_analysis ============================================================
 DOF ANALYSIS - Constraints vs Parameters
============================================================

Config                 Params Quad (8)                      
------------------------------------------------------------
m=2 only                    5 OVERDETERMINED (+3 redundant equations)
m=2 + shear                 7 OVERDETERMINED (+1 redundant equations)
m=2 + m=3                   7 OVERDETERMINED (+1 redundant equations)
m=2 + shear + m=3           9 UNDERDETERMINED (1 more data needed!)
m=2 + m=3 + m=4             9 UNDERDETERMINED (1 more data needed!)

PASSED
tests/test_linear_model.py::test_synthetic_recovery ============================================================
 SYNTHETIC DATA RECOVERY (Linear Model)
============================================================

Model: Linear Model (m_max=2)
Parameters: ['beta_x', 'beta_y', 'theta_E', 'c_2', 's_2']
N_params: 5
N_constraints: 8

Solution found:
  theta_E = 0.9846
  beta = (0.0043, 0.0069)
  c_2 = 0.0060
  s_2 = 0.0010

  max|res| = 2.23e-02
  consistency = 2.23e-02
  DOF: OVERDETERMINED (+3 redundant equations)

Physical parameters:
  amplitude_2 = 0.0061
  phase_2 = 4.7 deg

  [PASS] Inversion successful
PASSED
tests/test_linear_model.py::test_real_lens_data ============================================================
 REAL LENS DATA - Linear Model
============================================================

Einstein Cross (Q2237+0305):

  m=2         : max|res|=1.5896", theta_E=0.542, OVERDETERMINED (+3 redundant equations)
  m=2+shear   : max|res|=0.0416", theta_E=1.076, OVERDETERMINED (+1 redundant equations)
  m=3         : max|res|=0.0343", theta_E=1.104, OVERDETERMINED (+1 redundant equations)

  [PASS] Real lens inversion completed
PASSED
tests/test_linear_model.py::test_comparison_with_extended ============================================================
 COMPARISON: Linear vs Extended Model
============================================================

Linear Model (direct solve):
  theta_E = 0.9846
  max|res| = 2.23e-02

Extended Model (grid search):
  theta_E = 0.9904
  max|res| = 2.81e-03

Linear nonlinear_unknowns: []
Extended nonlinear_unknowns: ['phi_2']

  [PASS] Comparison completed
PASSED
tests/test_minimal_exact.py::TestLinearSolver::test_simple_2x2 PASSED
tests/test_minimal_exact.py::TestLinearSolver::test_identity PASSED
tests/test_minimal_exact.py::TestLinearSolver::test_singular_matrix PASSED
tests/test_minimal_exact.py::TestLinearSolver::test_near_singular PASSED
tests/test_minimal_exact.py::TestRootSolver::test_bisection_linear PASSED
tests/test_minimal_exact.py::TestRootSolver::test_bisection_quadratic PASSED
tests/test_minimal_exact.py::TestRootSolver::test_bisection_trig PASSED
tests/test_minimal_exact.py::TestRootSolver::test_find_all_roots PASSED
tests/test_minimal_exact.py::TestExactRecovery::test_standard_cross PASSED
tests/test_minimal_exact.py::TestExactRecovery::test_symmetric_cross PASSED
tests/test_minimal_exact.py::TestExactRecovery::test_asymmetric_cross PASSED
tests/test_minimal_exact.py::TestExactRecovery::test_varying_theta_E PASSED
tests/test_minimal_exact.py::TestMatrixRank::test_full_rank PASSED
tests/test_minimal_exact.py::TestMatrixRank::test_rank_deficient PASSED
tests/test_minimal_exact.py::TestMatrixRank::test_rectangular PASSED
tests/test_model_zoo.py::test_m2_allowed PASSED
tests/test_model_zoo.py::test_m2_shear_m3_forbidden PASSED
tests/test_model_zoo.py::test_arc_points_rescue PASSED
tests/test_model_zoo.py::test_multi_source_rescue PASSED
tests/test_model_zoo.py::test_shear_recovery PASSED
tests/test_model_zoo.py::test_m3_recovery PASSED
tests/test_model_zoo.py::test_zoo_comparison PASSED
tests/test_multi_source.py::TestDOFGatekeeper::test_overdetermined_allowed PASSED
tests/test_multi_source.py::TestDOFGatekeeper::test_exactly_determined_allowed PASSED
tests/test_multi_source.py::TestDOFGatekeeper::test_underdetermined_forbidden PASSED
tests/test_multi_source.py::TestDOFGatekeeper::test_max_params_single_source PASSED
tests/test_multi_source.py::TestDOFGatekeeper::test_max_params_two_sources PASSED
tests/test_multi_source.py::TestMultiSourceParams::test_phase_derived_from_components PASSED
tests/test_multi_source.py::TestMultiSourceParams::test_shear_phase_derived PASSED
tests/test_multi_source.py::TestMultiSourceBuilder::test_unknowns_single_source_m2 PASSED
tests/test_multi_source.py::TestMultiSourceBuilder::test_unknowns_two_sources_with_shear PASSED
tests/test_multi_source.py::TestMultiSourceBuilder::test_dof_blocks_underdetermined PASSED
tests/test_multi_source.py::TestMultiSourceRecovery::test_single_source_recovery PASSED
tests/test_multi_source.py::TestMultiSourceRecovery::test_two_source_shared_lens PASSED
tests/test_multi_source.py::TestMultiSourceRecovery::test_phase_is_output_not_input PASSED
tests/test_multi_source.py::TestDOFAnalysis::test_analyze_single_source PASSED
tests/test_multi_source.py::TestDOFAnalysis::test_analyze_forbidden_config PASSED
tests/test_multi_source.py::TestDOFAnalysis::test_analyze_multi_source_enables_more PASSED
tests/test_multipole_consistency.py::TestDoFCounting::test_minimal_model_4_images PASSED
tests/test_multipole_consistency.py::TestDoFCounting::test_underdetermined PASSED
tests/test_multipole_consistency.py::TestDoFCounting::test_multipole_m3 PASSED
tests/test_multipole_consistency.py::TestDoFCounting::test_image_multiplicity_quad PASSED
tests/test_multipole_consistency.py::TestMultipoleConsistency::test_m2_matches_minimal PASSED
tests/test_multipole_consistency.py::TestMultipoleConsistency::test_multipole_residuals PASSED
tests/test_multipole_consistency.py::TestMultipoleConsistency::test_phase_periodicity PASSED
tests/test_multipole_consistency.py::TestNumericalStability::test_small_quadrupole PASSED
tests/test_multipole_consistency.py::TestNumericalStability::test_large_offset PASSED
tests/test_multipole_consistency.py::TestNumericalStability::test_matrix_conditioning PASSED
tests/test_no_null_contract.py::TestIsNullOrNaN::test_none_is_null PASSED
tests/test_no_null_contract.py::TestIsNullOrNaN::test_nan_is_null PASSED
tests/test_no_null_contract.py::TestIsNullOrNaN::test_inf_is_null PASSED
tests/test_no_null_contract.py::TestIsNullOrNaN::test_empty_string_is_null PASSED
tests/test_no_null_contract.py::TestIsNullOrNaN::test_valid_number_not_null PASSED
tests/test_no_null_contract.py::TestIsNullOrNaN::test_valid_string_not_null PASSED
tests/test_no_null_contract.py::TestDictValidation::test_valid_dict_passes PASSED
tests/test_no_null_contract.py::TestDictValidation::test_null_detected PASSED
tests/test_no_null_contract.py::TestDictValidation::test_nested_null_detected PASSED
tests/test_no_null_contract.py::TestDictValidation::test_list_null_detected PASSED
tests/test_no_null_contract.py::TestDefaultSigma::test_quad_sigma_positive PASSED
tests/test_no_null_contract.py::TestDefaultSigma::test_ring_sigma_positive PASSED
tests/test_no_null_contract.py::TestDefaultSigma::test_single_point_fallback PASSED
tests/test_no_null_contract.py::TestFillUncertainties::test_all_defaults PASSED
tests/test_no_null_contract.py::TestFillUncertainties::test_partial_input PASSED
tests/test_no_null_contract.py::TestFullNumericPoints::test_creates_all_fields PASSED
tests/test_no_null_contract.py::TestFullNumericPoints::test_to_dict_no_null PASSED
tests/test_no_null_contract.py::TestNormalizedDistances::test_all_values_present PASSED
tests/test_no_null_contract.py::TestEstimates::test_center_estimate PASSED
tests/test_no_null_contract.py::TestEstimates::test_theta_E_estimate PASSED
tests/test_no_null_contract.py::TestAssertNoNullNoNaN::test_valid_dict_passes PASSED
tests/test_no_null_contract.py::TestAssertNoNullNoNaN::test_null_raises PASSED
tests/test_no_null_contract.py::TestAssertNoNullNoNaN::test_nan_raises PASSED
tests/test_no_null_contract.py::TestProvenanceSummary::test_counts_flags PASSED
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_quad_fallback_complete PASSED
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_ring_fallback_complete PASSED
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_quad_full_numeric_output PASSED
tests/test_no_null_contract.py::TestFallbackDatasetsComplete::test_ring_full_numeric_output PASSED
tests/test_no_null_contract.py::TestUserMinimalInput::test_4_points_no_uncertainties PASSED
tests/test_q2237_diagnostic.py::test_q2237_model_comparison 
==================================================
Q2237+0305 EINSTEIN CROSS DIAGNOSTIC
==================================================
m=2 only:     residual = 0.0081
m=2 + shear:  residual = 0.0065
m=2 + m=3:    residual = 0.0000
--------------------------------------------------
Improvement:  100.0%
PASSED
tests/test_q2237_diagnostic.py::test_q2237_forbidden_info PASSED
tests/test_q2237_diagnostic.py::test_q2237_full_report 
============================================================
MODEL ZOO COMPARISON
============================================================

m=2
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8, Params: 5
  DOF: 3
  Max Residual: 8.12e-03
  Condition: 5.63e+00

m=2 + shear
----------------------------------------
  Regime: STANDARD
  Constraints: 8, Params: 7
  DOF: 1
  Max Residual: 6.54e-03
  Condition: 6.96e+00

m=2 + m=3
----------------------------------------
  Regime: STANDARD
  Constraints: 8, Params: 7
  DOF: 1
  Max Residual: 5.55e-16
  Condition: inf

m=2 + shear + m=3
----------------------------------------
  Regime: FORBIDDEN
  Constraints: 8, Params: 9
  DOF: -1
  Status: FORBIDDEN (insufficient constraints)
    -> Add 1 flux ratio(s) (up to 3 available from 4 images)
    -> Add 1 time delay(s) (up to 3 available)
    -> Add 1 arc point(s) from extended emission (+2 constraints)
    -> Add second background source (if 4 images: +8 constraints, -2 params = +6 net)

============================================================
RANKING BY RESIDUAL
============================================================
  1. m=2 + m=3: 5.55e-16
  2. m=2 + shear: 6.54e-03
  3. m=2: 8.12e-03
PASSED
tests/test_radial_scaling_gauge.py::test_scaling_factor_definition PASSED
tests/test_radial_scaling_gauge.py::test_scaling_weak_field_limit PASSED
tests/test_radial_scaling_gauge.py::test_time_dilation_relation PASSED
tests/test_radial_scaling_gauge.py::test_effective_wavenumber PASSED
tests/test_radial_scaling_gauge.py::test_local_light_speed_invariant PASSED
tests/test_radial_scaling_gauge.py::test_shapiro_delay_cassini PASSED
tests/test_radial_scaling_gauge.py::test_shapiro_delay_solar_grazing PASSED
tests/test_radial_scaling_gauge.py::test_shapiro_xi_vs_ppn_factor PASSED
tests/test_radial_scaling_gauge.py::test_solar_limb_deflection PASSED
tests/test_radial_scaling_gauge.py::test_deflection_xi_vs_ppn_factor PASSED
tests/test_radial_scaling_gauge.py::test_gaia_deflection_precision PASSED
tests/test_radial_scaling_gauge.py::test_wkb_phase_scaling PASSED
tests/test_radial_scaling_gauge.py::test_interferometer_phase_difference PASSED
tests/test_radial_scaling_gauge.py::test_frame_consistency_loop_closure PASSED
tests/test_radial_scaling_gauge.py::test_coordinate_independence PASSED
tests/test_radial_scaling_gauge.py::test_pound_rebka_experiment PASSED
tests/test_radial_scaling_gauge.py::test_gps_time_drift PASSED
tests/test_radial_scaling_gauge.py::test_tokyo_skytree_clocks PASSED
tests/test_real_data.py::test_synthetic_exact 
======================================================================
TEST 1: Synthetic Data - Exact Recovery
======================================================================

True parameters:
  theta_E  = 1.0
  a        = 0.05
  b        = 0.15
  beta     = 0.08
  phi_beta = 30.0 deg
  phi_gamma = 20.0 deg

Generated 4 images:
  Image 1: (+1.046139, +0.424824)
  Image 2: (-0.558158, +0.767785)
  Image 3: (-0.932323, -0.274345)
  Image 4: (+0.088239, -0.918860)

Recovered parameters:
  theta_E   = 1.000000000000
  a         = 0.050000000000
  b         = -0.150000000000
  beta      = 0.080000000000
  phi_gamma = 20.000000000000 deg

  Max |residual| = 1.67e-16

Recovery errors:
  theta_E: 1.11e-16
  a: 2.08e-17
  b: 1.11e-16
  beta: 5.55e-17
  phi_gamma: 1.67e-16

>>> TEST 1 STATUS: PASS
PASSED
tests/test_real_data.py::test_synthetic_random 
======================================================================
TEST 2: Random Parameter Sweep (50 configurations)
======================================================================

Results:
  Configurations tested: 50
  Successful inversions: 47
  Success rate: 94.0%

  Max |residual| statistics:
    Mean:   2.35e-03
    Median: 7.77e-16
    Max:    6.32e-02

  Max parameter error statistics:
    Mean:   6.54e-03
    Max:    1.70e-01

>>> TEST 2 STATUS: PARTIAL
PASSED
tests/test_real_data.py::test_real_data 
======================================================================
TEST 3: Real Observational Data
======================================================================

------------------------------------------------------------
Real Lens: Q2237+0305 (Einstein Cross)
Source: CASTLES survey, Schneider et al. 1988
z_lens = 0.0394, z_source = 1.695
------------------------------------------------------------

Image positions (arcsec):
  A: (+0.758, +0.964)  r=1.226  theta=+51.8 deg
  B: (-0.869, +0.541)  r=1.024  theta=+148.1 deg
  C: (-0.634, -0.797)  r=1.018  theta=-128.5 deg
  D: (+0.674, -0.618)  r=0.914  theta=-42.5 deg

Recovered parameters:
  theta_E   = 1.0770 arcsec
  a         = 0.0454
  b         = -0.4663
  beta      = 0.1040 arcsec
  phi_gamma = 51.7 deg

  Max |residual| = 0.1031 arcsec

  Residuals per image (arcsec):
    A: x=+0.0000, y=-0.0000  |r|=0.0000
    B: x=+0.0000, y=+0.0000  |r|=0.0000
    C: x=+0.0000, y=+0.0000  |r|=0.0000
    D: x=+0.1031, y=-0.0465  |r|=0.1131

  Model adequacy: POOR (residuals >> measurement error, model may be inadequate)
  (astrometric error ~ 0.003 arcsec)

------------------------------------------------------------
Real Lens: B1608+656 (B1608+656)
Source: CASTLES survey, Fassnacht et al. 1996
z_lens = 0.6304, z_source = 1.394
------------------------------------------------------------

Image positions (arcsec):
  A: (+0.738, +1.961)  r=2.095  theta=+69.4 deg
  B: (-0.745, +1.354)  r=1.545  theta=+118.8 deg
  C: (-1.128, -0.599)  r=1.277  theta=-152.0 deg
  D: (+1.128, -0.213)  r=1.148  theta=-10.7 deg

Recovered parameters:
  theta_E   = 1.4217 arcsec
  a         = 0.7120
  b         = -0.0000
  beta      = 0.0000 arcsec
  phi_gamma = 78.8 deg

  Max |residual| = 0.4305 arcsec

  Residuals per image (arcsec):
    A: x=+0.0000, y=+0.0000  |r|=0.0000
    B: x=-0.0000, y=+0.0000  |r|=0.0000
    C: x=+0.0000, y=-0.0000  |r|=0.0000
    D: x=-0.4305, y=+0.0813  |r|=0.4381

  Model adequacy: POOR (residuals >> measurement error, model may be inadequate)
  (astrometric error ~ 0.003 arcsec)

------------------------------------------------------------
Real Lens: HE0435-1223 (HE0435-1223)
Source: COSMOGRAIL, Wisotzki et al. 2002
z_lens = 0.4546, z_source = 1.693
------------------------------------------------------------

Image positions (arcsec):
  A: (+1.272, +0.306)  r=1.308  theta=+13.5 deg
  B: (-0.277, +1.148)  r=1.181  theta=+103.6 deg
  C: (-1.332, -0.152)  r=1.341  theta=-173.5 deg
  D: (+0.294, -1.306)  r=1.339  theta=-77.3 deg

Recovered parameters:
  theta_E   = 1.2619 arcsec
  a         = 0.0642
  b         = 0.1486
  beta      = 0.0244 arcsec
  phi_gamma = 10.2 deg

  Max |residual| = 0.1138 arcsec

  Residuals per image (arcsec):
    A: x=+0.0000, y=+0.0000  |r|=0.0000
    B: x=+0.0000, y=-0.0000  |r|=0.0000
    C: x=+0.0000, y=+0.0000  |r|=0.0000
    D: x=-0.0563, y=+0.1138  |r|=0.1270

  Model adequacy: POOR (residuals >> measurement error, model may be inadequate)
  (astrometric error ~ 0.003 arcsec)

------------------------------------------------------------
Real Lens: PG1115+080 (PG1115+080)
Source: CASTLES survey, Weymann et al. 1980
z_lens = 0.311, z_source = 1.722
------------------------------------------------------------

Image positions (arcsec):
  A: (+0.948, +0.795)  r=1.237  theta=+40.0 deg
  B: (+1.071, +0.538)  r=1.199  theta=+26.7 deg
  C: (-1.093, -0.260)  r=1.123  theta=-166.6 deg
  D: (-0.213, -1.018)  r=1.040  theta=-101.8 deg

Recovered parameters:
  theta_E   = 1.0265 arcsec
  a         = 0.2139
  b         = -0.0000
  beta      = 0.0000 arcsec
  phi_gamma = 44.9 deg

  Max |residual| = 0.0700 arcsec

  Residuals per image (arcsec):
    A: x=+0.0000, y=+0.0000  |r|=0.0000
    B: x=+0.0000, y=+0.0000  |r|=0.0000
    C: x=+0.0000, y=-0.0000  |r|=0.0000
    D: x=-0.0146, y=-0.0700  |r|=0.0715

  Model adequacy: POOR (residuals >> measurement error, model may be inadequate)
  (astrometric error ~ 0.003 arcsec)

============================================================
Real Data Summary: 4/4 systems inverted
============================================================

>>> TEST 3 STATUS: PASS
PASSED
tests/test_real_data.py::test_noise_sensitivity 
======================================================================
TEST 4: Noise Sensitivity Analysis
======================================================================

Noise level (arcsec) | Max |residual| | theta_E error | Status
-----------------------------------------------------------------
             0e+00 |        1.67e-16 |      1.11e-16 | EXACT
             1e-05 |        2.23e-05 |      1.11e-05 | GOOD
             1e-04 |        3.64e-05 |      3.56e-05 | GOOD
             1e-03 |        8.75e-04 |      1.07e-04 | GOOD
             1e-02 |        3.94e-02 |      1.13e-02 | MARGINAL
             5e-02 |        9.45e-03 |      4.62e-02 | GOOD

>>> TEST 4 STATUS: COMPLETE
PASSED
tests/test_real_inversion.py::TestMorphologyClassifier::test_quad_classification QUAD test: 4 points with 4 azimuthal clusters: Einstein Cross configuration
PASSED
tests/test_real_inversion.py::TestMorphologyClassifier::test_ring_classification RING test: Extended emission (n=20), low radial scatter (0.012), high coverage (95.0%): Ring
PASSED
tests/test_real_inversion.py::TestMorphologyClassifier::test_double_classification DOUBLE test: 2 points: Double-image system (source outside caustic)
PASSED
tests/test_real_inversion.py::TestMorphologyClassifier::test_criteria_are_explicit Criteria: {'is_4_points': True, 'is_2_points': False, 'is_many_points': False, 'low_radial_scatter': np.True_, 'high_azimuthal_coverage': np.True_, 'small_max_gap': np.False_, 'has_4_clusters': np.True_, 'has_2_clusters': np.False_}
PASSED
tests/test_real_inversion.py::TestSourceConsistency::test_consistent_sources Source scatter: 0.057370
Max deviation: 0.057370
PASSED
tests/test_real_inversion.py::TestQuadInversion::test_synthetic_recovery Generated 2 images, need 4 for quad test
PASSED
tests/test_real_inversion.py::TestQuadInversion::test_model_comparison Generated 2 images, skipping
PASSED
tests/test_real_inversion.py::TestLinearSystem::test_system_dimensions System shape: A=(8, 5), b=(8,)
Parameters: ['beta_x', 'beta_y', 'theta_E', 'c2', 's2']
PASSED
tests/test_real_inversion.py::TestLinearSystem::test_overdetermined_system Regime: ill_conditioned (expected: overdetermined or determined)
PASSED
tests/test_regime_explorer.py::test_regime_determined PASSED
tests/test_regime_explorer.py::test_regime_overdetermined PASSED
tests/test_regime_explorer.py::test_regime_underdetermined PASSED
tests/test_regime_explorer.py::test_regime_ill_conditioned PASSED
tests/test_regime_explorer.py::test_underdetermined_multiple_solutions PASSED
tests/test_regime_explorer.py::test_underdetermined_param_ranges PASSED
tests/test_regime_explorer.py::test_underdetermined_non_identifiable PASSED
tests/test_regime_explorer.py::test_high_mmax_underdetermined PASSED
tests/test_regime_explorer.py::test_dof_rescue_multisource PASSED
tests/test_regime_explorer.py::test_recommendations_change PASSED
tests/test_ui_state.py::TestDatasetState::test_empty_state PASSED
tests/test_ui_state.py::TestDatasetState::test_to_dict PASSED
tests/test_ui_state.py::TestDatasetState::test_from_dict PASSED
tests/test_ui_state.py::TestParseUserPoints::test_parse_quad PASSED
tests/test_ui_state.py::TestParseUserPoints::test_parse_ring PASSED
tests/test_ui_state.py::TestParseUserPoints::test_wrong_count_quad PASSED
tests/test_ui_state.py::TestParseUserPoints::test_invalid_line PASSED
tests/test_ui_state.py::TestBuildUserDataset::test_build_quad PASSED
tests/test_ui_state.py::TestBuildUserDataset::test_build_with_redshifts PASSED
tests/test_ui_state.py::TestLoadFallbackDataset::test_load_quad PASSED
tests/test_ui_state.py::TestLoadFallbackDataset::test_load_ring PASSED
tests/test_ui_state.py::TestValidateDataset::test_valid_quad PASSED
tests/test_ui_state.py::TestValidateDataset::test_empty_fails PASSED
tests/test_ui_state.py::TestValidateDataset::test_wrong_mode_count PASSED
tests/test_ui_state.py::TestValidateDataset::test_nan_fails PASSED
tests/test_ui_state.py::TestValidationReport::test_valid_report PASSED
tests/test_ui_state.py::TestValidationReport::test_invalid_report PASSED
tests/test_ui_state.py::TestDatasetSummary::test_summary_valid PASSED
tests/test_ui_state.py::TestDatasetSummary::test_summary_invalid PASSED
tests/test_ui_state.py::TestRunState::test_default PASSED
tests/test_ui_state.py::TestRunState::test_to_from_dict PASSED
tests/test_validation_lab.py::test_UT1 PASSED
tests/test_validation_lab.py::test_UT2 PASSED
tests/test_validation_lab.py::test_UT3 PASSED
tests/test_validation_lab.py::test_ST1 PASSED
tests/test_validation_lab.py::test_ST2 PASSED
tests/test_validation_lab.py::test_ST3 PASSED
tests/test_validation_lab.py::test_CM1 [Scan/Hypothesis Test mode (nonlinear search)]
PASSED
tests/test_validation_lab.py::test_RB1 PASSED
tests/test_validation_lab.py::test_RB2 [Scan/Hypothesis Test mode (nonlinear search)]
PASSED
tests/test_validation_module.py::test_image_validation ==================================================
TEST: Image Validation
==================================================
VALID: 4 images, 8 constraints
Valid: True
Constraints: 8
[PASS]
PASSED
tests/test_validation_module.py::test_dof_analysis 
==================================================
TEST: DOF Analysis
==================================================

DOF Analysis for 4-image system:
------------------------------------------------------------
Model             Params   Constr    DOF Status              
------------------------------------------------------------
m2_only                5        8      3 OVERDETERMINED      
m2_shear               7        8      1 OVERDETERMINED      
m2_m3                  7        8      1 OVERDETERMINED      
m2_shear_m3            9        8     -1 UNDERDETERMINED     
m2_m3_m4               9        8     -1 UNDERDETERMINED     
------------------------------------------------------------

Auto-selected: m2_only
Status: OVERDETERMINED
DOF: 3
[PASS]
PASSED
tests/test_validation_module.py::test_result_interpretation 
==================================================
TEST: Result Interpretation
==================================================
Model: Linear m=2
DOF: OVERDETERMINED (3)
max|res|: 0.0200 arcsec
RMS: 0.0150 arcsec
Converged: True

Quality: MARGINAL
Residual/Noise: 6.7x
Interpretation: Residuals significantly above noise
Model adequate: True
[PASS]
PASSED
tests/test_validation_module.py::test_model_comparison 
==================================================
TEST: Model Comparison
==================================================
Model Comparison:
----------------------------------------
  m=2 only: max|res|=0.0500"
  m=2 + shear: max|res|=0.0200" <-- WINNER
----------------------------------------
Winner: m=2 + shear
Reason: Best residual: 0.0200"
[PASS]
PASSED
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_shear_data_shear_wins 
Shear data: m=2 residual=0.0213, m=2+shear residual=0.0135
PASSED
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_m3_data_m3_wins 
m=3 data: m=2 residual=0.0257, m=2+m=3 residual=0.0000
PASSED
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_full_model_forbidden_without_extras 
Full model: regime=FORBIDDEN
PASSED
tests/zoo/test_derivation_chain.py::TestDerivationChain::test_report_shows_derivation 
============================================================
DERIVATION CHAIN REPORT
============================================================
ObservablesBundle: report_test
  Sources: 1
  Total images: 4
  Total constraints: 8


[Step 1] m=2 only
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 5
  Max Residual: 1.7978e-02

[Step 2] m=2 + shear
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 7
  Max Residual: 1.5629e-03
  Improvement: 91.3% vs previous

[Step 3] m=2 + m=3
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 7
  Max Residual: 8.8818e-16
  Improvement: 100.0% vs previous

[Step 4] m=2 + shear + m=3
----------------------------------------
  Regime: FORBIDDEN
  Constraints: 8
  Parameters: 9
  Status: FORBIDDEN
    -> Need 1 more constraint(s)
    -> Options: flux ratios, time delays, arc points, or multi-source

============================================================
SUMMARY
============================================================
Best model: m=2 + m=3
Best residual: 8.8818e-16

FORBIDDEN models (need more observables):
  - m=2 + shear + m=3
      Need 1 more constraint(s)
      Options: flux ratios, time delays, arc points, or multi-source
PASSED
tests/zoo/test_derivation_chain.py::TestForbiddenToAllowed::test_arc_points_rescue_full_model 
With arc points: regime=OVERDETERMINED, constraints=14
PASSED
tests/zoo/test_derivation_chain.py::TestForbiddenToAllowed::test_multi_source_rescue_full_model 
With 2 sources: constraints=16, params=11
PASSED
tests/zoo/test_derivation_chain.py::TestRegression::test_basic_m2_still_works PASSED
tests/zoo/test_derivation_chain.py::TestRegression::test_bundle_backward_compatible PASSED
tests/zoo/test_geometry.py::TestTriadScene::test_create_standard_scene PASSED
tests/zoo/test_geometry.py::TestTriadScene::test_scene_distances PASSED
tests/zoo/test_geometry.py::TestTriadScene::test_add_multiple_sources PASSED
tests/zoo/test_geometry.py::TestProjection::test_project_single_source PASSED
tests/zoo/test_geometry.py::TestProjection::test_projection_tracer PASSED
tests/zoo/test_geometry.py::TestProjection::test_forward_backward_consistency 
Original beta: [ 0.1  -0.05]
Mean recovered beta: [ 0.0494316  -0.02356355]
Beta spread: [0.02629109 0.04803551]
PASSED
tests/zoo/test_geometry.py::TestSerialization::test_to_dict_and_back PASSED
tests/zoo/test_geometry.py::TestSerialization::test_json_roundtrip PASSED
tests/zoo/test_geometry.py::TestVisualization::test_visualizer_smoke_test PASSED
tests/zoo/test_geometry.py::TestVisualization::test_ascii_scene_output 
==================================================
SCENE: ascii_test
==================================================

Observer [O] -----> Lens [L] -----> Source(s) [S]
         z=0        z=1.00

3D Positions:
  Observer: (0, 0, 0)
  Lens:     (0.000, 0.000, 1.000)
  Source_0: (0.200, -0.100, 2.000)

Projected to Lens Plane:
  Source 0: beta = (0.1000, -0.0500)

Distances:
  D_L  = 1.000
  D_S  = 2.000
  D_LS = 1.000
PASSED
tests/zoo/test_m4_extension.py::TestM4Models::test_derivation_chain_includes_m4 PASSED
tests/zoo/test_m4_extension.py::TestM4Models::test_m4_data_m4_model_works 
m4 model: regime=OVERDETERMINED
PASSED
tests/zoo/test_m4_extension.py::TestM4Models::test_full_chain_report 
============================================================
DERIVATION CHAIN REPORT
============================================================
ObservablesBundle: full_chain
  Sources: 1
  Total images: 4
  Total constraints: 8


[Step 1] m=2 only
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 5
  Max Residual: 2.1615e-02

[Step 2] m=2 + shear
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 7
  M...
PASSED
tests/zoo/test_m4_extension.py::TestRealDataPipeline::test_list_available_systems 
Available systems: ['Q2237+0305']
PASSED
tests/zoo/test_m4_extension.py::TestRealDataPipeline::test_load_q2237 PASSED
tests/zoo/test_m4_extension.py::TestRealDataPipeline::test_q2237_derivation_chain 
============================================================
DERIVATION CHAIN REPORT
============================================================
ObservablesBundle: Q2237+0305
  Sources: 1
  Total images: 4
  Total constraints: 8


[Step 1] m=2 only
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 5
  Max Residual: 8.1155e-03

[Step 2] m=2 + shear
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 7
  Max Residual: 6.5393e-03
  Improvement: 19.4% vs previous

[Step 3] m=2 + m=3
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 7
  Max Residual: 5.5511e-16
  Improvement: 100.0% vs previous

[Step 4] m=2 + shear + m=3
----------------------------------------
  Regime: FORBIDDEN
  Constraints: 8
  Parameters: 9
  Status: FORBIDDEN
    -> Need 1 more constraint(s)
    -> Options: flux ratios, time delays, arc points, or multi-source

[Step 5] m=2 + m=4
----------------------------------------
  Regime: OVERDETERMINED
  Constraints: 8
  Parameters: 7
  Max Residual: 5.5511e-16

[Step 6] m=2 + shear + m=4
----------------------------------------
  Regime: FORBIDDEN
  Constraints: 8
  Parameters: 9
  Status: FORBIDDEN
    -> Need 1 more constraint(s)
    -> Options: flux ratios, time delays, arc points, or multi-source

[Step 7] m=2 + m=3 + m=4
----------------------------------------
  Regime: FORBIDDEN
  Constraints: 8
  Parameters: 9
  Status: FORBIDDEN
    -> Need 1 more constraint(s)
    -> Options: flux ratios, time delays, arc points, or multi-source

[Step 8] m=2 + shear + m=3 + m=4 (maximal)
----------------------------------------
  Regime: FORBIDDEN
  Constraints: 8
  Parameters: 11
  Status: FORBIDDEN
    -> Need 3 more constraint(s)
    -> Options: flux ratios, time delays, arc points, or multi-source

============================================================
SUMMARY
============================================================
Best model: m=2 + m=3
Best residual: 5.5511e-16

FORBIDDEN models (need more observables):
  - m=2 + shear + m=3
      Need 1 more constraint(s)
      Options: flux ratios, time delays, arc points, or multi-source
  - m=2 + shear + m=4
      Need 1 more constraint(s)
      Options: flux ratios, time delays, arc points, or multi-source
  - m=2 + m=3 + m=4
      Need 1 more constraint(s)
      Options: flux ratios, time delays, arc points, or multi-source
  - m=2 + shear + m=3 + m=4 (maximal)
      Need 3 more constraint(s)
      Options: flux ratios, time delays, arc points, or multi-source
PASSED
tests/zoo/test_m4_extension.py::TestArtifacts::test_save_artifacts PASSED
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_perfect_ring_classified_as_ring 
Perfect Ring Analysis:
  Morphology: ring
  Confidence: 0.81
  Radial scatter: 0.0094
  Azimuthal coverage: 0.98
  Recommended: ['isotropic']
PASSED
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_shear_ring_detected 
Shear Ring Analysis:
  Morphology: unknown
  m2 amplitude: 0.0563
  Recommended: ['m2', 'm2+shear']
PASSED
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_quad_classified_as_quad 
Quad Analysis:
  Morphology: quad
  Confidence: 0.90
  Azimuthal coverage: 0.73
  Recommended: ['m2', 'm2+shear']
PASSED
tests/zoo/test_ring_morphology.py::TestMorphologyClassifier::test_ring_to_cross_transition 
Ring -> Cross Transition:
  c2=0.00: ring, scatter=0.012, m2=0.001
  c2=0.05: ring, scatter=0.037, m2=0.025
  c2=0.10: unknown, scatter=0.068, m2=0.048
  c2=0.20: unknown, scatter=0.143, m2=0.101
  c2=0.30: unknown, scatter=0.210, m2=0.148
PASSED
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_perfect_ring_fit 
Ring Fit Result:
  Radius: 1.4984 (expected 1.5)
  Center: (0.0015, -0.0024)
  RMS residual: 0.0046
  Perturbation: isotropic
PASSED
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_perturbed_ring_detects_m2 
Perturbed Ring (m=2):
  m2 amplitude: 0.0992
  m4 amplitude: 0.0004
  Perturbation: quadrupole (m=2)
PASSED
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_m4_perturbation_detected 
Perturbed Ring (m=4):
  m2 amplitude: 0.0013
  m4 amplitude: 0.0794
  Perturbation: hexadecapole (m=4)
PASSED
tests/zoo/test_ring_morphology.py::TestRingAnalyzer::test_off_center_ring 
Off-Center Ring:
  True center: (0.2, -0.1)
  Found center: (0.1998, -0.0997)
PASSED
tests/zoo/test_ring_morphology.py::TestCenterEstimation::test_estimate_ring_center 
Center Estimation:
  True: (0.1, -0.05)
  Estimated: (0.0998, -0.0501)
PASSED
tests/zoo/test_ring_morphology.py::TestCenterEstimation::test_estimate_ring_radius 
Radius Estimation:
  True: 1.2
  Estimated: 1.2000
PASSED

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
====================== 279 passed, 63 warnings in 10.77s ======================

```


---

================================================================================
REPO: Unified-Results
Status: SUCCESS
Exit Code: 0
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results
configfile: pyproject.toml
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... 
================================================================================
Test Two Shells Alpha One
================================================================================
Physical Meaning:
  • Velocity propagates as v_k = v_(k-1) × q_k^(-alpha/2)
================================================================================

================================================================================
Test Two Shells Alpha One
================================================================================
Physical Meaning:
  • Velocity propagates as v_k = v_(k-1) × q_k^(-alpha/2)
================================================================================

================================================================================
Test Two Shells Alpha One
================================================================================
Physical Meaning:
  • Velocity propagates as v_k = v_(k-1) × q_k^(-alpha/2)
================================================================================
collected 78 items

tests/cosmos/test_multi_body_sigma.py::test_two_body_sigma_superposition 
================================================================================
TWO-BODY SEGMENT DENSITY SUPERPOSITION
================================================================================
Test Configuration:
  Body A: Position = (0.0, 0.0, 0.0) m
          Mass = 5.972e+24 kg (1 M Earth)
  Body B: Position = (0.5, 0.0, 0.0) m
          Mass = 5.972e+24 kg (1 M Earth)
  Test point: (1.0, 0.0, 0.0) m

Segment Density sigma:
  Body A only:  sigma_A = 1.145715e-03
  Body B only:  sigma_B = 1.145715e-03
  Combined:     sigma_total = 2.291431e-03
  Sum A+B:      sigma_A + sigma_B = 2.291431e-03

Superposition Check:
  sigma_total approx sigma_A + sigma_B: True
  Relative difference: 0.00%

Physical Interpretation:
  • Segment fields add linearly (superposition)
  • Consistent with weak-field GR limit
  • Both bodies contribute to spacetime structure
  • No non-linear effects at this scale
================================================================================
PASSED
tests/test_print_all_md.py::test_print_all_md_basic PASSED
tests/test_print_all_md.py::test_print_all_md_depth_order PASSED
tests/test_print_all_md.py::test_print_all_md_exclude_dirs PASSED
tests/test_print_all_md.py::test_print_all_md_size_limit PASSED
tests/test_print_all_md.py::test_print_all_md_no_files PASSED
tests/test_print_all_md.py::test_print_all_md_custom_includes PASSED
tests/test_ring_datasets.py::test_ring_dataset_completeness[data/observations/G79_29+0_46_CO_NH3_rings.csv-10-Star-forming Region] 
================================================================================
RING DATASET VALIDATION: G79_29+0_46_CO_NH3_rings
================================================================================
Category: Star-forming Region
File: data/observations/G79_29+0_46_CO_NH3_rings.csv

Dataset Properties:
  Rings found: 10
  Expected rings: 10
  Columns: ring, radius_pc, T, n, v_obs...

Physical Interpretation:
  ✅ Sufficient rings for inter-ring analysis
  ✅ Can validate growth statistics
  ✅ Can test temperature/velocity gradients
================================================================================
PASSED
tests/test_ring_datasets.py::test_ring_dataset_completeness[data/observations/CygnusX_DiamondRing_CII_rings.csv-3-Molecular Cloud] 
================================================================================
RING DATASET VALIDATION: CygnusX_DiamondRing_CII_rings
================================================================================
Category: Molecular Cloud
File: data/observations/CygnusX_DiamondRing_CII_rings.csv

Dataset Properties:
  Rings found: 3
  Expected rings: 3
  Columns: ring, radius_pc, T, n, v_obs...

Physical Interpretation:
  ✅ Sufficient rings for inter-ring analysis
  ✅ Can validate growth statistics
  ✅ Can test temperature/velocity gradients
================================================================================
PASSED
tests/test_ring_datasets.py::test_ring_growth_statistics[data/observations/G79_29+0_46_CO_NH3_rings.csv-10-Star-forming Region] 
================================================================================
RING GROWTH: G79_29+0_46_CO_NH3_rings
================================================================================
Category: Star-forming Region
Rings: 10

Radius Growth Statistics:
  Mean Δr: 0.178 pc
  Min Δr: 0.150 pc
  Max Δr: 0.200 pc
  All positive: True

Physical Interpretation:
  • Radius increases monotonically outward
  • Expanding shell/ring structure
  • No unphysical radius inversions
================================================================================
PASSED
tests/test_ring_datasets.py::test_ring_growth_statistics[data/observations/CygnusX_DiamondRing_CII_rings.csv-3-Molecular Cloud] 
================================================================================
RING GROWTH: CygnusX_DiamondRing_CII_rings
================================================================================
Category: Molecular Cloud
Rings: 3

Radius Growth Statistics:
  Mean Δr: 0.150 pc
  Min Δr: 0.150 pc
  Max Δr: 0.150 pc
  All positive: True

Physical Interpretation:
  • Radius increases monotonically outward
  • Expanding shell/ring structure
  • No unphysical radius inversions
================================================================================
PASSED
tests/test_ring_datasets.py::test_temperature_gradient[data/observations/G79_29+0_46_CO_NH3_rings.csv-10-Star-forming Region] 
================================================================================
TEMPERATURE GRADIENT: G79_29+0_46_CO_NH3_rings
================================================================================
Category: Star-forming Region
Rings: 10

Temperature Statistics:
  Inner ring: 78.0 K
  Outer ring: 20.0 K
  Total change: -58.0 K
  Mean gradient: -6.44 K/ring

Physical Interpretation:
  • Temperature decreases outward (cooling)
  • Consistent with expanding shell physics
  • Or shielding in molecular cloud
================================================================================
PASSED
tests/test_ring_datasets.py::test_temperature_gradient[data/observations/CygnusX_DiamondRing_CII_rings.csv-3-Molecular Cloud] 
================================================================================
TEMPERATURE GRADIENT: CygnusX_DiamondRing_CII_rings
================================================================================
Category: Molecular Cloud
Rings: 3

Temperature Statistics:
  Inner ring: 48.0 K
  Outer ring: 36.0 K
  Total change: -12.0 K
  Mean gradient: -6.00 K/ring

Physical Interpretation:
  • Temperature decreases outward (cooling)
  • Consistent with expanding shell physics
  • Or shielding in molecular cloud
================================================================================
PASSED
tests/test_ring_datasets.py::test_velocity_profile[data/observations/G79_29+0_46_CO_NH3_rings.csv-10-Star-forming Region] 
================================================================================
VELOCITY PROFILE: G79_29+0_46_CO_NH3_rings
================================================================================
Category: Star-forming Region
Rings: 10

Velocity Statistics:
  Inner ring: 14.50 km/s
  Outer ring: 1.00 km/s
  Mean velocity: 4.94 km/s
  Velocity range: 1.00 - 14.50 km/s

Velocity Profile:
  Type: Decreasing velocity
  Interpretation: Momentum-conserving expansion

Physical Interpretation:
  • Expansion dynamics validated
  • Velocity structure consistent with Star-forming Region
================================================================================
PASSED
tests/test_ring_datasets.py::test_velocity_profile[data/observations/CygnusX_DiamondRing_CII_rings.csv-3-Molecular Cloud] 
================================================================================
VELOCITY PROFILE: CygnusX_DiamondRing_CII_rings
================================================================================
Category: Molecular Cloud
Rings: 3

Velocity Statistics:
  Inner ring: 1.30 km/s
  Outer ring: 1.30 km/s
  Mean velocity: 1.30 km/s
  Velocity range: 1.30 - 1.30 km/s

Velocity Profile:
  Type: Constant expansion
  Interpretation: Pressure-driven expansion

Physical Interpretation:
  • Expansion dynamics validated
  • Velocity structure consistent with Molecular Cloud
================================================================================
PASSED
tests/test_ring_datasets.py::test_tracer_documentation[data/observations/G79_29+0_46_CO_NH3_rings.csv-10-Star-forming Region] 
================================================================================
TRACER DOCUMENTATION: G79_29+0_46_CO_NH3_rings
================================================================================
Category: Star-forming Region
Rings: 10

Molecular Tracers Used:
  • 1)
  • 2)
  • CO(1-0)
  • CO(2-1)
  • CO(3-2)
  • HI
  • NH3(1
  • NH3(2
  • [CII]158um

Physical Interpretation:
  ✅ Data provenance documented
  ✅ Multiple tracers provide robust constraints
  ✅ Can cross-check consistency
================================================================================
PASSED
tests/test_ring_datasets.py::test_tracer_documentation[data/observations/CygnusX_DiamondRing_CII_rings.csv-3-Molecular Cloud] 
================================================================================
TRACER DOCUMENTATION: CygnusX_DiamondRing_CII_rings
================================================================================
Category: Molecular Cloud
Rings: 3

Molecular Tracers Used:
  • CO(1-0)
  • [C II]158um

Physical Interpretation:
  ✅ Data provenance documented
  ✅ Multiple tracers provide robust constraints
  ✅ Can cross-check consistency
================================================================================
PASSED
tests/test_ring_datasets.py::test_multi_ring_catalog_exists 
================================================================================
MULTI-RING CATALOG DOCUMENTATION
================================================================================
Catalog file: data\observations\MULTI_RING_CATALOG.md
Size: 4154 bytes

Physical Interpretation:
  ✅ All multi-ring datasets documented
  ✅ Source papers referenced
  ✅ Quality assessment included
================================================================================
PASSED
tests/test_segwave_cli.py::TestCLIBasic::test_help_flag PASSED
tests/test_segwave_cli.py::TestCLIBasic::test_missing_required_args PASSED
tests/test_segwave_cli.py::TestCLIBasic::test_invalid_csv_path PASSED
tests/test_segwave_cli.py::TestCLIExecution::test_fixed_alpha_execution PASSED
tests/test_segwave_cli.py::TestCLIExecution::test_fit_alpha_execution PASSED
tests/test_segwave_cli.py::TestCLIExecution::test_frequency_tracking PASSED
tests/test_segwave_cli.py::TestCLIExecution::test_custom_exponents PASSED
tests/test_segwave_cli.py::TestCLIValidation::test_negative_v0 PASSED
tests/test_segwave_cli.py::TestCLIValidation::test_mutually_exclusive_alpha PASSED
tests/test_segwave_cli.py::TestBundledDatasets::test_g79_dataset_exists PASSED
tests/test_segwave_cli.py::TestBundledDatasets::test_cygx_dataset_exists PASSED
tests/test_segwave_cli.py::TestBundledDatasets::test_sources_json_exists PASSED
tests/test_segwave_cli.py::TestBundledDatasets::test_sources_config_yaml_exists PASSED
tests/test_segwave_cli.py::TestBundledDatasets::test_load_sources_config_function PASSED
tests/test_segwave_cli.py::TestBundledDatasets::test_g79_cli_smoke_run PASSED
tests/test_segwave_cli.py::TestBundledDatasets::test_cygx_cli_smoke_run PASSED
tests/test_segwave_core.py::TestQFactor::test_temperature_only_basic 
================================================================================
Q-FACTOR: Temperature Ratio (beta=1)
================================================================================
Configuration:
  Current ring: T_curr = 80.0 K
  Previous ring: T_prev = 100.0 K
  Beta parameter: beta = 1.0

Q-Factor Calculation:
  q_k = (T_curr/T_prev)^beta = (80.0/100.0)^1.0 = 0.800000

Physical Interpretation:
  q_k < 1 indicates cooling between rings
  Energy ratio = 80.0% of previous ring
  Velocity will scale as q_k^(-alpha/2)
================================================================================
PASSED
tests/test_segwave_core.py::TestQFactor::test_temperature_with_beta 
================================================================================
Q-FACTOR: Temperature with β=2 (Enhanced Sensitivity)
================================================================================
Configuration:
  T_curr = 80.0 K, T_prev = 100.0 K
  β = 2.0 (enhanced temperature sensitivity)

Calculation:
  q_k = (80.0/100.0)^2.0 = 0.640000
  Compare to β=1: 0.800000

Physical Interpretation:
  • β=2 amplifies temperature effect: 0.64 vs 0.80
  • Stronger cooling yields lower q_k
  • Results in more dramatic velocity changes
================================================================================
PASSED
tests/test_segwave_core.py::TestQFactor::test_temperature_and_density 
================================================================================
Q-FACTOR: Temperature AND Density Combined
================================================================================
Configuration:
  Temperature: 80.0 K → 100.0 K
  Density: 1.0e+05 → 2.0e+05 cm⁻³
  β = 1.0, η = 0.5

Calculation:
  q_T = (80.0/100.0)^1.0 = 0.800000
  q_n = (1e+05/2e+05)^0.5 = 0.707107
  q_k = q_T × q_n = 0.565685

Physical Interpretation:
  • Both cooling AND density drop reduce q_k
  • Combined effect: q_k = 0.566 < 0.8 (temperature only)
  • Density amplifies temperature effect
================================================================================
PASSED
tests/test_segwave_core.py::TestQFactor::test_invalid_temperature_raises PASSED
tests/test_segwave_core.py::TestQFactor::test_invalid_density_raises PASSED
tests/test_segwave_core.py::TestVelocityProfile::test_single_shell 
================================================================================
SINGLE RING: Initial Condition
================================================================================
Configuration:
  Ring 1: T = 100.0 K
  Initial velocity: v₀ = 10.0 km/s
  α parameter: 1.0

Calculation:
  q_1 = 1.0 (no prior ring, baseline)
  v_1 = v₀ × q_1^(-α/2) = 10.0 × 1.0 = 10.0 km/s

Predicted:
  q_k = 1.000000
  v_pred = 10.00 km/s

Physical Interpretation:
  • First ring sets baseline: v = v₀
  • No propagation yet (needs ≥2 rings)
  • This establishes initial conditions for chain
================================================================================
PASSED
tests/test_segwave_core.py::TestVelocityProfile::test_two_shells_alpha_one 
================================================================================
SSZ RING VELOCITY: Two-Shell Propagation
================================================================================
Configuration:
  Ring 1: T = 100.0 K, v = 10.0 km/s (initial)
  Ring 2: T = 80.0 K
  α parameter: 1.0

Velocity Propagation:
  q_2 = T_2/T_1 = 80.0/100.0 = 0.800000
  v_2 = v_1 × q_2^(-α/2)
  v_2 = 10.0 × 0.800000^(-0.5)
  v_2 = 11.1803 km/s

Predicted Velocity:
  v_pred(ring 2) = 11.1803 km/s

Physical Interpretation:
  • Cooler ring → Higher velocity (11.1803 > 10.0)
  • SSZ predicts velocity increase of 11.8%
  • Consistent with flat rotation curves
================================================================================
PASSED
tests/test_segwave_core.py::TestVelocityProfile::test_deterministic_chain 
================================================================================
5-RING CHAIN: Temperature Gradient
================================================================================
Ring Evolution:
  Ring 1: T = 100.0 K, q_k = 1.0000, v = 12.50 km/s
  Ring 2: T =  90.0 K, q_k = 0.9000, v = 13.18 km/s
  Ring 3: T =  80.0 K, q_k = 0.8889, v = 13.98 km/s
  Ring 4: T =  70.0 K, q_k = 0.8750, v = 14.94 km/s
  Ring 5: T =  60.0 K, q_k = 0.8571, v = 16.14 km/s

Velocity Evolution:
  v_initial = 12.50 km/s
  v_final = 16.14 km/s
  Total increase: 29.1%

Physical Interpretation:
  • Cooling trend: T drops 40 K over 5 rings
  • Velocity amplification: 29.1% increase
  • Monotonic rise consistent with flat rotation curves
================================================================================
PASSED
tests/test_segwave_core.py::TestVelocityProfile::test_alpha_zero_constant_velocity 
================================================================================
α=0 LIMIT: No Segmentation (Classical)
================================================================================
Configuration:
  α = 0.0 (no SSZ effect)
  Temperature varies: 100 → 60 K

Velocities:
  Ring 1: T = 100.0 K, v = 15.00 km/s
  Ring 2: T =  80.0 K, v = 15.00 km/s
  Ring 3: T =  60.0 K, v = 15.00 km/s

Physical Interpretation:
  • α=0 ⇒ No segment field contribution
  • All velocities = 15.0 km/s (constant)
  • Classical limit: temperature has no effect
  • This is what GR/Newtonian gravity predicts
================================================================================
PASSED
tests/test_segwave_core.py::TestVelocityProfile::test_with_density 
================================================================================
TEMPERATURE + DENSITY: Combined Effect
================================================================================
Configuration:
  β = 1.0 (temperature exponent)
  η = 0.3 (density exponent)
  α = 1.0

Ring Evolution:
  Ring 1: T = 100.0 K, n = 1.0e+05 cm⁻³, v = 10.00 km/s
  Ring 2: T =  90.0 K, n = 8.0e+04 cm⁻³, v = 10.90 km/s
  Ring 3: T =  80.0 K, n = 6.0e+04 cm⁻³, v = 12.07 km/s

Physical Interpretation:
  • Both T and n decrease across rings
  • Combined q_k = (T_k/T_prev)^β × (n_k/n_prev)^η
  • Density drop amplifies temperature effect
  • Results in stronger velocity increase
================================================================================
PASSED
tests/test_segwave_core.py::TestVelocityProfile::test_mismatched_lengths_raises PASSED
tests/test_segwave_core.py::TestFrequencyTrack::test_single_gamma 
================================================================================
FREQUENCY REDSHIFT: Single γ
================================================================================
Input: ν_in = 1.000e+12 Hz (1 THz)
Segment field: γ = 2.0

Redshift:
  ν_out = ν_in × γ^(-1/2)
  ν_out = 7.071e+11 Hz
  Redshift z = Δν/ν = 0.414

Physical Interpretation:
  • Photons lose energy in segment field
  • Observable as spectral line shift
  • Analogous to gravitational redshift
================================================================================
PASSED
tests/test_segwave_core.py::TestFrequencyTrack::test_frequency_decreases_with_gamma 
================================================================================
FREQUENCY EVOLUTION: γ Sequence
================================================================================
Input: ν_in = 1.000e+12 Hz

Frequency vs γ:
  γ = 1.0 → ν = 1.000e+12 Hz
  γ = 1.2 → ν = 9.129e+11 Hz
  γ = 1.5 → ν = 8.165e+11 Hz
  γ = 2.0 → ν = 7.071e+11 Hz

Monotonicity:
  All Δν < 0: True

Physical Interpretation:
  • Frequency decreases monotonically
  • Higher γ → More segment density → More redshift
================================================================================
PASSED
tests/test_segwave_core.py::TestFrequencyTrack::test_invalid_gamma_raises PASSED
tests/test_segwave_core.py::TestResiduals::test_perfect_match 
================================================================================
RESIDUALS: Perfect Match
================================================================================
Predicted: [10. 11. 12.]
Observed:  [10. 11. 12.]

Metrics:
  MAE (Mean Absolute Error): 0.000000
  RMSE (Root Mean Square Error): 0.000000
  Max |residual|: 0.000000

Physical Interpretation:
  • Perfect model fit: all errors = 0
  • SSZ theory exactly reproduces observations
================================================================================
PASSED
tests/test_segwave_core.py::TestResiduals::test_systematic_bias 
================================================================================
RESIDUALS: Systematic Bias
================================================================================
Predicted: [10. 11. 12.]
Observed:  [ 9. 10. 11.]
Bias: 1.0 km/s (constant)

Metrics:
  MAE: 1.000000
  RMSE: 1.000000
  Max |residual|: 1.000000

Physical Interpretation:
  • Consistent +1 km/s over-prediction
  • Could indicate calibration offset
  • Easily corrected by shifting v0
================================================================================
PASSED
tests/test_segwave_core.py::TestResiduals::test_mixed_residuals 
================================================================================
RESIDUALS: Mixed Over/Under Prediction
================================================================================
Predicted: [10.  11.5 12. ]
Observed:  [10.5 11.  12.5]
Residuals: [-0.5  0.5 -0.5]

Metrics:
  MAE: 0.500000
  RMSE: 0.500000
  Max |residual|: 0.500000

Physical Interpretation:
  • Alternating over/under predictions
  • No systematic bias (errors cancel)
  • RMS captures scatter: ±0.5 km/s
  • Random noise in measurements
================================================================================
PASSED
tests/test_segwave_core.py::TestCumulativeGamma::test_constant_q 
================================================================================
CUMULATIVE γ: Constant q = 1.5
================================================================================
q sequence: [1.  1.5 1.5 1.5]

Cumulative γ:
  γ_1 = 1.0000 (= 1.5^0)
  γ_2 = 1.5000 (= 1.5^1)
  γ_3 = 2.2500 (= 1.5^2)
  γ_4 = 3.3750 (= 1.5^3)

Physical Interpretation:
  • γ grows exponentially with constant q > 1
  • Each step multiplies by factor 1.5
  • Segment field accumulates over multiple rings
================================================================================
PASSED
tests/test_segwave_core.py::TestCumulativeGamma::test_all_ones 
================================================================================
CUMULATIVE γ: All q = 1 (No Change)
================================================================================
q sequence: [1. 1. 1. 1. 1.]
γ sequence: [1. 1. 1. 1. 1.]

Physical Interpretation:
  • q=1 everywhere → no temperature/density changes
  • γ=1 for all rings → no segment field accumulation
  • Isothermal, homogeneous medium
================================================================================
PASSED
tests/test_segwave_core.py::TestCumulativeGamma::test_increasing_sequence 
================================================================================
CUMULATIVE γ: Increasing Sequence
================================================================================
q sequence: [1.  1.2 1.1 1.3]

γ Evolution:
  Step 1: q = 1.0, γ_cum = 1.0000
  Step 2: q = 1.2, γ_cum = 1.2000
  Step 3: q = 1.1, γ_cum = 1.3200
  Step 4: q = 1.3, γ_cum = 1.7160

Monotonicity:
  All Δγ > 0: True

Physical Interpretation:
  • All q > 1 → energy/temperature rising
  • γ accumulates monotonically
  • Heating trend amplifies segment field
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestPPNParameters::test_ppn_beta_equals_one 
================================================================================
PPN PARAMETER β (Preferred-Frame)
================================================================================
Calculated β:  1.000000000000
GR prediction: 1.000000000000
Difference:    0.00e+00

Physical Interpretation:
  β = 1 → No preferred reference frame
  β = 1 → SSZ matches GR in weak gravitational fields
  β = 1 → Compatible with solar system observations
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestPPNParameters::test_ppn_gamma_equals_one 
================================================================================
PPN PARAMETER γ (Space Curvature)
================================================================================
Calculated γ:  1.000000000000
GR prediction: 1.000000000000
Difference:    0.00e+00

Physical Interpretation:
  γ = 1 → Light bending matches GR
  γ = 1 → Shapiro time delay matches GR
  γ = 1 → Gravitational lensing matches observations
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestNaturalBoundary::test_natural_boundary_radius[Sun] 
================================================================================
NATURAL BOUNDARY: Sun
================================================================================
Object: Our Sun - reference star
Mass:   1.988e+30 kg (1.00e+00 M_☉)

Radii:
  Schwarzschild r_s: 2.953e+03 m
  Natural r_φ:       2.389e+03 m
  Ratio r_φ/r_s:     0.809017 = φ/2
  φ value:           1.6180339887

Physical Interpretation:
  • Sun has a natural boundary at r_φ = 2.389e+03 m
  • Segment density saturates at this radius
  • No mathematical singularity - energy remains finite
  • Information is preserved at the boundary surface
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestNaturalBoundary::test_natural_boundary_radius[SgrA*] 
================================================================================
NATURAL BOUNDARY: SgrA*
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Mass:   8.544e+36 kg (4.30e+06 M_☉)

Radii:
  Schwarzschild r_s: 1.269e+10 m
  Natural r_φ:       1.027e+10 m
  Ratio r_φ/r_s:     0.809017 = φ/2
  φ value:           1.6180339887

Physical Interpretation:
  • SgrA* has a natural boundary at r_φ = 1.027e+10 m
  • Segment density saturates at this radius
  • No mathematical singularity - energy remains finite
  • Information is preserved at the boundary surface
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestNaturalBoundary::test_natural_boundary_radius[M87*] 
================================================================================
NATURAL BOUNDARY: M87*
================================================================================
Object: M87* - supermassive black hole, first to be imaged by EHT
Mass:   1.293e+40 kg (6.50e+09 M_☉)

Radii:
  Schwarzschild r_s: 1.920e+13 m
  Natural r_φ:       1.553e+13 m
  Ratio r_φ/r_s:     0.809017 = φ/2
  φ value:           1.6180339887

Physical Interpretation:
  • M87* has a natural boundary at r_φ = 1.553e+13 m
  • Segment density saturates at this radius
  • No mathematical singularity - energy remains finite
  • Information is preserved at the boundary surface
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[1.1-Earth] 
================================================================================
DUAL VELOCITIES: Earth at r = 1.1r_s
================================================================================
Object: Earth - our planet
Mass:   5.972e+24 kg
Radius: r = 9.757e-03 m (1.1r_s)

Velocities:
  Escape velocity v_esc:  2.858409e+08 m/s (0.953463c)
  Infall velocity v_fall: 3.144250e+08 m/s (1.048809c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         0.000e+00

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[1.1-Sun] 
================================================================================
DUAL VELOCITIES: Sun at r = 1.1r_s
================================================================================
Object: Our Sun - reference star
Mass:   1.988e+30 kg
Radius: r = 3.249e+03 m (1.1r_s)

Velocities:
  Escape velocity v_esc:  2.858409e+08 m/s (0.953463c)
  Infall velocity v_fall: 3.144250e+08 m/s (1.048809c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         1.780e-16

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[1.1-SgrA*] 
================================================================================
DUAL VELOCITIES: SgrA* at r = 1.1r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Mass:   8.544e+36 kg
Radius: r = 1.396e+10 m (1.1r_s)

Velocities:
  Escape velocity v_esc:  2.858409e+08 m/s (0.953463c)
  Infall velocity v_fall: 3.144250e+08 m/s (1.048809c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         1.780e-16

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[2.0-Earth] 
================================================================================
DUAL VELOCITIES: Earth at r = 2.0r_s
================================================================================
Object: Earth - our planet
Mass:   5.972e+24 kg
Radius: r = 1.774e-02 m (2.0r_s)

Velocities:
  Escape velocity v_esc:  2.119853e+08 m/s (0.707107c)
  Infall velocity v_fall: 4.239706e+08 m/s (1.414214c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         1.780e-16

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[2.0-Sun] 
================================================================================
DUAL VELOCITIES: Sun at r = 2.0r_s
================================================================================
Object: Our Sun - reference star
Mass:   1.988e+30 kg
Radius: r = 5.907e+03 m (2.0r_s)

Velocities:
  Escape velocity v_esc:  2.119853e+08 m/s (0.707107c)
  Infall velocity v_fall: 4.239706e+08 m/s (1.414214c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         1.780e-16

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[2.0-SgrA*] 
================================================================================
DUAL VELOCITIES: SgrA* at r = 2.0r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Mass:   8.544e+36 kg
Radius: r = 2.538e+10 m (2.0r_s)

Velocities:
  Escape velocity v_esc:  2.119853e+08 m/s (0.707107c)
  Infall velocity v_fall: 4.239706e+08 m/s (1.414214c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         1.780e-16

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[5.0-Earth] 
================================================================================
DUAL VELOCITIES: Earth at r = 5.0r_s
================================================================================
Object: Earth - our planet
Mass:   5.972e+24 kg
Radius: r = 4.435e-02 m (5.0r_s)

Velocities:
  Escape velocity v_esc:  1.340713e+08 m/s (0.447214c)
  Infall velocity v_fall: 6.703563e+08 m/s (2.236068c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         0.000e+00

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[5.0-Sun] 
================================================================================
DUAL VELOCITIES: Sun at r = 5.0r_s
================================================================================
Object: Our Sun - reference star
Mass:   1.988e+30 kg
Radius: r = 1.477e+04 m (5.0r_s)

Velocities:
  Escape velocity v_esc:  1.340713e+08 m/s (0.447214c)
  Infall velocity v_fall: 6.703563e+08 m/s (2.236068c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         0.000e+00

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[5.0-SgrA*] 
================================================================================
DUAL VELOCITIES: SgrA* at r = 5.0r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Mass:   8.544e+36 kg
Radius: r = 6.345e+10 m (5.0r_s)

Velocities:
  Escape velocity v_esc:  1.340713e+08 m/s (0.447214c)
  Infall velocity v_fall: 6.703563e+08 m/s (2.236068c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         0.000e+00

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[10.0-Earth] 
================================================================================
DUAL VELOCITIES: Earth at r = 10.0r_s
================================================================================
Object: Earth - our planet
Mass:   5.972e+24 kg
Radius: r = 8.870e-02 m (10.0r_s)

Velocities:
  Escape velocity v_esc:  9.480270e+07 m/s (0.316228c)
  Infall velocity v_fall: 9.480270e+08 m/s (3.162278c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         0.000e+00

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[10.0-Sun] 
================================================================================
DUAL VELOCITIES: Sun at r = 10.0r_s
================================================================================
Object: Our Sun - reference star
Mass:   1.988e+30 kg
Radius: r = 2.953e+04 m (10.0r_s)

Velocities:
  Escape velocity v_esc:  9.480270e+07 m/s (0.316228c)
  Infall velocity v_fall: 9.480270e+08 m/s (3.162278c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         0.000e+00

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestDualVelocities::test_dual_velocity_invariant[10.0-SgrA*] 
================================================================================
DUAL VELOCITIES: SgrA* at r = 10.0r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Mass:   8.544e+36 kg
Radius: r = 1.269e+11 m (10.0r_s)

Velocities:
  Escape velocity v_esc:  9.480270e+07 m/s (0.316228c)
  Infall velocity v_fall: 9.480270e+08 m/s (3.162278c)

Invariant Check:
  Product v_esc × v_fall: 8.987552e+16 m²/s²
  Target c²:              8.987552e+16 m²/s²
  Relative error:         0.000e+00

Physical Interpretation:
  • Rest energy: E_rest = m × v_esc × v_fall = mc²
  • Energy conservation holds exactly
  • Mass-energy equivalence is preserved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestEnergyConditions::test_energy_conditions_real_object[1.2-SgrA*] 
================================================================================
ENERGY CONDITIONS: SgrA* at r = 1.2r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Radius: r = 1.523e+10 m (1.2r_s)

Effective Stress-Energy Components:
  Energy density ρ:     -5.957276e-23 kg/m³
  Radial pressure p_r:  5.957276e-23 Pa
  Tangential pressure p_⊥: -1.191360e-22 Pa

Energy Conditions:
  WEC (Weak):      ✗ FAIL - ρ≥0 and ρ+p≥0
  DEC (Dominant):  ✗ FAIL - ρ≥|p|
  SEC (Strong):    ✗ FAIL - ρ+p+2p_⊥≥0
  NEC check: ρ+p_r = 0.000e+00 (should be ~0)

Physical Interpretation:
  • At r = 1.2r_s, strong field regime
  • Some conditions may not hold near r_φ
  • Natural boundary prevents singularity
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestEnergyConditions::test_energy_conditions_real_object[2.0-SgrA*] 
================================================================================
ENERGY CONDITIONS: SgrA* at r = 2.0r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Radius: r = 2.538e+10 m (2.0r_s)

Effective Stress-Energy Components:
  Energy density ρ:     -1.544126e-24 kg/m³
  Radial pressure p_r:  1.544126e-24 Pa
  Tangential pressure p_⊥: -6.182404e-24 Pa

Energy Conditions:
  WEC (Weak):      ✗ FAIL - ρ≥0 and ρ+p≥0
  DEC (Dominant):  ✗ FAIL - ρ≥|p|
  SEC (Strong):    ✗ FAIL - ρ+p+2p_⊥≥0
  NEC check: ρ+p_r = 0.000e+00 (should be ~0)

Physical Interpretation:
  • At r = 2.0r_s, strong field regime
  • Some conditions may not hold near r_φ
  • Natural boundary prevents singularity
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestEnergyConditions::test_energy_conditions_real_object[5.0-SgrA*] 
================================================================================
ENERGY CONDITIONS: SgrA* at r = 5.0r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Radius: r = 6.345e+10 m (5.0r_s)

Effective Stress-Energy Components:
  Energy density ρ:     1.027770e-25 kg/m³
  Radial pressure p_r:  -1.027770e-25 Pa
  Tangential pressure p_⊥: 5.469989e-26 Pa

Energy Conditions:
  WEC (Weak):      ✓ PASS - ρ≥0 and ρ+p≥0
  DEC (Dominant):  ✓ PASS - ρ≥|p|
  SEC (Strong):    ✓ PASS - ρ+p+2p_⊥≥0
  NEC check: ρ+p_r = 0.000e+00 (should be ~0)

Physical Interpretation:
  • At r = 5.0r_s, all conditions satisfied
  • Effective matter behaves physically
  • No exotic matter required
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestEnergyConditions::test_energy_conditions_real_object[10.0-SgrA*] 
================================================================================
ENERGY CONDITIONS: SgrA* at r = 10.0r_s
================================================================================
Object: Sagittarius A* - supermassive black hole at galactic center
Radius: r = 1.269e+11 m (10.0r_s)

Effective Stress-Energy Components:
  Energy density ρ:     9.388286e-27 kg/m³
  Radial pressure p_r:  -9.388286e-27 Pa
  Tangential pressure p_⊥: 8.190600e-27 Pa

Energy Conditions:
  WEC (Weak):      ✓ PASS - ρ≥0 and ρ+p≥0
  DEC (Dominant):  ✓ PASS - ρ≥|p|
  SEC (Strong):    ✓ PASS - ρ+p+2p_⊥≥0
  NEC check: ρ+p_r = 0.000e+00 (should be ~0)

Physical Interpretation:
  • At r = 10.0r_s, all conditions satisfied
  • Effective matter behaves physically
  • No exotic matter required
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestRealDataIntegration::test_load_real_data 
================================================================================
REAL ASTRONOMICAL DATA
================================================================================
Loaded 427 astronomical objects

Data columns: case, category, M_solar, a_m, e, P_year, T0_year, f_true_deg, z, f_emit_Hz, f_obs_Hz, lambda_emit_nm, lambda_obs_nm, v_los_mps, v_tot_mps, z_geom_hint, N0, source, r_emit_m, n_round

Physical Interpretation:
  • Real data validates SSZ predictions
  • Masses span 12 orders of magnitude
  • Perfect mass reconstruction achieved
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestMetricProperties::test_metric_continuity[Sun] 
================================================================================
METRIC CONTINUITY: Sun
================================================================================

Radius r = 2.0r_s:
  A(r):        0.5500000000
  A'(r) ≈      8.041744e-05
  |A_right - A_left|: 9.500000e-07

Radius r = 5.0r_s:
  A(r):        0.8152000000
  A'(r) ≈      1.181036e-05
  |A_right - A_left|: 3.488000e-07

Radius r = 10.0r_s:
  A(r):        0.9044000000
  A'(r) ≈      3.108346e-06
  |A_right - A_left|: 1.836000e-07

Physical Interpretation:
  • Metric is smooth and continuous
  • Gravitational field is well-defined
  • No unphysical discontinuities
================================================================================
PASSED
tests/test_ssz_real_data_comprehensive.py::TestMetricProperties::test_metric_continuity[SgrA*] 
================================================================================
METRIC CONTINUITY: SgrA*
================================================================================

Radius r = 2.0r_s:
  A(r):        0.5500000000
  A'(r) ≈      1.871479e-11
  |A_right - A_left|: 9.500000e-07

Radius r = 5.0r_s:
  A(r):        0.8152000000
  A'(r) ≈      2.748513e-12
  |A_right - A_left|: 3.488000e-07

Radius r = 10.0r_s:
  A(r):        0.9044000000
  A'(r) ≈      7.233758e-13
  |A_right - A_left|: 1.836000e-07

Physical Interpretation:
  • Metric is smooth and continuous
  • Gravitational field is well-defined
  • No unphysical discontinuities
================================================================================
PASSED
================================================================================
SEGMENTED SPACETIME TEST SUITE SUMMARY
================================================================================

Theoretical Framework:
  • φ-based segment density corrections to GR
  • Natural boundary at r_φ = (φ/2)r_s
  • PPN parameters: β = γ = 1 (matches GR in weak field)
  • Dual velocity invariant: v_esc × v_fall = c²

Validation Results:
  ✓ PPN parameters match GR
  ✓ Natural boundary prevents singularities
  ✓ Dual velocity invariant holds to machine precision
  ✓ Energy conditions satisfied (r ≥ 5r_s)
  ✓ Metric is C¹ continuous

Physical Predictions:
  • Black holes have finite surface at r_φ
  • Information is preserved
  • Singularity paradox is resolved
  • Hawking radiation emerges naturally

© 2025 Carmen Wrede, Lino Casu
Anti-Capitalist Software License (v 1.4)
================================================================================



============================= 78 passed in 50.48s =============================

```


---

================================================================================
REPO: ssz-trajectories
Status: SUCCESS
Exit Code: 0
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\ssz-trajectories
configfile: pyproject.toml
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 63 items

tests/test_analysis.py::TestAnalyzeOrbit::test_small_b_jumps PASSED
tests/test_analysis.py::TestAnalyzeOrbit::test_b50_jumps PASSED
tests/test_analysis.py::TestAnalyzeOrbit::test_b80_jumps PASSED
tests/test_analysis.py::TestAnalyzeOrbit::test_large_b_no_jumps PASSED
tests/test_analysis.py::TestAnalyzeOrbit::test_phi_total_positive PASSED
tests/test_analysis.py::TestAnalyzeOrbit::test_r_range PASSED
tests/test_analysis.py::TestDeflection::test_is_dphi_minus_pi PASSED
tests/test_analysis.py::TestDeflection::test_positive_deep_orbit PASSED
tests/test_analysis.py::TestDeflection::test_increases_below_barrier PASSED
tests/test_analysis.py::TestBridgeIdentity::test_exact_at_all_radii PASSED
tests/test_analysis.py::TestBridgeIdentity::test_components PASSED
tests/test_analysis.py::TestProperLength::test_finite_to_boundary PASSED
tests/test_analysis.py::TestProperLength::test_positive PASSED
tests/test_analysis.py::TestTortoise::test_finite_no_horizon PASSED
tests/test_embedding.py::TestXLocal::test_at_rs_strong PASSED
tests/test_embedding.py::TestXLocal::test_far_field_weak PASSED
tests/test_embedding.py::TestXLocal::test_monotone_decreasing_outward_blend PASSED
tests/test_embedding.py::TestNLevel::test_N1_at_rs PASSED
tests/test_embedding.py::TestNLevel::test_N0_far PASSED
tests/test_embedding.py::TestEpsilon::test_range PASSED
tests/test_embedding.py::TestCountJumps::test_no_jumps PASSED
tests/test_embedding.py::TestCountJumps::test_one_jump PASSED
tests/test_embedding.py::TestCountJumps::test_two_jumps PASSED
tests/test_embedding.py::TestCountJumps::test_empty PASSED
tests/test_embedding.py::TestCountJumps::test_single PASSED
tests/test_integrator.py::TestRK4Scalar::test_exponential_decay PASSED
tests/test_integrator.py::TestRK4Scalar::test_linear_growth PASSED
tests/test_integrator.py::TestTrapz::test_constant PASSED
tests/test_integrator.py::TestTrapz::test_linear PASSED
tests/test_integrator.py::TestTrapz::test_reversed_limits PASSED
tests/test_integrator.py::TestNullRadial::test_outgoing_monotone PASSED
tests/test_integrator.py::TestNullRadial::test_ingoing_monotone PASSED
tests/test_integrator.py::TestNullRadial::test_speed_bounded PASSED
tests/test_integrator.py::TestTimeLikeInfall::test_monotone_decrease PASSED
tests/test_integrator.py::TestTimeLikeInfall::test_reaches_boundary PASSED
tests/test_integrator.py::TestNullGeodesic::test_small_b_two_jumps PASSED
tests/test_integrator.py::TestNullGeodesic::test_large_b_no_jumps PASSED
tests/test_integrator.py::TestNullGeodesic::test_turning_point PASSED
tests/test_integrator.py::TestNullGeodesic::test_phi_increases PASSED
tests/test_integrator.py::TestTurningPoint::test_exists_for_small_b PASSED
tests/test_integrator.py::TestTurningPoint::test_turning_point_condition PASSED
tests/test_xi.py::TestXiStrong::test_zero_radius PASSED
tests/test_xi.py::TestXiStrong::test_negative_radius PASSED
tests/test_xi.py::TestXiStrong::test_at_rs PASSED
tests/test_xi.py::TestXiStrong::test_monotone_increasing PASSED
tests/test_xi.py::TestXiStrong::test_asymptotic_to_one PASSED
tests/test_xi.py::TestXiStrong::test_positive PASSED
tests/test_xi.py::TestXiWeak::test_at_large_r PASSED
tests/test_xi.py::TestXiWeak::test_inversely_proportional PASSED
tests/test_xi.py::TestXiWeak::test_zero_radius PASSED
tests/test_xi.py::TestXiHard::test_strong_regime PASSED
tests/test_xi.py::TestXiHard::test_weak_regime PASSED
tests/test_xi.py::TestXiHard::test_discontinuity_at_100 PASSED
tests/test_xi.py::TestXiBlend::test_pure_strong PASSED
tests/test_xi.py::TestXiBlend::test_pure_weak PASSED
tests/test_xi.py::TestXiBlend::test_smooth_in_blend PASSED
tests/test_xi.py::TestXiBlend::test_c2_continuity PASSED
tests/test_xi.py::TestXiBlend::test_monotone_decreasing_in_blend PASSED
tests/test_xi.py::TestMetricD::test_D_at_rs PASSED
tests/test_xi.py::TestMetricD::test_D_range PASSED
tests/test_xi.py::TestMetricD::test_s_inverse_of_D PASSED
tests/test_xi.py::TestDDerivative::test_positive_in_strong PASSED
tests/test_xi.py::TestDDerivative::test_finite PASSED

============================= 63 passed in 1.01s ==============================

```


---

================================================================================
REPO: segmented-energy
Status: FAILED
Exit Code: 2
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

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
============================== 3 errors in 2.98s ==============================

```


---

================================================================================
REPO: g79-cygnus-test
Status: FAILED
Exit Code: 3
================================================================================

## STDOUT (COMPLETE - NO TRUNCATION)

```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: E:\clone\g79-cygnus-test
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... ================================================================================
TESTING PARSEC-TO-METER CONVERSION IN MASS INTEGRATION
================================================================================

Integration range: 0.01 to 5.0 pc
Number of points: 200

In meters: 3.086e+14 to 1.543e+17 m

γ_seg range: 0.880003 to 0.999882

================================================================================
RESULTS:
================================================================================
M_core (kg):          1.990178e+44
M_core (solar masses): 100059229241878.33

Expected from paper:   8.7 ± 1.5 M_☉
Difference:            100059229241869.62 M_☉

⚠️  WARNING: Outside expected range!
================================================================================
================================================================================
TEMPERATURE EQUATIONS TEST SUITE
Segmented Spacetime Framework
================================================================================

[TEST 1/6] Temporal Density Function γ_seg(r) [Eq. 10]
--------------------------------------------------------------------------------
Parameters:
  α = 0.120 ± 0.030
  r_c = 1.9 pc

Results:
  γ_seg(0) = 0.8800 (inner core)
  γ_seg(r_c) = 0.9559 (characteristic radius)
  γ_seg(5 pc) = 0.9999 (outer shell)

Physical Interpretation:
  • Regions with γ_seg < 1 experience slower time flow
  • Minimum γ_seg = 0.8803 at r ≈ 0
  • Temporal compression factor: 1.14×
✓ Plot saved: Eq10_gamma_seg.png

[TEST 2/6] Basic Temperature Profile T(r) [Eq. 9]
--------------------------------------------------------------------------------
Parameters:
  T₀ = 240.0 K (outer H II temperature)

Predicted Temperatures:
  T(0) = 211.2 K (core)
  T(r_c) = 229.4 K (characteristic radius)
  T(5 pc) = 240.0 K (outer shell)

Observed Shell Temperatures:
  Shell 1: r=1.2 pc, T_obs=500 K, T_pred=220.7 K, Δ=+279.3 K
  Shell 2: r=2.3 pc, T_obs=200 K, T_pred=233.3 K, Δ=-33.3 K
  Shell 3: r=4.5 pc, T_obs=60 K, T_pred=239.9 K, Δ=-179.9 K
✓ Plot saved: Eq09_T_basic.png

[TEST 3/6] Dual-Frame Temperature [Eq. 15]
--------------------------------------------------------------------------------
Dual Temperature Relations:
  T_obs = T_local / γ_seg  (heating due to decoupling)
  T_local = T_obs × γ_seg   (cooling due to time dilation)

For T_local = 80.0 K:
  T_obs(r=0) = 90.9 K (apparent)
  T_obs(r_c) = 83.7 K

Physical Interpretation:
  • Inner g^(2) domain appears cooler internally
  • Same region appears hotter when viewed from g^(1)
  • Temperature 'inversion' is frame-dependent
✓ Plot saved: Eq15_dual_frame_temperature.png

[TEST 4/6] Energy Density Relations [Eq. 16]
--------------------------------------------------------------------------------
Stefan-Boltzmann Relations (u ∝ T⁴):
  u_obs^(2) = γ_seg⁴ × u_local  (compressed energy)
  u_obs^(1) = u_local / γ_seg⁴  (expanded energy)

Energy Density Ratios:
  At r=0: u_g2/u_g1 = 0.3607
  At r=r_c: u_g2/u_g1 = 0.6968

Physical Interpretation:
  • Energy stored in g^(2) appears compressed (u↑)
  • Same energy released in g^(1) appears diluted (u↓)
  • Total energy conserved across transition
✓ Plot saved: Eq16_energy_density.png

[TEST 5/6] Recoupling Temperature Release [Eq. 18]
--------------------------------------------------------------------------------
Energy Release Formula:
  ΔT_recouple = T_local × (1 - γ_seg)

Predicted Temperature Release:
  At r=0: ΔT = 9.6 K
  At r=r_c: ΔT = 3.5 K
  At r=5 pc: ΔT = 0.0 K

Physical Interpretation:
  • Energy stored in slower-time domain
  • Released as kinetic motion upon decoupling
  • Explains velocity excess Δv ≈ 5 km/s
✓ Plot saved: Eq18_recoupling_release.png

[TEST 6/6] Comprehensive Temperature Comparison
--------------------------------------------------------------------------------
✓ Plot saved: Temperature_Complete_Comparison.png

================================================================================
TEST SUITE SUMMARY
================================================================================

Equations Tested:
  ✓ Eq. (10): γ_seg(r) = 1 - α exp[-(r/r_c)²]
  ✓ Eq. (9):  T(r) = T₀ γ_seg(r)
  ✓ Eq. (15): T_obs = T_local / γ_seg (dual frames)
  ✓ Eq. (16): u_obs^(1,2) = u_local / γ_seg⁴
  ✓ Eq. (18): ΔT_recouple = T_local (1 - γ_seg)

Output Files Generated:
  • Eq09_T_basic.png (116 KB)
  • Eq10_gamma_seg.png (213 KB)
  • Eq15_dual_frame_temperature.png (253 KB)
  • Eq16_energy_density.png (173 KB)
  • Eq18_recoupling_release.png (170 KB)
  • Temperature_Complete_Comparison.png (181 KB)

Key Findings:
  • All equations mathematically consistent
  • Dual-frame temperatures reproduce observations
  • Energy release mechanism quantified
  • Temporal compression factor: 1.14×
  • Maximum ΔT_recouple: 9.6 K

================================================================================
ALL TEMPERATURE EQUATIONS VALIDATED ✓
================================================================================
================================================================================
THREE-PHASE DECOUPLING MODEL - VALIDATION
================================================================================

[TEST 1/4] Velocity Profile: Subsonic → Transonic → Supersonic
--------------------------------------------------------------------------------
Phase 1 (r < 1.5 pc): Subsonic
  v_internal(0.5 pc) = 5598.55 m/s = 0.011 c_s
  Mach number: M = 0.009 (subsonic)

Phase 2 (1.5 < r < 2.5 pc): Transonic (metric recoupling)
  v_transition(2.0 pc) = 10.41 km/s
  Mach number: M = 20.83 (transonic)

Phase 3 (r > 2.5 pc): Supersonic expansion
  v_external(4.0 pc) = 10.01 km/s
  Mach number: M = 20.0 (supersonic)
✓ Plot saved: three_phase_velocity_profile.png

[TEST 2/4] Temperature Evolution: Frame-Dependent Heating
--------------------------------------------------------------------------------
Internal temperature (g²): T_local = 80.0 K
Observed temperature at transition (g¹):
  T_obs(r=2 pc) = 83.3 K
  Ratio: T_obs/T_local = 1.04
✓ Plot saved: three_phase_temperature.png

[TEST 3/4] Energy Release: ΔT_recouple
--------------------------------------------------------------------------------
Maximum energy release:
  ΔT_max = 9.57 K (at r ≈ 0.10 pc)
  E_kinetic(r_seg) = 5.42e+07 J/kg
✓ Plot saved: three_phase_energy_release.png

[TEST 4/4] Complete Three-Phase State Diagram
--------------------------------------------------------------------------------
✓ Plot saved: three_phase_complete_diagram.png

================================================================================
THREE-PHASE MODEL VALIDATION COMPLETE
================================================================================

Phase Characteristics:

  Phase 1 (g²): Quasi-static, subsonic
    γ_seg: 0.88 – 0.95
    Velocity: < 1 km/s (M < 1)
    Temperature: T_local ≈ 80.0 K
    State: Temporally dense, energy accumulation

  Phase 2 (Transition): Metric recoupling
    γ_seg: 0.90 – 0.96
    Velocity: 3–5 km/s (M ≈ 1)
    Temperature: T_obs ≈ 200–500 K (apparent)
    State: Energy release, temporal→kinetic conversion

  Phase 3 (g¹): Inertial expansion
    γ_seg: 0.96 – 1.00
    Velocity: 10–16 km/s (M > 1)
    Temperature: T ≈ 60–240 K
    State: Classical expansion, cooling

Key Results:
  ✓ Velocity excess Δv ≈ 10.41 km/s (observed: 3-5 km/s)
  ✓ Temperature peak at transition zone (observed: yes)
  ✓ Subsonic inner region (observed: yes)
  ✓ Energy release mechanism quantified: ΔT_max = 9.57 K

================================================================================
ALL TESTS PASSED ✓
================================================================================
ERROR: No module named 'astroquery'
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

============================= 1 warning in 8.53s ==============================

```

## STDERR (COMPLETE - NO TRUNCATION)

```
mainloop: caught unexpected SystemExit!

```


---

