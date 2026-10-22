#!/usr/bin/env python3
"""
Masterclass Builder for Q006 and Q007
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q006: OSL Dating
# ==============================================================================
def generate_q006():
    title = "Q006: Optically Stimulated Luminescence (OSL) Geochronology & Zeroing Physics | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Quaternary Geology & Geochronology"
    h1_title = "Q006: Optically Stimulated Luminescence (OSL) Geochronology & Zeroing Physics"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 6<br>
<strong>Authoritative References:</strong> M.J. Aitken, <em>An Introduction to Optical Dating</em> (Oxford University Press, 1998); Murray & Wintle (2000, <em>Radiation Measurements</em>, 32, pp. 57–73); Rhodes, E.J. (2011, <em>Quaternary Science Reviews</em>, 30, pp. 770–822); Duller, G.A.T. (2008, <em>Luminescence Dating Guidelines</em>)."""

    part1 = r"""
  <!-- CARD 1: THE PHYSICS OF TRAPPED CHARGE LUMINESCENCE -->
  <div class="card">
    <div class="card-header bg-blue">1. The Solid-State Physics of Trapped-Charge Geochronology</div>
    <div class="card-body">
      <p><strong>Optically Stimulated Luminescence (OSL)</strong> dating is a revolutionary trapped-charge geochronological technique that determines the elapsed time since ubiquitous mineral grains (principally <strong>quartz</strong>, $\text{SiO}_2$, and <strong>potassium feldspar</strong>, $\text{KAlSi}_3\text{O}_8$) were last exposed to sunlight or heat. The physical mechanism operates through solid-state defect crystal lattices:</p>

      <ul>
        <li><strong>Ionizing Ambient Radiation:</strong> Natural sediments contain trace concentrations of radioactive isotopes ($^{238}\text{U}$, $^{235}\text{U}$, $^{232}\text{Th}$, their decay daughters, and $^{40}\text{K}$), accompanied by penetrating cosmic rays. This flux emits $\alpha, \beta$, and $\gamma$ radiation, steadily ionizing surrounding mineral grains.</li>
        <li><strong>Metastable Trapping:</strong> Ionization excites electrons from the valence band to the conduction band. Most electrons recombine instantly, but a fraction become trapped in crystal lattice defects (such as oxygen vacancies / E' centers and titanium/aluminum substitution sites). These trapped electrons occupy metastable energy states with lifetimes exceeding millions of years at ambient Earth temperatures.</li>
        <li><strong>Stimulation & Luminescence Emission:</strong> When stimulated in the laboratory with specific wavelengths of light (blue light at $470\text{ nm}$ for quartz, or infrared at $870\text{ nm}$ for feldspar), the trapped electrons are evicted from their traps, drop into luminescence centers, and emit photons of higher energy (UV light around $375\text{ nm}$). The emitted photon flux is directly proportional to the radiation dose absorbed.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">The Fundamental Luminescence Age Equation (Aitken, 1998)</div>
        $$\text{OSL Age (years)} = \frac{D_e}{\dot{D}} = \frac{\text{Equivalent Paleodose (Grays, Gy)}}{\text{Environmental Dose Rate (Gy/year or Gy/ka)}}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $D_e$ is the total ionizing radiation dose accumulated by the mineral since burial, and $\dot{D}$ is the annual dose rate emitted by radioactive decay in the host sediment and cosmic radiation.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q06/osl_dating_mechanism.png" alt="OSL Dating Physical Mechanism">
        <div class="tb-caption">
          <strong>Figure 6.1: Physical Mechanism of OSL Dating.</strong> The cyclic luminescence clock: (1) Daylight bleaching during subaerial transport zeroes the trapped electrons; (2) Burial under darkness accumulates trapped charge at dose rate $\dot{D}$; (3) Laboratory optical stimulation releases stored luminescence measuring paleodose $D_e$.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE ZEROING / BLEACHING EVENT -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Zeroing Event: Optical Bleaching vs. Thermal Firing</div>
    <div class="card-body">
      <p>For a trapped-charge clock to measure the true geological or archaeological age, the stored charge in the crystal traps must be completely evacuated (zeroed) at the starting event of interest ($t = 0$):</p>

      <ul>
        <li><strong>(i) Naturally Occurring Sediments (Optical Bleaching):</strong> During subaerial transport by wind (aeolian dunes, loess, sand sheets), rivers (alluvial plains, bars), or waves (coastal beaches, barrier islands), mineral grains are exposed to sunlight. Natural daylight is so potent that <strong>just a few seconds to minutes of direct sunlight exposure completely bleaches the light-sensitive quartz traps to zero</strong>. Upon subsequent burial by overlying strata, darkness ensues, and the luminescence clock begins ticking.</li>
        <li><strong>(ii) Man-Made Materials (Thermal Zeroing):</strong> When ancient humans fired archaeological ceramic vessels, pottery, bricks, or burnt clay hearths in kilns at temperatures exceeding $450 - 500^\circ\text{C}$, the thermal energy completely evacuated all trapped electrons, resetting the luminescence clock to zero at the exact moment of manufacture.</li>
      </ul>

      <div class="quote-box">
        "Optically stimulated luminescence (OSL) dating determines the time since quartz or feldspar grains were last exposed to daylight or heat. It is widely applied to naturally occurring sediments such as aeolian sands, loess, fluvial deposits, and coastal dunes, as well as heated archaeological materials like pottery and burnt flints."
        <span class="quote-ref">— E.J. Rhodes, <em>Optically Stimulated Luminescence Dating of Sediments over the Past 200,000 Years</em> (Quaternary Science Reviews, 2011, p. 771)</span>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY IGNEOUS & METAMORPHIC ROCKS CANNOT BE OSL DATED -->
  <div class="card">
    <div class="card-header bg-emerald">3. Crystal Saturation: Why Intrusive Igneous & Metamorphic Rocks Fail</div>
    <div class="card-body">
      <p>Why are <strong>(iii) Intrusive igneous rocks</strong> (granites, gabbros) and <strong>(iv) Metasedimentary rocks</strong> (quartzites, schists) fundamentally unsuitable for determining geological crystallization or metamorphic ages via OSL?</p>

      <ul>
        <li><strong>Trapping Saturation Limit ($D_0$):</strong> Mineral defect traps have a finite capacity. Under continuous natural background radiation ($\sim 2 - 4\text{ mGy/yr}$), the electron traps in quartz become completely filled and reach asymptotic saturation at doses around $100 - 300\text{ Gy}$ (corresponding to an absolute dating ceiling of $\sim 150,000 - 300,000\text{ years}$).</li>
        <li><strong>Millions of Years of Radiation:</strong> Intrusive igneous rocks crystallized deep in the crust millions of years ago (e.g., Archean or Proterozoic granites). Their traps reached 100% saturation tens of millions of years ago, rendering them completely incapable of measuring geological formation age.</li>
        <li><strong>Absence of Sunlight Zeroing:</strong> Intrusive plutons crystallize kilometers underground without ever seeing daylight. Because there was no optical bleaching event during crystallization, the OSL clock was never zeroed.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 6)</div>
    <div class="q-stmt">
      Q6. Optically Stimulated Luminescence (OSL) dating methods are useful for determining the age of: (i) Naturally occurring sediments, (ii) Man-made materials like pottery, (iii) Intrusive igneous rocks, (iv) Metasedimentary rocks. Choose the correct set of answer from the following options :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) (i), (ii) and (iii)</div>
      <div class="raw-opt correct">(B) (i) and (ii) &nbsp;✔</div>
      <div class="raw-opt">(C) (iii) and (iv)</div>
      <div class="raw-opt">(D) (i) and (iii)</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) (i) and (ii)</div>
      <div class="sub">
        OSL is specifically designed to date materials whose electron traps were zeroed by daylight exposure or kiln firing prior to burial—namely <strong>(i) naturally occurring sediments</strong> (aeolian, fluvial, coastal sands) and <strong>(ii) man-made materials like pottery</strong> (fired ceramics, burnt clay). Intrusive igneous and metamorphic rocks are saturated and cannot be OSL-dated for geological age.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) (i), (ii) and (iii)</span>
      <span class="tag wrong">Incorrect (Wrongly Includes Intrusive Rocks)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option includes <em>(iii) Intrusive igneous rocks</em>. Deep-seated plutonic rocks like granite or diorite never experience daylight exposure during emplacement and crystallize over millions of years, causing their electron traps to be completely saturated with radiation.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) (i) and (ii)</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Statements (i) and (ii) are the precise, classic domains of luminescence dating. Exposure to sunlight during sedimentary transport bleaches quartz/feldspar in naturally occurring sediments (i), while the intense heat of kiln firing ($> 500^\circ\text{C}$) thermal-bleaches archaeological ceramics (ii), providing the requisite zero baseline ($t = 0$).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) (iii) and (iv)</span>
      <span class="tag wrong">Incorrect (Exclusively Contains Invalid Saturated Bedrock)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> Both intrusive igneous rocks and metasedimentary rocks possess geological ages measured in millions or billions of years (Phanerozoic, Proterozoic, Archean), far exceeding the Quaternary saturation limit ($\sim 300\text{ ka}$) of luminescence dating.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) (i) and (iii)</span>
      <span class="tag wrong">Incorrect (Omits Archaeological Pottery & Includes Intrusive Rocks)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option wrongly omits man-made pottery (which was historically the very first material dated by thermoluminescence by Martin Aitken in the 1960s) and erroneously includes intrusive igneous rocks.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison: Trapped-Charge & Quaternary Geochronology Methods</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Geochronological Method</th>
            <th>Primary Target Minerals</th>
            <th>Clock Resetting (Zeroing) Mechanism</th>
            <th>Effective Dating Range</th>
            <th>Primary Geological & Archaeological Applications</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>OSL (Optically Stimulated Luminescence)</strong></td>
            <td>Quartz ($\text{SiO}_2$), K-Feldspar</td>
            <td><strong>Daylight exposure</strong> (bleaching) or <strong>Thermal firing</strong> ($> 450^\circ\text{C}$)</td>
            <td><strong>$\sim 10\text{ years to } 300,000\text{ years}$</strong></td>
            <td>Aeolian sand dunes, loess, fluvial terraces, coastal beach ridges, pottery, bricks</td>
          </tr>
          <tr>
            <td><strong>TL (Thermoluminescence)</strong></td>
            <td>Quartz, Feldspar, Calcite, Zircon</td>
            <td><strong>Heat / Thermal firing</strong> ($> 450 - 500^\circ\text{C}$)</td>
            <td>$\sim 100\text{ to } 500,000\text{ years}$</td>
            <td>Ancient pottery, burnt flint tools, kiln slag, volcanic ash/tephra</td>
          </tr>
          <tr>
            <td><strong>ESR (Electron Spin Resonance)</strong></td>
            <td>Tooth enamel (hydroxyapatite), corals, speleothems</td>
            <td>Biomineralization (formation) or daylight bleaching in fault gouge</td>
            <td>$\sim 5,000\text{ to } 2,000,000\text{ years}$</td>
            <td>Fossil tooth enamel, marine shells, carbonate speleothems, active fault gouge</td>
          </tr>
          <tr>
            <td><strong>Radiocarbon ($^{14}\text{C}$)</strong></td>
            <td>Organic carbon (wood, charcoal, bone, shell)</td>
            <td>Death of organism (cessation of $^{14}\text{C}$ atmospheric exchange)</td>
            <td>$\sim 300\text{ to } 50,000\text{ years}$</td>
            <td>Holocene and Late Pleistocene organic remains, peat bogs, archaeological charcoal</td>
          </tr>
          <tr>
            <td><strong>Cosmogenic Radionuclides ($^{10}\text{Be}, ^{26}\text{Al}$)</strong></td>
            <td>Quartz in surface boulders</td>
            <td>Exposure to secondary cosmic rays at Earth's surface</td>
            <td>$\sim 1,000\text{ to } 4,000,000\text{ years}$</td>
            <td>Glacial moraine boulders, fault scarp exposure, bedrock erosion rates</td>
          </tr>
          <tr>
            <td><strong>Fission Track Dating</strong></td>
            <td>Apatite, Zircon, Sphene</td>
            <td>Cooling below closure temperature ($T_c \approx 110^\circ\text{C}$ for apatite)</td>
            <td>$\sim 100,000\text{ to } 10^9\text{ years}$</td>
            <td>Tectonic exhumation, orogenic cooling rates, sedimentary basin thermal history</td>
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
          <strong>Practice Q1 (Numerical Age Calculation):</strong> In an OSL laboratory, a purified quartz aliquot from an alluvial terrace in the Mahanadi Basin yields an equivalent paleodose $D_e = 64.8\text{ Gy}$ using the SAR protocol. High-resolution gamma spectrometry and in-situ dosimetry measure an annual environmental dose rate $\dot{D} = 2.40\text{ Gy/ka}$ ($2.40\text{ mGy/yr}$). Calculate the depositional age of the terrace sand.
          <div class="pq-ans">✔ Worked Answer: $27,000\text{ years}$ ($27.0\text{ ka}$; Late Pleistocene / Marine Isotope Stage 2).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\text{OSL Age} = \frac{D_e}{\dot{D}} = \frac{64.8\text{ Gy}}{2.40\text{ Gy/ka}} = 27.0\text{ ka} = 27,000\text{ years}$$
            This dates the burial of the sand during the Last Glacial Maximum (LGM) aggradation phase.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the meaning and danger of <em>partial bleaching</em> in sediment luminescence dating, and which sedimentary environment is most susceptible?
          <div class="pq-ans">✔ Correct Answer: Incomplete zeroing of electron traps prior to burial; highly prevalent in turbid, deep fluvial and subaqueous debris-flow environments.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Water absorbs the UV/blue spectrum rapidly, and turbid suspended sediment shields grains from sunlight. Unbleached residual trapped charge remains, causing the calculated OSL age to be significantly older than the true burial event (age overestimation).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What revolutionary analytical protocol, developed by A.S. Murray and A.G. Wintle in 2000, transformed OSL dating into a high-precision technique?
          <div class="pq-ans">✔ Correct Answer: The Single-Aliquot Regenerative-dose (SAR) protocol.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The SAR protocol measures the natural luminescence and multiple laboratory regeneration doses on a single aliquot, using a small test dose after each cycle to monitor and mathematically correct for luminescence sensitivity changes.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Why is Infrared Stimulated Luminescence (IRSL) specifically applied to potassium feldspar rather than quartz?
          <div class="pq-ans">✔ Correct Answer: Quartz traps cannot be evicted by low-energy infrared photons ($870\text{ nm}$), whereas K-feldspar contains an infrared resonance excitation trap with an internal dose rate from radioactive $^{40}\text{K}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> K-feldspar is sensitive to IR stimulation, allowing dating in red-light safe conditions without exciting quartz. However, feldspars suffer from <em>anomalous fading</em> (quantum mechanical tunneling of electrons), which must be corrected.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How do cosmic rays contribute to the total annual environmental dose rate ($\dot{D}$)?
          <div class="pq-ans">✔ Correct Answer: Through penetrating muons and neutrons; the cosmic dose rate decreases exponentially with burial depth below the ground surface.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> At the surface, cosmic radiation contributes $\sim 0.30\text{ mGy/yr}$. With increasing overburden depth, absorption by overlying sediment attenuates the flux, approaching a low asymptotic value beyond $10\text{ meters}$ depth.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the physical basis of <em>luminescence thermometry</em> or <em>rock surface exposure dating</em>?
          <div class="pq-ans">✔ Correct Answer: Measuring the depth-penetration profile of daylight bleaching into the outer millimeters of an exposed rock boulder surface.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sunlight penetrates several millimeters into transparent quartz grains on rock surfaces, creating a bleaching front that advances inward over time, allowing direct dating of rock-art, glacial erratic exposure, or masonry construction.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Why must OSL sediment samples be collected strictly inside opaque, light-tight tubes (e.g., black PVC or steel tubes hammered into trench walls)?
          <div class="pq-ans">✔ Correct Answer: Because any exposure to ambient daylight during excavation instantly bleaches the quartz grains, permanently destroying the trapped paleodose record.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sampling tubes are sealed light-tight in the field and opened only inside darkrooms illuminated by dim amber/red safelights.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does moisture content (interstitial pore water) affect the calculated luminescence age of a buried sand deposit?
          <div class="pq-ans">✔ Correct Answer: Water absorbs ionizing radiation more effectively than solid mineral grains, reducing the effective annual dose rate ($\dot{D}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Higher moisture levels absorb gamma and beta rays before they reach the quartz grains. If water content is underestimated, $\dot{D}$ will be overestimated, resulting in an erroneously young calculated age ($Age = D_e / \dot{D}$).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 6, part1, part2, part3)


# ==============================================================================
# Q007: Fluvial Megafans
# ==============================================================================
def generate_q007():
    title = "Q007: Fluvial Megafans vs. Alluvial Fans: Scale, Slopes & Foreland Systems | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Fluvial Sedimentology & Basin Analysis"
    h1_title = "Q007: Fluvial Megafans vs. Alluvial Fans: Scale, Slopes & Foreland Systems"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 7<br>
<strong>Authoritative References:</strong> Gohain & Parkash (1990, <em>Sedimentary Geology</em>, 68, pp. 115–132); DeCelles & Cavazza (1999, <em>Sedimentary Geology</em>, 123, pp. 181–206); Leier et al. (2005, <em>Sedimentary Geology</em>, 178, pp. 59–76); Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Ch. 8, pp. 243–248); Hartley et al. (2010, <em>J. Sedimentary Research</em>, 80)."""

    part1 = r"""
  <!-- CARD 1: MEGAFANS AS DISTRIBUTIVE FLUVIAL SYSTEMS -->
  <div class="card">
    <div class="card-header bg-blue">1. Fluvial Megafans in Orogenic Foreland Basins</div>
    <div class="card-body">
      <p>In modern process sedimentology and sedimentary basin analysis (DeCelles & Cavazza 1999; Leier et al. 2005; Weissmann et al. 2010), a <strong>Fluvial Megafan</strong> is defined as a gigantic, low-gradient fan-shaped sedimentary body deposited by a large, long-lived orogenic river issuing from a mountainous canyon mouth onto an unconfined, aggradational foreland or intracontinental basin plain.</p>

      <ul>
        <li><strong>(i) Volumetrically Significant Basin Fill:</strong> Megafans constitute the primary, volumetrically dominant sediment routing and aggradational elements of retroarc and peripheral foreland basins adjacent to rising collisional mountain chains (e.g., the Himalayan foreland basin, the Andean Chaco/Pantanal plain).</li>
        <li><strong>(ii) Mountain-to-Plain Transition:</strong> Megafan construction is mechanically triggered when a large river carrying enormous sediment discharge ($> 10^8\text{ tons/yr}$) exits the narrow, high-relief confines of an orogenic thrust belt and abruptly enters a low-relief, low-gradient alluvial plain where lateral accommodation space is unrestricted.</li>
        <li><strong>(iv) Greater Size & Lower Slope:</strong> Megafans are distinguished by their extraordinary geographic scale (radial lengths $100 - 300\text{ km}$, surface areas $> 10^4 - 10^5\text{ km}^2$) and regionally imperceptible slope gradients ($< 0.1^\circ$, or $< 1\text{ m/km}$).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q07/foreland_megafan_vs_alluvial_fan.png" alt="Foreland Megafan vs Alluvial Fan Scale">
        <div class="tb-caption">
          <strong>Figure 7.1: Quantitative Scale Disparity: Megafans vs. Alluvial Fans.</strong> Cross-sectional and planform comparison illustrating that megafans operate over hundreds of kilometers with fractional degree slopes, whereas alluvial fans are steep, localized piedmont features.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: SCIENTIFIC REFUTATION: MEGAFANS ARE NOT ALLUVIAL FANS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Morphodynamic Discrimination: Why Megafans Are NOT Alluvial Fans</div>
    <div class="card-body">
      <p>A widespread misconception among non-specialists is statement <strong>(iii) "Fluvial megafans are also known as alluvial fans."</strong> In sedimentary geology, this statement is <strong>fundamentally false</strong>. While both exhibit a semi-conical radiating planform, they represent fundamentally distinct physical regimes:</p>

      <table>
        <thead>
          <tr>
            <th>Diagnostic Parameter</th>
            <th>Classical Alluvial Fan</th>
            <th>Fluvial Megafan</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Radial Length ($R$)</strong></td>
            <td>$< 10 - 20\text{ km}$ (localized)</td>
            <td><strong>$80 - 300\text{ km}$</strong> (regional landscape scale)</td>
          </tr>
          <tr>
            <td><strong>Surface Area ($A$)</strong></td>
            <td>$< 100\text{ km}^2$ (rarely up to $200\text{ km}^2$)</td>
            <td><strong>$> 10,000 - 100,000\text{ km}^2$</strong> ($10^4 - 10^5\text{ km}^2$)</td>
          </tr>
          <tr>
            <td><strong>Surface Gradient / Slope</strong></td>
            <td>Steep: <strong>$> 1.5^\circ \text{ to } 10^\circ$</strong> ($> 25 - 100\text{ m/km}$)</td>
            <td>Extremely Gentle: <strong>$< 0.1^\circ$</strong> ($0.1 - 1.0\text{ m/km}$)</td>
          </tr>
          <tr>
            <td><strong>Dominant Transport Process</strong></td>
            <td>Episodic subaerial debris flows, sheetfloods, sieve gravels</td>
            <td><strong>Perennial, channelized fluvial flow</strong> with active meander/braided belts</td>
          </tr>
          <tr>
            <td><strong>Sedimentary Texture</strong></td>
            <td>Coarse gravels, diamictites, poorly sorted boulders</td>
            <td>Sand and silt-dominated; gravel restricted strictly to apex</td>
          </tr>
        </tbody>
      </table>

      <div class="quote-box">
        "Megafans are distinguished from alluvial fans by their vastly greater size (areas exceeding $10^4\text{ km}^2$) and lower slopes (typically less than $0.1^\circ$). Unlike alluvial fans, which are dominated by gravity-driven debris flows and sheetfloods, megafans are built by perennial fluvial channel avulsion."
        <span class="quote-ref">— M.P. Leier, P.G. DeCelles and J.D. Pelham, <em>Large-scale Sandstone Architecture of Megafans</em> (Sedimentary Geology, 2005, p. 61)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q07/boggs_fig8_2_alluvial_fan_facies.png" alt="Alluvial Fan Facies Model from Boggs">
        <div class="tb-caption">
          <strong>Figure 7.2 (Sam Boggs Jr., 5th Ed., Fig. 8.2):</strong> Classical alluvial fan depositional model showing steep gradient, proximal debris-flow boulder sheets, and localized piedmont geometry, contrasting sharply with vast foreland megafan plains.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: CLASSIC INDIAN FORELAND EXAMPLES & NODAL AVULSION -->
  <div class="card">
    <div class="card-header bg-emerald">3. World Archetypes: Kosi & Gandak Megafans of the Himalayan Foreland</div>
    <div class="card-body">
      <p>The premier global archetypes for fluvial megafans occur in northern India and Nepal along the Indo-Gangetic peripheral foreland basin:</p>
      <ul>
        <li><strong>The Kosi Megafan (Bihar/Nepal):</strong> Built by the Kosi River emerging from the Main Boundary Thrust (MBT) at Chatra gorge. Covering over $15,000\text{ km}^2$, the Kosi has migrated more than $113\text{ km}$ laterally from east to west over the past 250 years through a series of dramatic <strong>nodal avulsions</strong> at the fan apex. The famous August 2008 Kosi avulsion breached its eastern embankment, shifting the channel $> 100\text{ km}$ eastward and flooding millions of people.</li>
        <li><strong>The Gandak Megafan:</strong> Located west of the Kosi, covering $\approx 12,000\text{ km}^2$, characterized by radiating paleochannels (channels called <em>dhars</em>) that disperse fine sand, silt, and overbank mud across eastern Uttar Pradesh and Bihar.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 7)</div>
    <div class="q-stmt">
      Q7. Fluvial megafans: (i) constitute volumetrically significant depositional elements of sedimentary basins adjacent to mountain belts, (ii) are related to the emergence of a large mountain river onto a low-relief alluvial plain, (iii) are also known as alluvial fans, (iv) are distinguished by their greater size and lower slope. Choose the correct set of answer from the following options :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) (i), (ii), (iii)</div>
      <div class="raw-opt">(B) (ii), (iii), (iv)</div>
      <div class="raw-opt correct">(C) (i), (ii), (iv) &nbsp;✔</div>
      <div class="raw-opt">(D) (i), (iii), (iv)</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) (i), (ii), (iv)</div>
      <div class="sub">
        Statements <strong>(i)</strong>, <strong>(ii)</strong>, and <strong>(iv)</strong> accurately describe the volume, geographic origin, and morphometric scale of fluvial megafans. Statement <strong>(iii) is scientifically incorrect</strong> because megafans are strictly distinct from alluvial fans in terms of scale ($> 10^4\text{ km}^2$ vs $< 100\text{ km}^2$), gradient ($< 0.1^\circ$ vs $> 1.5^\circ$), and transport physics.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) (i), (ii), (iii)</span>
      <span class="tag wrong">Incorrect (Erroneously Equates Megafans to Alluvial Fans)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option includes statement (iii). Fluvial megafans are not synonymous with alluvial fans; conflating them ignores two orders of magnitude difference in area and fundamentally different fluid-dynamic transport processes.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) (ii), (iii), (iv)</span>
      <span class="tag wrong">Incorrect (Omits Volumetric Basin Significance & Includes False Synonym)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option omits statement (i)—failing to recognize that megafans comprise the principal volumetric fill of foreland basins—while retaining the erroneous statement (iii).
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) (i), (ii), (iv)</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Statements (i), (ii), and (iv) embody the exact scientific consensus defined by DeCelles & Cavazza (1999) and Leier et al. (2005). Megafans are major foreland depositional elements (i), form where large rivers exit mountain belts onto flat plains (ii), and are universally distinguished from alluvial fans by their vastly greater size ($> 10^4\text{ km}^2$) and remarkably lower slopes ($< 0.1^\circ$) (iv).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) (i), (iii), (iv)</span>
      <span class="tag wrong">Incorrect (Omits Mountain-Plain Genesis & Includes False Synonym)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option omits statement (ii) (the foundational requirement of emergence of a mountain river onto an unconfined plain) and includes the incorrect statement (iii).
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparative Matrix: Alluvial Fans vs. Fluvial Megafans vs. Deltas</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Depositional System</th>
            <th>Surface Area Scale</th>
            <th>Typical Slope Gradient</th>
            <th>Dominant Fluid/Transport Mechanics</th>
            <th>Primary Subsurface Architecture</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Classical Alluvial Fan</strong></td>
            <td>$< 100\text{ km}^2$</td>
            <td>Steep: <strong>$1.5^\circ - 10^\circ$</strong></td>
            <td>Episodic debris flows, sheetfloods, sieve deposition</td>
            <td>Matrix-supported paraconglomerates, sheet diamictites (fanglomerate)</td>
          </tr>
          <tr>
            <td><strong>Fluvial Megafan</strong></td>
            <td><strong>$> 10^4 - 10^5\text{ km}^2$</strong></td>
            <td>Very Low: <strong>$< 0.1^\circ$</strong> ($< 1\text{ m/km}$)</td>
            <td>Perennial channelized discharge, catastrophic nodal avulsions</td>
            <td>Radiating ribbon channel sandbodies enclosed in thick overbank muds</td>
          </tr>
          <tr>
            <td><strong>Alluvial Plain (Axial Valley)</strong></td>
            <td>$10^4 - 10^6\text{ km}^2$</td>
            <td>Low: $0.01^\circ - 0.05^\circ$</td>
            <td>Axial meandering or braided master trunk drainage</td>
            <td>Broad sheet sandstones, multi-story channel belts parallel to basin axis</td>
          </tr>
          <tr>
            <td><strong>Fluvial Delta</strong></td>
            <td>$10^2 - 10^5\text{ km}^2$</td>
            <td>Nearly Flat: $< 0.05^\circ$</td>
            <td>Fluvial discharge entering standing body of water (marine/lake)</td>
            <td>Classic Gilbert-type tripartite topset, foreset, and bottomset beds</td>
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
          <strong>Practice Q1:</strong> What is a <em>nodal avulsion</em>, and why does it control the morphological fan geometry of the Kosi megafan?
          <div class="pq-ans">✔ Correct Answer: An avulsion that repeatedly originates at the fixed apex (node) where the river exits bedrock confinement, swinging like a pendulum.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the mountain canyon mouth acts as a fixed spatial pivot (node), sediment aggradation within the active channel increases bed elevation above the surrounding plain, eventually forcing the river to breach its banks at the node and establish a new radial path.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> In the Distributive Fluvial System (DFS) model proposed by Weissmann et al. (2010), what is the diagnostic downstream trend in channel size and discharge?
          <div class="pq-ans">✔ Correct Answer: Channel width, depth, and discharge decrease downstream due to distributary bifurcations, infiltration, and evaporation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Unlike tributary networks where discharge and channel size increase downstream, DFS megafans distribute water away from a single apex, resulting in downstream channel narrowing and sediment fining.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the typical paleocurrent pattern measured from cross-bedding in an ancient lithified megafan succession?
          <div class="pq-ans">✔ Correct Answer: A radial, divergent fan-like paleocurrent distribution radiating outward through an arc of $60^\circ - 120^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Channel belts diverge outward from the apex point source, producing a wide radial spread in directional sedimentary structures.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Why are debris-flow deposits virtually absent on the medial and distal portions of fluvial megafans?
          <div class="pq-ans">✔ Correct Answer: Because regional slope gradients ($< 0.1^\circ$) are far too gentle to maintain the yield strength required to propagate cohesive debris flows.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Debris flows require slopes typically $> 2^\circ - 5^\circ$ to sustain movement. The extremely flat foreland gradient halts coarse sediment transport, confining transport entirely to Newtonian water flow.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Name the two largest active fluvial megafans in the South American Chaco-Pantanal foreland basin of the Andes.
          <div class="pq-ans">✔ Correct Answer: The Pilcomayo Megafan and the Taquari Megafan.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The Pilcomayo and Taquari megafans drain the Andean cordillera into the retroarc foreland, each covering over $50,000\text{ km}^2$.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> How does tectonic flexural loading of an orogenic thrust belt promote megafan preservation in the geological record?
          <div class="pq-ans">✔ Correct Answer: Supracrustal tectonic loading depresses the lithosphere, generating massive accommodation space in the adjacent foredeep trough.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Rapid flexural subsidence creates deep sedimentary accommodation, allowing megafan sand and mud successions up to kilometers thick (e.g., Siwalik Group) to be buried and preserved.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In the Miocene Siwalik Group of the sub-Himalayas, which stratigraphic formation represents the ancient megafan deposits of the paleo-Indus and paleo-Ganga drainage systems?
          <div class="pq-ans">✔ Correct Answer: The Middle Siwaliks (characterized by thick, multistory channel sandstones).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The Middle Siwalik subgroup consists of massive, sub-arkosic "salt-and-pepper" sandstones deposited by giant Himalayan megafans during peak late Miocene orogenic unroofing.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why do megafans serve as world-class regional groundwater aquifers in northern India?
          <div class="pq-ans">✔ Correct Answer: Because porous, well-sorted coarse-to-medium sand channel ribbons radiate continuously from apex recharge zones down into the agricultural plains.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The apex receives direct, high-elevation precipitation and mountain runoff, charging radiating permeable sandy paleochannels that transmit freshwater hundreds of kilometers into semi-arid plains.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 7, part1, part2, part3)


if __name__ == "__main__":
    out_q6 = os.path.join(SOLUTIONS_DIR, "Q006_OSL_Dating_Quartz_Feldspar_Pottery_Complete_Guide.html")
    with open(out_q6, "w", encoding="utf-8") as f:
        f.write(generate_q006())
    print(f"Generated Q006: {out_q6} ({os.path.getsize(out_q6)} bytes)")

    out_q7 = os.path.join(SOLUTIONS_DIR, "Q007_Fluvial_Megafans_Sedimentology_Foreland_Complete_Guide.html")
    with open(out_q7, "w", encoding="utf-8") as f:
        f.write(generate_q007())
    print(f"Generated Q007: {out_q7} ({os.path.getsize(out_q7)} bytes)")
