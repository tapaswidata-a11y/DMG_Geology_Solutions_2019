"""
Batch 6 Sub-batch 6D Masterclass Runner (Q091 - Q095)
Upgrades Q091 to Q095 to full Assam DGMS 2019 masterclass standard.
"""

from gen_q091 import generate_q091
from gen_q092 import generate_q092
from gen_q093 import generate_q093
from gen_q094 import generate_q094
from gen_q095 import generate_q095

def build_all():
    print("=" * 70)
    print("Executing Batch 6 Sub-batch 6D: Q091 to Q095")
    print("=" * 70)
    generate_q091()
    generate_q092()
    generate_q093()
    generate_q094()
    generate_q095()
    print("=" * 70)
    print("Successfully built Q091 to Q095!")
    print("=" * 70)

if __name__ == "__main__":
    build_all()
