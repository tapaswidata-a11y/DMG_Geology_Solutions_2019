# guides_batch2.py - Comprehensive 3-Tier Masterclasses for Q11-Q25

guides_batch2 = {
    11: {
        "title": "Q11: Atmospheric Scattering Mechanisms (Rayleigh, Mie, Non-Selective) & Sky Coloration",
        "part1": """
        <h3>11.1 Physics of Atmospheric Scattering in Remote Sensing</h3>
        <p>In atmospheric physics and remote sensing (Lillesand, Kiefer & Chipman, <i>Remote Sensing and Image Interpretation</i>, 7th Ed., Ch. 1, pp. 9–14; Sabins, Ch. 1), solar radiation interacts with atmospheric particles through three distinct scattering mechanisms, classified by the ratio of particle diameter ($d$) to incident wavelength ($\\lambda$):</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Scattering Type</th>
                <th>Particle Diameter vs. Wavelength</th>
                <th>Primary Atmospheric Agents</th>
                <th>Wavelength Dependence & Spectral Behavior</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Rayleigh Scattering</b></td>
                <td>$d \\ll \\lambda$ (typically $d < 0.1\\lambda$)</td>
                <td>Gas molecules ($N_2, O_2, CO_2$)</td>
                <td><b>Extremely strong inverse 4th power dependence: $I \\propto \\lambda^{-4}$</b>. Scatters blue light $\\sim 9.4$ times more than red light.</td>
              </tr>
              <tr>
                <td><b>Mie Scattering</b></td>
                <td>$d \\approx \\lambda$ ($0.1\\lambda < d < 10\\lambda$)</td>
                <td>Smoke, dust, pollen, fine aerosols</td>
                <td>Weak wavelength dependence ($I \\propto \\lambda^{-\\alpha}$, where $\\alpha \\approx 0.5 - 2$). Creates overcast haze.</td>
              </tr>
              <tr>
                <td><b>Non-Selective Scattering</b></td>
                <td>$d \\gg \\lambda$ ($d > 10\\lambda$)</td>
                <td>Water droplets, ice crystals, cloud particles ($> 5-100\\ \\mu\\text{m}$)</td>
                <td><b>No wavelength dependence</b>; scatters all visible wavelengths equally ($I \\approx \\text{const}$), making clouds and fog appear white.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>11.2 Mathematical Derivation of Sky Coloration</h3>
        <p>According to Lord Rayleigh's scattering formula, the intensity of scattered light ($I_s$) at distance $R$ and scattering angle $\\theta$ is:</p>
        $$I_s = I_0 \\frac{8\\pi^4 \\alpha^2}{\\lambda^4 R^2} (1 + \\cos^2 \\theta)$$
        <p>Comparing blue light ($\\lambda_b = 0.45\\ \\mu\\text{m}$) and red light ($\\lambda_r = 0.70\\ \\mu\\text{m}$):</p>
        $$\\frac{I_{s,\\text{blue}}}{I_{s,\\text{red}}} = \\left(\\frac{\\lambda_r}{\\lambda_b}\\right)^4 = \\left(\\frac{0.70}{0.45}\\right)^4 = (1.555)^4 \\approx 5.86$$
        <p>Because nitrogen and oxygen molecules scatter shorter blue wavelengths almost 6 to 10 times more effectively throughout the daytime sky, the diffuse scattered skylight arriving at the Earth's surface is predominantly blue.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Rayleigh Scattering</b> — Rayleigh scattering by atmospheric gas molecules ($N_2, O_2$) with an intensity proportional to $\\lambda^{-4}$ preferentially scatters short blue wavelengths, causing the blue color of the daytime sky.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Mie Scattering — INCORRECT:</b> Mie scattering is caused by dust, pollen, and aerosols of sizes comparable to wavelength ($d \\approx \\lambda$). It creates whitish-gray atmospheric haze, not the clear blue sky.</li>
          <li><b>(B) Non-Selective Scattering — INCORRECT:</b> Caused by large cloud droplets ($d \\gg \\lambda$) that scatter all visible wavelengths equally, resulting in white clouds and fog.</li>
          <li><b>(C) Rayleigh Scattering — CORRECT:</b> Classical, universal atmospheric mechanism where $d \\ll \\lambda$, generating the $\\lambda^{-4}$ selective scattering of blue light.</li>
          <li><b>(D) Water droplets present in the sky — INCORRECT:</b> Water droplets produce non-selective scattering (white clouds) or rain, not molecular Rayleigh scattering.</li>
        </ul>
        """,
        "part3": """
        <h3>Worked Scattering & Optical Remote Sensing Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 11: Atmospheric Path Radiance & Band Selection</div>
          <p>Why do Landsat and Sentinel-2 optical geological sensors avoid using blue-band data for rock-type classification, preferring SWIR bands?</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>Due to Rayleigh scattering ($I \\propto \\lambda^{-4}$), atmospheric <b>path radiance (haze)</b> is at its maximum in the blue band ($0.45 - 0.52\\ \\mu\\text{m}$), severely degrading surface image contrast. In contrast, SWIR bands ($1.55 - 2.35\\ \\mu\\text{m}$) have $\\lambda$ values $4-5$ times larger, experiencing virtually zero Rayleigh scattering ($(\\frac{0.45}{2.20})^4 \\approx 0.0017$), providing razor-sharp surface diagnostic mineral absorption spectra.</p>
          </div>
        </div>
        """
    },
    12: {
        "title": "Q12: Spectroscopy & Molecular Vibrational Energy in SWIR and TIR Bands",
        "part1": """
        <h3>12.1 Electronic vs. Vibrational Transitions Across the Electromagnetic Spectrum</h3>
        <p>In optical remote sensing and mineral spectroscopy (Clark, 1999, <i>USGS Spectroscopy of Rocks and Minerals</i>; Lillesand, Kiefer & Chipman, Ch. 1 & 8; White, <i>Geochemistry</i>, Ch. 13), electromagnetic radiation interacts with matter via two fundamental physical mechanisms:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Energy Transition Type</th>
                <th>Electromagnetic Spectral Domain</th>
                <th>Physical Mechanism & Diagnostic Geological Absorption</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Electronic Transitions</b></td>
                <td><b>UV, Visible & Near-Infrared (VNIR: $0.2 - 1.0\\ \\mu\\text{m}$)</b></td>
                <td>Valence electrons jump between orbital states. Crystal field effects ($d-d$ transitions in $Fe^{2+}, Fe^{3+}, Cr^{3+}$), charge transfer (iron-oxygen charge transfer in hematite, goethite), and conduction bands.</td>
              </tr>
              <tr>
                <td><b>Molecular Vibrational Energy (Fundamental & Overtones)</b></td>
                <td><b>Short-Wave Infrared (SWIR: $1.4 - 2.5\\ \\mu\\text{m}$) & Thermal Infrared (TIR: $8.0 - 14.0\\ \\mu\\text{m}$)</b></td>
                <td><b>Stretching and bending vibrations of interatomic chemical bonds</b>:
                <br>• SWIR: Overtones and combination vibrational modes of $Al-OH$ ($2.20\\ \\mu\\text{m}$), $Mg-OH$ ($2.31\\ \\mu\\text{m}$), and $CO_3^{2-}$ ($2.35\\ \\mu\\text{m}$).
                <br>• TIR: Fundamental $Si-O-Si$ asymmetric stretching (Reststrahlen bands, $8.5 - 12\\ \\mu\\text{m}$) and kinetic molecular thermal emission.</td>
              </tr>
              <tr>
                <td><b>Rotational Transitions</b></td>
                <td>Microwave & Far-Infrared ($> 100\\ \\mu\\text{m}$)</td>
                <td>Pure rotational energy level transitions in free gas molecules.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>12.2 Quantum Harmonic Oscillator Mechanics</h3>
        <p>The vibrational frequency $(\\nu)$ of a diatomic chemical bond is governed by Hooke's spring law and reduced mass $(\\mu)$:</p>
        $$\\nu = \\frac{1}{2\\pi} \\sqrt{\\frac{k}{\\mu}}, \\quad \\text{where } \\mu = \\frac{m_1 m_2}{m_1 + m_2}$$
        <p>The energy associated with vibrational quantum transitions $(\\Delta E = h\\nu)$ corresponds precisely to photon wavelengths in the <b>SWIR and TIR regions</b> of the spectrum.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) SWIR and TIR region</b> — Molecular vibrational modes (fundamental stretching/bending and combination overtones of $Si-O$, $O-H$, $C-O$ bonds) are uniquely associated with the <b>SWIR and TIR regions</b> of the electromagnetic spectrum.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) UV and Photo UV region — INCORRECT:</b> Governed by high-energy electronic transitions and photo-ionization, not vibrational modes.</li>
          <li><b>(B) SWIR and TIR region — CORRECT:</b> SWIR ($1.4 - 2.5\\ \\mu\\text{m}$) features overtone/combination vibrational bands, and TIR ($8 - 14\\ \\mu\\text{m}$) features fundamental bond-stretching vibrations and thermal emissions.</li>
          <li><b>(C) Visible and NIR region — INCORRECT:</b> Dominated by crystal field electronic transitions ($Fe^{2+}/Fe^{3+}$) and chlorophyll $\\pi$-electron orbital excitation.</li>
          <li><b>(D) Microwave and Radio wave region — INCORRECT:</b> Associated with rotational states and magnetic dipole spin flips (e.g. 21-cm hydrogen line), possessing far too low photon energy for vibrational bond excitations.</li>
        </ul>
        """,
        "part3": """
        <h3>Mineral Spectroscopy Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 12: Hydrothermal Alteration Mapping in SWIR</div>
          <p>Which diagnostic vibrational absorption feature in the SWIR spectrum ($2.20\\ \\mu\\text{m}$) allows exploration geologists to identify clay minerals like kaolinite and alunite in copper-gold porphyry systems?</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>The combination overtone of the <b>$Al-OH$ bond stretching + $Al-OH$ bending vibration</b> occurs at precisely $2.20\\ \\mu\\text{m}$. Kaolinite produces a diagnostic doublet ($2.16\\ \\mu\\text{m}$ and $2.20\\ \\mu\\text{m}$), whereas alunite exhibits absorption at $2.17\\ \\mu\\text{m}$.</p>
          </div>
        </div>
        """
    },
    13: {
        "title": "Q13: Sun-Synchronous Orbital Mechanics & Constant Solar Illumination",
        "part1": """
        <h3>13.1 Orbital Mechanics of Sun-Synchronous Orbits (SSO)</h3>
        <p>In satellite remote sensing (Lillesand, Kiefer & Chipman, <i>Remote Sensing</i>, Ch. 6, pp. 385–388; Sabins, Ch. 3), earth observation satellites (Landsat, IRS, Sentinel-2, SPOT) are placed into <b>Sun-Synchronous Orbits (SSO)</b>.</p>
        <p>An SSO is a near-polar, retrograde orbit whose orbital plane precesses eastward at the exact same angular rate at which the Earth revolves around the Sun:</p>
        $$\\dot{\\Omega} = \\frac{360^\\circ}{365.2422\\text{ days}} \\approx 0.9856^\\circ / \\text{day} = 1.991 \\times 10^{-7}\\text{ rad/s}$$

        <h3>13.2 J2 Earth Oblateness Gravitational Torque</h3>
        <p>This nodal precession is mechanically achieved by harnessing the gravitational torque exerted by the Earth's equatorial bulge (the second zonal harmonic, $J_2 = 1.08263 \\times 10^{-3}$):</p>
        $$\\dot{\\Omega} = -\\frac{3}{2} J_2 \\left(\\frac{R_E}{p}\\right)^2 \\sqrt{\\frac{\\mu}{a^3}} \\cos i$$
        <p>To make $\\dot{\\Omega} > 0$ (positive eastward precession), $\\cos i$ must be negative, requiring an inclination $i > 90^\\circ$ (a retrograde orbit, typically $97^\\circ - 99^\\circ$ for altitudes of $700 - 900\\text{ km}$).</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Orbital Parameter</th>
                <th>Sun-Synchronous Orbit (SSO)</th>
                <th>Geostationary Orbit (GEO)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Altitude</b></td>
                <td>Low Earth Orbit: $600 - 900\\text{ km}$</td>
                <td>High Earth Orbit: $35,786\\text{ km}$</td>
              </tr>
              <tr>
                <td><b>Inclination</b></td>
                <td>Near-polar retrograde: $97^\\circ - 99^\\circ$</td>
                <td>Equatorial: $0^\\circ$</td>
              </tr>
              <tr>
                <td><b>Synchronization Target</b></td>
                <td><b>Local Solar Time (constant sun illumination geometry)</b></td>
                <td>Earth's rotational velocity (stationary over one equatorial point)</td>
              </tr>
              <tr>
                <td><b>Primary Utility</b></td>
                <td>Global high-resolution land imaging & geology</td>
                <td>Real-time weather monitoring & telecommunications</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) Local Solar time</b> — In a Sun-Synchronous orbit, the orbital plane precesses so that the satellite passes over any given geographic point at the exact same <b>Local Solar Time</b> on every pass.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Particular area of the Earth — INCORRECT:</b> Satellites that remain over a particular area are Geostationary satellites, not Sun-synchronous satellites.</li>
          <li><b>(B) Local Solar time — CORRECT:</b> Sun-synchronous satellites cross the equator at a fixed local solar time (e.g. 10:30 AM descending node for IRS and Landsat), maintaining uniform shadow lengths and sun angles.</li>
          <li><b>(C) Stationary on the Equator — INCORRECT:</b> Describes Geostationary orbits ($i = 0^\\circ, h = 35,786\\text{ km}$).</li>
          <li><b>(D) Stationary on the Pole — INCORRECT:</b> Physically impossible orbital state; polar orbits continuously circle over both poles.</li>
        </ul>
        """,
        "part3": """
        <h3>Remote Sensing Concept Application</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 13: Importance of Fixed Local Solar Time for Geological Mapping</div>
          <p>Why do optical geological satellites choose a mid-morning overpass time (e.g. 10:00 to 10:30 AM local solar time) rather than local noon (12:00 PM)?</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>A mid-morning overpass (10:00–10:30 AM) provides a balanced <b>solar elevation angle ($45^\circ - 55^\circ$)</b>, producing moderate topographic shadowing that highlights structural ridges, fault scarps, and fold trends, while avoiding convective afternoon cumulus cloud cover that typically forms around solar noon.</p>
          </div>
        </div>
        """
    },
    14: {
        "title": "Q14: Spatial Resolution & Geometric Ground Clarity in Remote Sensing",
        "part1": """
        <h3>14.1 The Four Fundamental Resolutions in Remote Sensing</h3>
        <p>In digital image processing (Lillesand, Kiefer & Chipman, <i>Remote Sensing</i>, Ch. 1, pp. 30–35), sensor performance is defined by four orthogonal resolutions:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Resolution Dimension</th>
                <th>Physical Definition & Governing Metric</th>
                <th>Primary Impact on Image Utility</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Spatial Resolution</b></td>
                <td><b>Size of the smallest ground area recorded by a detector (Instantaneous Field of View, IFOV; Ground Sampling Distance, GSD)</b></td>
                <td><b>Clarity, geometric discernibility, and edge sharpness of ground objects</b></td>
              </tr>
              <tr>
                <td><b>Spectral Resolution</b></td>
                <td>Width and number of discrete wavelength bands recorded across the electromagnetic spectrum ($\\Delta \\lambda$)</td>
                <td>Ability to discriminate distinct rock types, minerals, and chemical compositions</td>
              </tr>
              <tr>
                <td><b>Radiometric Resolution</b></td>
                <td>Bit-depth sensitivity to subtle differences in radiance intensity ($8\\text{-bit} = 256$, $12\\text{-bit} = 4096$)</td>
                <td>Contrast sensitivity in deep shadow and bright snow/salt domains</td>
              </tr>
              <tr>
                <td><b>Temporal Resolution</b></td>
                <td>Revisit period between consecutive image acquisitions over the same geographic location</td>
                <td>Monitoring dynamic seasonal changes, floods, landslides, and volcanic eruptions</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>14.2 Ground Sampling Distance (GSD) & Nyquist Criterion</h3>
        <p>The ground clarity of an object requires that its dimension exceeds approximately <b>$2.0 \\times \\text{GSD}$</b> (the two-dimensional Nyquist sampling limit) to be reliably resolved and identified without spatial aliasing.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) Spatial Resolution</b> — The clarity, sharpness, and geometric recognizability of individual ground objects on an image depends directly upon its <b>Spatial Resolution</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Spatial Resolution — CORRECT:</b> Directly dictates the minimum ground sampling distance and resolving power of individual spatial objects.</li>
          <li><b>(B) Spectral Resolution — INCORRECT:</b> Governs the ability to identify chemical composition and absorption bands, not geometric sharpness.</li>
          <li><b>(C) Temporal Resolution — INCORRECT:</b> Governs the frequency of overpasses (revisit interval), not image clarity.</li>
          <li><b>(D) Radiometric Resolution — INCORRECT:</b> Governs brightness quantization and bit depth, not ground detail size.</li>
        </ul>
        """,
        "part3": """
        <h3>Photogrammetric Resolution Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 14: Ground Sampling Distance (GSD) Calculation</div>
          <p>An airborne aerial camera with focal length $f = 150\\text{ mm}$ flies at an altitude of $H = 3,000\\text{ m}$ above mean terrain. If the physical detector pixel pitch is $p = 6.0\\ \\mu\\text{m}$, calculate the Ground Sampling Distance (GSD).</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            $$\\text{GSD} = p \\cdot \\frac{H}{f} = (6.0 \\times 10^{-6}\\text{ m}) \\cdot \\frac{3000\\text{ m}}{0.150\\text{ m}} = 6.0 \\times 10^{-6} \\times 20,000 = 0.12\\text{ m} = 12\\text{ cm}$$
            <p>The spatial resolution of the camera at this flying height is <b>$12\\text{ cm}$</b> per pixel.</p>
          </div>
        </div>
        """
    },
    15: {
        "title": "Q15: Photogrammetry: Fiducial Marks & Principal Point Determination",
        "part1": """
        <h3>15.1 Anatomy of a Metric Aerial Photograph</h3>
        <p>In aerial photogrammetry (Paul R. Wolf, Bon A. Dewitt, & Benjamin E. Wilkinson, <i>Elements of Photogrammetry with Applications in GIS</i>, 4th Ed., Ch. 4; Lillesand et al., Ch. 3), metric aerial cameras are equipped with precisely calibrated index markers rigidly affixed to the focal plane frame, known as <b>fiducial marks</b>.</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Photogrammetric Point</th>
                <th>Geometric Definition</th>
                <th>Diagnostic Property & Significance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Principal Point ($PP$ or $o$)</b></td>
                <td><b>The intersection point of straight lines connecting opposite fiducial marks on an aerial photograph</b></td>
                <td>Origin of the photographic coordinate system $(x, y)$; point where optical axis intersects focal plane at $90^\\circ$.</td>
              </tr>
              <tr>
                <td><b>Nadir Point ($n$)</b></td>
                <td>The point where the true plumb line (vertical) through the camera exposure station intersects the photograph</td>
                <td>Origin of relief displacement ($d = \\frac{r \\cdot h}{H}$). On a truly vertical photo, $n = PP$.</td>
              </tr>
              <tr>
                <td><b>Isocenter ($i$)</b></td>
                <td>The point on the photograph halfway between the principal point and nadir on the principal line</td>
                <td>Origin of tilt displacement ($d_t$). Scale is exactly true along the isometric parallel passing through $i$.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>15.2 Photographic Coordinate System Calibration</h3>
        <p>The calibration certificate of a metric aerial camera specifies the exact $(x, y)$ coordinates of each fiducial mark relative to the calibrated principal point to within $\\pm 1 - 2\\ \\mu\\text{m}$, eliminating film shrinkage and scanner distortion.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Principal points</b> — Fiducial marks imaged on the edges or corners of an aerial photograph are used to locate the geometric center or <b>Principal Point</b> of the photograph.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Flight path — INCORRECT:</b> The flight path is determined by connecting conjugate principal points (flight strip track), not by fiducial marks alone.</li>
          <li><b>(B) Scale of Aerial photographs — INCORRECT:</b> Photo scale is determined by the ratio of focal length to flying height ($S = f/H$) or ground control distance.</li>
          <li><b>(C) Principal points — CORRECT:</b> The defining function of fiducial marks is to define the photo coordinate axes and locate the principal point ($PP$).</li>
          <li><b>(D) Flight height — INCORRECT:</b> Flight height is measured by altimeters or stereoscopic parallax equations ($H = B \\cdot f / p$).</li>
        </ul>
        """,
        "part3": """
        <h3>Photogrammetric Relief Displacement Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 15: Relief Displacement from the Principal Point</div>
          <p>On a vertical aerial photograph taken with focal length $f = 152.4\\text{ mm}$ from flying height $H = 2,500\\text{ m}$ above terrain, the top of a communication tower has radial distance $r = 82.5\\text{ mm}$ from the principal point, and relief displacement $d = 3.3\\text{ mm}$. Calculate the height of the tower.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>The relief displacement formula on a vertical photograph is:</p>
            $$d = \\frac{r \\cdot h}{H} \\implies h = \\frac{d \\cdot H}{r}$$
            $$h = \\frac{3.3\\text{ mm} \\times 2500\\text{ m}}{82.5\\text{ mm}} = \\frac{8250}{82.5} = 100\\text{ meters}$$
            <p>The height of the tower is exactly <b>$100\\text{ meters}$</b>.</p>
          </div>
        </div>
        """
    },
    16: {
        "title": "Q16: Radar Systems: Real Aperture Radar (RAR) vs. Synthetic Aperture Radar (SAR)",
        "part1": """
        <h3>16.1 The Azimuth Resolution Paradox in Spaceborne Radar</h3>
        <p>In radar remote sensing (Lillesand, Kiefer & Chipman, <i>Remote Sensing</i>, Ch. 7, pp. 488–496; Curlander & McDonough, <i>Synthetic Aperture Radar</i>), radar pulses achieve range (cross-track) resolution via pulse duration ($\\tau$): $R_r = \\frac{c \\tau}{2 \\sin \\theta}$.</p>
        <p>However, along-track (azimuth) resolution ($R_a$) for a <b>Real Aperture Radar (RAR)</b> depends directly on the beamwidth ($\\beta$) and physical antenna length ($L$):</p>
        $$R_{a,\\text{RAR}} = R \\cdot \\beta = \\frac{\\lambda \\cdot R}{L}$$
        <p>Where $R$ is slant range, $\\lambda$ is radar wavelength, and $L$ is the physical length of the antenna.</p>

        <h3>16.2 Why RAR Fails from Space and How SAR Solves It</h3>
        <p>For a spaceborne satellite at slant range $R = 800\\text{ km}$ operating at C-band ($\\lambda = 0.056\\text{ m}$), achieving a modest ground azimuth resolution of $R_a = 10\\text{ m}$ with RAR would require a physical antenna length of:</p>
        $$L = \\frac{\\lambda \\cdot R}{R_a} = \\frac{0.056\\text{ m} \\times 800,000\\text{ m}}{10\\text{ m}} = 4,480\\text{ meters} = 4.48\\text{ km!}$$
        <p>Launching a 4.5-kilometer rigid antenna into orbit is physically impossible.</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Parameter</th>
                <th>Real Aperture Radar (RAR)</th>
                <th>Synthetic Aperture Radar (SAR)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Antenna Configuration</b></td>
                <td><b>Physical antenna only</b>; beam determined by real aperture length $L$</td>
                <td><b>Synthesizes a virtual antenna kilometers long</b> using spacecraft forward motion and Doppler phase histories</td>
              </tr>
              <tr>
                <td><b>Azimuth Resolution</b></td>
                <td>$R_a = \\frac{\\lambda R}{L}$ (degrades with distance)</td>
                <td><b>$R_a = \\frac{L}{2}$ (completely independent of distance and wavelength!)</b></td>
              </tr>
              <tr>
                <td><b>Spaceborne Feasibility</b></td>
                <td>Impractical from orbit (requires km-sized antenna)</td>
                <td>Universal orbital standard (Sentinel-1, NISAR, ALOS)</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) Size of the Antenna</b> — The major fundamental difference between Real Aperture Radar (RAR) and Synthetic Aperture Radar (SAR) lies in the <b>size of the antenna</b> (physical real antenna vs. motion-synthesized long virtual aperture).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Size of the Antenna — CORRECT:</b> In RAR, resolution is constrained by physical antenna dimensions ($R_a \\propto 1/L$), whereas SAR electronically synthesizes an antenna hundreds of times longer than its physical size.</li>
          <li><b>(B) Source of energy — INCORRECT:</b> Both RAR and SAR are active sensors that supply their own microwave energy transmitters (magnetrons / TWT / solid-state amplifiers).</li>
          <li><b>(C) Recording of data — INCORRECT:</b> Both record returning electromagnetic echoes, though SAR records coherent Doppler phase.</li>
          <li><b>(D) None of these — INCORRECT.</b></li>
        </ul>
        """,
        "part3": """
        <h3>SAR Azimuth Resolution Proof</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 16: Theoretical Azimuth Resolution of SAR</div>
          <p>A satellite carries a Synthetic Aperture Radar (SAR) with a physical antenna length of $L = 10.0\\text{ meters}$. What is the theoretical maximum azimuth resolution achievable by this SAR system?</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>For a fully focused synthetic aperture radar, the azimuth resolution is simply half the physical antenna length:</p>
            $$R_a = \\frac{L}{2} = \\frac{10.0\\text{ m}}{2} = 5.0\\text{ meters}$$
            <p>Remarkably, this $5\\text{ m}$ resolution is independent of orbital altitude ($H$) and radar wavelength ($\\lambda$).</p>
          </div>
        </div>
        """
    },
    17: {
        "title": "Q17: Optical Remote Sensing: Soil Moisture Absorption & NIR Image Tonal Response",
        "part1": """
        <h3>17.1 Spectral Reflectance Behavior of Water & Soil Moisture</h3>
        <p>In optical remote sensing and soil physics (Lillesand, Kiefer & Chipman, <i>Remote Sensing</i>, Ch. 1, pp. 16–20; Sabins, Ch. 2), the spectral reflectance curve of bare soil is dramatically altered by the introduction of moisture:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Soil Moisture State</th>
                <th>Optical Mechanism & Water Absorption</th>
                <th>Tonal Appearance on NIR Imagery</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Dry Bare Soil</b></td>
                <td>High surface scattering, minimal absorption; reflectance steadily increases from visible into NIR ($30 - 45\\%$)</td>
                <td><b>Light / Bright / White tone</b></td>
              </tr>
              <tr>
                <td><b>Moist / Wet Soil</b></td>
                <td>Water films coat soil particles, lowering refractive index contrast and causing multiple internal refractions; <b>water strongly absorbs NIR radiation</b></td>
                <td><b>Dark / Grey to Black tone</b></td>
              </tr>
              <tr>
                <td><b>Standing Open Water</b></td>
                <td>Near-total absorption of NIR wavelengths ($> 0.8\\ \\mu\\text{m}$, reflectance $< 2-3\\%$)</td>
                <td><b>Jet Black tone</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>17.2 The Physics of Water Film Refraction</h3>
        <p>When soil pores fill with water, the relative refractive index between mineral grains ($n_{\\text{quartz}} \\approx 1.54$) and the surrounding medium ($n_{\\text{water}} \\approx 1.33$) is much lower than grain-to-air ($n_{\\text{air}} = 1.00$):</p>
        $$\\frac{n_{\\text{quartz}}}{n_{\\text{water}}} = 1.16 \\quad \\text{vs.} \\quad \\frac{n_{\\text{quartz}}}{n_{\\text{air}}} = 1.54$$
        <p>This index matching increases the path length of light within the absorbing liquid, drastically reducing reflectance and darkening the image tone to <b>grey</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) grey</b> — Ground moisture strongly absorbs near-infrared (NIR) radiation, causing moist surfaces to appear in a dark <b>grey</b> tone on black-and-white NIR imagery (as opposed to the bright white tone of dry soil).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) white — INCORRECT:</b> White tone represents dry bare soil, salt flats, or snow with high NIR reflectance.</li>
          <li><b>(B) grey — CORRECT:</b> Water absorption lowers reflectance, producing medium-to-dark grey tones on NIR imagery.</li>
          <li><b>(C) red — INCORRECT:</b> On a standard False Color Composite (FCC), healthy vigorous vegetation appears red, not ground moisture.</li>
          <li><b>(D) blue — INCORRECT:</b> "Tone" in photographic interpretation strictly refers to the relative brightness or colour on a black-and-white photographic gray scale (white, light grey, grey, dark grey, black).</li>
        </ul>
        """,
        "part3": """
        <h3>Remote Sensing Image Interpretation Practice</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 17: Normalized Difference Water Index (NDWI)</div>
          <p>Write the mathematical formula for McFeeters' (1996) Normalized Difference Water Index (NDWI) and explain how it delineates water-saturated zones from surrounding dry land.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            $$\\text{NDWI} = \\frac{\\text{Green} - \\text{NIR}}{\\text{Green} + \\text{NIR}}$$
            <p>Because water features have high green reflectance and near-zero NIR reflectance, water bodies and saturated soils yield positive NDWI values ($> 0$), while terrestrial dry soil and vegetation (with high NIR reflectance) yield negative values, creating sharp binary contrast.</p>
          </div>
        </div>
        """
    },
    18: {
        "title": "Q18: Vegetation Spectral Signature & Chlorophyll Pigment Control",
        "part1": """
        <h3>18.1 The Spectral Reflectance Curve of Healthy Green Vegetation</h3>
        <p>In bio-optical remote sensing (Gates et al., 1965; Knipling, 1970; Lillesand, Kiefer & Chipman, <i>Remote Sensing</i>, Ch. 1, pp. 17–19), the spectral reflectance of a healthy plant leaf is divided into three distinct optical domains:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Spectral Domain</th>
                <th>Wavelength Band</th>
                <th>Primary Governing Biological Factor</th>
                <th>Optical Phenomenon</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Visible Domain</b></td>
                <td><b>$0.40 - 0.70\\ \\mu\\text{m}$</b></td>
                <td><b>Leaf Pigments (Chlorophyll a & b, Carotenoids)</b></td>
                <td>Intense absorption bands at $0.45\\ \\mu\\text{m}$ (blue) and $0.65\\ \\mu\\text{m}$ (red); intermediate <b>green reflection peak at $0.55\\ \\mu\\text{m}$ ($10 - 20\\%$)</b> gives foliage its green appearance.</td>
              </tr>
              <tr>
                <td><b>Near-Infrared (NIR)</b></td>
                <td>$0.70 - 1.30\\ \\mu\\text{m}$</td>
                <td><b>Internal Spongy Mesophyll Cell Structure</b></td>
                <td>Refractive index mismatches between hydrated cell walls and air cavities cause multiple internal scattering ($40 - 60\\%$ reflectance).</td>
              </tr>
              <tr>
                <td><b>Shortwave-Infrared (SWIR)</b></td>
                <td>$1.30 - 2.50\\ \\mu\\text{m}$</td>
                <td><b>Leaf Moisture & Water Content</b></td>
                <td>Strong liquid water absorption valleys at $1.45\\ \\mu\\text{m}$ and $1.94\\ \\mu\\text{m}$.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>18.2 Chlorophyll Pigment Absorption Peaks</h3>
        <p>Chlorophyll 'a' exhibits peak absorption at $0.43\\ \\mu\\text{m}$ and $0.66\\ \\mu\\text{m}$; chlorophyll 'b' absorbs at $0.45\\ \\mu\\text{m}$ and $0.65\\ \\mu\\text{m}$. The unabsorbed green photons between $0.50$ and $0.58\\ \\mu\\text{m}$ are reflected, directly creating the <b>green peak</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) Leaf pigment</b> — In the visible region of the spectrum (including the green band), leaf reflectance is governed almost exclusively by <b>leaf pigments (primarily chlorophyll)</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Leaf moisture — INCORRECT:</b> Leaf moisture governs reflectance in the Short-Wave Infrared (SWIR: $1.4 - 2.5\\ \\mu\\text{m}$), not the visible green band.</li>
          <li><b>(B) Leaf pigment — CORRECT:</b> Chlorophyll and accessory carotenoid pigments completely dominate optical absorption and reflection throughout the $0.4 - 0.7\\ \\mu\\text{m}$ visible spectrum.</li>
          <li><b>(C) Leaf cell structure — INCORRECT:</b> Spongy mesophyll cell structure controls the high reflectance plateau in the Near-Infrared (NIR: $0.7 - 1.3\\ \\mu\\text{m}$).</li>
          <li><b>(D) None of these — INCORRECT.</b></li>
        </ul>
        """,
        "part3": """
        <h3>Vegetation Remote Sensing Application</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 18: The \"Red Edge\" Phenomenon</div>
          <p>What is the \"Red Edge\" in vegetative remote sensing, and what biological transition causes it?</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>The <b>Red Edge</b> is the extremely steep rise in reflectance between $0.68\\ \\mu\\text{m}$ and $0.75\\ \\mu\\text{m}$. It marks the abrupt physical transition from <b>intense chlorophyll pigment absorption</b> in the visible red band to <b>massive internal mesophyll cellular scattering</b> in the near-infrared band.</p>
          </div>
        </div>
        """
    },
    19: {
        "title": "Q19: Indian Remote Sensing (IRS-1D) Satellite Sensor Specifications",
        "part1": """
        <h3>19.1 Payloads and Sensors of the IRS-1C / IRS-1D Satellite</h3>
        <p>In Indian space program history and sensor technology (ISRO NRSC Handbook; George Joseph, <i>Fundamentals of Remote Sensing</i>; Lillesand et al., Ch. 6), the <b>IRS-1D</b> (launched 29 September 1997 into an 821 km polar sun-synchronous orbit) carried three state-of-the-art optical payloads:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Sensor Name</th>
                <th>Sensor Type & Spectral Bands</th>
                <th>Spatial Resolution</th>
                <th>Swath Width & Revisit</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>PAN (Panchromatic Camera)</b></td>
                <td>Single visible band ($0.50 - 0.75\\ \\mu\\text{m}$)</td>
                <td><b>$5.8\\text{ meters}$</b> (steerable off-nadir up to $\\pm 26^\\circ$)</td>
                <td>$70\\text{ km}$ ($24\\text{ days}$)</td>
              </tr>
              <tr>
                <td><b>LISS-III (Linear Imaging Self-Scanning Sensor III)</b></td>
                <td><b>Multispectral: 4 bands</b>
                <br>• B2 (Green: $0.52 - 0.59\\ \\mu\\text{m}$)
                <br>• B3 (Red: $0.62 - 0.68\\ \\mu\\text{m}$)
                <br>• B4 (NIR: $0.77 - 0.86\\ \\mu\\text{m}$)
                <br>• B5 (SWIR: $1.55 - 1.70\\ \\mu\\text{m}$)</td>
                <td><b>$23.5\\text{ meters}$</b> (VNIR Bands 2, 3, 4)
                <br><i>($70.5\\text{ meters}$ for SWIR Band 5)</i></td>
                <td>$141\\text{ km}$ ($24\\text{ days}$)</td>
              </tr>
              <tr>
                <td><b>WiFS (Wide Field Sensor)</b></td>
                <td>2 bands (Red: $0.62-0.68\\ \\mu\\text{m}$, NIR: $0.77-0.86\\ \\mu\\text{m}$)</td>
                <td><b>$188\\text{ meters}$</b></td>
                <td>$810\\text{ km}$ ($5\\text{ days}$)</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) 23.5m</b> — The primary multispectral scanner (LISS-III) onboard the IRS-1D satellite has a spatial resolution of <b>23.5 meters</b> across its VNIR bands.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) 1m — INCORRECT:</b> 1-meter resolution belongs to modern high-resolution commercial satellites like IKONOS / Cartosat-2.</li>
          <li><b>(B) 30m — INCORRECT:</b> 30 meters is the canonical spatial resolution of the NASA Landsat Thematic Mapper (TM/ETM+/OLI).</li>
          <li><b>(C) 79m — INCORRECT:</b> 79 meters (nominal 80m) is the spatial resolution of the legacy Landsat Multispectral Scanner (MSS).</li>
          <li><b>(D) 23.5m — CORRECT:</b> The hallmark spatial resolution of ISRO's IRS-1C and IRS-1D LISS-III multispectral sensor.</li>
        </ul>
        """,
        "part3": """
        <h3>Satellite Specification Comparative Card</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 19: Sensor Comparison Matrix</div>
          <p>Match the satellite sensor to its exact spatial resolution: (1) Landsat-8 OLI Multispectral, (2) Sentinel-2 MSI VNIR, (3) IRS-1D LISS-III VNIR, (4) Cartosat-1 PAN.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <ul>
              <li>(1) Landsat-8 OLI Multispectral = <b>$30\\text{ meters}$</b></li>
              <li>(2) Sentinel-2 MSI VNIR = <b>$10\\text{ meters}$</b></li>
              <li>(3) IRS-1D LISS-III VNIR = <b>$23.5\\text{ meters}$</b></li>
              <li>(4) Cartosat-1 PAN = <b>$2.5\\text{ meters}$</b></li>
            </ul>
          </div>
        </div>
        """
    },
    20: {
        "title": "Q20: Topographic Remote Sensing: The Shuttle Radar Topography Mission (SRTM)",
        "part1": """
        <h3>20.1 Principle of Single-Pass InSAR on SRTM</h3>
        <p>In radar remote sensing and geomorphometry (Farr et al., 2007, <i>The Shuttle Radar Topography Mission</i>, Reviews of Geophysics; Lillesand, Kiefer & Chipman, Ch. 7, pp. 520–525), the <b>Shuttle Radar Topography Mission (SRTM)</b> was flown in February 2000 aboard Space Shuttle *Endeavour* (STS-99).</p>
        <p>SRTM revolutionized Earth observation by acquiring the first near-global high-precision <b>three-dimensional Digital Elevation Model (DEM)</b> using single-pass <b>Interferometric Synthetic Aperture Radar (InSAR)</b>:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Mission Characteristic</th>
                <th>SRTM Operational Configuration</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Interferometric Baseline ($B$)</b></td>
                <td>$60\\text{-meter}$ deployable carbon-fiber truss mast extending from shuttle cargo bay</td>
              </tr>
              <tr>
                <td><b>Antenna Configuration</b></td>
                <td>Dual-antenna single-pass InSAR (Main antenna in payload bay; Outboard antenna at mast tip)</td>
              </tr>
              <tr>
                <td><b>Radar Frequencies</b></td>
                <td>C-band ($\\lambda = 5.6\\text{ cm}$, NASA/JPL) and X-band ($\\lambda = 3.1\\text{ cm}$, DLR/ASI)</td>
              </tr>
              <tr>
                <td><b>Global Coverage & Resolution</b></td>
                <td>$80\\%$ of Earth's landmass ($60^\\circ\\text{N}$ to $56^\\circ\\text{S}$); 1-arc-second ($\approx 30\\text{ m}$) resolution</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>20.2 InSAR Height Derivation Formula</h3>
        <p>Interferometric phase difference ($\\Delta \\phi$) between the two antennas directly determines topographic surface height ($z$):</p>
        $$z = H - R \\cos \\theta, \\quad \\text{where } \\Delta \\phi = \\frac{2\\pi}{\\lambda} B \\sin(\\theta - \\alpha)$$
        <p>Eliminating temporal decorrelation via simultaneous single-pass acquisition enabled unprecedented 3D elevation accuracy.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) SRTM</b> — The <b>Shuttle Radar Topography Mission (SRTM)</b> is the dedicated space radar mission engineered specifically to provide high-resolution <b>three-dimensional topographic elevation data (DEMs)</b> globally.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) LANDSAT — INCORRECT:</b> Landsat is a 2D optical multispectral imaging satellite providing surface reflectance, not direct 3D elevation data.</li>
          <li><b>(B) SRTM — CORRECT:</b> The benchmark space mission for global 3D topographic models.</li>
          <li><b>(C) IKONOS — INCORRECT:</b> A high-resolution 2D commercial optical imaging satellite ($0.82\\text{ m}$ panchromatic).</li>
          <li><b>(D) ERS — INCORRECT:</b> European Remote Sensing satellite; while capable of repeat-pass InSAR, it is not a dedicated single-pass global 3D topographic mission like SRTM.</li>
        </ul>
        """,
        "part3": """
        <h3>Digital Elevation Model (DEM) Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 20: Digital Elevation Data Comparison</div>
          <p>Compare SRTM DEM with ASTER GDEM and Cartosat-1 DEM in terms of remote sensing technology.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <ul>
              <li><b>SRTM:</b> Generated via <b>Active Radar Interferometry (InSAR)</b> at C-band wavelengths, penetrating clouds and haze.</li>
              <li><b>ASTER GDEM:</b> Generated via <b>Passive Optical Stereoscopy</b> from nadir and backward-looking telescopes ($3N$ and $3B$ bands).</li>
              <li><b>Cartosat-1 (ISRO):</b> Generated via <b>High-resolution along-track Optical Stereoscopy</b> using Fore ($+26^\circ$) and Aft ($-5^\circ$) cameras.</li>
            </ul>
          </div>
        </div>
        """
    },
    21: {
        "title": "Q21: Structural Geology: Thrust Fault vs. High-Angle Reverse Fault Dip Angle (< 45°)",
        "part1": """
        <h3>21.1 Geometric & Kinematic Definitions of Compressional Faults</h3>
        <p>In structural geology and fault mechanics (Haakon Fossen, <i>Structural Geology</i>, 2010, Ch. 14, pp. 296–302; Van der Pluijm & Marshak, <i>Earth Structure</i>, Ch. 9; Bangar, Ch. 9), compressional dip-slip faults where the hanging wall moves upward relative to the footwall are subdivided by fault dip angle ($\\theta$):</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Fault Classification</th>
                <th>Fault Dip Angle ($\\theta$)</th>
                <th>Tectonic Context & Typical Kinematics</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Reverse Fault (Sensu Stricto)</b></td>
                <td><b>$\\theta > 45^\\circ$</b> (typically $60^\\circ$)</td>
                <td>High-angle crustal shortening, basement-involved block uplifts</td>
              </tr>
              <tr>
                <td><b>Thrust Fault</b></td>
                <td><b>$\\theta < 45^\\circ$</b> (typically $15^\\circ - 30^\\circ$)</td>
                <td>Low-angle regional contractional orogenic belts (fold-and-thrust belts, subduction accretionary prisms)</td>
              </tr>
              <tr>
                <td><b>Overthrust / Nappe</b></td>
                <td>$\\theta < 10^\\circ - 15^\\circ$ (often near-horizontal)</td>
                <td>Large-scale regional displacement exceeding tens to hundreds of kilometers</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>21.2 Anderson's Mechanical Model of Faulting</h3>
        <p>According to E.M. Anderson (1905, 1951), thrust faulting occurs when the maximum principal stress is horizontal ($\\sigma_1 = \\sigma_{xx}$) and the minimum principal stress is vertical ($\\sigma_3 = \\sigma_{zz} = \\rho g z$).</p>
        <p>The theoretical Coulomb fracture angle ($\\theta_c$) with the horizontal plane (direction of $\\sigma_1$) is:</p>
        $$\\theta_c = 45^\\circ - \\frac{\\phi}{2}$$
        <p>For typical crustal rocks with internal friction angle $\\phi \\approx 30^\\circ$, the predicted thrust fault dip angle is:</p>
        $$\\theta_c = 45^\\circ - 15^\\circ = 30^\\circ < 45^\\circ$$
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) < 45°</b> — In standard structural geology (Fossen; Billings; Bangar), a reverse fault dipping at an angle <b>less than 45° (< 45°)</b> is specifically designated as a <b>Thrust fault</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) 45° — INCORRECT:</b> 45° is the geometric boundary dividing high-angle and low-angle dip-slip faults.</li>
          <li><b>(B) < 45° — CORRECT:</b> The universal structural definition of a thrust fault is a reverse fault dipping at $< 45^\circ$.</li>
          <li><b>(C) > 30° — INCORRECT:</b> Most active thrust faults dip at $< 30^\circ$, making this option factually incorrect.</li>
          <li><b>(D) Both (A) and (B) are correct — INCORRECT:</b> 45° is not included in the standard definition.</li>
        </ul>
        """,
        "part3": """
        <h3>Structural Geometry Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 21: Fault Shortening & Heave Calculation</div>
          <p>A planar thrust fault dipping at $\\theta = 30^\\circ$ exhibits a dip-slip net slip of $S = 200\\text{ meters}$. Calculate the vertical throw and horizontal heave (crustal shortening) produced by the fault.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            $$\\text{Vertical Throw} = S \\cdot \\sin \\theta = 200 \\cdot \\sin(30^\\circ) = 200 \\times 0.5 = 100\\text{ meters}$$
            $$\\text{Horizontal Heave (Shortening)} = S \\cdot \\cos \\theta = 200 \\cdot \\cos(30^\\circ) = 200 \\times 0.866 = 173.2\\text{ meters}$$
            <p>Because $\\theta < 45^\circ$, the horizontal shortening ($173.2\\text{ m}$) significantly exceeds the vertical displacement ($100\\text{ m}$).</p>
          </div>
        </div>
        """
    },
    22: {
        "title": "Q22: Structural Geology: Attitude of Linear Features & Plunge Mechanics",
        "part1": """
        <h3>22.1 Geometric Description of Linear vs. Planar Geological Features</h3>
        <p>In structural geology (Haakon Fossen, <i>Structural Geology</i>, Ch. 2, pp. 24–28; Davis & Reynolds, <i>Structural Geology of Rocks and Regions</i>, Ch. 1), the spatial orientation (attitude) of linear and planar elements is strictly distinguished:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Attitude Parameter</th>
                <th>Geometric Definition</th>
                <th>Applies To</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Plunge</b></td>
                <td><b>The vertical angle between the horizontal plane and a line (or line of maximum elongation), measured downward in a vertical plane</b></td>
                <td><b>Linear features</b> (fold hinge lines, slickenside lineations, mineral stretching lineations)</td>
              </tr>
              <tr>
                <td><b>Trend</b></td>
                <td>The compass direction / azimuth of the vertical plane containing a plunging line</td>
                <td>Linear features</td>
              </tr>
              <tr>
                <td><b>Dip Angle</b></td>
                <td>The acute vertical angle between the horizontal plane and an inclined planar surface</td>
                <td><b>Planar features</b> (bedding, joints, faults, foliation)</td>
              </tr>
              <tr>
                <td><b>Strike</b></td>
                <td>The compass bearing of a horizontal line contained within an inclined geological plane</td>
                <td>Planar features</td>
              </tr>
              <tr>
                <td><b>Rake (Pitch)</b></td>
                <td>The angle between a line and the strike of the plane containing it, measured within the plane</td>
                <td>Linear features lying on a plane</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) plunge</b> — The vertical angle between the horizontal plane and a linear feature or axis of maximum elongation is formally defined as the <b>plunge</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) dip angle — INCORRECT:</b> Dip is the vertical angle of inclination of a <i>planar</i> surface (bedding or fault plane), not a linear feature.</li>
          <li><b>(B) strike — INCORRECT:</b> Strike is a horizontal compass direction on an inclined plane.</li>
          <li><b>(C) right-lateral strike slip — INCORRECT:</b> A kinematic fault displacement sense (dextral strike-slip), not an orientation angle.</li>
          <li><b>(D) plunge — CORRECT:</b> The precise structural definition for the vertical inclination of any linear geological element.</li>
        </ul>
        """,
        "part3": """
        <h3>Structural Geometry Notation Practice</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 22: Plunge / Trend Notation</div>
          <p>A fold hinge line is recorded as $35^\\circ \\to 140^\\circ$. Decode this structural measurement into its constituent plunge and trend components.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <ul>
              <li><b>Plunge:</b> $35^\circ$ (inclined $35^\circ$ downwards from the horizontal plane).</li>
              <li><b>Trend:</b> $140^\circ$ (pointing towards South-East, azimuth $140^\circ$).</li>
            </ul>
          </div>
        </div>
        """
    },
    23: {
        "title": "Q23: Rock Mechanics: Hooke's Law of Linear Elastic Deformation",
        "part1": """
        <h3>23.1 Fundamental Rheological Models of Rock Deformation</h3>
        <p>In continuum mechanics, rock mechanics, and structural geology (Haakon Fossen, <i>Structural Geology</i>, Ch. 6, pp. 110–115; Turcotte & Schubert, <i>Geodynamics</i>, Ch. 3), the mechanical response of a rock mass under applied stress ($\\sigma$) is described by constitutive rheological laws:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Constitutive Law</th>
                <th>Mathematical Formulation</th>
                <th>Physical Behavior & Rock Rheology</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Hooke's Law (Elasticity)</b></td>
                <td><b>$\\sigma = E \\cdot \\epsilon$</b></td>
                <td><b>Linear elastic behavior</b>: Strain is directly proportional to stress; instantaneous and 100% recoverable upon stress release.</td>
              </tr>
              <tr>
                <td><b>Newton's Law (Viscosity)</b></td>
                <td>$\\sigma = \\eta \\cdot \\dot{\\epsilon}$</td>
                <td><b>Viscous fluid flow</b>: Stress is proportional to strain rate; permanent non-recoverable deformation.</td>
              </tr>
              <tr>
                <td><b>St. Venant (Plasticity)</b></td>
                <td>$\\sigma = \\sigma_y$</td>
                <td><b>Plastic yield</b>: Permanent deformation occurs only when stress exceeds a critical yield stress.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>23.2 Generalized 3D Hooke's Law</h3>
        <p>In isotropic three-dimensional rock mechanics, Hooke's law relates stress and strain through Young's Modulus ($E$) and Poisson's Ratio ($\\nu$):</p>
        $$\\epsilon_x = \\frac{1}{E} [\\sigma_x - \\nu(\\sigma_y + \\sigma_z)]$$
        $$\\epsilon_y = \\frac{1}{E} [\\sigma_y - \\nu(\\sigma_x + \\sigma_z)]$$
        $$\\epsilon_z = \\frac{1}{E} [\\sigma_z - \\nu(\\sigma_x + \\sigma_y)]$$
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Hooke’s law</b> — In elastic deformation, the linear proportionality between stress and strain ($\\sigma = E \\cdot \\epsilon$) is known as <b>Hooke’s law</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Smith's law — INCORRECT:</b> No such constitutive physical law in rock mechanics.</li>
          <li><b>(B) Poisson's ratio — INCORRECT:</b> Poisson's ratio is a dimensionless constant ($\nu = -\epsilon_{\text{trans}} / \epsilon_{\text{axial}}$) measuring lateral expansion, not the proportionality law itself.</li>
          <li><b>(C) Hooke’s law — CORRECT:</b> Formulated by Robert Hooke in 1678 (<i>ut tensio, sic vis</i>), established as the foundational law of linear elasticity.</li>
          <li><b>(D) None of these — INCORRECT.</b></li>
        </ul>
        """,
        "part3": """
        <h3>Rock Elastic Moduli Calculation Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 23: Young's Modulus & Elastic Shortening</div>
          <p>A cylindrical granite core of length $L_0 = 100\\text{ mm}$ with Young's Modulus $E = 50\\text{ GPa}$ is subjected to a uniaxial compressive stress of $\\sigma = 150\\text{ MPa}$. Calculate the axial elastic strain ($\\epsilon$) and change in length ($\\Delta L$).</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            $$\\epsilon = \\frac{\\sigma}{E} = \\frac{150 \\times 10^6\\text{ Pa}}{50 \\times 10^9\\text{ Pa}} = 0.003 = 0.3\\%$$
            $$\\Delta L = \\epsilon \\cdot L_0 = 0.003 \\times 100\\text{ mm} = 0.3\\text{ mm}$$
            <p>The granite core shortens elastically by <b>$0.3\\text{ mm}$</b>, which will be completely recovered if the stress is released.</p>
          </div>
        </div>
        """
    },
    24: {
        "title": "Q24: Fold Geometry: The Hinge Line as the Line of Maximum Curvature",
        "part1": """
        <h3>24.1 Precise Terminology in Fold Geometry</h3>
        <p>In structural geology (Fleuty, 1964, <i>The Description of Folds</i>; Ramsay, 1967; Haakon Fossen, <i>Structural Geology</i>, Ch. 10, pp. 214–218), folded surfaces are rigorously characterized by specific mathematical lines and zones:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Fold Element</th>
                <th>Mathematical / Geometric Definition</th>
                <th>Orientation & Relationship to Topography</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Hinge Line (Hinge)</b></td>
                <td><b>The locus of points of maximum curvature on a folded layer profile ($\frac{d^2y}{dx^2} = \text{max}$)</b></td>
                <td>Intrinsic structural property; completely independent of spatial or topographic orientation.</td>
              </tr>
              <tr>
                <td><b>Fold Axis</b></td>
                <td>A geometric line which, when moved parallel to itself in space, generates the cylindrical fold form</td>
                <td>Direction vector of cylindrical symmetry; parallel to the hinge line in cylindrical folds.</td>
              </tr>
              <tr>
                <td><b>Crest Line</b></td>
                <td>The line connecting the highest topographic / spatial points along a folded layer</td>
                <td>Depends on spatial orientation; coincides with the hinge line only in upright vertical folds.</td>
              </tr>
              <tr>
                <td><b>Trough Line</b></td>
                <td>The line connecting the lowest topographic / spatial points along a folded layer</td>
                <td>Depends on spatial orientation; coincides with synclinal hinge only in upright folds.</td>
              </tr>
              <tr>
                <td><b>Inflection Line</b></td>
                <td>The line separating opposite senses of curvature (zero curvature point, $\kappa = 0$)</td>
                <td>Separates the anticline from the syncline along the fold limb.</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) hinge</b> — The line of maximum curvature on a folded rock surface is mathematically and structurally designated as the <b>hinge</b> (or hinge line).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) trough — INCORRECT:</b> The trough is the line of minimum structural elevation, which diverges from the hinge in inclined/plunging folds.</li>
          <li><b>(B) axis — INCORRECT:</b> The fold axis is an abstract directional vector generating a cylindrical fold by parallel translation, not an actual line of maximum curvature on the layer.</li>
          <li><b>(C) crest — INCORRECT:</b> The crest is the line connecting the highest points on the fold, which shifts away from the hinge line in asymmetrical and inclined folds.</li>
          <li><b>(D) hinge — CORRECT:</b> The canonical, universal structural definition established by M.J. Fleuty (1964) and J.G. Ramsay (1967).</li>
        </ul>
        """,
        "part3": """
        <h3>Fold Morphometrics Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 24: Crest vs. Hinge in an Overturned Anticline</div>
          <p>In an inclined or overturned anticline, do the crest line and the hinge line coincide? Explain why or why not.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p><b>No, they do not coincide.</b> In an inclined or overturned fold, the highest topographic point (the <b>crest</b>) shifts onto the upper limb, while the line of maximum mathematical curvature (the <b>hinge</b>) remains fixed at the structural nose of the fold. The crest and hinge only coincide in strictly upright folds with a vertical axial plane.</p>
          </div>
        </div>
        """
    },
    25: {
        "title": "Q25: Fold Classification: Parallel (Concentric) Folds & Curvature Evolution with Depth",
        "part1": """
        <h3>25.1 Ramsay's Isogon Classification of Folds</h3>
        <p>In structural geology (John G. Ramsay, 1967, <i>Folding and Fracturing of Rocks</i>; Ramsay & Huber, <i>The Techniques of Modern Structural Geology</i>, Vol. 2, pp. 308–320; Fossen, Ch. 10, pp. 225–230), folds are classified based on the behavior of <b>dip isogons</b> and variations in orthogonal layer thickness ($t_\\alpha$):</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Ramsay Fold Class</th>
                <th>Layer Thickness Condition</th>
                <th>Geometric Evolution with Depth & Structural Signatures</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Class 1B: Parallel Fold (Concentric)</b></td>
                <td><b>Orthogonal thickness is constant throughout: $t_\\alpha = t_0 = \\text{const}$</b></td>
                <td><b>Anticlines become sharper and more cuspidate with depth; synclines become broader and flatter with depth</b>. Terminates downward in core space problems, decollements, and cuspate detachment faults.</td>
              </tr>
              <tr>
                <td><b>Class 2: Similar Fold</b></td>
                <td>Axial-planar thickness is constant: $T_\\alpha = T_0$; orthogonal thickness thins on limbs ($t_\\alpha = t_0 \\cos \\alpha$)</td>
                <td><b>Fold profile remains identical and invariant with depth</b>; no change in curvature or sharpness; no space problem in the core.</td>
              </tr>
              <tr>
                <td><b>Class 1A</b></td>
                <td>Limbs thicker than hinge ($t_\\alpha > t_0$)</td>
                <td>Convergent dip isogons, rare in nature.</td>
              </tr>
              <tr>
                <td><b>Class 1C</b></td>
                <td>Limbs thinner than Class 1B but thicker than Class 2</td>
                <td>Weakly modified buckling fold.</td>
              </tr>
              <tr>
                <td><b>Class 3</b></td>
                <td>Extreme limb thinning ($t_\\alpha < t_0 \\cos \\alpha$)</td>
                <td>Divergent dip isogons, typical of incompetent layers between competent competent Class 1B beds.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>25.2 Mathematical Proof of Curvature Evolution in Concentric Folds</h3>
        <p>In concentric circular folding of a multilayer with constant orthogonal bed thickness $t$:</p>
        <p>For an anticline with outer radius of curvature $R_1$, the radius of curvature of the inner underlying layer is:</p>
        $$R_2 = R_1 - t$$
        <p>As depth increases, $R$ decreases towards zero ($R \\to 0$). Because curvature is the inverse of radius ($\\kappa = 1/R$), the curvature $\\kappa \\to \\infty$, forcing the anticlinal core to become <b>infinitely sharp, pinched, and cuspidate</b> until space runs out at depth $z = R_1$.</p>
        <p>Conversely, for the adjacent syncline, the center of curvature lies above ground, so going downward into depth increases the radius ($R_{\\text{depth}} = R_{\\text{surface}} + t$), causing curvature $\\kappa \\to 0$, making the syncline <b>progressively broader, open, and flatter</b> with depth!</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) Parallel fold</b> — A fold in which constant layer thickness causes <b>anticlines to become sharper and synclines to become broader with depth</b> is strictly defined as a <b>Parallel (or Concentric) fold (Ramsay Class 1B)</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Parallel fold — CORRECT:</b> Constant orthogonal thickness preserves layer geometry, mathematically forcing anticlinal cores to sharpen and synclinal cores to broaden with depth.</li>
          <li><b>(B) Similar fold — INCORRECT:</b> In similar folds (Class 2), the fold shape and sharpness are strictly invariant and identical at all depths.</li>
          <li><b>(C) Recumbent fold — INCORRECT:</b> Recumbent describes a spatial orientation where the axial plane is sub-horizontal (dip $< 10^\circ$), regardless of curvature evolution with depth.</li>
          <li><b>(D) Box fold — INCORRECT:</b> A box fold (conjugate fold) has two distinct axial planes and a broad, flat crest.</li>
        </ul>
        """,
        "part3": """
        <h3>Structural Core Space Problem Practice</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 25: The Space Problem at the Core of Parallel Folds</div>
          <p>What structural features commonly develop in sedimentary basins to accommodate the severe \"space problem\" in the sharp core of a parallel anticline?</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>Because concentric beds cannot penetrate into a negative radius of curvature, the core experiences extreme compressive jamming, accommodated by:
            <br>1. <b>Detachment / Decollement thrusting:</b> The competent folded stack detaches from the underlying flat basement.
            <br>2. <b>Out-of-the-core thrust faults:</b> Reverse faults propagate upwards out of the tight hinge.
            <br>3. <b>Core flowage of incompetent material:</b> Flow of ductile salt, shale, or gypsum into the anticlinal core (forming salt or shale diapirs).</p>
          </div>
        </div>
        """
    }
}
