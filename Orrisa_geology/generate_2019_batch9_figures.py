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

# Q106: Unconfined Compressive Strength (UCS) Test
def draw_q106(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q106: Unconfined Compressive Strength (UCS) of Building Stones\nThe Fundamental Index Property of Intact Rock (sigma3 = 0, Axial Load = sigma1)', fontsize=12.5, fontweight='bold', pad=15)

    # Testing platen Top & Bottom
    ax.add_patch(patches.Rectangle((3.5, 6.2), 3.0, 0.8, facecolor='#475569', edgecolor='#1e293b', lw=2))
    ax.text(5.0, 6.6, 'UPPER STEEL PLATEN', color='white', ha='center', va='center', fontweight='bold', fontsize=9.5)

    ax.add_patch(patches.Rectangle((3.5, 1.0), 3.0, 0.8, facecolor='#475569', edgecolor='#1e293b', lw=2))
    ax.text(5.0, 1.4, 'LOWER STEEL PLATEN', color='white', ha='center', va='center', fontweight='bold', fontsize=9.5)

    # Cylindrical rock core
    ax.add_patch(patches.Rectangle((4.0, 1.8), 2.0, 4.4, facecolor='#fef08a', edgecolor='#ca8a04', lw=2.5))
    ax.text(5.0, 4.0, 'ROCK CORE\nSPECIMEN\nL/D = 2.0 to 2.5\n(Unconfined: sigma3 = 0)', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#854d0e')

    # Shear failure crack
    ax.plot([4.2, 5.8], [2.2, 5.8], 'r--', lw=2.5)

    # Axial force arrows
    ax.annotate('', xy=(5.0, 6.2), xytext=(5.0, 7.5), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=3.5))
    ax.text(5.0, 7.7, 'Axial Compressive Load (P)', color='#dc2626', ha='center', fontweight='bold', fontsize=10.5)

    ax.annotate('', xy=(5.0, 1.0), xytext=(5.0, 0.2), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=3.5))

    # Formula Box
    formula = (
        "IS: 9143 / ASTM D7012 Unconfined Compressive Strength (UCS):\n"
        "• UCS = P_failure / A (Peak failure load divided by cross-sectional area).\n"
        "• Conducted without lateral confining pressure (sigma3 = 0) -> 'UNCONFINED' (Option D).\n"
        "• Serves as the premier index property for rock mass classification (RMR, Q-system)."
    )
    ax.text(0.5, 3.8, formula, fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q106', 'unconfined_compressive_strength_ucs_test.png', draw_q106)

# Q107: Compressive Strength Stress-Strain Curve
def draw_q107(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Axial Strain epsilon (%)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Compressive Stress sigma (MPa)', fontsize=11, fontweight='bold')
    ax.set_title('Q107: Complete Stress-Strain Behavior of Intact Rock Under Compression\nCompressive Strength: Maximum Force Per Unit Area Withstood Without Rupturing', fontsize=12, fontweight='bold', pad=15)

    strain = np.linspace(0, 6, 200)
    # Stress curve peaking at (4.5, 85) and then post-peak softening
    stress = 85 * (strain / 4.5) * np.exp(1 - strain / 4.5)

    ax.plot(strain, stress, color='#1d4ed8', lw=3, label='Stress-Strain Curve')

    # Peak point
    ax.plot(4.5, 85, 'ro', markersize=10)
    ax.annotate('★ PEAK COMPRESSIVE STRENGTH ★\n(Maximum stress before rupture = 85 MPa)\n(Option C)', xy=(4.5, 85), xytext=(5.5, 75), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=2), fontweight='bold', fontsize=9.5, bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626'))

    # Rupture point
    ax.plot(5.8, 45, 'kx', markersize=12, markeredgewidth=3)
    ax.text(6.0, 42, 'Complete Physical Rupture', fontweight='bold', fontsize=9, color='#991b1b')

    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='lower right', fontsize=10)

create_figure('figures_2019_Q107', 'compressive_strength_stress_strain_curve.png', draw_q107)

# Q108: Compressive Strength Comparison Across Rock Types
def draw_q108(ax):
    rocks = ['Basalt\n(Igneous)', 'Granite\n(Igneous)', 'Dolerite\n(Igneous)', 'Quartzite\n(Metamorphic)', 'Gneiss\n(Metamorphic)', 'Sandstone\n(Sedimentary)', 'Limestone\n(Sedimentary)', 'Shale\n(Sedimentary)']
    strengths = [250, 210, 230, 180, 140, 65, 70, 25]
    colors = ['#dc2626', '#ef4444', '#b91c1c', '#3b82f6', '#60a5fa', '#f59e0b', '#fbbf24', '#d97706']

    bars = ax.bar(rocks, strengths, color=colors, edgecolor='#1e293b', lw=1.2)
    ax.set_ylabel('Unconfined Compressive Strength (MPa)', fontsize=11, fontweight='bold')
    ax.set_title('Q108: Comparative Unconfined Compressive Strength Across Rock Classes\nIgneous Rocks Possess Exceptionally High Compressive Strength (> 150 - 300 MPa)', fontsize=12, fontweight='bold', pad=15)
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    # Group bracket for Igneous
    ax.annotate('★ IGNEOUS ROCKS: HIGHEST STRENGTH ★\n(Dense, interlocking crystalline fabric)', xy=(1, 260), xytext=(1, 280), ha='center', fontweight='bold', fontsize=9.5, bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626'))

    for b in bars:
        h = b.get_height()
        ax.annotate(f'{h} MPa', xy=(b.get_x() + b.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')

create_figure('figures_2019_Q108', 'compressive_strength_rock_types_comparison.png', draw_q108)

# Q109: Porosity vs Void Ratio
def draw_q109(ax):
    ax.axis('off')
    ax.set_title('Q109: Porosity vs. Void Ratio in Rock & Soil Mechanics\nPorosity: Ratio of Total Pore Space Volume (Vv) to Total Rock Volume (Vt)', fontsize=12.5, fontweight='bold', pad=15)

    # 3-Phase column
    ax.add_patch(patches.Rectangle((0.15, 0.55), 0.3, 0.25, facecolor='#bae6fd', edgecolor='#0284c7', lw=1.5))
    ax.text(0.3, 0.675, 'PORE SPACES (Voids: Air + Water)\nVolume of Voids = Vv', ha='center', va='center', fontweight='bold', fontsize=9.5)

    ax.add_patch(patches.Rectangle((0.15, 0.15), 0.3, 0.40, facecolor='#fde047', edgecolor='#ca8a04', lw=1.5))
    ax.text(0.3, 0.35, 'SOLID MINERAL GRAINS\nVolume of Solids = Vs', ha='center', va='center', fontweight='bold', fontsize=9.5)

    # Total volume bracket
    ax.annotate('', xy=(0.47, 0.80), xytext=(0.47, 0.15), arrowprops=dict(arrowstyle="<->", color='#1e293b', lw=2))
    ax.text(0.49, 0.475, 'TOTAL ROCK\nVOLUME (Vt)\nVt = Vv + Vs', va='center', fontweight='bold', fontsize=9.5)

    # Formulas Side by Side
    formula_box = (
        "DEFINITIONS & MATHEMATICAL RELATIONSHIPS:\n\n"
        "★ POROSITY (n) [Option B]:\n"
        "   n = (Volume of Voids / Total Volume) * 100% = (Vv / Vt) * 100\n"
        "   Measures the fraction of total rock volume occupied by pore spaces.\n\n"
        "• VOID RATIO (e) [Option A]:\n"
        "   e = (Volume of Voids / Volume of Solids) = Vv / Vs\n\n"
        "• Interconversion: n = e / (1 + e)    and    e = n / (1 - n)"
    )
    ax.text(0.65, 0.45, formula_box, fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#64748b', lw=1.5))

create_figure('figures_2019_Q109', 'porosity_vs_void_ratio_rock_mechanics.png', draw_q109)

# Q110: Rock Bulk Density with Natural Moisture
def draw_q110(ax):
    ax.axis('off')
    ax.set_title('Q110: Rock Density Definitions: Dry vs. Saturated vs. Bulk Density\nBulk Density: Density of Rock Retaining its In-Situ Natural Moisture Content', fontsize=12.5, fontweight='bold', pad=15)

    densities = [
        ('DRY DENSITY (rho_d)\nRock oven-dried at 105°C\nPores contain only air\nrho_d = M_dry / Vt', 0.2, 0.65, '#f1f5f9', '#64748b'),
        ('★ BULK DENSITY (rho_b) ★\nRock with NATURAL moisture\nIn-situ field moisture state\nrho_b = M_natural / Vt\n(Option C)', 0.5, 0.65, '#fef08a', '#ca8a04'),
        ('SATURATED DENSITY (rho_sat)\nAll pores 100% water-filled\nVacuum saturated state\nrho_sat = M_sat / Vt', 0.8, 0.65, '#dbeafe', '#1d4ed8')
    ]

    for title, x, y, fc, ec in densities:
        lw = 2.5 if 'BULK' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    callout = (
        "IS: 13030 / ISRM Standard Guidelines on Density Determination:\n"
        "• Bulk Density (Natural Density): Mass of intact rock specimen containing its natural (in-situ) moisture\n"
        "  divided by its total bulk volume (Vt).\n"
        "• Typical Bulk Densities: Basalt ~ 2.85 - 3.00 g/cm3 | Granite ~ 2.65 - 2.75 g/cm3 | Sandstone ~ 2.20 - 2.50 g/cm3."
    )
    ax.text(0.5, 0.22, callout, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q110', 'rock_bulk_density_natural_moisture_content.png', draw_q110)

# Q111: Impact Testing of Stone - Toughness
def draw_q111(ax):
    ax.axis('off')
    ax.set_title('Q111: Mechanical Testing of Building Stones: Impact Test for Toughness\nResistance of Stones to Shattering Under Repeated Sudden Blows (Impact Loads)', fontsize=12, fontweight='bold', pad=15)

    tests = [
        ('CRUSHING TEST\n(Hydraulic Press)\nDetermines:\nCOMPRESSIVE\nSTRENGTH', 0.2, 0.65, '#e2e8f0', '#475569'),
        ('★ IMPACT TEST ★\n(Page Impact Machine / AIV)\nDetermines:\nTOUGHNESS\n(Option D)', 0.5, 0.65, '#fef08a', '#ca8a04'),
        ('ABRASION TEST\n(Los Angeles Machine)\nDetermines:\nHARDNESS /\nWEAR RESISTANCE', 0.8, 0.65, '#dcfce7', '#16a34a')
    ]

    for title, x, y, fc, ec in tests:
        lw = 2.5 if 'IMPACT' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    box = (
        "IS: 2386 / Page Impact Test Mechanics:\n"
        "• A standard 2 kg hammer drops from successive heights (1 cm, 2 cm, 3 cm...) until the stone specimen fractures.\n"
        "• The height of blow at failure (in cm) is recorded as the Toughness Index.\n"
        "• High Toughness (> 19): Highly tough (Dolerite, Basalt) | Moderate: 13-19 | Low (< 13): Brittle stones."
    )
    ax.text(0.5, 0.22, box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q111', 'impact_testing_toughness_page_impact_test.png', draw_q111)

# Q112: Rock Burst in Deep Tunneling
def draw_q112(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q112: Geotechnical Hazards in Deep Underground Tunneling: Rock Bursts\nSudden, Violent Explosive Release of High Strain Energy in Brittle Crystalline Rocks', fontsize=12, fontweight='bold', pad=15)

    # Deep rock mass
    ax.fill([0, 10, 10, 0], [0.5, 0.5, 7.5, 7.5], color='#cbd5e1')

    # Tunnel opening (circular)
    circle = patches.Circle((5, 4), 1.8, facecolor='#f8fafc', edgecolor='#1e293b', lw=2.5)
    ax.add_patch(circle)
    ax.text(5, 4, 'DEEP TUNNEL\nEXCAVATION\n(High in-situ stress: sigma_v)', ha='center', va='center', fontweight='bold', fontsize=9.5)

    # Explosive rock burst spalling on sidewall
    ax.text(3.0, 4.0, '★ ROCK BURST ★\nViolent spalling &\nejection of rock slabs\n(Option B)', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#dc2626', bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626', lw=2))

    # Flying rock shards
    for dx, dy in [(3.6, 4.3), (3.8, 3.8), (3.9, 4.5)]:
        ax.plot([dx, dx+0.2], [dy, dy-0.1], color='#991b1b', lw=2.5)

    # Overburden stress arrows
    ax.annotate('', xy=(5, 5.8), xytext=(5, 7.2), arrowprops=dict(arrowstyle="->", color='#991b1b', lw=3))
    ax.text(5, 7.4, 'Massive In-Situ Overburden Stress (Over 500 - 1000 m Depth)', ha='center', fontweight='bold', fontsize=9.5, color='#991b1b')

    callout = (
        "Rock Burst Mechanics (Hoek & Brown; Bangar, p. 305):\n"
        "• Occurs in deep tunnels/mines driven through massive, brittle rocks (granites, quartzites) under high stress.\n"
        "• Excavation removes confining pressure, concentrating massive tangential stresses at sidewalls.\n"
        "• When strain energy exceeds rock strength, rock fails with explosive, gunshot-like violence (rock burst)."
    )
    ax.text(5, 1.2, callout, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q112', 'rock_burst_tunneling_high_stress_release.png', draw_q112)

# Q113: Strata Dipping Angles - Moderately Inclined Strata (Upto 45 deg)
def draw_q113(ax):
    ax.axis('off')
    ax.set_title('Q113: Structural Classification of Bedded Strata by Dip Angle\nModerately Inclined Strata: Beds Dipping at Angles Upto 45° (15° to 45°)', fontsize=12.5, fontweight='bold', pad=15)

    classes = [
        ('GENTLY INCLINED\nDip: < 15°\n(Nearly horizontal sheets)', 0.18, 0.65, '#e0f2fe', '#0284c7'),
        ('★ MODERATELY INCLINED ★\nDip: 15° to 45°\n(Upto 45°)\n(Option A)', 0.50, 0.65, '#fef08a', '#ca8a04'),
        ('STEEPLY INCLINED\nDip: 45° to 85°\n(Steeply tilted strata)', 0.82, 0.65, '#fed7aa', '#ea580c')
    ]

    for title, x, y, fc, ec in classes:
        lw = 2.5 if 'MODERATELY' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    dip_box = (
        "Standard Structural Geology Dip Classifications (Bangar, p. 162; Billings):\n"
        "• Horizontal / Gently Inclined: 0° to 10° or 15°.\n"
        "• Moderately Inclined: Dip angles between 15° and 45° (angles upto 45°).\n"
        "• Steeply Inclined: Dip angles exceeding 45° up to 85°.\n"
        "• Vertical: Dip angle = 90° | Overturned: Stratigraphic beds inverted past verticality."
    )
    ax.text(0.5, 0.22, dip_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q113', 'strata_dip_classification_moderately_inclined.png', draw_q113)

# Q114: Grouting Rectification of Joints
def draw_q114(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q114: Foundation Remediation by Grouting: Sealing Joint Networks\nCement-Bentonite Grouting Consolidates Open Joints and Halts Water Seepage', fontsize=12.5, fontweight='bold', pad=15)

    # Rock foundation with joint fractures
    ax.fill([1, 9, 9, 1], [1, 1, 6.5, 6.5], color='#cbd5e1')

    # Fractures / joints
    for x in [3.0, 5.0, 7.0]:
        ax.plot([x-0.8, x+0.8], [2.0, 6.0], 'k-', lw=1.5)
        ax.plot([x-0.5, x+0.5], [5.5, 1.5], 'k-', lw=1.5)

    # Grout hole pipe
    ax.plot([5.0, 5.0], [7.2, 2.0], color='#2563eb', lw=4)
    ax.text(5.0, 7.5, 'GROUT INJECTION PIPE (Drill Hole)', color='#2563eb', ha='center', fontweight='bold', fontsize=10)

    # Grout penetration into joints (purple slurry filling)
    for x in [4.2, 5.0, 5.8]:
        circle = patches.Circle((x, 3.5), 0.8, color='#c084fc', alpha=0.6)
        ax.add_patch(circle)

    ax.text(5.0, 3.5, '★ GROUTED JOINTS ★\nSlurry seals joints, stops\nleakage & increases bearing capacity\n(Option A)', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#4a044e')

    desc = (
        "Grouting in Engineering Geology (Bangar, p. 299; Krynine & Judd):\n"
        "• Open joints and fissures create severe leakage paths and weaken dam foundation rock masses.\n"
        "• Pressure grouting injects cement-bentonite or chemical resin slurries into drill holes.\n"
        "• The grout spreads into intersecting joints, cementing fractures into a solid, impermeable monolithic mass."
    )
    ax.text(5.0, 0.7, desc, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q114', 'grouting_rectification_rock_joints_dam_foundation.png', draw_q114)

# Q115: Anisotropic Rock Strength - Stress Normal to Bedding
def draw_q115(ax):
    ax.axis('off')
    ax.set_title('Q115: Compressive Strength Anisotropy in Bedded / Foliated Rocks\nMaximum Strength Occurs When Compressive Stresses Act NORMAL to Bedding Planes', fontsize=12, fontweight='bold', pad=15)

    cases = [
        ('★ NORMAL TO BEDDING ★\n(theta = 90°)\nMAXIMUM STRENGTH\nBedding planes pressed\ntightly together; no sliding\n(Option A)', 0.2, 0.65, '#fef08a', '#ca8a04'),
        ('INCLINED AT 30° - 45°\n(theta = 30° - 45°)\nMINIMUM STRENGTH\nResolved shear stress along\nbedding triggers premature sliding', 0.5, 0.65, '#fee2e2', '#dc2626'),
        ('PARALLEL TO BEDDING\n(theta = 0°)\nINTERMEDIATE STRENGTH\nBuckling and splitting\nalong weak laminations', 0.8, 0.65, '#e2e8f0', '#475569')
    ]

    for title, x, y, fc, ec in cases:
        lw = 2.5 if 'NORMAL' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    notes = (
        "Jaeger's Variable Cohesion Theory of Anisotropic Rock Strength:\n"
        "• In layered rocks (shale, sandstone, slate, gneiss), strength depends strongly on loading angle (theta).\n"
        "• When stress is NORMAL (perpendicular, 90°) to bedding, shear stresses on bedding planes are zero (tau = 0),\n"
        "  forcing failure through intact rock material, giving the MAXIMUM compressive strength.\n"
        "• When stress is inclined at 30°-45°, resolved shear stress causes easy sliding along weak bedding planes."
    )
    ax.text(0.5, 0.22, notes, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q115', 'anisotropic_rock_strength_stress_vs_bedding.png', draw_q115)

# Q116: Granitic Bedrock - Best Site for Dam Construction
def draw_q116(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q116: Geological Suitability of Dam Foundation Sites\nGranitic Bedrock: The Premier Foundation Offering Maximum Strength and Impermeability', fontsize=12, fontweight='bold', pad=15)

    # Concrete Gravity Dam cross section
    ax.fill([3.5, 5.0, 5.0, 2.0], [2.5, 2.5, 6.8, 2.5], color='#94a3b8', edgecolor='#1e293b', lw=2)
    ax.text(4.0, 4.5, 'CONCRETE\nGRAVITY DAM', ha='center', fontweight='bold', fontsize=9.5, color='white')

    # Water reservoir upstream
    ax.fill([0.5, 2.0, 2.0, 0.5], [2.5, 2.5, 6.0, 6.0], color='#38bdf8', alpha=0.7)
    ax.text(1.2, 4.5, 'RESERVOIR\nWATER', ha='center', fontweight='bold', fontsize=9, color='#0369a1')

    # Foundation bedrock
    ax.fill([0.5, 9.5, 9.5, 0.5], [0.5, 0.5, 2.5, 2.5], color='#fef08a', edgecolor='#ca8a04', lw=2.5)
    ax.text(5.5, 1.5, '★ SOUND GRANITIC BEDROCK FOUNDATION ★ (Option A)\n• Crushing Strength > 150 - 250 MPa   • Extremely low porosity (< 0.5%)\n• High Bearing Capacity & Safe against Seepage / Uplift Pressure', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#854d0e')

    # Disqualified alternatives box
    disq = (
        "Why other sites are disqualified for dam construction (Bangar, pp. 296-298):\n"
        "• Limestone Bedrock (Option D): Highly vulnerable to karst cavities, sinkholes, and catastrophic underground piping.\n"
        "• Sheared Zone (Option B): Promotes foundation sliding and major water leakage along fault planes.\n"
        "• Lateritic Zone (Option C): Highly porous, permeable, soft, and low bearing capacity."
    )
    ax.text(5.0, 7.3, disq, ha='center', fontsize=8.8, bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#ef4444'))

create_figure('figures_2019_Q116', 'granitic_bedrock_dam_site_engineering.png', draw_q116)

# Q117: Granite True Statement - Very High Crushing Strength
def draw_q117(ax):
    ax.axis('off')
    ax.set_title('Q117: Engineering Properties of Granite: Verification of True Statements\nGranite Possesses Very High Crushing Strength (150 to 300+ MPa)', fontsize=12.5, fontweight='bold', pad=15)

    props = [
        ('★ CRUSHING STRENGTH ★\nVERY HIGH (150 - 300 MPa)\nInterlocking quartz & feldspar\nTRUE STATEMENT (Option A)', 0.2, 0.65, '#fef08a', '#ca8a04'),
        ('POLISHABILITY\nTakes EXCELLENT, brilliant polish\nUsed as premium monument stone\n(Option B is False)', 0.5, 0.65, '#e2e8f0', '#64748b'),
        ('POROSITY & DURABILITY\nExtremely LOW porosity (< 0.5%)\nHigh resistance to weathering\n(Options C & D are False)', 0.8, 0.65, '#e2e8f0', '#64748b')
    ]

    for title, x, y, fc, ec in props:
        lw = 2.5 if 'CRUSHING' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    granite_box = (
        "Key Engineering Characteristics of Granite (IS: 3316; Bangar, p. 289):\n"
        "• Specific Gravity: 2.63 - 2.75 | Density: 2600 - 2750 kg/m3.\n"
        "• Crushing Strength: 150 - 300 MPa (1500 - 3000 kg/cm2) - among the strongest stones on Earth.\n"
        "• Water Absorption: < 0.5% by weight (impervious and highly durable against frost/acid rain).\n"
        "• Widely utilized for mega-dam abutments, bridge piers, monument cladding, and heavy dimension stone."
    )
    ax.text(0.5, 0.22, granite_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q117', 'granite_crushing_strength_and_durability.png', draw_q117)

# Q118: Road Metal Desirable vs Undesirable Properties
def draw_q118(ax):
    ax.axis('off')
    ax.set_title('Q118: Quality Evaluation of Road Aggregates (Road Metal)\nUndesirable Properties: Strongly Sheared (C) and Highly Porous/Permeable (D)', fontsize=12.5, fontweight='bold', pad=15)

    comp = [
        ('DESIRABLE ROAD PROPERTIES\n• Sufficient Crushing Strength (> 100 MPa)\n• High Toughness & Impact Value (< 18%)\n• Hydrophobic (prevents bitumen stripping)\n• Low Porosity & Water Absorption (< 1%)\n• Dense, fresh unweathered rock', 0.3, 0.60, '#dcfce7', '#16a34a'),
        ('UNDESIRABLE PROPERTIES\n★ Strongly Sheared (Option C) ★\n(Promotes crushing & fracture failure)\n\n★ Highly Porous & Permeable (Option D) ★\n(Causes water stripping & freeze thaw)\n• Hydrophilic (water strips bitumen)', 0.7, 0.60, '#fee2e2', '#dc2626')
    ]

    for title, x, y, fc, ec in comp:
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=2))

    notes = (
        "Indian Roads Congress (IRC) Aggregate Specifications:\n"
        "• Aggregate Crushing Value (ACV) must be < 30% (for wearing course < 25%).\n"
        "• Sheared or highly jointed rocks shatter easily under traffic wheel compaction.\n"
        "• High porosity allows water to enter and strip bitumen coating, destroying road pavements."
    )
    ax.text(0.5, 0.18, notes, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q118', 'road_metal_aggregate_desirable_properties.png', draw_q118)

# Q119: Workability of Building Stones
def draw_q119(ax):
    ax.axis('off')
    ax.set_title('Q119: Index Properties of Building Stones: Workability\nEase with Which a Stone Can Be Quarreled, Cut, Chiseled, and Dressed into Blocks', fontsize=12.5, fontweight='bold', pad=15)

    facets = [
        ('QUARRY EXTRACTION\nSplitting along natural rift,\ncleavage, and grain lines', 0.2, 0.65, '#e0f2fe', '#0284c7'),
        ('★ WORKABILITY ★\nEase of cutting & dressing\ninto smooth architectural blocks\n(Option B)', 0.5, 0.65, '#fef08a', '#ca8a04'),
        ('FINAL DRESSING\nChiseling, bush-hammering,\nrubbing, and polishing', 0.8, 0.65, '#dcfce7', '#16a34a')
    ]

    for title, x, y, fc, ec in facets:
        lw = 2.5 if 'WORKABILITY' in title else 1.2
        ax.text(x, y, title, ha='center', va='center', fontweight='bold', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=lw))

    callout = (
        "Building Stone Dressing Terminology (Bangar, p. 285; Mahapatra):\n"
        "• Workability is the facility or ease with which a stone can be extracted, cut, dressed, and shaped.\n"
        "• Moderately soft rocks (freestone like sandstones and limestones) have high workability.\n"
        "• Ultra-hard rocks (massive dolerite, quartzite) have low workability and require diamond saws."
    )
    ax.text(0.5, 0.22, callout, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q119', 'workability_stone_extraction_dressing.png', draw_q119)

# Q120: Slate - Roofing Slab Material
def draw_q120(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q120: Metamorphic Rocks in Construction: Slate as Roofing Slabs\nPerfect Planar Slaty Cleavage Allows Splitting into Thin, Waterproof Roofing Tiles', fontsize=12.5, fontweight='bold', pad=15)

    # Slanted roof with overlapping slate shingles
    for i in range(5):
        y = 5.5 - i * 0.8
        x = 2.0 + i * 0.8
        ax.add_patch(patches.Rectangle((x, y), 3.0, 0.4, angle=25, facecolor='#64748b', edgecolor='#1e293b', lw=1.5))

    ax.text(6.8, 5.0, '★ SLATE ROOFING SLABS ★\n(Option A)\n• Splits into thin sheets (4 - 8 mm)\n• Perfectly impermeable & waterproof\n• Resistant to atmospheric weathering\n• Acid-proof & frost-resistant', fontsize=10, fontweight='bold', color='#0f172a', bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef08a', edgecolor='#ca8a04', lw=2))

    slate_box = (
        "Slaty Cleavage & Engineering Utility (K.M. Bangar, p. 290):\n"
        "• Formed by low-grade regional metamorphism of shale (greenschist / pumpellyite facies).\n"
        "• Microscopic recrystallization aligns platy illite, chlorite, and sericite parallel to tectonic stress.\n"
        "• Allows splitting along flat planes of extraordinary smoothness and thinness, ideal for roofing and electrical switchboards."
    )
    ax.text(5.0, 1.0, slate_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q120', 'slate_roofing_slab_slaty_cleavage.png', draw_q120)
