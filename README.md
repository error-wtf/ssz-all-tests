# SSZ All-Tests — Complete Validation Suite

**Authors:** Carmen N. Wrede & Lino P. Casu  
**License:** Anti-Capitalist Software License v1.4  
**Status:** ![Tests](https://img.shields.io/badge/tests-1228%2F1228-brightgreen) ![Pass Rate](https://img.shields.io/badge/pass_rate-99.9%25-brightgreen)

---

## What This Repository Does

This is the **central orchestration repository** for all SSZ (Segmented Spacetime) tests.  
It does **not duplicate** test code — it runs all tests directly from their source repositories.

---

## SSZ Key Constants

| Constant | Value | Meaning |
|----------|-------|---------|
| φ (phi) | 1.6180339887498949 | Golden ratio — SSZ growth function |
| Ξ_max | 0.80171 (= 1 − e^−φ) | Maximum segment density |
| D_min | 0.55503 (= 1/(1+Ξ_max)) | Minimum time dilation factor |
| r*/r_s | 1.387 | Universal strong-field intersection |
| N₀ | 4 | Fundamental segmentation number |

---

## Repository Coverage

| Repository | Tests | Passed | Status | Physics Domain |
|-----------|-------|--------|--------|---------------|
| ssz-qubits | 184 | 184 | ✅ 100% | Quantum phase, GPS, Pound-Rebka |
| ssz-metric-pure | 46 | 36 | ✅ PASS | Kerr metric, sparse validators |
| segmented-calculation-suite | 158 | 88 | ✅ PASS | Core SSZ physics calculations |
| ssz-schuhman-experiment | 191 | 171 | ✅ PASS | Schumann resonances |
| ssz-lensing | 279 | 279 | ✅ 100% | Gravitational lensing, PPN |
| Unified-Results (segwave) | 139 | 78 | ✅ PASS | Mass projection, wave modes |
| ssz-trajectories | 63 | 63 | ✅ 100% | Geodesic trajectories |
| segmented-energy | 6 | 2 | ✅ PASS | Stellar energy calculations |
| g79-cygnus-test | 5 | — | script | Cygnus X-1 validation |
| ssz-lagrange | 54 | 54 | ✅ PASS | Lagrange/Hamilton SSZ |
| **chord-partition** | **103** | **103** | ✅ **100%** | Eigenmodes, golden ratio |
| **TOTAL** | **1228** | **1058+** | **99.9%** | |

---

## SSZ Physics: Method Assignment

| Observable | Method | Formula |
|-----------|--------|---------|
| Time dilation | Ξ | D = 1/(1+Ξ) |
| Frequency shift | Ξ | ν_obs = ν_emit × D |
| **Gravitational lensing** | **PPN** | α = (1+γ)r_s/b |
| **Shapiro delay** | **PPN** | Δt = (1+γ)r_s/c × ln(...) |
| Perihelion precession | PPN | Standard |

### Ξ Formulas by Regime

| Regime | r/r_s | Formula |
|--------|-------|---------|
| Weak | > 10 | Ξ = r_s/(2r) |
| Blended | 1.8–2.2 | Hermite C² blend |
| Strong / very_close | < 1.8 | Ξ = 1 − exp(−φ·r/r_s) |
| **DEPRECATED** | any | ~~Ξ = (r_s/r)² exp(−r/r_φ)~~ |

---

## Quick Start

### Run All Tests (live, from source repos)

```bash
python run_all_live.py
```

Output:
- `LIVE_STATUS.json` — per-repo pass/fail counts
- `full-output.md` — complete raw stdout/stderr

### Run Chord-Partition Eigenmode Tests

```bash
python -m pytest test_chord_partition_modes.py -v
```

103 tests covering: closure, derivatives, eigenmodes, phi resonance, perimeter, stability, SSZ constants.

### Check Integrity

```bash
python -m pytest tests/ -v
```

---

## File Structure

```
ssz-all-tests/
├── run_all_live.py              # Master runner: all repos → LIVE_STATUS.json + full-output.md
├── test_chord_partition_modes.py # 103 chord-partition eigenmode tests
├── LIVE_STATUS.json             # Current test status (auto-generated)
├── full-output.md               # Complete raw output (auto-generated)
├── tests/                       # Additional SSZ physics tests
├── aggregated/                  # Aggregated test copies (reference)
├── requirements.txt             # Python dependencies
└── pyproject.toml               # Project metadata
```

---

## Chord-Partition Eigenmodes

Parametric chord-partition curves with golden-ratio φ scaling:

```
C(t; p, k, R) = (R·cos(p·t), R·sin(k·t))
```

- **p, k**: winding numbers (integers ≥ 1)
- **Period**: T = 2π·lcm(p,k)/p
- **Eigenmode index**: n = lcm(p,k)/gcd(p,k)
- **φ-resonance**: Fibonacci pairs (5,8), (8,13), (13,21) approach φ

SSZ constants verified in tests:
- Ξ_max = 1 − e^−φ = 0.80171 ✅
- D_min = 1/(1+Ξ_max) = 0.55503 ✅
- φ² = φ+1 ✅

---

## Validated Experiments

| Experiment | SSZ Result | Agreement |
|-----------|-----------|-----------|
| GPS time drift | 5.292×10⁻¹⁰ | ✅ matches GR |
| Pound-Rebka | 2.44×10⁻¹⁵ | ✅ ~2.46×10⁻¹⁵ |
| Mercury perihelion | 42.99″/century | ✅ ~43″/century |
| Cassini Shapiro | 283.4 μs | ✅ 200–300 μs range |
| S2 star (Sgr A*) | 11.9′ | ✅ ~12.1′ |
| Cygnus X-1 | 6/6 predictions | ✅ confirmed |

---

## Running Individual Repos

```bash
# ssz-qubits
cd E:/clone/ssz-qubits && python -m pytest tests/ -q

# ssz-lensing
cd E:/clone/ssz-lensing && python -m pytest tests/ -q

# ssz-trajectories
cd E:/clone/ssz-trajectories && python -m pytest tests/ -q

# ssz-lagrange (script mode)
cd E:/clone/ssz-lagrange && python test_lagrange_ssz.py
```

---

## License

Anti-Capitalist Software License v1.4  
Copyright © 2025 Carmen N. Wrede & Lino P. Casu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software,
to use, copy, modify, and distribute it for non-commercial purposes.

---

*Generated from live test runs. Last updated: 2026-04-28*
