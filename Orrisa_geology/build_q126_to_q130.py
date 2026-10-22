#!/usr/bin/env python3
"""
Runner script to regenerate Q126 to Q130 and update index.html
"""
import sys
from gen_q126 import generate_q126
from gen_q127 import generate_q127
from gen_q128 import generate_q128
from gen_q129 import generate_q129
from gen_q130 import generate_q130
import subprocess

def main():
    print("Building Q126 to Q130 Masterclass Guides...")
    generate_q126()
    generate_q127()
    generate_q128()
    generate_q129()
    generate_q130()
    print("All 5 guides in Sub-batch 8B generated successfully!")

    print("Rebuilding master portal index.html...")
    res = subprocess.run(["python3", "build_assam_style_portal.py"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("Error compiling portal:", res.stderr)
        sys.exit(1)
    print("Portal compiled successfully!")

if __name__ == "__main__":
    main()
