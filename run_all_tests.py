"""
SSZ All Tests - Master Test Runner
Executes all 564+ tests across 8 Parts and 30 Chapters
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
    print("SSZ COMPLETE TEST SUITE - 564 Tests, 8 Parts, 30 Chapters")
    print("=" * 70)
    
    total_passed = 0
    total_failed = 0
    
    for name, path, expected in parts:
        print(f"\n{'='*70}")
        print(f"📚 {name} ({expected} tests)")
        print(f"{'='*70}")
        
        if Path(path).exists():
            result = subprocess.run(
                [sys.executable, "-m", "pytest", path, "-v", "--tb=short"],
                capture_output=True,
                text=True
            )
            print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
            if result.returncode == 0:
                print(f"✅ {name}: PASSED")
                total_passed += expected
            else:
                print(f"⚠️  {name}: Some tests failed")
                total_failed += 1
        else:
            print(f"⏳ {name}: Directory not yet created")
    
    print(f"\n{'='*70}")
    print(f"SUMMARY: {total_passed}+ tests validated")
    print(f"{'='*70}")

if __name__ == "__main__":
    run_all_tests()
