#!/usr/bin/env python3
"""
Master Portal Builder for OPSC 2019 Assistant Geologist Paper-II (GGM - 2/2019)
Generates index_2019.html with exact Assam DGMS 2019 Masterclass SPA Architecture
"""

import json
import os
import re
from bs4 import BeautifulSoup

DATA_PATH = "/home/tapaswi/Mines_Geology/Orrisa_geology/data/geology_2019.json"
BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
OUTPUT_INDEX = os.path.join(BASE_DIR, "index_2019.html")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions from {DATA_PATH}")

def get_canonical_discipline(q_num):
    if 1 <= q_num <= 10:
        return "Geomorphology & Quaternary Geology"
    elif 11 <= q_num <= 24:
        return "Volcanology, Weathering & Mass Wasting"
    elif 25 <= q_num <= 40:
        return "Structural Geology & Fault Mechanics"
    elif 41 <= q_num <= 55:
        return "Global Geotectonics & Plate Boundaries"
    elif 56 <= q_num <= 75:
        return "Indian Stratigraphy & Paleontology"
    elif 76 <= q_num <= 95:
        return "Igneous Petrology & Magmatic Systems"
    elif 96 <= q_num <= 110:
        return "Sedimentary Petrology & Carbonates"
    elif 111 <= q_num <= 125:
        return "Metamorphic Petrology & Mineral Equilibria"
    elif 126 <= q_num <= 135:
        return "Economic Geology & Mineral Deposits"
    elif 136 <= q_num <= 150:
        return "Applied Hydrogeology & Remote Sensing"
    return "General Geology"

# Group questions
sections_dict = {}
for q in questions:
    sec = q.get("section") or get_canonical_discipline(q["q"])
    q["canonical_sec"] = sec
    if sec not in sections_dict:
        sections_dict[sec] = []
    sections_dict[sec].append(q)

print(f"Grouped into {len(sections_dict)} canonical disciplines.")

# Sidebar navigation HTML
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
                # Remove standalone back-link
                back_nav = page_div.find("div", class_="back-nav")
                if back_nav:
                    back_nav.decompose()
                inner_html = page_div.decode_contents()
                # Rewrite relative image paths
                inner_html = inner_html.replace('src="../../figures_2019_Q', 'src="figures_2019_Q')
                inner_html = inner_html.replace('src="../figures_2019_Q', 'src="figures_2019_Q')
                inner_html = re.sub(r'<img\s+(?!loading=)', '<img loading="lazy" decoding="async" ', inner_html)
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

print(f"Total embedded image tags across Batch 1: {embedded_images_count}")

# CSS Styles
portal_css = """
  :root {
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
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: var(--font-sans);
    background-color: var(--bg-main);
    color: var(--text-main);
    line-height: 1.6;
    overflow-x: hidden;
  }

  .app-container {
    display: flex;
    min-height: 100vh;
  }

  /* ── SIDEBAR ── */
  .sidebar {
    width: var(--sidebar-width);
    background-color: var(--bg-sidebar);
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
  }

  .sidebar-header {
    padding: 20px 20px 16px 20px;
    border-bottom: 1px solid #1e293b;
    background: #050811;
  }
  .brand-badge {
    display: inline-block;
    background: linear-gradient(135deg, #0284c7, #38bdf8);
    color: #fff;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 8px;
  }
  .brand-title {
    font-size: 18px;
    font-weight: 800;
    color: var(--text-sidebar-bright);
    letter-spacing: -0.3px;
    margin-bottom: 4px;
  }
  .brand-sub {
    font-size: 12px;
    color: var(--text-sidebar);
    margin-bottom: 12px;
  }
  .year-switcher {
    display: flex;
    gap: 6px;
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid #1e293b;
  }
  .year-btn {
    flex: 1;
    text-align: center;
    font-size: 11.5px;
    font-weight: 700;
    padding: 6px 4px;
    border-radius: 5px;
    text-decoration: none;
    transition: all 0.15s ease;
  }
  .year-btn.active {
    background: #0284c7;
    color: #fff;
    box-shadow: 0 2px 6px rgba(2, 132, 199, 0.4);
  }
  .year-btn.inactive {
    background: #1e293b;
    color: #94a3b8;
  }
  .year-btn.inactive:hover {
    background: #334155;
    color: #f8fafc;
  }

  .sidebar-search {
    padding: 12px 16px;
    border-bottom: 1px solid #1e293b;
    background: #0b1120;
  }
  .search-input-wrapper {
    position: relative;
    display: flex;
    align-items: center;
  }
  .search-icon {
    position: absolute;
    left: 10px;
    width: 14px;
    height: 14px;
    color: #64748b;
    pointer-events: none;
  }
  .search-input {
    width: 100%;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 7px 10px 7px 32px;
    font-size: 12.5px;
    color: #f8fafc;
    outline: none;
    transition: all 0.15s ease;
  }
  .search-input:focus {
    border-color: #0284c7;
    background: #0f172a;
    box-shadow: 0 0 0 2px rgba(2, 132, 199, 0.25);
  }

  .sidebar-nav {
    flex: 1;
    overflow-y: auto;
    padding: 12px 10px;
  }
  .sidebar-nav::-webkit-scrollbar { width: 5px; }
  .sidebar-nav::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }

  .nav-section-title {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #64748b;
    padding: 14px 10px 6px 10px;
  }
  .nav-list { list-style: none; margin-bottom: 10px; }
  .nav-item { margin-bottom: 3px; }
  .nav-link {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 8px 10px;
    border-radius: 6px;
    color: var(--text-sidebar);
    text-decoration: none;
    font-size: 12.5px;
    transition: all 0.15s ease;
    border: 1px solid transparent;
  }
  .nav-link:hover {
    background-color: var(--bg-sidebar-hover);
    color: var(--text-sidebar-bright);
  }
  .nav-item.active .nav-link {
    background-color: rgba(2, 132, 199, 0.15);
    color: #38bdf8;
    border-color: rgba(2, 132, 199, 0.3);
    font-weight: 600;
  }
  .nav-badge {
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 700;
    background: #1e293b;
    color: #94a3b8;
    padding: 2px 5px;
    border-radius: 3px;
    margin-top: 2px;
    flex-shrink: 0;
  }
  .nav-item.active .nav-badge {
    background: #0284c7;
    color: #fff;
  }
  .nav-info { flex: 1; min-width: 0; }
  .nav-title {
    font-weight: 600;
    color: #e2e8f0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .nav-preview {
    font-size: 11px;
    color: #64748b;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-top: 2px;
  }

  /* ── MAIN CONTENT AREA ── */
  .main-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
  }

  .top-navbar {
    height: var(--header-height);
    background: var(--bg-surface);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 28px;
    position: sticky;
    top: 0;
    z-index: 40;
    box-shadow: var(--shadow-sm);
  }
  .navbar-left {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .mobile-menu-btn {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    color: var(--text-main);
  }
  .current-q-indicator {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    font-size: 15px;
  }
  .current-badge {
    background: #0284c7;
    color: #fff;
    font-family: var(--font-mono);
    font-size: 11px;
    padding: 2px 7px;
    border-radius: 4px;
  }

  .navbar-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .nav-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 14px;
    font-size: 13px;
    font-weight: 600;
    border-radius: 6px;
    cursor: pointer;
    border: 1px solid var(--border-color);
    background: var(--bg-surface);
    color: var(--text-main);
    transition: all 0.15s ease;
  }
  .nav-btn:hover { background: #f1f5f9; border-color: #cbd5e1; }
  .nav-btn-primary {
    background: #0284c7;
    color: #fff;
    border-color: #0284c7;
  }
  .nav-btn-primary:hover { background: #0369a1; border-color: #0369a1; }

  .content-area {
    padding: 32px 36px 64px 36px;
    max-width: 1020px;
    margin: 0 auto;
    width: 100%;
  }

  .question-module {
    display: none;
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    margin-bottom: 32px;
    box-shadow: var(--shadow-sm);
    overflow: hidden;
    content-visibility: hidden;
  }
  .question-module.visible {
    display: block;
    content-visibility: visible;
  }
  body.view-all .question-module {
    display: block !important;
    content-visibility: auto;
    contain-intrinsic-size: 1px 900px;
  }

  .module-topbar {
    background: #f8fafc;
    border-bottom: 1px solid var(--border-color);
    padding: 12px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .module-breadcrumbs {
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .crumb-sec { color: #0284c7; }
  .crumb-sep { color: #cbd5e1; }
  .crumb-q { color: var(--text-main); font-weight: 700; }

  .btn-action {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    font-weight: 600;
    color: #475569;
    background: #fff;
    border: 1px solid #cbd5e1;
    padding: 4px 10px;
    border-radius: 5px;
    text-decoration: none;
    transition: all 0.15s ease;
  }
  .btn-action:hover {
    background: #f1f5f9;
    color: #0f172a;
    border-color: #94a3b8;
  }

  .module-body { padding: 24px 30px; }

  /* Import Master Standard Card CSS */
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

  @media (max-width: 900px) {
    .sidebar {
      position: fixed;
      left: -100%;
      transition: left 0.3s ease;
    }
    .sidebar.open { left: 0; }
    .mobile-menu-btn { display: block; }
    .content-area { padding: 20px 16px; }
  }
"""

portal_js = """
  let currentQ = 1;
  const totalQ = """ + str(len(questions)) + """;
  let isViewAll = false;

  function selectQuestion(qNum) {
    if (isViewAll) {
      const el = document.getElementById('q' + qNum);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
        highlightNav(qNum);
      }
      return;
    }
    currentQ = qNum;
    document.querySelectorAll('.question-module').forEach(el => el.classList.remove('visible'));
    const target = document.getElementById('q' + qNum);
    if (target) {
      target.classList.add('visible');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    highlightNav(qNum);
    updateNavbarIndicator(qNum);
  }

  function highlightNav(qNum) {
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    const navItem = document.querySelector(`.nav-item[data-q="${qNum}"]`);
    if (navItem) {
      navItem.classList.add('active');
      navItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  function updateNavbarIndicator(qNum) {
    const badge = document.getElementById('currentBadge');
    const title = document.getElementById('currentTitle');
    const module = document.getElementById('q' + qNum);
    if (badge) badge.textContent = 'Q' + String(qNum).padStart(3, '0');
    if (title && module) title.textContent = module.getAttribute('data-topic');
  }

  function nextQuestion() {
    if (currentQ < totalQ) selectQuestion(currentQ + 1);
  }

  function prevQuestion() {
    if (currentQ > 1) selectQuestion(currentQ - 1);
  }

  function toggleViewAll() {
    isViewAll = !isViewAll;
    const btn = document.getElementById('viewAllToggle');
    if (isViewAll) {
      document.querySelectorAll('.question-module').forEach(el => el.classList.add('visible'));
      btn.textContent = 'Single Question View';
      btn.classList.remove('nav-btn-primary');
    } else {
      btn.textContent = 'View All Questions';
      btn.classList.add('nav-btn-primary');
      selectQuestion(currentQ);
    }
  }

  function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) sidebar.classList.toggle('open');
  }

  function filterQuestions(query) {
    query = query.toLowerCase().trim();
    document.querySelectorAll('.nav-item').forEach(item => {
      const title = item.querySelector('.nav-title').textContent.toLowerCase();
      const preview = item.querySelector('.nav-preview').textContent.toLowerCase();
      const badge = item.querySelector('.nav-badge').textContent.toLowerCase();
      if (!query || title.includes(query) || preview.includes(query) || badge.includes(query)) {
        item.style.display = '';
      } else {
        item.style.display = 'none';
      }
    });
  }

  // Keyboard Navigation
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') return;
    if (e.key === 'ArrowRight') nextQuestion();
    if (e.key === 'ArrowLeft') prevQuestion();
  });

  // Handle hash on load
  window.addEventListener('DOMContentLoaded', () => {
    const hash = window.location.hash;
    let initialQ = 1;
    if (hash && hash.startsWith('#q')) {
      const parsed = parseInt(hash.replace('#q', ''), 10);
      if (!isNaN(parsed) && parsed >= 1 && parsed <= totalQ) initialQ = parsed;
    }
    selectQuestion(initialQ);
  });
"""

full_portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Odisha Mining & Geology Masterclass Portal | OPSC 2019 Solutions</title>
<meta name="description" content="Authoritative, university textbook-grounded solutions, derivations, and high-yield concept guides for the Odisha OPSC 2019 Assistant Geologist Paper-II Examination (GGM - 2/2019).">

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
{portal_css}
</style>
</head>
<body>

<div class="app-container">

  <!-- ── SIDEBAR NAVIGATION ── -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <span class="brand-badge">OPSC 2019 · Active Phase</span>
      <h1 class="brand-title">Odisha Geology Masterclass</h1>
      <div class="brand-sub">Paper-II (GGM - 2/2019) · Complete Solutions</div>
      
      <!-- Multi-Year Switcher -->
      <div class="year-switcher">
        <a href="index.html" class="year-btn inactive" title="Open 2021 Portal (150/150 Questions Live)">2021 Exam (150 Live)</a>
        <a href="index_2019.html" class="year-btn active" title="Current Portal: 2019 Exam">2019 Exam (Batch 1)</a>
      </div>
    </div>

    <div class="sidebar-search">
      <div class="search-input-wrapper">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" class="search-input" placeholder="Search 2019 questions, topics, formulas..." oninput="filterQuestions(this.value)">
      </div>
    </div>

    <nav class="sidebar-nav">
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
          <span id="currentTitle">Bajada Geomorphology</span>
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
{portal_js}
</script>

</body>
</html>
"""

with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
    f.write(full_portal_html)

print(f"Generated {OUTPUT_INDEX} successfully ({len(full_portal_html)} bytes).")
