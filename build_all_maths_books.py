#!/usr/bin/env python3
"""
Master Builder for Master Functional Skills Mathematics Publications
Builds:
  1. Maths Level 2 Core Study Guide (48 pages)
  2. Maths Level 2 Companion Practice Workbook (60 pages)
  3. Maths Level 1 Core Revision Guide (46 pages)
  4. Maths Level 1 Companion Practice Workbook (56 pages)

Outputs to:
  - assets/downloads/
  - ~/Documents/
"""
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
SCRIPTS = [
    ("Maths Level 2 Core Study Guide", BASE_DIR / "generate_maths_l2_core_guide.py"),
    ("Maths Level 2 Companion Practice Workbook", BASE_DIR / "generate_maths_l2_companion_workbook.py"),
    ("Maths Level 1 Core Revision Guide", BASE_DIR / "generate_maths_l1_core_guide.py"),
    ("Maths Level 1 Companion Practice Workbook", BASE_DIR / "generate_maths_l1_companion_workbook.py"),
]

def main():
    print("=" * 70)
    print("  Master Functional Skills - Maths Publications Master Build System")
    print("=" * 70)
    
    for title, script_path in SCRIPTS:
        if not script_path.exists():
            print(f"[ERROR] Script not found: {script_path}")
            sys.exit(1)
        
        print(f"\n>>> Compiling: {title} ({script_path.name})...")
        res = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"[FAIL] {title} failed with code {res.returncode}")
            print(res.stderr)
            sys.exit(res.returncode)
        else:
            print(res.stdout.strip())
            
    print("\n" + "=" * 70)
    print("  ALL 4 PUBLICATIONS SUCCESSFULLY GENERATED AND VERIFIED")
    print("=" * 70)

if __name__ == "__main__":
    main()
