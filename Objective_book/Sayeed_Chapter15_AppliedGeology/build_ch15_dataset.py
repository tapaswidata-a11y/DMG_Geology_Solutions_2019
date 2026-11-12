import json
import os
from ch15_catalog_part1 import SECTION_A_QUESTIONS
from ch15_catalog_part2 import SECTION_B_QUESTIONS
from ch15_catalog_part3 import SECTION_C_QUESTIONS, SECTION_D_QUESTIONS

all_questions = []
global_id = 1

# Section A: Exploration Methods (1 to 90)
for q in SECTION_A_QUESTIONS:
    item = {
        "id": global_id,
        "global_q_num": global_id,
        "section": "Section A: Exploration Methods",
        "section_id": "sec_a",
        "section_q_num": q["sec_q"],
        "question": q["question"],
        "options": q["options"],
        "correct_option": q["answer"],
        "topic": q["topic"],
        "difficulty": "Medium" if global_id % 3 != 0 else ("Hard" if global_id % 2 == 0 else "Advanced")
    }
    all_questions.append(item)
    global_id += 1

# Section B: Mineral Processing, Mining Geology & Mineral Economics (1 to 54)
for q in SECTION_B_QUESTIONS:
    item = {
        "id": global_id,
        "global_q_num": global_id,
        "section": "Section B: Mineral Processing, Mining & Mineral Economics",
        "section_id": "sec_b",
        "section_q_num": q["sec_q"],
        "question": q["question"],
        "options": q["options"],
        "correct_option": q["answer"],
        "topic": q["topic"],
        "difficulty": "Medium" if global_id % 3 != 0 else ("Hard" if global_id % 2 == 0 else "Advanced")
    }
    all_questions.append(item)
    global_id += 1

# Section C: Hydrogeology (1 to 31)
for q in SECTION_C_QUESTIONS:
    item = {
        "id": global_id,
        "global_q_num": global_id,
        "section": "Section C: Hydrogeology",
        "section_id": "sec_c",
        "section_q_num": q["sec_q"],
        "question": q["question"],
        "options": q["options"],
        "correct_option": q["answer"],
        "topic": q["topic"],
        "difficulty": "Medium" if global_id % 3 != 0 else ("Hard" if global_id % 2 == 0 else "Advanced")
    }
    all_questions.append(item)
    global_id += 1

# Section D: Engineering Geology (1 to 15)
for q in SECTION_D_QUESTIONS:
    item = {
        "id": global_id,
        "global_q_num": global_id,
        "section": "Section D: Engineering Geology",
        "section_id": "sec_d",
        "section_q_num": q["sec_q"],
        "question": q["question"],
        "options": q["options"],
        "correct_option": q["answer"],
        "topic": q["topic"],
        "difficulty": "Medium" if global_id % 3 != 0 else ("Hard" if global_id % 2 == 0 else "Advanced")
    }
    all_questions.append(item)
    global_id += 1

os.makedirs('/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter15_AppliedGeology/data', exist_ok=True)
out_file = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter15_AppliedGeology/data/sayeed_ch15_applied_geology.json'

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Successfully compiled Chapter 15 Dataset: {len(all_questions)} questions saved to {out_file}!")
