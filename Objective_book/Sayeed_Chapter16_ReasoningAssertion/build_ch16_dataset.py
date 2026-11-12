import json
import os
from ch16_catalog import CH16_QUESTIONS, DIRECTIONS

compiled = []

for q in CH16_QUESTIONS:
    q_num = q['q_num']
    a_txt = q['assertion']
    r_txt = q['reason']
    
    full_q_text = (
        f"Assertion (A): {a_txt}\n"
        f"Reason (R): {r_txt}\n\n"
        "Choose the correct option based on the following directions:\n"
        "(a) Both (A) and (R) are true and (R) is the correct explanation of (A)\n"
        "(b) Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)\n"
        "(c) (A) is true, but (R) is false\n"
        "(d) Both (A) and (R) are false\n"
        "(e) (A) is false, but (R) is true"
    )

    item = {
        "id": q_num,
        "global_q_num": q_num,
        "section": "Reasoning and Assertion",
        "section_id": "sec_reasoning",
        "section_q_num": q_num,
        "assertion": a_txt,
        "reason": r_txt,
        "question": full_q_text,
        "options": {
            "a": DIRECTIONS["a"],
            "b": DIRECTIONS["b"],
            "c": DIRECTIONS["c"],
            "d": DIRECTIONS["d"],
            "e": DIRECTIONS["e"]
        },
        "correct_option": q['answer'],
        "topic": q['topic'],
        "difficulty": "Advanced"
    }
    compiled.append(item)

out_file = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter16_ReasoningAssertion/data/sayeed_ch16_reasoning_assertion.json'
os.makedirs(os.path.dirname(out_file), exist_ok=True)

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(compiled, f, indent=2, ensure_ascii=False)

print(f"Successfully compiled Chapter 16 Dataset: {len(compiled)} questions saved to {out_file}!")
