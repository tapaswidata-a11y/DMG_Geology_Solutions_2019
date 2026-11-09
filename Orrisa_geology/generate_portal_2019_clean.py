import re, os
with open("build_mining_applied_2021_full_system.py", "r", encoding="utf-8") as f:
    code = f.read()

# Adapt from 2021 to 2019
code = code.replace("2021", "2019")
code = code.replace("GPGM - 5/20", "GGM - 4/2019")
code = code.replace("build_mining_applied_metadata", "build_applied_2019_metadata")
code = code.replace("META_TABLE_MINING_2021", "META_TABLE_APPLIED_2019")

# Replace data loading part
old_data_load = '''with open(os.path.join(BASE_DIR, "extracted_ocr_mining_2019", "full_mining_2019_text.txt"), "r", encoding="utf-8") as f:
    full_str = f.read()

# Strip footers and clean OCR quirks
full_str = re.sub(r'WA-\\s*6A/29\\s*[\\.:]?\\s*\\(\\s*\\d+\\s*\\)', '', full_str)
full_str = re.sub(r'\\(Turn over\\s*\\)', '', full_str, flags=re.I)
full_str = re.sub(r'Contd\\.', '', full_str, flags=re.I)
full_str = re.sub(r'===\\s*PAGE.*===', '', full_str)
full_str = re.sub(r'(?:\\n|^)\\s*\\d{1,2}\\s*\\)\\s*(?=\\n|$)', '', full_str)
full_str = re.sub(r'(?:\\n|^)\\s*\\(\\s*\\d+\\s*\\)\\s*(?=\\n|$)', '', full_str)
full_str = re.sub(r'\\(Cc\\)', '(C)', full_str)
full_str = re.sub(r'\\.\\s*8\\)', '(B)', full_str)

pattern = r'(?:\\n|^)\\s*(\\d{1,3})\\s*[\\.\\)]\\s+'
splits = re.split(pattern, full_str)
raw_questions = {}
for i in range(1, len(splits), 2):
    q_num = int(splits[i])
    q_body = splits[i+1].strip()
    if 1 <= q_num <= 150 and q_num not in raw_questions:
        raw_questions[q_num] = q_body

print(f"Extracted {len(raw_questions)} raw questions.")

def clean_ocr(text):
    text = " ".join(text.split())
    reps = {
        "Allof": "All of",
        "beween": "between",
        "Slunit": "SI unit",
        "palaeontology": "paleontology",
        "Admantine": "Adamantine",
        "Theplane": "The plane",
        "Inadip": "In a dip",
        "Inorderto": "In order to",
        "velue": "value",
        "Asperthe": "As per the",
        "Sending": "Sensing",
        "Spactal": "Spatial",
        "Ehcrypted": "Encrypted",
        "Whatis": "What is",
        "fribal": "friable",
        "Allofthese": "All of these"
    }
    for k, v in reps.items():
        text = text.replace(k, v)
    return text

dataset = []

for q_num in range(1, 151):
    body = raw_questions[q_num]
    body_clean = re.sub(r'WA-\\s*\\S+', '', body)
    body_clean = re.sub(r'\\(Turn over\\s*\\)', '', body_clean, flags=re.I)
    body_clean = re.sub(r'Contd\\.', '', body_clean, flags=re.I)
    body_clean = re.sub(r'===\\s*PAGE.*===', '', body_clean)
    body_clean = re.sub(r'\\(\\s*\\d+\\s*\\)', '', body_clean)
    
    opt_matches = re.findall(r'\\(([A-D])\\)\\s*([^(\\n]+(?:\\n(?!\([A-D]\))[^(\\n]+)*)', body_clean)
    opts = {letter: clean_ocr(' '.join(opt_txt.split()).strip()) for letter, opt_txt in opt_matches}
    q_text = clean_ocr(' '.join(re.split(r'\\([A-D]\\)', body_clean)[0].split()).strip())'''

new_data_load = '''import parse_all_applied_2019 as p
from test_explicit_overrides import EXPLICIT_OVERRIDE
from test_clean_options_2019 import parse_question_options, clean_ocr

all_qs = p.all_questions
dataset = []

for q_num in range(1, 151):
    raw_body = all_qs[q_num]
    q_stem, parsed_opts = parse_question_options(raw_body, q_num)
    if q_num in EXPLICIT_OVERRIDE:
        opts = EXPLICIT_OVERRIDE[q_num]
    else:
        opts = parsed_opts
    q_text = q_stem'''

code = code.replace(old_data_load, new_data_load)

# Fix year switcher active button in the template
code = code.replace(
    '<a href="index_mining_applied_2019.html" class="year-btn active" title="Odisha 2019 Mining Officer Applied Geology Paper-II (150 Live)">Mining 2019 (150)</a>\n        <a href="index_mining_applied_2019.html" class="year-btn inactive"',
    '<a href="index_mining_applied_2021.html" class="year-btn inactive" title="Odisha 2021 Mining Officer Applied Geology Paper-II (150 Live)">Mining 2021 (150)</a>\n        <a href="index_mining_applied_2019.html" class="year-btn active"'
)

with open("build_mining_applied_2019_full_system.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_mining_applied_2019_full_system.py successfully.")
