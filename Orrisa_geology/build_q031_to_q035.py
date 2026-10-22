#!/usr/bin/env python3
"""
Masterclass Builder for Batch 3: Structural Geology (Q031 - Q035)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q031: Apparent Dip Calculation
# ==============================================================================
def generate_q031():
    title = "Q031: Trigonometry of True Dip vs. Apparent Dip in Mining Geology | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Geological Trigonometry"
    h1_title = "Q031: Trigonometry of True Dip vs. Apparent Dip in Mining Geology"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 31<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Dip & Strike, pp. 189–191, Fig. 7.2); Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 2, pp. 26–29); Marland P. Billings, <em>Structural Geology</em> (3rd Ed., pp. 412–418)."""

    part1 = r"""
  <!-- CARD 1: TRUE DIP VS APPARENT DIP -->
  <div class="card">
    <div class="card-header bg-blue">1. Geometric Principles: True Dip vs. Apparent Dip</div>
    <div class="card-body">
      <p>In structural geology and underground mining engineering, determining the geometric attitude of mineralized veins, fault planes, and sedimentary strata requires understanding the fundamental relationship between <strong>True Dip</strong> and <strong>Apparent Dip</strong>:</p>

      <ul>
        <li><strong>True Dip ($\delta$):</strong> The maximum vertical angle of inclination of a planar surface relative to the horizontal plane. It is measured strictly in a vertical plane oriented <strong>perpendicular ($90^\circ$) to the strike line</strong> of the bed. A plane has only <em>one unique true dip</em>.</li>
        <li><strong>Apparent Dip ($\delta'$):</strong> The vertical angle of inclination of a planar surface measured in any vertical cross-section oriented <strong>obliquely to the strike line</strong> (at an acute angle $\alpha$ relative to the true dip direction).</li>
        <li><strong>The Invariant Rule:</strong> Because true dip is the steepest line on a plane, <strong>apparent dip is always strictly less than true dip ($\delta' < \delta$)</strong> for any non-orthogonal section. As the cross-section approaches parallelism with strike ($\alpha \to 90^\circ$), apparent dip approaches zero ($\delta' \to 0^\circ$).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">The Fundamental Apparent Dip Trigonometric Equation</div>
        $$\tan\delta' = \tan\delta \cdot \cos\alpha$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $\delta$ is True Dip, $\delta'$ is Apparent Dip, and $\alpha$ is the horizontal angle between the True Dip direction and the Apparent Dip direction ($\alpha = |\text{True Dip Azimuth} - \text{Apparent Dip Azimuth}|$).</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q31/bangar_fig7_2_true_apparent_dip.png" alt="True Dip and Apparent Dip from Bangar">
        <div class="tb-caption">
          <strong>Figure 31.1 (K.M. Bangar, Fig. 7.2):</strong> Geometric block diagram illustrating the 3D trigonometric relationship between True Dip ($\delta$) perpendicular to strike and Apparent Dip ($\delta'$) in an oblique vertical section.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: STEP-BY-STEP DERIVATION FOR THE SULPHIDE VEIN -->
  <div class="card">
    <div class="card-header bg-indigo">2. Step-by-Step Analytical Calculation for the Sulphide Vein</div>
    <div class="card-body">
      <p>Given parameters for the sulphide vein in Question 31:</p>
      <ul>
        <li><strong>True Dip ($\delta$):</strong> $50^\circ$ toward $\text{N}45^\circ\text{W}$ (Azimuth $315^\circ$).</li>
        <li><strong>Direction of Apparent Dip Section:</strong> $\text{N}20^\circ\text{W}$ (Azimuth $340^\circ$).</li>
        <li><strong>Angle Between Directions ($\alpha$):</strong> $\alpha = 45^\circ - 20^\circ = 25^\circ$.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Analytical Solution</div>
        $$\tan\delta' = \tan(50^\circ) \cdot \cos(25^\circ)$$
        $$\tan(50^\circ) \approx 1.19175 \qquad \cos(25^\circ) \approx 0.90631$$
        $$\tan\delta' = 1.19175 \times 0.90631 = 1.08009$$
        $$\delta' = \arctan(1.08009) \approx \mathbf{47.20^\circ} \approx \mathbf{45^\circ}$$
      </div>

      <p>Among the given multiple-choice options (55°, 35°, 25°, 45°), <strong>45°</strong> is the closest integer option and the only mathematically viable choice (since apparent dip must be $< 50^\circ$, eliminating 55°, and cannot be as low as 35° or 25° for a small angle of $\alpha = 25^\circ$).</p>

      <div class="tb-figure">
        <img src="../../figures_Q31/apparent_dip_true_dip_nomogram_trigonometry.png" alt="Apparent Dip Nomogram and Trigonometry">
        <div class="tb-caption">
          <strong>Figure 31.2: Apparent Dip Nomogram & Trigonometric Verification.</strong> Plotting $\delta = 50^\circ$ and $\alpha = 25^\circ$ yields an apparent dip $\delta' \approx 47^\circ$, validating option 45°.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Alternative Angles</div>
    <div class="card-body">
      <p>Forensic analysis of the options:</p>
      <ul>
        <li><strong>55° (Option A):</strong> Physically impossible! Apparent dip can NEVER exceed true dip ($\delta' \le \delta$). A value of $55^\circ > 50^\circ$ violates basic geometry.</li>
        <li><strong>35° (Option B):</strong> Corresponds to an angle $\alpha \approx 54^\circ$ from true dip ($\tan 35^\circ / \tan 50^\circ = 0.700 / 1.192 = 0.587 \implies \cos^{-1}(0.587) \approx 54^\circ$), far larger than the actual $25^\circ$.</li>
        <li><strong>25° (Option C):</strong> Corresponds to an angle $\alpha \approx 67^\circ$ from true dip.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 31)</div>
    <div class="q-stmt">
      Q31. A sulphide vein dips 50° toward N45°W. Its apparent dip toward of N20°W will be around _____ :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) 55°</div>
      <div class="raw-opt">(B) 35°</div>
      <div class="raw-opt">(C) 25°</div>
      <div class="raw-opt correct">(D) 45° &nbsp;✔</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) 45°</div>
      <div class="sub">
        Using the standard apparent dip equation $\tan\delta' = \tan\delta \cdot \cos\alpha$ with true dip $\delta = 50^\circ$ and $\alpha = 45^\circ - 20^\circ = 25^\circ$: $\tan\delta' = 1.19175 \times 0.90631 = 1.0801 \implies \delta' \approx 47.2^\circ$, which is approximately <strong>45°</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) 55°</span>
      <span class="tag wrong">Incorrect (Geometrically Impossible: Exceeds True Dip)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Apparent dip is measured obliquely to true dip and can <em>never</em> exceed true dip ($\delta' \le \delta$). Because the true dip of the vein is 50°, an apparent dip of 55° is a physical impossibility.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) 35°</span>
      <span class="tag wrong">Incorrect (Severe Underestimation)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> An apparent dip of 35° would require the section to be oriented at $\alpha \approx 54^\circ$ away from true dip direction (i.e., toward $\text{N}09^\circ\text{E}$), whereas $\text{N}20^\circ\text{W}$ is only $25^\circ$ away.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 25°</span>
      <span class="tag wrong">Incorrect (Confuses Angle Between Bearings with Apparent Dip)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> 25° is the horizontal angle between the true dip bearing ($\text{N}45^\circ\text{W}$) and the apparent dip bearing ($\text{N}20^\circ\text{W}$), i.e., $\alpha = 45^\circ - 20^\circ = 25^\circ$. Conflating $\alpha$ with the resulting vertical apparent dip angle $\delta'$ is a classic trap.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) 45°</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By the fundamental formula $\tan\delta' = \tan\delta \cdot \cos\alpha$:
      $$\tan\delta' = \tan(50^\circ) \cdot \cos(25^\circ) = 1.19175 \times 0.90631 = 1.0801 \implies \delta' \approx 47.2^\circ$$
      Rounding to the nearest multiple of 5° in standard examination formatting yields <strong>45°</strong>.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Apparent Dip ($\delta'$) Look-Up Table for True Dip $\delta = 50^\circ$</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Angle from True Dip ($\alpha$)</th>
            <th>Bearing Example (True Dip $\text{N}45^\circ\text{W}$)</th>
            <th>$\cos\alpha$ Factor</th>
            <th>$\tan\delta' = \tan 50^\circ \cos\alpha$</th>
            <th>Calculated Apparent Dip ($\delta'$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>$0^\circ$ (True Dip Direction)</td>
            <td>$\text{N}45^\circ\text{W}$</td>
            <td>$1.0000$</td>
            <td>$1.1918$</td>
            <td><strong>$50.0^\circ$ (Maximum True Dip)</strong></td>
          </tr>
          <tr>
            <td>$10^\circ$</td>
            <td>$\text{N}35^\circ\text{W}$ / $\text{N}55^\circ\text{W}$</td>
            <td>$0.9848$</td>
            <td>$1.1736$</td>
            <td>$49.6^\circ$</td>
          </tr>
          <tr>
            <td><strong>$25^\circ$ (Exam Question)</strong></td>
            <td><strong>$\text{N}20^\circ\text{W}$</strong></td>
            <td><strong>$0.9063$</strong></td>
            <td><strong>$1.0801$</strong></td>
            <td><strong>$\mathbf{47.2^\circ \approx 45^\circ}$</strong></td>
          </tr>
          <tr>
            <td>$45^\circ$</td>
            <td>North ($000^\circ$) / West ($270^\circ$)</td>
            <td>$0.7071$</td>
            <td>$0.8427$</td>
            <td>$40.1^\circ$</td>
          </tr>
          <tr>
            <td>$60^\circ$</td>
            <td>$\text{N}15^\circ\text{E}$</td>
            <td>$0.5000$</td>
            <td>$0.5959$</td>
            <td>$30.8^\circ$</td>
          </tr>
          <tr>
            <td>$90^\circ$ (Along Strike Line)</td>
            <td>$\text{N}45^\circ\text{E}$ / $\text{S}45^\circ\text{W}$</td>
            <td>$0.0000$</td>
            <td>$0.0000$</td>
            <td><strong>$0.0^\circ$ (Horizontal Bedding Trace)</strong></td>
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
          <strong>Practice Q1 (Numerical):</strong> A limestone bed dips $30^\circ$ due East ($090^\circ$). What is its apparent dip in a railway cutting oriented toward $\text{N}30^\circ\text{E}$ ($030^\circ$)?
          <div class="pq-ans">✔ Worked Answer: $\delta' \approx 16.1^\circ$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            Angle $\alpha = 90^\circ - 30^\circ = 60^\circ$.<br>
            $$\tan\delta' = \tan(30^\circ) \cdot \cos(60^\circ) = (0.5774) \times (0.5000) = 0.2887$$<br>
            $$\delta' = \arctan(0.2887) \approx 16.1^\circ$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Two apparent dips of a bedding plane measured in two different quarry faces are $\delta_1' = 20^\circ$ toward South ($180^\circ$) and $\delta_2' = 20^\circ$ toward East ($090^\circ$). What is the true dip direction of the bed?
          <div class="pq-ans">✔ Correct Answer: $\text{S}45^\circ\text{E}$ ($135^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the two apparent dips are identical ($20^\circ$), the true dip direction must lie exactly midway between South and East, bisecting the $90^\circ$ angle at $135^\circ$ ($\text{S}45^\circ\text{E}$).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> In civil tunneling, why must tunnel engineers compute apparent dip rather than relying on true dip?
          <div class="pq-ans">✔ Correct Answer: Because tunnels rarely drive perpendicular to regional strike; the apparent dip in the tunnel's vertical alignment governs roof stability and rock bolts.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The apparent dip dictates how bedding planes intersect the tunnel crown and sidewalls, controlling potential block daylighting and wedge failures.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is the apparent dip of any planar geological surface in a vertical section drawn parallel to the strike of the surface?
          <div class="pq-ans">✔ Correct Answer: Exactly $0^\circ$ (horizontal).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because $\alpha = 90^\circ$, $\cos(90^\circ) = 0$, meaning $\tan\delta' = 0 \implies \delta' = 0^\circ$. Layers appear perfectly horizontal in a strike cross-section.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How can True Dip ($\delta$) be calculated if two apparent dips ($\delta_1', \delta_2'$) and their horizontal angle separation ($\beta$) are known?
          <div class="pq-ans">✔ Correct Answer: Using Cotangent Nomograms or Stereonet intersection of two apparent dip pitch lines.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> On a stereonet, plotting the two apparent dip lines as points defines a unique great circle whose dip angle represents the true dip.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What happens to apparent dip if a vertical borehole intersects an inclined coal seam?
          <div class="pq-ans">✔ Correct Answer: The apparent dip measured on the horizontal core face equals the True Dip.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The core axis is vertical, so the angle between the core axis and the bedding plane normal directly reveals true dip ($\delta = 90^\circ - \theta_{\text{core}}$).
          </div>
        </li>

        <li>
          <strong>Practice Q7 (Numerical):</strong> A fault has a true dip $\delta = 45^\circ$. At what angle $\alpha$ from the true dip direction will the apparent dip be exactly $30^\circ$?
          <div class="pq-ans">✔ Worked Answer: $\alpha \approx 54.7^\circ$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\cos\alpha = \frac{\tan(30^\circ)}{\tan(45^\circ)} = \frac{0.57735}{1.0000} = 0.57735 \implies \alpha = \arccos(0.57735) \approx 54.74^\circ$$
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why is the true dip of a planar bed always steeper than any of its apparent dips?
          <div class="pq-ans">✔ Correct Answer: Because true dip follows the gradient of steepest descent on the plane ($90^\circ$ to horizontal contour/strike lines).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Any oblique cross-section traverses a longer horizontal distance for the same vertical elevation drop, reducing the slope gradient ($\tan\delta' = \Delta z / \Delta x_{\text{oblique}} < \Delta z / \Delta x_{\text{true}}$).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 31, part1, part2, part3)


# ==============================================================================
# Q032: Himalayan Collisional Deformation
# ==============================================================================
def generate_q032():
    title = "Q032: Himalayan Collisional Orogenesis: Folds and Reverse Fault Systems | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geotectonics & Himalayan Geology"
    h1_title = "Q032: Himalayan Collisional Orogenesis: Folds and Reverse Fault Systems"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 32<br>
<strong>Authoritative References:</strong> K.S. Valdiya, <em>The Making of India: Geodynamic Evolution</em> (2nd Ed., Springer); Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 16: Orogenesis); Gansser, A., <em>Geology of the Himalayas</em> (Wiley, 1964); van der Pluijm & Marshak, <em>Earth Structure</em> (Fig. 21.21)."""

    part1 = r"""
  <!-- CARD 1: CONTINENTAL COLLISION & CONTRACTIONAL SHORTENING -->
  <div class="card">
    <div class="card-header bg-blue">1. The Himalayan Collisional Orogenic System</div>
    <div class="card-body">
      <p>The Himalayan Mountain Belt is Earth's premier active archetype of an <strong>in-sequence continent-continent collisional orogen</strong>. Initiated approximately $50 - 55\text{ million years ago}$ (Early Eocene) following the closure of the Neo-Tethys Ocean and the collision of the Indian Plate with the Eurasian Plate, the orogen accommodates roughly $15 - 20\text{ mm/yr}$ of ongoing horizontal tectonic convergence:</p>

      <ul>
        <li><strong>Contractional Tectonic Regime:</strong> Because continental lithosphere is buoyant and cannot be subducted deep into the mantle, convergence is accommodated by colossal <strong>crustal shortening and vertical thickening</strong> (doubling crustal thickness up to $70 - 75\text{ km}$ beneath the Tibetan Plateau).</li>
        <li><strong>Primary Deformational Structures:</strong> By fundamental structural mechanics, horizontal compression ($\sigma_1$ horizontal and oriented NNE-SSW) produces two dominant, ubiquitous structural styles throughout the Himalayas: <strong>Folds</strong> (anticlinoria, synclinoria, recumbent folds, nappes) and <strong>Reverse / Thrust Faults</strong> (south-vergent imbricate thrust sheets).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q32/vdp_fig21_21_india_asia_tethys_collision.png" alt="India Asia Collision Tethys from van der Pluijm and Marshak">
        <div class="tb-caption">
          <strong>Figure 32.1 (van der Pluijm & Marshak, Fig. 21.21):</strong> Geodynamic cross-section of the India-Asia continental collision. Shows horizontal contraction generating south-vergent crustal thrust wedges and colossal folds.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE FOUR MASTER HIMALAYAN THRUST SYSTEMS -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Foreland-Propagating Thrust Belt: MFT, MBT, and MCT</div>
    <div class="card-body">
      <p>The entire $2400\text{ km}$ arc of the Himalayas is partitioned into distinct lithotectonic zones bounded by four master south-verging <strong>thrust faults (reverse faults)</strong> and folded nappes:</p>

      <ul>
        <li><strong>1. Main Frontal Thrust (MFT / HFT):</strong> The southernmost active thrust fault, placing Neogene-Quaternary folded Siwalik molasses over the Indo-Gangetic Alluvial Plain.</li>
        <li><strong>2. Main Boundary Thrust (MBT):</strong> Separates the folded Siwalik group from the highly folded and faulted Proterozoic Lesser Himalayan sedimentary sequence.</li>
        <li><strong>3. Main Central Thrust (MCT):</strong> A colossal ductile shear zone and low-angle thrust dipping north, placing the high-grade metamorphic Higher Himalayan Crystalline Sequence (HHC) over the Lesser Himalayas.</li>
        <li><strong>4. Main Himalayan Thrust (MHT):</strong> The basal mega-decollement detachment underlying the entire orogen at $15 - 30\text{ km}$ depth, upon which all major Himalayan earthquakes nucleate.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q32/himalayan_thrust_belt_mct_mbt_mft.png" alt="Himalayan Thrust Belt Architecture MCT MBT MFT">
        <div class="tb-caption">
          <strong>Figure 32.2: Architecture of the Himalayan Thrust Belt.</strong> Cross-section showing in-sequence forward thrust propagation: MCT, MBT, and MFT, accommodating horizontal shortening via folding and reverse faulting.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Normal Faulting Distractors</div>
    <div class="card-body">
      <p>Candidates must clearly refute options containing normal faults:</p>
      <ul>
        <li><strong>Normal Faults (Options A & C):</strong> Normal faults require horizontal <em>crustal extension</em> ($\sigma_1$ vertical, $\sigma_3$ horizontal). While minor localized normal faulting occurs high in the orogenic superstructure due to gravitational collapse (e.g., South Tibetan Detachment System, STDS), the regional tectonic deformation of the Himalayan mountain belt is overwhelmingly <strong>contractional</strong>. Claiming normal faults are the common deformational structure is geodynamically false.</li>
      </ul>

      <div class="quote-box">
        "The Himalayan orogen is characterized by intense crustal shortening accommodated by south-verging thrust faults and associated asymmetric to recumbent folds... The major tectonic boundaries (MCT, MBT, MFT) are all contractional reverse/thrust fault systems."
        <span class="quote-ref">— K.S. Valdiya, <em>The Making of India: Geodynamic Evolution</em> (2016, pp. 385–395)</span>
      </div>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 32)</div>
    <div class="q-stmt">
      Q32. Rocks are deformed in the Himalayan mountain belt commonly forms which deformational structures ?
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Folds and normal faults</div>
      <div class="raw-opt correct">(B) Folds and reverse faults &nbsp;✔</div>
      <div class="raw-opt">(C) Normal faults and reverse faults</div>
      <div class="raw-opt">(D) None of these</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Folds and reverse faults</div>
      <div class="sub">
        As a direct result of ongoing NNE-directed continental collision and crustal shortening between the Indian and Eurasian plates, rocks in the Himalayan mountain belt are overwhelmingly deformed into <strong>Folds and reverse faults</strong> (including major thrust nappes like the MCT, MBT, and MFT).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Folds and normal faults</span>
      <span class="tag wrong">Incorrect (Normal Faults Indicate Extensional Regimes)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Normal faults are characteristic of extensional rift settings (such as the East African Rift or Basin and Range). The Himalayas represent an active convergent orogen dominated by compressive stress, not regional extension.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Folds and reverse faults</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Under horizontal compressive stress ($\sigma_1$ horizontal), rocks deform via horizontal shortening and vertical thickening, generating extensive fold systems (anticlinoria, synclinoria, recumbent folds) and south-vergent reverse/thrust fault systems (MCT, MBT, MFT) that define the Himalayan architecture.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Normal faults and reverse faults</span>
      <span class="tag wrong">Incorrect (Omits Fundamental Folding & Includes Extensional Faults)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Folding is the most prominent structural feature visible in Himalayan outcrops (e.g., Krol and Garhwal nappes). Omitting folds while including extensional normal faults misrepresents orogenic geodynamics.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) None of these</span>
      <span class="tag wrong">Incorrect (Valid Answer Exists in Option B)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Option (B) is the universally established, textbook consensus across all Indian and international geology literature.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Structural Framework of the Himalayan Orogen</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Tectonic Unit / Sub-Division</th>
            <th>Boundary Faults</th>
            <th>Dominant Lithologies</th>
            <th>Primary Deformational Structures</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Sub-Himalaya (Siwaliks)</strong></td>
            <td>MFT (South) / MBT (North)</td>
            <td>Neogene-Quaternary fluvial sandstones, conglomerates, shales</td>
            <td>Asymmetric fault-propagation folds, blind thrusts, piggyback basins (Duns)</td>
          </tr>
          <tr>
            <td><strong>Lesser Himalaya</strong></td>
            <td>MBT (South) / MCT (North)</td>
            <td>Proterozoic quartzites, stromatolitic limestones, phyllites</td>
            <td>Colossal synformal nappes (Krol, Almora, Garhwal), tight isoclinal folds, thrusts</td>
          </tr>
          <tr>
            <td><strong>Higher Himalaya (HHC)</strong></td>
            <td>MCT (South) / STDS (North)</td>
            <td>High-grade paragneisses, migmatites, leucogranites</td>
            <td>Polyphase ductile folding ($F_1, F_2, F_3$), shear zones, ductile recumbent folds</td>
          </tr>
          <tr>
            <td><strong>Tethyan Himalaya</strong></td>
            <td>STDS (South) / ITSZ (North)</td>
            <td>Neoproterozoic to Eocene fossiliferous marine sediments</td>
            <td>Detachment fold-and-thrust belt; back-thrusts; chevron folds</td>
          </tr>
          <tr>
            <td><strong>Indus-Tsangpo Suture (ITSZ)</strong></td>
            <td>Northern boundary</td>
            <td>Ophiolites, melanges, blueschists</td>
            <td>Subduction accretionary prism; vertical strike-slip shear zones</td>
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
          <strong>Practice Q1:</strong> What is a <em>Dun valley</em> (e.g., Dehradun) in Himalayan structural geomorphology?
          <div class="pq-ans">✔ Correct Answer: A longitudinal synclinal piggyback basin (intermontane valley) enclosed between the Siwalik hills and the Lesser Himalaya.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Duns develop behind the active Main Frontal Thrust (MFT) as fault-bend fold gravels aggrade in piggyback synclines.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What singular structural exception in the Himalayas exhibits normal faulting, and what causes it?
          <div class="pq-ans">✔ Correct Answer: The South Tibetan Detachment System (STDS); caused by gravitational orogenic collapse and ductile extrusion (channel flow) of the Higher Himalayan Crystallines.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> While the base of the HHC was thrust south along the MCT, its top collapsed north along the low-angle normal STDS during the Miocene.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the direction of tectonic transport (vergence) of the major folds and thrusts throughout the Himalayas?
          <div class="pq-ans">✔ Correct Answer: South to South-Southwest vergence (toward the Indian foreland).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Underthrusting of the Indian craton beneath Asia drives top-to-the-south reverse displacement across all major thrusts.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is the <em>Main Himalayan Thrust (MHT)</em>?
          <div class="pq-ans">✔ Correct Answer: The master basal decollement dipping gently ($\sim 5^\circ - 10^\circ$) northward, which roots all frontal thrusts (MFT, MBT, MCT).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The MHT accommodates the entire convergence budget and is locked over a $100\text{ km}$ width, rupturing periodically in giant earthquakes (e.g., 2015 Gorkha earthquake).
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> In Himachal Pradesh and Uttarakhand, the Almora and Shimla crystalline masses are preserved in the core of what structural feature?
          <div class="pq-ans">✔ Correct Answer: Synformal klippen (klippes).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Erosion removed the Higher Himalayan thrust sheet over anticlinal arches, leaving crystalline rocks preserved only in down-warped synformal depressions (klippen).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the average rate of active horizontal convergence between the Indian Plate and Eurasian Plate across the Himalayas?
          <div class="pq-ans">✔ Correct Answer: Approximately $35 - 40\text{ mm/yr}$ total convergence, with $15 - 20\text{ mm/yr}$ absorbed across the Himalayan thrust belt.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> About half the convergence is accommodated by Himalayan thrust shortening, and the remainder by internal deformation and eastward extrusion of Tibet.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> The Main Boundary Thrust (MBT) places which older rock unit over which younger rock unit?
          <div class="pq-ans">✔ Correct Answer: Proterozoic Lesser Himalayan metasediments over Neogene Siwalik molasse sediments.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The MBT represents a major in-sequence contractional boundary active during the Pliocene-Pleistocene.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why do transverse river gorges (such as the Kali Gandaki and Indus) cut across the highest Himalayan peaks?
          <div class="pq-ans">✔ Correct Answer: Antecedent drainage; rivers established their flow courses prior to the tectonic uplift of the Higher Himalayan peaks and cut down as the mountains rose.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Downcutting rates equaled or exceeded orogenic uplift rates, creating the deepest river gorges on Earth.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 32, part1, part2, part3)


# ==============================================================================
# Q033: Recumbent Fold Axial Plane Dip Angle
# ==============================================================================
def generate_q033():
    title = "Q033: Fold Attitude Classification: Recumbent Fold Axial Surface Geometry | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Fold Geometry"
    h1_title = "Q033: Fold Attitude Classification: Recumbent Fold Axial Surface Geometry"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 33<br>
<strong>Authoritative References:</strong> Fleuty, M.J. (1964, <em>The Description of Folds</em>, Proc. Geol. Assoc., 75, pp. 461–492); Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 12, pp. 244–248, Fig. 12.8); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds, pp. 192–193, Fig. 7.6)."""

    part1 = r"""
  <!-- CARD 1: FLEUTY'S FOLD ATTITUDE CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-blue">1. Fleuty's (1964) Classification of Folds by Axial Plane Attitude</div>
    <div class="card-body">
      <p>In structural geology, the spatial orientation of a fold is rigorously classified based on two independent geometric criteria: the <strong>dip of its axial surface (axial plane)</strong> and the <strong>plunge of its hinge line</strong>. In M.J. Fleuty's (1964) internationally accepted standard classification, folds are categorized by axial plane dip:</p>

      <table>
        <thead>
          <tr>
            <th>Fold Type (Fleuty, 1964)</th>
            <th>Dip of Axial Surface ($\theta_{\text{AP}}$)</th>
            <th>Limb Attitude & Stratigraphic Inversion</th>
            <th>Characteristic Kinematic Environment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Upright Fold</strong></td>
            <td>$80^\circ - 90^\circ$ (Vertical)</td>
            <td>Both limbs dip at equal angles in opposite directions; normal younging</td>
            <td>Symmetrical horizontal compression</td>
          </tr>
          <tr>
            <td><strong>Steeply Inclined Fold</strong></td>
            <td>$60^\circ - 80^\circ$</td>
            <td>Both limbs dip in opposite directions; one limb steeper</td>
            <td>Moderate tectonic asymmetry</td>
          </tr>
          <tr>
            <td><strong>Moderately Inclined Fold</strong></td>
            <td>$30^\circ - 60^\circ$</td>
            <td>Both limbs dip in opposite directions; asymmetrical</td>
            <td>Orogenic contractional belts</td>
          </tr>
          <tr>
            <td><strong>Gently Inclined / Overturned</strong></td>
            <td>$10^\circ - 30^\circ$</td>
            <td>One limb overturned (inverted stratigraphy); limbs dip in same direction</td>
            <td>Intense asymmetric tectonic shear</td>
          </tr>
          <tr>
            <td><strong>Recumbent Fold</strong></td>
            <td><strong>$0^\circ - 10^\circ$ (Horizontal or Sub-horizontal: $\approx 0^\circ$)</strong></td>
            <td><strong>Axial surface is horizontal; inverted (overturned) lower limb</strong></td>
            <td><strong>Large-scale crustal nappe translation; Alpine/Himalayan thrust sheets</strong></td>
          </tr>
        </tbody>
      </table>

      <div class="tb-figure">
        <img src="../../figures_Q33/fossen_fig12_8_fold_shapes_inverted_limbs.png" alt="Fold Shapes by Axial Plane Dip from Haakon Fossen">
        <div class="tb-caption">
          <strong>Figure 33.1 (Haakon Fossen, <em>Structural Geology</em>, Fig. 12.8):</strong> Fleuty's fold classification by axial plane dip, showing the progression from Upright ($90^\circ$) to Overturned and Recumbent ($0^\circ$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MORPHOLOGY OF A RECUMBENT FOLD -->
  <div class="card">
    <div class="card-header bg-indigo">2. Anatomical Architecture of a Recumbent Fold</div>
    <div class="card-body">
      <p>A <strong>Recumbent Fold</strong> represents the ultimate extreme of overturned folding, where intense horizontal shear completely overturns the fold until its axial plane lies <strong>essentially horizontal ($\approx 0^\circ$)</strong>:</p>

      <ul>
        <li><strong>Normal Limb (Upper Limb):</strong> The upper limb of the recumbent fold, which retains normal upright stratigraphic younging (older beds below, younger beds above).</li>
        <li><strong>Inverted Limb (Middle / Lower Limb):</strong> The lower limb, which has been rotated through more than $90^\circ$, causing the stratigraphic succession to be completely upside-down (inverted stratigraphy: younger beds below, older beds above).</li>
        <li><strong>Recumbent Nappes:</strong> When recumbent folds are sheared along their attenuated inverted limbs, they transition into <em>thrust nappes</em> (fold-nappes, e.g., the Morcles nappe in the Swiss Alps, or the Garhwal nappe in the Himalayas).</li>
      </ul>

      <div class="quote-box bangar">
        "Recumbent Fold: In this type of fold, the compressive forces are so intense that the fold is completely overturned, and the axial plane becomes practically horizontal (dips at 0° or nearly so). The limbs are horizontal or sub-horizontal, and one limb is completely overturned with inverted stratigraphy."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds, p. 193, Fig. 7.6)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q33/bangar_fig7_6_recumbent_fold.png" alt="Recumbent Fold from Bangar">
        <div class="tb-caption">
          <strong>Figure 33.2 (K.M. Bangar, Fig. 7.6):</strong> Authentic cross-section of a Recumbent Fold with a horizontal axial surface ($0^\circ$ dip), showing the normal upper limb and inverted lower limb.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of 90°, 60°, and 45° Dip Angles</div>
    <div class="card-body">
      <p>Candidate elimination based on Fleuty's boundaries:</p>
      <ul>
        <li><strong>90° (Option C):</strong> Defines an <strong>Upright fold</strong> with a perfectly vertical axial plane.</li>
        <li><strong>60° (Option B):</strong> Defines a <strong>Moderately to Steeply Inclined fold</strong>.</li>
        <li><strong>45° (Option A):</strong> Defines an <strong>Inclined or Overturned fold</strong>, not a recumbent fold.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 33)</div>
    <div class="q-stmt">
      Q33. In a recumbent fold, the axial plane dips about _____ :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) 45°</div>
      <div class="raw-opt">(B) 60°</div>
      <div class="raw-opt">(C) 90°</div>
      <div class="raw-opt correct">(D) 0° &nbsp;✔</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) 0°</div>
      <div class="sub">
        By standard structural definition (Fleuty 1964; Bangar p. 193; Fossen p. 244), the defining geometric criterion of a <strong>recumbent fold</strong> is that its axial surface is horizontal or essentially horizontal, dipping at approximately <strong>0°</strong> ($0^\circ - 10^\circ$).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) 45°</span>
      <span class="tag wrong">Incorrect (Moderately Inclined / Overturned Fold)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> An axial plane dipping at 45° characterizes an <em>inclined fold</em> or an <em>overturned fold</em>. It is far too steep to be classified as recumbent.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) 60°</span>
      <span class="tag wrong">Incorrect (Steeply Inclined Fold)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A dip of 60° places the fold into the <em>steeply inclined fold</em> category under Fleuty's classification.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 90°</span>
      <span class="tag wrong">Incorrect (Upright Symmetrical Fold)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> An axial plane dipping at 90° defines an <strong>upright fold</strong>, which is the exact polar opposite of a recumbent fold.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) 0°</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Derived from the Latin <em>recumbere</em> ("to recline or lie down"), a <strong>recumbent fold</strong> is geometrically defined as a fold whose axial surface is horizontal ($\approx 0^\circ$). The fold has been overturned so severely that its limbs and axial plane lie flat.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Fleuty (1964) Classification of Folds by Axial Surface Dip</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Fold Classification</th>
            <th>Dip of Axial Surface ($\theta_{\text{AP}}$)</th>
            <th>Attitude of Limbs</th>
            <th>Stratigraphic Younging Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Upright Fold</strong></td>
            <td>$80^\circ - 90^\circ$</td>
            <td>Both limbs dip steeply in opposite directions</td>
            <td>Both limbs normal (younger upwards)</td>
          </tr>
          <tr>
            <td><strong>Steeply Inclined</strong></td>
            <td>$60^\circ - 80^\circ$</td>
            <td>Both limbs dip in opposite directions at unequal angles</td>
            <td>Both limbs normal</td>
          </tr>
          <tr>
            <td><strong>Moderately Inclined</strong></td>
            <td>$30^\circ - 60^\circ$</td>
            <td>Asymmetrical limbs; one limb dip $< 45^\circ$</td>
            <td>Both limbs normal</td>
          </tr>
          <tr>
            <td><strong>Gently Inclined / Overturned</strong></td>
            <td>$10^\circ - 30^\circ$</td>
            <td>Both limbs dip in the same direction</td>
            <td>Lower limb inverted (upside-down)</td>
          </tr>
          <tr>
            <td><strong>Recumbent Fold</strong></td>
            <td><strong>$0^\circ - 10^\circ$ ($\approx 0^\circ$, Horizontal)</strong></td>
            <td><strong>Limbs are horizontal to sub-horizontal</strong></td>
            <td><strong>Lower limb completely inverted over regional scale</strong></td>
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
          <strong>Practice Q1:</strong> In an overturned fold, what field criterion proves that the middle limb is stratigraphically inverted?
          <div class="pq-ans">✔ Correct Answer: Inverted primary sedimentary structures (e.g., cross-bedding truncated at bottom, inverted graded bedding, or downward-pointing pillow lavas).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because bedding dips normally, only geopetal way-up indicators prove that the strata are completely upside-down.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>fold-nappe</em>?
          <div class="pq-ans">✔ Correct Answer: A colossal recumbent fold whose middle inverted limb is stretched, thinned, and translated horizontally tens of kilometers.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Classic examples include the Penninic nappes of the Alps, where recumbent folds travel over $50\text{ km}$ across basement rocks.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the difference between a <em>reclined fold</em> and a <em>recumbent fold</em>?
          <div class="pq-ans">✔ Correct Answer: A recumbent fold has a horizontal axial plane ($0^\circ$); a reclined fold has an inclined axial plane where the hinge line plunges down the true dip of the axial plane (rake $= 90^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In a reclined fold, plunge equals dip, and the hinge points straight down the axial plane.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In an upright symmetrical fold, how does the axial plane orient relative to the interlimb angle?
          <div class="pq-ans">✔ Correct Answer: It exactly bisects the interlimb angle.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Symmetrical folds have identical limb lengths and equal dips, causing the axial surface to be the exact bisecting plane.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How do parasitic folds ($S$-folds, $Z$-folds, $M$-folds) relate to the axial plane of a major recumbent fold?
          <div class="pq-ans">✔ Correct Answer: Their axial surfaces are parallel to the master axial plane, with $M$-folds occurring in the hinge zone and $S$/$Z$-folds on the limbs.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Pumpelly's Rule states that minor parasitic fold axes and axial surfaces are parallel to the major tectonic fold structure.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What cleavage type forms parallel to the horizontal axial plane of a recumbent fold?
          <div class="pq-ans">✔ Correct Answer: Horizontal to sub-horizontal axial planar cleavage ($S_1$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Recumbent folding reorients metamorphic mica grains into horizontal foliation planes parallel to the flat axial surface.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Can a recumbent fold have a steeply plunging hinge line?
          <div class="pq-ans">✔ Correct Answer: No; because the axial plane is horizontal ($0^\circ$), any line lying within it must also be horizontal ($0^\circ$ plunge).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> By geometry, a line lying on a horizontal plane can only have a plunge of $0^\circ$.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a <em>box fold</em>?
          <div class="pq-ans">✔ Correct Answer: A fold having a broad, flat crest and two distinct hinge lines with two conjugate axial planes dipping toward each other.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Box folds (conjugate folds) form where two conjugate shear bands or slip surfaces interact, creating a trapezoidal profile.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 33, part1, part2, part3)


# ==============================================================================
# Q034: Upper Crust Low P-T Brittle Deformation
# ==============================================================================
def generate_q034():
    title = "Q034: Crustal Rheology: The Brittle-Ductile Transition & Upper Crust Mechanics | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geodynamics & Crustal Rheology"
    h1_title = "Q034: Crustal Rheology: The Brittle-Ductile Transition & Upper Crust Mechanics"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 34<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 7: Brittle Deformation, pp. 135–158); Kohlstedt, Evans & Mackwell (1995, <em>Strength of the lithosphere</em>, JGR, 100); Sibson, R.H. (1977, <em>Fault rocks and fault mechanisms</em>, J. Geol. Soc. London, 133); Byerlee, J. (1978, <em>Friction of rocks</em>, Pure Appl. Geophys., 116)."""

    part1 = r"""
  <!-- CARD 1: THE BRITTLE-DUCTILE CRUSTAL PROFILE -->
  <div class="card">
    <div class="card-header bg-blue">1. The Strength Envelope of the Continental Crust</div>
    <div class="card-body">
      <p>In structural geology and geodynamics (Sibson, 1977; Kohlstedt et al., 1995; Fossen, 2016), the mechanical behavior of continental crust is governed by the vertical geothermal gradient ($dT/dz \approx 25 - 30^\circ\text{C/km}$) and lithostatic pressure gradient ($dP/dz \approx 27\text{ MPa/km}$). This produces a fundamental two-tier rheological structure separated by the <strong>Brittle-Ductile Transition (BDT)</strong>:</p>

      <ul>
        <li><strong>Upper Crust ($0 - 10\text{ to } 15\text{ km}$; Low $P$ & $T$):</strong> Temperatures are low ($T < 300^\circ\text{C}$) and confining pressures are low ($P < 300\text{ MPa}$). Under these low $P-T$ conditions, silicon-oxygen covalent bonds in quartz cannot activate crystal plastic deformation. Rocks behave in a <strong>Brittle manner</strong>, deforming through elastic strain, microcracking, frictional sliding along faults, and catastrophic seismogenic rupture.</li>
        <li><strong>Middle to Lower Crust ($> 10 - 15\text{ km}$; High $P$ & $T$):</strong> Temperatures exceed $300 - 350^\circ\text{C}$. Quartz activates crystal-plastic dislocation creep and dynamic recrystallization. Rocks deform in a <strong>Ductile manner</strong>, flowing permanently without macroscopic fracturing (forming mylonites and ductile shear zones).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Byerlee's Law of Upper Crustal Brittle Frictional Strength (1978)</div>
        $$\tau = 0.85 \cdot \sigma_n \quad (\text{for } \sigma_n < 200\text{ MPa})$$
        $$\tau = 50\text{ MPa} + 0.60 \cdot \sigma_n \quad (\text{for } \sigma_n > 200\text{ MPa})$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">In the brittle upper crust, rock strength increases linearly with depth (confining pressure $\sigma_n$) independent of temperature, lithology, or strain rate.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q34/brittle_ductile_transition_crustal_profile.png" alt="Brittle-Ductile Transition Crustal Strength Profile">
        <div class="tb-caption">
          <strong>Figure 34.1: Crustal Strength Profile ("Christmas Tree" Diagram).</strong> Showing the upper crust dominated by pressure-dependent Brittle deformation (Byerlee's Law), peaking at the Brittle-Ductile Transition zone ($\sim 10 - 15\text{ km}$), below which temperature-dependent Ductile flow dominates.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: FAULT ROCKS: BRITTLE CATACLASITES VS DUCTILE MYLONITES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Sibson's (1977) Fault Rock Architecture</div>
    <div class="card-body">
      <p>The transition from brittle to ductile processes with depth produces distinct textural fault rocks:</p>

      <table>
        <thead>
          <tr>
            <th>Crustal Regime</th>
            <th>Depth & Temperature</th>
            <th>Dominant Deformational Process</th>
            <th>Resulting Fault Rock Types</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Upper Crust (Near Surface)</strong></td>
            <td>$0 - 4\text{ km}$; $T < 100^\circ\text{C}$</td>
            <td><strong>Brittle:</strong> Frictional brecciation, dilation, gouge formation</td>
            <td><strong>Fault Breccia, Non-cohesive Fault Gouge</strong></td>
          </tr>
          <tr>
            <td><strong>Upper Crust (Seismogenic)</strong></td>
            <td>$4 - 10\text{ km}$; $T = 100 - 300^\circ\text{C}$</td>
            <td><strong>Brittle:</strong> Frictional sliding, grain crushing (cataclasis), pseudotachylyte friction melts</td>
            <td><strong>Cohesive Cataclasite, Pseudotachylyte</strong> (fossil earthquakes)</td>
          </tr>
          <tr>
            <td><strong>Middle to Lower Crust</strong></td>
            <td>$> 10 - 15\text{ km}$; $T > 300 - 450^\circ\text{C}$</td>
            <td><strong>Ductile:</strong> Crystal-plastic dislocation creep, dynamic recrystallization</td>
            <td><strong>Protomylonite, Mylonite, Ultramylonite, Blastosilicate gneisses</strong></td>
          </tr>
        </tbody>
      </table>

      <div class="quote-box">
        "In the upper crust, where temperatures and pressures are relatively low, deformation is dominated by brittle processes: fracture, friction, and cataclastic flow. Cataclasis involves mechanical microcracking, rotation, and frictional sliding of mineral fragments."
        <span class="quote-ref">— Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, 2016, p. 136)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q34/fossen_fig7_28_byerlees_law.png" alt="Byerlee's Law and Brittle Strength from Fossen">
        <div class="tb-caption">
          <strong>Figure 34.2 (Haakon Fossen, Fig. 7.28):</strong> Byerlee's empirical rock friction data, proving that brittle shear failure in the upper crust is strictly a function of normal stress, invariant across rock compositions.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Ductile, Dissolution, and Melting Distractors</div>
    <div class="card-body">
      <p>Candidates must clearly differentiate thermal thresholds:</p>
      <ul>
        <li><strong>(B) Ductile process:</strong> Requires elevated temperatures ($> 300^\circ\text{C}$ for quartz, $> 450^\circ\text{C}$ for feldspar) found in the middle and lower crust, not the low P-T upper crust.</li>
        <li><strong>(C) Dissolution (Pressure Solution):</strong> While pressure solution occurs in wet upper-crustal limestones and sandstones, it is a specialized mass-transfer mechanism; the primary, macroscopically dominant regional tectonic deformation mode is brittle fracture.</li>
        <li><strong>(D) Partial melting:</strong> Requires extreme temperatures ($> 650 - 700^\circ\text{C}$) found exclusively in the deep lower crust or mantle under granulite/migmatite facies.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 34)</div>
    <div class="q-stmt">
      Q34. In the upper crust where The P and T condition is relatively low, the deformational process dominant is :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Brittle process &nbsp;✔</div>
      <div class="raw-opt">(B) Ductile process</div>
      <div class="raw-opt">(C) Dissolution</div>
      <div class="raw-opt">(D) Partial melting</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Brittle process</div>
      <div class="sub">
        In the upper continental crust where confining pressure and temperature are relatively low ($T < 300^\circ\text{C}, P < 300\text{ MPa}$), rocks deform dominantly through <strong>Brittle processes</strong> (frictional sliding, fracturing, faulting, and cataclasis).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Brittle process</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Under the low pressure and temperature conditions of the upper $10 - 15\text{ km}$ of continental crust, silicate minerals cannot activate crystal-plastic dislocation glide. Instead, applied differential stress exceeds the frictional yield strength of the rock, causing deformation to be accommodated through brittle fracturing, jointing, cataclastic fault gouge generation, and seismogenic earthquakes.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Ductile process</span>
      <span class="tag wrong">Incorrect (Requires High Temperature in Middle/Lower Crust)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Ductile deformation (solid-state plastic flow and dynamic recrystallization) requires thermal activation ($T > 300^\circ\text{C}$), which only occurs at depths below the Brittle-Ductile Transition zone in the middle and lower crust.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Dissolution</span>
      <span class="tag wrong">Incorrect (Specialized Water-Assisted Mechanism)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Pressure solution (diffusive mass transfer) is an important local diagenetic and low-grade cleavage-forming process in wet porous sediments, but it is not the dominant macroscopic regional deformation regime of the crystalline upper crust.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Partial melting</span>
      <span class="tag wrong">Incorrect (Requires High-Grade Lower Crustal Temperatures > 650°C)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Partial melting (anatexis) produces migmatites and granitic magmas, requiring extreme metamorphic conditions ($T > 650 - 750^\circ\text{C}, P > 500\text{ MPa}$) characteristic of the deep root zones of collisional orogens, the exact antithesis of low P-T upper crust.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Crustal Deformation Regimes Matrix</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Crustal Zone</th>
            <th>Temperature & Depth</th>
            <th>Dominant Deformation Mode</th>
            <th>Microscopic Strain Mechanism</th>
            <th>Representative Fault Rocks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Upper Crust</strong></td>
            <td><strong>$T < 300^\circ\text{C}$<br>Depth: $0 - 12\text{ km}$</strong></td>
            <td><strong>Brittle Regime</strong></td>
            <td><strong>Microcracking, frictional sliding, grain rotation (Cataclasis)</strong></td>
            <td><strong>Fault Breccia, Fault Gouge, Cataclasite, Pseudotachylyte</strong></td>
          </tr>
          <tr>
            <td><strong>Brittle-Ductile Transition (BDT)</strong></td>
            <td>$T \approx 300 - 350^\circ\text{C}$<br>Depth: $10 - 15\text{ km}$</td>
            <td>Semi-brittle / Transitional</td>
            <td>Quartz is ductile (plastic flow); Feldspar remains brittle (fracturing)</td>
            <td>Protomylonite with fractured feldspar porphyroclasts</td>
          </tr>
          <tr>
            <td><strong>Middle to Lower Crust</strong></td>
            <td>$T > 350 - 650^\circ\text{C}$<br>Depth: $15 - 35\text{ km}$</td>
            <td>Ductile (Plastic) Regime</td>
            <td>Dislocation creep, subgrain rotation, dynamic recrystallization</td>
            <td>Mylonite, Ultramylonite, Ribbon Gneiss</td>
          </tr>
          <tr>
            <td><strong>Deep Lower Crust (Root Zone)</strong></td>
            <td>$T > 650 - 800^\circ\text{C}$<br>Depth: $> 30 - 40\text{ km}$</td>
            <td>Ductile Flow & Anatexis</td>
            <td>Diffusion creep, grain boundary sliding, partial melting</td>
            <td>Migmatites, Granulites</td>
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
          <strong>Practice Q1:</strong> What mineral acts as the primary "rheological thermometer" defining the Brittle-Ductile Transition in the continental crust at $\sim 300^\circ\text{C}$?
          <div class="pq-ans">✔ Correct Answer: Quartz ($\text{SiO}_2$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Quartz begins crystal plastic dislocation creep at $300^\circ\text{C}$. Because quartz is the weakest abundant mineral in granite, its ductile softening weakens the entire granitic crust.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> At what higher temperature does Feldspar undergo its brittle-ductile transition?
          <div class="pq-ans">✔ Correct Answer: Approximately $450^\circ - 500^\circ\text{C}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Between $300^\circ\text{C}$ and $450^\circ\text{C}$, quartz flows plastically around rigid, brittle-fracturing feldspar porphyroclasts, generating typical "core-and-mantle" mylonitic textures.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is a <em>pseudotachylyte</em>, and why is it considered the only unambiguous structural rock proof of an ancient earthquake?
          <div class="pq-ans">✔ Correct Answer: A dark, glassy to ultra-fine-grained rock formed by instantaneous frictional melting during high-velocity seismic fault rupture.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Coseismic slip ($> 1\text{ m/s}$) generates extreme flash heating along the fault surface ($> 1200^\circ\text{C}$), melting the rock into friction melt that quenches into glass.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Why does the maximum frequency of continental earthquakes terminate abruptly at depths below $15 - 20\text{ km}$?
          <div class="pq-ans">✔ Correct Answer: Rocks below the Brittle-Ductile Transition deform via continuous aseismic ductile creep, preventing elastic stress accumulation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Without brittle frictional locking, tectonic strain is released steadily by crystal plasticity without generating seismic stick-slip earthquakes.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How does increasing strain rate ($\dot{\epsilon}$) affect the depth of the Brittle-Ductile Transition?
          <div class="pq-ans">✔ Correct Answer: Higher strain rates push the BDT deeper into the crust (widens the brittle zone).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Fast strain rates do not provide enough time for thermally activated dislocation creep to occur, forcing rocks to fail brittly at higher temperatures.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What textural classification distinguishes a <em>Fault Breccia</em> from a <em>Cataclasite</em>?
          <div class="pq-ans">✔ Correct Answer: Fault breccia is non-cohesive and contains $> 30\%$ visible angular clasts; cataclasite is an indurated, cohesive rock with a pervasive fine-grained crushed matrix.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Breccias form at shallow depths ($< 4\text{ km}$); cataclasites form at deeper, cohesive brittle depths ($4 - 10\text{ km}$) where pressure lithifies crushed grains.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is <em>hydrofracturing (hydraulic fracturing)</em>, and what effective stress condition triggers it in the upper crust?
          <div class="pq-ans">✔ Correct Answer: When pore fluid pressure ($u$) exceeds the minimum principal stress ($\sigma_3$) plus the tensile strength of the rock ($u \ge \sigma_3 + T_0$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> High fluid pressure drives effective tensile stress negative, opening tension cracks and hydrofracture veins perpendicular to $\sigma_3$.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why is the oceanic crust's brittle-ductile transition controlled by Olivine rather than Quartz?
          <div class="pq-ans">✔ Correct Answer: Oceanic crust and mantle lithosphere are composed of basalt, gabbro, and peridotite, lacking quartz.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Olivine does not transition to plastic flow until $T \approx 600^\circ - 800^\circ\text{C}$, making oceanic lithosphere brittle down to much greater depths ($30 - 40\text{ km}$).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 34, part1, part2, part3)


# ==============================================================================
# Q035: Normal Fault Dip Angle Anderson Theory
# ==============================================================================
def generate_q035():
    title = r"Q035: Andersonian Fault Mechanics: Normal Fault Dip Angle ($\sim 60^\circ$) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Andersonian Mechanics"
    h1_title = "Q035: Andersonian Fault Mechanics: Normal Fault Dip Angle (~60°)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 35<br>
<strong>Authoritative References:</strong> E.M. Anderson, <em>The Dynamics of Faulting</em> (Oliver & Boyd, 1951); Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 7: Anderson's Classification, pp. 147–152, Fig. 7.14); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Faults, pp. 200–204)."""

    part1 = r"""
  <!-- CARD 1: ANDERSON'S FAULT MECHANICS & NORMAL FAULT DIP -->
  <div class="card">
    <div class="card-header bg-blue">1. Andersonian Dynamics & The Theoretical Dip of Normal Faults</div>
    <div class="card-body">
      <p>In 1905 and 1951, the Scottish structural geologist Ernest Masson Anderson published his definitive dynamic theory of faulting based on the <strong>Mohr-Coulomb failure criterion</strong> and the physical boundary condition of Earth's free surface (where shear stress is identically zero, requiring one principal stress to be strictly vertical):</p>

      <ul>
        <li><strong>Principal Stress State in Normal Faulting:</strong> In an extensional tectonic regime, the maximum principal stress is vertical ($\sigma_1 = \rho g z$, lithostatic overburden load), while the intermediate stress ($\sigma_2$) and minimum principal stress ($\sigma_3$) are horizontal ($\sigma_3$ aligns with the regional extension direction).</li>
        <li><strong>Mohr-Coulomb Angle Formulation:</strong> According to Coulomb shear fracture mechanics, conjugate shear failure planes initiate at an angle $\theta$ relative to the maximum compressive stress ($\sigma_1$):
        $$\theta = 45^\circ - \frac{\phi}{2}$$
        Where $\phi$ is the angle of internal friction of typical brittle crustal rocks ($\phi \approx 30^\circ$, friction coefficient $\mu = \tan\phi \approx 0.60$).
        $$\theta = 45^\circ - \frac{30^\circ}{2} = 30^\circ \quad \text{(Angle relative to vertical } \sigma_1\text{)}$$</li>
        <li><strong>Dip Angle Relative to the Horizontal Plane:</strong> Because dip is measured relative to the <strong>horizontal plane</strong>, the dip angle ($\delta$) of a newly formed normal fault is:
        $$\delta = 90^\circ - \theta = 90^\circ - 30^\circ = \mathbf{60^\circ} \quad \text{or} \quad \delta = 45^\circ + \frac{\phi}{2} = 45^\circ + 15^\circ = \mathbf{60^\circ}$$
        Therefore, in Andersonian mechanics and global structural field measurements, <strong>normal faults initiate with a characteristic steep dip of approximately 60° to the horizontal</strong> (which corresponds to an angle of $30^\circ$ to the vertical, NOT $45^\circ$ to vertical!).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q35/fossen_fig7_14_anderson_fault_angle.png" alt="Anderson Fault Angle from Haakon Fossen">
        <div class="tb-caption">
          <strong>Figure 35.1 (Haakon Fossen, <em>Structural Geology</em>, Fig. 7.14):</strong> Anderson's mechanical derivation for normal faulting. Showing vertical $\sigma_1$ generating conjugate normal faults dipping at $\approx 60^\circ$ to the horizontal.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: FORENSIC REFUTATION OF 45° TO VERTICAL -->
  <div class="card">
    <div class="card-header bg-indigo">2. Forensic Dissection: Why the Statement is FALSE</div>
    <div class="card-body">
      <p>The exam question states: <em>"Most common angle of normal faults is 45° to vertical."</em> This statement is <strong>completely false</strong> for two distinct reasons:</p>

      <ul>
        <li><strong>1. Angle with the Vertical is ~30°, NOT 45°:</strong> In pristine Andersonian rock fracture, the shear failure plane forms at an angle of $\theta = 45^\circ - \phi/2 = 30^\circ$ to the vertical ($\sigma_1$). An angle of $45^\circ$ to the vertical would require rock friction to be zero ($\phi = 0^\circ$), which never occurs in brittle crustal rocks!</li>
        <li><strong>2. Dip with Horizontal is ~60°, NOT 45°:</strong> If the statement intended to say "45° to horizontal", that is also incorrect because normal faults dip steeply at $\approx 60^\circ$ (typically $55^\circ - 70^\circ$). Contractional thrust faults dip at $< 45^\circ$.</li>
      </ul>

      <div class="quote-box bangar">
        "Normal Faults: In normal faults, the fault plane is usually very steep, dipping at angles between 50° and 70° (most commonly around 60°) to the horizontal... The hanging wall has moved downward relative to the footwall."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Faults, p. 201)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q35/anderson_fault_theory_principal_stresses.png" alt="Anderson Fault Theory Principal Stresses">
        <div class="tb-caption">
          <strong>Figure 35.2: Anderson's Conjugate Fault Geometries.</strong> Normal faults ($\sigma_1$ vertical) dip at $\sim 60^\circ$ to horizontal ($30^\circ$ to vertical); Thrust faults ($\sigma_1$ horizontal) dip at $\sim 30^\circ$ to horizontal.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: LOW-ANGLE NORMAL FAULTS (DETACHMENTS) -->
  <div class="card">
    <div class="card-header bg-emerald">3. Low-Angle Normal Faults: The Detachment Paradox</div>
    <div class="card-body">
      <p>In highly extended metamorphic core complexes (e.g., Basin and Range), geologists observe <strong>low-angle normal faults (detachment faults)</strong> dipping at $< 30^\circ$:</p>
      <ul>
        <li><strong>The Rolling Hinge Model:</strong> Detachment faults did not initiate at low angles; they initiated as steep $60^\circ$ Andersonian normal faults, which were rotated and flattened to low angles ($< 30^\circ$) by isostatic unloading and crustal flexure as the footwall was exhumed!</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 35)</div>
    <div class="q-stmt">
      Q35. Most common angle of normal faults is 45° to vertical.
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) False &nbsp;✔</div>
      <div class="raw-opt">(B) True</div>
      <div class="raw-opt">(C) None of these</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) False</div>
      <div class="sub">
        The statement is <strong>False</strong>. In classical Andersonian mechanics and global structural field measurements, normal faults initiate with a characteristic steep dip of approximately <strong>60° to the horizontal</strong>, which corresponds to an angle of <strong>30° to the vertical</strong> ($\theta = 45^\circ - \phi/2 \approx 30^\circ$).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) False</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Under Andersonian fault mechanics, the maximum principal stress ($\sigma_1$) in normal fault regimes is vertical. Coulomb shear failure occurs at an angle $\theta = 45^\circ - \phi/2$ to $\sigma_1$. Because crustal rocks have an angle of internal friction $\phi \approx 30^\circ$, normal faults form at $\approx 30^\circ$ to the vertical, and dip at $\approx 60^\circ$ to the horizontal. Stating that normal faults form at "45° to vertical" would require frictionless rock ($\phi = 0^\circ$), which is physically incorrect.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) True</span>
      <span class="tag wrong">Incorrect (Violates Coulomb Mechanics and Anderson's Law)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Accepting "True" ignores rock friction. Maximum shear stress ($\tau_{\text{max}}$) occurs on planes oriented at 45° to $\sigma_1$, but actual fracture occurs along planes where the ratio of shear stress to frictional resistance is maximized ($\approx 30^\circ$ to vertical).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) None of these</span>
      <span class="tag wrong">Incorrect (Binary Truth Value Exists)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The statement is definitively False.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Andersonian Fault Angles & Stress Orientations Matrix</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Fault Type</th>
            <th>Orientation of $\sigma_1$</th>
            <th>Angle to Vertical ($\sigma_1$)</th>
            <th>Dip Angle to Horizontal ($\delta$)</th>
            <th>Tectonic Kinematic Regime</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Normal Fault</strong></td>
            <td><strong>Vertical ($\sigma_1 = \rho g z$)</strong></td>
            <td><strong>$\approx 30^\circ$ ($45^\circ - \phi/2$)</strong></td>
            <td><strong>$\approx 60^\circ$ ($45^\circ + \phi/2$)</strong></td>
            <td><strong>Crustal Extension ($\Delta L > 0$)</strong></td>
          </tr>
          <tr>
            <td><strong>Thrust Fault</strong></td>
            <td>Horizontal ($\sigma_3 = \text{vertical}$)</td>
            <td>$\approx 60^\circ$ to vertical</td>
            <td><strong>$\approx 30^\circ$ to horizontal</strong></td>
            <td>Crustal Shortening ($\Delta L < 0$)</td>
          </tr>
          <tr>
            <td><strong>Strike-Slip Fault</strong></td>
            <td>Horizontal ($\sigma_2 = \text{vertical}$)</td>
            <td>$0^\circ$ (Vertical plane: $90^\circ$ dip)</td>
            <td>$\approx 90^\circ$ (Vertical)</td>
            <td>Conservative Lateral Shear</td>
          </tr>
          <tr>
            <td><strong>Low-Angle Detachment</strong></td>
            <td>Rotated stress / flexure</td>
            <td>$> 60^\circ$ to vertical</td>
            <td>$< 30^\circ$ (Sub-horizontal)</td>
            <td>Metamorphic Core Complex Exhumation</td>
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
          <strong>Practice Q1 (Numerical Derivation):</strong> Using the Coulomb failure criterion with an angle of internal friction $\phi = 32^\circ$, calculate the theoretical dip angle to the horizontal ($\delta$) of a newly formed Andersonian normal fault.
          <div class="pq-ans">✔ Worked Answer: $\delta = 61.0^\circ$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\delta = 45^\circ + \frac{\phi}{2} = 45^\circ + \frac{32^\circ}{2} = 45^\circ + 16^\circ = 61.0^\circ$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Why does maximum shear failure NOT occur on the plane of maximum shear stress ($\tau_{\text{max}}$ at $45^\circ$ to $\sigma_1$)?
          <div class="pq-ans">✔ Correct Answer: Because normal stress ($\sigma_n$) on the plane creates frictional resistance; failure occurs where the Coulomb shear stress excess ($\tau - \sigma_n \tan\phi$) is maximized.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Steeper planes have lower normal stress, reducing frictional clamping and shifting the failure orientation from $45^\circ$ to $\approx 30^\circ$ relative to $\sigma_1$.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is a <em>conjugate normal fault system</em>, and what is the dihedral angle between the two fault planes?
          <div class="pq-ans">✔ Correct Answer: Two sets of normal faults dipping in opposite directions toward each other; dihedral angle is $2\theta = 2(45^\circ - \phi/2) \approx 60^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The two conjugate planes intersect along the intermediate principal stress axis ($\sigma_2$).
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In oil exploration of rift basins, what is a <em>rollover anticline</em>, and along which fault type does it form?
          <div class="pq-ans">✔ Correct Answer: An anticlinal closure formed in the hanging wall of a listric normal fault as the block flexes to fit the curved fault surface.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Rollover anticlines are premier structural hydrocarbon traps in the North Sea, Niger Delta, and Gulf of Mexico.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the "Mechanical Paradox of Low-Angle Normal Faults"?
          <div class="pq-ans">✔ Correct Answer: According to Byerlee's friction law ($\mu = 0.6 - 0.85$), normal faults dipping $< 30^\circ$ should lock up and be unfavorably oriented for slip under vertical overburden load.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> To slip at $< 30^\circ$, detachment faults require extremely high pore fluid pressures, low-friction fault gouge (talc, clays), or rolling-hinge rotation.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What structural feature forms when the hanging wall of a listric normal fault collapses due to lack of support?
          <div class="pq-ans">✔ Correct Answer: A crestal collapse graben (keystone graben).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Bending of the hanging wall creates localized tension over the crest of the rollover, spawning antithetic and synthetic secondary normal faults.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is an <em>antithetic normal fault</em> versus a <em>synthetic normal fault</em>?
          <div class="pq-ans">✔ Correct Answer: Synthetic faults dip in the same direction as the master border fault; antithetic faults dip in the opposite direction toward the master fault.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Antithetic faults accommodate rotational strain within the hanging wall block of half-grabens.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> In extensional basin analysis, what parameter is represented by the <em>crustal stretching factor ($\beta$)</em> in McKenzie's (1978) model?
          <div class="pq-ans">✔ Correct Answer: The ratio of initial crustal thickness to final stretched crustal thickness ($\beta = t_0 / t_{\text{stretched}}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The $\beta$ factor dictates the magnitude of initial fault-controlled syn-rift tectonic subsidence and subsequent thermal post-rift sag subsidence.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 35, part1, part2, part3)


if __name__ == "__main__":
    for q_fn, q_name in [
        (generate_q031, "Q031_Apparent_Dip_Trigonometry_True_Dip_Vein_Complete_Guide.html"),
        (generate_q032, "Q032_Himalayan_Deformation_Folds_Reverse_Faults_Complete_Guide.html"),
        (generate_q033, "Q033_Recumbent_Fold_Axial_Plane_Dip_Angle_Complete_Guide.html"),
        (generate_q034, "Q034_Upper_Crust_Low_PT_Brittle_Deformation_Complete_Guide.html"),
        (generate_q035, "Q035_Normal_Fault_Dip_Angle_Anderson_Theory_Complete_Guide.html"),
    ]:
        out_path = os.path.join(SOLUTIONS_DIR, q_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(q_fn())
        print(f"Generated {q_name}: {out_path} ({os.path.getsize(out_path)} bytes)")
