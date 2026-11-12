import json
import os

data_path = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter15_AppliedGeology/data/sayeed_ch15_applied_geology.json'
with open(data_path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

total_q = len(questions)
sec_a_count = sum(1 for q in questions if q['section_id'] == 'sec_a')
sec_b_count = sum(1 for q in questions if q['section_id'] == 'sec_b')
sec_c_count = sum(1 for q in questions if q['section_id'] == 'sec_c')
sec_d_count = sum(1 for q in questions if q['section_id'] == 'sec_d')

cards_html = ""
for q in questions:
    q_num = q['global_q_num']
    sec_id = q['section_id']
    sec_title = q['section']
    sec_q = q['section_q_num']
    topic = q['topic']
    q_text = q['question']
    options = q['options']
    correct_opt = q['correct_option']
    diff = q['difficulty']

    opts_html = ""
    for k in sorted(options.keys()):
        val = options[k]
        is_corr = (k == correct_opt)
        badge = '<span class="badge-corr">CORRECT</span>' if is_corr else ""
        cls = "opt-row correct-row" if is_corr else "opt-row"
        opts_html += f"""
        <div class="{cls}" data-opt="{k}">
            <div class="opt-key">({k})</div>
            <div class="opt-val">{val}</div>
            {badge}
        </div>
        """

    cards_html += f"""
    <div class="q-card" data-qid="{q_num}" data-sec="{sec_id}" data-topic="{topic.lower()}">
        <div class="card-meta">
            <span class="meta-badge badge-qnum">Q{q_num:03d} (Sec {sec_q})</span>
            <span class="meta-badge badge-sec">{sec_title.split(':')[0]}</span>
            <span class="meta-badge badge-topic">{topic}</span>
            <span class="meta-badge badge-diff">{diff}</span>
        </div>
        <div class="q-prompt">{q_text}</div>
        <div class="options-container">
            {opts_html}
        </div>
        <div class="card-actions">
            <button class="btn btn-reveal" onclick="toggleAnswer({q_num})">Reveal Verified Answer</button>
            <a href="solutions/Q{q_num:03d}_sayeed_ch15.html" class="btn btn-sol" target="_blank">Full Masterclass Solution &rarr;</a>
        </div>
        <div class="answer-drawer" id="drawer-{q_num}">
            <div class="drawer-header">
                <strong>Verified Answer:</strong> Option ({correct_opt}) — {options.get(correct_opt, '')}
            </div>
            <div class="drawer-note">
                Covers: {topic}. Complete quantitative formulas, forensic option dissection, and synthesis table available in the Masterclass Solution.
            </div>
        </div>
    </div>
    """

portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 15: Applied Geology | Dr. Ausaf Sayeed Masterclass Portal</title>
    <!-- MathJax 3.2.2 for mathematical and physical geophysics/geomechanics formulas -->
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            }},
            svg: {{ fontCache: 'global' }}
        }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root {{
            --primary: #00695c;
            --primary-dark: #004d40;
            --primary-light: #e0f2f1;
            --primary-mid: #00897b;
            --accent: #0097a7;
            --bg: #f2f7f7;
            --card-bg: #ffffff;
            --text-main: #132e2d;
            --text-muted: #526f6e;
            --border: #c4e3e1;
            --success: #059669;
            --radius-sm: 6px;
            --radius: 12px;
            --radius-lg: 16px;
            --shadow: 0 4px 6px -1px rgba(0, 77, 64, 0.08), 0 2px 4px -2px rgba(0, 77, 64, 0.04);
            --shadow-lg: 0 10px 25px -5px rgba(0, 77, 64, 0.12), 0 8px 10px -6px rgba(0, 77, 64, 0.08);
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text-main);
            line-height: 1.6;
            padding: 24px;
        }}
        .portal-container {{
            max-width: 1100px;
            margin: 0 auto;
        }}
        .portal-header {{
            background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 60%, var(--primary-mid) 100%);
            color: white;
            padding: 36px 32px;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-lg);
            margin-bottom: 28px;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }}
        .header-nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            font-size: 0.9rem;
        }}
        .header-nav a {{
            color: #b2dfdb;
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: color 0.2s;
        }}
        .header-nav a:hover {{
            color: #ffffff;
            text-decoration: underline;
        }}
        .portal-title {{
            font-size: 2.1rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 10px;
        }}
        .portal-subtitle {{
            font-size: 1.05rem;
            color: #e0f2f1;
            max-width: 850px;
            margin-bottom: 20px;
            font-weight: 400;
        }}
        .portal-stats {{
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }}
        .stat-pill {{
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .controls-card {{
            background: var(--card-bg);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
            padding: 20px;
            margin-bottom: 24px;
        }}
        .search-box {{
            width: 100%;
            padding: 12px 18px;
            border: 2px solid var(--border);
            border-radius: var(--radius);
            font-size: 1rem;
            outline: none;
            transition: border-color 0.2s;
            margin-bottom: 16px;
        }}
        .search-box:focus {{
            border-color: var(--primary);
        }}
        .filter-tabs {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .tab-btn {{
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.88rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .tab-btn:hover {{
            background: var(--primary-light);
            border-color: var(--primary-mid);
        }}
        .tab-btn.active {{
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }}
        .quiz-banner {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #e0f2f1;
            border: 1px solid #80cbc4;
            padding: 12px 20px;
            border-radius: var(--radius);
            margin-bottom: 24px;
        }}
        .quiz-btn {{
            background: var(--primary);
            color: white;
            border: none;
            padding: 8px 18px;
            border-radius: 6px;
            font-weight: 700;
            cursor: pointer;
            transition: background 0.2s;
        }}
        .quiz-btn:hover {{
            background: var(--primary-dark);
        }}
        .q-card {{
            background: var(--card-bg);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
            padding: 24px;
            margin-bottom: 20px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .q-card:hover {{
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }}
        .card-meta {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }}
        .meta-badge {{
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 3px 8px;
            border-radius: 4px;
            letter-spacing: 0.04em;
        }}
        .badge-qnum {{ background: var(--primary-dark); color: white; }}
        .badge-sec {{ background: var(--primary-light); color: var(--primary-dark); }}
        .badge-topic {{ background: #e0f7fa; color: #006064; }}
        .badge-diff {{ background: #fef3c7; color: #92400e; }}
        .q-prompt {{
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--primary-dark);
            margin-bottom: 16px;
            line-height: 1.45;
        }}
        .options-container {{
            display: grid;
            gap: 8px;
            margin-bottom: 18px;
        }}
        .opt-row {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 14px;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            background: #fafafa;
            font-size: 0.95rem;
        }}
        .opt-row.revealed.correct-row {{
            background: #ecfdf5;
            border-color: var(--success);
            font-weight: 600;
        }}
        .opt-key {{
            font-weight: 700;
            color: var(--primary);
            min-width: 24px;
        }}
        .badge-corr {{
            display: none;
            background: var(--success);
            color: white;
            font-size: 0.65rem;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
            margin-left: auto;
        }}
        .opt-row.revealed .badge-corr {{
            display: inline-block;
        }}
        .card-actions {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            align-items: center;
        }}
        .btn {{
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.88rem;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }}
        .btn-reveal {{
            background: var(--primary-light);
            color: var(--primary-dark);
            border: 1px solid var(--primary-mid);
        }}
        .btn-reveal:hover {{
            background: #b2dfdb;
        }}
        .btn-sol {{
            background: var(--primary);
            color: white;
            border: 1px solid var(--primary);
        }}
        .btn-sol:hover {{
            background: var(--primary-dark);
        }}
        .answer-drawer {{
            display: none;
            margin-top: 16px;
            padding: 14px 18px;
            background: #f0fdfa;
            border-left: 4px solid var(--primary-mid);
            border-radius: 0 6px 6px 0;
            font-size: 0.92rem;
        }}
        .answer-drawer.open {{
            display: block;
        }}
        .drawer-header {{
            font-weight: 700;
            color: var(--primary-dark);
            margin-bottom: 6px;
        }}
        .drawer-note {{
            color: #334155;
            font-size: 0.88rem;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 24px;
            color: var(--text-muted);
            font-size: 0.9rem;
            border-top: 1px solid var(--border);
        }}
    </style>
</head>
<body>
    <div class="portal-container">
        <!-- Portal Header -->
        <header class="portal-header">
            <div class="header-nav">
                <a href="../../index.html">&larr; Main Solutions Index</a>
                <div>
                    <a href="../Sayeed_Chapter14_EconomicGeology/index_sayeed_ch14.html">&larr; Chapter 14 (Economic Geology)</a>
                </div>
            </div>
            <h1 class="portal-title">Chapter 15: Applied Geology</h1>
            <p class="portal-subtitle">
                Comprehensive Masterclass Portal for Dr. Ausaf Sayeed's Objective Geology Chapter 15.
                Exhaustive 3-part solutions covering Exploration Geophysics & Geochemistry, Ore Beneficiation, Mining Geology & Economics, Hydrogeology, and Rock Mechanics.
            </p>
            <div class="portal-stats">
                <span class="stat-pill">Total Questions: {total_q}</span>
                <span class="stat-pill">Sec A (Exploration): {sec_a_count}</span>
                <span class="stat-pill">Sec B (Mineral Processing & Mining): {sec_b_count}</span>
                <span class="stat-pill">Sec C (Hydrogeology): {sec_c_count}</span>
                <span class="stat-pill">Sec D (Engineering Geology): {sec_d_count}</span>
                <span class="stat-pill">Verified Key: 100% Complete</span>
            </div>
        </header>

        <!-- Controls: Search & Section Filter Tabs -->
        <div class="controls-card">
            <input type="text" id="searchInput" class="search-box" placeholder="Search questions by keywords, mineral, formula, or topic (e.g. Darcy, Schlumberger, RQD, Wilfley, Cuddalore)..." onkeyup="filterQuestions()">
            <div class="filter-tabs">
                <button class="tab-btn active" onclick="setSectionFilter('all', this)">All Sections ({total_q})</button>
                <button class="tab-btn" onclick="setSectionFilter('sec_a', this)">Sec A: Exploration Methods ({sec_a_count})</button>
                <button class="tab-btn" onclick="setSectionFilter('sec_b', this)">Sec B: Processing & Mining ({sec_b_count})</button>
                <button class="tab-btn" onclick="setSectionFilter('sec_c', this)">Sec C: Hydrogeology ({sec_c_count})</button>
                <button class="tab-btn" onclick="setSectionFilter('sec_d', this)">Sec D: Engineering Geology ({sec_d_count})</button>
            </div>
        </div>

        <!-- Quiz Mode Banner -->
        <div class="quiz-banner">
            <div>
                <strong>Random Practice Quiz:</strong> Test your applied geology knowledge with 10 random questions across all sections.
            </div>
            <button class="quiz-btn" onclick="startRandomQuiz()">Launch 10-Q Quiz</button>
        </div>

        <!-- Question Cards Grid -->
        <main id="questionsGrid">
            {cards_html}
        </main>

        <!-- Portal Footer -->
        <footer class="footer">
            <p><strong>Dr. Ausaf Sayeed's Objective Geology — Masterclass Solutions Portal</strong></p>
            <p>Chapter 15: Applied Geology (190 Questions) &bull; Gold-Standard 3-Part Technical Layout &bull; MathJax Formulations</p>
            <p style="margin-top: 8px;"><a href="../../index.html" style="color: var(--primary); text-decoration: none; font-weight: 600;">Return to Main Index Portal</a></p>
        </footer>
    </div>

    <!-- Interactive Portal Logic -->
    <script>
        let currentSection = 'all';

        function toggleAnswer(qid) {{
            const drawer = document.getElementById('drawer-' + qid);
            const card = drawer.closest('.q-card');
            const rows = card.querySelectorAll('.opt-row');
            
            if (drawer.classList.contains('open')) {{
                drawer.classList.remove('open');
                rows.forEach(r => r.classList.remove('revealed'));
            }} else {{
                drawer.classList.add('open');
                rows.forEach(r => r.classList.add('revealed'));
            }}
        }}

        function setSectionFilter(secId, btn) {{
            currentSection = secId;
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            filterQuestions();
        }}

        function filterQuestions() {{
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const cards = document.querySelectorAll('.q-card');

            cards.forEach(card => {{
                const cardSec = card.getAttribute('data-sec');
                const cardText = card.innerText.toLowerCase();

                const matchesSec = (currentSection === 'all' || cardSec === currentSection);
                const matchesSearch = (!query || cardText.includes(query));

                if (matchesSec && matchesSearch) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        function startRandomQuiz() {{
            const cards = Array.from(document.querySelectorAll('.q-card'));
            cards.forEach(c => c.style.display = 'none');
            
            // Pick 10 random cards
            const shuffled = cards.sort(() => 0.5 - Math.random());
            const selected = shuffled.slice(0, 10);
            
            selected.forEach(c => c.style.display = 'block');
            document.getElementById('searchInput').value = '';
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            
            window.scrollTo({{ top: 350, behavior: 'smooth' }});
            alert('Quiz mode active: 10 random questions displayed below. Click "Reveal Verified Answer" on each to check yourself!');
        }}
    </script>
</body>
</html>
"""

portal_out = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter15_AppliedGeology/index_sayeed_ch15.html'
with open(portal_out, 'w', encoding='utf-8') as f:
    f.write(portal_html)

print(f"Generated Interactive Portal: {portal_out} ({len(portal_html)} bytes)!")
