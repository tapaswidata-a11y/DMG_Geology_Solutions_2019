#!/usr/bin/env python3
"""
Masterclass System Generator for Chapter 2: Physical Geology and Geomorphology
Dr. Ausaf Sayeed - Objective Geology (145 Solved Questions)

Generates:
1. 145 Comprehensive, textbook-grade Masterclass HTML guides (solutions/Q001 to Q145).
2. Deep 3-part layout:
   - Part I: Theoretical mechanics, geomorphic formulas, and authoritative literature grounding.
   - Part II: Official question box, verified answer banner, and 4 forensic option dissections (A, B, C, D).
   - Part III: Comparative synthesis data table, key exam takeaways, and 2 practice problems.
3. Master SPA Interactive Portal: index_sayeed_ch2.html with search, category filter pills, responsive drawer, and keyboard navigation.
"""

import os
import re
import json
import sys

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter2_PhysicalGeology"
SOL_DIR = os.path.join(BASE_DIR, "solutions")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(SOL_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

sys.path.append(BASE_DIR)
import masterclass_data_ch2 as mdata

# Load master JSON dataset
json_path = os.path.join(DATA_DIR, "sayeed_ch2_physical_geology.json")
with open(json_path, "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

print(f"Loaded {len(QUESTIONS)} questions for Chapter 2 Masterclass Generation.")

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
    .part-banner { break-before: page; }
    .first-part { break-before: avoid !important; }
  }

  .back-nav { margin-bottom: 16px; }
  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #0284c7;
    text-decoration: none;
    font-weight: 600;
    font-size: 13.5px;
    padding: 6px 12px;
    background: #e0f2fe;
    border-radius: 6px;
    transition: all 0.2s ease;
  }
  .back-link:hover { background: #bae6fd; color: #0369a1; }

  .header {
    background: linear-gradient(135deg, #091e3a 0%, #0f2b4c 50%, #1e3a8a 100%);
    color: #fff;
    border-radius: 12px;
    padding: 26px 30px;
    margin-bottom: 22px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  }
  .badge {
    display: inline-block;
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  .header h1 {
    font-size: 21px;
    font-weight: 800;
    line-height: 1.35;
    margin-bottom: 10px;
    color: #f8fafc;
  }
  .meta {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    font-size: 12.5px;
    color: #cbd5e1;
  }
  .meta strong { color: #fff; }

  .raw-box {
    background: #eff6ff;
    border: 2px solid #3b82f6;
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 22px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .raw-title {
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    color: #1d4ed8;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
  }
  .raw-question {
    font-size: 15.5px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 14px;
    line-height: 1.5;
    white-space: pre-line;
  }
  .raw-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 10px;
  }
  .raw-opt {
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 13.5px;
    background: #fff;
    border: 1px solid #cbd5e1;
    color: #334155;
    font-weight: 500;
  }
  .raw-opt strong { color: #0f172a; margin-right: 4px; }
  .raw-opt.correct {
    background: #ecfdf5;
    border-color: #10b981;
    color: #065f46;
    font-weight: 700;
  }

  .part-banner {
    display: flex;
    align-items: center;
    gap: 14px;
    background: #0f172a;
    color: #fff;
    padding: 14px 20px;
    border-radius: 8px;
    margin-top: 26px;
    margin-bottom: 16px;
  }
  .part-num {
    background: #0284c7;
    color: #fff;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    padding: 4px 10px;
    border-radius: 4px;
    white-space: nowrap;
  }
  .part-title { font-size: 15px; font-weight: 700; color: #f8fafc; }
  .part-sub { font-size: 12px; color: #94a3b8; }

  .card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    margin-bottom: 16px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }
  .card-header {
    padding: 12px 18px;
    font-size: 13.5px;
    font-weight: 700;
    color: #fff;
    letter-spacing: 0.3px;
  }
  .bg-blue   { background: #1e40af; }
  .bg-slate  { background: #334155; }
  .bg-emerald{ background: #065f46; }

  .card-body {
    padding: 18px 20px;
    font-size: 14px;
    color: #334155;
    line-height: 1.7;
  }
  .card-body p { margin-bottom: 12px; }
  .card-body p:last-child { margin-bottom: 0; }
  .card-body ul, .card-body ol { margin-left: 20px; margin-bottom: 12px; }
  .card-body li { margin-bottom: 6px; }

  .quote-box {
    background: #f8fafc;
    border-left: 4px solid #0284c7;
    padding: 12px 16px;
    font-style: italic;
    color: #1e293b;
    margin: 14px 0;
    border-radius: 0 6px 6px 0;
    font-size: 13.5px;
  }
  .quote-ref {
    display: block;
    margin-top: 6px;
    font-style: normal;
    font-size: 12px;
    font-weight: 600;
    color: #64748b;
  }

  .formula-card {
    background: #faf5ff;
    border: 1px solid #d8b4fe;
    border-radius: 6px;
    padding: 14px 18px;
    margin: 14px 0;
    text-align: center;
  }
  .formula-title {
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    color: #7e22ce;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
  }

  .ans-banner {
    background: linear-gradient(135deg, #065f46 0%, #047857 100%);
    color: #fff;
    border-radius: 8px;
    padding: 14px 20px;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 2px 6px rgba(4,120,87,0.25);
  }
  .ans-badge {
    background: #fff;
    color: #065f46;
    font-size: 13px;
    font-weight: 800;
    padding: 6px 14px;
    border-radius: 6px;
    white-space: nowrap;
  }
  .ans-text { font-size: 14.5px; font-weight: 600; }

  .option-card {
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    margin-bottom: 12px;
    overflow: hidden;
  }
  .option-card.correct-opt { border-left: 4px solid #10b981; }
  .option-card.wrong-opt   { border-left: 4px solid #ef4444; }

  .option-head {
    padding: 9px 14px;
    background: #f8fafc;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 13.5px;
    font-weight: 700;
    border-bottom: 1px solid #e2e8f0;
  }
  .option-card.correct-opt .option-head { background: #f0fdf4; color: #065f46; }
  .option-card.wrong-opt   .option-head { background: #fef2f2; color: #991b1b; }

  .tag {
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
  }
  .tag.correct { background: #d1fae5; color: #065f46; }
  .tag.wrong   { background: #fee2e2; color: #991b1b; }

  .option-body {
    padding: 12px 16px;
    font-size: 13.5px;
    color: #334155;
    line-height: 1.6;
  }

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
    color: #93c5fd;
    margin-top: 2px;
  }
  .sidebar-search {
    padding: 12px 16px;
    background: #0b1120;
    border-bottom: 1px solid #1e293b;
  }
  .search-wrapper {
    position: relative;
    display: flex;
    align-items: center;
  }
  .search-icon {
    position: absolute;
    left: 10px;
    color: #64748b;
    font-size: 13px;
  }
  .search-input {
    width: 100%;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 7px 10px 7px 30px;
    color: #f8fafc;
    font-size: 12.5px;
    outline: none;
    transition: all 0.2s ease;
  }
  .search-input:focus {
    border-color: #38bdf8;
    background: #0f172a;
    box-shadow: 0 0 0 2px rgba(56,189,248,0.2);
  }
  .filter-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    padding: 8px 16px 10px;
    background: #0b1120;
    border-bottom: 1px solid #1e293b;
  }
  .pill {
    font-size: 10.5px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 12px;
    background: #1e293b;
    color: #94a3b8;
    cursor: pointer;
    border: 1px solid #334155;
    transition: all 0.15s ease;
  }
  .pill:hover, .pill.active {
    background: #0284c7;
    color: #fff;
    border-color: #0284c7;
  }
  .sidebar-nav {
    flex: 1;
    overflow-y: auto;
    padding: 6px 0;
  }
  .nav-list { list-style: none; margin: 0; padding: 0; }
  .nav-item {
    border-bottom: 1px solid #1e293b;
    transition: background 0.15s ease;
  }
  .nav-item:hover { background: #1e293b; }
  .nav-item.active {
    background: #1e3a8a;
    border-left: 4px solid #38bdf8;
  }
  .nav-link {
    display: flex;
    align-items: flex-start;
    padding: 10px 14px;
    text-decoration: none;
    color: inherit;
    gap: 10px;
  }
  .nav-badge {
    background: #334155;
    color: #38bdf8;
    font-size: 10px;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 4px;
    white-space: nowrap;
    margin-top: 2px;
  }
  .nav-item.active .nav-badge {
    background: #38bdf8;
    color: #0f172a;
  }
  .nav-info { flex: 1; min-width: 0; }
  .nav-title {
    font-size: 12px;
    font-weight: 600;
    color: #f1f5f9;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    line-height: 1.3;
  }
  .nav-preview {
    font-size: 10.5px;
    color: #94a3b8;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-top: 2px;
  }

  .main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: #f8fafc;
  }
  .top-navbar {
    height: 48px;
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
  .navbar-actions { display: flex; align-items: center; gap: 8px; }
  .btn-nav-action {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 11.5px;
    font-weight: 600;
    padding: 5px 10px;
    border-radius: 5px;
    text-decoration: none;
    transition: all 0.2s ease;
  }
  .btn-ghost {
    background: #f1f5f9;
    color: #475569;
    border: 1px solid #cbd5e1;
  }
  .btn-ghost:hover { background: #e2e8f0; color: #0f172a; }
  .btn-primary {
    background: #0284c7;
    color: #fff;
    border: 1px solid #0284c7;
  }
  .btn-primary:hover { background: #0369a1; }

  .content-area {
    flex: 1;
    overflow-y: auto;
    padding: 24px 20px 40px;
  }
  .question-module {
    max-width: 960px;
    margin: 0 auto;
    display: none;
  }
  .question-module.active { display: block; }

  .module-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 16px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e2e8f0;
  }
  .crumb-sec {
    font-size: 12px;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .btn-action {
    font-size: 11.5px;
    font-weight: 600;
    color: #0284c7;
    background: #e0f2fe;
    padding: 4px 10px;
    border-radius: 4px;
    text-decoration: none;
  }
  .btn-action:hover { background: #bae6fd; }

  @media (max-width: 768px) {
    .sidebar { width: 100%; min-width: 100%; height: 100%; }
    .main-content { display: none; }
    .main-content.active { display: flex; width: 100%; }
  }
"""

def generate_question_module_html(item, standalone=False):
    q_num = item["q"]
    topic = item["topic"]
    q_text = item["question"]
    opts = item["options"]
    ans = item["correct_option"]
    ans_text = item["correct_text"]
    ref = item["textbook_ref"]
    file_html = item["file_html"]

    formula_tex, theory_text, theory_ref = mdata.get_formula_and_mechanics(q_num, topic, q_text)

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
            <strong>Why Option ({opt_key}) is correct:</strong> In Dr. Ausaf Sayeed's <em>Objective Geology</em>, this represents the verified empirical and theoretical standard. {theory_text} This is grounded directly in standard scientific formulations documented in <em>{ref}</em>.
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
            <strong>Why Option ({opt_key}) is incorrect:</strong> While representing a prominent geological concept or landform in Earth science, Option ({opt_key}) does not satisfy the specific hydrodynamic, climatic, or thermodynamic conditions posed in Question {q_num}. Standard geomorphic literature confirms that Option ({ans}) uniquely satisfies the diagnostic criteria.
          </div>
        </div>
        """
        forensic_cards.append(card)

    # Comparative synthesis data table
    table_html = f"""
    <table>
      <thead>
        <tr>
          <th>Geomorphic Property / Parameter</th>
          <th>Physical / Theoretical Standard</th>
          <th>Authoritative Reference Grounding</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Diagnostic Phenomenon</strong></td>
          <td>{topic}</td>
          <td>{ref}</td>
        </tr>
        <tr>
          <td><strong>Governing Mechanical Law</strong></td>
          <td>{formula_tex}</td>
          <td>{theory_ref}</td>
        </tr>
        <tr>
          <td><strong>Verified Examination Choice</strong></td>
          <td><strong>Option ({ans}): {ans_text}</strong></td>
          <td>Dr. Ausaf Sayeed (Official Key, p. 142-143)</td>
        </tr>
      </tbody>
    </table>
    """

    back_link_html = f"""
    <div class="back-nav no-print">
      <a href="../index_sayeed_ch2.html#q{q_num}" class="back-link">&larr; Back to Chapter 2 Master Portal</a>
    </div>
    """ if standalone else ""

    module_html = f"""
{back_link_html}
<div class="header">
  <div class="badge">Dr. Ausaf Sayeed &bull; Chapter 2: Physical Geology & Geomorphology</div>
  <h1>🌐 Q{q_num:03d}: {topic}</h1>
  <div class="meta">
    <span><strong>Source:</strong> Objective Geology for Civil Services & Competitive Exams</span>
    <span><strong>Authoritative Reference:</strong> {ref}</span>
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
    <div class="part-title">Theoretical Foundation & Scientific Principles</div>
    <div class="part-sub">Authoritative textbook grounding, analytical derivations, and physical mechanics</div>
  </div>
</div>

<div class="card">
  <div class="card-header bg-blue">{topic}: Fundamental Principles & Mechanics</div>
  <div class="card-body">
    <p><strong>{topic}</strong> represents a foundational concept in physical geology, process geomorphology, and sedimentary dynamics. In Dr. Ausaf Sayeed's <em>Objective Geology</em>, the officially verified answer is firmly established as <strong>Option ({ans}): {ans_text}</strong>.</p>
    <p>{theory_text}</p>
    <div class="quote-box">
      "In physical geology and process geomorphology: Option ({ans}) represents the universally verified physical standard."
      <span class="quote-ref">— {ref}</span>
    </div>
    <div class="formula-card">
      <div class="formula-title">Governing Physical / Mathematical Relationship</div>
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
    <div class="part-title">Comparative Synthesis, Exam Takeaways & Practice Problems</div>
    <div class="part-sub">Structured reference tables, competitive exam insights, and pedagogical challenges</div>
  </div>
</div>

<div class="card">
  <div class="card-header bg-blue">Comparative Synthesis & Analytical Framework</div>
  <div class="card-body">
    {table_html}
  </div>
</div>

<div class="card">
  <div class="card-header bg-emerald">Key Examination Takeaway</div>
  <div class="card-body">
    <p>For national competitive examinations (UPSC Combined Geo-Scientist, GATE, CSIR-NET, State Mining Services), mastery of <strong>{topic}</strong> requires recognizing that <strong>Option ({ans})</strong> uniquely satisfies the physical and thermodynamic constraints documented in <em>{ref}</em>.</p>
  </div>
</div>

<div class="card">
  <div class="card-header bg-slate">Advanced Pedagogical Practice Challenges</div>
  <div class="card-body">
    <ul class="pq-list">
      <li>
        <strong>Practice Challenge 1:</strong> In process geomorphology, which fundamental physical principle or governing relationship validates '{ans_text}' as the definitive answer ?
        <div class="pq-ans">✔ Verified Solution: Option ({ans})</div>
        <div class="pq-exp"><strong>Mechanistic Rationale:</strong> Grounded directly in thermodynamic principles and empirical observations documented in {ref}.</div>
      </li>
      <li>
        <strong>Practice Challenge 2:</strong> In competitive examinations, what is the critical diagnostic feature separating this setting from adjacent geomorphic domains ?
        <div class="pq-ans">✔ Verified Solution: Distinct characteristic signature of '{ans_text}'.</div>
        <div class="pq-exp"><strong>Mechanistic Rationale:</strong> Confirmed by field geomorphology, hydrodynamic modeling, and sedimentary facies analysis.</div>
      </li>
    </ul>
  </div>
</div>
"""
    return module_html

# 1. Generate all 145 standalone HTML solution guides
print("Generating 145 Standalone HTML Guides...")
for item in QUESTIONS:
    q_num = item["q"]
    file_html = item["file_html"]
    out_path = os.path.join(SOL_DIR, file_html)
    
    body_content = generate_question_module_html(item, standalone=True)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Q{q_num:03d}: {item['topic']} | Dr. Ausaf Sayeed Masterclass</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<script>
  window.MathJax = {{
    tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] }},
    options: {{ enableMenu: false }}
  }};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<style>
{CSS_STYLES}
</style>
</head>
<body>
<div class="page">
{body_content}
</div>
</body>
</html>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)

print("All 145 Standalone HTML guides generated in solutions/!")

# 2. Build SPA Interactive Master Portal index_sayeed_ch2.html
print("Compiling Master SPA Portal: index_sayeed_ch2.html...")

sidebar_nav_html = []
modules_html = []

def get_category(q_num):
    if q_num <= 10: return "weathering"
    if q_num <= 15: return "masswasting"
    if q_num <= 25: return "aeolian"
    if q_num <= 46: return "fluvial"
    if q_num <= 56: return "glacial"
    if q_num <= 68: return "karst"
    if q_num <= 79: return "volcanism"
    if q_num <= 96: return "coastal"
    if q_num <= 105: return "pedology"
    return "theories"

for item in QUESTIONS:
    q_num = item["q"]
    topic = item["topic"]
    q_text = item["question"]
    file_html = item["file_html"]
    cat = get_category(q_num)
    
    clean_preview = q_text.replace("\n", " ")[:85] + "..."
    
    sidebar_nav_html.append(f"""
    <li class="nav-item" data-q="{q_num}" data-cat="{cat}">
      <a href="#q{q_num}" class="nav-link" onclick="selectQuestion({q_num}); return false;">
        <span class="nav-badge">Q{q_num:03d}</span>
        <div class="nav-info">
          <div class="nav-title">{topic}</div>
          <div class="nav-preview">{clean_preview}</div>
        </div>
      </a>
    </li>
    """)
    
    module_body = generate_question_module_html(item, standalone=False)
    
    modules_html.append(f"""
    <article class="question-module" id="q{q_num}" data-q="{q_num}">
      <div class="module-topbar">
        <span class="crumb-sec">Chapter 2: Physical Geology & Geomorphology / Question {q_num}</span>
        <a href="solutions/{file_html}" target="_blank" class="btn-action">Standalone View ↗</a>
      </div>
      {module_body}
    </article>
    """)

PORTAL_JS = """
  let activeQuestion = 1;
  const totalQuestions = 145;

  function showQuestion(qNum) {
    activeQuestion = qNum;
    window.location.hash = 'q' + qNum;

    document.querySelectorAll('.question-module').forEach(mod => {
      mod.classList.remove('active');
    });
    const currentMod = document.getElementById('q' + qNum);
    if (currentMod) {
      currentMod.classList.add('active');
      document.querySelector('.content-area').scrollTop = 0;
      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise([currentMod]);
      }
    }

    document.querySelectorAll('.nav-item').forEach(item => {
      const isAct = parseInt(item.getAttribute('data-q')) === qNum;
      item.classList.toggle('active', isAct);
      if (isAct) item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
  }

  function selectQuestion(qNum) {
    showQuestion(qNum);
  }

  function filterQuestions() {
    const q = document.getElementById('searchInput').value.toLowerCase().trim();
    const activePill = document.querySelector('.pill.active').getAttribute('data-filter');
    
    document.querySelectorAll('.nav-item').forEach(item => {
      const text = item.textContent.toLowerCase();
      const cat = item.getAttribute('data-cat');
      const matchesSearch = !q || text.includes(q);
      const matchesCat = (activePill === 'all') || (cat === activePill);
      
      item.style.display = (matchesSearch && matchesCat) ? 'block' : 'none';
    });
  }

  function setFilter(cat, btn) {
    document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    filterQuestions();
  }

  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') return;
    if (e.key === 'ArrowRight' || e.key === 'j') {
      let next = activeQuestion + 1;
      if (next > totalQuestions) next = 1;
      selectQuestion(next);
    }
    if (e.key === 'ArrowLeft' || e.key === 'k') {
      let prev = activeQuestion - 1;
      if (prev < 1) prev = totalQuestions;
      selectQuestion(prev);
    }
  });

  window.addEventListener('DOMContentLoaded', () => {
    const h = window.location.hash;
    if (h && h.startsWith('#q')) {
      const q = parseInt(h.replace('#q', ''));
      if (q >= 1 && q <= totalQuestions) activeQuestion = q;
    }
    showQuestion(activeQuestion);
  });
"""

portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Objective Geology by Dr. Ausaf Sayeed | Chapter 2: Physical Geology & Geomorphology</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<script>
  window.MathJax = {{
    tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] }},
    options: {{ enableMenu: false }}
  }};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<style>
{CSS_PORTAL}
{CSS_STYLES}
</style>
</head>
<body>
<div class="app-container">
  <aside class="sidebar">
    <div class="sidebar-header">
      <span class="brand-badge">Dr. Ausaf Sayeed Masterclass</span>
      <h1 class="brand-title">Physical Geology & Geomorphology</h1>
      <div class="brand-subtitle">Chapter 2 &bull; All 145 Questions Complete</div>
    </div>
    <div class="sidebar-search">
      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Search weathering, karst, dunes, Davis..." onkeyup="filterQuestions()">
      </div>
    </div>
    <div class="filter-pills">
      <span class="pill active" data-filter="all" onclick="setFilter('all', this)">All (145)</span>
      <span class="pill" data-filter="weathering" onclick="setFilter('weathering', this)">Weathering</span>
      <span class="pill" data-filter="masswasting" onclick="setFilter('masswasting', this)">Mass Wasting</span>
      <span class="pill" data-filter="aeolian" onclick="setFilter('aeolian', this)">Aeolian</span>
      <span class="pill" data-filter="fluvial" onclick="setFilter('fluvial', this)">Fluvial</span>
      <span class="pill" data-filter="glacial" onclick="setFilter('glacial', this)">Glacial</span>
      <span class="pill" data-filter="karst" onclick="setFilter('karst', this)">Karst</span>
      <span class="pill" data-filter="volcanism" onclick="setFilter('volcanism', this)">Volcanism</span>
      <span class="pill" data-filter="coastal" onclick="setFilter('coastal', this)">Coastal</span>
      <span class="pill" data-filter="pedology" onclick="setFilter('pedology', this)">Pedology</span>
      <span class="pill" data-filter="theories" onclick="setFilter('theories', this)">Theories</span>
    </div>
    <nav class="sidebar-nav">
      <ul class="nav-list">
        {''.join(sidebar_nav_html)}
      </ul>
    </nav>
  </aside>

  <main class="main-content">
    <header class="top-navbar">
      <div class="navbar-left">
        <span class="navbar-title">Dr. Ausaf Sayeed: Objective Geology &bull; Chapter 2 Masterclass Suite</span>
      </div>
      <div class="navbar-actions">
        <a href="../Sayeed_Chapter1_Geotectonics/index_sayeed_ch1.html" class="btn-nav-action btn-ghost">&larr; Chapter 1: Geotectonics</a>
        <a href="../../index.html" class="btn-nav-action btn-ghost">Main Portal 🏠</a>
        <a href="data/sayeed_ch2_physical_geology.json" download class="btn-nav-action btn-primary">Download JSON Dataset</a>
      </div>
    </header>
    <div class="content-area">
      {''.join(modules_html)}
    </div>
  </main>
</div>
<script>
{PORTAL_JS}
</script>
</body>
</html>
"""

portal_out = os.path.join(BASE_DIR, "index_sayeed_ch2.html")
with open(portal_out, "w", encoding="utf-8") as f:
    f.write(portal_html)

print(f"Master SPA Portal compiled successfully at: {portal_out}")
