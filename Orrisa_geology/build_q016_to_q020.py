#!/usr/bin/env python3
"""
Masterclass Builder for Batch 2: Remote Sensing & Photogrammetry (Q016 - Q020)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q016: Radar: Real vs Synthetic Aperture Radar
# ==============================================================================
def generate_q016():
    title = "Q016: Radar Resolution Mechanics: Real Aperture (RAR) vs. Synthetic Aperture (SAR) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Microwave Remote Sensing & Radar"
    h1_title = "Q016: Radar Resolution Mechanics: Real Aperture (RAR) vs. Synthetic Aperture (SAR)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 16<br>
<strong>Authoritative References:</strong> Floyd F. Sabins, <em>Remote Sensing: Principles and Interpretation</em> (3rd Ed., Ch. 6: Radar Imagery, pp. 177–205); Thomas M. Lillesand et al., <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 7, pp. 415–435); Curlander, J.C. & McDonough, R.N., <em>Synthetic Aperture Radar: Systems and Signal Processing</em> (Wiley)."""

    part1 = r"""
  <!-- CARD 1: RADAR GEOMETRY & RESOLUTION MECHANICS -->
  <div class="card">
    <div class="card-header bg-blue">1. Radar Imaging Geometry: Range vs. Azimuth Resolution</div>
    <div class="card-body">
      <p>Active side-looking radar systems (SLAR) image terrain by transmitting coherent microwave pulses ($\lambda = 1 - 100\text{ cm}$) and measuring the time delay, amplitude, and phase of the backscattered echo. In radar geometry, spatial resolution is fundamentally decoupled into two orthogonal directions:</p>

      <ul>
        <li><strong>Range (Cross-Track) Resolution ($R_r$):</strong> Governed by the transmitted pulse duration ($\tau$) or pulse bandwidth ($B$):
        $$R_r = \frac{c \cdot \tau}{2 \sin \theta} = \frac{c}{2 B \sin \theta}$$
        Where $c$ is the speed of light and $\theta$ is the incidence angle. Range resolution is improved simply by shortening pulse width via frequency modulation (chirp compression).</li>
        <li><strong>Azimuth (Along-Track) Resolution ($R_a$):</strong> Controlled by the physical beamwidth ($\beta$) of the radar antenna in the direction of flight. The antenna beamwidth in radians is:
        $$\beta = \frac{\lambda}{L_a}$$
        Where $\lambda$ is radar wavelength and $L_a$ is the physical length of the antenna.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q16/radar_real_vs_synthetic_aperture.png" alt="Real Aperture vs Synthetic Aperture Radar Geometry">
        <div class="tb-caption">
          <strong>Figure 16.1: Real Aperture (RAR) vs. Synthetic Aperture (SAR) Resolution.</strong> In RAR, azimuth resolution degrades proportionally with slant range ($R_a = \beta R$). In SAR, coherent Doppler processing synthesizes an antenna kilometers long, achieving range-independent azimuth resolution equal to half the antenna length ($R_a = L_a/2$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE PHYSICAL SIZE OF THE ANTENNA IN RAR VS SAR -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Crucial Difference: Physical Antenna Size ($L_a$)</div>
    <div class="card-body">
      <p>The monumental distinction between Real Aperture Radar (RAR) and Synthetic Aperture Radar (SAR) lies in the <strong>size, design, and physical requirements of the antenna</strong>:</p>

      <ul>
        <li><strong>Real Aperture Radar (RAR / Non-Coherent SLAR):</strong> The azimuth resolution equals the physical ground footprint of the radar beam at slant range ($R$):
        $$R_{a,\text{RAR}} = \beta \cdot R = \frac{\lambda \cdot R}{L_a}$$
        Notice that $R_a$ degrades directly with increasing range ($R$) and is inversely proportional to physical antenna length ($L_a$). At spacecraft altitudes ($R = 800\text{ km}$) using C-band ($\lambda = 5.6\text{ cm}$), achieving a modest $10\text{ m}$ azimuth resolution would require an impossible physical antenna length of:
        $$L_a = \frac{\lambda \cdot R}{R_a} = \frac{0.056\text{ m} \times 800,000\text{ m}}{10\text{ m}} = 4,480\text{ meters } (4.5\text{ km!})$$
        No spacecraft can deploy a 4.5-kilometer rigid antenna. RAR is therefore physically restricted to low-altitude aircraft.</li>
        <li><strong>Synthetic Aperture Radar (SAR - Carl Wiley, 1951):</strong> Instead of relying on a giant physical antenna, SAR transmits pulses continuously as the platform flies forward. Because the radar is coherent, it records both the amplitude and <em>Doppler phase history</em> of returned echoes. Signal processing synthesizes an effective aperture length equal to the distance the satellite travels while illuminating a ground target ($L_{\text{syn}} = \frac{\lambda R}{L_a}$).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">The Fundamental SAR Azimuth Resolution Equation</div>
        $$R_{a,\text{SAR}} = \frac{\lambda \cdot R}{2 L_{\text{syn}}} = \frac{\lambda \cdot R}{2 \left(\frac{\lambda R}{L_a}\right)} = \frac{L_a}{2}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">In SAR, azimuth resolution is completely <strong>independent of platform altitude ($R$) and wavelength ($\lambda$)</strong>, and is strictly equal to <strong>half the physical antenna length ($L_a / 2$)</strong>! Counter-intuitively, a smaller physical antenna yields a broader beam, creating a longer synthesized aperture and yielding finer spatial resolution.</p>
      </div>

      <div class="quote-box">
        "The major difference between real aperture radar and synthetic aperture radar is the size of the antenna. Real aperture systems require long physical antennas to produce narrow beams. Synthetic aperture systems use a relatively small physical antenna and synthesize a much longer antenna electronically through signal processing."
        <span class="quote-ref">— Floyd F. Sabins, <em>Remote Sensing: Principles and Interpretation</em> (3rd Ed., 1997, p. 182)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Energy Source and Recording Distractors</div>
    <div class="card-body">
      <p>Candidates must clearly refute the other answer choices:</p>
      <ul>
        <li><strong>Source of Energy:</strong> Both RAR and SAR are <em>active microwave sensors</em> that generate their own illumination using onboard high-power transmitters (magnetrons, klystrons, or solid-state T/R modules). Their energy source is identical.</li>
        <li><strong>Recording of Data:</strong> While SAR requires digital phase history storage and complex 2D Fourier range-Doppler focusing algorithms, the primary technological limitation that led to SAR invention was overcome strictly by revolutionizing the <strong>effective antenna size</strong>.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 16)</div>
    <div class="q-stmt">
      Q16. Major difference between Real Aperture Radar and Synthetic Aperture Radar is in their :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Size of the Antenna &nbsp;✔</div>
      <div class="raw-opt">(B) Source of energy</div>
      <div class="raw-opt">(C) Recording of data</div>
      <div class="raw-opt">(D) None of these</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Size of the Antenna</div>
      <div class="sub">
        The fundamental operational difference between Real Aperture Radar (RAR) and Synthetic Aperture Radar (SAR) is in the <strong>size of the antenna</strong>. RAR requires an impractically massive physical antenna ($L_a = \lambda R / R_a$) to narrow its beam, whereas SAR employs a compact physical antenna ($1 - 15\text{ m}$) and synthesizes a virtual antenna kilometers in length through Doppler signal processing.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Size of the Antenna</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Antenna dimensions dictate beamwidth and azimuth resolution. In RAR, the physical antenna length must be enormous to achieve high resolution over long ranges ($R_a = \lambda R / L_a$). In SAR, platform forward motion and Doppler phase histories synthesize an artificial antenna thousands of meters long from a small physical antenna, yielding range-independent resolution ($R_a = L_a / 2$).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Source of energy</span>
      <span class="tag wrong">Incorrect (Identical Active Microwave Transmitters)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Both RAR and SAR are active radar systems operating in the microwave spectrum ($1 - 100\text{ cm}$) using identical artificial microwave transmitters powered by the platform's electrical generators and solar panels.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Recording of data</span>
      <span class="tag wrong">Incorrect (Secondary Processing Consequence)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> While SAR requires recording coherent phase data and complex Doppler matrix reconstruction, the fundamental engineering hurdle that distinguishes the two paradigms is overcoming the physical size constraints of the antenna aperture.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) None of these</span>
      <span class="tag wrong">Incorrect (Valid Answer Exists in Option A)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Option (A) is the classic textbook definition found verbatim in remote sensing literature (Sabins, 1997, p. 182; Lillesand et al., 2015).
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Radar Comparison: Real Aperture (RAR) vs. Synthetic Aperture (SAR)</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>System Parameter</th>
            <th>Real Aperture Radar (RAR / SLAR)</th>
            <th>Synthetic Aperture Radar (SAR)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Azimuth Resolution Formula</strong></td>
            <td><strong>$R_a = \frac{\lambda \cdot R}{L_a}$</strong> (Degrades with distance)</td>
            <td><strong>$R_a = \frac{L_a}{2}$</strong> (Independent of range and wavelength!)</td>
          </tr>
          <tr>
            <td><strong>Physical Antenna Length ($L_a$)</strong></td>
            <td>Must be extremely long ($> 10 - 100\text{ m}$)</td>
            <td>Compact: <strong>$1 - 15\text{ m}$</strong> (smaller gives finer resolution)</td>
          </tr>
          <tr>
            <td><strong>Effective Aperture ($L_{\text{eff}}$)</strong></td>
            <td>Strictly equal to physical length $L_a$</td>
            <td>Synthesized length: <strong>$L_{\text{syn}} = \frac{\lambda \cdot R}{L_a}$</strong> (kilometers long)</td>
          </tr>
          <tr>
            <td><strong>Platform Suitability</strong></td>
            <td>Low-altitude aircraft only ($H < 5 - 10\text{ km}$)</td>
            <td>High-altitude aircraft and spacecraft ($H = 500 - 800\text{ km}$)</td>
          </tr>
          <tr>
            <td><strong>Signal Coherence Requirement</strong></td>
            <td>Non-coherent (measures intensity only)</td>
            <td>Fully coherent (measures both amplitude and Doppler phase)</td>
          </tr>
          <tr>
            <td><strong>Operational Examples</strong></td>
            <td>Early SLAR border surveillance systems</td>
            <td>Sentinel-1, RADARSAT, RISAT-1/2, ALOS-PALSAR, TerraSAR-X</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- HIGH-YIELD PRACTICE QUESTIONS (8 QUESTIONS) -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Questions)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A C-band Synthetic Aperture Radar satellite has a physical antenna length in the azimuth direction $L_a = 10.0\text{ m}$. What is the theoretical best along-track (azimuth) spatial resolution achievable by this SAR system?
          <div class="pq-ans">✔ Worked Answer: $R_a = 5.0\text{ meters}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            By the fundamental SAR theorem:
            $$R_a = \frac{L_a}{2} = \frac{10.0\text{ m}}{2} = 5.0\text{ m}$$
            This resolution is invariant whether the satellite is at $500\text{ km}$ or $1000\text{ km}$ altitude.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Why does a <em>smaller</em> physical antenna produce <em>finer</em> spatial azimuth resolution in a SAR system?
          <div class="pq-ans">✔ Correct Answer: A smaller antenna produces a broader beamwidth ($\beta = \lambda / L_a$), keeping the ground target in the beam for a longer distance and synthesizing a longer virtual aperture ($L_{\text{syn}}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the synthesized array length $L_{\text{syn}} \propto 1 / L_a$, reducing physical antenna size expands the Doppler bandwidth, sharpening the focused image.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What are the two primary SAR geometric distortions caused by side-looking radar imaging of mountainous terrain?
          <div class="pq-ans">✔ Correct Answer: Foreshortening, Layover, and Shadowing.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Foreshortening compresses slopes facing the radar; Layover occurs when the radar beam reaches the mountain peak before its base, causing the top to be imaged closer to near range; Shadowing occurs on slopes facing away from the radar beam.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In radar polarization, what do the abbreviations $HH, VV, HV$, and $VH$ signify?
          <div class="pq-ans">✔ Correct Answer: The electric field vector orientation on transmission and reception ($H = \text{Horizontal}, V = \text{Vertical}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> $HH$ and $VV$ are like-polarized channels; $HV$ and $VH$ are cross-polarized channels produced by multiple volumetric scattering in dense forest canopies.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> According to the Rayleigh Roughness Criterion, what condition determines whether a surface appears "smooth" (specular reflector / dark tone) or "rough" (diffuse scatterer / bright tone) to radar?
          <div class="pq-ans">✔ Correct Answer: $h < \frac{\lambda}{8 \cos\theta}$ (Smooth) vs. $h > \frac{\lambda}{8 \cos\theta}$ (Rough).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Where $h$ is root-mean-square surface height and $\theta$ is incidence angle. Smooth surfaces reflect microwaves away from the antenna (calm water appears black), while rough surfaces scatter energy back to the antenna (bright return).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What radar frequency band is used by ISRO's indigenous RISAT-1 earth observation satellite?
          <div class="pq-ans">✔ Correct Answer: C-band ($\lambda \approx 5.35\text{ GHz}, \lambda \approx 5.6\text{ cm}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> C-band provides an optimal compromise for all-weather agricultural monitoring, soil moisture estimation, and flood inundation mapping across India.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is <em>radar speckle</em>, and what spatial filtering techniques are applied to remove it?
          <div class="pq-ans">✔ Correct Answer: Salt-and-pepper graininess caused by random constructive and destructive interference of dephased returns within a resolution cell; removed by multi-looking or adaptive Lee/Frost spatial filters.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Coherent interference creates granular speckle noise, which is reduced by averaging independent sub-aperture looks or using statistical window filters.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why can L-band radar ($\lambda \approx 24\text{ cm}$) penetrate deep dry desert sand sheets (e.g., in the Sahara) whereas optical sensors cannot?
          <div class="pq-ans">✔ Correct Answer: Dry quartz sand has an extremely low dielectric constant ($\epsilon_r \approx 2 - 3$) and negligible electrical conductivity, allowing microwaves to penetrate several meters to map buried paleodrainage channels.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Demonstrated by the Space Shuttle SIR-A/SIR-B missions in 1981, L-band microwaves penetrated up to 2–5 meters of hyper-arid sand, revealing ancient buried river channels.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 16, part1, part2, part3)


# ==============================================================================
# Q017: Soil Moisture in NIR
# ==============================================================================
def generate_q017():
    title = "Q017: Spectral Reflectance of Soils: Moisture Attenuation & NIR Tone | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Optical Remote Sensing & Soil Spectroscopy"
    h1_title = "Q017: Spectral Reflectance of Soils: Moisture Attenuation & NIR Tone"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 17<br>
<strong>Authoritative References:</strong> John R. Jensen, <em>Remote Sensing of the Environment: An Earth Resource Perspective</em> (2nd Ed., Ch. 12: Soils & Minerals, pp. 411–425); Thomas M. Lillesand et al., <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 1, pp. 16–18); Bowers, S.A. & Hanks, R.J. (1965, <em>Reflection of radiant energy from soils</em>, Soil Science, 100, pp. 130–138)."""

    part1 = r"""
  <!-- CARD 1: SOIL SPECTRAL REFLECTANCE PHYSICS -->
  <div class="card">
    <div class="card-header bg-blue">1. The Spectral Reflectance Curve of Soil & Water Interaction</div>
    <div class="card-body">
      <p>The spectral reflectance of natural bare soil is governed by five fundamental physicochemical parameters: <strong>moisture content</strong>, <strong>organic matter</strong>, <strong>iron oxide content</strong>, <strong>texture/particle size</strong>, and <strong>surface roughness</strong>. Among these, soil moisture exerts the most dramatic, non-linear dampening effect on reflectance across the entire solar spectrum ($0.4 - 2.5\ \mu\text{m}$):</p>

      <ul>
        <li><strong>Dry Soil Baseline:</strong> Completely dry mineral soils display a smooth, continuous, monotonically increasing reflectance curve from the visible through the Near-Infrared (NIR, $0.7 - 1.1\ \mu\text{m}$) and SWIR, appearing in bright light-grey to white tones on imagery.</li>
        <li><strong>Moisture Reflectance Suppression:</strong> As volumetric soil moisture increases from $0\%$ to field capacity, <strong>reflectance decreases dramatically across all wavelengths</strong>, plunging the entire spectral curve downwards.</li>
        <li><strong>Liquid Water Absorption Bands:</strong> Prominent liquid water absorption bands centered at <strong>$1.4\ \mu\text{m}$</strong> and <strong>$1.9\ \mu\text{m}$</strong> (vibrational overtones and combinations) broaden, with a weaker absorption band at <strong>$0.95\ \mu\text{m}$</strong> extending directly into the NIR band.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q17/soil_moisture_nir_reflectance_tone.png" alt="Soil Moisture NIR Reflectance Attenuation and Tone">
        <div class="tb-caption">
          <strong>Figure 17.1: Soil Reflectance vs. Moisture Content.</strong> Progressive reduction in spectral reflectance across the VNIR and SWIR as volumetric moisture increases from $0\%$ (dry sand) to $35\%$ (saturated soil), transforming the surface tone from bright white to dark grey/black.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE OPTICAL MECHANISM: WHY WET SOILS ARE DARK -->
  <div class="card">
    <div class="card-header bg-indigo">2. Optical Physics: Refractive Index Matching & Internal Trapping</div>
    <div class="card-body">
      <p>Why does water make soil look darker? The darkening of moist soil is governed by two physical optics mechanisms (Ångström, 1925; Lekner & Dorf, 1988):</p>

      <ul>
        <li><strong>1. Refractive Index Matching:</strong> In dry soil, quartz grains ($n_{\text{quartz}} \approx 1.54$) are surrounded by air ($n_{\text{air}} \approx 1.00$). The high refractive index contrast ($\Delta n = 0.54$) causes strong Fresnel reflection and multiple scattering at grain boundaries, returning light to the sensor (high reflectance). When water ($n_{\text{water}} \approx 1.33$) fills the pore spaces, the index contrast drops to $\Delta n = 1.54 - 1.33 = 0.21$. Scattering drops by more than $60\%$, allowing light to penetrate deeply into the soil rather than being reflected.</li>
        <li><strong>2. Total Internal Reflection in Water Menisci:</strong> Surface water films create curved capillary menisci that trap backscattered rays via total internal reflection, forcing photons to undergo repeated absorption passes through the soil grains before they can escape.</li>
        <li><strong>Visual Image Rendering:</strong> In remote sensing imagery, pixel brightness is directly proportional to recorded radiance ($DN \propto L$). Low NIR reflectance means the sensor records low digital numbers, rendering moist ground in distinct <strong>grey to dark-grey</strong> (or black) tones.</li>
      </ul>

      <div class="quote-box">
        "As the moisture content of an agricultural soil increases, its overall spectral reflectance decreases across all wavelengths. In photographic or multispectral images, wet soil surfaces appear distinctly darker (lower grey values or darker tones) than surrounding dry soils."
        <span class="quote-ref">— John R. Jensen, <em>Remote Sensing of the Environment</em> (2nd Ed., 2007, p. 415)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Color Tone Distractors</div>
    <div class="card-body">
      <p>Understanding image display formats eliminates distractors:</p>
      <ul>
        <li><strong>White (Option A):</strong> White signifies maximum reflectance ($DN \approx 255$). This is characteristic of bone-dry sand dunes, salt playas, or snow/clouds, the polar opposite of wet soil.</li>
        <li><strong>Red (Option C):</strong> In a standard False Color Composite (FCC: NIR=Red, Red=Green, Green=Blue), healthy green vegetation appears bright red due to intense spongy mesophyll reflectance ($40 - 60\%$). Moist bare soil lacks chlorophyll and displays low NIR reflectance, appearing dark grey, brown, or black on FCCs.</li>
        <li><strong>Blue (Option D):</strong> In standard single-band grayscale display, pixels are exclusively rendered in shades of grey (0 = black to 255 = white). Colors like red or blue do not exist in single-band NIR imagery.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 17)</div>
    <div class="q-stmt">
      Q17. The moisture present in the ground surface is shown as _______ tone in the NIR region of imagery.
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) white</div>
      <div class="raw-opt correct">(B) grey &nbsp;✔</div>
      <div class="raw-opt">(C) red</div>
      <div class="raw-opt">(D) blue</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) grey</div>
      <div class="sub">
        Moisture present in the ground absorbs near-infrared radiation and decreases surface reflectance via refractive index matching, causing moist soils to appear in <strong>grey</strong> (medium grey to dark grey/black) tones on single-band NIR imagery.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) white</span>
      <span class="tag wrong">Incorrect (Indicates Maximum Reflectance / Bone-Dry Targets)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A white tone on grayscale imagery represents high radiant reflectance ($DN \approx 255$). In the NIR band, white tones are produced by bone-dry sand dunes, bleached carbonate outcrops, salt crusts, and clouds. Moisture suppresses reflectance, creating dark tones.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) grey</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> When water occupies soil pores, the refractive index contrast between quartz and the pore medium decreases, reducing multiple scattering while water absorption bands ($0.95, 1.4\ \mu\text{m}$) absorb incident energy. Consequently, moist ground reflects significantly less NIR energy than dry soil, producing a diagnostic <strong>grey</strong> (dark grey) tone.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) red</span>
      <span class="tag wrong">Incorrect (Confuses FCC Vegetation Display with Grayscale Tone)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> On a standard False Color Composite (FCC), healthy green vegetation appears red because NIR radiance is mapped to the red display gun. Bare moist ground has low NIR reflectance and never appears red. Furthermore, a single NIR band is displayed in grayscale tones, not color.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) blue</span>
      <span class="tag wrong">Incorrect (Single Band Imagery Contains No Chromatic Color)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Single-band NIR satellite imagery possesses no chromatic blue color; it is recorded as scalar radiance quantized into shades of grey. Clear deep water appears dark/black, but moist soil appears grey.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Physical Factors Governing Soil Spectral Reflectance</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Soil Soil Physicochemical Parameter</th>
            <th>Effect on Overall Reflectance</th>
            <th>Specific Spectral Manifestation</th>
            <th>Tone on Grayscale NIR Imagery</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Moisture Content (Increasing)</strong></td>
            <td><strong>Substantial decrease across all bands</strong></td>
            <td>Strong absorption at $0.95, 1.4, 1.9\ \mu\text{m}$; index matching</td>
            <td><strong>Medium to Dark Grey / Black</strong></td>
          </tr>
          <tr>
            <td><strong>Organic Matter ($> 2\%$)</strong></td>
            <td>Significant decrease across visible & NIR</td>
            <td>Masks mineral absorption features; flattens spectral slope</td>
            <td>Dark Grey to Black</td>
          </tr>
          <tr>
            <td><strong>Iron Oxide ($\text{Fe}^{3+}$ / Hematite)</strong></td>
            <td>Steep increase in red; absorption in UV/blue</td>
            <td>Diagnostic absorption trough at $0.85 - 0.90\ \mu\text{m}$</td>
            <td>Medium Grey</td>
          </tr>
          <tr>
            <td><strong>Texture: Fine Sand vs. Coarse Silt</strong></td>
            <td>Increases with decreasing particle size</td>
            <td>Smaller particles create more scattering surfaces</td>
            <td>Light Grey to White (when dry)</td>
          </tr>
          <tr>
            <td><strong>Surface Roughness (Plowed field)</strong></td>
            <td>Decreases reflectance</td>
            <td>Micro-shadowing traps incident solar radiation</td>
            <td>Medium to Dark Grey</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- HIGH-YIELD PRACTICE QUESTIONS (8 QUESTIONS) -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Questions)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> How does Ångström's (1925) optical equation explain the reduction in surface reflectance when dry soil is wetted with water?
          <div class="pq-ans">✔ Correct Answer: Refraction at the air-water boundary and lower relative refractive index ($n_{\text{mineral}} / n_{\text{water}}$) promotes multiple internal reflections, trapping light inside the liquid film.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Light reflected back from a mineral grain within a water layer strikes the water-air interface from below; if the angle exceeds the critical angle ($\theta_c \approx 48.6^\circ$), it undergoes total internal reflection back into the soil, causing repeated absorption.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> At what critical percentage of Soil Organic Matter (SOM) does organic carbon completely mask the diagnostic iron and clay absorption features of a soil?
          <div class="pq-ans">✔ Correct Answer: Approximately $2.0\% \text{ to } 2.5\%$ organic carbon content.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Soils containing $> 2\%$ decomposed organic humus display a dark, monotonic low-reflectance curve devoid of distinct mineral absorption troughs.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What satellite radar frequency band is globally utilized by NASA's SMAP (Soil Moisture Active Passive) mission to map volumetric soil moisture?
          <div class="pq-ans">✔ Correct Answer: L-band ($1.41\text{ GHz}, \lambda \approx 21\text{ cm}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Liquid water has an exceptionally high dielectric constant ($\epsilon_r \approx 80$) compared to dry soil ($\epsilon_r \approx 3 - 5$). L-band microwaves penetrate vegetation to measure the dielectric jump in the top $5\text{ cm}$ of soil.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In a False Color Composite (FCC: Bands NIR, Red, Green displayed as RGB), how do wet water-logged paddy fields appear?
          <div class="pq-ans">✔ Correct Answer: In dark blue to black tones (or dark purple-grey).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Water absorbs both NIR and Red light strongly. Because minimal energy is reflected to activate the red or green color guns, the water-logged soil appears dark bluish-black.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the "Soil Line" in spectral space, and what are its coordinates?
          <div class="pq-ans">✔ Correct Answer: The linear correlation line formed by plotting Red reflectance vs. NIR reflectance for bare soils ranging from wet to dry ($\rho_{\text{NIR}} = a \rho_{\text{Red}} + b$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Bare soils of varying moisture and roughness fall along a straight line in Red-NIR feature space, serving as the baseline for vegetation indices like PVI (Perpendicular Vegetation Index) and SAVI.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> How does crusting (such as a white halite/gypsum evaporite crust on an alkali soil) affect NIR reflectance?
          <div class="pq-ans">✔ Correct Answer: It dramatically increases reflectance, shifting image tone from dark grey to brilliant white.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> High-albedo precipitated salt crystals seal surface pores, eliminating moisture absorption and causing intense surface scattering.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Which two Short-Wave Infrared (SWIR) wavelengths correspond to the deepest fundamental vibrational overtones of liquid water in soil?
          <div class="pq-ans">✔ Correct Answer: $1.45\ \mu\text{m}$ and $1.95\ \mu\text{m}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> These two water absorption bands form deep troughs in the soil reflectance curve, with the $1.95\ \mu\text{m}$ band being the most diagnostic indicator of soil hydration.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does a freshly plowed agricultural field appear darker on satellite imagery than an adjacent untilled, smooth field of identical soil composition?
          <div class="pq-ans">✔ Correct Answer: Macroscopic surface roughness creates self-shadowing clods and furrow crevices that trap incident photons.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Clods and furrows act as micro-cavities that absorb radiation through multiple cavity reflections, lowering effective surface albedo.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 17, part1, part2, part3)


# ==============================================================================
# Q018: Vegetation Reflectance in Green Band
# ==============================================================================
def generate_q018():
    title = "Q018: Biophysical Controls on Plant Spectral Reflectance: Pigments vs. Cell Structure | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Optical Remote Sensing & Vegetation Biophysics"
    h1_title = "Q018: Biophysical Controls on Plant Spectral Reflectance: Pigments vs. Cell Structure"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 18<br>
<strong>Authoritative References:</strong> Thomas M. Lillesand et al., <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 1, pp. 16–18); John R. Jensen, <em>Remote Sensing of the Environment</em> (2nd Ed., Ch. 11: Vegetation Biophysics, pp. 357–372); Gates, D.M. et al. (1965, <em>Spectral properties of plants</em>, Applied Optics, 4, pp. 11–20); Knipling, E.B. (1970, <em>Physiological Remote Sensing</em>)."""

    part1 = r"""
  <!-- CARD 1: THE TRIPARTITE VEGETATION REFLECTANCE SPECTRUM -->
  <div class="card">
    <div class="card-header bg-blue">1. The Tripartite Biophysical Architecture of Green Leaves</div>
    <div class="card-body">
      <p>The spectral reflectance curve of healthy green vegetation is one of the most distinctive and extensively studied signatures in physical remote sensing. The curve is divided into three discrete spectral domains, each governed by an entirely different biophysical leaf component (Gates et al., 1965; Knipling, 1970):</p>

      <ul>
        <li><strong>1. Visible Region ($0.40 - 0.70\ \mu\text{m}$):</strong> Controlled entirely by <strong>Leaf Pigments</strong> (principally <em>Chlorophyll a</em> and <em>Chlorophyll b</em>, accompanied by accessory carotenes and xanthophylls). Chlorophyll pigments strongly absorb blue light ($\sim 0.45\ \mu\text{m}$) and red light ($\sim 0.65\ \mu\text{m}$) to drive photosynthetic electron transport, leaving an unabsorbed <strong>reflection peak in the green band ($\sim 0.55\ \mu\text{m}$, reflecting $10 - 20\%$ of energy)</strong>. This green reflectance peak is why healthy vegetation appears green to the human eye!</li>
        <li><strong>2. Near-Infrared Region ($0.70 - 1.30\ \mu\text{m}$):</strong> Controlled exclusively by <strong>Internal Leaf Cell Structure</strong> (the spongy mesophyll parenchyma). Leaves absorb almost zero NIR energy; multiple refraction at internal hydration cell-wall/air-space boundaries scatters $40 - 60\%$ of incident NIR photons back out, creating the massive "NIR plateau".</li>
        <li><strong>3. Short-Wave Infrared ($1.30 - 2.50\ \mu\text{m}$):</strong> Controlled exclusively by <strong>Leaf Moisture (Water Content)</strong>, displaying strong water absorption troughs at $1.4\ \mu\text{m}$ and $1.9\ \mu\text{m}$.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q18/vegetation_reflectance_curve.png" alt="Vegetation Spectral Reflectance Curve and Biophysical Controls">
        <div class="tb-caption">
          <strong>Figure 18.1: The Tripartite Spectral Response Curve of Green Vegetation.</strong> Showing the three distinct biophysical control zones: (1) Leaf pigments governing the visible spectrum with the green peak at $0.55\ \mu\text{m}$; (2) Spongy mesophyll cell structure creating the high NIR plateau ($0.7 - 1.3\ \mu\text{m}$); and (3) Leaf water content governing SWIR absorption ($1.4 - 2.5\ \mu\text{m}$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: PHOTOSYNTHETIC PIGMENTS & THE GREEN REFLECTION PEAK -->
  <div class="card">
    <div class="card-header bg-indigo">2. Photosynthetic Pigments: Why the Green Peak Exists</div>
    <div class="card-body">
      <p>In the palisade parenchyma layer of the upper leaf, chloroplasts contain photosynthetic pigment complexes tuned to capture photon energy:</p>

      <ul>
        <li><strong>Chlorophyll a & b Absorption Bands:</strong> Chlorophyll a has absorption peaks at $0.43\ \mu\text{m}$ (blue) and $0.66\ \mu\text{m}$ (red). Chlorophyll b absorbs at $0.45\ \mu\text{m}$ (blue) and $0.64\ \mu\text{m}$ (red). Up to $90 - 95\%$ of blue and red incident photons are absorbed in the chloroplasts.</li>
        <li><strong>The 0.55 $\mu$m Green Reflectance Peak:</strong> Photosynthetic pigments possess a gap in their absorption spectra between $0.50\ \mu\text{m}$ and $0.60\ \mu\text{m}$ (the green wavelengths). Because green photons are not absorbed, approximately $10 - 20\%$ are backscattered out through the upper epidermis.</li>
        <li><strong>Senescence / Chlorosis Shift:</strong> When a plant undergoes environmental stress, disease, or autumn senescence, chlorophyll degrades rapidly. The unmasking of yellow and orange carotenes and xanthophylls increases red reflectance, causing leaves to turn yellow or brown.</li>
      </ul>

      <div class="quote-box">
        "In the visible portion of the spectrum (0.4 to 0.7 $\mu$m), the spectral reflectance of green vegetation is governed primarily by the absorption characteristics of plant pigments, principally chlorophyll... A green reflectance peak occurs at approximately 0.55 $\mu$m, between the blue and red absorption bands."
        <span class="quote-ref">— Thomas M. Lillesand et al., <em>Remote Sensing and Image Interpretation</em> (7th Ed., 2015, p. 16)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Leaf Moisture and Cell Structure in the Green Band</div>
    <div class="card-body">
      <p>Candidates must clearly map which leaf component governs each specific spectral band:</p>
      <ul>
        <li><strong>Leaf Moisture (Option A):</strong> Governs the Short-Wave Infrared (SWIR, $1.4 - 2.5\ \mu\text{m}$). In the visible green band, liquid water absorption is virtually zero ($k \approx 10^{-8}$), having no effect on leaf green reflectance.</li>
        <li><strong>Leaf Cell Structure (Option C):</strong> Governs the Near-Infrared (NIR, $0.7 - 1.3\ \mu\text{m}$). The spongy mesophyll cell structure is transparent to visible light, which is absorbed by chloroplast pigments before it can undergo mesophyll scattering.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 18)</div>
    <div class="q-stmt">
      Q18. In the visible region (green band), leaf reflectance is governed by :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Leaf moisture</div>
      <div class="raw-opt correct">(B) Leaf pigment &nbsp;✔</div>
      <div class="raw-opt">(C) Leaf cell structure</div>
      <div class="raw-opt">(D) None of these</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Leaf pigment</div>
      <div class="sub">
        In the visible region of the spectrum ($0.4 - 0.7\ \mu\text{m}$), including the green band ($\sim 0.55\ \mu\text{m}$), leaf reflectance is strictly governed by <strong>Leaf pigments</strong> (principally chlorophyll a and b, carotenoids, and xanthophylls).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Leaf moisture</span>
      <span class="tag wrong">Incorrect (Governs the SWIR Region: 1.4 – 2.5 $\mu$m)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Leaf water content controls reflectance in the Short-Wave Infrared (SWIR, $1.4 - 2.5\ \mu\text{m}$) region, producing pronounced absorption troughs at $1.4\ \mu\text{m}$ and $1.9\ \mu\text{m}$. Pure water is transparent in the visible green band and exerts zero influence on green reflectance.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Leaf pigment</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By fundamental biophysical optics (Lillesand et al., 2015; Jensen, 2007), leaf reflectance in the visible spectrum is completely dominated by photosynthetic leaf pigments. Chlorophyll a and b absorb blue ($0.45\ \mu\text{m}$) and red ($0.65\ \mu\text{m}$) light heavily, allowing an unabsorbed reflectance peak at $0.55\ \mu\text{m}$ (green), which gives vegetation its characteristic green color.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Leaf cell structure</span>
      <span class="tag wrong">Incorrect (Governs the NIR Plateau: 0.7 – 1.3 $\mu$m)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The internal anatomical structure of the leaf—specifically the arrangement of hydrated cell walls and air voids in the spongy mesophyll layer—governs the Near-Infrared (NIR, $0.7 - 1.3\ \mu\text{m}$) plateau, causing massive scattering of $40 - 60\%$ of incident NIR energy. It does not govern the visible green band.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) None of these</span>
      <span class="tag wrong">Incorrect (Valid Answer Exists in Option B)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> "Leaf pigment" is the universally accepted, established scientific answer.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Biophysical Controls: The Three Vegetation Spectral Zones</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Spectral Region</th>
            <th>Wavelength Interval</th>
            <th>Primary Biophysical Governing Factor</th>
            <th>Physiological Mechanism & Key Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Visible (VNIR)</strong></td>
            <td><strong>$0.40 - 0.70\ \mu\text{m}$</strong></td>
            <td><strong>Leaf Pigments</strong> (Chlorophyll a, b, Carotenes)</td>
            <td><strong>Blue/Red photosynthetic absorption; Green reflectance peak at $0.55\ \mu\text{m}$</strong></td>
          </tr>
          <tr>
            <td><strong>Red Edge</strong></td>
            <td>$0.68 - 0.75\ \mu\text{m}$</td>
            <td>Transition boundary</td>
            <td>Steep rise in reflectance from chlorophyll absorption to mesophyll scatter</td>
          </tr>
          <tr>
            <td><strong>Near-Infrared (NIR)</strong></td>
            <td><strong>$0.70 - 1.30\ \mu\text{m}$</strong></td>
            <td><strong>Internal Spongy Mesophyll Structure</strong></td>
            <td>High internal refraction at cell-wall/air interfaces ($40 - 60\%$ reflectance plateau)</td>
          </tr>
          <tr>
            <td><strong>Short-Wave Infrared (SWIR)</strong></td>
            <td><strong>$1.30 - 2.50\ \mu\text{m}$</strong></td>
            <td><strong>Leaf Moisture (Water Content)</strong></td>
            <td>Deep vibrational absorption bands at $1.4\ \mu\text{m}$ and $1.9\ \mu\text{m}$; turgidity monitoring</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- HIGH-YIELD PRACTICE QUESTIONS (8 QUESTIONS) -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Questions)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> How is the Normalized Difference Vegetation Index (NDVI) formulated, and how does it exploit the contrasting controls of leaf pigment and cell structure?
          <div class="pq-ans">✔ Worked Answer: $\text{NDVI} = \frac{\rho_{\text{NIR}} - \rho_{\text{Red}}}{\rho_{\text{NIR}} + \rho_{\text{Red}}}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Pigments strongly absorb red light ($\rho_{\text{Red}} \approx 0.05$), while spongy mesophyll scatters NIR light intensely ($\rho_{\text{NIR}} \approx 0.50$). Healthy dense vegetation yields high positive NDVI values ($+0.6 \text{ to } +0.9$).
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What happens to the "Red Edge" position ($\lambda_{\text{re}}$) when vegetation suffers heavy metal stress or drought-induced chlorosis?
          <div class="pq-ans">✔ Correct Answer: It shifts toward shorter wavelengths (a "blue shift").</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Chlorophyll loss reduces the depth and width of the $0.68\ \mu\text{m}$ absorption trough, shifting the inflection point of the red-edge slope toward the blue/green spectrum (from $\sim 720\text{ nm}$ down to $\sim 700\text{ nm}$).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What are the primary accessory pigments responsible for the brilliant yellow, orange, and red colors of autumn leaves?
          <div class="pq-ans">✔ Correct Answer: Carotenoids (carotenes and xanthophylls) and anthocyanins.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> As photoperiod and temperatures drop, green chlorophyll breaks down first, unmasking the stable yellow carotenoids and newly synthesized red anthocyanin pigments.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In optical physics, what causes the intense scattering of near-infrared radiation inside the spongy mesophyll layer of a leaf?
          <div class="pq-ans">✔ Correct Answer: The substantial difference in refractive index between hydrated cellulose cell walls ($n \approx 1.42 - 1.48$) and intercellular air spaces ($n \approx 1.00$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> As NIR photons cross back and forth between cell walls and air cavities, multiple refractions and reflections scatter photons in all directions, redirecting half of them back out through the leaf surface.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Why does a stacked canopy of multiple leaf layers (Leaf Area Index $\text{LAI} > 4$) display higher NIR reflectance than a single isolated leaf, while visible red reflectance remains unchanged?
          <div class="pq-ans">✔ Correct Answer: Transmitted NIR radiation passes through the upper leaf and reflects off lower leaves back through the canopy (optical stacking); red light is completely absorbed by the first leaf layer.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Near-infrared has high transmissivity ($\sim 40 - 50\%$), allowing multi-story canopies to contribute additive reflectance, whereas visible red is absorbed almost entirely ($> 90\%$) by the topmost layer.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What vegetation index, formulated by Gao (1996), specifically monitors equivalent leaf water thickness in the SWIR spectrum?
          <div class="pq-ans">✔ Correct Answer: NDWI (Normalized Difference Water Index): $\text{NDWI} = \frac{\rho_{860} - \rho_{1240}}{\rho_{860} + \rho_{1240}}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> By ratioing an NIR band ($860\text{ nm}$, insensitive to moisture) with a SWIR water absorption band ($1240\text{ nm}$), NDWI directly tracks canopy moisture stress.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How does severe plant senescence affect the internal spongy mesophyll and the resulting NIR plateau?
          <div class="pq-ans">✔ Correct Answer: Dehydration causes cells to collapse and intercellular air voids to diminish, dramatically lowering NIR plateau reflectance.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Cellular collapse eliminates refractive index interfaces, causing the NIR reflectance of senescent vegetation to plunge toward bare soil levels.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does artificial green turf (plastic fake grass) appear dark on a False Color Composite (FCC) while natural grass appears bright red?
          <div class="pq-ans">✔ Correct Answer: Artificial turf contains green dye (reflecting visible green) but completely lacks the internal spongy mesophyll cell structure required to reflect near-infrared radiation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because plastic turf absorbs or has low reflectance in the NIR, it fails to activate the red display channel on an FCC, immediately unmasking military camouflage.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 18, part1, part2, part3)


# ==============================================================================
# Q019: IRS-1D LISS-III Spatial Resolution
# ==============================================================================
def generate_q019():
    title = "Q019: Indian Remote Sensing (IRS-1D) Payloads: LISS-III Spatial Resolution | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • ISRO Satellite Missions & Sensor Payloads"
    h1_title = "Q019: Indian Remote Sensing (IRS-1D) Payloads: LISS-III Spatial Resolution"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 19<br>
<strong>Authoritative References:</strong> ISRO National Remote Sensing Centre (NRSC), <em>IRS-1C/1D Data User's Handbook</em> (Department of Space, Govt. of India); Kasturirangan, K. et al. (1996, <em>IRS-1C - The Indian Space Programme's Advanced Remote Sensing Satellite</em>, Current Science, 70, pp. 492–500); Lillesand, Kiefer & Chipman (7th Ed., pp. 396–399)."""

    part1 = r"""
  <!-- CARD 1: THE IRS-1D SATELLITE MISSION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Indian Remote Sensing (IRS-1D) Mission & Sensor Suite</div>
    <div class="card-body">
      <p>Launched on <strong>29 September 1997</strong> aboard India's Polar Satellite Launch Vehicle (PSLV-C1) from Sriharikota, <strong>IRS-1D</strong> (along with its identical predecessor IRS-1C, launched in 1995) was an internationally acclaimed second-generation earth observation satellite developed by the <strong>Indian Space Research Organisation (ISRO)</strong>. Operating in a Sun-synchronous circular orbit at an altitude of $817\text{ km}$ ($i = 98.69^\circ$, 24-day repeat cycle), IRS-1D carried three cutting-edge imaging payloads:</p>

      <ul>
        <li><strong>1. LISS-III (Linear Imaging Self-Scanning Sensor III):</strong> The primary multispectral sensor (MSS) designed for regional natural resources management, agricultural monitoring, and geological mapping. LISS-III delivers a benchmark spatial resolution of <strong>$23.5\text{ meters}$</strong> in the Visible and Near-Infrared (VNIR) bands.</li>
        <li><strong>2. PAN (Panchromatic Camera):</strong> A high-resolution imaging camera operating across $0.50 - 0.75\ \mu\text{m}$ with a spatial resolution of <strong>$5.8\text{ meters}$</strong> and a $70\text{ km}$ swath, equipped with off-nadir steering ($\pm 26^\circ$) for stereoscopic 3D terrain mapping. In 1995, it was the highest-resolution civilian earth observation sensor in the world!</li>
        <li><strong>3. WiFS (Wide Field Sensor):</strong> A dual-band sensor (Red: $0.62 - 0.68\ \mu\text{m}$, NIR: $0.77 - 0.86\ \mu\text{m}$) with a spatial resolution of <strong>$188\text{ meters}$</strong> and an ultra-wide swath of $810\text{ km}$ (5-day revisit) for national-scale vegetation and drought dynamics.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q19/irs_1d_sensor_payloads_resolution.png" alt="IRS-1D Sensor Payloads and Spatial Resolution Spectrum">
        <div class="tb-caption">
          <strong>Figure 19.1: ISRO IRS-1D Sensor Payload Architecture.</strong> Comparison of the three complementary sensors: PAN ($5.8\text{ m}$), LISS-III ($23.5\text{ m}$ VNIR / $70.5\text{ m}$ SWIR), and WiFS ($188\text{ m}$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: DETAILED LISS-III SENSOR SPECIFICATIONS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Technical Specifications of LISS-III: The 23.5m Multispectral Benchmark</div>
    <div class="card-body">
      <p>LISS-III utilized linear charge-coupled device (CCD) pushbroom line arrays (6000 elements per array) to image terrain without moving optical scan mirrors. Its four spectral bands and spatial resolutions are structured as follows:</p>

      <table>
        <thead>
          <tr>
            <th>LISS-III Spectral Band</th>
            <th>Wavelength Range ($\mu\text{m}$)</th>
            <th>Spatial Resolution (GSD)</th>
            <th>Swath Width</th>
            <th>Primary Geological & Land Use Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Band 2 (Green)</strong></td>
            <td>$0.52 - 0.59\ \mu\text{m}$</td>
            <td><strong>$23.5\text{ meters}$</strong></td>
            <td>$141\text{ km}$</td>
            <td>Vegetation green reflectance peak; water turbidity</td>
          </tr>
          <tr>
            <td><strong>Band 3 (Red)</strong></td>
            <td>$0.62 - 0.68\ \mu\text{m}$</td>
            <td><strong>$23.5\text{ meters}$</strong></td>
            <td>$141\text{ km}$</td>
            <td>Chlorophyll absorption; soil/vegetation contrast; cultural features</td>
          </tr>
          <tr>
            <td><strong>Band 4 (Near-Infrared)</strong></td>
            <td>$0.77 - 0.86\ \mu\text{m}$</td>
            <td><strong>$23.5\text{ meters}$</strong></td>
            <td>$141\text{ km}$</td>
            <td>Biomass mapping; water-land boundary delimitation</td>
          </tr>
          <tr>
            <td><strong>Band 5 (Short-Wave IR)</strong></td>
            <td>$1.55 - 1.70\ \mu\text{m}$</td>
            <td>$70.5\text{ meters}$</td>
            <td>$148\text{ km}$</td>
            <td>Soil moisture; snow vs. cloud discrimination; hydrothermal alteration</td>
          </tr>
        </tbody>
      </table>

      <div class="quote-box">
        "The LISS-III camera operates in four spectral bands: three in the VNIR (0.52-0.59, 0.62-0.68, 0.77-0.86 $\mu$m) with a spatial resolution of 23.5 m at nadir, and one in the SWIR (1.55-1.70 $\mu$m) with a resolution of 70.5 m."
        <span class="quote-ref">— K. Kasturirangan et al., <em>IRS-1C - The Indian Space Programme's Advanced Remote Sensing Satellite</em> (Current Science, 1996, Vol. 70, No. 7, p. 494)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Forensic Dissection of Distractor Resolutions</div>
    <div class="card-body">
      <p>Candidates must clearly associate other famous remote sensing resolutions:</p>
      <ul>
        <li><strong>(A) 1m:</strong> Characteristic of modern sub-meter commercial high-resolution imaging satellites such as IKONOS-2 ($1\text{ m}$ PAN in 1999) or ISRO's Cartosat-2 series ($0.8\text{ m}$). It is far too fine for IRS-1D LISS-III.</li>
        <li><strong>(B) 30m:</strong> The classic spatial resolution of NASA's Landsat Thematic Mapper (TM/ETM+/OLI Bands 1–5, 7), which defined multispectral resolution from 1982 onwards.</li>
        <li><strong>(C) 79m (or 80m):</strong> The historical spatial resolution of the original Multispectral Scanner (MSS) onboard early Landsat-1, 2, and 3 (1972–1978).</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 19)</div>
    <div class="q-stmt">
      Q19. In IRS 1D satellite, the spatial resolution of MSS sensor is :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) 1m.</div>
      <div class="raw-opt">(B) 30m</div>
      <div class="raw-opt">(C) 79m</div>
      <div class="raw-opt correct">(D) 23.5m &nbsp;✔</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) 23.5m</div>
      <div class="sub">
        In the Indian Remote Sensing satellite <strong>IRS-1D</strong>, the primary multispectral sensor (MSS)—the <strong>LISS-III</strong> camera—operates with a spatial resolution of <strong>23.5 meters</strong> in its three visible and near-infrared bands (Bands 2, 3, and 4).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) 1m.</span>
      <span class="tag wrong">Incorrect (High-Resolution Satellite Domain like IKONOS / Cartosat-2)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A 1-meter spatial resolution belongs to very high-resolution military and commercial mapping satellites (e.g., IKONOS-2 launched in 1999, OrbView, or Cartosat-2). The highest optical resolution on IRS-1D was the Panchromatic (PAN) camera at $5.8\text{ m}$.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) 30m</span>
      <span class="tag wrong">Incorrect (Thematic Mapper / Landsat Benchmark)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> $30\text{ meters}$ is the global benchmark spatial resolution of NASA's Landsat Thematic Mapper (Landsat-4, 5, 7, 8, 9). ISRO purposely engineered LISS-III with an enhanced $23.5\text{ m}$ resolution to surpass Landsat TM in ground detail.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 79m</span>
      <span class="tag wrong">Incorrect (Landsat-1/2/3 First-Generation MSS Resolution)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> $79\text{ meters}$ (nominally $80\text{ m}$) was the resolution of the historical Multispectral Scanner (MSS) flown on Landsat-1, 2, and 3 in the 1970s, as well as ISRO's earliest first-generation LISS-I sensor on IRS-1A/1B ($72.5\text{ m}$).
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) 23.5m</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> On IRS-1C and IRS-1D, the flagship multispectral sensor LISS-III provided <strong>$23.5\text{ m}$</strong> ground spatial resolution across its VNIR bands (Green: $0.52 - 0.59\ \mu\text{m}$, Red: $0.62 - 0.68\ \mu\text{m}$, and NIR: $0.77 - 0.86\ \mu\text{m}$) over a $141\text{ km}$ swath, establishing India as a world leader in civilian remote sensing.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Evolution of ISRO Earth Observation Sensor Resolutions</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Satellite Mission</th>
            <th>Launch Year</th>
            <th>Sensor Payloads</th>
            <th>Spatial Resolution (GSD)</th>
            <th>Key Technological Milestone</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>IRS-1A / 1B</strong></td>
            <td>1988 / 1991</td>
            <td>LISS-I<br>LISS-IIA/B</td>
            <td>$72.5\text{ m}$<br>$36.25\text{ m}$</td>
            <td>India's first indigenous operational remote sensing satellites</td>
          </tr>
          <tr>
            <td><strong>IRS-1C / 1D</strong></td>
            <td>1995 / 1997</td>
            <td><strong>PAN</strong><br><strong>LISS-III (MSS)</strong><br><strong>WiFS</strong></td>
            <td><strong>$5.8\text{ m}$</strong><br><strong>$23.5\text{ m}$ (VNIR) / $70.5\text{ m}$ (SWIR)</strong><br><strong>$188\text{ m}$</strong></td>
            <td>World's best civilian resolution ($5.8\text{ m}$) in 1995; solid-state pushbroom CCDs</td>
          </tr>
          <tr>
            <td><strong>Resourcesat-1 / 2</strong></td>
            <td>2003 / 2011</td>
            <td>LISS-IV<br>LISS-III<br>AWiFS</td>
            <td><strong>$5.8\text{ m}$ (Multispectral!)</strong><br>$23.5\text{ m}$<br>$56\text{ m}$</td>
            <td>Multispectral LISS-IV imaging; AWiFS for rapid agricultural monitoring</td>
          </tr>
          <tr>
            <td><strong>Cartosat-1</strong></td>
            <td>2005</td>
            <td>PAN-Fore / PAN-Aft</td>
            <td>$2.5\text{ m}$ (Stereo)</td>
            <td>In-orbit along-track stereo for national 3D DEM generation</td>
          </tr>
          <tr>
            <td><strong>Cartosat-2 / 3</strong></td>
            <td>2007 / 2019</td>
            <td>Panchromatic / VNIR</td>
            <td>$< 0.8\text{ m}$ (Cartosat-2)<br><strong>$0.28\text{ m}$ (Cartosat-3)</strong></td>
            <td>Sub-meter cadastre, smart city urban planning, and defense reconnaissance</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- HIGH-YIELD PRACTICE QUESTIONS (8 QUESTIONS) -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Questions)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What was the spatial resolution of the SWIR band (Band 5: $1.55 - 1.70\ \mu\text{m}$) on the IRS-1D LISS-III sensor?
          <div class="pq-ans">✔ Correct Answer: $70.5\text{ meters}$ (with a swath of $148\text{ km}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> To maintain adequate signal-to-noise ratio with uncooled InGaAs linear array detectors in the lower solar flux SWIR region, pixel size was set at $70.5\text{ m}$ (exactly three times the $23.5\text{ m}$ VNIR pixel size).
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What scanning technology did LISS-III utilize instead of the oscillating scan mirrors used by Landsat TM?
          <div class="pq-ans">✔ Correct Answer: Pushbroom scanning (Linear Imaging Self-Scanning) using solid-state Charge-Coupled Device (CCD) arrays.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Pushbroom linear arrays image an entire cross-track line simultaneously as the satellite moves, achieving much longer dwell times per pixel and superior radiometric sensitivity.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What upgrade did ISRO introduce in the LISS-IV sensor flown on Resourcesat-1 (2003) compared to LISS-III?
          <div class="pq-ans">✔ Correct Answer: It delivered $5.8\text{ m}$ spatial resolution in three multispectral bands (Green, Red, NIR), whereas IRS-1D PAN was only panchromatic (monochrome) at $5.8\text{ m}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Resourcesat-1 was among the first satellites worldwide to achieve $< 6\text{ m}$ multi-band color imagery across a $23\text{ km}$ or $70\text{ km}$ swath.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What was the off-nadir steering capability of the IRS-1D PAN camera, and what capability did it enable?
          <div class="pq-ans">✔ Correct Answer: Up to $\pm 26^\circ$ across-track steering; enabled stereoscopic 3D terrain viewing and rapid revisit within 5 days.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> An optical mirror rotated to view the same ground target from two consecutive orbits, generating stereo pairs for topographic elevation extraction.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the revisit capability of the Wide Field Sensor (WiFS) on IRS-1D, and why was it chosen for national crop forecasting?
          <div class="pq-ans">✔ Correct Answer: 5-day revisit period with an $810\text{ km}$ swath.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Frequent 5-day coverage ensured cloud-free composite imagery during critical phenological growth stages of India's kharif and rabi crops.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What Indian ground station network receives, processes, and disseminates IRS-1D and Resourcesat satellite data?
          <div class="pq-ans">✔ Correct Answer: NRSC (National Remote Sensing Centre), Shadnagar Earth Station near Hyderabad.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> NRSC is the nodal agency under ISRO responsible for acquisition, processing, and archiving of all Indian Earth observation missions.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How does the radiometric quantization of IRS-1D LISS-III (7-bit / 8-bit) compare with Landsat-8 OLI (12-bit)?
          <div class="pq-ans">✔ Correct Answer: LISS-III quantizes signal into 128 (7-bit) or 256 (8-bit) gray levels; Landsat-8 OLI records 4,096 levels (12-bit scaled to 16-bit).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Higher bit depth prevents saturation over highly reflective targets and extracts subtle geological detail in steep shadow zones.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What was the operational life of IRS-1D, exceeding its designed mission life of 3 years?
          <div class="pq-ans">✔ Correct Answer: Over 10 years of active operational service (1997 to 2007+).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Excellent orbital insertion and onboard fuel management allowed IRS-1D to deliver valuable high-resolution imagery for more than a decade.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 19, part1, part2, part3)


# ==============================================================================
# Q020: SRTM 3D Topographic Data
# ==============================================================================
def generate_q020():
    title = "Q020: Spaceborne 3D Geodesy: Shuttle Radar Topography Mission (SRTM) & InSAR | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Digital Elevation Models & Radar Interferometry"
    h1_title = "Q020: Spaceborne 3D Geodesy: Shuttle Radar Topography Mission (SRTM) & InSAR"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 20<br>
<strong>Authoritative References:</strong> Farr, T.G. et al. (2007, <em>The Shuttle Radar Topography Mission</em>, Reviews of Geophysics, 45, RG2004); Thomas M. Lillesand et al., <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 7: InSAR & DEMs, pp. 448–454); Paul R. Wolf et al., <em>Elements of Photogrammetry</em> (4th Ed., Ch. 14)."""

    part1 = r"""
  <!-- CARD 1: THE SHUTTLE RADAR TOPOGRAPHY MISSION (SRTM) -->
  <div class="card">
    <div class="card-header bg-blue">1. The Shuttle Radar Topography Mission (SRTM): Breakthrough in 3D Geodesy</div>
    <div class="card-body">
      <p>In February 2000, NASA, the National Imagery and Mapping Agency (NIMA, now NGA), the German Aerospace Center (DLR), and the Italian Space Agency (ASI) conducted the <strong>Shuttle Radar Topography Mission (SRTM)</strong> aboard Space Shuttle <em>Endeavour</em> (Flight STS-99). SRTM accomplished an unprecedented geodetic triumph: acquiring a consistent, high-precision <strong>Three-Dimensional (3D) Digital Elevation Model (DEM)</strong> of Earth's land surface between latitudes $60^\circ\text{N}$ and $56^\circ\text{S}$, encompassing over $80\%$ of Earth's total landmass in just 11 days of flight.</p>

      <ul>
        <li><strong>Single-Pass Spaceborne Radar Interferometry (InSAR):</strong> Previous spaceborne radar interferometry (such as ERS-1/2) required "repeat-pass" orbits days or weeks apart, suffering severe decorrelation from wind, vegetation growth, and variable atmospheric water vapor. SRTM revolutionized radar geodesy by using <strong>Single-Pass Interferometry</strong>:
          <ul>
            <li><strong>Primary Main Antenna:</strong> Mounted rigidly inside the space shuttle's payload bay.</li>
            <li><strong>Secondary Outboard Antenna:</strong> Deployed at the tip of a lightweight, rigid carbon-fiber truss mast extending <strong>60 meters (197 feet)</strong> outward into space—representing the largest rigid human-made structure ever deployed in space!</li>
          </ul>
        </li>
        <li><strong>Simultaneous Transmission and Reception:</strong> Radar pulses transmitted from the main antenna were backscattered from the Earth's terrain and received simultaneously by both the main and outboard antennas, freezing the atmosphere and surface in an identical instant of time.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q20/srtm_shuttle_radar_3d_insar_geometry.png" alt="SRTM Space Shuttle 3D InSAR Geometry">
        <div class="tb-caption">
          <strong>Figure 20.1: SRTM Single-Pass Radar Interferometry Geometry.</strong> Showing the 60-meter mast separating the primary payload bay antenna from the outboard antenna, establishing a fixed interferometric baseline ($B$) to triangulate terrain elevation ($z$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE MATHEMATICAL PRINCIPLE OF RADAR INTERFEROMETRY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Interferometric Phase Difference ($\Delta\phi$) & Height Derivation</div>
    <div class="card-body">
      <p>The mathematical physics of extracting 3D ground topography ($z$) from dual-antenna radar interferometry relies on measuring the <strong>interferometric phase difference ($\Delta\phi$)</strong> between the two received microwave signals:</p>

      <div class="formula-card">
        <div class="formula-title">Interferometric Phase Difference & Elevation Derivation</div>
        $$\Delta\phi = \phi_1 - \phi_2 = \frac{2\pi}{\lambda} (R_1 - R_2) \approx \frac{2\pi}{\lambda} B \sin(\theta - \alpha)$$
        $$z = H - R_1 \cos\theta$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $\lambda$ is radar wavelength (C-band: $5.6\text{ cm}$; X-band: $3.1\text{ cm}$), $B$ is physical baseline length ($60\text{ m}$), $\alpha$ is baseline tilt angle, $\theta$ is look angle, and $H$ is shuttle altitude ($233\text{ km}$). Measuring $\Delta\phi$ to within fractions of a wavelength enables vertical height determination ($z$) to meter-level accuracy.</p>
      </div>

      <p>SRTM produced two primary global elevation datasets:</p>
      <ul>
        <li><strong>SRTM-1 (1 Arc-Second):</strong> Nominal ground spatial resolution of <strong>$30\text{ meters}$</strong> with an absolute vertical accuracy better than $\pm 16\text{ meters}$ (typically achieving $\pm 6 - 8\text{ m}$ in flat to moderate terrain).</li>
        <li><strong>SRTM-3 (3 Arc-Seconds):</strong> Averaged ground spatial resolution of <strong>$90\text{ meters}$</strong>, made globally accessible to researchers in 2003.</li>
      </ul>

      <div class="quote-box">
        "The Shuttle Radar Topography Mission (SRTM) successfully collected interferometric radar data covering more than 80% of Earth's land surface... providing the first high-resolution, homogeneous 3D digital topographic map of the world."
        <span class="quote-ref">— T.G. Farr et al., <em>The Shuttle Radar Topography Mission</em> (Reviews of Geophysics, 2007, 45, RG2004)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER SATELLITES FAIL (2D OPTICAL IMAGERY) -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Landsat, IKONOS & ERS as Primary Answers</div>
    <div class="card-body">
      <p>Understanding the distinction between 2D imagery and native 3D topographic mission architectures:</p>
      <ul>
        <li><strong>(A) LANDSAT:</strong> A classic nadir-looking <strong>2D multispectral optical imaging system</strong>. Landsat sensors (MSS, TM, ETM+, OLI) acquire 2D planar images of land reflectance ($x, y$ coordinates). They cannot measure vertical relief directly without external stereoscopic pairs or auxiliary DEMs.</li>
        <li><strong>(C) IKONOS:</strong> A commercial high-resolution 2D optical satellite ($0.8\text{ m}$ panchromatic, $4\text{ m}$ multispectral). While stereo pairs can be post-processed via optical photogrammetry into DEMs, IKONOS is an optical imager, not an inherently 3D topographic mission.</li>
        <li><strong>(D) ERS:</strong> ERS-1 and ERS-2 carried single radar antennas that required repeat-pass orbital passes (35 days apart) to perform interferometry, which suffered severe temporal decorrelation. SRTM was the definitive, dedicated mission created specifically to generate comprehensive 3D global topography.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 20)</div>
    <div class="q-stmt">
      Q20. Name the satellite providing three-dimensional topographic data :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) LANDSAT</div>
      <div class="raw-opt correct">(B) SRTM &nbsp;✔</div>
      <div class="raw-opt">(C) IKONOS</div>
      <div class="raw-opt">(D) ERS</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) SRTM</div>
      <div class="sub">
        The <strong>Shuttle Radar Topography Mission (SRTM)</strong> utilized single-pass dual-antenna radar interferometry (InSAR) aboard Space Shuttle <em>Endeavour</em> in 2000 to generate the world's premier high-resolution <strong>Three-Dimensional (3D) Digital Elevation Model (DEM)</strong> covering over 80% of Earth's landmass.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) LANDSAT</span>
      <span class="tag wrong">Incorrect (Planar 2D Multispectral Optical Satellite)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The Landsat series (Landsat-1 through 9) consists of nadir-pointing optical sensors producing planar two-dimensional (2D) multispectral reflectance images ($x, y$). They do not record native 3D topographic elevation data ($z$).
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) SRTM</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Flown in February 2000, SRTM was specifically engineered to map the Earth's topography in 3D. By deploying a 60-meter mast with an outboard radar antenna, it recorded single-pass interferometric phase shifts, creating the famous 30-meter and 90-meter near-global 3D Digital Elevation Models that serve as the universal topographic standard in geoscience and GIS.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) IKONOS</span>
      <span class="tag wrong">Incorrect (High-Resolution 2D Optical Satellite)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> IKONOS (launched in 1999) is an optical earth observation satellite designed for 2D high-resolution urban mapping and surveillance. It does not measure topographic heights natively via radar interferometry.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) ERS</span>
      <span class="tag wrong">Incorrect (Repeat-Pass Radar with High Temporal Decorrelation)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The European Remote Sensing satellites (ERS-1/2) carried single-antenna Synthetic Aperture Radars that required repeat-pass orbits (35-day repeat cycles), making global 3D topographic mapping unfeasible due to atmospheric changes and vegetative decorrelation.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison of Global 3D Digital Elevation Models (DEMs)</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Space Mission / Sensor</th>
            <th>Primary 3D Technology</th>
            <th>Global Spatial Resolution</th>
            <th>Vertical Accuracy ($LE90$)</th>
            <th>Global Coverage & Acquisition Year</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>SRTM (Endeavour STS-99)</strong></td>
            <td><strong>Single-Pass InSAR (C-band / X-band)</strong></td>
            <td><strong>$1\text{ arc-sec } (30\text{ m}) / 3\text{ arc-sec } (90\text{ m})$</strong></td>
            <td><strong>$\pm 6 - 16\text{ meters}$</strong></td>
            <td>$60^\circ\text{N} - 56^\circ\text{S}$ ($80\%$ of land); Feb 2000</td>
          </tr>
          <tr>
            <td><strong>TanDEM-X (DLR)</strong></td>
            <td>Bistatic Twin-Satellite InSAR (X-band)</td>
            <td>$0.4\text{ arc-sec } (12\text{ m})$</td>
            <td>$\pm 2 - 4\text{ meters}$</td>
            <td>Global pole-to-pole ($100\%$); 2010–2015</td>
          </tr>
          <tr>
            <td><strong>ASTER GDEM (Terra)</strong></td>
            <td>Optical Along-Track Stereoscopy (Bands 3N & 3B)</td>
            <td>$1\text{ arc-sec } (30\text{ m})$</td>
            <td>$\pm 15 - 20\text{ meters}$</td>
            <td>$83^\circ\text{N} - 83^\circ\text{S}$ (Optical stereo correlation); 2009–2019</td>
          </tr>
          <tr>
            <td><strong>ALOS AW3D30 (JAXA)</strong></td>
            <td>PRISM Optical Triplet Stereoscopy</td>
            <td>$1\text{ arc-sec } (30\text{ m})$ (resampled from $5\text{ m}$)</td>
            <td>$\pm 5\text{ meters}$</td>
            <td>Global land ($82^\circ\text{N} - 82^\circ\text{S}$); 2006–2011</td>
          </tr>
          <tr>
            <td><strong>Copernicus DEM (ESA)</strong></td>
            <td>Edited TanDEM-X InSAR</td>
            <td>$30\text{ m}$ (GLO-30) / $90\text{ m}$ (GLO-90)</td>
            <td>$\pm 4\text{ meters}$</td>
            <td>Global pole-to-pole; Released 2020</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- HIGH-YIELD PRACTICE QUESTIONS (8 QUESTIONS) -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Questions)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What was the physical length of the deployable mast deployed from Space Shuttle <em>Endeavour</em> during SRTM?
          <div class="pq-ans">✔ Correct Answer: 60 meters (197 feet).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The 60-meter mast separated the primary radar antenna inside the cargo bay from the outboard antenna, establishing the physical baseline ($B$) necessary to measure interferometric phase differences.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What two radar microwave frequency bands were simultaneously flown on SRTM?
          <div class="pq-ans">✔ Correct Answer: C-band ($\lambda = 5.6\text{ cm}$, by NASA/JPL) and X-band ($\lambda = 3.1\text{ cm}$, by DLR/ASI).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The C-band radar operated with ScanSAR mode to cover wide swaths ($225\text{ km}$), while the German/Italian X-band radar operated in high-resolution stripmap mode ($50\text{ km}$ swath).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the difference between a <em>Digital Surface Model (DSM)</em> and a <em>Digital Terrain Model (DTM)</em>, and which one does SRTM naturally produce?
          <div class="pq-ans">✔ Correct Answer: A DSM includes vegetation canopy tops and buildings; a DTM represents bare ground elevation. SRTM radar reflects off the upper tree canopy and is inherently a DSM.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because C-band microwaves ($\lambda = 5.6\text{ cm}$) scatter off forest foliage and tree branches, SRTM elevations in forested terrain are offset upward above bare Earth by a significant fraction of tree height.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Why does SRTM data contain "voids" (no-data gaps) in steep mountainous terrain (e.g., the Himalayas)?
          <div class="pq-ans">✔ Correct Answer: Due to radar shadow and extreme layover where steep slopes face away from or directly toward the radar antenna.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Extreme geometric distortion prevents phase unwrapping in steep relief, creating voids that have since been filled in Version 3 (SRTM Plus) using ASTER GDEM and topographic maps.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> In radar interferometry, what is the <em>altitude of ambiguity ($h_a$)</em>?
          <div class="pq-ans">✔ Correct Answer: The vertical elevation change that produces exactly one full $2\pi$ ($360^\circ$) interferometric phase cycle ($h_a = \frac{\lambda R \sin\theta}{B_{\perp}}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Shorter baselines have larger altitude of ambiguity (easier to unwrap phase but lower height precision); longer baselines have smaller $h_a$ (higher height precision but difficult phase unwrapping).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What mathematical process converts a cyclic, wrapped interferometric phase map ($-\pi$ to $+\pi$) into continuous, absolute terrain elevation?
          <div class="pq-ans">✔ Correct Answer: Phase Unwrapping (e.g., Minimum Cost Flow or Branch-Cut algorithms).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because radar phase is measured modulo $2\pi$, phase unwrapping integrates phase gradients across the interferogram to resolve the integer number of $2\pi$ phase cycles for every pixel.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is <em>DInSAR (Differential InSAR)</em>, and what geophysical phenomena can it measure with millimeter-level precision?
          <div class="pq-ans">✔ Correct Answer: Subtracting topographic phase from repeat-pass interferograms to measure surface crustal displacement from earthquakes, volcanic inflation, and land subsidence.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> DInSAR eliminates stationary topography, isolating tiny sub-centimeter line-of-sight surface deformations between satellite overpasses.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why did SRTM not acquire topographic data over the polar ice caps of Greenland and Antarctica?
          <div class="pq-ans">✔ Correct Answer: The Space Shuttle *Endeavour* had an orbital inclination of $57.0^\circ$, physically limiting ground coverage to between $60^\circ\text{N}$ and $56^\circ\text{S}$ latitudes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The shuttle's launch azimuth from Cape Canaveral constrained orbital inclination to $57^\circ$, leaving the high polar latitudes to be mapped later by polar satellites like CryoSat-2 and TanDEM-X.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 20, part1, part2, part3)


if __name__ == "__main__":
    for q_fn, q_name in [
        (generate_q016, "Q016_Radar_Real_vs_Synthetic_Aperture_Antenna_Complete_Guide.html"),
        (generate_q017, "Q017_Soil_Moisture_NIR_Reflectance_Absorption_Complete_Guide.html"),
        (generate_q018, "Q018_Vegetation_Reflectance_Chlorophyll_Pigment_Complete_Guide.html"),
        (generate_q019, "Q019_IRS_1D_LISS_III_Spatial_Resolution_Complete_Guide.html"),
        (generate_q020, "Q020_SRTM_Interferometric_SAR_3D_Topography_Complete_Guide.html"),
    ]:
        out_path = os.path.join(SOLUTIONS_DIR, q_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(q_fn())
        print(f"Generated {q_name}: {out_path} ({os.path.getsize(out_path)} bytes)")
