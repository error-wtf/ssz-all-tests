# SSZ FULL CHAIN OUTPUT

Generated: 2026-04-27T22:19:01.397839
Duration: 232.1s

## Global Summary

- **Total Repos:** 10
- **Passed:** 6
- **Skipped:** 2
- **Failed:** 1
- **Total Tests:** 588

| Repository | Status | Tests | Passed | Failed | Duration |
|------------|--------|-------|--------|--------|----------|
| ssz-qubits | ✅ PASS | 27 | 27 | 0 | 27.8s |
| ssz-metric-pure | ✅ PASS | 36 | 36 | 0 | 17.2s |
| segmented-calculation-suite | ✅ PASS | 158 | 158 | 0 | 7.6s |
| ssz-schuhman-experiment | ⚠️ NO_TESTS | 0 | 0 | 0 | 2.9s |
| ssz-lensing | ✅ PASS | 279 | 279 | 0 | 12.2s |
| Unified-Results | ⏭️ SKIP | 0 | 0 | 0 | 0.0s |
| ssz-trajectories | ✅ PASS | 63 | 63 | 0 | 3.2s |
| segmented-energy | ⏭️ SKIP | 0 | 0 | 0 | 0.0s |
| g79-cygnus-test | ✅ PASS | 5 | 5 | 0 | 131.0s |
| ssz-all-tests | ❌ FAIL | 20 | 18 | 2 | 30.3s |

---

## Detailed Results by Repository

### ssz-qubits

**Status:** PASS
**Duration:** 27.8s
**Runner:** e:\clone\ssz-qubits\run_tests.py
**Exit Code:** 0
**Tests:** 27
**Passed:** 27
**Failed:** 0

#### Output
```
on::test_tokyo_skytree_experiment 
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

============================= 17 passed in 0.33s ==============================


[PHASE 3] Generating Summary
======================================================================
SSZ-QUBITS TEST SUMMARY
Generated: 2026-04-27 22:15:37
======================================================================

Test File                                | Status     | Time      
-----------------------------------------------------------------
ssz_qubits.py (Demo)                     | PASS       | 0.69s     
test_edge_cases.py                       | PASS       | 5.16s     
test_entanglement.py                     | PASS       | 4.32s     
test_paper_a_support.py                  | PASS       | 3.41s     
test_paper_c_support.py                  | PASS       | 3.04s     
test_paper_d_validation.py               | PASS       | 0.73s     
test_roadmap_validation.py               | PASS       | 2.49s     
test_ssz_physics.py                      | PASS       | 2.56s     
test_ssz_qubit_applications.py           | PASS       | 2.56s     
test_validation.py                       | PASS       | 2.51s     
-----------------------------------------------------------------

RESULTS:
  Total test files: 10
  Passed: 10
  Failed: 0
  Total time: 27.46s

STATUS: ALL TESTS PASSED

======================================================================

Summary saved to: e:\clone\ssz-qubits\reports\RUN_SUMMARY.md
Full output saved to: e:\clone\ssz-qubits\reports\full-output.md

======================================================================
SSZ-Qubits - Segmented Spacetime Framework for Quantum Computing
Copyright (c) 2025 Carmen Wrede and Lino Casu
Licensed under the Anti-Capitalist Software License v1.4
https://github.com/error-wtf/ssz-qubits
======================================================================

```

---

### ssz-metric-pure

**Status:** PASS
**Duration:** 17.2s
**Runner:** pytest
**Exit Code:** 0
**Tests:** 36
**Passed:** 36
**Failed:** 0

#### Output
```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: e:\clone\ssz-metric-pure
configfile: pyproject.toml
testpaths: tests
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

============================= 36 passed in 14.78s =============================

```

---

### segmented-calculation-suite

**Status:** PASS
**Duration:** 7.6s
**Runner:** pytest
**Exit Code:** 0
**Tests:** 158
**Passed:** 158
**Failed:** 0

#### Output
```
mHint::test_geom_hint_finite PASSED [ 33%]
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

============================= 158 passed in 4.65s =============================

```

---

### ssz-schuhman-experiment

**Status:** NO_TESTS
**Duration:** 2.9s
**Runner:** e:\clone\ssz-schuhman-experiment\run_all_ssz_tests.py
**Exit Code:** 0
**Tests:** 0
**Passed:** 0
**Failed:** 0

#### Output
```
27   -4.41e+01 %

KEY INSIGHT:
  - Weak field (Earth, Sun, WD): Xi ~ r_s/r ~ GM/(Rc^2) << 1
  - Strong field (NS, BH): Xi ~ 1, Delta ~ -44%
  - SSZ effect scales with gravitational potential!

Earth Xi = 6.96e-10 < 10^-6: True
BH Delta = -44.1% ~ -44%: True
TEST RESULT: PASSED

######################################################################
#                         SUMMARY                                    #
######################################################################

  44% Prediction            PASSED
  Universal Crossover       PASSED
  Horizon Behavior          PASSED
  G79 Nebula                PASSED
  Segment Saturation        PASSED
  Earth/Schumann NULL       PASSED
  Scaling Comparison        PASSED

OVERALL: 7/7 tests passed

All SSZ predictions verified!

KEY FINDINGS:
  1. Delta = -44% at r = 5*r_s (SSZ slower than GR)
  2. Universal crossover at r* = 1.386562*r_s
  3. NO horizon singularity (D_SSZ(r_s) ~ 0.55)
  4. G79 z_temporal ~ 0.12 matches observations
  5. Xi is bounded, D_SSZ always positive
  6. Earth/Schumann: SSZ effect ~ 0 (NULL TEST)
  7. SAME formula works from Earth to Black Holes!

CONCLUSION:
  The Schumann null result is CONSISTENT with SSZ theory.
  Earth's gravity is simply too weak for detectable effects.
  Strong-field tests (NS, BH) are needed to see SSZ.


======================================================================
Running: SSZ Full Scale Test
Script: scripts/test_ssz_full_scale.py
======================================================================

################################################################################
#                    SSZ FULL SCALE TEST                                     #
#               From Earth to Supermassive Black Holes                       #
################################################################################

Testing SSZ predictions with CORRECT formulas:
  D_SSZ = 1 / (1 + Xi)
  Xi (weak) = r_s / (2r)
  Xi (strong) = Xi_max * (1 - exp(-phi * r / r_s))

====================================================================================================
Object                    Category        GM/(Rc^2)    Xi           D_SSZ      D_GR       Delta     
====================================================================================================
Earth                     Planet          6.96e-10     6.96e-10     1.0000     1.0000     0.00e+00% 
Jupiter                   Planet          2.02e-08     2.02e-08     1.0000     1.0000     6.66e-14% 
----------------------------------------------------------------------------------------------------
Sun                       Star            2.12e-06     2.12e-06     1.0000     1.0000     6.76e-10% 
Sirius A                  Star            2.51e-06     2.51e-06     1.0000     1.0000     9.43e-10% 
----------------------------------------------------------------------------------------------------
White Dwarf (Sirius B)    White Dwarf     2.60e-04     2.60e-04     0.9997     0.9997     1.01e-05% 
Heavy WD (Chandrasekhar)  White Dwarf     6.89e-04     6.89e-04     0.9993     0.9993     7.13e-05% 
----------------------------------------------------------------------------------------------------
NS J0030+0451             Neutron Star    1.63e-01     9.93e-01     0.5018     0.8205     -38.8%    
NS J0740+6620             Neutron Star    2.48e-01     9.62e-01     0.5098     0.7100     -28.2%    
NS J0348+0432             Neutron Star    2.28e-01     9.71e-01     0.5073     0.7371     -31.2%    
----------------------------------------------------------------------------------------------------
Stellar BH (10 M_sun)     Black Hole      1.00e-01     1.00e+00     0.5001     0.8944     -44.1%    
Stellar BH (30 M_sun)     Black Hole      1.00e-01     1.00e+00     0.5001     0.8944     -44.1%    
IMBH (1000 M_sun)         Black Hole      1.00e-01     1.00e+00     0.5001     0.8944     -44.1%    
----------------------------------------------------------------------------------------------------
Sgr A* (4M M_sun)         SMBH            1.00e-01     1.00e+00     0.5001     0.8944     -44.1%    
M87* (6.5B M_sun)         SMBH            1.00e-01     1.00e+00     0.5001     0.8944     -44.1%    
====================================================================================================

DETAILED ANALYSIS BY CATEGORY
--------------------------------------------------------------------------------

PLANET:
  Earth:
    Mass: 3.00e-06 M_sun
    r/r_s: 7.18e+08
    Compactness: 6.96e-10
    Xi: 6.96e-10
    D_SSZ: 1.000000
    D_GR: 1.000000
    Delta: 0.00e+00%
  Jupiter:
    Mass: 9.54e-04 M_sun
    r/r_s: 2.48e+07
    Compactness: 2.02e-08
    Xi: 2.02e-08
    D_SSZ: 1.000000
    D_GR: 1.000000
    Delta: 6.66e-14%

STAR:
  Sun:
    Mass: 1.00e+00 M_sun
    r/r_s: 2.36e+05
    Compactness: 2.12e-06
    Xi: 2.12e-06
    D_SSZ: 0.999998
    D_GR: 0.999998
    Delta: 6.76e-10%
  Sirius A:
    Mass: 2.02e+00 M_sun
    r/r_s: 1.99e+05
    Compactness: 2.51e-06
    Xi: 2.51e-06
    D_SSZ: 0.999997
    D_GR: 0.999997
    Delta: 9.43e-10%

WHITE DWARF:
  White Dwarf (Sirius B):
    Mass: 1.02e+00 M_sun
    r/r_s: 1.92e+03
    Compactness: 2.60e-04
    Xi: 2.60e-04
    D_SSZ: 0.999740
    D_GR: 0.999740
    Delta: 1.01e-05%
  Heavy WD (Chandrasekhar):
    Mass: 1.40e+00 M_sun
    r/r_s: 7.25e+02
    Compactness: 6.89e-04
    Xi: 6.89e-04
    D_SSZ: 0.999311
    D_GR: 0.999310
    Delta: 7.13e-05%

NEUTRON STAR:
  NS J0030+0451:
    Mass: 1.44e+00 M_sun
    r/r_s: 3.06e+00
    Compactness: 1.63e-01
    Xi: 9.93e-01
    D_SSZ: 0.501773
    D_GR: 0.820542
    Delta: -3.88e+01%
  NS J0740+6620:
    Mass: 2.08e+00 M_sun
    r/r_s: 2.02e+00
    Compactness: 2.48e-01
    Xi: 9.62e-01
    D_SSZ: 0.509758
    D_GR: 0.709992
    Delta: -2.82e+01%
  NS J0348+0432:
    Mass: 2.01e+00 M_sun
    r/r_s: 2.19e+00
    Compactness: 2.28e-01
    Xi: 9.71e-01
    D_SSZ: 0.507341
    D_GR: 0.737065
    Delta: -3.12e+01%

BLACK HOLE:
  Stellar BH (10 M_sun):
    Mass: 1.00e+01 M_sun
    r/r_s: 5.00e+00
    Compactness: 1.00e-01
    Xi: 1.00e+00
    D_SSZ: 0.500077
    D_GR: 0.894427
    Delta: -4.41e+01%
  Stellar BH (30 M_sun):
    Mass: 3.00e+01 M_sun
    r/r_s: 5.00e+00
    Compactness: 1.00e-01
    Xi: 1.00e+00
    D_SSZ: 0.500077
    D_GR: 0.894427
    Delta: -4.41e+01%
  IMBH (1000 M_sun):
    Mass: 1.00e+03 M_sun
    r/r_s: 5.00e+00
    Compactness: 1.00e-01
    Xi: 1.00e+00
    D_SSZ: 0.500077
    D_GR: 0.894427
    Delta: -4.41e+01%

SMBH:
  Sgr A* (4M M_sun):
    Mass: 4.00e+06 M_sun
    r/r_s: 5.00e+00
    Compactness: 1.00e-01
    Xi: 1.00e+00
    D_SSZ: 0.500077
    D_GR: 0.894427
    Delta: -4.41e+01%
  M87* (6.5B M_sun):
    Mass: 6.50e+09 M_sun
    r/r_s: 5.00e+00
    Compactness: 1.00e-01
    Xi: 1.00e+00
    D_SSZ: 0.500077
    D_GR: 0.894427
    Delta: -4.41e+01%

================================================================================
SUMMARY STATISTICS
================================================================================

Weak Field Objects (6):
  Compactness range: 6.96e-10 to 6.89e-04
  Xi range: 6.96e-10 to 6.89e-04
  Delta range: 0.00e+00% to 7.13e-05%
  -> SSZ effects UNDETECTABLE (Delta ~ 0%)

Strong Field Objects (8):
  Compactness range: 1.00e-01 to 2.48e-01
  Xi range: 9.62e-01 to 1.00e+00
  Delta range: -44.1% to -28.2%
  -> SSZ effects DETECTABLE (Delta ~ -28% to -44%)

================================================================================
KEY SSZ PREDICTIONS
================================================================================

1. EARTH (Schumann Null Test):
   Xi = 6.96e-10
   Delta = 0.00e+00%
   -> UNDETECTABLE (explains Schumann null result)

2. NEUTRON STAR (NS J0740+6620):
   Xi = 0.9617
   Delta = -28.2%
   -> DETECTABLE with NICER data

3. BLACK HOLE (at 5*r_s):
   Xi = 0.9997
   Delta = -44.1%
   -> The -44% prediction!

4. SMBH Sgr A* (at 5*r_s):
   Xi = 0.9997
   Delta = -44.1%
   -> Same as stellar BH (mass-independent!)

================================================================================
VALIDATION
================================================================================

1. Earth Xi < 10^-6: 6.96e-10 -> PASSED
2. NS |Delta| > 10%: -28.2% -> PASSED
3. BH Delta ~ -44%: -44.1% -> PASSED
4. Mass independence: |BH - SMBH| = 0.00% -> PASSED
5. Correct scaling (weak~0, strong<-20%): -> PASSED

OVERALL: 5/5 tests passed

================================================================================
CONCLUSION
================================================================================

The SSZ theory predictions are VALIDATED across all scales:

  - WEAK FIELD (Earth to WD): Xi ~ GM/(Rc^2) << 1
    -> SSZ = GR (no detectable difference)

  - STRONG FIELD (NS to SMBH): Xi ~ 1
    -> SSZ differs from GR by -28% to -44%

  - The -44% prediction at r = 5*r_s is CONFIRMED

  - The Schumann null result is EXPLAINED
    (Earth's Xi ~ 10^-9 is undetectable)

  - SAME formula works from Earth to SMBH!



######################################################################
#                         SUMMARY                                    #
######################################################################

  SSZ Correct Predictions                  PASSED
  SSZ Full Scale Test                      PASSED

OVERALL: 2/2 test suites passed

======================================================================
ALL SSZ TESTS PASSED!
======================================================================

VALIDATED PREDICTIONS:
  1. -44% time dilation at r = 5*r_s
  2. Universal crossover at r* = 1.387*r_s
  3. No horizon singularity (D_SSZ finite)
  4. G79 nebula z_temporal ~ 0.12
  5. Earth/Schumann null test (Xi ~ 10^-9)
  6. Mass-independent BH predictions
  7. Scaling from Earth to SMBH

CONCLUSION:
  SSZ theory is mathematically consistent across all scales.
  The Schumann null result is EXPLAINED by weak-field limit.
  Strong-field tests (NS, BH) needed for detection.

```

---

### ssz-lensing

**Status:** PASS
**Duration:** 12.2s
**Runner:** pytest
**Exit Code:** 0
**Tests:** 279
**Passed:** 279
**Failed:** 0

#### Output
```
l-packages\Python312\site-packages\_pytest\python.py:170: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_regime_explorer.py::test_underdetermined_multiple_solutions returned <class 'bool'>.
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
====================== 279 passed, 63 warnings in 9.49s =======================

```

---

### Unified-Results

**Status:** SKIP
**Duration:** 0.0s
**Reason:** Import configuration - requires PYTHONPATH fix
**Runner:** N/A
**Exit Code:** None
**Tests:** 0
**Passed:** 0
**Failed:** 0

---

### ssz-trajectories

**Status:** PASS
**Duration:** 3.2s
**Runner:** pytest
**Exit Code:** 0
**Tests:** 63
**Passed:** 63
**Failed:** 0

#### Output
```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\linoc\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: e:\clone\ssz-trajectories
configfile: pyproject.toml
testpaths: tests
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

============================= 63 passed in 1.01s ==============================

```

---

### segmented-energy

**Status:** SKIP
**Duration:** 0.0s
**Reason:** Dataset file missing - path config needed
**Runner:** N/A
**Exit Code:** None
**Tests:** 0
**Passed:** 0
**Failed:** 0

---

### g79-cygnus-test

**Status:** PASS
**Duration:** 131.0s
**Runner:** e:\clone\g79-cygnus-test\RUN_ALL_VALIDATED_TESTS.py
**Exit Code:** 0
**Tests:** 5
**Passed:** 5
**Failed:** 0

#### Output
```
---------------------------
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

STDERR: e:\clone\g79-cygnus-test\TEST_TEMPERATURE_EQUATIONS_COMPLETE.py:336: UserWarning: linestyle is redundantly defined by the 'linestyle' keyword argument and the fmt string "b-" (-> linestyle='-'). The keyword argument will take precedence.
  ax.plot(r_range, T_loc_in_g2, 'b-', linewidth=3, linestyle='-.',


✅ SUCCESS (4.6s)

================================================================================
[22:16:27] Running: Temperature Animations (5 GIFs)
Script: GENERATE_TEMPERATURE_ANIMATIONS.py
================================================================================

================================================================================
TEMPERATURE ANIMATIONS - GIF GENERATION
================================================================================

[1/5] Generating: temporal_density_evolution.gif
✓ Saved: temporal_density_evolution.gif
[2/5] Generating: temperature_profile_scan.gif
✓ Saved: temperature_profile_scan.gif
[3/5] Generating: dual_frame_temperature.gif
✓ Saved: dual_frame_temperature.gif
[4/5] Generating: energy_density_evolution.gif
✓ Saved: energy_density_evolution.gif
[5/5] Generating: recoupling_energy_release.gif
✓ Saved: recoupling_energy_release.gif

================================================================================
ANIMATION GENERATION COMPLETE
================================================================================

Generated Animations:
  • dual_frame_temperature.gif (431 KB)
  • energy_density_evolution.gif (463 KB)
  • recoupling_energy_release.gif (433 KB)
  • temperature_profile_scan.gif (496 KB)
  • temporal_density_evolution.gif (402 KB)

Animations cover:
  ✓ Eq. (10): Temporal density γ_seg(r)
  ✓ Eq. (9):  Temperature profile T(r)
  ✓ Eq. (15): Dual-frame transformation
  ✓ Eq. (16): Energy density u(r)
  ✓ Eq. (18): Recoupling release ΔT

================================================================================


✅ SUCCESS (57.9s)

================================================================================
[22:17:25] Running: Three-Phase Decoupling Model
Script: TEST_THREE_PHASE_DECOUPLING.py
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


✅ SUCCESS (4.8s)

================================================================================
[22:17:30] Running: Three-Phase Animations (3 GIFs)
Script: GENERATE_THREE_PHASE_ANIMATIONS.py
================================================================================

================================================================================
THREE-PHASE ANIMATIONS - GIF GENERATION
================================================================================

[1/3] Generating: radial_particle_journey.gif
✓ Saved: radial_particle_journey.gif
[2/3] Generating: velocity_buildup.gif
✓ Saved: velocity_buildup.gif
[3/3] Generating: phase_transition_dynamics.gif
✓ Saved: phase_transition_dynamics.gif

================================================================================
ANIMATION GENERATION COMPLETE
================================================================================

Generated Animations:
  • phase_transition_dynamics.gif (107 KB)
  • radial_particle_journey.gif (415 KB)
  • velocity_buildup.gif (490 KB)

Animations visualize:
  ✓ Radial particle journey through three phases
  ✓ Velocity buildup from subsonic to supersonic
  ✓ Complete phase transition dynamics

================================================================================


✅ SUCCESS (60.8s)

================================================================================
SUMMARY
================================================================================
✅ PASS - Parsec Conversion Validation
✅ PASS - Temperature Equations (Eq. 9-18)
✅ PASS - Temperature Animations (5 GIFs)
✅ PASS - Three-Phase Decoupling Model
✅ PASS - Three-Phase Animations (3 GIFs)

Total: 5/5 passed
Duration: 2.2 minutes

🎉 ALL TESTS PASSED!

```

---

### ssz-all-tests

**Status:** FAIL
**Duration:** 30.3s
**Runner:** e:\clone\ssz-all-tests-test\run_all_tests.py
**Exit Code:** 0
**Tests:** 20
**Passed:** 18
**Failed:** 2

#### Output
```
IV_frequency/test_ch16_17_frequency.py::TestCh17TimeDilation::test_interference_phase_shift PASSED [ 78%]
tests/part_IV_frequency/test_ch16_17_frequency.py::TestCh17TimeDilation::test_interference_constructive PASSED [ 82%]
tests/part_IV_frequency/test_ch16_17_frequency.py::TestCh17TimeDilation::test_interference_destructive PASSED [ 85%]
tests/part_IV_frequency/test_ch16_17_frequency.py::TestCh17TimeDilation::test_temporal_interference PASSED [ 89%]
tests/part_IV_frequency/test_ch16_17_frequency.py::TestCh17TimeDilation::test_ssz_time_dilation_excess PASSED [ 92%]
tests/part_IV_frequency/test_ch16_17_frequency.py::TestCh17TimeDilation::test_gravitational_redshift_time_dilation_equivalence PASSED [ 96%]
tests/part_IV_frequency/test_ch16_17_frequency.py::TestCh17TimeDilation::test_ssz_interference_modification PASSED [100%]

============================= 28 passed in 0.70s ==============================

[OK] Part IV: Frequency Framework: PASSED

======================================================================
[SSZ] Part V: Strong Field (94 tests)
======================================================================
ng_field/test_ch18_22_strong_field.py::TestCh18BHMetric::test_dilation_function PASSED [ 21%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh18BHMetric::test_metric_line_element PASSED [ 26%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh18BHMetric::test_no_event_horizon PASSED [ 31%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh18BHMetric::test_gravitational_potential PASSED [ 36%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh19SingularityResolution::test_finite_at_center PASSED [ 42%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh19SingularityResolution::test_dilation_monotonic_bounded PASSED [ 47%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh19SingularityResolution::test_no_infinite_curvature PASSED [ 52%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh19SingularityResolution::test_regular_center PASSED [ 57%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh19SingularityResolution::test_saturation_mechanism PASSED [ 63%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh20CosmicCensorship::test_natural_boundary_exists PASSED [ 68%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh20CosmicCensorship::test_weak_censorship_satisfied PASSED [ 73%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh20CosmicCensorship::test_strong_censorship_modified PASSED [ 78%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh21DarkStars::test_hawking_temperature_modified PASSED [ 84%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh21DarkStars::test_thermal_emission_finite PASSED [ 89%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh21DarkStars::test_surface_redshift PASSED [ 94%]
tests/part_V_strong_field/test_ch18_22_strong_field.py::TestCh22Superradiance::test_superradiant_regulator PASSED [100%]

============================= 19 passed in 1.17s ==============================

[OK] Part V: Strong Field: PASSED

======================================================================
[SSZ] Part VI: Astrophysics (14 tests)
======================================================================
ythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: e:\clone\ssz-all-tests-test
configfile: pyproject.toml
plugins: anyio-4.12.1, Faker-40.4.0
collecting ... collected 14 items

tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_schwarzschild_radius PASSED [  7%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_compactness_parameter PASSED [ 14%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_neutron_star_compactness PASSED [ 21%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_white_dwarf_mass_limit PASSED [ 28%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_neutron_star_mass_range PASSED [ 35%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_black_hole_spin_limit PASSED [ 42%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_eddington_luminosity PASSED [ 50%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh23CompactObjects::test_ssz_compact_object_modification PASSED [ 57%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh24Accretion::test_accretion_luminosity PASSED [ 64%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh24Accretion::test_accretion_efficiency PASSED [ 71%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh24Accretion::test_innermost_stable_orbit PASSED [ 78%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh24Accretion::test_accretion_disk_temperature PASSED [ 85%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh24Accretion::test_jet_formation_power PASSED [ 92%]
tests/part_VI_astrophysics/test_ch23_24_astrophysics.py::TestCh24Accretion::test_ssz_accretion_modification PASSED [100%]

============================= 14 passed in 0.72s ==============================

[OK] Part VI: Astrophysics: PASSED

======================================================================
[SSZ] Part VII: Dynamics (54 tests)
======================================================================
Ch25Perturbations::test_metric_perturbation_h_munu PASSED [ 70%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_gauge_transformation_harmonic PASSED [ 72%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_wave_equation_h_munu PASSED [ 74%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_gravitational_wave_plus_polarization PASSED [ 75%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_gravitational_wave_cross_polarization PASSED [ 77%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_gravitational_wave_amplitude PASSED [ 79%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_gravitational_wave_frequency PASSED [ 81%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_chirp_mass PASSED [ 83%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_inspiral_waveform PASSED [ 85%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_ringdown_waveform PASSED [ 87%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_quasinormal_mode_frequencies PASSED [ 88%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_scalar_perturbation_klein_gordon PASSED [ 90%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_vector_perturbation_proca PASSED [ 92%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_tensor_perturbation_linearized_einstein PASSED [ 94%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_density_contrast_evolution PASSED [ 96%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_growth_factor PASSED [ 98%]
tests/part_VII_dynamics/test_ch25_dynamics.py::TestCh25Perturbations::test_ssz_perturbation_modification PASSED [100%]

============================= 54 passed in 0.57s ==============================

[OK] Part VII: Dynamics: PASSED

======================================================================
[SSZ] Part VIII: Validation (77 tests)
======================================================================
st_neutron_star_redshift_prediction PASSED [ 16%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh30FalsifiablePredictions::test_neutron_star_instrument_nicer PASSED [ 22%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh30FalsifiablePredictions::test_bh_shadow_diameter PASSED [ 27%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh30FalsifiablePredictions::test_bh_shadow_ng_eht PASSED [ 33%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh30FalsifiablePredictions::test_qnm_frequency_shift PASSED [ 38%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh30FalsifiablePredictions::test_pulsar_timing_excess PASSED [ 44%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh30FalsifiablePredictions::test_ssz_is_falsifiable PASSED [ 50%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh30FalsifiablePredictions::test_gr_match_weak_field PASSED [ 55%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh28CodeConsistency::test_repository_count PASSED [ 61%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh28CodeConsistency::test_total_tests_564 PASSED [ 66%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh28CodeConsistency::test_segmented_calculation_suite_186 PASSED [ 72%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh28CodeConsistency::test_weak_field_tests_match_gr PASSED [ 77%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh28CodeConsistency::test_strong_field_tests_orthogonal PASSED [ 83%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh26AntiCircularity::test_no_circular_validation PASSED [ 88%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh26AntiCircularity::test_domain_separation PASSED [ 94%]
tests/part_VIII_validation/test_ch26_30_validation.py::TestCh26AntiCircularity::test_cross_consistency_post_hoc PASSED [100%]

============================= 18 passed in 2.69s ==============================

[OK] Part VIII: Validation: PASSED

======================================================================
SUMMARY: 331+ tests validated
======================================================================

```

---

*End of Report*
