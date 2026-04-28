# SSZ Understanding Report

**Generated:** 2026-04-28T00:49:33.560795

## What Was Tested

- **Total Tests:** 776
- **Passed:** 776
- **Failed:** 0

## Repositories

| Repo | Tests | Passed | Failed | Duration |
|------|-------|--------|--------|----------|
| ssz-qubits | 184 | 184 | 0 | 3.6s |
| ssz-metric-pure | 0 | 0 | 0 | 21.5s |
| segmented-calculation-suite | 145 | 145 | 0 | 7.9s |
| ssz-schuhman-experiment | 171 | 171 | 0 | 20.7s |
| ssz-lagrange | 0 | 0 | 0 | 12.1s |
| ssz-lensing | 213 | 213 | 0 | 10.3s |
| Unified-Results | 0 | 0 | 0 | 7.4s |
| ssz-trajectories | 63 | 63 | 0 | 3.7s |
| segmented-energy | 0 | 0 | 0 | 5.7s |
| g79-cygnus-test | 0 | 0 | 0 | 11.9s |

## Models with Physical Meaning

### XI_MAX

**Physical Meaning:** Maximale Segmentdichte bei r → ∞ (Sättigung)

**Formula:** `Xi_max = 1 - exp(-PHI)`

**Value:** 0.801711184986333

**Stability:** STABLE

**Importance:** FUNDAMENTAL

### D_MIN

**Physical Meaning:** Minimale Distanz-Funktion bei r = r_s

**Formula:** `D_min = 1/(1+Xi_max)`

**Value:** 0.555032951154731

**Stability:** STABLE

**Importance:** FUNDAMENTAL

### PHI

**Physical Meaning:** Goldener Schnitt - fundamentale Strukturkonstante

**Formula:** `PHI = (1 + sqrt(5))/2`

**Value:** 1.618033988749895

**Stability:** STABLE

**Importance:** FUNDAMENTAL

### QUBIT_T_SSZ

**Physical Meaning:** SSZ-korrigierte Zeit für Qubit-Kohärenz

**Formula:** `T_corr = h/c * PHI`

**Stability:** STABLE

**Importance:** HIGH - Quantenkommunikation

### PPN_PARAMS

**Physical Meaning:** Post-Newtonian Parameter für Weak-Field

**Formula:** `β = 1, γ = 1 (GR exakt)`

**Value:** {'beta': 1.0, 'gamma': 1.0}

**Stability:** STABLE

**Importance:** CRITICAL - GR-Kompatibilität

### DUAL_VELOCITY

**Physical Meaning:** Invariante v_esc × v_fall = c²

**Formula:** `v_esc × v_fall = c²`

**Stability:** STABLE

**Importance:** CRITICAL - SSZ-Fundament

### CHORD_PARTITION

**Physical Meaning:** Hypothetische Moden-Struktur

**Formula:** `Mehrere parametrisierte Funktionen`

**Stability:** MIXED

**Importance:** HYPOTHESIS - Mathematisch stabil, physikalisch unverankert

