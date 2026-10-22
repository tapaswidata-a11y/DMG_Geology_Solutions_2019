#!/usr/bin/env python3
"""
Q124 Generator: Bulk Density of Rocks with Natural Moisture Content
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q124():
    title = r"Q124: Engineering Geology: Bulk Density & Natural Moisture Content of Rocks | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Engineering Geology & Rock Mechanics"
    h1_title = "Q124: Bulk Density: Mass Per Unit Volume of Rock with Natural Moisture Content"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 124<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 10: Engineering Properties of Rocks, pp. 186–188); Bureau of Indian Standards (IS: 13030-1991: <em>Method of Test for Laboratory Determination of Water Content, Porosity, Density and Related Properties of Intact Rock Specimens</em>); ISRM Suggested Methods (1979); ASTM D7263."""

    part1 = r"""
  <!-- CARD 1: DEFINITIONS AND THE DENSITY SPECTRUM -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Physics & Standardization of Bulk Density</div>
    <div class="card-body">
      <p>
        In engineering geology, geotechnics, and rock mechanics, <strong>the mass per unit volume of a rock sample in its as-received state containing its natural in-situ moisture content is formally designated as its Bulk Density ($\rho_b$)</strong> (Bangar, p. 187; IS: 13030-1991; ISRM, 1979). When expressed as force per unit volume under gravity ($g = 9.81\text{ m/s}^2$), it is termed <strong>Unit Weight ($\gamma_b = \rho_b \cdot g$)</strong>.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q124/bangar_p187_bulk_density_natural_moisture.png" alt="Bulk Density Definition from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 124.1 — Bulk Density and Natural Moisture Content:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 187). Highlighting the exact codified definition: <em>"The mass per unit volume of a rock sample with natural moisture content is its bulk density."</em>
        </div>
      </div>

      <h4>The Fundamental Mass-Volume Formulation</h4>
      <p>
        Let a rock sample taken directly from drill core or quarry face have a total natural mass $M_{\text{nat}}$ consisting of dry solid mineral mass ($M_s$) and the mass of natural pore water ($M_w$), occupying a total overall bulk volume $V$ (including both solid minerals and void spaces):
      </p>
      <div class="math-block">
        $$\text{Bulk Density: } \rho_b = \frac{M_{\text{nat}}}{V} = \frac{M_s + M_w}{V}$$
        $$\text{Bulk Unit Weight: } \gamma_b = \rho_b \cdot g = \frac{W_{\text{nat}}}{V}$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q124/rock_bulk_density_moisture_content_relations.png" alt="Rock Bulk Density and Moisture Content Relations">
        <div class="figure-caption">
          <strong>Figure 124.2 — Three-Phase Density and Unit Weight Relationships:</strong> Structural diagram showing the partition of total bulk volume $V$ into solid mineral skeleton ($V_s$) and pore spaces ($V_v$), comparing dry density ($\rho_d$), bulk density with natural moisture ($\rho_b$), saturated density ($\rho_{\text{sat}}$), and submerged buoyant density ($\rho'$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: COMPARISON OF DENSITY TYPES -->
  <div class="card">
    <div class="card-header bg-emerald">2. The Spectrum of Rock Densities: Rigorous Distinctions</div>
    <div class="card-body">
      <p>
        Standard engineering testing codes (IS: 13030; ISRM; ASTM D7263) distinguish between four primary density states based on moisture conditioning:
      </p>

      <table class="table">
        <thead>
          <tr>
            <th>Density Type</th>
            <th>Symbol</th>
            <th>Mathematical Formula</th>
            <th>Moisture Conditioning State</th>
            <th>Primary Engineering Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bulk Density</strong></td>
            <td>$\rho_b$</td>
            <td>$\rho_b = \frac{M_s + M_w}{V} = \rho_d (1 + w)$</td>
            <td>As-received field core with natural in-situ moisture content ($w$).</td>
            <td>Calculation of in-situ vertical overburden stress ($\sigma_v = \gamma_b z$), dead load of rock in slopes and retaining walls.</td>
          </tr>
          <tr>
            <td><strong>Dry Density</strong></td>
            <td>$\rho_d$</td>
            <td>$\rho_d = \frac{M_s}{V} = \frac{\rho_b}{1 + w}$</td>
            <td>Specimen oven-dried at $105^\circ\text{C} \pm 3^\circ\text{C}$ to constant mass ($M_w = 0$).</td>
            <td>Baseline benchmark for compaction control, porosity calculation ($n = 1 - \rho_d / \rho_s$), and quality control.</td>
          </tr>
          <tr>
            <td><strong>Saturated Density</strong></td>
            <td>$\rho_{\text{sat}}$</td>
            <td>$\rho_{\text{sat}} = \frac{M_s + V_v \rho_w}{V}$</td>
            <td>Specimen subjected to vacuum saturation until all pore voids are 100% water-filled ($S_r = 100\%$).</td>
            <td>Submerged foundation analysis, submarine rock slope stability, reservoir rim stability.</td>
          </tr>
          <tr>
            <td><strong>Grain / True Density</strong></td>
            <td>$\rho_s$</td>
            <td>$\rho_s = \frac{M_s}{V_s}$</td>
            <td>Mass of solid minerals divided exclusively by the volume of solid grains (voids excluded).</td>
            <td>Mineralogical identification, specific gravity of grains ($G_s = \rho_s / \rho_w$), void ratio calculation.</td>
          </tr>
          <tr>
            <td><strong>Submerged (Buoyant) Density</strong></td>
            <td>$\rho'$</td>
            <td>$\rho' = \rho_{\text{sat}} - \rho_w = \left(\frac{G_s - 1}{1 + e}\right) \rho_w$</td>
            <td>Effective density below groundwater table considering Archimedes buoyant uplift.</td>
            <td>Effective stress analysis ($\sigma' = \gamma' z$), dam uplift pressure, pore water pressure stability.</td>
          </tr>
        </tbody>
      </table>

      <div class="figure-box">
        <img src="../../figures_Q124/bangar_sheet_187_bulk_density_rock_properties.png" alt="Engineering Properties of Rocks from Bangar p 187">
        <div class="figure-caption">
          <strong>Figure 124.3 — Physical Properties Table:</strong> Textbook sheet from K.M. Bangar (p. 187) displaying specific gravities, bulk densities ($\text{g/cm}^3$ and $\text{kN/m}^3$), and porosities for Granite, Dolerite, Sandstone, Shale, and Limestone.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: MEASUREMENT METHODS & FIELD SIGNIFICANCE -->
  <div class="card">
    <div class="card-header bg-indigo">3. Laboratory Determination & Practical Significance</div>
    <div class="card-body">
      <h4>Laboratory Determination Techniques (IS: 13030)</h4>
      <ul>
        <li><strong>Caliper Method (Regular Specimens):</strong> For machined cylindrical cores or cut prisms, diameter and length are measured with a precision vernier caliper or micrometer to calculate $V = \frac{\pi}{4} D^2 L$. Specimen is weighed immediately upon unsealing to determine $M_{\text{nat}}$.</li>
        <li><strong>Buoyancy / Water Displacement Method (Irregular Lumps):</strong> For irregular rock fragments, Archimedes' principle is applied. To prevent water from infiltrating the open pore spaces during submersion, the lump is briefly dipped in molten paraffin wax of known density ($\rho_{\text{wax}} \approx 0.90\text{ g/cm}^3$) to form a thin, impermeable coating before determining buoyant weight.</li>
      </ul>

      <h4>Practical Significance in Civil Engineering</h4>
      <ul>
        <li><strong>In-Situ Stress Fields:</strong> In deep tunnels and underground caverns, vertical in-situ principal stress ($\sigma_v$) is directly equal to the integrated bulk unit weight of overlying rock strata: $\sigma_v = \int_0^z \gamma_b(z) dz \approx \gamma_b z$. An accurate bulk density is required to prevent catastrophic rockbursts.</li>
        <li><strong>Dam Abutment & Gravity Dam Stability:</strong> Concrete and masonry gravity dams rely upon their own self-weight and the rock foundation's weight to resist overturning and sliding under horizontal reservoir hydrostatic thrust.</li>
        <li><strong>Haulage & Transportation Economics:</strong> In commercial quarrying and open-pit mining, bulk density dictates the payload capacity, truck fleet sizing, conveyor belt load ratings, and railway freight costs.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 124</div>
      <div class="question-text">
        The mass per unit volume of a rock sample with natural moisture content is its :
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Dry density</li>
        <li class="option-item"><strong>(B)</strong> Wet density</li>
        <li class="option-item correct"><strong>(C)</strong> Bulk density</li>
        <li class="option-item"><strong>(D)</strong> Natural density</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (C) Bulk density</strong> — By codified standard definition in engineering geology (Bangar, p. 187; IS: 13030; ISRM), the mass per unit volume of a rock sample containing its natural moisture content is designated as Bulk Density ($\rho_b$).
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Dry density — Incorrect Moisture Condition</div>
        <p>
          Dry density ($\rho_d$) is defined as the mass of <strong>oven-dried solid rock material</strong> per unit total volume:
          $$\rho_d = \frac{M_s}{V}$$
          It requires driving off all moisture by heating the specimen in an oven at $105^\circ\text{C}$ until constant weight is attained. It excludes all natural moisture ($M_w = 0$), making it incorrect for a sample containing its natural moisture content.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Wet density — Colloquial / Non-Standard Engineering Usage</div>
        <p>
          While "wet density" is occasionally used casually in informal parlance, standard Indian testing codes (IS: 13030-1991), ISRM suggested methods, and standard textbooks (Bangar, p. 187) formally codify this property as <strong>Bulk Density</strong>. Furthermore, in many geotechnical contexts, "wet density" implies an artificially soaked or saturated specimen ($\rho_{\text{sat}}$), whereas "bulk density" specifically designates the intact rock mass with its in-situ natural water content.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (C): Bulk density — Fully Verified & Codified Engineering Term</div>
        <p>
          Bulk density ($\rho_b$) is the exact verbatim definition given in K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 187, Section 10.3): <em>"The mass per unit volume of a rock sample with natural moisture content is its bulk density."</em> It incorporates both the solid mineral matrix and whatever moisture resides within the pores under ambient field conditions ($\rho_b = \frac{M_s + M_w}{V}$).
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Natural density — Non-Codified Synonym</div>
        <p>
          "Natural density" is an unstandardized, descriptive colloquialism. Professional geological and engineering standards universally adopt "bulk density" (or "in-situ bulk density"), not "natural density".
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Typical Density and Unit Weight Ranges for Major Rock Types</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Rock Type</th>
            <th>Specific Gravity of Grains ($G_s$)</th>
            <th>Bulk Density ($\rho_b$, $\text{g/cm}^3$)</th>
            <th>Bulk Unit Weight ($\gamma_b$, $\text{kN/m}^3$)</th>
            <th>Porosity ($n$, %)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Granite</strong></td>
            <td>$2.65 - 2.70$</td>
            <td>$2.60 - 2.68$</td>
            <td>$25.5 - 26.3$</td>
            <td>$0.5 - 1.5\%$</td>
          </tr>
          <tr>
            <td><strong>Basalt (Dense)</strong></td>
            <td>$2.85 - 3.05$</td>
            <td>$2.80 - 3.00$</td>
            <td>$27.5 - 29.4$</td>
            <td>$1.0 - 5.0\%$</td>
          </tr>
          <tr>
            <td><strong>Dolerite / Diabase</strong></td>
            <td>$2.90 - 3.10$</td>
            <td>$2.85 - 3.05$</td>
            <td>$28.0 - 29.9$</td>
            <td>$0.2 - 1.0\%$</td>
          </tr>
          <tr>
            <td><strong>Sandstone (Quartzose)</strong></td>
            <td>$2.65$</td>
            <td>$2.15 - 2.45$</td>
            <td>$21.1 - 24.0$</td>
            <td>$8.0 - 20.0\%$</td>
          </tr>
          <tr>
            <td><strong>Limestone (Dense)</strong></td>
            <td>$2.70 - 2.72$</td>
            <td>$2.50 - 2.68$</td>
            <td>$24.5 - 26.3$</td>
            <td>$1.0 - 8.0\%$</td>
          </tr>
          <tr>
            <td><strong>Shale (Compacted)</strong></td>
            <td>$2.65 - 2.75$</td>
            <td>$2.20 - 2.50$</td>
            <td>$21.6 - 24.5$</td>
            <td>$5.0 - 15.0\%$</td>
          </tr>
          <tr>
            <td><strong>Quartzite</strong></td>
            <td>$2.65$</td>
            <td>$2.62 - 2.65$</td>
            <td>$25.7 - 26.0$</td>
            <td>$0.1 - 1.0\%$</td>
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
        <strong>Problem 1: Bulk Density and Unit Weight from Caliper Measurements</strong><br>
        A fresh cylindrical rock core of dolerite has a diameter $D = 54.0\text{ mm}$, length $L = 108.0\text{ mm}$, and an as-received natural mass of $M_{\text{nat}} = 712.5\text{ g}$. Taking acceleration due to gravity $g = 9.81\text{ m/s}^2$, calculate: (a) the bulk density ($\rho_b$) in $\text{g/cm}^3$ and $\text{kg/m}^3$, and (b) the bulk unit weight ($\gamma_b$) in $\text{kN/m}^3$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate specimen volume $V$:
          $$V = \frac{\pi}{4} D^2 L = \frac{\pi}{4} (5.40\text{ cm})^2 \times (10.80\text{ cm}) = 247.34\text{ cm}^3$$
          2. Calculate bulk density $\rho_b$:
          $$\rho_b = \frac{M_{\text{nat}}}{V} = \frac{712.5\text{ g}}{247.34\text{ cm}^3} = 2.8806\text{ g/cm}^3 \approx 2.88\text{ g/cm}^3 = 2881\text{ kg/m}^3$$
          3. Calculate bulk unit weight $\gamma_b$:
          $$\gamma_b = \rho_b \cdot g = 2881\text{ kg/m}^3 \times 9.81\text{ m/s}^2 = 28,263\text{ N/m}^3 = 28.26\text{ kN/m}^3$$
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Relationship Between Bulk Density, Dry Density & Water Content</strong><br>
        A sandstone specimen has a bulk density of $\rho_b = 2.30\text{ g/cm}^3$ and a natural gravimetric moisture content of $w = 4.5\%$. Determine: (a) the dry density ($\rho_d$) of the rock, and (b) the mass of water contained in a $1.0\text{ m}^3$ block of this in-situ sandstone.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Dry density formula:
          $$\rho_d = \frac{\rho_b}{1 + w} = \frac{2.30\text{ g/cm}^3}{1 + 0.045} = \frac{2.30}{1.045} = 2.201\text{ g/cm}^3 = 2201\text{ kg/m}^3$$
          2. In a $1.0\text{ m}^3$ volume ($V = 1.0\text{ m}^3$):
          $$\text{Total Natural Mass } M_{\text{nat}} = \rho_b \times V = 2300\text{ kg}$$
          $$\text{Mass of Solids } M_s = \rho_d \times V = 2201\text{ kg}$$
          $$\text{Mass of Water } M_w = M_{\text{nat}} - M_s = 2300 - 2201 = 99\text{ kg} \text{ (or } 99\text{ litres)}$$
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Porosity Derivation from Dry Density and Grain Density</strong><br>
        The dry density of an arkosic sandstone is $\rho_d = 2.18\text{ g/cm}^3$. The grain density of the powdered mineral constituents is measured using a gas pycnometer to be $\rho_s = 2.65\text{ g/cm}^3$. Calculate the total porosity ($n$) and the void ratio ($e$) of the sandstone.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Relate dry density to grain density and porosity:
          $$\rho_d = \rho_s (1 - n) \implies 1 - n = \frac{\rho_d}{\rho_s}$$
          $$n = 1 - \frac{\rho_d}{\rho_s} = 1 - \frac{2.18}{2.65} = 1 - 0.8226 = 0.1774 = 17.74\%$$
          2. Compute void ratio $e$:
          $$e = \frac{n}{1 - n} = \frac{0.1774}{1 - 0.1774} = \frac{0.1774}{0.8226} = 0.2156$$
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Wax-Coated Immersion Method for Irregular Lumps</strong><br>
        To determine the bulk density of an irregular lump of porous limestone, the specimen is weighed in air ($M_1 = 340.0\text{ g}$). It is then coated with molten paraffin wax of density $\rho_{\text{wax}} = 0.90\text{ g/cm}^3$. The mass of the waxed specimen in air is $M_2 = 358.0\text{ g}$. When suspended in water ($\rho_w = 1.00\text{ g/cm}^3$), the submerged apparent mass is $M_3 = 205.0\text{ g}$. Calculate the bulk density ($\rho_b$) of the limestone.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Mass of the wax coating:
          $$M_{\text{wax}} = M_2 - M_1 = 358.0 - 340.0 = 18.0\text{ g}$$
          2. Volume of the wax coating:
          $$V_{\text{wax}} = \frac{M_{\text{wax}}}{\rho_{\text{wax}}} = \frac{18.0\text{ g}}{0.90\text{ g/cm}^3} = 20.0\text{ cm}^3$$
          3. Total volume of waxed specimen (by Archimedes' principle, loss of mass in water equals mass of displaced water):
          $$V_{\text{total}} = \frac{M_2 - M_3}{\rho_w} = \frac{358.0 - 205.0}{1.00} = 153.0\text{ cm}^3$$
          4. Volume of the bare rock specimen $V$:
          $$V = V_{\text{total}} - V_{\text{wax}} = 153.0 - 20.0 = 133.0\text{ cm}^3$$
          5. Bulk density of rock:
          $$\rho_b = \frac{M_1}{V} = \frac{340.0\text{ g}}{133.0\text{ cm}^3} = 2.556\text{ g/cm}^3 \approx 2.56\text{ g/cm}^3$$
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: In-Situ Vertical Stress Calculation Under Stratified Rock Column</strong><br>
        A deep exploratory mining shaft intersects three horizontal rock strata:
        (1) $0 - 50\text{ m}$: Weathered sandstone with bulk unit weight $\gamma_{b1} = 22.0\text{ kN/m}^3$;
        (2) $50 - 180\text{ m}$: Massive limestone with bulk unit weight $\gamma_{b2} = 26.0\text{ kN/m}^3$;
        (3) $180 - 400\text{ m}$: Dense basalt with bulk unit weight $\gamma_{b3} = 28.5\text{ kN/m}^3$.
        Calculate the total vertical overburden stress ($\sigma_v$) at the bottom of the shaft ($z = 400\text{ m}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Sum vertical stresses generated by each layer:
          $$\sigma_v = \sum \gamma_{bi} \cdot h_i$$
          $$\sigma_{v1} = 22.0\text{ kN/m}^3 \times 50\text{ m} = 1100\text{ kPa} = 1.10\text{ MPa}$$
          $$\sigma_{v2} = 26.0\text{ kN/m}^3 \times (180 - 50)\text{ m} = 26.0 \times 130 = 3380\text{ kPa} = 3.38\text{ MPa}$$
          $$\sigma_{v3} = 28.5\text{ kN/m}^3 \times (400 - 180)\text{ m} = 28.5 \times 220 = 6270\text{ kPa} = 6.27\text{ MPa}$$
          2. Total vertical stress at $400\text{ m}$:
          $$\sigma_v = 1.10 + 3.38 + 6.27 = 10.75\text{ MPa}$$
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Submerged Buoyant Unit Weight in Subsea Tunneling</strong><br>
        An undersea railway tunnel is excavated through marine basalt located below the ocean floor. The basalt has specific gravity $G_s = 2.90$ and void ratio $e = 0.05$. Assuming complete saturation ($S_r = 100\%$) by seawater of density $\rho_{\text{sw}} = 1025\text{ kg/m}^3$ ($\gamma_{\text{sw}} = 10.05\text{ kN/m}^3$), determine: (a) the saturated unit weight ($\gamma_{\text{sat}}$), and (b) the effective buoyant submerged unit weight ($\gamma'$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Saturated unit weight $\gamma_{\text{sat}}$:
          $$\gamma_{\text{sat}} = \left(\frac{G_s + e}{1 + e}\right) \gamma_w = \left(\frac{2.90 + 0.05}{1 + 0.05}\right) \times 9.81 = \left(\frac{2.95}{1.05}\right) \times 9.81 = 2.8095 \times 9.81 = 27.56\text{ kN/m}^3$$
          2. Effective submerged unit weight in seawater $\gamma'$:
          $$\gamma' = \gamma_{\text{sat}} - \gamma_{\text{sw}} = 27.56 - 10.05 = 17.51\text{ kN/m}^3$$
          <em>Geotechnical Implication:</em> Submergence reduces the effective confining body weight of the rock mass by $36.5\%$, significantly reducing sliding friction along inclined joint planes.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Water Absorption by Mass and Saturated Density</strong><br>
        A limestone block has an oven-dry mass $M_{\text{dry}} = 500.0\text{ g}$ and a bulk volume $V = 200.0\text{ cm}^3$. After 48 hours of immersion under water, its saturated surface-dry mass increases to $M_{\text{sat}} = 515.0\text{ g}$. Calculate: (a) dry density ($\rho_d$), (b) water absorption by mass ($A_w \%$), (c) saturated density ($\rho_{\text{sat}}$), and (d) apparent porosity ($n_a$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Dry density:
          $$\rho_d = \frac{M_{\text{dry}}}{V} = \frac{500.0\text{ g}}{200.0\text{ cm}^3} = 2.50\text{ g/cm}^3$$
          2. Water absorption by mass:
          $$A_w = \frac{M_{\text{sat}} - M_{\text{dry}}}{M_{\text{dry}}} \times 100\% = \frac{515.0 - 500.0}{500.0} \times 100\% = \frac{15.0}{500.0} \times 100\% = 3.0\%$$
          3. Saturated density:
          $$\rho_{\text{sat}} = \frac{M_{\text{sat}}}{V} = \frac{515.0\text{ g}}{200.0\text{ cm}^3} = 2.575\text{ g/cm}^3$$
          4. Apparent porosity:
          $$n_a = \frac{V_w}{V} = \frac{15.0\text{ cm}^3}{200.0\text{ cm}^3} = 0.075 = 7.5\%$$
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Commercial Quarry Dimension Stone Haulage Tonnage</strong><br>
        A dimension stone quarry extracts granite blocks measuring $2.5\text{ m} \times 1.5\text{ m} \times 1.2\text{ m}$. The granite has a laboratory bulk density of $\rho_b = 2.65\text{ tonnes/m}^3$. If a highway transport trailer has a maximum legal payload limit of $32.0\text{ tonnes}$, determine: (a) the tonnage of a single block, and (b) whether the trailer can legally carry two blocks in a single shipment.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Volume of one block:
          $$V = 2.5\text{ m} \times 1.5\text{ m} \times 1.2\text{ m} = 4.50\text{ m}^3$$
          2. Mass of one block:
          $$M_1 = V \times \rho_b = 4.50\text{ m}^3 \times 2.65\text{ tonnes/m}^3 = 11.925\text{ tonnes}$$
          3. Check two blocks:
          $$M_2 = 2 \times 11.925 = 23.85\text{ tonnes}$$
          $$\text{Since } 23.85\text{ tonnes} < 32.0\text{ tonnes}, \text{ the trailer can legally haul two blocks with } 8.15\text{ tonnes reserve capacity.}$$
          (Three blocks would weigh $35.775\text{ tonnes}$, exceeding the legal payload limit).
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=124,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q124_Bulk_Density_Natural_Moisture_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q124: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q124()
