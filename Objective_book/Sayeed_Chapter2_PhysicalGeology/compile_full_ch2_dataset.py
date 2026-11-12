#!/usr/bin/env python3
"""
Merge and Compile Master Dataset for Chapter 2: Physical Geology & Geomorphology
Dr. Ausaf Sayeed - Objective Geology (All 145 Questions)
"""

import os
import json
import re

import build_batch1_q1_to_q30 as b1
import build_batch2_q31_to_q60 as b2
import build_batch3_q61_to_q95 as b3
import build_batch4_q96_to_q120 as b4
import build_batch5_q121_to_q145 as b5

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter2_PhysicalGeology"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

all_batches = [b1.BATCH1_QS, b2.BATCH2_QS, b3.BATCH3_QS, b4.BATCH4_QS, b5.BATCH5_QS]
master_dict = {}
master_list = []

for batch in all_batches:
    for q_num, data in batch.items():
        master_dict[q_num] = data

for q_num in range(1, 146):
    if q_num not in master_dict:
        raise ValueError(f"Missing question {q_num}!")
    
    item = master_dict[q_num]
    ans_letter = item["ans"]
    correct_text = item["options"].get(ans_letter, "")
    
    # generate safe filename for standalone solution
    # e.g., Q001_Chemical_Weathering_Oceanic_Geochemistry_Complete_Guide.html
    clean_topic = re.sub(r'[^a-zA-Z0-9]+', '_', item['topic']).strip('_')
    # truncate if too long
    clean_topic = clean_topic[:65].rstrip('_')
    file_html = f"Q{q_num:03d}_{clean_topic}_Complete_Guide.html"
    
    entry = {
        "q": q_num,
        "topic": item["topic"],
        "question": item["question"],
        "options": item["options"],
        "correct_option": ans_letter,
        "correct_text": correct_text,
        "textbook_ref": item["ref"],
        "file_html": file_html,
        "title": f"Q{q_num}: {item['topic']}"
    }
    master_list.append(entry)

out_json = os.path.join(DATA_DIR, "sayeed_ch2_physical_geology.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(master_list, f, indent=2, ensure_ascii=False)

print(f"Master JSON dataset compiled with {len(master_list)} questions into {out_json} successfully!")
