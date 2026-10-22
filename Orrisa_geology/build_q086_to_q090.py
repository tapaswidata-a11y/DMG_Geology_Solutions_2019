"""
Batch 6 Sub-batch 6C Masterclass Runner (Q086 - Q090)
Upgrades Q086 to Q090 to full Assam DGMS 2019 masterclass standard.
"""

import sys
from gen_q086 import generate_q086
from gen_q087 import generate_q087
from gen_q088 import generate_q088
from gen_q089 import generate_q089
from gen_q090 import generate_q090

def build_all():
    print("=" * 70)
    print("Executing Batch 6 Sub-batch 6C: Q086 to Q090")
    print("=" * 70)
    generate_q086()
    generate_q087()
    generate_q088()
    generate_q089()
    generate_q090()
    print("=" * 70)
    print("Successfully built Q086 to Q090!")
    print("=" * 70)

if __name__ == "__main__":
    build_all()
