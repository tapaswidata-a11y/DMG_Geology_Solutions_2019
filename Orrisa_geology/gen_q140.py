#!/usr/bin/env python3
"""
Q140 Generator: Spatial Resolution Capabilities of Active Sensors: SAR and LiDAR
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q140():
    title = r"Q140: Remote Sensing: SAR & LiDAR High Spatial Resolution | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Remote Sensing, Radar & LiDAR"
    h1_title = "Q140: Spatial Resolution of Active Sensors: Dispelling the Fallacy of Coarse SAR and LiDAR"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 140<br>
<strong>Authoritative References:</strong> Thomas M. Lillesand, Ralph W. Kiefer, and Jonathan W. Chipman, <em>Remote Sensing and Image Interpretation</em> (7th Ed., Wiley, Ch. 6: Microwave, Radar, and LiDAR Sensing, pp. 280–345); Floyd F. Sabins, <em>Remote Sensing: Principles and Interpretation</em> (3rd Ed., W.H. Freeman); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11, p. 225); George Joseph and C. Jeganathan, <em>Fundamentals of Remote Sensing</em>."""

    part1 = r"""
  <!-- CARD 1: WORKING PRINCIPLES OF ACTIVE SENSORS -->
  <div class="card">
    <div class="card-header bg-blue">1. Principles of Active Microwave and Optical Sensors: SAR and LiDAR</div>
    <div class="card-body">
      <p>
        In modern remote sensing and geoinformatics, <strong>Synthetic Aperture Radar (SAR)</strong> and <strong>Light Detection and Ranging (LiDAR)</strong> represent the pinnacle of <strong>active high-resolution spatial imaging technologies</strong> (Lillesand et al., 2015; Sabins, 1997; Bangar, p. 225).
      </p>
      <p>
        The assertion that <em>"SAR and LiDAR data have a resolution varying from 100-150 m"</em> is <strong>categorically and factually FALSE</strong>. Modern airborne and spaceborne SAR and LiDAR systems operate at <strong>sub-meter to decimeter spatial resolutions</strong> (e.g., $0.1\text{ to } 3.0\text{ meters}$), providing unprecedented detail for structural geology, fault creep monitoring, terrain elevation, and mining topography.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q140/sar_lidar_high_spatial_resolution_capabilities.png" alt="SAR and LiDAR High Spatial Resolution Capabilities">
        <div class="figure-caption">
          <strong>Figure 140.1 — Spatial Resolution Spectrum of Active Sensors:</strong> Illustrates the true high-resolution performance: Spaceborne SAR (TerraSAR-X Spotlight mode at $0.24\text{ m}$ to $1.0\text{ m}$, Sentinel-1 at $5\text{ m}$) and Airborne LiDAR point clouds ($5\text{ to } 50\text{ points/m}^2$, generating $0.1\text{ to } 1.0\text{ m}$ DEM grids). Contrast with the erroneous exam claim of coarse $100\text{--}150\text{ m}$ resolution.
        </div>
      </div>

      <h4>Why SAR Achieves Ultra-High Spatial Resolution</h4>
      <p>
        In conventional real-aperture radar (RAR), angular beamwidth is inversely proportional to physical antenna length ($\beta \approx \lambda / L_a$), requiring impractically massive antennas kilometers long to achieve fine resolution from space. Synthetic Aperture Radar (SAR) overcomes this physical barrier through signal processing:
      </p>
      <ul>
        <li><strong>Aperture Synthesis:</strong> As the aircraft or spacecraft travels along its flight path, the radar transmits thousands of microwave pulses and records both the amplitude and Doppler phase shift of the returned backscatter. By mathematically synthesizing these returns across the flight trajectory, a virtual synthetic antenna kilometers in length is created.</li>
        <li><strong>Azimuth Resolution ($R_a$):</strong> The theoretical along-track resolution of a focused SAR is <em>completely independent of sensor altitude or platform range ($R$)</em>! It depends solely on half the physical antenna length:
          <div class="math-block">
            $$R_a = \frac{L_a}{2}$$
          </div>
          For an antenna of physical length $L_a = 2.0\text{ m}$, the theoretical azimuth resolution is <strong>$1.0\text{ meter}$</strong>, whether orbiting at $300\text{ km}$ or $800\text{ km}$ altitude!
        </li>
        <li><strong>Range Resolution ($R_r$):</strong> Governed by the bandwidth ($B$) of the frequency-modulated transmitted chirp pulse:
          <div class="math-block">
            $$R_r = \frac{c}{2 B}, \quad R_{\text{ground}} = \frac{c}{2 B \sin\theta}$$
          </div>
          Modern SAR sensors with bandwidths $B = 150 - 300\text{ MHz}$ deliver ground-range resolutions of <strong>$0.5\text{ to } 1.0\text{ meter}$</strong>.
        </li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q140/bangar_p225_sar_lidar_spatial_resolution.png" alt="SAR and LiDAR Resolution from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 140.2 — Active Sensor Resolutions in Engineering Geology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 225). Disproves the claim of coarse 100–150 m resolution and confirms the sub-meter precision of modern SAR and LiDAR.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: LIDAR HIGH-DENSITY SPATIAL PERFORMANCE -->
  <div class="card">
    <div class="card-header bg-emerald">2. LiDAR: Decimeter and Millimeter Spatial Resolution Architecture</div>
    <div class="card-body">
      <h4>How LiDAR Operates</h4>
      <p>
        LiDAR (Light Detection and Ranging) utilizes laser pulses in the near-infrared ($1064\text{ nm}$) or green ($532\text{ nm}$) wavelengths emitted at ultra-high repetition frequencies (up to $500\text{ to } 1000\text{ kHz}$):
      </p>
      <ul>
        <li><strong>Time-of-Flight Ranging:</strong> The round-trip travel time ($\Delta t$) of each laser pulse is measured with picosecond precision:
          <div class="math-block">
            $$R = \frac{c \cdot \Delta t}{2}$$
          </div>
        </li>
        <li><strong>Point Cloud Density:</strong> Airborne LiDAR systems flying at $500\text{--}1500\text{ m}$ produce point densities of <strong>$5\text{ to } 50+\text{ laser returns per square meter}$</strong>.</li>
        <li><strong>Derived DEM Resolution:</strong> Interpolating this dense 3D point cloud yields bare-earth Digital Elevation Models (DEMs) with horizontal grid cell resolutions of <strong>$0.25\text{ to } 1.0\text{ meter}$</strong> and vertical accuracies within <strong>$5\text{ to } 15\text{ centimeters}$</strong>!</li>
        <li><strong>Terrestrial Laser Scanning (TLS):</strong> Ground-based tripod LiDAR instruments map quarry faces and tunnel linings with <strong>millimeter-level resolution ($1 - 5\text{ mm}$)</strong>.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: REAL-WORLD OPERATIONAL SATELLITE CAPABILITIES -->
  <div class="card">
    <div class="card-header bg-indigo">3. Real-World Sensor Capabilities: The True Resolution Table</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Sensor System</th>
            <th>Type</th>
            <th>Operating Band / Wavelength</th>
            <th>Actual Operational Spatial Resolution</th>
            <th>Typical Geological Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>TerraSAR-X / TanDEM-X</strong></td>
            <td>Spaceborne SAR</td>
            <td>X-band ($\lambda = 3.1\text{ cm}$)</td>
            <td><strong>$0.24\text{ m}$ (Staring Spotlight) to $3.0\text{ m}$ (Stripmap)</strong></td>
            <td>Millimeter-scale tectonic fault slip, volcanic caldera deformation, mining subsidence.</td>
          </tr>
          <tr>
            <td><strong>COSMO-SkyMed</strong></td>
            <td>Spaceborne SAR</td>
            <td>X-band ($\lambda = 3.1\text{ cm}$)</td>
            <td><strong>$1.0\text{ m}$ (Spotlight) to $3.0\text{ m}$ (HIMAGE)</strong></td>
            <td>Rapid disaster mapping, slope landslide monitoring, open-cast wall stability.</td>
          </tr>
          <tr>
            <td><strong>Sentinel-1 (ESA)</strong></td>
            <td>Spaceborne SAR</td>
            <td>C-band ($\lambda = 5.6\text{ cm}$)</td>
            <td><strong>$5\text{ m} \times 20\text{ m}$ (IW Mode) to $5\text{ m} \times 5\text{ m}$ (SM)</strong></td>
            <td>Global tectonic strain mapping, aquifer compaction subsidence, coastal erosion.</td>
          </tr>
          <tr>
            <td><strong>ALOS-2 PALSAR-2</strong></td>
            <td>Spaceborne SAR</td>
            <td>L-band ($\lambda = 23.6\text{ cm}$)</td>
            <td><strong>$1.0\text{ m} \times 3.0\text{ m}$ (Spotlight) to $3.0\text{ m}$ (Ultra-Fine)</strong></td>
            <td>Penetration through dense forest canopies for geological mapping.</td>
          </tr>
          <tr>
            <td><strong>Airborne Airborne LiDAR</strong></td>
            <td>Airborne Laser</td>
            <td>NIR ($\lambda = 1064\text{ nm}$)</td>
            <td><strong>$0.1\text{ m} \text{ to } 0.5\text{ m}$ (Point density $10 - 50\text{ pts/m}^2$)</strong></td>
            <td>Micro-topography, hidden fault scarp identification beneath dense vegetation.</td>
          </tr>
          <tr>
            <td><strong>Terrestrial LiDAR (TLS)</strong></td>
            <td>Ground Laser</td>
            <td>NIR / Green</td>
            <td><strong>$1\text{ mm} \text{ to } 5\text{ mm}$</strong></td>
            <td>Open-pit bench face discontinuity surveying, tunnel convergence monitoring.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 140</div>
      <div class="question-text">
        SAR and LiDAR data have a resolution varying from 100-150 m.
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> True</li>
        <li class="option-item correct"><strong>(B)</strong> False</li>
        <li class="option-item"><strong>(C)</strong> Both True</li>
        <li class="option-item"><strong>(D)</strong> Both False</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (B) False</strong> — The statement is completely false. Modern Synthetic Aperture Radar (SAR) achieves spatial resolutions of $0.25\text{ to } 10\text{ meters}$, while LiDAR delivers point cloud resolutions of $0.1\text{ to } 1.0\text{ meters}$ (and terrestrial LiDAR down to millimeters), far superior to the coarse $100\text{--}150\text{ m}$ figure claimed.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): True — Factually and Technically Incorrect</div>
        <p>
          Affirming that SAR and LiDAR have resolutions of $100 - 150\text{ m}$ ignores over four decades of active sensor advancements. A resolution of $100 - 150\text{ m}$ is characteristic of very coarse passive optical scanners or historical spaceborne scatterometers. Both SAR and LiDAR were developed specifically to achieve high-resolution, all-weather, day-and-night imaging at the meter and sub-meter scale.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (B): False — Fully Verified & Factually Correct</div>
        <p>
          The statement is unequivocally <strong>False</strong> (Bangar, p. 225; Lillesand et al., Ch. 6):
        </p>
        <ol>
          <li>Spaceborne commercial SAR systems (TerraSAR-X, COSMO-SkyMed, RadarSat-2) routinely provide spatial resolutions of <strong>$0.25\text{ to } 3.0\text{ meters}$</strong>.</li>
          <li>Airborne LiDAR routinely operates with laser pulse footprints yielding bare-earth digital elevation models with grid cell resolutions of <strong>$0.25\text{ to } 1.0\text{ meter}$</strong>.</li>
          <li>Terrestrial LiDAR scanners (TLS) achieve <strong>millimeter-scale resolution ($1 - 5\text{ mm}$)</strong>.</li>
        </ol>
        <p>Because the actual operational resolution is two to three orders of magnitude finer than $100 - 150\text{ m}$, the statement is False.</p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C) & (D): Both True / Both False — Structurally Invalid Distractors</div>
        <p>
          In a binary proposition, an assertion is either logically True or False. Options (C) and (D) are nonsensical grammatical distractors inserted into the examination paper to catch careless guessing.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Active vs. Passive Remote Sensing Systems: Resolution and Operational Comparison</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Sensor Technology</th>
            <th>Energy Source</th>
            <th>Typical Spatial Resolution</th>
            <th>All-Weather / Day-Night Capability</th>
            <th>Primary Terrain Surface Interaction</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Synthetic Aperture Radar (SAR)</strong></td>
            <td>Active (Coherent microwave transmitter)</td>
            <td><strong>$0.25\text{ m} \text{ to } 10.0\text{ m}$</strong></td>
            <td><strong>Yes</strong> (Penetrates clouds, rain, fog, and darkness)</td>
            <td>Surface roughness, dielectric constant, moisture content, geometry.</td>
          </tr>
          <tr>
            <td><strong>Airborne LiDAR</strong></td>
            <td>Active (Pulsed laser diode)</td>
            <td><strong>$0.1\text{ m} \text{ to } 1.0\text{ m}$</strong></td>
            <td>Day and Night; cannot penetrate dense clouds/fog</td>
            <td>Direct optical reflection; multi-return pulses penetrate tree canopy gaps to hit bare earth.</td>
          </tr>
          <tr>
            <td><strong>Optical Satellite (WorldView-3)</strong></td>
            <td>Passive (Reflected sunlight)</td>
            <td>$0.31\text{ m}$ (Pan) / $1.24\text{ m}$ (MS)</td>
            <td>Daylight only; completely blocked by clouds</td>
            <td>Solar reflectance governed by electronic/vibrational mineral bonds.</td>
          </tr>
          <tr>
            <td><strong>Thermal Infrared (TIR)</strong></td>
            <td>Passive (Emitted terrestrial thermal radiation)</td>
            <td>$60\text{ m} \text{ to } 100\text{ m}$</td>
            <td>Day and Night; blocked by clouds</td>
            <td>Thermal inertia, kinetic surface temperature, silica quartz emissivity.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD: 8 PRACTICE PROBLEMS WITH FULL STEP-BY-STEP DERIVATIONS -->
  <div class="card">
    <div class="card-header bg-purple">8 Advanced Practice Problems & Fully Worked Solutions</div>
    <div class="card-body">
      <!-- PROBLEM 1 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 1: Theoretical SAR Azimuth Resolution Calculation</strong><br>
        A spaceborne Synthetic Aperture Radar operates in a polar orbit at an altitude of $H = 600\text{ km}$. The satellite carries a planar phased-array radar antenna with physical length $L_a = 4.8\text{ meters}$. Calculate the theoretical along-track azimuth resolution ($R_a$) of the fully focused SAR image.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Use the fundamental SAR azimuth resolution theorem:
          $$R_a = \frac{L_a}{2}$$
          2. Substitute $L_a = 4.8\text{ m}$:
          $$R_a = \frac{4.8\text{ m}}{2} = 2.40\text{ meters}$$
          <em>Key Geophysical Insight:</em> Despite orbiting at an enormous altitude of $600\text{ km}$, the SAR delivers a sharp $2.4\text{ m}$ azimuth resolution, proving that resolution is independent of range to the target.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: SAR Slant Range and Ground Range Resolution</strong><br>
        A spaceborne radar transmits a chirped microwave pulse with a frequency bandwidth of $B = 150.0\text{ MHz}$ ($1.5 \times 10^8\text{ Hz}$). The radar look angle to an open-pit mine is $\theta = 35.0^\circ$. Taking the speed of light $c = 3.0 \times 10^8\text{ m/s}$, calculate: (a) the slant range resolution ($R_r$), and (b) the projected ground range resolution ($R_{\text{ground}}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Slant range resolution $R_r$:
          $$R_r = \frac{c}{2 B} = \frac{3.0 \times 10^8\text{ m/s}}{2 \times (1.5 \times 10^8\text{ s}^{-1})} = \frac{3.0 \times 10^8}{3.0 \times 10^8} = 1.00\text{ meter}$$
          2. Ground range resolution $R_{\text{ground}}$:
          $$R_{\text{ground}} = \frac{R_r}{\sin\theta} = \frac{1.00\text{ m}}{\sin(35.0^\circ)} = \frac{1.00}{0.57358} \approx 1.74\text{ meters}$$
          Both range ($1.74\text{ m}$) and azimuth ($2.4\text{ m}$) resolutions are near $1\text{--}2\text{ meters}$, completely disproving the $100 - 150\text{ m}$ claim.
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: LiDAR Laser Footprint Diameter on Ground</strong><br>
        An airborne topographic LiDAR system is flown at an altitude $H = 1000\text{ m}$ above the ground. The laser beam divergence angle is $\gamma = 0.30\text{ milliradians}$ ($0.00030\text{ rad}$). Calculate the diameter ($D_{\text{spot}}$) of the circular illuminated laser footprint on the terrain surface.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Footprint diameter for small divergence angles:
          $$D_{\text{spot}} \approx H \times \gamma = 1000\text{ m} \times 0.00030\text{ rad} = 0.30\text{ meters} = 30.0\text{ cm}$$
          The individual laser footprint on the ground is a compact circle just $30\text{ cm}$ in diameter.
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: LiDAR Point Density to Grid Resolution Conversion</strong><br>
        An airborne LiDAR survey over a forested landslide zone achieves a mean bare-earth ground point density of $\rho_{\text{pts}} = 16.0\text{ points/m}^2$. Calculate: (a) the average point spacing ($s = 1 / \sqrt{\rho}$), and (b) the recommended Digital Elevation Model (DEM) grid cell resolution that can be reliably supported without interpolation voids.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Average point spacing:
          $$s = \frac{1}{\sqrt{\rho_{\text{pts}}}} = \frac{1}{\sqrt{16.0}} = \frac{1}{4.0} = 0.25\text{ meters} = 25.0\text{ cm}$$
          2. Supported DEM grid cell size:
          According to ASPRS standards, a cell size equal to or slightly larger than average spacing ($1 - 2\times$) is supported:
          $$\text{DEM Grid Resolution} = 0.50\text{ meters (50 cm)}$$
          (A half-meter grid is $200\times$ to $300\times$ finer than $100 - 150\text{ m}$).
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Time-of-Flight Ranging Precision in LiDAR</strong><br>
        A high-precision timing discriminator in a LiDAR receiver measures the round-trip laser pulse travel time with an electronic time measurement precision of $\delta t = 0.20\text{ nanoseconds}$ ($0.20 \times 10^{-9}\text{ s}$). Taking the velocity of light $c = 3.0 \times 10^8\text{ m/s}$, calculate the theoretical range measurement precision ($\delta R$) in centimeters.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Range formula: $R = \frac{c \cdot t}{2}$.
          2. Range precision:
          $$\delta R = \frac{c \cdot \delta t}{2} = \frac{(3.0 \times 10^8\text{ m/s}) \times (0.20 \times 10^{-9}\text{ s})}{2} = \frac{0.060\text{ m}}{2} = 0.030\text{ m} = 3.0\text{ cm}$$
          The LiDAR system measures distances with an accuracy of $\pm 3.0\text{ cm}$.
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Microwave Radar Frequency Bands and Wavelengths</strong><br>
        A geologist chooses between three spaceborne SAR satellite systems for mapping a tropical rainforest:
        (A) TerraSAR-X: Frequency $f_X = 9.65\text{ GHz}$;
        (B) Sentinel-1: Frequency $f_C = 5.405\text{ GHz}$;
        (C) ALOS-2: Frequency $f_L = 1.27\text{ GHz}$.
        Calculate the wavelength ($\lambda = c / f$) for each sensor and identify which system provides the best canopy penetration to image underlying bedrock faults.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Wavelength calculations ($c = 3.0 \times 10^8\text{ m/s}$):
          $$\lambda_X = \frac{3.0 \times 10^8}{9.65 \times 10^9} = 0.0311\text{ m} = 3.11\text{ cm (X-band)}$$
          $$\lambda_C = \frac{3.0 \times 10^8}{5.405 \times 10^9} = 0.0555\text{ m} = 5.55\text{ cm (C-band)}$$
          $$\lambda_L = \frac{3.0 \times 10^8}{1.27 \times 10^9} = 0.2362\text{ m} = 23.62\text{ cm (L-band)}$$
          2. Canopy Penetration:
          Microwave penetration depth increases with longer wavelengths. The $23.6\text{ cm}$ L-band waves of ALOS-2 penetrate through leaves and small branches, scattering directly off tree trunks and the ground surface to reveal bedrock structures hidden under dense jungle.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: InSAR Phase Sensitivity to Millimetric Surface Displacement</strong><br>
        In Synthetic Aperture Radar Interferometry (InSAR), the sensor uses TerraSAR-X ($\lambda = 31.0\text{ mm}$). Ground displacement along the radar line-of-sight ($\Delta r$) is related to interferometric phase change ($\Delta \phi$) by:
        $$\Delta \phi = \frac{4\pi}{\lambda} \Delta r$$
        If a subsidence bowl produces an interferometric phase shift of one full fringe ($\Delta \phi = 2\pi\text{ radians}$), calculate the exact ground displacement ($\Delta r$) in millimeters.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Rearrange for line-of-sight displacement $\Delta r$:
          $$\Delta r = \frac{\Delta \phi \cdot \lambda}{4\pi} = \frac{2\pi \cdot \lambda}{4\pi} = \frac{\lambda}{2}$$
          2. Substitute $\lambda = 31.0\text{ mm}$:
          $$\Delta r = \frac{31.0\text{ mm}}{2} = 15.5\text{ mm}$$
          One complete InSAR fringe corresponds to exactly $15.5\text{ millimeters}$ of ground motion, demonstrating extraordinary sub-centimeter sensitivity.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: ScanSAR Coarse Mode vs. High-Resolution Spotlight Mode</strong><br>
        A synthetic aperture radar satellite operates in multiple imaging modes:
        - Mode 1 (Staring Spotlight): Swath width $W_1 = 10\text{ km}$, spatial resolution $R_1 = 0.5\text{ m}$.
        - Mode 2 (ScanSAR Wide): Swath width $W_2 = 400\text{ km}$, spatial resolution $R_2 = 100\text{ m}$.
        Explain the physical trade-off between swath width and spatial resolution, and explain how candidates can be confused by the exam statement.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Physical Trade-Off:
          In radar imaging, there is a fundamental inverse relationship between the time the beam dwells on an individual ground target (dwell time) and the total swath width covered.
          - In Spotlight mode, the antenna is steerable and stares continuously at a small $10\text{ km}$ footprint as the satellite passes overhead, synthesizing a massive synthetic aperture that delivers an ultra-sharp $0.5\text{ m}$ resolution.
          - In ScanSAR mode, the radar beam rapidly scans across multiple sub-swaths to image an enormous $400\text{ km}$ territory in a single pass; dwell time per burst is tiny, degrading resolution to $100\text{ m}$.
          2. Exam Clarification: While coarse ScanSAR modes can exhibit $100\text{ m}$ resolution for oceanographic maritime monitoring, the definitive core capability of SAR is high-resolution ($0.25 - 5\text{ m}$) imaging, and LiDAR <em>never</em> operates at $100 - 150\text{ m}$. Stating that "SAR and LiDAR data have a resolution varying from 100-150 m" is categorically False.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=140,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q140_SAR_and_LiDAR_Spatial_Resolution_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q140: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q140()
