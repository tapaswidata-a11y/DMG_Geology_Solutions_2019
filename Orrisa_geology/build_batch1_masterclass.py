#!/usr/bin/env python3
"""
Master Generator for Odisha Geology 2021 Solutions: Batch 1 (Q002 - Q010)
Geomorphology & Quaternary Geology
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""

import os
import re

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
SOLUTIONS_DIR = os.path.join(BASE_DIR, "solutions", "geology_2021")

CSS_STYLES = r"""
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
  
  .header {
    background: linear-gradient(135deg, #091e3a 0%, #0f2b4c 50%, #1e3a8a 100%);
    color: #fff;
    border-radius: 12px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  }
  .badge {
    display: inline-block;
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 4px;
    padding: 4px 10px;
    margin-bottom: 12px;
  }
  .header h1 { font-size: 23px; font-weight: 800; line-height: 1.35; }
  .header .meta { font-size: 13.5px; color: #cbd5e1; margin-top: 10px; line-height: 1.5; }
  
  .back-nav { margin-bottom: 16px; }
  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #0284c7;
    text-decoration: none;
    font-size: 13.5px;
    font-weight: 600;
  }
  .back-link:hover { text-decoration: underline; }

  /* Part Banners - Identical to Assam DGMS 2019 */
  .part-banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    color: #fff;
    border-radius: 10px;
    padding: 16px 24px;
    margin: 28px 0 20px 0;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 3px 10px rgba(37, 99, 235, 0.2);
  }
  .first-part { margin-top: 10px; }
  .part-banner.green {
    background: linear-gradient(135deg, #065f46 0%, #059669 100%);
    box-shadow: 0 3px 10px rgba(5, 150, 105, 0.2);
  }
  .part-banner.purple {
    background: linear-gradient(135deg, #581c87 0%, #7c3aed 100%);
    box-shadow: 0 3px 10px rgba(124, 58, 237, 0.2);
  }
  .part-num {
    font-size: 26px;
    font-weight: 800;
    opacity: 0.9;
    border-right: 2px solid rgba(255,255,255,0.3);
    padding-right: 14px;
    line-height: 1;
    font-family: 'Fira Code', monospace;
  }
  .part-title { font-size: 17.5px; font-weight: 700; letter-spacing: 0.3px; }
  .part-sub { font-size: 12.5px; opacity: 0.9; margin-top: 3px; }

  /* Cards */
  .card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    margin-bottom: 22px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
  }
  .card-header {
    padding: 12px 20px;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #fff;
  }
  .card-body { padding: 20px 24px; font-size: 14.5px; color: #334155; line-height: 1.65; }
  .card-body p { margin-bottom: 12px; }
  .card-body p:last-child { margin-bottom: 0; }
  .card-body ul, .card-body ol { margin: 10px 0 16px 20px; }
  .card-body li { margin-bottom: 8px; }

  .bg-blue    { background: #1d4ed8; }
  .bg-indigo  { background: #4338ca; }
  .bg-emerald { background: #047857; }
  .bg-purple  { background: #6d28d9; }
  .bg-amber   { background: #b45309; }
  .bg-slate   { background: #334155; }

  /* Textbook Quote Boxes */
  .quote-box {
    background: #eff6ff;
    border-left: 5px solid #2563eb;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin: 16px 0;
    font-style: italic;
    color: #1e3a8a;
    font-size: 13.5px;
    line-height: 1.6;
  }
  .quote-box.bangar {
    background: #f0fdf4;
    border-left-color: #059669;
    color: #064e3b;
  }
  .quote-ref {
    display: block;
    font-size: 12px;
    font-style: normal;
    font-weight: 700;
    margin-top: 8px;
    letter-spacing: 0.2px;
  }
  .quote-box.bangar .quote-ref { color: #047857; }

  /* Textbook Image Wrappers */
  .tb-figure {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 14px;
    margin: 20px 0;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  }
  .tb-figure img {
    max-width: 100%;
    max-height: 520px;
    height: auto;
    border-radius: 6px;
    display: block;
    margin: 0 auto 12px auto;
  }
  .tb-caption {
    font-size: 12.5px;
    color: #334155;
    margin-top: 10px;
    text-align: left;
    line-height: 1.5;
    background: #f8fafc;
    padding: 10px 14px;
    border-radius: 6px;
    border-left: 3px solid #0284c7;
  }
  .tb-caption strong { color: #0f172a; font-weight: 700; }

  /* Formula Card */
  .formula-card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: #f8fafc;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 16px 0;
    border-left: 4px solid #38bdf8;
  }
  .formula-title {
    font-size: 12px;
    font-weight: 700;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }

  /* Question Box */
  .question-box {
    background: #eff6ff;
    border: 2px solid #3b82f6;
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 20px;
  }
  .q-num {
    font-size: 12.5px;
    font-weight: 800;
    color: #1d4ed8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
  }
  .q-stmt {
    font-size: 15.5px;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.5;
  }
  .raw-options {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }
  .raw-opt {
    background: #fff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 14px;
    color: #334155;
  }
  .raw-opt.correct {
    background: #f0fdf4;
    border-color: #10b981;
    color: #065f46;
    font-weight: 700;
  }

  /* Answer Banner */
  .answer-banner {
    background: linear-gradient(90deg, #059669 0%, #10b981 100%);
    color: #fff;
    border-radius: 10px;
    padding: 16px 22px;
    margin-bottom: 22px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 3px 10px rgba(16, 185, 129, 0.2);
  }
  .answer-banner .tick { font-size: 32px; line-height: 1; font-weight: bold; }
  .answer-banner .text { font-size: 17.5px; font-weight: 700; }
  .answer-banner .sub { font-size: 13.5px; opacity: 0.95; margin-top: 4px; line-height: 1.45; }

  /* Option Dissection Cards */
  .option {
    border-radius: 8px;
    margin-bottom: 14px;
    overflow: hidden;
    border: 2px solid transparent;
  }
  .option.correct { border-color: #10b981; }
  .option.wrong   { border-color: #f43f5e; }
  .option-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    font-weight: 700;
    font-size: 14px;
  }
  .option.correct .option-header { background: #d1fae5; color: #065f46; }
  .option.wrong   .option-header { background: #ffe4e6; color: #9f1239; }
  .option-body { padding: 12px 16px 14px; background: #fafafa; font-size: 13.5px; color: #334155; line-height: 1.6; }
  .tag {
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    border-radius: 4px;
    padding: 2px 8px;
    margin-left: auto;
    text-transform: uppercase;
  }
  .tag.correct { background: #059669; color: #fff; }
  .tag.wrong   { background: #e11d48; color: #fff; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 14px 0; }
  th {
    background: #0f172a;
    color: #fff;
    padding: 10px 12px;
    text-align: left;
    font-weight: 600;
  }
  td { padding: 9px 12px; border-bottom: 1px solid #e2e8f0; }
  tr:nth-child(even) td { background: #f8fafc; }
  td:first-child { font-weight: 600; color: #0f172a; }

  /* Practice Questions List */
  .pq-list { list-style: none; padding: 0; }
  .pq-list li {
    background: #fffbeb;
    border: 1px solid #fef3c7;
    border-left: 4px solid #d97706;
    border-radius: 6px;
    padding: 13px 18px;
    margin-bottom: 14px;
    font-size: 13.5px;
  }
  .pq-list li strong { color: #92400e; font-size: 14px; }
  .pq-ans {
    margin-top: 6px;
    color: #065f46;
    font-weight: 700;
  }
  .pq-exp {
    margin-top: 4px;
    color: #475569;
    font-size: 13px;
    line-height: 1.55;
  }

  @media (max-width: 768px) {
    .raw-options { grid-template-columns: 1fr; }
  }
"""

def wrap_html(title, badge, h1_title, meta_text, q_num, part1_content, part2_content, part3_content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<script>
  window.MathJax = {{
    tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] }}
  }};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
{CSS_STYLES}
</style>
</head>
<body>
<div class="page">
  <div class="back-nav no-print">
    <a href="../../index.html#q{q_num}" class="back-link">← Back to Master Portal</a>
  </div>
  
  <div class="header">
    <div class="badge">{badge}</div>
    <h1>{h1_title}</h1>
    <div class="meta">
      {meta_text}
    </div>
  </div>

  <!-- PART I -->
  <div class="part-banner first-part">
    <div class="part-num">PART I</div>
    <div>
      <div class="part-title">Theoretical Foundation & Scientific Principles</div>
      <div class="part-sub">Authoritative textbook grounding, analytical derivations, and geodynamic mechanics</div>
    </div>
  </div>
  {part1_content}

  <!-- PART II -->
  <div class="part-banner green">
    <div class="part-num">PART II</div>
    <div>
      <div class="part-title">Official Examination Question & Critical Option Dissection</div>
      <div class="part-sub">Rigorous forensic analysis refuting all distractors with physical principles</div>
    </div>
  </div>
  {part2_content}

  <!-- PART III -->
  <div class="part-banner purple">
    <div class="part-num">PART III</div>
    <div>
      <div class="part-title">Synthesis Reference Tables & High-Yield Practice Questions</div>
      <div class="part-sub">8 Curated exam-standard practice problems with complete step-by-step worked solutions</div>
    </div>
  </div>
  {part3_content}

</div>
</body>
</html>
"""

print("Batch 1 master generator script initialized.")
