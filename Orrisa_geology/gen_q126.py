#!/usr/bin/env python3
"""
Q126 Generator: Brazilian Test for Indirect Tensile Strength of Rock Specimens
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q126():
    title = r"Q126: Engineering Geology: Brazilian Test for Tensile Strength | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Engineering Geology & Rock Mechanics"
    h1_title = "Q126: The Brazilian Test: Determining Tensile Strength of Rocks via Diametral Compression"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 126<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 10: Engineering Properties of Rocks, pp. 186–188); ISRM Suggested Methods for Determining Tensile Strength of Rock Materials (Part 2: Indirect Tensile Strength by the Brazilian Method, 1978); ASTM D3967 (<em>Standard Test Method for Splitting Tensile Strength of Intact Rock Core Specimens</em>); Jaeger, Cook & Zimmerman, <em>Fundamentals of Rock Mechanics</em> (4th Ed., Ch. 6)."""

    part1 = r"""
  <!-- CARD 1: WORKING PRINCIPLE AND DERIVATION -->
  <div class="card">
    <div class="card-header bg-blue">1. Working Principle, Elastic Mechanics & Derivation of the Brazilian Formula</div>
    <div class="card-body">
      <p>
        In engineering geology and experimental rock mechanics, <strong>the Brazilian Test (also known as the Splitting Tensile Test or Indirect Tensile Test)</strong> is the universally standardized laboratory method used to determine the <strong>Tensile Strength ($\sigma_t$) of intact rock</strong> (Bangar, p. 187; ISRM, 1978; ASTM D3967).
      </p>
      <p>
        The test was originally conceived by Brazilian engineer Fernando L.L. Carneiro (1943) for concrete and subsequently adapted for rock core specimens. It circumvents the severe experimental difficulties of direct uniaxial pull testing (such as core necking, clamping stress concentrations, and epoxy debonding) by applying a <strong>compressive line load across the diameter of a circular disc</strong>.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q126/brazilian_test_tensile_strength.png" alt="Brazilian Test Setup and Stress Distribution">
        <div class="figure-caption">
          <strong>Figure 126.1 — Brazilian Test Configuration and Theoretical Stress Distribution:</strong> A circular rock disc of diameter $D$ and thickness $t$ compressed diametrally by load $P$. Biaxial elastic stress analysis demonstrates a remarkably uniform horizontal tensile stress ($\sigma_x = -\sigma_t$) across approximately $75\%$ of the vertical diameter, causing clean vertical splitting along the loading axis.
        </div>
      </div>

      <h4>Elastic Theory of the Diametrally Loaded Disc</h4>
      <p>
        According to the classical theory of elasticity (Timoshenko & Goodier; Hondros, 1959), when a circular disc of diameter $D$ and axial thickness $t$ is subjected to diametral concentrated line loads $P$ applied at the top and bottom:
      </p>
      <ul>
        <li>Along the vertical loading diameter ($y$-axis), the vertical normal stress $\sigma_y$ is highly compressive:
          $$\sigma_y = -\frac{2 P}{\pi D t} \left[\frac{D^2}{y(D - y)} - 1\right]$$
        </li>
        <li>Simultaneously, the horizontal normal stress $\sigma_x$ across the vertical diameter is <strong>tensile and nearly constant</strong> over the central portion of the disc:
          $$\sigma_x = \frac{2 P}{\pi D t} = \text{constant}$$
        </li>
      </ul>
      <p>
        Because rock is dramatically weaker in tension than in compression ($\sigma_c \approx 10\text{ to } 20 \times \sigma_t$), tensile failure initiates at the center of the disc and propagates outward toward both loaded edges, cleanly cleaving the specimen in half along the vertical diameter.
      </p>

      <div class="math-block">
        $$\text{Brazilian Tensile Strength: } \sigma_t = \frac{2 P}{\pi D t} \approx 0.6366 \frac{P}{D t}$$
        $$\text{where: } P = \text{Peak compressive load at failure (N)}, \quad D = \text{Disc diameter (mm)}, \quad t = \text{Disc thickness (mm)}$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q126/bangar_p187_brazilian_tensile_strength.png" alt="Tensile Strength and Brazilian Test from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 126.2 — Brazilian Test in Engineering Geology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 187). Explains: <em>"The Brazilian test is used to determine the tensile strength of stones indirectly by compressing a disc-shaped specimen diametrically."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: ISRM & ASTM TESTING STANDARDS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Standard ISRM & ASTM D3967 Testing Protocols: Dimensions & Jaws</div>
    <div class="card-body">
      <h4>Standard Specimen Dimensions and Geometry</h4>
      <ul>
        <li><strong>Disc Shape:</strong> Circular disc diamond-sawn from cylindrical drill core ($NX$ core, diameter $D \approx 54\text{ mm}$, or minimum diameter $\ge 47\text{ mm}$).</li>
        <li><strong>Thickness-to-Diameter Ratio ($t / D$):</strong> The thickness $t$ must be approximately equal to the radius ($t \approx 0.5 D$). Specifically, ASTM D3967 mandates:
          $$0.2 \le \frac{t}{D} \le 0.75 \quad (\text{ideally } t / D \approx 0.50)$$
          If $t / D < 0.2$, the disc behaves as a thin membrane prone to buckling. If $t / D > 0.75$, 3D end-effects and shear wedge crushing dominate before tensile splitting can initiate.</li>
        <li><strong>Curved Loading Jaws:</strong> To prevent premature crushing of mineral grains immediately beneath the sharp line contacts, the ISRM mandates the use of <strong>curved steel loading platens</strong> with a radius of curvature $1.5 \times$ the disc radius, distributing contact stress over an arc of $10^\circ \text{ to } 15^\circ$. Alternatively, cushioning strips of blotting paper or cardboard ($0.5\text{ mm}$ thick) are inserted.</li>
        <li><strong>Loading Rate:</strong> Applied continuously at a constant rate such that failure occurs within $1\text{ to } 10\text{ minutes}$ (stress rate of $0.05\text{ to } 0.1\text{ MPa/s}$).</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: WHY DIRECT PULL FAILS AND ENGINEERING IMPORTANCE -->
  <div class="card">
    <div class="card-header bg-indigo">3. Direct vs. Indirect Tensile Testing & Practical Engineering Importance</div>
    <div class="card-body">
      <h4>Why the Brazilian Test Superseded Direct Tension Testing</h4>
      <p>
        Direct tensile testing of rock requires machining dog-bone specimens or gluing heavy steel end-caps with epoxy resins. It suffers from severe practical failures:
      </p>
      <ul>
        <li>Epoxy shear debonding under high humidity or high rock strength.</li>
        <li>Bending moments induced by slight eccentricities in the tensile pull rods, causing non-uniform premature edge cracking.</li>
        <li>High machining costs and fragility of weak, fractured, or foliated rock cores.</li>
      </ul>
      <p>
        The Brazilian test provides an economical, rapid, and highly reproducible indirect measurement using standard core slices without complex machining.
      </p>

      <h4>Geotechnical and Mining Significance</h4>
      <ul>
        <li><strong>Underground Excavation Roof Stability:</strong> Mine roofs span open roadways and delaminate under gravity-induced flexural tensile stresses.</li>
        <li><strong>Hydraulic Fracturing:</strong> In petroleum engineering and geothermal stimulation, borehole fluid pressure must overcome the in-situ minimum principal stress plus the tensile strength of the rock ($\Delta P \ge 3\sigma_3 - \sigma_1 + \sigma_t - P_p$).</li>
        <li><strong>Explosive Blasting Fragmentation:</strong> Shockwaves from detonation reflect from free rock faces as tensile stress waves, spalling the rock because of its extreme tensile weakness.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 126</div>
      <div class="question-text">
        The ‘Brazilian test’ is used to determine :
      </div>
      <ul class="option-list">
        <li class="option-item correct"><strong>(A)</strong> Tensile strength</li>
        <li class="option-item"><strong>(B)</strong> Compressive strength</li>
        <li class="option-item"><strong>(C)</strong> Shear strength</li>
        <li class="option-item"><strong>(D)</strong> Modulus of elasticity</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (A) Tensile strength</strong> — The Brazilian test is the universally recognized indirect diametral compression method for determining the tensile strength ($\sigma_t$) of rocks and concrete.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option correct">
        <div class="option-title">Option (A): Tensile strength — Fully Verified & Correct</div>
        <p>
          The Brazilian test is defined in standard textbooks (Bangar, p. 187; Jaeger & Cook) and international standards (ISRM, 1978; ASTM D3967) as the standard indirect method for evaluating the <strong>tensile strength ($\sigma_t$)</strong> of intact rock core discs. By applying compressive loads across the diameter, an internal uniform tensile stress is created normal to the diameter ($\sigma_t = \frac{2 P}{\pi D t}$), triggering vertical tensile splitting.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Compressive strength — Incorrect Test Method</div>
        <p>
          Compressive strength (UCS) is determined by the Uniaxial Compression Test (ISRM, 1979; ASTM D7012) on cylindrical rock specimens with an aspect ratio of $L/D = 2.0 - 2.5$, where axial load is applied perpendicular to the planar ends. Although the Brazilian test applies a compressive load externally to the disc, its internal failure mechanism and calibrated output measure tensile strength, not compressive strength.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): Shear strength — Incorrect Test Method</div>
        <p>
          Shear strength is evaluated using Direct Shear Box testing (IS: 13047), Triaxial Compression testing (Hoek cell), or Punch Shear testing. The Brazilian test generates pure tensile splitting along the central axis with zero shear stress.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Modulus of elasticity — Incorrect Property</div>
        <p>
          Modulus of elasticity ($E$) is determined from axial and lateral strain gauges (or LVDTs) mounted on cylindrical specimens during uniaxial or triaxial compression testing ($E = \Delta \sigma / \Delta \varepsilon$). It is a deformability modulus, not measured by the Brazilian splitting test.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Methods for Determining Tensile Strength of Rocks</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Testing Method</th>
            <th>Loading Configuration</th>
            <th>Specimen Geometry</th>
            <th>Governing Equation</th>
            <th>Practical Advantages / Drawbacks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Brazilian Test (Indirect Tension)</strong></td>
            <td>Diametral compression line load ($P$)</td>
            <td>Circular disc ($D \approx 54\text{ mm}, t \approx 0.5D$)</td>
            <td>$\sigma_t = \frac{2 P}{\pi D t}$</td>
            <td><strong>Industry Standard:</strong> Simple core preparation, reproducible, avoids clamping/epoxy problems.</td>
          </tr>
          <tr>
            <td><strong>Direct Pull Test (Uniaxial Tension)</strong></td>
            <td>Direct axial tensile pull</td>
            <td>Dog-bone cylinder with glued steel end-caps</td>
            <td>$\sigma_t = \frac{P_{\text{tensile}}}{A}$</td>
            <td>True pure uniaxial tension; highly expensive, severe grip alignment errors, frequent epoxy failure.</td>
          </tr>
          <tr>
            <td><strong>Bending Test (Modulus of Rupture)</strong></td>
            <td>Three-point or four-point transverse bending</td>
            <td>Prismatic bar ($b \times d \times L$)</td>
            <td>$R = \frac{3 W L}{2 b d^2}$</td>
            <td>Overestimates true tensile strength by $50 - 100\%$ due to stress gradients and non-linear yield.</td>
          </tr>
          <tr>
            <td><strong>Point Load Test (Diametral)</strong></td>
            <td>Point-load concentrated indentation</td>
            <td>Intact drill core ($L > 1.4 D$)</td>
            <td>$I_s = \frac{P}{D_e^2}; \quad \sigma_t \approx 1.25 \times I_s$</td>
            <td>Fast field index; less accurate than Brazilian test due to complex 3D cone fracture.</td>
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
        <strong>Problem 1: Standard Brazilian Tensile Strength Calculation</strong><br>
        A Brazilian test is performed on an $NX$ core disc of fresh granite with diameter $D = 54.0\text{ mm}$ and thickness $t = 27.0\text{ mm}$. The digital testing machine records a peak diametral splitting load of $P = 21.6\text{ kN}$. Calculate the tensile strength ($\sigma_t$) of the granite in $\text{MPa}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Use the standard Brazilian tensile strength formula:
          $$\sigma_t = \frac{2 P}{\pi D t}$$
          2. Substitute given values ($P = 21,600\text{ N}, D = 54.0\text{ mm}, t = 27.0\text{ mm}$):
          $$\sigma_t = \frac{2 \times 21,600}{\pi \times 54.0 \times 27.0} = \frac{43,200}{\pi \times 1458.0} = \frac{43,200}{4580.44} = 9.431\text{ N/mm}^2 = 9.43\text{ MPa}$$
          The Brazilian tensile strength of the granite is $9.43\text{ MPa}$.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Ratio of Compressive Strength to Tensile Strength</strong><br>
        In a geotechnical laboratory program for a tunnel project, basalt core specimens yield a mean Unconfined Compressive Strength of $\sigma_c = 145.0\text{ MPa}$ and a Brazilian tensile strength of $\sigma_t = 11.6\text{ MPa}$. (a) Calculate the ratio $\sigma_c / \sigma_t$. (b) Assess whether this ratio falls within the classical theoretical and empirical range for brittle crystalline rocks.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate the ratio:
          $$\frac{\sigma_c}{\sigma_t} = \frac{145.0\text{ MPa}}{11.6\text{ MPa}} = 12.50$$
          2. Theoretical Assessment: Griffith's classical crack theory predicts an ideal ratio of $\sigma_c / \sigma_t = 8.0$ for open 2D Griffith cracks. In real crystalline rocks with closed microcracks and internal friction, empirical ratios consistently range between $10.0\text{ and } 20.0$. Thus, $12.50$ is a typical, highly representative value.
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Required Peak Load for Limestone Core Disc</strong><br>
        A limestone disc has diameter $D = 50.0\text{ mm}$ and thickness $t = 25.0\text{ mm}$. The rock is known to have a tensile strength of $\sigma_t = 6.5\text{ MPa}$. What peak diametral compressive load $P$ is expected to cause tensile splitting?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Rearrange the Brazilian formula for $P$:
          $$P = \frac{\pi D t \sigma_t}{2}$$
          2. Substitute values:
          $$P = \frac{\pi \times 50.0\text{ mm} \times 25.0\text{ mm} \times 6.5\text{ N/mm}^2}{2} = \frac{\pi \times 1250 \times 6.5}{2} = \frac{25,525.44}{2} = 12,762.7\text{ N} \approx 12.76\text{ kN}$$
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Hydraulic Fracturing Breakdown Pressure Calculation</strong><br>
        A borehole at depth $z = 1200\text{ m}$ is subjected to hydraulic fracturing. The in-situ horizontal stresses are $\sigma_h = 24.0\text{ MPa}$ and $\sigma_H = 34.0\text{ MPa}$, and pore-water pressure is $P_p = 12.0\text{ MPa}$. The Brazilian tensile strength of the sandstone formation is $\sigma_t = 5.5\text{ MPa}$. Using the Hubbert-Willis breakdown equation:
        $$P_b = 3 \sigma_h - \sigma_H + \sigma_t - P_p$$
        Calculate the borehole fluid breakdown pressure ($P_b$) required to initiate a vertical hydraulic fracture.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Substitute given values into the Hubbert-Willis equation:
          $$P_b = 3(24.0) - 34.0 + 5.5 - 12.0$$
          $$P_b = 72.0 - 34.0 + 5.5 - 12.0 = 31.5\text{ MPa}$$
          The formation will fracture when fluid injection pressure reaches $31.5\text{ MPa}$.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Anisotropic Tensile Strength in Metamorphic Foliation</strong><br>
        A foliated biotite schist core is tested using the Brazilian method in two configurations:
        (1) Diametral load applied perpendicular to foliation planes (inducing tensile splitting across foliation): measured $\sigma_{t\perp} = 8.4\text{ MPa}$;
        (2) Diametral load applied parallel to foliation planes (foliation planes aligned with the vertical splitting line): measured $\sigma_{t\parallel} = 2.1\text{ MPa}$.
        Calculate the Tensile Anisotropy Index ($I_{t} = \sigma_{t\perp} / \sigma_{t\parallel}$) and discuss the structural failure mode.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate Tensile Anisotropy Index:
          $$I_{t} = \frac{\sigma_{t\perp}}{\sigma_{t\parallel}} = \frac{8.4\text{ MPa}}{2.1\text{ MPa}} = 4.0$$
          2. Discussion: When foliation is aligned parallel to the tensile splitting axis, the weak van der Waals bonds between parallel aligned biotite sheets split open at only $25\%$ of the force required to fracture across intact quartz-feldspar crystals, demonstrating extreme mechanical directionality.
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Stress State at the Center of a Brazilian Disc</strong><br>
        For a disc of diameter $D = 54\text{ mm}$ and thickness $t = 27\text{ mm}$ under load $P = 18.0\text{ kN}$, calculate: (a) the principal tensile stress $\sigma_1$ at the center, and (b) the vertical compressive stress $\sigma_3$ at the center (where $y = D/2$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Center point coordinates: $x = 0, y = D/2$.
          2. Horizontal tensile stress $\sigma_x$:
          $$\sigma_x = \frac{2 P}{\pi D t} = \frac{2 \times 18,000}{\pi \times 54 \times 27} = \frac{36,000}{4580.44} = +7.86\text{ MPa (Tension)}$$
          3. Vertical compressive stress $\sigma_y$:
          $$\sigma_y = -\frac{2 P}{\pi D t} \left[\frac{D^2}{(D/2)(D/2)} - 1\right] = -\sigma_x [4 - 1] = -3 \sigma_x$$
          $$\sigma_y = -3 \times 7.86\text{ MPa} = -23.58\text{ MPa (Compression)}$$
          <em>Key Insight:</em> At the center of the Brazilian disc, the vertical compressive stress is exactly three times the horizontal tensile stress ($\sigma_y = -3 \sigma_x$).
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Thickness-to-Diameter Ratio ($t/D$) Validity Check</strong><br>
        A student pre-cuts four rock core discs of diameter $D = 50\text{ mm}$ with varying thicknesses:
        Disc 1 ($t = 8\text{ mm}$), Disc 2 ($t = 15\text{ mm}$), Disc 3 ($t = 25\text{ mm}$), Disc 4 ($t = 45\text{ mm}$).
        Assess each disc against the ASTM D3967 geometric criteria ($0.2 \le t/D \le 0.75$) and identify which discs are valid.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate $t / D$ for each disc:
          <ul>
            <li>Disc 1: $t/D = 8 / 50 = 0.16 < 0.20$ &rarr; <strong>Invalid</strong> (too thin; prone to buckling and premature edge chipping).</li>
            <li>Disc 2: $t/D = 15 / 50 = 0.30$ &rarr; <strong>Valid</strong> ($0.20 \le 0.30 \le 0.75$).</li>
            <li>Disc 3: $t/D = 25 / 50 = 0.50$ &rarr; <strong>Optimal / Valid</strong> (ideal $t/D \approx 0.50$ recommended by ISRM).</li>
            <li>Disc 4: $t/D = 45 / 50 = 0.90 > 0.75$ &rarr; <strong>Invalid</strong> (too thick; 3D end-effects and shear crushing dominate).</li>
          </ul>
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Griffith Failure Criterion with Brazilian and UCS Data</strong><br>
        According to Griffith's classical failure criterion for brittle materials, when $\sigma_1 + 3\sigma_3 > 0$, failure occurs when:
        $$(\sigma_1 - \sigma_3)^2 = 8 \sigma_t (\sigma_1 + \sigma_3)$$
        If a rock has a Brazilian tensile strength $\sigma_t = 8.0\text{ MPa}$, predict its theoretical Uniaxial Compressive Strength ($\sigma_c$) where $\sigma_1 = \sigma_c$ and $\sigma_3 = 0$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Substitute $\sigma_1 = \sigma_c$ and $\sigma_3 = 0$ into Griffith's criterion:
          $$(\sigma_c - 0)^2 = 8 \sigma_t (\sigma_c + 0)$$
          $$\sigma_c^2 = 8 \sigma_t \sigma_c$$
          2. Divide both sides by $\sigma_c$ ($\sigma_c \ne 0$):
          $$\sigma_c = 8 \sigma_t$$
          3. Calculate $\sigma_c$:
          $$\sigma_c = 8 \times 8.0\text{ MPa} = 64.0\text{ MPa}$$
          <em>Geological Note:</em> Griffith's open-crack theory demonstrates why intact rock compressive strength is naturally an order of magnitude higher than tensile strength.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=126,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q126_Brazilian_Test_Tensile_Strength_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q126: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q126()
