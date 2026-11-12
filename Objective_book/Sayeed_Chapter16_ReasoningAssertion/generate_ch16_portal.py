import json
import os

data_path = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter16_ReasoningAssertion/data/sayeed_ch16_reasoning_assertion.json'
with open(data_path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

total_q = len(questions)

cards_html = ""
for q in questions:
    q_num = q['global_q_num']
    topic = q['topic']
    a_txt = q['assertion']
    r_txt = q['reason']
    options = q['options']
    correct_opt = q['correct_option']
    diff = q['difficulty']

    opts_html = ""
    for k in sorted(options.keys()):
        val = options[k]
        is_corr = (k == correct_opt)
        badge = '<span class="badge-corr">CORRECT VERDICT</span>' if is_corr else ""
        cls = "opt-row correct-row" if is_corr else "opt-row"
        opts_html += f"""
        <div class="{cls}" data-opt="{k}">
            <div class="opt-key">({k})</div>
            <div class="opt-val">{val}</div>
            {badge}
        </div>
        """

    cards_html += f"""
    <div class="q-card" data-qid="{q_num}" data-topic="{topic.lower()}">
        <div class="card-meta">
            <span class="meta-badge badge-qnum">Q{q_num:02d}</span>
            <span class="meta-badge badge-sec">Assertion-Reasoning</span>
            <span class="meta-badge badge-topic">{topic}</span>
            <span class="meta-badge badge-diff">{diff}</span>
        </div>
        <div class="statement-panel">
            <div class="statement-row">
                <span class="statement-tag">Assertion (A):</span>
                <span class="statement-content">{a_txt}</span>
            </div>
            <div class="statement-row" style="margin-top: 10px;">
                <span class="statement-tag">Reason (R):</span>
                <span class="statement-content">{r_txt}</span>
            </div>
        </div>
        <div class="options-container">
            {opts_html}
        </div>
        <div class="card-actions">
            <button class="btn btn-reveal" onclick="toggleAnswer({q_num})">Reveal Logical Verdict</button>
            <a href="solutions/Q{q_num:03d}_sayeed_ch16.html" class="btn btn-sol" target="_blank">Full Masterclass Solution &rarr;</a>
        </div>
        <div class="answer-drawer" id="drawer-{q_num}">
            <div class="drawer-header">
                <strong>Verified Key:</strong> Option ({correct_opt}) — {options.get(correct_opt, '')}
            </div>
            <div class="drawer-note">
                Domain: {topic}. Complete logical proof, factual verification of (A) and (R), causality analysis, and foundational formulas available in the Masterclass Solution.
            </div>
        </div>
    </div>
    """

portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 16: Reasoning and Assertion | Dr. Ausaf Sayeed Masterclass Portal</title>
    <!-- MathJax 3.2.2 -->
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
            --primary: #312e81;
            --primary-dark: #1e1b4b;
            --primary-light: #e0e7ff;
            --primary-mid: #4338ca;
            --accent: #4f46e5;
            --accent-glow: #6366f1;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border: #c7d2fe;
            --success: #059669;
            --radius: 12px;
            --radius-lg: 16px;
            --shadow: 0 4px 6px -1px rgba(49, 46, 129, 0.08), 0 2px 4px -2px rgba(49, 46, 129, 0.04);
            --shadow-lg: 0 10px 25px -5px rgba(49, 46, 129, 0.12), 0 8px 10px -6px rgba(49, 46, 129, 0.08);
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
            max-width: 1050px;
            margin: 0 auto;
        }}
        .portal-header {{
            background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 50%, var(--primary-mid) 100%);
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
            color: #c7d2fe;
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
            color: #e0e7ff;
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
        .celebration-box {{
            background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
            border: 2px solid #10b981;
            border-radius: var(--radius);
            padding: 18px 24px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            gap: 16px;
        }}
        .celebration-icon {{
            font-size: 2.2rem;
        }}
        .celebration-text {{
            color: #065f46;
            font-size: 0.98rem;
        }}
        .celebration-text strong {{
            font-size: 1.1rem;
            display: block;
            margin-bottom: 4px;
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
        }}
        .search-box:focus {{
            border-color: var(--primary);
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
            margin-bottom: 14px;
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
        .badge-topic {{ background: #ede9fe; color: #5b21b6; }}
        .badge-diff {{ background: #fef3c7; color: #92400e; }}
        .statement-panel {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-left: 4px solid var(--primary-mid);
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 18px;
        }}
        .statement-row {{
            display: flex;
            gap: 8px;
            font-size: 1.05rem;
            line-height: 1.45;
        }}
        .statement-tag {{
            font-weight: 700;
            color: var(--primary-dark);
            min-width: 125px;
        }}
        .statement-content {{
            color: var(--text-main);
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
            font-size: 0.92rem;
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
            background: #c7d2fe;
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
            background: #fdf2f8;
            border-left: 4px solid #db2777;
            border-radius: 0 6px 6px 0;
            font-size: 0.92rem;
        }}
        .answer-drawer.open {{
            display: block;
        }}
        .drawer-header {{
            font-weight: 700;
            color: #831843;
            margin-bottom: 6px;
        }}
        .drawer-note {{
            color: #475569;
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
                    <a href="../Sayeed_Chapter15_AppliedGeology/index_sayeed_ch15.html">&larr; Chapter 15 (Applied Geology)</a>
                </div>
            </div>
            <h1 class="portal-title">Chapter 16: Questions Based on Assertion and Reasoning</h1>
            <p class="portal-subtitle">
                The Final Masterclass Chapter of Dr. Ausaf Sayeed's Objective Geology.
                Rigorous forensic evaluation of 35 Assertion-Reasoning problems covering Geodynamics, Mineral Optics, Petrology, Stratigraphy, and Structural Mechanics.
            </p>
            <div class="portal-stats">
                <span class="stat-pill">Total Questions: {total_q}</span>
                <span class="stat-pill">Format: 5-Option Assertion & Reason</span>
                <span class="stat-pill">Verified Key: 100% Complete</span>
                <span class="stat-pill">Book Status: 16 of 16 Chapters Solved!</span>
            </div>
        </header>

        <!-- Celebration Banner -->
        <div class="celebration-box">
            <div class="celebration-icon">&#127942;</div>
            <div class="celebration-text">
                <strong>Textbook Milestone Achieved: Complete 16-Chapter Masterclass Solutions!</strong>
                Every chapter from Chapter 1 (General Geology & Geotectonics) to Chapter 16 (Reasoning & Assertion) has now been fully solved with exhaustive 3-part Masterclass solutions, responsive SPA portals, and MathJax quantitative formulations.
            </div>
        </div>

        <!-- Controls: Search -->
        <div class="controls-card">
            <input type="text" id="searchInput" class="search-box" placeholder="Search questions by topic, statement keywords, or mineral/concept (e.g. Bouguer, Curie, Cinnabar, Dollo, Andesite)..." onkeyup="filterQuestions()">
        </div>

        <!-- Question Cards Grid -->
        <main id="questionsGrid">
            {cards_html}
        </main>

        <!-- Portal Footer -->
        <footer class="footer">
            <p><strong>Dr. Ausaf Sayeed's Objective Geology — Masterclass Solutions Portal</strong></p>
            <p>Chapter 16: Questions Based on Assertion and Reasoning (35 Questions) &bull; Final Textbook Chapter &bull; 100% Solved</p>
            <p style="margin-top: 8px;"><a href="../../index.html" style="color: var(--primary); text-decoration: none; font-weight: 600;">Return to Main Index Portal</a></p>
        </footer>
    </div>

    <!-- Interactive Portal Logic -->
    <script>
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

        function filterQuestions() {{
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const cards = document.querySelectorAll('.q-card');

            cards.forEach(card => {{
                const cardText = card.innerText.toLowerCase();
                if (!query || cardText.includes(query)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>
"""

portal_out = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter16_ReasoningAssertion/index_sayeed_ch16.html'
with open(portal_out, 'w', encoding='utf-8') as f:
    f.write(portal_html)

print(f"Generated Interactive Portal: {portal_out} ({len(portal_html)} bytes)!")
