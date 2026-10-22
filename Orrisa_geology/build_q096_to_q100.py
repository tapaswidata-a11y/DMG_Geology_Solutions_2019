"""
Batch 6 Sub-batch 6E Masterclass Runner (Q096 - Q100)
Upgrades Q096 to Q100 to full Assam DGMS 2019 masterclass standard.
"""

from gen_q096 import generate_q096
from gen_q097 import generate_q097
from gen_q098 import generate_q098
from gen_q099 import generate_q099
from gen_q100 import generate_q100

def build_all():
    print("=" * 70)
    print("Executing Batch 6 Sub-batch 6E: Q096 to Q100")
    print("=" * 70)
    generate_q096()
    generate_q097()
    generate_q098()
    generate_q099()
    generate_q100()
    print("=" * 70)
    print("Successfully built Q096 to Q100!")
    print("=" * 70)

if __name__ == "__main__":
    build_all()
