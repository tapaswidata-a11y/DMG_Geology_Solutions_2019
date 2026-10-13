import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set global styles
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# ==========================================
# Figure 76: Supergene Copper Deposit Profile
# ==========================================
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

# Zones vertical coordinates
# Gossan: 80 - 100
# Leached/Oxidized Zone: 55 - 80
# Water table: y = 55
# Supergene Sulfide Enrichment Zone: 25 - 55
# Primary Protore (Hypogene): 0 - 25

# Background zones
ax.axhspan(80, 100, color='#b45309', alpha=0.25, label='Gossan (Fe-cap)')
ax.axhspan(55, 80, color='#fef08a', alpha=0.35, label='Oxidized / Leached Zone')
ax.axhspan(25, 55, color='#38bdf8', alpha=0.3, label='Supergene Sulfide Enrichment Zone')
ax.axhspan(0, 25, color='#94a3b8', alpha=0.3, label='Primary Protore (Hypogene Zone)')

# Water table line
ax.axhline(55, color='#0284c7', linestyle='--', linewidth=2.5)
ax.text(2, 56, '▼ Regional Water Table (Phreatic Surface)', color='#0369a1', fontsize=12, fontweight='bold')

# Zone Labels & Details
ax.text(50, 90, '1. GOSSAN (LEACHED CAPPING)\nSpongy, cellular mass of Goethite, Limonite, Hematite, Quartz & Clays\nCu completely leached downwards; highly porous iron cap', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='#78350f',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef3c7', edgecolor='#b45309', alpha=0.9))

ax.text(50, 68, '2. OXIDIZED ZONE (Above Water Table)\nStrongly oxidizing, vadose meteoric infiltration\nMalachite, Azurite, Cuprite, Chrysocolla & NATIVE COPPER\n(Oxidation & reduction of soluble copper sulfates above water table)', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='#854d0e',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef9c3', edgecolor='#ca8a04', alpha=0.9))

ax.text(50, 40, '3. SUPERGENE SULFIDE ENRICHMENT ZONE (At & Below Water Table)\nReducing, neutral-to-weakly alkaline environment\nReaction of descending Cu²⁺ solutions with primary sulfides\nPrecipitates: CHALCOCITE (Cu₂S), COVELLITE (CuS), Digenite, Bornite\nDrastic grade upgrade (e.g., 0.3% Cu protore → 2.5% to 5.0% Cu)', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='#0369a1',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#e0f2fe', edgecolor='#0284c7', alpha=0.9))

# Gradational boundary note
ax.text(50, 25, '~~~~~~~~ Gradational, irregular lower boundary ~~~~~~~~', ha='center', va='center', color='#475569', fontsize=11, fontstyle='italic', fontweight='bold')

ax.text(50, 12, '4. PROTORE (PRIMARY HYPOGENE ZONE)\nUnaltered low-grade primary mineralization (chalcopyrite CuFeS₂ + pyrite FeS₂)\nHydrothermal magmatic origin; Cu content typically 0.2% – 0.8%', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='#334155',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f1f5f9', edgecolor='#64748b', alpha=0.9))

# Downward arrows showing meteoric leaching
for x_arr in [15, 85]:
    ax.annotate('', xy=(x_arr, 35), xytext=(x_arr, 95),
                arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=3, mutation_scale=20))
    ax.text(x_arr, 65, 'Descending\nAcidic Cu²⁺\nMeteoric\nSolutions\n(CuSO₄)', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#075985',
            bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#0284c7', alpha=0.85))

ax.set_xlim(0, 100)
ax.set_ylim(0, 102)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Supergene Copper Deposit Weathering Profile & Geochemical Zoning\n(Grounded in Evans Ore Geology & Park & MacDiarmid)', fontsize=13, fontweight='bold', pad=15, color='#0f172a')

plt.tight_layout()
plt.savefig('figures_Q76/supergene_copper_weathering_profile.png', dpi=300)
plt.close()
print("Figure 76 generated.")

# ==========================================
# Figure 77: BIF Types - Algoma vs Superior
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), dpi=300)

# Subplot 1: Algoma-type
ax1.set_facecolor('#f8fafc')
ax1.plot([0, 10], [8, 8], color='#334155', lw=2)
# volcanic layers
ax1.fill_between([0, 10], [6, 6], [8, 8], color='#64748b', alpha=0.3, label='Submarine Volcanics (Basalt/Rhyolite)')
ax1.fill_between([0, 10], [4.5, 4.5], [6, 6], color='#dc2626', alpha=0.6, label='Algoma-type BIF (Banded Chert-Fe)')
ax1.fill_between([0, 10], [2, 2], [4.5, 4.5], color='#475569', alpha=0.3, label='Greywacke / Turbidite sequence')
ax1.fill_between([0, 10], [0, 0], [2, 2], color='#334155', alpha=0.4, label='Volcanic Basement')

# Annotations
ax1.text(5, 5.25, 'Algoma-type BIF\n(Interbedded Chert + Magnetite/Hematite)', ha='center', va='center', color='white', fontweight='bold', fontsize=10)
ax1.text(5, 7, 'Submarine Pillow Basalts & Pyroclastics', ha='center', va='center', color='#1e293b', fontweight='bold', fontsize=10)
ax1.text(5, 3.25, 'Volcanogenic Turbidites / Greywackes', ha='center', va='center', color='#1e293b', fontweight='bold', fontsize=10)

ax1.text(5, 1.0, 'Archean Greenstone Belt Setting\n(Abitibi, Dharwar; Age: > 2.5–3.5 Ga; ARCHEAN)', ha='center', va='center', color='#0f172a', fontweight='bold', fontsize=10,
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#ef4444'))

ax1.set_title('Algoma-Type Iron Formation\n• Geological Age: ARCHEAN (> 2.5 Ga; NOT Cambrian!)\n• Setting: Submarine Volcanic Sequences in Greenstone Belts\n• Origin: Exhalative hydrothermal venting, narrow basins', fontsize=11, fontweight='bold', color='#991b1b')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 8.5)
ax1.set_xticks([])
ax1.set_yticks([])

# Subplot 2: Superior-type
ax2.set_facecolor('#f8fafc')
# Passive margin shelf
x_vals = np.linspace(0, 10, 100)
shelf_top = 7 - 0.2*x_vals
shelf_bif_bot = 5 - 0.2*x_vals
shelf_bot = 2 - 0.2*x_vals

ax2.fill_between(x_vals, shelf_bif_bot, shelf_top, color='#b91c1c', alpha=0.7, label='Superior-type BIF (Mesabi, Hamersley)')
ax2.fill_between(x_vals, shelf_bot, shelf_bif_bot, color='#cbd5e1', alpha=0.5, label='Quartzite / Shelf Dolomite')
ax2.fill_between(x_vals, 0, shelf_bot, color='#94a3b8', alpha=0.3, label='Stable Continental Cratonic Basement')

# Seawater wedge
ax2.fill_between(x_vals, shelf_top, 8, color='#38bdf8', alpha=0.25)
ax2.text(7, 7.5, 'Broad Shallow Ocean Shelf', color='#0369a1', fontweight='bold', fontsize=11)

ax2.text(5, 5.8, 'Superior-type BIF Sheet\n(Continuously traceable over 100s of km)', ha='center', va='center', color='white', fontweight='bold', fontsize=10)
ax2.text(5, 3.4, 'Cratonic Platform Shelf Sediments (Quartzites, Carbonates)', ha='center', va='center', color='#1e293b', fontweight='bold', fontsize=10)

ax2.text(5, 1.0, 'Late Archean to Paleoproterozoic (2.4–1.8 Ga)\nGreat Oxidation Event (GOE); Lake Superior, Hamersley, Bailadila', ha='center', va='center', color='#0f172a', fontweight='bold', fontsize=10,
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#dcfce7', edgecolor='#22c55e'))

ax2.set_title('Superior-Type Iron Formation\n• Geological Age: Late Archean to Paleoproterozoic (2.4–1.8 Ga)\n• Setting: Passive Continental Margins & Shallow Shelf Basins\n• Origin: Basin-wide oxidation of upwelling dissolved Fe²⁺', fontsize=11, fontweight='bold', color='#166534')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 8.5)
ax2.set_xticks([])
ax2.set_yticks([])

plt.tight_layout()
plt.savefig('figures_Q77/algoma_vs_superior_iron_formations.png', dpi=300)
plt.close()
print("Figure 77 generated.")

# ==========================================
# Figure 78: Hydrocarbon & Fossil Fuel Deposits
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#f8fafc')

deposits = [
    ("A. Lignite (Brown Coal)", "2. Neyveli, Tamil Nadu", "Cuddalore District; Cenozoic (Tertiary / Miocene)\nMajor open-cast mining for thermal power; Neyveli Lignite Corp (NLC)", "#78350f", "#fef3c7"),
    ("B. Crude Oil (Petroleum)", "1. Kalol, Gujarat", "Cambay Cenozoic Basin; Discovered 1961 by ONGC\nEocene-Oligocene deltaic sandstones reservoir", "#0f766e", "#ccfbf1"),
    ("C. Bituminous Coal", "4. Kamptee, Maharashtra", "Nagpur District; Gondwana Supergroup (Barakar / Kamthi Fm)\nMajor non-coking bituminous coal producer for central India", "#1e293b", "#f1f5f9"),
    ("D. Natural Gas", "3. Jaisalmer, Rajasthan", "Jaisalmer Basin; Mesozoic-Tertiary (Pariwar / Sanu formations)\nMajor gas fields: Manhera Tibba, Tanot, Dandewala (OIL/ONGC)", "#1d4ed8", "#dbeafe")
]

y_pos = [3.3, 2.2, 1.1, 0.0]

for y, (dep, loc, desc, col, bg) in zip(y_pos, deposits):
    # Left box: deposit
    ax.text(0.5, y+0.35, dep, fontsize=12, fontweight='bold', color=col,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=bg, edgecolor=col, lw=1.5))
    # Arrow
    ax.annotate('', xy=(3.8, y+0.35), xytext=(2.6, y+0.35),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=2.5, mutation_scale=15))
    # Right box: location & details
    ax.text(4.0, y+0.35, f"{loc}\n{desc}", fontsize=10.5, fontweight='normal', color='#0f172a', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#94a3b8', lw=1.2))

ax.set_xlim(0, 9.5)
ax.set_ylim(-0.6, 4.2)
ax.axis('off')
ax.set_title('Match List-I (Hydrocarbon / Fossil Fuel) with List-II (Indian Locations)\nDGMS 2019 Examination • Verified Official Key: (a) A-2, B-1, C-4, D-3', fontsize=12.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q78/hydrocarbon_deposits_india_matching.png', dpi=300)
plt.close()
print("Figure 78 generated.")

# ==========================================
# Figure 79: Rock Mass Rating (RMR) Parameters
# ==========================================
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
ax.set_facecolor('#ffffff')

# Bieniawski parameters
rmr_params = [
    ("1. Strength of Intact Rock", "Uniaxial Compressive Strength (UCS) or Point Load Index", "Max Rating: 15", "#16a34a", True),
    ("2. Rock Quality Designation (RQD)", "Core recovery length of sound pieces >= 10 cm", "Max Rating: 20", "#16a34a", True),
    ("3. Spacing of Discontinuities", "Distance between natural joints/fractures along scanline", "Max Rating: 20", "#16a34a", True),
    ("4. Condition of Discontinuities", "Roughness, persistence, aperture, infilling, weathering", "Max Rating: 30", "#16a34a", True),
    ("5. Groundwater Conditions", "Inflow rate per 10m tunnel, joint water pressure ratio", "Max Rating: 15", "#16a34a", True),
    ("6. Discontinuity Orientation", "Adjustment for strike/dip favorable/unfavorable to tunnel", "Adjustment: 0 to -12", "#0284c7", True),
    ("EXCLUDED: Slake Durability Index (Id2)", "Measures resistance of shales/mudrocks to wet-dry cycles\nNOT a parameter in Bieniawski RMR (Used in Franklin index/ISRM)", "RMR Score: NONE (0)", "#dc2626", False)
]

y_coords = np.linspace(6, 0, 7)

for y, (title, desc, rating, col, is_in) in zip(y_coords, rmr_params):
    badge = "✓ INCLUDED IN RMR" if is_in else "✗ NOT IN RMR (CORRECT ANSWER)"
    badge_bg = "#dcfce7" if is_in else "#fee2e2"
    badge_col = "#166534" if is_in else "#991b1b"
    
    ax.text(0.2, y+0.25, title, fontsize=11, fontweight='bold', color=col)
    ax.text(0.2, y-0.15, desc, fontsize=9.5, color='#475569')
    ax.text(7.2, y+0.25, rating, fontsize=10, fontweight='bold', color=col, ha='right')
    ax.text(9.5, y+0.1, badge, fontsize=9, fontweight='bold', color=badge_col, ha='right',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=badge_bg, edgecolor=badge_col, lw=1))
    
    # separator line
    ax.axhline(y-0.35, color='#e2e8f0', lw=1)

ax.set_xlim(0, 10)
ax.set_ylim(-0.6, 6.8)
ax.axis('off')
ax.set_title("Bieniawski's Rock Mass Rating (RMR) Parameters vs. Slake Durability Index\nGeomechanics Classification System (Bieniawski 1973, 1989)", fontsize=12, fontweight='bold', pad=15, color='#0f172a')

plt.tight_layout()
plt.savefig('figures_Q79/rmr_parameters_bieniawski_classification.png', dpi=300)
plt.close()
print("Figure 79 generated.")

# ==========================================
# Figure 80: Geological Conditions for Dam Construction
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5), dpi=300)

# (A) Upstream Dip (Favorable / Ideal)
ax1.set_facecolor('#f8fafc')
# Dam body
dam_poly_1 = patches.Polygon([[4, 2], [6, 2], [5, 6], [4.5, 6]], closed=True, facecolor='#64748b', edgecolor='#334155', lw=2)
ax1.add_patch(dam_poly_1)
ax1.text(5.1, 4.5, 'DAM\nBODY', ha='center', va='center', color='white', fontweight='bold', fontsize=10)

# Reservoir water
res_poly_1 = patches.Polygon([[0, 2], [4, 2], [4.5, 5.5], [0, 5.5]], closed=True, facecolor='#38bdf8', alpha=0.35)
ax1.add_patch(res_poly_1)
ax1.text(2, 4, 'RESERVOIR\nWATER', ha='center', va='center', color='#0369a1', fontweight='bold', fontsize=11)

# Bedding dipping upstream (to the left)
for y_bed in np.linspace(-0.5, 2, 6):
    ax1.plot([0, 10], [y_bed + 2.5, y_bed - 0.5], color='#475569', lw=2, linestyle='-')

# Resultant thrust arrow
ax1.annotate('', xy=(5.2, 1.2), xytext=(4.5, 3.2),
            arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=3, mutation_scale=20))
ax1.text(4.2, 2.2, 'Resultant Thrust (R)\nacts nearly PERPENDICULAR\nto bedding planes!', color='#b91c1c', fontweight='bold', fontsize=9.5)

ax1.text(5, 0.5, 'GENTLE UPSTREAM DIP (IDEAL & STABLE)\n• Resistance to sliding along bedding is maximum\n• Uplift water pressure under base is minimized\n• Seepage direction opposes hydraulic thrust', 
         ha='center', va='center', fontsize=9.5, fontweight='bold', color='#166534',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#dcfce7', edgecolor='#22c55e', lw=1.5))

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 7)
ax1.axis('off')
ax1.set_title('(A) Strata Dipping UPSTREAM (Ideal Condition)\n(Bangar Engineering Geology Fig. 10.3)', fontsize=11.5, fontweight='bold', color='#166534')

# (B) Downstream Dip (Unfavorable / Hazardous)
ax2.set_facecolor('#f8fafc')
# Dam body
dam_poly_2 = patches.Polygon([[4, 2], [6, 2], [5, 6], [4.5, 6]], closed=True, facecolor='#64748b', edgecolor='#334155', lw=2)
ax2.add_patch(dam_poly_2)
ax2.text(5.1, 4.5, 'DAM\nBODY', ha='center', va='center', color='white', fontweight='bold', fontsize=10)

# Reservoir water
res_poly_2 = patches.Polygon([[0, 2], [4, 2], [4.5, 5.5], [0, 5.5]], closed=True, facecolor='#38bdf8', alpha=0.35)
ax2.add_patch(res_poly_2)
ax2.text(2, 4, 'RESERVOIR\nWATER', ha='center', va='center', color='#0369a1', fontweight='bold', fontsize=11)

# Bedding dipping downstream (to the right)
for y_bed in np.linspace(-0.5, 2, 6):
    ax2.plot([0, 10], [y_bed - 0.5, y_bed + 2.5], color='#475569', lw=2, linestyle='-')

# Resultant thrust arrow
ax2.annotate('', xy=(6.5, 2.5), xytext=(4.5, 3.2),
            arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=3, mutation_scale=20))
ax2.text(6.0, 3.5, 'Resultant Thrust (R)\nacts nearly PARALLEL\nto bedding planes!\nSevere Sliding Hazard!', color='#b91c1c', fontweight='bold', fontsize=9.5)

ax2.text(5, 0.5, 'DOWNSTREAM DIP (HAZARDOUS & UNSTABLE)\n• Resultant force facilitates downstream sliding\n• Seepage water lubricates bedding planes\n• High uplift pressure develops under dam toe', 
         ha='center', va='center', fontsize=9.5, fontweight='bold', color='#991b1b',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#fee2e2', edgecolor='#ef4444', lw=1.5))

ax2.set_xlim(0, 10)
ax2.set_ylim(0, 7)
ax2.axis('off')
ax2.set_title('(B) Strata Dipping DOWNSTREAM (Hazardous)\n(Bangar Engineering Geology Fig. 10.4)', fontsize=11.5, fontweight='bold', color='#991b1b')

plt.tight_layout()
plt.savefig('figures_Q80/dam_foundation_dip_upstream_downstream.png', dpi=300)
plt.close()
print("Figure 80 generated.")
