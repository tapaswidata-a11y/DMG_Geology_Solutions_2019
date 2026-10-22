#!/usr/bin/env python3
"""
Runner script to regenerate Q136 to Q140 and update index.html
"""
import sys
from gen_q136 import generate_q136
from gen_q137 import generate_q137
from gen_q138 import generate_q138
from gen_q139 import generate_q139
from gen_q140 import generate_q140
import subprocess

def main():
    print("Building Q136 to Q140 Masterclass Guides...")
    generate_q136()
    generate_q137()
    generate_q138()
    generate_q139()
    generate_q140()
    print("All 5 guides in Sub-batch 9A generated successfully!")

    print("Rebuilding master portal index.html...")
    res = subprocess.run(["python3", "build_assam_style_portal.py"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("Error compiling portal:", res.stderr)
        sys.exit(1)
    print("Portal compiled successfully!")

if __name__ == "__main__":
    main()
