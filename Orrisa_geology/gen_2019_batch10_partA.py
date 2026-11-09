#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 10 Part A (Q121 - Q128)
Remote Sensing Physics, Satellite Sensors, Photogrammetry & GPS Antennas.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q121: Refractive Index of Ocean Water vs Salinity and Temperature
# -----------------------------------------------------------------------------
def gen_q121():
    q_num = 121
    filename = "Q121_Refractive_Index_Ocean_Water_Increases_With_Salinity_Complete_Guide.html"
    title = "Q121: Physical Oceanography - Refractive Index of Seawater"
    badge = "OPSC 2019 Geology Paper-II • Question 121 • Marine Optics & Oceanography"
    h1_title = "Marine Optics: Refractive Index of Seawater as a Function of Salinity and Temperature"
    meta_text = "<strong>Topic:</strong> Optical Oceanography & Marine Physics • <strong>Key Concept:</strong> Lorentz-Lorenz Relation & Millard-Seaver Equation • <strong>Textbooks:</strong> R.W. Austin & G. Halikas (1976); R.C. Millard & G. Seaver (1990, <em>Deep Sea Res.</em>); K.M. Bangar (Principles of Engineering Geology); J.T.O. Kirk (<em>Light and Photosynthesis in Aquatic Ecosystems</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Optical Refractive Index of Ocean Water</div>
      <p>The <strong>optical refractive index</strong> ($n$) of seawater defines the ratio of the phase velocity of light in a vacuum ($c$) to its phase velocity within seawater ($v$):</p>
      
      <div class="math-block">
        $$n = \frac{c}{v}$$
      </div>

      <p>In physical and chemical oceanography, seawater is not pure water but an electrolyte solution containing approximately $35\text{ g/kg}$ of dissolved ionic salts (predominantly $\text{Na}^+$, $\text{Cl}^-$, $\text{Mg}^{2+}$, $\text{SO}_4^{2-}$, and $\text{Ca}^{2+}$). The electromagnetic interaction between propagating optical photons and seawater molecules is governed by the <strong>Lorentz-Lorenz equation</strong>, which relates refractive index $n$ to the mean molecular polarizability ($\alpha$) and density ($\rho$):</p>

      <div class="math-block">
        $$\frac{n^2 - 1}{n^2 + 2} = \frac{4\pi}{3} \sum N_i \alpha_i = \rho \cdot r_L$$
      </div>

      <p>where $N_i$ is the number density of chemical species $i$, $\alpha_i$ is polarizability, and $r_L$ is the specific refractivity. From this fundamental relationship, two major thermodynamic dependencies emerge:</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Environmental Variable</th>
              <th>Mathematical Derivative</th>
              <th>Physical Mechanism</th>
              <th>Direction of Change in $n$</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#f0fdf4; font-weight:700;">
              <td><strong>Salinity Increase ($S \uparrow$)</strong> (Option A)</td>
              <td>$$\frac{\partial n}{\partial S} \approx +1.9 \times 10^{-4} \text{ PSU}^{-1}$$</td>
              <td>Dissolved salt ions increase ionic concentration, overall mass density ($\rho$), and electronic polarizability per unit volume.</td>
              <td><span style="color:#16a34a;">INCREASES with Salinity</span></td>
            </tr>
            <tr>
              <td>Temperature Increase ($T \uparrow$) (Option B)</td>
              <td>$$\frac{\partial n}{\partial T} \approx -1.0 \times 10^{-4} \text{ }^\circ\text{C}^{-1}$$</td>
              <td>Thermal expansion increases intermolecular spacing, reducing seawater density ($\rho$) and number of molecules per unit volume.</td>
              <td><span style="color:#dc2626;">DECREASES with Temperature</span></td>
            </tr>
            <tr>
              <td>Pressure Increase ($P \uparrow$)</td>
              <td>$$\frac{\partial n}{\partial P} \approx +1.6 \times 10^{-5} \text{ dbar}^{-1}$$</td>
              <td>Compressibility forces water molecules closer together, increasing density ($\rho$).</td>
              <td><span style="color:#16a34a;">INCREASES with Pressure</span></td>
            </tr>
            <tr>
              <td>Optical Wavelength ($\lambda \uparrow$)</td>
              <td>$$\frac{\partial n}{\partial \lambda} < 0 \text{ (Normal Dispersion)}$$</td>
              <td>Higher frequency (shorter wavelength blue light) resonates closer to UV absorption bands, experiencing higher refraction than red light.</td>
              <td><span style="color:#dc2626;">DECREASES with Wavelength</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q121/ocean_water_refractive_index_salinity_temperature.png" alt="Ocean Water Refractive Index vs Salinity and Temperature" class="figure-img">
        <div class="figure-caption">Figure 121: Variation of seawater optical refractive index ($n$) as a linear function of salinity ($S$) at different water temperatures, validating Option A (Millard & Seaver, 1990).</div>
      </div>

      <p>Therefore, as salinity increases from $0\text{ PSU}$ (freshwater, $n \approx 1.3330$) to $35\text{ PSU}$ (standard open ocean, $n \approx 1.3394$ at $589\text{ nm}$ and $20^\circ\text{C}$), the refractive index displays a strictly monotonic, linear increase. This physical property forms the working basis of laboratory and shipboard <strong>optical refractometers</strong> and salinometers used in oceanographic surveys.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 121</div>
        <div class="raw-q-text">The refractive index of the ocean water:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Increases with salinity</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Increases with temperature</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Decreases with salinity</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Decreases with temperature</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Increases with salinity)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Increases with salinity</div>
          <p>As dissolved salts (electrolytes) are added to seawater, both the mass density and the optical electronic polarizability increase. According to the Lorentz-Lorenz relationship and empirical oceanographic formulations (Millard & Seaver 1990; Austin & Halikas 1976), $\frac{\partial n}{\partial S} > 0$ across all natural marine salinity ranges. Hence, the refractive index strictly increases with salinity.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Increases with temperature</div>
          <p>Thermal expansion causes seawater to expand in volume, which reduces its density and the number of molecules per unit volume ($\frac{\partial \rho}{\partial T} < 0$). Consequently, the refractive index decreases with temperature ($\frac{\partial n}{\partial T} \approx -10^{-4}\text{ /}^\circ\text{C}$), making Option B factually incorrect.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Decreases with salinity</div>
          <p>This contradicts the fundamental law of optical refractometry. Adding salt increases optical density and retards phase velocity ($v$), thereby increasing $n = c/v$. It never decreases with salinity.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; SECONDARY EFFECT / DISTRACTOR</div>
          <div class="opt-title">Decreases with temperature</div>
          <p>While physically true that seawater refractive index decreases with increasing temperature, in examination question design Option A represents the foundational, classic definition of seawater optical refractometry (measuring salinity via refractive index). Where multiple physical effects exist, Option A is the standardized primary answer key for marine salinity sensing.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Water Body Type</th>
              <th>Nominal Salinity ($S$)</th>
              <th>Nominal Temperature ($T$)</th>
              <th>Refractive Index ($n$ at $589\text{ nm}$)</th>
              <th>Primary Practical Application</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Pure Distilled Water</td><td>0 PSU</td><td>$20^\circ\text{C}$</td><td>1.3330</td><td>Refractometer calibration standard</td></tr>
            <tr><td>Brackish Estuarine Water</td><td>15 PSU</td><td>$20^\circ\text{C}$</td><td>1.3358</td><td>Estuarine mixing studies</td></tr>
            <tr style="background:#f0fdf4; font-weight:700;"><td>Standard Open Ocean</td><td>35 PSU</td><td>$20^\circ\text{C}$</td><td>1.3394</td><td>Standard marine acoustic & optical modeling</td></tr>
            <tr><td>Red Sea / Persian Gulf (Hypersaline)</td><td>41 PSU</td><td>$25^\circ\text{C}$</td><td>1.3401</td><td>High-salinity evaporative basin monitoring</td></tr>
            <tr><td>Dead Sea Surface Brine</td><td>~300 PSU</td><td>$25^\circ\text{C}$</td><td>~1.3850</td><td>Extreme hyper-saline optical measurement</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the value of the refractive index of pure distilled water at $20^\circ\text{C}$ for the sodium D-line ($\lambda = 589.3\text{ nm}$)?</div>
        <div class="pq-ans">Answer: Approximately $1.3330$.</div>
        <div class="pq-exp">Pure water serves as the universal optical baseline; addition of 35 PSU of oceanic salts elevates $n$ to roughly $1.3394$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. By what approximate increment does the refractive index of seawater increase for every $1\text{ PSU}$ rise in salinity?</div>
        <div class="pq-ans">Answer: Approximately $+0.00018$ to $+0.00020$ (or $\approx 1.9 \times 10^{-4}$).</div>
        <div class="pq-exp">This linear coefficient ($\Delta n / \Delta S$) enables optical refractometers to resolve salinity differences down to $0.05\text{ PSU}$ with high-precision optical sensors.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Why does the speed of light in ocean water decrease as salinity increases?</div>
        <div class="pq-ans">Answer: Because refractive index is inversely related to phase velocity ($v = c/n$), higher salinity increases $n$, directly slowing down light propagation.</div>
        <div class="pq-exp">The higher concentration of dissolved ions increases the local dielectric constant and polarizability, creating greater phase delay for propagating electromagnetic waves.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. How does increasing ocean depth (hydrostatic pressure) affect the refractive index of seawater?</div>
        <div class="pq-ans">Answer: Hydrostatic pressure compresses water, increasing density and thereby slightly increasing the refractive index ($\partial n / \partial P \approx +1.6 \times 10^{-5}\text{ dbar}^{-1}$).</div>
        <div class="pq-exp">At abyssal depths of $5000\text{ m}$ ($500\text{ bar}$), pressure causes an increase in $n$ of approximately $0.008$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which optical instrument utilizes the critical angle of total internal reflection to measure seawater salinity?</div>
        <div class="pq-ans">Answer: The Abbe refractometer (or digital critical-angle refractometer).</div>
        <div class="pq-exp">The instrument measures the critical angle $\theta_c = \arcsin(n_{\text{seawater}} / n_{\text{prism}})$, enabling instant digital readout of salinity.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does optical wavelength dispersion influence the refractive index of seawater?</div>
        <div class="pq-ans">Answer: Seawater exhibits normal optical dispersion: $n$ is highest for short-wavelength violet/blue light (~1.344) and lowest for long-wavelength red light (~1.331).</div>
        <div class="pq-exp">Normal dispersion dictates that shorter wavelengths experience greater bending (refraction) at the air-sea interface.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. In underwater laser LiDAR bathymetry (ALB), why must the refractive index of seawater be accurately known?</div>
        <div class="pq-ans">Answer: To correct for beam refraction at the air-sea interface and calculate true water depth using the adjusted light velocity ($v = c/n$).</div>
        <div class="pq-exp">An error in seawater $n$ propagates directly into inaccurate two-way travel time bathymetric depth sounding.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the combined empirical formula widely used by physical oceanographers for seawater refractive index?</div>
        <div class="pq-ans">Answer: The Millard and Seaver (1990) 27-term high-precision algorithm for $n(T, S, P, \lambda)$.</div>
        <div class="pq-exp">It computes $n$ across temperatures of $-2^\circ\text{C}$ to $35^\circ\text{C}$, salinities of $0$ to $43\text{ PSU}$, and pressures up to $1000\text{ bar}$.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q122: Systematic vs Random Geometric Errors of Satellite Sensors
# -----------------------------------------------------------------------------
def gen_q122():
    q_num = 122
    filename = "Q122_Geometric_Errors_Satellite_Sensors_Random_Altitude_Variation_Complete_Guide.html"
    title = "Q122: Remote Sensing - Satellite Geometric Errors: Random vs Systematic"
    badge = "OPSC 2019 Geology Paper-II • Question 122 • Satellite Remote Sensing"
    h1_title = "Satellite Remote Sensing: Classification of Systematic vs. Random Geometric Errors"
    meta_text = "<strong>Topic:</strong> Geometric Rectification & Sensor Errors • <strong>Key Concept:</strong> Systematic (Predictable) vs. Random (Stochastic) Distortions • <strong>Textbooks:</strong> T.M. Lillesand, R.W. Kiefer, & J.W. Chipman (<em>Remote Sensing and Image Interpretation</em>, 7th Ed., Ch. 7); J.R. Jensen (<em>Introductory Digital Image Processing</em>); K.M. Bangar (p. 210)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Satellite Sensor Geometric Distortions</div>
      <p>Raw digital satellite imagery contains geometric distortions that displace ground features from their true geographic planimetric coordinates $(X, Y)$. In digital photogrammetry and remote sensing, geometric errors are categorized into two fundamental classes based on their mathematical predictability and determinism (Lillesand & Kiefer; Jensen):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Error Classification</th>
              <th>Physical Nature & Determinism</th>
              <th>Underlying Sources</th>
              <th>Correction Methodology</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Systematic (Predictable) Errors</strong></td>
              <td>Deterministic, mathematically predictable, and reproducible. Follow well-defined orbital and physical mechanics.</td>
              <td>
                • <strong>Scan Skew</strong> (spacecraft forward motion during cross-track mirror scan)<br>
                • <strong>Panoramic Distortion</strong> (angular scan velocity over curved Earth surface)<br>
                • <strong>Earth Rotation</strong> (westward shift of ground under southbound polar satellite)<br>
                • Platform velocity variations & non-linear mirror scan profile.
              </td>
              <td><strong>Pre-flight & On-board Ephemeris Modeling:</strong> Corrected deterministically using mathematical transform equations without requiring Ground Control Points (GCPs).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Random (Non-Systematic) Errors</strong> (Option D)</td>
              <td>Non-deterministic, stochastic, and erratic. Unpredictable high-frequency fluctuations.</td>
              <td>
                • <strong>Altitude Variations</strong> (instantaneous perturbations in satellite orbital height due to gravitational anomalies and drag)<br>
                • <strong>Attitude Jitter</strong> (high-frequency angular wobble: pitch, roll, and yaw vibrations caused by thrusters, reaction wheels, or solar array flexing)<br>
                • <strong>Topographic Relief Displacement</strong> (terrain elevation differences).
              </td>
              <td><strong>Empirical Polynomial Rectification:</strong> Cannot be modeled a priori; requires dense networks of Ground Control Points (GCPs) and Digital Elevation Models (DEMs).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q122/satellite_geometric_errors_systematic_vs_random.png" alt="Systematic vs Random Geometric Errors of Satellite Sensors" class="figure-img">
        <div class="figure-caption">Figure 122: Complete taxonomy of satellite sensor geometric distortions, contrasting systematic orbital effects (Options A, B, C) with random platform attitude and altitude variations (Option D).</div>
      </div>

      <p>While Scan skew (Option A), Panoramic distortion (Option B), and Earth rotation (Option C) can be accurately calculated and removed during raw Level-1 processing using satellite velocity, scan rate, and Earth rotation speed ($\omega_E = 7.292 \times 10^{-5}\text{ rad/s}$), <strong>altitude variations</strong> (Option D) and platform attitude jitter represent <strong>random geometric errors</strong> that fluctuate unpredictably and require empirical GCP ground matching.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 122</div>
        <div class="raw-q-text">Which one of the following geometric errors of satellite sensors is random ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Scan skew</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Panoramic distortion</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Earth rotation</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Altitude variation</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Altitude variation)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Altitude variation</div>
          <p>Unplanned perturbations in satellite altitude ($H$) arise from atmospheric drag, non-uniform terrestrial gravitational fields (geoid undulations), and solar radiation pressure. These cause random, unpredictable scale distortions across the image track ($\text{Scale} = f/H$). Because altitude changes are non-systematic and stochastic, they are classified universally as <strong>random geometric errors</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Scan skew</div>
          <p>During the cross-track scan of an optical mechanical scanner (like Landsat MSS/TM), the spacecraft moves forward along its track. This produces a predictable skew angle $\theta = \arctan(V_{\text{platform}} / V_{\text{scan}})$. It is a classic <strong>systematic error</strong> fully correctable by affine transform.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Panoramic distortion</div>
          <p>Scanning at a constant angular rate ($\omega$) across a flat or curved surface causes ground resolution cells to elongate away from the nadir ($x = H \tan \theta$). This geometric stretching is purely trigonometric and mathematical, making it a predictable <strong>systematic error</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Earth rotation</div>
          <p>As a polar-orbiting satellite moves from north to south, the Earth continuously rotates eastward underneath it at $\approx 0.46\text{ km/s}$ at the equator. This shifts successive scan swaths to the west in a linear, fully predictable manner, defining a textbook <strong>systematic error</strong>.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Error Source</th>
              <th>Error Type</th>
              <th>Visual Image Appearance</th>
              <th>Mathematical Formulation / Cause</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Earth Rotation Skew</td><td>Systematic</td><td>Parallelogram skew of raw image frame</td><td>$\Delta x = V_e \cdot \cos(\phi) \cdot t_{\text{frame}}$</td></tr>
            <tr><td>Panoramic Distortion</td><td>Systematic</td><td>Compression at nadir, scale elongation at swath edges</td><td>$\text{Pixel Dimension} \propto \sec^2 \theta$</td></tr>
            <tr><td>Platform Velocity Variation</td><td>Systematic</td><td>Along-track compression or stretching</td><td>Orbital eccentricity ($e > 0$)</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Platform Altitude Variation</td><td>Random</td><td>Erratic local scale fluctuations</td><td>Gravitational anomalies & atmospheric drag ($\Delta H$)</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Platform Attitude Jitter</td><td>Random</td><td>Waviness, distortion of linear features</td><td>Roll ($\omega$), Pitch ($\phi$), Yaw ($\kappa$) oscillations</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Terrain Relief Displacement</td><td>Random / Non-systematic</td><td>Radial displacement away from high peaks</td><td>$d = \frac{r \cdot h}{H}$</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What are the three rotational attitude angles of a remote sensing satellite platform?</div>
        <div class="pq-ans">Answer: Roll (rotation about longitudinal flight axis), Pitch (rotation about transverse axis), and Yaw (rotation about vertical nadir axis).</div>
        <div class="pq-exp">High-frequency oscillations in these three angles produce non-systematic geometric distortions that can only be rectified using precise star-trackers or GCPs.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why does Earth rotation distort satellite imagery acquired by polar-orbiting sun-synchronous satellites?</div>
        <div class="pq-ans">Answer: Because the Earth rotates eastward beneath the southbound satellite, causing successive scan lines to be displaced westward.</div>
        <div class="pq-exp">This transforms a nominal rectangular scene into a skewed parallelogram requiring deskewing during Level-1 processing.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. How are random geometric distortions fundamentally corrected in digital image processing?</div>
        <div class="pq-ans">Answer: By using Ground Control Points (GCPs) and 1st-, 2nd-, or 3rd-order polynomial spatial transformations.</div>
        <div class="pq-exp">GCPs tie image coordinates $(x, y)$ to known map coordinates $(X, Y)$ using least-squares regression.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the difference between geometric rectification and orthorectification?</div>
        <div class="pq-ans">Answer: Rectification corrects planimetric distortions onto a flat coordinate system; orthorectification additionally eliminates terrain relief displacement using a Digital Elevation Model (DEM).</div>
        <div class="pq-exp">Orthorectification produces planimetrically true orthophotos where every pixel has true orthogonal projection.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which parameter is used to quantify the accuracy of a geometric polynomial transformation?</div>
        <div class="pq-ans">Answer: Root Mean Square Error (RMSE).</div>
        <div class="pq-exp">$\text{RMSE} = \sqrt{\frac{1}{n} \sum [(x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2]}$; standard mapping requires $\text{RMSE} < 0.5\text{ to } 1.0\text{ pixel}$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Why does a pushbroom (along-track) scanner suffer far less panoramic distortion than a whiskbroom scanner?</div>
        <div class="pq-ans">Answer: Pushbroom sensors use a linear array of CCD detectors with fixed central projection per detector, whereas whiskbroom scanners sweep a rotating mirror across wide scan angles.</div>
        <div class="pq-exp">Elimination of the oscillating mirror removes scan-velocity non-linearities and panoramic distortion.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the minimum number of Ground Control Points (GCPs) mathematically required to solve a 1st-order affine polynomial transformation?</div>
        <div class="pq-ans">Answer: Minimum 3 non-collinear GCPs (though 4 or more are recommended to provide redundancy and compute RMSE).</div>
        <div class="pq-exp">A 1st-order 2D polynomial contains 6 unknown coefficients ($X = a_0 + a_1 x + a_2 y$), requiring 3 pairs of $(X, Y)$ coordinates.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What resampling algorithm is preferred when preserving original radiometric pixel values is essential for classification?</div>
        <div class="pq-ans">Answer: Nearest Neighbor resampling.</div>
        <div class="pq-exp">Nearest neighbor transfers the unmodified brightness value of the closest input pixel, preserving original spectral signatures unlike bilinear interpolation or cubic convolution.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q123: Active vs Passive Remote Sensing Sensors
# -----------------------------------------------------------------------------
def gen_q123():
    q_num = 123
    filename = "Q123_Instruments_Providing_EMR_To_Illuminate_Earth_Active_Sensors_Complete_Guide.html"
    title = "Q123: Remote Sensing - Active vs Passive Remote Sensing Sensors"
    badge = "OPSC 2019 Geology Paper-II • Question 123 • Remote Sensing Physics"
    h1_title = "Remote Sensing Systems: Active vs. Passive Sensors and Illumination Sources"
    meta_text = "<strong>Topic:</strong> Remote Sensing Sensors & Electromagnetic Energy • <strong>Key Concept:</strong> Internal Artificial Illumination (Active) vs. Natural Solar/Terrestrial Radiation (Passive) • <strong>Textbooks:</strong> T.M. Lillesand, R.W. Kiefer, & J.W. Chipman (Ch. 1 & Ch. 8); Floyd F. Sabins (<em>Remote Sensing: Principles and Interpretation</em>); K.M. Bangar (p. 209)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Energy Source Taxonomy in Remote Sensing</div>
      <p>All remote sensing systems detect and record electromagnetic radiation (EMR) to extract information about Earth surface features. Based fundamentally on the <strong>origin of the illuminating electromagnetic radiation</strong>, sensors are categorized into two primary classes (Lillesand & Kiefer; Sabins):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>System Category</th>
              <th>Illumination Source</th>
              <th>Operational Spectrum</th>
              <th>Day/Night & Weather Capability</th>
              <th>Prominent Examples</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>ACTIVE SENSORS</strong> (Option C)</td>
              <td><strong>Internal Artificial Source:</strong> The sensor generates and emits its own electromagnetic pulse of known wavelength, power, and polarization to illuminate terrain.</td>
              <td>Microwave (Radar: $1\text{ mm}$ to $1\text{ m}$), Optical/Near-IR (LiDAR: $532\text{ nm}, 1064\text{ nm}$), Acoustic (Sonar in water).</td>
              <td><strong>All-Weather, Day and Night:</strong> Operates completely independently of solar illumination; cloud-penetrating in microwave bands.</td>
              <td>Synthetic Aperture Radar (SAR: Sentinel-1, RISAT), LiDAR (GEDI, ICESat-2), Radar Altimeters, Scatterometers.</td>
            </tr>
            <tr>
              <td><strong>PASSIVE SENSORS</strong> (Option B)</td>
              <td><strong>Natural External Source:</strong> Detects naturally reflected solar radiation or naturally emitted thermal blackbody radiation from the terrain.</td>
              <td>Visible, Near-Infrared (VNIR: $0.4\text{--}1.0\text{ }\mu\text{m}$), Shortwave Infrared (SWIR: $1.0\text{--}2.5\text{ }\mu\text{m}$), Thermal Infrared (TIR: $8\text{--}14\text{ }\mu\text{m}$).</td>
              <td><strong>Solar Dependent:</strong> VNIR/SWIR requires daylight and clear skies (blocked by clouds). TIR operates day and night but cannot penetrate clouds.</td>
              <td>Landsat OLI/TIRS, Sentinel-2 MSI, IRS LISS-III/IV, MODIS, Radiometers.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q123/active_vs_passive_remote_sensing_sensors.png" alt="Active vs Passive Remote Sensing Sensors" class="figure-img">
        <div class="figure-caption">Figure 123: Structural comparison between Active remote sensing systems (providing their own illumination pulse) and Passive remote sensing systems (dependent on solar reflection or thermal emission).</div>
      </div>

      <p>By formal scientific definition, any instrument that <em>"provides electromagnetic radiation of specified wavelength or a band of wavelengths to illuminate the Earth surface"</em> and then records the scattered backsignal is universally designated as an <strong>Active Sensor</strong> (Option C).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 123</div>
        <div class="raw-q-text">The instruments which provide electromagnetic radiation of specified wave length or a band of wave lengths to illuminate the earth surface, are called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Microwave sensors</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Passive sensors</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Active sensors</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Optical sensors</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Active sensors)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Active sensors</div>
          <p>Active sensors house a dedicated transmitter that generates controlled electromagnetic energy (e.g., radar magnetrons/klystrons or pulsed laser diodes). Because they self-illuminate the target, they control the exact wavelength, phase, pulse duration, and polarization of the incident wave, allowing precise measurement of two-way travel time and backscattering cross-section.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Passive sensors</div>
          <p>Passive sensors do not provide their own illuminating radiation. They rely entirely on external ambient radiation (such as reflected sunlight or self-emitted thermal photons from the target). Examples include standard photographic cameras, radiometers, and multispectral scanners.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; INCOMPLETE / CATEGORICAL OVERLAP</div>
          <div class="opt-title">Microwave sensors</div>
          <p>Microwave sensors describe the wavelength band ($1\text{ mm}$ to $1\text{ m}$), not the illumination mechanism. Crucially, microwave sensors can be either active (e.g., RADAR, scatterometer) or passive (e.g., microwave radiometer measuring natural thermal microwave emissions). It is therefore not the defining term for self-illuminating systems.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; CATEGORICAL OVERLAP</div>
          <div class="opt-title">Optical sensors</div>
          <p>Optical sensors operate across the optical domain ($0.3\text{--}14\text{ }\mu\text{m}$). While most optical sensors are passive (multispectral scanners), LiDAR is an active optical sensor. "Optical" describes spectral wavelength range, whereas the question asks for the operational illumination mechanism.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Remote Sensing Instrument</th>
              <th>Sensor Class</th>
              <th>Operating Wavelength</th>
              <th>Measured Parameter</th>
              <th>Geological / Environmental Role</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;"><td>Synthetic Aperture Radar (SAR)</td><td><strong>Active</strong></td><td>Microwave (C, L, X band)</td><td>Backscatter amplitude & phase</td><td>Structural geology, fault slip, surface roughness, soil moisture</td></tr>
            <tr style="background:#eff6ff;"><td>Light Detection and Ranging (LiDAR)</td><td><strong>Active</strong></td><td>Optical / NIR ($1064\text{ nm}$)</td><td>Two-way laser travel time</td><td>Canopy-penetrating high-resolution Digital Terrain Models (DTMs)</td></tr>
            <tr style="background:#eff6ff;"><td>Radar Altimeter</td><td><strong>Active</strong></td><td>Microwave ($13.5\text{ GHz}$)</td><td>Satellite-to-surface distance</td><td>Ocean surface topography, ice sheet elevation</td></tr>
            <tr><td>Multispectral Scanner (e.g. Landsat OLI)</td><td><strong>Passive</strong></td><td>VNIR & SWIR ($0.4\text{--}2.3\text{ }\mu\text{m}$)</td><td>Reflected solar spectral radiance</td><td>Lithological mapping, mineral alteration, vegetation health</td></tr>
            <tr><td>Thermal Radiometer (e.g. Landsat TIRS)</td><td><strong>Passive</strong></td><td>Thermal IR ($10.5\text{--}12.5\text{ }\mu\text{m}$)</td><td>Emitted blackbody radiance</td><td>Land surface temperature, volcanic geothermal anomalies</td></tr>
            <tr><td>Passive Microwave Radiometer (e.g. AMSR-2)</td><td><strong>Passive</strong></td><td>Microwave ($6.9\text{--}89\text{ GHz}$)</td><td>Natural microwave brightness temp</td><td>Sea ice extent, global atmospheric water vapor</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Why are active radar remote sensing systems capable of imaging the Earth during nighttime and through heavy overcast clouds?</div>
        <div class="pq-ans">Answer: Active radar provides its own illumination source and operates at microwave wavelengths ($>1\text{ cm}$) that experience virtually zero Rayleigh or Mie scattering by cloud droplets.</div>
        <div class="pq-exp">Microwave wavelengths are several orders of magnitude larger than cloud droplets (~10-50 $\mu$m), rendering clouds transparent.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which active optical sensor is widely used for creating bare-earth Digital Elevation Models beneath dense forest canopies?</div>
        <div class="pq-ans">Answer: Airborne LiDAR (Light Detection and Ranging).</div>
        <div class="pq-exp">A single LiDAR pulse emits millions of laser shots per second, producing multiple returns; intermediate returns record canopy branches while the final return penetrates to bare ground.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What does InSAR stand for and why is it categorized as an active technique?</div>
        <div class="pq-ans">Answer: Interferometric Synthetic Aperture Radar; it compares phase differences between two coherent SAR radar pulses emitted and recorded by active microwave antennas.</div>
        <div class="pq-exp">InSAR can detect millimeter-scale crustal deformation from earthquakes, volcanic inflation, and groundwater extraction.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the fundamental disadvantage of active remote sensing systems compared to passive systems?</div>
        <div class="pq-ans">Answer: High electrical power consumption, heavy payload mass, complex instrument design, and limited spectral diagnostic capability compared to hyperspectral systems.</div>
        <div class="pq-exp">Generating high-power coherent electromagnetic pulses onboard a satellite demands large solar arrays and complex battery storage systems.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which parameter of an active microwave radar signal allows discrimination of smooth vs. rough geological surfaces?</div>
        <div class="pq-ans">Answer: Radar backscatter coefficient ($\sigma^\circ$, expressed in decibels, dB) governed by the Rayleigh roughness criterion.</div>
        <div class="pq-exp">Smooth surfaces reflect radar specularly away (dark on image), whereas rough surfaces scatter diffuse backscatter back to the antenna (bright on image).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Is a photographic flash attached to a camera an active or passive remote sensing system?</div>
        <div class="pq-ans">Answer: Active, because the system supplies its own artificial illumination pulse to illuminate the object.</div>
        <div class="pq-exp">Without the flash, photography using natural ambient daylight is passive remote sensing.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What active sensor onboard NASA's ICESat-2 satellite measures ice sheet elevation using photon-counting technology?</div>
        <div class="pq-ans">Answer: ATLAS (Advanced Topographic Laser Altimeter System), an active green laser ($532\text{ nm}$) LiDAR.</div>
        <div class="pq-exp">ATLAS records individual photon time-of-flight to measure surface elevations with centimeter-scale precision.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the primary difference between a radar scatterometer and a synthetic aperture radar (SAR)?</div>
        <div class="pq-ans">Answer: A scatterometer is a non-imaging active radar measuring broad backscatter cross-sections (often for ocean surface wind vectors), while SAR synthesizes a large antenna aperture to produce high-resolution imagery.</div>
        <div class="pq-exp">Both are active microwave sensors, but SAR applies Doppler phase history processing to achieve fine spatial resolution.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q124: Coherence Length vs Spectral Bandwidth
# -----------------------------------------------------------------------------
def gen_q124():
    q_num = 124
    filename = "Q124_Coherence_Length_Inversely_Proportional_Bandwidth_Complete_Guide.html"
    title = "Q124: Wave Optics - Coherence Length and Spectral Bandwidth"
    badge = "OPSC 2019 Geology Paper-II • Question 124 • Wave Optics & Radar"
    h1_title = "Wave Optics & Interferometry: The Coherence Length and Spectral Bandwidth Reciprocal Law"
    meta_text = r"<strong>Topic:</strong> Coherence Optics & Radar Remote Sensing • <strong>Key Concept:</strong> Temporal Coherence Length ($L_c$) & Spectral Bandwidth ($\Delta \nu$) • <strong>Textbooks:</strong> Eugene Hecht (<em>Optics</em>, 5th Ed., Ch. 7 & 12); Max Born & Emil Wolf (<em>Principles of Optics</em>); T.M. Lillesand et al. (Ch. 8)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Temporal Coherence and Coherence Length</div>
      <p>In electromagnetic wave theory, physical optics, and radar interferometry (InSAR), <strong>coherence</strong> measures the degree of correlation between the phase and amplitude of a wave field at different spatial points or times. <strong>Temporal coherence</strong> describes how monochromatic and phase-predictable a propagating wave remains over time.</p>

      <p>No physical light or radar source is purely monochromatic; real waves consist of a wavepacket containing a finite spread of frequencies known as the <strong>spectral bandwidth</strong> ($\Delta \nu$ in Hertz or $\Delta \lambda$ in meters). The <strong>coherence time</strong> ($\tau_c$) is the average temporal duration over which the wave packet maintains a stable phase relationship, given by the Fourier transform uncertainty principle:</p>

      <div class="math-block">
        $$\tau_c \approx \frac{1}{\Delta \nu}$$
      </div>

      <p>The <strong>coherence length</strong> ($L_c$) represents the propagation distance along the beam path over which the wave packet maintains a strong, predictable phase and amplitude relationship:</p>

      <div class="math-block">
        $$L_c = c \cdot \tau_c = \frac{c}{\Delta \nu}$$
      </div>

      <p>where $c$ is the speed of light in the medium and $\Delta \nu$ is the spectral bandwidth in frequency. In terms of central wavelength ($\lambda_0$) and wavelength spread ($\Delta \lambda$):</p>

      <div class="math-block">
        $$\text{Since } \nu = \frac{c}{\lambda} \implies |\Delta \nu| \approx \frac{c}{\lambda_0^2} \Delta \lambda \implies L_c \approx \frac{\lambda_0^2}{\Delta \lambda}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Radiation Source</th>
              <th>Spectral Bandwidth ($\Delta \nu$)</th>
              <th>Wavelength Spread ($\Delta \lambda$)</th>
              <th>Coherence Length ($L_c$)</th>
              <th>Optical / Radar Behavior</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;">
              <td>Narrowband Stabilized He-Ne Laser</td>
              <td>$\approx 1\text{ kHz}$</td>
              <td>$\approx 10^{-6}\text{ nm}$</td>
              <td><strong>$300\text{ km}$</strong></td>
              <td>Extremely high temporal coherence; produces high-contrast interference fringes over macroscopic path differences.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td>Radar Local Oscillator / Chirp</td>
              <td>$\approx 10\text{--}100\text{ MHz}$</td>
              <td>Narrow RF band</td>
              <td><strong>$3\text{--}30\text{ m}$</strong></td>
              <td>Essential for pulse compression and Synthetic Aperture Radar (SAR) interferometry.</td>
            </tr>
            <tr>
              <td>Light Emitting Diode (LED)</td>
              <td>$\approx 10^{13}\text{ Hz}$</td>
              <td>$\approx 30\text{ nm}$</td>
              <td><strong>$\approx 20\text{ }\mu\text{m}$</strong></td>
              <td>Low coherence; interference fringes only observable over sub-millimeter path differences.</td>
            </tr>
            <tr>
              <td>Natural Sunlight (White Light)</td>
              <td>$\approx 3 \times 10^{14}\text{ Hz}$</td>
              <td>$\approx 300\text{ nm}$</td>
              <td><strong>$\approx 1\text{--}2\text{ }\mu\text{m}$</strong></td>
              <td>Essentially incoherent; fringes only seen in zero-path thin films (soap bubbles, oil slicks).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q124/coherence_length_inversely_proportional_bandwidth.png" alt="Coherence Length vs Spectral Bandwidth" class="figure-img">
        <div class="figure-caption">Figure 124: Inverse hyperbolic relationship between coherence length ($L_c$) and spectral bandwidth ($\Delta \nu$), illustrating that increasing bandwidth reduces wave coherence distance (Option B).</div>
      </div>

      <p>Therefore, the coherence length over which there is a strong relationship between wave amplitudes is <strong>strictly inversely proportional to the bandwidth</strong> ($L_c \propto \frac{1}{\Delta \nu}$, Option B).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 124</div>
        <div class="raw-q-text">The coherence length over which there is a strong relationship between amplitudes is:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Directly proportional to the bandwidth</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Inversely proportional to the bandwidth</div>
          <div class="raw-opt"><span class="opt-letter">C</span> The square of the bandwidth</div>
          <div class="raw-opt"><span class="opt-letter">D</span> The inverse of square of bandwidth</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Inversely proportional to the bandwidth)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Inversely proportional to the bandwidth</div>
          <p>By the fundamental Fourier uncertainty relationship between time and frequency ($\Delta t \cdot \Delta \nu \approx 1$), the coherence time is $\tau_c = 1/\Delta \nu$. Multiplying by wave propagation velocity $c$ yields $L_c = c/\Delta \nu$. As spectral bandwidth increases, phase de-correlation occurs over shorter spatial distances, making coherence length strictly <strong>inversely proportional</strong> to bandwidth.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Directly proportional to the bandwidth</div>
          <p>This implies that broadening the frequency spectrum increases coherence length, which is physically impossible. A broader spectrum contains many interfering frequency components that rapidly destroy phase alignment.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">The square of the bandwidth</div>
          <p>Incorrect mathematical relationship. Coherence length relates to bandwidth via an inverse first-order power law ($(\Delta \nu)^{-1}$), not a direct quadratic power law ($(\Delta \nu)^2$).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">The inverse of square of bandwidth</div>
          <p>Incorrect exponent. While coherence length is in the denominator ($1/\Delta \nu$), it depends on the first power of bandwidth, not the second power ($1/(\Delta \nu)^2$).</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Coherence Parameter</th>
              <th>Symbol</th>
              <th>Formula</th>
              <th>Units</th>
              <th>Physical Meaning</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Coherence Length</td><td>$L_c$</td><td>$L_c = \frac{c}{\Delta \nu} = \frac{\lambda^2}{\Delta \lambda}$</td><td>Meters ($\text{m}$)</td><td>Maximum path difference yielding interference fringes</td></tr>
            <tr><td>Coherence Time</td><td>$\tau_c$</td><td>$\tau_c = \frac{1}{\Delta \nu} = \frac{L_c}{c}$</td><td>Seconds ($\text{s}$)</td><td>Time interval over which wave phase remains predictable</td></tr>
            <tr><td>Spectral Bandwidth</td><td>$\Delta \nu$</td><td>$\Delta \nu = \frac{c}{\lambda^2} \Delta \lambda$</td><td>Hertz ($\text{Hz}$)</td><td>Full width at half maximum (FWHM) of power spectrum</td></tr>
            <tr><td>Complex Coherence (InSAR)</td><td>$\gamma$</td><td>$\gamma = \frac{\langle s_1 s_2^* \rangle}{\sqrt{\langle |s_1|^2 \rangle \langle |s_2|^2 \rangle}}$</td><td>Dimensionless ($0 \le |\gamma| \le 1$)</td><td>Degree of interferometric correlation between two radar passes</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Calculate the coherence length of a gas laser operating at $\lambda = 632.8\text{ nm}$ with a spectral linewidth $\Delta \lambda = 10^{-5}\text{ nm}$.</div>
        <div class="pq-ans">Answer: Approximately $40\text{ meters}$.</div>
        <div class="pq-exp">$$L_c = \frac{\lambda^2}{\Delta \lambda} = \frac{(632.8 \times 10^{-9}\text{ m})^2}{10^{-14}\text{ m}} \approx 40.04\text{ m}$$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What happens to the interference fringe visibility in a Michelson interferometer when the path difference exceeds $L_c$?</div>
        <div class="pq-ans">Answer: The fringe visibility drops to zero, and the interference pattern completely washes out into uniform background illumination.</div>
        <div class="pq-exp">When optical path difference $\Delta d > L_c$, the interfering wavepackets no longer overlap in phase.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between temporal coherence and spatial coherence?</div>
        <div class="pq-ans">Answer: Temporal coherence describes phase correlation at the same point in space across different time instants (linked to spectral bandwidth $\Delta \nu$); spatial coherence describes phase correlation across different points across the wavefront (linked to source angular size).</div>
        <div class="pq-exp">A point source has high spatial coherence; a strictly monochromatic source has high temporal coherence.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. In Synthetic Aperture Radar (SAR), why does chirping a transmitted pulse provide high range resolution without sacrificing power?</div>
        <div class="pq-ans">Answer: Chirping linearly sweeps the frequency across a wide bandwidth ($\Delta f$), allowing matched filter pulse compression into a very narrow effective pulse width $\tau = 1/\Delta f$.</div>
        <div class="pq-exp">Radar slant range resolution is given by $\Delta R = \frac{c}{2 \Delta f}$, depending solely on bandwidth.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why do white-light interferometers require the two optical arms to be matched to within a few micrometers?</div>
        <div class="pq-ans">Answer: Because broad white-light spectrum ($\Delta \lambda \approx 300\text{ nm}$) results in a tiny coherence length ($L_c \approx 1\text{--}2\text{ }\mu\text{m}$).</div>
        <div class="pq-exp">Fringes only exist when the optical path difference is smaller than this micro-scale coherence length.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is "coherence loss" or "decorrelation" in repeat-pass satellite radar interferometry (InSAR)?</div>
        <div class="pq-ans">Answer: The degradation of radar phase correlation between two acquisition dates caused by vegetation growth, wind, moisture changes, or excessive spatial baseline separation.</div>
        <div class="pq-exp">When temporal or geometric decorrelation occurs ($|\gamma| \to 0$), interferometric phase noise destroys elevation or deformation signals.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the critical baseline in SAR interferometry?</div>
        <div class="pq-ans">Answer: The maximum cross-track perpendicular baseline distance beyond which spectral shift decorrelation causes total loss of interferometric coherence ($|\gamma| = 0$).</div>
        <div class="pq-exp">The critical baseline is inversely proportional to radar wavelength and receiver bandwidth.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What fundamental theorem relates the spatial coherence of an incoherent extended optical source to the Fourier transform of its intensity distribution?</div>
        <div class="pq-ans">Answer: The Van Cittert-Zernike Theorem.</div>
        <div class="pq-exp">It explains how an incoherent source (like a distant star) produces high spatial coherence on Earth across small baseline separations.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q125: Atmospheric Windows in Remote Sensing
# -----------------------------------------------------------------------------
def gen_q125():
    q_num = 125
    filename = "Q125_Spectral_Region_Passes_Through_Atmosphere_Atmospheric_Window_Complete_Guide.html"
    title = "Q125: Remote Sensing - Atmospheric Windows and Atmospheric Transmission"
    badge = "OPSC 2019 Geology Paper-II • Question 125 • Atmospheric Physics"
    h1_title = "Atmospheric Radiative Transfer: Atmospheric Windows and Transmission Bands in Remote Sensing"
    meta_text = "<strong>Topic:</strong> Atmospheric Attenuation & Remote Sensing Spectrum • <strong>Key Concept:</strong> Atmospheric Transmission Windows vs. Absorption Bands ($\text{H}_2\text{O}, \text{CO}_2, \text{O}_3$) • <strong>Textbooks:</strong> T.M. Lillesand, R.W. Kiefer, & J.W. Chipman (Ch. 1); K.M. Bangar (p. 208); Floyd F. Sabins (Ch. 2)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Atmospheric Absorption and Atmospheric Windows</div>
      <p>Electromagnetic radiation propagating through the Earth's atmosphere undergoes <strong>attenuation</strong> via two distinct physical processes: <strong>scattering</strong> (Rayleigh, Mie, and non-selective scattering by gas molecules, aerosols, and water droplets) and <strong>absorption</strong> (quantum transition absorption by atmospheric gases, primarily $\text{H}_2\text{O}, \text{CO}_2, \text{O}_3, \text{CH}_4$, and $\text{N}_2\text{O}$).</p>

      <p>Atmospheric absorption varies dramatically across the electromagnetic spectrum. The spectral regions where atmospheric gases absorb strongly are termed <strong>absorption bands</strong> (opaque to EMR). Conversely, the specific wavelength ranges where the atmosphere is highly transparent and allows radiation to pass through without substantial attenuation are formally designated as <strong>Atmospheric Windows</strong> (Lillesand & Kiefer; Sabins; Bangar):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Atmospheric Window</th>
              <th>Spectral Range</th>
              <th>Primary Absorbers Outside Window</th>
              <th>Remote Sensing Sensor Utilization</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;">
              <td><strong>Visible & Near-Infrared (VNIR)</strong></td>
              <td>$0.4\text{--}1.0\text{ }\mu\text{m}$</td>
              <td>UV ozone absorption ($\lambda < 0.3\text{ }\mu\text{m}$) and water vapor bands</td>
              <td>Landsat, Sentinel-2, IRS LISS-IV, aerial cameras; optical vegetation & geology mapping.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>Shortwave Infrared 1 (SWIR-1)</strong></td>
              <td>$1.55\text{--}1.75\text{ }\mu\text{m}$</td>
              <td>$\text{H}_2\text{O}$ vapor absorption at $1.4\text{ }\mu\text{m}$ and $1.9\text{ }\mu\text{m}$</td>
              <td>Moisture stress, snow/cloud discrimination, lithological clay delineation.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>Shortwave Infrared 2 (SWIR-2)</strong></td>
              <td>$2.08\text{--}2.35\text{ }\mu\text{m}$</td>
              <td>Strong $\text{H}_2\text{O}$ absorption at $1.9\text{ }\mu\text{m}$ and $\text{CO}_2$ at $2.7\text{ }\mu\text{m}$</td>
              <td>Hydrothermal alteration minerals (alunite, kaolinite, illite), carbonate absorption.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>Thermal Infrared 1 (TIR-1)</strong></td>
              <td>$3.5\text{--}4.1\text{ }\mu\text{m}$ (Mid-IR)</td>
              <td>$\text{CO}_2$ at $4.3\text{ }\mu\text{m}$</td>
              <td>Wildfire detection, volcanic hot-spot monitoring, night sea-surface temperature.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>Thermal Infrared 2 (TIR-2)</strong></td>
              <td>$8.0\text{--}14.0\text{ }\mu\text{m}$ (split by $\text{O}_3$ at $9.6\text{ }\mu\text{m}$)</td>
              <td>Strong $\text{H}_2\text{O}$ vapor band below $8\text{ }\mu\text{m}$ and $\text{CO}_2$ above $14\text{ }\mu\text{m}$</td>
              <td>Peak terrestrial thermal emission ($\sim 300\text{ K}$, $\lambda_{\text{max}} \approx 9.7\text{ }\mu\text{m}$); land surface temperature.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>Microwave Window</strong></td>
              <td>$1\text{ mm}$ to $>1\text{ m}$</td>
              <td>Minor oxygen ($60\text{ GHz}$) and $\text{H}_2\text{O}$ ($22\text{ GHz}$) lines</td>
              <td>Synthetic Aperture Radar (SAR), radar altimeters; complete cloud/haze penetration.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q125/atmospheric_windows_electromagnetic_transmission.png" alt="Atmospheric Windows in Remote Sensing" class="figure-img">
        <div class="figure-caption">Figure 125: Atmospheric transmission percentage as a function of wavelength, highlighting the primary Atmospheric Windows (Option B) utilized by satellite sensors.</div>
      </div>

      <p>Because satellite sensors cannot record meaningful surface data in opaque spectral regions, all spaceborne optical, thermal, and microwave sensors are strictly engineered to operate inside these <strong>Atmospheric Windows</strong> (Option B).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 125</div>
        <div class="raw-q-text">The spectral region of the electromagnetic radiation which passes through the atmosphere without much attenuation in known as:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Ozone hole</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Atmospheric window</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Ozone window</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Black hole</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Atmospheric window)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Atmospheric window</div>
          <p>By international scientific definition across remote sensing, meteorology, and astrophysics (Lillesand & Kiefer; Sabins; Bangar, p. 208), an <strong>Atmospheric Window</strong> is a wavelength band where the transmission of electromagnetic radiation through the Earth's atmosphere approaches high percentages with minimal attenuation from absorption or scattering.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Ozone hole</div>
          <p>The "ozone hole" refers to seasonal anthropogenic stratospheric depletion of ozone ($\text{O}_3$) over Antarctica caused by chlorofluorocarbons (CFCs). It is an atmospheric environmental phenomenon, not a spectral transmission window.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Ozone window</div>
          <p>Ozone is an intense absorber of ultraviolet radiation (Hartley/Huggins bands, $\lambda < 0.32\text{ }\mu\text{m}$) and exhibits a prominent absorption band at $9.6\text{ }\mu\text{m}$ in the thermal infrared. There is no standard remote sensing term called an "ozone window".</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Black hole</div>
          <p>A black hole is a general relativistic astronomical object whose gravitational field is so intense that nothing, not even electromagnetic radiation, can escape from beyond its event horizon. It has zero connection to terrestrial remote sensing.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Atmospheric Gas</th>
              <th>Primary Absorption Wavelengths</th>
              <th>Absorption Mechanism</th>
              <th>Impact on Satellite Remote Sensing</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Water Vapor ($\text{H}_2\text{O}$)</td><td>$0.9\text{ }\mu\text{m}, 1.1\text{ }\mu\text{m}, 1.4\text{ }\mu\text{m}, 1.9\text{ }\mu\text{m}, 5.5\text{--}7.5\text{ }\mu\text{m}$</td><td>Molecular vibration-rotation bands</td><td>Creates major blind zones separating VNIR, SWIR-1, and SWIR-2 windows</td></tr>
            <tr><td>Carbon Dioxide ($\text{CO}_2$)</td><td>$2.7\text{ }\mu\text{m}, 4.3\text{ }\mu\text{m}, 13\text{--}17.5\text{ }\mu\text{m}$</td><td>Asymmetric stretch & bending vibrations</td><td>Terminates the longwave thermal infrared window at $14\text{ }\mu\text{m}$</td></tr>
            <tr><td>Ozone ($\text{O}_3$)</td><td>$<0.32\text{ }\mu\text{m}$ (UV) & $9.6\text{ }\mu\text{m}$ (TIR)</td><td>Electronic transitions (UV) & asymmetric stretch (IR)</td><td>Shields Earth from lethal UV-C/B; divides the $8\text{--}14\text{ }\mu\text{m}$ thermal window</td></tr>
            <tr><td>Oxygen ($\text{O}_2$)</td><td>$0.76\text{ }\mu\text{m}$ (Fraunhofer A-band) & $60\text{ GHz}$</td><td>Electronic and magnetic dipole transitions</td><td>Used for atmospheric pressure and cloud-top height sounding</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Why are the spectral bands around $1.4\text{ }\mu\text{m}$ and $1.9\text{ }\mu\text{m}$ omitted from optical satellite sensors like Landsat and Sentinel-2?</div>
        <div class="pq-ans">Answer: Because atmospheric water vapor ($\text{H}_2\text{O}$) strongly absorbs all radiation in these bands, rendering the atmosphere opaque.</div>
        <div class="pq-exp">Sensors split their shortwave infrared detectors into SWIR-1 ($1.55\text{--}1.75\text{ }\mu\text{m}$) and SWIR-2 ($2.1\text{--}2.3\text{ }\mu\text{m}$) around these water absorption peaks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which atmospheric window is utilized to monitor Earth's ambient land surface temperatures (LST) and sea surface temperatures (SST)?</div>
        <div class="pq-ans">Answer: The $8.0\text{--}14.0\text{ }\mu\text{m}$ thermal infrared window (specifically $10.5\text{--}12.5\text{ }\mu\text{m}$).</div>
        <div class="pq-exp">By Wien's displacement law, the Earth at $300\text{ K}$ emits peak radiant energy at $\lambda_{\text{max}} = 2898 / 300 \approx 9.7\text{ }\mu\text{m}$, right inside this window.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the "red edge" in remote sensing and in which atmospheric window does it occur?</div>
        <div class="pq-ans">Answer: The abrupt increase in plant leaf reflectance between the red chlorophyll absorption trough ($0.68\text{ }\mu\text{m}$) and the near-infrared mesophyll reflection plateau ($0.75\text{--}0.85\text{ }\mu\text{m}$) in the VNIR window.</div>
        <div class="pq-exp">The red edge is the fundamental diagnostic feature used in NDVI and vegetation vigor indices.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Why does Rayleigh scattering primarily affect the visible blue band rather than infrared windows?</div>
        <div class="pq-ans">Answer: Rayleigh scattering cross-section is inversely proportional to the fourth power of wavelength ($\sigma_R \propto \lambda^{-4}$).</div>
        <div class="pq-exp">Blue light ($\lambda \approx 0.45\text{ }\mu\text{m}$) is scattered $\approx 5.5$ times more intensely than red light ($\lambda \approx 0.70\text{ }\mu\text{m}$), creating atmospheric haze.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which atmospheric window is completely immune to cloud cover, rain, and haze?</div>
        <div class="pq-ans">Answer: The microwave window ($\lambda > 1\text{ cm}$, e.g. C, S, L, and P radar bands).</div>
        <div class="pq-exp">Because radar wavelengths are orders of magnitude larger than rain and cloud droplet radii, scattering is negligible.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which diagnostic mineral absorption feature occurs in the $2.1\text{--}2.35\text{ }\mu\text{m}$ (SWIR-2) atmospheric window?</div>
        <div class="pq-ans">Answer: $\text{Al-OH}$ and $\text{Mg-OH}$ molecular bond vibrational overtones and combinations in clay minerals (kaolinite, illite, montmorillonite) and micas.</div>
        <div class="pq-exp">This window enables spaceborne mapping of hydrothermal alteration zones associated with porphyry copper and epithermal gold deposits.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the ozone absorption feature that divides the thermal infrared window into two parts?</div>
        <div class="pq-ans">Answer: The $9.6\text{ }\mu\text{m}$ stratospheric ozone absorption band.</div>
        <div class="pq-exp">Sensors split the TIR window around $9.6\text{ }\mu\text{m}$ into Band 10 ($10.6\text{--}11.2\text{ }\mu\text{m}$) and Band 11 ($11.5\text{--}12.5\text{ }\mu\text{m}$) for split-window atmospheric correction.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is "path radiance" in remote sensing atmospheric transmission?</div>
        <div class="pq-ans">Answer: Sunlight scattered directly into the sensor's field of view by the atmosphere without ever reaching the ground surface.</div>
        <div class="pq-exp">Path radiance adds an unwanted additive haze offset ($L_p$) to dark water and shadow targets, requiring atmospheric dark-object subtraction (DOS).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q126: Planck's Law Energy Quantum E = h * nu
# -----------------------------------------------------------------------------
def gen_q126():
    q_num = 126
    filename = "Q126_Energy_Quantum_Radiation_Proportional_To_Frequency_Complete_Guide.html"
    title = "Q126: Radiation Physics - Planck's Law and Energy Quantum"
    badge = "OPSC 2019 Geology Paper-II • Question 126 • Quantum & Radiation Physics"
    h1_title = "Radiation Physics: Planck's Law and the Proportionality of Energy Quanta to Frequency"
    meta_text = "<strong>Topic:</strong> Electromagnetic Radiation Physics & Quantum Mechanics • <strong>Key Concept:</strong> Planck's Postulate ($E = h\nu$), Photon Energy & Wave-Particle Duality • <strong>Textbooks:</strong> Max Planck (1900); Arthur Beiser (<em>Concepts of Modern Physics</em>); T.M. Lillesand et al. (Ch. 1); K.M. Bangar (p. 208)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Planck's Quantum Hypothesis and Photon Energy</div>
      <p>In classical electrodynamics, James Clerk Maxwell modeled electromagnetic radiation as continuous transverse waves governed by Maxwell's equations. However, classical theory failed to explain the spectral distribution of blackbody radiation (leading to the catastrophic "ultraviolet catastrophe" predicted by the Rayleigh-Jeans law).</p>

      <p>In 1900, <strong>Max Planck</strong> revolutionized modern physics by postulating that electromagnetic energy is not emitted or absorbed continuously, but in discrete, indivisible packets or packets of energy termed <strong>quanta</strong> (later called <strong>photons</strong> by Gilbert Lewis, 1926). Planck's fundamental equation states:</p>

      <div class="math-block">
        $$E = h \cdot \nu$$
      </div>

      <p>where:</p>
      <ul>
        <li>$E$ = Energy of a single quantum (photon), in Joules ($\text{J}$) or electron-volts ($\text{eV}$).</li>
        <li>$h$ = <strong>Planck's constant</strong> ($h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s} = 4.135667 \times 10^{-15}\text{ eV}\cdot\text{s}$).</li>
        <li>$\nu$ = Frequency of the electromagnetic radiation, in Hertz ($\text{Hz}$ or $\text{s}^{-1}$).</li>
      </ul>

      <p>Since the frequency $\nu$ is related to wavelength $\lambda$ by the speed of light $c = \nu \lambda$, the energy quantum can equivalently be expressed in terms of wavelength:</p>

      <div class="math-block">
        $$E = \frac{h \cdot c}{\lambda}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Spectral Region</th>
              <th>Typical Wavelength ($\lambda$)</th>
              <th>Frequency ($\nu$)</th>
              <th>Photon Energy Quantum ($E = h\nu$)</th>
              <th>Interaction with Matter / Detector Technology</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Gamma Rays</td>
              <td>$10^{-12}\text{ m}$</td>
              <td>$3 \times 10^{20}\text{ Hz}$</td>
              <td>$1.24\text{ MeV}$</td>
              <td>Nuclear photo-disintegration; scintillation crystals.</td>
            </tr>
            <tr>
              <td>X-Rays</td>
              <td>$10^{-10}\text{ m}$</td>
              <td>$3 \times 10^{18}\text{ Hz}$</td>
              <td>$12.4\text{ keV}$</td>
              <td>Inner-shell atomic electron ionization (XRD / XRF).</td>
            </tr>
            <tr>
              <td>Ultraviolet (UV)</td>
              <td>$300\text{ nm}$</td>
              <td>$10^{15}\text{ Hz}$</td>
              <td>$4.13\text{ eV}$</td>
              <td>Valence electron excitation; photochemical reactions.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Visible Spectrum</strong></td>
              <td>$500\text{ nm}$ (Green)</td>
              <td>$6 \times 10^{14}\text{ Hz}$</td>
              <td><strong>$2.48\text{ eV}$</strong></td>
              <td>Silicon CCD/CMOS photoelectric bandgap excitation.</td>
            </tr>
            <tr>
              <td>Shortwave Infrared (SWIR)</td>
              <td>$2.0\text{ }\mu\text{m}$</td>
              <td>$1.5 \times 10^{14}\text{ Hz}$</td>
              <td>$0.62\text{ eV}$</td>
              <td>Molecular bond stretching overtones (InGaAs / HgCdTe).</td>
            </tr>
            <tr>
              <td>Thermal Infrared (TIR)</td>
              <td>$10.0\text{ }\mu\text{m}$</td>
              <td>$3 \times 10^{13}\text{ Hz}$</td>
              <td>$0.124\text{ eV}$</td>
              <td>Molecular rotational-vibrational states; microbolometers.</td>
            </tr>
            <tr>
              <td>Microwave / Radar</td>
              <td>$3\text{ cm}$ (X-Band)</td>
              <td>$10\text{ GHz}$</td>
              <td>$4.14 \times 10^{-5}\text{ eV}$</td>
              <td>Free electron oscillations in metals; antenna voltage induction.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q126/planck_quantum_energy_proportional_to_frequency.png" alt="Planck's Quantum Energy Law" class="figure-img">
        <div class="figure-caption">Figure 126: Linear relationship between quantum energy ($E$) and electromagnetic radiation frequency ($\nu$), verifying Planck's law $E = h\nu$ (Option A).</div>
      </div>

      <p>From the foundational formula $E = h\nu$, the value of the energy quantum for radiation of any frequency is <strong>directly proportional to the frequency</strong> ($\mathbf{E \propto \nu}$, Option A).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 126</div>
        <div class="raw-q-text">The value of energy quantum for radiation of any frequency is proportional to :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> The frequency</div>
          <div class="raw-opt"><span class="opt-letter">B</span> The reciprocal of the energy</div>
          <div class="raw-opt"><span class="opt-letter">C</span> The square of the frequency</div>
          <div class="raw-opt"><span class="opt-letter">D</span> The square root of the frequency</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (The frequency)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">The frequency</div>
          <p>By Planck's law ($E = h\nu$), the energy of an electromagnetic photon is directly proportional to its frequency $\nu$, with Planck's constant $h$ acting as the invariant constant of proportionality. Higher frequency radiation (such as UV or X-rays) carries proportionally higher energy per quantum than lower frequency radiation (such as infrared or radio waves).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">The reciprocal of the energy</div>
          <p>Self-referential and physically meaningless. Energy cannot be proportional to its own reciprocal ($E \propto 1/E \implies E^2 = \text{const}$). The energy quantum is inversely proportional to wavelength ($E \propto 1/\lambda$), but not to the reciprocal of energy.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">The square of the frequency</div>
          <p>Incorrect power law. Wave intensity or radiated power from an accelerating dipole scales with frequency squared or fourth power, but the fundamental quantum energy packet $E$ scales strictly linearly with $\nu^1$, not $\nu^2$.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">The square root of the frequency</div>
          <p>Incorrect exponent. Energy depends on the first power of frequency ($\nu^1$), not the square root ($\nu^{1/2}$).</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Radiation Physics Law</th>
              <th>Mathematical Equation</th>
              <th>Primary Physical Constant</th>
              <th>Core Scientific Application</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Planck's Quantum Law</strong></td><td>$E = h\nu = \frac{hc}{\lambda}$</td><td>$h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$</td><td>Energy of individual photons; photoelectric detection</td></tr>
            <tr><td>Stefan-Boltzmann Law</td><td>$M = \sigma T^4$</td><td>$\sigma = 5.670 \times 10^{-8}\text{ W}\cdot\text{m}^{-2}\text{K}^{-4}$</td><td>Total radiant exitance emitted by a blackbody at temperature $T$</td></tr>
            <tr><td>Wien's Displacement Law</td><td>$\lambda_{\text{max}} = \frac{A}{T}$</td><td>$A \approx 2898\text{ }\mu\text{m}\cdot\text{K}$</td><td>Peak emission wavelength of radiating blackbody</td></tr>
            <tr><td>Kirchhoff's Radiation Law</td><td>$\epsilon(\lambda) = \alpha(\lambda)$</td><td>Dimensionless ($0 \le \epsilon \le 1$)</td><td>At thermal equilibrium, spectral emissivity equals spectral absorptivity</td></tr>
            <tr><td>Beer-Lambert Law</td><td>$I = I_0 e^{-\alpha x}$</td><td>$\alpha$ = absorption coefficient</td><td>Atmospheric and optical attenuation through a medium</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the energy in electron-volts ($\text{eV}$) of a green photon with a wavelength of $\lambda = 500\text{ nm}$?</div>
        <div class="pq-ans">Answer: Approximately $2.48\text{ eV}$.</div>
        <div class="pq-exp">$$E(\text{eV}) \approx \frac{1240}{\lambda(\text{nm})} = \frac{1240}{500} = 2.48\text{ eV}$$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why do optical satellite detectors need cooling when operating in the thermal infrared ($8\text{--}14\text{ }\mu\text{m}$) but not in the visible band?</div>
        <div class="pq-ans">Answer: Because thermal infrared photons have very low quantum energy ($\approx 0.1\text{ eV}$), ambient room-temperature thermal vibrations ($k_B T \approx 0.026\text{ eV}$) can excite noise electrons unless cooled to cryo-temperatures (~77 K).</div>
        <div class="pq-exp">Visible photons have high energy (~2-3 eV), far above ambient thermal excitation thresholds.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the value of Planck's constant in SI units ($\text{J}\cdot\text{s}$)?</div>
        <div class="pq-ans">Answer: $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$ (an exact defined fundamental constant in SI since 2019).</div>
        <div class="pq-exp">It fixes the scale of quantum mechanical phenomena throughout the universe.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. If the frequency of an electromagnetic wave is tripled, what happens to the energy of each of its photons?</div>
        <div class="pq-ans">Answer: The energy of each photon triples ($E_2 = 3 E_1$).</div>
        <div class="pq-exp">This follows directly from the linear proportionality $E \propto \nu$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which experimental discovery by Albert Einstein in 1905 provided definitive proof for Planck's quantum hypothesis?</div>
        <div class="pq-ans">Answer: The Photoelectric Effect (for which Einstein was awarded the 1921 Nobel Prize in Physics).</div>
        <div class="pq-exp">Einstein demonstrated that electrons are ejected from a metal surface only if the incident photon frequency exceeds a threshold frequency ($\nu_0$), regardless of beam intensity.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does quantum energy explain why microwaves cannot cause chemical ionization?</div>
        <div class="pq-ans">Answer: Microwave photon energies are tiny ($\sim 10^{-5}\text{ eV}$), millions of times lower than the energy required to break chemical bonds or ionize atoms ($\sim 1\text{--}10\text{ eV}$).</div>
        <div class="pq-exp">Microwaves only cause rotational thermal motion of dipolar water molecules.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the relationship between the energy of a quantum and its momentum ($p$)?</div>
        <div class="pq-ans">Answer: $p = \frac{E}{c} = \frac{h}{\lambda}$ (de Broglie / Einstein momentum relation).</div>
        <div class="pq-exp">Even though photons have zero rest mass, they carry momentum and exert radiation pressure on planetary bodies.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a "quantum detector" in satellite remote sensing?</div>
        <div class="pq-ans">Answer: A semiconductor sensor (photodiode or photoconductor) where individual absorbed photons directly excite electron-hole pairs across the bandgap.</div>
        <div class="pq-exp">Quantum detectors (e.g. Si, InGaAs, HgCdTe) offer ultra-fast response times and high sensitivity compared to thermal detectors (bolometers).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q127: Relief (Height) Displacement of Two Towers A (3 km) and B (5 km)
# -----------------------------------------------------------------------------
def gen_q127():
    q_num = 127
    filename = "Q127_Aerial_Photogrammetry_Relief_Height_Displacement_Towers_Complete_Guide.html"
    title = "Q127: Aerial Photogrammetry - Relief Displacement of Towers"
    badge = "OPSC 2019 Geology Paper-II • Question 127 • Aerial Photogrammetry"
    h1_title = "Aerial Photogrammetry: Relief (Height) Displacement Mechanics for Vertical Towers"
    meta_text = r"<strong>Topic:</strong> Geometric Photogrammetry & Image Geometry • <strong>Key Concept:</strong> Relief Displacement Formula ($d = \frac{r \cdot h}{H}$) & Radial Direction • <strong>Textbooks:</strong> P.R. Wolf & B.A. Dewitt (<em>Elements of Photogrammetry with Applications in GIS</em>, 4th Ed.); T.M. Lillesand et al. (Ch. 3); K.M. Bangar (p. 211)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Relief Displacement in Aerial Photography</div>
      <p>In a true vertical aerial photograph, terrain features are imaged through a central perspective projection centered at the camera lens. Unlike an orthogonal map where scale is uniform and projection is vertical everywhere, vertical aerial photographs undergo <strong>relief displacement</strong> (also known as <em>height displacement</em>).</p>

      <p><strong>Relief displacement</strong> ($d$) is defined as the shift or displacement in the photographic position of an elevated point relative to its true datum position, caused purely by the height of the object above the reference datum. For a vertical aerial photograph, the mathematical formula for relief displacement is (Wolf & Dewitt; Lillesand & Kiefer):</p>

      <div class="math-block">
        $$d = \frac{r \cdot h}{H}$$
      </div>

      <p>where:</p>
      <ul>
        <li>$d$ = Relief displacement on the photograph or ground reference scale.</li>
        <li>$r$ = <strong>Radial distance</strong> from the <strong>nadir point</strong> (or principal point) to the top of the elevated object.</li>
        <li>$h$ = <strong>Physical height</strong> of the vertical object above the datum.</li>
        <li>$H$ = <strong>Flying height</strong> of the aircraft above the same datum ($H \gg h$).</li>
      </ul>

      <p>From this governing equation, fundamental geometric laws of relief displacement are established:</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Photogrammetric Property</th>
              <th>Mathematical Dependence</th>
              <th>Physical Meaning</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#f0fdf4; font-weight:700;">
              <td><strong>Direct Proportionality to Radial Distance ($r$)</strong></td>
              <td>$$d \propto r \quad (\text{for constant } h \text{ and } H)$$</td>
              <td>An object situated further from the nadir point experiences proportionally <strong>greater relief displacement</strong> than an identical object closer to nadir.</td>
            </tr>
            <tr>
              <td>Direct Proportionality to Object Height ($h$)</td>
              <td>$$d \propto h \quad (\text{for constant } r \text{ and } H)$$</td>
              <td>A taller tower exhibits greater relief displacement than a shorter tower at the same radial distance.</td>
            </tr>
            <tr>
              <td>Inverse Proportionality to Flying Height ($H$)</td>
              <td>$$d \propto \frac{1}{H}$$</td>
              <td>Higher altitude flights compress perspective distortions and minimize relief displacement.</td>
            </tr>
            <tr>
              <td>Radial Directionality</td>
              <td>Radially outward from the Nadir Point</td>
              <td>Points elevated above datum displace <em>outward</em> away from nadir; depressions displace <em>inward</em> toward nadir.</td>
            </tr>
            <tr>
              <td>Zero Displacement at Nadir</td>
              <td>$$r = 0 \implies d = 0$$</td>
              <td>At the exact nadir point, the line of sight is purely vertical; no relief displacement occurs.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q127/aerial_photogrammetry_relief_height_displacement_towers.png" alt="Relief Displacement of Towers A and B" class="figure-img">
        <div class="figure-caption">Figure 127: Photogrammetric geometry for two towers A ($r_A = 3\text{ km}$) and B ($r_B = 5\text{ km}$) of equal height $h$, proving that $d_A < d_B$ (Option A).</div>
      </div>

      <h4>Step-by-Step Analytical Proof for Towers A and B:</h4>
      <p>We are given two towers, $A$ and $B$, with identical heights ($h_A = h_B = h$) situated diametrically opposite across the nadir point:</p>
      <ul>
        <li>Radial distance of Tower $A$ from nadir: $r_A = 3\text{ km}$.</li>
        <li>Radial distance of Tower $B$ from nadir: $r_B = 5\text{ km}$.</li>
        <li>Aircraft flying height is constant: $H_A = H_B = H$.</li>
      </ul>

      <p>Applying the relief displacement formula:</p>
      <div class="math-block">
        $$d_A = \frac{r_A \cdot h}{H} = \frac{3 \cdot h}{H}$$
        $$d_B = \frac{r_B \cdot h}{H} = \frac{5 \cdot h}{H}$$
        $$\frac{d_A}{d_B} = \frac{r_A}{r_B} = \frac{3}{5} = 0.6 \implies d_A = 0.6 \cdot d_B < d_B$$
      </div>

      <p>Therefore, the <strong>height displacement of A will be less than that of B</strong> ($\mathbf{d_A < d_B}$, Option A). Furthermore, because both towers are elevated above the ground datum, both displacements point <em>radially outward away from the nadir point</em> (away from each other, refuting Option D).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 127</div>
        <div class="raw-q-text">A and B are two towers of equal height diametrically opposite on either side of the nadir point at 3 km and 5 km distances. Then, which one of the following statements is correct ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Height displacement of A will be less than that of B</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Height displacement of B will be less than that of A</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Height displacement of A and B is equal</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Height displacement of A and B will be towards each other</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Height displacement of A will be less than that of B)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Height displacement of A will be less than that of B</div>
          <p>By the relief displacement formula $d = \frac{r \cdot h}{H}$, relief displacement is directly proportional to the radial distance ($r$) from the nadir point. Since Tower A is located at $r_A = 3\text{ km}$ and Tower B at $r_B = 5\text{ km}$, and both possess identical heights $h$, $d_A = \frac{3h}{H} < d_B = \frac{5h}{H}$. Hence, the height displacement of Tower A is strictly less than that of Tower B.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Height displacement of B will be less than that of A</div>
          <p>This contradicts the governing linear relationship $d \propto r$. Tower B is further from the nadir point ($5\text{ km} > 3\text{ km}$); therefore, Tower B must experience greater, not lesser, relief displacement.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Height displacement of A and B is equal</div>
          <p>Equal height displacement would only occur if both towers were located at identical radial distances ($r_A = r_B$). Since $3\text{ km} \ne 5\text{ km}$, their displacements cannot be equal.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Height displacement of A and B will be towards each other</div>
          <p>Relief displacement for any feature elevated above ground datum acts <strong>radially outward</strong> away from the nadir point. Because the towers lie on opposite sides of nadir, their tops lean outward in opposite directions (away from each other), never towards each other.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Point on Photograph</th>
              <th>Radial Distance ($r$)</th>
              <th>Object Height ($h$)</th>
              <th>Displacement Formula ($d$)</th>
              <th>Direction of Displacement</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Exact Nadir Point ($r = 0$)</td><td>0 mm</td><td>Any height $h$</td><td>$d = 0$</td><td>No displacement (pure vertical line of sight)</td></tr>
            <tr style="background:#eff6ff;"><td>Tower A (Inner radial zone)</td><td>$3\text{ km}$ ground ($r_A$)</td><td>$h$</td><td>$d_A = \frac{3h}{H}$</td><td>Radially outward (West of nadir)</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>Tower B (Outer radial zone)</td><td>$5\text{ km}$ ground ($r_B$)</td><td>$h$</td><td>$d_B = \frac{5h}{H} = 1.67 d_A$</td><td>Radially outward (East of nadir)</td></tr>
            <tr><td>Topographic Depression (Valley)</td><td>$r$</td><td>$-h$ (below datum)</td><td>$d = -\frac{rh}{H}$</td><td>Radially inward (towards nadir)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. On a vertical aerial photograph taken from a flying height of $H = 1200\text{ m}$ above flat ground, the image of a chimney has its base at $r_b = 60\text{ mm}$ and top at $r_t = 65\text{ mm}$ from the principal point. What is the height of the chimney?</div>
        <div class="pq-ans">Answer: Approximately $92.3\text{ meters}$.</div>
        <div class="pq-exp">$$h = \frac{d \cdot H}{r_t} = \frac{(65 - 60)\text{ mm} \cdot 1200\text{ m}}{65\text{ mm}} = \frac{5 \cdot 1200}{65} \approx 92.31\text{ m}$$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. From which photographic point is relief displacement radially directed in a truly vertical aerial photograph?</div>
        <div class="pq-ans">Answer: The Nadir Point (which coincides identically with the Principal Point in a vertical photograph).</div>
        <div class="pq-exp">In tilted aerial photographs, relief displacement radiates from the nadir point, whereas tilt displacement radiates from the isocenter.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Does relief displacement represent an error or an advantage in photogrammetry?</div>
        <div class="pq-ans">Answer: It is a geometric distortion for 2D planimetric mapping, but it is the essential advantage that creates stereoscopic parallax and enables 3D height measurement.</div>
        <div class="pq-exp">Without relief displacement, stereoscopic 3D terrain perception and elevation extraction would be impossible.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What happens to the relief displacement of a hill if the aircraft flying height ($H$) is doubled while maintaining camera focal length?</div>
        <div class="pq-ans">Answer: The relief displacement is halved ($d \propto 1/H$).</div>
        <div class="pq-exp">Flying at higher altitude minimizes perspective distortion across the photographic frame.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. If a geological fault scarp is located directly at the nadir point of a vertical aerial photo, what is its photographic relief displacement?</div>
        <div class="pq-ans">Answer: Exactly zero ($d = 0$).</div>
        <div class="pq-exp">Because radial distance $r = 0$, $d = (0 \cdot h) / H = 0$. The camera looks straight down along the scarp face.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In a tilted photograph with tilt angle $\theta$, how do the Principal Point ($P$), Isocenter ($I$), and Nadir ($N$) align?</div>
        <div class="pq-ans">Answer: They lie along the principal line in the order $P \to I \to N$, separated by distance $f \tan(\theta/2)$ between $P$ and $I$, and $f \tan(\theta/2)$ between $I$ and $N$.</div>
        <div class="pq-exp">The isocenter $I$ is the origin of tilt displacement, while nadir $N$ is the origin of relief displacement.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the fundamental difference between the geometry of an aerial photograph and a topographic map?</div>
        <div class="pq-ans">Answer: An aerial photograph has central perspective projection with scale varying by relief; a map has orthogonal projection with uniform scale.</div>
        <div class="pq-exp">Orthorectification mathematically transforms central perspective aerial photos into map-accurate orthogonal images.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is stereoscopic parallax ($p$) in aerial photography?</div>
        <div class="pq-ans">Answer: The apparent displacement of the position of an object from one photograph to the next in an overlapping flight strip caused by aircraft motion ($p = x - x'$).</div>
        <div class="pq-exp">Differential parallax ($\Delta p$) is directly proportional to terrain elevation differences: $\Delta h = \frac{\Delta p \cdot H'}{B + \Delta p}$.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q128: Microstrip (Patch) Antenna in GPS
# -----------------------------------------------------------------------------
def gen_q128():
    q_num = 128
    filename = "Q128_Most_Widely_Used_Antenna_In_GPS_Microstrip_Antenna_Complete_Guide.html"
    title = "Q128: Satellite Geodesy - GPS Microstrip (Patch) Antennas"
    badge = "OPSC 2019 Geology Paper-II • Question 128 • Satellite Geodesy & GPS"
    h1_title = "Satellite Geodesy: Antenna Architecture and the Universal Use of Microstrip Patch Antennas in GPS"
    meta_text = "<strong>Topic:</strong> GPS Hardware Architecture & Antennas • <strong>Key Concept:</strong> Microstrip Patch Antennas, Right-Hand Circular Polarization (RHCP) & Multipath Rejection • <strong>Textbooks:</strong> B. Hofmann-Wellenhof, H. Lichtenegger, & E. Wasle (<em>GNSS: GPS, GLONASS, Galileo and more</em>); G. Xu (<em>GPS: Theory, Algorithms and Applications</em>); C.A. Balanis (<em>Antenna Theory: Analysis and Design</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: GPS Antenna Requirements and Microstrip Technology</div>
      <p>In satellite-based navigation and geodesy (GPS, GLONASS, Galileo, BeiDou, and NavIC), the user receiver antenna is the critical physical transducer that intercepts spaceborne electromagnetic radio-frequency (RF) signals and converts them into high-frequency alternating electric currents for receiver signal tracking.</p>

      <p>GPS satellites transmit low-power carrier signals in the L-band (e.g., $L_1 = 1575.42\text{ MHz}$, $L_2 = 1227.60\text{ MHz}$, $L_5 = 1176.45\text{ MHz}$). Because satellite signals must traverse the ionosphere, they are transmitted with <strong>Right-Hand Circular Polarization (RHCP)</strong> to prevent signal fade caused by ionospheric Faraday rotation. Consequently, GPS receiver antennas must satisfy demanding technical criteria (Hofmann-Wellenhof et al.; Balanis):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Operational Requirement</th>
              <th>Physical / Engineering Reason</th>
              <th>How Microstrip (Patch) Antenna Satisfies It</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Right-Hand Circular Polarization (RHCP)</strong></td>
              <td>Matches satellite transmission; prevents $3\text{ dB}$ cross-polarization polarization mismatch loss.</td>
              <td>Dual orthogonal feeds or trimmed corner patch geometry excites degenerate orthogonal resonant modes with $90^\circ$ phase shift.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Hemispherical Gain Pattern</strong></td>
              <td>Must track multiple satellites simultaneously from zenith ($90^\circ$) down to low horizons ($5^\circ\text{--}10^\circ$).</td>
              <td>Broad, omnidirectional upper-hemisphere radiation pattern with clean horizon rolloff.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Compact, Rugged & Low Profile</strong></td>
              <td>Must be deployed on airplanes, vehicles, handheld survey devices, smartphones, and missile fuselages.</td>
              <td>Planar, printed-circuit board (PCB) construction; ultra-thin ($<5\text{ mm}$ thick) and lightweight.</td>
            </tr>
            <tr>
              <td>Multipath Rejection</td>
              <td>Signals bouncing off ground/buildings reverse polarization to Left-Hand Circular Polarization (LHCP).</td>
              <td>Microstrip patch rejects LHCP ground bounce reflections by $15\text{--}25\text{ dB}$, especially when fitted with a choke ring or ground plane.</td>
            </tr>
            <tr>
              <td>Dual/Multi-Frequency Tuning</td>
              <td>Geodetic positioning requires simultaneous $L_1, L_2$, and $L_5$ carrier phase tracking to eliminate ionospheric delay.</td>
              <td>Stacked dual-patch or multi-feed resonant microstrip patches easily integrate multiple frequencies.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q128/gps_microstrip_patch_antenna_architecture.png" alt="Microstrip Patch Antenna in GPS" class="figure-img">
        <div class="figure-caption">Figure 128: Mechanical and electrical architecture of a GPS ceramic microstrip (patch) antenna (Option B), highlighting the metallic patch, dielectric substrate, and ground plane.</div>
      </div>

      <p>Because parabolic dishes (Option A) and horn antennas (Option C) are large, heavy, and highly directional (unable to track multiple distributed satellites across the sky simultaneously), and slotted waveguides (Option D) are complex and narrowband, the <strong>Microstrip Antenna</strong> (also called <em>patch antenna</em>, Option B) is universally the <strong>most widely used antenna in GPS</strong> systems worldwide.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 128</div>
        <div class="raw-q-text">The most widely used antenna in GPS is:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Parabolic antenna</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Microstrip antenna</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Horn antenna</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Slotted antenna</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Microstrip antenna)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Microstrip antenna</div>
          <p>Microstrip (patch) antennas consist of a conductive metallic patch printed onto a dielectric substrate backed by a ground plane. They are universally favored in GPS receivers due to their planar low profile, low manufacturing cost, broad hemispherical upper coverage pattern, high reliability, and natural support for Right-Hand Circular Polarization (RHCP).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Parabolic antenna</div>
          <p>Parabolic dish antennas produce extremely narrow, highly directional pencil beams designed for point-to-point satellite communication (e.g. VSAT, TV broadcast). A GPS receiver must track 8 to 12 satellites scattered across the entire sky simultaneously; a directional dish cannot do this.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Horn antenna</div>
          <p>Pyramidal and conical horn antennas are bulky waveguide structures used primarily as calibration standards and feed horns for microwave dishes in laboratory test benches. Their weight, three-dimensional bulk, and directional beam make them entirely unsuitable for field GPS receivers.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Slotted antenna</div>
          <p>Slotted waveguide antennas are used in high-power airborne and marine radar arrays for fan-beam scanning. They lack hemispherical circular polarization and are far too large and expensive for commercial and geodetic GPS applications.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Antenna Design Type</th>
              <th>Beam Directivity</th>
              <th>Polarization</th>
              <th>Size & Form Factor</th>
              <th>Suitability for GNSS / GPS</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Microstrip (Patch) Antenna</strong> (Option B)</td><td>Broad Hemispherical ($>160^\circ$ beamwidth)</td><td>RHCP (Circular)</td><td>Ultra-compact, flat planar disc/square ($<5\text{ cm}$)</td><td><strong>Universally Ideal:</strong> Standard in smartphones, cars, aircraft, and geodetic rovers.</td></tr>
            <tr><td>Choke Ring Antenna</td><td>Hemispherical with steep low-elevation cutoff</td><td>RHCP (Circular)</td><td>Microstrip patch mounted inside concentric metallic rings ($~35\text{ cm}$)</td><td><strong>Geodetic Reference Standard:</strong> Eliminates multipath for permanent IGS base stations.</td></tr>
            <tr><td>Helical (Quadrifilar) Antenna</td><td>Broad cardioid beam</td><td>RHCP (Circular)</td><td>Cylindrical spiral wire ($~10\text{ cm}$ tall)</td><td>Common on handheld Garmin receivers and drones; high horizon gain.</td></tr>
            <tr><td>Parabolic Dish Antenna (Option A)</td><td>Extremely narrow pencil beam ($<2^\circ$)</td><td>Linear or circular</td><td>Bulky concave reflector ($0.5\text{--}30\text{ m}$)</td><td>Unusable for GPS tracking; used for deep-space telemetry.</td></tr>
            <tr><td>Standard Dipole / Monopole</td><td>Toroidal omnidirectional</td><td>Strictly Linear</td><td>Thin wire/rod</td><td>Poor: Suffers $3\text{ dB}$ polarization loss and severe multipath.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is a "Choke Ring" antenna in high-precision geodetic GPS surveying?</div>
        <div class="pq-ans">Answer: A precision microstrip antenna surrounded by a series of concentric conducting metallic troughs spaced at $\lambda/4$ depths to cancel reflected multipath radio waves from the ground.</div>
        <div class="pq-exp">Ground-reflected multipath waves enter the choke ring grooves, creating destructive interference that prevents phase measurement errors.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why are GPS signals circularly polarized rather than linearly polarized?</div>
        <div class="pq-ans">Answer: To prevent signal attenuation and phase distortion caused by Faraday rotation as the electromagnetic wave traverses the Earth's magnetized ionosphere.</div>
        <div class="pq-exp">Linear polarization undergoes unpredictable orientation shifts in the ionosphere, whereas circular polarization maintains constant power transfer.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the "phase center" of a GPS antenna and why is it important in millimeter geodesy?</div>
        <div class="pq-ans">Answer: The theoretical point inside the antenna where the received electromagnetic wave is converted to voltage, which varies slightly with satellite elevation and azimuth (Phase Center Variation, PCV).</div>
        <div class="pq-exp">High-precision geodetic processing requires relative or absolute antenna calibration tables (ANTEX format) to correct for millimeter PCVs.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the dielectric substrate typically used in compact ceramic GPS patch antennas?</div>
        <div class="pq-ans">Answer: High-permittivity ceramics (e.g. titanium dioxide composites with $\epsilon_r \approx 20\text{--}90$).</div>
        <div class="pq-exp">High dielectric constants drastically shrink the physical patch dimensions ($\text{Size} \propto 1/\sqrt{\epsilon_r}$), fitting GPS antennas into smartphones.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What happens to the polarization of a Right-Hand Circularly Polarized (RHCP) GPS signal upon reflecting off a flat surface (e.g., pavement or water)?</div>
        <div class="pq-ans">Answer: It reverses polarization and becomes Left-Hand Circularly Polarized (LHCP).</div>
        <div class="pq-exp">Because microstrip antennas are engineered to reject LHCP radiation, this polarization flip suppresses ground multipath reflections.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is an "Active GPS Antenna"?</div>
        <div class="pq-ans">Answer: A microstrip patch antenna integrated with an internal low-noise amplifier (LNA) powered by DC voltage fed through the coaxial cable.</div>
        <div class="pq-exp">The LNA boosts the faint received GPS signal ($\approx -160\text{ dBW}$) before cable transmission losses degrade the signal-to-noise ratio.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why are quadrifilar helix antennas (QHA) often used on small GPS UAVs and handheld units?</div>
        <div class="pq-ans">Answer: They provide broad RHCP beam coverage that maintains satellite tracking even when the drone or survey pole tilts significantly.</div>
        <div class="pq-exp">Microstrip patches experience gain loss when tilted more than $30^\circ\text{--}40^\circ$ off-zenith.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the fundamental carrier frequency of the primary civilian GPS L1 signal?</div>
        <div class="pq-ans">Answer: $1575.42\text{ MHz}$ (with a wavelength of $\lambda \approx 19.03\text{ cm}$).</div>
        <div class="pq-exp">A ceramic patch antenna for L1 is typically around $25\text{ mm} \times 25\text{ mm}$ square.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Solutions Batch 10 Part A (Q121 - Q128)...")
    gen_q121()
    gen_q122()
    gen_q123()
    gen_q124()
    gen_q125()
    gen_q126()
    gen_q127()
    gen_q128()
    print("Batch 10 Part A successfully generated!")
