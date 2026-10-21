#!/usr/bin/env python3
import os
import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import subprocess, glob

base_dir = '/home/tapaswi/Mines_Geology/Orrisa_geology'
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# Helper to create folders
for q in range(1, 26):
    os.makedirs(os.path.join(base_dir, f'figures_Q{q:02d}'), exist_ok=True)

print("Created figures directories figures_Q01 to figures_Q25.")

# =========================================================================
# Q1: Landslides & Shear Planes (Rotational Slump vs Translational Slide)
# =========================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=250)
fig.patch.set_facecolor('#ffffff')

# Rotational Slide (Slump)
ax1.set_facecolor('#f8fafc')
ax1.set_title('(A) Rotational Slide (Slump): Curved Spoon-Shaped Shear Plane', fontsize=11, fontweight='bold', color='#0f172a', pad=12)
x = np.linspace(0, 10, 100)
# Original slope
ax1.plot([0, 3, 8, 10], [8, 7, 2, 1], color='#94a3b8', linestyle='--', lw=1.5, label='Original Ground Surface')
# Curved slip surface
theta = np.linspace(np.pi*0.1, np.pi*0.65, 100)
cx, cy, r = 5.5, 6.0, 4.8
arc_x = cx - r * np.cos(theta)
arc_y = cy - r * np.sin(theta)
ax1.plot(arc_x, arc_y, color='#dc2626', lw=3, label='Well-Defined Shear Failure Plane (Slip Surface)')
# Displaced block surface with backward tilt
ax1.plot([1.2, 4.5, 7.5], [6.8, 5.0, 2.2], color='#0284c7', lw=2.5)
ax1.fill_between(arc_x, arc_y, np.interp(arc_x, [1.2, 4.5, 7.5], [6.8, 5.0, 2.2]), color='#bae6fd', alpha=0.6, label='Displaced Sliding Mass')
# Bedrock below
ax1.fill_between(arc_x, 0, arc_y, color='#e2e8f0', alpha=0.7, label='Stable Bedrock / Footwall (Below Shear Plane)')
ax1.annotate('Main Scarp\n(Shear Headwall)', xy=(1.5, 6.8), xytext=(0.2, 8.2),
             fontsize=9.5, fontweight='bold', color='#b91c1c', arrowprops=dict(facecolor='#b91c1c', width=1.5, headwidth=6))
ax1.annotate('Backward-Tilted\nCrown Block', xy=(3.5, 5.5), xytext=(2.0, 3.5),
             fontsize=9.5, fontweight='bold', color='#0369a1', arrowprops=dict(facecolor='#0369a1', width=1.5, headwidth=6))
ax1.annotate('Toe of Surface of Rupture\n(Transverse Ridges)', xy=(7.2, 2.0), xytext=(6.5, 0.5),
             fontsize=9.5, fontweight='bold', color='#059669', arrowprops=dict(facecolor='#059669', width=1.5, headwidth=6))
ax1.set_xlim(0, 10); ax1.set_ylim(0, 9); ax1.set_xticks([]); ax1.set_yticks([])
ax1.legend(loc='lower left', fontsize=8)

# Translational Slide
ax2.set_facecolor('#f8fafc')
ax2.set_title('(B) Translational Slide: Planar Discontinuity Shear Plane', fontsize=11, fontweight='bold', color='#0f172a', pad=12)
ax2.plot([0, 2, 8, 10], [8, 7, 2, 1], color='#94a3b8', linestyle='--', lw=1.5)
# Planar shear plane along bedding
ax2.plot([2.5, 7.5], [6.2, 1.8], color='#dc2626', lw=3, label='Planar Shear Plane (Bedding/Foliation)')
ax2.plot([3.5, 8.5], [6.6, 2.2], color='#0284c7', lw=2.5)
# Fill block
ax2.fill_between([2.5, 7.5], [6.2, 1.8], [7.2, 2.8], color='#bae6fd', alpha=0.6, label='Translational Slide Block')
ax2.fill_between([0, 2.5, 7.5, 10], [0, 0, 0, 0], [8, 6.2, 1.8, 1], color='#e2e8f0', alpha=0.7)
ax2.annotate('Driving Shear Stress (τd)\n= W · sin(θ)', xy=(5.5, 4.0), xytext=(6.8, 5.5),
             fontsize=9.5, fontweight='bold', color='#dc2626', arrowprops=dict(facecolor='#dc2626', width=2, headwidth=7))
ax2.annotate('Resisting Shear Strength (τf)\n= c\' + σn\' · tan(φ\')', xy=(4.5, 3.5), xytext=(2.0, 1.5),
             fontsize=9.5, fontweight='bold', color='#15803d', arrowprops=dict(facecolor='#15803d', width=2, headwidth=7))
ax2.set_xlim(0, 10); ax2.set_ylim(0, 9); ax2.set_xticks([]); ax2.set_yticks([])
ax2.legend(loc='lower left', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q01/landslide_shear_plane_mechanics.png'), dpi=250)
plt.close()
print("Generated Q01 landslide figure.")

# =========================================================================
# Q2: Fluvial Channel Sinuosity Index (Boggs Fig 8.9 extraction + Schematic)
# =========================================================================
# Extract Boggs Fig 8.9 directly from page 269
boggs_p269 = '/tmp/boggs_render/p_269-269.png'
if os.path.exists(boggs_p269):
    img = cv2.imread(boggs_p269)
    h, w, _ = img.shape
    # crop bottom half where Fig 8.9 sits
    fig8_9 = img[int(h*0.52):int(h*0.95), int(w*0.05):int(w*0.96)]
    cv2.imwrite(os.path.join(base_dir, 'figures_Q02/boggs_fig8_9_meandering_morphology.png'), fig8_9)
    print("Extracted Boggs Fig 8.9 for Q02.")

# Sinuosity Spectrum Diagram
fig, ax = plt.subplots(figsize=(10, 5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Channel Pattern Classification by Sinuosity Index (S = L_channel / L_valley)', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Sinuosity bar
ax.fill_between([1.0, 1.05], [0, 0], [1, 1], color='#cbd5e1', alpha=0.8, label='Straight Channel (S < 1.05)')
ax.fill_between([1.05, 1.50], [0, 0], [1, 1], color='#fde68a', alpha=0.8, label='Sinuous Channel (1.05 ≤ S < 1.50)')
ax.fill_between([1.50, 2.50], [0, 0], [1, 1], color='#86efac', alpha=0.8, label='True Meandering River (S ≥ 1.50)')

# Critical Threshold Line
ax.axvline(1.50, color='#dc2626', lw=3, linestyle='--', label='Canonical Threshold: S = 1.5 (Leopold & Wolman, 1957)')
ax.text(1.51, 0.5, ' CRITICAL THRESHOLD: S = 1.5\n (Meandering Regime Boundary)', fontsize=10.5, fontweight='bold', color='#b91c1c')

# Labels and formulas
ax.text(1.01, 0.3, 'Straight\n(S < 1.05)', fontsize=9, fontweight='bold', color='#475569')
ax.text(1.22, 0.3, 'Sinuous Channel\n(1.05 ≤ S < 1.5)', fontsize=10, fontweight='bold', color='#92400e')
ax.text(1.90, 0.3, 'Fully Meandering River\n(Point bars, Chute cutoffs, Oxbow lakes)', fontsize=10.5, fontweight='bold', color='#166534')

ax.set_xlim(1.0, 2.5)
ax.set_ylim(0, 1.1)
ax.set_xlabel('Sinuosity Index (S)', fontsize=11, fontweight='bold', labelpad=8)
ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q02/sinuosity_threshold_spectrum.png'), dpi=250)
plt.close()
print("Generated Q02 sinuosity figures.")

# =========================================================================
# Q3: Aeolian System Controls (Kocurek-Lancaster Triad)
# =========================================================================
fig, ax = plt.subplots(figsize=(9, 6), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('The Kocurek-Lancaster (1999) Triad of Aeolian System Controls', fontsize=12, fontweight='bold', color='#0f172a', pad=14)

# Draw Triangle of Controls
tri_x = [1, 9, 5, 1]
tri_y = [1, 1, 8, 1]
ax.plot(tri_x, tri_y, color='#0284c7', lw=2.5)
ax.fill(tri_x, tri_y, color='#e0f2fe', alpha=0.4)

# Vertices
ax.scatter([1, 9, 5], [1, 1, 8], color=['#0284c7', '#d97706', '#16a34a'], s=200, zorder=5)

ax.text(0.2, 0.4, '(i) TRANSPORT CAPACITY (Tc)\nGoverned by wind shear velocity (u*³)\nand aerodynamic threshold', fontsize=9.5, fontweight='bold', color='#0369a1')
ax.text(6.8, 0.4, '(ii) SEDIMENT SUPPLY (Gs)\nTotal volume of source sand\nin upwind provenance basin', fontsize=9.5, fontweight='bold', color='#b45309')
ax.text(2.6, 8.3, '(iv) SEDIMENT AVAILABILITY (As)\nFraction susceptible to entrainment;\nlimited by moisture, crusts & vegetation', fontsize=9.5, fontweight='bold', color='#15803d')

# Center Box
center_txt = (
    "AEOLIAN EQUILIBRIUM STATE:\n"
    "• Tc > As, Gs -> Deflation Lag, Ventifacts\n"
    "• As, Gs > Tc -> Massive Sand Accumulation (Erg)\n"
    "• Temperature/Climate (Hot vs Cold) is NOT\n"
    "  a primary physical constraint!"
)
ax.text(2.6, 3.2, center_txt, fontsize=10, color='#1e293b', fontweight='500',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.5))

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.2, 9.5)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q03/aeolian_control_triad.png'), dpi=250)
plt.close()
print("Generated Q03 aeolian figure.")

# =========================================================================
# Q4: Morphotectonic Indices for Drainage Basins (Keller & Pinter)
# =========================================================================
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(13, 9), dpi=250)
fig.patch.set_facecolor('#ffffff')

# 1. AF
ax1.set_facecolor('#f8fafc')
ax1.set_title('1. Drainage Basin Asymmetry (AF = 100 · Ar / At)', fontsize=10.5, fontweight='bold', color='#0f172a')
bx = np.array([0, 1, 3, 5, 4, 2, 0])
by = np.array([2, 5, 6, 4, 1, 0, 2])
ax1.plot(bx, by, color='#475569', lw=2)
ax1.plot([0, 2, 4.5], [2, 1.5, 3.5], color='#2563eb', lw=3, label='Trunk Stream (Tilted Right)')
ax1.text(1.2, 3.8, 'Left Basin Area (Al)', fontsize=9, color='#64748b')
ax1.text(2.8, 1.8, 'Right Basin Area (Ar)', fontsize=9, color='#0284c7', fontweight='bold')
ax1.annotate('Tectonic Tilting Vector', xy=(2.5, 2.5), xytext=(1.0, 1.0),
             fontsize=9, fontweight='bold', color='#dc2626', arrowprops=dict(facecolor='#dc2626', width=2, headwidth=6))
ax1.set_xticks([]); ax1.set_yticks([]); ax1.legend(loc='upper right', fontsize=8)

# 2. SL Index
ax2.set_facecolor('#f8fafc')
ax2.set_title('2. Stream Length-Gradient Index (SL = (ΔH / ΔL) · L)', fontsize=10.5, fontweight='bold', color='#0f172a')
lx = np.linspace(0, 10, 100)
ly = 8 * np.exp(-0.25 * lx)
ax2.plot(lx, ly, color='#0284c7', lw=2.5, label='Equilibrium Profile')
# Knickpoint
ly[40:60] = ly[40:60] + 0.8 * np.sin(np.linspace(0, np.pi, 20))
ax2.plot(lx, ly, color='#dc2626', lw=2, linestyle='--', label='Tectonic Knickpoint / High SL')
ax2.annotate('Fault Scarp / Knickpoint (High SL)', xy=(4.8, 3.2), xytext=(5.5, 5.0),
             fontsize=9, fontweight='bold', color='#dc2626', arrowprops=dict(facecolor='#dc2626', width=1.5, headwidth=6))
ax2.set_xlabel('Channel Distance (L)', fontsize=9); ax2.set_ylabel('Elevation (H)', fontsize=9)
ax2.legend(loc='upper right', fontsize=8)

# 3. Smf
ax3.set_facecolor('#f8fafc')
ax3.set_title('3. Mountain-Front Sinuosity (Smf = Lmf / Ls)', fontsize=10.5, fontweight='bold', color='#0f172a')
ax3.plot([1, 9], [3, 3], color='#dc2626', lw=2.5, linestyle=':', label='Straight Fault Line (Ls)')
# Sinuous mountain front
mfx = np.linspace(1, 9, 100)
mfy = 3 + 0.9 * np.sin(mfx * 1.8)
ax3.plot(mfx, mfy, color='#15803d', lw=2.5, label='Mountain Front Base (Lmf)')
ax3.fill_between(mfx, mfy, 7, color='#dcfce7', alpha=0.5)
ax3.text(4, 5.5, 'Mountain Block (Uplifting)', fontsize=10, fontweight='bold', color='#166534')
ax3.text(4, 1.5, 'Foreland Basin (Alluvial Plain)', fontsize=10, color='#475569')
ax3.set_xticks([]); ax3.set_yticks([]); ax3.legend(loc='lower right', fontsize=8)

# 4. Vf
ax4.set_facecolor('#f8fafc')
ax4.set_title('4. Valley Floor Width to Height Ratio (Vf = 2Vfw / [(Eld-Esc)+(Erd-Esc)])', fontsize=9.5, fontweight='bold', color='#0f172a')
# V-shaped valley
ax4.plot([1, 5, 9], [6, 1, 6], color='#b45309', lw=2.5, label='Active Uplift: Deep V-Gorge (Vf << 1)')
ax4.plot([1, 3.5, 6.5, 9], [4, 1.5, 1.5, 4], color='#0284c7', lw=2, linestyle='--', label='Inactive: Flat Valley Floor (Vf >> 1)')
ax4.text(4.2, 0.4, 'Vfw', fontsize=9, fontweight='bold', color='#0369a1')
ax4.set_xticks([]); ax4.set_yticks([]); ax4.legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q04/morphotectonic_indices_suite.png'), dpi=250)
plt.close()
print("Generated Q04 morphotectonics figure.")

# =========================================================================
# Q5: Pedestal Rocks & Mushroom Rocks (Wind Abrasion)
# =========================================================================
fig, ax = plt.subplots(figsize=(9, 6), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Genesis of Pedestal / Mushroom Rock via Basal Wind Abrasion', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Ground
ax.fill_between([-1, 11], [-0.5, -0.5], [1.0, 1.0], color='#fed7aa', alpha=0.6, label='Desert Floor (Saltation Source)')
# Basal intense abrasion zone
ax.fill_between([-1, 11], [1.0, 1.0], [2.5, 2.5], color='#fecaca', alpha=0.4, label='Zone of Maximum Sandblasting (0.3 - 1.0 m above ground)')

# Mushroom Rock Profile
mx = [3, 4, 4.3, 4.4, 4.3, 3.5, 2.0, 2.2, 4.5, 5.5, 7.8, 8.0, 6.5, 5.7, 5.6, 5.7, 6.0, 7.0]
my = [1, 1, 1.8, 2.3, 3.0, 4.0, 4.5, 6.2, 6.5, 6.5, 6.2, 4.5, 4.0, 3.0, 2.3, 1.8, 1, 1]
ax.fill(mx, my, color='#d97706', alpha=0.85, edgecolor='#78350f', lw=2)

# Arrows of saltating sand
for sy in [1.2, 1.6, 2.0, 2.3]:
    ax.annotate('', xy=(3.8, sy), xytext=(1.0, sy),
                arrowprops=dict(facecolor='#dc2626', edgecolor='none', width=2, headwidth=6))
ax.text(0.5, 2.6, 'High-velocity sand grains\nsaltating in lower 1 meter', fontsize=9, fontweight='bold', color='#b91c1c')

# Annotations
ax.annotate('Wider Resistant Cap Rock\n(Slight abrasion; wind velocity\ncarries fine dust only)', xy=(5.0, 5.5), xytext=(7.0, 7.0),
            fontsize=9.5, fontweight='bold', color='#78350f', arrowprops=dict(facecolor='#78350f', width=1.5, headwidth=6))

ax.annotate('Undercut Slender Neck / Stem\n(Carved by intense quartz sand\nkinetic abrasion)', xy=(4.4, 2.2), xytext=(6.5, 3.2),
            fontsize=9.5, fontweight='bold', color='#b91c1c', arrowprops=dict(facecolor='#b91c1c', width=1.5, headwidth=6))

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(0, 8)
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc='lower left', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q05/mushroom_rock_abrasion_genesis.png'), dpi=250)
plt.close()
print("Generated Q05 mushroom rock figure.")

# =========================================================================
# Q6: OSL Luminescence Dating Mechanism
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('The Complete Optically Stimulated Luminescence (OSL) Dating Cycle', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Three stages: Transport/Bleaching, Burial/Trap Accumulation, Laboratory Measurement
stages = ['Stage 1: Transport & Sunlight Bleaching', 'Stage 2: Burial & Trap Accumulation', 'Stage 3: Optical Stimulation (Lab)']
cols = ['#0284c7', '#d97706', '#7c3aed']

for i, (st, col) in enumerate(zip(stages, cols)):
    ax.text(i*3.5 + 1.6, 5.2, st, fontsize=10, fontweight='bold', color=col, ha='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffffff', edgecolor=col, lw=1.5))

# Conduction band and valence band lines
for i in range(3):
    ox = i * 3.5
    ax.plot([ox+0.3, ox+3.0], [4.0, 4.0], color='#0f172a', lw=2) # Conduction Band
    ax.plot([ox+0.3, ox+3.0], [1.5, 1.5], color='#0f172a', lw=2) # Valence Band
    ax.plot([ox+0.8, ox+2.5], [2.8, 2.8], color='#dc2626', linestyle='--', lw=1.5) # Electron Traps
    ax.text(ox+1.65, 4.2, 'Conduction Band', fontsize=8, ha='center', color='#475569')
    ax.text(ox+1.65, 1.2, 'Valence Band', fontsize=8, ha='center', color='#475569')
    ax.text(ox+1.65, 3.0, 'Defect Traps (Metastable)', fontsize=7.5, ha='center', color='#b91c1c')

# Stage 1: Sunlight drains traps
ax.annotate('Sunlight Photons\n(Optical Bleaching)', xy=(1.65, 2.8), xytext=(1.65, 3.6),
            fontsize=8.5, fontweight='bold', color='#0284c7', arrowprops=dict(facecolor='#0284c7', width=1.5, headwidth=5))
ax.text(1.65, 2.3, 'Traps Evacuated\n(Signal ZEROED)', fontsize=8.5, fontweight='bold', color='#15803d', ha='center')

# Stage 2: Natural radioactivity fills traps
ax.annotate('Natural Radiation\n(U, Th, ⁴⁰K, Cosmic)\nDose Rate (Dr)', xy=(5.15, 2.8), xytext=(5.15, 1.8),
            fontsize=8.5, fontweight='bold', color='#d97706', arrowprops=dict(facecolor='#d97706', width=1.5, headwidth=5))
ax.text(5.15, 3.4, 'Electrons Trapped\nover Geologic Time', fontsize=8.5, fontweight='bold', color='#b45309', ha='center')

# Stage 3: Lab stimulation & photon emission
ax.annotate('Blue/Green LED (hν)', xy=(8.65, 2.8), xytext=(7.8, 3.4),
            fontsize=8.5, fontweight='bold', color='#7c3aed', arrowprops=dict(facecolor='#7c3aed', width=1.5, headwidth=5))
ax.annotate('UV Luminescence Photon\nSignal (Equivalent Dose De)', xy=(8.65, 4.0), xytext=(9.2, 4.6),
            fontsize=8.5, fontweight='bold', color='#059669', arrowprops=dict(facecolor='#059669', width=1.5, headwidth=5))

ax.set_xlim(0, 11)
ax.set_ylim(0.5, 6.0)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q06/osl_dating_mechanism.png'), dpi=250)
plt.close()
print("Generated Q06 OSL figure.")

# =========================================================================
# Q8: Trellis Drainage Pattern
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Trellis Drainage Pattern on Dipping & Folded Alternating Strata', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Draw alternating hard and soft bands
for yb in [0, 2, 4, 6]:
    ax.fill_between([0, 10], [yb, yb], [yb+1, yb+1], color='#cbd5e1', alpha=0.5, label='Hard Resistant Rock (Sandstone/Quartzite Ridge)' if yb==0 else "")
    ax.fill_between([0, 10], [yb+1, yb+1], [yb+2, yb+2], color='#fed7aa', alpha=0.4, label='Soft Erodible Rock (Shale/Limestone Vale)' if yb==0 else "")

# Strike streams (Subsequent) flowing along soft vales
ax.plot([0, 10], [1.5, 1.5], color='#2563eb', lw=3.5, label='Primary Subsequent Stream (Flowing along Strike Vale)')
ax.plot([0, 10], [3.5, 3.5], color='#2563eb', lw=3.5)
ax.plot([0, 10], [5.5, 5.5], color='#2563eb', lw=3.5)

# Orthogonal dip/scarp tributaries joining at ~90 degrees
trib_x = [2.0, 4.0, 6.5, 8.5]
for tx in trib_x:
    ax.plot([tx, tx], [0.5, 1.5], color='#0284c7', lw=2)
    ax.plot([tx+0.8, tx+0.8], [2.5, 1.5], color='#0284c7', lw=2)
    ax.plot([tx, tx], [2.5, 3.5], color='#0284c7', lw=2)
    ax.plot([tx+0.8, tx+0.8], [4.5, 3.5], color='#0284c7', lw=2)

ax.text(8.2, 1.8, 'Strike Valley', fontsize=9.5, fontweight='bold', color='#1e40af')
ax.annotate('Orthogonal Tributary\n(Dip / Scarp Stream\njoining at 90°)', xy=(4.0, 1.0), xytext=(5.0, 0.4),
            fontsize=9.5, fontweight='bold', color='#0369a1', arrowprops=dict(facecolor='#0369a1', width=1.5, headwidth=6))

ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis('off')
ax.legend(loc='upper right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q08/trellis_drainage_pattern.png'), dpi=250)
plt.close()
print("Generated Q08 trellis drainage figure.")

# =========================================================================
# Q10: Hogback vs Cuesta vs Mesa
# =========================================================================
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5), dpi=250)
fig.patch.set_facecolor('#ffffff')

# Mesa
ax1.set_facecolor('#f8fafc')
ax1.set_title('(A) Mesa: Horizontal Strata (Dip ≈ 0°)', fontsize=11, fontweight='bold', color='#0f172a')
ax1.fill_between([2, 8], [4, 4], [4.8, 4.8], color='#334155', alpha=0.9, label='Resistant Caprock')
ax1.fill_between([1, 2, 8, 9], [0, 4, 4, 0], color='#cbd5e1', alpha=0.7, label='Softer Underlying Strata')
ax1.text(5, 5.2, 'Flat Tableland', fontsize=9.5, fontweight='bold', ha='center', color='#0f172a')
ax1.set_xlim(0, 10); ax1.set_ylim(0, 6); ax1.axis('off'); ax1.legend(loc='lower center', fontsize=8)

# Cuesta
ax2.set_facecolor('#f8fafc')
ax2.set_title('(B) Cuesta: Gentle Dip (< 20°)\nAsymmetrical Slopes', fontsize=11, fontweight='bold', color='#0f172a')
# Gentle dip slope on left, steep scarp on right
cx = [1, 7, 7.8, 9]
cy = [1, 4.5, 1.2, 0.5]
ax2.plot(cx, cy, color='#0284c7', lw=2.5)
ax2.fill_between(cx, 0, cy, color='#bae6fd', alpha=0.6)
ax2.text(3.5, 3.2, 'Gentle Dip Slope (θ < 15°)\nConcordant with strata', fontsize=9, fontweight='bold', color='#0369a1')
ax2.text(7.2, 2.5, 'Steep Scarp\nSlope', fontsize=9, fontweight='bold', color='#b91c1c')
ax2.set_xlim(0, 10); ax2.set_ylim(0, 6); ax2.axis('off')

# Hogback
ax3.set_facecolor('#f8fafc')
ax3.set_title('(C) Hogback: Steep Dip (> 40°–60°)\nNear-Equal Flank Slopes', fontsize=11, fontweight='bold', color='#0f172a')
hx = [2, 5, 8]
hy = [0.8, 5.2, 0.8]
ax3.plot(hx, hy, color='#dc2626', lw=3)
ax3.fill_between(hx, 0, hy, color='#fecaca', alpha=0.6)
ax3.text(5, 5.5, 'Sharp, Narrow Crest', fontsize=9.5, fontweight='bold', ha='center', color='#991b1b')
ax3.text(2.6, 2.8, 'Dip Slope (θ ≈ 50°)\nVery Steep', fontsize=9, fontweight='bold', color='#b91c1c')
ax3.text(6.2, 2.8, 'Scarp Slope\nEqual Inclination!', fontsize=9, fontweight='bold', color='#b91c1c')
ax3.set_xlim(0, 10); ax3.set_ylim(0, 6); ax3.axis('off')

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q10/hogback_vs_cuesta_morphology.png'), dpi=250)
plt.close()
print("Generated Q10 hogback figure.")

# =========================================================================
# Q11: Atmospheric Scattering (Rayleigh λ^-4 vs Mie)
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Atmospheric Scattering Intensity vs. Wavelength (Rayleigh λ⁻⁴ Law)', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

wl = np.linspace(0.4, 0.75, 200) # visible spectrum
# Rayleigh scattering I ~ 1 / lambda^4
rayleigh = (0.45 / wl)**4

ax.plot(wl, rayleigh, color='#2563eb', lw=3.5, label='Rayleigh Scattering Intensity (I ∝ 1/λ⁴)')
# Visible color spectrum band
ax.axvspan(0.40, 0.49, color='#38bdf8', alpha=0.25, label='Blue Region (~0.45 μm: Maximum Scattering)')
ax.axvspan(0.49, 0.57, color='#4ade80', alpha=0.20, label='Green Region (~0.55 μm)')
ax.axvspan(0.57, 0.75, color='#f87171', alpha=0.20, label='Red Region (~0.70 μm: Minimal Scattering)')

ax.annotate('Blue Light Scattered ~9.4x More Than Red Light!\nBathing the Sky in Diffuse Blue Skylight',
            xy=(0.45, 1.0), xytext=(0.52, 1.2),
            fontsize=10, fontweight='bold', color='#1e40af',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffffff', edgecolor='#2563eb', lw=1.5),
            arrowprops=dict(facecolor='#1e40af', width=1.5, headwidth=6))

ax.set_xlabel('Wavelength (μm)', fontsize=11, fontweight='bold', labelpad=8)
ax.set_ylabel('Relative Scattering Intensity', fontsize=11, fontweight='bold', labelpad=8)
ax.set_xlim(0.40, 0.75)
ax.set_ylim(0, 1.8)
ax.legend(loc='upper right', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q11/rayleigh_scattering_curve.png'), dpi=250)
plt.close()
print("Generated Q11 Rayleigh scattering figure.")

# =========================================================================
# Q18: Vegetation Spectral Reflectance Curve (Chlorophyll Green Peak)
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Typical Spectral Reflectance Curve of Green Vegetation', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

wl = np.linspace(0.4, 2.5, 400)
# Model typical vegetation reflectance curve
refl = np.zeros_like(wl)
for i, w in enumerate(wl):
    if w < 0.50:
        refl[i] = 0.05 + 0.02 * np.sin(w*10) # Blue absorption
    elif w < 0.60:
        refl[i] = 0.12 - 0.07 * ((w - 0.55)/0.05)**2 # Green peak
    elif w < 0.68:
        refl[i] = 0.05 # Red absorption
    elif w < 0.75:
        refl[i] = 0.05 + 0.45 * ((w - 0.68)/0.07) # Red Edge
    elif w < 1.30:
        refl[i] = 0.50 + 0.03 * np.sin(w*8) # NIR plateau
    else:
        # SWIR with water absorption pits at 1.45 and 1.94
        base = 0.35 - 0.1 * (w - 1.3)
        water1 = 0.20 * np.exp(-((w - 1.45)/0.08)**2)
        water2 = 0.22 * np.exp(-((w - 1.94)/0.08)**2)
        refl[i] = max(0.02, base - water1 - water2)

ax.plot(wl, refl * 100, color='#15803d', lw=3.5, label='Healthy Green Vegetation Reflectance')

# Optical Domains
ax.axvspan(0.4, 0.7, color='#fef08a', alpha=0.3, label='Visible (0.4–0.7 μm): Governed by Leaf Pigments (Chlorophyll)')
ax.axvspan(0.7, 1.3, color='#bbf7d0', alpha=0.3, label='NIR (0.7–1.3 μm): Governed by Mesophyll Cell Structure')
ax.axvspan(1.3, 2.5, color='#bae6fd', alpha=0.3, label='SWIR (1.3–2.5 μm): Governed by Leaf Water Content')

# Annotations
ax.annotate('GREEN PEAK (~0.55 μm)\nChlorophyll reflects green photons', xy=(0.55, 12), xytext=(0.42, 28),
            fontsize=9.5, fontweight='bold', color='#15803d', arrowprops=dict(facecolor='#15803d', width=1.5, headwidth=6))
ax.annotate('RED EDGE\nSteep optical jump', xy=(0.72, 30), xytext=(0.82, 22),
            fontsize=9.5, fontweight='bold', color='#b45309', arrowprops=dict(facecolor='#b45309', width=1.5, headwidth=6))
ax.annotate('NIR Scattering Plateau (~50%)\nInternal spongy mesophyll', xy=(1.0, 50), xytext=(1.05, 58),
            fontsize=9.5, fontweight='bold', color='#047857', arrowprops=dict(facecolor='#047857', width=1.5, headwidth=6))
ax.annotate('Water Absorption\nPits (1.45 & 1.94 μm)', xy=(1.45, 12), xytext=(1.55, 25),
            fontsize=9.5, fontweight='bold', color='#0284c7', arrowprops=dict(facecolor='#0284c7', width=1.5, headwidth=6))

ax.set_xlabel('Wavelength (μm)', fontsize=11, fontweight='bold', labelpad=8)
ax.set_ylabel('Reflectance (%)', fontsize=11, fontweight='bold', labelpad=8)
ax.set_xlim(0.4, 2.5)
ax.set_ylim(0, 68)
ax.legend(loc='upper right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q18/vegetation_reflectance_curve.png'), dpi=250)
plt.close()
print("Generated Q18 vegetation reflectance figure.")

# =========================================================================
# Q21: Thrust Fault (< 45°) Mechanics (Anderson Model)
# =========================================================================
fig, ax = plt.subplots(figsize=(9, 6), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Andersonian Mechanics of Thrust Faulting (Dip θ < 45°)', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Fault line inclined at 30 degrees
fx = np.linspace(2, 8, 100)
fy = (fx - 2) * np.tan(np.radians(30)) + 1.5
ax.plot(fx, fy, color='#dc2626', lw=3.5, label='Thrust Fault Plane (Dip θ = 30° < 45°)')

# Footwall and Hanging Wall
ax.fill_between(fx, 0, fy, color='#cbd5e1', alpha=0.6, label='Footwall Block (Stationary)')
ax.fill_between([2, 2, 8, 8], [fy[0], 6.5, 6.5, fy[-1]], color='#bae6fd', alpha=0.6, label='Hanging Wall Block (Displaced Upwards)')

# Stress vectors
ax.annotate('Maximum Principal Stress (σ1)\nHORIZONTAL Contraction', xy=(1.0, 3.5), xytext=(-0.5, 3.5),
            fontsize=10, fontweight='bold', color='#dc2626', arrowprops=dict(facecolor='#dc2626', width=2.5, headwidth=8))
ax.annotate('', xy=(9.0, 3.5), xytext=(10.5, 3.5),
            arrowprops=dict(facecolor='#dc2626', width=2.5, headwidth=8))

# Hanging wall motion arrow
ax.annotate('Hanging Wall Upthrow\n(Contractional Slip)', xy=(5.0, 4.0), xytext=(3.5, 5.5),
            fontsize=10, fontweight='bold', color='#0284c7', arrowprops=dict(facecolor='#0284c7', width=2, headwidth=7))

# Angle arc
ax.plot([3.5, 4.5], [fy[25], fy[25]], color='#475569', linestyle=':')
ax.text(4.2, fy[25]+0.3, 'θ < 45°', fontsize=11, fontweight='bold', color='#b91c1c')

ax.set_xlim(-1, 11)
ax.set_ylim(0, 7)
ax.axis('off')
ax.legend(loc='lower right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q21/thrust_fault_geometry.png'), dpi=250)
plt.close()
print("Generated Q21 thrust fault figure.")

# =========================================================================
# Q25: Ramsay Class 1B Parallel (Concentric) Fold Curvature with Depth
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Ramsay Class 1B (Parallel/Concentric) Fold: Curvature Evolution with Depth', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Concentric arcs for anticline and syncline
# Anticline centered at (3, 1), Syncline centered at (7, 6)
theta_anti = np.linspace(np.pi*0.1, np.pi*0.9, 100)
for r in [4.0, 3.0, 2.0, 1.0, 0.2]:
    arc_x = 3.0 + r * np.cos(theta_anti)
    arc_y = 1.0 + r * np.sin(theta_anti)
    col = '#dc2626' if r == 0.2 else '#0284c7'
    lw = 2.5 if r == 0.2 else 1.8
    ax.plot(arc_x, arc_y, color=col, lw=lw)

# Syncline arcs
theta_sync = np.linspace(np.pi*1.1, np.pi*1.9, 100)
for r in [1.5, 2.5, 3.5, 4.5, 5.5]:
    arc_x = 7.0 + r * np.cos(theta_sync)
    arc_y = 6.0 + r * np.sin(theta_sync)
    ax.plot(arc_x, arc_y, color='#15803d', lw=1.8)

ax.text(3.0, 0.4, 'ANTICLINE CORE:\nRadius R -> 0, Curvature κ -> ∞\nSharp, pinched, cuspidate\n(Room Problem & Detachment)',
        fontsize=9.5, fontweight='bold', color='#b91c1c', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fee2e2', edgecolor='#dc2626', lw=1.2))

ax.text(7.0, 0.4, 'SYNCLINE DEPTH:\nRadius R -> ∞, Curvature κ -> 0\nBroad, open, flat trough\n(Smoothly opens downward)',
        fontsize=9.5, fontweight='bold', color='#166534', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#dcfce7', edgecolor='#15803d', lw=1.2))

ax.text(1.0, 5.0, 'Layer Thickness (t)\nis CONSTANT\neverywhere (Class 1B)', fontsize=10, fontweight='bold', color='#0369a1')

ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q25/ramsay_parallel_fold_depth_curvature.png'), dpi=250)
plt.close()
print("Generated Q25 parallel fold figure.")

print("All figures successfully created and saved into figures_Q01 to figures_Q25!")
