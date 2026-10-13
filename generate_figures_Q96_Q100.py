import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Set high visual publication standards
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# ==========================================
# Figure 96: Halmyrolysis (Submarine Weathering & Ion Exchange)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_facecolor('#f8fafc')

# Draw river entering marine basin
x = np.linspace(0, 10, 200)
# Estuary and ocean water line
ax.fill_between([0, 10], [6, 6], [8.5, 8.5], color='#bae6fd', alpha=0.5, label='Marine Water Column (High Salinity: Na+, Mg2+, K+, SO42-)')
# River inflow
ax.fill_between([0, 3], [5.5, 5.5], [6, 6], color='#7dd3fc', alpha=0.8, label='River Inflow (Freshwater with Suspended Clays & Dissolved Ions)')
# Seafloor sediment bed
ax.fill_between([0, 10], [1, 1], [5.5, 5.5], color='#fed7aa', alpha=0.7, label='Seafloor Sediments / Volcanics undergoing Halmyrolysis')
ax.fill_between([0, 10], [0, 0], [1, 1], color='#cbd5e1', alpha=0.8, label='Oceanic Basement (Basalt)')

# Annotations of chemical exchange
ax.annotate('River Water Ingress\nCarrying Clay Minerals\n& Terrestrial Ions', xy=(1.5, 5.8), xytext=(0.5, 7.2),
            fontsize=10, fontweight='bold', color='#0369a1',
            arrowprops=dict(facecolor='#0369a1', edgecolor='none', width=2, headwidth=7))

# Ion removal and adsorption arrows
ax.annotate('HALMYROLYSIS ZONE\n(Submarine Weathering)', xy=(5.5, 5.5), xytext=(4.5, 7.5),
            fontsize=12, fontweight='bold', color='#b45309',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef3c7', edgecolor='#b45309', lw=1.5),
            arrowprops=dict(facecolor='#b45309', edgecolor='none', width=2, headwidth=8))

# Chemical reactions
exchange_text = (
    "Chemical Processes in Halmyrolysis:\n"
    "1. Removal of River Ions (Flocculation of Fe, Al, Si colloids)\n"
    "2. Cation Exchange: Clays take up Mg²⁺, K⁺, Na⁺ from seawater; release Ca²⁺\n"
    "3. Low-temperature alteration of basaltic glass & ash to Smectite, Glauconite, Zeolites\n"
    "4. Sinks for oceanic K, Mg, and silica prior to deep burial"
)
ax.text(5.0, 3.2, exchange_text, fontsize=10.5, color='#1e293b',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.2))

# Exchange arrows
ax.annotate('K⁺, Mg²⁺, Na⁺ Uptake', xy=(4.0, 4.8), xytext=(4.0, 6.2),
            fontsize=9.5, fontweight='bold', color='#15803d',
            arrowprops=dict(facecolor='#15803d', edgecolor='none', width=1.5, headwidth=6))
ax.annotate('Ca²⁺ Desorption', xy=(7.0, 6.2), xytext=(7.0, 4.8),
            fontsize=9.5, fontweight='bold', color='#b91c1c',
            arrowprops=dict(facecolor='#b91c1c', edgecolor='none', width=1.5, headwidth=6))

ax.set_xlim(0, 10)
ax.set_ylim(0, 8.8)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Halmyrolysis: Submarine Weathering & Ion Exchange at the River-Sea Interface\n(DGMS JSO Geology 2019 • Q.96)",
             fontsize=13, fontweight='bold', color='#0f172a', pad=14)
ax.legend(loc='lower center', ncol=2, fontsize=8.5, frameon=True, facecolor='white')

plt.tight_layout()
plt.savefig('figures_Q96/halmyrolysis_submarine_weathering_ion_exchange.png', dpi=300)
plt.close()
print("Figure 96 generated.")

# ==========================================
# Figure 97: Initial 87Sr/86Sr Ratio of Earth (BABI - Basaltic Achondrites)
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5), dpi=300)

# Subplot 1: Rb-Sr Isochron Concept for Achondrites
time_evolution = np.array([4.56, 3.0, 1.5, 0.0]) # Ga
sr_babi = 0.69897
# Achondrite (Extremely low Rb/Sr ~ 0.001)
sr_achondrite = sr_babi + 0.001 * (np.exp(1.42e-11 * (4.56e9 - time_evolution*1e9)) - 1)
# Bulk Silicate Earth (Rb/Sr ~ 0.08)
sr_bse = sr_babi + 0.08 * (np.exp(1.42e-11 * (4.56e9 - time_evolution*1e9)) - 1)
# Continental Crust (High Rb/Sr ~ 0.25)
sr_crust = sr_babi + 0.25 * (np.exp(1.42e-11 * (4.56e9 - time_evolution*1e9)) - 1)

age_axis = 4.56 - time_evolution

ax1.plot(age_axis, sr_achondrite, 'o-', color='#b91c1c', lw=2.5, label='Basaltic Achondrite (Rb/Sr ≈ 0)\nInitial ⁸⁷Sr/⁸⁶Sr = 0.69897 (BABI)')
ax1.plot(age_axis, sr_bse, 's-', color='#1e3a8a', lw=2.2, label='Bulk Silicate Earth / Mantle (Rb/Sr ≈ 0.08)')
ax1.plot(age_axis, sr_crust, '^--', color='#d97706', lw=1.8, label='Continental Crust (Rb/Sr ≈ 0.25)')

ax1.scatter([0], [sr_babi], color='#dc2626', s=140, zorder=5)
ax1.annotate('BABI = 0.69897\n(Achondrite Best Initial)\nPapanastassiou & Wasserburg (1969)',
             xy=(0, sr_babi), xytext=(0.4, 0.706),
             fontsize=9.5, fontweight='bold', color='#dc2626',
             arrowprops=dict(facecolor='#dc2626', edgecolor='none', width=1.5, headwidth=6),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'))

ax1.set_xlabel("Time Elapsed Since Formation (Gyr)", fontsize=11, fontweight='bold', color='#1e293b')
ax1.set_ylabel("⁸⁷Sr / ⁸⁶Sr Ratio", fontsize=11, fontweight='bold', color='#1e293b')
ax1.set_title("⁸⁷Sr/⁸⁶Sr Growth Curves over 4.56 Ga", fontsize=12, fontweight='bold', color='#0f172a')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=8.5, frameon=True)

# Subplot 2: Summary of Solar System Initial Sr Standards
categories = ['BABI\n(Basaltic\nAchondrite)', 'ALL\n(Allende CAI\nChondrite)', 'Bulk Earth\n(Estimated Initial)', 'Modern Mantle\n(MORB Source)', 'Continental\nCrust (Avg)']
values = [0.69897, 0.69877, 0.69897, 0.70280, 0.71200]
colors = ['#dc2626', '#f97316', '#2563eb', '#059669', '#7c3aed']

bars = ax2.bar(categories, values, color=colors, width=0.55, edgecolor='#334155', lw=1.2)
ax2.set_ylim(0.695, 0.715)
ax2.set_ylabel("⁸⁷Sr / ⁸⁶Sr Ratio", fontsize=11, fontweight='bold', color='#1e293b')
ax2.set_title("Comparison of Solar System & Earth Sr Isotope Values", fontsize=12, fontweight='bold', color='#0f172a')
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.0005, f"{yval:.5f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

ax2.grid(axis='y', linestyle='--', alpha=0.5)
plt.suptitle("Origin of Earth's Initial ⁸⁷Sr/⁸⁶Sr Ratio: The Basaltic Achondrite Best Initial (BABI)\n(DGMS JSO Geology 2019 • Q.97)",
             fontsize=13, fontweight='bold', color='#0f172a', y=1.02)
plt.tight_layout()
plt.savefig('figures_Q97/sr_isotope_evolution_babi_achondrite.png', dpi=300, bbox_inches='tight')
plt.close()
print("Figure 97 generated.")

# ==========================================
# Figure 98: Goldschmidt's Geochemical Classification
# ==========================================
fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
ax.set_facecolor('#f8fafc')

# 4 Quadrants for Goldschmidt's Classification
# 1. Lithophile
ax.fill_between([0, 5], [5, 5], [10, 10], color='#dbeafe', alpha=0.8)
ax.text(2.5, 9.4, "LITHOPHILE (Silicate-Loving)", fontsize=13, fontweight='bold', color='#1e3a8a', ha='center')
ax.text(2.5, 8.8, "Enriched in Silicates & Oxides • Strong affinity for O\nHigh charge, ionic radius, heat of oxide formation", fontsize=9.5, color='#1e40af', ha='center')
litho_elements = "Li, Na, K, Rb, Cs, Be, Mg, Ca, Sr, Ba,\nAl, REE, Si, Ti, Zr, Hf, V, Nb, Ta, U, Th, O, F"
ax.text(2.5, 7.0, litho_elements, fontsize=11, fontweight='bold', color='#0f172a', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#eff6ff', edgecolor='#3b82f6'))
ax.text(2.5, 5.5, "Options: Oxygen (a) [Litho], Lithium (b) [Litho], Niobium (d) [Litho]", fontsize=9, color='#1e3a8a', ha='center', fontstyle='italic')

# 2. Chalcophile (Highlighted)
ax.fill_between([5, 10], [5, 5], [10, 10], color='#fef3c7', alpha=0.9)
ax.text(7.5, 9.4, "CHALCOPHILE (Sulfur-Loving) ★", fontsize=13, fontweight='bold', color='#b45309', ha='center')
ax.text(7.5, 8.8, "Enriched in Sulfides • Strong affinity for S\nCovalent bonding, intermediate electronegativity", fontsize=9.5, color='#92400e', ha='center')
chalco_elements = "Cu, Ag, Zn, Cd, Hg, Ga, In, Tl, Pb, As, Sb, Bi, S, Se, Te"
ax.text(7.5, 7.0, chalco_elements, fontsize=11.5, fontweight='bold', color='#78350f', ha='center',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#fef08a', edgecolor='#b45309', lw=2))
ax.text(7.5, 5.5, "★ Option (c): Silver (Ag) is a quintessential CHALCOPHILE element!", fontsize=9.5, fontweight='bold', color='#b45309', ha='center')

# 3. Siderophile
ax.fill_between([0, 5], [0, 0], [5, 5], color='#f1f5f9', alpha=0.8)
ax.text(2.5, 4.4, "SIDEROPHILE (Iron-Loving)", fontsize=13, fontweight='bold', color='#334155', ha='center')
ax.text(2.5, 3.8, "Enriched in Metallic Core • Metallic bonding\nAffinity for metallic Fe-Ni alloys", fontsize=9.5, color='#475569', ha='center')
sidero_elements = "Fe, Co, Ni, Ru, Rh, Pd, Os, Ir, Pt, Au, Re"
ax.text(2.5, 2.3, sidero_elements, fontsize=11, fontweight='bold', color='#1e293b', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

# 4. Atmophile
ax.fill_between([5, 10], [0, 0], [5, 5], color='#dcfce7', alpha=0.8)
ax.text(7.5, 4.4, "ATMOPHILE (Gas / Volatile)", fontsize=13, fontweight='bold', color='#166534', ha='center')
ax.text(7.5, 3.8, "Enriched in Atmosphere & Hydrosphere\nVolatile elemental gases or hydrides", fontsize=9.5, color='#15803d', ha='center')
atmo_elements = "H, C, N, He, Ne, Ar, Kr, Xe"
ax.text(7.5, 2.3, atmo_elements, fontsize=11, fontweight='bold', color='#14532d', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0fdf4', edgecolor='#22c55e'))

# Border dividers
ax.axvline(5, color='#94a3b8', lw=2, linestyle='--')
ax.axhline(5, color='#94a3b8', lw=2, linestyle='--')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])

ax.set_title("Goldschmidt's Geochemical Classification of Elements: Identification of Chalcophile Ag\n(DGMS JSO Geology 2019 • Q.98)",
             fontsize=13, fontweight='bold', color='#0f172a', pad=14)

plt.tight_layout()
plt.savefig('figures_Q98/goldschmidt_geochemical_classification_periodic_table.png', dpi=300)
plt.close()
print("Figure 98 generated.")

# ==========================================
# Figure 99: Geophysical Methods, Principles, and Units
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_facecolor('#ffffff')

# Comparison Table of Geophysical Methods
methods = [
    ("GRAVITY METHOD", "Density Contrast (Δρ)\n(g/cm³)", "Gal, Milligal (mGal)\n[1 mGal = 10⁻⁵ m/s²]", "Gravimeter\n(LaCoste-Romberg)", "#2563eb", "★ Milligal is GRAVITY, NOT Magnetic!"),
    ("MAGNETIC METHOD", "Magnetic Susceptibility (κ)\nRemanent Magnetization", "Tesla (T), nanoTesla (nT),\nGamma [1 nT = 1 γ = 10⁻⁵ G]", "Proton Precession, Fluxgate,\nOptically Pumped", "#059669", "Pyrrhotite & Magnetite cause anomalies"),
    ("ELECTRICAL METHOD", "Electrical Resistivity (ρ)\nConductivity (σ)", "Ohm-meter (Ω·m),\nSiemens/m (S/m)", "Resistivity meter\n(Wenner, Schlumberger)", "#d97706", "Apparent resistivity soundings"),
    ("RADIOMETRIC METHOD", "Radioactive Decay\n(γ-ray photon flux)", "Counts per second (cps),\nBecquerel (Bq), Roentgen", "Scintillometer [NaI(Tl)],\nGamma-ray spectrometer", "#7c3aed", "Scintillometers detect U, Th, K radioactivity")
]

y_pos = [7.5, 5.2, 2.9, 0.6]

for (name, prop, unit, inst, col, highlight), y in zip(methods, y_pos):
    # Method banner
    ax.fill_between([0.2, 9.8], [y, y], [y + 1.8, y + 1.8], color=col, alpha=0.1, edgecolor=col, lw=1.5)
    ax.text(0.5, y + 1.25, name, fontsize=12, fontweight='bold', color=col)
    ax.text(0.5, y + 0.45, f"Physical Property:\n{prop}", fontsize=9.5, color='#334155')
    ax.text(3.6, y + 0.85, f"Standard Units:\n{unit}", fontsize=9.5, fontweight='bold', color='#0f172a')
    ax.text(6.3, y + 0.85, f"Key Instrument:\n{inst}", fontsize=9.5, color='#334155')
    ax.text(0.5, y + 0.1, highlight, fontsize=9, fontweight='bold', color=col, fontstyle='italic')

ax.set_xlim(0, 10)
ax.set_ylim(0, 9.8)
ax.set_xticks([])
ax.set_yticks([])

ax.set_title("Geophysical Exploration Methods: Measured Properties, Units, and Instrumentation\n(DGMS JSO Geology 2019 • Q.99)",
             fontsize=13, fontweight='bold', color='#0f172a', pad=14)

plt.tight_layout()
plt.savefig('figures_Q99/geophysical_methods_units_gravity_magnetic.png', dpi=300)
plt.close()
print("Figure 99 generated.")

# ==========================================
# Figure 100: Geochemical Anomaly, Threshold & Background
# ==========================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
ax.set_facecolor('#f8fafc')

# Generate synthetic dispersion profile over an ore body
x_dist = np.linspace(-500, 500, 400)
background_mean = 25 # ppm
background_sd = 5 # ppm
noise = np.random.normal(0, 2.5, len(x_dist))
anomaly_peak = 180 * np.exp(-(x_dist)**2 / (2 * 60**2))
total_conc = background_mean + anomaly_peak + noise

threshold = background_mean + 2 * background_sd # 35 ppm

# Plot profile
ax.plot(x_dist, total_conc, color='#1e3a8a', lw=2.2, label='Measured Indicator Element Concentration (ppm)')
ax.axhline(background_mean, color='#64748b', linestyle='--', lw=1.8, label=f'Local Background (Mean b̄ = {background_mean} ppm)')
ax.axhline(threshold, color='#dc2626', linestyle='-', lw=2, label=f'Local Threshold (Threshold = b̄ + 2s = {threshold} ppm)')

# Fill anomaly region
anomaly_mask = total_conc > threshold
ax.fill_between(x_dist, threshold, total_conc, where=anomaly_mask, color='#fca5a5', alpha=0.6,
                label='SIGNIFICANT GEOCHEMICAL ANOMALY (Conc > Local Threshold / Background)')

# Draw buried ore body below
ax.annotate('Buried Ore Body\n(Source of Anomaly)', xy=(0, 20), xytext=(0, -25),
            fontsize=10, fontweight='bold', color='#b45309', ha='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fef3c7', edgecolor='#b45309'),
            arrowprops=dict(facecolor='#b45309', edgecolor='none', width=2, headwidth=7))

# Annotate threshold definition
ax.annotate('Threshold Cutoff:\nValues > Background + 2σ\nSignify Mineralization!',
            xy=(120, threshold), xytext=(220, 100),
            fontsize=10, fontweight='bold', color='#dc2626',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'),
            arrowprops=dict(facecolor='#dc2626', edgecolor='none', width=1.5, headwidth=6))

ax.set_xlim(-500, 500)
ax.set_ylim(-35, 230)
ax.set_xlabel("Distance Across Strike (meters)", fontsize=11, fontweight='bold', color='#1e293b')
ax.set_ylabel("Concentration of Indicator Element (ppm)", fontsize=11, fontweight='bold', color='#1e293b')
ax.set_title("Geochemical Exploration: Distinction Between Background, Threshold, and Anomaly\n(DGMS JSO Geology 2019 • Q.100)",
             fontsize=13, fontweight='bold', color='#0f172a', pad=14)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='white')

plt.tight_layout()
plt.savefig('figures_Q100/geochemical_anomaly_background_threshold_profile.png', dpi=300)
plt.close()
print("Figure 100 generated.")
