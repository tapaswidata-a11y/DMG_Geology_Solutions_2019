import re

PORTALS = [
    ("index.html", "Geo 2021 (150)"),
    ("index_2019.html", "Geo 2019 (150)"),
    ("index_petrologist_2021.html", "Petro 2021 (150)"),
    ("index_mining_applied_2021.html", "Mining 2021 (150)"),
    ("index_mining_applied_2019.html", "Mining 2019 (150)"),
]

def make_switcher_html(active_name, is_root=False):
    prefix = "" if not is_root else "Orrisa_geology/"
    assam_link = "../index.html" if not is_root else "index.html"
    
    links = [
        (f"{prefix}index.html", "Geo 2021 (150)", "Odisha 2021 Geologist Paper-II (150 Live)"),
        (f"{prefix}index_2019.html", "Geo 2019 (150)", "Odisha 2019 Geologist Paper-II (150 Live)"),
        (f"{prefix}index_petrologist_2021.html", "Petro 2021 (150)", "Odisha 2021 Petrologist Paper-II (150 Live)"),
        (f"{prefix}index_mining_applied_2021.html", "Mining 2021 (150)", "Odisha 2021 Mining Officer Applied Geology Paper-II (150 Live)"),
        (f"{prefix}index_mining_applied_2019.html", "Mining 2019 (150)", "Odisha 2019 Mining Officer Applied Geology Paper-II (150 Live)"),
        (assam_link, "Assam 2019 (100)", "Assam 2019 Assistant Geologist (100 Live)")
    ]
    
    html = ['      <div class="year-switcher">']
    for href, label, title in links:
        cls = "year-btn active" if label == active_name else "year-btn inactive"
        html.append(f'        <a href="{href}" class="{cls}" title="{title}">{label}</a>')
    html.append('      </div>')
    return '\n'.join(html)

# Update Odisha portals
for fname, active_label in PORTALS:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the year-switcher block
    pattern = r'<div class="year-switcher">.*?</div>'
    new_sw = make_switcher_html(active_label, is_root=False)
    updated, n = re.subn(pattern, new_sw, content, flags=re.DOTALL)
    if n > 0:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"Updated {fname} ({n} matches)")
    else:
        print(f"FAILED to match year-switcher in {fname}")

# Update root index.html
with open("../index.html", "r", encoding="utf-8") as f:
    root_content = f.read()

root_new_sw = make_switcher_html("Assam 2019 (100)", is_root=True)
root_updated, n = re.subn(r'<div class="year-switcher">.*?</div>', root_new_sw, root_content, flags=re.DOTALL)
if n > 0:
    with open("../index.html", "w", encoding="utf-8") as f:
        f.write(root_updated)
    print(f"Updated ../index.html ({n} matches)")
else:
    print("FAILED to match year-switcher in ../index.html")

