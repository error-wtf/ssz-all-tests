"""
SSZ All Tests - Master Test Runner
Executes all SSZ physics tests across all parts
"""

import subprocess
import sys
from pathlib import Path


def run_all_tests():
    """Run complete test suite"""
    parts = [
        ("Part I: Foundations", "tests/part_I_foundations", 186),
        ("Part II: Kinematics", "tests/part_II_kinematics", 47),
        ("Part III: Electromagnetism", "tests/part_III_electromagnetism", 64),
        ("Part IV: Frequency Framework", "tests/part_IV_frequency", 28),
        ("Part V: Strong Field", "tests/part_V_strong_field", 94),
        ("Part VI: Astrophysics", "tests/part_VI_astrophysics", 14),
        ("Part VII: Dynamics", "tests/part_VII_dynamics", 54),
        ("Part VIII: Validation", "tests/part_VIII_validation", 77),
    ]

    print("=" * 70)
    print("SSZ COMPLETE TEST SUITE")
    print("=" * 70)

    total_passed = 0
    total_failed = 0

    for name, path, expected in parts:
        test_dir = Path(path)
        if not test_dir.exists():
            print(f"  SKIP {name}: directory not found")
            continue

        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_dir), "-v", "--tb=short"],
            capture_output=True, text=True, encoding='utf-8', errors='replace'
        )

        passed = result.stdout.count(" PASSED")
        failed = result.stdout.count(" FAILED")
        total_passed += passed
        total_failed += failed

        status = "✅" if failed == 0 else "❌"
        print(f"  {status} {name}: {passed} passed, {failed} failed")

    print("=" * 70)
    print(f"TOTAL: {total_passed} passed, {total_failed} failed")
    return total_failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
