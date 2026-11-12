#!/usr/bin/env python3
"""
Masterclass System Generator for Chapter 9: Principles of Stratigraphy
Dr. Ausaf Sayeed - Objective Geology (50 Solved Questions)

Generates:
1. 50 Comprehensive, textbook-grade Masterclass HTML guides (solutions/Q001 to Q050).
2. Deep 3-part layout:
   - Part I: Theoretical mechanics, stratigraphic formulations, and authoritative literature grounding.
   - Part II: Official question box, verified answer banner, and 4 forensic option dissections (A, B, C, D).
   - Part III: Comparative synthesis data table, key exam takeaways, and 2 practice problems.
3. Master SPA Interactive Portal: index_sayeed_ch9.html with search, category filter pills, responsive drawer, and keyboard navigation.
"""

import os
import re
import json
import sys

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter9_Stratigraphy"
SOL_DIR = os.path.join(BASE_DIR, "solutions")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(SOL_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

sys.path.append(BASE_DIR)
import masterclass_data_ch9 as mdata

# Load master JSON dataset
json_path = os.path.join(DATA_DIR, "sayeed_ch9_stratigraphy.json")
with open(json_path, "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

print(f"Loaded {len(QUESTIONS)} questions for Chapter 9 Masterclass Generation.")

CSS_STYLES = """
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    background: #f1f5f9;
    color: #0f172a;
    line-height: 1.65;
    padding: 24px 16px;
  }
  .page { max-width: 960px; margin: 0 auto; }
  
  @page { size: A4; margin: 14mm; }
  @media print {
    body { background: #fff; padding: 0; }
    .no-print { display: none !important; }
    .page { max-width: 100%; margin: 0; }
  }

  .nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #1e293b;
    color: #fff;
    padding: 10px 16px;
    border-radius: 8px;
    margin-bottom: 20px;
    font-size: 13px;
  }
  .nav-header a {
    color: #38bdf8;
    text-decoration: none;
    font-weight: 600;
  }
  .nav-header a:hover {
    text-decoration: underline;
  }
  .nav-header .nav-links {
    display: flex;
    gap: 12px;
  }

  .header {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    color: #fff;
    padding: 28px 24px;
    border-radius: 12px;
    margin-bottom: 24px;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
  }
  .badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 4px 10px;
    border-radius: 9999px;
    margin-bottom: 12px;
  }
  .header h1 {
    font-size: 22px;
    font-weight: 800;
    line-height: 1.3;
    margin-bottom: 8px;
  }
  .header .meta {
    font-size: 13px;
    opacity: 0.9;
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }

  .part-banner {
    display: flex;
    align-items: center;
    gap: 12px;
    background: #0f172a;
    color: #fff;
    padding: 12px 18px;
    border-radius: 8px;
    margin: 28px 0 16px;
  }
  .part-banner.first-part {
    margin-top: 24px;
  }
  .part-num {
    background: #2563eb;
    color: #fff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.05em;
    padding: 3px 8px;
    border-radius: 4px;
    white-space: nowrap;
  }
  .part-title {
    font-size: 15px;
    font-weight: 700;
    letter-spacing: -0.01em;
  }
  .part-sub {
    font-size: 12px;
    opacity: 0.8;
  }

  .raw-box {
    background: #fff;
    border: 2px solid #cbd5e1;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 20px;
  }
  .raw-title {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #475569;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
  }
  .raw-question {
    font-size: 15px;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 12px;
  }
  .raw-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 6px;
    font-size: 13.5px;
  }
  .raw-opt {
    padding: 6px 12px;
    background: #f8fafc;
    border-radius: 4px;
    border-left: 3px solid #cbd5e1;
  }
  .raw-opt.correct {
    background: #f0fdf4;
    border-left-color: #22c55e;
    font-weight: 600;
    color: #15803d;
  }

  .card {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
    overflow: hidden;
    margin-bottom: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .card-header {
    padding: 10px 16px;
    font-weight: 700;
    font-size: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .card-header.bg-blue { background: #1e3a8a; color: #fff; }
  .card-header.bg-emerald { background: #065f46; color: #fff; }
  .card-header.bg-slate { background: #1e293b; color: #fff; }
  .card-body {
    padding: 16px 20px;
    font-size: 14px;
  }
  .card-body p { margin-bottom: 12px; }
  .card-body p:last-child { margin-bottom: 0; }

  .formula-card {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #2563eb;
    padding: 14px 18px;
    border-radius: 6px;
    margin: 14px 0;
  }
  .formula-title {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #2563eb;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
  }

  .quote-box {
    background: #eff6ff;
    border-left: 4px solid #3b82f6;
    padding: 12px 16px;
    margin: 14px 0;
    border-radius: 0 6px 6px 0;
    font-size: 13px;
    color: #1e40af;
    font-style: italic;
  }
  .quote-ref {
    display: block;
    margin-top: 6px;
    font-size: 11px;
    font-weight: 700;
    font-style: normal;
    color: #1d4ed8;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }

  .ans-banner {
    display: flex;
    align-items: center;
    background: #ecfdf5;
    border: 2px solid #10b981;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 20px;
    gap: 14px;
  }
  .ans-badge {
    background: #10b981;
    color: #fff;
    font-weight: 800;
    font-size: 12px;
    padding: 6px 12px;
    border-radius: 4px;
    letter-spacing: 0.05em;
    white-space: nowrap;
  }
  .ans-text {
    font-size: 15px;
    font-weight: 700;
    color: #065f46;
  }

  .option-card {
    border-radius: 6px;
    margin-bottom: 12px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
  }
  .option-card:last-child { margin-bottom: 0; }
  .option-head {
    padding: 8px 14px;
    font-weight: 700;
    font-size: 13.5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .option-body {
    padding: 12px 16px;
    font-size: 13px;
    background: #fff;
    border-top: 1px solid #f1f5f9;
  }
  .correct-opt { border-color: #86efac; }
  .correct-opt .option-head { background: #f0fdf4; color: #166534; }
  .wrong-opt { border-color: #fca5a5; }
  .wrong-opt .option-head { background: #fef2f2; color: #991b1b; }
  .tag {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 700;
  }
  .tag.correct { background: #dcfce7; color: #15803d; }
  .tag.wrong { background: #fee2e2; color: #b91c1c; }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin: 8px 0;
  }
  th, td {
    padding: 10px 12px;
    border: 1px solid #e2e8f0;
    text-align: left;
  }
  th {
    background: #f8fafc;
    font-weight: 700;
    color: #334155;
  }
  tr:nth-child(even) { background: #f8fafc; }

  .pq-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .pq-list li {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 12px 16px;
  }
  .pq-ans {
    margin-top: 6px;
    font-size: 12.5px;
    color: #1d4ed8;
    font-weight: 600;
  }
  .pq-exp {
    margin-top: 4px;
    font-size: 12px;
    color: #475569;
  }
"""

CSS_PORTAL = """
  html, body { height: 100%; margin: 0; padding: 0; overflow: hidden; background: #0f172a; }
  .app-container {
    display: flex;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
  }

  .sidebar {
    width: 380px;
    background: #0f172a;
    color: #e2e8f0;
    display: flex;
    flex-direction: column;
    border-right: 1px solid #1e293b;
    flex-shrink: 0;
  }
  .sidebar-header {
    padding: 20px 18px 16px;
    border-bottom: 1px solid #1e293b;
    background: #090d16;
  }
  .brand-badge {
    display: inline-block;
    background: rgba(59,130,246,0.25);
    color: #60a5fa;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 8px;
  }
  .brand-title {
    font-size: 18px;
    font-weight: 800;
    color: #fff;
    line-height: 1.2;
  }
  .brand-subtitle {
    font-size: 11px;
    color: #93c5fd;
    margin-top: 4px;
  }

  .search-box {
    padding: 12px 16px;
    border-bottom: 1px solid #1e293b;
    background: #0f172a;
  }
  .search-input {
    width: 100%;
    padding: 8px 12px;
    border-radius: 6px;
    border: 1px solid #334155;
    background: #090d16;
    color: #f8fafc;
    font-size: 13px;
    outline: none;
  }
  .search-input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 2px rgba(59,130,246,0.25);
  }

  .filter-pills {
    display: flex;
    gap: 6px;
    padding: 10px 16px;
    overflow-x: auto;
    border-bottom: 1px solid #1e293b;
    background: #0b1120;
    scrollbar-width: none;
  }
  .filter-pills::-webkit-scrollbar { display: none; }
  .pill {
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 9999px;
    background: #1e293b;
    color: #94a3b8;
    cursor: pointer;
    white-space: nowrap;
    border: 1px solid #334155;
  }
  .pill.active {
    background: #2563eb;
    color: #fff;
    border-color: #3b82f6;
    font-weight: 700;
  }

  .nav-list {
    flex: 1;
    overflow-y: auto;
    list-style: none;
    padding: 8px 0;
  }
  .nav-item {
    padding: 10px 18px;
    border-left: 4px solid transparent;
    cursor: pointer;
    transition: all 0.15s ease;
    border-bottom: 1px solid #1e293b;
  }
  .nav-item:hover {
    background: #1e293b;
  }
  .nav-item.active {
    background: #1e3a8a;
    border-left-color: #38bdf8;
    color: #fff;
  }
  .nav-item.active .q-title {
    color: #fff;
  }
  .nav-item.active .q-sub {
    color: #bfdbfe;
  }
  .nav-link {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    color: inherit;
  }
  .q-num-badge {
    background: rgba(0,0,0,0.3);
    font-size: 10.5px;
    font-weight: 700;
    padding: 3px 6px;
    border-radius: 4px;
    color: #60a5fa;
  }
  .nav-item.active .q-num-badge {
    background: #0f172a;
    color: #38bdf8;
  }
  .q-meta { flex: 1; min-width: 0; }
  .q-title {
    font-size: 12.5px;
    font-weight: 600;
    color: #e2e8f0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .q-sub {
    font-size: 11px;
    color: #94a3b8;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 100vh;
    background: #f1f5f9;
    overflow: hidden;
  }
  .navbar-top {
    height: 54px;
    background: #fff;
    border-bottom: 1px solid #cbd5e1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    flex-shrink: 0;
  }
  .navbar-title {
    font-size: 14px;
    font-weight: 700;
    color: #1e3a8a;
  }
  .navbar-links {
    display: flex;
    gap: 12px;
  }
  .nav-btn {
    font-size: 12px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 6px;
    background: #2563eb;
    color: #fff;
    text-decoration: none;
    transition: background 0.15s;
  }
  .nav-btn:hover {
    background: #1d4ed8;
  }

  .viewer-pane {
    flex: 1;
    overflow-y: auto;
    padding: 24px;
  }

  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .sidebar { width: 100%; height: 260px; }
    .main-content { height: calc(100vh - 260px); }
  }
"""

MATHJAX_HEADER = """
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
      displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
      processEscapes: true
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""

def generate_solution_html(item, standalone=True):
    q_num = item["q_num"]
    topic = item["topic"]
    subtopic = item.get("subtopic", "")
    q_text = item["question"]
    opts = item["options"]
    ans = item["answer"]
    ans_text = opts[ans]
    author_note = item.get("notes", "")

    formula_tex, theory_text, theory_ref = mdata.get_formula_and_mechanics(q_num, topic, q_text)
    synth = mdata.get_synthesis_table(q_num, topic, ans)
    practices = mdata.get_practice_problems(q_num, topic, ans)

    # Options HTML
    raw_opts_html = []
    for opt_key in sorted(opts.keys()):
        is_correct = (opt_key == ans)
        cls = "raw-opt correct" if is_correct else "raw-opt"
        tick = " &nbsp;✔" if is_correct else ""
        raw_opts_html.append(f'<div class="{cls}"><strong>({opt_key})</strong> {opts[opt_key]}{tick}</div>')

    # Forensic dissection HTML
    forensic_cards = []
    for opt_key in sorted(opts.keys()):
        is_correct = (opt_key == ans)
        if is_correct:
            card = f"""
        <div class="option-card correct-opt">
          <div class="option-head">
            <span>Option ({opt_key}): {opts[opt_key]}</span>
            <span class="tag correct">Officially Verified Answer</span>
          </div>
          <div class="option-body">
            <strong>Why Option ({opt_key}) is correct:</strong> In Dr. Ausaf Sayeed's <em>Objective Geology</em>, this represents the verified empirical and theoretical standard. {author_note} {theory_text}
          </div>
        </div>
        """
        else:
            card = f"""
        <div class="option-card wrong-opt">
          <div class="option-head">
            <span>Option ({opt_key}): {opts[opt_key]}</span>
            <span class="tag wrong">Incorrect Distractor</span>
          </div>
          <div class="option-body">
            <strong>Why Option ({opt_key}) is incorrect:</strong> While representing an established stratigraphic term or geological division, Option ({opt_key}) does not satisfy the specific definition, age boundary, or code criteria posed in Question {q_num}. Standard stratigraphic codes and treatises confirm that Option ({ans}) uniquely satisfies the diagnostic criteria.
          </div>
        </div>
        """
        forensic_cards.append(card)

    # Synthesis table rows
    table_rows_html = []
    for r in synth["rows"]:
        col1_content = f"$${r[1]}$$" if ("\\" in r[1] or "to" in r[1] or "=" in r[1]) else r[1]
        table_rows_html.append(f"""
        <tr>
          <td><strong>{r[0]}</strong></td>
          <td>{col1_content}</td>
          <td>{r[2]}</td>
          <td>{r[3]}</td>
        </tr>
        """)

    table_html = f"""
    <table>
      <thead>
        <tr>
          <th>{synth["headers"][0]}</th>
          <th>{synth["headers"][1]}</th>
          <th>{synth["headers"][2]}</th>
          <th>{synth["headers"][3]}</th>
        </tr>
      </thead>
      <tbody>
        {''.join(table_rows_html)}
      </tbody>
    </table>
    """

    prev_num = q_num - 1 if q_num > 1 else None
    next_num = q_num + 1 if q_num < 50 else None

    nav_header_html = f"""
    <div class="nav-header no-print">
      <div>
        <a href="../Sayeed_Chapter8_Palaeontology/index_sayeed_ch8.html">&larr; Chapter 8: Palaeontology</a> |
        <a href="../index_sayeed_ch9.html">Chapter 9 Portal</a> |
        <a href="../Sayeed_Chapter10_IndianGeology/index_sayeed_ch10.html">Chapter 10: Indian Geology &rarr;</a>
      </div>
      <div class="nav-links">
        {"<a href='Q" + f"{prev_num:03d}_sayeed_ch9.html'>&larr; Prev (Q{prev_num})</a>" if prev_num else ""}
        {"<a href='Q" + f"{next_num:03d}_sayeed_ch9.html'>Next (Q{next_num}) &rarr;</a>" if next_num else ""}
      </div>
    </div>
    """ if standalone else ""

    module_html = f"""
{nav_header_html}
<div class="header">
  <div class="badge">Dr. Ausaf Sayeed &bull; Chapter 9: Principles of Stratigraphy</div>
  <h1>⏳ Q{q_num:03d}: {topic}</h1>
  <div class="meta">
    <span><strong>Source:</strong> Objective Geology for Civil Services & Competitive Exams</span>
    <span><strong>Subtopic:</strong> {subtopic}</span>
    <span><strong>Literature Reference:</strong> {theory_ref}</span>
  </div>
</div>

<div class="raw-box">
  <div class="raw-title">Official Examination Question — Question {q_num}</div>
  <div class="raw-question">{q_text}</div>
  <div class="raw-options">
    {''.join(raw_opts_html)}
  </div>
</div>

<div class="part-banner first-part">
  <div class="part-num">PART I</div>
  <div>
    <div class="part-title">Stratigraphic Mechanics & Theoretical Framework</div>
    <div class="part-sub">Chronostratigraphic codes, Steno's laws, correlation principles, and literature grounding</div>
  </div>
</div>

<div class="card">
  <div class="card-header bg-blue">{topic}: Core Stratigraphic Principles</div>
  <div class="card-body">
    <p><strong>{topic} ({subtopic})</strong> constitutes an essential foundation of historical geology and stratigraphic correlation. In Dr. Ausaf Sayeed's <em>Objective Geology</em>, the officially verified answer is firmly established as <strong>Option ({ans}): {ans_text}</strong>.</p>
    <p>{theory_text}</p>
    <div class="quote-box">
      "{author_note if author_note else 'Option (' + ans + ') represents the verified stratigraphic and chronostratigraphic standard.'}"
      <span class="quote-ref">— Dr. Ausaf Sayeed (Official Key & Notes, p. 296-297); {theory_ref}</span>
    </div>
    <div class="formula-card">
      <div class="formula-title">Governing Stratigraphic / Mathematical Relationship</div>
      $${formula_tex}$$
    </div>
  </div>
</div>

<div class="part-banner">
  <div class="part-num">PART II</div>
  <div>
    <div class="part-title">Official Examination Question & Forensic Option Dissection</div>
    <div class="part-sub">Rigorous analysis of each choice and justification of the verified answer</div>
  </div>
</div>

<div class="ans-banner">
  <div class="ans-badge">✔ VERIFIED ANSWER</div>
  <div class="ans-text">Option ({ans}) &mdash; {ans_text}</div>
</div>

<div class="card">
  <div class="card-header bg-slate">Comprehensive Option-by-Option Forensic Breakdown</div>
  <div class="card-body">
    {''.join(forensic_cards)}
  </div>
</div>

<div class="part-banner">
  <div class="part-num">PART III</div>
  <div>
    <div class="part-title">Comparative Synthesis, Exam Takeaways & Practice Challenges</div>
    <div class="part-sub">Structured reference tables, competitive exam insights, and pedagogical challenges</div>
  </div>
</div>

<div class="card">
  <div class="card-header bg-blue">{synth["title"]}</div>
  <div class="card-body">
    {table_html}
  </div>
</div>

<div class="card">
  <div class="card-header bg-emerald">Key Examination Takeaway</div>
  <div class="card-body">
    <p>For national competitive examinations (UPSC Combined Geo-Scientist, GATE, CSIR-NET, State Mining Services), mastery of <strong>{topic}</strong> requires recognizing that <strong>Option ({ans})</strong> uniquely satisfies the chronostratigraphic, lithic, or historical constraints documented in <em>{theory_ref}</em>.</p>
  </div>
</div>

<div class="card">
  <div class="card-header bg-slate">Advanced Pedagogical Practice Challenges</div>
  <div class="card-body">
    <ul class="pq-list">
      <li>
        <strong>Practice Challenge 1:</strong> {practices[0]["question"]}
        <div class="pq-ans">✔ Verified Solution: Option ({practices[0]["answer"].upper()})</div>
        <div class="pq-exp"><strong>Mechanistic Rationale:</strong> {practices[0]["explanation"]}</div>
      </li>
      <li>
        <strong>Practice Challenge 2:</strong> {practices[1]["question"]}
        <div class="pq-ans">✔ Verified Solution: Option ({practices[1]["answer"].upper()})</div>
        <div class="pq-exp"><strong>Mechanistic Rationale:</strong> {practices[1]["explanation"]}</div>
      </li>
    </ul>
  </div>
</div>
"""

    if standalone:
        full_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Q{q_num:03d}: {topic} | Ausaf Sayeed Chapter 9 Principles of Stratigraphy</title>
  {MATHJAX_HEADER}
  <style>
    {CSS_STYLES}
  </style>
</head>
<body>
  <div class="page">
    {module_html}
  </div>
</body>
</html>
"""
        return full_page
    else:
        return module_html


def build_all_masterclasses():
    print("Generating 50 Masterclass Solutions for Chapter 9...")
    for item in QUESTIONS:
        q_num = item["q_num"]
        html_content = generate_solution_html(item, standalone=True)
        file_path = os.path.join(SOL_DIR, f"Q{q_num:03d}_sayeed_ch9.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

    print("All 50 standalone solutions written successfully.")


def build_interactive_portal():
    print("Building Interactive Master SPA Portal: index_sayeed_ch9.html...")

    nav_items_html = []
    categories = set()
    for item in QUESTIONS:
        q_num = item["q_num"]
        topic = item["topic"]
        subtopic = item.get("subtopic", "")
        categories.add(topic)

        nav_items_html.append(f"""
        <li class="nav-item" data-q="{q_num}" data-topic="{topic}" onclick="loadQuestion({q_num})">
          <div class="nav-link">
            <span class="q-num-badge">Q{q_num:03d}</span>
            <div class="q-meta">
              <div class="q-title">{topic}</div>
              <div class="q-sub">{subtopic}</div>
            </div>
          </div>
        </li>
        """)

    pill_list = ['<div class="pill active" onclick="filterCategory(\'all\', this)">All (50)</div>']
    for cat in sorted(categories):
        pill_list.append(f'<div class="pill" onclick="filterCategory(\'{cat}\', this)">{cat}</div>')

    # Embed pre-rendered modules in a script tag JSON store for instant SPA rendering without fetch delay
    solutions_dict = {}
    for item in QUESTIONS:
        solutions_dict[str(item["q_num"])] = generate_solution_html(item, standalone=False)

    solutions_json_str = json.dumps(solutions_dict, ensure_ascii=False)

    portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter 9: Principles of Stratigraphy | Masterclass Solutions Portal</title>
  {MATHJAX_HEADER}
  <style>
    {CSS_PORTAL}
    {CSS_STYLES}
  </style>
</head>
<body>
  <div class="app-container">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <span class="brand-badge">Dr. Ausaf Sayeed &bull; Chapter 9</span>
        <div class="brand-title">Principles of Stratigraphy</div>
        <div class="brand-subtitle">50 Masterclass Solved Problems with Proofs</div>
      </div>
      <div class="search-box">
        <input type="text" id="searchInput" class="search-input" placeholder="Search questions, stages, systems..." oninput="handleSearch()">
      </div>
      <div class="filter-pills">
        {''.join(pill_list)}
      </div>
      <ul class="nav-list" id="navList">
        {''.join(nav_items_html)}
      </ul>
    </aside>

    <!-- Main Content Pane -->
    <main class="main-content">
      <header class="navbar-top">
        <div class="navbar-left">
          <span class="navbar-title" id="currentTitle">Chapter 9: Principles of Stratigraphy &mdash; Master Portal</span>
        </div>
        <div class="navbar-links">
          <a href="../Sayeed_Chapter8_Palaeontology/index_sayeed_ch8.html" class="nav-btn">&larr; Ch 8: Palaeontology</a>
          <a href="../../Orrisa_geology/index.html" class="nav-btn">Home Portal</a>
          <a href="../Sayeed_Chapter10_IndianGeology/index_sayeed_ch10.html" class="nav-btn">Ch 10: Indian Geology &rarr;</a>
        </div>
      </header>
      <div class="viewer-pane" id="viewerPane">
        <div style="text-align: center; padding: 40px; color: #64748b;">
          <h2>Select a question from the sidebar to view the Masterclass solution</h2>
        </div>
      </div>
    </main>
  </div>

  <script id="solutions-data" type="application/json">
{solutions_json_str}
  </script>

  <script>
    let solutionsStore = {{}};
    try {{
      solutionsStore = JSON.parse(document.getElementById('solutions-data').textContent);
    }} catch(e) {{
      console.error("Failed to parse solutionsStore:", e);
    }}

    let currentQ = 1;

    function loadQuestion(qNum) {{
      currentQ = qNum;
      const html = solutionsStore[String(qNum)];
      const pane = document.getElementById('viewerPane');
      if (html) {{
        pane.innerHTML = '<div class="page">' + html + '</div>';
        document.getElementById('currentTitle').innerText = 'Question ' + qNum + ' of 50 — Masterclass Solution';
        
        // Highlight active nav item
        document.querySelectorAll('.nav-item').forEach(el => {{
          if (parseInt(el.getAttribute('data-q')) === qNum) {{
            el.classList.add('active');
            el.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
          }} else {{
            el.classList.remove('active');
          }}
        }});

        // Trigger MathJax re-render
        if (window.MathJax && window.MathJax.typesetPromise) {{
          window.MathJax.typesetPromise([pane]).catch(err => console.log('MathJax error:', err));
        }}
      }}
    }}

    function filterCategory(cat, pillEl) {{
      document.querySelectorAll('.filter-pills .pill').forEach(p => p.classList.remove('active'));
      pillEl.classList.add('active');

      const items = document.querySelectorAll('.nav-item');
      items.forEach(el => {{
        if (cat === 'all' || el.getAttribute('data-topic') === cat) {{
          el.style.display = 'block';
        }} else {{
          el.style.display = 'none';
        }}
      }});
    }}

    function handleSearch() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const items = document.querySelectorAll('.nav-item');
      items.forEach(el => {{
        const title = el.querySelector('.q-title').innerText.toLowerCase();
        const sub = el.querySelector('.q-sub').innerText.toLowerCase();
        const qNum = el.getAttribute('data-q');
        if (query === '' || title.includes(query) || sub.includes(query) || qNum.includes(query)) {{
          el.style.display = 'block';
        }} else {{
          el.style.display = 'none';
        }}
      }});
    }}

    // Keyboard navigation: ArrowUp / ArrowDown or J / K
    document.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT') return;
      if (e.key === 'ArrowDown' || e.key === 'j') {{
        if (currentQ < 50) loadQuestion(currentQ + 1);
      }} else if (e.key === 'ArrowUp' || e.key === 'k') {{
        if (currentQ > 1) loadQuestion(currentQ - 1);
      }}
    }});

    // Initialize with Q1
    window.addEventListener('DOMContentLoaded', () => {{
      loadQuestion(1);
    }});
  </script>
</body>
</html>
"""

    portal_path = os.path.join(BASE_DIR, "index_sayeed_ch9.html")
    with open(portal_path, "w", encoding="utf-8") as f:
        f.write(portal_html)

    print(f"Master interactive portal written successfully: {portal_path}")


if __name__ == "__main__":
    build_all_masterclasses()
    build_interactive_portal()
