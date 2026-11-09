import re, json

PAGE_RANGES = [
    (2, 1, 8),
    (3, 9, 15),
    (4, 16, 22),
    (5, 23, 28),
    (6, 29, 34),
    (7, 35, 40),
    (8, 41, 47),
    (9, 48, 54),
    (10, 55, 62),
    (11, 63, 69),
    (12, 70, 77),
    (13, 78, 85),
    (14, 86, 93),
    (15, 94, 101),
    (16, 102, 108),
    (17, 109, 115),
    (18, 116, 123),
    (19, 124, 131),
    (20, 132, 139),
    (21, 140, 147),
    (22, 148, 150),
]

def clean_page(p):
    with open(f'extracted_ocr_applied_2019_clean/page_{p:02d}.txt') as f:
        txt = f.read()
    # Left column then Right column
    parts = txt.split('=== PAGE')
    combined = ''
    for part in parts:
        if not part.strip(): continue
        lines = part.splitlines()
        # strip header line
        col_text = '\n'.join(lines[1:])
        combined += '\n' + col_text
    
    # Clean unwanted footers / headers
    combined = re.sub(r'ER\s*-?\s*4A/12.*', '', combined)
    combined = re.sub(r'Contd\..*', '', combined, flags=re.I)
    combined = re.sub(r'\(Turn over\).*', '', combined, flags=re.I)
    combined = re.sub(r'SPACE\s+FOR\s+ROUGH.*', '', combined, flags=re.I)
    return combined

all_pages_clean = {}
for p, s, e in PAGE_RANGES:
    all_pages_clean[p] = clean_page(p)

print('Cleaned pages loaded.')
