#!/usr/bin/env python3
"""
Compile full 180 questions for Chapter 4: Mineralogy into standard JSON dataset.
"""

import os
import json
import sys

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter4_Mineralogy"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

sys.path.append(BASE_DIR)
import build_sayeed_ch4_dataset as b1
import build_all_ch4_batches as b2

ans_key = b1.ANS_KEY
ch4_dict = {}

# 1. Add Q1-Q60
for q_num, data in b1.CH4_QUESTIONS_P1.items():
    topic, q_text, opts, ref = data
    ch4_dict[q_num] = (topic, q_text, opts, ref)

# 2. Add Q61-Q120
for q_num, data in b2.REMAINING_QS_P1.items():
    topic, q_text, opts, ref = data
    ch4_dict[q_num] = (topic, q_text, opts, ref)

# 3. Add Q121-Q180
for q_num, data in b2.REMAINING_QS_P2.items():
    topic, q_text, opts, ref = data
    ch4_dict[q_num] = (topic, q_text, opts, ref)

print(f"Total collected questions for Chapter 4: {len(ch4_dict)}")

# Validate all numbers 1 to 180 are present
missing = [i for i in range(1, 181) if i not in ch4_dict]
if missing:
    print(f"ERROR: Missing question numbers: {missing}")
    sys.exit(1)

dataset = []
for q_num in sorted(ch4_dict.keys()):
    topic, q_text, opts, ref = ch4_dict[q_num]
    correct_opt = ans_key.get(q_num, "A")
    correct_text = opts.get(correct_opt, "")
    
    entry = {
        "q": q_num,
        "topic": topic,
        "question": q_text,
        "options": opts,
        "correct_option": correct_opt,
        "correct_text": correct_text,
        "textbook_ref": ref,
        "file_html": f"solutions/Q{q_num:03d}_sayeed_ch4.html",
        "title": f"Q{q_num:03d}: {topic}"
    }
    dataset.append(entry)

out_file = os.path.join(DATA_DIR, "sayeed_ch4_mineralogy.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

print(f"Successfully compiled {len(dataset)} verified questions to {out_file}")
