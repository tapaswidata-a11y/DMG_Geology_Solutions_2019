import json
import os
import sys

sys.path.append('/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter16_ReasoningAssertion')
import masterclass_data_ch16

solutions_dir = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter16_ReasoningAssertion/solutions'
os.makedirs(solutions_dir, exist_ok=True)

with open('/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter16_ReasoningAssertion/data/sayeed_ch16_reasoning_assertion.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

total_q = len(questions)

for idx, q in enumerate(questions):
    q_num = q['global_q_num']
    sec_title = q['section']
    topic = q['topic']
    a_txt = q['assertion']
    r_txt = q['reason']
    options = q['options']
    correct_opt = q['correct_option']
    difficulty = q['difficulty']

    formula, mechanics, refs = masterclass_data_ch16.get_formula_and_mechanics(q_num, topic, a_txt, r_txt)
    dissection = masterclass_data_ch16.get_options_dissection(q_num, a_txt, r_txt, correct_opt, topic)
    synthesis = masterclass_data_ch16.get_synthesis_and_strategy(q_num, topic, correct_opt, a_txt, r_txt)

    prev_link = f"Q{q_num-1:03d}_sayeed_ch16.html" if q_num > 1 else "../index_sayeed_ch16.html"
    next_link = f"Q{q_num+1:03d}_sayeed_ch16.html" if q_num < total_q else "../index_sayeed_ch16.html"

    options_html = ""
    for opt_k in sorted(options.keys()):
        opt_v = options[opt_k]
        is_correct = (opt_k == correct_opt)
        cls = "option-item correct" if is_correct else "option-item"
        badge = '<span class="badge-correct">CORRECT ANSWER</span>' if is_correct else ""
        options_html += f"""
        <div class="{cls}">
            <div class="opt-label">({opt_k})</div>
            <div class="opt-text">{opt_v}</div>
            {badge}
        </div>
        """

    dissection_html = ""
    for opt_k in sorted(options.keys()):
        opt_v = options[opt_k]
        is_correct = (opt_k == correct_opt)
        badge_cls = "badge-correct" if is_correct else "badge-incorrect"
        status_text = "CORRECT" if is_correct else "INCORRECT"
        analysis = dissection.get(opt_k, "")
        dissection_html += f"""
        <div class="dissection-item">
            <div class="dissection-header">
                <span class="{badge_cls}">Option ({opt_k}): {status_text}</span>
                <span class="dissection-opt-text">{opt_v}</span>
            </div>
            <div class="dissection-body">
                {analysis}
            </div>
        </div>
        """

    takeaways_html = "".join([f"<li>{item}</li>" for item in synthesis['takeaways']])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q{q_num:03d} Solution - Sayeed Reasoning & Assertion | Masterclass Portal</title>
    <!-- MathJax for quantitative formulations -->
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            }},
            svg: {{ fontCache: 'global' }}
        }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root {{
            --primary: #312e81;
            --primary-dark: #1e1b4b;
            --primary-light: #e0e7ff;
            --accent: #4338ca;
            --accent-glow: #6366f1;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --border: #c7d2fe;
            --success: #059669;
            --error: #dc2626;
            --radius: 12px;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            --shadow-lg: 0 10px 15px -3px rgba(49, 46, 129, 0.1), 0 4px 6px -4px rgba(49, 46, 129, 0.05);
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text-dark);
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}
        .nav-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            padding: 12px 20px;
            background: var(--card-bg);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }}
        .nav-btn {{
            text-decoration: none;
            color: var(--primary);
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 6px;
            transition: all 0.2s;
        }}
        .nav-btn:hover {{
            background: var(--primary-light);
            color: var(--primary-dark);
        }}
        .card {{
            background: var(--card-bg);
            border-radius: var(--radius);
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--border);
            padding: 32px;
            margin-bottom: 24px;
        }}
        .badge-header {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 16px;
        }}
        .tag {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 9999px;
        }}
        .tag-chapter {{ background: var(--primary-light); color: var(--primary-dark); }}
        .tag-topic {{ background: #ede9fe; color: #5b21b6; }}
        .tag-diff {{ background: #fef3c7; color: #92400e; }}
        .statement-box {{
            background: #f8fafc;
            border-left: 4px solid var(--accent);
            padding: 16px 20px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 20px;
        }}
        .statement-title {{
            font-weight: 700;
            color: var(--primary-dark);
            margin-bottom: 6px;
        }}
        .statement-text {{
            font-size: 1.05rem;
            color: var(--text-dark);
            margin-bottom: 12px;
        }}
        .options-list {{
            display: grid;
            gap: 10px;
            margin-bottom: 28px;
        }}
        .option-item {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 18px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            background: #fafafa;
            font-size: 0.95rem;
        }}
        .option-item.correct {{
            border-color: var(--success);
            background: #ecfdf5;
            font-weight: 600;
        }}
        .opt-label {{
            font-weight: 700;
            color: var(--primary);
        }}
        .badge-correct {{
            background: var(--success);
            color: white;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 4px;
            margin-left: auto;
        }}
        .badge-incorrect {{
            background: #ef4444;
            color: white;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 4px;
        }}
        .part-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 2px solid var(--primary-light);
            padding-bottom: 8px;
            margin-top: 32px;
            margin-bottom: 16px;
            color: var(--primary-dark);
            font-size: 1.15rem;
            font-weight: 700;
        }}
        .part-num {{
            background: var(--primary);
            color: white;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
        }}
        .formula-box {{
            background: #f8fafc;
            border-left: 4px solid var(--accent);
            padding: 16px 20px;
            border-radius: 0 8px 8px 0;
            margin: 16px 0;
            overflow-x: auto;
        }}
        .mechanics-text {{
            font-size: 1rem;
            color: #334155;
            margin-bottom: 16px;
            text-align: justify;
        }}
        .dissection-item {{
            margin-bottom: 14px;
            padding: 14px;
            background: #fdfdfd;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
        }}
        .dissection-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 8px;
        }}
        .dissection-opt-text {{
            font-weight: 600;
            color: var(--text-dark);
        }}
        .dissection-body {{
            font-size: 0.92rem;
            color: #475569;
            padding-left: 8px;
        }}
        .synthesis-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 0.95rem;
        }}
        .synthesis-table th, .synthesis-table td {{
            border: 1px solid #cbd5e1;
            padding: 10px 14px;
            text-align: left;
        }}
        .synthesis-table th {{
            background: var(--primary-light);
            color: var(--primary-dark);
            font-weight: 700;
        }}
        .pitfall-box {{
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-left: 4px solid #f59e0b;
            padding: 14px 18px;
            border-radius: 0 8px 8px 0;
            color: #92400e;
            margin-top: 16px;
            font-size: 0.92rem;
        }}
        .ref-footer {{
            margin-top: 24px;
            font-size: 0.8rem;
            color: var(--text-muted);
            border-top: 1px dashed #cbd5e1;
            padding-top: 12px;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Navigation -->
        <div class="nav-bar">
            <a href="{prev_link}" class="nav-btn">&larr; Previous Q</a>
            <a href="../index_sayeed_ch16.html" class="nav-btn">&#9776; Chapter 16 Portal</a>
            <a href="{next_link}" class="nav-btn">Next Q &rarr;</a>
        </div>

        <!-- Question Card -->
        <div class="card">
            <div class="badge-header">
                <span class="tag tag-chapter">Sayeed Objective Geology</span>
                <span class="tag tag-topic">Ch 16: Reasoning and Assertion</span>
                <span class="tag tag-topic">{topic}</span>
                <span class="tag tag-diff">{difficulty}</span>
            </div>

            <!-- Statement Box -->
            <div class="statement-box">
                <div class="statement-title">Assertion (A):</div>
                <div class="statement-text">{a_txt}</div>
                <div class="statement-title" style="margin-top: 12px;">Reason (R):</div>
                <div class="statement-text">{r_txt}</div>
            </div>

            <div class="options-list">
                {options_html}
            </div>

            <!-- Masterclass Part 1 -->
            <div class="part-header">
                <div class="part-num">1</div>
                <div>Foundational Geological Principles & Quantitative Framework</div>
            </div>
            <div class="formula-box">
                $${formula}$$
            </div>
            <div class="mechanics-text">
                {mechanics}
            </div>

            <!-- Masterclass Part 2 -->
            <div class="part-header">
                <div class="part-num">2</div>
                <div>Forensic Logical Dissection (Assertion-Reasoning Proof)</div>
            </div>
            <div class="dissection-list">
                {dissection_html}
            </div>

            <!-- Masterclass Part 3 -->
            <div class="part-header">
                <div class="part-num">3</div>
                <div>Synthesis, Exam Strategy & Key Takeaways</div>
            </div>
            <table class="synthesis-table">
                <tr>
                    <th style="width: 25%;">Parameter</th>
                    <th>Logical Analysis</th>
                </tr>
                <tr>
                    <td><strong>Core Concept</strong></td>
                    <td>{topic}</td>
                </tr>
                <tr>
                    <td><strong>Verified Key</strong></td>
                    <td>Option ({correct_opt}): {options.get(correct_opt, '')}</td>
                </tr>
                <tr>
                    <td><strong>Key Takeaways</strong></td>
                    <td>
                        <ul style="padding-left: 20px; margin: 4px 0;">
                            {takeaways_html}
                        </ul>
                    </td>
                </tr>
            </table>

            <div class="pitfall-box">
                <strong>Exam Pitfall Alert:</strong> {synthesis['exam_pitfall']}
            </div>

            <div class="ref-footer">
                Key Literature & Standard Authorities: {refs}
            </div>
        </div>

        <!-- Bottom Navigation -->
        <div class="nav-bar">
            <a href="{prev_link}" class="nav-btn">&larr; Previous Q</a>
            <a href="../index_sayeed_ch16.html" class="nav-btn">&#9776; Chapter 16 Portal</a>
            <a href="{next_link}" class="nav-btn">Next Q &rarr;</a>
        </div>
    </div>
</body>
</html>
"""

    out_path = os.path.join(solutions_dir, f"Q{q_num:03d}_sayeed_ch16.html")
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(html_content)

print(f"Generated all {total_q} standalone solution pages in {solutions_dir}!")
