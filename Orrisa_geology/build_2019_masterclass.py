#!/usr/bin/env python3
"""
Master Generator for Odisha Geology 2019 Solutions
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""

import os
import re

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
SOLUTIONS_DIR = os.path.join(BASE_DIR, "solutions", "geology_2019")
os.makedirs(SOLUTIONS_DIR, exist_ok=True)

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
  .header h1 {
    font-size: 26px;
    font-weight: 800;
    line-height: 1.3;
    margin-bottom: 12px;
    color: #fff;
  }
  .header .meta {
    font-size: 13px;
    color: #cbd5e1;
    line-height: 1.6;
  }
  .back-nav {
    margin-bottom: 16px;
  }
  .back-link {
    display: inline-flex;
    align-items: center;
    color: #2563eb;
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
    background: #fff;
    padding: 6px 14px;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    transition: all 0.15s ease;
  }
  .back-link:hover {
    background: #f8fafc;
    border-color: #94a3b8;
    color: #1d4ed8;
  }
  
  .part-banner {
    display: flex;
    align-items: center;
    gap: 16px;
    border-radius: 8px;
    padding: 14px 20px;
    margin: 32px 0 18px 0;
    color: #fff;
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    box-shadow: 0 2px 8px rgba(37,99,235,0.25);
  }
  .part-banner.green {
    background: linear-gradient(135deg, #065f46 0%, #059669 100%);
    box-shadow: 0 2px 8px rgba(5,150,105,0.25);
  }
  .part-banner.purple {
    background: linear-gradient(135deg, #581c87 0%, #7c3aed 100%);
    box-shadow: 0 2px 8px rgba(124,58,237,0.25);
  }
  .part-num {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: -1px;
    opacity: 0.85;
    line-height: 1;
    padding-right: 14px;
    border-right: 2px solid rgba(255,255,255,0.3);
  }
  .part-title {
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  .part-sub {
    font-size: 12px;
    opacity: 0.85;
  }
  
  .card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    overflow: hidden;
  }
  .card-header {
    padding: 14px 20px;
    font-weight: 700;
    font-size: 15px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid #e2e8f0;
  }
  .card-header.bg-blue   { background: #eff6ff; color: #1e40af; border-left: 4px solid #2563eb; }
  .card-header.bg-emerald{ background: #ecfdf5; color: #065f46; border-left: 4px solid #059669; }
  .card-header.bg-indigo { background: #e0e7ff; color: #3730a3; border-left: 4px solid #4f46e5; }
  .card-header.bg-amber  { background: #fffbeb; color: #92400e; border-left: 4px solid #d97706; }
  .card-header.bg-red    { background: #fef2f2; color: #991b1b; border-left: 4px solid #dc2626; }
  .card-header.bg-slate  { background: #f8fafc; color: #334155; border-left: 4px solid #64748b; }
  .card-header.bg-purple { background: #faf5ff; color: #6b21a8; border-left: 4px solid #9333ea; }
  
  .card-body {
    padding: 20px 24px;
  }
  .card-body p { margin-bottom: 12px; }
  .card-body p:last-child { margin-bottom: 0; }
  .card-body ul, .card-body ol {
    margin: 8px 0 14px 24px;
  }
  .card-body li { margin-bottom: 6px; }
  
  .figure-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 16px;
    margin: 18px 0;
    text-align: center;
  }
  .figure-box img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    background: #fff;
  }
  .figure-caption {
    margin-top: 10px;
    font-size: 13px;
    color: #475569;
    text-align: left;
    line-height: 1.5;
  }
  
  .question-box {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 16px;
  }
  .options-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
    margin-top: 14px;
  }
  @media(min-width: 600px) {
    .options-grid { grid-template-columns: 1fr 1fr; }
  }
  .option-item {
    background: #fff;
    border: 1px solid #e2e8f0;
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 14px;
  }
  .answer-banner {
    background: #ecfdf5;
    border: 2px solid #059669;
    color: #065f46;
    border-radius: 8px;
    padding: 12px 18px;
    font-weight: 700;
    font-size: 15px;
    margin-top: 14px;
  }
  
  .option-card {
    border-radius: 8px;
    margin-bottom: 14px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
  }
  .option-card.option-correct {
    border-color: #86efac;
    background: #f0fdf4;
  }
  .option-card.option-wrong {
    border-color: #fecaca;
    background: #fff5f5;
  }
  .option-card-header {
    padding: 10px 16px;
    font-weight: 700;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .option-correct .option-card-header {
    background: #dcfce7;
    color: #166534;
  }
  .option-wrong .option-card-header {
    background: #fee2e2;
    color: #991b1b;
  }
  .option-card-body {
    padding: 12px 18px;
    font-size: 14px;
  }
  
  .math-block {
    background: #f8fafc;
    border-left: 3px solid #64748b;
    padding: 10px 16px;
    margin: 12px 0;
    font-size: 14px;
    border-radius: 0 6px 6px 0;
    overflow-x: auto;
  }
  .definition-box {
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-left: 4px solid #0284c7;
    border-radius: 6px;
    padding: 14px 18px;
    margin: 14px 0;
    font-size: 14px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 13.5px;
  }
  th, td {
    padding: 9px 12px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }
  th {
    background: #f1f5f9;
    font-weight: 700;
  }
  tr:nth-child(even) { background: #f8fafc; }
"""

def wrap_html_2019(q_num, title, badge, h1_title, meta_text, part1_content, part2_content, part3_content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
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
    <a href="../../index_2019.html#q{q_num}" class="back-link">← Back to 2019 Master Portal</a>
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

print("2019 Master Generator initialized successfully.")
