"""
Batch 7 Sub-batch 7A Masterclass Runner (Q101 - Q105)
Upgrades Q101 to Q105 to full Assam DGMS 2019 masterclass standard.
"""

from gen_q101 import generate_q101
from gen_q102 import generate_q102
from gen_q103 import generate_q103
from gen_q104 import generate_q104
from gen_q105 import generate_q105

def build_all():
    print("=" * 70)
    print("Executing Batch 7 Sub-batch 7A: Q101 to Q105")
    print("=" * 70)
    generate_q101()
    generate_q102()
    generate_q103()
    generate_q104()
    generate_q105()
    print("=" * 70)
    print("Successfully built Q101 to Q105!")
    print("=" * 70)

if __name__ == "__main__":
    build_all()
