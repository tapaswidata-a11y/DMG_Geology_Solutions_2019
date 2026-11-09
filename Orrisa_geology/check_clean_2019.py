import re

with open('/home/tapaswi/Mines_Geology/Orrisa_geology/extracted_ocr_applied_2019_clean/full_applied_2019_text.txt') as f:
    full_str = f.read()

# Strip footers
full_str = re.sub(r'ER\s*-4A/12.*', '', full_str)
full_str = re.sub(r'Contd\.', '', full_str, flags=re.I)
full_str = re.sub(r'===\s*PAGE.*===', '', full_str)

# Normalize punctuation before numbers
cleaned = re.sub(r'(?:^|\n)\s*[;:\'\"|~•*–-]*\s*(\d{1,3})\s*[:\.\)]\s*', r'\n\1. ', full_str)

pattern = r'(?:\n|^)\s*(\d{1,3})\s*\.\s+'
splits = re.split(pattern, cleaned)
parsed = {}
for i in range(1, len(splits), 2):
    q_num = int(splits[i])
    q_body = splits[i+1].strip()
    if 1 <= q_num <= 150 and q_num not in parsed:
        parsed[q_num] = q_body

print(f'Total questions parsed from 2019 Applied Geo: {len(parsed)} / 150')
missing = set(range(1, 151)) - set(parsed.keys())
print('Missing count:', len(missing))
print('Missing numbers:', sorted(list(missing)))
