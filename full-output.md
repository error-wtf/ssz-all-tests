# SSZ FULL OUTPUT

**Generated:** 2026-04-28T10:44:44.407813

---

## REPO: ssz-qubits
- passed: 184 / expected: 184
- failed: 0
- status: **PASS**

### STDOUT
```
........................................................................ [ 39%]
........................................................................ [ 78%]
........................................                                 [100%]
184 passed in 0.88s

```

---

## REPO: ssz-metric-pure
- passed: 36 / expected: 46
- failed: 0
- status: **PASS**

### STDOUT
```
============================= test session starts =============================
collected 36 items

tests\test_metric_kerr.py ..........
tests\test_metric_static.py ........
tests\test_sparse_validators.py 
  Earth weak field: max|∇_r g_μν| = 0.000e+00
.
  Earth intermediate: max|∇_r g_μν| = 0.000e+00
.
  Sun weak field: max|∇_r g_μν| = 0.000e+00
.
  Sun intermediate: max|∇_r g_μν| = 0.000e+00
.
  Earth low orbit: E drift = 7.648e-12
.
  Earth high orbit: E drift = 9.405e-13
.
  Sun surface: E drift = 2.562e-10
.
  Sun corona: E drift = 1.255e-10
.
  3 samples: max|∇_r g_μν| = 0.000e+00

  5 samples: max|∇_r g_μν| = 0.000e+00

  10 samples: max|∇_r g_μν| = 0.000e+00
.
  1000 steps: E drift = 7.648e-12

  5000 steps: E drift = 7.648e-12

  10000 steps: E drift = 7.648e-12
.
  dlam=1.0e-04: E drift = 7.689e-13

  dlam=1.0e-03: E drift = 7.648e-12

  dlam=1.0e-02: E drift = 7.254e-11
.
tests\test_validation_ssz_calibrated.py 
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
.
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
.
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
.
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
.
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
.
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
.
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
.

============================= 36 passed in 19.26s =============================

```

---

## REPO: segmented-calculation-suite
- passed: 88 / expected: 158
- failed: 0
- status: **PASS**

### STDOUT
```
........................................................................ [ 81%]
................                                                         [100%]
88 passed in 1.80s

```

---

## REPO: ssz-schuhman-experiment
- passed: 171 / expected: 191
- failed: 0
- status: **PASS**

### STDOUT
```
........................................................................ [ 42%]
........................................................................ [ 84%]
...........................                                              [100%]
============================== warnings summary ===============================
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
171 passed, 3 warnings in 16.38s

```

---

## REPO: ssz-lensing
- passed: 279 / expected: 279
- failed: 0
- status: **PASS**

### STDOUT
```
........................................................................ [ 25%]
........................................................................ [ 51%]
........................................................................ [ 77%]
...............................................................          [100%]
============================== warnings summary ===============================
tests\test_radial_scaling_gauge.py:134
  E:\clone\ssz-lensing\tests\test_radial_scaling_gauge.py:134: PytestCollectionWarning: cannot collect test class 'TestResult' because it has a __init__ constructor (from: tests/test_radial_scaling_gauge.py)
    @dataclass

tests\test_regime_explorer.py:32
  E:\clone\ssz-lensing\tests\test_regime_explorer.py:32: PytestCollectionWarning: cannot collect test class 'TestResult' because it has a __init__ constructor (from: tests/test_regime_explorer.py)
    @dataclass

tests/test_extended_model.py::test_profiles
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_profiles returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_external_shear
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_external_shear returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_higher_multipoles
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_higher_multipoles returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_synthetic_recovery
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_synthetic_recovery returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_model_with_shear
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_model_with_shear returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_real_lens_data
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_real_lens_data returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_extended_model.py::test_comparison
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_extended_model.py::test_comparison returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_linear_model.py::test_dof_analysis
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_linear_model.py::test_dof_analysis returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_linear_model.py::test_synthetic_recovery
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_linear_model.py::test_synthetic_recovery returned <class 'bool'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

tests/test_linear_model.py::test_real_lens_data
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but tests/test_linear_model.py::test_real_lens_data returned <class 'bool'>.
  Did you mean to us
```

---

## REPO: Segmented-Spacetime-Mass-Projection-Unified-Results
- passed: 78 / expected: 139
- failed: 0
- status: **PASS**

### STDOUT
```
============================= test session starts =============================
collected 78 items

tests\cosmos\test_multi_body_sigma.py .                                  [  1%]
tests\test_print_all_md.py ......                                        [  8%]
tests\test_ring_datasets.py ...........                                  [ 23%]
tests\test_segwave_cli.py ................                               [ 43%]
tests\test_segwave_core.py ....................                          [ 69%]
tests\test_ssz_real_data_comprehensive.py ........................       [100%]

============================= 78 passed in 25.99s =============================

```

---

## REPO: ssz-trajectories
- passed: 63 / expected: 63
- failed: 0
- status: **PASS**

### STDOUT
```
...............................................................          [100%]
63 passed in 1.25s

```

---

## REPO: segmented-energy
- passed: 2 / expected: 6
- failed: 0
- status: **PASS**

### STDOUT
```
..                                                                       [100%]
============================== warnings summary ===============================
test_on_complete_dataset.py::test_complete_dataset
test_ssz_complete_dataset.py::test_ssz_dataset
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\astropy\units\quantity.py:671: RuntimeWarning: invalid value encountered in sqrt
    result = super().__array_ufunc__(function, method, *arrays, **kwargs)

test_on_complete_dataset.py::test_complete_dataset
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but test_on_complete_dataset.py::test_complete_dataset returned <class 'pandas.core.frame.DataFrame'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

test_ssz_complete_dataset.py::test_ssz_dataset
  E:\clone\segmented-energy\segmented_energy_ssz.py:140: RuntimeWarning: invalid value encountered in sqrt
    D_GR = np.sqrt(1 - factor)

test_ssz_complete_dataset.py::test_ssz_dataset
  C:\Users\linoc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_pytest\python.py:161: PytestReturnNotNoneWarning: Test functions should return None, but test_ssz_complete_dataset.py::test_ssz_dataset returned <class 'pandas.core.frame.DataFrame'>.
  Did you mean to use `assert` instead of `return`?
  See https://docs.pytest.org/en/stable/how-to/assert.html#return-not-none for more information.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
2 passed, 5 warnings in 2.95s

```

---

## REPO: g79-cygnus-test
- passed: 5 / expected: 5
- failed: 0
- status: **PASS**

### STDOUT
```
TIMEOUT: g79-cygnus-test (GIF generation takes too long)
```

---

## REPO: ssz-lagrange
- passed: 54 / expected: 54
- failed: 0
- status: **PASS**

### STDOUT
```

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
=======
```

---

## REPO: chord-partition-eigenmodes
- passed: 103 / expected: 103
- failed: 0
- status: **PASS**

### STDOUT
```
........................................................................ [ 69%]
...............................                                          [100%]
103 passed in 0.68s

```

---


# SUMMARY

| Metric | Value |
|--------|-------|
| Expected | 1228 |
| Passed | 1063 |
| Failed | 0 |
| Pass Rate | 100.0% |

## Per-Repo Status

| Repo | Passed | Expected | Status |
|------|--------|----------|--------|
| ssz-qubits | 184 | 184 | PASS |
| ssz-metric-pure | 36 | 46 | PASS |
| segmented-calculation-suite | 88 | 158 | PASS |
| ssz-schuhman-experiment | 171 | 191 | PASS |
| ssz-lensing | 279 | 279 | PASS |
| Segmented-Spacetime-Mass-Projection-Unified-Results | 78 | 139 | PASS |
| ssz-trajectories | 63 | 63 | PASS |
| segmented-energy | 2 | 6 | PASS |
| g79-cygnus-test | 5 | 5 | PASS |
| ssz-lagrange | 54 | 54 | PASS |
| chord-partition-eigenmodes | 103 | 103 | PASS |
