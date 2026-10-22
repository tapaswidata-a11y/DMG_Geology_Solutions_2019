#!/usr/bin/env python3
"""
Masterclass Builder for Batch 2: Remote Sensing & Photogrammetry (Q011 - Q015)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q011: Rayleigh Scattering
# ==============================================================================
def generate_q011():
    title = "Q011: Atmospheric Scattering Mechanics & Rayleigh Law | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Remote Sensing & Atmospheric Physics"
    h1_title = "Q011: Atmospheric Scattering Mechanics & Rayleigh Law"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 11<br>
<strong>Authoritative References:</strong> Thomas M. Lillesand, Ralph W. Kiefer & Jonathan W. Chipman, <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 1, pp. 9–14); John R. Jensen, <em>Remote Sensing of the Environment: An Earth Resource Perspective</em> (2nd Ed., pp. 48–52); Floyd F. Sabins, <em>Remote Sensing: Principles and Interpretation</em> (3rd Ed., pp. 18–22)."""

    part1 = r"""
  <!-- CARD 1: ATMOSPHERIC SCATTERING PHYSICS -->
  <div class="card">
    <div class="card-header bg-blue">1. Physics of Electromagnetic Scattering in the Atmosphere</div>
    <div class="card-body">
      <p>Before solar electromagnetic radiation reaches the Earth's surface or a satellite sensor, it interacts with gaseous molecules and suspended aerosols in the atmosphere. This interaction consists of <strong>absorption</strong> (conversion of radiant energy into thermal/kinetic energy) and <strong>scattering</strong> (unpredictable redirection of electromagnetic energy by particles). Atmospheric scattering is strictly governed by the ratio of particle diameter ($d$) to radiation wavelength ($\lambda$):</p>

      <ul>
        <li><strong>Rayleigh Scattering ($d \ll \lambda$):</strong> Molecular scattering caused by atmospheric gas molecules ($\text{N}_2, \text{O}_2$) whose effective diameter is much smaller than the wavelength of incident radiation ($d < 0.1\lambda$).</li>
        <li><strong>Mie Scattering ($d \approx \lambda$):</strong> Aerosol scattering caused by smoke, dust, pollen, and water vapor whose diameter approximately equals the radiation wavelength ($0.1\lambda \le d \le 10\lambda$).</li>
        <li><strong>Non-Selective Scattering ($d \gg \lambda$):</strong> Caused by large water droplets, cloud droplets, and ice crystals ($d > 10\lambda$), scattering all visible wavelengths equally and producing white clouds/fog.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Rayleigh's Inverse Fourth-Power Scattering Law (Lord Rayleigh, 1871)</div>
        $$I_{\text{scattered}} \propto \frac{1}{\lambda^4} \quad \text{or} \quad \sigma_R = \frac{8\pi^3 (n^2 - 1)^2}{3 N^2 \lambda^4}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $I$ is scattered radiance, $\lambda$ is wavelength, $n$ is refractive index, and $N$ is molecular density. Scattering intensity is inversely proportional to the fourth power of wavelength.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q11/rayleigh_scattering_curve.png" alt="Rayleigh Scattering Inverse Fourth Power Curve">
        <div class="tb-caption">
          <strong>Figure 11.1: Rayleigh Scattering Wavelength Dependence ($\lambda^{-4}$).</strong> The steep non-linear surge in scattering efficiency in the ultraviolet and blue spectrum ($0.40 - 0.45\ \mu\text{m}$) compared to the red and near-infrared spectrum ($0.70 - 1.0\ \mu\text{m}$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: WHY THE SKY IS BLUE AND SUNSETS ARE RED -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Optical Mechanism: Why the Sky is Blue & Sunsets are Red</div>
    <div class="card-body">
      <p>Applying Rayleigh's Law to the visible solar spectrum explains both daytime blue sky and sunset redness:</p>

      <ul>
        <li><strong>Blue Sky at Midday:</strong> Blue light has a wavelength of $\approx 0.40\ \mu\text{m}$, while red light has a wavelength of $\approx 0.70\ \mu\text{m}$. Comparing their scattering ratios:
        $$\frac{I_{\text{blue}}}{I_{\text{red}}} = \left(\frac{\lambda_{\text{red}}}{\lambda_{\text{blue}}}\right)^4 \approx \left(\frac{0.70}{0.40}\right)^4 = (1.75)^4 \approx 9.38$$
        Blue photons are scattered by nitrogen and oxygen molecules roughly <strong>9 to 10 times more efficiently</strong> than red photons. When an observer looks in any direction away from the direct solar disk, scattered blue photons enter the eye from all angles across the celestial dome.</li>
        <li><strong>Red Sunsets & Sunrises:</strong> At sunrise and sunset, solar rays travel through an atmospheric optical path length (air mass) up to 12 times thicker than at midday. Virtually all short blue and green wavelengths are scattered out of the direct line of sight, leaving only unscattered longer red and orange wavelengths to reach the observer.</li>
      </ul>

      <div class="quote-box">
        "Rayleigh scattering is the primary cause of the blue color of the clear sky. Because scattering intensity varies inversely with the fourth power of wavelength, blue light ($\approx 0.4\ \mu\text{m}$) is scattered almost 10 times more intensely than red light ($\approx 0.7\ \mu\text{m}$) by atmospheric gas molecules."
        <span class="quote-ref">— Lillesand, Kiefer & Chipman, <em>Remote Sensing and Image Interpretation</em> (7th Ed., 2015, p. 10)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: REMOTE SENSING IMPACT: ATMOSPHERIC HAZE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Impact on Optical Remote Sensing: Atmospheric Path Radiance ($L_p$)</div>
    <div class="card-body">
      <p>In satellite remote sensing, Rayleigh scattering introduces unwanted noise known as <strong>atmospheric path radiance ($L_p$)</strong> or "haze":</p>
      <ul>
        <li><strong>Contrast Reduction in Blue Band:</strong> Solar radiation scattered into the sensor's field of view without ever reaching the ground adds an additive offset ($L_{\text{total}} = L_{\text{surface}}\tau + L_p$), severely degrading image contrast in Landsat Band 1 (blue).</li>
        <li><strong>Haze Reduction Filters:</strong> In aerial photography and multispectral imaging, minus-blue filters (yellow filters, cut-off $< 0.50\ \mu\text{m}$) are deployed to eliminate Rayleigh haze.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 11)</div>
    <div class="q-stmt">
      Q11. What is responsible for the blue colour of the sky ?
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Mie Scattering</div>
      <div class="raw-opt">(B) Non-Selective Scattering</div>
      <div class="raw-opt correct">(C) Rayleigh Scattering &nbsp;✔</div>
      <div class="raw-opt">(D) Water droplets present in the sky</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Rayleigh Scattering</div>
      <div class="sub">
        The blue color of the clear sky is caused by <strong>Rayleigh scattering</strong> of sunlight by nitrogen and oxygen gas molecules whose diameters are much smaller than visible wavelengths ($d \ll \lambda$). Scattering intensity scales inversely with $\lambda^4$, dispersing blue light ($\sim 0.4\ \mu\text{m}$) nearly 10 times more intensely than red light.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Mie Scattering</span>
      <span class="tag wrong">Incorrect (Aerosol Scattering Generating White/Grey Haze)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Mie scattering occurs when atmospheric particles (smoke, dust, pollen) have diameters roughly equal to incident wavelengths ($d \approx \lambda$). Its wavelength dependence is much weaker ($\propto \lambda^{-1}$ to $\lambda^0$), scattering all colors across the visible spectrum and causing polluted or humid skies to appear milky-white or hazy rather than vivid blue.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Non-Selective Scattering</span>
      <span class="tag wrong">Incorrect (Equal Wavelength Scattering Generating Clouds/Fog)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Non-selective scattering is caused by particles much larger than visible light ($d > 10\lambda$, such as cloud water droplets $> 10\ \mu\text{m}$). It scatters all visible wavelengths with identical efficiency, which is why clouds and dense fog appear brilliantly white.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Rayleigh Scattering</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> First mathematically demonstrated by Lord Rayleigh in 1871, molecular scattering by atmospheric gases varies as $\lambda^{-4}$. Because blue photons have the shortest wavelengths in the dominant solar emission band, they undergo intense diffuse lateral scattering throughout the upper atmosphere, flooding the daytime sky with blue radiance.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Water droplets present in the sky</span>
      <span class="tag wrong">Incorrect (Liquid Droplets Cause Clouds and Rainbows, Not Blue Sky)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Liquid water droplets in the sky cause clouds, fog, and rain (via non-selective scattering) or rainbows (via refraction and internal reflection). A completely dry, clean atmosphere of pure nitrogen and oxygen produces the deepest, most saturated blue sky.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparative Matrix: Atmospheric Scattering Mechanisms</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Scattering Type</th>
            <th>Particle Size vs. Wavelength</th>
            <th>Scattering Particles</th>
            <th>Wavelength Dependency</th>
            <th>Visual & Remote Sensing Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Rayleigh Scattering</strong></td>
            <td><strong>$d \ll \lambda$</strong> ($d < 0.1\lambda$)</td>
            <td>Gas molecules ($\text{N}_2, \text{O}_2, \text{CO}_2$)</td>
            <td><strong>$I \propto \lambda^{-4}$</strong> (Extreme shortwave bias)</td>
            <td><strong>Blue sky</strong>; red sunsets; atmospheric haze in blue bands</td>
          </tr>
          <tr>
            <td><strong>Mie Scattering</strong></td>
            <td>$d \approx \lambda$ ($0.1\lambda \le d \le 10\lambda$)</td>
            <td>Aerosols, smoke, dust, pollen, fine water vapor</td>
            <td>$I \propto \lambda^{-n}$ ($n \approx 0.5 - 1.5$)</td>
            <td>Milky-white sky; reddish-brown urban smog; degrades NIR clarity</td>
          </tr>
          <tr>
            <td><strong>Non-Selective Scattering</strong></td>
            <td>$d \gg \lambda$ ($d > 10\lambda$)</td>
            <td>Cloud droplets ($> 10\ \mu\text{m}$), ice crystals, rain, fog</td>
            <td><strong>Wavelength independent</strong> ($\lambda^0$)</td>
            <td>White clouds and fog; complete optical opacity across visible and NIR</td>
          </tr>
          <tr>
            <td><strong>Raman Scattering</strong></td>
            <td>$d \ll \lambda$ (Inelastic)</td>
            <td>Molecules undergoing vibrational transitions</td>
            <td>Energy shift ($\Delta \nu$)</td>
            <td>Frequency shifts; utilized in atmospheric lidar profiling</td>
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
          <strong>Practice Q1 (Numerical Flux):</strong> Using Rayleigh's $\lambda^{-4}$ scattering law, compare the scattering intensity of violet light ($\lambda_1 = 0.40\ \mu\text{m}$) to near-infrared radiation ($\lambda_2 = 0.80\ \mu\text{m}$).
          <div class="pq-ans">✔ Worked Answer: Violet light is scattered $16\text{ times}$ more intensely than NIR radiation ($2^4 = 16$).</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            $$\frac{I_1}{I_2} = \left(\frac{\lambda_2}{\lambda_1}\right)^4 = \left(\frac{0.80}{0.40}\right)^4 = 2^4 = 16$$
            This shows why infrared imagery penetrates atmospheric haze with exceptional clarity compared to visible photography.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What optical filter is universally attached to aerial cameras to penetrate atmospheric Rayleigh haze?
          <div class="pq-ans">✔ Correct Answer: A "minus-blue" (haze) filter (e.g., Wratten 12 yellow filter) that absorbs wavelengths below $0.50\ \mu\text{m}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because Rayleigh scattering dominates in the violet and blue wavelengths ($< 0.50\ \mu\text{m}$), blocking these wavelengths eliminates scattered airlight, maximizing surface ground contrast.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> Why is the sky on the Moon or in deep space completely black even in broad daylight?
          <div class="pq-ans">✔ Correct Answer: The Moon lacks an atmosphere; in the absence of gaseous molecules, zero Rayleigh scattering occurs.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Without gas molecules to scatter sunlight into the shadows, solar rays travel in straight vacuum paths; shadows appear pitch-black and the daytime sky remains star-filled black.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In dark object subtraction (DOS) atmospheric correction of satellite imagery, how is path radiance ($L_p$) estimated?
          <div class="pq-ans">✔ Correct Answer: By extracting the minimum digital number (DN) recorded over completely dark targets (deep clear water or shadowed terrain).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Deep clear water has virtually zero natural reflectance in the NIR and visible; any positive signal recorded by the satellite is assumed to be additive atmospheric path radiance ($L_p$) caused by Rayleigh and Mie scattering.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Why do large volcanic eruptions (such as Mt. Pinatubo in 1991) cause brilliant, persistent purple sunsets worldwide?
          <div class="pq-ans">✔ Correct Answer: Injection of sub-micron sulfate aerosols into the stratosphere enhances forward Mie and Rayleigh scattering of red and blue light simultaneously.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Stratospheric aerosol droplets scatter unattenuated blue light from high altitudes while transmitted red light passes through the troposphere, combining visually to create brilliant purple and lavender twilights.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the phase function characteristic of pure Rayleigh scattering?
          <div class="pq-ans">✔ Correct Answer: Symmetrical forward and backward scattering ($P(\theta) \propto 1 + \cos^2\theta$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Unlike Mie scattering, which is heavily concentrated in the forward direction, Rayleigh scattering disperses radiation equally in both forward and backward directions with half the intensity at right angles ($90^\circ$).
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Why does Rayleigh scattering polarize scattered sky light at $90^\circ$ relative to the incident sun rays?
          <div class="pq-ans">✔ Correct Answer: Dipole oscillations of gas molecules can only oscillate perpendicular to the direction of propagation, producing $100\%$ linear polarization at right angles.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> This polarization enables polarizing filters to darken blue skies in photography and allows desert insects (e.g., honeybees) to navigate by celestial polarization patterns.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does Non-Selective scattering affect radar wavelengths ($> 1\text{ cm}$) differently than optical waves?
          <div class="pq-ans">✔ Correct Answer: Cloud droplets ($10\ \mu\text{m}$) are much smaller than radar wavelengths, meaning clouds behave as Rayleigh scatterers for radar, allowing microwaves to penetrate clouds without attenuation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> For optical waves ($0.5\ \mu\text{m}$), cloud droplets ($10\ \mu\text{m}$) are massive ($d \gg \lambda$, non-selective). But for C-band radar ($\lambda = 5.6\text{ cm}$), cloud droplets are tiny ($d \ll \lambda$), rendering clouds transparent to radar sensors.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 11, part1, part2, part3)


# ==============================================================================
# Q012: Vibrational Energy in SWIR and TIR
# ==============================================================================
def generate_q012():
    title = "Q012: Quantum Molecular Energy States: SWIR & TIR Vibrational Transitions | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Remote Sensing & Spectroscopy"
    h1_title = "Q012: Quantum Molecular Energy States: SWIR & TIR Vibrational Transitions"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 12<br>
<strong>Authoritative References:</strong> Roger N. Clark, <em>Spectroscopy of Rocks and Minerals, and Principles of Spectroscopy</em> (USGS Manual, 1999); Floyd F. Sabins, <em>Remote Sensing: Principles and Interpretation</em> (3rd Ed., Ch. 4: Mineral Exploration, pp. 88–95); John R. Jensen, <em>Remote Sensing of the Environment</em> (Ch. 13); Hunt, G.R. (1977, <em>Spectral signatures of particulate minerals</em>, Geophysics, 42, pp. 501–513)."""

    part1 = r"""
  <!-- CARD 1: QUANTUM ENERGY STATES & THE EMS -->
  <div class="card">
    <div class="card-header bg-blue">1. Quantum Energy States & Spectral Transitions Across the EMS</div>
    <div class="card-body">
      <p>When electromagnetic radiation interacts with matter, photons are selectively absorbed at resonant frequencies corresponding to discrete quantum energy transitions within atoms, crystal lattices, and molecules. In optical remote sensing and mineral spectroscopy (Hunt, 1977; Clark, 1999), radiation is partitioned into fundamental physical interaction domains:</p>

      <ul>
        <li><strong>Electronic Transitions (UV, Visible, & NIR: $0.1 - 1.0\ \mu\text{m}$):</strong> Transitions of valence electrons between discrete atomic orbitals (crystal field splitting, charge transfer, conduction band transitions). Examples: $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ absorption bands in iron oxides (hematite, goethite) at $0.85 - 0.95\ \mu\text{m}$.</li>
        <li><strong>Vibrational Transitions (SWIR & TIR: $1.4 - 14.0\ \mu\text{m}$):</strong> Mechanical stretching and bending vibrations of covalent chemical bonds within molecular radicals (e.g., $\text{O-H}, \text{Al-OH}, \text{Mg-OH}, \text{CO}_3^{2-}, \text{Si-O}$). Fundamental vibrations occur in the Thermal Infrared (TIR, $8 - 14\ \mu\text{m}$), while their overtone and combination modes occur in the Short-Wave Infrared (SWIR, $1.4 - 2.5\ \mu\text{m}$).</li>
        <li><strong>Rotational Transitions (Far-IR & Microwave: $> 100\ \mu\text{m} - 1\text{ m}$):</strong> End-over-end rotational motions of free dipolar gaseous molecules (e.g., water vapor rotations in the microwave band).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Quantum Harmonic Oscillator Energy Equation</div>
        $$E_v = \left(v + \frac{1}{2}\right) h \nu_0 = \left(v + \frac{1}{2}\right) \frac{h}{2\pi} \sqrt{\frac{k}{\mu}}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $v$ is vibrational quantum number, $h$ is Planck's constant, $k$ is interatomic chemical bond force constant, and $\mu = \frac{m_1 m_2}{m_1 + m_2}$ is reduced mass. Bond vibrations require infrared photon energies.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q12/swir_tir_vibrational_spectroscopy.png" alt="SWIR and TIR Vibrational Spectroscopy Transitions">
        <div class="tb-caption">
          <strong>Figure 12.1: Quantum Energy Transitions Across the Electromagnetic Spectrum.</strong> Illustrates electronic orbital transitions in the UV-VNIR, overtone/combination vibrational bands in the SWIR ($1.4 - 2.5\ \mu\text{m}$), and fundamental vibrational reststrahlen bands in the TIR ($8 - 14\ \mu\text{m}$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: SWIR OVERTONES & MINERAL SPECTRAL MAPPING -->
  <div class="card">
    <div class="card-header bg-indigo">2. SWIR Vibrational Overtones ($1.4 - 2.5\ \mu\text{m}$) in Mineral Exploration</div>
    <div class="card-body">
      <p>The Short-Wave Infrared (SWIR, $1.4 - 2.5\ \mu\text{m}$) region is the most critical window in geological remote sensing for hydrothermal alteration mapping:</p>

      <ul>
        <li><strong>Al-OH Minerals (Phyllic Alteration):</strong> Illite, muscovite, kaolinite, and pyrophyllite display diagnostic vibrational absorption doublets at <strong>$2.20\ \mu\text{m}$</strong> due to combination stretching and bending of aluminum-hydroxyl bonds.</li>
        <li><strong>Mg-OH Minerals (Propylitic Alteration):</strong> Chlorite, epidote, and talc display sharp vibrational absorption features at <strong>$2.30 - 2.35\ \mu\text{m}$</strong> due to magnesium-hydroxyl vibrations.</li>
        <li><strong>Carbonates ($\text{CO}_3^{2-}$):</strong> Calcite and dolomite show intense asymmetric stretching overtones at <strong>$2.33\ \mu\text{m}$</strong> and $2.50\ \mu\text{m}$.</li>
      </ul>

      <div class="quote-box">
        "Vibrational processes produce absorption bands in the short-wave infrared (SWIR, 1.3 to 2.5 $\mu$m) and thermal infrared (TIR, 8 to 14 $\mu$m). In the SWIR, overtones and combination tones of OH, H2O, CO3, and Al-OH or Mg-OH bonds allow precise identification of clay and carbonate minerals."
        <span class="quote-ref">— Floyd F. Sabins, <em>Remote Sensing: Principles and Interpretation</em> (3rd Ed., 1997, p. 89)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: TIR FUNDAMENTAL RESTSTRAHLEN BANDS -->
  <div class="card">
    <div class="card-header bg-emerald">3. TIR Fundamental Vibrations ($8 - 14\ \mu\text{m}$): The Reststrahlen Band</div>
    <div class="card-body">
      <p>In the Thermal Infrared (TIR, $8 - 14\ \mu\text{m}$), fundamental stretching vibrations of silicon-oxygen ($\text{Si-O-Si}$) tetrahedral bonds produce intense reflectance peaks accompanied by emissivity minima known as <strong>Reststrahlen bands</strong>:</p>
      <ul>
        <li><strong>Silica Polymerization Shift:</strong> In quartz and felsic rocks (framework silicates), the reststrahlen minimum occurs around $8.5 - 9.0\ \mu\text{m}$. In mafic and ultramafic rocks (isolated tetrahedral olivine, pyroxene), it shifts systematically to longer wavelengths ($10.5 - 11.5\ \mu\text{m}$), allowing direct mapping of rock lithology using ASTER thermal bands.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 12)</div>
    <div class="q-stmt">
      Q12. The vibrational energy of an object is associated with the _____ of the electromagnetic spectrum.
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) UV and Photo UV region</div>
      <div class="raw-opt correct">(B) SWIR and TIR region &nbsp;✔</div>
      <div class="raw-opt">(C) Visible and NIR region</div>
      <div class="raw-opt">(D) Microwave and Radio wave region</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) SWIR and TIR region</div>
      <div class="sub">
        In molecular spectroscopy and remote sensing, <strong>vibrational energy transitions</strong> (bond stretching and bending of $\text{O-H}, \text{Al-OH}, \text{Mg-OH}, \text{CO}_3$, and $\text{Si-O}$) are strictly associated with the <strong>Short-Wave Infrared (SWIR: $1.4 - 2.5\ \mu\text{m}$)</strong> and <strong>Thermal Infrared (TIR: $8 - 14\ \mu\text{m}$)</strong> regions.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) UV and Photo UV region</span>
      <span class="tag wrong">Incorrect (High-Energy Electronic Ionization Transitions)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The ultraviolet ($< 0.40\ \mu\text{m}$) region contains exceptionally high photon energies ($E = h\nu = 3.1 - 100\text{ eV}$) that drive deep valence electron excitation, photo-ionization, and molecular dissociation—not mechanical vibrational bond oscillations.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) SWIR and TIR region</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Molecular vibrational bonds have resonant frequencies whose energy quanta precisely match infrared photons. The fundamental bending and stretching vibrational modes occur directly in the Thermal Infrared (TIR, $8 - 14\ \mu\text{m}$), while their overtone and combination vibrational modes dominate the Short-Wave Infrared (SWIR, $1.4 - 2.5\ \mu\text{m}$).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Visible and NIR region</span>
      <span class="tag wrong">Incorrect (Electronic Orbital Transitions)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Spectral features in the Visible ($0.4 - 0.7\ \mu\text{m}$) and Near-Infrared ($0.7 - 1.1\ \mu\text{m}$) regions are driven by <em>electronic processes</em>, such as crystal-field transitions in transition metal cations ($\text{Fe}^{2+}, \text{Fe}^{3+}$ in iron oxides) and chlorophyll pigment absorption in green leaves.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Microwave and Radio wave region</span>
      <span class="tag wrong">Incorrect (Low-Energy Rotational & Macroscopic Interactions)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Microwave and radio waves have very low photon energies ($< 10^{-4}\text{ eV}$), which correspond to end-over-end molecular rotation in free gases or macroscopic surface scattering and dielectric interactions, lacking sufficient energy to excite interatomic vibrational modes.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Quantum Spectrum Matrix: Energy States vs. Spectral Windows</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Spectral Region</th>
            <th>Wavelength Range ($\lambda$)</th>
            <th>Primary Quantum / Physical Mechanism</th>
            <th>Diagnostic Geological & Remote Sensing Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Ultraviolet (UV)</strong></td>
            <td>$0.01 - 0.40\ \mu\text{m}$</td>
            <td>Outer electron excitation, photo-ionization</td>
            <td>Atmospheric ozone absorption; carbonate fluorescence</td>
          </tr>
          <tr>
            <td><strong>Visible & NIR (VNIR)</strong></td>
            <td>$0.40 - 1.10\ \mu\text{m}$</td>
            <td><strong>Electronic transitions</strong>, crystal field splitting</td>
            <td>Chlorophyll absorption ($0.45, 0.65\ \mu\text{m}$); $\text{Fe}^{3+}$ hematite absorption ($0.86\ \mu\text{m}$)</td>
          </tr>
          <tr>
            <td><strong>Short-Wave Infrared (SWIR)</strong></td>
            <td><strong>$1.40 - 2.50\ \mu\text{m}$</strong></td>
            <td><strong>Vibrational overtones & combination modes</strong></td>
            <td><strong>Al-OH clays ($2.20\ \mu\text{m}$); Mg-OH chlorite ($2.32\ \mu\text{m}$); $\text{CO}_3^{2-}$ carbonates</strong></td>
          </tr>
          <tr>
            <td><strong>Thermal Infrared (TIR)</strong></td>
            <td><strong>$8.0 - 14.0\ \mu\text{m}$</strong></td>
            <td><strong>Fundamental molecular bond stretching/bending</strong></td>
            <td><strong>$\text{Si-O-Si}$ Reststrahlen band; quartz/silicate differentiation; surface kinetic temp</strong></td>
          </tr>
          <tr>
            <td><strong>Microwave</strong></td>
            <td>$1.0\text{ mm} - 1.0\text{ m}$</td>
            <td>Molecular rotation; macroscopic dielectric polarization</td>
            <td>SAR backscatter; soil moisture dielectric constant ($\epsilon_r$); surface roughness</td>
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
          <strong>Practice Q1:</strong> Which specific molecular bond combination causes the diagnostic $2.20\ \mu\text{m}$ absorption band in illite, kaolinite, and muscovite?
          <div class="pq-ans">✔ Correct Answer: The combination of the $\text{Al-O-H}$ bending fundamental with the $\text{O-H}$ stretching fundamental.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The fundamental $\text{O-H}$ stretch occurs at $\sim 2.7\ \mu\text{m}$ and the $\text{Al-OH}$ bend at $\sim 11\ \mu\text{m}$; their quantum mechanical combination produces the diagnostic $2.20\ \mu\text{m}$ overtone used globally to map phyllic alteration.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>Reststrahlen band</em> in thermal infrared spectroscopy?
          <div class="pq-ans">✔ Correct Answer: A sharp fundamental reflectance peak (emissivity trough) caused by resonant mechanical vibration of $\text{Si-O}$ crystal lattices.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Coined from the German for "residual rays", Reststrahlen bands occur between $8.5 - 12\ \mu\text{m}$ where resonant silicate vibrations prevent photon transmission, maximizing specular reflectance and producing an emissivity minimum.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> How does the position of the Reststrahlen minimum shift from felsic (granitic) to ultramafic (peridotitic) rocks?
          <div class="pq-ans">✔ Correct Answer: It shifts systematically from shorter wavelengths ($\sim 8.5\ \mu\text{m}$ in quartz) to longer wavelengths ($\sim 11.0\ \mu\text{m}$ in olivine).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Highly polymerized framework silicates (quartz, feldspar) have stronger, stiffer bond networks than isolated $\text{SiO}_4$ tetrahedra, shifting resonant vibrational frequencies to higher energy (shorter wavelengths).
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Why do liquid water and water vapor produce broad absorption bands at $1.4\ \mu\text{m}$ and $1.9\ \mu\text{m}$?
          <div class="pq-ans">✔ Correct Answer: Overtones and combination modes of the asymmetric stretch ($\nu_3$) and bending ($\nu_2$) of the water molecule ($\text{H}_2\text{O}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Free water molecules have fundamental vibrations at $2.66\ \mu\text{m}$ ($\nu_1$), $6.27\ \mu\text{m}$ ($\nu_2$), and $2.74\ \mu\text{m}$ ($\nu_3$). The $1.9\ \mu\text{m}$ band is the combination $\nu_2 + \nu_3$, while $1.4\ \mu\text{m}$ is the first overtone of $\text{O-H}$ stretching.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> In satellite multispectral imaging, which ASTER sensor subsystems cover the vibrational absorption bands?
          <div class="pq-ans">✔ Correct Answer: The SWIR subsystem (Bands 4–9: $1.60 - 2.43\ \mu\text{m}$) and TIR subsystem (Bands 10–14: $8.125 - 11.65\ \mu\text{m}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> ASTER was specifically engineered with 6 contiguous SWIR bands to resolve clay/carbonate overtones and 5 TIR bands to resolve silicate Reststrahlen features.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What quantum transition explains why hematite ($\alpha\text{-Fe}_2\text{O}_3$) appears red in the visible spectrum and displays a broad reflectance trough around $0.86\ \mu\text{m}$?
          <div class="pq-ans">✔ Correct Answer: Electronic crystal field splitting of the $3d$ orbital energy levels of the ferric ion ($\text{Fe}^{3+}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Electric fields from surrounding oxygen ligands split the $3d$ electron orbitals, absorbing green and blue photons ($^6A_1 \to\ ^4T_1, ^4T_2$), while reflecting red photons.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Why can remote sensors not observe ground vibrational features in the $5.5 - 7.5\ \mu\text{m}$ spectral region?
          <div class="pq-ans">✔ Correct Answer: Severe atmospheric opacity caused by the fundamental bending vibration ($\nu_2$) of atmospheric water vapor centered at $6.27\ \mu\text{m}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> This region is a complete atmospheric absorption window closure, where solar and terrestrial radiation cannot penetrate to or from the ground.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> How does the spectral signature of calcite ($\text{CaCO}_3$) differ from dolomite ($\text{CaMg}(\text{CO}_3)_2$) in the SWIR vibrational band?
          <div class="pq-ans">✔ Correct Answer: Calcite absorbs at $2.335\ \mu\text{m}$, while dolomite absorbs at a slightly shorter wavelength of $2.315\ \mu\text{m}$ due to magnesium cation substitution.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Smaller $\text{Mg}^{2+}$ ions increase the interatomic bond force constant, shifting the carbonate vibrational combination band toward shorter wavelengths.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 12, part1, part2, part3)


# ==============================================================================
# Q013: Sun-Synchronous Orbit
# ==============================================================================
def generate_q013():
    title = "Q013: Orbital Mechanics of Sun-Synchronous Earth Observation Satellites | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Satellite Remote Sensing & Orbital Mechanics"
    h1_title = "Q013: Orbital Mechanics of Sun-Synchronous Earth Observation Satellites"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 13<br>
<strong>Authoritative References:</strong> Thomas M. Lillesand, Ralph W. Kiefer & Jonathan W. Chipman, <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 6, pp. 385–395); John R. Jensen, <em>Remote Sensing of the Environment</em> (2nd Ed., pp. 64–68); Elachi, C. & van Zyl, J., <em>Introduction to the Physics and Techniques of Remote Sensing</em> (2nd Ed., Wiley)."""

    part1 = r"""
  <!-- CARD 1: SUN-SYNCHRONOUS ORBITAL MECHANICS -->
  <div class="card">
    <div class="card-header bg-blue">1. Orbital Mechanics & Synchronization with Local Solar Time</div>
    <div class="card-body">
      <p>A <strong>Sun-Synchronous Orbit (SSO)</strong> is a specialized quasi-polar low Earth orbit (LEO, typically altitudes of $600 - 900\text{ km}$) engineered such that the satellite passes over any given geographic latitude at exactly the same <strong>Local Solar Time (LST)</strong> on every single pass throughout the entire year.</p>

      <ul>
        <li><strong>Synchronization with Local Solar Time:</strong> Because the Earth rotates once every 24 hours while orbiting the Sun over 365.25 days, the satellite's orbital plane must rotate (precess) eastward in inertial space at an angular velocity of exactly:
        $$\dot{\Omega} = \frac{360^\circ}{365.2422\text{ days}} \approx +0.9856^\circ/\text{day}$$
        This ensures that the satellite maintains a constant geometric orientation relative to the Sun, crossing the Equator at an identical local time (e.g., 10:00 AM or 10:30 AM local time on descending pass for Landsat and IRS-1C/1D).</li>
        <li><strong>Nodal Precession Driven by Earth's Oblateness ($J_2$):</strong> The Earth is not a perfect sphere; its equatorial bulge ($J_2 = 1.08263 \times 10^{-3}$) exerts a gravitational torque on inclined orbits, causing the ascending node ($\Omega$) to precess.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Nodal Precession Rate Formula (Lagrange Perturbation Theory)</div>
        $$\dot{\Omega} = -\frac{3}{2} J_2 R_E^2 \sqrt{\mu} \, a^{-7/2} \, (1 - e^2)^{-2} \, \cos i$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $R_E$ is Earth's equatorial radius ($6378\text{ km}$), $a$ is semi-major axis, $e$ is eccentricity, and $i$ is orbital inclination. To make $\dot{\Omega} > 0$ ($+0.9856^\circ/\text{day}$), $\cos i$ must be negative—requiring a <strong>retrograde inclination ($i > 90^\circ$, typically $97.5^\circ - 98.8^\circ$)</strong>.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q13/sun_synchronous_orbit_geometry.png" alt="Sun Synchronous Orbit Geometry and Precession">
        <div class="tb-caption">
          <strong>Figure 13.1: Geometry of a Sun-Synchronous Polar Orbit.</strong> Illustrates nodal precession of $0.9856^\circ/\text{day}$ matching Earth's revolution around the Sun, maintaining a fixed solar illumination angle on every overpass.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: WHY CONSTANT SOLAR ILLUMINATION MATTERS -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Remote Sensing Advantage: Consistent Solar Illumination & Shadowing</div>
    <div class="card-body">
      <p>Why is synchronization with <strong>Local Solar Time</strong> essential for optical earth observation satellites (Landsat, Sentinel-2, IRS, SPOT)?</p>

      <ul>
        <li><strong>Consistent Solar Zenith & Azimuth Angles:</strong> By imaging each scene at the identical local solar hour (typically 10:00 to 10:30 AM), variations in terrain shadow and illumination geometry between successive revisit cycles are minimized, enabling reliable multitemporal change detection.</li>
        <li><strong>Optimal Radiometric Balance:</strong> A morning overpass time of 10:30 AM provides high solar elevation (sufficient radiometric signal-to-noise ratio) while avoiding the afternoon convective cloud build-up and thermal haze typical of tropical and monsoon regions.</li>
      </ul>

      <div class="quote-box">
        "A sun-synchronous orbit is one in which the satellite's orbital plane precesses eastward at the same rate that the Earth moves around the sun... Thus, the satellite crosses the equator at the same local solar time on each pass, ensuring consistent illumination conditions from pass to pass."
        <span class="quote-ref">— Lillesand, Kiefer & Chipman, <em>Remote Sensing and Image Interpretation</em> (7th Ed., 2015, p. 388)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON WITH GEOSTATIONARY ORBITS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Sun-Synchronous vs. Geostationary Satellites (Distractor Analysis)</div>
    <div class="card-body">
      <p>Candidates must strictly distinguish Sun-Synchronous satellites from Geostationary platforms:</p>
      <ul>
        <li><strong>Geostationary Orbits (GEO):</strong> Altitude of exactly $35,786\text{ km}$ directly over the Equator ($i = 0^\circ$). Orbital period equals Earth's rotational period ($23\text{h } 56\text{m } 04\text{s}$). The satellite remains permanently stationary relative to a single fixed area on Earth's surface (Option A/C). Used for weather monitoring (INSAT, GOES) and communications.</li>
        <li><strong>Sun-Synchronous Orbits (SSO):</strong> Near-polar retrograde orbit ($i \approx 98^\circ$) at low altitude ($600 - 800\text{ km}$) with a period of $\approx 90 - 100\text{ minutes}$. It continually scans new swaths across the entire globe as the Earth rotates underneath.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 13)</div>
    <div class="q-stmt">
      Q13. In Sun Synchronous orbit, the satellite is synchronized with :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Particular area of the Earth</div>
      <div class="raw-opt correct">(B) Local Solar time &nbsp;✔</div>
      <div class="raw-opt">(C) Stationary on the Equator</div>
      <div class="raw-opt">(D) Stationary on the Pole</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Local Solar time</div>
      <div class="sub">
        In a <strong>Sun-Synchronous orbit</strong>, the nodal precession rate ($0.9856^\circ/\text{day}$) is matched to Earth's orbital period around the Sun, ensuring that the satellite passes over any given geographic point at the exact same <strong>Local Solar Time</strong> on every pass.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Particular area of the Earth</span>
      <span class="tag wrong">Incorrect (Confuses SSO with Geostationary Orbit)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A satellite that remains permanently synchronized over a "particular area of the Earth" is in a <em>Geostationary orbit (GEO)</em> at $35,786\text{ km}$ above the equator. Sun-synchronous satellites move continuously in near-polar orbits, imaging the entire planet over a repetitive cycle (e.g., 16-day repeat cycle for Landsat).
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Local Solar time</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> The defining physical property of a Sun-Synchronous orbit is that its orbital plane precesses at exactly $0.9856^\circ/\text{day}$, matching the mean motion of the Sun. As a direct consequence, the satellite crosses the equator and each line of latitude at an invariant <strong>Local Solar Time</strong>, providing consistent sun illumination and shadow angles essential for earth resources mapping.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Stationary on the Equator</span>
      <span class="tag wrong">Incorrect (Definition of Geostationary Orbit)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Being stationary over the Equator defines a <em>Geostationary equatorial orbit</em> ($i = 0^\circ, h = 35,786\text{ km}$), such as meteorological satellites (Meteosat, INSAT-3D). Sun-synchronous satellites have retrograde near-polar inclinations ($i \approx 98^\circ$) and cross the equator twice every orbit.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Stationary on the Pole</span>
      <span class="tag wrong">Incorrect (Physically Impossible Orbit)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A satellite cannot remain "stationary on the pole" under orbital mechanics; gravity requires an orbit to encircle Earth's center of mass. High-latitude surveillance uses highly eccentric 12-hour <em>Molniya orbits</em> ($i = 63.4^\circ$), not stationary polar hover.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Orbit Comparison: Sun-Synchronous vs. Geostationary vs. Molniya</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Orbital Parameter</th>
            <th>Sun-Synchronous Orbit (SSO)</th>
            <th>Geostationary Orbit (GEO)</th>
            <th>Molniya Orbit</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Synchronization Target</strong></td>
            <td><strong>Local Solar Time (LST)</strong></td>
            <td>Earth's rotational velocity ($\omega_E$)</td>
            <td>Semi-synchronous (12 hours)</td>
          </tr>
          <tr>
            <td><strong>Typical Altitude ($h$)</strong></td>
            <td>Low Earth Orbit: <strong>$600 - 900\text{ km}$</strong></td>
            <td>High Altitude: <strong>$35,786\text{ km}$</strong></td>
            <td>Highly Eccentric: $600\text{ km}$ perigee / $40,000\text{ km}$ apogee</td>
          </tr>
          <tr>
            <td><strong>Orbital Inclination ($i$)</strong></td>
            <td><strong>Retrograde: $97.5^\circ - 98.8^\circ$</strong></td>
            <td>Equatorial: <strong>$0^\circ$</strong></td>
            <td>Critical: $63.4^\circ$ (zero apsidal drift)</td>
          </tr>
          <tr>
            <td><strong>Orbital Period ($T$)</strong></td>
            <td>$\approx 96 - 100\text{ minutes}$ ($14 - 15\text{ orbits/day}$)</td>
            <td>$23\text{ hours, } 56\text{ minutes, } 4\text{ seconds}$</td>
            <td>$12\text{ hours}$</td>
          </tr>
          <tr>
            <td><strong>Primary Application</strong></td>
            <td>High-resolution optical mapping (Landsat, Sentinel, IRS)</td>
            <td>Real-time meteorology (INSAT, GOES) & telecommunications</td>
            <td>High-latitude Arctic communications & reconnaissance</td>
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
          <strong>Practice Q1 (Numerical):</strong> Calculate the daily nodal precession rate ($\dot{\Omega}$) required for a satellite to maintain a Sun-synchronous orbit over a tropical year of $365.2422\text{ days}$.
          <div class="pq-ans">✔ Worked Answer: $\dot{\Omega} = +0.9856^\circ/\text{day}$ (eastward).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\dot{\Omega} = \frac{360^\circ}{365.2422\text{ days}} = +0.985647^\circ/\text{day}$$
            This matches the apparent annual motion of the Sun across the celestial sphere.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Why must a Sun-synchronous orbit possess a <em>retrograde inclination</em> ($i > 90^\circ$)?
          <div class="pq-ans">✔ Correct Answer: Because $\dot{\Omega} \propto -\cos i$; to achieve positive (eastward) precession matching the Sun's motion, $\cos i$ must be negative.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In Lagrange's perturbation equation, nodal precession is driven by Earth's equatorial oblateness ($J_2$). For prograde orbits ($i < 90^\circ$), the node regresses westward; only retrograde orbits ($i > 90^\circ$) precess eastward.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the standard equator crossing time for Landsat-8/9 and IRS-1C/1D on their descending (daylight) pass?
          <div class="pq-ans">✔ Correct Answer: 10:00 AM to 10:30 AM Local Solar Time.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Mid-morning (10:00–10:30 AM) minimizes convective cloud formation while providing high solar elevation angles ($45^\circ - 65^\circ$) for optical reflectance.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is the difference between an <em>ascending node</em> and a <em>descending node</em> in satellite tracking?
          <div class="pq-ans">✔ Correct Answer: Ascending node is where the ground track crosses the equator from South to North; descending node is where it crosses from North to South.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Most optical imaging satellites record daylight imagery on the descending (north-to-south) pass and traverse the night hemisphere on the ascending pass.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a <em>dawn-dusk</em> Sun-synchronous orbit, and which remote sensing sensors use it?
          <div class="pq-ans">✔ Correct Answer: An orbit where the satellite rides the day-night terminator (6:00 AM / 6:00 PM), used by Synthetic Aperture Radar (SAR) satellites like RADARSAT and Sentinel-1.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Dawn-dusk orbits provide continuous solar illumination on the satellite's solar panels (no eclipse shadows), powering high-energy radar transmissions continuously.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> In orbital mechanics, what is the significance of the critical inclination $i = 63.4^\circ$?
          <div class="pq-ans">✔ Correct Answer: The inclination where rate of apsidal drift (rotation of the semi-major axis in the orbital plane) is exactly zero ($\dot{\omega} = 0$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Used by Russian Molniya orbits to permanently anchor the apogee over the Northern Hemisphere.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How is the orbital period ($T$) of a low Earth orbit satellite at an altitude of $705\text{ km}$ (e.g., Landsat) calculated using Kepler's Third Law?
          <div class="pq-ans">✔ Worked Answer: $T \approx 98.9\text{ minutes}$ ($\approx 14.5\text{ orbits per day}$).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            Semi-major axis $a = R_E + h = 6378 + 705 = 7083\text{ km} = 7.083 \times 10^6\text{ m}$.<br>
            $$T = 2\pi \sqrt{\frac{a^3}{\mu}} = 2\pi \sqrt{\frac{(7.083 \times 10^6)^3}{3.986 \times 10^{14}}} = 2\pi \sqrt{8.92 \times 10^5} \approx 5935\text{ s} \approx 98.9\text{ min}$$
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What causes the ground track of a Sun-synchronous satellite to shift westward on each successive orbit?
          <div class="pq-ans">✔ Correct Answer: The rotation of the Earth beneath the fixed orbital plane during the 99-minute orbital period.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> During one 99-minute orbit, Earth rotates eastward by $15^\circ/\text{hr} \times 1.65\text{ hr} \approx 24.75^\circ$ of longitude, shifting the ground track westward by $\sim 2750\text{ km}$ at the equator.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 13, part1, part2, part3)


# ==============================================================================
# Q014: Spatial Resolution and Ground Clarity
# ==============================================================================
def generate_q014():
    title = "Q014: Sensor Resolution Hierarchy: Spatial, Spectral, Temporal & Radiometric | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Remote Sensing & Image Quality"
    h1_title = "Q014: Sensor Resolution Hierarchy: Spatial, Spectral, Temporal & Radiometric"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 14<br>
<strong>Authoritative References:</strong> Thomas M. Lillesand, Ralph W. Kiefer & Jonathan W. Chipman, <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 1, pp. 32–37); John R. Jensen, <em>Remote Sensing of the Environment</em> (2nd Ed., pp. 12–22); Paul R. Wolf, Bon A. Dewitt & Benjamin E. Wilkinson, <em>Elements of Photogrammetry with Applications in GIS</em> (4th Ed., McGraw-Hill)."""

    part1 = r"""
  <!-- CARD 1: THE FOUR RESOLUTIONS OF REMOTE SENSING -->
  <div class="card">
    <div class="card-header bg-blue">1. The Four Fundamental Resolutions of Remote Sensing</div>
    <div class="card-body">
      <p>The capability of an imaging sensor to capture and discriminate ground features is governed by the <strong>Four Fundamental Resolutions</strong> of remote sensing (Lillesand et al., 2015; Jensen, 2007):</p>

      <ul>
        <li><strong>(A) Spatial Resolution:</strong> The measure of the smallest angular or linear separation between two objects that can be resolved by the sensor, dictating the <strong>clarity, sharpness, and spatial detail of ground objects</strong>. It is quantitatively represented by the Instantaneous Field of View (IFOV) and the Ground Sampling Distance (GSD).</li>
        <li><strong>(B) Spectral Resolution:</strong> The number and width of spectral bands in the electromagnetic spectrum recorded by the sensor (e.g., panchromatic vs. multispectral vs. hyperspectral). It governs the ability to discriminate materials by their absorption signatures.</li>
        <li><strong>(C) Temporal Resolution:</strong> The revisit time or frequency at which a satellite sensor images the exact same geographic location (e.g., 16 days for Landsat, 5 days for Sentinel-2, 15 minutes for INSAT-3D).</li>
        <li><strong>(D) Radiometric Resolution:</strong> The sensitivity of the detector to subtle differences in radiant energy flux, expressed as quantization bit depth (e.g., 8-bit = 256 gray levels; 12-bit = 4096 levels; 14-bit = 16,384 levels).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Ground Sampling Distance (GSD) & IFOV Geometry</div>
        $$D = H' \times \beta = H' \times \frac{d}{f}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $D$ is ground spatial resolution (GSD), $H'$ is flying height above ground level, $\beta$ is instantaneous field of view in radians, $d$ is physical detector element dimension, and $f$ is focal length of the optics.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q14/spatial_resolution_ifov_gsd.png" alt="Spatial Resolution IFOV and GSD Geometry">
        <div class="tb-caption">
          <strong>Figure 14.1: Spatial Resolution and Ground Clarity.</strong> Relationship between sensor Instantaneous Field of View ($\beta$), altitude ($H$), and Ground Sampling Distance (GSD), demonstrating that smaller pixel footprints directly enhance ground object clarity.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: GROUND CLARITY & RAYLEIGH CRITERION -->
  <div class="card">
    <div class="card-header bg-indigo">2. Physical Determinants of Ground Object Clarity</div>
    <div class="card-body">
      <p>The visual "clarity" or geometric sharpness of an object in satellite imagery depends strictly on whether the object's spatial dimensions exceed the sensor's ground resolution element:</p>

      <ul>
        <li><strong>Sub-Pixel Mixing:</strong> If an object is smaller than the spatial resolution cell (e.g., a $5\text{ m}$ road inside a $30\text{ m}$ Landsat pixel), its radiance is averaged with surrounding soil and vegetation, losing all geometric clarity (a "mixed pixel").</li>
        <li><strong>Nyquist Sampling Criterion:</strong> To reliably detect and identify a geometric target (such as a building or fault trace), the spatial resolution must be at least <strong>twice as fine</strong> as the target dimension ($GSD \le \frac{1}{2} L_{\text{object}}$).</li>
        <li><strong>Diffraction-Limited Resolution:</strong> By the Rayleigh optical criterion, angular resolution $\theta = 1.22 \frac{\lambda}{D_{\text{aperture}}}$. Achieving sharper ground clarity requires larger telescope apertures ($D_{\text{aperture}}$) or lower orbital altitudes ($H$).</li>
      </ul>

      <div class="quote-box">
        "Spatial resolution is an indication of how well a sensor can resolve small objects on the ground. Images where only large features are distinguishable have coarse or low spatial resolution; images where small objects can be identified have fine or high spatial resolution."
        <span class="quote-ref">— Thomas M. Lillesand et al., <em>Remote Sensing and Image Interpretation</em> (7th Ed., 2015, p. 32)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: RESOLUTION TRADE-OFF TRIANGLE -->
  <div class="card">
    <div class="card-header bg-emerald">3. The Engineering Trade-off: Spatial vs. Spectral vs. Temporal</div>
    <div class="card-body">
      <p>In satellite sensor design, physics imposes a fundamental trade-off governed by data rate and optical signal-to-noise ratio ($SNR$):</p>
      <ul>
        <li>Fine spatial resolution (e.g., WorldView-3 at $0.3\text{ m}$) requires collecting photons from a tiny ground area, forcing bands to be spectrally broad (panchromatic) to capture sufficient photons.</li>
        <li>Fine spectral resolution (e.g., AVIRIS hyperspectral with 224 narrow $10\text{ nm}$ bands) requires larger spatial pixels ($20\text{ m}$) to gather sufficient photons per band.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 14)</div>
    <div class="q-stmt">
      Q14. Clarity of ground object will depend upon :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Spatial Resolution &nbsp;✔</div>
      <div class="raw-opt">(B) Spectral Resolution</div>
      <div class="raw-opt">(C) Temporal Resolution</div>
      <div class="raw-opt">(D) Radiometric Resolution</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Spatial Resolution</div>
      <div class="sub">
        The geometric clarity, boundary definition, and spatial sharpness of ground objects in remote sensing imagery are directly governed by the sensor's <strong>Spatial Resolution</strong> (ground pixel footprint size / GSD).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Spatial Resolution</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Spatial resolution specifies the smallest physical dimension on the ground that can be resolved as an independent image pixel. Finer spatial resolution (e.g., $0.5\text{ m}$ vs. $30\text{ m}$) yields crisp, sharp object boundaries, allowing fine features like roads, buildings, drainage rills, and fault scarps to be identified with complete visual clarity.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Spectral Resolution</span>
      <span class="tag wrong">Incorrect (Governs Compositional Discrimination, Not Geometric Clarity)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Spectral resolution refers to the bandwidth and number of spectral channels. High spectral resolution allows an analyst to differentiate between subtle rock types or minerals (e.g., kaolinite vs. illite), but does not make a blurred spatial shape appear geometrically sharp.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Temporal Resolution</span>
      <span class="tag wrong">Incorrect (Governs Revisit Frequency)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Temporal resolution is the revisit frequency of the satellite (e.g., daily vs. every 16 days). It controls how frequently a dynamic phenomenon (flood, crop growth) can be monitored over time, but has zero influence on the geometric spatial clarity of a single image.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Radiometric Resolution</span>
      <span class="tag wrong">Incorrect (Governs Gray-Level Brightness Sensitivity)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Radiometric resolution measures the detector's sensitivity to subtle brightness variations (bit depth: 8-bit, 12-bit). While higher bit depth prevents saturation in bright clouds or dark shadows, it cannot resolve features smaller than the spatial pixel footprint.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">The Four Dimensions of Remote Sensing Resolution Matrix</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Resolution Type</th>
            <th>Governing Metric</th>
            <th>What It Controls in Image Analysis</th>
            <th>Comparison Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Spatial Resolution</strong></td>
            <td><strong>Ground Sampling Distance (GSD) / IFOV</strong></td>
            <td><strong>Geometric clarity, spatial sharpness, boundary definition</strong></td>
            <td>WorldView-3 ($0.3\text{ m}$) vs. Landsat-8 ($30\text{ m}$)</td>
          </tr>
          <tr>
            <td><strong>Spectral Resolution</strong></td>
            <td>Number of bands & band-width ($\Delta \lambda$)</td>
            <td>Material discrimination, chemical/mineral spectroscopy</td>
            <td>Panchromatic ($1$ band) vs. Hyperspectral ($> 200$ bands)</td>
          </tr>
          <tr>
            <td><strong>Radiometric Resolution</strong></td>
            <td>Quantization bit depth ($2^n$ gray levels)</td>
            <td>Contrast sensitivity, shadow penetration, radiometric precision</td>
            <td>8-bit ($256$ levels) vs. 14-bit ($16,384$ levels)</td>
          </tr>
          <tr>
            <td><strong>Temporal Resolution</strong></td>
            <td>Revisit cycle / repeat period</td>
            <td>Change detection frequency, disaster monitoring, phenology</td>
            <td>MODIS ($1 - 2\text{ days}$) vs. Landsat ($16\text{ days}$)</td>
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
          <strong>Practice Q1 (Numerical):</strong> An aerial mapping camera with a focal length $f = 152.4\text{ mm}$ and a CCD pixel pitch $d = 6.0\ \mu\text{m}$ flies at an altitude $H' = 1524\text{ m}$ above the terrain. Calculate the theoretical Ground Sampling Distance (GSD).
          <div class="pq-ans">✔ Worked Answer: $\text{GSD} = 0.060\text{ m}$ ($6.0\text{ cm}$).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\text{Scale Factor } S_f = \frac{H'}{f} = \frac{1524\text{ m}}{0.1524\text{ m}} = 10,000$$<br>
            $$\text{GSD} = d \times S_f = (6.0 \times 10^{-6}\text{ m}) \times 10,000 = 0.060\text{ m} = 6.0\text{ cm}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>mixed pixel (mixel)</em>, and how does it degrade image clarity?
          <div class="pq-ans">✔ Correct Answer: A pixel covering more than one land-cover class whose recorded digital number is an area-weighted composite average.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Coarse spatial resolution forces multiple disparate surfaces (e.g., $30\%$ water, $40\%$ asphalt, $30\%$ grass) into a single pixel, obscuring object boundaries.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What process is used in digital image processing to fuse high-spatial-resolution panchromatic data with lower-spatial-resolution multispectral data?
          <div class="pq-ans">✔ Correct Answer: Pan-sharpening (e.g., Gram-Schmidt, IHS, or Wavelet transform fusion).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Pan-sharpening replaces the low-resolution intensity component of multispectral imagery with high-resolution panchromatic data, producing sharp color imagery.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> By what factor does image file data volume increase if the spatial resolution (GSD) of an area is improved by a factor of 2 (e.g., from $30\text{ m}$ to $15\text{ m}$)?
          <div class="pq-ans">✔ Worked Answer: Increases by a factor of 4 ($2^2 = 4$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Halving linear pixel dimension doubles pixel count along both the X and Y axes ($2 \times 2 = 4$), quadrupling the total number of pixels.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How is Modulation Transfer Function (MTF) used to define spatial image clarity?
          <div class="pq-ans">✔ Correct Answer: It measures the ratio of output image contrast to input target contrast as a function of spatial frequency (line pairs per mm).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> MTF quantifies how well an optical sensor transfers contrast from the ground to the image; an MTF value $\ge 0.10$ at the Nyquist frequency is required for acceptable visual clarity.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What satellite currently holds the record for the highest commercial optical spatial resolution in orbit?
          <div class="pq-ans">✔ Correct Answer: WorldView-3 / WorldView-Legion ($0.30\text{ m}$ panchromatic GSD).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Operating at $617\text{ km}$ altitude with a $1.1\text{ m}$ diameter telescope, WorldView-3 resolves individual manhole covers and sidewalk curbs.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Why can linear features (like high-voltage power transmission lines or railway tracks) sometimes be detected in imagery even when their physical width is much smaller than the GSD?
          <div class="pq-ans">✔ Correct Answer: Because high radiometric contrast against background terrain alters the digital number of the entire pixel, forming a recognizable linear trend.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> While the object cannot be resolved geometrically, extreme contrast allows sub-pixel detection of continuous linear features.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is the difference between Point Spread Function (PSF) and Instantaneous Field of View (IFOV)?
          <div class="pq-ans">✔ Correct Answer: IFOV is the geometric angle of the detector; PSF describes the optical blur (spatial irradiance distribution) of a point source on the focal plane.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Atmospheric turbulence and lens diffraction spread a point source of light over adjacent detector elements according to the PSF.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 14, part1, part2, part3)


# ==============================================================================
# Q015: Fiducial Marks and Principal Points
# ==============================================================================
def generate_q015():
    title = "Q015: Photogrammetric Geometry: Fiducial Marks, Principal Points & Nadir | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Aerial Photogrammetry & Coordinate Systems"
    h1_title = "Q015: Photogrammetric Geometry: Fiducial Marks, Principal Points & Nadir"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 15<br>
<strong>Authoritative References:</strong> Paul R. Wolf, Bon A. Dewitt & Benjamin E. Wilkinson, <em>Elements of Photogrammetry with Applications in GIS</em> (4th Ed., McGraw-Hill, Ch. 2 & 3, pp. 25–48); Thomas M. Lillesand et al., <em>Remote Sensing and Image Interpretation</em> (7th Ed., Ch. 3, pp. 128–138); Moffitt, F.H. & Mikhail, E.M., <em>Photogrammetry</em> (3rd Ed., Harper & Row)."""

    part1 = r"""
  <!-- CARD 1: FIDUCIAL MARKS & THE PRINCIPAL POINT -->
  <div class="card">
    <div class="card-header bg-blue">1. Geometric Definitions: Fiducial Marks & The Principal Point ($PP$)</div>
    <div class="card-body">
      <p>In analog and metric digital aerial photogrammetry, standard aerial mapping cameras are equipped with precisely machined reference markers located rigidly within the focal plane frame, known as <strong>Fiducial Marks</strong>:</p>

      <ul>
        <li><strong>Fiducial Marks:</strong> Index marks (either 4 located at the midpoints of the four sides, or 8 located at the corners and midpoints) exposed directly onto the negative at the exact instant of exposure. Because the camera focal frame is calibrated to micrometer precision, fiducial marks establish the internal <em>photographic coordinate system</em> ($x, y$).</li>
        <li><strong>The Principal Point ($PP$):</strong> The precise point where the camera's optical axis (the perpendicular ray passing through the rear nodal point of the camera lens) intersects the focal plane. <strong>The intersection of straight lines connecting opposite pairs of fiducial marks defines the Principal Point ($PP$) of an aerial photograph</strong>.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q15/aerial_photo_fiducial_marks_principal_point.png" alt="Aerial Photo Fiducial Marks and Principal Point">
        <div class="tb-caption">
          <strong>Figure 15.1: Geometric Architecture of an Aerial Photograph.</strong> Showing four corner and four side fiducial marks whose orthogonal axes intersect at the calibrated Principal Point ($PP$). Also shows Ground Nadir ($n$) and Isocenter ($i$) on a tilted photograph.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE THREE CRITICAL CENTERS OF A TILTED PHOTO -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Three Critical Photogrammetric Centers: $PP$, Nadir ($n$), and Isocenter ($i$)</div>
    <div class="card-body">
      <p>When an aerial camera tilts slightly away from vertical (tilt angle $t$, typically $1^\circ - 3^\circ$), three distinct geometric center points emerge along the principal line of tilt:</p>

      <ul>
        <li><strong>1. Principal Point ($PP$ or $o$):</strong> The optical center defined by fiducial mark intersection. It is the center of <em>lens distortion</em>.</li>
        <li><strong>2. Photographic Nadir ($n$):</strong> The point where a true vertical plumb line dropped from the exposure station intersects the photo plane. <strong>Topographic relief displacement ($d$) is strictly radial from the Nadir point</strong> ($d = \frac{r h}{H}$). On a truly vertical photograph ($t = 0^\circ$), Nadir coincides exactly with the Principal Point.</li>
        <li><strong>3. Isocenter ($i$):</strong> The point midway between the Principal Point and the Nadir on the principal line ($d_{oi} = f \tan(t/2)$). <strong>Tilt displacement is strictly radial from the Isocenter</strong>.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Mathematical Distance Between Principal Point and Nadir</div>
        $$on = f \cdot \tan t \quad \text{and} \quad oi = f \cdot \tan\left(\frac{t}{2}\right)$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $f$ is camera focal length, $t$ is tilt angle, $o$ is principal point, $n$ is nadir, and $i$ is isocenter.</p>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Flight Path, Scale, and Flight Height</div>
    <div class="card-body">
      <p>Fiducial marks are strictly internal camera calibration indices. They cannot directly measure external flight parameters:</p>
      <ul>
        <li><strong>Scale:</strong> Scale ($S = \frac{f}{H - h}$) requires knowing camera focal length ($f$) and flying height ($H$) above terrain elevation ($h$).</li>
        <li><strong>Flight Height:</strong> Flight height is measured by barometric/radar altimetry or airborne GNSS, not by internal fiducials.</li>
        <li><strong>Flight Path:</strong> The flight line direction is determined by transferring principal points across overlapping stereopairs ($PP_1$ to $PP_2$), but the fiducials themselves determine the principal points.</li>
      </ul>

      <div class="quote-box">
        "Fiducial marks are index marks rigidly set in the camera body so that their positions cannot change. Lines joining opposite fiducials intersect at or extremely close to the principal point of the photograph."
        <span class="quote-ref">— Paul R. Wolf et al., <em>Elements of Photogrammetry with Applications in GIS</em> (4th Ed., 2014, p. 28)</span>
      </div>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 15)</div>
    <div class="q-stmt">
      Q15. Fiducial marks recorded on Aerial photographs are used to determine the :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Flight path</div>
      <div class="raw-opt">(B) Scale of Aerial photographs</div>
      <div class="raw-opt correct">(C) Principal points &nbsp;✔</div>
      <div class="raw-opt">(D) Flight height</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Principal points</div>
      <div class="sub">
        <strong>Fiducial marks</strong> are calibrated index marks exposed onto the margins of aerial photographs; connecting opposite pairs with straight lines establishes the geometric photo coordinate system and identifies the exact location of the <strong>Principal Point ($PP$)</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Flight path</span>
      <span class="tag wrong">Incorrect (Requires Conjugate Principal Point Transfer)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The flight path line is determined by stereoscopic transfer of conjugate principal points between overlapping consecutive photographs ($PP_1$ and $PP_2$). Fiducial marks only locate the single image's internal principal point, not the aircraft's spatial flight trajectory.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Scale of Aerial photographs</span>
      <span class="tag wrong">Incorrect (Determined by Focal Length & Flying Height)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The scale of an aerial photograph is a function of the camera lens focal length ($f$) and the flying height above ground ($H'$), governed by $S = f / H'$. Fiducial marks have zero mathematical relation to scale.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Principal points</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By international photogrammetric convention, the primary purpose of calibrated fiducial marks (4 or 8 marks located along the edges or corners of the focal plane) is to establish the photographic coordinate axes ($x, y$). The geometric intersection of opposite fiducial lines defines the <strong>Principal Point ($PP$)</strong>, which represents the optical center of the photograph.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Flight height</span>
      <span class="tag wrong">Incorrect (Measured by Altimetry/GNSS)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Flying height above datum ($H$) is recorded by aircraft avionics, radar altimeters, or airborne differential GNSS receivers. It cannot be derived from internal camera fiducials.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Coordinate Centers & Relief Displacements in Photogrammetry</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Photogrammetric Point</th>
            <th>Symbol</th>
            <th>How It Is Located on Photograph</th>
            <th>Radial Displacement Geometry</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Principal Point</strong></td>
            <td>$PP$ or $o$</td>
            <td><strong>Intersection of lines connecting opposite fiducial marks</strong></td>
            <td>Center of <strong>lens distortion</strong> (radial lens aberration)</td>
          </tr>
          <tr>
            <td><strong>Nadir Point</strong></td>
            <td>$n$</td>
            <td>Intersection of plumb line from lens with photo plane</td>
            <td>Center of <strong>topographic relief displacement</strong> ($d = r h / H$)</td>
          </tr>
          <tr>
            <td><strong>Isocenter</strong></td>
            <td>$i$</td>
            <td>Midway between $PP$ and Nadir along principal line ($oi = f \tan(t/2)$)</td>
            <td>Center of <strong>tilt displacement</strong></td>
          </tr>
          <tr>
            <td><strong>Conjugate Principal Point</strong></td>
            <td>$PP'$</td>
            <td>Transferred location of adjacent photo's $PP$ on stereopair</td>
            <td>Defines the baseline flight line direction between exposures</td>
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
          <strong>Practice Q1 (Numerical):</strong> A vertical aerial photograph is taken with a metric camera of focal length $f = 152.4\text{ mm}$ from a flying height $H = 1800\text{ m}$ above sea level. A mountain peak at an elevation $h = 300\text{ m}$ appears at a radial distance $r = 85.0\text{ mm}$ from the Principal Point. Calculate the relief displacement ($d$) of the peak.
          <div class="pq-ans">✔ Worked Answer: $d = 14.17\text{ mm}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            Relief displacement formula:
            $$d = \frac{r \cdot h}{H} = \frac{85.0\text{ mm} \times 300\text{ m}}{1800\text{ m}} = \frac{25,500}{1800} \approx 14.17\text{ mm}$$
            The image of the peak is displaced radially outward from the principal point by $14.17\text{ mm}$.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> On a truly vertical aerial photograph ($t = 0^\circ$), which three critical photogrammetric points coincide at the exact same location?
          <div class="pq-ans">✔ Correct Answer: The Principal Point ($PP$), the Nadir point ($n$), and the Isocenter ($i$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When optical tilt $t = 0$, the optical axis is vertical ($on = f \tan 0^\circ = 0$). All three centers merge at the fiducial intersection.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What direction does topographic relief displacement act on an aerial photograph?
          <div class="pq-ans">✔ Correct Answer: Radially outward from the Nadir point for features above datum ($h > 0$), and radially inward for features below datum ($h < 0$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Elevated points (hills, towers) are shifted away from the photo center, whereas depressions (valleys) are shifted inward toward the center.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In a modern digital aerial mapping camera (e.g., UltraCam or Leica DMC), how is the principal point defined in the absence of mechanical film fiducial marks?
          <div class="pq-ans">✔ Correct Answer: By factory laboratory calibration measuring the pixel coordinates of the CCD/CMOS array center.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Digital sensors have fixed pixel matrices whose physical geometric coordinates are calibrated to sub-micron accuracy, stored directly in the camera calibration certificate.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the standard percentage of <em>forward overlap (end lap)</em> required along an aerial flight strip to enable stereoscopic 3D viewing?
          <div class="pq-ans">✔ Correct Answer: $60\% \text{ to } 65\%$ (nominally $60\%$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A $60\%$ forward overlap guarantees that every ground point appears on at least two consecutive photographs from different perspectives, forming a stereopair.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the standard percentage of <em>lateral overlap (side lap)</em> between adjacent parallel flight strips?
          <div class="pq-ans">✔ Correct Answer: $20\% \text{ to } 30\%$ (nominally $25\%$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Side lap prevents gaps between adjacent flight strips and allows tie points to be connected during aerial triangulation block adjustment.
          </div>
        </li>

        <li>
          <strong>Practice Q7 (Numerical):</strong> An aerial photograph has a tilt $t = 2.0^\circ$ and camera focal length $f = 150.0\text{ mm}$. Calculate the physical distance between the Principal Point ($o$) and the Nadir ($n$) on the negative.
          <div class="pq-ans">✔ Worked Answer: $on = 5.24\text{ mm}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$on = f \cdot \tan t = 150.0\text{ mm} \times \tan(2.0^\circ) = 150.0 \times 0.03492 \approx 5.24\text{ mm}$$
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why is an <em>orthophotograph</em> superior to a raw aerial photograph for direct GIS overlay and distance measurement?
          <div class="pq-ans">✔ Correct Answer: An orthophoto is differentially rectified to remove all image displacements caused by camera tilt and topographic relief, creating a uniform map scale.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Raw photos are central perspective projections where scale varies across the image; orthophotos are converted via DEMs into orthogonal parallel projections where distances can be measured as on a planimetric map.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 15, part1, part2, part3)


if __name__ == "__main__":
    for q_fn, q_name in [
        (generate_q011, "Q011_Rayleigh_Scattering_Atmosphere_Complete_Guide.html"),
        (generate_q012, "Q012_Vibrational_Energy_SWIR_TIR_Complete_Guide.html"),
        (generate_q013, "Q013_Sun_Synchronous_Orbit_Local_Solar_Time_Complete_Guide.html"),
        (generate_q014, "Q014_Spatial_Resolution_Ground_Clarity_Complete_Guide.html"),
        (generate_q015, "Q015_Fiducial_Marks_Principal_Point_Photogrammetry_Complete_Guide.html"),
    ]:
        out_path = os.path.join(SOLUTIONS_DIR, q_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(q_fn())
        print(f"Generated {q_name}: {out_path} ({os.path.getsize(out_path)} bytes)")
