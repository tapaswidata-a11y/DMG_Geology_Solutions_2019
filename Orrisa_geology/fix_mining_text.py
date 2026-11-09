import subprocess, os, pytesseract, re
from PIL import Image

pdf = '/home/tapaswi/Mines_Geology/Orrisa_geology/Mining Officer Applied Geology P_II.pdf'
out_dir = '/home/tapaswi/Mines_Geology/Orrisa_geology/extracted_ocr_mining_2021'

# Fix page 13
subprocess.run(['pdftoppm', '-png', '-r', '200', '-f', '13', '-l', '13', pdf, f'{out_dir}/p13_fix'], check=True)
fname = f'{out_dir}/p13_fix-13.png'
im = Image.open(fname)
w, h = im.size
left = im.crop((30, 70, 750, h - 70))
right = im.crop((750, 70, w - 20, h - 70))
txt_l = pytesseract.image_to_string(left, config='--psm 6')
txt_r = pytesseract.image_to_string(right, config='--psm 6')
combined = f'=== PAGE 13 LEFT ===\n{txt_l}\n=== PAGE 13 RIGHT ===\n{txt_r}\n'
with open(f'{out_dir}/page_13.txt', 'w') as f:
    f.write(combined)
if os.path.exists(fname):
    os.remove(fname)

# Recompile full text
all_text = []
for p in range(2, 24):
    with open(f'{out_dir}/page_{p:02d}.txt') as f:
        all_text.append(f.read())

full_str = '\n'.join(all_text)
# Normalize known OCR quirks
full_str = re.sub(r'(?:^|\n)\s*4\.\s+Tornadoes', '\n1. Tornadoes', full_str)
full_str = re.sub(r'(?:^|\n)\s*44,\s+Which\s+of', '\n14. Which of', full_str)
full_str = re.sub(r'(?:^|\n)\s*[‘\'`]?\s*54\.\s+It\s+is', '\n54. It is', full_str)
full_str = re.sub(r'(?:^|\n)\s*:\s*62\.\s+Inadip', '\n62. In a dip', full_str)
full_str = re.sub(r'(?:^|\n)\s*428\.\s+Which\s+one', '\n128. Which one', full_str)

with open(f'{out_dir}/full_mining_2021_text.txt', 'w') as f:
    f.write(full_str)

pattern = r'(?:\n|^)\s*(\d{1,3})\s*[\.\)]\s+'
splits = re.split(pattern, full_str)
parsed = {}
for i in range(1, len(splits), 2):
    q_num = int(splits[i])
    q_body = splits[i+1].strip()
    if 1 <= q_num <= 150 and q_num not in parsed:
        parsed[q_num] = q_body

print(f'Total parsed questions: {len(parsed)} / 150')
missing = set(range(1, 151)) - set(parsed.keys())
print('Missing:', missing)
