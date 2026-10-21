import re

with open("qp_pages/full_ordered_text.txt") as f:
    text = f.read()

# Let's inspect pages 12, 13, 14, 15
for p in range(12, 16):
    print(f"==================== PAGE {p} ====================")
    with open(f"qp_pages/page_{p:02d}_combined.txt") as fp:
        print(fp.read())

