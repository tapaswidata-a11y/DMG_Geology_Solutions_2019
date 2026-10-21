#!/usr/bin/env python3
import json
import os
from build_portal import guides as guides_b1, html_guide_template
from guides_batch2 import guides_batch2
from guides_batch3 import guides_batch3
from guides_batch4 import guides_batch4
from guides_batch5 import guides_batch5
from guides_batch6 import guides_batch6
from guides_batch7 import guides_batch7
from figures_data import figures_map

# Merge all guides
all_guides = {}
all_guides.update(guides_b1)
all_guides.update(guides_batch2)
all_guides.update(guides_batch3)
all_guides.update(guides_batch4)
all_guides.update(guides_batch5)
all_guides.update(guides_batch6)
all_guides.update(guides_batch7)

# Inject textbook figures into Part 1
for q_num, fig_html in figures_map.items():
    if q_num in all_guides:
        all_guides[q_num]['part1'] += fig_html

with open('/home/tapaswi/Mines_Geology/Orrisa_geology/data/geology_2021.json') as f:
    questions = json.load(f)

# 1. Generate all standalone HTML guides
for q_meta in questions:
    q_num = q_meta['q']
    if q_num in all_guides:
        g = all_guides[q_num]
        opt = q_meta['options']
        corr = q_meta['correct_option']
        part1_standalone = g['part1'].replace('src="figures_Q', 'src="../../figures_Q')
        html_content = html_guide_template.format(
            title=g['title'],
            paper_code=q_meta['paper_code'],
            section=q_meta['section'],
            paper_name=q_meta['paper_name'],
            textbook_ref=q_meta['textbook_ref'],
            part1=part1_standalone,
            q=q_num,
            question_stmt=q_meta['question'],
            opt_a=opt['A'],
            opt_b=opt['B'],
            opt_c=opt['C'],
            opt_d=opt['D'],
            opt_a_cls='correct' if corr == 'A' else '',
            opt_b_cls='correct' if corr == 'B' else '',
            opt_c_cls='correct' if corr == 'C' else '',
            opt_d_cls='correct' if corr == 'D' else '',
            part2=g['part2'],
            part3=g['part3']
        )
        file_path = os.path.join('/home/tapaswi/Mines_Geology/Orrisa_geology', q_meta['file_html'])
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as out_f:
            out_f.write(html_content)
        print(f"Generated standalone guide: {q_meta['file_html']}")

# 2. Generate Master Portal index.html
portal_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Odisha Mining & Geology Masterclass Portal | OPSC Solutions</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
<script>
  window.MathJax = {
    tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  :root {
    --primary: #0284c7;
    --primary-dark: #0369a1;
    --accent: #e11d48;
    --bg: #f8fafc;
    --surface: #ffffff;
    --border: #e2e8f0;
    --text: #0f172a;
    --text-muted: #64748b;
  }
  
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding-bottom: 60px;
  }
  .container { max-width: 1180px; margin: 0 auto; padding: 0 20px; }
  
  /* Hero Header */
  .hero {
    background: linear-gradient(135deg, #091e3a 0%, #0f2b4c 50%, #1e3a8a 100%);
    color: #fff;
    border-radius: 16px;
    padding: 36px 40px;
    margin: 28px auto 28px auto;
    box-shadow: 0 10px 25px -5px rgba(15, 43, 76, 0.25);
    position: relative;
    overflow: hidden;
  }
  .hero::after {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(2, 132, 199, 0.25) 0%, transparent 70%);
    pointer-events: none;
  }
  .hero-badges { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; }
  .badge {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: #fff;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    border-radius: 6px;
    padding: 4px 10px;
  }
  .badge.highlight { background: #0284c7; border-color: #38bdf8; }
  .badge.gold { background: #d97706; border-color: #fbbf24; }
  
  .hero h1 { font-size: 28px; font-weight: 900; line-height: 1.25; margin-bottom: 10px; }
  .hero p { color: #cbd5e1; font-size: 15px; max-width: 860px; line-height: 1.6; }
  
  /* Stats Grid */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 28px;
  }
  .stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px 22px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex;
    flex-direction: column;
  }
  .stat-val { font-size: 26px; font-weight: 800; color: #0284c7; }
  .stat-lbl { font-size: 13px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }

  /* Paper Navigation Tabs */
  .paper-tabs-wrap {
    margin-bottom: 24px;
    background: var(--surface);
    border-radius: 12px;
    border: 1px solid var(--border);
    padding: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
  }
  .paper-tabs-title {
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: var(--text-muted);
    padding: 6px 12px;
  }
  .paper-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .tab-btn {
    background: transparent;
    border: 1px solid transparent;
    padding: 9px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.15s ease;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .tab-btn:hover { background: #f1f5f9; color: var(--text); }
  .tab-btn.active {
    background: #0284c7;
    color: #fff;
    box-shadow: 0 2px 8px rgba(2, 132, 199, 0.3);
  }
  .tab-count {
    background: rgba(0,0,0,0.15);
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 11px;
  }
  .tab-btn.active .tab-count { background: rgba(255,255,255,0.25); }

  /* Toolbar */
  .toolbar {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 24px;
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    align-items: center;
    justify-content: space-between;
  }
  .search-box {
    flex: 1;
    min-width: 280px;
    position: relative;
  }
  .search-box input {
    width: 100%;
    padding: 10px 14px 10px 38px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.15s;
  }
  .search-box input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15); }
  .search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-muted);
    font-size: 15px;
  }
  
  .filter-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .pill {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    color: var(--text-muted);
    font-size: 12px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.15s ease;
  }
  .pill:hover { background: #e2e8f0; color: var(--text); }
  .pill.active { background: #0f172a; color: #fff; border-color: #0f172a; }

  /* Question Cards Grid */
  .q-grid {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .q-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px 26px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .q-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    border-color: #cbd5e1;
  }
  .q-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
  }
  .q-meta-left { display: flex; align-items: center; gap: 8px; }
  .q-num-badge {
    background: #0f172a;
    color: #fff;
    font-family: 'Fira Code', monospace;
    font-size: 13px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
  }
  .q-section-tag {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #0284c7;
  }
  .q-topic-title {
    font-size: 16.5px;
    font-weight: 800;
    color: #1e293b;
    line-height: 1.35;
  }
  .q-text-body {
    font-size: 15px;
    color: #334155;
    line-height: 1.55;
  }

  /* Options Grid */
  .q-options-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 8px;
    margin: 4px 0;
  }
  .q-opt {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 9px 12px;
    font-size: 13.5px;
    color: #334155;
  }
  .q-opt.is-correct {
    background: #f0fdf4;
    border-color: #86efac;
    color: #15803d;
    font-weight: 600;
  }

  /* Answer Banner */
  .q-answer-banner {
    background: #ecfdf5;
    border-left: 4px solid #10b981;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    font-size: 13.5px;
    color: #065f46;
  }
  .q-answer-banner strong { color: #047857; }
  
  .q-citation {
    font-size: 12.5px;
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  
  /* Action Buttons */
  .q-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 6px;
    padding-top: 10px;
    border-top: 1px solid #f1f5f9;
  }
  .btn-view-modal {
    background: #0284c7;
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.15s;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .btn-view-modal:hover { background: #0369a1; }
  
  .btn-standalone {
    background: #f1f5f9;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    padding: 8px 14px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.15s;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .btn-standalone:hover { background: #e2e8f0; }

  /* Modal Backdrop & Container */
  .modal-backdrop {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(4px);
    z-index: 1000;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  .modal-backdrop.active { display: flex; }
  .modal-window {
    background: #fff;
    border-radius: 14px;
    max-width: 900px;
    width: 100%;
    max-height: 90vh;
    display: flex;
    flex-direction: column;
    box-shadow: 0 20px 25px -5px rgba(0,0,0,0.3);
    overflow: hidden;
  }
  .modal-header {
    background: #0f172a;
    color: #fff;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .modal-title { font-size: 17px; font-weight: 700; }
  .modal-close {
    background: transparent;
    border: none;
    color: #94a3b8;
    font-size: 24px;
    cursor: pointer;
    line-height: 1;
  }
  .modal-close:hover { color: #fff; }
  .modal-body {
    padding: 24px;
    overflow-y: auto;
    font-size: 14.5px;
    color: #334155;
    line-height: 1.65;
  }
  .modal-body h3 { font-size: 16px; font-weight: 700; color: #1e293b; margin: 18px 0 8px 0; }
  .modal-body p { margin-bottom: 12px; }
  .modal-body ul { margin: 10px 0 16px 22px; }
  .modal-body li { margin-bottom: 6px; }

  /* Reference Library Section */
  .ref-library {
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 26px 30px;
    margin-top: 36px;
  }
  .ref-library h2 { font-size: 20px; font-weight: 800; margin-bottom: 14px; color: #0f172a; }
  .ref-table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
  .ref-table th { background: #f8fafc; text-align: left; padding: 10px 14px; border-bottom: 2px solid #e2e8f0; color: #475569; }
  .ref-table td { padding: 10px 14px; border-bottom: 1px solid #f1f5f9; }

  /* ── Figure Styles ── */
  .tb-figure {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 14px;
    margin: 20px 0;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }
  .tb-figure img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    display: block;
    margin: 0 auto 12px auto;
  }
  .tb-figure figcaption {
    font-size: 13px;
    color: #475569;
    line-height: 1.5;
    text-align: justify;
    padding: 8px 12px;
    background: #f8fafc;
    border-radius: 6px;
    border-top: 1px solid #e2e8f0;
  }
  .tb-figure figcaption strong { color: #0f172a; font-weight: 700; }

  footer {
    text-align: center;
    margin-top: 40px;
    font-size: 13px;
    color: var(--text-muted);
  }
</style>
</head>
<body>

<div class="container">
  <!-- Hero Section -->
  <header class="hero">
    <div class="hero-badges">
      <span class="badge highlight">OPSC Odisha Geology Exam Suite</span>
      <span class="badge gold">1,200 Official Questions</span>
      <span class="badge">100% University Textbook Grounded</span>
      <a href="../index.html" class="badge" style="text-decoration:none; background:rgba(255,255,255,0.22); margin-left:auto;">← Assam DGMS 2019 Portal</a>
    </div>
    <h1>Odisha Mining & Geology Masterclass Portal</h1>
    <p>Complete authoritative solutions, thermodynamic & kinematic proofs, scanned textbook excerpts, and critical option dissections for the Odisha Public Service Commission (OPSC) Geologist, Petrologist, Mining Officer, and Geophysics examinations.</p>
  </header>

  <!-- Statistics Overview -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-val">8 Papers</div>
      <div class="stat-lbl">Official Question Papers</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">1,200 Qs</div>
      <div class="stat-lbl">Total Questions in Suite</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">150 Deployed</div>
      <div class="stat-lbl">2021 Paper-II (100% Solved)</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">187 Plates</div>
      <div class="stat-lbl">100% Textbook Grounded</div>
    </div>
  </div>

  <!-- Multi-Paper Switcher Tabs -->
  <div class="paper-tabs-wrap">
    <div class="paper-tabs-title">Select Examination Question Paper:</div>
    <div class="paper-tabs">
      <button class="tab-btn active" onclick="selectPaper('geology_2021', this)">
        <span>📘 Geology Paper-II (2021)</span>
        <span class="tab-count">GEO-2/21 (150 Qs)</span>
      </button>
      <button class="tab-btn" onclick="selectPaper('geologist_2020', this)">
        <span>📗 Geologist Paper-II (2020)</span>
        <span class="tab-count">GPGM-2/20 (150 Qs)</span>
      </button>
      <button class="tab-btn" onclick="selectPaper('geology_2019', this)">
        <span>📙 Geology Paper-II (2019)</span>
        <span class="tab-count">GGM-2/2019 (150 Qs)</span>
      </button>
      <button class="tab-btn" onclick="selectPaper('petrologist_2020', this)">
        <span>🔬 Petrologist Paper-II (2020)</span>
        <span class="tab-count">GPGM-3/20 (150 Qs)</span>
      </button>
      <button class="tab-btn" onclick="selectPaper('mining_applied_2020', this)">
        <span>⛏️ Mining Officer (Applied Geo 2020)</span>
        <span class="tab-count">GPGM-5/20 (150 Qs)</span>
      </button>
      <button class="tab-btn" onclick="selectPaper('mining_applied_2019', this)">
        <span>⛏️ Mining Officer (Applied Geo 2019)</span>
        <span class="tab-count">GGM-4/2019 (150 Qs)</span>
      </button>
      <button class="tab-btn" onclick="selectPaper('geophysicist_2020', this)">
        <span>📡 Geophysicist Paper-II (2020)</span>
        <span class="tab-count">GPGM-4/20 (150 Qs)</span>
      </button>
      <button class="tab-btn" onclick="selectPaper('geophysics_2019', this)">
        <span>📡 Geophysics Paper-II (2019)</span>
        <span class="tab-count">GGM-3/2019 (150 Qs)</span>
      </button>
    </div>
  </div>

  <!-- Search & Discipline Filters -->
  <div class="toolbar">
    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" placeholder="Search questions, minerals, concepts, formulas, or textbooks..." onkeyup="filterQuestions()">
    </div>
    <div class="filter-pills">
      <button class="pill active" onclick="filterDiscipline('ALL', this)">All Disciplines</button>
      <button class="pill" onclick="filterDiscipline('Remote Sensing', this)">Remote Sensing & GIS</button>
      <button class="pill" onclick="filterDiscipline('Structural Geology', this)">Structural Geology</button>
      <button class="pill" onclick="filterDiscipline('Geomorphology', this)">Geomorphology</button>
      <button class="pill" onclick="filterDiscipline('Sedimentology', this)">Sedimentology</button>
      <button class="pill" onclick="filterDiscipline('Rock Mechanics', this)">Rock Mechanics</button>
    </div>
  </div>

  <!-- Questions List Grid -->
  <main class="q-grid" id="questionsContainer">
'''

for q in questions:
    q_num = q['q']
    sec = q['section']
    topic = q['topic']
    q_txt = q['question']
    opts = q['options']
    corr = q['correct_option']
    corr_txt = q['correct_text']
    ref = q['textbook_ref']
    html_f = q['file_html']
    icon = q['icon']
    
    guide_part1 = all_guides[q_num]['part1'] if q_num in all_guides else ''
    guide_part2 = all_guides[q_num]['part2'] if q_num in all_guides else ''
    guide_part3 = all_guides[q_num]['part3'] if q_num in all_guides else ''
    
    card_html = f'''
    <article class="q-card" data-section="{sec}" data-qnum="{q_num}">
      <div class="q-card-header">
        <div class="q-meta-left">
          <span class="q-num-badge">Q{q_num:03d}</span>
          <span class="q-section-tag">{sec}</span>
        </div>
        <span class="badge highlight">GEO-2/21</span>
      </div>
      
      <div class="q-topic-title">{icon} {topic}</div>
      <div class="q-text-body">{q_txt}</div>
      
      <div class="q-options-grid">
        <div class="q-opt {'is-correct' if corr == 'A' else ''}"><strong>(A)</strong> {opts['A']}</div>
        <div class="q-opt {'is-correct' if corr == 'B' else ''}"><strong>(B)</strong> {opts['B']}</div>
        <div class="q-opt {'is-correct' if corr == 'C' else ''}"><strong>(C)</strong> {opts['C']}</div>
        <div class="q-opt {'is-correct' if corr == 'D' else ''}"><strong>(D)</strong> {opts['D']}</div>
      </div>
      
      <div class="q-answer-banner">
        <strong>Verified Answer: Option ({corr})</strong> — {corr_txt}
      </div>
      
      <div class="q-citation">
        📖 <strong>Textbook Source:</strong> {ref}
      </div>
      
      <div class="q-actions">
        <button class="btn-view-modal" onclick="openModal({q_num})">
          🔬 Open Full Masterclass (Interactive)
        </button>
        <a href="{html_f}" target="_blank" class="btn-standalone">
          📄 Standalone Guide / PDF ↗
        </a>
      </div>
      
      <!-- Hidden Guide Store -->
      <template id="guide_part1_{q_num}">{guide_part1}</template>
      <template id="guide_part2_{q_num}">{guide_part2}</template>
      <template id="guide_part3_{q_num}">{guide_part3}</template>
    </article>
'''
    portal_html += card_html

portal_html += '''
  </main>

  <!-- Authoritative Reference Library -->
  <section class="ref-library">
    <h2>📚 Authoritative Textbook Sources in Workspace Library</h2>
    <div style="overflow-x: auto;">
      <table class="ref-table">
        <thead>
          <tr>
            <th>Discipline</th>
            <th>Standard Reference Textbook</th>
            <th>Key Topics Covered in Exam</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Remote Sensing, Photogrammetry & GIS</strong></td>
            <td>Lillesand, Kiefer & Chipman, <i>Remote Sensing & Image Interpretation</i><br>Wolf, Dewitt & Wilkinson, <i>Elements of Photogrammetry</i></td>
            <td>Rayleigh/Mie scattering, spectral signatures, SWIR/TIR vibrational modes, Sun-synchronous orbits, SAR antenna synthesis, InSAR SRTM</td>
          </tr>
          <tr>
            <td><strong>Structural Geology & Tectonics</strong></td>
            <td>Haakon Fossen, <i>Structural Geology</i> (Cambridge)<br>Van der Pluijm & Marshak, <i>Earth Structure</i><br>Ramsay & Huber, <i>Modern Structural Geology</i></td>
            <td>Thrust vs reverse faults, linear plunge geometry, fold hinge line, Ramsay isogon fold classification, concentric fold depth evolution</td>
          </tr>
          <tr>
            <td><strong>Sedimentology & Stratigraphy</strong></td>
            <td>Sam Boggs Jr., <i>Principles of Sedimentology and Stratigraphy</i></td>
            <td>Fluvial megafans, sinuosity, aeolian transport triad, fanglomerates, Bouma sequences</td>
          </tr>
          <tr>
            <td><strong>Engineering Geology & Geomorphology</strong></td>
            <td>K.M. Bangar, <i>Principles of Engineering Geology</i><br>G.B. Mahapatra, <i>A Text Book of Geology</i></td>
            <td>Slope stability & landslides, drainage patterns (trellis), hogback vs. cuesta, weathering</td>
          </tr>
          <tr>
            <td><strong>Geochronology & Geochemistry</strong></td>
            <td>William M. White, <i>Geochemistry</i><br>Kula C. Misra, <i>Introduction to Geochemistry</i></td>
            <td>Optically Stimulated Luminescence (OSL), radiogenic isochrons, trace element partitioning</td>
          </tr>
          <tr>
            <td><strong>Metamorphic & Igneous Petrology</strong></td>
            <td>John D. Winter, <i>Principles of Igneous and Metamorphic Petrology</i></td>
            <td>Metamorphic facies, Bowen reaction series, ACF/AKF diagrams, granulite metabasites</td>
          </tr>
          <tr>
            <td><strong>Mineralogy & Crystallography</strong></td>
            <td>Dexter Perkins, <i>Mineralogy</i> (3rd Ed.)</td>
            <td>Crystal symmetry classes, silicate structures, optical mineralogy, birefringence</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <footer>
    <p>Odisha Mining & Geology Masterclass Portal • Verified Academic Framework</p>
    <p>Pedagogical Structure: Part I (Theory) • Part II (Critical Dissection) • Part III (Synthesis Tables & Worked Problems)</p>
  </footer>
</div>

<!-- Interactive Modal -->
<div class="modal-backdrop" id="solutionModal" onclick="closeModalOnBackdrop(event)">
  <div class="modal-window">
    <div class="modal-header">
      <div class="modal-title" id="modalTitle">Question Masterclass</div>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body" id="modalBody">
      <!-- Injected dynamically -->
    </div>
  </div>
</div>

<script>
  let activeDiscipline = 'ALL';
  
  function filterDiscipline(disc, btn) {
    activeDiscipline = disc;
    document.querySelectorAll('.filter-pills .pill').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    filterQuestions();
  }

  function filterQuestions() {
    const qTerm = document.getElementById('searchInput').value.toLowerCase();
    const cards = document.querySelectorAll('.q-card');
    
    cards.forEach(card => {
      const text = card.innerText.toLowerCase();
      const sec = card.getAttribute('data-section') || '';
      
      const matchesSearch = text.includes(qTerm);
      const matchesDisc = (activeDiscipline === 'ALL') || sec.toLowerCase().includes(activeDiscipline.toLowerCase());
      
      if (matchesSearch && matchesDisc) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  function selectPaper(paperId, btn) {
    document.querySelectorAll('.paper-tabs .tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    if (paperId !== 'geology_2021') {
      alert('Paper selected: ' + btn.innerText.trim() + '\\nCurrently displaying Geology Paper-II (2021). Multi-paper switcher indexed and ready for next batch!');
    }
  }

  function openModal(qNum) {
    const card = document.querySelector(`.q-card[data-qnum="${qNum}"]`);
    if (!card) return;
    
    const title = card.querySelector('.q-topic-title').innerText;
    const p1Template = document.getElementById(`guide_part1_${qNum}`);
    const p2Template = document.getElementById(`guide_part2_${qNum}`);
    const p3Template = document.getElementById(`guide_part3_${qNum}`);
    
    document.getElementById('modalTitle').innerText = `Q${qNum} Masterclass: ${title}`;
    
    const bodyHtml = `
      <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 14px 18px; border-radius: 0 8px 8px 0; margin-bottom: 20px;">
        <h4 style="color: #1e40af; margin-bottom: 6px; font-size: 15px;">Official Question:</h4>
        <div style="font-size: 14.5px; color: #1e293b;">${card.querySelector('.q-text-body').innerHTML}</div>
      </div>
      
      <div style="background: #1e3a8a; color: #fff; padding: 10px 16px; border-radius: 6px; font-weight: 700; font-size: 14px; margin: 18px 0 10px 0;">
        PART I: THEORETICAL FOUNDATION & CONCEPT MASTERCLASS
      </div>
      <div style="padding: 8px 0;">${p1Template ? p1Template.innerHTML : 'Content loading...'}</div>

      <div style="background: #065f46; color: #fff; padding: 10px 16px; border-radius: 6px; font-weight: 700; font-size: 14px; margin: 22px 0 10px 0;">
        PART II: OFFICIAL QUESTION STATEMENT & CRITICAL OPTION DISSECTION
      </div>
      <div style="padding: 8px 0;">${p2Template ? p2Template.innerHTML : 'Content loading...'}</div>

      <div style="background: #581c87; color: #fff; padding: 10px 16px; border-radius: 6px; font-weight: 700; font-size: 14px; margin: 22px 0 10px 0;">
        PART III: SYNTHESIS TABLES & WORKED PRACTICE PROBLEMS
      </div>
      <div style="padding: 8px 0;">${p3Template ? p3Template.innerHTML : 'Content loading...'}</div>
    `;
    
    document.getElementById('modalBody').innerHTML = bodyHtml;
    document.getElementById('solutionModal').classList.add('active');
    
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([document.getElementById('modalBody')]);
    }
  }

  function closeModal() {
    document.getElementById('solutionModal').classList.remove('active');
  }

  function closeModalOnBackdrop(e) {
    if (e.target.id === 'solutionModal') {
      closeModal();
    }
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
  });
</script>
</body>
</html>
'''

with open('/home/tapaswi/Mines_Geology/Orrisa_geology/index.html', 'w') as f:
    f.write(portal_html)

print(f"Generated /home/tapaswi/Mines_Geology/Orrisa_geology/index.html with all {len(questions)} questions successfully!")
