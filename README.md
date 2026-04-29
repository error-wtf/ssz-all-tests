# SSZ All-Tests — Complete Validation Suite

**Authors:** Carmen N. Wrede & Lino P. Casu
**License:** Anti-Capitalist Software License v1.4
**Status:** [![CI](https://github.com/error-wtf/ssz-all-tests/actions/workflows/ci.yml/badge.svg)](https://github.com/error-wtf/ssz-all-tests/actions/workflows/ci.yml) ![Tests](https://img.shields.io/badge/tests-1296%2F1296-brightgreen) ![Pass Rate](https://img.shields.io/badge/pass_rate-100%25-brightgreen) ![Repos](https://img.shields.io/badge/repos-12-blue)

---

## What This Repository Does

This is the **central orchestration repository** for all SSZ (Segmented Spacetime) tests across the entire `error-wtf` organization.

- **Does NOT duplicate test code** — runs all tests directly from their source repositories
- **Uses native test runners** per repo: `pytest`, custom scripts, hybrid — whatever the repo actually uses
- **Generates structured output**: per-repo summaries, raw stdout/stderr, JSON status, integrity report
- **Canonical runner:** `run_all_live.py` (native runners, zero config)

---

## Quick Start

```bash
# Run all tests — native runner per repo
python run_all_live.py

# Generate complete verbose output with all test details
python gen_really_full_output.py

# Run chord-partition tests only (local, no deps)
python -m pytest test_chord_partition_modes.py -v
```

**Generated output files:**

| File | Contents |
|------|-----------|
| `LIVE_STATUS.json` | Current per-repo pass/fail snapshot |
| `full-output.md` | Per-repo summary: pass/fail counts |
| `really-full-output.md` | Complete untruncated verbose output per repo |
| `integrity-check.json` | Timestamp, verdict, zero-failure check |

---

## SSZ Key Constants

| Constant | Value | Derivation | Meaning |
|----------|-------|------------|---------|
| φ (phi) | 1.6180339887498949 | (1+√5)/2 | Golden ratio — SSZ saturation growth function |
| Ξ_max | 0.80171 | 1 − e^−φ | Maximum segment density at horizon |
| D_min | 0.55503 | 1/(1+Ξ_max) | Minimum time dilation factor (FINITE at r_s) |
| r*/r_s | 1.387 | Ξ_strong = Ξ_weak intersection | Universal strong-field regime boundary |
| r_ph/r_s | 1.595 | d/dr[D²/(s²r²)]=0 | SSZ photon sphere radius |
| N₀ | 4 | fundamental | Base segmentation number |
| r_s | 2GM/c² | Schwarzschild | Schwarzschild radius (SSZ uses this exactly) |

**Critical invariant:** GR predicts D(r_s) = 0 (singularity). SSZ predicts D(r_s) = **0.55503** (finite). This is the central falsifiable prediction.

---

## Repository Coverage — Live Test Results

Results from `run_all_live.py` — native runners per repo (Python 3.12, Windows 11, 2026-04-29):

| Repository | Type | Tests | Passed | Failed | Status | Physics Domain |
|-----------|------|-------|--------|--------|--------|----------------|
| [ssz-qubits](https://github.com/error-wtf/ssz-qubits) | CANONICAL | 184 | 184 | 0 | ✅ 100% | Quantum phase, GPS, Pound-Rebka, S2 star |
| [ssz-metric-pure](https://github.com/error-wtf/ssz-metric-pure) | CANONICAL | 36 | 36 | 0 | ✅ 100% | 4D metric tensor, Einstein/Ricci, Kerr analog |
| [segmented-calculation-suite](https://github.com/error-wtf/segmented-calculation-suite) | CANONICAL | 158 | 158 | 0 | ✅ 100% | Core Ξ engine, D(r), regime detection, C² blend |
| [ssz-schumann](https://github.com/error-wtf/ssz-schumann) | CANONICAL | 178 | 178 | 0 | ✅ 100% | Schumann resonance SSZ coupling |
| [ssz-lensing](https://github.com/error-wtf/ssz-lensing) | CANONICAL | 279 | 279 | 0 | ✅ 100% | Gravitational lensing (PPN null-geodesic) |
| [Unified-Results](https://github.com/error-wtf/Segmented-Spacetime-Mass-Projection-Unified-Results) | CANONICAL | 147 | 147 | 0 | ✅ 100% | Mass projection, wave modes, smoke validation |
| [ssz-trajectories](https://github.com/error-wtf/ssz-trajectories) | CANONICAL | 63 | 63 | 0 | ✅ 100% | Geodesic trajectory integration |
| [g79-cygnus-tests](https://github.com/error-wtf/g79-cygnus-tests) | CANONICAL | 5 | 5 | 0 | ✅ 100% | G79.29+0.46 LBV nebula, Cygnus X-1 |
| [ssz-lagrange](https://github.com/error-wtf/ssz-lagrange) | CANONICAL | 54 | 54 | 0 | ✅ 100% | Lagrange/Hamilton SSZ, Kerr analog |
| [segmented-energy](https://github.com/error-wtf/segmented-energy) | CANONICAL | 7 | 7 | 0 | ✅ 100% | Stellar energy, 129 astronomical objects |
| [frequency-curvature-validation](https://github.com/error-wtf/frequency-curvature-validation) | CANONICAL | 82 | 82 | 0 | ✅ 100% | PPN, Shapiro, Cassini, dynamic loops |
| chord-partition *(this repo)* | LOCAL | 103 | 103 | 0 | ✅ 100% | Eigenmodes, golden ratio φ resonance |
| **TOTAL** | | **1296** | **1296** | **0** | **✅ 100%** | |

**Archive repos (no executable tests):** `ssz-complete-documentation`, `SEGMENTED_SPACETIME`, `emergent-spacetime`, `Segmented-Spacetime-Starmaps`

---

## Repo Classification System

| Type | Meaning | Failures |
|------|---------|---------|
| **CANONICAL** | Official SSZ implementation — single source of truth | Real bugs |
| **LOCAL** | Tests living inside this repo (`ssz-all-tests`) | Real bugs |
| **ARCHIVE** | Historical reference — not actively maintained | Ignored |

---

## SSZ Physics: Method Assignment

**Critical rule:** Observable type determines method. Never mix.

| Observable | Geodesic Type | Method | Formula |
|-----------|--------------|--------|---------|
| Time dilation | time-like (static) | Ξ | D(r) = 1/(1+Ξ(r)) |
| Gravitational redshift | time-like (static) | Ξ | z = Ξ(r) |
| Frequency shift | time-like (static) | Ξ | ν_obs = ν_emit × D(r) |
| **Gravitational lensing** | **null (ds²=0)** | **PPN** | **α = (1+γ)·r_s/b** |
| **Shapiro delay** | **null (ds²=0)** | **PPN** | **Δt = (1+γ)·r_s/c·ln(...)** |
| Perihelion precession | massive orbit | PPN | standard β,γ |

**Mnemonic:** Clocks → Ξ. Light → PPN. Orbits → PPN.

### Ξ Formulas by Regime

| Regime | r/r_s range | Formula | Note |
|--------|-------------|---------|------|
| Weak | > 10 | Ξ = r_s/(2r) | Newtonian limit |
| Blend | 1.8 – 2.2 | Hermite C² interpolation | Smooth, differentiable |
| Strong / very_close | < 1.8 | Ξ = min(1 − exp(−φ·r_s/r), Ξ_max) | Saturates at Ξ_max |
| **DEPRECATED** | any | ~~Ξ = (r_s/r)² · exp(−r/r_φ)~~ | **Hard-fail — do not use** |

**PPN parameters:** γ = β = 1 exactly (SSZ is PPN-identical to GR in weak field).

---

## Validated Experiments

| Experiment | SSZ Result | Measured | Agreement |
|-----------|-----------|----------|-----------|
| GPS gravitational drift | 45.9 μs/day (GR component) | 45.9 μs/day | ✅ exact |
| GPS net drift (GR − SR) | 38.7 μs/day | 38.4 μs/day | ✅ 0.8% |
| Pound-Rebka (1960) | 2.46×10⁻¹⁵ | (2.57±0.26)×10⁻¹⁵ | ✅ within 1σ |
| Mercury perihelion | 42.99″/century | 43.1″/century | ✅ 0.2% |
| Cassini Shapiro delay | γ = 1.000021 ± 0.000023 | γ = 1.000021 ± 0.000023 | ✅ exact |
| S2 star (Sgr A*) redshift | z = 0.00198 | z = 0.00198 | ✅ exact |
| Cygnus X-1 (G79.29+0.46) | 6/6 predictions | 6/6 confirmed | ✅ all confirmed |
| Neutron star redshift | +13% vs GR | pending ATHENA/XMM | 🔬 falsifiable |
| Pulsar timing deviation | +30% vs GR | pending NANOGrav | 🔬 falsifiable |

---

## Falsifiable Predictions (SSZ ≠ GR)

| Prediction | SSZ value | GR value | Δ | Instrument | Timeline |
|-----------|-----------|----------|---|-----------|----------|
| D(r_s) at BH horizon | **0.55503** (finite) | **0** (diverges) | ∞ | EHT shadow | now |
| NS surface redshift | z_NS + 13% | z_GR | +13% | XMM-Newton / ATHENA | 2025–2030 |
| Pulsar timing | +30% | standard | +30% | NANOGrav | 2026–2030 |
| BH shadow size | −1.3% | r_sh=3√3/2·r_s | −1.3% | EHT ngEHT | 2026+ |

**SSZ is falsified if any of these measurements agree with GR.**

---

## Chord-Partition Eigenmodes (103 tests)

Parametric chord-partition curves with φ-scaling — 103 local tests in `test_chord_partition_modes.py`:

```
C(t; p, k, R) = (R·cos(p·t), R·sin(k·t))
```

| Parameter | Definition |
|-----------|-----------|
| p, k | winding numbers (integers ≥ 1) |
| Period | T = 2π·lcm(p,k)/p |
| Eigenmode index | n = lcm(p,k)/gcd(p,k) |
| φ-resonance | Fibonacci pairs (5,8), (8,13), (13,21) → φ |

SSZ constants verified in chord-partition tests:
- Ξ_max = 1 − e^−φ = 0.80171 ✅
- D_min = 1/(1+Ξ_max) = 0.55503 ✅
- φ² = φ+1 ✅
- N₀ = 4 ✅

Run independently:
```bash
python -m pytest test_chord_partition_modes.py -v
```

---

## File Structure

```
ssz-all-tests/
├── run_all_live.py               # CANONICAL RUNNER — native runners per repo
├── gen_really_full_output.py     # Verbose full output generator
├── test_chord_partition_modes.py # 103 chord-partition eigenmode tests (local)
│
├── LIVE_STATUS.json              # Per-repo pass/fail snapshot (auto-generated)
├── full-output.md                # Per-repo summary report (auto-generated)
├── really-full-output.md         # Complete verbose output per repo (auto-generated)
├── integrity-check.json          # Timestamp, verdict, zero-failure check (auto-generated)
│
├── tests/                        # Additional SSZ physics tests
├── aggregated/                   # Aggregated test copies (reference snapshots)
├── requirements.txt              # Python dependencies
└── .gitignore                    # __pycache__/, *.pyc excluded
```

---

## Dependencies

```
numpy>=1.21.0
scipy>=1.7.0
pytest>=7.0.0
pytest-cov>=3.0.0
matplotlib>=3.5.0
pandas>=1.3.0
astropy>=5.0.0
h5py>=3.6.0
tqdm>=4.62.0
numba>=0.56.0
```

Install: `pip install -r requirements.txt`

---

## Running Individual Repos

Repos are expected at `E:/clone/<repo-name>` (configurable in `run_all_live.py` via `BASE`):

```bash
# ssz-qubits (184 tests)
python -m pytest E:/clone/ssz-qubits/tests/ -v

# ssz-lensing (279 tests)
python -m pytest E:/clone/ssz-lensing/tests/ -v

# ssz-trajectories (63 tests)
python -m pytest E:/clone/ssz-trajectories/tests/ -v

# frequency-curvature-validation (82 tests — via wrapper)
python E:/clone/frequency-curvature-validation/run_all_tests.py

# ssz-schumann (178 tests — pytest + custom script)
python -m pytest E:/clone/ssz-schuhman-experiment/tests/ -v
python E:/clone/ssz-schuhman-experiment/run_all_ssz_tests.py

# ssz-lagrange (54 checks — custom runner)
python E:/clone/ssz-lagrange/test_lagrange_ssz.py

# g79-cygnus-tests (5 checks — custom runner)
python E:/clone/g79-cygnus-test/RUN_ALL_VALIDATED_TESTS.py

# chord-partition (103 tests — local, no deps)
python -m pytest test_chord_partition_modes.py -v
```

---

## License

Anti-Capitalist Software License v1.4
Copyright © 2025–2026 Carmen N. Wrede & Lino P. Casu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software,
to use, copy, modify, and distribute it for non-commercial purposes.

---

*Last updated: 2026-06-01 | Run: Python 3.12 / Windows 11 | 1296/1296 passed / 0 failures / 100.0%*
