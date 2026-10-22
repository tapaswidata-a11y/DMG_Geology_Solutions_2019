"""
Batch 7 Sub-batch 7C Masterclass Runner (Q111 - Q115)
Upgrades Q111 to Q115 to full Assam DGMS 2019 masterclass standard.
"""

from gen_q111 import generate_q111
from gen_q112 import generate_q112
from gen_q113 import generate_q113
from gen_q114 import generate_q114
from gen_q115 import generate_q115

def build_all():
    print("=" * 70)
    print("Executing Batch 7 Sub-batch 7C: Q111 to Q115")
    print("=" * 70)
    generate_q111()
    generate_q112()
    generate_q113()
    generate_q114()
    generate_q115()
    print("=" * 70)
    print("Successfully built Q111 to Q115!")
    print("=" * 70)

if __name__ == "__main__":
    build_all()
