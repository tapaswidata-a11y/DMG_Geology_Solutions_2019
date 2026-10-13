import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# ==========================================
# Figure 81: Glacial Alpine Landforms
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#f8fafc')

landforms = [
    ("CIRQUE (Corrie / Cwm)", "Steep-walled, armchair-shaped/semicircular hollow\nat head of glacial valley carved by plucking & rotational slip", "#1e3a8a", "#dbeafe", "✓ Correctly Matched"),
    ("ARÊTE (Knife-Edge Ridge)", "Narrow, sharp-edged, jagged sawtooth rock ridge\nseparating two adjacent glaciated valleys or cirques", "#0f766e", "#ccfbf1", "⭐ True Definition of Ridge"),
    ("COL (Mountain Pass / Saddle)", "Low saddle-like depression or breach in an arête\nformed where two opposing cirques erode backwards into each other", "#dc2626", "#fee2e2", "✗ MISMATCHED IN EXAM (Option c)"),
    ("NUNATAK (Glacial Island)", "Exposed, unglaciated bedrock peak or island\nsurrounded on all sides by an ice sheet or glacial ice", "#1e3a8a", "#dbeafe", "✓ Correctly Matched"),
    ("FJORD (Glacial Trough)", "Deep, steep-sided U-shaped glacial valley inundated\nand drowned below sea level following post-glacial sea-level rise", "#1e3a8a", "#dbeafe", "✓ Correctly Matched")
]

y_vals = np.linspace(4.8, 0, 5)

for y, (name, desc, col, bg, badge) in zip(y_vals, landforms):
    badge_col = "#991b1b" if "MISMATCHED" in badge else ("#0f766e" if "⭐" in badge else "#166534")
    badge_bg = "#fee2e2" if "MISMATCHED" in badge else ("#ccfbf1" if "⭐" in badge else "#dcfce7")
    
    ax.text(0.2, y+0.4, name, fontsize=11.5, fontweight='bold', color=col)
    ax.text(0.2, y-0.05, desc, fontsize=10, color='#334155')
    ax.text(9.8, y+0.25, badge, fontsize=9.5, fontweight='bold', color=badge_col, ha='right',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=badge_bg, edgecolor=badge_col, lw=1.2))
    ax.axhline(y-0.35, color='#cbd5e1', lw=1)

ax.set_xlim(0, 10)
ax.set_ylim(-0.6, 5.6)
ax.axis('off')
ax.set_title("Glacial Landforms & Geomorphology: Arête vs. Col Differentiation\nDGMS 2019 Examination • Verified Official Key: (c) Col : Narrow, sharp-edged ridge", fontsize=12.5, fontweight='bold', color='#0f172a', pad=15)

plt.tight_layout()
plt.savefig('figures_Q81/glacial_landforms_arete_col_cirque.png', dpi=300)
plt.close()
print("Figure 81 generated.")

# ==========================================
# Figure 82: Atterberg Limits Phase Diagram
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_facecolor('#ffffff')

# Four states: Solid, Semi-Solid, Plastic, Liquid
# Boundaries: 0% -> Shrinkage Limit (wS) -> Plastic Limit (wP) -> Liquid Limit (wL) -> Liquid
x_bounds = [0, 25, 55, 85, 100]

colors = ['#cbd5e1', '#fed7aa', '#bbf7d0', '#bae6fd']
labels = ['SOLID\nSTATE', 'SEMI-SOLID\nSTATE', 'PLASTIC\nSTATE', 'LIQUID\nSTATE']

for i in range(4):
    ax.axvspan(x_bounds[i], x_bounds[i+1], color=colors[i], alpha=0.6)
    mid_x = (x_bounds[i] + x_bounds[i+1]) / 2
    ax.text(mid_x, 0.5, labels[i], ha='center', va='center', fontsize=12, fontweight='bold', color='#1e293b')

# Boundary lines
for x, limit_name, limit_sym in [(25, 'SHRINKAGE LIMIT', 'w_s (SL)'), 
                                 (55, 'PLASTIC LIMIT', 'w_p (PL)\n★ TARGET BOUNDARY'), 
                                 (85, 'LIQUID LIMIT', 'w_l (LL)')]:
    ax.axvline(x, color='#1e3a8a', linestyle='--', lw=2)
    ax.text(x, 0.95, f"{limit_name}\n({limit_sym})", ha='center', va='top', fontsize=10.5, fontweight='bold',
            color='#1e3a8a', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#1e3a8a', lw=1.2))

# Highlight boundary between Plastic and Semi-solid
ax.annotate('Boundary between Plastic\n& Semi-Solid States:\nPLASTIC LIMIT (Option b)',
            xy=(55, 0.25), xytext=(40, 0.12),
            arrowprops=dict(arrowstyle="-|>", color='#b91c1c', lw=2.5, mutation_scale=20),
            fontsize=10.5, fontweight='bold', color='#991b1b',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626', lw=1.5))

# Plasticity Index span
ax.annotate('', xy=(85, 0.72), xytext=(55, 0.72),
            arrowprops=dict(arrowstyle="<->", color='#059669', lw=2))
ax.text(70, 0.77, 'Plasticity Index (Ip = LL - PL)', ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#065f46')

# Water content arrow at bottom
ax.annotate('', xy=(100, -0.05), xytext=(0, -0.05),
            arrowprops=dict(arrowstyle="-|>", color='#334155', lw=2))
ax.text(50, -0.15, 'Increasing Soil Moisture / Water Content (w %) ➔', ha='center', va='center', fontsize=11, fontweight='bold', color='#1e293b')

ax.set_xlim(0, 100)
ax.set_ylim(-0.25, 1.15)
ax.axis('off')
ax.set_title("Atterberg Consistency Limits & Soil State Transitions\n(Albert Atterberg 1911; Arthur Casagrande Soil Mechanics)", fontsize=13, fontweight='bold', pad=15, color='#0f172a')

plt.tight_layout()
plt.savefig('figures_Q82/atterberg_limits_phase_diagram.png', dpi=300)
plt.close()
print("Figure 82 generated.")

# ==========================================
# Figure 83: Arch Dam Load Transmission Mechanics
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#f8fafc')

# Plan view of an Arch Dam in a narrow gorge
# Canyon walls / Abutments
left_wall = patches.Polygon([[0, 0], [2.5, 0], [2.5, 6], [0, 6]], closed=True, facecolor='#94a3b8', edgecolor='#334155', lw=2)
right_wall = patches.Polygon([[7.5, 0], [10, 0], [10, 6], [7.5, 6]], closed=True, facecolor='#94a3b8', edgecolor='#334155', lw=2)
ax.add_patch(left_wall)
ax.add_patch(right_wall)

ax.text(1.25, 3, 'LEFT ROCK\nABUTMENT\n(Valley Wall)', ha='center', va='center', color='white', fontweight='bold', fontsize=11)
ax.text(8.75, 3, 'RIGHT ROCK\nABUTMENT\n(Valley Wall)', ha='center', va='center', color='white', fontweight='bold', fontsize=11)

# Curved arch dam
theta = np.linspace(np.pi*0.2, np.pi*0.8, 100)
r_inner = 3.6
r_outer = 4.2
center_x = 5.0
center_y = 6.2

# Inner arc (downstream)
x_in = center_x + r_inner * np.cos(theta)
y_in = center_y - r_inner * np.sin(theta)
# Outer arc (upstream)
x_out = center_x + r_outer * np.cos(theta)
y_out = center_y - r_outer * np.sin(theta)

dam_x = np.concatenate([x_in, x_out[::-1]])
dam_y = np.concatenate([y_in, y_out[::-1]])
ax.fill(dam_x, dam_y, color='#475569', edgecolor='#1e293b', lw=2)
ax.text(5, 2.3, 'ARCH DAM (Upstream Convexity)', ha='center', va='center', color='white', fontweight='bold', fontsize=10)

# Reservoir water upstream
ax.text(5, 1.0, 'RESERVOIR WATER THRUST (P)\n(Acts downstream onto upstream arch face)', ha='center', va='center', color='#0369a1', fontweight='bold', fontsize=11)

# Thrust arrows onto arch face
for ang in [np.pi*0.35, np.pi*0.5, np.pi*0.65]:
    x_t = center_x + 4.8 * np.cos(ang)
    y_t = center_y - 4.8 * np.sin(ang)
    x_end = center_x + 4.2 * np.cos(ang)
    y_end = center_y - 4.2 * np.sin(ang)
    ax.annotate('', xy=(x_end, y_end), xytext=(x_t, y_t),
                arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=2.5, mutation_scale=15))

# Arch ring thrust vectors into abutments
ax.annotate('', xy=(2.0, 3.8), xytext=(3.0, 3.3),
            arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=3.5, mutation_scale=20))
ax.text(2.6, 4.4, 'Enormous Lateral\nThrust Transmitted\ninto Abutment!', color='#b91c1c', fontweight='bold', fontsize=10)

ax.annotate('', xy=(8.0, 3.8), xytext=(7.0, 3.3),
            arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=3.5, mutation_scale=20))
ax.text(7.4, 4.4, 'Enormous Lateral\nThrust Transmitted\ninto Abutment!', color='#b91c1c', fontweight='bold', fontsize=10)

# Explanation box
ax.text(5, 5.4, 'ARCH ACTION PRINCIPLE:\nHorizontal water pressure is converted by curvature into internal membrane compression (ring thrust)\nand transmitted laterally into the massive rock abutments / valley flanks.', 
        ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e3a8a',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#eff6ff', edgecolor='#3b82f6', lw=1.5))

ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Arch Dam Structural Mechanics: Lateral Load Transmission to Abutments\n(K.M. Bangar Chapter 10 & Legget Engineering Geology)', fontsize=12, fontweight='bold', pad=12, color='#0f172a')

plt.tight_layout()
plt.savefig('figures_Q83/arch_dam_abutment_thrust_mechanics.png', dpi=300)
plt.close()
print("Figure 83 generated.")

# ==========================================
# Figure 84: Brazilian Test Tensile Strength
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#ffffff')

# Circular rock specimen
rock_circle = patches.Circle((4, 3.2), 2.2, facecolor='#f1f5f9', edgecolor='#334155', lw=2.5)
ax.add_patch(rock_circle)

# Vertical diametral crack / failure line
ax.plot([4, 4], [1.0, 5.4], color='#dc2626', linestyle='--', lw=2.5)
ax.text(4.15, 3.2, 'Failure Plane\n(Splits in Tension!)', color='#b91c1c', fontweight='bold', fontsize=10, va='center')

# Applied compressive loads P
ax.annotate('', xy=(4, 5.4), xytext=(4, 6.6),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=4, mutation_scale=25))
ax.text(4, 6.8, 'Applied Compressive Load (P)', ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1e3a8a')

ax.annotate('', xy=(4, 1.0), xytext=(4, -0.2),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=4, mutation_scale=25))
ax.text(4, -0.4, 'Reaction Load (P)', ha='center', va='top', fontsize=11, fontweight='bold', color='#1e3a8a')

# Tensile stress arrows in middle
for y_arr in [2.3, 3.2, 4.1]:
    ax.annotate('', xy=(3.0, y_arr), xytext=(3.7, y_arr),
                arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=2, mutation_scale=12))
    ax.annotate('', xy=(5.0, y_arr), xytext=(4.3, y_arr),
                arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=2, mutation_scale=12))
ax.text(2.6, 3.2, 'Tensile\nStress (σt)', color='#991b1b', fontweight='bold', fontsize=9.5, ha='right', va='center')

# Right side formula box
ax.text(8.0, 3.2, 'BRAZILIAN TEST FORMULA:\n\nσt = 2P / (π · D · t)\n\nWhere:\n• σt = Indirect Tensile Strength\n• P = Failure Compressive Load\n• D = Core Specimen Diameter\n• t = Core Specimen Thickness\n\nPrinciple:\nDiametral line compression generates\nuniform perpendicular tensile stress\nalong 75% of the loaded diameter,\ncausing rock to split cleanly in tension.',
        fontsize=10, color='#0f172a', va='center', ha='center',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#64748b', lw=1.5))

ax.set_xlim(0, 10.5)
ax.set_ylim(-0.7, 7.2)
ax.axis('off')
ax.set_title("The Brazilian Test (Indirect Tensile Strength Determination)\n(ISRM Suggested Method; ASTM D3967)", fontsize=12.5, fontweight='bold', color='#0f172a', pad=15)

plt.tight_layout()
plt.savefig('figures_Q84/brazilian_test_tensile_strength.png', dpi=300)
plt.close()
print("Figure 84 generated.")

# ==========================================
# Figure 85: Tunneling in Geological Structures
# ==========================================
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5.5), dpi=300)

# 1. Thick Horizontal Formation (BEST)
ax1.set_facecolor('#f8fafc')
for y in [1, 2.5, 4]:
    ax1.axhline(y, color='#475569', lw=2)
# Tunnel horseshoe
tunnel_1 = patches.Circle((5, 2.5), 0.9, facecolor='#ffffff', edgecolor='#0f766e', lw=2.5)
ax1.add_patch(tunnel_1)
ax1.text(5, 2.5, 'TUNNEL', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#0f766e')
ax1.text(5, 4.6, 'Thick Horizontal Bed\nActs as Stable Beam / Bridge', ha='center', va='center', color='#166534', fontweight='bold', fontsize=9.5)
ax1.text(5, 0.4, '★ BEST CONDITION (Option b)\n• Uniform rock mass throughout\n• Symmetric vertical loading\n• Stable roof, minimal overbreak\n• Predictable groundwater', 
         ha='center', va='center', fontsize=9, fontweight='bold', color='#166534',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#dcfce7', edgecolor='#22c55e'))
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5.5)
ax1.axis('off')
ax1.set_title('(A) Thick Horizontal Formation\n(Ideal & Safest)', fontsize=11, fontweight='bold', color='#166534')

# 2. Anticlinal Crest
ax2.set_facecolor('#f8fafc')
x = np.linspace(0, 10, 100)
for h in [2.5, 3.5, 4.5]:
    y_fold = h - 0.08*(x - 5)**2
    ax2.plot(x, y_fold, color='#475569', lw=2)
tunnel_2 = patches.Circle((5, 3.0), 0.9, facecolor='#ffffff', edgecolor='#dc2626', lw=2.5)
ax2.add_patch(tunnel_2)
ax2.text(5, 3.0, 'TUNNEL', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#dc2626')
# Tension fractures
for x_f in [4.6, 5.0, 5.4]:
    ax2.plot([x_f, x_f], [3.9, 4.6], color='#dc2626', linestyle='--', lw=1.8)
ax2.text(5, 4.8, 'Tension Fractures\nat Fold Crest!', color='#b91c1c', fontweight='bold', fontsize=9, ha='center')
ax2.text(5, 0.4, 'UNFAVORABLE (Option a)\n• Tensile joints in crest arch\n• Loose rock, severe roof collapse\n• High rock burst / overbreak risk',
         ha='center', va='center', fontsize=9, fontweight='bold', color='#991b1b',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee2e2', edgecolor='#ef4444'))
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 5.5)
ax2.axis('off')
ax2.set_title('(B) Anticlinal Axis / Crest\n(Tensile Joint Hazard)', fontsize=11, fontweight='bold', color='#991b1b')

# 3. Synclinal Trough
ax3.set_facecolor('#f8fafc')
for h in [0.8, 1.8, 2.8]:
    y_syn = h + 0.08*(x - 5)**2
    ax3.plot(x, y_syn, color='#475569', lw=2)
tunnel_3 = patches.Circle((5, 2.2), 0.9, facecolor='#ffffff', edgecolor='#dc2626', lw=2.5)
ax3.add_patch(tunnel_3)
ax3.text(5, 2.2, 'TUNNEL', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#dc2626')
# Water arrows
for x_w in [2.5, 7.5]:
    ax3.annotate('', xy=(4.5 if x_w < 5 else 5.5, 2.8), xytext=(x_w, 3.8),
                arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=2.5, mutation_scale=15))
ax3.text(5, 4.8, 'Water Seepage Trap!\nArtesian Water Head', color='#0369a1', fontweight='bold', fontsize=9, ha='center')
ax3.text(5, 0.4, 'WORST CONDITION (Option c)\n• Natural catchment & water trap\n• Severe flooding & heavy inflows\n• High hydrostatic lining pressure',
         ha='center', va='center', fontsize=9, fontweight='bold', color='#991b1b',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee2e2', edgecolor='#ef4444'))
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 5.5)
ax3.axis('off')
ax3.set_title('(C) Synclinal Axis / Trough\n(Severe Water Flooding)', fontsize=11, fontweight='bold', color='#991b1b')

plt.tight_layout()
plt.savefig('figures_Q85/tunneling_geological_conditions_strata.png', dpi=300)
plt.close()
print("Figure 85 generated.")
