#!/usr/bin/env python3
"""
Runner script to regenerate Q131 to Q135 and update index.html
"""
import sys
from gen_q131 import generate_q131
from gen_q132 import generate_q132
from gen_q133 import generate_q133
from gen_q134 import generate_q134
from gen_q135 import generate_q135
import subprocess

def main():
    print("Building Q131 to Q135 Masterclass Guides...")
    generate_q131()
    generate_q132()
    generate_q133()
    generate_q134()
    generate_q135()
    print("All 5 guides in Sub-batch 8C generated successfully!")

    print("Rebuilding master portal index.html...")
    res = subprocess.run(["python3", "build_assam_style_portal.py"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("Error compiling portal:", res.stderr)
        sys.exit(1)
    print("Portal compiled successfully!")

if __name__ == "__main__":
    main()
