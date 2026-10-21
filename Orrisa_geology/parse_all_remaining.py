import re, glob, os

files = sorted(glob.glob("qp_pages/page_*_left.txt") + glob.glob("qp_pages/page_*_right.txt"))
# Sort properly by page number then left/right
def sort_key(f):
    m = re.search(r'page_(\d+)_(\w+)', f)
    p = int(m.group(1))
    col = 0 if m.group(2) == 'left' else 1
    return (p, col)

files.sort(key=sort_key)

full_ordered_text = ""
for f in files:
    with open(f) as fp:
        full_ordered_text += f"\n--- {f} ---\n" + fp.read()

with open("qp_pages/full_ordered_text.txt", "w") as fp:
    fp.write(full_ordered_text)

# Now let's extract question by question
# Pattern for question number at start of line
lines = full_ordered_text.split('\n')
questions = {}
current_q = None
current_text = []

for line in lines:
    m = re.match(r'^\s*([7-9]\d|1[0-4]\d|150)\s*[\.\)]\s*(.*)', line)
    if m:
        if current_q is not None:
            questions[current_q] = "\n".join(current_text).strip()
        current_q = int(m.group(1))
        current_text = [m.group(2)]
    else:
        if current_q is not None and not line.startswith('--- qp_pages/'):
            current_text.append(line)

if current_q is not None:
    questions[current_q] = "\n".join(current_text).strip()

print(f"Total parsed questions (Q76-Q150): {len(questions)}")
found_nums = sorted(questions.keys())
print("Found question numbers:", found_nums)
missing = [q for q in range(76, 151) if q not in questions]
print("Missing:", missing)

