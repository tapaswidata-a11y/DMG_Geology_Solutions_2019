#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 1 to 5
Assam DGMS 2019 Masterclass Standard
"""

import os

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
SOLUTIONS_DIR = os.path.join(BASE_DIR, "solutions", "geology_2019")
os.makedirs(SOLUTIONS_DIR, exist_ok=True)

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
  .header h1 { font-size: 23px; font-weight: 800; line-height: 1.35; color: #fff; }
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
    background: #fff;
    padding: 6px 14px;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    transition: all 0.15s ease;
  }
  .back-link:hover { background: #f8fafc; border-color: #94a3b8; color: #0369a1; }

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
  .card-body ul, .card-body ol { margin: 8px 0 14px 24px; }
  .card-body li { margin-bottom: 6px; }

  .bg-blue    { background: #1d4ed8; }
  .bg-indigo  { background: #4338ca; }
  .bg-emerald { background: #047857; }
  .bg-purple  { background: #6d28d9; }
  .bg-amber   { background: #b45309; }
  .bg-slate   { background: #334155; }

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

def generate_page(q_num, filename, title, badge, h1_title, meta_text, part1_html, part2_html, part3_html):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | OPSC Geology 2019 Masterclass</title>
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
      <div class="part-sub">Authoritative textbook grounding, analytical derivations, and geomorphic mechanics</div>
    </div>
  </div>
  {part1_html}

  <!-- PART II -->
  <div class="part-banner green">
    <div class="part-num">PART II</div>
    <div>
      <div class="part-title">Official Examination Question & Critical Option Dissection</div>
      <div class="part-sub">Rigorous forensic analysis refuting all distractors with physical principles</div>
    </div>
  </div>
  {part2_html}

  <!-- PART III -->
  <div class="part-banner purple">
    <div class="part-num">PART III</div>
    <div>
      <div class="part-title">Synthesis Reference Tables & High-Yield Practice Questions</div>
      <div class="part-sub">8 Curated exam-standard practice problems with complete step-by-step worked solutions</div>
    </div>
  </div>
  {part3_html}

</div>
</body>
</html>"""
    filepath = os.path.join(SOLUTIONS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {filepath} ({len(html)} bytes)")

# ==========================================
# QUESTION 1: BAJADA & ALLUVIAL FAN
# ==========================================
q1_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Geomorphic Architecture of Piedmont Alluvial Fans & Bajadas</div>
    <div class="card-body">
      <p>An <strong>alluvial fan</strong> is a low, outspread, gently sloping mass of loose clastic alluvium shaped like an open fan or a segment of a low cone, deposited by a stream at the point of sudden topographic break—typically where a high-gradient mountain canyon emerges onto an adjacent piedmont lowland or rift basin floor. When adjacent mountain drainages emerge in close proximity along an active fault-bounded mountain front, the lateral flanks of individual contiguous alluvial fans expand, overlap, and coalesce laterally to construct a broad, continuous, undulating alluvial apron termed a <strong>bajada</strong> (derived from the Spanish term for "slope" or "descent").</p>
      
      <div class="quote-box bangar">
        "Where several streams emerge from a mountain front at short intervals, the individual alluvial fans spread out laterally and coalesce to form a continuous, undulating plain of gravel and sand along the base of the mountains. Such a compound alluvial fan or piedmont alluvial apron is known as a <strong>bajada</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Sediment Transport & Fluvial Deposits, p. 25)</span>
      </div>

      <p>Morphodynamically, a bajada represents a major depositional sediment sink in arid, semi-arid, and paraglacial tectonic basins (basin-and-range topography). Sediment deposition across the bajada system is governed by three primary hydrodynamic transport mechanisms:</p>
      <ul>
        <li><strong>Debris Flows (Viscous Plastic Flow):</strong> High-density, matrix-rich slurries composed of poorly sorted boulders, cobbles, and mud ($>80\\text{ wt}\\%$ sediment) driven by gravity. Debris flows dominate the proximal fan head, depositing unstratified, matrix-supported diamictons with characteristic inverse grading and steep initial depositional dips ($5^\\circ$ to $15^\\circ$).</li>
        <li><strong>Sheetfloods (Supercritical Unconfined Flow):</strong> Broad, unchannelized sheets of sediment-laden turbulent water flowing down the mid-fan slope following sudden flash flood events. Sheetfloods produce couplets of plane-bedded gravelly sand and cross-stratified sands with moderate sorting.</li>
        <li><strong>Channelized Streamflow (Incised Radial Distributaries):</strong> Anastomosing and braided distributary channels that bifurcate downstream from the fan apex across the mid-to-distal fan, depositing cross-bedded gravels, sands, and horizontally stratified silts.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Alluvial Fan Morphometry & Basin Area Scaling (Bull, 1964; Denny, 1967)</div>
        $$A_f = c \\cdot A_d^h$$
        $$\\text{Slope } S_f = k \\cdot A_d^{-m}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $A_f$ is fan area ($\\text{km}^2$), $A_d$ is contributing drainage basin area ($\\text{km}^2$), $c$ is a lithology-dependent coefficient ($0.1$ to $2.0$), and $h$ is a power-law exponent typically ranging between $0.7$ and $1.1$. Fan slope $S_f$ scales inversely with basin area ($m \\approx 0.15 - 0.35$).</p>
      </div>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q001/bangar_p25_alluvial_fans_bajada.png" alt="K.M. Bangar Alluvial Fan and Bajada Geomorphology">
        <div class="tb-caption">
          <strong>Figure 1.1: Classic Piedmont Fan-Bajada Evolution (K.M. Bangar, p. 25).</strong> Schematic cross-section and planform illustrating how isolated mountain streams discharge debris at a mountain front, forming individual cone-shaped alluvial fans that progressively coalesce along strike into a continuous, compound piedmont bajada.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q001/boggs_fig8_2_alluvial_fan_bajada.png" alt="Sam Boggs Jr Alluvial Fan Depositional Model">
        <div class="tb-caption">
          <strong>Figure 1.2: Alluvial Fan Depositional Systems & Sub-environments (Sam Boggs Jr., Fig. 8.2).</strong> Detailed architectural zonation depicting the Proximal Fan (fanhead trench, debris flows, boulder gravels), Mid-Fan (braided distributary channels, sheetflood sand lobes), and Distal Fan (fine sand and silt grading into terminal playa muds and evaporites).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Piedmont Zonation: Pediment vs. Bajada vs. Playa</div>
    <div class="card-body">
      <p>In structural desert basins (bolsons), the transition from the mountain front to the central basin floor comprises three sharply distinct physiographic zones that are frequently tested in UPSC/OPSC competitive exams:</p>
      <table>
        <thead>
          <tr>
            <th>Zone</th>
            <th>Morphogenetic Nature</th>
            <th>Primary Process</th>
            <th>Sediment Thickness</th>
            <th>Typical Slope</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Pediment</strong></td>
            <td>Erosional bedrock bench</td>
            <td>Scarp retreat, sheetwash, lateral stream planation</td>
            <td>Thin veneer ($<1 - 2\\text{ m}$) or bare bedrock</td>
            <td>$0.5^\\circ - 7^\\circ$</td>
          </tr>
          <tr>
            <td><strong>Bajada</strong></td>
            <td>Depositional alluvial apron</td>
            <td>Coalescence of aggrading alluvial fans</td>
            <td>Thick clastic wedge (tens to hundreds of meters)</td>
            <td>$1^\\circ - 10^\\circ$</td>
          </tr>
          <tr>
            <td><strong>Playa</strong></td>
            <td>Terminal evaporitic basin floor</td>
            <td>Suspension settling of clays, chemical precipitation of salts</td>
            <td>Thick, horizontally laminated muds & evaporites</td>
            <td>$< 0.1^\\circ$ (Near horizontal)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q1_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 1)</div>
    <div class="q-stmt">
      1. &lsquo;Bajada&rsquo; is a type of :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Glacial deposit</div>
      <div class="raw-opt correct">(B) Alluvial fan &nbsp;✔</div>
      <div class="raw-opt">(C) Meandering stream</div>
      <div class="raw-opt">(D) Sand dune</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Alluvial fan</div>
      <div class="sub">
        In physical geology and geomorphology (K.M. Bangar, p. 25; Sam Boggs Jr., p. 235; Arthur L. Bloom, p. 284), a <strong>bajada</strong> is officially classified as a compound, coalescent <strong>alluvial fan</strong> apron formed along the piedmont zone of a mountain front.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Glacial deposit</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Glacial deposits consist of unsorted, unstratified till (forming moraines, drumlins, and till plains) deposited directly by ice, or stratified fluvioglacial drift (eskers, kames, varves, sandurs) deposited by glacial meltwater. A bajada is strictly an alluvial/piedmont landform developed by running water and subaerial mass flows in fluvial and arid/semi-arid desert basin environments, bearing no genetic connection to glacial ice.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Alluvial fan</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> A bajada is genetically defined as a continuous, gently sloping alluvial depositional apron formed by the lateral coalescence and overlapping of multiple individual adjacent <strong>alluvial fans</strong> along a mountain piedmont. Individual apexes correspond to separate stream canyons, but downstream their clastic aprons merge into a single seamless depositional body flanking the mountain range.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Meandering stream</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A meandering stream is a single-thread channel morphology defined by high sinuosity ($S \\ge 1.5$), cohesive banks, low channel slopes, and continuous lateral migration via outer cut-bank erosion and inner point-bar accretion across a low-gradient alluvial floodplain. In contrast, bajada streams are high-gradient, multi-thread, ephemeral, braided, or unconfined sheetfloods.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Sand dune</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A sand dune is an aeolian depositional bedform constructed by wind-driven saltation and accumulation of well-sorted, fine-to-medium quartz sand (forming barchans, seifs, transverse dunes, and star dunes). Bajadas are aqueous and gravity-driven alluvial deposits composed predominantly of poorly sorted, coarse gravels, cobbles, and sands.
    </div>
  </div>
"""

q1_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Alluvial Fan Sub-Environments</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Fan Sub-Environment</th>
            <th>Primary Sedimentary Facies</th>
            <th>Bedforms & Structures</th>
            <th>Dominant Grain Size</th>
            <th>Sorting & Maturity</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Proximal Fan (Fanhead)</strong></td>
            <td>Matrix-supported debris-flow conglomerates ($Gms$), sieve lobes</td>
            <td>Inverse grading, crude horizontal alignment, lack of stratification</td>
            <td>Boulders, cobbles, gravelly mud</td>
            <td>Very poorly sorted; extremely immature</td>
          </tr>
          <tr>
            <td><strong>Mid-Fan (Braided / Sheetflood)</strong></td>
            <td>Clast-supported gravels ($Gm, Gp$), planar/trough cross-bedded sands ($St, Sp$)</td>
            <td>Upstream clast imbrication, trough scours, planar cross-stratification</td>
            <td>Pebbles, granules, coarse-to-medium sand</td>
            <td>Moderately to poorly sorted; subangular</td>
          </tr>
          <tr>
            <td><strong>Distal Fan (Bajada Toe)</strong></td>
            <td>Horizontally stratified sheetflood sands ($Sh$), climbing ripples ($Sr$), silt/mud ($Fl$)</td>
            <td>Parallel laminations, ripple drift, mudcracks, desiccation cracks</td>
            <td>Fine sand, silt, mud</td>
            <td>Moderately sorted; subrounded</td>
          </tr>
          <tr>
            <td><strong>Playa Fringe / Bolson</strong></td>
            <td>Massive muds ($Fm$), nodular gypsum, halite, caliche crusts</td>
            <td>Evaporite crystals, tepee structures, desiccation polygons</td>
            <td>Clay, silt, chemical salts</td>
            <td>Chemically mature; fine suspension settling</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> An alluvial fan has a radius $R = 8.0\\text{ km}$. The elevation at the fan apex is $1450\\text{ m}$ above sea level, while the distal toe of the fan grades into a playa at an elevation of $1050\\text{ m}$. Calculate the average depositional slope of the fan in degrees and in percentage gradient.
          <div class="pq-ans">✔ Worked Answer: Slope angle $\\alpha \\approx 2.86^\\circ$; Gradient $= 5.0\\%$</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Elevation drop $\\Delta h = 1450\\text{ m} - 1050\\text{ m} = 400\\text{ m}$.<br>
            Horizontal distance $L = 8.0\\text{ km} = 8000\\text{ m}$.<br>
            $$\\text{Gradient} = \\frac{\\Delta h}{L} = \\frac{400}{8000} = 0.05 = 5.0\\%$$<br>
            $$\\tan \\alpha = 0.05 \\implies \\alpha = \\arctan(0.05) \\approx 2.862^\\circ$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the fundamental geological difference between a "pediment" and a "bajada"?
          <div class="pq-ans">✔ Correct Answer: A pediment is an erosional bedrock surface; a bajada is a depositional prism of coalesced clastic alluvium.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Both occur in piedmont zones. However, a pediment is carved by scarp retreat and sheet erosion into solid bedrock, possessing only a veneer of transient gravel. In contrast, a bajada is built by the active accumulation of coalescing alluvial fans, forming a thick, basinward-thickening clastic sediment wedge.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What sedimentary texture is diagnostic of "sieve deposits" on coarse-grained alluvial fans?
          <div class="pq-ans">✔ Correct Answer: Well-sorted, open-framework clast-supported gravels completely lacking fine matrix material.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sieve deposits occur on steep proximal fans when highly permeable, matrix-deficient coarse gravels allow muddy water to infiltrate instantaneously downwards into the fan body, leaving behind a clean, interlocking open-work framework of pebbles and cobbles devoid of sand and silt.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Bull's alluvial fan equation $A_f = c A_d^h$, how does drainage basin lithology affect the coefficient $c$?
          <div class="pq-ans">✔ Correct Answer: Basins underlain by easily erodible sedimentary rocks (e.g., shale, mudstone) have much higher $c$ values than basins underlain by resistant crystalline rocks (e.g., quartzite, granite).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Erodible rocks generate vastly larger sediment yields for a given runoff volume, building significantly larger alluvial fans ($A_f$) for the same drainage basin area ($A_d$).
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What geomorphic process leads to "fanhead trenching" where a stream cuts deeply into its own alluvial fan apex?
          <div class="pq-ans">✔ Correct Answer: A change in the ratio of sediment load to water discharge (e.g., post-glacial runoff increase), tectonic uplift of the mountain block, or base-level lowering.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When stream discharge increases relative to sediment load, or when base-level drops, the stream shifts from aggradation to vertical downcutting, entrenching a steep canyon through the fanhead and shifting the active locus of fan deposition further down-fan.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What paleocurrent structure provides the most reliable indicator of flow direction in mid-fan sheetflood gravels?
          <div class="pq-ans">✔ Correct Answer: Upstream clast imbrication ($a(p)b(i)$ or $a(t)b(i)$ fabrics) where flat pebbles dip upstream into the current.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Hydrodynamic drag causes tabular clasts in riverbeds and sheetfloods to rotate and settle with their maximum projection planes inclined upstream, offering the minimum resistance to flow.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In seismic reflection profiles of continental rift basins, how does a bajada complex typically manifest?
          <div class="pq-ans">✔ Correct Answer: As a wedge-shaped clastic prism adjacent to the border fault, exhibiting chaotic to reflection-free proximal seismic facies that transition basinward into high-amplitude continuous parallel reflectors.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The proximal coarse, unstratified debris flows scatter seismic energy, producing chaotic seismic character, while the distal fine-grained lacustrine/playa sheet sands produce coherent, stratified reflections.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why are alluvial fans and bajadas in arid regions of critical importance in hydrogeology?
          <div class="pq-ans">✔ Correct Answer: They serve as primary regional groundwater recharge zones with high porosity and hydraulic conductivity.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The coarse, highly permeable gravels and sands at the apex and mid-fan absorb episodic mountain runoff and flash floods, funneling freshwater deep into artesian aquifers underlying the arid basin floor.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=1,
    filename="Q001_Bajada_Alluvial_Fan_Geomorphology_Complete_Guide.html",
    title="Q001: Bajada Geomorphology, Alluvial Fan Coalescence & Piedmont Dynamics",
    badge="GGM - 2/2019 • Fluvial Geomorphology & Sedimentology",
    h1_title="Q001: Geomorphic Architecture of Bajadas, Piedmont Alluvial Fans & Basin Zonation",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 1<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 25); Sam Boggs Jr. (<em>Sedimentology & Stratigraphy</em>, Ch. 8, pp. 235–242); Arthur L. Bloom (<em>Geomorphology</em>, Ch. 12)",
    part1_html=q1_part1,
    part2_html=q1_part2,
    part3_html=q1_part3
)

# ==========================================
# QUESTION 2: BRAIDED STREAM INTERWOVEN CHANNELS
# ==========================================
q2_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Hydrodynamic Mechanics of Braided River Systems</div>
    <div class="card-body">
      <p>A <strong>braided stream</strong> (or braided river) is a multi-thread fluvial channel system consisting of a network of interwoven, bifurcating, and repeatedly converging channels separated by mobile, dynamic alluvial islands and mid-channel sediment bars (longitudinal, transverse, and compound bars). Braiding represents a primary equilibrium response of a river transporting high volumes of coarse bedload under steep slopes and highly erodible, non-cohesive bank conditions.</p>

      <div class="quote-box bangar">
        "When a river is heavily laden with coarse sediment (gravel, pebbles, coarse sand) and its velocity decreases, it deposits sediment within its own bed as shoals and sandbars. As a consequence, the stream splits into numerous interwoven, bifurcating branches that reunite downstream. Such a stream characterized by an intricate network of interlaced channels is called a <strong>braided stream</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (River Deposition & Channel Forms, p. 25)</span>
      </div>

      <p>In classical quantitative fluvial geomorphology (Leopold and Wolman, 1957; Schumm, 1977), channel pattern is governed by the interaction between <strong>channel slope ($S$)</strong>, <strong>bankfull discharge ($Q$)</strong>, and the <strong>nature of sediment load</strong>:</p>

      <div class="formula-card">
        <div class="formula-title">Leopold-Wolman Channel Pattern Threshold (Leopold & Wolman, 1957)</div>
        $$S_c = 0.0125 \\cdot Q^{-0.44}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $S_c$ is the critical threshold valley slope and $Q$ is bankfull discharge in $\\text{m}^3/\\text{s}$. For any given discharge $Q$:<br>
        • If $S > S_c$: Channel develops a <strong>braided</strong> multi-thread pattern.<br>
        • If $S < S_c$: Channel develops a <strong>meandering</strong> single-thread pattern.</p>
      </div>

      <p>Four fundamental physical conditions promote river braiding:</p>
      <ol>
        <li><strong>High Bedload-to-Suspended-Load Ratio ($Q_b/Q_s > 0.11$):</strong> Streams transporting coarse sands and gravels as bedload cannot maintain uniform transport during falling stages, precipitating mid-channel bar formation.</li>
        <li><strong>Steep Channel Gradient ($S$):</strong> High energy slopes generate intense bed shear stresses ($\\tau_0 = \\gamma R S$) that continuously mobilize coarse bedload.</li>
        <li><strong>Erodible, Non-Cohesive Banks:</strong> Banks composed of silt-poor sands and gravels have low shear strength and lack binding clay or vegetative cover, allowing rapid lateral channel widening (high width-to-depth ratios, $W/D > 40$).</li>
        <li><strong>Flashy, Highly Fluctuating Discharge ($Q_{max} / Q_{min} \\gg 10$):</strong> Rapid hydrograph recession drops stream competence abruptly, stranding bedload bars within the channel.</li>
      </ol>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q002/bangar_p25_braided_stream_channels.png" alt="K.M. Bangar Braided Stream Channels">
        <div class="tb-caption">
          <strong>Figure 2.1: Interwoven Braided Channel Network (K.M. Bangar, p. 25).</strong> Plan view illustrating how river overloading causes mid-channel deposition of longitudinal and transverse gravel bars, forcing the flow to split into multiple interwoven branches.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q002/boggs_fig8_6_braided_stream_bars.png" alt="Sam Boggs Jr Braided River Bar Types">
        <div class="tb-caption">
          <strong>Figure 2.2: Bar Dynamics in Braided Rivers (Sam Boggs Jr., Fig. 8.6).</strong> Morphological evolution of longitudinal bars (coarse gravel nucleus growing downstream) and transverse bars (lobate sand bedforms migrating downstream with steep slip faces).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Diagnostic Bar Types in Braided Fluvial Systems</div>
    <div class="card-body">
      <p>Mid-channel bars in braided rivers undergo continuous accretion, dissection, and migration. Three distinct bar geometries dominate:</p>
      <ul>
        <li><strong>Longitudinal Bars:</strong> Elongate, diamond- or lens-shaped gravel bars oriented parallel to the primary channel axis. Formed by vertical aggradation of the coarsest bedload particles in mid-channel where flow depth decreases. Characterized by upstream clast imbrication and crude horizontal bedding ($Gm$ facies).</li>
        <li><strong>Transverse Bars:</strong> Tabular sand or gravel bars oriented perpendicularly or obliquely to channel flow. They migrate downstream by avalanching down a steep slip-face, producing planar cross-stratification ($Gp$ or $Sp$ facies).</li>
        <li><strong>Compound / Island Bars:</strong> Large, complex semi-permanent macroforms formed by the amalgamation of multiple longitudinal and transverse bars, stabilized periodically by pioneer vegetation.</li>
      </ul>
    </div>
  </div>
"""

q2_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 2)</div>
    <div class="q-stmt">
      2. A stream consisting of interwoven channels is known as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Fluvioglacial stream</div>
      <div class="raw-opt correct">(B) Braided stream &nbsp;✔</div>
      <div class="raw-opt">(C) Meandering stream</div>
      <div class="raw-opt">(D) Matured valley stream</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Braided stream</div>
      <div class="sub">
        In standard university sedimentology and geomorphology (K.M. Bangar, p. 25; Sam Boggs Jr., p. 244; Leopold & Wolman, 1957), a multi-thread stream consisting of an intricate network of <strong>interwoven, interlaced channels</strong> is universally defined as a <strong>Braided stream</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Fluvioglacial stream</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> "Fluvioglacial stream" denotes the <em>origin of meltwater</em> discharged from a melting glacier. While many proglacial outwash streams (sandurs) do exhibit braided geometry due to extreme sediment loading, "fluvioglacial" is a genetic climatic classification, not a channel morphological pattern. Fluvioglacial streams can also flow through straight bedrock gorges, incised canyons, or subglacial tunnels (eskers).
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Braided stream</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard international definition, a river channel pattern characterized by multiple interwoven, bifurcating, and rejoining anabranches separated by ephemeral mid-channel gravel and sand bars is precisely termed a <strong>braided stream</strong> (or braided river).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Meandering stream</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A meandering stream consists of a single, continuous, highly sinuous channel ($S \\ge 1.5$) that curves back and forth across a floodplain without interwoven branches. Channel division in meandering rivers is confined to occasional neck cutoffs forming isolated oxbow lakes.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Matured valley stream</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A "matured valley stream" refers to the Davisian geomorphic cycle stage where a river flows over a broad, graded floodplain with low gradient and established meander belts, natural levees, and oxbows, rather than an active multi-thread interwoven braided network.
    </div>
  </div>
"""

q2_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Fluvial Morphology Comparison: Braided vs. Meandering vs. Anastomosing</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Parameter</th>
            <th>Braided Stream</th>
            <th>Meandering Stream</th>
            <th>Anastomosing Stream</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Channel Planform</strong></td>
            <td>Multi-thread, interwoven, bifurcating</td>
            <td>Single-thread, high sinuosity ($S \\ge 1.5$)</td>
            <td>Multi-thread, discrete interconnected channels</td>
          </tr>
          <tr>
            <td><strong>Channel Bars & Islands</strong></td>
            <td>Transient, unvegetated, mobile gravel/sand bars</td>
            <td>Point bars on inner convex meander bends</td>
            <td>Stable, vegetated, cohesive floodplain islands</td>
          </tr>
          <tr>
            <td><strong>Width-to-Depth Ratio ($W/D$)</strong></td>
            <td>Very high ($W/D > 40 - 100$)</td>
            <td>Moderate to low ($W/D < 10 - 20$)</td>
            <td>Low ($W/D < 10$)</td>
          </tr>
          <tr>
            <td><strong>Sediment Load Type</strong></td>
            <td>Coarse bedload (gravel, sand, pebbles)</td>
            <td>Mixed load to suspended load (silt, fine sand)</td>
            <td>Suspended load (silt, clay, organic muds)</td>
          </tr>
          <tr>
            <td><strong>Bank Stability & Cohesion</strong></td>
            <td>Non-cohesive, highly erodible sand/gravel</td>
            <td>Moderately cohesive silt-clay with vegetation</td>
            <td>Very high cohesion; thick organic/clay banks</td>
          </tr>
          <tr>
            <td><strong>Typical Slope Gradient</strong></td>
            <td>Steep ($S > 0.001 - 0.01$)</td>
            <td>Low ($S < 0.0005$)</td>
            <td>Very low ($S < 0.0001$)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A river has a bankfull discharge $Q = 800\\text{ m}^3/\\text{s}$. Using the Leopold-Wolman empirical threshold $S_c = 0.0125 Q^{-0.44}$, determine the threshold slope separating meandering from braided channels. If the actual river channel slope is $S = 0.0015$, determine its planform pattern.
          <div class="pq-ans">✔ Worked Answer: Threshold slope $S_c \\approx 0.00066$ ($0.066\\%$); Actual river is Braided ($S > S_c$).</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            $$S_c = 0.0125 \\times (800)^{-0.44}$$
            $$\\ln(800) = 6.6846 \\implies -0.44 \\times 6.6846 = -2.9412$$
            $$800^{-0.44} = e^{-2.9412} \\approx 0.0528$$
            $$S_c = 0.0125 \\times 0.0528 \\approx 0.000660 \\text{ (or } 0.066\\%\\text{)}$$
            Since the actual river slope $S = 0.0015$ exceeds $S_c = 0.00066$, the stream possesses excess stream power, promoting mid-channel bar formation and a <strong>Braided</strong> channel network.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the critical distinction between a "braided river" and an "anastomosing river"?
          <div class="pq-ans">✔ Correct Answer: Stability and composition of the islands (transient, non-cohesive bars in braided vs. stable, cohesive, vegetated floodplain blocks in anastomosing).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Both are multi-channel systems. However, braided rivers consist of wide, shallow channels separated by shifting gravel/sand bars with non-cohesive banks. Anastomosing rivers consist of deep, narrow, stable channels separated by permanent, vegetated floodplain islands with cohesive silt-clay banks.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What sedimentary lithofacies (Miall, 1978) characterizes the longitudinal gravel bars of a braided river?
          <div class="pq-ans">✔ Correct Answer: Lithofacies $Gm$ (Massive or crudely bedded gravel with upstream imbrication).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In Miall's architectural element classification, $Gm$ represents horizontally bedded or massive clast-supported gravel sheets deposited by high-energy longitudinal bar accretion during peak flood discharges.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Name two prime examples of mega-braided river systems in the Indian subcontinent.
          <div class="pq-ans">✔ Correct Answer: The Brahmaputra (Jamuna) River in Assam/Bangladesh and the Kosi River in Bihar.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The Brahmaputra carries vast coarse sediment loads from the rapidly uplifting Himalayas under heavy monsoon rains, resulting in a classic braided river system exceeding $10 - 15\\text{ km}$ in braidplain width.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How does vegetation encroachment affect a braided channel pattern during prolonged drought?
          <div class="pq-ans">✔ Correct Answer: Plant roots bind bar sediments and increase bank cohesion, consolidating bars and transitioning the river toward a single-thread or wandering pattern.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Root networks dramatically enhance the critical shear stress required for bank erosion, preventing multi-channel bifurcation and confining flow into fewer, deeper channels.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> Why are thick overbank mud and shale units virtually absent in braided river sedimentary rock sequences?
          <div class="pq-ans">✔ Correct Answer: Continual lateral avulsion and channel shifting sweeps across the entire braidplain, reworking and eroding fine overbank deposits.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The absence of stable, cohesive levees allows channels to sweep back and forth across the entire valley floor, resulting in amalgamated, multistory sandstone/conglomerate bodies with very low preservation of mudrocks ($<5-10\\%$).
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In sequence stratigraphy, in which systems tract are braided fluvial sandstones most commonly deposited?
          <div class="pq-ans">✔ Correct Answer: Lowstand Systems Tract (LST) or early Transgressive Systems Tract (TST).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> During relative sea-level falls and early lowstand periods, fluvial valley incision steepens gradients and flushes coarse bedload into incised valleys, forming extensive multi-story braided valley fills.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a "chute cutoff", and does it occur in braided or meandering rivers?
          <div class="pq-ans">✔ Correct Answer: It occurs during high flood stages across point bars in high-energy meandering/wandering rivers, often acting as a transitional mechanism toward braiding.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When a flood bypasses a meander loop by cutting a new channel directly across the swale of a point bar, it creates a chute cutoff. If chute cutoffs become persistent, the channel network degenerates into a braided stream.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=2,
    filename="Q002_Braided_Stream_Interwoven_Channels_Complete_Guide.html",
    title="Q002: Braided Stream Morphology, Leopold-Wolman Criterion & Bar Dynamics",
    badge="GGM - 2/2019 • Fluvial Geomorphology & Sedimentology",
    h1_title="Q002: Hydrodynamics of Braided Rivers, Interwoven Channels & Bar Architecture",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 2<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 25); Sam Boggs Jr. (<em>Sedimentology & Stratigraphy</em>, Ch. 8, pp. 244–248); Leopold & Wolman (1957, USGS Prof. Paper 282-B)",
    part1_html=q2_part1,
    part2_html=q2_part2,
    part3_html=q2_part3
)

# ==========================================
# QUESTION 3: CANYON - DEEP VALLEY WITH VERTICAL SIDES
# ==========================================
q3_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Morphological Architecture of Gorges & Canyons</div>
    <div class="card-body">
      <p>In fluvial geomorphology, a <strong>canyon</strong> (or <strong>gorge</strong>) is an exceptionally deep, narrow, steep-sided bedrock valley with nearly vertical rock walls, carved by vigorous stream incision through resistant, horizontally bedded or massive crystalline rock formations. Canyons represent juvenile (youthful) fluvial landforms where the rate of vertical river downcutting massively exceeds the rate of lateral valley widening and valley-wall mass wasting.</p>

      <div class="quote-box bangar">
        "When vertical erosion (downcutting) by a youthful river proceeds at a much faster rate than the weathering and mass wasting of its valley walls, an exceptionally deep and narrow valley with steep, near-vertical sides is produced. A very deep, narrow valley with vertical rocky walls is called a <strong>gorge</strong> or a <strong>canyon</strong> (e.g., the Grand Canyon of the Colorado River)."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Fluvial Landforms: Valleys & Gorges, p. 24)</span>
      </div>

      <p>The formation of deep, vertical-walled canyons requires a specific convergence of geodynamic, climatic, and lithologic conditions:</p>
      <ul>
        <li><strong>Rapid Fluvial Incision vs. Slow Slope Degradation:</strong> Fluvial incision operates through hydraulic plucking, cavitation, and bedload abrasion (stream power $\\Omega = \\gamma Q S$). For vertical walls to persist, the valley walls must be immune to rapid slope failure, slumping, and rain-wash erosion.</li>
        <li><strong>Arid to Semi-Arid Climatic Regime:</strong> In humid climates, abundant rainfall, chemical weathering, and soil creep continuously soften and recline valley slopes into gentle V-shaped profiles. In arid climates, surface runoff on valley slopes is minimal, preserving sheer vertical cliffs.</li>
        <li><strong>Resistant, Flat-Lying Strata or Massive Rock:</strong> Massive crystalline rocks (granite, basalt) or alternating horizontal beds of hard caprock (sandstone, limestone, dolomite) overlying softer shales produce stepped, vertical canyon profiles.</li>
        <li><strong>Regional Tectonic Uplift (Base-Level Lowering):</strong> Sustained, epeirogenic or tectonic plateau uplift maintains high channel slope ($S$) and driving stream power over millions of years.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Stream Power Incision Law (Howard & Kerby, 1983; Whipple & Tucker, 1999)</div>
        $$E = K \\cdot A^m \\cdot S^n$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $E$ is vertical bedrock incision rate ($\\text{m/yr}$), $K$ is bedrock erodibility coefficient, $A$ is upstream drainage area (proxy for discharge $Q$), $S$ is channel slope, and $m, n$ are exponents ($m/n \\approx 0.4 - 0.6$). Canyon incision occurs when $E > W_s$ (where $W_s$ is valley-wall degradation rate).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q003/bangar_p24_river_valleys_canyons_gorges.png" alt="K.M. Bangar River Valleys Canyons Gorges">
        <div class="tb-caption">
          <strong>Figure 3.1: Morphological Evolution of River Valleys (K.M. Bangar, p. 24).</strong> Cross-sections illustrating (A) Youthful narrow V-shaped valley, (B) Gorge and vertical-walled Canyon formed where downcutting outpaces slope retreat, and (C) Mature broad-bottomed valley with floodplain.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Geomorphic Distinction: Gorge vs. Canyon vs. Asymmetrical Valley</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Valley Type</th>
            <th>Wall Geometry</th>
            <th>Primary Controls</th>
            <th>Classic Type Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Gorge (Sensu Stricto)</strong></td>
            <td>Nearly vertical walls; uniform narrow width from crest to base</td>
            <td>Extremely resistant massive rock (granite, quartzite); intense downcutting</td>
            <td>Indus Gorge (Nanga Parbat), George of Kali Gandaki (Himalayas)</td>
          </tr>
          <tr>
            <td><strong>Canyon (Sensu Stricto)</strong></td>
            <td>Steep stepped-cliff walls ("staircase" topography); broad regional scale</td>
            <td>Alternating resistant (cliffs) and weak (slopes) horizontal strata in arid plateaus</td>
            <td>Grand Canyon (Colorado Plateau, USA), Fish River Canyon (Namibia)</td>
          </tr>
          <tr>
            <td><strong>Asymmetrical Valley</strong></td>
            <td>Unequal slope inclinations on opposing sides</td>
            <td>Unilateral dip of rock strata (homoclinal shift) or microclimatic insolation differences</td>
            <td>Cuesta valleys, strike valleys in folded fold belts</td>
          </tr>
          <tr>
            <td><strong>V-Shaped Valley</strong></td>
            <td>Symmetrical sloping walls ($30^\\circ - 45^\\circ$)</td>
            <td>Equilibrium between vertical river downcutting and lateral mass wasting in humid climates</td>
            <td>Youthful headwater streams in temperate mountain belts</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q3_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 3)</div>
    <div class="q-stmt">
      3. A canyon is a :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) A deep valley with vertical sides &nbsp;✔</div>
      <div class="raw-opt">(B) A deep asymmetrical valley</div>
      <div class="raw-opt">(C) Broad, matured stream course</div>
      <div class="raw-opt">(D) Valley formed by aeolian activity</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) A deep valley with vertical sides</div>
      <div class="sub">
        In physical geology and geomorphology (K.M. Bangar, p. 24; Arthur Holmes, p. 524; W.D. Thornbury, p. 115), a <strong>canyon</strong> is defined precisely as an exceptionally <strong>deep valley with vertical (or near-vertical) rocky sides</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) A deep valley with vertical sides</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> A canyon is universally defined as a steep-walled, exceptionally deep and narrow bedrock chasm with near-vertical cliffs. It forms where vigorous fluvial downcutting is highly concentrated while valley-side mass wasting is retarded by arid climate and resistant rock strata.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) A deep asymmetrical valley</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> An asymmetrical valley is a valley where one side is significantly steeper than the other, typically caused by uniclinal shifting of a river down the dip-slope of inclined sedimentary beds (homoclinal valleys flanking cuestas) or by asymmetric solar insolation. Canyons are symmetrical or stepped-cliff chasms, not fundamentally asymmetrical valleys.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Broad, matured stream course</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A broad, mature stream course is characterized by wide floodplains, low relief, meander loops, and gentle valley walls. A canyon is the exact antithesis: an incised, high-relief, youthful or rejuvenated erosional feature without a mature floodplain.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Valley formed by aeolian activity</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Aeolian processes (wind action) produce landforms such as sand dunes, yardangs, zeugens, and deflation hollows. Wind completely lacks the density and hydraulic energy to carve deep, vertical bedrock valleys into mountain plateaus; canyons are exclusively carved by running water.
    </div>
  </div>
"""

q3_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Global Canyon Architectures & Geological Origins</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Canyon / Gorge</th>
            <th>Geographic Region</th>
            <th>River System</th>
            <th>Depth / Relief</th>
            <th>Primary Geodynamic & Lithologic Driver</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Grand Canyon</strong></td>
            <td>Arizona, USA</td>
            <td>Colorado River</td>
            <td>$\\approx 1800\\text{ m}$</td>
            <td>Epeirogenic uplift of Colorado Plateau; alternating Paleozoic carbonates/shales</td>
          </tr>
          <tr>
            <td><strong>Yarlung Tsangpo Grand Canyon</strong></td>
            <td>Tibet, China</td>
            <td>Yarlung Tsangpo (Brahmaputra)</td>
            <td>$> 5000\\text{ m}$</td>
            <td>Active Himalayan tectonic syntaxis uplift; massive monsoonal stream power</td>
          </tr>
          <tr>
            <td><strong>Kali Gandaki Gorge</strong></td>
            <td>Nepal Himalaya</td>
            <td>Kali Gandaki River</td>
            <td>$\\approx 5500\\text{ m}$</td>
            <td>Antecedent river cutting down between Annapurna and Dhaulagiri peaks</td>
          </tr>
          <tr>
            <td><strong>Bledowska / Fish River Canyon</strong></td>
            <td>Namibia</td>
            <td>Fish River</td>
            <td>$\\approx 550\\text{ m}$</td>
            <td>Post-Gondwana continental plateau uplift and horizontal quartzite incision</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> The Colorado River has incised a total depth of $1800\\text{ m}$ through the Colorado Plateau over the last $6.0\\text{ million years}$ (Ma). Calculate the average long-term bedrock incision rate in millimeters per year ($\\text{mm/yr}$) and in meters per million years ($\\text{m/Ma}$).
          <div class="pq-ans">✔ Worked Answer: Incision rate $= 0.30\\text{ mm/yr} = 300\\text{ m/Ma}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Total incision depth $D = 1800\\text{ m} = 1,800,000\\text{ mm}$.<br>
            Total time elapsed $T = 6,000,000\\text{ yr} = 6.0\\text{ Ma}$.<br>
            $$\\text{Incision Rate} = \\frac{D}{T} = \\frac{1,800,000\\text{ mm}}{6,000,000\\text{ yr}} = 0.30\\text{ mm/yr}$$
            $$\\text{Rate in m/Ma} = \\frac{1800\\text{ m}}{6.0\\text{ Ma}} = 300\\text{ m/Ma}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What geological term describes a river that maintained its course across an uplifting mountain range by incising a deep gorge at a rate equal to the rate of tectonic uplift?
          <div class="pq-ans">✔ Correct Answer: An Antecedent stream (Antecedence).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> An antecedent river predates the tectonic uplift of the topography across which it flows. If the river's vertical incision rate equals or exceeds the rate of structural uplift ($E \\ge U$), it maintains its original course, cutting a transverse gorge through the rising mountain barrier (e.g., the Indus and Brahmaputra rivers cutting across the Himalayas).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What causes the distinctive "staircase" (cliff-and-bench) topography in the Grand Canyon?
          <div class="pq-ans">✔ Correct Answer: Differential weathering and erosion of alternating resistant cliff-forming strata and weak slope-forming strata.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Competent, massive units (e.g., Coconino Sandstone, Redwall Limestone) resist weathering and stand as sheer vertical cliffs. Incompetent, soft units (e.g., Bright Angel Shale, Hermit Shale) weather rapidly and retreat into gentle structural benches and debris slopes.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is a "slot canyon", and how does it form?
          <div class="pq-ans">✔ Correct Answer: An exceptionally narrow, deep bedrock gorge (often $<1-3\\text{ m}$ wide and tens of meters deep) carved by violent, abrasive flash floods into homogeneous sandstone.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Classic examples like Antelope Canyon (Arizona) form along vertical joint fractures in massive eolian sandstones (Navajo Sandstone), where flash floods carrying suspended quartz sand gouge fluted, swirling vertical walls.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How do "submarine canyons" differ fundamentally from subaerial river canyons?
          <div class="pq-ans">✔ Correct Answer: Submarine canyons are carved on continental slopes by submarine turbidity currents and underwater mass wasting, not subaerial rivers.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Turbidity currents—gravity-driven, sediment-laden hyperpycnal density flows—erode deep V-shaped and U-shaped chasms across continental margins, feeding deep-sea submarine fans.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What hydraulic mechanism allows a bedrock river to incise vertically into hard crystalline bedrock?
          <div class="pq-ans">✔ Correct Answer: A combination of hydraulic plucking (quarrying of joint-bounded blocks), cavitation, and abrasion by sediment bedload tools.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Pure water cannot erode hard granite; abrasive bedload particles (gravel and sand tools) dragged and bounced along the bed scour rock surfaces, while turbulent flow plucks jointed bedrock blocks.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In geotechnical engineering, what primary geological hazard is encountered when siting a mega-dam in a deep, narrow canyon?
          <div class="pq-ans">✔ Correct Answer: Valley-stress relief joints (sheeting joints) parallel to the vertical canyon walls and high in-situ horizontal stress concentrations at the valley floor.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Rapid valley excavation removes lateral confining pressure, causing rock to rebound and fracture along stress-relief joints parallel to the cliffs, creating severe rock-fall and abutment sliding risks.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why did the classic Davisian cycle of erosion consider canyons to represent the "youthful" stage of river development?
          <div class="pq-ans">✔ Correct Answer: Because vertical downcutting is the dominant process, lateral valley widening has barely begun, and the valley floor lacks an alluvial floodplain.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> William Morris Davis defined "youth" by vigorous vertical incision, steep channel gradients, waterfalls, rapids, and steep V-shaped or vertical canyon walls.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=3,
    filename="Q003_Canyon_Gorge_Vertical_Valley_Complete_Guide.html",
    title="Q003: Canyon Morphology, Stream Downcutting & Bedrock Incision Dynamics",
    badge="GGM - 2/2019 • Fluvial Geomorphology & Tectonics",
    h1_title="Q003: Geomorphology of Canyons, Gorges & Vertical Fluvial Incision Mechanics",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 3<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 24); Arthur Holmes (<em>Principles of Physical Geology</em>, pp. 524–528); W.D. Thornbury (<em>Principles of Geomorphology</em>, Ch. 5)",
    part1_html=q3_part1,
    part2_html=q3_part2,
    part3_html=q3_part3
)

# ==========================================
# QUESTION 4: TRELLIS DRAINAGE PATTERN
# ==========================================
q4_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Structural Control on Drainage Networks: The Trellis Pattern</div>
    <div class="card-body">
      <p>A <strong>trellis drainage pattern</strong> is a geometric drainage network characterized by a system of primary subparallel master streams flowing along the strike of alternating bands of resistant and non-resistant folded or tilted rock strata, joined at approximately <strong>right angles ($90^\\circ$)</strong> by short tributary streams flowing down the dip and anti-dip slopes. The resulting network strongly resembles a garden trellis used to support climbing vines.</p>

      <div class="quote-box bangar">
        "In areas where the rocks have been folded into parallel anticlines and synclines, or where homoclinal beds with alternating hard and soft layers crop out, a network of parallel or subparallel streams develops along the strike and dip directions. The master streams flow in strike valleys along the soft rocks, while short tributaries flow down the dip slopes at right angles to join them. This pattern is called a <strong>trellis drainage pattern</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Drainage Patterns & Structural Geology, p. 27)</span>
      </div>

      <p>The development of a trellis drainage network is strictly governed by the differential erosion of structurally deformed bedrock:</p>
      <ul>
        <li><strong>Structural Alignment:</strong> Characteristic of folded mountain belts with parallel plunging anticlines and synclines (e.g., the Appalachian Valley and Ridge Province; Zagros Fold Belt) and homoclinal ridges (cuestas and hogbacks).</li>
        <li><strong>Subsequent Master Streams:</strong> The long, primary parallel rivers develop as <em>subsequent streams</em> that excavate strike-valleys along weak, easily erodible strata (such as shales, marls, and weathered limestones).</li>
        <li><strong>Consequent & Obsequent Tributaries:</strong> Short secondary streams flow perpendicularly down the structural dip slopes (consequent streams) or down the steep scarp faces opposite to dip (obsequent streams), joining the strike streams at nearly $90^\\circ$ angles.</li>
        <li><strong>Water Gaps & Wind Gaps:</strong> Where transverse superposed or antecedent master rivers breach resistant quartzite or sandstone ridges, narrow transverse gorges termed <em>water gaps</em> are created. If an incising strike stream captures the upper course of a transverse river via stream piracy, the abandoned transverse gap becomes a dry <em>wind gap</em>.</li>
      </ul>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q004/bangar_p27_trellis_drainage_pattern.png" alt="K.M. Bangar Drainage Patterns Trellis Dendritic">
        <div class="tb-caption">
          <strong>Figure 4.1: Canonical Drainage Patterns (K.M. Bangar, p. 27).</strong> Comparative diagrams showing (A) Dendritic (isotropic flat-lying rocks), (B) Trellis (folded alternating strata with right-angle tributary junctions), (C) Radial (dome or volcanic cone), (D) Rectangular (joint-controlled orthogonal network), and (E) Annular (eroded dome).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Genetic Classification of Streams in a Trellis Network</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Stream Type</th>
            <th>Structural Alignment</th>
            <th>Flow Direction Relative to Bedding</th>
            <th>Role in Trellis Network</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Consequent Stream</strong></td>
            <td>Dip direction</td>
            <td>Flows down the initial regional slope / structural dip</td>
            <td>Primary tributaries draining dip-slope surfaces</td>
          </tr>
          <tr>
            <td><strong>Subsequent Stream</strong></td>
            <td>Strike direction</td>
            <td>Carved along belts of weak, easily erodible rock</td>
            <td>Master trunk streams occupying parallel strike valleys</td>
          </tr>
          <tr>
            <td><strong>Obsequent Stream</strong></td>
            <td>Anti-dip direction</td>
            <td>Flows in direction opposite to the regional structural dip</td>
            <td>Short tributaries flowing down steep cuesta/hogback scarps</td>
          </tr>
          <tr>
            <td><strong>Resequent Stream</strong></td>
            <td>Dip direction</td>
            <td>Flows down structural dip, but at a later geomorphic stage</td>
            <td>Secondary tributaries reoccupying dip slopes after denudation</td>
          </tr>
          <tr>
            <td><strong>Insequent Stream</strong></td>
            <td>Random / Uncontrolled</td>
            <td>Flows without apparent structural or lithologic control</td>
            <td>Rare in trellis systems; common in dendritic networks</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q4_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 4)</div>
    <div class="q-stmt">
      4. A network of parallel or subparallel streams developed along strike and dip directions are known as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Dendritic</div>
      <div class="raw-opt">(B) Radial</div>
      <div class="raw-opt correct">(C) Trellis &nbsp;✔</div>
      <div class="raw-opt">(D) Domal</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Trellis</div>
      <div class="sub">
        In structural geomorphology and photogeology (K.M. Bangar, p. 27; Arthur L. Bloom, p. 272; W.D. Thornbury, p. 122), a stream network where parallel streams follow <strong>strike and dip directions</strong> joining at right angles is universally termed a <strong>Trellis pattern</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Dendritic</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A dendritic drainage pattern resembles the branching form of an oak or maple tree, where tributaries join at acute angles ($<90^\\circ$). Dendritic drainage develops on horizontally bedded, homogeneous sedimentary rocks or isotropic massive igneous rocks (granite) where there is <em>no structural control</em> and rock resistance is uniform in all directions.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Radial</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A radial drainage pattern develops when streams flow outward in all directions like spokes from a central topographic high, such as an isolated volcanic cone, volcanic crater rim, or elevated structural dome.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Trellis</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> The trellis drainage pattern is explicitly defined by subparallel master streams flowing along strike valleys in weak strata, connected to parallel tributaries draining down structural dip slopes and scarp slopes, meeting at nearly $90^\\circ$ right angles.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Domal</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> "Domal" is not an internationally recognized canonical drainage pattern name. Streams draining structural domes exhibit either <em>radial</em> drainage (diverging outward from the center) or <em>annular</em> drainage (ring-like concentric circular channels following weak strata around an eroded structural dome).
    </div>
  </div>
"""

q4_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Classification Matrix: Canonical Drainage Patterns</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Pattern</th>
            <th>Geometric Morphology</th>
            <th>Underlying Structural & Lithologic Control</th>
            <th>Tributary Junction Angle</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dendritic</strong></td>
            <td>Irregular branching like tree limbs</td>
            <td>Uniformly resistant, flat-lying sedimentary rocks or massive crystalline rocks (granite)</td>
            <td>Acute ($< 90^\\circ$, typically $30^\\circ - 60^\\circ$)</td>
          </tr>
          <tr>
            <td><strong>Trellis</strong></td>
            <td>Subparallel master streams with orthogonal tributaries</td>
            <td>Folded alternating hard/soft strata (anticlines/synclines), parallel cuestas and hogbacks</td>
            <td>Right angles ($\\approx 90^\\circ$)</td>
          </tr>
          <tr>
            <td><strong>Rectangular</strong></td>
            <td>Sharp $90^\\circ$ bends with rectangular grid plan</td>
            <td>Intersecting orthogonal joint sets, fault systems, or regional fracture systems</td>
            <td>Right angles ($90^\\circ$)</td>
          </tr>
          <tr>
            <td><strong>Radial</strong></td>
            <td>Radiating outward from a central summit</td>
            <td>Isolated volcanic cones, volcanic plugs, structural domes, conical hills</td>
            <td>Divergent radial paths</td>
          </tr>
          <tr>
            <td><strong>Annular</strong></td>
            <td>Concentric circular or ring-like pathways</td>
            <td>Deeply eroded structural domes, salt diapirs, or ring dykes with alternating soft/hard concentric beds</td>
            <td>Curvilinear right angles</td>
          </tr>
          <tr>
            <td><strong>Centripetal</strong></td>
            <td>Converging inward toward a central low</td>
            <td>Inland drainage basins, desert playas, bolson depressions, sinkholes, calderas</td>
            <td>Convergent paths</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> How does a geologist distinguish in the field or on satellite imagery between a "Trellis" pattern and a "Rectangular" pattern?
          <div class="pq-ans">✔ Correct Answer: Trellis patterns display alternating bands of differing rock types (lithologic control), whereas rectangular patterns develop across uniform lithologies cut by orthogonal joint sets.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Both patterns feature $90^\\circ$ tributary junctions. However, trellis drainage is characterized by long, parallel strike ridges (hogbacks/cuestas) separated by strike valleys in folded strata. In rectangular drainage, the streams abruptly bend at right angles following joint and fault planes without lithologically controlled topographic ridges.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a "water gap", and what is a "wind gap"?
          <div class="pq-ans">✔ Correct Answer: A water gap is a transverse notch through a resistant ridge containing an active stream; a wind gap is an abandoned, dry notch left behind after river piracy.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Water gaps are formed when superposed or antecedent streams cut perpendicularly across resistant strike ridges. If a subsequent strike stream captures the river upstream of the gap, flow through the ridge ceases, leaving a dry structural saddle termed a wind gap.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> In what type of drainage network does "river piracy" (stream capture) occur with the highest frequency?
          <div class="pq-ans">✔ Correct Answer: Trellis drainage networks in folded strata.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Subsequent streams eroding rapidly along soft, non-resistant shale strike-valleys have lower base levels than transverse consequent streams crossing resistant quartzite ridges, allowing subsequent streams to easily breach interfluves and capture transverse streams.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What does an "annular" drainage pattern diagnose in tectonic geomorphology?
          <div class="pq-ans">✔ Correct Answer: A breached, deeply dissected structural dome or igneous pluton with concentric rings of alternating hard and soft sedimentary rock strata.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> As an uplifted dome is eroded, streams etch circular subsequent valleys into weak concentric strata, forming ring-like channels (annular drainage) around the central crystalline core.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What stream pattern is produced when streams flow in opposite directions away from a linear mountain divide?
          <div class="pq-ans">✔ Correct Answer: Parallel or subparallel drainage.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> On steep, elongated structural dip-slopes or regional fault scarps, streams flow down the slope in uniformly parallel paths without substantial branching.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "barbed" (or hooked) drainage pattern, and what tectonic phenomenon does it reveal?
          <div class="pq-ans">✔ Correct Answer: Tributaries joining a master stream at acute upstream angles; diagnoses stream reversal caused by tectonic tilting or glacial damming.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Under normal conditions, tributaries join flowing downstream. A barbed pattern indicates that tectonic uplift or fault tilting reversed the flow direction of the master river while its tributaries maintained their original courses.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In morphometric analysis, how does the Bifurcation Ratio ($R_b$) of a trellis drainage basin compare to a dendritic basin?
          <div class="pq-ans">✔ Correct Answer: Trellis basins often exhibit anomalously high bifurcation ratios ($R_b > 5 - 10$) between specific stream orders due to structural elongation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> While dendritic networks in homogeneous rocks have stable bifurcation ratios between $3$ and $5$, strongly elongated trellis networks with parallel tributaries show high $R_b$ values.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why are trellis drainage basins particularly prone to delayed, attenuated hydrograph flood peaks compared to circular dendritic basins?
          <div class="pq-ans">✔ Correct Answer: Because tributary runoff travels along elongated, narrow strike valleys and arrives at the master stream at staggered intervals.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In circular dendritic basins, tributaries are equidistant from the basin mouth, causing simultaneous runoff concentration and sharp flood peaks. In elongated trellis basins, the elongation stretches time-to-peak.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=4,
    filename="Q004_Trellis_Drainage_Pattern_Folded_Strata_Complete_Guide.html",
    title="Q004: Trellis Drainage Networks, Strike-Dip Controls & Structural Geomorphology",
    badge="GGM - 2/2019 • Structural Geology & Geomorphology",
    h1_title="Q004: Structural Control of Drainage Networks: Trellis vs. Dendritic Patterns",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 4<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 27); Arthur L. Bloom (<em>Geomorphology</em>, Ch. 11, pp. 272–276); W.D. Thornbury (<em>Principles of Geomorphology</em>, Ch. 5)",
    part1_html=q4_part1,
    part2_html=q4_part2,
    part3_html=q4_part3
)

# ==========================================
# QUESTION 5: EUSTATIC SEA LEVEL FLUCTUATIONS
# ==========================================
q5_part1 = """
  <div class="card">
    <div class="card-header bg-blue">The Physical Concept of Eustasy & Global Sea-Level Dynamics</div>
    <div class="card-body">
      <p>The term <strong>eustasy</strong> (or <strong>eustatic sea-level change</strong>) was introduced into geological science by the eminent Austrian geologist <strong>Eduard Suess</strong> in 1888 in his monumental treatise <em>Das Antlitz der Erde</em> (The Face of the Earth). Eustasy denotes <strong>simultaneous, worldwide changes in sea level</strong> that affect all global oceans uniformly, measured relative to a fixed datum such as the center of the Earth.</p>

      <div class="quote-box bangar">
        "Changes in sea level that take place globally and simultaneously throughout the world oceans are called <strong>eustatic changes</strong>. They are caused either by changes in the total volume of water in the ocean basins (such as during the growth and melting of continental ice sheets) or by changes in the capacity of the ocean basins themselves due to plate tectonic movements."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Marine Geology & Eustatic Movements, p. 33)</span>
      </div>

      <p>Eustatic fluctuations occur across vastly different temporal scales and are driven by four distinct geodynamic mechanisms:</p>
      <ul>
        <li><strong>Glacio-Eustasy (Ice Volume Fluctuations):</strong> Changes in the mass and volume of liquid ocean water caused by the freezing and melting of continental ice sheets (Antarctica, Greenland, Laurentide). Operates on orbital Milankovitch timescales ($10^4 - 10^5\\text{ years}$) with rapid rates ($1 - 10\\text{ mm/yr}$). During the Last Glacial Maximum (LGM, $\\approx 21,000\\text{ years ago}$), glacio-eustasy dropped global sea level by $\\approx 120 - 130\\text{ meters}$.</li>
        <li><strong>Tectono-Eustasy (Ocean Basin Volume Changes):</strong> Changes in the volumetric capacity of ocean basins driven by seafloor spreading rates, mid-ocean ridge inflation, and continental collision. When seafloor spreading is rapid, young oceanic lithosphere is hot, buoyant, and thermally expanded, displacing seawater onto continental interiors (marine transgression, e.g., the Cretaceous highstand $+200 - 300\\text{ m}$). Operates on first- and second-order timescales ($10^7 - 10^8\\text{ years}$).</li>
        <li><strong>Sedimentation Eustasy:</strong> Slow displacement of seawater by the cumulative deposition of clastic and carbonate sediments into ocean basins ($<0.01\\text{ mm/yr}$).</li>
        <li><strong>Thermo-Steric Eustasy (Thermal Expansion):</strong> Changes in seawater volume driven by temperature and salinity variations without mass addition (modern global warming expansion $\\approx 1 - 2\\text{ mm/yr}$).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Relative Sea Level (RSL) vs. Eustatic Sea Level (ESL) Equation</div>
        $$\\Delta \\text{RSL} = \\Delta \\text{ESL} - \\Delta z_{\\text{tectonic}} - \\Delta z_{\\text{isostatic}} + \\Delta z_{\\text{geoid}}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $\\Delta \\text{RSL}$ is local relative sea level observed at a coastline, $\\Delta \\text{ESL}$ is global eustatic sea level, $\\Delta z_{\\text{tectonic}}$ is local tectonic crustal uplift/subsidence, $\\Delta z_{\\text{isostatic}}$ is glacio-isostatic adjustment (GIA), and $\\Delta z_{\\text{geoid}}$ is gravitational geoid deformation.</p>
      </div>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q005/bangar_p33_marine_transgression_eustasy.png" alt="K.M. Bangar Marine Transgression and Eustatic Base Level Changes">
        <div class="tb-caption">
          <strong>Figure 5.1: Marine Transgression, Regression & Eustasy (K.M. Bangar, p. 33).</strong> Stratigraphic architecture of onlapping marine transgressive sequences and offlapping regressive sequences produced by eustatic sea-level fluctuations.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q005/boggs_fig12_8_eustatic_sea_level_curve.png" alt="Sam Boggs Jr Global Phanerozoic Eustatic Sea Level Curve">
        <div class="tb-caption">
          <strong>Figure 5.2: Global Eustatic Cycles Across Geological Time (Sam Boggs Jr., Fig. 12.8).</strong> The Exxon/Vail-Haq global eustatic curve displaying first-, second-, and third-order sea-level fluctuations throughout the Phanerozoic Eon.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Phanerozoic Eustatic Cycle Hierarchy (Vail et al., 1977)</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Order</th>
            <th>Duration ($T$)</th>
            <th>Amplitude</th>
            <th>Primary Geodynamic Driving Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1st Order (Megacycles)</strong></td>
            <td>$200 - 400\\text{ Ma}$</td>
            <td>$> 100 - 300\\text{ m}$</td>
            <td>Supercontinent assembly and breakup (Wilson Cycles, mantle convection)</td>
          </tr>
          <tr>
            <td><strong>2nd Order (Supercycles)</strong></td>
            <td>$10 - 100\\text{ Ma}$</td>
            <td>$50 - 150\\text{ m}$</td>
            <td>Changes in global seafloor spreading rates and ridge system volume</td>
          </tr>
          <tr>
            <td><strong>3rd Order (Mesocycles)</strong></td>
            <td>$1 - 10\\text{ Ma}$</td>
            <td>$20 - 100\\text{ m}$</td>
            <td>Major continental ice sheet oscillations and intraplate stress reconfigurations</td>
          </tr>
          <tr>
            <td><strong>4th / 5th Order (Milankovitch)</strong></td>
            <td>$20 - 400\\text{ ka}$</td>
            <td>$10 - 150\\text{ m}$</td>
            <td>Orbital forcing (Eccentricity, Obliquity, Precession) driving glacio-eustasy</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q5_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 5)</div>
    <div class="q-stmt">
      5. The term &lsquo;eustatic&rsquo; implies :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Worldwide changes in sea level &nbsp;✔</div>
      <div class="raw-opt">(B) Erosion of land to peneplanation</div>
      <div class="raw-opt">(C) Exhumation of rocks</div>
      <div class="raw-opt">(D) Confluence of river streams</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Worldwide changes in sea level</div>
      <div class="sub">
        In stratigraphy, sedimentology, and geodynamics (Eduard Suess, 1888; K.M. Bangar, p. 33; Sam Boggs Jr., p. 434; Vail et al., 1977), <strong>eustatic</strong> refers specifically and universally to <strong>worldwide, simultaneous changes in sea level</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Worldwide changes in sea level</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Coined by Eduard Suess from the Greek roots <em>eu</em> (good, true) and <em>statikos</em> (standing), eustasy denotes global, simultaneous sea-level changes affecting all ocean basins worldwide, distinct from local tectonic subsidence or uplift.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Erosion of land to peneplanation</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The erosion of landmasses to an ultimate low-relief, nearly flat erosion surface is termed <em>peneplanation</em> (introduced by William Morris Davis). A peneplain is an ultimate subaerial geomorphic landform, completely distinct from global sea-level fluctuations.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Exhumation of rocks</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Exhumation is the unroofing and exposure of deeply buried metamorphic or plutonic basement rocks at the Earth's surface through tectonic extension (normal fault detachment) or massive denudational erosion, having no linguistic or mechanical connection to eustasy.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Confluence of river streams</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The junction point where two or more flowing streams merge into a single trunk river is known as a <em>confluence</em> (e.g., Allahabad/Prayagraj), a basic fluvial hydrologic term unrelated to global marine eustasy.
    </div>
  </div>
"""

q5_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comparison: Eustasy vs. Isostasy vs. Tectonism</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Concept</th>
            <th>Primary Mechanism</th>
            <th>Spatial Extent</th>
            <th>Temporal Timescale</th>
            <th>Diagnostic Field / Stratigraphic Record</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Eustasy</strong></td>
            <td>Changes in ocean water volume (ice) or ocean basin volume (ridges)</td>
            <td>Global (Synchronous across all oceans)</td>
            <td>$10^4\\text{ yr}$ (glacial) to $10^8\\text{ yr}$ (tectonic)</td>
            <td>Synchronous global sequence boundaries and transgressive surface onlaps</td>
          </tr>
          <tr>
            <td><strong>Isostasy</strong></td>
            <td>Gravitational buoyant equilibrium of crust floating on asthenosphere</td>
            <td>Regional to local (Ice sheet or mountain range scale)</td>
            <td>$10^3 - 10^4\\text{ yr}$ (viscous relaxation)</td>
            <td>Raised post-glacial shorelines, tilted marine terraces in Scandinavia/Canada</td>
          </tr>
          <tr>
            <td><strong>Tectonism</strong></td>
            <td>Crustal deformation driven by plate boundary forces</td>
            <td>Regional to local (Orogenic belts, rift basins)</td>
            <td>$10^5 - 10^7\\text{ yr}$</td>
            <td>Angular unconformities, faulted strata, localized rapid basin subsidence</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> The Antarctic Ice Sheet contains approximately $V_{\\text{ice}} = 27.0 \\times 10^6\\text{ km}^3$ of ice with an average density $\\rho_{\\text{ice}} = 917\\text{ kg/m}^3$. Assuming complete melting and that the melted water spreads uniformly over the global ocean area $A_{\\text{ocean}} = 3.61 \\times 10^8\\text{ km}^2$ (density $\\rho_{\\text{water}} = 1000\\text{ kg/m}^3$), calculate the equivalent glacio-eustatic sea-level rise in meters.
          <div class="pq-ans">✔ Worked Answer: Sea-level rise $\\Delta h \\approx 68.6\\text{ meters}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Equivalent liquid water volume $V_{\\text{water}} = V_{\\text{ice}} \\times \\frac{\\rho_{\\text{ice}}}{\\rho_{\\text{water}}}$<br>
            $$V_{\\text{water}} = 27.0 \\times 10^6\\text{ km}^3 \\times \\frac{917}{1000} = 24.759 \\times 10^6\\text{ km}^3$$<br>
            $$\\Delta h = \\frac{V_{\\text{water}}}{A_{\\text{ocean}}} = \\frac{24.759 \\times 10^6\\text{ km}^3}{3.61 \\times 10^8\\text{ km}^2} = 0.06858\\text{ km} \\approx 68.6\\text{ m}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Who first introduced the term "eustatic" into geological literature?
          <div class="pq-ans">✔ Correct Answer: Eduard Suess in 1888 in his book <em>The Face of the Earth</em> (<em>Das Antlitz der Erde</em>).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Suess recognized that certain major marine transgressions and regressions occurred synchronously across distant continents, postulating global changes in sea level that he termed eustatic.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What was the magnitude of global eustatic sea-level depression during the Last Glacial Maximum (LGM) $\\approx 21,000\\text{ years ago}$?
          <div class="pq-ans">✔ Correct Answer: Approximately $120\\text{ to } 130\\text{ meters}$ below modern sea level.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The vast accumulation of water into the Laurentide, Fennoscandian, and Antarctic ice sheets locked up $\\approx 50\\text{ million km}^3$ of water, exposing continental shelves worldwide and creating land bridges (e.g., Beringia).
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In sequence stratigraphy, what systems tract is directly formed by a rapid eustatic fall in sea level that outpaces tectonic subsidence?
          <div class="pq-ans">✔ Correct Answer: The Falling Stage Systems Tract (FSST) or Forced Regressive Wedge.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Forced regression occurs when the shoreline shifts basinward independently of sediment supply due to absolute sea-level fall, creating subaerial exposure of the shelf and valley incision.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Why were global sea levels during the mid-Cretaceous period ($100\\text{ Ma}$) estimated to be $150 - 250\\text{ meters}$ higher than today?
          <div class="pq-ans">✔ Correct Answer: Rapid seafloor spreading following the breakup of Pangea expanded the global mid-ocean ridge system, displacing seawater onto continents (tectono-eustasy), combined with an ice-free greenhouse climate.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Fast-spreading ridges are thermally inflated and occupy far greater volume than slow-spreading ridges, dramatically reducing the volumetric capacity of ocean basins.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is "Glacio-Isostatic Adjustment" (GIA), and how does it affect local relative sea level in post-glacial areas?
          <div class="pq-ans">✔ Correct Answer: Post-glacial crustal rebound of the lithosphere following ice sheet unloading, causing local sea level to appear to fall rapidly even while global eustasy rises.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In Scandinavia and Hudson Bay, the land is rebounding at up to $10\\text{ mm/yr}$, uplifting former marine wave-cut platforms high above current sea level as raised beaches.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is the difference between an "autogenic" shoreline shift and an "allogenic" eustatic transgression?
          <div class="pq-ans">✔ Correct Answer: Autogenic shifts are caused by internal sedimentary dynamics (e.g., delta lobe switching); allogenic eustatic shifts are forced by external global sea-level changes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Delta avulsion can cause local coastline retreat due to sediment starvation, but this is an autogenic process; a true eustatic transgression occurs basin-wide simultaneously.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> How do oxygen isotope ratios ($\\delta^{18}\\text{O}$) in benthic foraminifera shells serve as a proxy for ancient glacio-eustatic sea-level fluctuations?
          <div class="pq-ans">✔ Correct Answer: Evaporation preferentially removes light $^{16}\\text{O}$ from oceans, which gets trapped in continental ice sheets, enriching ocean water and foraminifera calcite in heavy $^{18}\\text{O}$ during glacial sea-level lowstands.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Higher $\\delta^{18}\\text{O}$ values in marine carbonate shells directly correlate with larger continental ice volume and lower eustatic sea levels.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=5,
    filename="Q005_Eustatic_Sea_Level_Fluctuations_Complete_Guide.html",
    title="Q005: Eustasy, Global Sea-Level Dynamics & Glacio-Tectonic Mechanisms",
    badge="GGM - 2/2019 • Stratigraphy & Marine Geodynamics",
    h1_title="Q005: The Physics of Eustasy: Global Sea-Level Fluctuations & Sequence Dynamics",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 5<br><strong>Authoritative References:</strong> Eduard Suess (<em>Das Antlitz der Erde</em>, 1888); K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 33); Sam Boggs Jr. (<em>Sedimentology & Stratigraphy</em>, Ch. 12, pp. 434–442); Vail et al. (1977)",
    part1_html=q5_part1,
    part2_html=q5_part2,
    part3_html=q5_part3
)

print("Batch 1 (Q001 - Q005) generated successfully.")
