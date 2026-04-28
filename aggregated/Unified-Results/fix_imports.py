"""
Unified-Results Repository Fix
Resolves import configuration issues
"""

import sys
import os
from pathlib import Path

# Add repository root to Python path
repo_root = Path(__file__).parent
sys.path.insert(0, str(repo_root))

# Create __init__.py files for package structure
init_files = [
    repo_root / "src" / "__init__.py",
    repo_root / "ssz" / "__init__.py",
    repo_root / "core" / "__init__.py",
]

for init_file in init_files:
    init_file.parent.mkdir(parents=True, exist_ok=True)
    if not init_file.exists():
        init_file.write_text('"""SSZ Unified-Results Package"""\n')

print("✅ Unified-Results import fix applied")
print(f"Python path: {sys.path[:3]}")
