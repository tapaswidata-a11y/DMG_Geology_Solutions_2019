import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def create_figure(q_dir, filename, draw_func):
    os.makedirs(q_dir, exist_ok=True)
    filepath = os.path.join(q_dir, filename)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    draw_func(ax)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300)
    plt.close()
    print(f"Generated: {filepath}")

# Q091: Arkose Sandstone - Folk QFL Ternary
def draw_q091(ax):
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.1, 1.1)
    ax.axis('off')
    ax.set_title('Q091: Folk (1968) Sandstone Classification Ternary Diagram\nArkose Field: Characterized by > 25% Feldspar Content', fontsize=13, fontweight='bold', pad=15)

    Q = np.array([0.5, 0.9])
    F = np.array([0.1, 0.1])
    L = np.array([0.9, 0.1])

    ax.plot([Q[0], F[0]], [Q[1], F[1]], 'k-', lw=1.5)
    ax.plot([F[0], L[0]], [F[1], L[1]], 'k-', lw=1.5)
    ax.plot([L[0], Q[0]], [L[1], Q[1]], 'k-', lw=1.5)

    ax.text(Q[0], Q[1]+0.04, 'QUARTZ (Q)', ha='center', fontweight='bold', fontsize=11, color='#2563eb')
    ax.text(F[0]-0.05, F[1]-0.04, 'FELDSPARS (F)\n(> 25% for Arkose)', ha='center', fontweight='bold', fontsize=9.5, color='#d97706')
    ax.text(L[0]+0.05, L[1]-0.04, 'LITHIC FRAGMENTS (L)\n(Rock fragments)', ha='center', fontweight='bold', fontsize=9.5, color='#059669')

    # 25% F line (parallel to Q-L)
    # Arkose field (Bottom-left)
    ax.add_patch(patches.Polygon([[0.1, 0.1], [0.35, 0.1], [0.38, 0.45], [0.22, 0.45]], facecolor='#fef08a', edgecolor='#ca8a04', lw=2))
    ax.text(0.26, 0.28, '★ ARKOSE ★\n(Feldspar > 25%)\n(Option C)', ha='center', va='center', fontweight='bold', fontsize=10, color='#854d0e')

    # Subarkose field (above Arkose)
    ax.add_patch(patches.Polygon([[0.22, 0.45], [0.38, 0.45], [0.44, 0.75], [0.35, 0.75]], facecolor='#ffedd5', edgecolor='#ea580c', lw=1.2))
    ax.text(0.35, 0.60, 'Subarkose\n(5-25% F)', ha='center', va='center', fontsize=8.5, color='#c2410c')

    # Quartzarenite field (top)
    ax.add_patch(patches.Polygon([[0.45, 0.80], [0.55, 0.80], [0.50, 0.90]], facecolor='#dbeafe', edgecolor='#1d4ed8', lw=1.2))
    ax.text(0.50, 0.83, 'Quartzarenite\n(Q > 95%)', ha='center', va='center', fontsize=8, color='#1e40af')

    # Key callout
    box = (
        "Pettijohn & Folk Petrographic Definition:\n"
        "• Arkose: Sandstone containing > 25% feldspar (dominantly K-feldspar / microcline).\n"
        "• Tectonic Setting: Fault-bounded rift basins (graben) adjacent to uplifted granitic basements.\n"
        "• Climate: Rapid erosion in arid or cold climates minimizing chemical weathering of feldspar."
    )
    ax.text(0.5, -0.05, box, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q091', 'arkose_sandstone_folk_ternary_feldspar.png', draw_q091)

# Q092: Udden-Wentworth Grain Size Scale - Silt Grade (1/16 to 1/256 mm)
def draw_q092(ax):
    ax.set_xlim(-10, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('Q092: Udden-Wentworth Grain Size Scale for Detrital Sediments\nSilt Grade Size Range: 1/16 mm to 1/256 mm (+4 phi to +8 phi)', fontsize=13, fontweight='bold', pad=15)

    grades = [
        ('GRAVEL / BOULDER\n> 2 mm\n(phi < -1)', -8, 4, '#e2e8f0', '#64748b', False),
        ('SAND GRADE\n2 mm to 1/16 mm\n(0.0625 mm)\n(phi: -1 to +4)', -4, 4, '#fed7aa', '#ea580c', False),
        ('★ SILT GRADE ★\n1/16 mm to 1/256 mm\n(0.0625 to 0.0039 mm)\n(phi: +4 to +8)\n(Option A)', 0, 4, '#fef08a', '#ca8a04', True),
        ('CLAY GRADE\n< 1/256 mm\n(< 0.0039 mm)\n(phi > +8)', 4, 4, '#dcfce7', '#16a34a', False)
    ]

    for label, x, width, fc, ec, bold in grades:
        lw = 2.5 if bold else 1.2
        ax.add_patch(patches.Rectangle((x, 4.5), width, 2.5, facecolor=fc, edgecolor=ec, lw=lw))
        ax.text(x + width/2, 5.75, label, ha='center', va='center', fontweight='bold', fontsize=9.5)

    scale_text = (
        "Standard Wentworth (1922) Particle Size Classes:\n"
        "• Boulder: > 256 mm | Cobble: 64 to 256 mm | Pebble: 4 to 64 mm | Granule: 2 to 4 mm\n"
        "• Sand: 2 mm (2000 um) down to 1/16 mm (62.5 um)\n"
        "• Silt: 1/16 mm (62.5 um) down to 1/256 mm (3.9 um) [Divided into Coarse, Medium, Fine, Very Fine]\n"
        "• Clay: Less than 1/256 mm (< 3.9 um) [Colloidal and phyllosilicate dominated]"
    )
    ax.text(0, 2.0, scale_text, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#64748b', lw=1.5))

create_figure('figures_2019_Q092', 'udden_wentworth_grain_size_scale_silt_grade.png', draw_q092)

# Q093: Clay Galls in Sandstone
def draw_q093(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q093: Genesis & Structure of Clay Galls (Mud Galls / Rip-Up Clasts)\nFlat or Lens-Shaped Hardened Clay Leaves Deposited in Sandstone Beds', fontsize=12.5, fontweight='bold', pad=15)

    # Cross section of sandstone
    ax.add_patch(patches.Rectangle((1, 2), 8, 4.5, facecolor='#fef3c7', edgecolor='#b45309', lw=2))
    ax.text(1.5, 6.0, 'Host Sandstone Bed (Cross-bedded or Massive Sand)', fontsize=10, fontweight='bold', color='#92400e')

    # Clay galls (lenticular, flat leaves)
    galls = [
        (2.5, 3.5, 1.2, 0.25, 15),
        (4.5, 4.2, 1.5, 0.3, -10),
        (6.5, 3.2, 1.1, 0.2, 5),
        (3.8, 2.8, 1.4, 0.25, 20),
        (7.2, 4.8, 1.0, 0.22, -15),
        (5.5, 5.0, 1.3, 0.28, 8)
    ]
    for x, y, w, h, angle in galls:
        ellipse = patches.Ellipse((x, y), w, h, angle=angle, facecolor='#64748b', edgecolor='#1e293b', lw=1.5)
        ax.add_patch(ellipse)

    ax.text(5.0, 3.6, '★ Clay Galls (Mud Galls) ★\nFlat / Lenticular Discs of Desiccated Clay\nRipped up and redeposited by currents', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#0f172a', bbox=dict(boxstyle='round,pad=0.4', facecolor='#e2e8f0', edgecolor='#475569'))

    desc = (
        "Petrogenetic Cycle of Clay Galls (Pettijohn, 1975; Bangar, p. 134):\n"
        "1. Mud deposited in floodplain, playa, or tidal flat dries out and cracks under the sun (mudcracks).\n"
        "2. The hardened sun-baked clay curled up into thin flakes ('leaves of clay').\n"
        "3. A violent flood current tears up these clay leaves (mud rip-up clasts), rolls and rounds them slightly.\n"
        "4. They are deposited as flat, lens-shaped 'clay galls' embedded within overlying sand strata."
    )
    ax.text(5.0, 0.8, desc, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q093', 'clay_galls_mud_rip_up_clasts_sandstone.png', draw_q093)

# Q094: Clast Size - Cobble (64 to 256 mm)
def draw_q094(ax):
    ax.axis('off')
    ax.set_title('Q094: Coarse Clastic Sedimentary Rock Grain Sizes (Udden-Wentworth)\nCobble: Rounded Clasts between 64 mm and 256 mm Diameter', fontsize=12.5, fontweight='bold', pad=15)

    clasts = [
        ('BOULDER', '> 256 mm\n(> 10 inches)', 0.15, 0.65, '#cbd5e1', '#475569', 1.8),
        ('★ COBBLE ★\n(Option C)', '64 mm to 256 mm\n(2.5 to 10 inches)', 0.45, 0.65, '#fef08a', '#ca8a04', 1.3),
        ('PEBBLE', '4 mm to 64 mm\n(0.16 to 2.5 inches)', 0.72, 0.65, '#fed7aa', '#ea580c', 0.8),
        ('GRANULE', '2 mm to 4 mm', 0.90, 0.65, '#dcfce7', '#16a34a', 0.4)
    ]

    for name, size, x, y, fc, ec, scale in clasts:
        lw = 2.5 if 'COBBLE' in name else 1.2
        # draw circular clast
        circle = patches.Circle((x, y), 0.08 * scale, facecolor=fc, edgecolor=ec, lw=lw)
        ax.add_patch(circle)
        ax.text(x, y - 0.18, name, ha='center', va='top', fontweight='bold', fontsize=9.5)
        ax.text(x, y - 0.28, size, ha='center', va='top', fontsize=8.5, color='#475569')

    comp_box = (
        "Wentworth Coarse Clast Definitions:\n"
        "• Boulder: Any clast > 256 mm diameter (human head sized to giant house sized).\n"
        "• Cobble: Clasts between 64 mm and 256 mm diameter (fist to grapefruit sized).\n"
        "• Pebble: Clasts between 4 mm and 64 mm diameter (divided into coarse, medium, fine).\n"
        "• Granule: Clasts between 2 mm and 4 mm (very fine gravel grade).\n"
        "• When consolidated: Rounded clasts form Conglomerate; angular clasts form Sedimentary Breccia."
    )
    ax.text(0.5, 0.12, comp_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q094', 'clast_size_classification_cobble_pebble_boulder.png', draw_q094)

# Q095: Current Bedding / Cross-Stratification
def draw_q095(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q095: Cross-Bedding Architecture: Current Beds (False Bedding)\nInclined Bedding Planes Formed by Unidirectional Current Flow', fontsize=12.5, fontweight='bold', pad=15)

    # Main horizontal bounding planes
    ax.plot([0.5, 9.5], [6.0, 6.0], 'k-', lw=2.5, label='Upper Master Bedding Plane')
    ax.plot([0.5, 9.5], [2.5, 2.5], 'k-', lw=2.5, label='Lower Master Bedding Plane')

    # Current flow arrow
    ax.annotate('', xy=(8.5, 6.8), xytext=(1.5, 6.8), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=4))
    ax.text(5.0, 7.2, 'CURRENT FLOW DIRECTION (Palaeocurrent)', color='#dc2626', fontweight='bold', fontsize=11, ha='center')

    # Inclined foreset beds (current beds)
    for x_start in np.linspace(1.5, 8.0, 12):
        # arc dipping down-current
        x_pts = np.linspace(x_start, x_start + 1.2, 50)
        y_pts = 2.5 + 3.5 / (1 + np.exp(3.5 * (x_pts - (x_start + 0.6))))
        ax.plot(x_pts, y_pts, color='#ca8a04', lw=1.8)

    ax.text(5.0, 4.5, '★ CURRENT BEDS ★\n(Inclined Foreset Strata)\nDipping in current flow direction\n(Option B)', ha='center', va='center', fontweight='bold', fontsize=10.5, color='#854d0e', bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef08a', edgecolor='#ca8a04', lw=2))

    desc = (
        "Morphological Elements of Current Bedding (K.M. Bangar, p. 132; Boggs, 2014):\n"
        "• Current Beds (Cross-beds): Inclined lamina formed on the lee side of migrating ripples/dunes.\n"
        "• Topset: Gently dipping upper beds, often truncated by subsequent erosional scours.\n"
        "• Foreset: Steeply inclined beds meeting bottomset tangentially (asymptotic base indicates right way up).\n"
        "• Geopetal Criterion: Truncation at top, asymptotic tangential contact at base."
    )
    ax.text(5.0, 1.0, desc, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q095', 'current_bedding_cross_stratification_geometry.png', draw_q095)

# Q096: Diagenesis - Compaction and Cementation
def draw_q096(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q096: The Realm of Diagenesis: Compaction and Cementation\nPost-Depositional Lithification of Sediments Prior to Metamorphism', fontsize=12.5, fontweight='bold', pad=15)

    stages = [
        ("1. DEPOSITION\nLoose sediment grains\nPorosity: 40 - 70%\nPore water filled", 1.8, 5.5, '#e0f2fe', '#0284c7'),
        ("2. COMPACTION\nBurial overburden load\nPore volume reduced\nGrains reoriented", 5.0, 5.5, '#fef08a', '#ca8a04'),
        ("3. CEMENTATION\nPrecipitation of calcite,\nquartz, iron oxides in pores\nSolid rock formed", 8.2, 5.5, '#dcfce7', '#16a34a')
    ]

    for title, x, y, fc, ec in stages:
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=2))
        if x < 8.0:
            ax.annotate('', xy=(x+1.5, y), xytext=(x+1.1, y), arrowprops=dict(arrowstyle="->", color='#475569', lw=2.5))

    # Big overarching Diagenesis bracket
    ax.add_patch(patches.Rectangle((0.5, 3.8), 9.0, 2.8, fill=False, edgecolor='#dc2626', linestyle='--', lw=2))
    ax.text(5.0, 3.9, '★ DIAGENESIS (Option D) ★ (T < 200°C, P < 2 kbar)', ha='center', va='bottom', color='#dc2626', fontweight='bold', fontsize=11)

    notes = (
        "Diagenetic Processes and Environments (Boggs, 2014; Bangar, p. 130):\n"
        "• Compaction: Physical rearrangement of grains and dewatering under lithostatic pressure.\n"
        "• Cementation: Chemical precipitation of mineral authigenic cements binding loose grains.\n"
        "• Common Cements: Calcite, Silica (quartz overgrowths/chert), Hematite/Goethite, Clay minerals.\n"
        "• Boundary with Metamorphism: Occurs when temperature exceeds ~200°C (anchizone / greenschist)."
    )
    ax.text(5.0, 1.8, notes, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q096', 'sedimentary_diagenesis_compaction_cementation.png', draw_q096)

# Q097: Oscillation Ripples in Beach Environment
def draw_q097(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q097: Oscillation (Wave) Ripples Formed in Beach / Nearshore Environment\nSymmetrical Profiles Generated by Bidirectional Water Orbital Motion', fontsize=12.5, fontweight='bold', pad=15)

    # Water surface
    ax.plot([0.5, 9.5], [6.8, 6.8], color='#38bdf8', lw=2, linestyle='-')
    ax.text(5.0, 7.2, 'SHALLOW WATER BODY (Above Wave Base - Beach / Littoral Shelf)', color='#0284c7', fontweight='bold', fontsize=10.5, ha='center')

    # Orbital wave circles
    for x in [2.5, 5.0, 7.5]:
        ellipse = patches.Ellipse((x, 5.5), 1.2, 0.7, fill=False, edgecolor='#0284c7', lw=1.5, linestyle=':')
        ax.add_patch(ellipse)
        ax.annotate('', xy=(x+0.5, 5.7), xytext=(x+0.4, 5.8), arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.5))
        ax.annotate('', xy=(x-0.5, 5.3), xytext=(x-0.4, 5.2), arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.5))

    # Symmetrical ripple profile
    x_rip = np.linspace(1, 9, 200)
    y_rip = 2.5 + 0.8 * np.sin(2 * np.pi * (x_rip - 1) / 2)**2
    ax.fill_between(x_rip, 1.0, y_rip, color='#fef08a', edgecolor='#ca8a04', lw=2)
    ax.plot(x_rip, y_rip, color='#ca8a04', lw=2)

    # Crest markers
    for x_c in [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]:
        ax.plot([x_c, x_c], [2.5, 3.4], 'r--', lw=1)

    ax.text(5.0, 3.9, '★ SYMMETRICAL OSCILLATION RIPPLES ★\nSharp Crests + Broad Rounded Troughs\n(Beach Environment - Option B)', ha='center', va='center', fontweight='bold', fontsize=10, color='#854d0e', bbox=dict(boxstyle='round,pad=0.4', facecolor='#fffbeb', edgecolor='#f59e0b'))

    diff_box = (
        "Oscillation Ripples vs. Current Ripples (Bangar, p. 133; Boggs, 2014):\n"
        "• Oscillation (Wave) Ripples: Symmetrical crests; bidirectional oscillatory flow; formed on beaches, lakes, lagoons.\n"
        "• Current Ripples: Asymmetrical profile (gentle stoss side, steep lee side); unidirectional flow in rivers & deserts.\n"
        "• Ripple Index ($L/H$): Wave ripples have $L/H < 10$; current ripples typically have $L/H > 15$."
    )
    ax.text(5.0, 0.5, diff_box, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q097', 'oscillation_ripples_symmetrical_wave_action.png', draw_q097)

# Q098: Ferroan Calcite Cement - Deep Burial Diagenesis
def draw_q098(ax):
    ax.axis('off')
    ax.set_title('Q098: Carbonate Diagenetic Realms & Ferroan Calcite Cement\nIncorporation of Fe2+ in Calcite Lattice Signifies Anoxic Deep Burial Diagenesis', fontsize=12.5, fontweight='bold', pad=15)

    realms = [
        ('METEORIC VADOSE\n(Above water table)\nOxidizing (High Eh)\nFe3+ oxides precipitated\nNon-ferroan calcite', 0.2, 0.65, '#fef3c7', '#d97706'),
        ('METEORIC PHREATIC\n(Below water table, shallow)\nSuboxic / Oxidizing\nNon-ferroan to\nweakly zoned calcite', 0.5, 0.65, '#dbeafe', '#2563eb'),
        ('★ DEEP BURIAL ZONE ★\n(Isolated from atmosphere)\nDeep Anoxic Reducing (Low Eh)\nFe2+ stable & substitutes for Ca2+\nFERROAN CALCITE CEMENT\n(Option A)', 0.8, 0.65, '#fef08a', '#dc2626')
    ]

    for title, x, y, fc, ec in realms:
        lw = 2.5 if 'DEEP' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    ax.annotate('', xy=(0.68, 0.65), xytext=(0.62, 0.65), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=2.5))
    ax.annotate('', xy=(0.38, 0.65), xytext=(0.32, 0.65), arrowprops=dict(arrowstyle="->", color='#475569', lw=2))

    chem_box = (
        "Chemical & Petrographic Principles (Tucker & Wright, 1990; Scholle, 1978):\n"
        "• In oxidizing near-surface waters, iron is insoluble $Fe^{3+}$ (forming hematite/limonite staining).\n"
        "• Under deep burial conditions (anaerobic, reducing bacterial sulphate reduction), $Fe^{3+} \\rightarrow Fe^{2+}$.\n"
        "• $Fe^{2+}$ (ionic radius 0.78 A) readily substitutes for $Ca^{2+}$ (1.00 A) in the calcite crystal lattice.\n"
        "• Diagnostic Test: Dickson's potassium ferricyanide stain turns ferroan calcite a brilliant blue-purple."
    )
    ax.text(0.5, 0.18, chem_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q098', 'ferroan_calcite_cement_deep_burial_diagenesis.png', draw_q098)

# Q099: Syn-sedimentary Deformation - High Sedimentation
def draw_q099(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q099: Soft-Sediment (Syn-Sedimentary) Deformation Structures\nTriggered by Rapid, High Sedimentation Rates and Pore-Fluid Overpressuring', fontsize=12.5, fontweight='bold', pad=15)

    # Upper dense sand bed
    ax.fill([1, 9, 9, 1], [4.5, 4.5, 6.5, 6.5], color='#fed7aa')
    ax.text(5.0, 5.8, 'Dense, Rapidly Deposited Sand Layer (High Overburden Load)', ha='center', fontweight='bold', fontsize=10, color='#9a3412')

    # Flame structures penetrating upward
    flames_x = [2.0, 3.8, 5.5, 7.2]
    for fx in flames_x:
        ax.fill([fx-0.3, fx, fx+0.3], [3.0, 4.8, 3.0], color='#64748b')
        ax.plot([fx-0.3, fx, fx+0.3], [3.0, 4.8, 3.0], color='#1e293b', lw=1.5)

    # Lower water-rich mud layer
    ax.fill([1, 9, 9, 1], [1.5, 1.5, 3.0, 3.0], color='#64748b')
    ax.text(5.0, 2.0, 'Undercompacted, Water-Saturated Mud Substratum (Liquefied)', ha='center', fontweight='bold', fontsize=10, color='white')

    ax.text(5.0, 3.8, '★ Flame & Ball-and-Pillow Structures ★\nDensity inversion caused by HIGH SEDIMENTATION\n(Option D)', ha='center', va='center', fontweight='bold', fontsize=10, color='#831843', bbox=dict(boxstyle='round,pad=0.5', facecolor='#fbcfe8', edgecolor='#be185d', lw=2))

    callout = (
        "Mechanisms of Syn-Sedimentary Deformation (Collinson et al., 2006):\n"
        "• Rapid 'dumping' of sediment prevents orderly dewatering, producing excess pore-fluid pressure.\n"
        "• Reverse density gradient (dense sand overlying unconsolidated soupy mud) triggers Rayleigh-Taylor instability.\n"
        "• Classic Structures: Flame structures, ball-and-pillow, convolute bedding, sand volcanoes, slump folds."
    )
    ax.text(5.0, 0.6, callout, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q099', 'syn_sedimentary_deformation_convolute_flame_structures.png', draw_q099)

# Q100: Sedimentary Skewness - Organic Detritus / Coarse Tail
def draw_q100(ax):
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Grain Size (phi scale: Coarse on left, Fine on right)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Relative Frequency', fontsize=11, fontweight='bold')
    ax.set_title('Q100: Grain Size Skewness (Folk & Ward, 1957; Friedman, 1961)\nOrganic / Bioclastic Detritus Imparts Negative Skewness (Coarse Tail)', fontsize=12.5, fontweight='bold', pad=15)

    x = np.linspace(-4, 4, 200)

    # Normal curve (Sk = 0)
    y_norm = np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)
    ax.plot(x, y_norm, 'k--', label='Normal Distribution (Sk = 0)', lw=1.5)

    # Negatively skewed (tail toward negative phi / coarse) - Highlighted
    # skew toward negative x (coarse side)
    y_neg = np.exp(-0.5 * (x - 0.5)**2) * (1 - 0.6 * np.tanh(x)) / np.sqrt(2 * np.pi)
    ax.plot(x, y_neg, color='#dc2626', lw=2.5, label='★ Negative Skewness (Coarse Shell Tail - Option C) ★')
    ax.fill_between(x[x < -0.5], 0, y_neg[x < -0.5], color='#fee2e2', alpha=0.7)

    # Positively skewed (tail toward positive phi / fine)
    y_pos = np.exp(-0.5 * (x + 0.5)**2) * (1 + 0.6 * np.tanh(x)) / np.sqrt(2 * np.pi)
    ax.plot(x, y_pos, color='#2563eb', lw=1.5, label='Positive Skewness (Fine Tail - Silt/Clay)')

    ax.text(-2.5, 0.45, 'COARSE TAIL\n(Mollusc shells &\norganic detritus)', color='#dc2626', fontweight='bold', fontsize=9.5, ha='center')
    ax.text(2.5, 0.45, 'FINE TAIL\n(Excess silt/clay)', color='#2563eb', fontweight='bold', fontsize=9.5, ha='center')

    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, linestyle=':', alpha=0.6)

create_figure('figures_2019_Q100', 'sedimentary_skewness_grain_size_distribution.png', draw_q100)

# Q101: Shallow Marine Palaeocurrents (Bimodal & Polymodal)
def draw_q101(ax):
    ax.axis('off')
    ax.set_title('Q101: Palaeocurrent Distribution Patterns by Sedimentary Environment\nShallow Marine Regimes Feature Both Bimodal (Tidal) and Polymodal (Storm/Wave) Patterns', fontsize=12, fontweight='bold', pad=15)

    patterns = [
        ('FLUVIAL (River Channels)\nUNIMODAL\nSingle dominant down-slope direction', 0.2, 0.65, '#dbeafe', '#1d4ed8'),
        ('★ SHALLOW MARINE / TIDAL ★\nBIMODAL (Bipolar Herringbone)\nFlood vs. Ebb tidal currents (180° opposite)', 0.5, 0.65, '#fef08a', '#ca8a04'),
        ('★ SHELF / MARINE STORM ★\nPOLYMODAL\nMultiple directions: Tides + Waves + Storm surges\n(Option D: Both Bimodal & Polymodal)', 0.8, 0.65, '#dcfce7', '#16a34a')
    ]

    for title, x, y, fc, ec in patterns:
        lw = 2.5 if 'SHALLOW' in title or 'SHELF' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    palaeo_box = (
        "Palaeocurrent Systematics (Pettijohn, Potter & Siever, 1987; Boggs, 2014):\n"
        "• Fluvial: Unimodal vector distributions with narrow spread pointing down depositional paleoslope.\n"
        "• Shallow Marine (Tidal): Bimodal bipolar (two opposite modes 180° apart) due to flood and ebb tides.\n"
        "• Shallow Marine (Shelf/Shoreface): Polymodal patterns produced by interplay of tides, longshore currents, and wave refractions.\n"
        "• Hence, shallow marine environments characteristically exhibit BOTH bimodal and polymodal patterns."
    )
    ax.text(0.5, 0.20, palaeo_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q101', 'palaeocurrent_rose_diagram_shallow_marine.png', draw_q101)

# Q102: Miogeosyncline vs Eugeosyncline
def draw_q102(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q102: Classical Geosynclinal Theory (Kay, 1951; Stille, 1940)\nMiogeosyncline: Thinner Non-Volcanic Sediments Adjacent to Stable Craton', fontsize=12.5, fontweight='bold', pad=15)

    # Craton (Left)
    ax.fill([0, 3, 3, 0], [2, 2, 6, 6], color='#cbd5e1')
    ax.text(1.5, 4.5, 'STABLE\nCRATON\n(Shield / Platform)', ha='center', va='center', fontweight='bold', fontsize=10, color='#1e293b')

    # Miogeosyncline (Center) - Highlighted
    ax.fill([3, 6, 6, 3], [1.5, 1.5, 4.5, 4.5], color='#fef08a', edgecolor='#ca8a04', lw=2.5)
    ax.text(4.5, 3.2, '★ MIOGEOSYNCLINE ★\n(Option B)\n• Adjacent to craton\n• Thinner sediments (shallow marine)\n• NO volcanic rocks (Avolcanic)', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#854d0e')

    # Eugeosyncline (Right)
    ax.fill([6, 9.5, 9.5, 6], [0.5, 0.5, 3.5, 3.5], color='#fed7aa', edgecolor='#ea580c', lw=2)
    ax.text(7.75, 2.2, 'EUGEOSYNCLINE\n• Deep oceanward trench\n• Thick greywacke / flysch\n• ABUNDANT volcanics (ophiolites)', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#9a3412')

    box = (
        "Kay's (1951) Geosynclinal Terminology:\n"
        "• Orthogeosyncline: Linear mobile belt divided into Miogeosyncline (inner) and Eugeosyncline (outer).\n"
        "• Miogeosyncline: Non-volcanic basin bordering the cratonic borderland; orthoquartzite-carbonate suite.\n"
        "• Modern Plate Tectonic Analog: Miogeosyncline = Passive continental shelf; Eugeosyncline = Forearc/accretionary prism."
    )
    ax.text(5.0, 0.7, box, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q102', 'miogeosyncline_vs_eugeosyncline_craton_margin.png', draw_q102)

# Q103: Greywacke Clay Matrix
def draw_q103(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q103: Greywacke Petrography & Matrix Mineralogy\nCharacterized by Abundant Detrital Matrix (>15%) Principally Made of Clay Minerals', fontsize=12.5, fontweight='bold', pad=15)

    # Matrix background (dark clay paste)
    ax.add_patch(patches.Rectangle((1, 2), 8, 4.5, facecolor='#94a3b8', edgecolor='#334155', lw=2))
    ax.text(1.2, 6.1, 'Matrix: Pervasive paste of Clay Minerals (Illite, Smectite), Chlorite & Sericite (> 15% to 50%)', fontsize=9, fontweight='bold', color='#0f172a')

    # Angular unsorted grains of quartz and lithics
    grains = [
        [(2.0, 3.5), (2.5, 4.2), (2.8, 3.6), (2.2, 3.2)], # quartz
        [(4.0, 4.8), (4.5, 5.2), (4.8, 4.5), (4.2, 4.0)], # feldspar
        [(6.0, 3.2), (6.8, 3.8), (6.5, 2.8)], # lithic
        [(3.5, 2.5), (4.2, 3.0), (3.8, 2.2)],
        [(7.0, 4.8), (7.8, 5.2), (7.5, 4.2)]
    ]
    for poly in grains:
        ax.add_patch(patches.Polygon(poly, facecolor='#fef08a', edgecolor='#ca8a04', lw=1.5))

    ax.text(5.0, 3.8, '★ GREYWACKE ★\n(Wacke Sandstone)\nAngular grains embedded in abundant CLAY MATRIX\n(Option C)', ha='center', va='center', fontweight='bold', fontsize=10, color='#854d0e', bbox=dict(boxstyle='round,pad=0.5', facecolor='#fffbeb', edgecolor='#ca8a04', lw=2))

    notes = (
        "Sandstone Matrix Classifications (Dott, 1964; Pettijohn, 1975):\n"
        "• Arenite: Matrix-poor sandstone (< 15% matrix); grain-supported.\n"
        "• Wacke (Greywacke): Matrix-rich sandstone (15% to 50% clay-chlorite matrix); matrix-supported.\n"
        "• Siltstone is composed of silt-sized quartz grains (1/16-1/256 mm), not clay minerals.\n"
        "• Arkose has < 15% matrix, dominated by framework feldspar."
    )
    ax.text(5.0, 0.8, notes, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q103', 'greywacke_clay_matrix_peteology_dott.png', draw_q103)

# Q104: Graded Bedding in Turbidite (Bouma Sequence)
def draw_q104(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q104: Primary Depositional Sedimentary Structure: Graded Bedding\nNormal Grading in Turbidites (Bouma Ta Division): Coarse Base to Fine Top', fontsize=12.5, fontweight='bold', pad=15)

    # Sediment column
    ax.add_patch(patches.Rectangle((2.5, 1.5), 5.0, 5.5, facecolor='#f8fafc', edgecolor='#1e293b', lw=2))

    # Top: Fine mud/clay (Ta/Te)
    ax.fill([2.5, 7.5, 7.5, 2.5], [5.8, 5.8, 7.0, 7.0], color='#cbd5e1')
    ax.text(5.0, 6.4, 'TOP: Fine Clay & Silt (Pelagic / Suspension Settling)', ha='center', va='center', fontweight='bold', fontsize=9)

    # Middle: Medium to fine sand
    ax.fill([2.5, 7.5, 7.5, 2.5], [4.0, 4.0, 5.8, 5.8], color='#fed7aa')
    ax.text(5.0, 4.9, 'MIDDLE: Medium to Fine Sand', ha='center', va='center', fontweight='bold', fontsize=9.5)

    # Bottom: Coarse sand & granules
    ax.fill([2.5, 7.5, 7.5, 2.5], [1.5, 1.5, 4.0, 4.0], color='#fef08a')
    # Draw pebbles/grains at base
    for gx in np.linspace(3.0, 7.0, 8):
        circle = patches.Circle((gx, 2.2), 0.25, facecolor='#64748b', edgecolor='#1e293b')
        ax.add_patch(circle)
    ax.text(5.0, 3.2, 'BASE: Coarse Sand & Pebbles (Fastest Settling)', ha='center', va='center', fontweight='bold', fontsize=9.5)

    # Grain size gradient arrow
    ax.annotate('', xy=(1.8, 6.8), xytext=(1.8, 1.8), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=3))
    ax.text(1.3, 4.3, 'GRAIN SIZE DECREASING UPWARD\n(Normal Grading)', color='#dc2626', fontweight='bold', fontsize=9, rotation=90, va='center')

    ax.text(5.0, 0.6, '★ GRADED BEDDING ★ (Depositional Structure formed by waning currents - Option A)', ha='center', fontsize=9.5, fontweight='bold', bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'))

create_figure('figures_2019_Q104', 'graded_bedding_bouma_sequence_turbidite.png', draw_q104)

# Q105: Coquina - Limestone of Organic Detritus
def draw_q105(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q105: Coquina: Bioclastic Limestone Made of Organic Detritus\nCoarse Mechanical Accumulation of Shell Fragments and Skeletal Debris (>75%)', fontsize=12.5, fontweight='bold', pad=15)

    # Shell accumulation box
    ax.add_patch(patches.Rectangle((1, 2), 8, 4.5, facecolor='#fef3c7', edgecolor='#b45309', lw=2))
    ax.text(1.3, 6.1, 'Coquina Fabric: Loosely cemented bioclasts with high interstitial porosity', fontsize=9.5, fontweight='bold', color='#92400e')

    # Curved shell shapes
    shells = [
        (2.5, 4.5, 1.2, 0.6, 20),
        (4.2, 3.2, 1.4, 0.7, -15),
        (6.0, 4.8, 1.3, 0.5, 40),
        (7.5, 3.5, 1.1, 0.6, -30),
        (3.5, 5.0, 1.0, 0.5, 10),
        (5.5, 2.5, 1.3, 0.6, -5)
    ]
    for x, y, w, h, angle in shells:
        arc = patches.Arc((x, y), w, h, angle=angle, theta1=0, theta2=180, edgecolor='#be185d', lw=2.5)
        ax.add_patch(arc)

    ax.text(5.0, 3.8, '★ COQUINA ★\n(Bioclastic Organic Limestone)\nConsists predominantly of broken molluscan shell debris\n(Option B)', ha='center', va='center', fontweight='bold', fontsize=10.5, color='#831843', bbox=dict(boxstyle='round,pad=0.5', facecolor='#fbcfe8', edgecolor='#be185d', lw=2))

    def_box = (
        "Classification of Carbonate Rocks (Dunham, 1962; Folk, 1962; Bangar, p. 138):\n"
        "• Coquina: Detrital organic limestone composed almost entirely of loosely cemented shell fragments.\n"
        "• Coquinite: Consolidated, thoroughly lithified firm equivalent of coquina.\n"
        "• Oolite: Chemical limestone composed of spherical, concentrically laminated ooids.\n"
        "• Calc-tufa: Spongy porous freshwater calcium carbonate precipitated around springs and waterfalls."
    )
    ax.text(5.0, 0.8, def_box, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q105', 'coquina_fossiliferous_organic_detritus_limestone.png', draw_q105)
