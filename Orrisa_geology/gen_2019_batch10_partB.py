#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 10 Part B (Q129 - Q135)
Electromagnetic Optics, GPS Orbit, Sun-Synchronous Orbits, Albedo, Solar Spectrum, LISS-IV & DIP.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q129: Fresnel Reflection & Transmission at Dielectric Interface
# -----------------------------------------------------------------------------
def gen_q129():
    q_num = 129
    filename = "Q129_Electromagnetic_Wave_Boundary_Reflection_Fresnel_Reflection_Complete_Guide.html"
    title = "Q129: Optical Physics - Fresnel Reflection at Dielectric Boundary"
    badge = "OPSC 2019 Geology Paper-II • Question 129 • Wave Optics & Electromagnetics"
    h1_title = "Electromagnetic Wave Theory: Fresnel Reflection and Transmission Across Media Interfaces"
    meta_text = r"<strong>Topic:</strong> Wave Optics & Boundary Conditions • <strong>Key Concept:</strong> Fresnel Reflection Coefficients ($R_s, R_p$) & Dielectric Boundary Physics • <strong>Textbooks:</strong> Eugene Hecht (<em>Optics</em>, 5th Ed., Ch. 4); Max Born & Emil Wolf (<em>Principles of Optics</em>); T.M. Lillesand et al. (Ch. 1); K.M. Bangar (p. 208)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Fresnel Reflection and Boundary Electrodynamics</div>
      <p>When an electromagnetic (EM) plane wave propagating through a medium of refractive index $n_1$ impinges upon a smooth, planar boundary separating it from a second dielectric medium of refractive index $n_2$, classical electrodynamics (governed by Maxwell's boundary equations) dictates that the incident wave divides into two components:</p>
      <ul>
        <li>A <strong>reflected wave</strong> that turns back into the original incident medium at angle $\theta_r = \theta_i$ (Law of Reflection).</li>
        <li>A <strong>transmitted (refracted) wave</strong> that penetrates and propagates through the second medium at refracted angle $\theta_t$ governed by Snell's Law ($n_1 \sin \theta_i = n_2 \sin \theta_t$).</li>
      </ul>

      <p>The mathematical and physical description of how the incident energy is partitioned between reflection and transmission as a function of incidence angle ($\theta_i$), refractive indices ($n_1, n_2$), and polarization state was formulated by <strong>Augustin-Jean Fresnel</strong> in 1823, and is universally designated as <strong>Fresnel Reflection</strong> (and the <strong>Fresnel Equations</strong>):</p>

      <div class="math-block">
        $$\text{Perpendicular (s-polarized / TE): } r_s = \frac{n_1 \cos\theta_i - n_2 \cos\theta_t}{n_1 \cos\theta_i + n_2 \cos\theta_t} = -\frac{\sin(\theta_i - \theta_t)}{\sin(\theta_i + \theta_t)}$$
        $$\text{Parallel (p-polarized / TM): } r_p = \frac{n_2 \cos\theta_i - n_1 \cos\theta_t}{n_2 \cos\theta_i + n_1 \cos\theta_t} = \frac{\tan(\theta_i - \theta_t)}{\tan(\theta_i + \theta_t)}$$
      </div>

      <p>The fraction of reflected power (reflectance, $R$) is given by $R_s = |r_s|^2$ and $R_p = |r_p|^2$. At normal incidence ($\theta_i = 0^\circ$):</p>

      <div class="math-block">
        $$R = \left(\frac{n_2 - n_1}{n_2 + n_1}\right)^2$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Boundary Phenomenon</th>
              <th>Governing Formulation</th>
              <th>Physical Focus</th>
              <th>Distinction from Other Terms</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>FRESNEL REFLECTION</strong> (Option A)</td>
              <td>Fresnel Equations ($r_s, r_p, R$)</td>
              <td>Quantifies the <strong>amplitude and power fraction of the wave reflected back</strong> into the initial medium from a dielectric boundary.</td>
              <td>Covers both reflection and transmission wave splitting across media of different refractive indices.</td>
            </tr>
            <tr>
              <td>Snell's Law (Option C)</td>
              <td>$n_1 \sin \theta_i = n_2 \sin \theta_t$</td>
              <td>Defines only the <strong>angular trajectory (direction)</strong> of the transmitted beam; does not compute reflected/transmitted energy fractions.</td>
              <td>Geometric ray path only; ignores wave amplitudes, polarization, and energy.</td>
            </tr>
            <tr>
              <td>Fresnel Refraction (Option B)</td>
              <td>$t_s, t_p$ transmission coefficients</td>
              <td>Non-standard terminology; the transmitted portion is termed <em>Fresnel transmission</em> or refraction.</td>
              <td>The question specifically highlights the wave reflected back into the incident medium.</td>
            </tr>
            <tr>
              <td>Spectral Reflectance (Option D)</td>
              <td>$\rho(\lambda) = \frac{\Phi_r(\lambda)}{\Phi_i(\lambda)}$</td>
              <td>Macroscopic ratio of reflected to incident radiant flux as a function of wavelength for natural terrain surfaces.</td>
              <td>Empirical terrain surface property; not the microscopic wave boundary splitting phenomenon.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q129/fresnel_reflection_transmission_dielectric_boundary.png" alt="Fresnel Reflection and Transmission at Dielectric Boundary" class="figure-img">
        <div class="figure-caption">Figure 129: Electromagnetic plane wave impinging on a boundary between two media with refractive indices $n_1$ and $n_2$, illustrating Fresnel Reflection and Transmission (Option A).</div>
      </div>

      <p>Therefore, the classic physical phenomenon wherein an electromagnetic wave strikes a boundary between two media with different refractive indices, with a portion reflected back into the incident medium and the rest transmitted into the second medium, is universally known as <strong>Fresnel Reflection</strong> (Option A).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 129</div>
        <div class="raw-q-text">“An Electromagnetic wave falls on to a boundary between two less homogeneous media with different refractive indices and a part of the wave is reflected back to the incident medium and the rest is transmitted on to the second media.” This phenomenon is known as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Fresnel reflection</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Fresnel refraction</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Snell’s law</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Spectral reflectance</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Fresnel reflection)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Fresnel reflection</div>
          <p>The stated definition is the verbatim textbook definition of <strong>Fresnel reflection</strong> (Hecht; Born & Wolf; Lillesand & Kiefer). It describes the fundamental electromagnetic boundary-value problem where impedance mismatch between two media of differing refractive indices ($n_1 \ne n_2$) forces a portion of the incident wave energy to be reflected back into the incident medium while transmitting the remainder.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Fresnel refraction</div>
          <p>"Fresnel refraction" is an informal/non-standard phrase. The transmitted component is governed by Fresnel transmission coefficients ($t_s, t_p$). Because the question emphasizes the reflected wave component returning to the incident medium, the universal scientific term for this boundary phenomenon is Fresnel reflection.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Snell’s law</div>
          <p>Snell's Law ($n_1 \sin\theta_i = n_2 \sin\theta_t$) specifies only the geometric direction of the refracted ray. It does not predict or compute how much energy is reflected back versus transmitted, nor does it account for wave polarization.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Spectral reflectance</div>
          <p>Spectral reflectance ($\rho_\lambda$) is an empirical remote sensing measure describing the percentage of incident light reflected by a natural target (like green leaves, water, or granite) across individual wavelength bands. It is not the foundational wave-optics boundary principle defined in the question.</p>
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
              <th>Boundary Phenomenon</th>
              <th>Incidence Condition</th>
              <th>Governing Equation / Property</th>
              <th>Geological / Remote Sensing Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Normal Fresnel Reflection</td><td>$\theta_i = 0^\circ$</td><td>$R = \left(\frac{n_2 - n_1}{n_2 + n_1}\right)^2$</td><td>Calibrates air-water surface reflection ($R \approx 2\%$ for water, $n=1.33$)</td></tr>
            <tr><td>Brewster's Angle</td><td>$\theta_i = \theta_B = \arctan(n_2/n_1)$</td><td>$r_p = 0 \implies R_p = 0$</td><td>Parallel polarized light completely penetrates without reflection; reflected beam is $100\%$ s-polarized (used in polarizing sunglasses)</td></tr>
            <tr><td>Total Internal Reflection (TIR)</td><td>$\theta_i \ge \theta_c = \arcsin(n_2/n_1)$ (from dense to rare)</td><td>$R = 1.0$ ($100\%$ reflection)</td><td>Forms optical fiber waveguides and refractometer critical angle salinometers</td></tr>
            <tr><td>Diffuse (Lambertian) Reflection</td><td>Rough surface ($h > \lambda / (8 \cos\theta)$)</td><td>$I(\theta) = I_0 \cos\theta$</td><td>Scatters incident sunlight equally in all directions; models soil and rock outcrops</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the normal-incidence Fresnel reflectance ($R$) at the boundary between air ($n_1 = 1.0$) and pure water ($n_2 = 1.333$)?</div>
        <div class="pq-ans">Answer: Approximately $0.0204$ (or $2.04\%$).</div>
        <div class="pq-exp">$$R = \left(\frac{1.333 - 1.0}{1.333 + 1.0}\right)^2 = \left(\frac{0.333}{2.333}\right)^2 \approx (0.1427)^2 \approx 0.0204$$. Roughly $98\%$ of the light is transmitted into the water column.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is Brewster's angle ($\theta_B$) for light incident from air ($n_1 = 1.0$) onto a flat water surface ($n_2 = 1.333$)?</div>
        <div class="pq-ans">Answer: Approximately $53.1^\circ$.</div>
        <div class="pq-exp">$$\theta_B = \arctan\left(\frac{n_2}{n_1}\right) = \arctan(1.333) \approx 53.1^\circ$$. At this angle, p-polarized reflection drops to zero.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Under what optical condition does total internal reflection occur according to Fresnel formulas?</div>
        <div class="pq-ans">Answer: When light travels from an optically denser medium to a rarer medium ($n_1 > n_2$) at an angle of incidence exceeding the critical angle ($\theta_i \ge \theta_c = \arcsin(n_2/n_1)$).</div>
        <div class="pq-exp">Beyond the critical angle, the refracted wave becomes an evanescent wave decaying exponentially along the boundary, yielding $100\%$ reflection.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. How does surface roughness modify pure specular Fresnel reflection in remote sensing?</div>
        <div class="pq-ans">Answer: By the Rayleigh roughness criterion ($h > \lambda / (8 \cos\theta)$), microscopic surface roughness breaks coherent specular reflection into diffuse Lambertian scattering.</div>
        <div class="pq-exp">Mirror-like Fresnel reflection only occurs on smooth water or polished mineral faces; natural soils exhibit diffuse scattering.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What causes "sun glint" in optical satellite imagery over oceans?</div>
        <div class="pq-ans">Answer: Direct specular Fresnel reflection of sunlight into the satellite sensor's aperture from wind-roughened ocean wave facets.</div>
        <div class="pq-exp">Sun glint saturates optical detectors, obscuring chlorophyll and ocean color information.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In radar remote sensing, how does the dielectric constant of moist soil affect Fresnel reflection?</div>
        <div class="pq-ans">Answer: Water has a high dielectric constant ($\epsilon_r \approx 80$) compared to dry soil ($\epsilon_r \approx 3\text{--}4$); increasing soil moisture dramatically elevates Fresnel reflectivity and radar backscatter.</div>
        <div class="pq-exp">This physical dependence enables spaceborne mapping of soil moisture by SAR and microwave radiometers.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why is the reflected light at Brewster's angle purely linearly polarized?</div>
        <div class="pq-ans">Answer: Because at Brewster's angle, the reflected and transmitted rays are perpendicular ($\theta_i + \theta_t = 90^\circ$); electric dipoles oscillating parallel to the reflection plane have zero radiation along their axis, extinguishing the p-wave.</div>
        <div class="pq-exp">Only the s-polarized component (oscillating perpendicular to the plane of incidence) is reflected.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the complex refractive index ($\tilde{n} = n + i k$) and how does the extinction coefficient ($k$) relate to Fresnel reflection?</div>
        <div class="pq-ans">Answer: The imaginary part $k$ represents optical absorption; high values of $k$ (as in metals and metallic sulfides) produce very high Fresnel reflectivity even at normal incidence.</div>
        <div class="pq-exp">$$R = \frac{(n-1)^2 + k^2}{(n+1)^2 + k^2}$$; this explains the bright metallic luster of pyrite and galena under reflected-light ore microscopy.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q130: Normal Altitude of GPS Satellites (~20,200 km)
# -----------------------------------------------------------------------------
def gen_q130():
    q_num = 130
    filename = "Q130_Normal_Altitude_Of_GPS_Satellite_20200_km_Complete_Guide.html"
    title = "Q130: Satellite Geodesy - Normal Altitude of GPS Satellites"
    badge = "OPSC 2019 Geology Paper-II • Question 130 • Satellite Geodesy & GPS"
    h1_title = "Satellite Geodesy: Orbital Altitude, Constellation Architecture, and Orbital Mechanics of the Global Positioning System (GPS)"
    meta_text = r"<strong>Topic:</strong> GPS Space Segment & Orbital Dynamics • <strong>Key Concept:</strong> Semi-Synchronous Medium Earth Orbit (MEO) at $20,200\text{ km}$ • <strong>Textbooks:</strong> B. Hofmann-Wellenhof et al. (<em>GNSS: GPS, GLONASS, Galileo and more</em>); G. Xu (<em>GPS: Theory, Algorithms and Applications</em>); K.M. Bangar (p. 212)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: GPS Space Segment Orbital Architecture</div>
      <p>The Global Positioning System (GPS, formally NAVSTAR GPS) consists of three interconnected segments: the <strong>Space Segment</strong> (satellite constellation), the <strong>Control Segment</strong> (master control stations, tracking stations, and ground antennas), and the <strong>User Segment</strong> (GPS receivers).</p>

      <p>The baseline nominal constellation of the GPS Space Segment is designed as a Walker $24/6/1$ constellation (24 operational satellites distributed evenly across 6 orbital planes inclined at $55^\circ$ to the equator, with 4 satellites per plane plus on-orbit spares). According to Kepler's Third Law, the orbital period ($T$) of a satellite depends strictly on the semi-major axis ($a$) of its orbit:</p>

      <div class="math-block">
        $$T = 2\pi \sqrt{\frac{a^3}{G M_E}}$$
      </div>

      <p>where $G M_E = 3.986004418 \times 10^{14}\text{ m}^3\text{s}^{-2}$ is the Earth's standard gravitational parameter. GPS satellites are engineered into a <strong>semi-synchronous circular orbit</strong> having an orbital period of exactly <strong>half a sidereal day</strong> (11 hours, 58 minutes, or $43,080\text{ seconds}$):</p>

      <div class="math-block">
        $$a = \left[G M_E \left(\frac{T}{2\pi}\right)^2\right]^{1/3} \approx 26,560\text{ km}$$
      </div>

      <p>Subtracting the mean equatorial radius of the Earth ($R_E \approx 6,378\text{ km}$), we obtain the nominal <strong>orbital altitude</strong> ($h$) above the Earth's surface:</p>

      <div class="math-block">
        $$h = a - R_E = 26,560\text{ km} - 6,378\text{ km} \approx \mathbf{20,182\text{ km}} \approx \mathbf{20,200\text{ km}}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Satellite System / Regime</th>
              <th>Orbital Regime</th>
              <th>Nominal Altitude ($h$)</th>
              <th>Orbital Period ($T$)</th>
              <th>Orbital Inclination ($i$)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>NAVSTAR GPS (USA)</strong> (Option B)</td>
              <td><strong>Medium Earth Orbit (MEO)</strong></td>
              <td><strong>$\approx 20,200\text{ km}$</strong></td>
              <td><strong>11 hr 58 min (Half Sidereal Day)</strong></td>
              <td>$55.0^\circ$</td>
            </tr>
            <tr>
              <td>GLONASS (Russia)</td>
              <td>Medium Earth Orbit (MEO)</td>
              <td>$19,100\text{ km}$</td>
              <td>11 hr 15 min</td>
              <td>$64.8^\circ$</td>
            </tr>
            <tr>
              <td>Galileo (European Union)</td>
              <td>Medium Earth Orbit (MEO)</td>
              <td>$23,222\text{ km}$</td>
              <td>14 hr 05 min</td>
              <td>$56.0^\circ$</td>
            </tr>
            <tr>
              <td>Low Earth Orbit (LEO, e.g. Landsat, Sentinel)</td>
              <td>Low Earth Orbit (LEO)</td>
              <td>$700\text{--}800\text{ km}$</td>
              <td>$\approx 90\text{--}100\text{ min}$</td>
              <td>$\approx 98^\circ$ (Sun-synchronous)</td>
            </tr>
            <tr>
              <td>Geostationary Orbit (GEO, e.g. INSAT, GOES)</td>
              <td>Geostationary / Geosynchronous</td>
              <td>$35,786\text{ km} \approx 36,000\text{ km}$ (Option D)</td>
              <td>23 hr 56 min (1 Sidereal Day)</td>
              <td>$0.0^\circ$ (Equatorial)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q130/gps_satellite_normal_altitude_20200_km_meo.png" alt="Normal Altitude of GPS Satellites" class="figure-img">
        <div class="figure-caption">Figure 130: Orbital altitude comparison across satellite classes, showing GPS positioned in Medium Earth Orbit at $20,200\text{ km}$ with an orbital radius of $26,560\text{ km}$ (Option B).</div>
      </div>

      <p>This orbital altitude provides the optimal geometric compromise: high enough that a single satellite's footprint covers over $38\%$ of the globe, ensuring that anywhere on Earth at least 4 to 12 satellites are continuously visible simultaneously above a $15^\circ$ elevation cutoff mask.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 130</div>
        <div class="raw-q-text">The normal altitude of GPS satellite is about:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> 16,200 km</div>
          <div class="raw-opt"><span class="opt-letter">B</span> 20,200 km</div>
          <div class="raw-opt"><span class="opt-letter">C</span> 24,400 km</div>
          <div class="raw-opt"><span class="opt-letter">D</span> 36,100 km</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (20,200 km)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">20,200 km</div>
          <p>By international GPS geodetic specification (ICD-GPS-200; Hofmann-Wellenhof et al.; Bangar, p. 212), the semi-major axis of a GPS satellite orbit is $a = 26,560\text{ km}$. Subtracting the Earth's radius ($R_E \approx 6,378\text{ km}$) yields the nominal orbital altitude of <strong>$\approx 20,200\text{ km}$</strong> (or $20,182\text{ km}$ exact). This semi-synchronous orbit delivers a repeat track period of 12 sidereal hours.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">16,200 km</div>
          <p>Incorrect altitude. An altitude of $16,200\text{ km}$ would produce an orbital period of $\approx 8.8\text{ hours}$, which is not resonant with Earth's rotation and would destroy the repeating ground-track geometry of the GPS constellation.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">24,400 km</div>
          <p>Incorrect altitude. While closer to the European Galileo constellation ($23,222\text{ km}$), it does not correspond to the United States GPS constellation altitude.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">36,100 km</div>
          <p>This approximates the altitude of a <strong>Geostationary / Geosynchronous orbit</strong> ($h \approx 35,786\text{ km}$), typical of communication and meteorological satellites (e.g. INSAT, Meteosat, GOES) and SBAS augmentation payloads (GAGAN, WAAS), but not the core MEO GPS satellites.</p>
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
              <th>Constellation Parameter</th>
              <th>GPS (NAVSTAR) Value</th>
              <th>GLONASS (Russia)</th>
              <th>Galileo (Europe)</th>
              <th>BeiDou-3 MEO (China)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Nominal Altitude</td><td><strong>$20,200\text{ km}$</strong></td><td>$19,100\text{ km}$</td><td>$23,222\text{ km}$</td><td>$21,528\text{ km}$</td></tr>
            <tr><td>Orbital Radius ($a$)</td><td>$26,560\text{ km}$</td><td>$25,510\text{ km}$</td><td>$29,600\text{ km}$</td><td>$27,906\text{ km}$</td></tr>
            <tr><td>Orbital Period</td><td>$11\text{ hr } 58\text{ min}$</td><td>$11\text{ hr } 15\text{ min}$</td><td>$14\text{ hr } 05\text{ min}$</td><td>$12\text{ hr } 53\text{ min}$</td></tr>
            <tr><td>Number of Orbital Planes</td><td>6 planes ($55^\circ$ inclination)</td><td>3 planes ($64.8^\circ$)</td><td>3 planes ($56^\circ$)</td><td>3 planes ($55^\circ$)</td></tr>
            <tr><td>Ground Track Repeat</td><td>1 sidereal day (repeats daily $4\text{ min}$ earlier)</td><td>8 sidereal days (17 orbits)</td><td>10 sidereal days (17 orbits)</td><td>7 sidereal days (13 orbits)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Why do GPS satellite ground tracks repeat approximately 4 minutes earlier each solar day?</div>
        <div class="pq-ans">Answer: Because the GPS orbital period is half a sidereal day ($11\text{ hr } 58\text{ min}$); two full orbits take 1 sidereal day ($23\text{ hr } 56\text{ min } 4\text{ sec}$), which is $\approx 3\text{ min } 56\text{ sec}$ shorter than a mean solar day ($24\text{ hours}$).</div>
        <div class="pq-exp">A surveyor observing satellite geometry at 10:00 AM on Monday will see the identical constellation geometry at 09:56 AM on Tuesday.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why are GPS satellites placed at $20,200\text{ km}$ altitude rather than in Low Earth Orbit (LEO, $800\text{ km}$)?</div>
        <div class="pq-ans">Answer: At $20,200\text{ km}$, each satellite has a vast footprint covering over $38\%$ of Earth's surface, requiring only 24 satellites for global continuous coverage (compared to hundreds needed in LEO).</div>
        <div class="pq-exp">Higher altitude also avoids atmospheric drag and provides stable, precisely predictable Keplerian orbits.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the minimum number of GPS satellites that a receiver must track simultaneously to determine a unique 3D position and receiver clock offset?</div>
        <div class="pq-ans">Answer: Exactly 4 satellites.</div>
        <div class="pq-exp">Four pseudorange equations are mathematically required to solve for the four unknowns: $X, Y, Z$ coordinates and receiver clock bias $\Delta t_r$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. How does the orbital altitude of $20,200\text{ km}$ impact the signal travel time from a GPS satellite to a ground receiver?</div>
        <div class="pq-ans">Answer: The one-way travel time of the radio wave ($t = d/c$) ranges from approximately $0.067\text{ seconds}$ (at zenith) to $0.086\text{ seconds}$ (at the horizon).</div>
        <div class="pq-exp">$$\frac{20,200\text{ km}}{300,000\text{ km/s}} \approx 0.0673\text{ s}$$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What relativistic effect must be corrected because of the GPS orbital altitude of $20,200\text{ km}$?</div>
        <div class="pq-ans">Answer: General relativistic gravitational blueshift: clocks at $20,200\text{ km}$ tick faster than ground clocks by $+45.9\text{ }\mu\text{s/day}$, while special relativistic velocity slows them by $-7.2\text{ }\mu\text{s/day}$ (net $+38.7\text{ }\mu\text{s/day}$).</div>
        <div class="pq-exp">Satellite atomic clocks are intentionally pre-set to run slower at $10.22999999543\text{ MHz}$ instead of $10.23\text{ MHz}$ so they match ground time exactly.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is Dilution of Precision (DOP) in GPS positioning?</div>
        <div class="pq-ans">Answer: A dimensionless multiplier that expresses how the geometric distribution of tracked satellites magnifies ranging measurement errors into final position errors ($\sigma_{\text{pos}} = \text{GDOP} \cdot \sigma_0$).</div>
        <div class="pq-exp">Low DOP values ($<2$) indicate excellent geometry with satellites widely spaced across the sky.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the name of India's regional satellite navigation system and how do its satellite altitudes differ from GPS?</div>
        <div class="pq-ans">Answer: NavIC (IRNSS); it operates at geostationary and inclined geosynchronous altitudes ($\approx 36,000\text{ km}$), whereas GPS operates at $20,200\text{ km}$ MEO.</div>
        <div class="pq-exp">NavIC's higher orbit focuses continuous coverage over India and the surrounding $1500\text{ km}$ region with only 7 satellites.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the difference between Pseudorange (code phase) and Carrier Phase measurements in GPS?</div>
        <div class="pq-ans">Answer: Pseudorange measures transit time using PRN chipping codes (meter-scale accuracy); carrier phase tracks the cycles of the RF carrier wave ($\lambda \approx 19\text{ cm}$, achieving millimeter-scale geodetic accuracy).</div>
        <div class="pq-exp">Carrier phase tracking requires resolving the integer cycle ambiguity ($N$).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q131: Sun-Synchronous Orbit for Monitoring Dynamic Changes
# -----------------------------------------------------------------------------
def gen_q131():
    q_num = 131
    filename = "Q131_Monitoring_Dynamic_Changes_Sun_Synchronous_Orbit_Complete_Guide.html"
    title = "Q131: Satellite Orbits - Sun-Synchronous Orbit for Dynamic Monitoring"
    badge = "OPSC 2019 Geology Paper-II • Question 131 • Satellite Orbits"
    h1_title = "Satellite Remote Sensing: Sun-Synchronous Orbit Architecture for Monitoring Dynamic Terrestrial Changes"
    meta_text = r"<strong>Topic:</strong> Satellite Orbital Mechanics & Earth Observation • <strong>Key Concept:</strong> Sun-Synchronous Polar Orbits, Nodal Precession & Constant Solar Illumination • <strong>Textbooks:</strong> T.M. Lillesand et al. (Ch. 6); Floyd F. Sabins (Ch. 2); K.M. Bangar (p. 210); C.D. Brown (<em>Elements of Spacecraft Design</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Sun-Synchronous Orbit Physics and Dynamic Monitoring</div>
      <p>When monitoring dynamic surface phenomena on Earth—such as seasonal vegetation phenology, crop growth, volcanic thermal activity, reservoir storage, glacial retreat, urban sprawl, and coastal erosion—satellite data must be collected under <strong>consistent, repeatable solar illumination conditions</strong> over successive repeat passes.</p>

      <p>If solar elevation and azimuth change radically between acquisition dates, differing shadows and changing solar illumination geometry introduce massive false radiance variations that corrupt automated image differencing and change-detection algorithms. To eliminate this critical error source, Earth observation satellites are placed into a <strong>Sun-Synchronous Orbit</strong> (Option B).</p>

      <h4>Orbital Mechanics of Sun-Synchronism</h4>
      <p>Because the Earth is an oblate spheroid (flattened at the poles with equatorial bulge $J_2 = 1.08263 \times 10^{-3}$), its non-spherical gravitational field exerts a torque on inclined orbits, causing the orbital plane to rotate or precess about the Earth's polar axis. This rate of <strong>nodal precession</strong> ($\dot{\Omega}$) is governed by:</p>

      <div class="math-block">
        $$\dot{\Omega} = -\frac{3}{2} J_2 \left(\frac{R_E}{a(1-e^2)}\right)^2 \sqrt{\frac{G M_E}{a^3}} \cos i$$
      </div>

      <p>where $a$ is the semi-major axis, $e$ is orbital eccentricity, and $i$ is orbital inclination. For an orbit to be <strong>sun-synchronous</strong>, the orbital plane must precess eastward at exactly the same rate as the Earth's mean orbital revolution around the Sun ($360^\circ / 365.25\text{ days} = 0.9856^\circ/\text{day} = 1.991 \times 10^{-7}\text{ rad/s}$):</p>

      <div class="math-block">
        $$\dot{\Omega} = +0.9856^\circ / \text{day} \implies \cos i < 0 \implies 90^\circ < i < 180^\circ \text{ (Retrograde Orbit)}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Orbit Type</th>
              <th>Orbital Characteristics</th>
              <th>Illumination Geometry</th>
              <th>Suitability for Monitoring Dynamic Changes</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>SUN-SYNCHRONOUS ORBIT</strong> (Option B)</td>
              <td>Near-polar, retrograde ($i \approx 97^\circ\text{--}99^\circ$), low altitude ($600\text{--}800\text{ km}$). Precesses at $0.9856^\circ/\text{day}$.</td>
              <td><strong>Constant Local Solar Time:</strong> Satellite crosses the equator at the exact same local solar time (typically 10:00 to 10:30 AM) on every pass.</td>
              <td><strong>Ideal & Standard:</strong> Landsat, Sentinel-2, IRS LISS, SPOT. Consistent shadow lengths enable automated multitemporal change detection.</td>
            </tr>
            <tr>
              <td>Non-Synchronous Circular Orbit (Option A)</td>
              <td>Circular orbit ($e=0$) at arbitrary inclination (e.g., ISS at $51.6^\circ$).</td>
              <td>Solar time drifts continuously; passes over targets at dawn, noon, dusk, or midnight.</td>
              <td>Poor: Massive seasonal and diurnal illumination shifts obscure true ground reflectance changes.</td>
            </tr>
            <tr>
              <td>Near Polar Orbit (Option C)</td>
              <td>Inclination near $90^\circ$ but without exact sun-synchronous precession tuning.</td>
              <td>Does not maintain constant local solar time; orbital plane slowly drifts relative to the Sun.</td>
              <td>Sub-optimal: Lacks fixed solar illumination angle; causes seasonal shadow drift.</td>
            </tr>
            <tr>
              <td>Geostationary Orbit (GEO)</td>
              <td>$h \approx 35,786\text{ km}$, $i = 0^\circ$ over the equator.</td>
              <td>Continuous view of one hemisphere, but spatial resolution is coarse ($1\text{--}4\text{ km}$).</td>
              <td>Excellent for rapid weather/clouds, but poor spatial resolution for terrestrial geological change.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q131/sun_synchronous_orbit_dynamic_change_monitoring.png" alt="Sun-Synchronous Orbit Dynamic Monitoring" class="figure-img">
        <div class="figure-caption">Figure 131: Mechanics of a Sun-Synchronous Orbit showing the orbital plane precessing $0.9856^\circ/\text{day}$ to maintain a constant solar angle throughout Earth's annual revolution (Option B).</div>
      </div>

      <p>Because the sun-synchronous orbit ensures that the satellite crosses every terrestrial latitude at precisely the same local solar time, it provides identical solar elevation angles, minimizes shadow differences, and maximizes radiometric comparability across multitemporal scenes.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 131</div>
        <div class="raw-q-text">For interpolation of satellite data used for monitoring dynamic changes that occur on the earth surface, the most suitable orbit for the satellite is :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Circular orbit</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Sun-synchronous orbit</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Near polar orbit</div>
          <div class="raw-opt"><span class="opt-letter">D</span> None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Sun-synchronous orbit)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Sun-synchronous orbit</div>
          <p>A sun-synchronous orbit is precisely tuned so that the satellite's orbital plane precesses eastward at the exact rate of Earth's solar revolution. This guarantees that the satellite passes over any given location on Earth at the <strong>identical local solar time</strong> on every repeat cycle, ensuring uniform sun angle and shadow conditions essential for multitemporal analysis and monitoring dynamic surface changes.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; INSUFFICIENT SPECIFICATION</div>
          <div class="opt-title">Circular orbit</div>
          <p>While sun-synchronous orbits are circular ($e \approx 0$) to keep scale constant, a generic circular orbit can have any inclination (e.g. $28^\circ$ or $51^\circ$). If not sun-synchronous, its overpass time drifts around the clock, causing erratic illumination changes that make dynamic monitoring impossible.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; INCOMPLETE SPECIFICATION</div>
          <div class="opt-title">Near polar orbit</div>
          <p>Sun-synchronous orbits are indeed near-polar ($i \approx 98^\circ$). However, "near polar" alone does not guarantee sun-synchronism; an orbit with $i = 90^\circ$ (true polar) has zero nodal precession ($\cos 90^\circ = 0$), causing its overpass time to drift relative to the Sun by 2 hours every month.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">None of these</div>
          <p>Incorrect, because Option B is the universally accepted standard orbit across all international Earth observation satellite programs.</p>
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
              <th>Satellite Mission</th>
              <th>Orbital Altitude</th>
              <th>Inclination ($i$)</th>
              <th>Equatorial Crossing Time</th>
              <th>Repeat Cycle</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Landsat 8 & 9 (OLI/TIRS)</td><td>$705\text{ km}$</td><td>$98.2^\circ$</td><td>10:00 AM &plusmn; 15 min (Descending)</td><td>16 days (8 days combined)</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>Sentinel-2A & 2B (MSI)</td><td>$786\text{ km}$</td><td>$98.62^\circ$</td><td>10:30 AM (Descending)</td><td>5 days (combined)</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>IRS Resourcesat-1 & 2 (LISS)</td><td>$817\text{ km}$</td><td>$98.7^\circ$</td><td>10:30 AM (Descending)</td><td>24 days</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>Terra & Aqua (MODIS)</td><td>$705\text{ km}$</td><td>$98.2^\circ$</td><td>10:30 AM (Terra) / 1:30 PM (Aqua)</td><td>1 to 2 days (wide swath)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Why do almost all optical land-monitoring satellites choose a descending equatorial crossing time around 10:00 to 10:30 AM?</div>
        <div class="pq-ans">Answer: 10:00 to 10:30 AM provides the ideal compromise: sun elevation is sufficiently high to provide strong radiance, but convective afternoon cloud buildup (cumulus formation) has not yet begun.</div>
        <div class="pq-exp">Waiting until solar noon creates severe afternoon cloudiness over tropical and temperate landmasses.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why must the orbital inclination of a sun-synchronous satellite be greater than $90^\circ$ (retrograde)?</div>
        <div class="pq-ans">Answer: Because nodal precession must be positive (eastward, $+0.9856^\circ/\text{day}$); since the precession formula contains $-\cos i$, $\cos i$ must be negative, requiring $90^\circ < i < 180^\circ$.</div>
        <div class="pq-exp">A retrograde orbit travels slightly against the direction of Earth's rotation to achieve positive nodal precession.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the "temporal resolution" or "repeat cycle" of an Earth observation satellite?</div>
        <div class="pq-ans">Answer: The time interval required for the satellite to complete an integer number of orbits and retrace its exact same ground track.</div>
        <div class="pq-exp">Landsat has a 16-day repeat cycle (233 orbits); Sentinel-2 has a 10-day cycle per satellite (5 days with two satellites).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a "frozen orbit" in satellite Earth observation?</div>
        <div class="pq-ans">Answer: An orbit whose eccentricity ($e$) and argument of perigee ($\omega$) are chosen so that gravitational perturbations cancel, keeping orbital altitude over any given latitude constant over time.</div>
        <div class="pq-exp">Sun-synchronous imaging satellites are placed in frozen orbits to ensure image scale remains identical across repeat tracks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What happens to the nodal precession rate of an orbit if its altitude is increased?</div>
        <div class="pq-ans">Answer: The precession rate decreases ($d\Omega/dt \propto a^{-7/2}$); therefore, to remain sun-synchronous at higher altitudes, the inclination must increase further into retrograde ($i$ increases).</div>
        <div class="pq-exp">At $h=705\text{ km}$, $i=98.2^\circ$; at $h=817\text{ km}$, $i=98.7^\circ$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which satellite change-detection technique computes the algebraic difference between pixel values of two registered, radiometrically calibrated scenes?</div>
        <div class="pq-ans">Answer: Image Differencing ($\Delta BV = BV_{t2} - BV_{t1} + C$).</div>
        <div class="pq-exp">Image differencing requires identical solar illumination geometry provided by sun-synchronous orbits.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Can a geostationary satellite provide global coverage of the Earth's polar regions?</div>
        <div class="pq-ans">Answer: No; because geostationary satellites orbit above the equator ($i=0^\circ$), their line of sight cannot view polar latitudes beyond $\approx 81^\circ\text{N/S}$.</div>
        <div class="pq-exp">Polar monitoring strictly requires polar and sun-synchronous orbits.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a "dawn-dusk" sun-synchronous orbit and what remote sensing instruments typically use it?</div>
        <div class="pq-ans">Answer: A sun-synchronous orbit riding the solar terminator line (crossing equator at ~6:00 AM/PM); used by active SAR satellites (e.g. Radarsat) to maintain continuous solar array illumination.</div>
        <div class="pq-exp">A dawn-dusk orbit avoids the Earth's shadow, providing uninterrupted electrical power to high-drain radar transmitters.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q132: Planetary Albedo vs Spectral Reflectance
# -----------------------------------------------------------------------------
def gen_q132():
    q_num = 132
    filename = "Q132_Ratio_Total_Solar_Radiant_Energy_Returned_Is_Albedo_Complete_Guide.html"
    title = "Q132: Climatology - Planetary Albedo and Radiation Budget"
    badge = "OPSC 2019 Geology Paper-II • Question 132 • Planetary Physics & Climatology"
    h1_title = "Planetary Radiation Physics: Albedo as the Ratio of Total Returned to Incident Solar Radiant Energy"
    meta_text = r"<strong>Topic:</strong> Planetary Radiation Budget & Reflectance • <strong>Key Concept:</strong> Bond Albedo ($A$), Geometric Albedo & Earth Radiation Balance • <strong>Textbooks:</strong> D.L. Hartmann (<em>Global Physical Climatology</em>, 2nd Ed.); J.R. Holton (<em>Dynamic Meteorology</em>); T.M. Lillesand et al. (Ch. 1); K.M. Bangar (p. 209)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Planetary Albedo and Solar Radiant Energy Balance</div>
      <p>The term <strong>albedo</strong> (derived from the Latin <em>albedo</em>, meaning "whiteness") was introduced into photometry by Johann Heinrich Lambert in his 1760 treatise <em>Photometria</em>. In planetary astronomy, climatology, and remote sensing, albedo is a fundamental dimensionless physical quantity defining the reflectivity of an astronomical body.</p>

      <p>By international astrophysical definition, the <strong>Bond Albedo</strong> (also termed <em>planetary albedo</em>, $A$) is defined as the <strong>ratio of the total solar radiant energy reflected and scattered into space across all wavelengths and directions to the total solar radiant energy incident upon the planetary body</strong> (Hartmann; Holton):</p>

      <div class="math-block">
        $$\text{Albedo } (A) = \frac{\text{Total Solar Radiant Energy Returned to Space}}{\text{Total Incident Solar Radiant Energy}} = \frac{\int_0^\infty \int_{4\pi} I_r(\lambda, \theta, \phi) \, d\Omega \, d\lambda}{\int_0^\infty F_{\text{solar}}(\lambda) \, d\lambda}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Reflectance Metric</th>
              <th>Mathematical Definition</th>
              <th>Spectral & Spatial Scope</th>
              <th>Distinction</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>ALBEDO (Bond / Planetary Albedo)</strong> (Option C)</td>
              <td>$$A = \frac{\Phi_{\text{returned}}}{\Phi_{\text{incident}}}$$</td>
              <td><strong>Broadband & Hemispherical (Global):</strong> Integrated over the entire electromagnetic spectrum ($0$ to $\infty$) and all scattering angles ($4\pi$ steradians).</td>
              <td>Quantifies the total global energy fraction rejected by the planetary system into space.</td>
            </tr>
            <tr>
              <td>Spectral Reflectance ($\rho_\lambda$) (Option A)</td>
              <td>$$\rho(\lambda) = \frac{\Phi_r(\lambda)}{\Phi_i(\lambda)}$$</td>
              <td><strong>Narrowband:</strong> Evaluated at a single specific discrete wavelength $\lambda$ or narrow sensor band (e.g., $0.66\text{ }\mu\text{m}$).</td>
              <td>Varies dramatically across the spectrum (e.g. vegetation has low red reflectance but high NIR reflectance).</td>
            </tr>
            <tr>
              <td>Reflectance Factor (Option B)</td>
              <td>$$R(\theta, \phi) = \frac{\Phi_{\text{sample}}}{\Phi_{\text{Lambertian}}}$$</td>
              <td><strong>Bidirectional (BRF):</strong> Ratio of radiant flux reflected by target to that of an ideal lossless Lambertian diffuser under identical viewing geometry.</td>
              <td>Used in laboratory and field spectroradiometry; directional, not global integrated energy.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q132/planetary_albedo_total_solar_radiant_energy_ratio.png" alt="Planetary Albedo and Radiation Budget" class="figure-img">
        <div class="figure-caption">Figure 132: Earth's global solar radiation budget showing that $\approx 30\%$ ($100\text{ W/m}^2$) of incident solar flux ($340\text{ W/m}^2$) is returned to space, defining Earth's planetary albedo of $A \approx 0.30$ (Option C).</div>
      </div>

      <h4>Earth's Planetary Energy Balance</h4>
      <p>The total solar irradiance intercepted by Earth's cross-sectional area ($\pi R_E^2$) is $S_0 \cdot \pi R_E^2$, where the solar constant $S_0 \approx 1361\text{ W/m}^2$. Distributed over the spherical Earth area ($4\pi R_E^2$), mean incoming solar flux is $S_0/4 \approx 340\text{ W/m}^2$. Satellite measurements from NASA's CERES mission confirm that the Earth returns approximately $102\text{ W/m}^2$ back into space, yielding Earth's average <strong>planetary albedo</strong>:</p>

      <div class="math-block">
        $$A_{\text{Earth}} \approx \frac{102\text{ W/m}^2}{340\text{ W/m}^2} \approx \mathbf{0.30} \quad (\mathbf{30\%})$$
      </div>

      <p>The remaining $70\%$ is absorbed by the atmosphere and surface, driving Earth's climate and geological weathering cycles.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 132</div>
        <div class="raw-q-text">The ratio of the total solar radiant energy returned by a planetary body to the total radiant energy incident on the body is called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Reflectance</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Reflectance factor</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Albedo</div>
          <div class="raw-opt"><span class="opt-letter">D</span> None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Albedo)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Albedo</div>
          <p>By international astronomical and climatological definition (Hartmann; Holton; Bangar, p. 209), the <strong>Albedo</strong> (specifically the <em>Bond Albedo</em>) is the ratio of the total electromagnetic solar radiant energy reflected/returned by a planet into space across all wavelengths and directions to the total solar radiant energy incident upon it.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; INCOMPLETE SPECIFICATION</div>
          <div class="opt-title">Reflectance</div>
          <p>Reflectance is generally a wavelength-dependent (spectral) or directional surface property ($\rho_\lambda$). The question specifies the <em>total solar radiant energy returned by an entire planetary body</em>, which is formally designated as the planet's albedo.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Reflectance factor</div>
          <p>Reflectance factor (e.g. Bidirectional Reflectance Factor, BRF) is a directional laboratory and field metric comparing the radiance of a target to a standard white Spectralon panel. It is not the total global planetary energy ratio.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">None of these</div>
          <p>Incorrect, because Albedo is the precise textbook definition.</p>
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
              <th>Terrestrial Surface / Planetary Body</th>
              <th>Typical Albedo Range ($A$)</th>
              <th>Physical Reason for Reflectivity</th>
              <th>Climatic / Geological Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Fresh Dry Snow</td><td>$0.80\text{--}0.90$ ($80\text{--}90\%$)</td><td>Multiple refractive scattering in transparent ice micro-crystals</td><td>Drives positive ice-albedo climate feedback loops</td></tr>
            <tr><td>Thick Stratocumulus Clouds</td><td>$0.60\text{--}0.85$ ($60\text{--}85\%$)</td><td>Dense Mie scattering by spherical water droplets</td><td>Major contributor to Earth's $30\%$ planetary albedo</td></tr>
            <tr><td>Dry Desert Quartz Sand</td><td>$0.35\text{--}0.45$ ($35\text{--}45\%$)</td><td>High quartz purity, low moisture, high surface roughness</td><td>Desert radiative cooling anomalies</td></tr>
            <tr><td>Green Forest Canopy</td><td>$0.10\text{--}0.20$ ($10\text{--}20\%$)</td><td>Strong chlorophyll absorption in blue and red bands</td><td>Low albedo; acts as terrestrial thermal heat sink</td></tr>
            <tr><td>Calm Deep Ocean Water</td><td>$0.05\text{--}0.10$ ($5\text{--}10\%$)</td><td>High optical penetration, low normal Fresnel reflection ($2\%$)</td><td>Absorbs over $90\%$ of solar energy; drives ocean thermal currents</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>Earth as a Whole (Planetary)</td><td><strong>$0.29\text{--}0.31$ ($\approx 30\%$)</strong></td><td>Composite average of clouds ($20\%$), surface ($9\%$), and atmosphere ($1\%$)</td><td>Governs Earth's effective radiating equilibrium temperature ($255\text{ K}$)</td></tr>
            <tr><td>The Moon (Planetary Bond Albedo)</td><td>$0.12$ ($12\%$)</td><td>Dark basaltic maria and impact regolith; no atmosphere or clouds</td><td>Absorbs almost all incident sunlight; extreme diurnal temperature swings</td></tr>
            <tr><td>Venus (Planetary Bond Albedo)</td><td>$0.77$ ($77\%$)</td><td>Dense global sulphuric acid ($\text{H}_2\text{SO}_4$) cloud deck</td><td>Reflects three-quarters of all sunlight back to space</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What would be Earth's effective radiating equilibrium temperature ($T_e$) if its planetary albedo increased from $0.30$ to $0.40$?</div>
        <div class="pq-ans">Answer: It would drop from $255\text{ K}$ ($-18^\circ\text{C}$) to approximately $245\text{ K}$ ($-28^\circ\text{C}$).</div>
        <div class="pq-exp">$$T_e = \left[\frac{S_0 (1 - A)}{4 \sigma}\right]^{1/4}$$; higher albedo reflects more energy, causing severe global cooling.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the difference between Bond Albedo and Geometric Albedo in planetary astronomy?</div>
        <div class="pq-ans">Answer: Bond albedo ($A$) integrates scattered energy over all angles and all wavelengths; Geometric albedo ($p$) is the ratio of target brightness at zero phase angle (opposition) to that of a flat Lambertian disk.</div>
        <div class="pq-exp">They are related by the phase integral $q$: $A = p \cdot q$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the "ice-albedo feedback" mechanism in Quaternary paleoclimatology and Pleistocene glaciation?</div>
        <div class="pq-ans">Answer: A positive feedback: cooling forms high-albedo snow/ice ($A \approx 0.85$), which reflects more solar radiation into space, amplifying the cooling and causing ice sheets to expand.</div>
        <div class="pq-exp">Conversely, melting exposes dark ocean or land ($A \approx 0.10$), accelerating global warming.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Why does melting of Arctic sea ice decrease regional albedo dramatically?</div>
        <div class="pq-ans">Answer: Sea ice covered with snow has an albedo of $0.60\text{--}0.85$, whereas open ocean water has an albedo of only $0.06\text{--}0.10$.</div>
        <div class="pq-exp">Open water absorbs nine times more solar radiation than snow-covered ice, driving rapid Arctic amplification.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which NASA satellite instrument has measured Earth's planetary albedo and radiant energy budget with high precision since 1999?</div>
        <div class="pq-ans">Answer: CERES (Clouds and the Earth's Radiant Energy System) onboard Terra, Aqua, Suomi-NPP, and NOAA-20.</div>
        <div class="pq-exp">CERES measures both reflected shortwave solar radiation ($0.3\text{--}5.0\text{ }\mu\text{m}$) and outgoing longwave thermal radiation ($5\text{--}100\text{ }\mu\text{m}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does cloud cover affect Earth's net radiation budget?</div>
        <div class="pq-ans">Answer: Clouds have a dual effect: high shortwave albedo reflection cools Earth (albedo effect), while greenhouse trapping of outgoing thermal IR warms Earth; currently, the cooling albedo effect dominates by $\approx -20\text{ W/m}^2$.</div>
        <div class="pq-exp">Low, thick clouds cool strongly; high thin cirrus clouds promote net warming.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an albedometer?</div>
        <div class="pq-ans">Answer: An instrument consisting of two pyranometers mounted back-to-back: one pointing upward to measure global incoming solar radiation and one downward to measure reflected radiation.</div>
        <div class="pq-exp">The ratio of the two sensor outputs gives the instant surface albedo: $A = K^\uparrow / K^\downarrow$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the typical albedo of fresh basaltic lava vs. white rhyolitic pumice?</div>
        <div class="pq-ans">Answer: Fresh basaltic lava has a very low albedo ($0.08\text{--}0.12$), whereas rhyolitic pumice has a high albedo ($0.35\text{--}0.50$).</div>
        <div class="pq-exp">High ferrous iron and pyroxene in basalt absorb visible light, whereas light-colored quartz and vesicular glass reflect light efficiently.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q133: Wien's Displacement Law & Maximum Solar Radiation around 0.55 um
# -----------------------------------------------------------------------------
def gen_q133():
    q_num = 133
    filename = "Q133_Maximum_Sun_Radiation_Occurs_Around_0_55_um_Complete_Guide.html"
    title = "Q133: Solar Physics - Wien's Law and Solar Radiation Peak"
    badge = "OPSC 2019 Geology Paper-II • Question 133 • Solar Physics & Radiation"
    h1_title = "Solar Radiation Physics: Wien's Displacement Law and the Peak Emission Wavelength at 0.55 µm"
    meta_text = r"<strong>Topic:</strong> Solar Radiation Physics & Blackbody Spectrum • <strong>Key Concept:</strong> Wien's Displacement Law ($\lambda_{\text{max}} = A/T$) & Solar Photosphere Temperature ($5800\text{ K}$) • <strong>Textbooks:</strong> T.M. Lillesand et al. (Ch. 1); K.M. Bangar (p. 208); Floyd F. Sabins (Ch. 2); Frank Shu (<em>The Physical Universe</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Solar Blackbody Radiation and Wien's Displacement Law</div>
      <p>The Sun is the preeminent primary source of electromagnetic radiation for passive optical remote sensing. For thermodynamic calculations, the Sun radiates closely as an ideal <strong>blackbody</strong> radiator with an effective surface photosphere temperature of approximately <strong>$T_{\text{Sun}} \approx 5778\text{ K} \approx 5800\text{ K}$</strong>.</p>

      <p>According to <strong>Planck's Radiation Law</strong>, the spectral radiant exitance ($M_\lambda$) of a blackbody across wavelength $\lambda$ is given by:</p>

      <div class="math-block">
        $$M_\lambda(T) = \frac{2\pi h c^2}{\lambda^5 \left[\exp\left(\frac{h c}{\lambda k_B T}\right) - 1\right]}$$
      </div>

      <p>By differentiating Planck's equation with respect to wavelength ($\frac{dM_\lambda}{d\lambda} = 0$) and finding the wavelength corresponding to maximum spectral radiant exitance, Wilhelm Wien derived <strong>Wien's Displacement Law</strong> (1893):</p>

      <div class="math-block">
        $$\lambda_{\text{max}} \cdot T = A \implies \lambda_{\text{max}} = \frac{A}{T}$$
      </div>

      <p>where $A$ is Wien's displacement constant ($A \approx 2897.8\text{ }\mu\text{m}\cdot\text{K} \approx 2898\text{ }\mu\text{m}\cdot\text{K}$). Substituting the Sun's effective photosphere temperature ($T \approx 5800\text{ K}$ to $5270\text{ K}$):</p>

      <div class="math-block">
        $$\text{At } T = 5800\text{ K}: \quad \lambda_{\text{max}} = \frac{2898\text{ }\mu\text{m}\cdot\text{K}}{5800\text{ K}} \approx \mathbf{0.50\text{ }\mu\text{m}} \text{ (Blue-Green)}$$
        $$\text{At } T = 5270\text{ K}: \quad \lambda_{\text{max}} = \frac{2898\text{ }\mu\text{m}\cdot\text{K}}{5270\text{ K}} \approx \mathbf{0.55\text{ }\mu\text{m}} \text{ (Green-Yellow visible)}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Radiating Body</th>
              <th>Effective Temperature ($T$)</th>
              <th>Peak Emission Wavelength ($\lambda_{\text{max}}$)</th>
              <th>Spectral Band Designation</th>
              <th>Remote Sensing Relevance</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>The Sun (Photosphere)</strong> (Option B)</td>
              <td><strong>$\approx 5800\text{ K}$</strong></td>
              <td><strong>$\approx 0.48\text{--}0.55\text{ }\mu\text{m}$</strong></td>
              <td><strong>Visible Spectrum (Green/Yellow)</strong></td>
              <td>Primary source of reflected energy for all optical VNIR sensors.</td>
            </tr>
            <tr>
              <td>Forest Fire / Volcanic Lava</td>
              <td>$\approx 800\text{--}1200\text{ K}$</td>
              <td>$\approx 2.4\text{--}3.6\text{ }\mu\text{m}$</td>
              <td>Shortwave & Mid-Infrared (MIR)</td>
              <td>Hotspot detection using $3.7\text{ }\mu\text{m}$ and $2.2\text{ }\mu\text{m}$ bands.</td>
            </tr>
            <tr>
              <td>The Earth (Ambient Surface)</td>
              <td>$\approx 300\text{ K}$ ($27^\circ\text{C}$)</td>
              <td>$\approx 9.7\text{ }\mu\text{m}$</td>
              <td>Thermal Infrared (TIR: $8\text{--}14\text{ }\mu\text{m}$)</td>
              <td>Source of emitted thermal energy for land surface temperature sensors.</td>
            </tr>
            <tr>
              <td>Cosmic Microwave Background</td>
              <td>$2.73\text{ K}$</td>
              <td>$\approx 1.06\text{ mm}$</td>
              <td>Microwave / Sub-millimeter</td>
              <td>Cosmological background radiation.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q133/wiens_law_maximum_solar_radiation_0_55_um.png" alt="Wien's Law and Solar Radiation Peak" class="figure-img">
        <div class="figure-caption">Figure 133: Spectral radiant exitance of the Sun ($5800\text{ K}$) vs. Earth ($300\text{ K}$), showing the solar maximum centered around $0.48\text{--}0.55\text{ }\mu\text{m}$ in the visible band (Option B).</div>
      </div>

      <p>In standard textbook remote sensing (Lillesand & Kiefer; Bangar, p. 208), the Sun's maximum radiant emission is cited as occurring around <strong>$0.55\text{ }\mu\text{m}$</strong> (Option B), matching the peak sensitivity of the human visual system (photopic vision centered at $555\text{ nm}$).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 133</div>
        <div class="raw-q-text">The maximum sun’s radiation occurs around :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> 0.4 um wave length</div>
          <div class="raw-opt"><span class="opt-letter">B</span> 0.55 wave length</div>
          <div class="raw-opt"><span class="opt-letter">C</span> 0.7 um wavelength</div>
          <div class="raw-opt"><span class="opt-letter">D</span> None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (0.55 wave length [0.55 µm])
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">0.55 wave length (0.55 µm)</div>
          <p>By Wien's displacement law ($\lambda_{\text{max}} = A/T$), for a solar surface temperature of $\approx 5500\text{--}5800\text{ K}$, the peak spectral emission is centered around $\mathbf{0.48\text{ to } 0.55\text{ }\mu\text{m}}$ (the green-yellow visible portion of the electromagnetic spectrum). In standard geology and remote sensing literature (Lillesand & Kiefer; Bangar, p. 208), this peak is cited as $0.55\text{ }\mu\text{m}$ (or $550\text{ nm}$).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">0.4 um wave length</div>
          <p>$0.4\text{ }\mu\text{m}$ marks the violet boundary between ultraviolet and visible light. While solar irradiance is substantial here, it lies on the steep rising limb of Planck's curve and is significantly lower than the peak at $0.55\text{ }\mu\text{m}$.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">0.7 um wavelength</div>
          <p>$0.7\text{ }\mu\text{m}$ ($700\text{ nm}$) marks the red boundary where visible light transitions into the near-infrared (NIR). Beyond $0.55\text{ }\mu\text{m}$, solar spectral irradiance decreases monotonically with increasing wavelength.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">None of these</div>
          <p>Incorrect, because Option B is the recognized standard answer.</p>
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
              <th>Wavelength Range</th>
              <th>Electromagnetic Region</th>
              <th>Percentage of Total Solar Energy</th>
              <th>Interaction with Earth Atmosphere</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>$< 0.4\text{ }\mu\text{m}$</td><td>Ultraviolet (UV)</td><td>$\approx 7\%$</td><td>Largely absorbed by stratospheric ozone ($\text{O}_3$); causes intense Rayleigh scattering</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>$0.4\text{--}0.7\text{ }\mu\text{m}$ (Peak at $0.55\text{ }\mu\text{m}$)</td><td>Visible Light (VIS)</td><td><strong>$\approx 43\%$</strong></td><td>High atmospheric transmission; sensed by optical cameras and human eye</td></tr>
            <tr><td>$0.7\text{--}3.0\text{ }\mu\text{m}$</td><td>Near-IR (NIR) & Shortwave-IR (SWIR)</td><td>$\approx 49\%$</td><td>Interrupted by water vapor absorption bands at $1.4\text{ }\mu\text{m}$ and $1.9\text{ }\mu\text{m}$</td></tr>
            <tr><td>$> 3.0\text{ }\mu\text{m}$</td><td>Thermal-IR & Microwave</td><td>$\approx 1\%$</td><td>Negligible solar contribution; dominated by terrestrial thermal emission</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Using Wien's displacement law ($\lambda_{\text{max}} = 2898/T$), calculate the peak emission wavelength of the Earth's surface assuming a mean temperature of $T = 288\text{ K}$ ($15^\circ\text{C}$).</div>
        <div class="pq-ans">Answer: Approximately $10.06\text{ }\mu\text{m}$ (in the thermal infrared band).</div>
        <div class="pq-exp">$$\lambda_{\text{max}} = \frac{2898}{288} \approx 10.06\text{ }\mu\text{m}$$; this falls inside the $8\text{--}14\text{ }\mu\text{m}$ atmospheric window.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why does the human eye have its peak photopic visual sensitivity at approximately $555\text{ nm}$ ($0.55\text{ }\mu\text{m}$)?</div>
        <div class="pq-ans">Answer: Evolutionary adaptation to the peak spectral emission of sunlight penetrating the Earth's atmosphere.</div>
        <div class="pq-exp">Terrestrial organisms evolved optical receptors tuned precisely to where solar photon flux is most abundant.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the crossover wavelength where reflected solar radiation equals emitted terrestrial thermal radiation?</div>
        <div class="pq-ans">Answer: Approximately $3.0\text{ to } 4.0\text{ }\mu\text{m}$ (in the mid-infrared band).</div>
        <div class="pq-exp">Below $3.0\text{ }\mu\text{m}$, reflected solar radiation dominates; above $4.0\text{ }\mu\text{m}$, emitted terrestrial thermal radiation dominates.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the Stefan-Boltzmann Law and how does total solar exitance scale with surface temperature?</div>
        <div class="pq-ans">Answer: $M = \sigma T^4$; total emitted radiant energy increases with the fourth power of absolute temperature.</div>
        <div class="pq-exp">Doubling the surface temperature increases total radiant emission by a factor of $2^4 = 16$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the value of the Solar Constant ($S_0$) at the mean Earth-Sun distance (1 AU)?</div>
        <div class="pq-ans">Answer: Approximately $1361\text{ W/m}^2$ (measured at top of atmosphere by satellite radiometers).</div>
        <div class="pq-exp">Solar constant variations over the 11-year sunspot cycle are small (~0.1%).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In Wien's law, why is it called a "displacement" law?</div>
        <div class="pq-ans">Answer: Because as temperature increases, the peak of the blackbody radiation curve is "displaced" toward shorter and shorter wavelengths ($\lambda_{\text{max}} \propto 1/T$).</div>
        <div class="pq-exp">A heating iron bar transitions from infrared (invisible) to dull red ($700\text{ nm}$), bright orange, and finally white-hot ($0.5\text{ }\mu\text{m}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What are the Fraunhofer absorption lines observed in the solar spectrum?</div>
        <div class="pq-ans">Answer: Dark absorption lines produced by cooler atomic gases in the Sun's outer chromosphere absorbing specific resonant wavelengths (e.g. Sodium D-lines at $589\text{ nm}$, Hydrogen H-$\alpha$ at $656\text{ nm}$).</div>
        <div class="pq-exp">Fraunhofer lines allow remote spectroscopic determination of the chemical composition of the Sun.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What fraction of total solar energy falls within the visible spectrum ($0.4\text{--}0.7\text{ }\mu\text{m}$)?</div>
        <div class="pq-ans">Answer: Approximately $43\%$ to $45\%$.</div>
        <div class="pq-exp">Nearly half of all solar photons fall inside the narrow visible slice centered at $0.55\text{ }\mu\text{m}$.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q134: Spatial Resolution of Resourcesat-1 (IRS-P6) Sensors: LISS-IV = 5.8 m
# -----------------------------------------------------------------------------
def gen_q134():
    q_num = 134
    filename = "Q134_Resolution_Of_LISS_IV_Resourcesat_1_Is_5_8_m_Complete_Guide.html"
    title = "Q134: Indian Remote Sensing - Resourcesat-1 LISS-IV Spatial Resolution"
    badge = "OPSC 2019 Geology Paper-II • Question 134 • Indian Remote Sensing (IRS)"
    h1_title = "Indian Remote Sensing (IRS) Systems: Multi-Resolution Sensor Architecture of Resourcesat-1 (IRS-P6)"
    meta_text = r"<strong>Topic:</strong> ISRO Satellite Sensors & Spatial Resolution • <strong>Key Concept:</strong> Resourcesat-1 Payload Suite: LISS-IV ($5.8\text{ m}$), LISS-III ($23.5\text{ m}$) & AWiFS ($56\text{ m}$) • <strong>Textbooks:</strong> ISRO Resourcesat-1 Mission Specifications; T.M. Lillesand et al. (Ch. 6); K.M. Bangar (p. 210); B.C. Panda (<em>Remote Sensing: Principles and Applications</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Resourcesat-1 (IRS-P6) Multi-Resolution Architecture</div>
      <p>Launched by the Indian Space Research Organisation (ISRO) onboard PSLV-C5 on October 17, 2003, <strong>Resourcesat-1 (IRS-P6)</strong> is a state-of-the-art Earth observation satellite engineered for multidisciplinary natural resources monitoring, agriculture, soil survey, forestry, and geological mapping.</p>

      <p>Placed into a sun-synchronous circular orbit at an altitude of $817\text{ km}$ with an inclination of $98.7^\circ$ and a 10:30 AM equatorial descending node, Resourcesat-1 pioneered a unique <strong>three-tier synchronized multi-resolution imaging system</strong> designed to observe terrain simultaneously across local, regional, and national scales:</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sensor Payload</th>
              <th>Spatial Resolution (Nadir)</th>
              <th>Spectral Bands</th>
              <th>Swath Width</th>
              <th>Target Application</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>LISS-IV (Linear Imaging Self-Scanning Sensor-IV)</strong> (Option A)</td>
              <td><strong>$5.8\text{ meters}$</strong></td>
              <td>Band 2 (Green: $0.52\text{--}0.59\text{ }\mu\text{m}$)<br>Band 3 (Red: $0.62\text{--}0.68\text{ }\mu\text{m}$)<br>Band 4 (NIR: $0.77\text{--}0.86\text{ }\mu\text{m}$)</td>
              <td>$23.9\text{ km}$ (Multispectral Mode, MX)<br>$70.3\text{ km}$ (Mono Mode)</td>
              <td>Cadastral-level mapping (1:10,000 to 1:25,000 scale), urban planning, precision agriculture, detailed fault scarp mapping.</td>
            </tr>
            <tr>
              <td><strong>LISS-III (Linear Imaging Self-Scanning Sensor-III)</strong> (Option B)</td>
              <td><strong>$23.5\text{ meters}$</strong></td>
              <td>Band 2 (Green), Band 3 (Red), Band 4 (NIR), Band 5 (SWIR: $1.55\text{--}1.70\text{ }\mu\text{m}$)</td>
              <td>$141\text{ km}$</td>
              <td>District-level mapping (1:50,000 scale), mineral exploration, regional geological structural analysis.</td>
            </tr>
            <tr>
              <td><strong>AWiFS (Advanced Wide Field Sensor)</strong> (Option C)</td>
              <td><strong>$56\text{ meters}$</strong></td>
              <td>Band 2 (Green), Band 3 (Red), Band 4 (NIR), Band 5 (SWIR)</td>
              <td>$740\text{ km}$ (Twin camera heads)</td>
              <td>National-scale dynamic vegetation monitoring, crop production forecasting, snowmelt runoff with 5-day revisit.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q134/resourcesat_1_liss_iv_spatial_resolution_5_8m.png" alt="Resourcesat-1 LISS-IV Resolution" class="figure-img">
        <div class="figure-caption">Figure 134: Hierarchical multi-sensor spatial resolution suite of ISRO's Resourcesat-1 (IRS-P6), illustrating LISS-IV at $5.8\text{ m}$ (Option A), LISS-III at $23.5\text{ m}$, and AWiFS at $56\text{ m}$.</div>
      </div>

      <p>LISS-IV operates in two distinct imaging modes: a <strong>Multispectral (MX) mode</strong> transmitting three VNIR spectral bands across a $23.9\text{ km}$ swath, and a <strong>Monochrome (Mono) mode</strong> transmitting single-band data across a wide $70.3\text{ km}$ swath. Furthermore, the LISS-IV camera head features across-track steerability up to $\pm 26^\circ$, enabling 5-day stereoscopic imaging and targeted disaster revisit.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 134</div>
        <div class="raw-q-text">The resolution (m) of LISS-IV Resourcesat—1 is:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> 5.8 m</div>
          <div class="raw-opt"><span class="opt-letter">B</span> 23.5 m</div>
          <div class="raw-opt"><span class="opt-letter">C</span> 56 m</div>
          <div class="raw-opt"><span class="opt-letter">D</span> 70.5 m</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (5.8 m)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">5.8 m</div>
          <p>By official ISRO technical specifications (ISRO NRSC; Lillesand & Kiefer; Bangar, p. 210), the <strong>LISS-IV camera onboard Resourcesat-1 (IRS-P6)</strong> has a ground sampling distance (spatial resolution at nadir) of exactly <strong>$5.8\text{ meters}$</strong> in both multispectral and panchromatic/monochrome modes.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">23.5 m</div>
          <p>$23.5\text{ m}$ is the spatial resolution of the <strong>LISS-III</strong> sensor onboard IRS-1C, IRS-1D, and Resourcesat-1/2, not LISS-IV.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">56 m</div>
          <p>$56\text{ m}$ is the nadir spatial resolution of the <strong>AWiFS (Advanced Wide Field Sensor)</strong> onboard Resourcesat-1/2.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">70.5 m</div>
          <p>$70.5\text{ m}$ approximates the wide swath width of LISS-IV in Mono mode ($70.3\text{ km}$), or is a distractor derived by confusing swath dimensions with resolution numbers ($72.5\text{ m}$ was the resolution of the legacy LISS-I sensor on IRS-1A/1B).</p>
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
              <th>IRS Mission</th>
              <th>Sensor Name</th>
              <th>Nadir Spatial Resolution</th>
              <th>Swath Width</th>
              <th>Launch Year</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>IRS-1A & 1B</td><td>LISS-I / LISS-II</td><td>$72.5\text{ m}$ / $36.25\text{ m}$</td><td>$148\text{ km}$</td><td>1988 / 1991</td></tr>
            <tr><td>IRS-1C & 1D</td><td>PAN / LISS-III / WiFS</td><td>$5.8\text{ m}$ (Pan) / $23.5\text{ m}$ / $188\text{ m}$</td><td>$70\text{ km}$ / $141\text{ km}$ / $810\text{ km}$</td><td>1995 / 1997</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>Resourcesat-1 (IRS-P6)</td><td><strong>LISS-IV</strong></td><td><strong>$5.8\text{ m}$ (Multispectral)</strong></td><td>$23.9\text{ km}$ / $70.3\text{ km}$</td><td>2003</td></tr>
            <tr style="background:#eff6ff;"><td>Resourcesat-2 & 2A</td><td>LISS-IV / LISS-III / AWiFS</td><td>$5.8\text{ m}$ / $23.5\text{ m}$ / $56\text{ m}$</td><td>$70.3\text{ km}$ (full MX) / $141\text{ km}$ / $740\text{ km}$</td><td>2011 / 2016</td></tr>
            <tr><td>Cartosat-1</td><td>PAN (Fore / Aft stereo)</td><td>$2.5\text{ m}$</td><td>$30\text{ km}$</td><td>2005</td></tr>
            <tr><td>Cartosat-2 Series</td><td>Panchromatic / VNIR</td><td>$< 1.0\text{ m}$ (down to $0.65\text{ m}$)</td><td>$9.6\text{ km}$</td><td>2007–2018</td></tr>
            <tr><td>Cartosat-3</td><td>PAN / MX</td><td>$0.28\text{ m}$ (Pan) / $1.12\text{ m}$ (MX)</td><td>$16\text{ km}$</td><td>2019</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What major advancement in LISS-IV was introduced with the launch of Resourcesat-2 compared to Resourcesat-1?</div>
        <div class="pq-ans">Answer: Resourcesat-2 enabled multispectral (MX) 3-band imaging across the full $70.3\text{ km}$ swath width, whereas Resourcesat-1 was limited to $23.9\text{ km}$ in MX mode.</div>
        <div class="pq-exp">Resourcesat-2 eliminated the hardware bottleneck by integrating improved high-data-rate X-band downlinks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which detector technology is used in ISRO's LISS sensors?</div>
        <div class="pq-ans">Answer: Pushbroom Linear Charge-Coupled Device (CCD) detector arrays (along-track scanning).</div>
        <div class="pq-exp">Pushbroom arrays eliminate rotating scan mirrors, drastically increasing dwell time and signal-to-noise ratio.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Can the LISS-IV sensor acquire stereoscopic imagery for generating Digital Elevation Models (DEMs)?</div>
        <div class="pq-ans">Answer: Yes; its camera head can be tilted across-track up to $\pm 26^\circ$, allowing stereo pairs to be acquired on successive orbits.</div>
        <div class="pq-exp">Stereo pairs yield high-resolution 3D terrain models for engineering geology and landslide analysis.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the radiometric resolution (bit depth) of the LISS-IV sensor onboard Resourcesat-1?</div>
        <div class="pq-ans">Answer: 7-bit quantization (128 digital brightness levels), upgraded to 10-bit (1024 levels) in Resourcesat-2.</div>
        <div class="pq-exp">Higher bit depth enhances detection of subtle radiometric differences in shadows and dense canopies.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which ISRO satellite series is dedicated to sub-meter high-resolution cartographic mapping and DEM generation?</div>
        <div class="pq-ans">Answer: The Cartosat series (Cartosat-1, 2, 2A/2B/2C/2D/2E, and Cartosat-3).</div>
        <div class="pq-exp">Cartosat-3 achieves $28\text{ cm}$ panchromatic spatial resolution.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which spectral band is present in LISS-III and AWiFS but completely absent in LISS-IV?</div>
        <div class="pq-ans">Answer: The Shortwave Infrared (SWIR) Band 5 ($1.55\text{--}1.70\text{ }\mu\text{m}$).</div>
        <div class="pq-exp">LISS-IV operates strictly in the three VNIR bands (Green, Red, NIR); SWIR was omitted to maintain high optical spatial resolution.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the mapping scale recommended by the Survey of India for satellite imagery with $5.8\text{ m}$ spatial resolution?</div>
        <div class="pq-ans">Answer: 1:12,500 to 1:25,000 scale thematic mapping.</div>
        <div class="pq-exp">As an empirical rule of thumb: $\text{Map Scale} \approx \text{Spatial Resolution (m)} \times 2000 \text{ to } 4000$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the revisit time of Resourcesat-1 LISS-IV when utilizing its $\pm 26^\circ$ off-nadir steering capability?</div>
        <div class="pq-ans">Answer: Approximately 5 days (compared to the standard 24-day nadir repeat cycle).</div>
        <div class="pq-exp">Off-nadir steering enables rapid response during floods, cyclones, and landslides.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q135: Digital Image Processing (Rectification, Enhancement, Classification)
# -----------------------------------------------------------------------------
def gen_q135():
    q_num = 135
    filename = "Q135_Digital_Data_Manipulation_Enhancement_Image_Processing_Complete_Guide.html"
    title = "Q135: Digital Image Processing - Foundations and Core Operations"
    badge = "OPSC 2019 Geology Paper-II • Question 135 • Digital Image Processing (DIP)"
    h1_title = "Digital Image Processing: The Core Framework of Preprocessing, Enhancement, Transformation, and Classification"
    meta_text = r"<strong>Topic:</strong> Digital Image Processing Principles • <strong>Key Concept:</strong> The Four Core Domains of DIP: Restoration, Enhancement, Transformation & Classification • <strong>Textbooks:</strong> J.R. Jensen (<em>Introductory Digital Image Processing: A Remote Sensing Perspective</em>, 4th Ed.); T.M. Lillesand et al. (Ch. 7); R.C. Gonzalez & R.E. Woods (<em>Digital Image Processing</em>); K.M. Bangar (p. 211)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Scope of Digital Image Processing (DIP)</div>
      <p>In remote sensing and computer vision, <strong>Digital Image Processing (DIP)</strong> encompasses the broad scientific discipline, theoretical framework, and computational manipulation of digital matrix data (pixel arrays) to extract information, improve visual interpretability, and correct geometric/radiometric distortions.</p>

      <p>A digital satellite image is fundamentally modeled as a discrete two-dimensional spatial function $f(x, y)$, where $x$ and $y$ are spatial coordinates and the amplitude of $f$ at any coordinate is the <strong>Brightness Value (BV)</strong> or <strong>Digital Number (DN)</strong>. DIP is systematically divided into four foundational sequential sub-disciplines (Jensen; Lillesand & Kiefer; Gonzalez & Woods):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>DIP Processing Domain</th>
              <th>Core Mathematical Operations</th>
              <th>Primary Technical Objective</th>
              <th>Specific Methods & Algorithms</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Radiometric & Geometric Rectification (Restoration)</strong></td>
              <td>Sensor calibration, line-dropout repair, atmospheric dark-object subtraction (DOS), polynomial geometric warping.</td>
              <td>Corrects sensor errors, atmospheric path radiance, and geometric distortions to restore ground fidelity.</td>
              <td>Affine transformation, GCP regression, Nearest Neighbor / Bilinear resampling, FLAASH.</td>
            </tr>
            <tr>
              <td><strong>2. Image Enhancement</strong></td>
              <td>Point and local neighborhood spatial operators: $g(x,y) = T[f(x,y)]$.</td>
              <td>Maximizes visual contrast and feature discrimination for human visual interpretation.</td>
              <td>Linear contrast stretching, Histogram equalization, High-pass/directional filtering, Edge detection (Sobel/Laplacian).</td>
            </tr>
            <tr>
              <td><strong>3. Spectral Transformation</strong></td>
              <td>Band arithmetic, orthogonal subspace rotations, color space conversions.</td>
              <td>Reduces dimensionality, compresses correlation, and highlights diagnostic geological absorption.</td>
              <td>Principal Component Analysis (PCA), Band Ratios (e.g. Clay Ratio $1.6/2.2$), Normalized Difference Vegetation Index (NDVI).</td>
            </tr>
            <tr>
              <td><strong>4. Image Classification</strong></td>
              <td>Supervised and unsupervised statistical and machine-learning pattern recognition.</td>
              <td>Converts continuous spectral pixel values into thematic, discrete land cover / geological rock-type classes.</td>
              <td>Maximum Likelihood (MLC), Minimum Distance, ISODATA, Random Forest, Support Vector Machines (SVM).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q135/digital_image_processing_enhancement_classification_rectification.png" alt="Digital Image Processing Operations" class="figure-img">
        <div class="figure-caption">Figure 135: End-to-end architecture of Digital Image Processing (Option B), spanning image rectification, enhancement, spectral band transformation, and thematic classification.</div>
      </div>

      <p>By formal scientific definition, the umbrella discipline encompassing <em>"the art and science of manipulation of digital data including enhancement, classification, and rectification"</em> is universally known as <strong>Image Processing</strong> (or <em>Digital Image Processing</em>, Option B). Orthorectification (Option A) and Rectification (Option C) represent individual sub-operations within the broader image processing domain.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 135</div>
        <div class="raw-q-text">The art and science of manipulation of digital data including enhancement, classification and rectification is known as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Orthorectification</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Image processing</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Rectification</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Geometric correction</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Image processing)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Image processing</div>
          <p>By international remote sensing and photogrammetric definitions (Jensen; Lillesand & Kiefer; Gonzalez & Woods; Bangar, p. 211), <strong>Image Processing</strong> (Digital Image Processing, DIP) is the overarching field that integrates all computational algorithms for manipulating digital image data—including radiometric/geometric rectification, contrast enhancement, spatial filtering, band transformation, and automated multispectral classification.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; SUBSET OPERATION</div>
          <div class="opt-title">Orthorectification</div>
          <p>Orthorectification is a specialized sub-procedure of geometric rectification that corrects for terrain relief displacement using a Digital Elevation Model (DEM). It does not encompass contrast enhancement, spatial filtering, or thematic classification.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; SUBSET OPERATION</div>
          <div class="opt-title">Rectification</div>
          <p>Rectification is the geometric process of transforming image pixel coordinates into a standard map projection coordinate system. It is only one preparatory phase of image processing, completely omitting enhancement and classification.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; SUBSET OPERATION</div>
          <div class="opt-title">Geometric correction</div>
          <p>Geometric correction addresses sensor distortions and platform wobble. Like Options A and C, it is a sub-component of image restoration, not the comprehensive science defined in the question.</p>
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
              <th>Image Processing Sub-Operation</th>
              <th>Input Data</th>
              <th>Mathematical Operator</th>
              <th>Output Product</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Contrast Stretching</td><td>Raw low-contrast digital scene</td><td>Linear min-max normalization: $\text{DN}' = \frac{\text{DN} - \text{MIN}}{\text{MAX} - \text{MIN}} \times 255$</td><td>Enhanced visual contrast image utilizing full dynamic range</td></tr>
            <tr><td>Spatial Filtering (High-Pass)</td><td>Rectified multispectral image</td><td>$3 \times 3$ convolution kernel: $\sum \sum w_{ij} f(x+i, y+j)$</td><td>Sharpened structural lineaments, geological contacts, and faults</td></tr>
            <tr><td>Principal Component Analysis</td><td>$k$ highly correlated spectral bands</td><td>Eigenvector decomposition of covariance matrix: $\mathbf{Y} = \mathbf{V}^T \mathbf{X}$</td><td>Uncorrelated PC bands concentrating $>95\%$ variance in PC1/PC2</td></tr>
            <tr><td>Supervised Classification</td><td>Multispectral image + Training sites</td><td>Bayesian Maximum Likelihood decision rule ($P(\omega_i | x)$)</td><td>Thematic lithological / land use map with quantified class boundaries</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental difference between supervised and unsupervised image classification?</div>
        <div class="pq-ans">Answer: Supervised classification uses user-defined training sites of known ground-truth classes to train a classifier; unsupervised classification automatically clusters pixels into natural statistical spectral groupings (e.g. K-means, ISODATA) without prior training data.</div>
        <div class="pq-exp">Supervised classification requires prior field knowledge; unsupervised classification discovers intrinsic data structure.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is Histogram Equalization in image enhancement?</div>
        <div class="pq-ans">Answer: A non-linear contrast enhancement technique that redistributes pixel brightness values so that the cumulative distribution function (CDF) of the output image is linear, producing a uniform flat histogram.</div>
        <div class="pq-exp">It expands contrast in the most heavily populated brightness ranges at the expense of sparsely populated tails.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Why are band ratio images (e.g. Landsat Band 5 / Band 7) uniquely powerful in geological exploration?</div>
        <div class="pq-ans">Answer: Band ratios cancel out topographic shadow effects (illumination variations) while accentuating diagnostic mineral absorption features (e.g. clay and hydroxyl minerals absorb in Band 7 and reflect in Band 5).</div>
        <div class="pq-exp">Ratioing isolates intrinsic spectral reflectance from extrinsic lighting and slope geometry.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the purpose of a Low-Pass spatial filter in digital image processing?</div>
        <div class="pq-ans">Answer: To suppress high-frequency spatial noise, smooth the image, and blur sharp boundaries by computing local neighborhood averages.</div>
        <div class="pq-exp">Low-pass filters reduce random speckle noise in radar and optical images before classification.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the Normalized Difference Vegetation Index (NDVI) formula?</div>
        <div class="pq-ans">Answer: $$\text{NDVI} = \frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$$.</div>
        <div class="pq-exp">Healthy green vegetation absorbs red light for photosynthesis and strongly reflects near-infrared from spongy mesophyll tissue, yielding high positive NDVI ($0.5\text{--}0.85$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In supervised classification, what statistical decision rule assumes a multivariate normal (Gaussian) distribution for each spectral class?</div>
        <div class="pq-ans">Answer: The Maximum Likelihood Classifier (MLC).</div>
        <div class="pq-exp">MLC calculates the probability that a pixel belongs to each candidate class based on the mean vector and covariance matrix, assigning it to the highest-probability class.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an "Error Matrix" or "Confusion Matrix" in remote sensing classification accuracy assessment?</div>
        <div class="pq-ans">Answer: A cross-tabulation table comparing classified map categories against verified reference ground-truth data to compute Producer's Accuracy, User's Accuracy, Overall Accuracy, and the Kappa Coefficient ($\hat{K}$).</div>
        <div class="pq-exp">Kappa evaluates accuracy while accounting for chance agreement.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is "Pansharpening" (Image Fusion) in digital image processing?</div>
        <div class="pq-ans">Answer: Merging a high-spatial-resolution panchromatic band with lower-spatial-resolution multispectral bands (using IHS, Brovey, or Gram-Schmidt transforms) to produce high-resolution color imagery.</div>
        <div class="pq-exp">Pansharpening preserves the spatial sharpness of the panchromatic image while retaining the spectral colors of the multispectral data.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Solutions Batch 10 Part B (Q129 - Q135)...")
    gen_q129()
    gen_q130()
    gen_q131()
    gen_q132()
    gen_q133()
    gen_q134()
    gen_q135()
    print("Batch 10 Part B successfully generated!")
