with open("/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter13_MetamorphicPetrology/full_ch13_text.txt") as f:
    text = f.read()

import re

# Let's inspect questions 1 to 20
for q in range(1, 21):
    m = re.search(rf'(?:^|\n)\s*{q}\s*[\.\)]\s*(.*?)(?=(?:\n\s*\d{{1,3}}\s*[\.\)]|\Z))', text, re.DOTALL)
    if m:
        first_line = m.group(1).strip().splitlines()[0]
        print(f"Q{q:03d}: {first_line[:75]}")
    else:
        print(f"Q{q:03d}: NOT FOUND DIRECTLY")
