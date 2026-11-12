import re

with open("/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter1_Geotectonics/combined_ch1_ocr.txt") as f:
    text = f.read()

# Only keep from "General Geology and Geotectonics"
start_idx = text.find("General Geology and Geotectonics")
if start_idx != -1:
    text = text[start_idx:]

# Remove page header lines
text = re.sub(r'---\s*PAGE\s*\d+\s*COL\s*\d+\s*---', '', text)
text = re.sub(r'Scanned by CamScanner', '', text)

# Find question numbers
pattern = r'(?:^|\n)\s*([*#]?\d{1,3})\s*[\.\)]\s*(.+?)(?=(?:\n\s*[*#]?\d{1,3}\s*[\.\)]\s*)|\Z)'
matches = re.findall(pattern, text, re.DOTALL)

print(f"Total question matches found: {len(matches)}")
found_nums = []
for q_str, q_body in matches:
    clean_num = int(re.sub(r'\D', '', q_str))
    found_nums.append(clean_num)

print(f"Unique question numbers: {len(set(found_nums))}")
print(f"Range: min={min(found_nums)}, max={max(found_nums)}")
missing = [i for i in range(1, 236) if i not in found_nums]
print(f"Missing question numbers count: {len(missing)}")
if missing:
    print(f"Missing list: {missing[:30]}...")
