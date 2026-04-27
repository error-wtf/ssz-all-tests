# -*- coding: utf-8 -*-
# =============================================================================
# SOURCE: Unified-Results
# ORIGINAL PATH: e:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results\scripts\tests\test_plot_ssz_maps.py
# AGGREGATED: 2026-04-27T20:52:58.168261
# =============================================================================
# This file was automatically aggregated from the SSZ repository.
# Do not modify - changes will be lost on next aggregation.
# =============================================================================

import pandas as pd
from pathlib import Path
from scripts.viz.plot_ssz_maps import plot_mollweide, VizConfig


def _dummy_cfg(tmp_path: Path) -> VizConfig:
    return VizConfig(run_id="test", cosmology_field=tmp_path / "dummy.parquet", viz_dir=tmp_path)


def test_plot_mollweide_handles_nan(tmp_path: Path):
    df = pd.DataFrame({"l_deg": [float("nan")]*5, "b_deg": [float("nan")]*5})
    out = tmp_path / "moll.png"
    cfg = _dummy_cfg(tmp_path)
    cfg.viz_dir = tmp_path
    result = plot_mollweide(df, cfg)
    assert result.exists()


def test_plot_mollweide_derives_galactic(tmp_path: Path):
    df = pd.DataFrame({"ra": [10, 20, 30], "dec": [-5, 0, 5]})
    cfg = _dummy_cfg(tmp_path)
    cfg.viz_dir = tmp_path
    result = plot_mollweide(df, cfg)
    assert result.exists()
