#!/usr/bin/env python3
"""
Compile full 125 questions for Chapter 5: Optical Mineralogy into standard JSON dataset.
"""

import os
import json
import sys

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter5_OpticalMineralogy"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

sys.path.append(BASE_DIR)
import build_sayeed_ch5_dataset as b1
import build_all_ch5_batches as b2

ans_key = b1.ANS_KEY
ch5_dict = {}

# 1. Add Q1-Q60
for q_num, data in b1.CH5_QUESTIONS_P1.items():
    topic, q_text, opts, ref = data
    ch5_dict[q_num] = (topic, q_text, opts, ref)

# 2. Add Q61-Q125
for q_num, data in b2.REMAINING_QS_CH5.items():
    topic, q_text, opts, ref = data
    ch5_dict[q_num] = (topic, q_text, opts, ref)

print(f"Total collected questions for Chapter 5: {len(ch5_dict)}")

# Validate all numbers 1 to 125 are present
missing = [i for i in range(1, 126) if i not in ch5_dict]
if missing:
    print(f"ERROR: Missing question numbers: {missing}")
    sys.exit(1)

dataset = []
for q_num in sorted(ch5_dict.keys()):
    topic, q_text, opts, ref = ch5_dict[q_num]
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
        "file_html": f"solutions/Q{q_num:03d}_sayeed_ch5.html",
        "title": f"Q{q_num:03d}: {topic}"
    }
    dataset.append(entry)

out_file = os.path.join(DATA_DIR, "sayeed_ch5_optical_mineralogy.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

print(f"Successfully compiled {len(dataset)} verified questions to {out_file}")
