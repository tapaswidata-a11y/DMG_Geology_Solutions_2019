#!/usr/bin/env python3
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

base_dir = '/home/tapaswi/Mines_Geology/Orrisa_geology'
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# =========================================================================
# Q7: Fluvial Megafans vs Alluvial Fans Architecture
# =========================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')

# Alluvial Fan
ax1.set_facecolor('#f8fafc')
ax1.set_title('(A) Alluvial Fan: Steep, Small Footprint (< 100 km²)', fontsize=11, fontweight='bold', color='#0f172a')
theta = np.linspace(-np.pi/4, np.pi/4, 50)
r = np.linspace(0.5, 5, 20)
T, R = np.meshgrid(theta, r)
X = R * np.cos(T)
Y = R * np.sin(T)
ax1.fill_between([0, 4.5, 4.5, 0], [0, 3.5, -3.5, 0], color='#fed7aa', alpha=0.6)
ax1.plot([0, 4.5], [0, 3.5], color='#b45309', lw=2)
ax1.plot([0, 4.5], [0, -3.5], color='#b45309', lw=2)
ax1.scatter([0], [0], color='#dc2626', s=100, label='Apex (Mountain Gorge)')
ax1.text(2.2, 0, 'Steep Slopes (1.5°–10°)\nDebris Flows & Sieve Beds\nArea < 100 km²', fontsize=9.5, fontweight='bold', color='#78350f', ha='center')
ax1.set_xlim(-0.5, 5); ax1.set_ylim(-4, 4); ax1.axis('off'); ax1.legend(loc='upper left', fontsize=8.5)

# Fluvial Megafan
ax2.set_facecolor('#f8fafc')
ax2.set_title('(B) Fluvial Megafan: Immense Foreland Basin Scale (> 10⁴ km²)', fontsize=11, fontweight='bold', color='#0f172a')
ax2.fill_between([0, 7.5, 7.5, 0], [0, 4.0, -4.0, 0], color='#bae6fd', alpha=0.6)
# Multi-channel avulsion belts
for y_end in [-3.0, -1.5, 0, 1.5, 3.0]:
    ax2.plot([0, 2.5, 7.5], [0, y_end*0.4, y_end], color='#0284c7', lw=1.8, linestyle='--')
ax2.plot([0, 2.5, 7.5], [0, -0.6, -1.5], color='#1d4ed8', lw=3, label='Active Fluvial Channel Belt (Kosi River Type)')
ax2.scatter([0], [0], color='#dc2626', s=120, label='Nodal Apex (Himalayan / Mountain Exit)')
ax2.text(4.2, 1.8, 'Extremely Low Gradient (< 0.1°)\nRadial Length > 100 km, Area > 10⁴ km²\nUnconfined Avulsion Dominated', fontsize=9.5, fontweight='bold', color='#0369a1', ha='center')
ax2.set_xlim(-0.5, 8); ax2.set_ylim(-4.5, 4.5); ax2.axis('off'); ax2.legend(loc='upper left', fontsize=8.5)

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q07/foreland_megafan_vs_alluvial_fan.png'), dpi=250)
plt.close()
print("Generated Q07 megafan figure.")

# =========================================================================
# Q9: Fanglomerate Facies & Texture
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Fanglomerate: Lithified Alluvial Fan Debris Flow & Gravel Facies (A.C. Lawson 1913)', fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)

# Matrix background
ax.fill_between([0, 10], [0, 0], [6, 6], color='#fed7aa', alpha=0.7, label='Argillaceous-Sandy Matrix (> 15% Matrix = Paraconglomerate)')

# Draw poorly sorted, angular to sub-angular clasts
np.random.seed(42)
clast_sizes = [0.8, 1.2, 0.6, 1.5, 0.5, 0.9, 1.1, 0.7, 1.4, 0.4, 0.6, 1.0]
cx = [1.5, 3.2, 5.0, 7.5, 8.8, 2.0, 4.2, 6.2, 8.2, 3.8, 6.8, 5.2]
cy = [4.5, 4.8, 4.2, 4.5, 3.2, 2.0, 2.2, 2.8, 1.5, 1.0, 1.2, 3.0]

for x, y, r in zip(cx, cy, clast_sizes):
    # polygonal angular clast
    num_pts = np.random.randint(5, 8)
    angles = np.linspace(0, 2*np.pi, num_pts, endpoint=False)
    pts_x = x + r * (0.8 + 0.4*np.random.rand(num_pts)) * np.cos(angles)
    pts_y = y + r * (0.8 + 0.4*np.random.rand(num_pts)) * np.sin(angles)
    ax.fill(pts_x, pts_y, color='#64748b', edgecolor='#1e293b', lw=1.5)

ax.text(5.0, 5.5, 'FANGLOMERATE TEXTURAL CHARACTERISTICS:\n• Extreme textural immaturity & poor sorting\n• Polymodal grain size (Boulders in muddy-sand matrix)\n• Clasts derived from adjacent fault scarps',
        fontsize=9.5, fontweight='bold', color='#0f172a', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.2))

ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off'); ax.legend(loc='lower right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q09/alluvial_fan_fanglomerate_facies.png'), dpi=250)
plt.close()
print("Generated Q09 fanglomerate figure.")

# =========================================================================
# Q12: SWIR & TIR Molecular Vibrational Spectroscopy
# =========================================================================
fig, ax = plt.subplots(figsize=(11, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Electromagnetic Spectrum: Electronic vs. Molecular Vibrational Transitions', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Spectrum blocks
domains = [
    ('UV & Visible (0.2–0.7 μm)', 0.2, 0.7, '#fef08a', 'Electronic Transitions\n(Valence electron orbital jumps,\nFe³⁺/Fe²⁺ charge transfer)'),
    ('NIR (0.7–1.3 μm)', 0.7, 1.3, '#bbf7d0', 'Electronic & Early Overtones\n(Crystal field d-d transitions,\nchlorophyll scattering)'),
    ('SWIR (1.4–2.5 μm)', 1.4, 2.5, '#bae6fd', 'MOLECULAR VIBRATIONAL OVERTONES\n(Al-OH 2.20 μm, Mg-OH 2.31 μm,\nCO₃²⁻ 2.35 μm, H₂O 1.94 μm)'),
    ('TIR (8.0–14.0 μm)', 8.0, 14.0, '#fed7aa', 'FUNDAMENTAL VIBRATIONAL MODES\n(Si-O-Si stretching 8.5–12 μm Reststrahlen bands,\nthermal kinetic emission)')
]

ax.plot([0, 15], [3, 3], color='#0f172a', lw=2)

x_pos = [1.5, 4.5, 8.0, 12.5]
for (name, start, end, col, desc), xp in zip(domains, x_pos):
    ax.fill_between([xp-1.3, xp+1.3], [1.5, 1.5], [4.5, 4.5], color=col, alpha=0.8, edgecolor='#334155', lw=1.5)
    ax.text(xp, 4.1, name, fontsize=9.5, fontweight='bold', ha='center', color='#0f172a')
    ax.text(xp, 2.3, desc, fontsize=8, ha='center', color='#1e293b')

ax.annotate('QUESTION FOCUS: Vibrational Energy Domains (SWIR + TIR)', xy=(10.2, 4.6), xytext=(6.5, 5.4),
            fontsize=10.5, fontweight='bold', color='#b91c1c',
            arrowprops=dict(facecolor='#b91c1c', width=2, headwidth=7))

ax.set_xlim(0, 15); ax.set_ylim(0.5, 6.0); ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q12/swir_tir_vibrational_spectroscopy.png'), dpi=250)
plt.close()
print("Generated Q12 spectroscopy figure.")

# =========================================================================
# Q13: Sun-Synchronous Orbit Geometry
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Sun-Synchronous Near-Polar Retrograde Orbit (i ≈ 98.6°)', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Earth circle
earth = plt.Circle((5, 3), 1.8, color='#38bdf8', alpha=0.8, ec='#0284c7', lw=2)
ax.add_patch(earth)
ax.plot([5, 5], [1.0, 5.0], color='#0f172a', lw=2, linestyle='--', label='Earth Rotational Axis (N-S)')
ax.plot([3.0, 7.0], [3, 3], color='#0f172a', lw=1.5, label='Equatorial Plane')

# Inclined orbit ellipse
orbit_theta = np.radians(8) # retrograde tilt from polar (98 deg)
ox = 5 + 2.6 * np.cos(np.linspace(0, 2*np.pi, 100)) * np.cos(orbit_theta) - 1.2 * np.sin(np.linspace(0, 2*np.pi, 100)) * np.sin(orbit_theta)
oy = 3 + 2.6 * np.cos(np.linspace(0, 2*np.pi, 100)) * np.sin(orbit_theta) + 1.2 * np.sin(np.linspace(0, 2*np.pi, 100)) * np.cos(orbit_theta)
ax.plot(ox, oy, color='#dc2626', lw=2.5, label='Orbital Track (Retrograde Inclination i ≈ 98°)')

# Sunlight illumination angle
for y_ray in [2.0, 3.0, 4.0]:
    ax.annotate('', xy=(1.0, y_ray), xytext=(-0.5, y_ray),
                arrowprops=dict(facecolor='#f59e0b', edgecolor='none', width=2, headwidth=6))
ax.text(-0.5, 4.3, 'Parallel Solar Rays\n(Constant Sun Angle)', fontsize=9, fontweight='bold', color='#b45309')

ax.text(5.0, 5.4, 'J2 Equatorial Bulge Gravitational Torque\ncauses Nodal Precession = 0.9856°/day\nSynchronized with LOCAL SOLAR TIME (e.g. 10:30 AM overpass)',
        fontsize=9.5, fontweight='bold', color='#1e40af', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#eff6ff', edgecolor='#2563eb', lw=1.2))

ax.set_xlim(-1, 10); ax.set_ylim(0.5, 6.2); ax.axis('off'); ax.legend(loc='lower right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q13/sun_synchronous_orbit_geometry.png'), dpi=250)
plt.close()
print("Generated Q13 SSO figure.")

# =========================================================================
# Q14: Spatial Resolution & IFOV / GSD
# =========================================================================
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Spatial Resolution: Instantaneous Field of View (IFOV) & Ground Sampling Distance (GSD)', fontsize=11, fontweight='bold', color='#0f172a', pad=12)

# Satellite detector
ax.scatter([5], [5.2], color='#0f172a', s=150, label='Sensor Detector at Flying Altitude H')
ax.plot([5, 3], [5.2, 1.2], color='#0284c7', lw=1.8, linestyle='--')
ax.plot([5, 7], [5.2, 1.2], color='#0284c7', lw=1.8, linestyle='--')

# Ground surface
ax.plot([1, 9], [1.2, 1.2], color='#334155', lw=3)
ax.fill_between([3, 7], [1.2, 1.2], [1.0, 1.0], color='#86efac', alpha=0.8, label='Ground Resolution Cell (GSD = H · IFOV)')

ax.text(5.0, 4.2, 'IFOV (Angular Instantaneous\nField of View, mrad)', fontsize=9, fontweight='bold', color='#0369a1', ha='center')
ax.text(5.0, 0.5, 'Ground Sampling Distance (GSD)\nGoverns object edge clarity and spatial discernibility', fontsize=9.5, fontweight='bold', color='#166534', ha='center')

ax.set_xlim(1, 9); ax.set_ylim(0, 6); ax.axis('off'); ax.legend(loc='upper right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q14/spatial_resolution_ifov_gsd.png'), dpi=250)
plt.close()
print("Generated Q14 spatial resolution figure.")

# =========================================================================
# Q15: Aerial Photograph Fiducial Marks & Principal Point
# =========================================================================
fig, ax = plt.subplots(figsize=(7, 7), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Fiducial Marks Defining the Principal Point (PP) of an Aerial Photograph', fontsize=11, fontweight='bold', color='#0f172a', pad=12)

# Photo frame
ax.plot([1, 9, 9, 1, 1], [1, 1, 9, 9, 1], color='#0f172a', lw=3)

# Fiducial marks on corners/sides
fids = [(1, 5), (9, 5), (5, 1), (5, 9)]
for fx, fy in fids:
    ax.scatter([fx], [fy], color='#dc2626', s=120, zorder=5)

# Connecting lines
ax.plot([1, 9], [5, 5], color='#dc2626', linestyle=':', lw=2, label='Fiducial Axis X')
ax.plot([5, 5], [1, 9], color='#dc2626', linestyle=':', lw=2, label='Fiducial Axis Y')

# Principal Point at (5, 5)
ax.scatter([5], [5], color='#2563eb', s=180, zorder=6, label='PRINCIPAL POINT (PP) [Geometric Center]')
ax.annotate('Principal Point (PP)\n(Intersection of opposite fiducials)', xy=(5, 5), xytext=(5.6, 6.2),
            fontsize=9.5, fontweight='bold', color='#1e40af',
            arrowprops=dict(facecolor='#1e40af', width=1.5, headwidth=6))

ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off'); ax.legend(loc='lower center', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q15/aerial_photo_fiducial_marks_principal_point.png'), dpi=250)
plt.close()
print("Generated Q15 fiducial marks figure.")

# =========================================================================
# Q16: Radar: Real Aperture vs Synthetic Aperture
# =========================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')

# RAR
ax1.set_facecolor('#f8fafc')
ax1.set_title('(A) Real Aperture Radar (RAR):\nAzimuth Resolution Ra = λ·R / L', fontsize=11, fontweight='bold', color='#0f172a')
ax1.plot([1, 2], [5, 5], color='#0f172a', lw=6, label='Short Physical Antenna (L)')
ax1.plot([1.5, 0.5], [5, 1], color='#b45309', linestyle='--')
ax1.plot([1.5, 4.5], [5, 1], color='#b45309', linestyle='--')
ax1.plot([0.5, 4.5], [1, 1], color='#dc2626', lw=4, label='Wide Beam / Poor Resolution')
ax1.text(2.5, 0.4, 'Azimuth Resolution degrades with Slant Range (R)\nSpaceborne 10m resolution requires 4.5 km antenna!', fontsize=8.5, color='#991b1b', ha='center')
ax1.set_xlim(0, 5); ax1.set_ylim(0, 6); ax1.axis('off'); ax1.legend(loc='upper right', fontsize=8)

# SAR
ax2.set_facecolor('#f8fafc')
ax2.set_title('(B) Synthetic Aperture Radar (SAR):\nVirtual Synthesized Antenna L_synth >> L', fontsize=11, fontweight='bold', color='#0f172a')
ax2.plot([1, 4.5], [5, 5], color='#2563eb', lw=2.5, linestyle=':', label='Synthesized Antenna Flight Path')
for x in [1.5, 2.5, 3.5]:
    ax2.scatter([x], [5], color='#0f172a', s=80)
    ax2.plot([x, 2.5], [5, 1.2], color='#0284c7', alpha=0.5)

ax2.plot([2.3, 2.7], [1.2, 1.2], color='#16a34a', lw=5, label='Fine Resolution Ra = L / 2')
ax2.text(2.5, 0.4, 'Azimuth Resolution Ra = L / 2\nIndependent of altitude and range!', fontsize=9, fontweight='bold', color='#166534', ha='center')
ax2.set_xlim(0, 5); ax2.set_ylim(0, 6); ax2.axis('off'); ax2.legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q16/radar_real_vs_synthetic_aperture.png'), dpi=250)
plt.close()
print("Generated Q16 radar figure.")

# =========================================================================
# Q17: Soil Moisture Spectral Reflectance
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Effect of Soil Moisture on Spectral Reflectance: NIR Darkening', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

wl = np.linspace(0.4, 2.5, 300)
dry_soil = 0.15 + 0.25 * (wl - 0.4) / 2.1
moist_soil = (0.08 + 0.15 * (wl - 0.4) / 2.1) * (1 - 0.4*np.exp(-((wl-1.45)/0.12)**2) - 0.5*np.exp(-((wl-1.94)/0.12)**2))
water_body = 0.05 * np.exp(-3*(wl - 0.4))

ax.plot(wl, dry_soil * 100, color='#d97706', lw=3, label='Dry Soil (Bright / White tone on NIR image)')
ax.plot(wl, moist_soil * 100, color='#0284c7', lw=3, label='Moist / Saturated Soil (Dark Grey tone on NIR image)')
ax.plot(wl, water_body * 100, color='#1e3a8a', lw=2.5, linestyle='--', label='Clear Water (Black tone on NIR image)')

# NIR domain highlight
ax.axvspan(0.75, 1.1, color='#bae6fd', alpha=0.3, label='NIR Band (Water Absorption reduces reflectance to grey tone)')

ax.set_xlabel('Wavelength (μm)', fontsize=11, fontweight='bold', labelpad=8)
ax.set_ylabel('Reflectance (%)', fontsize=11, fontweight='bold', labelpad=8)
ax.set_xlim(0.4, 2.5); ax.set_ylim(0, 48); ax.legend(loc='upper left', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q17/soil_moisture_nir_reflectance_tone.png'), dpi=250)
plt.close()
print("Generated Q17 soil moisture figure.")

# =========================================================================
# Q19: IRS-1D Satellite Sensor Suite
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('ISRO IRS-1C / IRS-1D Optical Sensor Payloads & Spatial Resolutions', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

sensors = ['PAN (Panchromatic)', 'LISS-III (VNIR Multispectral)', 'LISS-III (SWIR Band 5)', 'WiFS (Wide Field Sensor)']
res = [5.8, 23.5, 70.5, 188.0]
cols = ['#0f172a', '#0284c7', '#d97706', '#16a34a']

bars = ax.barh(sensors, res, color=cols, height=0.5)
for b, r in zip(bars, res):
    ax.text(r + 3, b.get_y() + 0.15, f'{r} meters', fontsize=10.5, fontweight='bold', color='#0f172a')

ax.set_xlabel('Spatial Resolution (meters) - Lower number = Sharper Detail', fontsize=10.5, fontweight='bold', labelpad=8)
ax.set_xlim(0, 220)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q19/irs_1d_sensor_payloads_resolution.png'), dpi=250)
plt.close()
print("Generated Q19 IRS-1D sensor figure.")

# =========================================================================
# Q20: SRTM InSAR 60-m Mast Geometry
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Shuttle Radar Topography Mission (SRTM): Single-Pass InSAR Mast Geometry', fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)

# Space Shuttle & Mast
ax.scatter([2], [4.5], color='#0f172a', s=200, label='Shuttle Cargo Bay (Main Antenna A1)')
ax.plot([2, 5.5], [4.5, 4.5], color='#dc2626', lw=4, label='60-meter Deployable Mast (Interferometric Baseline B)')
ax.scatter([5.5], [4.5], color='#dc2626', s=120, label='Outboard Antenna A2')

# Radar beams to ground target
ax.plot([2, 5], [4.5, 1.2], color='#0284c7', lw=1.8, linestyle='--')
ax.plot([5.5, 5], [4.5, 1.2], color='#b45309', lw=1.8, linestyle='--')
ax.scatter([5], [1.2], color='#15803d', s=150, label='Ground Target (Topographic Height z)')

# Topographic profile
tx = np.linspace(0, 10, 100)
ty = 1.0 + 0.4 * np.sin(tx * 1.5)
ax.plot(tx, ty, color='#15803d', lw=2.5)

ax.annotate('Interferometric Phase Shift (Δφ)\nyields DEM Elevation with 16m accuracy', xy=(5, 1.2), xytext=(6.5, 2.5),
            fontsize=9.5, fontweight='bold', color='#166534', arrowprops=dict(facecolor='#166534', width=1.5, headwidth=6))

ax.set_xlim(0, 10); ax.set_ylim(0.5, 5.5); ax.axis('off'); ax.legend(loc='upper right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q20/srtm_shuttle_radar_3d_insar_geometry.png'), dpi=250)
plt.close()
print("Generated Q20 SRTM figure.")

# =========================================================================
# Q22: Structural Plunge and Trend in 3D Block Diagram
# =========================================================================
fig, ax = plt.subplots(figsize=(9, 6), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Attitude of a Linear Geological Feature: Plunge vs. Trend vs. Pitch', fontsize=12, fontweight='bold', color='#0f172a', pad=12)

# Horizontal reference plane (ellipse)
h_theta = np.linspace(0, 2*np.pi, 100)
hx = 5 + 4 * np.cos(h_theta)
hy = 3 + 1.2 * np.sin(h_theta)
ax.plot(hx, hy, color='#64748b', lw=1.5, linestyle='--', label='Horizontal Projection Plane')

# Origin
ax.scatter([5], [3], color='#0f172a', s=100)

# Plunging line vector inclined downwards
ax.annotate('', xy=(8, 1.2), xytext=(5, 3),
            arrowprops=dict(facecolor='#dc2626', edgecolor='none', width=3, headwidth=8))
ax.text(8.2, 1.0, 'Linear Feature\n(Fold Hinge / Lineation)', fontsize=9.5, fontweight='bold', color='#dc2626')

# Horizontal projection vector (Trend)
ax.plot([5, 8], [3, 2.2], color='#0284c7', lw=2, linestyle=':')
ax.text(7.2, 2.5, 'Trend Direction\n(Azimuth)', fontsize=9, fontweight='bold', color='#0284c7')

# Vertical angle = Plunge
ax.text(6.4, 1.8, 'PLUNGE (θ)\nVertical Angle\nfrom Horizontal', fontsize=9.5, fontweight='bold', color='#b91c1c')

ax.set_xlim(0, 10); ax.set_ylim(0, 5.5); ax.axis('off'); ax.legend(loc='upper left', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q22/linear_feature_plunge_trend_block.png'), dpi=250)
plt.close()
print("Generated Q22 plunge figure.")

# =========================================================================
# Q23: Hooke's Law Stress-Strain Curve
# =========================================================================
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Rock Mechanics: Complete Stress-Strain Curve & Hooke\'s Law Linear Elasticity', fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)

strain = np.linspace(0, 0.08, 200)
# Elastic Hookean domain: sigma = E * strain
elastic_limit = 0.02
stress = np.zeros_like(strain)
for i, s in enumerate(strain):
    if s <= elastic_limit:
        stress[i] = 120 * (s / elastic_limit) # Linear Hooke's law
    elif s <= 0.06:
        stress[i] = 120 + 30 * np.sin((s - elastic_limit) / 0.04 * np.pi/2) # Plastic yield
    else:
        stress[i] = 150 - 200 * (s - 0.06) # Brittle failure

ax.plot(strain * 100, stress, color='#0f172a', lw=3)
ax.fill_between(strain[:50]*100, 0, stress[:50], color='#dcfce7', alpha=0.6, label='HOOKE\'S LAW DOMAIN: Linear Elastic (σ = E · ε)\n100% Recoverable Strain')
ax.fill_between(strain[50:150]*100, 0, stress[50:150], color='#fef3c7', alpha=0.5, label='Plastic Yield & Ductile Flow')

# Annotations
ax.scatter([elastic_limit*100], [120], color='#16a34a', s=120, zorder=5)
ax.text(elastic_limit*100 + 0.2, 115, 'Elastic Limit (Yield Stress σy)', fontsize=9.5, fontweight='bold', color='#15803d')
ax.scatter([6.0], [150], color='#dc2626', s=120, zorder=5)
ax.text(6.1, 145, 'Ultimate Compressive Strength (UCS)', fontsize=9.5, fontweight='bold', color='#b91c1c')

ax.set_xlabel('Axial Strain ε (%)', fontsize=10.5, fontweight='bold', labelpad=8)
ax.set_ylabel('Compressive Stress σ (MPa)', fontsize=10.5, fontweight='bold', labelpad=8)
ax.set_xlim(0, 8); ax.set_ylim(0, 170); ax.legend(loc='lower right', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q23/rock_mechanics_hookes_law_stress_strain.png'), dpi=250)
plt.close()
print("Generated Q23 Hooke's law figure.")

# =========================================================================
# Q24: Fold Anatomy: Hinge Line as Line of Maximum Curvature
# =========================================================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=250)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f8fafc')
ax.set_title('Fold Anatomy: Hinge Line (Maximum Curvature) vs. Crest & Axial Surface', fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)

# Fold profile: Asymmetric inclined anticline
fx = np.linspace(1, 9, 200)
fy = 2.0 + 3.0 * np.exp(-((fx - 4.5)/1.8)**2)
ax.plot(fx, fy, color='#0284c7', lw=3.5, label='Folded Geological Layer')

# Points of interest
# Hinge point (max curvature) at peak
ax.scatter([4.5], [5.0], color='#dc2626', s=150, zorder=5, label='HINGE POINT (Point of Maximum Curvature)')
ax.plot([4.5, 4.5], [1.0, 5.5], color='#dc2626', linestyle='--', lw=2, label='Axial Surface Trace')

# Limbs
ax.text(2.5, 3.0, 'Back Limb', fontsize=10, fontweight='bold', color='#475569')
ax.text(6.8, 3.0, 'Fore Limb', fontsize=10, fontweight='bold', color='#475569')

# Inflection point
ax.scatter([3.2], [3.2], color='#d97706', s=100, zorder=5, label='Inflection Point (Curvature κ = 0)')
ax.scatter([5.8], [3.2], color='#d97706', s=100, zorder=5)

ax.annotate('HINGE LINE\nConnecting points of maximum curvature across layer', xy=(4.5, 5.0), xytext=(5.5, 5.5),
            fontsize=9.5, fontweight='bold', color='#b91c1c', arrowprops=dict(facecolor='#b91c1c', width=1.5, headwidth=6))

ax.set_xlim(0, 10); ax.set_ylim(0.5, 6.2); ax.axis('off'); ax.legend(loc='lower center', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'figures_Q24/fold_anatomy_hinge_line_curvature.png'), dpi=250)
plt.close()
print("Generated Q24 fold anatomy figure.")

print("All remaining figures for Q1-Q25 generated successfully!")
