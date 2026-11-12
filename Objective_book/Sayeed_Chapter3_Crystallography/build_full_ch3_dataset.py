#!/usr/bin/env python3
"""
Compile full 150 questions for Chapter 3: Crystallography into standard JSON.
"""

import os
import json
import re
import sys

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter3_Crystallography"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

sys.path.append(BASE_DIR)
import build_sayeed_ch3_dataset as b1
import build_all_ch3_batches as b2

ans_key = b1.ANS_KEY
ch3_dict = {}

# 1. Add Q1-Q30
for q_num, data in b1.CH3_QUESTIONS.items():
    topic, q_text, opts, ref = data
    ch3_dict[q_num] = (topic, q_text, opts, ref)

# 2. Add Q31-Q60
for q_num, data in b2.REMAINING_QS.items():
    topic, q_text, opts, ref = data
    ch3_dict[q_num] = (topic, q_text, opts, ref)

# 3. Add Q61-Q150
for q_num, data in b2.REMAINING_QS_PART2.items():
    topic, q_text, opts, ref = data
    ch3_dict[q_num] = (topic, q_text, opts, ref)

print(f"Total collected questions: {len(ch3_dict)}")

# Validate all numbers 1 to 150 are present
missing = [i for i in range(1, 151) if i not in ch3_dict]
if missing:
    print(f"ERROR: Missing question numbers: {missing}")
    sys.exit(1)

dataset = []
for q_num in sorted(ch3_dict.keys()):
    topic, q_text, opts, ref = ch3_dict[q_num]
    correct_opt = ans_key.get(q_num, "A")
    correct_text = opts.get(correct_opt, "")
    
    # Clean latex backslashes if needed
    entry = {
        "q": q_num,
        "topic": topic,
        "question": q_text,
        "options": opts,
        "correct_option": correct_opt,
        "correct_text": correct_text,
        "textbook_ref": ref,
        "file_html": f"solutions/Q{q_num:03d}_sayeed_ch3.html",
        "title": f"Q{q_num:03d}: {topic}"
    }
    dataset.append(entry)

out_file = os.path.join(DATA_DIR, "sayeed_ch3_crystallography.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(dataset)} verified questions to {out_file}")
