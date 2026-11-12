import re

with open("/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter1_Geotectonics/combined_ch1_ocr.txt") as f:
    text = f.read()

# Normalize
text = text[text.find("General Geology and Geotectonics"):]
text = re.sub(r'---\s*PAGE\s*\d+\s*COL\s*\d+\s*---', '', text)
text = re.sub(r'Scanned by CamScanner', '', text)

# Regex to find questions 1 to 30
# Look for number followed by dot or parenthesis
raw_questions = {}
for q in range(1, 31):
    # Pattern matching q. or *q. or #q. or q,
    p = rf'(?:^|\n)\s*[*#]?{q}\s*[\.\,\)]\s*(.+?)(?=(?:\n\s*[*#]?\d{{1,3}}\s*[\.\,\)]\s*)|\Z)'
    m = re.search(p, text, re.DOTALL)
    if m:
        raw_questions[q] = m.group(1).strip()
    else:
        raw_questions[q] = "NOT_FOUND"

for q, body in raw_questions.items():
    first_line = body.split('\n')[0] if body != "NOT_FOUND" else "NOT_FOUND"
    print(f"Q{q:02d}: {first_line[:80]}")
