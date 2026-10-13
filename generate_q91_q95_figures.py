import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# ==========================================
# Figure 91: Radiometric Quantities in Remote Sensing
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#f8fafc')

radiometrics = [
    ("Radiant Energy (Qλ)", "Total energy of electromagnetic radiation", "Joules (J)", "#64748b", "#f1f5f9"),
    ("Radiant Flux (Φλ)", "Time rate of radiant energy flow (dQ/dt)", "Watts (W = J/s)", "#0284c7", "#e0f2fe"),
    ("IRRADIANCE (Eλ) — TARGET", "Radiant flux INCIDENT UPON a surface PER UNIT AREA\nEλ = dΦ / dA (Downwelling incoming flux)", "Watts / m² (W·m⁻²)", "#16a34a", "#dcfce7"),
    ("Radiant Exitance (Mλ)", "Radiant flux EMITTED / LEAVING from a surface PER UNIT AREA\nMλ = dΦ / dA (Upwelling exitance)", "Watts / m² (W·m⁻²)", "#b45309", "#fef3c7"),
    ("Radiance (Lλ)", "Radiant flux per unit projected area per unit solid angle\nLλ = d²Φ / (dA·cosθ·dΩ) — What sensors measure!", "Watts / (m² · sr)", "#7c3aed", "#f3e8ff")
]

y_vals = np.linspace(4.8, 0.4, 5)

for y, (name, desc, unit, col, bg) in zip(y_vals, radiometrics):
    ax.text(0.5, y+0.35, name, fontsize=11.5, fontweight='bold', color=col,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=bg, edgecolor=col, lw=1.5))
    ax.text(0.5, y-0.1, desc, fontsize=9.5, color='#1e293b')
    ax.text(9.5, y+0.15, f"Unit: {unit}", fontsize=10, fontweight='bold', color=col, ha='right')
    ax.axhline(y-0.3, color='#e2e8f0', lw=1)

ax.set_xlim(0, 10)
ax.set_ylim(-0.2, 5.8)
ax.axis('off')
ax.set_title("Fundamental Radiometric Quantities in Remote Sensing & Optical Physics\nDGMS 2019 Examination • Verified Official Key: (c) Irradiance (Eλ)", fontsize=12.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q91/radiometric_quantities_irradiance.png', dpi=300)
plt.close()
print("Figure 91 generated.")

# ==========================================
# Figure 92: Polarization of Reflected Light & Brewster's Angle
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#ffffff')

# Water surface
ax.axhline(2.5, color='#0284c7', lw=2)
ax.fill_between([0, 10], [0, 0], [2.5, 2.5], color='#38bdf8', alpha=0.25)
ax.text(8.5, 2.1, 'WATER SURFACE (n ≈ 1.333)', color='#0369a1', fontweight='bold', fontsize=9.5)

# Normal line
ax.plot([5, 5], [1.0, 5.5], color='#94a3b8', linestyle=':', lw=1.5)
ax.text(5.1, 5.3, 'Surface Normal', color='#64748b', fontsize=8.5)

# Incident unpolarized ray
ax.annotate('', xy=(5, 2.5), xytext=(1.5, 5.5),
            arrowprops=dict(arrowstyle="-|>", color='#eab308', lw=3, mutation_scale=20))
ax.text(2.5, 4.5, 'Unpolarized Sunlight\n(Random vibration in all planes)', color='#854d0e', fontweight='bold', fontsize=9.5)

# Reflected ray (Polarized!)
ax.annotate('', xy=(8.5, 5.5), xytext=(5, 2.5),
            arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=3, mutation_scale=20))
ax.text(7.2, 3.8, 'Reflected Light:\nCOMPLETELY POLARIZED!\n(Vibrates parallel to surface plane)\nBrewster Angle θB ≈ 53°', color='#b91c1c', fontweight='bold', fontsize=9.5)

# Refracted ray
ax.annotate('', xy=(6.5, 0.5), xytext=(5, 2.5),
            arrowprops=dict(arrowstyle="-|>", color='#0284c7', lw=2, mutation_scale=15))
ax.text(6.0, 1.2, 'Refracted Ray', color='#0369a1', fontsize=9)

# Polarizing filter camera
ax.text(8.5, 5.8, 'Camera with Polarizing Filter\nBlocks surface reflected glare!', ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1e3a8a',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#eff6ff', edgecolor='#3b82f6'))

# Note on blue sky polarization
ax.text(5.0, 0.4, 'FACT CHECK ON STATEMENTS:\n1. Plane polarized light vibrates in one plane only (TRUE).\n2. Light reflected from water surface is linearly polarized (TRUE - Brewster Law).\n3. Blue sky light is strongly polarized by Rayleigh scattering (Statement 3 is FALSE).',
        ha='center', va='center', fontsize=9, fontweight='bold', color='#1e293b',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8fafc', edgecolor='#64748b', lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 6.8)
ax.axis('off')
ax.set_title("Polarization of Reflected Light & Brewster's Angle (Water Reflection Glare)\nDGMS 2019 Examination • Verified Official Key: (a) 1 and 2", fontsize=12.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q92/polarization_reflected_light_brewster.png', dpi=300)
plt.close()
print("Figure 92 generated.")

# ==========================================
# Figure 93: Earth Curvature Manifestation vs Altitude
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)

# (A) Low Altitude Sensor (Least Curvature Manifested)
ax1.set_facecolor('#f8fafc')
# Flat ground patch
ax1.plot([0, 10], [1.5, 1.5], color='#16a34a', lw=3)
ax1.text(5, 1.0, 'Local Ground Surface (Patch length ~10 km)\nEarth radius R = 6371 km >> Swath width\nSpherical curvature deviation Δh ≈ D² / (2R) ≈ 0 m!\nSurface appears completely FLAT!', 
         ha='center', va='center', fontsize=9, fontweight='bold', color='#166534',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#dcfce7', edgecolor='#22c55e'))

# Low altitude satellite
ax1.plot(5, 4.5, marker='s', markersize=12, color='#0284c7')
ax1.text(5, 4.9, 'Low Altitude Sensor (e.g. UAV / Aircraft / LEO)', ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#0369a1')
# Field of view lines
ax1.plot([5, 2], [4.5, 1.5], color='#0284c7', linestyle='--', lw=1.5)
ax1.plot([5, 8], [4.5, 1.5], color='#0284c7', linestyle='--', lw=1.5)

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5.8)
ax1.axis('off')
ax1.set_title('(A) Lowest Altitude Sensor\n• LEAST Curvature Manifested in Image\n• Local tangent plane approximation holds\n• Curvature distortion is virtually negligible', fontsize=11, fontweight='bold', color='#166534')

# (B) High Altitude Sensor (Prominent Curvature Manifested)
ax2.set_facecolor('#f8fafc')
# Curved Earth arc
theta = np.linspace(np.pi*0.25, np.pi*0.75, 100)
arc_r = 5.0
arc_cx = 5.0
arc_cy = -2.0
x_arc = arc_cx + arc_r * np.cos(theta)
y_arc = arc_cy + arc_r * np.sin(theta)
ax2.plot(x_arc, y_arc, color='#16a34a', lw=3)
ax2.fill_between(x_arc, 0, y_arc, color='#86efac', alpha=0.3)
ax2.text(5, 1.2, 'Global Spherical Earth Horizon\nBroad continental swath subtends large arc θ\nProminent circular Earth curvature visibly manifested!', 
         ha='center', va='center', fontsize=9, fontweight='bold', color='#1e3a8a',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#eff6ff', edgecolor='#3b82f6'))

# High altitude satellite
ax2.plot(5, 4.8, marker='s', markersize=12, color='#b45309')
ax2.text(5, 5.2, 'High Altitude Sensor (e.g. Geostationary 36,000 km)', ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#9a3412')
# FOV lines to horizon
ax2.plot([5, 1.5], [4.8, 1.5], color='#ea580c', linestyle='--', lw=1.5)
ax2.plot([5, 8.5], [4.8, 1.5], color='#ea580c', linestyle='--', lw=1.5)

ax2.set_xlim(0, 10)
ax2.set_ylim(0, 5.8)
ax2.axis('off')
ax2.set_title('(B) Highest Altitude Sensor\n• HIGHEST Curvature Manifested in Image\n• Full global spherical arc is imaged', fontsize=11, fontweight='bold', color='#9a3412')

plt.tight_layout()
plt.savefig('figures_Q93/earth_curvature_manifestation_altitude.png', dpi=300)
plt.close()
print("Figure 93 generated.")

# ==========================================
# Figure 94: Nucleosynthesis & The Bi-209 Limit
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.set_facecolor('#ffffff')

# Nucleosynthesis flow
ax.text(5.0, 5.8, 'STELLAR NUCLEOSYNTHESIS: HOW HEAVY ELEMENTS ARE FORMED', ha='center', va='center', fontsize=12, fontweight='bold', color='#0f172a')

# s-process path terminating at Bi-209
ax.text(2.5, 4.5, 'SLOW NEUTRON CAPTURE (s-process)\n• In AGB giant stars: (τ_neutron >> τ_beta)\n• Nuclei beta-decay before capturing next neutron\n• TERMINATES AT ²⁰⁹Bi (Bismuth-209)!\n  ²⁰⁹Bi + n ➔ ²¹⁰Bi ➔ ²¹⁰Po ➔ ²⁰⁶Pb + α\n  (Closed alpha-decay cycle terminates s-process!)',
        fontsize=9.5, color='#1e3a8a', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#eff6ff', edgecolor='#3b82f6', lw=1.5))

# Bottleneck line
ax.plot([5.2, 5.2], [1.0, 5.0], color='#dc2626', linestyle='--', lw=2.5)
ax.text(5.2, 3.2, '²⁰⁹Bi TERMINUS\n(Bottleneck!)', ha='center', va='center', color='#b91c1c', fontweight='bold', fontsize=9.5,
        bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#dc2626'))

# r-process and p-process blowing past Bi-209
ax.text(7.6, 4.5, 'RAPID PROCESSES (Beyond ²⁰⁹Bi):\n\n1. RAPID NEUTRON CAPTURE (r-process):\n• Neutron star mergers & core-collapse supernovae\n• Extreme neutron flux (τ_neutron << τ_beta)\n• Synthesizes ACTINIDES: ²³²Th, ²³⁵U, ²³⁸U!\n\n2. RAPID PROTON CAPTURE (p-process):\n• Synthesizes proton-rich heavy isotopes',
        fontsize=9.5, color='#166534', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#dcfce7', edgecolor='#22c55e', lw=1.5))

# Summary box
ax.text(5.0, 1.2, 'CONCLUSION FOR DGMS EXAM:\nNuclides heavier than ²⁰⁹Bi CANNOT be formed by the s-process, p-p chain, or CNO cycle.\nThey are formed exclusively by the RAPID NEUTRON CAPTURE (r-process) and PROTON CAPTURE (p-process)!\n(Verified Official Key: Option c)',
        ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0f172a',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#475569', lw=1.2))

ax.set_xlim(0, 10.2)
ax.set_ylim(0.2, 6.4)
ax.axis('off')
ax.set_title("Cosmochemistry & Nucleosynthesis: Overcoming the ²⁰⁹Bi Limit via the r-Process & p-Process\n(White Geochemistry Chapter 10 & Faure Isotope Geology)", fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q94/nucleosynthesis_bi209_r_process_p_process.png', dpi=300)
plt.close()
print("Figure 94 generated.")

# ==========================================
# Figure 95: Nepheline + Quartz = Albite Reaction
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_facecolor('#f8fafc')

# Stoichiometry boxes
ax.text(2.0, 4.2, 'NEPHELINE (Feldspathoid)\nNaAlSiO₄\n(Silica-Undersaturated)', ha='center', va='center', fontsize=11, fontweight='bold', color='#1e3a8a',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#dbeafe', edgecolor='#1e3a8a', lw=1.5))

ax.text(3.7, 4.2, '+', ha='center', va='center', fontsize=20, fontweight='bold', color='#0f172a')

ax.text(5.4, 4.2, '2 QUARTZ\n2 SiO₂\n(Silica Phase)', ha='center', va='center', fontsize=11, fontweight='bold', color='#0f766e',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ccfbf1', edgecolor='#0f766e', lw=1.5))

ax.annotate('', xy=(7.2, 4.2), xytext=(6.5, 4.2),
            arrowprops=dict(arrowstyle="-|>", color='#dc2626', lw=3, mutation_scale=20))

ax.text(8.7, 4.2, 'ALBITE (Plagioclase)\nNaAlSi₃O₈\n(Silica-Saturated)', ha='center', va='center', fontsize=11.5, fontweight='bold', color='#b91c1c',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fee2e2', edgecolor='#dc2626', lw=2))

# Chemical explanation
ax.text(5.0, 2.0, 'PETROLOGICAL SIGNIFICANCE (Winter Petrology Chapter 7 & Perkins Mineralogy):\n\n• Incompatible Assemblage: Nepheline and Quartz can NEVER stably coexist together in igneous rocks!\n• Any excess silica reacts completely with nepheline to form albite:\n  NaAlSiO₄ + 2 SiO₂ ➔ NaAlSi₃O₈ (Albite)\n• Albite acts as the critical THERMAL DIVIDE between:\n  1. Silica-undersaturated alkaline magmas (foid syenites, phonolites)\n  2. Silica-oversaturated subalkaline magmas (granites, rhyolites)',
        ha='center', va='center', fontsize=9.5, color='#1e293b',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.2))

ax.set_xlim(0, 10.5)
ax.set_ylim(0.5, 5.5)
ax.axis('off')
ax.set_title("Mineral Chemistry: Combination of Nepheline and Quartz Yields Albite\nDGMS 2019 Examination • Verified Official Key: (d) Albite", fontsize=12.5, fontweight='bold', color='#0f172a', pad=12)

plt.tight_layout()
plt.savefig('figures_Q95/nepheline_quartz_albite_reaction.png', dpi=300)
plt.close()
print("Figure 95 generated.")
