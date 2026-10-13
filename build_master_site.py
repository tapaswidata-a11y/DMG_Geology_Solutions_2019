#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup

q_metadata = [
    {
        "q": 1,
        "file": "Q1_Bouma_Sequence_Turbidites_Complete_Guide.html",
        "pdf": "Q1_Bouma_Sequence_Turbidites_Complete_Guide.pdf",
        "section": "Sedimentology & Stratigraphy",
        "topic": "Bouma Sequence & Turbidite Current Dynamics",
        "question": "The ideal sequence of sedimentary structures in a turbidite bed (Bouma sequence) from bottom to top is:",
        "correct": "Massive/graded (Ta) → Parallel lam (Tb) → Rippled/convolute (Tc) → Upper parallel (Td) → Pelagic (Te)",
        "icon": "🌊"
    },
    {
        "q": 2,
        "file": "Q2.boggs_syntaxial_analysis.html",
        "pdf": "Q2.boggs_syntaxial_analysis.pdf",
        "section": "Sedimentology & Stratigraphy",
        "topic": "Syntaxial Overgrowths & Sandstone Diagenesis",
        "question": "Secondary mineral growth in optical continuity with a detrital grain is known as:",
        "correct": "Syntaxial overgrowth (Cementation in optical continuity with detrital quartz/calcite)",
        "icon": "💎"
    },
    {
        "q": 3,
        "file": "Q3.grainstone_dunham_comprehensive.html",
        "pdf": "Q3.grainstone_dunham_comprehensive.pdf",
        "section": "Sedimentology & Stratigraphy",
        "topic": "Grainstone & Dunham Carbonate Classification",
        "question": "A mud-free, grain-supported carbonate rock in Dunham's classification is termed as:",
        "correct": "Grainstone (< 1% mud matrix, grain-supported high-energy shoal carbonate)",
        "icon": "🪨"
    },
    {
        "q": 4,
        "file": "Q4.barrovian_zone_solution.html",
        "pdf": "Q4.barrovian_zone_solution.pdf",
        "section": "Metamorphic Petrology",
        "topic": "Barrovian Metamorphic Zones & Isograd Sequence",
        "question": "The correct sequence of Barrovian metamorphic zones in pelitic rocks with increasing grade is:",
        "correct": "Chlorite → Biotite → Garnet → Staurolite → Kyanite → Sillimanite",
        "icon": "🔥"
    },
    {
        "q": 5,
        "file": "Q5.granulite_facies_solution.html",
        "pdf": "Q5.granulite_facies_solution.pdf",
        "section": "Metamorphic Petrology",
        "topic": "Granulite Facies Mineral Assemblages & Fluid Absenteeism",
        "question": "The mineral assemblage characteristic of the granulite facies in metabasites is:",
        "correct": "Orthopyroxene + Clinopyroxene + Plagioclase ± Garnet (Dehydration breakdown of hornblende)",
        "icon": "🌋"
    },
    {
        "q": 6,
        "file": "Q6.pressure_shadows_solution.html",
        "pdf": "Q6.pressure_shadows_solution.pdf",
        "section": "Metamorphic Petrology & Textures",
        "topic": "Pressure Shadows & Kinematic Strain Markers",
        "question": "Low-pressure domains adjacent to rigid porphyroblasts where fibrous minerals precipitate are termed:",
        "correct": "Pressure shadows (Pressure fringes / Strain fringes)",
        "icon": "🌀"
    },
    {
        "q": 7,
        "file": "Q7.matching_metamorphic_rocks_solution.html",
        "pdf": "Q7.matching_metamorphic_rocks_solution.pdf",
        "section": "Metamorphic Petrology",
        "topic": "Metamorphic Rock & Facies Systematics",
        "question": "Matching diagnostic metamorphic rocks and mineral assemblages with their respective facies:",
        "correct": "Eclogite (Omphacite+Garnet), Blueschist (Glaucophane), Greenschist (Chlorite+Actinolite), Granulite (Pyroxene granulite)",
        "icon": "⚖️"
    },
    {
        "q": 8,
        "file": "Q8.protolith_interpretation_solution.html",
        "pdf": "Q8.protolith_interpretation_solution.pdf",
        "section": "Metamorphic Petrology",
        "topic": "Protolith Discrimination & Pelite Evolution",
        "question": "Metamorphic rock rich in Al-silicates (andalusite, kyanite, sillimanite) is derived from which protolith?",
        "correct": "Pelitic protolith (Shale / Mudstone with high Al/Si ratio)",
        "icon": "📜"
    },
    {
        "q": 9,
        "file": "Q9_Eclogite_Facies_Reactions_Complete_Guide.html",
        "pdf": "Q9_Eclogite_Facies_Reactions_Complete_Guide.pdf",
        "section": "Metamorphic Petrology",
        "topic": "Eclogite Facies & Subduction Dehydration Reactions",
        "question": "The breakdown of plagioclase under high P/T subduction metamorphism yields:",
        "correct": "Omphacite (Jadeite-rich clinopyroxene) + Pyrope-rich Garnet + Quartz (Absence of plagioclase)",
        "icon": "💎"
    },
    {
        "q": 10,
        "file": "Q10_Granoblastic_Polygonal_Texture.html",
        "pdf": "Q10_Granoblastic_Polygonal_Texture.pdf",
        "section": "Metamorphic Petrology & Textures",
        "topic": "Granoblastic Polygonal Texture & Annealing Interfacial Energy",
        "question": "A metamorphic texture characterized by equant, polygonal grains meeting at 120° triple junctions is called:",
        "correct": "Granoblastic polygonal texture (Foam texture / Static annealing equilibrium)",
        "icon": "🛑"
    },
    {
        "q": 11,
        "file": "Q11_CalcSilicate_Metamorphism_Complete_Guide.html",
        "pdf": "Q11_CalcSilicate_Metamorphism_DMG2019.pdf",
        "section": "Metamorphic Petrology",
        "topic": "Calc-Silicate Metamorphism & Decarbonation Reactions",
        "question": "Progressive contact metamorphism of siliceous dolomite (Bowen's reaction sequence) yields:",
        "correct": "Talc → Tremolite → Diopside → Forsterite → Wollastonite",
        "icon": "🧪"
    },
    {
        "q": 12,
        "file": "Q12_Hinge_Line_Fold_Geometry_Complete_Guide.html",
        "pdf": "Q12_Hinge_Line_Fold_Geometry_Complete_Guide.pdf",
        "section": "Structural Geology & Tectonics",
        "topic": "Fold Geometry: Hinge Line vs. Fold Axis",
        "question": "The line connecting points of maximum curvature on a folded surface is termed as:",
        "correct": "Hinge line (A tangible physical line of maximum curvature; cylindrical or non-cylindrical)",
        "icon": "📐"
    },
    {
        "q": 13,
        "file": "Q13_Transform_Faults_Complete_Guide.html",
        "pdf": "Q13_Transform_Faults_Complete_Guide.pdf",
        "section": "Structural Geology & Tectonics",
        "topic": "Transform Faults vs. Transcurrent Faults (J. Tuzo Wilson)",
        "question": "A strike-slip fault that terminates abruptly against other plate boundaries (ridge-ridge transform) is a:",
        "correct": "Transform fault (Seismicity restricted to the intra-ridge segment; slip sense opposite to apparent offset)",
        "icon": "⚡"
    },
    {
        "q": 14,
        "file": "Q14_Diapir_Folds_Salt_Tectonics_Complete_Guide.html",
        "pdf": "Q14_diapir_fold.pdf",
        "section": "Structural Geology & Tectonics",
        "topic": "Salt Tectonics, Diapiric Folds & Halokinesis",
        "question": "Piercement folds produced by mobile, ductile core material piercing overlying brittle strata are:",
        "correct": "Diapir folds (Diapirs / Salt domes driven by Rayleigh-Taylor buoyancy)",
        "icon": "🍄"
    },
    {
        "q": 15,
        "file": "Q15_Oblique_Slip_Faults_Complete_Guide.html",
        "pdf": "Q15_Oblique_Slip_Faults_Complete_Guide.pdf",
        "section": "Structural Geology & Tectonics",
        "topic": "Fault Kinematics & Oblique-Slip Faults",
        "question": "A fault having both dip-slip as well as strike-slip components is termed as:",
        "correct": "Oblique-slip fault (Net slip vector inclined at intermediate pitch 10°–80°)",
        "icon": "↔️"
    },
    {
        "q": 16,
        "file": "Q16_Isometric_System_Crystal_Symmetry_Complete_Guide.html",
        "pdf": "Q16_Isometric_System.pdf",
        "section": "Mineralogy & Crystallography",
        "topic": "Isometric System Symmetry (4 Three-Fold Axes at 54°44′)",
        "question": "Four three-fold axes, each inclined at 54°44′ to crystallographic axes, characterize which crystal system?",
        "correct": "Isometric (Cubic) system (Body diagonals of the cube; arccos(1/√3) = 54°44′)",
        "icon": "🎲"
    },
    {
        "q": 17,
        "file": "Q17_Saussuritization_Plagioclase_Alteration_Complete_Guide.html",
        "pdf": "Q17_Postmagmatic_Alteration_Complete_Concept_Guide.pdf",
        "section": "Mineralogy & Petrology",
        "topic": "Saussuritization of Calcic Plagioclase",
        "question": "Ca-rich plagioclase breaks down to almost pure albite and epidote during which deuteric alteration?",
        "correct": "Saussuritization (Autometamorphic hydration of anorthite molecule to albite + epidote/zoisite)",
        "icon": "🔬"
    },
    {
        "q": 18,
        "file": "Q18_Incompatible_Trace_Elements_Complete_Guide.html",
        "pdf": "Q18_Incompatible_Trace_Elements_Complete_Guide.pdf",
        "section": "Igneous Petrology & Geochemistry",
        "topic": "Incompatible Trace Elements & Igneous Differentiation",
        "question": "Which one of the following rocks is normally expected to have the highest abundance of incompatible trace elements?",
        "correct": "Granite (Terminal felsic liquid accumulating all LILE and HFSE rejected by early mafic minerals)",
        "icon": "📈"
    },
    {
        "q": 19,
        "file": "Q19_Magma_Series_Tectonic_Settings_Complete_Guide.html",
        "pdf": "Q19_Magma_Series_Complete_Guide.pdf",
        "section": "Igneous Petrology & Geochemistry",
        "topic": "Calc-Alkaline Magma Series in Subduction Zones",
        "question": "Which one of the following magma series is found only in subduction zones?",
        "correct": "Calc-alkaline (Hydrous, oxidized wedge melting; early titanomagnetite suppresses iron enrichment)",
        "icon": "🌋"
    },
    {
        "q": 20,
        "file": "Q20_Rb_Sr_Isotope_System_Complete_Guide.html",
        "pdf": "Q20_Rb_Sr_Isotope_System_Complete_Guide.pdf",
        "section": "Isotope Geochemistry",
        "topic": "Rb-Sr Isotope System & Planetary Reservoirs",
        "question": "Average continental crust reservoir is represented by which one of the following Rb/Sr values?",
        "correct": "0.158 (Enriched relative to Bulk Silicate Earth 0.027 due to incompatible Rb extraction)",
        "icon": "⏱️"
    },
    {
        "q": 21,
        "file": "Q21_REE_Diagram_Europium_Anomaly_Complete_Guide.html",
        "pdf": "Q21_REE_Diagram_Europium_Anomaly_Complete_Guide.pdf",
        "section": "Isotope Geochemistry",
        "topic": "REE Systematics & The Europium Anomaly (Sm-Gd)",
        "question": "In a rare earth element (REE) diagram, europium anomaly is seen between which REE pair?",
        "correct": "Sm-Gd (Europium Z=63 sits between Samarium Z=62 and Gadolinium Z=64; Eu* = √(Sm_N × Gd_N))",
        "icon": "📊"
    },
    {
        "q": 22,
        "file": "Q22_Epsilon_Notation_CHUR_Complete_Guide.html",
        "pdf": "Q22_Epsilon_Notation_CHUR_Complete_Guide.pdf",
        "section": "Isotope Geochemistry",
        "topic": "Epsilon Nd (εNd) Notation & CHUR",
        "question": "Which symbol denotes the deviation of the Nd-isotopic composition from the chondritic uniform reservoir?",
        "correct": "ε (Epsilon) — Parts per 10,000 deviation from CHUR [(Nd_sample/Nd_CHUR - 1) × 10⁴]",
        "icon": "🔣"
    },
    {
        "q": 23,
        "file": "Q23_UPb_Concordia_Discordia_Complete_Guide.html",
        "pdf": "Q23_UPb_Concordia_Discordia_Complete_Guide.pdf",
        "section": "Isotope Geochemistry",
        "topic": "U-Pb Geochronology & The Concordia Curve",
        "question": "In a 238U/206Pb vs 235U/207Pb diagram, the locus of points having the same dual ages is known as:",
        "correct": "Concordia curve (Parametric curve of concordant ages; Discordia chord dates lead loss events)",
        "icon": "⏳"
    },
    {
        "q": 24,
        "file": "Q24_Silicate_Melt_Structure_Complete_Guide.html",
        "pdf": "Q24_Silicate_Melt_Structure_Complete_Guide.pdf",
        "section": "Melt Physics & Petrogenesis",
        "topic": "Silicate Melt Physics: Network Modifiers vs. Formers",
        "question": "In the atomic structure of silicate melts, Ca2+ and Mg2+ ions are categorized as:",
        "correct": "Network modifiers (Depolymerize melt framework by breaking Si-O-Si bridging bonds into non-bridging oxygens)",
        "icon": "⚛️"
    },
    {
        "q": 25,
        "file": "Q25_MORB_Petrogenesis_Mantle_Source_Complete_Guide.html",
        "pdf": "Q25_MORB_Petrogenesis_Mantle_Source_Complete_Guide.pdf",
        "section": "Igneous Petrology & Geochemistry",
        "topic": "MORB Petrogenesis & Mantle Reservoir Systematics",
        "question": "Which one of the following Mid-Oceanic Ridge Basalts (MORB) is derived from an incompatible element-poor mantle?",
        "correct": "N-MORB (Normal MORB derived from depleted upper mantle DMM with (La/Sm)_N < 1, depleted in incompatible elements)",
        "icon": "🌊"
    },
    {
        "q": 26,
        "file": "Q26_Nd_Isotopic_Reservoirs_BSE_CHUR_Complete_Guide.html",
        "pdf": "Q26_Nd_Isotopic_Reservoirs_BSE_CHUR_Complete_Guide.pdf",
        "section": "Geochemistry & Geochronology",
        "topic": "Mantle Reservoirs & BSE/CHUR Isotope Systematics",
        "question": "Which one of the following geochemical reservoirs is defined by the Nd-isotopic composition of chondritic meteorites?",
        "correct": "BSE (Bulk Silicate Earth / CHUR with 143Nd/144Nd = 0.512638 and εNd = 0)",
        "icon": "🪐"
    },
    {
        "q": 27,
        "file": "Q27_Equilibrium_Mineral_Assemblage_Fo_Qtz_Complete_Guide.html",
        "pdf": "Q27_Equilibrium_Mineral_Assemblage_Fo_Qtz_Complete_Guide.pdf",
        "section": "Igneous Petrology & Phase Equilibria",
        "topic": "Equilibrium Mineral Assemblages & Fo-Qtz Incompatibility",
        "question": "Which of the following do NOT constitute an equilibrium mineral assemblage in a rock?",
        "correct": "Forsterite and quartz (Chemically incompatible pair; react via Fo + Qtz → 2 En)",
        "icon": "🌋"
    },
    {
        "q": 28,
        "file": "Q28_Wave_Dominated_Coastline_Zonation_Complete_Guide.html",
        "pdf": "Q28_Wave_Dominated_Coastline_Zonation_Complete_Guide.pdf",
        "section": "Sedimentary Environments & Coastal Dynamics",
        "topic": "Wave-Dominated Coastline Hydrodynamic Zonation",
        "question": "In a wave-dominated coastline, the correct distribution of environment from land to sea is:",
        "correct": "Swash zone → surf zone → breaker zone → shoaling zone (Landward beach face to seaward shoreface)",
        "icon": "🏖️"
    },
    {
        "q": 29,
        "file": "Q29_Deltaic_Zonation_Delta_Front_Complete_Guide.html",
        "pdf": "Q29_Deltaic_Zonation_Delta_Front_Complete_Guide.pdf",
        "section": "Sedimentary Environments & Stratigraphy",
        "topic": "Deltaic Environments: Subaqueous Delta Zonation",
        "question": "The uppermost part of subaqueous delta that lies at water depth down to 10 m or so, is referred to as:",
        "correct": "Delta front (Uppermost subaqueous delta, depth 0 to ~10 m; mouth bar sands)",
        "icon": "🌊"
    },
    {
        "q": 30,
        "file": "Q30_Bedform_Succession_Bed_Shear_Complete_Guide.html",
        "pdf": "Q30_Bedform_Succession_Bed_Shear_Complete_Guide.pdf",
        "section": "Sedimentary Environments & Stratigraphy",
        "topic": "Hydrodynamics: Bedform Succession with Increasing Bed Shear",
        "question": "Which one of the following sequences of sedimentary structures is correct in terms of increasing bed shear?",
        "correct": "Ripple, dune, parting lineation, flute mark (Lower flow regime to turbulent sole scour)",
        "icon": "🌊"
    },
    {
        "q": 31,
        "file": "Q31_Benioff_Zone_Deep_Earthquakes_Complete_Guide.html",
        "pdf": "Q31_Benioff_Zone_Deep_Earthquakes_Complete_Guide.pdf",
        "section": "Seismology & Earth Interior",
        "topic": "Seismotectonics: Deep-Focus Earthquakes & Wadati-Benioff Zone",
        "question": "The deep-focused earthquakes commonly originate along:",
        "correct": "Benioff zone (Dipping subducting lithospheric slab down to ~670 km)",
        "icon": "⚡"
    }
]

print("Processing HTML files and extracting inner contents...")
extracted_content = []

for meta in q_metadata:
    fname = meta["file"]
    q_num = meta["q"]
    with open(fname, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
        # find container
        container = soup.find("div", class_="page") or soup.find("div", class_="container") or soup.body
        
        # fix relative image links if needed (they are already figures_QXX/...)
        # wrap in an article tag
        article_html = f'''
        <article class="question-module" id="q{q_num}" data-q="{q_num}" data-section="{meta['section']}" data-topic="{meta['topic']}">
          <div class="module-topbar">
            <div class="module-breadcrumbs">
              <span class="crumb-sec">{meta['section']}</span>
              <span class="crumb-sep">/</span>
              <span class="crumb-q">Question {q_num}</span>
            </div>
            <div class="module-actions">
              <a href="{meta['file']}" target="_blank" class="btn-action" title="Open standalone HTML page">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                Standalone View
              </a>
              <a href="{meta['pdf']}" target="_blank" class="btn-action btn-pdf" title="Download Print-Ready PDF">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                PDF Guide
              </a>
            </div>
          </div>
          <div class="module-body">
            {container.decode_contents()}
          </div>
        </article>
        '''
        extracted_content.append(article_html)

# Build Sections list for Sidebar
sections_dict = {}
for m in q_metadata:
    sec = m["section"]
    if sec not in sections_dict:
        sections_dict[sec] = []
    sections_dict[sec].append(m)

sidebar_nav_html = []
for sec, q_list in sections_dict.items():
    sidebar_nav_html.append(f'<div class="nav-section-title">{sec}</div>')
    sidebar_nav_html.append('<ul class="nav-list">')
    for m in q_list:
        sidebar_nav_html.append(f'''
        <li class="nav-item" data-q="{m['q']}">
          <a href="#q{m['q']}" class="nav-link" onclick="selectQuestion({m['q']}); return false;">
            <span class="nav-badge">Q{m['q']:02d}</span>
            <div class="nav-info">
              <div class="nav-title">{m['topic']}</div>
              <div class="nav-preview">{m['question']}</div>
            </div>
          </a>
        </li>
        ''')
    sidebar_nav_html.append('</ul>')

sidebar_html = "\n".join(sidebar_nav_html)
all_articles_html = "\n".join(extracted_content)

# HTML Template
index_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DGMS 2019 Geology · Comprehensive Textbook Solutions & Masterclass Portal</title>
<meta name="description" content="Authoritative, textbook-grounded solutions and concept guides for all questions of the DGMS 2019 Junior Scientific Officer (Geology) Examination.">

<!-- Fonts & MathJax -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
  }},
  svg: {{ fontCache: 'global' }}
}};
</script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

<style>
  /* ── Master Theme & Variables ── */
  :root {{
    --bg-main: #f8fafc;
    --bg-surface: #ffffff;
    --bg-sidebar: #0f172a;
    --bg-sidebar-hover: #1e293b;
    --bg-sidebar-active: #2563eb;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --text-sidebar: #94a3b8;
    --text-sidebar-bright: #f8fafc;
    --border-color: #e2e8f0;
    --primary: #2563eb;
    --primary-dark: #1d4ed8;
    --accent: #10b981;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'Fira Code', Consolas, monospace;
    --sidebar-width: 340px;
    --header-height: 64px;
    --radius: 8px;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: var(--font-sans);
    background-color: var(--bg-main);
    color: var(--text-main);
    line-height: 1.6;
    overflow-x: hidden;
  }}

  /* ── Master Layout ── */
  .app-container {{
    display: flex;
    min-height: 100vh;
  }}

  /* ── Left Sidebar ── */
  .sidebar {{
    width: var(--sidebar-width);
    background: var(--bg-sidebar);
    color: var(--text-sidebar);
    height: 100vh;
    position: sticky;
    top: 0;
    display: flex;
    flex-direction: column;
    z-index: 50;
    flex-shrink: 0;
    border-right: 1px solid #1e293b;
    box-shadow: 2px 0 12px rgba(0,0,0,0.15);
  }}

  .sidebar-header {{
    padding: 20px 20px 16px 20px;
    border-bottom: 1px solid #1e293b;
    background: #090d16;
  }}
  .brand-badge {{
    display: inline-block;
    background: linear-gradient(135deg, #2563eb, #3b82f6);
    color: #fff;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 6px;
  }}
  .brand-title {{
    font-size: 15px;
    font-weight: 700;
    color: #fff;
    line-height: 1.3;
  }}
  .brand-sub {{
    font-size: 11.5px;
    color: #64748b;
    margin-top: 4px;
  }}

  .sidebar-search {{
    padding: 12px 16px;
    border-bottom: 1px solid #1e293b;
    background: #0f172a;
  }}
  .search-box {{
    display: flex;
    align-items: center;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 6px 10px;
    gap: 8px;
  }}
  .search-box input {{
    background: transparent;
    border: none;
    outline: none;
    color: #fff;
    font-size: 12.5px;
    width: 100%;
    font-family: inherit;
  }}
  .search-box input::placeholder {{ color: #64748b; }}
  .search-box svg {{ color: #64748b; flex-shrink: 0; }}

  .sidebar-nav {{
    flex: 1;
    overflow-y: auto;
    padding: 12px 10px 24px 10px;
  }}
  .sidebar-nav::-webkit-scrollbar {{ width: 6px; }}
  .sidebar-nav::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 3px; }}

  .nav-section-title {{
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748b;
    padding: 12px 10px 6px 10px;
    margin-top: 6px;
  }}
  .nav-list {{ list-style: none; }}
  .nav-item {{ margin-bottom: 3px; }}
  .nav-link {{
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 8px 10px;
    border-radius: 6px;
    color: var(--text-sidebar);
    text-decoration: none;
    transition: all 0.15s ease;
  }}
  .nav-link:hover {{
    background: var(--bg-sidebar-hover);
    color: #fff;
  }}
  .nav-item.active .nav-link {{
    background: var(--bg-sidebar-active);
    color: #fff;
    box-shadow: 0 2px 6px rgba(37,99,235,0.3);
  }}
  .nav-badge {{
    background: #1e293b;
    color: #93c5fd;
    font-size: 10.5px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 4px;
    flex-shrink: 0;
    margin-top: 1px;
  }}
  .nav-item.active .nav-badge {{
    background: #1d4ed8;
    color: #fff;
  }}
  .nav-info {{ flex: 1; min-width: 0; }}
  .nav-title {{
    font-size: 12.5px;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .nav-preview {{
    font-size: 11px;
    color: #64748b;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-top: 2px;
  }}
  .nav-item.active .nav-preview {{ color: #bfdbfe; }}

  /* ── Main View Area ── */
  .main-wrapper {{
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
  }}

  /* Top Navbar */
  .top-navbar {{
    height: var(--header-height);
    background: #fff;
    border-bottom: 1px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 40;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 28px;
    box-shadow: var(--shadow-sm);
  }}
  .navbar-left {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .current-q-indicator {{
    font-size: 14px;
    font-weight: 700;
    color: #1e293b;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .current-badge {{
    background: #eff6ff;
    color: #2563eb;
    border: 1px solid #bfdbfe;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11.5px;
    font-weight: 700;
  }}
  .navbar-actions {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .nav-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 14px;
    border-radius: 6px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
    border: 1px solid var(--border-color);
    background: #fff;
    color: #334155;
    text-decoration: none;
    transition: all 0.15s ease;
  }}
  .nav-btn:hover {{
    background: #f1f5f9;
    color: #0f172a;
  }}
  .nav-btn-primary {{
    background: #2563eb;
    color: #fff;
    border-color: #2563eb;
  }}
  .nav-btn-primary:hover {{
    background: #1d4ed8;
    color: #fff;
  }}

  /* Content Display */
  .content-area {{
    flex: 1;
    padding: 32px 24px 60px 24px;
    max-width: 1040px;
    margin: 0 auto;
    width: 100%;
  }}

  /* Question Module Article */
  .question-module {{
    display: none; /* hidden until selected in single-view */
    background: transparent;
    margin-bottom: 40px;
  }}
  .question-module.active {{
    display: block;
    animation: fadeIn 0.25s ease-in-out;
  }}
  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(6px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  /* When "View All" is toggled */
  body.view-all .question-module {{
    display: block !important;
    border-bottom: 2px dashed #cbd5e1;
    padding-bottom: 48px;
    margin-bottom: 48px;
  }}

  .module-topbar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #fff;
    border: 1px solid var(--border-color);
    border-radius: var(--radius);
    padding: 12px 18px;
    margin-bottom: 20px;
    box-shadow: var(--shadow-sm);
  }}
  .module-breadcrumbs {{
    font-size: 12.5px;
    color: var(--text-muted);
    font-weight: 500;
  }}
  .crumb-sec {{ color: #2563eb; font-weight: 600; }}
  .crumb-sep {{ margin: 0 6px; color: #cbd5e1; }}
  .crumb-q {{ color: #0f172a; font-weight: 700; }}

  .module-actions {{
    display: flex;
    gap: 8px;
  }}
  .btn-action {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    font-weight: 600;
    padding: 5px 11px;
    border-radius: 5px;
    text-decoration: none;
    color: #475569;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    transition: all 0.15s ease;
  }}
  .btn-action:hover {{
    background: #f1f5f9;
    color: #0f172a;
    border-color: #94a3b8;
  }}
  .btn-action.btn-pdf {{
    background: #eff6ff;
    color: #1d4ed8;
    border-color: #bfdbfe;
  }}
  .btn-action.btn-pdf:hover {{
    background: #dbeafe;
    color: #1e40af;
  }}

  /* Mobile Responsive Drawer */
  .mobile-menu-btn {{
    display: none;
    background: none;
    border: none;
    color: #334155;
    cursor: pointer;
  }}
  @media (max-width: 900px) {{
    .sidebar {{
      position: fixed;
      left: -100%;
      transition: left 0.3s ease;
    }}
    .sidebar.open {{ left: 0; }}
    .mobile-menu-btn {{ display: block; }}
  }}

  /* ── Master Question Module Component Styles ── */
  .page {{ max-width: 940px; margin: 0 auto; }}
  
  .header {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    color: #fff;
    border-radius: 12px;
    padding: 26px 30px;
    margin-bottom: 22px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  }}
  .header .badge {{
    display: inline-block;
    background: #2563eb;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 4px;
    padding: 3px 10px;
    margin-bottom: 10px;
  }}
  .header h1 {{ font-size: 22px; font-weight: 700; line-height: 1.35; }}
  .header .meta {{ font-size: 13px; color: #94a3b8; margin-top: 8px; }}

  .part-banner {{
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    color: #fff;
    border-radius: 10px;
    padding: 16px 24px;
    margin: 28px 0 20px 0;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 3px 10px rgba(37, 99, 235, 0.2);
  }}
  .part-banner.green {{
    background: linear-gradient(135deg, #065f46 0%, #059669 100%);
    box-shadow: 0 3px 10px rgba(5, 150, 105, 0.2);
  }}
  .part-banner.purple {{
    background: linear-gradient(135deg, #581c87 0%, #7c3aed 100%);
    box-shadow: 0 3px 10px rgba(124, 58, 237, 0.2);
  }}
  .part-banner .part-num {{
    font-size: 26px;
    font-weight: 800;
    opacity: 0.9;
    border-right: 2px solid rgba(255,255,255,0.3);
    padding-right: 14px;
    line-height: 1;
  }}
  .part-banner .part-title {{
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.3px;
  }}
  .part-banner .part-sub {{
    font-size: 12.5px;
    opacity: 0.9;
    margin-top: 2px;
  }}

  .answer-banner {{
    background: linear-gradient(90deg, #059669 0%, #10b981 100%);
    color: #fff;
    border-radius: 10px;
    padding: 16px 22px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 3px 10px rgba(16, 185, 129, 0.2);
  }}
  .answer-banner .tick {{ font-size: 32px; line-height: 1; font-weight: bold; }}
  .answer-banner .text {{ font-size: 18px; font-weight: 700; }}
  .answer-banner .sub {{ font-size: 13.5px; opacity: 0.95; margin-top: 3px; }}

  .card {{
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 22px 24px;
    margin-bottom: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}
  .card h2 {{
    font-size: 16.5px;
    font-weight: 700;
    color: #1e293b;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .card h3 {{
    font-size: 14px;
    font-weight: 700;
    color: #334155;
    margin: 14px 0 6px 0;
  }}
  .card p {{ margin-bottom: 10px; font-size: 13.5px; }}

  .highlight-box {{
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    margin: 12px 0;
    font-size: 13px;
  }}
  .quote-box {{
    background: #fdf4ff;
    border-left: 4px solid #a855f7;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin: 14px 0;
    font-style: italic;
    font-size: 13px;
    color: #3b0764;
  }}
  .quote-box .citation {{
    font-style: normal;
    font-weight: 700;
    color: #7e22ce;
    margin-top: 6px;
    font-size: 11.5px;
  }}

  .formula-card {{
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: #f8fafc;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 14px 0;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 13px;
    border-left: 4px solid #38bdf8;
  }}
  .formula-card .title {{
    font-family: 'Segoe UI', sans-serif;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 6px;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .tb-figure {{
    background: #fff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 12px;
    margin: 18px 0;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }}
  .tb-figure img {{
    max-width: 100%;
    height: auto;
    border-radius: 4px;
    display: block;
    margin: 0 auto 10px auto;
    max-height: 480px;
    object-fit: contain;
  }}
  .tb-figure .caption {{
    font-size: 12px;
    color: #475569;
    text-align: left;
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
    line-height: 1.45;
  }}
  .tb-figure .caption strong {{ color: #1e293b; }}

  .option {{
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 12px;
    background: #fff;
  }}
  .option.correct {{
    border-color: #10b981;
    background: #f0fdf4;
  }}
  .option.incorrect {{
    border-color: #f87171;
    background: #fef2f2;
  }}
  .option-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 6px;
  }}
  .option.correct .option-header {{ color: #065f46; }}
  .option.incorrect .option-header {{ color: #991b1b; }}
  .badge-tag {{
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
  }}
  .badge-correct {{ background: #dcfce7; color: #15803d; }}
  .badge-incorrect {{ background: #fee2e2; color: #b91c1c; }}

  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
    margin: 14px 0;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 9px 12px;
    text-align: left;
  }}
  th {{
    background: #f1f5f9;
    font-weight: 700;
    color: #1e293b;
  }}
  tr:nth-child(even) {{ background: #f8fafc; }}

  .question-box {{
    background: #eff6ff;
    border: 2px solid #3b82f6;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 18px;
  }}
  .question-box .q-num {{
    font-size: 12px;
    font-weight: 700;
    color: #1d4ed8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
  }}
  .question-box .q-stmt {{
    font-size: 15px;
    font-weight: 600;
    color: #0f172a;
    line-height: 1.5;
  }}

  .practice-box {{
    background: #faf5ff;
    border: 1px solid #d8b4fe;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 14px;
  }}
  .practice-box .p-title {{
    font-weight: 700;
    color: #6b21a8;
    font-size: 13.5px;
    margin-bottom: 6px;
  }}
  .practice-box .ans {{
    background: #f3e8ff;
    border-radius: 6px;
    padding: 8px 12px;
    margin-top: 8px;
    font-size: 12.5px;
    color: #4c1d95;
  }}

</style>
</head>
<body>

<div class="app-container">

  <!-- ── SIDEBAR NAVIGATION ── -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <span class="brand-badge">DGMS 2019 · Complete Suite</span>
      <h1 class="brand-title">Geology Master Solution</h1>
      <div class="brand-sub">{len(q_metadata)} Comprehensive Textbook Guides</div>
    </div>

    <div class="sidebar-search">
      <div class="search-box">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="searchInput" placeholder="Search questions, topics, rocks..." onkeyup="filterQuestions()">
      </div>
    </div>

    <nav class="sidebar-nav" id="sidebarNav">
      {sidebar_html}
    </nav>
  </aside>

  <!-- ── MAIN CONTENT ── -->
  <div class="main-wrapper">
    <!-- Sticky Top Navbar -->
    <header class="top-navbar">
      <div class="navbar-left">
        <button class="mobile-menu-btn" onclick="toggleSidebar()" aria-label="Toggle menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
        <div class="current-q-indicator">
          <span class="current-badge" id="currentBadge">Q01</span>
          <span id="currentTitle">Bouma Sequence & Turbidite Current Dynamics</span>
        </div>
      </div>
      <div class="navbar-actions">
        <button class="nav-btn" onclick="prevQuestion()" title="Previous Question (Left Arrow)">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
          Prev
        </button>
        <button class="nav-btn" onclick="nextQuestion()" title="Next Question (Right Arrow)">
          Next
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
        <button class="nav-btn nav-btn-primary" id="viewAllToggle" onclick="toggleViewAll()">
          View All Questions
        </button>
      </div>
    </header>

    <!-- Question Modules Container -->
    <main class="content-area" id="contentArea">
      {all_articles_html}
    </main>
  </div>

</div>

<!-- ── INTERACTIVE CONTROLLER ── -->
<script>
  let currentQ = 1;
  const totalQ = {len(q_metadata)};
  let isViewAll = false;

  function selectQuestion(qNum) {{
    if (isViewAll) {{
      toggleViewAll();
    }}
    currentQ = qNum;
    
    // Update active module
    document.querySelectorAll('.question-module').forEach(el => {{
      el.classList.remove('active');
    }});
    const activeEl = document.getElementById('q' + qNum);
    if (activeEl) {{
      activeEl.classList.add('active');
    }}

    // Update active nav link
    document.querySelectorAll('.nav-item').forEach(el => {{
      el.classList.remove('active');
      if (parseInt(el.getAttribute('data-q')) === qNum) {{
        el.classList.add('active');
        el.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
      }}
    }});

    // Update navbar indicator
    const qBadge = document.getElementById('currentBadge');
    const qTitle = document.getElementById('currentTitle');
    if (activeEl) {{
      qBadge.textContent = 'Q' + (qNum < 10 ? '0' + qNum : qNum);
      qTitle.textContent = activeEl.getAttribute('data-topic');
    }}

    // Update URL hash cleanly
    if (history.replaceState) {{
      history.replaceState(null, null, '#q' + qNum);
    }}

    // Scroll main window to top
    window.scrollTo({{ top: 0, behavior: 'smooth' }});

    // Typeset MathJax
    if (window.MathJax && window.MathJax.typesetPromise) {{
      MathJax.typesetPromise();
    }}
  }}

  function prevQuestion() {{
    if (currentQ > 1) selectQuestion(currentQ - 1);
  }}

  function nextQuestion() {{
    if (currentQ < totalQ) selectQuestion(currentQ + 1);
  }}

  function toggleViewAll() {{
    isViewAll = !isViewAll;
    const body = document.body;
    const btn = document.getElementById('viewAllToggle');
    if (isViewAll) {{
      body.classList.add('view-all');
      btn.textContent = 'Single Question View';
      btn.classList.remove('nav-btn-primary');
    }} else {{
      body.classList.remove('view-all');
      btn.textContent = 'View All Questions';
      btn.classList.add('nav-btn-primary');
      selectQuestion(currentQ);
    }}
    if (window.MathJax && window.MathJax.typesetPromise) {{
      MathJax.typesetPromise();
    }}
  }}

  function toggleSidebar() {{
    document.getElementById('sidebar').classList.toggle('open');
  }}

  function filterQuestions() {{
    const query = document.getElementById('searchInput').value.toLowerCase();
    document.querySelectorAll('.nav-item').forEach(item => {{
      const text = item.textContent.toLowerCase();
      if (text.includes(query)) {{
        item.style.display = '';
      }} else {{
        item.style.display = 'none';
      }}
    }});
  }}

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT') return;
    if (e.key === 'ArrowLeft') prevQuestion();
    if (e.key === 'ArrowRight') nextQuestion();
  }});

  // Handle URL hash on load and change
  function initFromHash() {{
    const hash = window.location.hash;
    const match = hash.match(/#q(\d+)/);
    if (match) {{
      const q = parseInt(match[1]);
      if (q >= 1 && q <= totalQ) {{
        selectQuestion(q);
        return;
      }}
    }}
    selectQuestion(1);
  }}

  window.addEventListener('DOMContentLoaded', initFromHash);
  window.addEventListener('hashchange', initFromHash);
</script>

</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_template)

print("Master application successfully created at index.html!")

# Generate questions.html directory page
cards_html = []
for m in q_metadata:
    q_num = m['q']
    content_search = f"{m['topic']} {m['question']} {m['section']} {m['correct']}".lower()
    card = f'''
    <div class="q-card" data-q="{q_num}" data-content="{content_search}">
      <div class="q-card-top">
        <span class="q-badge">Q{q_num:02d}</span>
        <span class="q-section">{m['section']}</span>
      </div>
      <div class="q-topic">{m['icon']} {m['topic']}</div>
      <div class="q-text"><strong>Question:</strong> {m['question']}</div>
      <div class="q-answer"><strong>Correct Answer / Key Concept:</strong> {m['correct']}</div>
      <div class="q-actions">
        <a href="index.html#q{q_num}" class="btn-action primary">Interactive Master View</a>
        <a href="{m['file']}" target="_blank" class="btn-action secondary">Standalone Chapter Guide</a>
        <a href="{m['pdf']}" target="_blank" class="btn-action pdf">Download PDF Guide</a>
      </div>
    </div>'''
    cards_html.append(card)

questions_catalog_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>All Questions Directory (Q01–Q{len(q_metadata):02d}) | DGMS 2019 Geology Solutions</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    background: #f8fafc;
    color: #0f172a;
    line-height: 1.5;
    padding: 30px 16px;
  }}
  .container {{ max-width: 1040px; margin: 0 auto; }}
  .header {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    color: #fff;
    border-radius: 14px;
    padding: 32px 36px;
    margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  }}
  .badge {{
    display: inline-block;
    background: #e11d48;
    color: #fff;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 4px;
    padding: 3px 10px;
    margin-bottom: 12px;
  }}
  .header h1 {{ font-size: 26px; font-weight: 800; margin-bottom: 8px; }}
  .header p {{ color: #94a3b8; font-size: 14.5px; max-width: 780px; }}
  
  .toolbar {{
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    background: #fff;
    padding: 14px 18px;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}
  .search-input {{
    flex: 1;
    min-width: 240px;
    padding: 10px 14px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.15s;
  }}
  .search-input:focus {{ border-color: #2563eb; ring: 2px solid #bfdbfe; }}
  .btn-all-scroll {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #2563eb;
    color: #fff;
    text-decoration: none;
    font-size: 13.5px;
    font-weight: 600;
    padding: 9px 16px;
    border-radius: 8px;
    transition: background 0.15s;
  }}
  .btn-all-scroll:hover {{ background: #1d4ed8; }}

  .q-grid {{
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}
  .q-card {{
    background: #fff;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    padding: 18px 22px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: transform 0.15s, box-shadow 0.15s;
  }}
  .q-card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }}
  .q-card-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .q-badge {{
    background: #0f172a;
    color: #fff;
    font-family: 'Fira Code', monospace;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 5px;
  }}
  .q-section {{
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    color: #64748b;
    letter-spacing: 0.5px;
  }}
  .q-topic {{
    font-size: 16px;
    font-weight: 700;
    color: #1e293b;
  }}
  .q-text {{
    font-size: 14px;
    color: #334155;
    line-height: 1.5;
  }}
  .q-answer {{
    font-size: 13.5px;
    background: #f0fdf4;
    border-left: 3px solid #16a34a;
    padding: 8px 12px;
    border-radius: 0 6px 6px 0;
    color: #15803d;
  }}
  .q-actions {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 4px;
  }}
  .btn-action {{
    font-size: 12.5px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none;
    transition: all 0.15s;
  }}
  .btn-action.primary {{
    background: #f1f5f9;
    color: #0f172a;
    border: 1px solid #cbd5e1;
  }}
  .btn-action.primary:hover {{ background: #e2e8f0; }}
  .btn-action.secondary {{
    background: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #bfdbfe;
  }}
  .btn-action.secondary:hover {{ background: #dbeafe; }}
  .btn-action.pdf {{
    background: #fef2f2;
    color: #dc2626;
    border: 1px solid #fecaca;
  }}
  .btn-action.pdf:hover {{ background: #fee2e2; }}

  .footer {{
    margin-top: 36px;
    text-align: center;
    font-size: 13px;
    color: #64748b;
  }}
</style>
</head>
<body>
<div class="container">

  <div class="header">
    <div class="badge">DGMS 2019 • Official Syllabus Architecture</div>
    <h1>Comprehensive Questions Directory (Q01–Q{len(q_metadata):02d})</h1>
    <p>Junior Scientific Officer (Geology) Examination 2019 — Complete question catalog, verified answer keys, and direct links to comprehensive chapter modules and textbook-referenced PDF study guides.</p>
  </div>

  <div class="toolbar">
    <input type="text" id="searchInput" class="search-input" placeholder="Search questions, topics, rock types, or concepts..." onkeyup="filterCards()">
    <a href="index.html#all" class="btn-all-scroll">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
      Continuous Scroll: Read All Questions
    </a>
  </div>

  <div class="q-grid" id="qGrid">
    {''.join(cards_html)}
  </div>

  <div class="footer">
    <strong>DGMS 2019 Geology Master Directory · {len(q_metadata)} Comprehensive Chapters</strong><br>
    Hosted on GitHub Pages · Department of Geology & Mines Exam Architecture
  </div>

</div>

<script>
function filterCards() {{
  const query = document.getElementById('searchInput').value.toLowerCase();
  document.querySelectorAll('.q-card').forEach(card => {{
    const text = card.getAttribute('data-content');
    if (text.includes(query)) {{
      card.style.display = 'flex';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}
</script>
</body>
</html>'''

with open("questions.html", "w", encoding="utf-8") as f:
    f.write(questions_catalog_html)

print("Questions directory successfully created at questions.html!")
