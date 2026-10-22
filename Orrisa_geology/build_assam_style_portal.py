#!/usr/bin/env python3
import json
import os
import re
from bs4 import BeautifulSoup

DATA_PATH = "/home/tapaswi/Mines_Geology/Orrisa_geology/data/geology_2021.json"
BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
OUTPUT_INDEX = os.path.join(BASE_DIR, "index.html")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions from {DATA_PATH}")

def get_canonical_discipline(q_num):
    if 1 <= q_num <= 10:
        return "Geomorphology & Quaternary Geology"
    elif 11 <= q_num <= 20:
        return "Remote Sensing & Photogrammetry"
    elif 21 <= q_num <= 35:
        return "Structural Geology & Fault Mechanics"
    elif 36 <= q_num <= 50:
        return "Global Geotectonics & Paleontology"
    elif 51 <= q_num <= 75:
        return "Indian Stratigraphy & Biostratigraphy"
    elif 76 <= q_num <= 90:
        return "Igneous Petrology & Magmatic Systems"
    elif 91 <= q_num <= 105:
        return "Sedimentary Petrology & Carbonates"
    elif 106 <= q_num <= 120:
        return "Metamorphic Petrology & Mineral Equilibria"
    elif 121 <= q_num <= 130:
        return "Rock Mechanics & Engineering Geology"
    elif 131 <= q_num <= 150:
        return "GIS, Spatial Analysis & Hydrogeology"
    return "General Geology"

# Build Section Mapping
sections_dict = {}
for q in questions:
    sec = get_canonical_discipline(q["q"])
    q["canonical_sec"] = sec
    if sec not in sections_dict:
        sections_dict[sec] = []
    sections_dict[sec].append(q)

print(f"Grouped into {len(sections_dict)} canonical syllabus disciplines.")

# Build Sidebar Navigation HTML
sidebar_nav_html = []
for sec_name, q_list in sections_dict.items():
    sidebar_nav_html.append(f'<div class="nav-section-title">{sec_name}</div>')
    sidebar_nav_html.append('<ul class="nav-list">')
    for q in q_list:
        q_num = q["q"]
        topic = q.get("topic", f"Question {q_num}")
        preview = q.get("question", "")[:85] + "..."
        icon = q.get("icon", "📘")
        sidebar_nav_html.append(f'''
        <li class="nav-item" data-q="{q_num}">
          <a href="#q{q_num}" class="nav-link" onclick="selectQuestion({q_num}); return false;">
            <span class="nav-badge">Q{q_num:03d}</span>
            <div class="nav-info">
              <div class="nav-title">{icon} {topic}</div>
              <div class="nav-preview">{preview}</div>
            </div>
          </a>
        </li>
        ''')
    sidebar_nav_html.append('</ul>')

# Build Modules for Main Content Area
modules_html = []
embedded_images_count = 0

for q in questions:
    q_num = q["q"]
    sec = q["canonical_sec"]
    topic = q.get("topic", f"Question {q_num}")
    html_file = q.get("file_html", "")
    full_html_path = os.path.join(BASE_DIR, html_file)
    
    body_content = ""
    if os.path.exists(full_html_path):
        with open(full_html_path, "r", encoding="utf-8") as hf:
            soup = BeautifulSoup(hf.read(), "html.parser")
            page_div = soup.find("div", class_="page") or soup.body
            if page_div:
                # Remove back-link
                back_nav = page_div.find("div", class_="back-nav")
                if back_nav:
                    back_nav.decompose()
                # Fix relative paths from ../../figures_Q to figures_Q
                inner_html = page_div.decode_contents()
                inner_html = inner_html.replace('src="../../figures_Q', 'src="figures_Q')
                inner_html = inner_html.replace('src="../figures_Q', 'src="figures_Q')
                embedded_images_count += len(re.findall(r'<img\s+[^>]*src=[\"\']([^\"\']+)[\"\']', inner_html))
                body_content = inner_html
    
    if not body_content:
        body_content = f"<p>Guide content for Question {q_num} is being compiled.</p>"
        
    module_article = f'''
    <article class="question-module" id="q{q_num}" data-q="{q_num}" data-section="{sec}" data-topic="{topic}">
      <div class="module-topbar">
        <div class="module-breadcrumbs">
          <span class="crumb-sec">{sec}</span>
          <span class="crumb-sep">/</span>
          <span class="crumb-q">Question {q_num:03d}</span>
        </div>
        <div class="module-actions">
          <a href="{html_file}" target="_blank" class="btn-action" title="Open standalone HTML page">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            Standalone View
          </a>
        </div>
      </div>
      <div class="module-body">
        {body_content}
      </div>
    </article>
    '''
    modules_html.append(module_article)

print(f"Total embedded image tags across all 150 questions: {embedded_images_count}")

# Master Template (Exact DGMS 2019 Assam Portal Architecture)
portal_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Odisha Mining & Geology Masterclass Portal | OPSC 2021 Solutions</title>
<meta name="description" content="Authoritative, university textbook-grounded solutions, derivations, and high-yield concept guides for all 150 questions of the Odisha OPSC 2021 Geology Paper-II Examination.">

<!-- Fonts & MathJax -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
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
    --bg-sidebar: #090d16;
    --bg-sidebar-hover: #1e293b;
    --bg-sidebar-active: #0284c7;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --text-sidebar: #94a3b8;
    --text-sidebar-bright: #f8fafc;
    --border-color: #e2e8f0;
    --primary: #0284c7;
    --primary-dark: #0369a1;
    --accent: #10b981;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'Fira Code', Consolas, monospace;
    --sidebar-width: 360px;
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
    background: #050811;
  }}
  .brand-badge {{
    display: inline-block;
    background: linear-gradient(135deg, #0284c7, #38bdf8);
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
    font-size: 15.5px;
    font-weight: 800;
    color: #fff;
    line-height: 1.3;
  }}
  .brand-sub {{
    font-size: 11.5px;
    color: #94a3b8;
    margin-top: 4px;
  }}
  .brand-nav-links {{
    margin-top: 10px;
    display: flex;
    gap: 6px;
  }}
  .brand-nav-btn {{
    flex: 1;
    text-align: center;
    background: rgba(255, 255, 255, 0.08);
    color: #cbd5e1;
    font-size: 10.5px;
    font-weight: 600;
    padding: 4px 6px;
    border-radius: 4px;
    text-decoration: none;
    border: 1px solid rgba(255, 255, 255, 0.15);
    transition: all 0.15s;
  }}
  .brand-nav-btn:hover {{
    background: #0284c7;
    color: #fff;
    border-color: #38bdf8;
  }}

  .sidebar-search {{
    padding: 12px 16px;
    border-bottom: 1px solid #1e293b;
    background: #090d16;
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
    color: #38bdf8;
    padding: 14px 10px 6px 10px;
    margin-top: 4px;
    border-top: 1px solid rgba(255,255,255,0.05);
  }}
  .nav-section-title:first-child {{ border-top: none; }}
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
    box-shadow: 0 2px 6px rgba(2,132,199,0.35);
  }}
  .nav-badge {{
    background: #1e293b;
    color: #38bdf8;
    font-size: 10.5px;
    font-weight: 700;
    font-family: var(--font-mono);
    padding: 2px 6px;
    border-radius: 4px;
    flex-shrink: 0;
    margin-top: 1px;
  }}
  .nav-item.active .nav-badge {{
    background: rgba(255,255,255,0.25);
    color: #fff;
  }}
  .nav-info {{ flex: 1; min-width: 0; }}
  .nav-title {{
    font-size: 12.5px;
    font-weight: 600;
    line-height: 1.3;
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
  .nav-item.active .nav-preview {{ color: #e0f2fe; }}

  /* ── Main Content Area ── */
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
    padding: 0 24px;
    box-shadow: var(--shadow-sm);
  }}
  .navbar-left {{
    display: flex;
    align-items: center;
    gap: 16px;
    min-width: 0;
  }}
  .mobile-menu-btn {{
    display: none;
    background: transparent;
    border: none;
    color: var(--text-main);
    cursor: pointer;
  }}
  .current-q-indicator {{
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .current-badge {{
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    font-family: var(--font-mono);
    padding: 3px 8px;
    border-radius: 4px;
  }}
  .navbar-actions {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }}
  .nav-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #fff;
    border: 1px solid var(--border-color);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-main);
    cursor: pointer;
    transition: all 0.15s;
  }}
  .nav-btn:hover {{ background: #f8fafc; border-color: #cbd5e1; }}
  .nav-btn-primary {{
    background: #0284c7;
    color: #fff;
    border-color: #0284c7;
  }}
  .nav-btn-primary:hover {{ background: #0369a1; }}

  /* Content Body */
  .content-area {{
    flex: 1;
    padding: 32px 24px 60px 24px;
    max-width: 1020px;
    margin: 0 auto;
    width: 100%;
  }}

  .question-module {{
    display: none;
  }}
  .question-module.active {{
    display: block;
    animation: fadeIn 0.15s ease-in-out;
  }}
  body.view-all .question-module {{
    display: block !important;
    border-bottom: 2px solid #e2e8f0;
    margin-bottom: 50px;
    padding-bottom: 50px;
  }}

  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(4px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  .module-topbar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-color);
  }}
  .module-breadcrumbs {{
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-muted);
  }}
  .crumb-sec {{ color: #0284c7; }}
  .crumb-sep {{ color: #94a3b8; }}
  .crumb-q {{ color: var(--text-main); }}

  .module-actions {{
    display: flex;
    gap: 8px;
  }}
  .btn-action {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    text-decoration: none;
    background: #fff;
    color: #0284c7;
    border: 1px solid #bae6fd;
    transition: all 0.15s;
  }}
  .btn-action:hover {{ background: #f0f9ff; }}

  /* Content Cards Inside Modules */
  .header {{
    background: linear-gradient(135deg, #091e3a 0%, #0f2b4c 50%, #1e3a8a 100%);
    color: #fff;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 22px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.1);
  }}
  .header .badge {{
    display: inline-block;
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 4px;
    padding: 3px 8px;
    margin-bottom: 8px;
  }}
  .header h1 {{ font-size: 21px; font-weight: 800; line-height: 1.35; }}
  .header .meta {{ font-size: 13px; color: #cbd5e1; margin-top: 8px; line-height: 1.5; }}

  .part-banner {{
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    color: #fff;
    border-radius: 8px;
    padding: 14px 20px;
    margin: 26px 0 18px 0;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 2px 8px rgba(37, 99, 235, 0.2);
  }}
  .part-banner.green {{
    background: linear-gradient(135deg, #065f46 0%, #059669 100%);
    box-shadow: 0 2px 8px rgba(5, 150, 105, 0.2);
  }}
  .part-banner.purple {{
    background: linear-gradient(135deg, #581c87 0%, #7c3aed 100%);
    box-shadow: 0 2px 8px rgba(124, 58, 237, 0.2);
  }}
  .part-num {{
    font-size: 24px;
    font-weight: 800;
    opacity: 0.9;
    border-right: 2px solid rgba(255,255,255,0.3);
    padding-right: 14px;
    line-height: 1;
    font-family: var(--font-mono);
  }}
  .part-title {{ font-size: 16.5px; font-weight: 700; letter-spacing: 0.3px; }}
  .part-sub {{ font-size: 12px; opacity: 0.9; margin-top: 2px; }}

  .card {{
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    margin-bottom: 22px;
    overflow: hidden;
    border: 1px solid var(--border-color);
  }}
  .card-header {{
    padding: 12px 20px;
    font-size: 13.5px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #fff;
  }}
  .card-body {{ padding: 20px 24px; font-size: 14.5px; color: #334155; line-height: 1.65; }}
  .bg-blue    {{ background: #1d4ed8; }}
  .bg-indigo  {{ background: #4338ca; }}
  .bg-emerald {{ background: #047857; }}
  .bg-purple  {{ background: #6d28d9; }}
  .bg-amber   {{ background: #b45309; }}
  .bg-slate   {{ background: #334155; }}

  .quote-box {{
    background: #eff6ff;
    border-left: 5px solid #2563eb;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin: 16px 0;
    font-style: italic;
    color: #1e3a8a;
    font-size: 13.5px;
    line-height: 1.6;
  }}
  .quote-box.bangar {{
    background: #f0fdf4;
    border-left-color: #059669;
    color: #064e3b;
  }}
  .quote-ref {{
    display: block;
    font-size: 12px;
    font-style: normal;
    font-weight: 700;
    margin-top: 8px;
    letter-spacing: 0.2px;
  }}
  .quote-box.bangar .quote-ref {{ color: #047857; }}

  .formula-card {{
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: #f8fafc;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 16px 0;
    border-left: 4px solid #38bdf8;
  }}
  .formula-title {{
    font-size: 12px;
    font-weight: 700;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }}

  .tb-figure {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 14px;
    margin: 20px 0;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }}
  .tb-figure img {{
    max-width: 100%;
    max-height: 480px;
    height: auto;
    border-radius: 6px;
    display: block;
    margin: 0 auto 12px auto;
  }}
  .tb-figure figcaption, .tb-caption {{
    font-size: 13px;
    color: #475569;
    line-height: 1.5;
    text-align: justify;
    padding: 10px 14px;
    background: #f8fafc;
    border-radius: 6px;
    border-left: 3px solid #0284c7;
    margin-top: 10px;
  }}
  .tb-figure figcaption strong, .tb-caption strong {{ color: #0f172a; font-weight: 700; }}

  .question-box, .q-box {{
    background: #eff6ff;
    border: 2px solid #3b82f6;
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 20px;
  }}
  .q-num {{
    font-size: 12.5px;
    font-weight: 800;
    color: #1d4ed8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
  }}
  .q-stmt {{ font-size: 15.5px; font-weight: 700; color: #0f172a; margin-bottom: 12px; line-height: 1.5; }}
  .raw-options, .options-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 14px;
  }}
  .raw-opt, .opt-item {{
    background: #fff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 13.5px;
  }}
  .raw-opt.correct, .opt-item.correct {{
    background: #f0fdf4;
    border-color: #10b981;
    color: #065f46;
    font-weight: 700;
  }}

  .answer-banner, .verified-box {{
    background: linear-gradient(90deg, #059669 0%, #10b981 100%);
    color: #fff;
    border-radius: 10px;
    padding: 16px 22px;
    margin-bottom: 22px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 3px 10px rgba(16, 185, 129, 0.2);
  }}
  .answer-banner .tick {{ font-size: 32px; line-height: 1; font-weight: bold; }}
  .answer-banner .text {{ font-size: 17.5px; font-weight: 700; }}
  .answer-banner .sub {{ font-size: 13.5px; opacity: 0.95; margin-top: 4px; line-height: 1.45; }}

  .option {{
    border-radius: 8px;
    margin-bottom: 14px;
    overflow: hidden;
    border: 2px solid transparent;
  }}
  .option.correct {{ border-color: #10b981; }}
  .option.wrong   {{ border-color: #f43f5e; }}
  .option-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    font-weight: 700;
    font-size: 14px;
  }}
  .option.correct .option-header {{ background: #d1fae5; color: #065f46; }}
  .option.wrong   .option-header {{ background: #ffe4e6; color: #9f1239; }}
  .option-body {{ padding: 12px 16px 14px; background: #fafafa; font-size: 13.5px; color: #334155; line-height: 1.6; }}
  .tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    border-radius: 4px;
    padding: 2px 8px;
    margin-left: auto;
    text-transform: uppercase;
  }}
  .tag.correct {{ background: #059669; color: #fff; }}
  .tag.wrong   {{ background: #e11d48; color: #fff; }}

  table, .spec-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    text-align: left;
    margin: 14px 0;
  }}
  th, .spec-table th {{
    background: #0f172a;
    color: #fff;
    padding: 10px 12px;
    font-weight: 600;
  }}
  td, .spec-table td {{
    padding: 9px 12px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
  }}
  tr:nth-child(even) td, .spec-table tr:nth-child(even) td {{ background: #f8fafc; }}

  .pq-list {{ list-style: none; padding: 0; }}
  .pq-list li {{
    background: #fffbeb;
    border: 1px solid #fef3c7;
    border-left: 4px solid #d97706;
    border-radius: 6px;
    padding: 13px 18px;
    margin-bottom: 14px;
    font-size: 13.5px;
  }}
  .pq-list li strong {{ color: #92400e; font-size: 14px; }}
  .pq-ans {{
    margin-top: 6px;
    color: #065f46;
    font-weight: 700;
  }}
  .pq-exp {{
    margin-top: 4px;
    color: #475569;
    font-size: 13px;
    line-height: 1.55;
  }}

  .content-card {{
    background: #fff;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    padding: 22px 26px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    margin-bottom: 20px;
  }}
  .content-card h3 {{ font-size: 16px; font-weight: 700; color: #1e293b; margin: 16px 0 8px 0; }}
  .content-card p {{ margin-bottom: 12px; font-size: 14.5px; color: #334155; line-height: 1.65; }}
  .content-card ul {{ margin: 10px 0 14px 22px; font-size: 14.5px; color: #334155; }}
  .content-card li {{ margin-bottom: 6px; }}

  .qa-card {{
    background: #faf5ff;
    border: 1px solid #e9d5ff;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 14px;
  }}
  .q-title {{ font-size: 14.5px; font-weight: 700; color: #6b21a8; margin-bottom: 6px; }}
  .a-box {{
    background: #fff;
    border-left: 3px solid #7c3aed;
    padding: 10px 14px;
    border-radius: 0 6px 6px 0;
    margin-top: 8px;
    font-size: 13.5px;
  }}

  @media (max-width: 900px) {{
    .sidebar {{ position: fixed; left: -100%; transition: left 0.2s ease; }}
    .sidebar.open {{ left: 0; }}
    .mobile-menu-btn {{ display: block; }}
    .raw-options, .options-grid {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>

<div class="app-container">

  <!-- ── SIDEBAR NAVIGATION ── -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <span class="brand-badge">OPSC 2021 · Complete Suite</span>
      <h1 class="brand-title">Odisha Geology Masterclass</h1>
      <div class="brand-sub">150 Comprehensive Textbook Chapters</div>
      <div class="brand-nav-links">
        <a href="../index.html" class="brand-nav-btn">← Assam DGMS Portal</a>
        <a href="https://github.com/tapaswidata-a11y/DMG_Geology_Solutions_2019" target="_blank" class="brand-nav-btn">GitHub Repo ↗</a>
      </div>
    </div>

    <div class="sidebar-search">
      <div class="search-box">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="searchInput" placeholder="Search questions, rocks, topics..." onkeyup="filterQuestions()">
      </div>
    </div>

    <nav class="sidebar-nav" id="sidebarNav">
      {''.join(sidebar_nav_html)}
    </nav>
  </aside>

  <!-- ── MAIN CONTENT AREA ── -->
  <div class="main-wrapper">
    <!-- Top Navbar -->
    <header class="top-navbar">
      <div class="navbar-left">
        <button class="mobile-menu-btn" onclick="toggleSidebar()" aria-label="Toggle menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
        <div class="current-q-indicator">
          <span class="current-badge" id="currentBadge">Q001</span>
          <span id="currentTitle">Slope Stability & Landslide Shear Plane Mechanics</span>
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

    <!-- Master Modules Container -->
    <main class="content-area" id="contentArea">
      {''.join(modules_html)}
    </main>
  </div>

</div>

<script>
  let currentQ = 1;
  const totalQ = {len(questions)};
  let isViewAll = false;

  const qTopics = {{
    {', '.join([f'{q["q"]}: "{q.get("topic", "").replace(chr(34), "")}"' for q in questions])}
  }};

  function selectQuestion(qNum) {{
    currentQ = qNum;

    // Update active state in sidebar
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    const activeItem = document.querySelector(`.nav-item[data-q="${{qNum}}"]`);
    if (activeItem) {{
      activeItem.classList.add('active');
      activeItem.scrollIntoView({{ block: 'nearest' }});
    }}

    // Update main view
    document.querySelectorAll('.question-module').forEach(el => el.classList.remove('active'));
    const activeModule = document.getElementById(`q${{qNum}}`);
    if (activeModule) {{
      activeModule.classList.add('active');
    }}

    // Update navbar badge and title
    const padQ = String(qNum).padStart(3, '0');
    document.getElementById('currentBadge').textContent = `Q${{padQ}}`;
    document.getElementById('currentTitle').textContent = qTopics[qNum] || `Question ${{qNum}}`;

    // Update URL hash without jumping
    history.replaceState(null, null, `#q${{qNum}}`);

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

  // Handle URL hash on load
  function initFromHash() {{
    const hash = window.location.hash;
    const match = hash.match(/#q(\\d+)/);
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
</html>'''

with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
    f.write(portal_html)

print(f"Successfully created Assam-identical Master Portal at {OUTPUT_INDEX}!")
