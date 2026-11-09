import re
import parse_all_applied_2019 as p
from build_applied_2019_metadata import META_TABLE_APPLIED_2019

def clean_ocr(text):
    text = " ".join(text.split())
    reps = {
        "Allofthese": "All of these",
        "Asaltdome": "A salt dome",
        "Riftvalleys": "Rift valleys",
        "Quartzarenite": "Quartz arenite",
        "Feldspathic arenite": "Feldspathic arenite",
        "Braidedriver": "Braided river",
        "Clayminerals": "Clay minerals",
        "Clay minerals": "Clay minerals",
        "Granularsandstone": "Granular sandstone",
        "Arkosic": "Arkosic",
        "Greywacke": "Graywacke",
        "Fore-are": "Fore-arc",
        "ForelandBasin": "Foreland Basin",
        "Intracratonic": "Intracratonic",
        "Gravitymethod": "Gravity method",
        "Magnetic method": "Magnetic method",
        "HalfSoted": "Half Sorted",
        "inte connected": "interconnected",
        "sttructures": "structures",
        "standstone": "sandstone",
        "Epsiloncrossbedding": "Epsilon cross bedding",
        "Ovidsonly": "Ooids only",
        "afects": "affects",
        "desending": "descending",
        "asthenosphete": "asthenosphere",
        "forination": "formation",
        "Alkalifeldspar": "Alkali feldspar",
        "poterozoic": "proterozoic",
        "Poterozoic": "Proterozoic",
        "short geological": "short geological",
        "inthe": "in the",
        "Chamokite": "Charnockite",
        "gtanulite": "granulite",
        "desposits": "deposits",
        "voleanic": "volcanic",
        "Kimberite": "Kimberlite",
        "Indiami": "India mined",
        "Indiamined": "India mined",
        "earthquakes": "earthquakes",
        "ofearthquakes": "of earthquakes",
        "i marked": "is marked",
        "Uppermantle": "Upper mantle",
        "lowermantle": "lower mantle",
        "Whatisthe": "What is the",
        "averageheightoftheGPS": "average height of the GPS",
        "satelite": "satellite",
        "arrangelnent": "arrangement",
        "arrangeinent": "arrangement",
        "terran": "terrain",
        "feat": "features",
        "Uniconforinity": "Unconformity",
        "betieen": "between",
        "Lahiar": "Lahar",
        "forméd": "formed",
        "sedments": "sediments",
        "Graphicgranite": "Graphic granite",
        "thyolite": "rhyolite",
        "Homblendé": "Hornblende",
        "Cojumnar": "Columnar",
        "cab is": "can be",
        "sensi": "sensing",
        "altitu": "altitude",
        "indian": "Indian",
        "waveis": "wave is",
        "consturcted": "constructed",
        "Embankment dam": "Embankment dam",
        "iule": "rule",
        "soliis": "soil is",
        "Astatic": "A static",
        "concluded": "conducted",
        "Transmitvty": "Transmissivity",
    }
    for k, v in reps.items():
        text = text.replace(k, v)
    return text

def parse_question_options(raw_body, q_num):
    # Normalize option indicators
    txt = raw_body
    # Replace common variations
    txt = re.sub(r'[\(\[\{]\s*[aA4@]\s*[\)\]\}]', '\n(A) ', txt)
    txt = re.sub(r'[\(\[\{]\s*[bB8®]\s*[\)\]\}]', '\n(B) ', txt)
    txt = re.sub(r'[\(\[\{]\s*[cC©]\s*[\)\]\}]', '\n(C) ', txt)
    txt = re.sub(r'[\(\[\{]\s*(?:[dD0O]|Dy)\s*[\)\]\}]', '\n(D) ', txt)
    
    # Standalone letter/symbol at start of line
    txt = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*[aA4@]\s*[\.\:\)]\s*', r'\n(A) ', txt)
    txt = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*[bB8®]\s*[\.\:\)]\s*', r'\n(B) ', txt)
    txt = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*[cC©]\s*[\.\:\)]\s*', r'\n(C) ', txt)
    txt = re.sub(r'(?:^|\n)\s*[_\-•*~;:\'\"\s]*(?:[dD0O]|Dy)\s*[\.\:\)]\s*', r'\n(D) ', txt)
    
    # Special standalone replacements
    txt = re.sub(r'(?:^|\n)\s*®\s*', r'\n(B) ', txt)
    txt = re.sub(r'(?:^|\n)\s*©\s*', r'\n(C) ', txt)

    splits = re.split(r'\n\s*\(([A-D])\)\s*', '\n' + txt)
    q_stem = clean_ocr(splits[0].strip())
    opts = {}
    for i in range(1, len(splits), 2):
        letter = splits[i]
        opt_text = clean_ocr(splits[i+1].strip())
        # Clean trailing noise or option leakage
        opt_lines = [l.strip() for l in opt_text.splitlines() if l.strip()]
        opts[letter] = " ".join(opt_lines)
    return q_stem, opts

all_qs = p.all_questions
incomplete = []
for q in range(1, 151):
    q_stem, opts = parse_question_options(all_qs[q], q)
    missing_opts = [l for l in ['A', 'B', 'C', 'D'] if l not in opts or not opts[l]]
    if missing_opts:
        incomplete.append((q, missing_opts, opts, all_qs[q][:90]))

print(f'Completely structured: {150 - len(incomplete)} / 150')
if incomplete:
    print('Incomplete count:', len(incomplete))
    for item in incomplete:
        print(f"Q{item[0]:03d}: Missing {item[1]} -> Found {list(item[2].keys())}")
