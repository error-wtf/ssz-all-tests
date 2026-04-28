"""
Segmented-Energy Repository Fix
Resolves dataset path configuration
"""

import sys
import os
from pathlib import Path

# Repository root
repo_root = Path(__file__).parent

# Create data directory if missing
data_dir = repo_root / "data"
data_dir.mkdir(exist_ok=True)

# Create symlink or copy required datasets
required_datasets = [
    "observer_data_complete.csv",
    "observer_data_large.csv",
    "astronomical_systems.json",
]

for dataset in required_datasets:
    source = repo_root / dataset
    target = data_dir / dataset
    if source.exists() and not target.exists():
        try:
            import shutil
            shutil.copy2(source, target)
            print(f"✅ Copied {dataset} to data/")
        except Exception as e:
            print(f"⚠️  Could not copy {dataset}: {e}")

# Add data dir to path
sys.path.insert(0, str(repo_root))
os.environ['SSZ_DATA_PATH'] = str(data_dir)

print(f"✅ Segmented-Energy dataset fix applied")
print(f"Data path: {data_dir}")
