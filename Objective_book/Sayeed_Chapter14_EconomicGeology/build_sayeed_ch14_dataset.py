#!/usr/bin/env python3
"""
Master Dataset Builder for Chapter 14: Economic Geology
Dr. Ausaf Sayeed - Objective Geology (243 Solved Questions)
"""

import os
import json
import sys

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter14_EconomicGeology"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

sys.path.append(BASE_DIR)
from ch14_catalog_part1 import CATALOG_PART1
from ch14_catalog_part2 import CATALOG_PART2
from ch14_catalog_part3 import CATALOG_PART3
from ch14_catalog_part4 import CATALOG_PART4

full_catalog = CATALOG_PART1 + CATALOG_PART2 + CATALOG_PART3 + CATALOG_PART4
print(f"Total compiled questions: {len(full_catalog)}")
assert len(full_catalog) == 243, f"Expected 243 questions, found {len(full_catalog)}"

# Verify all numbers and answers
with open(os.path.join(DATA_DIR, "ch14_key.json")) as f:
    key_dict = {int(k): v for k, v in json.load(f).items()}

for item in full_catalog:
    q_num = item["q_num"]
    expected_ans = key_dict[q_num]
    assert item["answer"] == expected_ans, f"Key mismatch at Q{q_num}"

out_json = os.path.join(DATA_DIR, "sayeed_ch14_economic_geology.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(full_catalog, f, indent=2, ensure_ascii=False)

print(f"Master Chapter 14 JSON written successfully: {out_json} ({os.path.getsize(out_json)} bytes)")
