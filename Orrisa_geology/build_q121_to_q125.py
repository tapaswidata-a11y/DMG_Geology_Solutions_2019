#!/usr/bin/env python3
"""
Runner script to regenerate Q121 to Q125 and update index.html
"""
import sys
from gen_q121 import generate_q121
from gen_q122 import generate_q122
from gen_q123 import generate_q123
from gen_q124 import generate_q124
from gen_q125 import generate_q125
import subprocess

def main():
    print("Building Q121 to Q125 Masterclass Guides...")
    generate_q121()
    generate_q122()
    generate_q123()
    generate_q124()
    generate_q125()
    print("All 5 guides in Sub-batch 8A generated successfully!")

    print("Rebuilding master portal index.html...")
    res = subprocess.run(["python3", "build_assam_style_portal.py"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("Error compiling portal:", res.stderr)
        sys.exit(1)
    print("Portal compiled successfully!")

if __name__ == "__main__":
    main()
