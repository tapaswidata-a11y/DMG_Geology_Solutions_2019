#!/usr/bin/env python3
"""
Runner script to regenerate Q146 to Q150 and update index.html
Completes the entire 150-question Masterclass project (100% coverage)!
"""
import sys
from gen_q146 import generate_q146
from gen_q147 import generate_q147
from gen_q148 import generate_q148
from gen_q149 import generate_q149
from gen_q150 import generate_q150
import subprocess

def main():
    print("Building Q146 to Q150 Masterclass Guides (The Final Sub-batch!)...")
    generate_q146()
    generate_q147()
    generate_q148()
    generate_q149()
    generate_q150()
    print("All 5 guides in Sub-batch 9C generated successfully!")

    print("Rebuilding master portal index.html with all 150 Masterclass questions...")
    res = subprocess.run(["python3", "build_assam_style_portal.py"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("Error compiling portal:", res.stderr)
        sys.exit(1)
    print("Master Portal index.html compiled successfully (150/150 Questions Live)!")

if __name__ == "__main__":
    main()
