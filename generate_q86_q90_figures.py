import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# ==========================================
# Figure 86: Geothermal Energy Systems
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#f8fafc')

# Left side: Shallow surface thermal envelope
ax.axhspan(4.5, 5.5, color='#fed7aa', alpha=0.3)
ax.plot([0.5, 4.0], [5.0, 5.0], color='#ea580c', lw=2)
ax.text(2.25, 5.2, 'Shallow Ground (0–15 m depth):\nSeasonal temperature variation penetrates only < 10–15 m!\nHas ZERO effect on commercial geothermal reservoirs at 1–3 km depth.',
        fontsize=9, color='#9a3412', ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffedd5', edgecolor='#ea580c'))

# Middle/Bottom: Magmatic hydrothermal convection system
magma = patches.Ellipse((2.25, 1.2), 3.0, 1.2, facecolor='#dc2626', edgecolor='#991b1b', lw=2)
ax.add_patch(magma)
ax.text(2.25, 1.2, 'MAGMA CHAMBER / INTRUSION\n(T > 700°C–1000°C at Plate Boundary)', ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)

# Hydrothermal circulation loops
for x_c in [1.2, 3.3]:
    ax.annotate('', xy=(x_c, 3.8), xytext=(x_c, 2.0),
                arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=2.5, mutation_scale=15))
ax.text(2.25, 2.8, 'Deep Meteoric Groundwater\nCirculation & Convection\n(T = 150°C–350°C)', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0369a1')

# Right side: Geothermal Gradient Comparison
ax.text(7.2, 4.8, 'GEOTHERMAL GRADIENT COMPARISON:', fontsize=10.5, fontweight='bold', color='#1e3a8a')

grad_data = [
    ("Normal Continental Crust", "25°C – 30°C / km", "Background conductive gradient;\nFar too low for commercial power generation!", "#64748b", "#f1f5f9"),
    ("Commercial Geothermal Fields", "> 100°C – 250°C / km", "High-enthalpy fields along plate boundaries\n(e.g., Iceland, The Geysers, Taupo TVZ, Ring of Fire)", "#dc2626", "#fee2e2")
]

y_p = [3.4, 1.4]
for y, (name, val, desc, col, bg) in zip(y_p, grad_data):
    ax.text(7.2, y+0.4, f"{name}: {val}", fontsize=10, fontweight='bold', color=col,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=bg, edgecolor=col, lw=1.2))
    ax.text(7.2, y-0.1, desc, fontsize=8.5, color='#334155')

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.8)
ax.axis('off')
ax.set_title("Geothermal Energy Principles: Plate Boundary Settings & Thermal Gradients\nDGMS 2019 Examination • Verified Official Key: (a) 1 and 3 only", fontsize=12.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q86/geothermal_energy_plate_boundaries_gradients.png', dpi=300)
plt.close()
print("Figure 86 generated.")

# ==========================================
# Figure 87: Ocean Acidification Chemistry
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#f8fafc')

steps = [
    ("1. Fossil Fuel & Industrial CO2 Emissions", "CO2 enters atmosphere and dissolves into surface ocean waters\nCO2(atm) ➔ CO2(aq)", "#1e293b", "#e2e8f0"),
    ("2. Carbonic Acid Formation & Acidification", "Dissolved CO2 reacts with water to release hydrogen ions (H+):\nCO2(aq) + H2O ⇌ H2CO3 ⇌ H+ + HCO3-\n➔ Increases [H+] ions: Lowers seawater pH (MAKES OCEAN ACIDIC!)", "#dc2626", "#fee2e2"),
    ("3. Carbonate Ion Depletion (The Calcification Crisis)", "Excess H+ reacts with and CONSUMES dissolved carbonate ions (CO3 2-):\nH+ + CO3 2- ⇌ HCO3- (Bicarbonate)\n➔ Depletes CO3 2- needed for CaCO3 shell formation!", "#b45309", "#fef3c7"),
    ("4. Shell Dissolution & Biological Harm", "Calcifying organisms (corals, pteropods, foraminifera, mollusks)\nCANNOT build shells and existing CaCO3 shells dissolve!\n(Statement 3 claiming CO2 'helps shell formation' is FALSE!)", "#7f1d1d", "#fecaca")
]

y_crds = np.linspace(4.8, 0.4, 4)

for y, (title, desc, col, bg) in zip(y_crds, steps):
    ax.text(0.5, y+0.4, title, fontsize=11, fontweight='bold', color=col,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=bg, edgecolor=col, lw=1.2))
    ax.text(0.5, y-0.1, desc, fontsize=9.5, color='#1e293b')
    if y > 1.0:
        ax.annotate('', xy=(5.0, y-0.35), xytext=(5.0, y-0.15),
                    arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=2, mutation_scale=12))

ax.set_xlim(0, 10)
ax.set_ylim(-0.2, 5.8)
ax.axis('off')
ax.set_title("Ocean Acidification Geochemical Cascade & Marine Shell Calcification\nDGMS 2019 Examination • Verified Official Key: (a) 1 only", fontsize=12.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q87/ocean_acidification_carbonate_chemistry.png', dpi=300)
plt.close()
print("Figure 87 generated.")

# ==========================================
# Figure 88: Saltwater Intrusion & Ghyben-Herzberg
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#ffffff')

# Topography and sea level
x_pts = np.linspace(0, 10, 200)
land_surface = 5.0 - 0.2*x_pts
water_table = 4.2 - 0.15*x_pts # above sea level for x < 7

# Sea level line at y = 3.15
sea_level = 3.15
ax.axhline(sea_level, color='#0284c7', linestyle=':', lw=1.5)
ax.text(9.5, sea_level+0.15, 'Mean Sea Level (MSL = 0)', color='#0284c7', fontsize=9.5, fontweight='bold', ha='right')

# Ocean water wedge on right
ax.fill_between([6.5, 10, 10, 6.5], [sea_level, sea_level, 0, 0], color='#38bdf8', alpha=0.3)
ax.text(8.2, 1.5, 'SEA WATER\n(Density ρs = 1.025 g/cm³)', ha='center', va='center', color='#0369a1', fontweight='bold', fontsize=10)

# Ghyben-Herzberg saltwater interface: z = 40 h
# Fresh water lens floats over saltwater
interface_x = np.linspace(0, 6.5, 100)
h_fresh = water_table[:100] - sea_level
interface_y = sea_level - 1.8 * (6.5 - interface_x) / 6.5 # schematic 40:1 scale

# Freshwater zone
ax.fill_between(interface_x, np.maximum(interface_y, 0), water_table[:100], color='#bbf7d0', alpha=0.35)
ax.text(2.5, 2.5, 'FRESHWATER LENS\n(Density ρf = 1.000 g/cm³)\nFloats on denser saltwater!', ha='center', va='center', color='#166534', fontweight='bold', fontsize=10)

# Saltwater beneath lens
ax.fill_between(interface_x, 0, np.maximum(interface_y, 0), color='#fed7aa', alpha=0.3)
ax.text(2.5, 0.4, 'Encroaching Saltwater Wedge (ρs > ρf)', ha='center', va='center', color='#9a3412', fontweight='bold', fontsize=9.5)

# Interface line
ax.plot(interface_x, np.maximum(interface_y, 0), color='#ea580c', lw=2.5, linestyle='--')
ax.text(4.2, 1.2, 'Ghyben-Herzberg Interface (z ≈ 40 · h)', color='#c2410c', fontweight='bold', fontsize=9.5, rotation=15)

# Pumping well and upconing
ax.plot([3.5, 3.5], [1.8, 5.2], color='#1e293b', lw=3)
ax.text(3.5, 5.5, 'Over-Pumping Well\n(Causes Upconing & Encroachment!)', ha='center', va='bottom', color='#b91c1c', fontweight='bold', fontsize=9.5)

# Upconing bulge
upcone_x = np.linspace(2.5, 4.5, 50)
upcone_y = 1.1 + 0.5 * np.cos(np.pi * (upcone_x - 3.5) / 1.0)
ax.plot(upcone_x, upcone_y, color='#dc2626', lw=2.5)
ax.text(3.5, 1.5, '▲ Saltwater Upconing', color='#b91c1c', fontweight='bold', fontsize=9, ha='center')

ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.axis('off')
ax.set_title("Ghyben-Herzberg Principle: Coastal Freshwater Lens & Saltwater Intrusion\nDGMS 2019 Examination • Verified Official Key: (a) 1 and 3 only", fontsize=12, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q88/ghyben_herzberg_saltwater_intrusion.png', dpi=300)
plt.close()
print("Figure 88 generated.")

# ==========================================
# Figure 89: BOD and Dissolved Oxygen Sag Curve
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_facecolor('#f8fafc')

x_t = np.linspace(0, 10, 200)
# Waste discharge at x = 1.5
# BOD curve: spikes at 1.5 then decays exponentially
bod = np.zeros_like(x_t)
bod[x_t >= 1.5] = 9.0 * np.exp(-0.4 * (x_t[x_t >= 1.5] - 1.5))

# DO sag curve (Streeter-Phelps)
do_curve = 8.5 * np.ones_like(x_t)
deficit = np.zeros_like(x_t)
deficit[x_t >= 1.5] = 6.5 * (np.exp(-0.4*(x_t[x_t >= 1.5]-1.5)) - np.exp(-0.8*(x_t[x_t >= 1.5]-1.5)))
do_curve = 8.5 - deficit

ax.plot(x_t, bod, color='#dc2626', lw=2.5, label='Biochemical Oxygen Demand (BOD) — Organic Matter Load')
ax.plot(x_t, do_curve, color='#0284c7', lw=2.5, label='Dissolved Oxygen (DO) Concentration (mg/L)')

# Organic discharge point
ax.annotate('Organic Waste Discharge\n(Point Source Pollution)', xy=(1.5, 8.5), xytext=(0.8, 9.8),
            arrowprops=dict(arrowstyle="-|>", color='#b91c1c', lw=2),
            fontsize=9.5, fontweight='bold', color='#991b1b')

# Critical DO deficit
min_idx = np.argmin(do_curve)
ax.annotate('Critical DO Deficit Point\n(Fish Kill Zone / Anaerobic Stress)', xy=(x_t[min_idx], do_curve[min_idx]), xytext=(x_t[min_idx]+0.5, do_curve[min_idx]-1.2),
            arrowprops=dict(arrowstyle="-|>", color='#0369a1', lw=2),
            fontsize=9.5, fontweight='bold', color='#075985')

ax.set_xlim(0, 10)
ax.set_ylim(0, 11)
ax.set_xlabel('Distance Downstream / Travel Time from Outfall ➔', fontsize=10.5, fontweight='bold', color='#1e293b')
ax.set_ylabel('Concentration (mg/L)', fontsize=10.5, fontweight='bold', color='#1e293b')
ax.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='#cbd5e1', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title("Organic Matter Loading & The Dissolved Oxygen Sag Curve (Streeter-Phelps Model)\nDGMS 2019 Examination • Verified Official Key: (b) Biochemical oxygen demand (BOD)", fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q89/bod_dissolved_oxygen_sag_curve.png', dpi=300)
plt.close()
print("Figure 89 generated.")

# ==========================================
# Figure 90: Earthquake Epicenter Triangulation
# ==========================================
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
ax.set_facecolor('#ffffff')

# True Epicenter at (5, 4.5)
epi_x, epi_y = 5.0, 4.5

# Three seismograph stations
stations = [
    ("Station 1 (Jaipur)", 2.0, 2.0, "#1e3a8a"),
    ("Station 2 (Delhi)", 8.0, 3.0, "#0f766e"),
    ("Station 3 (Shimla)", 4.0, 8.0, "#b45309")
]

for name, sx, sy, col in stations:
    r = np.sqrt((sx - epi_x)**2 + (sy - epi_y)**2)
    # Circle of distance from (tS - tP)
    circle = patches.Circle((sx, sy), r, fill=False, edgecolor=col, linestyle='--', lw=2)
    ax.add_patch(circle)
    # Station marker
    ax.plot(sx, sy, marker='^', markersize=12, color=col)
    ax.text(sx, sy-0.4, f"{name}\nΔt = (tS - tP)\nDistance r = {r:.1f} km", ha='center', va='top', fontsize=9, fontweight='bold', color=col)

# Epicenter star
ax.plot(epi_x, epi_y, marker='*', markersize=20, color='#dc2626', markeredgecolor='#7f1d1d')
ax.text(epi_x, epi_y+0.4, '★ EARTHQUAKE EPICENTER\n(Intersection of ≥ 3 Station Circles)', ha='center', va='bottom', fontsize=11, fontweight='bold', color='#b91c1c')

ax.text(5.0, 0.4, 'TRIANGULATION METHOD:\n1. Measure (tS - tP) arrival time difference at each seismograph station.\n2. Compute epicentral distance: D = (tS - tP) / (1/Vs - 1/Vp).\n3. Draw distance circles from at least THREE stations; their intersection locates the EPICENTER.',
        ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e293b',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#eff6ff', edgecolor='#3b82f6', lw=1.2))

ax.set_xlim(-1, 11)
ax.set_ylim(-0.2, 9.5)
ax.axis('off')
ax.set_title("Seismology: Earthquake Epicenter Location by Three-Station Triangulation\nDGMS 2019 Examination • Verified Official Key: (b) 1 and 3 only", fontsize=12, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q90/earthquake_epicenter_triangulation_stations.png', dpi=300)
plt.close()
print("Figure 90 generated.")
