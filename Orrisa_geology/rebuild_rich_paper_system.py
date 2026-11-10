#!/usr/bin/env python3
"""
Rebuild Rich Masterclass System for:
1. Mining Officer (Applied Geology) 2019
2. Mining Officer (Applied Geology) 2021
3. Petrologist 2021

Executes:
- Synthesis of deep, rich solutions for all 150 questions per paper (450 total)
- Generates 150 standalone HTML guides in solutions/<paper>/ with full Part I, Part II, Part III
- Compiles the full SPA portal (index_<paper>.html) with sidebar, search, and embedded modules
- Updates data/<paper>.json
"""

import os
import re
import json
from bs4 import BeautifulSoup
import builder_engine as eng
import synthesize_solution as syn

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
DATA_DIR = os.path.join(BASE_DIR, "data")

PAPER_CONFIGS = [
    {
        "id": "mining_applied_2019",
        "name": "Mining Officer (Applied Geology) Paper-II (2019)",
        "code": "GGM - 4/2019",
        "portal_file": "index_mining_applied_2019.html",
        "sol_dir": os.path.join(BASE_DIR, "solutions", "mining_applied_2019"),
        "brand_title": "Applied Geology Paper-II (2019)",
        "brand_badge": "OPSC Mining Officer",
        "brand_subtitle": "GGM - 4/2019 • 150 Solved Modules",
        "navbar_title": "OPSC Mining Officer (Applied Geology) 2019 • 150 Question Masterclass",
        "back_link": "../../index_mining_applied_2019.html",
        "back_label": "Back to Mining Officer 2019 Master Portal"
    },
    {
        "id": "mining_applied_2021",
        "name": "Mining Officer (Applied Geology) Paper-II (2021)",
        "code": "GPGM - 5/20",
        "portal_file": "index_mining_applied_2021.html",
        "sol_dir": os.path.join(BASE_DIR, "solutions", "mining_applied_2021"),
        "brand_title": "Applied Geology Paper-II (2021)",
        "brand_badge": "OPSC Mining Officer",
        "brand_subtitle": "GPGM - 5/20 • 150 Solved Modules",
        "navbar_title": "OPSC Mining Officer (Applied Geology) 2021 • 150 Question Masterclass",
        "back_link": "../../index_mining_applied_2021.html",
        "back_label": "Back to Mining Officer 2021 Master Portal"
    },
    {
        "id": "petrologist_2021",
        "name": "Petrologist Paper-II (2021)",
        "code": "GPGM - 3/20",
        "portal_file": "index_petrologist_2021.html",
        "sol_dir": os.path.join(BASE_DIR, "solutions", "petrologist_2021"),
        "brand_title": "Petrologist Paper-II (2021)",
        "brand_badge": "OPSC Petrologist",
        "brand_subtitle": "GPGM - 3/20 • 150 Solved Modules",
        "navbar_title": "OPSC Petrologist 2021 • 150 Question Masterclass",
        "back_link": "../../index_petrologist_2021.html",
        "back_label": "Back to Petrologist 2021 Master Portal"
    }
]

PORTAL_JS = """
  let activeQuestion = 1;
  const totalQuestions = 150;

  function toggleSidebar(forceState) {
    const sidebar = document.querySelector('.sidebar');
    if (forceState !== undefined) {
      if (forceState) sidebar.classList.add('open');
      else sidebar.classList.remove('open');
    } else {
      sidebar.classList.toggle('open');
    }
  }

  function filterQuestions() {
    const query = document.getElementById('searchInput').value.toLowerCase().trim();
    const navItems = document.querySelectorAll('.nav-item');
    const modules = document.querySelectorAll('.question-module');

    navItems.forEach(item => {
      const text = item.textContent.toLowerCase();
      if (!query || text.includes(query)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });

    if (query) {
      modules.forEach(m => {
        const text = m.textContent.toLowerCase();
        if (text.includes(query)) {
          m.style.display = 'block';
        } else {
          m.style.display = 'none';
        }
      });
    } else {
      showQuestion(activeQuestion);
    }
  }

  function filterBySection(secName, btn) {
    document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');

    const navItems = document.querySelectorAll('.nav-item');
    const modules = document.querySelectorAll('.question-module');

    if (secName === 'All') {
      navItems.forEach(i => i.style.display = 'block');
      showQuestion(activeQuestion);
      return;
    }

    let firstMatch = null;
    modules.forEach(m => {
      const match = m.getAttribute('data-section') === secName;
      if (match) {
        m.style.display = 'block';
        if (!firstMatch) firstMatch = parseInt(m.getAttribute('data-q'));
      } else {
        m.style.display = 'none';
      }
    });

    navItems.forEach(item => {
      const qNum = parseInt(item.getAttribute('data-q'));
      const mod = document.getElementById('q' + qNum);
      if (mod && mod.getAttribute('data-section') === secName) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });

    if (firstMatch) {
      selectQuestion(firstMatch);
    }
  }

  function selectQuestion(qNum) {
    activeQuestion = qNum;
    showQuestion(qNum);
    window.location.hash = 'q' + qNum;
    if (window.innerWidth <= 992) {
      toggleSidebar(false);
    }
  }

  function showQuestion(qNum) {
    const modules = document.querySelectorAll('.question-module');
    const navItems = document.querySelectorAll('.nav-item');

    modules.forEach(m => {
      if (parseInt(m.getAttribute('data-q')) === qNum) {
        m.style.display = 'block';
        m.scrollIntoView({ behavior: 'smooth', block: 'start' });
      } else {
        m.style.display = 'none';
      }
    });

    navItems.forEach(item => {
      if (parseInt(item.getAttribute('data-q')) === qNum) {
        item.classList.add('active');
        item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      } else {
        item.classList.remove('active');
      }
    });
  }

  function navigateQuestion(delta) {
    let nextQ = activeQuestion + delta;
    if (nextQ < 1) nextQ = totalQuestions;
    if (nextQ > totalQuestions) nextQ = 1;
    selectQuestion(nextQ);
  }

  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') return;
    if (e.key === 'ArrowRight' || e.key === 'j') navigateQuestion(1);
    if (e.key === 'ArrowLeft' || e.key === 'k') navigateQuestion(-1);
  });

  window.addEventListener('DOMContentLoaded', () => {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#q')) {
      const q = parseInt(hash.replace('#q', ''));
      if (q >= 1 && q <= totalQuestions) {
        activeQuestion = q;
      }
    }
    showQuestion(activeQuestion);
  });
"""

CSS_STYLES_PORTAL = """
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    background: #0f172a;
    color: #f8fafc;
    height: 100vh;
    overflow: hidden;
  }
  .app-container {
    display: flex;
    height: 100vh;
    width: 100vw;
  }

  /* Left Sidebar */
  .sidebar {
    width: 360px;
    background: #1e293b;
    border-right: 1px solid #334155;
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    transition: transform 0.25s ease;
    z-index: 50;
  }
  .sidebar-header {
    padding: 18px 20px 14px;
    border-bottom: 1px solid #334155;
  }
  .sidebar-header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 12px;
  }
  .brand-badge {
    background: #0284c7;
    color: #fff;
    font-size: 10.5px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }
  .brand-title {
    font-size: 16px;
    font-weight: 800;
    color: #fff;
    margin-top: 6px;
  }
  .brand-subtitle {
    font-size: 12px;
    color: #94a3b8;
    margin-top: 2px;
  }
  .sidebar-close-btn {
    display: none;
    background: transparent;
    border: none;
    color: #94a3b8;
    font-size: 18px;
    cursor: pointer;
  }

  /* Year Switcher */
  .year-switcher {
    display: flex;
    gap: 4px;
    background: #0f172a;
    padding: 4px;
    border-radius: 6px;
    margin-top: 8px;
    flex-wrap: wrap;
  }
  .year-btn {
    flex: 1 1 30%;
    text-align: center;
    padding: 5px 6px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
    text-decoration: none;
    color: #94a3b8;
    transition: all 0.15s;
    white-space: nowrap;
  }
  .year-btn:hover { color: #f8fafc; background: rgba(255,255,255,0.05); }
  .year-btn.active { background: #0284c7; color: #fff; font-weight: 700; }

  /* Search */
  .sidebar-search {
    padding: 12px 16px;
    border-bottom: 1px solid #334155;
  }
  .search-wrapper {
    position: relative;
    display: flex;
    align-items: center;
  }
  .search-icon {
    position: absolute;
    left: 12px;
    font-size: 13px;
    color: #64748b;
  }
  .search-input {
    width: 100%;
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 8px 12px 8px 34px;
    color: #f8fafc;
    font-size: 13px;
    outline: none;
    transition: border-color 0.2s;
  }
  .search-input:focus { border-color: #0284c7; }

  /* Nav list */
  .sidebar-nav {
    flex: 1;
    overflow-y: auto;
    padding: 8px 0;
  }
  .nav-section-title {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #64748b;
    padding: 12px 18px 4px;
    letter-spacing: 0.6px;
  }
  .nav-list { list-style: none; }
  .nav-item {
    border-bottom: 1px solid rgba(51, 65, 85, 0.4);
  }
  .nav-link {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 10px 16px;
    text-decoration: none;
    color: #cbd5e1;
    transition: all 0.15s;
  }
  .nav-link:hover { background: #334155; color: #fff; }
  .nav-item.active .nav-link {
    background: #0284c7;
    color: #fff;
  }
  .nav-badge {
    background: rgba(0,0,0,0.25);
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    font-family: 'Fira Code', monospace;
    flex-shrink: 0;
  }
  .nav-item.active .nav-badge { background: rgba(255,255,255,0.25); }
  .nav-info { flex: 1; min-width: 0; }
  .nav-title {
    font-size: 12.5px;
    font-weight: 600;
    line-height: 1.35;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .nav-preview {
    font-size: 11.5px;
    color: #94a3b8;
    margin-top: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .nav-item.active .nav-preview { color: #e0f2fe; }

  /* Main Content Area */
  .main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
    background: #f1f5f9;
    color: #0f172a;
  }

  .top-navbar {
    background: #fff;
    border-bottom: 1px solid #cbd5e1;
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
  }
  .navbar-left { display: flex; align-items: center; gap: 14px; }
  .btn-sidebar-toggle {
    display: none;
    align-items: center;
    gap: 6px;
    background: #0f172a;
    color: #fff;
    border: none;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
  }
  .navbar-title { font-size: 14.5px; font-weight: 700; color: #0f172a; }
  .navbar-actions { display: flex; align-items: center; gap: 10px; }
  .btn-action {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #f1f5f9;
    color: #334155;
    border: 1px solid #cbd5e1;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.15s;
  }
  .btn-action:hover { background: #e2e8f0; color: #0f172a; }

  /* Filter pills bar */
  .filter-bar {
    background: #fff;
    border-bottom: 1px solid #cbd5e1;
    padding: 8px 24px;
    display: flex;
    gap: 8px;
    overflow-x: auto;
    flex-shrink: 0;
  }
  .filter-pill {
    background: #f1f5f9;
    color: #475569;
    border: 1px solid #cbd5e1;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.15s;
  }
  .filter-pill:hover { background: #e2e8f0; color: #0f172a; }
  .filter-pill.active { background: #0284c7; color: #fff; border-color: #0284c7; }

  /* Content area scrollable */
  .content-area {
    flex: 1;
    overflow-y: auto;
    padding: 24px 32px 60px;
  }

  .question-module {
    max-width: 960px;
    margin: 0 auto;
    display: none;
  }
  .module-topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #fff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 10px 18px;
    margin-bottom: 16px;
  }
  .module-breadcrumbs {
    font-size: 13px;
    font-weight: 600;
    color: #64748b;
  }
  .crumb-sec { color: #0284c7; }
  .crumb-sep { margin: 0 6px; color: #cbd5e1; }
  .crumb-q { color: #0f172a; font-weight: 700; }

  @media (max-width: 992px) {
    .sidebar {
      position: fixed;
      left: 0;
      top: 0;
      bottom: 0;
      transform: translateX(-100%);
    }
    .sidebar.open { transform: translateX(0); }
    .sidebar-close-btn { display: block; }
    .btn-sidebar-toggle { display: inline-flex; }
    .content-area { padding: 16px 16px 40px; }
  }
"""

def process_paper(cfg):
    print(f"\n==========================================")
    print(f"Processing: {cfg['name']} [{cfg['code']}]")
    print(f"==========================================")
    
    json_path = os.path.join(DATA_DIR, f"{cfg['id']}.json")
    with open(json_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)
    print(f"Loaded {len(dataset)} questions from {json_path}")
    
    os.makedirs(cfg["sol_dir"], exist_ok=True)
    
    # 1. Generate rich solutions and standalone HTMLs
    updated_dataset = []
    for item in dataset:
        q_num = item["q"]
        sol_data = syn.build_rich_solution(item)
        
        # Render standalone HTML
        html_content = eng.render_standalone_html(
            item, sol_data, cfg["back_link"], cfg["back_label"]
        )
        
        sol_file_rel = item["file_html"]
        sol_file_abs = os.path.join(BASE_DIR, sol_file_rel)
        with open(sol_file_abs, "w", encoding="utf-8") as out_f:
            out_f.write(html_content)
            
        # Update entry
        entry = dict(item)
        entry["title"] = sol_data["title"]
        entry["takeaways"] = sol_data["takeaways"]
        updated_dataset.append(entry)
        
    # Write updated dataset
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(updated_dataset, f, indent=2)
    print(f"Updated {json_path} with enriched data.")
    print(f"Generated 150 detailed HTML guides in {cfg['sol_dir']}")
    
    # 2. Compile Master SPA Portal
    sections_dict = {}
    for q in dataset:
        s = q["section"]
        if s not in sections_dict:
            sections_dict[s] = []
        sections_dict[s].append(q)

    sidebar_nav_html = []
    for sec_name, q_list in sections_dict.items():
        sidebar_nav_html.append(f'<div class="nav-section-title">{sec_name}</div>')
        sidebar_nav_html.append('<ul class="nav-list">')
        for q in q_list:
            q_num = q["q"]
            top = q["topic"]
            preview = q["question"][:85] + "..."
            icon = q.get("icon", "🌍")
            sidebar_nav_html.append(f'''
            <li class="nav-item" data-q="{q_num}">
              <a href="#q{q_num}" class="nav-link" onclick="selectQuestion({q_num}); return false;">
                <span class="nav-badge">Q{q_num:03d}</span>
                <div class="nav-info">
                  <div class="nav-title">{icon} {top}</div>
                  <div class="nav-preview">{preview}</div>
                </div>
              </a>
            </li>
            ''')
        sidebar_nav_html.append('</ul>')

    modules_html = []
    for q in dataset:
        q_num = q["q"]
        sec = q["section"]
        top = q["topic"]
        html_file = q["file_html"]
        full_html_path = os.path.join(BASE_DIR, html_file)
        
        with open(full_html_path, "r", encoding="utf-8") as hf:
            soup = BeautifulSoup(hf.read(), "html.parser")
            page_div = soup.find("div", class_="page") or soup.body
            back_nav = page_div.find("div", class_="back-nav")
            if back_nav:
                back_nav.decompose()
            inner_html = page_div.decode_contents()
            inner_html = re.sub(r'<img\s+(?!loading=)', '<img loading="lazy" decoding="async" ', inner_html)
        
        module_article = f'''
        <article class="question-module" id="q{q_num}" data-q="{q_num}" data-section="{sec}" data-topic="{top}">
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
          {inner_html}
        </article>
        '''
        modules_html.append(module_article)

    filter_pills_html = ['<button class="filter-pill active" onclick="filterBySection(\'All\', this)">All Questions (150)</button>']
    for sec_name, q_list in sections_dict.items():
        filter_pills_html.append(f'<button class="filter-pill" onclick="filterBySection(\'{sec_name}\', this)">{sec_name} ({len(q_list)})</button>')

    # Active indicator in switcher
    p_id = cfg["id"]
    switcher_html = f'''
        <a href="index.html" class="year-btn inactive" title="Odisha 2021 Geologist Paper-II (150 Live)">Geo 2021 (150)</a>
        <a href="index_2019.html" class="year-btn inactive" title="Odisha 2019 Geologist Paper-II (150 Live)">Geo 2019 (150)</a>
        <a href="index_petrologist_2021.html" class="year-btn {"active" if p_id == "petrologist_2021" else "inactive"}" title="Odisha 2021 Petrologist Paper-II (150 Live)">Petro 2021 (150)</a>
        <a href="index_mining_applied_2021.html" class="year-btn {"active" if p_id == "mining_applied_2021" else "inactive"}" title="Odisha 2021 Mining Officer Applied Geology Paper-II (150 Live)">Mining 2021 (150)</a>
        <a href="index_mining_applied_2019.html" class="year-btn {"active" if p_id == "mining_applied_2019" else "inactive"}" title="Odisha 2019 Mining Officer Applied Geology Paper-II (150 Live)">Mining 2019 (150)</a>
        <a href="../index.html" class="year-btn inactive" title="Assam 2019 Assistant Geologist (100 Live)">Assam 2019 (100)</a>
    '''

    portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cfg['name']} | 150 Question Masterclass Portal</title>
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
{CSS_STYLES_PORTAL}
{eng.CSS_STYLES}
</style>
</head>
<body>
<div class="app-container">
  <!-- Left Sidebar -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-header-top">
        <div>
          <span class="brand-badge">{cfg['brand_badge']}</span>
          <h1 class="brand-title">{cfg['brand_title']}</h1>
          <div class="brand-subtitle">{cfg['brand_subtitle']}</div>
        </div>
        <button class="sidebar-close-btn" onclick="toggleSidebar(false)" title="Close Sidebar">✕</button>
      </div>

      <!-- Multi-Paper Switcher -->
      <div class="year-switcher">
        {switcher_html}
      </div>
    </div>

    <div class="sidebar-search">
      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Search questions, minerals, mines..." onkeyup="filterQuestions()">
      </div>
    </div>

    <nav class="sidebar-nav">
      {''.join(sidebar_nav_html)}
    </nav>
  </aside>

  <!-- Main Content Area -->
  <main class="main-content">
    <header class="top-navbar">
      <div class="navbar-left">
        <button class="btn-sidebar-toggle" onclick="toggleSidebar()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
          Menu
        </button>
        <span class="navbar-title">{cfg['navbar_title']}</span>
      </div>
      <div class="navbar-actions">
        <a href="data/{cfg['id']}.json" download class="btn-action">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          JSON Dataset
        </a>
      </div>
    </header>

    <div class="filter-bar">
      {''.join(filter_pills_html)}
    </div>

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

    portal_path = os.path.join(BASE_DIR, cfg["portal_file"])
    with open(portal_path, "w", encoding="utf-8") as f:
        f.write(portal_html)
    print(f"Compiled {portal_path} successfully!")

if __name__ == "__main__":
    for config in PAPER_CONFIGS:
        process_paper(config)
    print("\nALL 3 PAPERS PROCESSED AND REBUILT SUCCESSFULLY!")
