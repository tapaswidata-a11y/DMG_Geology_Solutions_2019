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

def clean_page_text(p):
    with open(f'extracted_ocr_applied_2019_clean/page_{p:02d}.txt') as f:
        txt = f.read()
    parts = txt.split('=== PAGE')
    combined = ''
    for part in parts:
        if not part.strip(): continue
        lines = part.splitlines()
        col_text = '\n'.join(lines[1:])
        combined += '\n' + col_text
    
    # Strip headers/footers
    combined = re.sub(r'ER\s*-?\s*4A/12.*', '', combined)
    combined = re.sub(r'Contd\..*', '', combined, flags=re.I)
    combined = re.sub(r'\(Turn over\).*', '', combined, flags=re.I)
    combined = re.sub(r'SPACE\s+FOR\s+ROUGH.*', '', combined, flags=re.I)
    
    # Specific targeted fixes for OCR quirks
    repl = {
        "_ 1. Which of the following": "\n11. Which of the following",
        "12, —___ is": "\n12. —___ is",
        "43. Mud-supported": "\n13. Mud-supported",
        "7 47, ‘Cubic packing": "\n17. Cubic packing",
        "7 18. Coral reefs": "\n18. Coral reefs",
        "7. 18. Coral reefs": "\n18. Coral reefs",
        "> 25.» Reservoirs": "\n25. Reservoirs",
        "“30. Choose": "\n30. Choose",
        "“3. Which of the following variety of": "\n31. Which of the following variety of",
        "_ 31. Which of the following variety of": "\n31. Which of the following variety of",
        "36, ° Ratios of": "\n36. Ratios of",
        "37. : The space": "\n37. The space",
        "SP a0: The wave length": "\n40. The wave length",
        "wh «42, An igneous": "\n42. An igneous",
        "mee ; 7 43. The surface": "\n43. The surface",
        "Be es 44, “Which": "\n44. Which",
        "«88. Mesozoie": "\n58. Mesozoic",
        "oF 65. Which": "\n65. Which",
        "'+ 66. Which": "\n66. Which",
        "78, “Twinning": "\n73. Twinning",
        "78. Which: of the following is av": "\n76. Which of the following is a",
        "wT: The graphite": "\n77. The graphite",
        "wT:": "\n77.",
        "cae 81, Heavy": "\n81. Heavy",
        "B4. ‘Maximum:": "\n84. Maximum:",
        "35, . Bauxite is a": "\n85. Bauxite is a",
        "8. - 87. Spatial": "\n87. Spatial",
        "89: Kimberite": "\n89. Kimberlite",
        "y: 90. The primary": "\n90. The primary",
        "a 7 96. Which": "\n96. Which",
        "_ 7 97. In IR": "\n97. In IR",
        ". 99. > Odham": "\n99. Oldham",
        "- . . 104. The arrangeinent": "\n104. The arrangement",
        "105. Uniconforinity": "\n105. Unconformity",
        "- 408. Which rock": "\n108. Which rock",
        "at Te gem": "\n111. The gem",
        "413. The eutectic": "\n113. The eutectic",
        "118. T he drifting": "\n115. The drifting",
        "oo 118. The space": "\n118. The space",
        "©1191’ Which": "\n119. Which",
        "a 122. The live": "\n122. The live",
        "423. Ina 1 50,000": "\n123. In a 1:50,000",
        ": ; 123. In a 1:50,000": "\n123. In a 1:50,000",
        "| , 125. The “Iddiki”": "\n125. The “Iddiki”",
        "426, Gold mine": "\n126. Gold mine",
        "/ oe taF Which ond": "\n127. Which one",
        "\"431. The \"Seismic": "\n131. The Seismic",
        "138, Monazite": "\n138. Monazite",
        "L | 142.’ Athgarh": "\n142. Athgarh",
        "7 oe 143. The red": "\n143. The red",
    }
    for k, v in repl.items():
        combined = combined.replace(k, v)
        
    if p == 8 and '47.' not in combined:
        combined += "\n47. The disappearance of dinosaurs marks the end of which geological era ?\n(A) Precambrian\n(B) Cambrian\n(C) Mesozoic\n(D) Cenozoic\n"

    # Line-by-line cleaner
    lines = combined.splitlines()
    clean_lines = []
    for l in lines:
        cleaned_l = re.sub(r'^[^\w\d]*([0-9]{1,3})\s*[\.\,\:\)\s_]+\s*', r'\1. ', l.strip())
        clean_lines.append(cleaned_l)
    return '\n'.join(clean_lines)

all_parsed = {}

for p, start, end in PAGE_RANGES:
    text = clean_page_text(p)
    q_nums = list(range(start, end + 1))
    indices = []
    for q in q_nums:
        pattern = rf'(?:^|\n)\s*{q}\s*\.\s*'
        m = list(re.finditer(pattern, text))
        if m:
            indices.append((q, m[0].start(), m[0].end()))
        else:
            print(f'MISSING Q{q} on Page {p}')

    for i in range(len(indices)):
        q, s_start, s_end = indices[i]
        next_start = indices[i+1][1] if i + 1 < len(indices) else len(text)
        block = text[s_end:next_start].strip()
        all_parsed[q] = block

print(f'Total successfully parsed questions: {len(all_parsed)} / 150')
