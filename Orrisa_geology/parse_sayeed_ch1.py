import os
import re
import json

TXT_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter1_Geotectonics/ocr_columns_text"

# Read in order of pages and columns
all_text = ""
for p in range(48, 69):
    for col in [1, 2]:
        fn = f"page-{p:03d}_col{col}.txt"
        fp = os.path.join(TXT_DIR, fn)
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
                # On page 48 col 1, questions start after "General Geology and Geotectonics"
                all_text += f"\n--- PAGE {p} COL {col} ---\n" + content

print(f"Aggregated {len(all_text)} characters across all columns.")

# Save raw combined
with open("/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter1_Geotectonics/combined_ch1_ocr.txt", "w", encoding="utf-8") as f:
    f.write(all_text)
