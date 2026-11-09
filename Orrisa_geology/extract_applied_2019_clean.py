import subprocess, os, pytesseract, re
from PIL import Image

pdf = '/home/tapaswi/Mines_Geology/Orrisa_geology/091819_Applied_Geology.pdf'
out_dir = '/home/tapaswi/Mines_Geology/Orrisa_geology/extracted_ocr_applied_2019_clean'
os.makedirs(out_dir, exist_ok=True)

def find_gutter(d):
    words = [(d['left'][i], d['left'][i] + d['width'][i]) for i in range(len(d['text'])) if d['text'][i].strip()]
    best_gap_x = 760
    max_gap = 0
    for split in range(700, 880, 5):
        intersecting = sum(1 for (l, r) in words if l < split < r)
        if intersecting == 0:
            left_dist = min([split - r for (l, r) in words if r <= split] or [999])
            right_dist = min([l - split for (l, r) in words if l >= split] or [999])
            gap = left_dist + right_dist
            if gap > max_gap:
                max_gap = gap
                best_gap_x = split
    return best_gap_x

all_text = []

for p in range(2, 24):
    prefix = f'{out_dir}/p{p:02d}'
    subprocess.run(['pdftoppm', '-png', '-r', '200', '-f', str(p), '-l', str(p), pdf, prefix], check=True)
    fname = f'{prefix}-{p:02d}.png'
    im = Image.open(fname)
    w, h = im.size
    d = pytesseract.image_to_data(im, output_type=pytesseract.Output.DICT)
    gutter = find_gutter(d)
    
    # Left column: wide margin from x=5 to gutter
    left_im = im.crop((5, 70, gutter - 5, h - 70))
    # Right column: from gutter to w-5
    right_im = im.crop((gutter + 5, 70, w - 5, h - 70))
    
    txt_l = pytesseract.image_to_string(left_im, config='--psm 6')
    txt_r = pytesseract.image_to_string(right_im, config='--psm 6')
    
    combined = f'=== PAGE {p} LEFT (gutter={gutter}) ===\n{txt_l}\n=== PAGE {p} RIGHT ===\n{txt_r}\n'
    all_text.append(combined)
    with open(f'{out_dir}/page_{p:02d}.txt', 'w') as f:
        f.write(combined)
    os.remove(fname)

full_str = '\n'.join(all_text)
with open(f'{out_dir}/full_applied_2019_text.txt', 'w') as f:
    f.write(full_str)

print('Clean extraction of 2019 Applied Geology done.')
