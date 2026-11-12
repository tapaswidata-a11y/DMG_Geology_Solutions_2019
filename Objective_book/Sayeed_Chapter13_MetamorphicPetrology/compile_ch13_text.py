import os

SPLIT_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter13_MetamorphicPetrology/ocr_split"

sheet_sequence = []
sheet_sequence.append("sheet_198_right.txt")
for s in range(199, 207):
    sheet_sequence.append(f"sheet_{s}_left.txt")
    sheet_sequence.append(f"sheet_{s}_right.txt")
sheet_sequence.append("sheet_207_left.txt")
sheet_sequence.append("sheet_207_right.txt")

full_text = ""
for fname in sheet_sequence:
    path = os.path.join(SPLIT_DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        full_text += f"\n--- {fname} ---\n" + f.read()

out_path = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter13_MetamorphicPetrology/full_ch13_text.txt"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Full Chapter 13 text compiled: {len(full_text)} characters.")
