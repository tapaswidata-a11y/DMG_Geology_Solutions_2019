#!/usr/bin/env python3
"""
Q125 Generator: Schmidt Rebound Hammer Testing of Rock & Concrete Hardness
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q125():
    title = r"Q125: Engineering Geology: Schmidt Rebound Hammer Testing & Rock Hardness | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Engineering Geology & Rock Mechanics"
    h1_title = "Q125: Schmidt Rebound Hammer: Working Principle, Empirical Indices vs. Absolute Strength"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 125<br>
<strong>Authoritative References:</strong> Evert Hoek, <em>Practical Rock Engineering</em> (Ch. 5: Rock Mass Properties, pp. 82–84, Fig. 5.7); ISRM (International Society for Rock Mechanics), <em>Suggested Methods for the Quantitative Description of Discontinuities in Rock Masses</em> (1978); ASTM D5873 (<em>Standard Test Method for Determination of Rock Hardness by Rebound Hammer Method</em>); K.M. Bangar, <em>Principles of Engineering Geology</em> (p. 188); D.U. Deere and R.P. Miller (1966), <em>Engineering Classification and Index Properties for Intact Rock</em>."""

    part1 = r"""
  <!-- CARD 1: WORKING PRINCIPLE AND REBOUND MECHANICS -->
  <div class="card">
    <div class="card-header bg-blue">1. Working Principle, Mechanical Operation & The Nature of Rebound Value (R)</div>
    <div class="card-body">
      <p>
        The <strong>Schmidt Rebound Hammer</strong> (also known as the sclerometer or Swiss hammer) is a portable, non-destructive mechanical instrument widely employed in civil engineering and engineering geology to assess the surface hardness and estimate the compressive strength of rock faces and concrete structures (ISRM, 1978; ASTM D5873; Hoek, 2007; Bangar, p. 188).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q125/bangar_p188_schmidt_hammer_rebound_hardness.png" alt="Schmidt Rebound Hammer Testing from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 125.1 — Schmidt Hammer Rebound Testing:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 188). Describes the non-destructive rebound operation, spring-actuated hammer impact, and the empirical nature of the rebound number $R$.
        </div>
      </div>

      <h4>Mechanical Operation of the Instrument</h4>
      <p>
        The device operates on the principle of <strong>elastic collision and kinetic energy restitution</strong>:
      </p>
      <ol>
        <li>A cylindrical steel plunger protruding from the front of the housing is pressed firmly and perpendicularly against the test rock surface.</li>
        <li>This action compresses an internal heavy-duty spring connected to an internal steel hammer mass ($m$).</li>
        <li>At maximum extension, an internal latch automatically releases the hammer mass, propelling it forward with a fixed, calibrated impact energy ($E_{\text{impact}}$).</li>
        <li>The hammer strikes the shoulder of the plunger, which transmits a compressive shock pulse into the rock.</li>
        <li>A portion of the kinetic energy is dissipated through localized plastic deformation, micro-crushing of mineral grains, and acoustic radiation, while the remaining elastic strain energy causes the hammer mass to <strong>rebound</strong> backward along the guide rod.</li>
        <li>A lightweight rider slides along a graduated scale, capturing the maximum backward displacement. The reading is designated as the <strong>Rebound Number ($R$)</strong>, expressed on an arbitrary scale from $10$ to $100$.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q125/hoek_fig7_schmidt_rebound_hammer_orientation.png" alt="Schmidt Hammer Orientation Correction from Evert Hoek">
        <div class="figure-caption">
          <strong>Figure 125.2 — Influence of Testing Orientation on Rebound Value (R):</strong> Authoritative calibration chart from Evert Hoek (<em>Practical Rock Engineering</em>, Ch. 5, Fig. 5.7). Illustrates the essential correction curves required when the hammer is inclined vertically downward ($\alpha = -90^\circ$), horizontal ($\alpha = 0^\circ$), or vertically upward ($\alpha = +90^\circ$) due to gravitational forces acting on the hammer mass.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: WHY R IS AN EMPIRICAL RELATIVE INDEX, NOT AN ABSOLUTE MEASURE -->
  <div class="card">
    <div class="card-header bg-emerald">2. The Crucial Distinction: Empirical Relative Index vs. Absolute Physical Measure</div>
    <div class="card-body">
      <h4>Why Statement (C) is Technically False</h4>
      <p>
        The central misconception in non-destructive testing is assuming that the Schmidt hammer gives an "absolute" measurement of rock strength or hardness. <strong>It does not:</strong>
      </p>
      <ul>
        <li><strong>No Direct Physical Units:</strong> Rebound value $R$ is a <em>purely arbitrary, dimensionless index</em> (scaled $10 - 100$). It does not measure stress (such as $\text{MPa}$ or $\text{N/mm}^2$), nor does it correspond directly to fundamental physical hardness scales (e.g., Mohs scratch hardness, Vickers diamond pyramid hardness, or Brinell ball indentation).</li>
        <li><strong>Strictly an Empirical Proxy:</strong> The rebound value reflects the near-surface restitution coefficient of the rock. To convert $R$ into an estimated Uniaxial Compressive Strength ($\sigma_c$), one must rely on <strong>empirical statistical regression curves</strong> (e.g., the Deere-Miller chart or ISRM equations) that incorporate rock unit weight ($\gamma$):
          <div class="math-block">
            $$\log_{10} \sigma_c = 0.00088 \gamma R + 1.01 \quad (\text{Deere \& Miller, 1966})$$
          </div>
        </li>
        <li><strong>Dependence on Extraneous Testing Variables:</strong> The recorded rebound distance is drastically influenced by external environmental and geometric factors independent of intact material strength:
          <ul>
            <li><strong>Hammer Inclination ($\theta$):</strong> Gravity accelerates the hammer mass when pointing downward (yielding artificially high readings) and decelerates it when firing upward.</li>
            <li><strong>Surface Roughness & Weathering:</strong> A paper-thin weathered rind ($< 1\text{ mm}$) or surface roughness will cause micro-crushing and absorb impact energy, depressing $R$ by $30 - 50\%$ even if the underlying rock mass is exceptionally sound.</li>
            <li><strong>Specimen Rigidity / Mass:</strong> When testing loose core pieces without clamping them rigidly in a heavy steel V-block ($> 20\text{ kg}$), the specimen flexes and vibrates, dissipating energy and giving falsely low $R$ values.</li>
            <li><strong>Moisture State:</strong> Water-saturated rock surfaces yield systematically lower $R$ values than oven-dry or ambient dry surfaces.</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: HAMMER TYPES AND ISRM TESTING PROTOCOL -->
  <div class="card">
    <div class="card-header bg-indigo">3. Hammer Specifications & ISRM Standard Testing Protocols</div>
    <div class="card-body">
      <h4>Type L vs. Type N Schmidt Hammers</h4>
      <table class="table">
        <thead>
          <tr>
            <th>Specification</th>
            <th>Type L Hammer (Rock Mechanics)</th>
            <th>Type N Hammer (Concrete / Hard Rock)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Impact Energy</strong></td>
            <td><strong>$0.735\text{ N}\cdot\text{m}$ ($0.735\text{ J}$)</strong></td>
            <td><strong>$2.207\text{ N}\cdot\text{m}$ ($2.207\text{ J}$)</strong> ($3\times$ higher energy)</td>
          </tr>
          <tr>
            <td><strong>Primary Application</strong></td>
            <td>Drill cores, thin rock slabs, weak or fragile rocks (ISRM Recommended Standard).</td>
            <td>Heavy civil concrete structures, massive in-situ rock outcrops, blocky hard rock faces.</td>
          </tr>
          <tr>
            <td><strong>Specimen Damage</strong></td>
            <td>Minimal surface damage; does not shatter fragile cores.</td>
            <td>Can shatter or induce macro-cracking in drill cores of diameter $< 75\text{ mm}$.</td>
          </tr>
        </tbody>
      </table>

      <h4>ISRM Standard Data Reduction Protocol</h4>
      <p>
        To eliminate outliers caused by local mineral grains, micro-voids, or localized crushing, the ISRM mandates the following test procedure:
      </p>
      <ol>
        <li>Select a smooth, planar, unweathered rock face free from visible micro-cracks.</li>
        <li>Perform at least <strong>$20$ individual impacts</strong> separated by at least one plunger diameter ($> 30\text{ mm}$) to prevent testing pre-shattered rock.</li>
        <li>Discard the lowest $50\%$ of the recorded values (which represent local surface crushing or void collapse) and compute the <strong>mean of the upper $50\%$ (top 10 values)</strong> to establish the representative Rebound Value ($R$).</li>
      </ol>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 125</div>
      <div class="question-text">
        Find out the incorrect statement regarding Schmidt Hammer :
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> It is concrete test hammer originally designed for carrying out in-situ tests on the hardness of concrete.</li>
        <li class="option-item"><strong>(B)</strong> The instrument measures the distance of rebound of a controlled impact on a rock surface.</li>
        <li class="option-item correct"><strong>(C)</strong> The distance of rebound (R) gives an absolute measure of surface hardness or strength.</li>
        <li class="option-item"><strong>(D)</strong> Schmidt hammer rebound values have been found to correlate well with other measures of rock strength, including Young’s Modulus and Uniaxial Strength.</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (C)</strong> — Statement (C) is FALSE and therefore the correct selection! The rebound value ($R$) is strictly an <strong>empirical, non-destructive relative index</strong>, NOT an <strong>absolute measure</strong> of hardness or compressive strength.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Statement is TRUE (Hence Incorrect Choice)</div>
        <p>
          Historical Fact: The Schmidt rebound hammer was invented in 1948 by Swiss civil engineer Ernst Schmidt specifically for the non-destructive in-situ evaluation of concrete hardness and curing uniformity in civil engineering construction. It was only later adopted by geotechnical engineers and formalized by the ISRM (1978) for rock mechanics testing. Because Statement (A) is factually correct, it is not the "incorrect statement" sought by the question.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Statement is TRUE (Hence Incorrect Choice)</div>
        <p>
          Physical Operation: The core working mechanism of the Schmidt hammer relies on a spring-propelled internal mass delivering a controlled, standardized impact energy to the plunger. The rider directly measures the distance of rebound ($R$) of this mass along the guide bar. Because Statement (B) accurately describes the mechanical operating principle of the instrument, it is factually true.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (C): Statement is FALSE — Fully Verified & Correct Option</div>
        <p>
          Statement (C) claims that $R$ gives an <em>"absolute measure of surface hardness or strength."</em> This is fundamentally false:
        </p>
        <ol>
          <li>The rebound number $R$ is a unitless, arbitrary index on a scale from $10$ to $100$. It has no physical dimensions of stress ($\text{N/m}^2$, $\text{Pa}$) or standard hardness units.</li>
          <li>It provides only a <strong>relative empirical index</strong>. To estimate compressive strength ($\sigma_c$) or Young's modulus ($E$), the rebound number must be calibrated against laboratory crushing tests using empirical correlation charts (Deere-Miller, 1966; Hoek, 2007).</li>
          <li>The reading is heavily influenced by non-material factors including hammer orientation (gravity effects), specimen size/mass, and surface roughness.</li>
        </ol>
        <p>Therefore, Statement (C) is the incorrect statement and constitutes the correct answer to the question.</p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Statement is TRUE (Hence Incorrect Choice)</div>
        <p>
          Empirical Validity: Extensive peer-reviewed research across decades (Deere & Miller, 1966; ISRM, 1978; Barton & Choubey, 1977; Hoek, 2007) has proven that when properly normalized for orientation and surface roughness, rebound values correlate exceptionally well ($r > 0.85 - 0.92$) with Uniaxial Compressive Strength ($\sigma_c$), Joint Wall Compressive Strength (JCS), and tangent Young's Modulus ($E_t$). Because Statement (D) is true, it is not the target of the question.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison: Hardness and Strength Testing Methods for Rocks</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Test Method</th>
            <th>Property Measured</th>
            <th>Nature of Result</th>
            <th>Standard Units</th>
            <th>Destructive vs. Non-Destructive</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Schmidt Rebound Hammer</strong></td>
            <td>Elastic restitution of spring-driven impact</td>
            <td><strong>Empirical relative index ($R$)</strong></td>
            <td>Dimensionless ($10 - 100$)</td>
            <td>Non-destructive (reusable surface)</td>
          </tr>
          <tr>
            <td><strong>Unconfined Compressive Strength (UCS)</strong></td>
            <td>Maximum axial compressive load capacity</td>
            <td><strong>Absolute mechanical strength</strong></td>
            <td>Stress: $\text{MPa}$ or $\text{N/mm}^2$</td>
            <td>Destructive (complete core rupture)</td>
          </tr>
          <tr>
            <td><strong>Point Load Strength ($I_{s(50)}$)</strong></td>
            <td>Point-load tensile splitting resistance</td>
            <td>Empirical index calibrated to UCS</td>
            <td>Stress: $\text{MPa}$</td>
            <td>Destructive</td>
          </tr>
          <tr>
            <td><strong>Mohs Hardness Scale</strong></td>
            <td>Resistance to scratching by standard minerals</td>
            <td>Ordinal qualitative ranking</td>
            <td>Dimensionless scale ($1 - 10$)</td>
            <td>Micro-destructive (scratch)</td>
          </tr>
          <tr>
            <td><strong>Equotip (Leeb) Hardness Tester</strong></td>
            <td>Electronic velocity rebound of tungsten carbide ball</td>
            <td>Empirical dynamic hardness index ($HL$)</td>
            <td>Leeb value ($HL$)</td>
            <td>Micro-non-destructive</td>
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
        <strong>Problem 1: ISRM Trimming Protocol for Rebound Hardness</strong><br>
        A series of 20 Schmidt hammer impacts is conducted on a smooth joint surface in massive granite using a Type L hammer. The recorded rebound values ($R$) in ascending order are:
        $$32, 34, 35, 36, 38, 38, 40, 41, 42, 42, 44, 45, 45, 46, 48, 48, 50, 51, 52, 54$$
        Apply the standard ISRM data reduction protocol to determine the representative rebound hardness ($R_{\text{rep}}$) of the joint surface.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. According to ISRM (1978) protocol: Discard the lower $50\%$ of the readings (the lowest 10 values: $32$ through $42$).<br>
          2. Retain the upper $50\%$ (the highest 10 values):
          $$\text{Upper } 10 \text{ values} = \{44, 45, 45, 46, 48, 48, 50, 51, 52, 54\}$$
          3. Calculate the arithmetic mean of these 10 values:
          $$\sum = 44 + 45 + 45 + 46 + 48 + 48 + 50 + 51 + 52 + 54 = 483$$
          $$R_{\text{rep}} = \frac{483}{10} = 48.3 \approx 48$$
          The representative rebound hardness is $R = 48$.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Orientation Correction Due to Gravitational Effect</strong><br>
        A tunnel engineer tests the roof of a cavern by firing a Type L Schmidt hammer vertically upward ($\alpha = +90^\circ$). The measured rebound reading is $R_{\text{meas}} = 44$. From Hoek's calibration curves, the gravitational correction for vertically upward firing at this rebound level is $\Delta R = -6.0$. Determine: (a) the normalized horizontal rebound value ($R_{\text{norm}}$), and (b) explain why an upward-fired reading must be reduced.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Normalized horizontal rebound value:
          $$R_{\text{norm}} = R_{\text{meas}} + \Delta R = 44 + (-6.0) = 38.0$$
          2. Physical Explanation: When firing vertically upward, the hammer mass is propelled upward against gravity during impact, but during rebound, gravity pulls the mass downward in the direction of rebound travel, artificially increasing the rebound distance. Therefore, upward readings must be corrected downward to normalize to standard horizontal firing.
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Indirect UCS Estimation via Deere-Miller Empirical Equation</strong><br>
        A dolerite rock outcrop has a unit weight $\gamma = 29.0\text{ kN/m}^3$. A horizontal Schmidt hammer survey gives an average normalized rebound value of $R = 52$. Using the Deere-Miller empirical regression equation:
        $$\log_{10} \sigma_c = 0.00088 \gamma R + 1.01$$
        (where $\sigma_c$ is in $\text{MPa}$ and $\gamma$ is in $\text{kN/m}^3$), calculate the estimated Uniaxial Compressive Strength of the intact rock.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Compute the exponent argument:
          $$0.00088 \times \gamma \times R = 0.00088 \times 29.0 \times 52 = 1.32704$$
          2. Compute $\log_{10} \sigma_c$:
          $$\log_{10} \sigma_c = 1.32704 + 1.01 = 2.33704$$
          3. Calculate $\sigma_c$:
          $$\sigma_c = 10^{2.33704} \approx 217.3\text{ MPa}$$
          The rock is classified as ISRM Grade R5: Very Strong Rock.
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Joint Wall Compressive Strength (JCS) in Barton's Shear Criterion</strong><br>
        In Barton's shear strength criterion for rock discontinuities:
        $$\tau = \sigma_n \tan\left[ \text{JRC} \log_{10}\left(\frac{\text{JCS}}{\sigma_n}\right) + \phi_b \right]$$
        Schmidt hammer testing on an unweathered joint surface gives a Joint Wall Compressive Strength $\text{JCS} = 80\text{ MPa}$. The basic friction angle is $\phi_b = 30^\circ$, and Joint Roughness Coefficient is $\text{JRC} = 10$. Calculate the peak shear strength ($\tau$) under an effective normal stress of $\sigma_n = 0.8\text{ MPa}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Compute the stress ratio:
          $$\frac{\text{JCS}}{\sigma_n} = \frac{80\text{ MPa}}{0.8\text{ MPa}} = 100$$
          2. Compute $\log_{10}(100) = 2.0$:
          $$\text{Roughness angle contribution } = \text{JRC} \times \log_{10}\left(\frac{\text{JCS}}{\sigma_n}\right) = 10 \times 2.0 = 20^\circ$$
          3. Total friction angle:
          $$\phi_{\text{peak}} = 20^\circ + \phi_b = 20^\circ + 30^\circ = 50^\circ$$
          4. Compute peak shear strength $\tau$:
          $$\tau = \sigma_n \tan(50^\circ) = 0.8\text{ MPa} \times 1.19175 = 0.9534\text{ MPa} \approx 953\text{ kPa}$$
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Weathering Rind Assessment via Micro-Rebound Disparity</strong><br>
        A limestone cliff face shows signs of chemical solution weathering. Schmidt hammer testing directly on the weathered exposed rock face yields a rebound value of $R_{\text{weathered}} = 28$. After grinding away a $4\text{ mm}$ surface layer using a carborundum stone to expose fresh, unweathered limestone, the rebound value increases to $R_{\text{fresh}} = 48$. Calculate: (a) the percentage reduction in rebound hardness caused by the weathering rind, and (b) discuss the implication for rock slope stability.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Percentage reduction in rebound hardness:
          $$\Delta R (\%) = \left(\frac{R_{\text{fresh}} - R_{\text{weathered}}}{R_{\text{fresh}}}\right) \times 100\% = \left(\frac{48 - 28}{48}\right) \times 100\% = \frac{20}{48} \times 100\% = 41.67\%$$
          2. Stability Implication: The weathering rind has lost over $40\%$ of its surface stiffness, and its JCS is significantly degraded. Discontinuity asperities will crush easily under normal stresses rather than overriding them, dramatically lowering dilation and shear resistance along the slope joints.
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Estimation of Static Young's Modulus (E) from Rebound Value</strong><br>
        Using the empirical correlation proposed by Sachpazis (1990) for carbonate rocks:
        $$E_s (\text{GPa}) = 0.82 \times R - 12.5$$
        Estimate the static tangent Young's modulus of a dolomite rock formation that exhibits an average rebound value of $R = 55$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Substitute $R = 55$ into the empirical equation:
          $$E_s = 0.82 \times 55 - 12.5 = 45.1 - 12.5 = 32.6\text{ GPa}$$
          The estimated static modulus of elasticity of the dolomite is $32.6\text{ GPa}$.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Impact Energy Comparison Between Type N and Type L Hammers</strong><br>
        The standard impact energy of a Type N hammer is $E_N = 2.207\text{ J}$, while that of a Type L hammer is $E_L = 0.735\text{ J}$. (a) Calculate the ratio $E_N / E_L$. (b) Why does the ISRM specifically recommend the Type L hammer for testing rock core specimens rather than the Type N hammer?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Ratio of impact energies:
          $$\frac{E_N}{E_L} = \frac{2.207\text{ J}}{0.735\text{ J}} = 3.00$$
          The Type N hammer delivers exactly three times the kinetic impact energy of the Type L hammer.
          2. ISRM Recommendation Reason: Standard drill cores ($NX$ diameter $\approx 54\text{ mm}$) have limited volume and mass. The high kinetic impact energy of the Type N hammer ($2.207\text{ J}$) can induce micro-fracturing, internal spalling, or outright macroscopic shattering of the cylindrical core, invalidating the rebound reading. The gentler $0.735\text{ J}$ impact of the Type L hammer avoids structural destruction of intact cores while still mobilizing elastic rebound.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Influence of Moisture Condition on Rebound Values</strong><br>
        A laboratory investigation conducts Schmidt hammer tests on identical specimens of sandstone under two conditions: (1) oven-dry, and (2) water-saturated. The dry specimens yield a mean rebound of $R_{\text{dry}} = 42$, while the saturated specimens yield $R_{\text{sat}} = 31$. (a) Determine the percentage decrease in rebound hardness due to water saturation. (b) Explain the micro-mechanical mechanism responsible for this reduction.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Percentage decrease:
          $$\Delta R (\%) = \left(\frac{R_{\text{dry}} - R_{\text{sat}}}{R_{\text{dry}}}\right) \times 100\% = \left(\frac{42 - 31}{42}\right) \times 100\% = \frac{11}{42} \times 100\% = 26.19\%$$
          2. Micro-mechanical Mechanism:
          <ul>
            <li><strong>Rehbinder / Hydro-chemical Softening:</strong> Water molecules adsorb onto silicate and clay mineral surfaces at grain boundaries, reducing surface free energy and weakening intergranular cementation bonds.</li>
            <li><strong>Pore Pressure Dissipation:</strong> High-frequency dynamic impact momentarily generates transient micro-pore water pressures ($\Delta u$) in saturated pore spaces, reducing effective normal intergranular stress and facilitating plastic grain dislocation and acoustic energy damping.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=125,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q125_Schmidt_Hammer_Rebound_Testing_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q125: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q125()
