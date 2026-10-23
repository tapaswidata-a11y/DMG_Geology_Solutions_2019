#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 9 Part A (Q106 - Q113)
Engineering Geology: Rock Mechanics, Index Properties, Compressive Strength, and Rock Bursts.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q106: Unconfined Compressive Strength (UCS) as Index Property
# -----------------------------------------------------------------------------
def gen_q106():
    q_num = 106
    filename = "Q106_Compressive_Strength_Index_Property_Is_Unconfined_Complete_Guide.html"
    title = "Q106: Rock Mechanics - Unconfined Compressive Strength (UCS)"
    badge = "OPSC 2019 Geology Paper-II • Question 106 • Engineering Geology"
    h1_title = "Rock Mechanics: Unconfined Compressive Strength (UCS) as the Premier Index Property"
    meta_text = "<strong>Topic:</strong> Rock Mechanics & Stone Testing • <strong>Key Concept:</strong> UCS Testing Protocol & Rock Mass Classification • <strong>Textbooks:</strong> IS: 9143 (1979); E. Hoek & J.W. Bray; K.M. Bangar (p. 286)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Unconfined Compressive Strength (UCS) in Engineering Geology</div>
      <p>In rock engineering and geotechnical design, the <strong>Unconfined Compressive Strength (UCS)</strong> (also known as <em>uniaxial compressive strength</em>) is universally recognized by the International Society for Rock Mechanics (ISRM) and the Bureau of Indian Standards (IS: 9143) as the single <strong>most important index property of intact rock and building stones</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Testing Regime</th>
              <th>Confining Pressure ($\sigma_3$)</th>
              <th>Pore Fluid Drainage Condition</th>
              <th>Standard Laboratory & Field Role</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>UNCONFINED (Uniaxial) COMPRESSIVE STRENGTH (UCS)</strong> (Option D)</td>
              <td><strong>Zero Lateral Confinement ($\sigma_2 = \sigma_3 = 0$)</strong></td>
              <td>Tested dry or at natural moisture content; air-jacketed cylinder.</td>
              <td><strong>Primary index property for rock classification (Deere & Miller, 1966), RMR (Bieniawski), Q-system (Barton), and GSI</strong>.</td>
            </tr>
            <tr>
              <td>Confined (Triaxial) Strength (Option A)</td>
              <td>$\sigma_3 > 0$ (Hydraulic cell pressure)</td>
              <td>Drained or undrained; simulates deep burial stress.</td>
              <td>Determines failure envelopes, internal friction angle ($\phi$), and cohesion ($c$).</td>
            </tr>
            <tr>
              <td>Drained Compressive Strength (Option B)</td>
              <td>$\sigma_3 > 0$</td>
              <td>Pore water allowed to drain; excess pore pressure $u = 0$.</td>
              <td>Long-term slope and foundation stability analysis.</td>
            </tr>
            <tr>
              <td>Undrained Compressive Strength (Option C)</td>
              <td>$\sigma_3 > 0$</td>
              <td>Pore water prevented from escaping; $u \ne 0$.</td>
              <td>Short-term sudden loading (e.g., rapid dam filling or earthquake shock).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "The <strong>unconfined compressive strength (UCS)</strong> is by far the most widely used and important mechanical property of rocks. It represents the ultimate compressive stress an unconfined cylindrical specimen can bear before failing along shear fractures. Because it is simple to determine, highly reproducible, and correlates directly with rock hardness, durability, drillability, and modulus of elasticity, UCS forms the backbone of all engineering classifications of building stones."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Properties of Building Stones, pp. 286&ndash;288)</div>
      </div>

      <div class="formula-box">
        $$\text{Unconfined Compressive Strength (UCS): } \sigma_c = \frac{P_{\text{failure}}}{A} = \frac{4 P_{\text{failure}}}{\pi D^2}$$
        $$\text{Standard Specimen Geometry: } \text{Cylinder with Height-to-Diameter Ratio } \frac{L}{D} = 2.0 \text{ to } 2.5 \quad (D \approx 54\text{ mm, NX core})$$
        $$\text{Lateral Boundary Condition: } \sigma_2 = \sigma_3 = 0 \implies \mathbf{UNCONFINED\ (Option\ D)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q106/unconfined_compressive_strength_ucs_test.png" alt="Unconfined Compressive Strength UCS Test" class="figure-img">
        <div class="figure-caption">Figure 106: Laboratory Unconfined Compressive Strength (UCS) testing configuration (IS: 9143) showing axial compressive failure of an unconfined cylindrical rock core specimen.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 106</div>
        <div class="raw-q-text">Which type of compressive strength is taken as the most important index property of stones ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Confined</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Drained</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Undrained</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Unconfined</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Unconfined)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Unconfined</div>
          <p>By international and Indian engineering geology standards (IS: 9143; ISRM; Deere & Miller; Bangar, p. 286), the <strong>Unconfined compressive strength (UCS)</strong> is universally accepted as the premier and most fundamental <strong>index property</strong> of building stones and intact rock masses.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Confined</div>
          <p>Confined compressive strength requires complex triaxial cells to apply lateral confining fluid pressures ($\sigma_3$). While essential for deep underground tunnel analysis, it is too complex and costly to serve as a routine index property for building stones.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Drained</div>
          <p>Drained strength is a specialized soil/rock mechanics parameter where pore water is allowed to escape during shear, used in effective stress analysis rather than as a baseline stone index property.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Undrained</div>
          <p>Undrained compressive strength tests low-permeability rocks/clays where pore pressures build up during rapid loading; it is not the general index property used to grade stone quarries.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Strength Class (IS: 9143 / Deere & Miller)</th>
              <th>UCS Range (MPa)</th>
              <th>UCS Range ($kg/cm^2$)</th>
              <th>Representative Rock Types</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Class A: Very High Strength</td><td>&gt; 220 MPa</td><td>&gt; 2240 $kg/cm^2$</td><td>Basalt, Fresh Dolerite, Massive Quartzite, Charnockite</td></tr>
            <tr><td>Class B: High Strength</td><td>110 &ndash; 220 MPa</td><td>1120 &ndash; 2240 $kg/cm^2$</td><td>Granite, Gneiss, Dense Limestone, Dolomite</td></tr>
            <tr><td>Class C: Medium Strength</td><td>55 &ndash; 110 MPa</td><td>560 &ndash; 1120 $kg/cm^2$</td><td>Sandstone, Marble, Slate, Schist</td></tr>
            <tr><td>Class D: Low Strength</td><td>28 &ndash; 55 MPa</td><td>280 &ndash; 560 $kg/cm^2$</td><td>Porous Sandstone, Soft Limestone, Siltstone</td></tr>
            <tr><td>Class E: Very Low Strength</td><td>&lt; 28 MPa</td><td>&lt; 280 $kg/cm^2$</td><td>Chalk, Clay Shale, Weathered Tuff, Highly Weathered Rocks</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the standard height-to-diameter ($L/D$) ratio specified for laboratory UCS testing of rock cores?</div>
        <div class="pq-ans">Answer: 2.0 to 2.5 (IS: 9143 / ISRM)</div>
        <div class="pq-exp">An $L/D$ ratio of 2.0 to 2.5 eliminates end-platen frictional confinement effects while avoiding buckling instability.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. If a rock specimen has an $L/D$ ratio of less than 2.0, what correction formula is applied to obtain standard UCS ($\sigma_{c}$)?</div>
        <div class="pq-ans">Answer: $\sigma_{c} = \frac{\sigma_{c\text{-measured}}}{0.778 + 0.222 (D/L)}$ (ASTM / Protodyakonov correction)</div>
        <div class="pq-exp">Shorter specimens exhibit falsely elevated strengths due to platen restraint across the entire core height.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What indirect field test correlates strongly with UCS and can be conducted directly on irregular rock lumps?</div>
        <div class="pq-ans">Answer: The Point Load Strength Index test ($I_{s(50)}$)</div>
        <div class="pq-exp">ISRM and IS: 8764 relate point load index to compressive strength via the empirical formula: $\text{UCS} \approx 20\text{ to } 25 \times I_{s(50)}$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the typical UCS value of fresh, unweathered granite?</div>
        <div class="pq-ans">Answer: 150 to 250 MPa (approximately 1500 to 2500 $kg/cm^2$).</div>
        <div class="pq-exp">Granite's dense interlocking hypidiomorphic quartz-feldspar fabric provides massive compressive load-bearing capability.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What non-destructive rebound test measures surface hardness and estimates UCS in the field?</div>
        <div class="pq-ans">Answer: The Schmidt Rebound Hammer Test (L-type hammer)</div>
        <div class="pq-exp">The rebound number ($R$) calibrated against rock dry density provides a rapid, empirical estimation of in-situ UCS.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does moisture saturation affect the UCS of sedimentary sandstones and shales?</div>
        <div class="pq-ans">Answer: Saturation reduces UCS by 30% to 65% compared to dry strength.</div>
        <div class="pq-exp">Water weakens clay cements, reduces surface energy (Rehbinder effect), and develops pore pressure, sharply diminishing compressive strength.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the Brazilian Test used for in rock mechanics?</div>
        <div class="pq-ans">Answer: Determining the indirect tensile strength of rock discs.</div>
        <div class="pq-exp">Compressing a circular rock disc diametrically induces uniform tensile stress across the loaded diameter ($\sigma_t = \frac{2P}{\pi D t}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the typical ratio between tensile strength and compressive strength for intact rock?</div>
        <div class="pq-ans">Answer: Tensile strength is approximately 1/10th to 1/20th (5% to 10%) of compressive strength.</div>
        <div class="pq-exp">Griffith's crack theory proves that pre-existing microscopic microcracks open rapidly in tension, making rocks 10 to 20 times weaker in tension.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q107: Maximum Force Per Unit Area Before Rupturing (Compressive Strength)
# -----------------------------------------------------------------------------
def gen_q107():
    q_num = 107
    filename = "Q107_Maximum_Force_Per_Unit_Area_Without_Rupturing_Is_Compressive_Strength_Complete_Guide.html"
    title = "Q107: Rock Mechanics - Compressive Strength Definition"
    badge = "OPSC 2019 Geology Paper-II • Question 107 • Engineering Geology"
    h1_title = "Stress-Strain Mechanics: Compressive (Crushing) Strength of Building Stones"
    meta_text = "<strong>Topic:</strong> Mechanical Properties of Rocks • <strong>Key Concept:</strong> Peak Stress Without Rupturing • <strong>Textbooks:</strong> K.M. Bangar (p. 286); P.K. Mukherjee; G.B. Mahapatra"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Defining Compressive (Crushing) Strength</div>
      <p>In continuum mechanics and rock engineering, <strong>Compressive Strength</strong> (commonly termed <em>crushing strength</em>) is defined as the <strong>maximum compressive force expressed per unit area that a stone or rock specimen can withstand without crushing, collapsing, or rupturing</strong> under gradually applied axial load:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Strength Parameter</th>
              <th>Mode of Force Application</th>
              <th>Failure Mechanism</th>
              <th>Typical Relative Value for Rock</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>COMPRESSIVE STRENGTH</strong> (Option C)</td>
              <td><strong>Axial Opposing Compressive Load</strong> pushing grains inward.</td>
              <td>Shear rupture along conjugate shear planes / microcrack coalescence.</td>
              <td><strong>HIGHEST ($\mathbf{100\%}$ Baseline: 50 &ndash; 300 MPa)</strong>.</td>
            </tr>
            <tr>
              <td>Shear Strength (Option A)</td>
              <td>Parallel tangential forces sliding adjacent planes.</td>
              <td>Overcoming cohesion ($c$) and internal friction ($\sigma \tan \phi$).</td>
              <td>Intermediate ($~10\text{--}25\%$ of compressive strength).</td>
            </tr>
            <tr>
              <td>Tensile Strength (Option B)</td>
              <td>Opposing pulling-apart forces stretching rock.</td>
              <td>Direct Mode-I opening of Griffith microcracks.</td>
              <td><strong>LOWEST ($~5\text{--}10\%$ of compressive strength)</strong>.</td>
            </tr>
            <tr>
              <td>Bending (Flexural) Strength (Option D)</td>
              <td>Transverse beam bending load (modulus of rupture).</td>
              <td>Tensile fiber failure at the outermost convex surface.</td>
              <td>Low to moderate ($~10\text{--}15\%$ of compressive strength).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "The <strong>crushing strength or compressive strength</strong> of a stone is the maximum force per unit area which a stone can bear without crushing or rupturing. It is tested on a universal testing machine by crushing cubical or cylindrical specimens until complete failure occurs. A good building stone should have a crushing strength of not less than 1000 kg/cm² (100 MPa)."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Properties of Building Stones, p. 286)</div>
      </div>

      <div class="formula-box">
        $$\text{Definition: } \sigma_c = \frac{P_{\text{max}}}{A} \quad \left[\text{Units: } \frac{\text{N}}{\text{mm}^2} \equiv \text{MPa} \equiv \frac{\text{kgf}}{\text{cm}^2} \times 0.09806\right]$$
        $$\mathbf{Maximum\ Force\ Per\ Unit\ Area\ Without\ Rupturing} \equiv \mathbf{Compressive\ Strength\ (Option\ C)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q107/compressive_strength_stress_strain_curve.png" alt="Compressive Strength Stress Strain Curve" class="figure-img">
        <div class="figure-caption">Figure 107: Complete rock stress-strain curve under compressive loading, demonstrating the peak stress (compressive strength) sustained prior to physical rupture.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 107</div>
        <div class="raw-q-text">What is the maximum force expressed per unit area, which a stone can withstand without rupturing ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Shear strength</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Tensile strength</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Compressive strength</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Bending strength</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Compressive strength)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Compressive strength</div>
          <p>By standard engineering definition (IS: 1121 Part I; Bangar, p. 286; Mahapatra), the maximum compressive load per unit cross-sectional area that a building stone can withstand before collapsing, crushing, or rupturing is formally defined as its <strong>Compressive strength</strong> (or crushing strength).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Shear strength</div>
          <p>Shear strength is the maximum shearing or sliding stress along a plane that a stone can resist, governed by cohesion and angle of internal friction ($\tau = c + \sigma \tan \phi$), not the general crushing capacity per unit area.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Tensile strength</div>
          <p>Tensile strength is the resistance of stone against pulling or tearing apart forces, which in rocks is extremely low (only 5% to 10% of compressive strength).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Bending strength</div>
          <p>Bending (transverse) strength measures resistance against flexural bending moments when supported at ends and loaded in the center, not pure compressive rupture.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Type</th>
              <th>Compressive Strength (MPa)</th>
              <th>Tensile Strength (MPa)</th>
              <th>Shear Strength (MPa)</th>
              <th>Modulus of Rupture (Bending, MPa)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Fresh Basalt</td><td>200 &ndash; 350 MPa</td><td>12 &ndash; 20 MPa</td><td>25 &ndash; 45 MPa</td><td>20 &ndash; 35 MPa</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Granite</td><td>150 &ndash; 250 MPa</td><td>8 &ndash; 15 MPa</td><td>18 &ndash; 30 MPa</td><td>14 &ndash; 25 MPa</td></tr>
            <tr><td>Dolomitic Limestone</td><td>80 &ndash; 160 MPa</td><td>5 &ndash; 10 MPa</td><td>10 &ndash; 20 MPa</td><td>8 &ndash; 15 MPa</td></tr>
            <tr><td>Quartzose Sandstone</td><td>60 &ndash; 120 MPa</td><td>3 &ndash; 7 MPa</td><td>8 &ndash; 15 MPa</td><td>5 &ndash; 12 MPa</td></tr>
            <tr><td>Clay Shale</td><td>15 &ndash; 45 MPa</td><td>1 &ndash; 3 MPa</td><td>3 &ndash; 8 MPa</td><td>2 &ndash; 5 MPa</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the minimum crushing strength required for stones used in heavy masonry structures according to Indian Standard codes?</div>
        <div class="pq-ans">Answer: 100 MPa ($1000\text{ kg/cm}^2$) for heavy structures; 35 MPa for normal building works.</div>
        <div class="pq-exp">IS: 1905 dictates minimum crushing strength thresholds to ensure safety against structural failure.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What shape of laboratory specimen is mandated by IS: 1121 for testing compressive strength of natural stone?</div>
        <div class="pq-ans">Answer: Either cubes ($70\text{ mm} \times 70\text{ mm} \times 70\text{ mm}$) or cylinders ($L/D = 1.0\text{ to } 2.0$).</div>
        <div class="pq-exp">Cube specimens must be dressed flat with parallel faces within 0.1 mm tolerance to prevent eccentric edge loading.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the angle ($\theta$) of the shear rupture failure plane relative to the major principal stress ($\sigma_1$) in Mohr-Coulomb failure?</div>
        <div class="pq-ans">Answer: $\theta = 45^\circ + \phi / 2$ (typically $55^\circ\text{--}65^\circ$ to the horizontal platen).</div>
        <div class="pq-exp">Failure planes form inclined shear cones governed by the internal friction angle ($\phi$) of the rock material.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the conversion factor between MPa ($\text{N/mm}^2$) and $kg/cm^2$?</div>
        <div class="pq-ans">Answer: $1\text{ MPa} \approx 10.197\text{ kg/cm}^2$ (or $1\text{ kg/cm}^2 \approx 0.098\text{ MPa}$).</div>
        <div class="pq-exp">For quick estimation: $100\text{ MPa} \approx 1000\text{ kg/cm}^2$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What happens to the compressive strength of a rock if the rate of loading is increased significantly?</div>
        <div class="pq-ans">Answer: The apparent compressive strength increases (dynamic strength is higher than static strength).</div>
        <div class="pq-exp">Fast loading gives microcracks insufficient time to propagate, yielding artificially higher peak strengths (IS codes specify 0.5 to 1.0 MPa/sec).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which building stone has the highest crushing strength among common Indian stones?</div>
        <div class="pq-ans">Answer: Basalt (Deccan Trap) and Fine-grained Dolerite (up to 300-350 MPa).</div>
        <div class="pq-exp">Dense ophitic micro-crystalline plagioclase-pyroxene intergrowth provides colossal mechanical resistance.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is ductile versus brittle failure in rocks under compression?</div>
        <div class="pq-ans">Answer: Brittle rocks fracture suddenly with little plastic strain; ductile rocks undergo substantial plastic flow before failure without sudden loss of strength.</div>
        <div class="pq-exp">Under shallow crustal conditions, intact rocks behave in a brittle manner; deep confining pressure drives the brittle-ductile transition.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is Young's Modulus ($E$) of a rock in compressive stress testing?</div>
        <div class="pq-ans">Answer: The ratio of axial stress to axial strain within the linear elastic range ($E = \Delta \sigma / \Delta \epsilon$).</div>
        <div class="pq-exp">Young's modulus represents elastic stiffness; fresh granite has $E \approx 40\text{--}70\text{ GPa}$.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q108: Rocks Possessing Very High Compressive Strength (Igneous)
# -----------------------------------------------------------------------------
def gen_q108():
    q_num = 108
    filename = "Q108_Rocks_Possessing_Very_High_Compressive_Strength_Are_Igneous_Complete_Guide.html"
    title = "Q108: Rock Strength Comparison - Igneous Rocks"
    badge = "OPSC 2019 Geology Paper-II • Question 108 • Engineering Geology"
    h1_title = "Comparative Rock Mechanics: Why Igneous Rocks Possess Very High Compressive Strength"
    meta_text = "<strong>Topic:</strong> Lithological Strength Classification • <strong>Key Concept:</strong> Interlocking Crystalline Textures vs. Porosity • <strong>Textbooks:</strong> K.M. Bangar (pp. 286-289); F.G. Bell; Goodman"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Micro-Structural Controls on Compressive Strength</div>
      <p>The compressive strength of any rock mass is fundamentally determined by three primary petrographic parameters: (1) <strong>interlocking crystalline fabric</strong>, (2) <strong>mineral hardness and bonding</strong>, and (3) <strong>void volume (porosity and microcracks)</strong>. On this basis, <strong>Igneous Rocks</strong> possess the highest compressive strength among all major rock classes:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Class</th>
              <th>Fabric & Grain Boundary Architecture</th>
              <th>Porosity Range</th>
              <th>Compressive Strength Range (MPa)</th>
              <th>Engineering Evaluation</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>IGNEOUS ROCKS</strong> (Option A)</td>
              <td><strong>Interlocking crystalline mosaic</strong> (crystallized directly from molten magma without voids).</td>
              <td><strong>Extremely Low (&lt; 0.5% &ndash; 1.5%)</strong></td>
              <td><strong>★ VERY HIGH: 150 &ndash; 350+ MPa ★</strong></td>
              <td><strong>Superlative foundation rocks for mega-dams, high-rise piers, and heavy dimension stone (Basalt, Granite, Dolerite)</strong>.</td>
            </tr>
            <tr>
              <td>Metamorphic Rocks (Non-foliated)</td>
              <td>Solid-state granoblastic recrystallization (Quartzite, Marble).</td>
              <td>Very Low (&lt; 1%)</td>
              <td>High to Very High (100 &ndash; 250 MPa)</td>
              <td>High strength, but foliated varieties (schist, slate) are weakened by directional cleavage planes.</td>
            </tr>
            <tr>
              <td>Sedimentary Rocks (Option B)</td>
              <td>Clastic grains bonded by authigenic cement; grain-to-grain contact points.</td>
              <td>High (5% to 35%)</td>
              <td>Low to Moderate (10 &ndash; 100 MPa)</td>
              <td>Weakened by porous matrix, clay content, and soluble cements (Sandstone, Shale, Limestone).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Among all geological formations, <strong>unweathered igneous rocks possess very high compressive strength</strong>. Rocks like basalt, dolerite, granite, and diorite have strengths between 1500 and 3000 kg/cm² (150 to 300 MPa). This massive strength stems from their completely crystalline, interlocking fabric of hard silicates (quartz, feldspar, pyroxene) that grew together during solidification from magma, leaving virtually no pore voids."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Properties of Building Stones, pp. 288&ndash;289)</div>
      </div>

      <div class="formula-box">
        $$\text{Ryskewitsch-Duckworth Porosity-Strength Model: } \sigma = \sigma_0 e^{-b \cdot n}$$
        $$\text{In Igneous Rocks: Porosity } n \rightarrow 0 \implies \mathbf{Compressive\ Strength\ \sigma \rightarrow Maximum\ (150\text{--}350\text{ MPa})}$$
        $$\therefore \mathbf{Rocks\ with\ Very\ High\ Compressive\ Strength \equiv IGNEOUS\ ROCKS\ (Option\ A)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q108/compressive_strength_rock_types_comparison.png" alt="Compressive Strength Rock Types Comparison" class="figure-img">
        <div class="figure-caption">Figure 108: Comparative unconfined compressive strength across rock types, demonstrating the commanding strength dominance of crystalline igneous rocks over sedimentary and foliated metamorphic rocks.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 108</div>
        <div class="raw-q-text">Which rocks possess very high compressive strength ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Igneous</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Sedimentary</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Metamorphic</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Both sedimentary and metamorphic</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Igneous)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Igneous</div>
          <p>Fresh, unweathered <strong>igneous rocks</strong> (basalt, granite, dolerite, diorite) possess <strong>very high compressive strength</strong> (routinely exceeding 150 to 300 MPa). Their direct crystallization from silicate melts produces a tightly interlocking mosaic of hard minerals with virtually zero primary porosity ($< 1\%$).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Sedimentary</div>
          <p>Sedimentary rocks (sandstone, shale, limestone) possess low to moderate compressive strength (10 to 80 MPa) because they consist of clastic grains held together by weak cements with high porosity (10% to 30%).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Metamorphic</div>
          <p>While massive non-foliated metamorphic rocks like quartzite have high strength, the vast majority of metamorphic rocks are <strong>foliated</strong> (slates, phyllites, schists) and suffer from pronounced directional planes of weakness that shear easily under stress.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Both sedimentary and metamorphic</div>
          <p>Sedimentary rocks have the lowest compressive strengths among intact rocks; grouping them with high strength is completely inaccurate.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Class & Member</th>
              <th>Mean UCS (MPa)</th>
              <th>Deere & Miller Strength Class</th>
              <th>Porosity (%)</th>
              <th>Engineering Suitability</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Basalt (Igneous)</strong></td><td><strong>250 &ndash; 350 MPa</strong></td><td><strong>Class A: Very High</strong></td><td>&lt; 0.5%</td><td>Heavy railway ballast, breakwater armour, dam foundation</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Granite (Igneous)</strong></td><td><strong>180 &ndash; 250 MPa</strong></td><td><strong>Class A / B: Very High</strong></td><td>&lt; 0.8%</td><td>Mega-dam abutments, monumental dimension stone</td></tr>
            <tr><td>Quartzite (Metamorphic)</td><td>150 &ndash; 220 MPa</td><td>Class B: High</td><td>&lt; 1.0%</td><td>High strength, but extremely abrasive to drilling tools</td></tr>
            <tr><td>Biotite Schist (Metamorphic)</td><td>35 &ndash; 70 MPa</td><td>Class C / D: Medium</td><td>2.0 &ndash; 5.0%</td><td>Prone to sliding along schistosity planes</td></tr>
            <tr><td>Quartz Sandstone (Sedimentary)</td><td>40 &ndash; 80 MPa</td><td>Class C / D: Medium</td><td>12 &ndash; 20%</td><td>General masonry; strength drops when saturated</td></tr>
            <tr><td>Shale (Sedimentary)</td><td>10 &ndash; 30 MPa</td><td>Class E: Very Low</td><td>15 &ndash; 30%</td><td>Unsuitable for engineering foundations (slakes in water)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Why is fresh Deccan Trap basalt widely regarded as the finest construction aggregate in Western and Central India?</div>
        <div class="pq-ans">Answer: It possesses colossal crushing strength (>250 MPa), high toughness, low water absorption (<0.5%), and excellent bitumen affinity.</div>
        <div class="pq-exp">Basalt's fine-grained, interlocking ophitic and intersertal fabric gives it exceptional resistance to traffic abrasion and impact.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which sedimentary rock can occasionally reach high compressive strength comparable to granites?</div>
        <div class="pq-ans">Answer: Pure orthoquartzite (silica-cemented quartzarenite)</div>
        <div class="pq-exp">When silica completely fills all pore spaces as syntaxial quartz overgrowths, sandstone converts into a tough, impermeable orthoquartzite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the effect of chemical weathering on the compressive strength of granitic rocks?</div>
        <div class="pq-ans">Answer: Weathering can reduce compressive strength by 80% to 95% (from 200 MPa down to <10 MPa in saprolite).</div>
        <div class="pq-exp">Hydrolysis alters hard interlocking feldspars into soft, porous kaolinite clay, destroying rock integrity.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the Deere-Miller Engineering Classification based on?</div>
        <div class="pq-ans">Answer: Unconfined compressive strength (UCS) and the Modulus Ratio ($E_t / \sigma_c$).</div>
        <div class="pq-exp">Deere and Miller (1966) plot rock strength classes (A to E) against modulus ratios (High, Medium, Low) for structural rock classification.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why are foliated metamorphic rocks (like mica schists) dangerous as dam abutments despite being crystalline?</div>
        <div class="pq-ans">Answer: Because mica alignment creates continuous planes of weakness with very low shear strength along foliation.</div>
        <div class="pq-exp">Water lubrication along schistosity can trigger catastrophic foundation sliding under reservoir thrust.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which volcanic igneous rock possesses LOW compressive strength due to high vesicular porosity?</div>
        <div class="pq-ans">Answer: Pumice and Scoria (UCS typically < 10-20 MPa).</div>
        <div class="pq-exp">Extreme trapped gas bubble porosity (>60-80%) makes pumice so weak and light that it floats on water.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. How does grain size affect the compressive strength within the igneous gabbro-dolerite-basalt family?</div>
        <div class="pq-ans">Answer: Fine-grained basalt and dolerite are stronger than coarse-grained gabbro.</div>
        <div class="pq-exp">The Hall-Petch effect in rocks: smaller grain size increases grain boundary area, impeding microcrack propagation and boosting strength.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the crushing strength threshold below which a rock is classified as 'weak' in engineering practice?</div>
        <div class="pq-ans">Answer: Less than 25 MPa (ISRM / British Standard)</div>
        <div class="pq-exp">Rocks with UCS < 25 MPa can be gouged with a geological pick and represent weak foundation conditions.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q109: Porosity Definition (Ratio of Voids to Total Volume)
# -----------------------------------------------------------------------------
def gen_q0109():
    q_num = 109
    filename = "Q109_Ratio_Pore_Spaces_To_Total_Volume_Is_Porosity_Complete_Guide.html"
    title = "Q109: Rock Mechanics - Porosity vs. Void Ratio"
    badge = "OPSC 2019 Geology Paper-II • Question 109 • Engineering Geology & Hydrogeology"
    h1_title = "Pore Physics: Porosity, Void Ratio, and Volumetric Index Properties"
    meta_text = "<strong>Topic:</strong> Index Properties of Rocks & Soils • <strong>Key Concept:</strong> Porosity ($V_v / V_t$) vs. Void Ratio ($V_v / V_s$) • <strong>Textbooks:</strong> K.M. Bangar (p. 284); Terzaghi & Peck; Sam Boggs Jr."

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Defining Porosity & Volumetric Phase Relations</div>
      <p>In hydrogeology, petroleum geology, and rock/soil mechanics, a natural geological material is conceptualized as a multi-phase system consisting of <strong>solid mineral grains ($V_s$)</strong> and open interstitial <strong>pore spaces (voids, $V_v$)</strong> occupied by water and/or air. The fundamental volumetric parameters are defined as follows:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Volumetric Property</th>
              <th>Mathematical Definition</th>
              <th>Physical Meaning & Reference Base</th>
              <th>Range of Values</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>POROSITY ($n$)</strong> (Option B)</td>
              <td>$$n = \frac{V_v}{V_t} \times 100\%$$</td>
              <td><strong>Ratio between the total volume of pore spaces ($V_v$) and the TOTAL volume of the rock ($V_t = V_s + V_v$)</strong>.</td>
              <td>Always expressed as a fraction ($0 < n < 1$) or percentage ($0\% \text{ to } 100\%$). Cannot exceed 100%.</td>
            </tr>
            <tr>
              <td><strong>Void Ratio ($e$)</strong> (Option A)</td>
              <td>$$e = \frac{V_v}{V_s}$$</td>
              <td>Ratio between the total volume of pore spaces ($V_v$) and the volume of <strong>SOLID mineral grains only ($V_s$)</strong>.</td>
              <td>Expressed as a decimal ratio; can exceed 1.0 (or $> 100\%$) in soft clays and loose silts.</td>
            </tr>
            <tr>
              <td>Bulk Density ($\rho_b$) (Option D)</td>
              <td>$$\rho_b = \frac{M_{\text{total}}}{V_t}$$</td>
              <td>Total mass of rock (solids + moisture) per unit total volume.</td>
              <td>Units: $\text{g/cm}^3$ or $\text{kg/m}^3$ (typically 1.8 to 3.0).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Porosity</strong> is the ratio between the total volume of pore spaces (voids) to the total volume of the rock, generally expressed as a percentage. It indicates the storage capacity of the rock for fluids like water, oil, or gas. In contrast, <em>void ratio</em> is the ratio of the volume of voids to the volume of the solid grains alone."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Properties of Building Stones, p. 284)</div>
      </div>

      <div class="formula-box">
        $$\mathbf{Porosity\ (n)} = \frac{\mathbf{Volume\ of\ Pore\ Spaces\ (V_v)}}{\mathbf{Total\ Volume\ of\ the\ Rock\ (V_t)}} \times 100\% \equiv \mathbf{Option\ B}$$
        $$\text{Inter-relationship: } n = \frac{e}{1 + e} \quad \text{and} \quad e = \frac{n}{1 - n}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q109/porosity_vs_void_ratio_rock_mechanics.png" alt="Porosity vs Void Ratio Rock Mechanics" class="figure-img">
        <div class="figure-caption">Figure 109: Three-phase diagram of rock volume illustrating the precise difference between Porosity (Vv / Vt) and Void Ratio (Vv / Vs).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 109</div>
        <div class="raw-q-text">Ratio between the total volume of pore spaces to the total volume of the rock is a measure of:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Void ratio</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Porosity</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Pores ratio</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Bulk density</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Porosity)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Porosity</div>
          <p>By fundamental definition across physics, hydrogeology, and rock mechanics (IS: 13030; Bangar, p. 284; Todd; Freeze & Cherry), the ratio of the total volume of pore spaces ($V_v$) to the <strong>total volume of the rock ($V_t$)</strong> is defined as <strong>Porosity</strong> ($n$).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Void ratio</div>
          <p>Void ratio ($e$) is the ratio of the volume of pore spaces ($V_v$) to the <strong>volume of solid mineral grains ($V_s$)</strong>, NOT to the total volume ($V_t$).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Pores ratio</div>
          <p>'Pores ratio' is a fictitious non-geological distractor without physical or mathematical definition.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Bulk density</div>
          <p>Bulk density is the ratio of <strong>mass to volume</strong> ($\rho = M/V$), expressed in units of $\text{g/cm}^3$ or $\text{kg/m}^3$, not a dimensionless volume-to-volume ratio.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Geological Material</th>
              <th>Typical Porosity ($n\%$)</th>
              <th>Typical Void Ratio ($e$)</th>
              <th>Primary vs. Secondary Nature</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Unweathered Granite / Basalt</td><td>0.1% &ndash; 1.0%</td><td>0.001 &ndash; 0.01</td><td>Micro-fractures and crystal defects</td></tr>
            <tr><td>Dense Crystalline Limestone</td><td>1.0% &ndash; 5.0%</td><td>0.01 &ndash; 0.05</td><td>Intercrystalline / moldic voids</td></tr>
            <tr><td>Well-sorted Quartz Sandstone</td><td>15% &ndash; 25%</td><td>0.18 &ndash; 0.33</td><td>Intergranular primary porosity</td></tr>
            <tr><td>Unconsolidated Sand</td><td>30% &ndash; 45%</td><td>0.43 &ndash; 0.82</td><td>Interparticle primary porosity</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Soft Marine Clay</td><td>50% &ndash; 75%</td><td>1.00 &ndash; 3.00</td><td>Flocculated card-house structure</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. If a soil has a void ratio $e = 0.50$, what is its porosity ($n$)?</div>
        <div class="pq-ans">Answer: $n = 33.33\%$ (or 0.333)</div>
        <div class="pq-exp">$n = \frac{e}{1 + e} = \frac{0.50}{1 + 0.50} = \frac{0.50}{1.50} = 0.333 \implies 33.33\%$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. If a sandstone has a porosity $n = 20\%$, what is its void ratio ($e$)?</div>
        <div class="pq-ans">Answer: $e = 0.25$</div>
        <div class="pq-exp">$e = \frac{n}{1 - n} = \frac{0.20}{1 - 0.20} = \frac{0.20}{0.80} = 0.25$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the theoretical maximum porosity for an aggregate of uniform spherical grains packed in cubic packing?</div>
        <div class="pq-ans">Answer: $47.64\%$</div>
        <div class="pq-exp">In cubic packing, volume of solids in a unit cell of edge $2R$ is $\frac{4}{3}\pi R^3 / 8 R^3 = \frac{\pi}{6} \approx 0.5236$, leaving $n = 1 - 0.5236 = 47.64\%$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the theoretical minimum porosity for uniform spheres in rhombohedral (hexagonal close) packing?</div>
        <div class="pq-ans">Answer: $25.95\%$ (or $\approx 26\%$)</div>
        <div class="pq-exp">Rhombohedral packing represents the densest possible geometric packing of uniform spheres without crushing.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the difference between total porosity and effective porosity?</div>
        <div class="pq-ans">Answer: Total porosity includes all voids (isolated + interconnected); effective porosity includes only interconnected pores that allow fluid flow.</div>
        <div class="pq-exp">Pumice and clay have very high total porosity, but low effective porosity because pores are either isolated (pumice) or bound by molecular adhesion (clay).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Why does a clay have higher porosity (50-70%) than a well-sorted sand (30-40%), yet far lower permeability?</div>
        <div class="pq-ans">Answer: Clay has immense total pore volume due to open card-house fabric, but pore throat diameters are sub-microscopic, creating colossal viscous drag.</div>
        <div class="pq-exp">Permeability is governed by pore throat size ($r^2$), not by total pore volume ($n$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is secondary porosity in limestone reservoirs?</div>
        <div class="pq-ans">Answer: Porosity formed after deposition by groundwater dissolution (vugs, caverns) or tectonic fracturing.</div>
        <div class="pq-exp">Dissolution along joints creates cavernous and karst porosity holding major hydrocarbon reserves.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What laboratory instrument is used to measure the grain volume of rock cores for porosity determination?</div>
        <div class="pq-ans">Answer: Helium Pycnometer (Boyle's Law Porosimeter)</div>
        <div class="pq-exp">Helium gas penetrates the finest interconnected pores, enabling highly accurate measurement of solid grain volume ($V_s$).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q110: Rock Density with Natural Moisture (Bulk Density)
# -----------------------------------------------------------------------------
def gen_q0110():
    q_num = 110
    filename = "Q110_Density_Of_Rock_With_Natural_Moisture_Is_Bulk_Density_Complete_Guide.html"
    title = "Q110: Rock Mechanics - Bulk Density & Natural Moisture"
    badge = "OPSC 2019 Geology Paper-II • Question 110 • Engineering Geology"
    h1_title = "Rock Density Mechanics: Bulk Density Retaining In-Situ Natural Moisture"
    meta_text = "<strong>Topic:</strong> Index Properties of Building Stones • <strong>Key Concept:</strong> Bulk Density vs. Dry Density vs. Saturated Density • <strong>Textbooks:</strong> IS: 13030 (1991); ISRM Suggested Methods; K.M. Bangar (p. 284)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Density States in Engineering Geology</div>
      <p>In geotechnical engineering and rock mechanics (IS: 13030; ISRM), the density of rock is defined as the ratio of mass to total volume. Depending on the moisture state within the pore network, three standardized density parameters are recognized:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Density Parameter</th>
              <th>Pore Fluid Condition</th>
              <th>Mathematical Formulation</th>
              <th>Engineering Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>BULK DENSITY ($\rho_b$)</strong> (Option C)</td>
              <td><strong>Natural In-Situ Moisture Content ($w_{\text{nat}}$)</strong> as excavated from quarry.</td>
              <td>$$\rho_b = \frac{M_{\text{natural}}}{V_t}$$</td>
              <td><strong>The fundamental in-situ unit weight used for calculating overburden stresses, slope stability, and foundation loads</strong>.</td>
            </tr>
            <tr>
              <td>Dry Density ($\rho_d$) (Option A)</td>
              <td>Completely dried in oven at $105^\circ\text{C}$ until constant mass; pores contain only air.</td>
              <td>$$\rho_d = \frac{M_{\text{dry}}}{V_t} = \frac{\rho_b}{1 + w}$$</td>
              <td>Baseline parameter for porosity determination and compaction control.</td>
            </tr>
            <tr>
              <td>Saturated Density ($\rho_{\text{sat}}$)</td>
              <td>All pore spaces 100% filled with water under vacuum saturation ($S_r = 1.0$).</td>
              <td>$$\rho_{\text{sat}} = \frac{M_{\text{sat}}}{V_t} = \rho_d + n \rho_w$$</td>
              <td>Used for stability of submerged dam foundations, sea walls, and below-water-table slopes.</td>
            </tr>
            <tr>
              <td>True (Grain) Density ($\rho_s$)</td>
              <td>Solid mineral grains only without voids.</td>
              <td>$$\rho_s = \frac{M_{\text{dry}}}{V_s}$$</td>
              <td>Reflects mineral composition (e.g., pure quartz = $2.65\text{ g/cm}^3$).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "The density of the rock with its natural moisture content is known as its <strong>bulk density</strong> (or natural wet density). It is the mass of the rock in its natural, in-situ state divided by its total volume. In engineering projects, bulk density governs the dead load of stone masonry and the gravitational driving forces on rock slopes."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Properties of Building Stones, p. 284)</div>
      </div>

      <div class="formula-box">
        $$\mathbf{Bulk\ Density\ (\rho_b)} = \frac{\mathbf{Mass\ of\ Rock\ with\ Natural\ Moisture\ (M_{\text{natural}})}}{\mathbf{Total\ Bulk\ Volume\ of\ Rock\ (V_t)}} \equiv \mathbf{Option\ C}$$
        $$\text{Relationship with Dry Density: } \rho_b = \rho_d (1 + w) \quad (w = \text{Natural Moisture Content})$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q110/rock_bulk_density_natural_moisture_content.png" alt="Rock Bulk Density Natural Moisture Content" class="figure-img">
        <div class="figure-caption">Figure 110: Comparison of the three standard rock density states: Dry Density (pores air-filled), Bulk Density (with natural moisture), and Saturated Density (pores 100% water-filled).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 110</div>
        <div class="raw-q-text">The density of the rock with natural moisture content is known as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Dry density</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Wet density</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Bulk density</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Natural density</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Bulk density)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Bulk density</div>
          <p>By official Indian Standard specification (IS: 13030) and classical textbook definitions (Bangar, p. 284; Mahapatra), the mass per unit total volume of rock containing its <strong>natural moisture content</strong> is formally designated as <strong>Bulk density</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Dry density</div>
          <p>Dry density is measured after driving out all moisture in an oven at $105^\circ\text{C}$ to zero moisture content; it does not contain natural moisture.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Wet density</div>
          <p>While casually used, 'wet density' in strict testing usually denotes artificially saturated rock (saturated density); the formal engineering term for natural in-situ moisture state is <strong>bulk density</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Natural density</div>
          <p>'Natural density' is an informal descriptive phrase; the standardized technical term in Indian and ISRM standards is <strong>bulk density</strong>.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Type</th>
              <th>Bulk Density ($\text{g/cm}^3$)</th>
              <th>Bulk Density ($\text{kg/m}^3$)</th>
              <th>Natural Moisture Content ($w\%$)</th>
              <th>Engineering Suitability</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Deccan Trap Basalt</td><td>2.85 &ndash; 3.00</td><td>2850 &ndash; 3000</td><td>&lt; 0.5%</td><td>Heavy gravity dams, breakwaters</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Granite</td><td>2.65 &ndash; 2.75</td><td>2650 &ndash; 2750</td><td>&lt; 0.5%</td><td>Bridge abutments, heavy masonry</td></tr>
            <tr><td>Dense Limestone</td><td>2.50 &ndash; 2.70</td><td>2500 &ndash; 2700</td><td>0.5% &ndash; 2.0%</td><td>Dimension stone, lime manufacture</td></tr>
            <tr><td>Quartz Sandstone</td><td>2.20 &ndash; 2.50</td><td>2200 &ndash; 2500</td><td>2.0% &ndash; 6.0%</td><td>Ashlar masonry, architectural carving</td></tr>
            <tr><td>Porous Tuff / Chalk</td><td>1.40 &ndash; 1.80</td><td>1400 &ndash; 1800</td><td>10% &ndash; 25%</td><td>Lightweight non-load-bearing fill</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. If a rock specimen has a total volume of $100\text{ cm}^3$ and weighs 265 grams in its natural moisture state, what is its bulk density?</div>
        <div class="pq-ans">Answer: $2.65\text{ g/cm}^3$ (or $2650\text{ kg/m}^3$)</div>
        <div class="pq-exp">$\rho_b = M_{\text{nat}} / V_t = 265\text{ g} / 100\text{ cm}^3 = 2.65\text{ g/cm}^3$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. If the same specimen from Problem 1 weighs 260 grams after oven-drying, what is its natural moisture content ($w$)?</div>
        <div class="pq-ans">Answer: $1.92\%$</div>
        <div class="pq-exp">$w = \frac{M_{\text{nat}} - M_{\text{dry}}}{M_{\text{dry}}} \times 100 = \frac{265 - 260}{260} \times 100 = \frac{5}{260} \times 100 \approx 1.92\%$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What method is specified by IS: 13030 to measure the total volume ($V_t$) of an irregular porous rock lump?</div>
        <div class="pq-ans">Answer: The Water Displacement Method with Paraffin Wax Coating (or Mercury Displacement).</div>
        <div class="pq-exp">Coating the specimen with an ultra-thin layer of melted paraffin wax prevents water from entering the pores during submersion.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Why is high bulk density desirable for stones used in breakwaters and harbour sea-walls?</div>
        <div class="pq-ans">Answer: High density provides greater gravitational submerged weight ($W' = (\rho_b - \rho_w) g V$) resisting displacement by violent storm waves.</div>
        <div class="pq-exp">Hudson's formula proves that armour stone stability on sea-walls increases with the cube of the submerged unit weight.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the relation between dry density ($\rho_d$), specific gravity ($G$), and porosity ($n$)?</div>
        <div class="pq-ans">Answer: $\rho_d = G \cdot \rho_w (1 - n)$</div>
        <div class="pq-exp">Since dry mass occupies volume $(1 - n) V_t$, the dry density is directly proportional to $(1 - n)$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which Indian state has extensive quarries of heavy Deccan Trap basalt used for railway ballast?</div>
        <div class="pq-ans">Answer: Maharashtra, Gujarat, and Western Madhya Pradesh</div>
        <div class="pq-exp">Deccan basalts have high bulk density ($~2.9\text{ g/cm}^3$), making them ideal for heavy-haul rail beds.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is submerged (buoyant) density ($\rho'$)?</div>
        <div class="pq-ans">Answer: $\rho' = \rho_{\text{sat}} - \rho_{\text{water}}$</div>
        <div class="pq-exp">Buoyancy reduces the effective weight of rocks submerged beneath the water table.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What temperature is standardized for oven-drying rock specimens to determine moisture content and dry density?</div>
        <div class="pq-ans">Answer: $105^\circ\text{C} \pm 5^\circ\text{C}$ for at least 24 hours.</div>
        <div class="pq-exp">This temperature evaporates all free pore water and adsorbed capillary moisture without destroying structural lattice water in gypsum or clays.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q111: Impact Testing of Stone (Toughness)
# -----------------------------------------------------------------------------
def gen_q0111():
    q_num = 111
    filename = "Q111_Impact_Testing_Of_Stone_Done_To_Know_Toughness_Complete_Guide.html"
    title = "Q111: Stone Testing - Impact Testing for Toughness"
    badge = "OPSC 2019 Geology Paper-II • Question 111 • Engineering Geology"
    h1_title = "Building Stone Testing: Impact Testing and the Measurement of Toughness"
    meta_text = "<strong>Topic:</strong> Mechanical Testing of Stones • <strong>Key Concept:</strong> Impact Resistance & Toughness Index • <strong>Textbooks:</strong> IS: 2386 (Part IV); Page Impact Test; K.M. Bangar (p. 288)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Mechanical Meaning of Toughness & Impact Testing</div>
      <p>In mechanical engineering and stone testing, <strong>toughness</strong> is defined as the ability of a material to absorb kinetic energy and resist fracturing, shattering, or disintegrating under <strong>sudden impact blows</strong>. While crushing strength measures resistance to slow, static loads, <strong>Impact Testing</strong> is conducted specifically to determine a stone's <strong>Toughness</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Laboratory Test Method</th>
              <th>Dynamic Stress Imposed</th>
              <th>Primary Property Measured</th>
              <th>Standard Apparatus & Reference</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>IMPACT TEST</strong> (Option D)</td>
              <td><strong>Sudden dynamic impact blow</strong> (falling hammer).</td>
              <td><strong>★ TOUGHNESS ★ (Option D)</strong> (Resistance to shattering under repeated shock loads).</td>
              <td><strong>Page Impact Testing Machine / Aggregate Impact Value (AIV) (IS: 2386 Part IV)</strong>.</td>
            </tr>
            <tr>
              <td>Crushing Test</td>
              <td>Slow, gradually increasing static compressive load.</td>
              <td>Compressive (Crushing) Strength</td>
              <td>Universal Testing Machine / Compression Press (IS: 1121 Part I).</td>
            </tr>
            <tr>
              <td>Abrasion Test</td>
              <td>Frictional rubbing and abrasive grinding.</td>
              <td>Hardness & Wear Resistance</td>
              <td>Los Angeles Abrasion / Deval Attrition Machine (IS: 2386 Part IV).</td>
            </tr>
            <tr>
              <td>Soundness Test</td>
              <td>Cyclic immersion in sodium or magnesium sulfate salt solutions.</td>
              <td>Durability (Frost & Weathering resistance)</td>
              <td>Sodium Sulfate Soundness Apparatus (IS: 2386 Part V).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "The resistance of a stone to impact or shattering under a sudden blow is known as its <strong>toughness</strong>. It is determined by the <strong>impact test</strong> using a Page Impact Machine. A steel hammer weighing 2 kg is dropped on a cylindrical stone core from successive heights increasing by 1 cm until the specimen breaks. The height of the blow in centimeters that causes failure is taken as the <strong>toughness index</strong> of the stone."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Properties of Building Stones, p. 288)</div>
      </div>

      <div class="formula-box">
        $$\text{Page Impact Toughness Test: } \text{Toughness Index } (T) \equiv \text{Drop Height of 2 kg Hammer at Fracture (in cm)}$$
        $$\text{Aggregate Impact Value (AIV): } \text{AIV } (\%) = \frac{W_2 (\text{Fines passing 2.36 mm sieve})}{W_1 (\text{Total sample weight})} \times 100\%$$
        $$\mathbf{Impact\ Testing\ of\ Stone} \implies \mathbf{Determines\ TOUGHNESS\ (Option\ D)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q111/impact_testing_toughness_page_impact_test.png" alt="Impact Testing Toughness Page Impact Test" class="figure-img">
        <div class="figure-caption">Figure 111: Impact testing apparatus and mechanics for determining stone toughness (resistance to sudden impact loads) alongside crushing and abrasion tests.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 111</div>
        <div class="raw-q-text">The impact testing of a stone is done to know the:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Durability</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Porosity</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Density</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Toughness</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Toughness)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Toughness</div>
          <p>By standard civil engineering and building stone testing codes (IS: 2386 Part IV; ASTM D3; Bangar, p. 288; Mahapatra), <strong>impact testing</strong> is conducted specifically to measure the <strong>toughness</strong> (impact resistance against dynamic shattering) of stones and road aggregates.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Durability</div>
          <p>Durability (weathering resistance) is determined by the <strong>soundness test</strong> (sodium sulfate cycles), freezing-and-thawing tests, or water absorption tests, NOT by impact testing.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Porosity</div>
          <p>Porosity is determined through water absorption saturation methods or helium pycnometry, measuring volumetric voids rather than dynamic shock response.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Density</div>
          <p>Density is measured by mass-to-volume displacement (pycnometer or water immersion), an intrinsic mass property unrelated to mechanical impact blows.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Type</th>
              <th>Toughness Index (Page Test, cm)</th>
              <th>Classification</th>
              <th>Aggregate Impact Value (AIV, %)</th>
              <th>Field Performance</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Fresh Dolerite / Basalt</td><td>&gt; 19 cm</td><td><strong>High Toughness</strong></td><td>&lt; 15%</td><td>Superb resistance to heavy traffic hammering</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Granite</td><td>13 &ndash; 19 cm</td><td><strong>Medium Toughness</strong></td><td>15% &ndash; 25%</td><td>Good road base, but quartz can shatter under point impact</td></tr>
            <tr><td>Dense Quartzite</td><td>12 &ndash; 16 cm</td><td>Medium Toughness</td><td>18% &ndash; 24%</td><td>Hard but brittle; shatters into sharp splinters</td></tr>
            <tr><td>Limestone</td><td>8 &ndash; 13 cm</td><td><strong>Low Toughness (Brittle)</strong></td><td>25% &ndash; 35%</td><td>Pulverizes into white dust under heavy impact</td></tr>
            <tr><td>Shale / Soft Sandstone</td><td>&lt; 8 cm</td><td><strong>Very Low Toughness</strong></td><td>&gt; 40%</td><td>Completely rejected for road wearing courses</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. In the Page Impact Test, what is the weight of the falling hammer and from what height does the test start?</div>
        <div class="pq-ans">Answer: The hammer weighs 2.0 kg and drops initially from a height of 1.0 cm.</div>
        <div class="pq-exp">The drop height increases by 1 cm after each blow (1 cm, 2 cm, 3 cm...) until the specimen fractures.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What toughness index value classifies a stone as 'high toughness' according to standard engineering specifications?</div>
        <div class="pq-ans">Answer: Greater than 19 cm ($T > 19$).</div>
        <div class="pq-exp">$T > 19$ is high toughness; 13 to 19 is medium toughness; $< 13$ is poor/low toughness.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. In the Aggregate Impact Value (AIV) test (IS: 2386 Part IV), how many blows are delivered and by what hammer weight?</div>
        <div class="pq-ans">Answer: 15 blows by a 13.5 to 14.0 kg hammer dropping from a height of 380 mm (38 cm).</div>
        <div class="pq-exp">AIV is the percentage of crushed fines passing through a 2.36 mm IS sieve after 15 standard blows.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the maximum permissible Aggregate Impact Value (AIV) for aggregates used in bituminous concrete road wearing courses?</div>
        <div class="pq-ans">Answer: Maximum 24% (IRC guidelines specify $\le 24\%$ or $\le 30\%$ for base courses).</div>
        <div class="pq-exp">Lower AIV values signify higher toughness and resistance to shattering under vehicle wheel impacts.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why does dolerite have higher toughness than coarse granite even though both are igneous?</div>
        <div class="pq-ans">Answer: Dolerite possesses an ophitic texture where flexible plagioclase laths are enclosed in pyroxene, absorbing impact energy without propagating cracks.</div>
        <div class="pq-exp">Granite contains large brittle quartz crystals that cleave and shatter readily under impact blows.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What test determines the resistance of stone to wear caused by mutual rubbing of aggregates against each other?</div>
        <div class="pq-ans">Answer: The Attrition Test (Deval Attrition Test)</div>
        <div class="pq-exp">Frictional rubbing of stones against stones is attrition; rubbing of stones against external steel balls/abrasives is abrasion.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the relationship between toughness and brittleness in rocks?</div>
        <div class="pq-ans">Answer: Toughness and brittleness are inverse properties; high toughness implies low brittleness.</div>
        <div class="pq-exp">Brittle rocks fracture with minimal strain energy absorption, whereas tough rocks deform plastically and dissipate energy before failing.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the Charpy or Izod test used for?</div>
        <div class="pq-ans">Answer: Measuring the notched impact energy of construction materials (steels and structural composites).</div>
        <div class="pq-exp">Charpy tests measure the kinetic energy absorbed by a swinging pendulum hammer breaking a notched specimen.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q112: Sudden Release of Stress in Tunneling (Rock Bursts)
# -----------------------------------------------------------------------------
def gen_q0112():
    q_num = 112
    filename = "Q112_Sudden_Release_Of_Stress_In_Tunneling_Results_In_Rock_Bursts_Complete_Guide.html"
    title = "Q112: Tunneling Geotechnics - Rock Bursts Hazard"
    badge = "OPSC 2019 Geology Paper-II • Question 112 • Engineering Geology"
    h1_title = "Underground Geomechanics: High In-Situ Stresses and the Hazard of Rock Bursts"
    meta_text = "<strong>Topic:</strong> Geological Hazards in Tunneling • <strong>Key Concept:</strong> Explosive Stress Release & Strainburst Mechanics • <strong>Textbooks:</strong> E. Hoek & E.T. Brown (1980); K.M. Bangar (p. 305); F.G. Bell"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Geomechanics of Rock Bursts in Deep Excavations</div>
      <p>In deep underground civil tunneling and mining excavations (typically at depths exceeding 500 to 1000 meters), rocks exist under colossal lithostatic confining stresses ($\sigma_v = \rho g z$). When an opening is blasted or bored, the confining support is instantly removed, redistributing stress into severe concentrations around the excavation periphery. The <strong>sudden explosive release of stored elastic strain energy</strong> in massive, brittle rocks causes violent rock ejection known as a <strong>Rock Burst</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Tunneling Phenomenon</th>
              <th>Physical / Mechanical Mechanism</th>
              <th>Speed of Occurrence</th>
              <th>Geological Pre-Conditions</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>ROCK BURST (Strainburst)</strong> (Option B)</td>
              <td><strong>Sudden, violent explosive release of accumulated elastic strain energy</strong> as tangential stress ($\sigma_\theta$) exceeds rock strength.</td>
              <td><strong>Instantaneous</strong> (Microseconds to seconds; gunshot-like explosion).</td>
              <td><strong>Deep overburden (&gt;500 m); hard, brittle, massive crystalline rocks (granites, quartzites, gneisses) with zero open joints</strong>.</td>
            </tr>
            <tr>
              <td>Rock Fall (Option A)</td>
              <td>Gravitational detachment of loose, jointed blocks from the tunnel roof.</td>
              <td>Rapid gravity fall.</td>
              <td>Shallow tunnels; heavily fractured, blocky, intersecting joint sets.</td>
            </tr>
            <tr>
              <td>Squeezing Ground</td>
              <td>Time-dependent ductile inward plastic creep of overstressed rock.</td>
              <td>Slow (Days to months).</td>
              <td>Weak, ductile rocks under high stress (shales, phyllites, fault gouge).</td>
            </tr>
            <tr>
              <td>Water Gush (Option D)</td>
              <td>Sudden inrush of groundwater through karst channels or fault zones.</td>
              <td>Sudden flooding.</td>
              <td>Karst limestone cavities or permeable water-bearing shear zones.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "In deep tunnels driven through hard, brittle, massive rocks (like quartzites, granites, or traps), the rock is subjected to colossal in-situ stresses. When the tunnel is excavated, the rock around the boundary expands into the opening. If the elastic strain energy stored in the rock is released suddenly and violently, slabs of rock fly off the walls and roof with explosive force, accompanied by a sound like a cannon shot. This dangerous phenomenon is known as a <strong>rock burst</strong>."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Tunnels and Underground Works, p. 305)</div>
      </div>

      <div class="formula-box">
        $$\text{Kirsch Solution for Tangential Stress at Sidewall: } \sigma_\theta = 3\sigma_v - \sigma_h \quad (\text{For hydrostatic stress: } \sigma_\theta = 2\sigma_0)$$
        $$\text{Rock Burst Criterion (Hoek): } \frac{\sigma_\theta}{\text{UCS}} > 0.8\text{ to } 1.0 \implies \mathbf{Sudden\ Explosive\ Failure \equiv ROCK\ BURST\ (Option\ B)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q112/rock_burst_tunneling_high_stress_release.png" alt="Rock Burst Tunneling High Stress Release" class="figure-img">
        <div class="figure-caption">Figure 112: Mechanics of rock burst in deep tunneling: concentration of high tangential stresses at tunnel walls triggering explosive failure and ejection of rock slabs.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 112</div>
        <div class="raw-q-text">The sudden release of stress in rocks during tunneling will normally result in :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Rock fall</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Rock bursts</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Blockage</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Water gush</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Rock bursts)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Rock bursts</div>
          <p>By unanimous rock mechanics consensus (Hoek & Brown; Barton; Bangar, p. 305; Mahapatra), the <strong>sudden, violent, explosive release of stored strain energy</strong> in high-stress rock environments during underground tunneling produces <strong>rock bursts</strong> (spontaneous ejection and shattering of rock slabs from the excavation boundary).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Rock fall</div>
          <p>A rock fall is the passive falling of unkeyed, loosened rock blocks under gravity along pre-existing joints, not a dynamic explosion caused by the sudden release of high in-situ strain energy.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Blockage</div>
          <p>'Blockage' is an informal descriptive consequence of collapsed material in a tunnel, not the geomechanical stress-release process itself.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Water gush</div>
          <p>A water gush is a hydrogeological inrush caused by encountering a confined, pressurized aquifer or flooded fault zone, entirely independent of strain energy release in brittle rocks.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Underground Behavior</th>
              <th>Dominant Rock Type</th>
              <th>Stress Regime ($\sigma_v / \text{UCS}$)</th>
              <th>Failure Mode</th>
              <th>Remedial Engineering Support</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Rock Burst (Option B)</strong></td><td>Massive, hard, brittle (Granite, Quartzite)</td><td>High ($\sigma_v / \text{UCS} > 0.4$, $\sigma_\theta \approx \text{UCS}$)</td><td>Violent explosive spalling & rock ejection</td><td>Yielding rockbolts (D-bolts), steel mesh, fiber-reinforced shotcrete, destress blasting</td></tr>
            <tr><td>Squeezing Ground</td><td>Ductile, soft, clayey (Phyllite, Shale, Gouge)</td><td>High ($\sigma_v / \text{UCS} > 0.5$, ductile)</td><td>Slow plastic inward convergence of walls</td><td>Yielding steel arches, compressible lining, flexible slots</td></tr>
            <tr><td>Ravelling / Rock Fall</td><td>Heavily jointed, blocky rock mass</td><td>Low to moderate stress</td><td>Gravitational drop of wedge blocks</td><td>Systematic rockbolting, wire mesh, pattern shotcreting</td></tr>
            <tr><td>Swelling Ground</td><td>Montmorillonite / Smectite rich shales</td><td>Chemical water absorption</td><td>Massive volumetric expansion upon wetting</td><td>Invert drainage, rigid closed circular concrete linings</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. In which famous Indian deep gold mining area were rock bursts a catastrophic historical hazard claiming numerous miners' lives?</div>
        <div class="pq-ans">Answer: The Kolar Gold Fields (KGF) in Karnataka (Champion Reef Mine down to >3200 m depth).</div>
        <div class="pq-exp">At depths exceeding 3 km in massive amphibolitic schists, explosive rock bursts registered as local earthquakes on seismographs.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What preventive drilling technique is used to alleviate stress concentrations and prevent rock bursts ahead of a tunnel face?</div>
        <div class="pq-ans">Answer: Destress blasting (or stress-relief drilling).</div>
        <div class="pq-exp">Drilling large-diameter pilot relief holes or detonating small cushion charges fractured the rock ahead, dissipating strain energy harmlessly.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What modern specialized rock reinforcement bolt is designed to absorb colossal kinetic energy during a rock burst without snapping?</div>
        <div class="pq-ans">Answer: Yielding rockbolts (e.g., D-Bolt, Cone Bolt, or Garford bolt).</div>
        <div class="pq-exp">Yielding bolts can stretch 15% to 20% plastically while maintaining high load resistance, dissipating the kinetic shock of ejected rock.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a microseismic monitoring system in deep tunneling?</div>
        <div class="pq-ans">Answer: A network of acoustic geophones that record high-frequency acoustic emissions generated by propagating microcracks prior to a rock burst.</div>
        <div class="pq-exp">Spiking microseismic event rates provide early warning of an imminent strainburst, allowing evacuation of tunnel crews.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the difference between a strainburst and a fault-slip rock burst?</div>
        <div class="pq-ans">Answer: A strainburst is local explosive spalling at the tunnel skin; a fault-slip burst is an induced earthquake caused by shearing along a nearby major fault.</div>
        <div class="pq-exp">Fault-slip bursts generate massive seismic magnitudes ($M_L > 2.0\text{--}3.5$) that can destroy hundreds of meters of tunnel.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which Himalayan tunnel project experienced severe rock bursts during excavation through high-cover quartzite massifs?</div>
        <div class="pq-ans">Answer: The Rohtang (Atal) Tunnel and Nathpa Jhakri Hydroelectric Tunnel (Himachal Pradesh).</div>
        <div class="pq-exp">Overburden exceeding 1500 to 1900 m in brittle crystalline quartzites triggered intense strainbursting during drilling.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why are heavily jointed, fractured rocks LESS prone to rock bursts than completely intact, massive rocks?</div>
        <div class="pq-ans">Answer: Joint planes allow the rock mass to deform, slip, and relieve stress gradually, preventing the storage of high elastic strain energy.</div>
        <div class="pq-exp">Massive, unjointed rocks behave like a giant loaded spring, holding immense strain until catastrophic failure occurs.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is 'overbreak' in tunneling?</div>
        <div class="pq-ans">Answer: The volume of rock excavated beyond the neat designed perimeter profile of the tunnel.</div>
        <div class="pq-exp">Rock bursts, unfavorable joint dips, and excessive blasting charges dramatically increase overbreak, requiring costly concrete backfilling.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q113: Strata Dipping Angles (Moderately Inclined Strata Upto 45 deg)
# -----------------------------------------------------------------------------
def gen_q0113():
    q_num = 113
    filename = "Q113_Strata_Dipping_Upto_45_Degrees_Are_Moderately_Inclined_Complete_Guide.html"
    title = "Q113: Structural Geology - Classification of Inclined Strata"
    badge = "OPSC 2019 Geology Paper-II • Question 113 • Structural Geology"
    h1_title = "Structural Geometry: Classification of Inclined Strata and Dip Angle Limits"
    meta_text = "<strong>Topic:</strong> Dip and Strike Systematics • <strong>Key Concept:</strong> Gentle vs. Moderate vs. Steep Dip Angles • <strong>Textbooks:</strong> M.P. Billings (Structural Geology); K.M. Bangar (p. 162); G.B. Mahapatra"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Geometric Classification of Inclined Strata</div>
      <p>In structural geology and geological mapping, planar sedimentary strata and metamorphic foliations are described by their <strong>attitude</strong> (strike and dip). The angle of inclination of a bedding plane with the true horizontal plane is termed its <strong>true dip ($\theta$)</strong>. In standard geological engineering classifications (Billings, 1972; Bangar, p. 162), inclined strata are classified based on the magnitude of dip angle:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Inclination Class</th>
              <th>Dip Angle Range ($\theta$)</th>
              <th>Outcrop Character & Topographic Expression</th>
              <th>Engineering Significance (Slopes & Tunnels)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Gently Inclined (Gentle Dip)</td>
              <td>$0^\circ < \theta < 15^\circ$ (or $0^\circ\text{--}10^\circ$)</td>
              <td>Forms mesas, buttes, and gentle cuestas; broad outcrop widths in valleys.</td>
              <td>Extremely stable flat foundations; horizontal tunnel drives.</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>MODERATELY INCLINED STRATA</strong> (Option A)</td>
              <td><strong>$15^\circ \le \theta \le 45^\circ$ (Angles upto $45^\circ$)</strong></td>
              <td><strong>Asymmetrical ridges (cuestas) with distinct dip slope and escarpment</strong>.</td>
              <td><strong>Critical dip range for translational planar rockslides (daylighting on slope cuts)</strong>.</td>
            </tr>
            <tr>
              <td>Steeply Inclined Strata (Option B)</td>
              <td>$45^\circ < \theta < 85^\circ$</td>
              <td>Symmetrical razor-backed ridges (hogbacks); narrow outcrop bands.</td>
              <td>Prone to toppling failures; tunnels cutting normal to strike are most stable.</td>
            </tr>
            <tr>
              <td>Vertical Strata</td>
              <td>$\theta \approx 90^\circ$</td>
              <td>Straight linear bands cutting straight across contour lines regardless of topography.</td>
              <td>No dip-slope sliding; high vertical bearing capacity.</td>
            </tr>
            <tr>
              <td>Overturned Strata (Option D)</td>
              <td>Inverted past $90^\circ$</td>
              <td>Oldest beds lie on top of younger beds; confirmed by geopetal structures.</td>
              <td>Indicates intense recumbent nappe folding.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "According to the angle of inclination (dip), stratified rocks are categorized into: <strong>Gently inclined strata</strong> (dipping at angles less than 15°), <strong>Moderately inclined strata</strong> (dipping at angles between 15° and 45°, or <strong>angles up to 45°</strong>), and <strong>Steeply inclined strata</strong> (dipping at angles greater than 45°). Plunge (Option C) refers specifically to the inclination of a linear fold axis, not a planar stratum."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Structural Geology, pp. 162&ndash;164)</div>
      </div>

      <div class="formula-box">
        $$\text{True Dip Angle: } \theta = \arctan \left(\frac{\Delta h}{L}\right)$$
        $$\mathbf{Dip\ Angle\ Range: } 15^\circ \le \theta \le 45^\circ \implies \mathbf{MODERATELY\ INCLINED\ STRATA\ (Option\ A)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q113/strata_dip_classification_moderately_inclined.png" alt="Strata Dip Classification Moderately Inclined" class="figure-img">
        <div class="figure-caption">Figure 113: Geometrical classification of bedded strata based on dip angle: Gently Inclined (&lt;15°), Moderately Inclined (15° to 45°), and Steeply Inclined (&gt;45°).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 113</div>
        <div class="raw-q-text">Strata dipping at angles upto 45° are called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Moderately inclined strata</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Steeply inclined strata</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Plunge</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Overturned</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Moderately inclined strata)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Moderately inclined strata</div>
          <p>By standard structural geology conventions (Billings; Bangar, p. 162; Mahapatra), stratified rock layers dipping at angles between 15° and 45° (or <strong>angles upto 45°</strong>) are formally designated as <strong>moderately inclined strata</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Steeply inclined strata</div>
          <p>Steeply inclined strata have dip angles <strong>greater than 45°</strong> up to nearly vertical ($45^\circ\text{--}85^\circ$), forming symmetrical hogback ridges.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Plunge</div>
          <p>'Plunge' is the inclination of a <strong>linear feature</strong> (such as a fold hinge line or lineation) with the horizontal plane, not the planar dip of a bedding surface.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Overturned</div>
          <p>Overturned strata have been rotated through tectonic folding past the vertical (over $90^\circ$), such that original young beds underlie older beds.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Dip Magnitude Class</th>
              <th>Dip Angle ($\theta$)</th>
              <th>Geomorphological Ridge Form</th>
              <th>Rule of 'V's Behavior</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Gently Inclined</td><td>$&lt; 15^\circ$ (or $0^\circ\text{--}10^\circ$)</td><td>Mesa / Butte / Cuesta (Dip slope $&lt; 15^\circ$)</td><td>Forms sharp 'V' pointing upstream in valleys</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Moderately Inclined (Option A)</strong></td><td><strong>$15^\circ \le \theta \le 45^\circ$</strong></td><td><strong>Cuesta (Asymmetrical ridge)</strong></td><td>Forms distinct 'V' downstream if dip exceeds gradient</td></tr>
            <tr><td>Steeply Inclined (Option B)</td><td>$&gt; 45^\circ$</td><td>Hogback (Symmetrical razorback)</td><td>Forms shallow broad 'V' pointing downstream</td></tr>
            <tr><td>Vertical</td><td>$\theta = 90^\circ$</td><td>Vertical rib / wall</td><td>Cuts straight across valleys without any 'V'</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the difference between a cuesta and a hogback?</div>
        <div class="pq-ans">Answer: A cuesta has a gentle dip slope ($< 30^\circ\text{--}40^\circ$) and a steep scarp slope; a hogback has nearly equal steep slopes on both sides ($> 40^\circ\text{--}45^\circ$).</div>
        <div class="pq-exp">Moderately inclined strata produce cuestas; steeply inclined strata produce symmetrical hogbacks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why are cut slopes excavated in moderately inclined strata dipping into the roadway exceptionally dangerous?</div>
        <div class="pq-ans">Answer: If daylighted, the bedding plane acts as a planar slide surface where dip angle ($\theta$) exceeds the friction angle ($\phi$).</div>
        <div class="pq-exp">Translational planar rockslides occur spontaneously along moderately inclined beds ($20^\circ\text{--}45^\circ$) when the toe is excavated.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the Strike of an inclined stratum?</div>
        <div class="pq-ans">Answer: The compass direction of a horizontal line drawn on the bedding plane (perpendicular to true dip).</div>
        <div class="pq-exp">Strike is always exactly perpendicular to the direction of maximum (true) dip.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is Apparent Dip ($\alpha$) versus True Dip ($\theta$)?</div>
        <div class="pq-ans">Answer: True dip is the maximum inclination perpendicular to strike; apparent dip is the inclination along any other oblique direction ($\alpha < \theta$).</div>
        <div class="pq-exp">$\tan \alpha = \tan \theta \cdot \cos \beta$, where $\beta$ is the angle between strike and apparent dip direction.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What does the Rule of 'V's state when strata dip upstream?</div>
        <div class="pq-ans">Answer: The outcrop pattern in the valley forms a 'V' pointing upstream.</div>
        <div class="pq-exp">Whenever beds dip upstream (against the valley gradient), the outcrop 'V' invariably points upstream.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the relation between true bed thickness ($T$), outcrop width ($W$), and dip angle ($\theta$) on horizontal ground?</div>
        <div class="pq-ans">Answer: $T = W \cdot \sin \theta$</div>
        <div class="pq-exp">As dip angle increases, the outcrop width for the same true bed thickness narrows.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. In tunnel construction, which alignment relative to strike of inclined strata provides the most stable conditions?</div>
        <div class="pq-ans">Answer: Tunneling perpendicular to strike (cutting across beds), preferably driving into the dip.</div>
        <div class="pq-exp">Driving parallel to strike leaves entire sidewalls supported on a single dipping bedding plane, promoting sidewall sliding.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a clinometer used for in field geology?</div>
        <div class="pq-ans">Answer: Measuring the angle of dip of a geological plane or the plunge of a lineation.</div>
        <div class="pq-exp">A Brunton compass combines a magnetic needle for strike azimuth with a spirit-level clinometer for dip angle measurement.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Batch 9 Part A (Q106 - Q113)...")
    gen_q106()
    gen_q107()
    gen_q108()
    gen_q0109()
    gen_q0110()
    gen_q0111()
    gen_q0112()
    gen_q0113()
    print("Batch 9 Part A successfully generated!")
