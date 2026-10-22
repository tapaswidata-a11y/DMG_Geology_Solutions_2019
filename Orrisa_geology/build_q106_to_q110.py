"""
Batch 7 Sub-batch 7B Masterclass Runner (Q106 - Q110)
Upgrades Q106 to Q110 to full Assam DGMS 2019 masterclass standard.
"""

from gen_q106 import generate_q106
from gen_q107 import generate_q107
from gen_q108 import generate_q108
from gen_q109 import generate_q109
from gen_q110 import generate_q110

def build_all():
    print("=" * 70)
    print("Executing Batch 7 Sub-batch 7B: Q106 to Q110")
    print("=" * 70)
    generate_q106()
    generate_q107()
    generate_q108()
    generate_q109()
    generate_q110()
    print("=" * 70)
    print("Successfully built Q106 to Q110!")
    print("=" * 70)

if __name__ == "__main__":
    build_all()
