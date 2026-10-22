#!/usr/bin/env python3
"""
Q123 Generator: Void Ratio vs. Porosity Phase Relationships in Rock and Soil Mechanics
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q123():
    title = r"Q123: Engineering Geology: Void Ratio vs. Porosity Phase Relations | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Engineering Geology & Rock Mechanics"
    h1_title = "Q123: Phase Relations: Void Ratio vs. Porosity in Rock Mechanics and Geotechnics"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 123<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 10: Engineering Properties of Rocks, pp. 186–188); Karl Terzaghi, Ralph B. Peck, and Gholamreza Mesri, <em>Soil Mechanics in Engineering Practice</em> (3rd Ed., Ch. 1); ISRM Suggested Methods for Determining Water Content, Porosity, Density and Related Properties (1979); ASTM D7263."""

    part1 = r"""
  <!-- CARD 1: DEFINITIONS AND THREE-PHASE SYSTEM -->
  <div class="card">
    <div class="card-header bg-blue">1. The Three-Phase Physical System & Fundamental Volumetric Definitions</div>
    <div class="card-body">
      <p>
        In engineering geology, soil mechanics, and rock physics, geological materials (rocks and soils) are idealized as a <strong>multi-phase physical system</strong> consisting of solid mineral grains and pore spaces (voids). The pore spaces may be partially or completely filled with pore-water and air/gas.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q123/soil_mechanics_three_phase_void_ratio_porosity.png" alt="Three-Phase Volumetric Relationships of Rock and Soil">
        <div class="figure-caption">
          <strong>Figure 123.1 — Three-Phase Volumetric Diagram:</strong> Representation of a unit element of rock mass divided into solid mineral framework ($V_s$), pore water ($V_w$), and air/gas ($V_a$). Illustrates the critical boundary difference: Void ratio ($e$) is normalized against the solid volume ($V_s$), whereas Porosity ($n$) is normalized against the total composite volume ($V$).
        </div>
      </div>

      <h4>Rigorous Mathematical Definitions</h4>
      <p>
        Let the total volume of a rock specimen be $V$, which consists of the volume of solid rock mass / mineral skeleton ($V_s$) and the volume of voids / pore spaces ($V_v$):
      </p>
      <div class="math-block">
        $$V = V_s + V_v = V_s + V_w + V_a$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q123/bangar_p187_void_ratio_porosity_rock_mass.png" alt="Void Ratio and Porosity Definitions from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 123.2 — Porosity and Void Ratio Formulations:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 187). Highlighting the unambiguous distinction: <em>"The ratio of the total volume of pore spaces to the total volume of the solid rock mass is termed as void ratio ($e$)."</em>
        </div>
      </div>

      <ul>
        <li>
          <strong>Void Ratio ($e$):</strong> The ratio of the total volume of pore spaces ($V_v$) to the volume of the <strong>solid rock mass / mineral skeleton ($V_s$)</strong>:
          <div class="math-block">
            $$e = \frac{V_v}{V_s}$$
          </div>
          <em>Key Physical Feature:</em> Because $V_s$ is in the denominator, the void ratio is a true dimensionless ratio (not a percentage). It can theoretically exceed $1.0$ (e.g., $e > 1.0$ to $4.0$ in pumice, volcanic tuff, diatomite, and soft bentonitic clay).
        </li>
        <li>
          <strong>Porosity ($n$):</strong> The ratio of the total volume of pore spaces ($V_v$) to the <strong>total bulk volume of the rock specimen ($V$)</strong>:
          <div class="math-block">
            $$n = \frac{V_v}{V} = \frac{V_v}{V_s + V_v}$$
          </div>
          <em>Key Physical Feature:</em> Usually expressed as a fraction or percentage ($n \times 100\%$). Because the total volume $V$ is strictly greater than the pore volume ($V > V_v$), porosity must strictly lie in the range $0 < n < 1.0$ ($0\% < n < 100\%$).
        </li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: INTERCONVERSION & DERIVATION -->
  <div class="card">
    <div class="card-header bg-emerald">2. Algebraic Inter-Conversion & Geotechnical Equivalence</div>
    <div class="card-body">
      <h4>Derivation of the Conversion Equations</h4>
      <p>
        The relationship between void ratio ($e$) and porosity ($n$) is derived directly from the fundamental volume partition equation $V = V_s + V_v$:
      </p>
      <ol>
        <li><strong>Expressing $n$ in terms of $e$:</strong>
          Divide both numerator and denominator of the porosity definition by $V_s$:
          $$n = \frac{V_v}{V} = \frac{V_v}{V_s + V_v} = \frac{\frac{V_v}{V_s}}{\frac{V_s}{V_s} + \frac{V_v}{V_s}} = \frac{e}{1 + e}$$
        </li>
        <li><strong>Expressing $e$ in terms of $n$:</strong>
          Rearrange the equation $n(1 + e) = e \implies n + n e = e \implies n = e(1 - n)$:
          $$e = \frac{n}{1 - n}$$
        </li>
        <li><strong>Total Volume Expansion Factor ($1 + e$):</strong>
          $$\frac{V}{V_s} = \frac{V_s + V_v}{V_s} = 1 + \frac{V_v}{V_s} = 1 + e \implies V = V_s (1 + e)$$
          $$1 - n = 1 - \frac{e}{1 + e} = \frac{1}{1 + e} \implies V_s = V(1 - n)$$
        </li>
      </ol>

      <table class="table">
        <thead>
          <tr>
            <th>Characteristic</th>
            <th>Void Ratio ($e$)</th>
            <th>Porosity ($n$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mathematical Definition</strong></td>
            <td>$e = \frac{V_v}{V_s}$</td>
            <td>$n = \frac{V_v}{V} = \frac{V_v}{V_s + V_v}$</td>
          </tr>
          <tr>
            <td><strong>Normalizing Base</strong></td>
            <td>Solid mineral skeleton ($V_s$, unchanging constant under loading)</td>
            <td>Total volume ($V$, variable under compressive deformation)</td>
          </tr>
          <tr>
            <td><strong>Range of Values</strong></td>
            <td>$0 < e < \infty$ (can readily exceed $1.0$)</td>
            <td>$0 < n < 1.0$ (strictly bounded between $0\%$ and $100\%$)</td>
          </tr>
          <tr>
            <td><strong>Geotechnical Usage</strong></td>
            <td>Preferred in settlement, consolidation, and compaction calculations because $V_s$ remains constant during volume strain.</td>
            <td>Preferred in hydrogeology, groundwater flow, reservoir engineering, and geophysical logging.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 3: GEOLOGICAL TYPES OF POROSITY -->
  <div class="card">
    <div class="card-header bg-indigo">3. Geological Types of Porosity: Primary, Secondary & Effective Porosity</div>
    <div class="card-body">
      <p>
        In engineering geology and hydrogeology, not all pore spaces behave identically:
      </p>
      <ul>
        <li><strong>Primary Porosity:</strong> Pores formed during initial deposition or crystallization of the rock (e.g., intergranular pores in sandstone, vesicles in basaltic lava).</li>
        <li><strong>Secondary Porosity:</strong> Pores formed after rock consolidation due to tectonic stress, metamorphism, or chemical weathering (e.g., joints, faults, foliation partings, karst solution cavities in limestone).</li>
        <li><strong>Effective Porosity ($n_e$):</strong> The ratio of <strong>interconnected pore volume</strong> through which fluids can actively flow to the total rock volume ($n_e = V_{\text{interconnected}} / V$). Isolated vugs or microscopic dead-end pores contribute to total porosity but do not participate in fluid transmission.</li>
        <li><strong>Specific Yield ($S_y$) & Specific Retention ($S_r$):</strong> In an unconfined aquifer:
          $$n = S_y + S_r$$
          where $S_y$ is the volume of water drained by gravity per unit total volume, and $S_r$ is the volume of water held by capillary and surface tension forces against gravity.
        </li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 123</div>
      <div class="question-text">
        The ratio of the total volume of the pore spaces to the total volume of the solid rock mass is termed as :
      </div>
      <ul class="option-list">
        <li class="option-item correct"><strong>(A)</strong> Void ratio</li>
        <li class="option-item"><strong>(B)</strong> Porosity</li>
        <li class="option-item"><strong>(C)</strong> Pores ratio</li>
        <li class="option-item"><strong>(D)</strong> Effective porosity</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (A) Void ratio</strong> — By exact geotechnical definition, the ratio of the volume of pore spaces ($V_v$) to the volume of the solid rock mass ($V_s$) is designated as the Void Ratio ($e = V_v / V_s$).
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option correct">
        <div class="option-title">Option (A): Void ratio — Fully Verified & Correct</div>
        <p>
          Void ratio ($e$) is defined rigorously in soil mechanics, rock mechanics, and engineering geology textbooks (Bangar, p. 187; Terzaghi & Peck; ISRM) as the ratio of the volume of voids (pores) to the volume of solid rock mass:
          $$e = \frac{V_v}{V_s}$$
          Because the volume of solids $V_s$ does not change during mechanical compression or consolidation (assuming incompressible mineral grains), geotechnical engineers utilize void ratio as the primary state variable for compaction and settlement equations.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Porosity — Incorrect Normalization</div>
        <p>
          Porosity ($n$) is defined as the ratio of the volume of pore spaces ($V_v$) to the <strong>total volume of the rock specimen ($V = V_s + V_v$)</strong>:
          $$n = \frac{V_v}{V}$$
          The question explicitly specifies the ratio to the "total volume of the solid rock mass" ($V_s$), which is the mathematical definition of void ratio, not porosity. Confusing total volume with solid volume is a classical examination pitfall.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): Pores ratio — Fabricated Distractor</div>
        <p>
          "Pores ratio" is a completely fictitious, non-existent term fabricated as an examination distractor to mislead candidates unfamiliar with standard phase-relationship terminology.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Effective porosity — Incorrect Definition</div>
        <p>
          Effective porosity ($n_e$) is the ratio of the volume of <strong>interconnected, drainable pore spaces ($V_{vi}$)</strong> to the <strong>total volume ($V$)</strong> of the rock. It accounts only for channels that permit fluid migration, excluding isolated, closed vesicles (such as gas bubbles in pumice). Like total porosity, it is normalized to total volume $V$, not solid volume $V_s$.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Geotechnical Parameters for Rock and Soil Phases</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Parameter Name</th>
            <th>Symbol</th>
            <th>Mathematical Formula</th>
            <th>Units / Format</th>
            <th>Typical Range in Intact Rocks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Void Ratio</strong></td>
            <td>$e$</td>
            <td>$e = \frac{V_v}{V_s} = \frac{n}{1 - n}$</td>
            <td>Dimensionless decimal (e.g. $0.05$)</td>
            <td>$0.005 - 0.40$ (dense rocks); $> 1.0$ (pumice)</td>
          </tr>
          <tr>
            <td><strong>Total Porosity</strong></td>
            <td>$n$</td>
            <td>$n = \frac{V_v}{V} = \frac{e}{1 + e}$</td>
            <td>Percentage ($0 - 100\%$) or fraction</td>
            <td>$0.5\% - 30\%$ (Granite: $<1\%$; Sandstone: $10-25\%$)</td>
          </tr>
          <tr>
            <td><strong>Effective Porosity</strong></td>
            <td>$n_e$</td>
            <td>$n_e = \frac{V_{\text{interconnected}}}{V}$</td>
            <td>Percentage ($0 - 100\%$)</td>
            <td>$0.1\% - 22\%$ (always $\le n$)</td>
          </tr>
          <tr>
            <td><strong>Degree of Saturation</strong></td>
            <td>$S_r$</td>
            <td>$S_r = \frac{V_w}{V_v} = \frac{w G_s}{e}$</td>
            <td>Percentage ($0 - 100\%$)</td>
            <td>$0\%$ (oven dry) to $100\%$ (fully saturated)</td>
          </tr>
          <tr>
            <td><strong>Moisture Content</strong></td>
            <td>$w$</td>
            <td>$w = \frac{M_w}{M_s} \times 100\%$</td>
            <td>Percentage</td>
            <td>$0.1\% - 15\%$ (intact rock)</td>
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
        <strong>Problem 1: Exact Conversion from Porosity to Void Ratio</strong><br>
        A porous sandstone specimen has a laboratory measured porosity of $n = 20.0\%$ ($0.20$). Calculate its void ratio ($e$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Use the fundamental conversion formula:
          $$e = \frac{n}{1 - n}$$
          2. Substitute $n = 0.20$:
          $$e = \frac{0.20}{1 - 0.20} = \frac{0.20}{0.80} = 0.25$$
          The void ratio of the sandstone is $0.25$.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Conversion from Void Ratio to Porosity</strong><br>
        A sample of volcanic pumice has an exceptionally high void ratio of $e = 1.50$ due to abundant vesicular cavities. Calculate its porosity ($n$) expressed as a percentage.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Use the conversion formula:
          $$n = \frac{e}{1 + e}$$
          2. Substitute $e = 1.50$:
          $$n = \frac{1.50}{1 + 1.50} = \frac{1.50}{2.50} = 0.60 = 60.0\%$$
          <em>Physical Insight:</em> Even though void ratio exceeds $1.0$ ($e = 1.50$), porosity can never exceed $100\%$ ($n = 60\%$).
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Determination of $e$ and $n$ from Laboratory Masses and Volumes</strong><br>
        A cylindrical core of limestone has diameter $D = 50\text{ mm}$, length $L = 100\text{ mm}$, and an oven-dry mass of $M_s = 485.0\text{ g}$. The true grain density of the solid calcite minerals is $\rho_s = 2.71\text{ g/cm}^3$. Calculate: (a) total volume $V$, (b) volume of solids $V_s$, (c) volume of voids $V_v$, (d) porosity $n$, and (e) void ratio $e$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Total bulk volume $V$:
          $$V = \frac{\pi}{4} D^2 L = \frac{\pi}{4} (5.0\text{ cm})^2 \times (10.0\text{ cm}) = 196.35\text{ cm}^3$$
          2. Volume of solid mineral skeleton $V_s$:
          $$V_s = \frac{M_s}{\rho_s} = \frac{485.0\text{ g}}{2.71\text{ g/cm}^3} = 178.97\text{ cm}^3$$
          3. Volume of voids $V_v$:
          $$V_v = V - V_s = 196.35 - 178.97 = 17.38\text{ cm}^3$$
          4. Porosity $n$:
          $$n = \frac{V_v}{V} = \frac{17.38}{196.35} = 0.0885 = 8.85\%$$
          5. Void ratio $e$:
          $$e = \frac{V_v}{V_s} = \frac{17.38}{178.97} = 0.0971$$
          Check: $e = \frac{n}{1 - n} = \frac{0.0885}{1 - 0.0885} = \frac{0.0885}{0.9115} = 0.0971$ (Verified).
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Consolidation Settlement & Void Ratio Reduction</strong><br>
        A saturated clay-shale bed of initial thickness $H_0 = 12.0\text{ m}$ has an initial void ratio $e_0 = 0.85$. Under heavy embankment loading, the void ratio decreases to $e_1 = 0.70$. Assuming one-dimensional vertical strain and incompressible solid grains, calculate the total consolidation settlement ($\Delta H$) of the shale layer.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Use the standard settlement equation:
          $$\frac{\Delta H}{H_0} = \frac{\Delta e}{1 + e_0}$$
          2. Compute change in void ratio $\Delta e$:
          $$\Delta e = e_0 - e_1 = 0.85 - 0.70 = 0.15$$
          3. Calculate settlement $\Delta H$:
          $$\Delta H = H_0 \left(\frac{\Delta e}{1 + e_0}\right) = 12.0\text{ m} \times \left(\frac{0.15}{1 + 0.85}\right) = 12.0 \times \left(\frac{0.15}{1.85}\right) = 12.0 \times 0.08108 = 0.973\text{ m} \approx 97.3\text{ cm}$$
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Athy's Law for Compaction with Depth</strong><br>
        In a sedimentary basin, the porosity of shale decreases with depth $z$ according to Athy's compaction equation: $n(z) = n_0 e^{-c z}$, where initial surface porosity is $n_0 = 40.0\%$ and compaction coefficient is $c = 0.0004\text{ m}^{-1}$. Calculate the void ratio of the shale at a depth of $z = 1500\text{ m}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Compute porosity at $z = 1500\text{ m}$:
          $$c z = 0.0004 \times 1500 = 0.60$$
          $$n(1500) = 0.40 \times e^{-0.60} = 0.40 \times 0.54881 = 0.2195 = 21.95\%$$
          2. Compute corresponding void ratio $e$:
          $$e = \frac{n}{1 - n} = \frac{0.2195}{1 - 0.2195} = \frac{0.2195}{0.7805} = 0.281$$
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Degree of Saturation from Void Ratio and Water Content</strong><br>
        A weathered granite regolith has a void ratio $e = 0.65$, water content $w = 18.0\%$, and specific gravity of solid mineral grains $G_s = 2.68$. Calculate the degree of saturation ($S_r$) of the specimen.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Use the fundamental phase identity:
          $$S_r \cdot e = w \cdot G_s$$
          2. Solve for degree of saturation $S_r$:
          $$S_r = \frac{w \cdot G_s}{e} = \frac{0.18 \times 2.68}{0.65} = \frac{0.4824}{0.65} = 0.7422 = 74.22\%$$
          The rock pore spaces are 74.2% filled with water and 25.8% filled with air.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Effective Porosity vs. Total Porosity in Vesicular Basalt</strong><br>
        A core of vesicular basalt has a total volume $V = 200\text{ cm}^3$ and total porosity $n = 18.0\%$. In a helium pycnometer test, the volume of interconnected open pores accessible to gas is determined to be $V_{\text{connected}} = 16.0\text{ cm}^3$, while the remaining vesicles are sealed. Calculate: (a) the total pore volume $V_v$, (b) the effective porosity $n_e$, and (c) the percentage of total pore volume that is completely sealed.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Total pore volume $V_v$:
          $$V_v = n \times V = 0.18 \times 200\text{ cm}^3 = 36.0\text{ cm}^3$$
          2. Effective porosity $n_e$:
          $$n_e = \frac{V_{\text{connected}}}{V} = \frac{16.0\text{ cm}^3}{200\text{ cm}^3} = 0.080 = 8.0\%$$
          3. Sealed pore volume and percentage:
          $$V_{\text{sealed}} = V_v - V_{\text{connected}} = 36.0 - 16.0 = 20.0\text{ cm}^3$$
          $$\% \text{ Sealed} = \left(\frac{20.0}{36.0}\right) \times 100\% = 55.56\%$$
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Critical Hydraulic Gradient for Quicksand / Piping</strong><br>
        An alluvial sandy aquifer underlying a dam foundation has a specific gravity $G_s = 2.65$ and a void ratio $e = 0.65$. Calculate: (a) the critical hydraulic gradient ($i_c$) at which piping / quicksand failure occurs, and (b) re-express $i_c$ directly in terms of porosity $n$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Critical hydraulic gradient in terms of void ratio:
          $$i_c = \frac{G_s - 1}{1 + e} = \frac{2.65 - 1}{1 + 0.65} = \frac{1.65}{1.65} = 1.00$$
          2. Re-express in terms of porosity $n$:
          Since $\frac{1}{1 + e} = 1 - n$:
          $$i_c = (G_s - 1)(1 - n)$$
          Compute $n$:
          $$n = \frac{e}{1 + e} = \frac{0.65}{1.65} = 0.3939$$
          $$i_c = (2.65 - 1)(1 - 0.3939) = 1.65 \times 0.6061 = 1.00$$
          <em>Geotechnical Criterion:</em> If upward seepage head loss per unit length reaches $i_c = 1.00$, effective vertical stress reduces to zero ($\sigma' = 0$), causing fluidization of the sediment.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=123,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q123_Void_Ratio_vs_Porosity_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q123: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q123()
