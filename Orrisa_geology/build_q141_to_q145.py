#!/usr/bin/env python3
"""
Runner script to regenerate Q141 to Q145 and update index.html
"""
import sys
from gen_q141 import generate_q141
from gen_q142 import generate_q142
from gen_q143 import generate_q143
from gen_q144 import generate_q144
from gen_q145 import generate_q145
import subprocess

def main():
    print("Building Q141 to Q145 Masterclass Guides...")
    generate_q141()
    generate_q142()
    generate_q143()
    generate_q144()
    generate_q145()
    print("All 5 guides in Sub-batch 9B generated successfully!")

    print("Rebuilding master portal index.html...")
    res = subprocess.run(["python3", "build_assam_style_portal.py"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("Error compiling portal:", res.stderr)
        sys.exit(1)
    print("Portal compiled successfully!")

if __name__ == "__main__":
    main()
