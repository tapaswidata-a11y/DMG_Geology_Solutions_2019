import re
import os

with open('extracted_ocr/geology_2021/full_text.txt', 'r', encoding='utf-8') as f:
    full_text = f.read()

# Let's inspect the questions from 76 to 150
# Questions typically start with number followed by . or )
pattern = re.compile(r'(\n\s*(\d{1,3})\s*[\.\)]\s+)', re.MULTILINE)
matches = list(pattern.finditer(full_text))

q_dict = {}
for i in range(len(matches)):
    q_num = int(matches[i].group(2))
    start_pos = matches[i].start()
    end_pos = matches[i+1].start() if i+1 < len(matches) else len(full_text)
    q_text = full_text[start_pos:end_pos].strip()
    if 76 <= q_num <= 150:
        q_dict[q_num] = q_text

print(f"Parsed {len(q_dict)} questions from 76 to 150 in full_text.txt")
missing = [q for q in range(76, 151) if q not in q_dict]
print(f"Missing question numbers: {missing}")

for q in sorted(q_dict.keys())[:15]:
    print(f"\n--- Q{q} ---")
    print(q_dict[q][:250])

