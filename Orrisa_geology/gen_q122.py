#!/usr/bin/env python3
"""
Q122 Generator: Transverse Strength (Modulus of Rupture) & Bending Resistance of Stones
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q122():
    title = r"Q122: Engineering Geology: Transverse Strength & Bending Capacity of Stones | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Engineering Geology & Rock Mechanics"
    h1_title = "Q122: Transverse Strength (Modulus of Rupture): Capacity of Building Stones to Withstand Bending Loads"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 122<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 10: Engineering Properties of Rocks, pp. 186–188); Bureau of Indian Standards (IS: 9143-1979: <em>Method for Determination of Permissible Stress in Stone Masonry</em>); ASTM C99 (<em>Standard Test Method for Modulus of Rupture of Dimension Stone</em>); ASTM C880 (<em>Standard Test Method for Flexural Strength of Dimension Stone</em>); Timoshenko & Gere, <em>Mechanics of Materials</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND BEAM BENDING MECHANICS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Mechanics & Terminology of Transverse Strength</div>
    <div class="card-body">
      <p>
        In engineering geology, structural stone design, and rock mechanics, the <strong>capacity of a stone beam or slab to withstand bending / flexural loads without rupture is formally designated as its Transverse Strength</strong> (Bangar, p. 187; IS: 9143; ASTM C99). In structural mechanics, it is widely referred to as the <strong>Modulus of Rupture ($R$ or $\sigma_b$)</strong> or <strong>Flexural Strength</strong>.
      </p>
      <p>
        When a prismatic stone block is supported at its ends and subjected to a transverse load acting perpendicular to its longitudinal axis, it experiences internal bending moments. The stone acts as a structural beam, generating a coupled stress state:
      </p>
      <ul>
        <li><strong>Upper Fibers:</strong> Subjected to longitudinal <strong>compressive stress</strong>.</li>
        <li><strong>Neutral Axis:</strong> Experiences zero bending normal stress.</li>
        <li><strong>Lower Fibers:</strong> Subjected to maximum longitudinal <strong>tensile stress</strong> ($\sigma_t$).</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q122/three_point_bending_modulus_rupture.png" alt="Three-Point Bending Test and Modulus of Rupture Mechanics">
        <div class="figure-caption">
          <strong>Figure 122.1 — Three-Point Bending Test Configuration & Stress Distribution:</strong> Prismatic stone beam of length $L$, breadth $b$, and depth $d$ under central concentrated load $W$. Illustrates the triangular bending stress distribution: maximum compression at the top surface, zero stress at the neutral axis, and maximum tension at the bottom surface triggering tensile fracture.
        </div>
      </div>

      <h4>Why Transverse Failure is Governed by Tensile Weakness</h4>
      <p>
        Intact rocks are exceptionally strong in compression but inherently flawed and weak in tension ($\sigma_t \approx \frac{1}{10} \text{ to } \frac{1}{20} \sigma_c$). Consequently, when a stone beam is bent, failure is <strong>never caused by compressive crushing of the top surface</strong>; instead, failure initiates suddenly and catastrophically by <strong>tensile fracture of the outermost bottom fibers</strong> where tensile stress exceeds the tensile strength of the rock material.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q122/bangar_p187_transverse_bending_strength.png" alt="Transverse Strength of Building Stones from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 122.2 — Transverse Strength and Modulus of Rupture:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 187). Explains the definition: <em>"The capacity of a stone to withstand bending loads is termed as its transverse strength."</em> Details the three-point loading formula and testing protocol for stone lintels and slabs.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MATHEMATICAL DERIVATION & TESTING STANDARDS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Mathematical Formulation: Derivation of the Modulus of Rupture Formula</div>
    <div class="card-body">
      <h4>Derivation from Classical Beam Flexure Theory</h4>
      <p>
        According to the Navier-Bernoulli Euler beam bending equation:
      </p>
      <div class="math-block">
        $$\frac{M}{I} = \frac{\sigma}{y} = \frac{E}{\rho}$$
        $$\implies \sigma = \frac{M y}{I}$$
      </div>
      <p>
        Consider a prismatic rectangular stone bar of span length $L$ between knife-edge supports, width (breadth) $b$, and depth (thickness) $d$, loaded centrally with a single concentrated load $W$:
      </p>
      <ol>
        <li><strong>Maximum Bending Moment ($M_{\text{max}}$):</strong> For a simply supported beam with a central point load $W$:
          $$M_{\text{max}} = \frac{W L}{4}$$
        </li>
        <li><strong>Section Modulus ($Z$):</strong> The moment of inertia of a rectangular cross-section about the neutral axis is $I = \frac{b d^3}{12}$, and the distance to the outermost fiber is $y_{\text{max}} = \frac{d}{2}$:
          $$Z = \frac{I}{y_{\text{max}}} = \frac{\frac{b d^3}{12}}{\frac{d}{2}} = \frac{b d^2}{6}$$
        </li>
        <li><strong>Modulus of Rupture / Transverse Strength ($R$):</strong>
          $$R = \frac{M_{\text{max}}}{Z} = \frac{\frac{W L}{4}}{\frac{b d^2}{6}} = \frac{3 W L}{2 b d^2}$$
        </li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q122/bangar_sheet_187_transverse_bending_strength.png" alt="Engineering Properties of Stones from Bangar p 187">
        <div class="figure-caption">
          <strong>Figure 122.3 — Engineering Mechanical Properties Table:</strong> Textbook sheet from K.M. Bangar (p. 187) displaying comparative values of crushing compressive strength, transverse strength, and shear strength for standard Indian building stones.
        </div>
      </div>

      <h4>Standard Testing Specifications (IS: 9143 & ASTM C99)</h4>
      <ul>
        <li><strong>IS: 9143 Protocol:</strong> Test specimens are prepared as rectangular prisms of dimensions $200\text{ mm} \times 50\text{ mm} \times 50\text{ mm}$ supported over a span of $L = 150\text{ mm}$ on rounded steel rollers. Load is applied at the center until fracture occurs.</li>
        <li><strong>ASTM C99 (Three-Point Loading):</strong> Specimen size $100\text{ mm} \times 200\text{ mm} \times 57\text{ mm}$ over a span of $178\text{ mm}$.</li>
        <li><strong>ASTM C880 (Four-Point / Third-Point Loading):</strong> Two equal loads applied at one-third points of the span ($L/3$), producing a pure bending moment with zero shear stress across the middle third.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: PRACTICAL CIVIL ENGINEERING APPLICATIONS -->
  <div class="card">
    <div class="card-header bg-indigo">3. Civil Engineering Applications & Structural Significance</div>
    <div class="card-body">
      <p>
        Evaluating the transverse strength of stones is crucial whenever structural elements are subjected to flexure or lateral bending rather than direct coaxial compression:
      </p>
      <ul>
        <li><strong>Stone Lintels & Beams:</strong> Stone blocks bridging doorway and window openings in load-bearing masonry walls act as simply supported beams carrying the dead weight of masonry above. If the stone lacks adequate transverse strength, tensile cracking develops at the lower center face, causing sudden collapse.</li>
        <li><strong>Pavement Slabs & Flagstones:</strong> Paving stones, platform flooring, and pedestrian walkways supported on uneven sub-bases experience heavy wheel or point loads that induce intense flexural stresses. Sandstone and slate flags require high transverse strength.</li>
        <li><strong>Roof Slates & Cantilevered Corbels:</strong> Thin roofing slates spanning battens and cantilevered balcony corbels projecting from historical stone buildings rely entirely on transverse strength to prevent shear-bending snap.</li>
        <li><strong>Underground Mine Roof Strata:</strong> In underground coal and metal mines, immediate roof beds spanning between pillars or roadway supports behave as clamped or simply supported rock beams under gravity and overburden pressure. Flexural tensile failure triggers massive roof falls.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 122</div>
      <div class="question-text">
        Capacity of a stone to withstand bending loads is termed as :
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Bending strength</li>
        <li class="option-item"><strong>(B)</strong> Shear strength</li>
        <li class="option-item correct"><strong>(C)</strong> Transverse strength</li>
        <li class="option-item"><strong>(D)</strong> Lateral strength</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (C) Transverse strength</strong> — In engineering geology, Indian Standard specifications (IS: 9143), and standard textbooks (Bangar, p. 187), the capacity of a stone to resist bending loads is formally designated as Transverse Strength (Modulus of Rupture).
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Bending strength — Partially Descriptive but Non-Standard Terminology</div>
        <p>
          While "bending strength" is a descriptive vernacular phrase describing the physical phenomenon of flexure, it is <strong>not the formal engineering term</strong> codified in engineering geology textbooks (Bangar, p. 187) or standard Indian testing codes (IS: 9143). Standard specifications explicitly designate this index property as <strong>Transverse Strength</strong> (or Modulus of Rupture). In professional geotechnical exams, standard codified nomenclature takes strict precedence over colloquial synonyms.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Shear strength — Incorrect Mechanics</div>
        <p>
          Shear strength is the capacity of a rock or soil to resist sliding and shear failure along an internal rupture plane under shear stresses ($\tau$). It is governed by the Mohr-Coulomb criterion: $\tau_f = c + \sigma_n \tan\phi$, where $c$ is cohesion and $\phi$ is angle of internal friction. Shear strength measures resistance against parallel shearing forces, not flexural bending moments.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (C): Transverse strength — Fully Verified & Correct</div>
        <p>
          Transverse strength is the textbook engineering definition (Bangar, p. 187, Section 10.3): <em>"The capacity of a stone to withstand bending loads is termed as its transverse strength."</em> It is measured by applying a transverse load perpendicular to the axis of a beam supported at both ends until tensile rupture occurs in the outermost fibers ($R = \frac{3 W L}{2 b d^2}$).
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Lateral strength — Incorrect Concept</div>
        <p>
          "Lateral strength" refers to the resistance of a vertical structural element (such as a retaining wall, foundation pile, or masonry pier) against horizontal/lateral loads (e.g., wind pressure, seismic inertia, or lateral earth pressure). It has no relation to the flexural capacity of a stone specimen under beam bending.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Matrix: Strength Properties of Common Indian Building Stones</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Stone Type</th>
            <th>Crushing Strength (UCS, MPa)</th>
            <th>Transverse Strength ($R$, MPa)</th>
            <th>Tensile Strength ($\sigma_t$, MPa)</th>
            <th>Ratio ($R / \text{UCS}$)</th>
            <th>Structural Suitability</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Granite</strong></td>
            <td>$100 - 250$</td>
            <td>$12 - 25$</td>
            <td>$7 - 15$</td>
            <td>$\approx 0.10$</td>
            <td>Heavy pillars, monumental lintels, high-load pier caps.</td>
          </tr>
          <tr>
            <td><strong>Basalt</strong></td>
            <td>$150 - 300$</td>
            <td>$15 - 30$</td>
            <td>$8 - 18$</td>
            <td>$\approx 0.10$</td>
            <td>Pavement blocks, foundation rubble, road ballast.</td>
          </tr>
          <tr>
            <td><strong>Sandstone (Quartzose)</strong></td>
            <td>$40 - 100$</td>
            <td>$6 - 15$</td>
            <td>$3 - 8$</td>
            <td>$\approx 0.15$</td>
            <td>Architectural lintels, ashlar masonry, flooring flags.</td>
          </tr>
          <tr>
            <td><strong>Limestone (Dense)</strong></td>
            <td>$50 - 120$</td>
            <td>$7 - 16$</td>
            <td>$4 - 9$</td>
            <td>$\approx 0.13$</td>
            <td>Window sills, flooring slabs, masonry facings.</td>
          </tr>
          <tr>
            <td><strong>Quartzite</strong></td>
            <td>$150 - 300$</td>
            <td>$15 - 28$</td>
            <td>$10 - 20$</td>
            <td>$\approx 0.10$</td>
            <td>Extremely durable aggregate, high-wear paving, retaining walls.</td>
          </tr>
          <tr>
            <td><strong>Slate</strong></td>
            <td>$60 - 150$</td>
            <td>$20 - 45$ (along cleavage)</td>
            <td>$5 - 12$</td>
            <td>$\approx 0.25$</td>
            <td>Roofing tiles, damp-proof courses, electrical switchboards.</td>
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
        <strong>Problem 1: Transverse Strength (Modulus of Rupture) Calculation</strong><br>
        In an IS: 9143 standard transverse strength test, a sandstone prism of width $b = 50\text{ mm}$ and depth $d = 50\text{ mm}$ is placed on knife-edge supports spaced $L = 150\text{ mm}$ apart. A central transverse load is applied until the specimen fractures at $W = 6.25\text{ kN}$. Calculate the transverse strength (Modulus of Rupture, $R$) in $\text{MPa}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Apply the 3-point bending formula:
          $$R = \frac{3 W L}{2 b d^2}$$
          2. Substitute given values ($W = 6250\text{ N}, L = 150\text{ mm}, b = 50\text{ mm}, d = 50\text{ mm}$):
          $$R = \frac{3 \times 6250 \times 150}{2 \times 50 \times (50)^2} = \frac{2,812,500}{2 \times 50 \times 2500} = \frac{2,812,500}{250,000} = 11.25\text{ N/mm}^2 = 11.25\text{ MPa}$$
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Stone Lintel Safe Load Capacity</strong><br>
        A granite lintel is used to span an open doorway of clear span $L = 1.8\text{ m}$. The lintel has width $b = 250\text{ mm}$ and depth $d = 200\text{ mm}$. If the transverse strength of the granite is $R = 15\text{ MPa}$ and a safety factor of $\text{FoS} = 5.0$ is required, calculate the maximum safe central point load $W_{\text{safe}}$ that can be placed on the lintel (neglecting lintel self-weight).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Allowable bending stress $\sigma_{\text{allow}}$:
          $$\sigma_{\text{allow}} = \frac{R}{\text{FoS}} = \frac{15\text{ MPa}}{5.0} = 3.0\text{ MPa} = 3.0\text{ N/mm}^2$$
          2. Section modulus $Z$:
          $$Z = \frac{b d^2}{6} = \frac{250 \times (200)^2}{6} = \frac{250 \times 40,000}{6} = \frac{10,000,000}{6} = 1,666,667\text{ mm}^3$$
          3. Maximum allowable bending moment $M_{\text{allow}}$:
          $$M_{\text{allow}} = \sigma_{\text{allow}} \times Z = 3.0\text{ N/mm}^2 \times 1,666,667\text{ mm}^3 = 5,000,000\text{ N}\cdot\text{mm} = 5.0\text{ kN}\cdot\text{m}$$
          4. For a simply supported central point load, $M_{\text{max}} = \frac{W L}{4}$:
          $$\frac{W_{\text{safe}} \times 1.8\text{ m}}{4} = 5.0\text{ kN}\cdot\text{m} \implies W_{\text{safe}} = \frac{4 \times 5.0}{1.8} = \frac{20.0}{1.8} = 11.11\text{ kN}$$
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Minimum Lintel Depth Calculation</strong><br>
        A sandstone lintel must span a window opening of span $L = 2.0\text{ m}$ and support a total uniformly distributed load (UDL) of $w = 8\text{ kN/m}$. The lintel width is fixed at $b = 300\text{ mm}$. If the allowable flexural tensile stress of the sandstone is $\sigma_{\text{allow}} = 2.5\text{ MPa}$, calculate the minimum required depth $d$ of the lintel.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Maximum bending moment for a simply supported beam with UDL:
          $$M_{\text{max}} = \frac{w L^2}{8} = \frac{8\text{ kN/m} \times (2.0\text{ m})^2}{8} = \frac{32}{8} = 4.0\text{ kN}\cdot\text{m} = 4.0 \times 10^6\text{ N}\cdot\text{mm}$$
          2. Equate to flexural capacity:
          $$\sigma_{\text{allow}} = \frac{M_{\text{max}}}{Z} \implies Z_{\text{req}} = \frac{M_{\text{max}}}{\sigma_{\text{allow}}} = \frac{4.0 \times 10^6\text{ N}\cdot\text{mm}}{2.5\text{ N/mm}^2} = 1.6 \times 10^6\text{ mm}^3$$
          3. Solve for required depth $d$ ($Z = \frac{b d^2}{6}$):
          $$\frac{300 \times d^2}{6} = 1.6 \times 10^6 \implies 50 d^2 = 1,600,000 \implies d^2 = 32,000$$
          $$d = \sqrt{32,000} \approx 178.89\text{ mm} \approx 180\text{ mm}$$
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Three-Point vs. Four-Point (Third-Point) Bending Comparison</strong><br>
        A basalt prism of dimensions $60\text{ mm} \times 60\text{ mm} \times 300\text{ mm}$ is tested over span $L = 240\text{ mm}$. Under three-point loading, a center load of $W_3 = 9.0\text{ kN}$ produces failure. Under four-point loading (loads applied at third points, $L/3 = 80\text{ mm}$ from each support), the total load at failure is $W_4 = 11.25\text{ kN}$. Compare the calculated Modulus of Rupture for both configurations.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Three-point loading Modulus of Rupture ($R_3$):
          $$R_3 = \frac{3 W_3 L}{2 b d^2} = \frac{3 \times 9000 \times 240}{2 \times 60 \times (60)^2} = \frac{6,480,000}{432,000} = 15.0\text{ MPa}$$
          2. Four-point loading Modulus of Rupture ($R_4$):
          For third-point loading with two loads $W_4 / 2$ at distance $a = L/3$, $M_{\text{max}} = \frac{W_4}{2} \times \frac{L}{3} = \frac{W_4 L}{6}$:
          $$R_4 = \frac{M_{\text{max}}}{Z} = \frac{\frac{W_4 L}{6}}{\frac{b d^2}{6}} = \frac{W_4 L}{b d^2}$$
          Substitute values:
          $$R_4 = \frac{11,250 \times 240}{60 \times (60)^2} = \frac{2,700,000}{216,000} = 12.5\text{ MPa}$$
          <em>Insight:</em> Four-point testing stresses the entire middle third volume, encountering a higher probability of critical flaws, and thus yields a slightly lower, more conservative strength ($12.5\text{ MPa}$ vs $15.0\text{ MPa}$).
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Flagstone Paving Breaking Under Wheel Point Load</strong><br>
        A pedestrian plaza is paved with square sandstone flagstones of size $600\text{ mm} \times 600\text{ mm}$ and thickness $t = 40\text{ mm}$. During maintenance, a utility vehicle wheel delivers a concentrated wheel load of $P = 3.5\text{ kN}$ at the center of a flagstone that is bridge-supported on two edge sleepers spaced $L = 500\text{ mm}$ apart. If the transverse strength of the sandstone is $R = 8.0\text{ MPa}$, determine whether the flagstone will crack.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Effective beam width $b = 600\text{ mm}$, thickness $d = 40\text{ mm}$, span $L = 500\text{ mm}$:
          $$Z = \frac{b d^2}{6} = \frac{600 \times (40)^2}{6} = \frac{600 \times 1600}{6} = 160,000\text{ mm}^3$$
          2. Bending moment under wheel load:
          $$M_{\text{max}} = \frac{P L}{4} = \frac{3500\text{ N} \times 500\text{ mm}}{4} = 437,500\text{ N}\cdot\text{mm}$$
          3. Induced tensile bending stress $\sigma_b$:
          $$\sigma_b = \frac{M_{\text{max}}}{Z} = \frac{437,500}{160,000} = 2.734\text{ MPa}$$
          4. Check against transverse strength:
          $$\text{Since } \sigma_b = 2.734\text{ MPa} < R = 8.0\text{ MPa}, \quad \text{Factor of Safety } = \frac{8.0}{2.734} = 2.93$$
          The flagstone will safely support the wheel load without cracking.
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Mine Roof Strata Bending as Clamped Rock Beam</strong><br>
        An immediate sandstone roof stratum of thickness $h = 0.8\text{ m}$ spans across a mine roadway of width $B = 4.5\text{ m}$. The rock unit weight is $\gamma = 25\text{ kN/m}^3$. Assuming the roof stratum behaves as a fixed-ended (clamped) beam bending under its own self-weight ($w = \gamma \times h \times 1.0\text{ m}$ per unit advance), calculate: (a) the maximum bending moment at the supports, and (b) the maximum tensile stress induced.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Self-weight per unit length of $1\text{ m}$ wide strip:
          $$w = \gamma \times h \times 1.0 = 25\text{ kN/m}^3 \times 0.8\text{ m} \times 1.0\text{ m} = 20\text{ kN/m} = 20\text{ N/mm}$$
          2. Maximum bending moment for a fixed-ended beam occurs at the abutments:
          $$M_{\text{abutment}} = \frac{w B^2}{12} = \frac{20\text{ kN/m} \times (4.5\text{ m})^2}{12} = \frac{20 \times 20.25}{12} = 33.75\text{ kN}\cdot\text{m} = 33.75 \times 10^6\text{ N}\cdot\text{mm}$$
          3. Section modulus of $1\text{ m}$ ($1000\text{ mm}$) wide beam of depth $h = 800\text{ mm}$:
          $$Z = \frac{b h^2}{6} = \frac{1000 \times (800)^2}{6} = \frac{6.4 \times 10^8}{6} = 1.0667 \times 10^8\text{ mm}^3$$
          4. Maximum tensile stress $\sigma_t$:
          $$\sigma_t = \frac{M}{Z} = \frac{33.75 \times 10^6\text{ N}\cdot\text{mm}}{1.0667 \times 10^8\text{ mm}^3} = 0.316\text{ MPa}$$
          <em>Mining Note:</em> If horizontal tectonic stresses or delamination occurs, tensile bending stress can easily exceed the weak tensile strength of bedding planes ($< 0.5\text{ MPa}$), causing bed separation and roof collapse.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Anisotropy Effect on Transverse Strength in Slate</strong><br>
        A metamorphic slate specimen is tested for transverse strength in two orientations: (1) with cleavage planes oriented parallel to the beam length and perpendicular to load (maximum flexural resistance), and (2) with cleavage planes oriented parallel to the load direction. If the measured transverse strength in orientation (1) is $R_1 = 36\text{ MPa}$ and in orientation (2) is $R_2 = 12\text{ MPa}$, calculate the "Anisotropy Ratio of Transverse Strength" ($I_A$) and explain the geological cause.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate Anisotropy Ratio:
          $$I_A = \frac{R_{\text{max}}}{R_{\text{min}}} = \frac{R_1}{R_2} = \frac{36\text{ MPa}}{12\text{ MPa}} = 3.0$$
          2. Geological Cause: Slate possesses strong planar preferred orientation of sheet silicates (muscovite, illite, chlorite). In orientation (2), the tensile stresses acting perpendicular to cleavage readily split the weakly bonded silicate sheets apart, resulting in a three-fold drop in flexural resistance.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Relationship between Modulus of Rupture and Direct Tensile Strength</strong><br>
        Laboratory tests on an intact limestone show a direct uniaxial tensile strength (via pull-test) of $\sigma_t = 6.0\text{ MPa}$. When tested under three-point bending, the measured Modulus of Rupture is $R = 10.8\text{ MPa}$. (a) Calculate the ratio $R / \sigma_t$. (b) Explain the two primary mechanical reasons why the Modulus of Rupture is consistently higher than direct uniaxial tensile strength in brittle rocks.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Ratio:
          $$\frac{R}{\sigma_t} = \frac{10.8}{6.0} = 1.80$$
          2. Mechanical Reasons:
          <ul>
            <li><strong>Stress Gradient Effect:</strong> In a direct tensile test, the entire cross-section of the specimen is under uniform maximum tensile stress, so failure is initiated by the single worst microscopic flaw in the entire volume. In bending, only a minute skin of rock at the extreme outermost bottom fiber reaches maximum tension, dramatically reducing the statistical probability of a critical flaw coinciding with peak stress.</li>
            <li><strong>Non-Linear Inelastic Stress Distribution:</strong> Classical beam theory assumes linear elastic stress-strain behavior up to rupture. In reality, rock exhibits microcracking and stress-redistribution (plasticity/yielding) near failure at the outer fibers, shifting the neutral axis and making the true maximum fiber stress lower than that calculated by elastic formulas ($R = 1.5 - 2.0 \times \sigma_t$).</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=122,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q122_Transverse_Strength_Bending_Loads_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q122: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q122()
