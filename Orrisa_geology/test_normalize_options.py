import re
import parse_all_applied_2019 as p

def normalize_text_options(raw):
    # Normalize common OCR distortions for (A), (B), (C), (D)
    # (A) variants
    raw = re.sub(r'[\(\[\{]?\s*[4Afa@]\s*[\)\]\}]', '(A)', raw)
    # (B) variants: (8), (B), (b), ®
    raw = re.sub(r'[\(\[\{]?\s*[8bB®]\s*[\)\]\}]', '(B)', raw)
    # (C) variants: (C), (c), (©), ©
    raw = re.sub(r'[\(\[\{]?\s*[cC©]\s*[\)\]\}]', '(C)', raw)
    # (D) variants: (D), (d), (0), (Dy, (O)
    raw = re.sub(r'[\(\[\{]?\s*(?:[dD0O]|Dy)\s*[\)\]\}]', '(D)', raw)
    
    # Standalone letter/symbol at start of line
    raw = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*[4Afa@]\s*[\.\:\)]\s*', r'\n(A) ', raw)
    raw = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*[8bB®]\s*[\.\:\)]\s*', r'\n(B) ', raw)
    raw = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*[cC©]\s*[\.\:\)]\s*', r'\n(C) ', raw)
    raw = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*(?:[dD0O]|Dy)\s*[\.\:\)]\s*', r'\n(D) ', raw)
    
    # Special character bullets
    raw = re.sub(r'(?:^|\n)\s*©\s*', r'\n(C) ', raw)
    raw = re.sub(r'(?:^|\n)\s*®\s*', r'\n(B) ', raw)
    return raw

all_qs = p.all_questions
imperfect = []
for q in range(1, 151):
    body = normalize_text_options(all_qs[q])
    has_a = '(A)' in body
    has_b = '(B)' in body
    has_c = '(C)' in body
    has_d = '(D)' in body
    if not (has_a and has_b and has_c and has_d):
        imperfect.append((q, has_a, has_b, has_c, has_d, [l for l in body.splitlines() if any(k in l for k in ['(A)', '(B)', '(C)', '(D)']) or len(l) < 25]))

print(f'Clean options: {150 - len(imperfect)} / 150')
if imperfect:
    print('Imperfect count:', len(imperfect))
    for item in imperfect[:10]:
        print(item[:4], item[4])
