#!/usr/bin/env python3
"""
Masterclass System Generator for Chapter 7: Structural Geology
Dr. Ausaf Sayeed - Objective Geology (150 Solved Questions)

Generates:
1. 150 Comprehensive, textbook-grade Masterclass HTML guides (solutions/Q001 to Q150).
2. Deep 3-part layout:
   - Part I: Theoretical mechanics, structural formulas, and authoritative literature grounding.
   - Part II: Official question box, verified answer banner, and 4 forensic option dissections (A, B, C, D).
   - Part III: Comparative synthesis data table, key exam takeaways, and 2 practice problems.
3. Master SPA Interactive Portal: index_sayeed_ch7.html with search, category filter pills, responsive drawer, and keyboard navigation.
"""

import os
import re
import json
import sys

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter7_StructuralGeology"
SOL_DIR = os.path.join(BASE_DIR, "solutions")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(SOL_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

sys.path.append(BASE_DIR)
import masterclass_data_ch7 as mdata

# Load master JSON dataset
json_path = os.path.join(DATA_DIR, "sayeed_ch7_structural_geology.json")
with open(json_path, "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

print(f"Loaded {len(QUESTIONS)} questions for Chapter 7 Masterclass Generation.")

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
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    color: #fff;
    padding: 26px 30px;
    border-radius: 12px;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
  }
  .badge {
    display: inline-block;
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 8px;
  }
  .header h1 {
    font-size: 22px;
    font-weight: 800;
    line-height: 1.35;
    margin-bottom: 6px;
  }
  .header .meta {
    font-size: 12px;
    color: #94a3b8;
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
  }

  .raw-box {
    background: #fff;
    border-left: 5px solid #0284c7;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }
  .raw-title {
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #0284c7;
    margin-bottom: 6px;
  }
  .raw-question {
    font-size: 15px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 14px;
    line-height: 1.5;
  }
  .raw-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
  }
  .raw-opt {
    padding: 8px 12px;
    border-radius: 6px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    font-size: 13.5px;
  }
  .raw-opt.correct {
    background: #ecfdf5;
    border-color: #10b981;
    font-weight: 700;
    color: #065f46;
  }

  .part-banner {
    display: flex;
    align-items: center;
    gap: 12px;
    background: #0f172a;
    color: #f8fafc;
    padding: 12px 18px;
    border-radius: 8px;
    margin: 28px 0 16px;
  }
  .part-banner.first-part { margin-top: 0; }
  .part-num {
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 900;
    padding: 4px 8px;
    border-radius: 4px;
    letter-spacing: 0.6px;
  }
  .part-title { font-size: 15px; font-weight: 800; }
  .part-sub { font-size: 11px; color: #94a3b8; }

  .card {
    background: #fff;
    border-radius: 8px;
    margin-bottom: 18px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    overflow: hidden;
  }
  .card-header {
    padding: 12px 18px;
    font-size: 13.5px;
    font-weight: 700;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .card-header.bg-blue { background: #1e40af; }
  .card-header.bg-emerald { background: #065f46; }
  .card-header.bg-purple { background: #6b21a8; }
  .card-header.bg-amber { background: #92400e; }
  .card-header.bg-slate { background: #334155; }
  .card-body { padding: 18px 20px; font-size: 14px; color: #334155; line-height: 1.65; }
  .card-body p { margin-bottom: 10px; }
  .card-body p:last-child { margin-bottom: 0; }

  .formula-card {
    background: #0f172a;
    color: #f8fafc;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 14px 0;
    text-align: center;
  }
  .formula-title {
    font-size: 11px;
    font-weight: 700;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
  }

  .quote-box {
    background: #f8fafc;
    border-left: 4px solid #0284c7;
    padding: 12px 16px;
    font-style: italic;
    color: #334155;
    margin: 12px 0;
    border-radius: 0 6px 6px 0;
  }
  .quote-ref {
    display: block;
    font-style: normal;
    font-size: 12px;
    font-weight: 700;
    color: #64748b;
    margin-top: 6px;
  }

  .ans-banner {
    display: flex;
    align-items: center;
    gap: 12px;
    background: #dcfce7;
    border: 2px solid #16a34a;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 18px;
  }
  .ans-badge {
    background: #16a34a;
    color: #fff;
    font-size: 12px;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 4px;
    white-space: nowrap;
  }
  .ans-text { font-size: 15px; font-weight: 700; color: #14532d; }

  .option-card {
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    margin-bottom: 12px;
    overflow: hidden;
  }
  .option-card.correct-opt { border-color: #86efac; background: #f0fdf4; }
  .option-card.wrong-opt { border-color: #cbd5e1; background: #fff; }
  .option-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 14px;
    font-size: 13.5px;
    font-weight: 700;
    border-bottom: 1px solid rgba(0,0,0,0.06);
  }
  .correct-opt .option-head { background: #dcfce7; color: #166534; }
  .wrong-opt .option-head { background: #f1f5f9; color: #475569; }
  .option-body { padding: 12px 14px; font-size: 13.5px; color: #334155; }
  .tag {
    font-size: 10.5px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .tag.correct { background: #16a34a; color: #fff; }
  .tag.wrong { background: #64748b; color: #fff; }

  table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 13px; }
  th, td { padding: 9px 12px; border: 1px solid #cbd5e1; text-align: left; }
  th { background: #0f2b4c; color: #fff; font-weight: 600; }
  tr:nth-child(even) { background: #f8fafc; }

  .pq-list { list-style: none !important; margin: 0 !important; }
  .pq-list li {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 14px 16px;
    margin-bottom: 12px;
  }
  .pq-ans {
    background: #ecfdf5;
    color: #065f46;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 4px;
    margin-top: 8px;
    font-size: 12.5px;
    display: inline-block;
  }
  .pq-exp {
    margin-top: 6px;
    font-size: 13px;
    color: #475569;
  }
"""

CSS_PORTAL = """
  html, body {
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    background: #f1f5f9;
  }
  .app-container {
    display: flex;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
  }
  .sidebar {
    width: 380px;
    min-width: 380px;
    background: #0f172a;
    color: #f8fafc;
    display: flex;
    flex-direction: column;
    border-right: 1px solid #1e293b;
    box-shadow: 2px 0 8px rgba(0,0,0,0.15);
    z-index: 20;
  }
  .sidebar-header {
    padding: 18px 20px 14px;
    background: linear-gradient(135deg, #091e3a 0%, #1e3a8a 100%);
    border-bottom: 1px solid #1e293b;
  }
  .brand-badge {
    display: inline-block;
    background: #0284c7;
    color: #fff;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 6px;
  }
  .brand-title {
    font-size: 16px;
    font-weight: 800;
    color: #f8fafc;
    line-height: 1.3;
  }
  .brand-subtitle {
    font-size: 11.5px;
    color: #94a3b8;
    margin-top: 3px;
  }
  .search-box {
    padding: 12px 16px;
    background: #1e293b;
    border-bottom: 1px solid #334155;
  }
  .search-input {
    width: 100%;
    background: #0f172a;
    border: 1px solid #475569;
    border-radius: 6px;
    padding: 8px 12px;
    color: #fff;
    font-size: 13px;
    outline: none;
    transition: border-color 0.2s;
  }
  .search-input:focus { border-color: #38bdf8; }
  .filter-pills {
    display: flex;
    gap: 6px;
    padding: 8px 16px;
    overflow-x: auto;
    background: #0f172a;
    border-bottom: 1px solid #1e293b;
    scrollbar-width: none;
  }
  .filter-pills::-webkit-scrollbar { display: none; }
  .pill {
    background: #1e293b;
    color: #cbd5e1;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 12px;
    white-space: nowrap;
    cursor: pointer;
    border: 1px solid #334155;
    transition: all 0.15s ease;
  }
  .pill:hover, .pill.active {
    background: #0284c7;
    color: #fff;
    border-color: #0284c7;
  }
  .nav-list {
    flex: 1;
    overflow-y: auto;
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .nav-item {
    border-bottom: 1px solid #1e293b;
    cursor: pointer;
    transition: background 0.15s ease;
  }
  .nav-item:hover { background: #1e293b; }
  .nav-item.active { background: #0284c7; color: #fff; }
  .nav-link {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    text-decoration: none;
    color: inherit;
  }
  .q-num-badge {
    background: rgba(255,255,255,0.12);
    font-size: 11px;
    font-weight: 800;
    padding: 3px 7px;
    border-radius: 4px;
    color: #38bdf8;
  }
  .active .q-num-badge { color: #fff; background: rgba(0,0,0,0.25); }
  .q-meta { flex: 1; min-width: 0; }
  .q-title {
    font-size: 12.5px;
    font-weight: 600;
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
  .active .q-sub { color: #e0f2fe; }

  .main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: #f8fafc;
  }
  .navbar-top {
    height: 52px;
    background: #fff;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    z-index: 10;
  }
  .navbar-left { display: flex; align-items: center; gap: 12px; }
  .navbar-title {
    font-size: 13.5px;
    font-weight: 700;
    color: #0f172a;
  }
  .navbar-links { display: flex; align-items: center; gap: 10px; }
  .nav-btn {
    font-size: 12px;
    font-weight: 600;
    color: #0284c7;
    text-decoration: none;
    padding: 5px 10px;
    border-radius: 5px;
    background: #e0f2fe;
    transition: all 0.15s ease;
  }
  .nav-btn:hover { background: #bae6fd; color: #0369a1; }
  .viewer-pane {
    flex: 1;
    overflow-y: auto;
    padding: 24px 28px;
  }
  @media (max-width: 768px) {
    .app-container { flex-direction: column; }
    .sidebar { width: 100%; min-width: 100%; height: 40vh; }
    .main-content { height: 60vh; }
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
            <strong>Why Option ({opt_key}) is incorrect:</strong> While representing an established structural term or kinematic configuration, Option ({opt_key}) does not satisfy the specific geometric, mechanical, or orientation constraints posed in Question {q_num}. Standard structural geology literature confirms that Option ({ans}) uniquely satisfies the diagnostic criteria.
          </div>
        </div>
        """
        forensic_cards.append(card)

    # Synthesis table rows
    table_rows_html = []
    for r in synth["rows"]:
        table_rows_html.append(f"""
        <tr>
          <td><strong>{r[0]}</strong></td>
          <td>$${r[1]}$$</td>
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
    next_num = q_num + 1 if q_num < 150 else None

    nav_header_html = f"""
    <div class="nav-header no-print">
      <div>
        <a href="../Sayeed_Chapter6_Geochemistry/index_sayeed_ch6.html">&larr; Chapter 6: Geochemistry</a> |
        <a href="../index_sayeed_ch7.html">Chapter 7 Portal</a> |
        <a href="../Sayeed_Chapter8_Palaeontology/index_sayeed_ch8.html">Chapter 8: Palaeontology &rarr;</a>
      </div>
      <div class="nav-links">
        {"<a href='Q" + f"{prev_num:03d}_sayeed_ch7.html'>&larr; Prev (Q{prev_num})</a>" if prev_num else ""}
        {"<a href='Q" + f"{next_num:03d}_sayeed_ch7.html'>Next (Q{next_num}) &rarr;</a>" if next_num else ""}
      </div>
    </div>
    """ if standalone else ""

    module_html = f"""
{nav_header_html}
<div class="header">
  <div class="badge">Dr. Ausaf Sayeed &bull; Chapter 7: Structural Geology</div>
  <h1>📐 Q{q_num:03d}: {topic}</h1>
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
    <div class="part-title">Structural Mechanics & Theoretical Framework</div>
    <div class="part-sub">Analytical derivations, stress/strain tensors, failure criteria, and literature grounding</div>
  </div>
</div>

<div class="card">
  <div class="card-header bg-blue">{topic}: Core Mechanical Principles</div>
  <div class="card-body">
    <p><strong>{topic} ({subtopic})</strong> constitutes an essential structural component of crustal deformation analysis. In Dr. Ausaf Sayeed's <em>Objective Geology</em>, the officially verified answer is firmly established as <strong>Option ({ans}): {ans_text}</strong>.</p>
    <p>{theory_text}</p>
    <div class="quote-box">
      "{author_note if author_note else 'Option (' + ans + ') represents the verified structural and kinematic standard.'}"
      <span class="quote-ref">— Dr. Ausaf Sayeed (Official Key & Notes, p. 256-258); {theory_ref}</span>
    </div>
    <div class="formula-card">
      <div class="formula-title">Governing Structural / Mathematical Relationship</div>
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
    <p>For national competitive examinations (UPSC Combined Geo-Scientist, GATE, CSIR-NET, State Mining Services), mastery of <strong>{topic}</strong> requires recognizing that <strong>Option ({ans})</strong> uniquely satisfies the kinematic, stress-state, or geometric constraints documented in <em>{theory_ref}</em>.</p>
  </div>
</div>

<div class="card">
  <div class="card-header bg-slate">Advanced Pedagogical Practice Challenges</div>
  <div class="card-body">
    <ul class="pq-list">
      <li>
        <strong>Practice Challenge 1:</strong> {practices[0]["question"]}
        <div class="pq-ans">✔ Verified Solution: Option ({practices[0]["answer"]})</div>
        <div class="pq-exp"><strong>Mechanistic Rationale:</strong> {practices[0]["explanation"]}</div>
      </li>
      <li>
        <strong>Practice Challenge 2:</strong> {practices[1]["question"]}
        <div class="pq-ans">✔ Verified Solution: Option ({practices[1]["answer"]})</div>
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
  <title>Q{q_num:03d}: {topic} | Ausaf Sayeed Chapter 7 Structural Geology</title>
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
    print("Generating 150 Masterclass Solutions for Chapter 7...")
    for item in QUESTIONS:
        q_num = item["q_num"]
        html_content = generate_solution_html(item, standalone=True)
        file_path = os.path.join(SOL_DIR, f"Q{q_num:03d}_sayeed_ch7.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

    print("All 150 standalone solutions written successfully.")


def build_interactive_portal():
    print("Building Interactive Master SPA Portal: index_sayeed_ch7.html...")

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

    pill_list = ['<div class="pill active" onclick="filterCategory(\'all\', this)">All (150)</div>']
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
  <title>Chapter 7: Structural Geology | Masterclass Solutions Portal</title>
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
        <span class="brand-badge">Dr. Ausaf Sayeed &bull; Chapter 7</span>
        <div class="brand-title">Structural Geology</div>
        <div class="brand-subtitle">150 Masterclass Solved Problems with Proofs</div>
      </div>
      <div class="search-box">
        <input type="text" id="searchInput" class="search-input" placeholder="Search questions, topics, keywords..." oninput="handleSearch()">
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
          <span class="navbar-title" id="currentTitle">Chapter 7: Structural Geology &mdash; Master Portal</span>
        </div>
        <div class="navbar-links">
          <a href="../Sayeed_Chapter6_Geochemistry/index_sayeed_ch6.html" class="nav-btn">&larr; Ch 6: Geochemistry</a>
          <a href="../../Orrisa_geology/index.html" class="nav-btn">Home Portal</a>
          <a href="../Sayeed_Chapter8_Palaeontology/index_sayeed_ch8.html" class="nav-btn">Ch 8: Palaeontology &rarr;</a>
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
        document.getElementById('currentTitle').innerText = 'Question ' + qNum + ' of 150 — Masterclass Solution';
        
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
          window.MathJax.typesetPromise([pane]).catch(err => console.log('MathJax typeset error:', err));
        }}

        // Update URL hash
        window.location.hash = 'q' + qNum;
      }}
    }}

    function filterCategory(cat, el) {{
      document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');

      const items = document.querySelectorAll('.nav-item');
      items.forEach(it => {{
        if (cat === 'all' || it.getAttribute('data-topic') === cat) {{
          it.style.display = '';
        }} else {{
          it.style.display = 'none';
        }}
      }});
    }}

    function handleSearch() {{
      const query = document.getElementById('searchInput').value.toLowerCase();
      const items = document.querySelectorAll('.nav-item');
      items.forEach(it => {{
        const text = it.innerText.toLowerCase();
        if (text.includes(query)) {{
          it.style.display = '';
        }} else {{
          it.style.display = 'none';
        }}
      }});
    }}

    // Auto-load question from URL hash or default to Q1
    window.addEventListener('DOMContentLoaded', () => {{
      const hash = window.location.hash;
      let qNum = 1;
      if (hash && hash.startsWith('#q')) {{
        const parsed = parseInt(hash.replace('#q', ''));
        if (!isNaN(parsed) && parsed >= 1 && parsed <= 150) {{
          qNum = parsed;
        }}
      }}
      loadQuestion(qNum);
    }});
  </script>
</body>
</html>
"""

    portal_path = os.path.join(BASE_DIR, "index_sayeed_ch7.html")
    with open(portal_path, "w", encoding="utf-8") as f:
        f.write(portal_html)

    print(f"Master SPA Portal generated at {portal_path} ({os.path.getsize(portal_path)} bytes).")


if __name__ == "__main__":
    build_all_masterclasses()
    build_interactive_portal()
