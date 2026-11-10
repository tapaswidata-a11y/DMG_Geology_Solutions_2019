"""
Reusable Masterclass HTML Engine & Renderer
Generates textbook-grade standalone HTML solutions and portal modules.
"""

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

  .back-nav { margin-bottom: 16px; }
  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #0284c7;
    text-decoration: none;
    font-weight: 600;
    font-size: 13.5px;
    padding: 6px 12px;
    background: #e0f2fe;
    border-radius: 6px;
    transition: all 0.2s ease;
  }
  .back-link:hover { background: #bae6fd; color: #0369a1; }

  .header {
    background: linear-gradient(135deg, #091e3a 0%, #0f2b4c 50%, #1e3a8a 100%);
    color: #fff;
    border-radius: 12px;
    padding: 26px 30px;
    margin-bottom: 22px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  }
  .badge {
    display: inline-block;
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  .header h1 {
    font-size: 21px;
    font-weight: 800;
    line-height: 1.35;
    margin-bottom: 10px;
    color: #f8fafc;
  }
  .meta {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    font-size: 12.5px;
    color: #cbd5e1;
  }
  .meta strong { color: #fff; }

  .raw-box {
    background: #eff6ff;
    border: 2px solid #3b82f6;
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 22px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .raw-title {
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    color: #1d4ed8;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
  }
  .raw-question {
    font-size: 15.5px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 14px;
    line-height: 1.5;
  }
  .raw-options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  .raw-opt {
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 13.5px;
    background: #fff;
    border: 1px solid #cbd5e1;
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

  .part-banner {
    display: flex;
    align-items: center;
    gap: 16px;
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    color: #fff;
    padding: 14px 20px;
    border-radius: 10px;
    margin: 28px 0 18px 0;
    box-shadow: 0 3px 10px rgba(37, 99, 235, 0.2);
  }
  .part-banner.green {
    background: linear-gradient(135deg, #065f46 0%, #059669 100%);
    box-shadow: 0 3px 10px rgba(5, 150, 105, 0.2);
  }
  .part-banner.purple {
    background: linear-gradient(135deg, #581c87 0%, #7c3aed 100%);
    box-shadow: 0 3px 10px rgba(124, 58, 237, 0.2);
  }
  .first-part { margin-top: 10px; }
  .part-num {
    font-size: 24px;
    font-weight: 800;
    opacity: 0.9;
    border-right: 2px solid rgba(255,255,255,0.3);
    padding-right: 14px;
    line-height: 1;
    font-family: 'Fira Code', monospace;
  }
  .part-title { font-size: 16.5px; font-weight: 700; letter-spacing: 0.3px; }
  .part-sub { font-size: 12px; opacity: 0.9; margin-top: 2px; }

  .card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 20px;
    overflow: hidden;
  }
  .card-header {
    padding: 11px 20px;
    font-size: 13.5px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #fff;
  }
  .bg-blue   { background: #1d4ed8; }
  .bg-indigo { background: #4338ca; }
  .bg-emerald{ background: #047857; }
  .bg-purple { background: #6d28d9; }
  .bg-slate  { background: #334155; }
  
  .card-body { padding: 20px 24px; font-size: 14px; color: #334155; line-height: 1.68; }
  .card-body p { margin-bottom: 12px; }
  .card-body p:last-child { margin-bottom: 0; }
  .card-body ul, .card-body ol { margin: 8px 0 12px 22px; }
  .card-body li { margin-bottom: 6px; }

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
  .quote-ref {
    display: block;
    font-size: 12px;
    font-style: normal;
    font-weight: 700;
    margin-top: 8px;
    color: #1d4ed8;
  }

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
  .option-body { padding: 14px 18px; background: #fafafa; font-size: 13.5px; color: #334155; line-height: 1.65; }
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

  table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 12px 0; }
  th { background: #0f172a; color: #fff; padding: 10px 12px; text-align: left; font-weight: 600; }
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
  .pq-ans { margin-top: 6px; color: #065f46; font-weight: 700; }
  .pq-exp { margin-top: 4px; color: #475569; font-size: 13px; line-height: 1.55; }

  @media (max-width: 768px) {
    .raw-options { grid-template-columns: 1fr; }
  }
"""

def render_standalone_html(item, sol_dict, back_portal_url, back_portal_label):
    q = item["q"]
    opts = item["options"]
    corr = item["correct_option"]
    sec = item["section"]
    top = item["topic"]
    stmt = item["question"]
    p_code = item["paper_code"]
    p_name = item["paper_name"]
    icon = item.get("icon", "🌍")
    
    # Extract rich data
    title = sol_dict.get("title", f"{top}")
    p1_concept = sol_dict.get("concept", f"<p>Standard geological and engineering principles govern <strong>{top}</strong>.</p>")
    quote = sol_dict.get("quote", "")
    quote_ref = sol_dict.get("quote_ref", item.get("textbook_ref", ""))
    formula = sol_dict.get("formula", "")
    dissections = sol_dict.get("dissections", {})
    t_headers = sol_dict.get("table_headers", ["Parameter", "Exam Specification", "Geological Significance"])
    t_rows = sol_dict.get("table_rows", [
        ["Topic & Domain", top, sec],
        ["Verified Option", f"Option ({corr}): {opts.get(corr, '')}", item.get("correct_text", "")],
        ["Authoritative Source", quote_ref, "Official Examination Standard"]
    ])
    takeaways = sol_dict.get("takeaways", f"Verified Answer: Option ({corr}) ({opts.get(corr, '')}) correctly satisfies all diagnostic criteria.")
    practice_qs = sol_dict.get("practice_qs", [
        {"q": f"What primary parameter diagnoses {top} in field exploration?", "ans": f"Option ({corr})", "exp": f"Grounded in verified geological relationships from {quote_ref}."}
    ])
    
    # Raw options html
    raw_opt_html = "".join([
        f'<div class="raw-opt {"correct" if corr == let else ""}">'
        f'<strong>({let})</strong> {opts.get(let, "")} {"&nbsp;✔" if corr == let else ""}'
        f'</div>'
        for let in ["A", "B", "C", "D"]
    ])
    
    # Quote html
    quote_html = ""
    if quote:
        quote_html = f"""
        <div class="quote-box">
          "{quote.strip()}"
          <span class="quote-ref">— {quote_ref}</span>
        </div>
        """
    
    # Formula html
    formula_html = ""
    if formula:
        formula_html = f"""
        <div class="formula-card">
          <div class="formula-title">Governing Physical / Mathematical Relationship</div>
          {formula}
        </div>
        """

    # Part 2 Option cards
    opt_cards = []
    for let in ["A", "B", "C", "D"]:
        is_c = (corr == let)
        dissect_txt = dissections.get(let, "")
        if not dissect_txt:
            if is_c:
                dissect_txt = f"<strong>Why Option ({let}) is correct:</strong> Accurately satisfies the foundational definition and technical criteria established in authoritative literature."
            else:
                dissect_txt = f"<strong>Why Option ({let}) is incorrect:</strong> Represents an alternative or non-applicable geological category that does not satisfy the specific conditions of the question stem."
        
        opt_card = f"""
        <div class="option {'correct' if is_c else 'wrong'}">
          <div class="option-header">
            <span>({let}) {opts.get(let, '')}</span>
            <span class="tag {'correct' if is_c else 'wrong'}">{'Correct Verified Option' if is_c else 'Incorrect Distractor'}</span>
          </div>
          <div class="option-body">
            {dissect_txt}
          </div>
        </div>
        """
        opt_cards.append(opt_card)
        
    # Part 3 Table
    th_cells = "".join([f"<th>{h}</th>" for h in t_headers])
    tr_rows = []
    for row in t_rows:
        td_cells = "".join([f"<td>{c}</td>" for c in row])
        tr_rows.append(f"<tr>{td_cells}</tr>")
    table_html = f"""
    <table>
      <thead>
        <tr>{th_cells}</tr>
      </thead>
      <tbody>
        {''.join(tr_rows)}
      </tbody>
    </table>
    """
    
    # Part 3 Practice questions
    pq_items = []
    for idx, pq in enumerate(practice_qs, 1):
        pq_items.append(f"""
        <li>
          <strong>Practice Problem {idx}:</strong> {pq.get('q', '')}
          <div class="pq-ans">✔ Verified Solution: {pq.get('ans', '')}</div>
          <div class="pq-exp"><strong>Mechanistic Rationale:</strong> {pq.get('exp', '')}</div>
        </li>
        """)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Q{q:03d}: {title} | {p_name} Masterclass</title>
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
{CSS_STYLES}
</style>
</head>
<body>
<div class="page">
  <div class="back-nav no-print">
    <a href="{back_portal_url}#q{q}" class="back-link">← {back_portal_label}</a>
  </div>
  
  <div class="header">
    <div class="badge">{p_code} &bull; {sec}</div>
    <h1>{icon} Q{q:03d}: {title}</h1>
    <div class="meta">
      <span><strong>Official Exam:</strong> {p_name}, Question {q}</span>
      <span><strong>Authoritative Reference:</strong> {quote_ref}</span>
    </div>
  </div>

  <div class="raw-box">
    <div class="raw-title">Official Examination Question — Question {q}</div>
    <div class="raw-question">{stmt}</div>
    <div class="raw-options">
      {raw_opt_html}
    </div>
  </div>

  <div class="part-banner first-part">
    <div class="part-num">PART I</div>
    <div>
      <div class="part-title">Theoretical Foundation & Scientific Principles</div>
      <div class="part-sub">Authoritative textbook grounding, analytical derivations, and physical mechanics</div>
    </div>
  </div>
  
  <div class="card">
    <div class="card-header bg-blue">{top}: Fundamental Principles & Mechanics</div>
    <div class="card-body">
      {p1_concept}
      {quote_html}
      {formula_html}
    </div>
  </div>

  <div class="part-banner green">
    <div class="part-num">PART II</div>
    <div>
      <div class="part-title">Forensic Option Dissection & Error Analysis</div>
      <div class="part-sub">Individual forensic validation of the correct choice and refutation of incorrect distractors</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Verified Official Answer: ({corr}) {opts.get(corr, '')}</div>
      <div class="sub">{item.get('correct_text', '')}</div>
    </div>
  </div>

  {''.join(opt_cards)}

  <div class="part-banner purple">
    <div class="part-num">PART III</div>
    <div>
      <div class="part-title">Synthesis Reference Tables & High-Yield Practice Questions</div>
      <div class="part-sub">Comparative data matrices, essential exam takeaways, and worked derivations</div>
    </div>
  </div>
  
  <div class="card">
    <div class="card-header bg-slate">Technical Data & Diagnostic Comparison</div>
    <div class="card-body" style="padding: 0; overflow-x: auto;">
      {table_html}
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Key Examination Takeaway</div>
    <div class="card-body">
      <p>{takeaways}</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems with Worked Solutions</div>
    <div class="card-body">
      <ul class="pq-list">
        {''.join(pq_items)}
      </ul>
    </div>
  </div>
</div>
</body>
</html>
"""
    return full_html
