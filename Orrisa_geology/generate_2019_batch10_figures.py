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

# Q121: Refractive Index of Ocean Water vs Salinity and Temperature
def draw_q121(ax):
    salinity = np.linspace(0, 40, 100)
    n_10C = 1.3330 + 0.000195 * salinity
    n_20C = 1.3320 + 0.000190 * salinity
    n_30C = 1.3308 + 0.000185 * salinity
    ax.plot(salinity, n_10C, lw=3, color='#1d4ed8', label='T = 10 °C (Cold Water: Higher n)')
    ax.plot(salinity, n_20C, lw=3, color='#16a34a', label='T = 20 °C (Temperate Water)')
    ax.plot(salinity, n_30C, lw=3, color='#dc2626', label='T = 30 °C (Warm Water: Lower n)')
    ax.set_xlabel('Ocean Water Salinity S (PSU or ppt)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Refractive Index (n) at lambda = 589 nm', fontsize=11, fontweight='bold')
    ax.set_title('Q121: Optical Refractive Index of Seawater (Lorentz-Lorenz & Millard-Seaver Law)\nRefractive Index Increases Linearly with Salinity (Option A) & Decreases with Temperature (Option D)', fontsize=11.5, fontweight='bold', pad=12)
    ax.annotate('★ INCREASES WITH SALINITY (Option A) ★\nSlope dn/dS = +0.00019 per PSU\nDissolved Na+ and Cl- ions increase\noptical density & polarizability', xy=(35, n_10C[87]), xytext=(16, 1.3385),
                arrowprops=dict(arrowstyle='->', color='#1e3a8a', lw=2),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#dbeafe', edgecolor='#1d4ed8'), fontsize=9.5, fontweight='bold')
    ax.annotate('★ DECREASES WITH TEMPERATURE (Option D) ★\ndn/dT ≈ -0.0001 per °C (Thermal Expansion)', xy=(25, n_30C[62]), xytext=(12, 1.3322),
                arrowprops=dict(arrowstyle='->', color='#991b1b', lw=2),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'), fontsize=9.5, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='upper left', fontsize=9.5)

create_figure('figures_2019_Q121', 'ocean_water_refractive_index_salinity_temperature.png', draw_q121)

# Q122: Systematic vs Random Geometric Errors of Satellite Sensors
def draw_q122(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q122: Classification of Geometric Distortions in Satellite Remote Sensing\nSystematic (Predictable) Distortions vs. Random (Altitude & Attitude) Variations', fontsize=12, fontweight='bold', pad=12)
    # Left box: Systematic
    ax.add_patch(patches.FancyBboxPatch((0.4, 1.2), 4.3, 5.8, boxstyle='round,pad=0.2', facecolor='#eff6ff', edgecolor='#2563eb', lw=2))
    ax.text(2.55, 6.6, 'SYSTEMATIC (PREDICTABLE) ERRORS\n(Corrected by Ephemeris & Sensor Models)', ha='center', va='center', fontweight='bold', fontsize=10, color='#1e40af')
    sys_text = (
        "1. Scan Skew (Option A):\n   Forward spacecraft motion during cross-track\n   mirror sweep -> predictable diagonal tilt.\n\n"
        "2. Panoramic Distortion (Option B):\n   Constant IFOV angular scan across curved\n   Earth -> ground pixel stretches at swath edges.\n\n"
        "3. Earth Rotation Skew (Option C):\n   Eastward Earth rotation during southbound\n   pass shifts successive scan lines westward."
    )
    ax.text(0.6, 3.8, sys_text, va='center', fontsize=9, color='#1e293b')

    # Right box: Random
    ax.add_patch(patches.FancyBboxPatch((5.3, 1.2), 4.3, 5.8, boxstyle='round,pad=0.2', facecolor='#fef2f2', edgecolor='#dc2626', lw=2.5))
    ax.text(7.45, 6.6, '★ RANDOM (NON-SYSTEMATIC) ERRORS ★\n(Corrected using Ground Control Points - GCPs)', ha='center', va='center', fontweight='bold', fontsize=10, color='#991b1b')
    rand_text = (
        "★ 1. ALTITUDE VARIATION (Option D): ★\n   Unpredictable orbital height fluctuations\n   (atmospheric drag, gravity anomalies)\n   causing random scale changes.\n\n"
        "2. Attitude Variations (Roll, Pitch, Yaw):\n   Random spacecraft jitter & solar wind torques.\n\n"
        "3. Local Topographic Relief Displacement:\n   Terrain elevation variations across scene."
    )
    ax.text(5.5, 3.8, rand_text, va='center', fontsize=9, fontweight='bold', color='#7f1d1d')
    ax.text(5.0, 0.4, 'Verification: Scan skew, Panoramic distortion, and Earth rotation are deterministic/systematic; Altitude variation is RANDOM (Option D).', ha='center', fontsize=9.5, fontweight='bold', bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q122', 'satellite_geometric_errors_systematic_vs_random.png', draw_q122)

# Q123: Active vs Passive Remote Sensing Sensors
def draw_q123(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q123: Active vs. Passive Sensors in Remote Sensing\nActive Sensors Provide Their Own Electromagnetic Radiation to Illuminate the Earth Surface', fontsize=11.5, fontweight='bold', pad=12)
    # Ground
    ax.add_patch(patches.Rectangle((0.5, 0.5), 9.0, 1.0, facecolor='#86efac', edgecolor='#15803d', lw=2))
    ax.text(5.0, 1.0, 'EARTH SURFACE TARGET (Terrain, Canopy, Ocean)', ha='center', va='center', fontweight='bold', fontsize=10, color='#14532d')
    # Sun for Passive
    ax.add_patch(patches.Circle((1.5, 6.5), 0.6, facecolor='#facc15', edgecolor='#ca8a04', lw=2))
    ax.text(1.5, 6.5, 'SUN', ha='center', va='center', fontweight='bold', fontsize=9.5)
    ax.annotate('', xy=(2.8, 1.5), xytext=(1.8, 5.9), arrowprops=dict(arrowstyle='->', color='#eab308', lw=2.5, ls='--'))
    ax.annotate('', xy=(3.8, 5.8), xytext=(3.0, 1.5), arrowprops=dict(arrowstyle='->', color='#2563eb', lw=2.5))
    ax.add_patch(patches.Rectangle((3.2, 5.8), 1.6, 0.8, facecolor='#93c5fd', edgecolor='#1d4ed8', lw=2))
    ax.text(4.0, 6.2, 'PASSIVE SENSOR\n(LISS, Landsat, MODIS)', ha='center', va='center', fontweight='bold', fontsize=8.5)
    ax.text(2.5, 7.3, 'Passive: Relies on external\nsolar illumination or thermal emission', ha='center', fontsize=8.5, color='#1e40af')

    # Active sensor
    ax.add_patch(patches.Rectangle((6.8, 5.8), 2.2, 0.9, facecolor='#fca5a5', edgecolor='#dc2626', lw=2.5))
    ax.text(7.9, 6.25, '★ ACTIVE SENSOR ★\n(RADAR, SAR, LiDAR)\n(Option C)', ha='center', va='center', fontweight='bold', fontsize=8.8, color='#7f1d1d')
    ax.annotate('Transmitted Pulse\n(Illuminates Earth)', xy=(7.5, 1.5), xytext=(7.5, 5.8), arrowprops=dict(arrowstyle='->', color='#dc2626', lw=3))
    ax.annotate('Backscattered Echo', xy=(8.3, 5.8), xytext=(8.3, 1.5), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=3))
    ax.text(7.9, 7.3, 'Active: Emits specified wavelength/band\nto illuminate Earth day & night!', ha='center', fontweight='bold', fontsize=9, color='#991b1b')

create_figure('figures_2019_Q123', 'active_vs_passive_remote_sensing_sensors.png', draw_q123)

# Q124: Coherence Length vs Spectral Bandwidth
def draw_q124(ax):
    bw = np.linspace(0.5, 10, 200)
    Lc = 30.0 / bw
    ax.plot(bw, Lc, color='#7c3aed', lw=3.5, label=r'Coherence Length $L_c = c / \Delta\nu \propto 1 / \Delta\nu$')
    ax.set_xlabel(r'Spectral Bandwidth $\Delta\nu$ (GHz)', fontsize=11, fontweight='bold')
    ax.set_ylabel(r'Coherence Length $L_c$ (cm)', fontsize=11, fontweight='bold')
    ax.set_title('Q124: Wave Optics & SAR Interferometry — Coherence Length vs. Bandwidth\nCoherence Length (Lc) Is Inversely Proportional to Spectral Bandwidth (Option B)', fontsize=11.5, fontweight='bold', pad=12)
    ax.plot(1.5, 20.0, 'ro', markersize=9)
    ax.annotate('Narrow Bandwidth (Monochromatic Laser/SAR):\nLong Coherence Length (Strong Phase Correlation)', xy=(1.5, 20.0), xytext=(2.8, 22.0),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'), fontsize=9, fontweight='bold')
    ax.plot(6.0, 5.0, 'bo', markersize=9)
    ax.annotate('Wide Bandwidth (Broadband Light):\nShort Coherence Length', xy=(6.0, 5.0), xytext=(5.5, 11.0),
                arrowprops=dict(arrowstyle='->', color='#1d4ed8', lw=2),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#dbeafe', edgecolor='#1d4ed8'), fontsize=9, fontweight='bold')
    ax.text(5.2, 29.0, 'Fundamental Formula:\n• Coherence Time: tau_c = 1 / Delta_nu\n• Coherence Length: L_c = c * tau_c = c / Delta_nu = lambda^2 / Delta_lambda\n• Therefore: L_c is INVERSELY PROPORTIONAL to Bandwidth (Option B)', fontsize=9.5, bbox=dict(facecolor='#f3e8ff', edgecolor='#7c3aed'))
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=10)

create_figure('figures_2019_Q124', 'coherence_length_inversely_proportional_bandwidth.png', draw_q124)

# Q125: Atmospheric Windows in Remote Sensing
def draw_q125(ax):
    wl = np.linspace(0.2, 14, 500)
    trans = np.zeros_like(wl)
    # Visible-NIR window (0.4-1.1), SWIR windows (1.5-1.8, 2.0-2.4), MWIR (3-5), TIR (8-14)
    trans += 85 * np.exp(-((wl - 0.65)/0.35)**4)
    trans += 75 * np.exp(-((wl - 1.65)/0.15)**4)
    trans += 75 * np.exp(-((wl - 2.2)/0.18)**4)
    trans += 80 * np.exp(-((wl - 4.0)/0.6)**4)
    trans += 90 * np.exp(-((wl - 10.5)/2.2)**6)
    trans = np.clip(trans, 2, 95)
    ax.plot(wl, trans, color='#0f766e', lw=2.5)
    ax.fill_between(wl, 0, trans, color='#99f6e4', alpha=0.5, label='★ ATMOSPHERIC WINDOWS (High Transmission) ★')
    ax.fill_between(wl, trans, 100, color='#cbd5e1', alpha=0.6, label='Atmospheric Absorption Bands (H2O, CO2, O3)')
    ax.set_xlabel('Wavelength lambda (micrometers, µm)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Atmospheric Transmittance (%)', fontsize=11, fontweight='bold')
    ax.set_ylim(0, 108)
    ax.set_title('Q125: Atmospheric Windows Across the Electromagnetic Spectrum\nSpectral Regions Passing Through Atmosphere Without Much Attenuation (Option B)', fontsize=11.5, fontweight='bold', pad=12)
    ax.text(0.7, 92, 'Visible/NIR\n(0.4-1.1 µm)', ha='center', fontweight='bold', fontsize=8.5, color='#115e59')
    ax.text(4.0, 86, 'MWIR\n(3-5 µm)', ha='center', fontweight='bold', fontsize=8.5, color='#115e59')
    ax.text(10.5, 95, 'Thermal IR Window\n(8-14 µm)', ha='center', fontweight='bold', fontsize=9, color='#115e59')
    ax.text(6.3, 35, 'H2O Absorption\n(5.5-7.5 µm)', ha='center', fontweight='bold', fontsize=8.5, color='#991b1b')
    ax.text(0.25, 45, 'O3\nUV Block', ha='center', fontweight='bold', fontsize=8, color='#991b1b')
    ax.legend(loc='upper right', fontsize=9.5)
    ax.grid(True, linestyle=':', alpha=0.5)

create_figure('figures_2019_Q125', 'atmospheric_windows_electromagnetic_transmission.png', draw_q125)

# Q126: Planck's Law Energy Quantum E = h * nu
def draw_q126(ax):
    freq = np.linspace(0, 10, 100) # 10^14 Hz
    energy = 0.4136 * freq # eV
    ax.plot(freq, energy, color='#dc2626', lw=3.5, label=r'Planck Quantum Relation: $E = h\nu$ (Slope = $h$)')
    ax.set_xlabel(r'Radiation Frequency $\nu$ ($10^{14}$ Hz)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Photon Quantum Energy E (eV)', fontsize=11, fontweight='bold')
    ax.set_title("Q126: Planck's Quantum Theory of Electromagnetic Radiation\nEnergy of a Radiation Quantum (Photon) Is Directly Proportional to Frequency (Option A)", fontsize=11.5, fontweight='bold', pad=12)
    ax.plot(4.3, 1.78, 'bo', markersize=8)
    ax.text(4.5, 1.65, 'Red Light (4.3e14 Hz -> 1.78 eV)', fontsize=9, fontweight='bold', color='#1d4ed8')
    ax.plot(7.5, 3.10, 'mo', markersize=8)
    ax.text(5.2, 3.25, 'Violet Light (7.5e14 Hz -> 3.10 eV)', fontsize=9, fontweight='bold', color='#7e22ce')
    ax.text(0.6, 2.8, "Planck-Einstein Relation (1900/1905):\n• E = h * nu = (h * c) / lambda\n• h = 6.626 x 10^-34 J.s (Planck's Constant)\n• Therefore: E is DIRECTLY PROPORTIONAL\n  to Frequency nu (Option A)!", fontsize=9.5, fontweight='bold', bbox=dict(facecolor='#fef2f2', edgecolor='#dc2626'))
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='lower right', fontsize=10)

create_figure('figures_2019_Q126', 'planck_quantum_energy_proportional_to_frequency.png', draw_q126)

# Q127: Relief (Height) Displacement of Two Towers A (3 km) and B (5 km)
def draw_q127(ax):
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    ax.set_title('Q127: Aerial Photogrammetry — Radial Relief (Height) Displacement Formula (d = r·h / H)\nTower A (r = 3 km) vs. Tower B (r = 5 km) of Equal Height h: d_A < d_B (Option A)', fontsize=11.5, fontweight='bold', pad=12)
    # Ground line
    ax.plot([-6, 6], [1.0, 1.0], 'k-', lw=2.5)
    ax.plot([0, 0], [0.5, 7.8], 'k--', lw=1.5)
    ax.text(0.1, 0.6, 'Nadir / Principal Point (N, r=0)', fontweight='bold', fontsize=9)
    # Camera lens at (0, 7.0)
    ax.plot(0, 7.0, 'ko', markersize=10)
    ax.text(0, 7.4, 'Camera Exposure Station L (Flying Height H)', ha='center', fontweight='bold', fontsize=9.5, color='#1e40af')
    # Image plane at y = 5.2
    ax.plot([-5.5, 5.5], [5.2, 5.2], color='#2563eb', lw=2.5, label='Image Plane (Focal Length f)')
    # Tower A at x = -3, height = 2.0
    ax.add_patch(patches.Rectangle((-3.15, 1.0), 0.3, 2.0, facecolor='#f59e0b', edgecolor='#b45309', lw=2))
    ax.text(-3.0, 0.5, 'Tower A\n(r_A = 3 km)', ha='center', fontweight='bold', fontsize=9, color='#b45309')
    # Rays for Tower A base and top
    ax.plot([0, -3.0], [7.0, 1.0], 'b:', lw=1.5)
    ax.plot([0, -4.5], [7.0, 1.0], 'r-', lw=2) # passes through (-3.0, 3.0)
    # Tower B at x = +5 (scaled to +4.2), height = 2.0
    ax.add_patch(patches.Rectangle((3.85, 1.0), 0.3, 2.0, facecolor='#10b981', edgecolor='#047857', lw=2))
    ax.text(4.0, 0.5, 'Tower B\n(r_B = 5 km)', ha='center', fontweight='bold', fontsize=9, color='#047857')
    ax.plot([0, 4.0], [7.0, 1.0], 'b:', lw=1.5)
    ax.plot([0, 6.0], [7.0, 1.0], 'r-', lw=2) # passes through (4.0, 3.0)

    ax.annotate('d_A (Smaller\ndisplacement)', xy=(-1.1, 5.2), xytext=(-3.8, 6.1), arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2), fontweight='bold', fontsize=9, bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626'))
    ax.annotate('d_B (Larger displacement\nsince r_B = 5 km > r_A = 3 km)', xy=(1.5, 5.2), xytext=(2.0, 6.1), arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2), fontweight='bold', fontsize=9, bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626'))
    ax.text(0, 3.6, 'Relief Displacement Formula:\nd = (r * h) / H\nSince h_A = h_B and H is constant:\nd is directly proportional to radial distance r!\nr_A (3 km) < r_B (5 km)  ===>  d_A < d_B (Option A)', ha='center', fontsize=9.2, fontweight='bold', bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q127', 'aerial_photogrammetry_relief_height_displacement_towers.png', draw_q127)

# Q128: Microstrip (Patch) Antenna in GPS
def draw_q128(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q128: Satellite Geodesy & GNSS Hardware — Microstrip (Patch) Antenna in GPS\nCompact, Circularly Polarized (RHCP), Hemispherical-Coverage Antenna (Option B)', fontsize=11.5, fontweight='bold', pad=12)
    # Ground plane
    ax.add_patch(patches.Polygon([[1.5, 2.0], [7.5, 2.0], [8.5, 3.2], [2.5, 3.2]], facecolor='#64748b', edgecolor='#1e293b', lw=2))
    ax.text(4.8, 2.2, 'Metallic Ground Plane (Copper Backing)', color='white', fontweight='bold', fontsize=9, ha='center')
    # Dielectric substrate
    ax.add_patch(patches.Polygon([[1.8, 2.5], [7.2, 2.5], [8.1, 3.6], [2.7, 3.6]], facecolor='#bbf7d0', edgecolor='#15803d', lw=2))
    ax.text(5.0, 2.9, 'High-Permittivity Ceramic Dielectric Substrate (epsilon_r)', color='#14532d', fontweight='bold', fontsize=9, ha='center')
    # Radiating metallic patch
    ax.add_patch(patches.Polygon([[2.8, 3.1], [6.2, 3.1], [6.9, 3.9], [3.5, 3.9]], facecolor='#f59e0b', edgecolor='#b45309', lw=2.5))
    ax.text(4.85, 3.5, '★ RADIATING MICROSTRIP PATCH ★\n(L1 = 1575.42 MHz, L2 = 1227.60 MHz)', color='#78350f', fontweight='bold', fontsize=9.5, ha='center')
    # Hemispherical radiation lobes
    theta = np.linspace(0, np.pi, 100)
    rx = 4.85 + 2.8 * np.cos(theta)
    ry = 3.9 + 2.6 * np.sin(theta)**1.5
    ax.plot(rx, ry, 'r--', lw=2.5)
    ax.fill(rx, ry, color='#fecaca', alpha=0.35)
    ax.text(4.85, 5.4, 'Omnidirectional Upper-Hemisphere\nReception Pattern (RHCP Polarization)\nTracks 4 to 12+ GPS Satellites Simultaneously!', ha='center', fontweight='bold', fontsize=9.5, color='#991b1b')
    ax.text(5.0, 0.8, 'Why Microstrip Antenna (Option B) Dominates GPS:\nLow profile, rugged, inexpensive PCB fabrication, supports Right-Hand Circular Polarization (RHCP),\nand receives signals from satellites across the entire sky dome without mechanical steering.', ha='center', fontsize=9, bbox=dict(facecolor='#f8fafc', edgecolor='#475569'))

create_figure('figures_2019_Q128', 'gps_microstrip_patch_antenna_architecture.png', draw_q128)

# Q129: Fresnel Reflection & Transmission at Dielectric Interface
def draw_q129(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q129: Electromagnetic Wave Interaction at a Dielectric Boundary (n1 != n2)\nFresnel Reflection & Refraction Equations Governing Reflected and Transmitted Amplitudes', fontsize=11.5, fontweight='bold', pad=12)
    # Media 1 and Media 2
    ax.add_patch(patches.Rectangle((0.5, 4.0), 9.0, 3.2, facecolor='#eff6ff', edgecolor='#93c5fd', lw=1.5))
    ax.add_patch(patches.Rectangle((0.5, 0.8), 9.0, 3.2, facecolor='#dbeafe', edgecolor='#3b82f6', lw=1.5))
    ax.plot([0.5, 9.5], [4.0, 4.0], 'k-', lw=2.5)
    ax.plot([5.0, 5.0], [1.0, 7.0], 'k--', lw=1.5)
    ax.text(1.8, 6.6, 'Incident Medium 1\nRefractive Index = n1', fontweight='bold', fontsize=10, color='#1e40af')
    ax.text(1.8, 1.4, 'Transmitting Medium 2\nRefractive Index = n2 (n2 > n1)', fontweight='bold', fontsize=10, color='#1e3a8a')
    # Incident ray
    ax.annotate('', xy=(5.0, 4.0), xytext=(2.0, 6.8), arrowprops=dict(arrowstyle='->', color='#dc2626', lw=3.5))
    ax.text(2.6, 5.5, 'Incident EM Wave (E_i)\nAngle theta_i', fontweight='bold', color='#dc2626', fontsize=9.5, rotation=-40)
    # Reflected ray
    ax.annotate('', xy=(8.0, 6.8), xytext=(5.0, 4.0), arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=3))
    ax.text(6.1, 5.5, '★ Reflected Wave (E_r) ★\nFresnel Reflection (Option A)\ntheta_r = theta_i', fontweight='bold', color='#b45309', fontsize=9.5, rotation=40)
    # Transmitted ray
    ax.annotate('', xy=(6.8, 1.1), xytext=(5.0, 4.0), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=3))
    ax.text(6.0, 2.3, 'Transmitted / Refracted Wave (E_t)\nn1 sin(theta_i) = n2 sin(theta_t)', fontweight='bold', color='#15803d', fontsize=9.5)
    ax.text(7.5, 3.4, 'Fresnel Reflection Coefficient (Normal Incidence):\nR = |(n1 - n2) / (n1 + n2)|^2 ,  T = 1 - R', ha='center', fontweight='bold', fontsize=9, bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q129', 'fresnel_reflection_transmission_dielectric_boundary.png', draw_q129)

# Q130: Normal Altitude of GPS Satellites (~20,200 km)
def draw_q130(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q130: Orbital Altitudes of Earth Observation, GNSS (GPS), and Geostationary Satellites\nGPS Constellation Operates in Medium Earth Orbit (MEO) at ~20,200 km Altitude (Option B)', fontsize=11.5, fontweight='bold', pad=12)
    # Earth circle on left
    earth = patches.Circle((1.8, 4.0), 1.2, facecolor='#3b82f6', edgecolor='#1d4ed8', lw=2.5)
    ax.add_patch(earth)
    ax.text(1.8, 4.0, 'EARTH\nR = 6,378 km', color='white', fontweight='bold', ha='center', va='center', fontsize=9.5)
    # LEO arc
    leo = patches.Arc((1.8, 4.0), 3.4, 3.4, theta1=-60, theta2=60, color='#16a34a', lw=2.5, ls='--')
    ax.add_patch(leo)
    ax.text(3.7, 5.4, 'LEO (IRS / Landsat / Sentinel)\nAltitude: 600 - 900 km', color='#15803d', fontweight='bold', fontsize=9)
    # MEO GPS arc
    meo = patches.Arc((1.8, 4.0), 7.6, 6.6, theta1=-55, theta2=55, color='#dc2626', lw=3.5)
    ax.add_patch(meo)
    ax.plot(5.6, 4.0, 'rs', markersize=12)
    ax.text(5.8, 4.0, '★ GPS CONSTELLATION (MEO) ★\nNormal Altitude = 20,200 km (Option B)\nOrbital Period = 11 hr 58 min (2 orbits/day)\n6 Orbital Planes at 55° Inclination', color='#991b1b', fontweight='bold', fontsize=9.5, va='center', bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626'))
    # GEO arc
    geo = patches.Arc((1.8, 4.0), 14.5, 7.6, theta1=-35, theta2=35, color='#7c3aed', lw=2.5, ls='-.')
    ax.add_patch(geo)
    ax.text(7.5, 1.4, 'GEO (INSAT / Meteosat)\nAltitude: ~35,786 km (36,000 km)', color='#6d28d9', fontweight='bold', fontsize=9)

create_figure('figures_2019_Q130', 'gps_satellite_normal_altitude_20200_km_meo.png', draw_q130)

# Q131: Sun-Synchronous Orbit for Monitoring Dynamic Earth Surface Changes
def draw_q131(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q131: Sun-Synchronous Orbit (SSO) for Dynamic Multi-Temporal Change Detection\nConstant Local Solar Time (LST) & Uniform Illumination Geometry Across Repeat Passes (Option B)', fontsize=11.5, fontweight='bold', pad=12)
    # Earth in center
    ax.add_patch(patches.Circle((4.5, 4.0), 1.6, facecolor='#60a5fa', edgecolor='#1e3a8a', lw=2))
    ax.text(4.5, 4.0, 'EARTH\nEquatorial Bulge J2\nPrecesses Orbit\n+0.9856° / day', color='white', fontweight='bold', ha='center', va='center', fontsize=9)
    # Orbit ellipse tilted at 98 deg
    orbit = patches.Ellipse((4.5, 4.0), 2.2, 5.8, angle=-8, fill=False, edgecolor='#dc2626', lw=3)
    ax.add_patch(orbit)
    ax.text(4.5, 7.3, '★ SUN-SYNCHRONOUS NEAR-POLAR ORBIT (i ≈ 98° - 99°) ★', ha='center', fontweight='bold', fontsize=10, color='#991b1b')
    # Sun rays from right
    for y in [2.5, 4.0, 5.5]:
        ax.annotate('', xy=(6.5, y), xytext=(9.2, y), arrowprops=dict(arrowstyle='->', color='#eab308', lw=3))
    ax.text(8.2, 6.2, 'Incoming Solar Rays\nConstant Sun-Orbit Angle!\n(e.g., 10:30 AM Equator Crossing)', ha='center', fontweight='bold', fontsize=9.5, color='#a16207')
    # Info box
    info = (
        "Why Sun-Synchronous Orbit (Option B) Is Ideal for Change Monitoring:\n"
        "• Crosses every latitude at the EXACT SAME LOCAL SOLAR TIME on every pass.\n"
        "• Eliminates false shadow/illumination artifacts between multi-date images.\n"
        "• Used by Resourcesat (IRS), Landsat, Sentinel-2, and SPOT satellites."
    )
    ax.text(5.0, 0.6, info, ha='center', fontsize=9, bbox=dict(facecolor='#fef2f2', edgecolor='#dc2626'))

create_figure('figures_2019_Q131', 'sun_synchronous_orbit_dynamic_change_monitoring.png', draw_q131)

# Q132: Planetary Albedo vs Spectral Reflectance
def draw_q132(ax):
    surfaces = ['Fresh Snow\n/ Ice', 'Cumulus\nClouds', 'Desert\nSand', 'Planetary Earth\n(Mean Albedo)', 'Green Forest\nCanopy', 'Calm Ocean\nWater']
    albedos = [0.85, 0.70, 0.35, 0.30, 0.15, 0.06]
    colors = ['#e2e8f0', '#94a3b8', '#fcd34d', '#3b82f6', '#22c55e', '#1e3a8a']
    bars = ax.bar(surfaces, albedos, color=colors, edgecolor='#0f172a', lw=1.5)
    ax.set_ylabel('Albedo (A = E_reflected / E_incident)', fontsize=11, fontweight='bold')
    ax.set_ylim(0, 1.05)
    ax.set_title('Q132: Radiometric Definitions — Planetary Albedo (Option C)\nRatio of Total Solar Radiant Energy Returned by a Planetary Body to Total Incident Energy', fontsize=11.5, fontweight='bold', pad=12)
    for b, val in zip(bars, albedos):
        ax.text(b.get_x() + b.get_width()/2, val + 0.02, f'{val:.2f}\n({int(val*100)}%)', ha='center', fontweight='bold', fontsize=9)
    ax.text(3.2, 0.78, '★ ALBEDO DEFINITION (Option C) ★\nA = (Total Broadband Hemispherical Reflected Flux)\n    / (Total Incident Solar Radiant Flux)\n• Earth Mean Bond Albedo ≈ 0.30 (30%)\n• Spectral Reflectance rho(lambda) is at a single wavelength;\n  Albedo integrates over ALL solar wavelengths!', fontsize=9.2, bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))
    ax.grid(axis='y', linestyle='--', alpha=0.5)

create_figure('figures_2019_Q132', 'planetary_albedo_total_solar_radiant_energy_ratio.png', draw_q132)

# Q133: Wien's Displacement Law & Maximum Solar Radiation around 0.55 um
def draw_q133(ax):
    wl = np.linspace(0.15, 2.5, 400) # micrometers
    # Planck curve for T = 5778 K
    c1 = 3.7418e8
    c2 = 14388.0
    T = 5778.0
    irrad = (c1 / (wl**5)) / (np.exp(c2 / (wl * T)) - 1.0)
    irrad = irrad / np.max(irrad) * 100.0
    ax.plot(wl, irrad, color='#dc2626', lw=3, label='Solar Blackbody Spectrum (T ≈ 5778 K)')
    ax.axvspan(0.4, 0.7, color='#fde047', alpha=0.35, label='Visible Light Band (0.4 - 0.7 µm)')
    ax.axvline(0.55, color='#15803d', lw=2.5, ls='--')
    ax.plot(0.50, 100, 'ro', markersize=10)
    ax.annotate("★ PEAK SOLAR RADIATION (~0.50 - 0.55 µm) ★\nWien's Displacement Law: lambda_max = 2898 / T\nOccurs in Visible Green-Yellow Band (Option B: 0.55 µm)", xy=(0.55, 98), xytext=(0.85, 82),
                arrowprops=dict(arrowstyle='->', color='#15803d', lw=2.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#dcfce7', edgecolor='#15803d'), fontsize=9.5, fontweight='bold')
    ax.set_xlabel('Wavelength lambda (micrometers, µm)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Relative Spectral Irradiance (%)', fontsize=11, fontweight='bold')
    ax.set_ylim(0, 112)
    ax.set_title("Q133: Solar Spectral Irradiance & Wien's Displacement Law\nMaximum Sun's Radiation Occurs Around 0.55 µm Wavelength (Option B)", fontsize=11.5, fontweight='bold', pad=12)
    ax.legend(loc='upper right', fontsize=9.5)
    ax.grid(True, linestyle=':', alpha=0.6)

create_figure('figures_2019_Q133', 'wiens_law_maximum_solar_radiation_0_55_um.png', draw_q133)

# Q134: Spatial Resolution of Resourcesat-1 (IRS-P6) Sensors: LISS-IV = 5.8 m
def draw_q134(ax):
    sensors = ['LISS-IV\n(High-Res Multispectral)\n★ Option A ★', 'LISS-III\n(Medium-Res 4-Band)\n(Option B)', 'AWiFS\n(Wide-Field Sensor)\n(Option C)', 'LISS-I (IRS-1A)\n(Historical Sensor)\n(72.5 m)']
    res = [5.8, 23.5, 56.0, 72.5]
    colors = ['#dc2626', '#2563eb', '#16a34a', '#64748b']
    bars = ax.bar(sensors, res, color=colors, edgecolor='#0f172a', lw=1.5, width=0.55)
    ax.set_ylabel('Spatial Resolution / Ground Sample Distance (m)', fontsize=11, fontweight='bold')
    ax.set_ylim(0, 85)
    ax.set_title('Q134: ISRO Resourcesat-1 (IRS-P6) Payload Spatial Resolutions\nLISS-IV Spatial Resolution Is 5.8 m (Option A)', fontsize=12, fontweight='bold', pad=12)
    for b, val in zip(bars, res):
        ax.text(b.get_x() + b.get_width()/2, val + 2.0, f'{val} m', ha='center', fontweight='bold', fontsize=10.5)
    ax.annotate('★ LISS-IV = 5.8 m Resolution ★\nBands: B2 (Green 0.52-0.59 µm),\nB3 (Red 0.62-0.68 µm), B4 (NIR 0.77-0.86 µm)\nSwath: 23.9 km (MS) / 70 km (Mono)', xy=(0, 5.8), xytext=(0.35, 42),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'), fontsize=9.5, fontweight='bold')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

create_figure('figures_2019_Q134', 'resourcesat_1_liss_iv_spatial_resolution_5_8m.png', draw_q134)

# Q135: Digital Image Processing (Rectification, Enhancement, Classification)
def draw_q135(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q135: Digital Image Processing (DIP) Workflow in Remote Sensing\nManipulation of Digital Data Including Rectification, Enhancement & Classification (Option B)', fontsize=11.5, fontweight='bold', pad=12)
    # Main header banner
    ax.add_patch(patches.FancyBboxPatch((1.5, 6.2), 7.0, 1.1, boxstyle='round,pad=0.15', facecolor='#fef2f2', edgecolor='#dc2626', lw=2.5))
    ax.text(5.0, 6.75, '★ DIGITAL IMAGE PROCESSING (DIP) — (Option B) ★\nComplete Science of Digital Satellite Data Manipulation', ha='center', va='center', fontweight='bold', fontsize=10.5, color='#991b1b')
    # Three pillars
    boxes = [
        (0.4, '1. PRE-PROCESSING\n(Rectification & Restoration)\n\n• Radiometric Correction\n  (Haze / Sun angle / Striping)\n• Geometric Rectification\n  (GCPs, Resampling, Ortho)', '#dbeafe', '#1d4ed8'),
        (3.6, '2. IMAGE ENHANCEMENT\n(Visual Interpretability)\n\n• Contrast Stretching\n• Histogram Equalization\n• Spatial Filtering (Edge/LPF)\n• Band Ratioing (NDVI, PCA)', '#dcfce7', '#15803d'),
        (6.8, '3. IMAGE CLASSIFICATION\n(Information Extraction)\n\n• Unsupervised (K-Means, ISODATA)\n• Supervised (Maximum Likelihood,\n  Random Forest, SVM, CNN)\n• Accuracy Assessment (Kappa)', '#fef3c7', '#b45309')
    ]
    for x, txt, fc, ec in boxes:
        ax.add_patch(patches.FancyBboxPatch((x, 1.2), 2.8, 4.2, boxstyle='round,pad=0.15', facecolor=fc, edgecolor=ec, lw=2))
        ax.text(x + 1.4, 3.3, txt, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e293b')
        ax.annotate('', xy=(x + 1.4, 5.4), xytext=(5.0, 6.2), arrowprops=dict(arrowstyle='->', color=ec, lw=2))

create_figure('figures_2019_Q135', 'digital_image_processing_enhancement_classification_rectification.png', draw_q135)

# Q136: Geographic Field (Continuous Surface Where Every Point Has a Value)
def draw_q136(ax):
    x = np.linspace(0, 10, 50)
    y = np.linspace(0, 6, 40)
    X, Y = np.meshgrid(x, y)
    Z = 500 + 150 * np.sin(0.6 * X) * np.cos(0.7 * Y) + 80 * np.exp(-((X-7)**2 + (Y-3)**2)/3)
    cp = ax.contourf(X, Y, Z, levels=15, cmap='terrain')
    plt.colorbar(cp, ax=ax, label='Continuous Field Attribute Value Z(x, y) [e.g., Elevation m]')
    ax.contour(X, Y, Z, levels=15, colors='k', linewidths=0.5, alpha=0.5)
    pts = [(2.0, 2.0), (5.0, 4.2), (7.5, 2.8)]
    for px, py in pts:
        val = 500 + 150 * np.sin(0.6 * px) * np.cos(0.7 * py) + 80 * np.exp(-((px-7)**2 + (py-3)**2)/3)
        ax.plot(px, py, 'ro', markersize=8, markeredgecolor='white', markeredgewidth=1.5)
        ax.text(px + 0.2, py + 0.15, f'P({px:.1f},{py:.1f})\nZ = {val:.0f} m', fontweight='bold', fontsize=8.5, bbox=dict(facecolor='white', alpha=0.85, edgecolor='#dc2626'))
    ax.set_xlabel('Easting X Coordinate (km)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Northing Y Coordinate (km)', fontsize=11, fontweight='bold')
    ax.set_title('Q136: Continuous Geographic Field Model Z = f(x, y) in GIS\nFor Every Point (x, y) in the Study Area, a Single Attribute Value Can Be Determined (Option A)', fontsize=11, fontweight='bold', pad=12)

create_figure('figures_2019_Q136', 'geographic_field_continuous_surface_value_every_point.png', draw_q136)

# Q137: Spatial Autocorrelation & Tobler's First Law of Geography
def draw_q137(ax):
    h = np.linspace(0, 100, 200)
    # Spherical semivariogram and autocorrelation
    gamma = np.where(h <= 60, 1.0 * (1.5*(h/60) - 0.5*(h/60)**3), 1.0)
    rho = 1.0 - gamma
    ax.plot(h, rho, color='#dc2626', lw=3.5, label='Spatial Autocorrelation r(h) (High at short lag distance)')
    ax.plot(h, gamma, color='#2563eb', lw=2.5, ls='--', label='Semivariance gamma(h) (Kriging Variogram)')
    ax.axvline(60, color='#15803d', lw=2, ls=':')
    ax.text(62, 0.5, 'Range of Spatial\nDependence (a = 60 km)', fontweight='bold', color='#15803d', fontsize=9.5)
    ax.set_xlabel('Separation Lag Distance h Between Sample Points (km)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Normalized Correlation / Semivariance', fontsize=11, fontweight='bold')
    ax.set_title("Q137: Principle Enabling Spatial Interpolation — Spatial Autocorrelation (Option A)\nTobler's First Law: Near Points Have Strongly Correlated Values, Allowing Unknown Estimation", fontsize=11, fontweight='bold', pad=12)
    ax.annotate('★ SPATIAL AUTOCORRELATION (Option A) ★\nNearby sample points share similar values\n(Moran\'s I > 0), making IDW & Kriging possible!', xy=(12, 0.72), xytext=(22, 0.80),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'), fontsize=9.2, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='center right', fontsize=9.5)

create_figure('figures_2019_Q137', 'spatial_autocorrelation_toblers_law_variogram.png', draw_q137)

# Q138: Spatial Data Infrastructure (SDI) Architecture
def draw_q138(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q138: Spatial Data Infrastructure (SDI) — Pillars & Architecture (Option B)\nInstitutional, Technical, Policy & Standards Framework for Sharing Geospatial Data (NSDI)', fontsize=11.5, fontweight='bold', pad=12)
    ax.add_patch(patches.Circle((5.0, 4.0), 1.35, facecolor='#dc2626', edgecolor='#7f1d1d', lw=2.5))
    ax.text(5.0, 4.0, '★ SDI ★\nSpatial Data\nInfrastructure\n(Option B)', color='white', fontweight='bold', ha='center', va='center', fontsize=10.5)
    pillars = [
        (1.8, 6.2, '1. Institutional Policy\n& Governance\n(NSDI / Open Data)'),
        (8.2, 6.2, '2. OGC Technical\nStandards\n(WMS, WFS, WCS, ISO 19115)'),
        (1.8, 1.8, '3. Fundamental Core\nSpatial Datasets\n(Geodetic, Topo, Geology)'),
        (8.2, 1.8, '4. Clearinghouse &\nGeoportal Network\n(Metadata Discovery)'),
        (5.0, 7.1, '5. Users, Citizens & Decision Makers')
    ]
    for px, py, txt in pillars:
        ax.add_patch(patches.FancyBboxPatch((px-1.35, py-0.6), 2.7, 1.2, boxstyle='round,pad=0.12', facecolor='#eff6ff', edgecolor='#1d4ed8', lw=2))
        ax.text(px, py, txt, ha='center', va='center', fontweight='bold', fontsize=8.5, color='#1e3a8a')
        ax.annotate('', xy=(5.0 + (px-5.0)*0.38, 4.0 + (py-4.0)*0.38), xytext=(px - (px-5.0)*0.35, py - (py-4.0)*0.35),
                    arrowprops=dict(arrowstyle='<->', color='#475569', lw=2))

create_figure('figures_2019_Q138', 'spatial_data_infrastructure_sdi_components.png', draw_q138)

# Q139: Spatial Interpolation Using Known Control Points to Estimate Unknown Points
def draw_q139(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q139: Spatial Interpolation in GIS (IDW, Kriging, Spline)\nEstimating Values at Unknown Points Using Surrounding Sample Points with Known Values (Option B)', fontsize=11, fontweight='bold', pad=12)
    # Unknown target point in center
    ax.plot(5.0, 4.0, 'r*', markersize=20)
    ax.text(5.0, 4.55, '★ Unknown Target Point (x0, y0) ★\nEstimated Value Z_hat = 148.2 ppm', ha='center', fontweight='bold', fontsize=9.5, color='#991b1b', bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626'))
    known_pts = [
        (2.0, 6.0, 'Z1 = 160 ppm', 'd1 = 3.6 km (w1 = 0.25)'),
        (8.0, 5.8, 'Z2 = 130 ppm', 'd2 = 3.5 km (w2 = 0.26)'),
        (2.5, 1.8, 'Z3 = 175 ppm', 'd3 = 3.3 km (w3 = 0.30)'),
        (7.8, 1.6, 'Z4 = 115 ppm', 'd4 = 3.7 km (w4 = 0.19)')
    ]
    for kx, ky, ztxt, dtxt in known_pts:
        ax.plot(kx, ky, 'bo', markersize=11)
        ax.plot([kx, 5.0], [ky, 4.0], 'b--', lw=2)
        ax.text(kx, ky + (0.55 if ky > 4 else -0.65), f'Known Point\n{ztxt}', ha='center', fontweight='bold', fontsize=9, bbox=dict(facecolor='#dbeafe', edgecolor='#1d4ed8'))
        ax.text((kx+5.0)/2, (ky+4.0)/2 - 0.25, dtxt, ha='center', fontsize=8, color='#1e40af', fontweight='bold')
    ax.text(5.0, 0.45, 'Inverse Distance Weighting (IDW) Formula:  Z_hat(x0) = Sum[ w_i * Z(x_i) ] / Sum[ w_i ],  where w_i = 1 / d_i^p', ha='center', fontweight='bold', fontsize=9.5, bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q139', 'spatial_interpolation_idw_kriging_unknown_points.png', draw_q139)

# Q140: Representation of a Large City Across Map Scales (1:25,000 vs 1:1,000,000)
def draw_q140(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q140: Cartographic Scale & Feature Generalization in GIS\nHow a Large City Appears on a Large-Scale 1:25,000 Topographic Map (Options B / C)', fontsize=11.5, fontweight='bold', pad=12)
    # Left panel: Small scale 1:1,000,000
    ax.add_patch(patches.Rectangle((0.5, 1.5), 4.0, 5.2, facecolor='#f8fafc', edgecolor='#64748b', lw=2))
    ax.text(2.5, 6.3, 'Small-Scale Map (1 : 1,000,000)\n(1 cm = 10 km)', ha='center', fontweight='bold', fontsize=9.5, color='#334155')
    ax.plot(2.5, 3.8, 'ro', markersize=12)
    ax.text(2.5, 3.1, 'Bhubaneswar\n(Appears as a Single Point - Option A)', ha='center', fontweight='bold', fontsize=9, color='#991b1b')

    # Right panel: Large scale 1:25,000
    ax.add_patch(patches.Rectangle((5.2, 1.5), 4.3, 5.2, facecolor='#fef2f2', edgecolor='#dc2626', lw=2.5))
    ax.text(7.35, 6.3, '★ Large-Scale Map (1 : 25,000) ★\n(1 cm = 250 m -> Detailed Urban Features)', ha='center', fontweight='bold', fontsize=9.5, color='#991b1b')
    # Polygons (sectors/parks)
    ax.add_patch(patches.Polygon([[5.7, 2.2], [9.0, 2.2], [8.8, 5.4], [5.9, 5.2]], facecolor='#fecdd3', edgecolor='#e11d48', lw=2, label='City Boundary Polygon'))
    ax.add_patch(patches.Rectangle((6.2, 3.8), 1.0, 0.9, facecolor='#bbf7d0', edgecolor='#16a34a', lw=1.5))
    ax.add_patch(patches.Rectangle((7.6, 2.7), 0.9, 0.8, facecolor='#bfdbfe', edgecolor='#2563eb', lw=1.5))
    # Lines (road network)
    ax.plot([5.7, 9.0], [3.6, 3.6], 'k-', lw=2)
    ax.plot([7.4, 7.4], [2.2, 5.3], 'k-', lw=2)
    # Points (landmarks/stations)
    ax.plot([6.5, 8.1, 6.8], [3.0, 4.5, 4.8], 'ko', markersize=6)
    ax.text(7.35, 1.8, 'Appears as Polygons, Road Lines & Landmark Points\n(Option B: Cluster of points, lines & polygons / Option C: Polygon)', ha='center', fontweight='bold', fontsize=8.3, color='#7f1d1d')

create_figure('figures_2019_Q140', 'city_representation_1_25000_scale_map_generalization.png', draw_q140)

# Q141: Map Scale Conversion 1:50,000 (1 mm = 50 metres)
def draw_q141(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q141: Representative Fraction (RF = 1 : 50,000) Scale Calculation\n1 mm on a 1:50,000 Scale Topographic Map Represents Exactly 50 Metres on the Ground (Option C)', fontsize=11.5, fontweight='bold', pad=12)
    ax.add_patch(patches.FancyBboxPatch((0.8, 4.2), 8.4, 2.5, boxstyle='round,pad=0.2', facecolor='#eff6ff', edgecolor='#1d4ed8', lw=2.5))
    calc_txt = (
        "Step-by-Step Dimensional Derivation (RF = 1 : 50,000):\n"
        "• Ground Distance (D_g) = Map Distance (d_m) × Scale Denominator (S)\n"
        "• D_g = 1 mm × 50,000 = 50,000 mm\n"
        "• Convert millimetres to centimetres (÷ 10):  50,000 mm = 5,000 cm\n"
        "• Convert millimetres to metres (÷ 1,000):     50,000 mm = 50 metres  ★ (Option C) ★"
    )
    ax.text(5.0, 5.45, calc_txt, ha='center', va='center', fontweight='bold', fontsize=10, color='#1e3a8a')
    # Graphic scale bar
    ax.add_patch(patches.Rectangle((1.5, 2.0), 3.5, 0.4, facecolor='#1e293b', edgecolor='k'))
    ax.add_patch(patches.Rectangle((5.0, 2.0), 3.5, 0.4, facecolor='white', edgecolor='k', lw=1.5))
    ax.text(1.5, 1.5, '0 mm (0 m)', ha='center', fontweight='bold', fontsize=9.5)
    ax.text(5.0, 1.5, '1 mm Map = 50 m Ground', ha='center', fontweight='bold', fontsize=10, color='#dc2626')
    ax.text(8.5, 1.5, '2 mm Map = 100 m Ground', ha='center', fontweight='bold', fontsize=9.5)

create_figure('figures_2019_Q141', 'map_scale_1_50000_1mm_equals_50_metres.png', draw_q141)

# Q142: DBMS (Database Management System) in GIS
def draw_q142(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q142: Database Management System (DBMS) Architecture in Geoinformatics\nLinking Spatial Geometry (Vector/Raster) with Relational Attribute Tables via Unique Feature IDs (Option C)', fontsize=11, fontweight='bold', pad=12)
    # Left box: Spatial Geometry
    ax.add_patch(patches.FancyBboxPatch((0.5, 1.8), 3.6, 4.6, boxstyle='round,pad=0.15', facecolor='#dcfce7', edgecolor='#15803d', lw=2))
    ax.text(2.3, 5.9, 'SPATIAL GEOMETRY ENGINE\n(Coordinates x, y)', ha='center', fontweight='bold', fontsize=9.5, color='#14532d')
    ax.add_patch(patches.Polygon([[1.2, 4.2], [2.4, 4.5], [2.2, 3.2], [1.0, 3.4]], facecolor='#86efac', edgecolor='#166534', lw=2))
    ax.text(1.7, 3.85, 'FID = 101', fontweight='bold', fontsize=8.5, ha='center')
    ax.add_patch(patches.Polygon([[2.5, 4.3], [3.7, 4.1], [3.5, 2.6], [2.3, 2.9]], facecolor='#4ade80', edgecolor='#166534', lw=2))
    ax.text(3.0, 3.45, 'FID = 102', fontweight='bold', fontsize=8.5, ha='center')

    # Right box: RDBMS Table
    ax.add_patch(patches.FancyBboxPatch((5.3, 1.8), 4.2, 4.6, boxstyle='round,pad=0.15', facecolor='#fef2f2', edgecolor='#dc2626', lw=2.5))
    ax.text(7.4, 5.9, '★ DBMS (Option C) ★\nDatabase Management System\n(PostgreSQL/PostGIS, Oracle Spatial)', ha='center', fontweight='bold', fontsize=9.5, color='#991b1b')
    tbl = (
        "FID  | Lithology  | Fe_Grade | District\n"
        "-----+------------+----------+-----------\n"
        "101  | BHQ / BIF  |  64.5 %  | Keonjhar\n"
        "102  | Chromite   |  52.0 %  | Jajpur\n"
        "103  | Bauxite    |  48.2 %  | Koraput"
    )
    ax.text(7.4, 3.6, tbl, ha='center', va='center', family='monospace', fontsize=8.8, fontweight='bold', bbox=dict(facecolor='white', edgecolor='#dc2626'))
    ax.annotate('Relational Join\n(Primary Key FID)', xy=(5.2, 4.0), xytext=(4.2, 4.0), arrowprops=dict(arrowstyle='<->', color='#1d4ed8', lw=3), ha='center', fontweight='bold', fontsize=8.5)

create_figure('figures_2019_Q142', 'dbms_database_management_system_gis_architecture.png', draw_q142)

# Q143: Buffer Operation in GIS (Point, Line, Polygon Proximity Zones)
def draw_q143(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Q143: Proximity Analysis — Buffer Operation in GIS (Option C)\nDetermining the Area Within a Set Distance (d) Around Point, Line, or Area (Polygon) Features', fontsize=11.5, fontweight='bold', pad=12)
    # 1. Point buffer
    ax.add_patch(patches.Circle((1.8, 4.2), 1.2, facecolor='#93c5fd', edgecolor='#1d4ed8', lw=2, ls='--'))
    ax.plot(1.8, 4.2, 'ro', markersize=9)
    ax.annotate('d', xy=(3.0, 4.2), xytext=(1.8, 4.2), arrowprops=dict(arrowstyle='<->', color='#dc2626', lw=1.8))
    ax.text(1.8, 2.3, '1. Point Buffer\n(Circular Zone of Radius d\naround Borehole/Well)', ha='center', fontweight='bold', fontsize=9)
    # 2. Line buffer
    ax.plot([4.5, 5.5, 5.2], [5.4, 4.2, 3.0], color='#93c5fd', lw=36, solid_capstyle='round', alpha=0.8)
    ax.plot([4.5, 5.5, 5.2], [5.4, 4.2, 3.0], color='#1d4ed8', lw=3)
    ax.text(5.0, 2.3, '2. Line Buffer\n(Corridor of Width 2d\nalong Fault / River / Highway)', ha='center', fontweight='bold', fontsize=9)
    # 3. Polygon buffer
    ax.add_patch(patches.Polygon([[7.3, 5.5], [9.3, 5.3], [9.1, 3.0], [7.2, 3.2]], facecolor='#93c5fd', edgecolor='#1d4ed8', lw=2, ls='--'))
    ax.add_patch(patches.Polygon([[7.7, 5.0], [8.8, 4.9], [8.7, 3.5], [7.6, 3.6]], facecolor='#fca5a5', edgecolor='#dc2626', lw=2))
    ax.text(8.25, 2.3, '3. Polygon (Area) Buffer\n(Outward Setback Zone d\naround Mining Lease / Lake)', ha='center', fontweight='bold', fontsize=9)
    ax.text(5.0, 0.7, '★ Verified Application (Option C): Determining the area within a set distance from a point, line, or area feature ★', ha='center', fontweight='bold', fontsize=9.5, bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q143', 'gis_buffer_operation_point_line_polygon.png', draw_q143)

# Q144: Peter Burrough (1986) Classic Toolbox Definition of GIS
def draw_q144(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q144: Foundational Definitions of GIS — Peter A. Burrough (1986) (Option B)\n"A Powerful Set of Tools for Collecting, Storing, Retrieving, Transforming & Displaying Spatial Data"', fontsize=11, fontweight='bold', pad=12)
    steps = [
        (1.1, '1. COLLECTING\n(Data Capture:\nRS, GPS, Digitizing)', '#dbeafe', '#1d4ed8'),
        (3.05, '2. STORING\n(Spatial DBMS:\nVector & Raster)', '#dcfce7', '#15803d'),
        (5.0, '3. RETRIEVING\n(Spatial & SQL\nAttribute Queries)', '#fef3c7', '#b45309'),
        (6.95, '4. TRANSFORMING\n(Spatial Analysis,\nOverlay, Modeling)', '#f3e8ff', '#7c3aed'),
        (8.9, '5. DISPLAYING\n(Cartographic Maps,\n3D Visualization)', '#fee2e2', '#dc2626')
    ]
    for x, txt, fc, ec in steps:
        ax.add_patch(patches.FancyBboxPatch((x-0.8, 3.2), 1.6, 2.8, boxstyle='round,pad=0.12', facecolor=fc, edgecolor=ec, lw=2))
        ax.text(x, 4.6, txt, ha='center', va='center', fontweight='bold', fontsize=8.2, color='#0f172a')
    for i in range(4):
        ax.annotate('', xy=(steps[i+1][0]-0.85, 4.6), xytext=(steps[i][0]+0.85, 4.6), arrowprops=dict(arrowstyle='->', color='#334155', lw=2.5))
    ax.add_patch(patches.FancyBboxPatch((1.0, 0.8), 8.0, 1.7, boxstyle='round,pad=0.15', facecolor='#fef2f2', edgecolor='#dc2626', lw=2))
    ax.text(5.0, 1.65, '★ VERBATIM AUTHOR CITATION: Peter A. Burrough (1986) — Option (B) ★\nBook: "Principles of Geographical Information Systems for Land Resources Assessment" (Oxford Univ. Press, p. 6)', ha='center', va='center', fontweight='bold', fontsize=9.2, color='#991b1b')

create_figure('figures_2019_Q144', 'peter_burrough_1986_gis_definition_five_functions.png', draw_q144)

# Q145: Reclassification in GIS
def draw_q145(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Q145: Raster & Vector Reclassification in GIS (Option A)\nCombining One or More Input Data Ranges into New Classes to Create a New Data Layer', fontsize=11.5, fontweight='bold', pad=12)
    # Input 3x3 grid
    in_vals = [[4, 12, 28], [8, 19, 35], [3, 14, 42]]
    out_vals = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    out_cols = [['#bbf7d0', '#fef08a', '#fca5a5'] for _ in range(3)]
    ax.text(2.1, 6.2, 'Input Slope Layer (Degrees)\n(Continuous Ranges 0° - 45°)', ha='center', fontweight='bold', fontsize=9.5, color='#1e3a8a')
    ax.text(7.8, 6.2, 'New Reclassified Hazard Layer\n(1 = Low, 2 = Moderate, 3 = High)', ha='center', fontweight='bold', fontsize=9.5, color='#991b1b')
    for r in range(3):
        for c in range(3):
            x1 = 0.7 + c * 0.95
            y1 = 4.5 - r * 0.95
            ax.add_patch(patches.Rectangle((x1, y1), 0.95, 0.95, facecolor='#eff6ff', edgecolor='#1d4ed8', lw=1.5))
            ax.text(x1+0.47, y1+0.47, f'{in_vals[r][c]}°', ha='center', va='center', fontweight='bold', fontsize=10)
            x2 = 6.4 + c * 0.95
            ax.add_patch(patches.Rectangle((x2, y1), 0.95, 0.95, facecolor=out_cols[r][c], edgecolor='#dc2626', lw=1.5))
            ax.text(x2+0.47, y1+0.47, f'Class {out_vals[r][c]}', ha='center', va='center', fontweight='bold', fontsize=9.5)
    ax.annotate('RECLASSIFY\nLookup Table:\n0°-10°  -> 1\n10°-25° -> 2\n>25°    -> 3', xy=(6.2, 4.0), xytext=(4.8, 4.0),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=3), ha='center', va='center', fontweight='bold', fontsize=9, bbox=dict(facecolor='#fef3c7', edgecolor='#d97706'))
    ax.text(5.0, 1.0, '★ Option (A): Combining one or more data ranges into a new data range to create a new data layer ★', ha='center', fontweight='bold', fontsize=9.5, bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626'))

create_figure('figures_2019_Q145', 'gis_reclassification_data_ranges_new_layer.png', draw_q145)

# Q146: Point-in-Polygon Overlay in GIS
def draw_q146(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title("Q146: Vector Spatial Overlay — 'Point-in-Polygon' Operation (Option D)\nDetermining Which Point Features Lie Within the Boundary of Each Polygon", fontsize=11.5, fontweight='bold', pad=12)
    # Polygon A and Polygon B
    polyA = patches.Polygon([[1.0, 2.0], [4.8, 2.2], [4.5, 5.8], [1.2, 5.4]], facecolor='#dbeafe', edgecolor='#1d4ed8', lw=2.5)
    polyB = patches.Polygon([[4.8, 2.2], [8.8, 2.0], [8.5, 5.6], [4.5, 5.8]], facecolor='#dcfce7', edgecolor='#15803d', lw=2.5)
    ax.add_patch(polyA)
    ax.add_patch(polyB)
    ax.text(2.8, 5.1, 'Polygon A:\nGranite Formation', fontweight='bold', fontsize=10, color='#1e40af', ha='center')
    ax.text(6.8, 5.1, 'Polygon B:\nGondwana Sandstone', fontweight='bold', fontsize=10, color='#166534', ha='center')
    # Points inside A
    ptsA = [(2.0, 3.8, 'W1'), (3.2, 2.9, 'W2'), (3.8, 4.2, 'W3')]
    for x, y, lbl in ptsA:
        ax.plot(x, y, 'ro', markersize=10)
        ax.text(x+0.2, y, f'{lbl} (In Poly A)', fontweight='bold', fontsize=9, color='#991b1b')
    # Points inside B
    ptsB = [(5.8, 3.6, 'W4'), (7.4, 3.0, 'W5')]
    for x, y, lbl in ptsB:
        ax.plot(x, y, 'bo', markersize=10)
        ax.text(x+0.2, y, f'{lbl} (In Poly B)', fontweight='bold', fontsize=9, color='#1e3a8a')
    # Point outside
    ax.plot(9.2, 4.2, 'kx', markersize=10, markeredgewidth=2.5)
    ax.text(9.1, 3.6, 'W6\n(Outside)', ha='center', fontweight='bold', fontsize=8.5)
    ax.text(5.0, 0.8, '★ Verified Definition (Option D): An overlay method used to determine as to which points lie within the boundary of a polygon ★', ha='center', fontweight='bold', fontsize=9.2, bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q146', 'point_in_polygon_overlay_gis_operation.png', draw_q146)

# Q147: Raster Data Model (Matrix of Cells Organized into Rows and Columns)
def draw_q147(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Q147: Raster Data Structure in GIS (Option B)\nA Matrix of Cells (Pixels) Organized into Rows and Columns Containing Digital Information Values', fontsize=11.5, fontweight='bold', pad=12)
    vals = [
        [10, 10, 25, 25, 40],
        [10, 25, 25, 40, 40],
        [25, 25, 80, 80, 40],
        [25, 80, 80, 80, 40],
        [10, 25, 80, 40, 40]
    ]
    cmap_dict = {10: '#bbf7d0', 25: '#fef08a', 40: '#fed7aa', 80: '#fca5a5'}
    for r in range(5):
        ax.text(1.6, 5.2 - r*0.85, f'Row {r+1}', ha='right', va='center', fontweight='bold', fontsize=9, color='#334155')
        for c in range(5):
            if r == 0:
                ax.text(2.3 + c*0.95, 5.85, f'Col {c+1}', ha='center', fontweight='bold', fontsize=9, color='#334155')
            x = 1.8 + c*0.95
            y = 4.8 - r*0.85
            v = vals[r][c]
            ax.add_patch(patches.Rectangle((x, y), 0.95, 0.85, facecolor=cmap_dict[v], edgecolor='#1e293b', lw=1.5))
            ax.text(x+0.475, y+0.425, str(v), ha='center', va='center', fontweight='bold', fontsize=10)
    ax.annotate('Single Grid Cell / Pixel (Row r, Col c)\nStores Digital Number (DN) or Attribute Code', xy=(4.15, 3.5), xytext=(6.8, 4.2),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#fee2e2', edgecolor='#dc2626'), fontsize=9.5, fontweight='bold')
    ax.text(5.0, 0.6, '★ Option (B) RASTER: Matrix of cells organized into rows and columns, each containing a value representing information ★', ha='center', fontweight='bold', fontsize=9.2, bbox=dict(facecolor='#dbeafe', edgecolor='#1d4ed8'))

create_figure('figures_2019_Q147', 'raster_matrix_rows_columns_cell_values.png', draw_q147)

# Q148: Map Projection Families (Cylindrical, Conic, Azimuthal) vs Geographic Coordinate System
def draw_q148(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Q148: Developable Map Projection Families vs. Unprojected Geographic Coordinates\nCylindrical, Conic & Azimuthal Are Map Projections; "Geographic" (Lat/Lon) Is NOT a Projection (Option D)', fontsize=11, fontweight='bold', pad=12)
    cards = [
        (0.4, '1. CYLINDRICAL\nPROJECTION (Option A)\n\n• Cylinder tangent/secant\n  at Equator (Mercator, UTM)\n• Parallels & meridians form\n  orthogonal straight grid', '#dbeafe', '#1d4ed8'),
        (2.8, '2. CONIC\nPROJECTION (Option B)\n\n• Cone tangent/secant at\n  Mid-Latitudes (Lambert\n  Conformal, Albers)\n• Fan-shaped graticule', '#dcfce7', '#15803d'),
        (5.2, '3. AZIMUTHAL / PLANAR\nPROJECTION (Option C)\n\n• Flat plane tangent at\n  Pole (Stereographic,\n  Orthographic, Gnomonic)\n• Radial meridians', '#f3e8ff', '#7c3aed'),
        (7.6, '★ 4. GEOGRAPHIC ★\n(Option D — NOT A PROJECTION)\n\n• 3D Spherical/Ellipsoidal\n  Coordinate System (GCS)\n• Angular Latitude (phi)\n  & Longitude (lambda) in deg!', '#fee2e2', '#dc2626')
    ]
    for x, txt, fc, ec in cards:
        ax.add_patch(patches.FancyBboxPatch((x, 1.3), 2.1, 5.0, boxstyle='round,pad=0.12', facecolor=fc, edgecolor=ec, lw=2))
        ax.text(x+1.05, 3.8, txt, ha='center', va='center', fontweight='bold', fontsize=8.3, color='#0f172a')

create_figure('figures_2019_Q148', 'map_projection_types_vs_geographic_coordinate_system.png', draw_q148)

# Q149: Cartographic Modeling (Tomlin's Map Algebra & Spatial Operation Flowchart)
def draw_q149(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Q149: Cartographic Modeling & Map Algebra in GIS (C. Dana Tomlin, 1990) (Option B)\nExpressing and Organizing Spatial Operations in a Logical Flowchart to Develop a GIS Model', fontsize=11, fontweight='bold', pad=12)
    # Input maps on left
    inputs = [(0.5, 5.5, 'DEM Layer\n(Elevation)'), (0.5, 3.5, 'Fault Line\nVector Layer'), (0.5, 1.5, 'Lithology\nPolygon Layer')]
    for x, y, txt in inputs:
        ax.add_patch(patches.FancyBboxPatch((x, y), 2.0, 1.1, boxstyle='round,pad=0.1', facecolor='#dbeafe', edgecolor='#1d4ed8', lw=2))
        ax.text(x+1.0, y+0.55, txt, ha='center', va='center', fontweight='bold', fontsize=8.8)
    # Spatial operations in middle
    ops = [(3.7, 5.5, 'Focal Function:\nCalculate Slope'), (3.7, 3.5, 'Zonal / Distance:\nBuffer 500 m'), (3.7, 1.5, 'Local Function:\nReclassify Weights')]
    for (ix, iy, _), (ox, oy, otxt) in zip(inputs, ops):
        ax.add_patch(patches.FancyBboxPatch((ox, oy), 2.3, 1.1, boxstyle='round,pad=0.1', facecolor='#fef3c7', edgecolor='#d97706', lw=2))
        ax.text(ox+1.15, oy+0.55, otxt, ha='center', va='center', fontweight='bold', fontsize=8.5)
        ax.annotate('', xy=(ox, oy+0.55), xytext=(ix+2.0, iy+0.55), arrowprops=dict(arrowstyle='->', color='#334155', lw=2))
        ax.annotate('', xy=(7.1, 4.05), xytext=(ox+2.3, oy+0.55), arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.2))
    # Output model on right
    ax.add_patch(patches.FancyBboxPatch((7.1, 2.8), 2.5, 2.5, boxstyle='round,pad=0.15', facecolor='#fee2e2', edgecolor='#dc2626', lw=2.5))
    ax.text(8.35, 4.05, '★ CARTOGRAPHIC\nMODEL OUTPUT ★\n\nWeighted Overlay:\nLandslide Susceptibility\nZonation Map', ha='center', va='center', fontweight='bold', fontsize=9, color='#991b1b')
    ax.text(5.0, 0.5, '★ Option (B): A way of expressing and organizing methods by which spatial operations are selected and used to develop a GIS model ★', ha='center', fontweight='bold', fontsize=8.8, bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q149', 'cartographic_modeling_spatial_operations_flowchart.png', draw_q149)

# Q150: The GIS Data Stream (Raw Spatial Data -> Integrated GIS Database)
def draw_q150(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Q150: The GIS "Data Stream" Pipeline (Heywood, Cornelius & Carver) (Option A)\nThe Process by Which Raw Spatial Data Is Processed into a Clean, Integrated GIS Database', fontsize=11.5, fontweight='bold', pad=12)
    stages = [
        (0.4, '1. RAW SPATIAL\nDATA INPUT\n\n• Paper Maps\n• Satellite Images\n• GPS Field Logs\n• Tabular Surveys', '#e2e8f0', '#475569'),
        (2.4, '2. DATA CAPTURE\n& DIGITIZING\n\n• Scanning\n• Vectorizing\n• Format Import', '#dbeafe', '#1d4ed8'),
        (4.4, '3. EDITING &\nERROR CLEANING\n\n• Fix Overshoots\n• Close Slivers\n• Edge-Matching', '#fef3c7', '#d97706'),
        (6.4, '4. TOPOLOGY &\nPROJECTION\n\n• Build Topology\n• Datum Shift\n• Re-projecting', '#dcfce7', '#15803d'),
        (8.3, '★ 5. INTEGRATED\nGIS DATABASE ★\n\n• Seamless Ready\n  Geodatabase\n  (Option A)', '#fee2e2', '#dc2626')
    ]
    for x, txt, fc, ec in stages:
        ax.add_patch(patches.FancyBboxPatch((x, 2.0), 1.55, 3.8, boxstyle='round,pad=0.12', facecolor=fc, edgecolor=ec, lw=2))
        ax.text(x+0.775, 3.9, txt, ha='center', va='center', fontweight='bold', fontsize=8.0, color='#0f172a')
    for i in range(4):
        ax.annotate('', xy=(stages[i+1][0], 3.9), xytext=(stages[i][0]+1.55, 3.9), arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.5))
    ax.text(5.0, 0.8, '★ Verified Definition (Option A): The process by which raw spatial data is processed into an integrated GIS database ★', ha='center', fontweight='bold', fontsize=9.3, bbox=dict(facecolor='#fef08a', edgecolor='#ca8a04'))

create_figure('figures_2019_Q150', 'gis_data_stream_raw_spatial_data_to_integrated_database.png', draw_q150)
print("ALL 30 FIGURES (Q121 - Q150) GENERATED SUCCESSFULLY!")
