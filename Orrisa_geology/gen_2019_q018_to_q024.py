#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 18 to 24
Assam DGMS 2019 Masterclass Standard
"""

import os
from gen_2019_q001_to_q005 import CSS_STYLES, generate_page

# ==========================================
# QUESTION 18: HADE OF FAULT PLANE
# ==========================================
q18_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Geometric Elements of Fault Planes: Dip vs. Hade</div>
    <div class="card-body">
      <p>In structural geology and mining geometry, a fault plane is a planar fracture along which measurable displacement has occurred. To fully specify the spatial attitude of an inclined fault plane, structural geologists and mining engineers utilize two complementary angular measurements measured relative to orthogonal reference planes:</p>
      <ul>
        <li><strong>Dip ($\delta$):</strong> The maximum angle of inclination that the fault plane makes with a <strong>horizontal plane</strong>, measured perpendicular to the strike in a vertical plane ($0^\\circ \\le \\delta \\le 90^\\circ$).</li>
        <li><strong>Hade ($\theta_h$):</strong> The angle that the fault plane makes with a <strong>vertical plane</strong>, measured perpendicular to the strike ($0^\\circ \\le \\theta_h \\le 90^\\circ$).</li>
      </ul>

      <div class="quote-box bangar">
        "The angle which an inclined fault plane makes with the vertical plane is known as the <strong>hade</strong> of the fault. It is the complement of the dip angle of the fault plane, such that:
        $$\\text{Hade} + \\text{Dip} = 90^\\circ \\implies \\text{Hade} = 90^\\circ - \\text{Dip}$$
        For example, if a fault plane has a dip of $60^\\circ$, its hade is $30^\\circ$. The hade is always measured in a direction perpendicular to the strike of the fault."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Structural Geology: Fault Terminology, p. 208)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Fundamental Angular Relationship for Fault Plane Geometry</div>
        $$\\text{Hade } (\\theta_h) = 90^\\circ - \\text{Dip } (\\delta)$$
        $$\\text{Heave } (H) = \\text{Dip Slip } (S_d) \\cdot \\cos \\delta = S_d \\cdot \\sin \\theta_h$$
        $$\\text{Throw } (T) = \\text{Dip Slip } (S_d) \\cdot \\sin \\delta = S_d \\cdot \\cos \\theta_h$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $\\text{Heave}$ is the horizontal displacement component perpendicular to strike, and $\\text{Throw}$ is the vertical displacement component.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q018/bangar_p110_fault_elements_hade_dip.png" alt="K.M. Bangar Fault Terminology Hade Dip Throw Heave">
        <div class="tb-caption">
          <strong>Figure 18.1: Geometric Elements of a Fault (K.M. Bangar, p. 110).</strong> Three-dimensional block diagram illustrating fault strike, dip angle ($\delta$ from horizontal), hade angle ($\theta_h$ from vertical), hanging wall, footwall, throw, and heave.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Displacement Vectors & Components on Fault Planes</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Fault Element</th>
            <th>Reference Datum</th>
            <th>Angular / Spatial Definition</th>
            <th>Significance in Mining Geology</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dip</strong></td>
            <td>Horizontal plane</td>
            <td>Angle of maximum inclination from horizontal ($0^\\circ - 90^\\circ$)</td>
            <td>Governs fault classification (high-angle vs. low-angle thrust/normal)</td>
          </tr>
          <tr>
            <td><strong>Hade</strong></td>
            <td><strong>Vertical plane</strong></td>
            <td><strong>Angle that fault plane makes with vertical ($90^\\circ - \\text{Dip}$)</strong></td>
            <td>Traditional mining parameter used in vertical shaft sinking calculations</td>
          </tr>
          <tr>
            <td><strong>Throw</strong></td>
            <td>Vertical axis</td>
            <td>Vertical displacement component between severed bed ends</td>
            <td>Determines vertical offset of faulted coal seams or ore bodies</td>
          </tr>
          <tr>
            <td><strong>Heave</strong></td>
            <td>Horizontal axis</td>
            <td>Horizontal displacement component perpendicular to fault strike</td>
            <td>Represents horizontal loss (gap) or overlap of strata</td>
          </tr>
          <tr>
            <td><strong>Net Slip</strong></td>
            <td>Fault plane</td>
            <td>Total true displacement vector connecting matching piercing points</td>
            <td>Total actual movement across the fault surface</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q18_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 18)</div>
    <div class="q-stmt">
      18. The angle which the fault plane makes with vertical plane is known as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Net slip</div>
      <div class="raw-opt">(B) Heave</div>
      <div class="raw-opt">(C) Strike slip</div>
      <div class="raw-opt correct">(D) Hade &nbsp;✔</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) Hade</div>
      <div class="sub">
        In structural geology and mining geometry (K.M. Bangar, p. 208; Marland P. Billings, p. 138; Fossen, 2016; Davis & Reynolds, 1996), the angle which the fault plane makes with a <strong>vertical plane</strong> is universally defined as the <strong>Hade</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Net slip</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Net slip is a <em>distance</em> (linear displacement vector measured in meters), representing the total true displacement between two formerly contiguous piercing points on opposing sides of the fault plane. It is not an angle made with a vertical plane.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Heave</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Heave is the <em>horizontal component</em> of dip slip (measured in meters), representing the horizontal gap or separation between the displaced ends of a faulted bed measured perpendicular to strike. It is a linear distance, not an angle.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Strike slip</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Strike slip is the component of net slip measured <em>parallel to the fault strike</em> within the fault plane. It is a linear displacement component, not an angle.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) Hade</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard international definition, <strong>hade</strong> is the exact angle that an inclined fault plane (or vein/bed) makes with the vertical plane. It is the geometric complement of the dip angle ($\\text{Hade} = 90^\\circ - \\text{Dip}$).
    </div>
  </div>
"""

q18_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Coordinate Transformations: Dip, Hade, Throw & Heave</div>
    <div class="card-body">
      <p>Given an inclined fault with dip angle $\\delta$ and true dip-slip displacement $S_d$:</p>
      $$\\text{Hade } \\theta_h = 90^\\circ - \\delta$$
      $$\\text{Throw } T = S_d \\cdot \\sin \\delta = S_d \\cdot \\cos \\theta_h$$
      $$\\text{Heave } H = S_d \\cdot \\cos \\delta = S_d \\cdot \\sin \\theta_h$$
      $$\\tan \\delta = \\frac{\\text{Throw}}{\\text{Heave}} \\implies \\tan \\theta_h = \\frac{\\text{Heave}}{\\text{Throw}}$$
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A normal fault in a coal mine dips at an angle $\\delta = 55^\\circ$. (a) Calculate the hade of the fault plane. (b) If the measured throw of a faulted coal seam is $T = 32.0\\text{ m}$, calculate the heave ($H$) and the dip-slip ($S_d$) along the fault plane.
          <div class="pq-ans">✔ Worked Answer: (a) $\\text{Hade} = 35^\\circ$; (b) $\\text{Heave} = 22.4\\text{ m}$; $\\text{Dip-slip} = 39.1\\text{ m}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            (a) $\\text{Hade } \\theta_h = 90^\\circ - \\delta = 90^\\circ - 55^\\circ = 35^\\circ$.<br>
            (b) $\\text{Heave } H = \\frac{T}{\\tan \\delta} = \\frac{32.0}{\\tan 55^\\circ} = \\frac{32.0}{1.4281} \\approx 22.41\\text{ m}$.<br>
            $$\\text{Dip-slip } S_d = \\frac{T}{\\sin \\delta} = \\frac{32.0}{\\sin 55^\\circ} = \\frac{32.0}{0.8192} \\approx 39.06\\text{ m}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> If a fault plane is perfectly vertical ($\delta = 90^\circ$), what is its hade?
          <div class="pq-ans">✔ Correct Answer: $\text{Hade} = 0^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the fault plane is coincident with the vertical plane, the angle between them is zero ($\text{Hade} = 90^\circ - 90^\circ = 0^\circ$).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> If a detachment fault has a hade $\theta_h = 75^\circ$, classify the fault as high-angle or low-angle based on its dip.
          <div class="pq-ans">✔ Correct Answer: Low-angle fault ($\text{Dip } \delta = 15^\circ < 45^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> $\text{Dip} = 90^\circ - \text{Hade} = 90^\circ - 75^\circ = 15^\circ$. Since $\delta < 45^\circ$, it is a low-angle detachment or thrust fault.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In historical Cornish mining terminology, why did miners prefer measuring "hade" rather than "dip"?
          <div class="pq-ans">✔ Correct Answer: Because miners suspended a plumb-bob (vertical plumb-line) inside shafts; measuring the angle from the plumb-line directly gave the hade.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A plumb-line gives a precise vertical reference; measuring deviation of the mineral vein from the string gave the hade without needing an artificial horizontal bubble level.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the "apparent dip" of a fault plane, and how does it compare to the "true dip"?
          <div class="pq-ans">✔ Correct Answer: Apparent dip is the inclination measured in any vertical plane not perpendicular to strike; it is always strictly less than the true dip ($\tan \alpha = \tan \delta \cdot \cos \beta$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> True dip is measured perpendicular to strike and represents the maximum inclination; in any oblique cross-section, apparent dip ($\alpha$) is smaller.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "fault scrap" vs. a "fault-line scarp"?
          <div class="pq-ans">✔ Correct Answer: A fault scarp is generated directly by active tectonic displacement; a fault-line scarp is carved by differential erosion along an ancient, dormant fault line.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Fault-line scarps often face in the opposite direction of the original tectonic displacement if the downthrown side contains more resistant rock (obsequent fault-line scarp).
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In structural contour mapping of a planar fault, how does the spacing between strike contours relate to dip and hade?
          <div class="pq-ans">✔ Correct Answer: Horizontal contour spacing $S = \Delta h / \tan \delta = \Delta h \cdot \tan \theta_h$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> For a given contour interval $\Delta h$, steeper faults (smaller hade) have closely spaced contours; gently dipping faults (larger hade) have widely spaced contours.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is the "Rake" (or Pitch) of a line on an inclined fault plane?
          <div class="pq-ans">✔ Correct Answer: The angle that a linear feature (e.g., striations/slickenlines) makes with the horizontal strike line within the fault plane ($0^\circ \le \phi \le 90^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Measured on the inclined plane itself using a protractor; $\text{Rake} = 90^\circ$ represents pure dip-slip; $\text{Rake} = 0^\circ$ represents pure strike-slip.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=18,
    filename="Q018_Fault_Hade_Angle_with_Vertical_Plane_Complete_Guide.html",
    title="Q018: Fault Geometry, Hade, Dip, Throw & Heave Derivations",
    badge="GGM - 2/2019 • Structural Geology & Fault Mechanics",
    h1_title="Q018: Geometry of Fault Planes: Dip, Hade, Throw & Coordinate Transformations",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 18<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 208); Marland P. Billings (<em>Structural Geology</em>, pp. 138–142); Haakon Fossen (<em>Structural Geology</em>, Ch. 9)",
    part1_html=q18_part1,
    part2_html=q18_part2,
    part3_html=q18_part3
)

# ==========================================
# QUESTION 19: NORMAL FAULT - HANGING WALL DOWNTHROWN
# ==========================================
q19_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Kinematics & Andersonian Mechanics of Normal Faulting</div>
    <div class="card-body">
      <p>In structural geology and fault mechanics, a <strong>normal fault</strong> (historically termed a gravity fault) is a dip-slip fault where the <strong>hanging wall has moved downward relative to the footwall</strong>. Normal faults are the fundamental structural hallmark of <strong>crustal extension</strong> (rifting, basin-and-range extension, and mid-ocean ridge spreading centers).</p>

      <div class="quote-box bangar">
        "In a dip-slip fault, the block lying above the inclined fault plane is called the hanging wall, and the block lying below it is called the footwall. When the <strong>hanging wall has moved down relative to the footwall</strong>, the fault is called a <strong>normal fault</strong>. Normal faults are produced by tensional forces in the Earth's crust that tend to stretch and pull the rocks apart."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Chapter 7: Faults, p. 209)</span>
      </div>

      <p>The mechanical physics of normal faulting is formalized by <strong>Anderson's Theory of Faulting (1905, 1951)</strong>, based on the principle that the Earth's surface is a free surface that can support zero shear stress, requiring one of the three principal stress axes to be vertical:</p>

      <div class="formula-card">
        <div class="formula-title">Andersonian Stress State for Normal Faulting (Anderson, 1905)</div>
        $$\\sigma_1 \\text{ (Maximum Principal Compressive Stress) is VERTICAL } (\\sigma_v = \\rho g z)$$
        $$\\sigma_2 \\text{ (Intermediate Principal Stress) is HORIZONTAL (Parallel to Fault Strike)}$$
        $$\\sigma_3 \\text{ (Minimum Principal Compressive Stress) is HORIZONTAL (Extensional Direction)}$$
        $$\\text{Theoretical Fault Dip Angle: } \\theta = 45^\\circ + \\frac{\\phi}{2} \\approx 60^\\circ \\quad (\\text{for typical rock friction } \\phi = 30^\\circ)$$
      </div>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q019/bangar_fig7_24_normal_fault_hanging_wall.png" alt="K.M. Bangar Normal and Reverse Faults">
        <div class="tb-caption">
          <strong>Figure 19.1: Normal vs. Reverse Fault Geometry (K.M. Bangar, Fig. 7.24).</strong> (A) Normal fault showing hanging wall downthrown along an inclined fault plane under extensional stress, resulting in crustal lengthening and missing stratigraphy, contrasted with (B) Reverse fault.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q019/fossen_fig9_2_normal_fault_regime.png" alt="Haakon Fossen Andersonian Fault Regimes">
        <div class="tb-caption">
          <strong>Figure 19.2: Anderson's Three Tectonic Stress Regimes (Haakon Fossen, Fig. 9.2).</strong> Normal faulting regime where $\sigma_1$ is vertical and $\sigma_3$ is horizontal, generating conjugate normal faults dipping at $\approx 60^\circ$ and accommodating horizontal crustal extension.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Matrix: Normal vs. Reverse vs. Strike-Slip Faults</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Fault Class</th>
            <th>Hanging Wall Kinematics</th>
            <th>Tectonic Stress Regime</th>
            <th>Principal Stress Orientation</th>
            <th>Crustal Deformation Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Normal Fault</strong></td>
            <td><strong>Downthrown relative to footwall</strong></td>
            <td><strong>Tensional / Extensional</strong></td>
            <td>$\\sigma_1$ Vertical; $\\sigma_3$ Horizontal</td>
            <td>Crustal lengthening (extension); stratigraphic omission</td>
          </tr>
          <tr>
            <td><strong>Reverse Fault</strong></td>
            <td>Upthrown relative to footwall</td>
            <td>Compressional</td>
            <td>$\\sigma_1$ Horizontal; $\\sigma_3$ Vertical</td>
            <td>Crustal shortening; stratigraphic repetition</td>
          </tr>
          <tr>
            <td><strong>Thrust Fault</strong></td>
            <td>Upthrown at low angle ($\\text{Dip} \\le 45^\\circ$)</td>
            <td>Compressional (Orogenic)</td>
            <td>$\\sigma_1$ Horizontal; $\\sigma_3$ Vertical</td>
            <td>Regional nappe stacking; older strata over younger</td>
          </tr>
          <tr>
            <td><strong>Strike-Slip Fault</strong></td>
            <td>Horizontal lateral displacement</td>
            <td>Shearing / Transcurrent</td>
            <td>$\\sigma_1, \\sigma_3$ Horizontal; $\\sigma_2$ Vertical</td>
            <td>Lateral translation; neither lengthening nor shortening</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q19_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 19)</div>
    <div class="q-stmt">
      19. If the hanging wall in a fault is in downthrown side, it is called :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Reverse fault</div>
      <div class="raw-opt correct">(B) Normal fault &nbsp;✔</div>
      <div class="raw-opt">(C) Tear fault</div>
      <div class="raw-opt">(D) Hinge fault</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Normal fault</div>
      <div class="sub">
        In structural geology, fault mechanics, and tectonic analysis (K.M. Bangar, p. 209; Marland P. Billings, p. 142; Haakon Fossen, p. 338; E.M. Anderson, 1905), a fault where the <strong>hanging wall occupies the downthrown side</strong> is universally defined as a <strong>Normal fault</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Reverse fault</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> In a reverse fault, the hanging wall has moved <em>upward</em> (upthrown) relative to the footwall under horizontal compressional stress ($\sigma_1$ horizontal), causing crustal shortening and duplicating stratigraphic layers in vertical boreholes.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Normal fault</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By fundamental definition, whenever the hanging wall block moves downward along the dip of the fault plane relative to the footwall, the fault is termed a <strong>normal fault</strong>. This movement accommodates crustal extension and produces a gap (omission) of strata in vertical drill holes.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Tear fault</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A tear fault is a localized, near-vertical strike-slip fault that bounds or accommodates differential movement within an advancing thrust sheet or allochthonous nappe, displaying horizontal slip rather than hanging-wall downthrow.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Hinge fault</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A hinge fault (or rotational fault) is a fault where displacement increases progressively away from a stationary pivot or hinge axis where displacement is zero; movement involves rotational torque rather than uniform dip-slip translation.
    </div>
  </div>
"""

q19_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Structural Signatures of Normal Faulting in Boreholes & Seismic Sections</div>
    <div class="card-body">
      <p>Normal faulting imparts unmistakable structural signatures across subsurface geological data:</p>
      <ul>
        <li><strong>Stratigraphic Omission (Missing Beds):</strong> A vertical borehole drilled through a normal fault plane encounters an abrupt stratigraphic gap—beds that should be present between the hanging wall and footwall are omitted.</li>
        <li><strong>Crustal Lengthening:</strong> Measured horizontal line length across a normal fault terrain increases by $\Delta L = \sum \text{Heave}$, directly quantifying regional tectonic extension.</li>
        <li><strong>Rollover Anticlines & Growth Strata:</strong> Listric normal faults (fault planes that curve to shallower dips at depth) force the hanging-wall block to rotate and collapse, forming a rollover anticline with growth stratigraphy that thickens toward the fault plane.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A continental rift valley is traversed by a conjugate set of 10 normal faults, each dipping at $\delta = 60^\circ$ and having an average throw $T = 150.0\text{ m}$. Calculate: (a) the heave per fault, and (b) the total regional horizontal tectonic extension ($\Delta L$) accommodated by the fault system.
          <div class="pq-ans">✔ Worked Answer: (a) $\text{Heave} = 86.6\text{ m}$; (b) $\Delta L = 866.0\text{ meters}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            (a) For each fault: $\text{Heave } H = \frac{T}{\tan \delta} = \frac{150.0}{\tan 60^\circ} = \frac{150.0}{\sqrt{3}} \approx 86.60\text{ m}$.<br>
            (b) Total regional crustal lengthening:<br>
            $$\Delta L = n \times H = 10 \times 86.60\text{ m} = 866.0\text{ meters}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a "Horst" and a "Graben"?
          <div class="pq-ans">✔ Correct Answer: A graben is a central downthrown block bounded by conjugate normal faults dipping toward each other; a horst is an uplifted block bounded by outward-dipping normal faults.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Classic grabens include the Rhine Graben and East African Rift; classic horsts include the Black Forest and Vosges mountains.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> Why do conjugate normal faults typically intersect at an angle of $60^\circ$ in pristine rock?
          <div class="pq-ans">✔ Correct Answer: Because according to Coulomb-Mohr fracture criterion with internal friction $\phi \approx 30^\circ$, failure occurs along planes inclined at $\theta = 45^\circ + \phi/2 = 60^\circ$ to $\sigma_3$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The dihedral angle between conjugate fault planes bisected by $\sigma_1$ is $2(45^\circ - \phi/2) = 60^\circ$.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In oil and gas drilling, if a well penetrates a fault and certain reservoir sandstone beds are completely missing, what type of fault was crossed?
          <div class="pq-ans">✔ Correct Answer: A Normal fault.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Normal faults produce stratigraphic omission (gap); reverse faults produce stratigraphic repetition (the same bed is drilled twice).
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "listric normal fault"?
          <div class="pq-ans">✔ Correct Answer: A normal fault whose fault surface is concave-upward, dipping steeply near the surface and flattening to subhorizontal at depth.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Listric faults sole into a subhorizontal basal detachment (décollement) in passive continental margins and extensional basins.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "detachment fault" (or core complex fault)?
          <div class="pq-ans">✔ Correct Answer: A regional, low-angle ($\delta < 30^\circ$) normal fault accommodating extreme crustal extension, exhuming lower crustal metamorphic core complexes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Common in the Basin and Range province (USA) and Aegean Sea, juxtaposing unmetamorphosed brittle upper-crustal rocks against ductile mylonitic gneisses.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is an "antithetic normal fault" vs. a "synthetic normal fault"?
          <div class="pq-ans">✔ Correct Answer: A synthetic fault dips in the same direction as the master fault; an antithetic fault dips in the opposite direction.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Antithetic faults form within the hanging-wall block to accommodate bending strain during rollover folding.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is "growth faulting" in deltaic environments?
          <div class="pq-ans">✔ Correct Answer: A syn-sedimentary normal fault that moves concurrently with deposition, resulting in dramatically thicker sedimentary beds on the downthrown hanging wall.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Ubiquitous in Cenozoic delta provinces (e.g., Niger Delta, Gulf of Mexico, Krishna-Godavari Basin), forming prime structural-stratigraphic petroleum traps.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=19,
    filename="Q019_Normal_Fault_Hanging_Wall_Downthrown_Complete_Guide.html",
    title="Q019: Normal Faults, Hanging Wall Kinematics & Andersonian Extensional Mechanics",
    badge="GGM - 2/2019 • Structural Geology & Tectonics",
    h1_title="Q019: Kinematics of Normal Faulting: Hanging Wall Dynamics & Andersonian Tectonics",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 19<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 209); E.M. Anderson (<em>The Dynamics of Faulting</em>, 1905/1951); Haakon Fossen (<em>Structural Geology</em>, Ch. 9)",
    part1_html=q19_part1,
    part2_html=q19_part2,
    part3_html=q19_part3
)

# ==========================================
# QUESTION 20: FOLD AXIS PARALLEL TO HINGE
# ==========================================
q20_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Geometric Anatomy of Folds: Hinge Line vs. Fold Axis</div>
    <div class="card-body">
      <p>In rigorous structural analysis (Ramsay, 1967; Fleuty, 1964; Billings, 1972; Davis & Reynolds, 1996), a fundamental distinction is maintained between physical, material structural features and imaginary mathematical generators of folded surfaces:</p>
      <ul>
        <li><strong>Hinge Line (Hinge):</strong> The physical material line of <strong>maximum curvature</strong> along a folded layer. It connects all points of maximum curvature across the fold profile. The hinge is a tangible physical feature in a folded rock.</li>
        <li><strong>Fold Axis:</strong> An imaginary geometric line which, when moved parallel to itself in three-dimensional space, generates the shape of the folded surface (by definition, for a <em>cylindrical fold</em>). Therefore, in a cylindrical fold, <strong>the fold axis is strictly parallel to the hinge line</strong>.</li>
      </ul>

      <div class="quote-box bangar">
        "The hinge of a fold is the line connecting the points of maximum curvature on a folded layer. An imaginary line which, by moving parallel to itself, generates the folded surface is known as the <strong>axis of the fold</strong>. In cylindrical folds, the axis of the fold is parallel to the hinge line."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Chapter 7: Folds, p. 185)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Mathematical Definition of Cylindrical Folds (Ramsay, 1967)</div>
        $$\\text{Fold Surface: } z = f(x) \\quad (\\text{Invariant along } y\\text{-axis})$$
        $$\\vec{b} = \\text{Unit Vector of Fold Axis} \\implies \\vec{b} \\parallel \\vec{t}_{\\text{hinge}}$$
        $$\\beta\\text{-axis} = \\pi_1 \\times \\pi_2 \\quad (\\text{Intersection of Bedding Poles in Stereonet})$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">In a cylindrical fold, all tangents to the hinge line are collinear and parallel to the fold axis ($\vec{b}$). On a stereographic projection, poles to bedding ($\pi$-poles) define a great circle whose pole is the fold axis ($\beta$-axis).</p>
      </div>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q020/bangar_fig7_5_fold_axis_hinge.png" alt="K.M. Bangar Fold Hinge Axial Plane Axis">
        <div class="tb-caption">
          <strong>Figure 20.1: Anatomical Elements of a Fold (K.M. Bangar, Fig. 7.5).</strong> Schematic block diagram illustrating the hinge line (maximum curvature), the parallel fold axis, the axial surface connecting hinges of successive layers, crest, trough, and limbs.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q020/fossen_fig12_1_fold_hinge_anatomy.png" alt="Haakon Fossen Fold Hinge Anatomy">
        <div class="tb-caption">
          <strong>Figure 20.2: Modern Geometric Fold Terminology (Haakon Fossen, Fig. 12.1).</strong> Rigorous distinction between the hinge zone (region of high curvature), the hinge line, the axial surface, and inflection lines separating concave and convex domains.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Dissection of Canonical Fold Anatomical Terminology</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Fold Element</th>
            <th>Geometric Reality</th>
            <th>Spatial Definition</th>
            <th>Orientation Parameters</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fold Axis</strong></td>
            <td>Imaginary geometric line</td>
            <td><strong>A line which is parallel to the hinge in a cylindrical fold</strong>; generates fold by translation</td>
            <td>Plunge and Trend ($P \\to T$)</td>
          </tr>
          <tr>
            <td><strong>Hinge Line</strong></td>
            <td>Physical material line</td>
            <td>The locus of points of maximum curvature on a specific folded surface</td>
            <td>Plunge and Trend</td>
          </tr>
          <tr>
            <td><strong>Axial Plane / Surface</strong></td>
            <td>Curvilinear or planar surface</td>
            <td>Surface passing through and connecting the hinge lines of successive stacked beds</td>
            <td>Strike and Dip ($S / D$)</td>
          </tr>
          <tr>
            <td><strong>Crest Line</strong></td>
            <td>Topographic material line</td>
            <td>The line connecting the highest elevation points along an anticline</td>
            <td>Can diverge from hinge in plunging inclined folds</td>
          </tr>
          <tr>
            <td><strong>Trough Line</strong></td>
            <td>Topographic material line</td>
            <td>The line connecting the lowest elevation points along a syncline</td>
            <td>Can diverge from hinge in plunging inclined folds</td>
          </tr>
          <tr>
            <td><strong>Inflection Line</strong></td>
            <td>Boundary line</td>
            <td>Line separating domains of opposite curvature where curvature is zero ($d^2z/dx^2 = 0$)</td>
            <td>Boundaries of the fold limb</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q20_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 20)</div>
    <div class="q-stmt">
      20. The line which is parallel to the hinge in a fold is called :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Axis of the fold &nbsp;✔</div>
      <div class="raw-opt">(B) Axial plane of the fold</div>
      <div class="raw-opt">(C) Crest of the fold</div>
      <div class="raw-opt">(D) Plunge of the fold</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Axis of the fold</div>
      <div class="sub">
        In structural geology (K.M. Bangar, p. 185; Marland P. Billings, p. 35; John G. Ramsay, 1967; Haakon Fossen, p. 238), the line which is <strong>parallel to the hinge in a cylindrical fold</strong> is defined precisely as the <strong>Axis of the fold (Fold Axis)</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Axis of the fold</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> In structural geometry, the axis of a fold is a direction or imaginary generator line that generates the cylindrical fold surface when translated in space. In any cylindrical fold, the fold axis is geometrically parallel to the hinge line.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Axial plane of the fold</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The axial plane (axial surface) is a <em>two-dimensional planar or curvilinear surface</em>, not a line. It connects the hinge lines of all successive layers in a fold stack.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Crest of the fold</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The crest is the line connecting the highest geographic elevation points of an anticline. In inclined plunging folds, the crest line diverges markedly from the hinge line and is not defined as parallel to it.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Plunge of the fold</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Plunge is an <em>angle</em> (measured in degrees from the horizontal, $0^\circ \le P \le 90^\circ$) representing the vertical inclination of the fold hinge or axis, not a physical line.
    </div>
  </div>
"""

q20_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Cylindrical vs. Non-Cylindrical Folds in Structural Mapping</div>
    <div class="card-body">
      <p>The concept of a fold axis strictly applies to <strong>cylindrical folds</strong>:</p>
      <ul>
        <li><strong>Cylindrical Folds:</strong> Possess a straight hinge line parallel to a single fixed fold axis. On a stereonet (pi-diagram), bedding poles lie along a single great circle ($\pi$-circle), and the pole to this circle is the fold axis ($\beta$).</li>
        <li><strong>Non-Cylindrical (Periclinal / Conical) Folds:</strong> Hinge lines are curved, meaning no single line can generate the entire fold surface. Such folds (e.g., doubly plunging domes, basins, sheath folds) lack a single unique fold axis.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> Under what geometric condition do the Hinge line and Crest line of an anticlinal fold coincide exactly?
          <div class="pq-ans">✔ Correct Answer: When the fold is upright (vertical axial plane) or non-plunging.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In an upright symmetric anticline, the highest point (crest) coincides with the point of maximum curvature (hinge). In an inclined plunging fold, the crest shifts onto the upper limb, diverging from the hinge.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a "cylindrical fold", and how is it tested using a stereonet?
          <div class="pq-ans">✔ Correct Answer: A fold generated by translating a straight line (the fold axis); tested by verifying that bedding poles ($\pi$-poles) fall onto a single great circle ($\pi$-girdle).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The pole to the $\pi$-girdle defines the trend and plunge of the fold axis ($\beta$).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is a "sheath fold", and what deformation environment does it diagnose?
          <div class="pq-ans">✔ Correct Answer: A strongly non-cylindrical, tubular or tongue-shaped fold with highly curved hinge lines; diagnostic of intense non-coaxial ductile shear in high-strain shear zones.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In mylonite zones, differential flow velocity rotates hinge lines toward the transport direction, folding them into closed tubular sheath geometries.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Distinguish between the "Trend" and "Plunge" of a fold axis.
          <div class="pq-ans">✔ Correct Answer: Plunge is the vertical inclination angle from the horizontal ($0^\circ - 90^\circ$); Trend is the geographic azimuth direction toward which the axis plunges ($0^\circ - 360^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Recorded in structural geology notation as $P \to T$ (e.g., $25^\circ \to 140^\circ$).
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the "interlimb angle" of a fold, and how is it measured?
          <div class="pq-ans">✔ Correct Answer: The minimum angle subtended between the two limbs of a fold, measured in the profile plane perpendicular to the fold hinge.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Fleuty (1964) classified folds by interlimb angle: Gentle ($120^\circ-180^\circ$), Open ($70^\circ-120^\circ$), Close ($30^\circ-70^\circ$), Tight ($0^\circ-30^\circ$), Isoclinal ($0^\circ-10^\circ$).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the "profile plane" of a fold?
          <div class="pq-ans">✔ Correct Answer: A vertical or inclined cross-sectional plane constructed strictly perpendicular to the fold hinge line/axis.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Only in the profile plane is the true geometry, layer thickness, and interlimb angle observed without apparent geometric distortion.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is a "doubly plunging fold"?
          <div class="pq-ans">✔ Correct Answer: A fold whose hinge line plunges in opposite directions at both ends, forming an elongate dome (anticline) or canoe-shaped basin (syncline).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Erosion of doubly plunging anticlines exposes older rocks in the center surrounded by oval outcrop belts of younger strata (inliers).
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is the "axial trace" on a geological map?
          <div class="pq-ans">✔ Correct Answer: The line of intersection between the axial surface of a fold and the Earth's topographic surface.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Represented on geological maps by a standardized line symbol with arrows indicating anticlinal or synclinal dip directions.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=20,
    filename="Q020_Fold_Axis_Parallel_to_Hinge_Complete_Guide.html",
    title="Q020: Fold Geometry, Hinge Lines, Fold Axes & Profile Analysis",
    badge="GGM - 2/2019 • Structural Geology & Fold Mechanics",
    h1_title="Q020: Geometric Anatomy of Folds: Hinge Lines, Fold Axes & Cylindrical Modeling",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 20<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 185); Marland P. Billings (<em>Structural Geology</em>, pp. 35–42); John G. Ramsay (<em>Folding and Fracturing of Rocks</em>, 1967)",
    part1_html=q20_part1,
    part2_html=q20_part2,
    part3_html=q20_part3
)

# ==========================================
# QUESTION 21: RECUMBENT FOLD - HORIZONTAL AXIAL PLANE
# ==========================================
q21_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Morphological Classification of Folds by Axial Plane Attitude</div>
    <div class="card-body">
      <p>In structural geology (Fleuty, 1964; Billings, 1972; Ramsay, 1967; Bangar, p. 190), folds are rigorously categorized according to the <strong>dip angle of their axial plane (axial surface)</strong>. When tectonic deformation is so severe that the axial plane is pushed over until it is <strong>subhorizontal to completely horizontal (dip $0^\\circ - 10^\\circ$)</strong>, the fold is universally termed a <strong>recumbent fold</strong>.</p>

      <div class="quote-box bangar">
        "A recumbent fold is an overtilted fold in which the axial plane has been rotated into an essentially horizontal position (dip of axial plane is less than $10^\\circ$ or nearly $0^\\circ$). In a recumbent fold, the limbs are roughly horizontal, with one limb lying directly above the other. The lower limb is completely inverted (overturned), while the upper limb is normal. Recumbent folds are characteristic of regions of intense orogenic compression, such as the Alps and the Himalayas."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Chapter 7: Classification of Folds, p. 190)</span>
      </div>

      <p>A recumbent fold consists of two distinct structural components:</p>
      <ul>
        <li><strong>Normal Limb (Upper / Autochthonous):</strong> The upper limb, where the stratigraphic sequence maintains its original normal polarity (younger beds overlying older beds).</li>
        <li><strong>Inverted / Overturned Limb (Lower / Reverse):</strong> The lower limb lying beneath the subhorizontal axial surface, where the entire stratigraphic sequence has been upside-down inverted (older beds overlying younger beds).</li>
        <li><strong>Nappe Evolution:</strong> When tectonic compressional stress continues beyond recumbent folding, the inverted limb is sheared out and sheared along a low-angle thrust fault (thrust plane), translating the upper normal limb tens to hundreds of kilometers as an allochthonous <strong>nappe</strong> (thrust nappe).</li>
      </ul>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q021/bangar_p98_recumbent_fold_axial_plane.png" alt="K.M. Bangar Recumbent Fold Horizontal Axial Plane">
        <div class="tb-caption">
          <strong>Figure 21.1: Architecture of a Recumbent Fold (K.M. Bangar, p. 98).</strong> Cross-section illustrating a horizontal axial plane ($\text{Dip } \approx 0^\circ$), horizontal hinge line, normal upper limb, and inverted lower limb leading to nappe formation.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Fleuty's Standardized Fold Classification by Axial Plane Dip (Fleuty, 1964)</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Fold Class</th>
            <th>Dip of Axial Plane</th>
            <th>Limb Dip & Polarity</th>
            <th>Tectonic Setting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Upright Fold</strong></td>
            <td>$80^\\circ - 90^\\circ$ (Near vertical)</td>
            <td>Both limbs dip in opposite directions; normal polarity</td>
            <td>Mild symmetric lateral compression</td>
          </tr>
          <tr>
            <td><strong>Steeply Inclined</strong></td>
            <td>$60^\\circ - 80^\\circ$</td>
            <td>Limbs dip in opposite directions with unequal angles</td>
            <td>Moderately asymmetric compression</td>
          </tr>
          <tr>
            <td><strong>Moderately Inclined</strong></td>
            <td>$30^\\circ - 60^\\circ$</td>
            <td>Limbs dip in opposite directions</td>
            <td>Asymmetric tectonic shortening</td>
          </tr>
          <tr>
            <td><strong>Gently Inclined</strong></td>
            <td>$10^\\circ - 30^\\circ$</td>
            <td>Limbs may dip in same direction; one overturned</td>
            <td>Strong tectonic shear</td>
          </tr>
          <tr>
            <td><strong>Recumbent Fold</strong></td>
            <td><strong>$0^\\circ - 10^\\circ$ (Essentially Horizontal)</strong></td>
            <td><strong>Subhorizontal limbs; lower limb completely overturned</strong></td>
            <td><strong>Intense orogenic collision (Alps, Himalayas, Caledonides)</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q21_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 21)</div>
    <div class="q-stmt">
      21. If the axial plane of the fold is horizontal, then it is said to be :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Open fold</div>
      <div class="raw-opt">(B) Tight fold</div>
      <div class="raw-opt correct">(C) Recumbent fold &nbsp;✔</div>
      <div class="raw-opt">(D) Isoclinal fold</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Recumbent fold</div>
      <div class="sub">
        In structural geology (K.M. Bangar, p. 190; Marland P. Billings, p. 48; M.J. Fleuty, 1964; Haakon Fossen, p. 242), a fold whose <strong>axial plane is horizontal (or nearly horizontal, dip $<10^\circ$)</strong> is universally defined as a <strong>Recumbent fold</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Open fold</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> "Open fold" is an interlimb angle classification describing the degree of fold tightness ($70^\circ \le \text{interlimb angle} \le 120^\circ$). It specifies how tightly the limbs are squeezed, completely independent of the spatial orientation or dip of the axial plane (an open fold can be upright, inclined, or recumbent).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Tight fold</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> "Tight fold" also refers to interlimb angle ($0^\circ \le \text{interlimb angle} \le 30^\circ$). It describes tight compressive squeezing of the limbs, not the inclination of the axial plane.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Recumbent fold</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By fundamental international definition, a <strong>recumbent fold</strong> is a fold whose axial plane has been overturned and rotated into a <strong>horizontal or subhorizontal</strong> orientation ($\text{Dip } \le 10^\circ$), with the lower limb inverted beneath the upper normal limb.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Isoclinal fold</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> An isoclinal fold is a fold where both limbs are mutually parallel (interlimb angle $0^\circ - 10^\circ$), dipping at the same angle in the same direction. An isoclinal fold can have a vertical axial plane (upright isocline), an inclined axial plane, or a horizontal axial plane (recumbent isocline). Thus, "isoclinal" defines limb parallelism, not a horizontal axial plane.
    </div>
  </div>
"""

q21_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Tectonic Metamorphic Architecture of Recumbent Folds & Nappes</div>
    <div class="card-body">
      <p>Recumbent folds are the fundamental building blocks of ductile collision orogens (e.g., the Penninic nappes of the Alps and the Higher Himalayan Crystalline nappes):</p>
      <ul>
        <li><strong>Inverted Metamorphic Sequences:</strong> In recumbent folds and thrust nappes, hot, high-grade crystalline rocks (kyanite/sillimanite gneisses) are thrust over cooler, low-grade rocks (garnet/biotite schists), producing the famous "inverted metamorphism" observed across the Main Central Thrust (MCT) zone of the Himalayas.</li>
        <li><strong>Facing and Polarity:</strong> Stratigraphic facing (younging direction) in the upper limb faces upwards toward the sky, whereas facing in the lower overturned limb points downwards into the Earth.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What primary sedimentary way-up structure can a field geologist use to confirm that they are standing on the overturned lower limb of a recumbent fold?
          <div class="pq-ans">✔ Correct Answer: Inverted cross-bedding (truncated tops pointing down), upside-down graded bedding (coarse at top, fine at bottom), or inverted geopetal structures.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because bedding is nearly horizontal in a recumbent fold, only way-up structures reveal whether the beds are right-side-up (upper limb) or upside-down inverted (lower limb).
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What structural feature forms when the thinned, sheared lower limb of a recumbent fold is completely cut out along a shear plane?
          <div class="pq-ans">✔ Correct Answer: A thrust nappe (fold nappe / nappe de recouvrement).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Severe shear strain ruptures the middle inverted limb, transforming the recumbent anticline into an allochthonous thrust sheet (nappe).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is an "isoclinal recumbent fold"?
          <div class="pq-ans">✔ Correct Answer: A fold that has both mutually parallel limbs (interlimb angle $\approx 0^\circ$) AND a horizontal axial plane.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Represents the culmination of extreme compressive orogenic shearing where limbs are parallel and stacked horizontally.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In a recumbent fold, where is the hinge zone located relative to the limbs?
          <div class="pq-ans">✔ Correct Answer: At the frontal nose (apex) of the fold where the upper normal limb wraps around into the lower inverted limb.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The hinge line is horizontal and forms the nose of the horizontally projecting fold.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "fenster" (or window) in a recumbent nappe terrain?
          <div class="pq-ans">✔ Correct Answer: An erosional hole or window cut through an overlying allochthonous nappe, exposing the younger, autochthonous footwall rocks beneath.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A classic structural feature in the Alps and Himalayas where deep river valleys erode through nappe sheets.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "klippe"?
          <div class="pq-ans">✔ Correct Answer: An isolated, erosional remnant of an allochthonous recumbent nappe perched atop autochthonous footwall strata.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The counterpart to a fenster; represents an isolated mountain summit of older thrust rocks surrounded by younger footwall rocks.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Can a recumbent fold be refolded by a later tectonic deformation event?
          <div class="pq-ans">✔ Correct Answer: Yes; superposed deformation produces Type 2 (crescent/mushroom) or Type 3 (convergent/divergent) Ramsay interference patterns.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In polyphase orogenic belts, early recumbent folds ($F_1$) with horizontal axial planes are commonly refolded by upright $F_2$ folds, arching the axial surface.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is the difference between an "overturned fold" and a "recumbent fold"?
          <div class="pq-ans">✔ Correct Answer: In an overturned fold, the axial plane is inclined ($10^\circ - 60^\circ$); in a recumbent fold, the axial plane has become virtually horizontal ($0^\circ - 10^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A recumbent fold represents the extreme end-member of overturning where limbs lie subhorizontal.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=21,
    filename="Q021_Recumbent_Fold_Horizontal_Axial_Plane_Complete_Guide.html",
    title="Q021: Recumbent Folds, Horizontal Axial Planes & Nappe Tectonics",
    badge="GGM - 2/2019 • Structural Geology & Tectonics",
    h1_title="Q021: Geometry and Mechanics of Recumbent Folds: Horizontal Axial Surfaces & Nappes",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 21<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 190); M.J. Fleuty (<em>Proceedings of the Geologists' Association</em>, 1964); Marland P. Billings (<em>Structural Geology</em>, pp. 48–52)",
    part1_html=q21_part1,
    part2_html=q21_part2,
    part3_html=q21_part3
)

# ==========================================
# QUESTION 22: BLENDED UNCONFORMITY - RESIDUAL SOIL CONTACT
# ==========================================
q22_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Stratigraphic Anatomy of Unconformities & Residual Contacts</div>
    <div class="card-body">
      <p>An <strong>unconformity</strong> represents a substantial hiatus or gap in the geologic rock record, marking a prolonged period of non-deposition, subaerial exposure, and weathering/erosion before younger sedimentary strata are deposited. While most unconformities are marked by a sharp, knife-edge erosional contact, a special and critically diagnostic category occurs when ancient in-situ subaerial weathering produced a deep residual soil mantle that was preserved beneath the transgressing younger strata—termed a <strong>blended unconformity</strong>.</p>

      <div class="quote-box bangar">
        "Where younger sedimentary rocks are deposited directly over an ancient land surface consisting of thick residual soil that grades imperceptibly downwards into the underlying crystalline bedrock, the boundary between the two formations is transitional and fuzzy rather than a sharp plane. Such an unconformity is called a <strong>blended unconformity</strong>. It indicates that the old weathered mantle was preserved without being stripped away by erosion before the deposition of younger sediments."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Chapter 8: Unconformities, p. 225)</span>
      </div>

      <p>In classical stratigraphic taxonomy (Dunbar & Rodgers, 1957; Billings, 1972; Boggs, 2011), unconformities are classified into four primary geometrical and genetic categories:</p>
      <ul>
        <li><strong>Blended Unconformity:</strong> A contact where younger sedimentary strata rest upon an ancient weathered paleosol/saprolite profile that grades transitionally into the underlying parent rock. The contact is blurred, transitional, and mechanically interlocking.</li>
        <li><strong>Nonconformity:</strong> An unconformity where layered sedimentary or volcanic rocks rest upon an eroded, unweathered surface of older crystalline plutonic (granitic) or metamorphic (schist, gneiss) basement rocks, separated by a sharp contact.</li>
        <li><strong>Angular Unconformity:</strong> An unconformity where younger, flatter-lying strata overlie older tilted, folded, or deformed strata with a discordant angular relationship (e.g., Hutton's classic unconformity at Siccar Point).</li>
        <li><strong>Disconformity:</strong> An unconformity between parallel sedimentary layers where the contact is a sharp, irregular erosional surface, but bedding planes above and below are parallel.</li>
      </ul>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q022/boggs_fig12_5_unconformities_blended.png" alt="Sam Boggs Jr Four Types of Unconformities">
        <div class="tb-caption">
          <strong>Figure 22.1: Types of Unconformities in Stratigraphic Analysis (Sam Boggs Jr., Fig. 12.5).</strong> Diagrammatic cross-sections illustrating (A) Angular unconformity, (B) Disconformity, (C) Nonconformity, and (D) Paraconformity, alongside the blended paleosol-residual soil contact.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Matrix: Types of Unconformable Contacts</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Unconformity Type</th>
            <th>Underlying Rock Type</th>
            <th>Structural Discordance</th>
            <th>Contact Nature</th>
            <th>Diagnostic Geological Process</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Blended Unconformity</strong></td>
            <td>In-situ residual soil / saprolite over bedrock</td>
            <td>Variable</td>
            <td><strong>Gradational, fuzzy, transitional contact</strong></td>
            <td>Preservation of ancient subaerial paleosol under calm transgression</td>
          </tr>
          <tr>
            <td><strong>Nonconformity</strong></td>
            <td>Crystalline plutonic or metamorphic rock</td>
            <td>Non-stratified beneath; bedded above</td>
            <td>Sharp, distinct erosional contact</td>
            <td>Exhumation and deep erosion of crystalline basement</td>
          </tr>
          <tr>
            <td><strong>Angular Unconformity</strong></td>
            <td>Tilted, folded, or deformed strata</td>
            <td><strong>Angular discordance ($\Delta \theta > 0$)</strong></td>
            <td>Sharp truncational contact</td>
            <td>Orogenic folding/tilting followed by regional peneplanation</td>
          </tr>
          <tr>
            <td><strong>Disconformity</strong></td>
            <td>Parallel sedimentary strata</td>
            <td>None (Bedding parallel above and below)</td>
            <td>Irregular, channelized erosional relief</td>
            <td>Subaerial fluvial incision or sea-level drop without folding</td>
          </tr>
          <tr>
            <td><strong>Paraconformity</strong></td>
            <td>Parallel sedimentary strata</td>
            <td>None</td>
            <td>Flat, featureless bedding-plane contact</td>
            <td>Submarine non-deposition / hiatal starvation (recognized only by fossils)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q22_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 22)</div>
    <div class="q-stmt">
      22. A contact of younger sediments deposited over a thick residual soil that grades into underlying bedrock is called :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Discontinuity</div>
      <div class="raw-opt">(B) Non-conformity</div>
      <div class="raw-opt correct">(C) Blended unconformity &nbsp;✔</div>
      <div class="raw-opt">(D) Angular unconformity</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Blended unconformity</div>
      <div class="sub">
        In stratigraphy and historical geology (K.M. Bangar, p. 225; Marland P. Billings, p. 230; Dunbar & Rodgers, 1957; Sam Boggs Jr., p. 415), an unconformable boundary where younger sediments overlie an in-situ <strong>residual soil that grades into underlying bedrock</strong> is specifically termed a <strong>Blended unconformity</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Discontinuity</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> "Discontinuity" is a general geotechnical term describing any physical break or fracture in a rock mass (such as joints, faults, or bedding planes). It is not the formal stratigraphic designation for a residual soil unconformity.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Non-conformity</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A nonconformity is an unconformity where bedded sedimentary rocks lie upon clean, unweathered, deeply eroded plutonic igneous rocks (granite) or metamorphic rocks (gneiss) across a <em>sharp, distinct erosional surface</em>, devoid of a transitional residual soil zone.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Blended unconformity</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> When a deep ancient regolith/paleosol mantle is preserved during marine or fluvial transgression, the younger basal sediments mix with the loose topsoil, creating a gradational contact that blends downward into saprolite and solid bedrock. This is the exact, verbatim textbook definition of a <strong>blended unconformity</strong>.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Angular unconformity</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> An angular unconformity is defined by structural angular discordance, where younger strata overlie older folded or tilted strata at an angle, marked by a sharp truncational plane.
    </div>
  </div>
"""

q22_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Paleopedology & Saprolite Profiles in the Stratigraphic Record</div>
    <div class="card-body">
      <p>Blended unconformities are of paramount importance in paleoclimatology and mineral exploration:</p>
      <ul>
        <li><strong>Paleosol Recognition:</strong> The transitional zone preserves fossil soil horizons (paleosols), featuring root traces, pedogenic caliche nodules, and illuvial clay cutans that preserve ancient atmospheric conditions ($p\text{CO}_2$, precipitation).</li>
        <li><strong>Paleoplacer Deposits:</strong> Chemical leaching of the bedrock during residual weathering often leaves dense, resistant minerals (gold, cassiterite, diamonds) concentrated directly within the blended basal sediment wedge.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What geochemical profile in a blended unconformity confirms that the transitional zone represents an in-situ paleosol rather than an unweathered sedimentary conglomerate?
          <div class="pq-ans">✔ Correct Answer: Downward increasing Chemical Index of Alteration (CIA) toward the top surface, along with depletion of mobile cations ($Ca^{2+}, Na^+, K^+$) and enrichment in residual $Al_2O_3$ and $Fe_2O_3$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In-situ chemical leaching strips mobile bases from feldspars, leaving kaolinite/bauxite near the surface grading into unweathered granite at depth.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a "saprolite"?
          <div class="pq-ans">✔ Correct Answer: Chemically weathered bedrock that retains the original crystalline rock textures, structures, and relict fabric, but has lost coherence and density.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Saprolite forms the $C$-horizon of deep weathering profiles, often underlying the basal sediments of a blended unconformity.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> How does a "buttress unconformity" (onlap unconformity) develop?
          <div class="pq-ans">✔ Correct Answer: Younger sedimentary beds onlap and terminate progressively against steep, rugged paleotopographic paleocliffs of older rock.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Instead of horizontal planar layering, strata terminate at high angles against the buried mountain flank.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In civil engineering and tunneling, why do blended unconformities present severe excavation hazards?
          <div class="pq-ans">✔ Correct Answer: Unpredictable transitions from competent fresh bedrock to completely decomposed, water-saturated saprolite soil cause sudden collapse and crown cave-ins.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Tunneling machines encountering an unexpected deep weathering pocket experience sudden loss of face support.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the difference between a Disconformity and a Paraconformity?
          <div class="pq-ans">✔ Correct Answer: A disconformity shows visible physical erosional relief (valleys/channels); a paraconformity is a flat bedding plane with no visible physical erosion, identified solely by fossil gaps.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Paraconformities represent submarine hiatal surfaces where sedimentation ceased without subaerial stream gouging.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "basal conglomerate", and where is it found relative to an unconformity?
          <div class="pq-ans">✔ Correct Answer: A conglomerate layer situated at the very base of the younger sedimentary sequence directly above an unconformity, composed of pebbles derived from the underlying older rocks.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Transgressing waves rework the weathered surface, concentrating resistant quartz and quartzite pebbles into a basal conglomerate.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Can an unconformity act as a petroleum trap?
          <div class="pq-ans">✔ Correct Answer: Yes; permeable sandstone beds truncated beneath an impermeable shale unconformity form world-class "truncation traps" (e.g., Prudhoe Bay, Alaska).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The overlying impermeable transgressive shale seals the porous, dipping reservoir beds below.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is Hutton's classic "Great Unconformity" at Siccar Point, Scotland?
          <div class="pq-ans">✔ Correct Answer: A classic angular unconformity where gently dipping Devonian Old Red Sandstone overlies near-vertical, folded Silurian greywackes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> James Hutton used this in 1788 to demonstrate deep geological time ("no vestige of a beginning, no prospect of an end").
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=22,
    filename="Q022_Blended_Unconformity_Residual_Soil_Contact_Complete_Guide.html",
    title="Q022: Blended Unconformities, Paleosols & Stratigraphic Hiatus Analysis",
    badge="GGM - 2/2019 • Stratigraphy & Historical Geology",
    h1_title="Q022: Stratigraphic Architecture of Unconformities: Blended Contacts & Paleosol Preservations",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 22<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 225); Dunbar & Rodgers (<em>Principles of Stratigraphy</em>, 1957); Sam Boggs Jr. (<em>Sedimentology & Stratigraphy</em>, Ch. 12, pp. 415–420)",
    part1_html=q22_part1,
    part2_html=q22_part2,
    part3_html=q22_part3
)

# ==========================================
# QUESTION 23: INTERSECTION OF BEDDING & CLEAVAGE - LINEATION
# ==========================================
q23_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Kinematics of Intersection Lineations in Tectonic Shear Zones</div>
    <div class="card-body">
      <p>In structural geology and metamorphic petrology (Ramsay & Huber, 1983; Hobbs, Means & Williams, 1976; Billings, 1972; Fossen, 2016), when two penetrative planar fabric surfaces intersect in three-dimensional space, their line of intersection geometrically generates a prominent linear fabric termed an <strong>intersection lineation</strong>. Specifically, the intersection of primary sedimentary bedding ($S_0$) with a secondary tectonic cleavage or foliation plane ($S_1$) produces an <strong>$S_0 \\times S_1$ intersection lineation (denoted $L_0^1$ or $L_{1/0}$)</strong>.</p>

      <div class="quote-box bangar">
        "Any linear feature developed in a rock as a result of tectonic deformation is called a <strong>lineation</strong>. When a rock possessing primary bedding planes is subjected to folding and develops a secondary tectonic cleavage, the line of intersection of the bedding planes ($S_0$) with the cleavage planes ($S_1$) produces a conspicuous lineation on both surfaces, known as an <strong>intersection lineation</strong>. In cylindrical folds, this lineation is parallel to the fold axis."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Chapter 7: Secondary Structures & Lineations, p. 235)</span>
      </div>

      <p>The mathematical and geometric properties of intersection lineations are of foundational importance in structural mapping:</p>

      <div class="formula-card">
        <div class="formula-title">Vector Cross-Product Formulation of Intersection Lineation</div>
        $$\\vec{L}_{1/0} = \\vec{n}_{S0} \\times \\vec{n}_{S1}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $\vec{n}_{S0}$ is the normal vector to the bedding plane ($S_0$) and $\vec{n}_{S1}$ is the normal vector to the cleavage plane ($S_1$). In cylindrical folds, the intersection lineation vector $\vec{L}_{1/0}$ is <strong>co-axial with the fold hinge line ($\vec{B}$)</strong>!</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q023/bangar_p125_cleavage_foliation_lineation.png" alt="K.M. Bangar Cleavage Foliation and Intersection Lineation">
        <div class="tb-caption">
          <strong>Figure 23.1: Intersection Lineation Anatomy (K.M. Bangar, p. 125).</strong> Hand specimen and outcrop block diagram showing sedimentary bedding ($S_0$) intersected by axial-planar slaty cleavage ($S_1$), creating prominent $L_0 \times S_1$ pencil cleavage and parallel intersection lineation.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Structural Taxonomy: Lineation vs. Boudin vs. Mullion vs. Joint</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Structural Element</th>
            <th>Dimensionality</th>
            <th>Primary Origin</th>
            <th>Diagnostic Field Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lineation</strong></td>
            <td><strong>1D (Linear fabric)</strong></td>
            <td><strong>Intersection of planar fabrics ($S_0 \\times S_1$)</strong> or mineral alignment</td>
            <td>Parallel stripes, mineral streaks, crinkles, pencil cleavage</td>
          </tr>
          <tr>
            <td><strong>Boudin / Boudinage</strong></td>
            <td>2D/3D pinch-and-swell</td>
            <td>Tensile stretching of a competent layer within incompetent matrix</td>
            <td>Sausage-shaped segmented blocks with quartz-filled necks</td>
          </tr>
          <tr>
            <td><strong>Mullion Structure</strong></td>
            <td>1D/2D cylindrical flutes</td>
            <td>Buckling instability at interface between high-contrast rocks</td>
            <td>Cuspate-lobate fluted rock columns parallel to fold axes</td>
          </tr>
          <tr>
            <td><strong>Joint</strong></td>
            <td>2D (Planar fracture)</td>
            <td>Brittle tensile or shear fracturing without displacement</td>
            <td>Clean, planar fractures cutting across rock masses</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q23_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 23)</div>
    <div class="q-stmt">
      23. The intersection of bedding and cleavage produces :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Lineation &nbsp;✔</div>
      <div class="raw-opt">(B) Boudin</div>
      <div class="raw-opt">(C) Mullion structure</div>
      <div class="raw-opt">(D) Joint</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Lineation</div>
      <div class="sub">
        In structural geology (K.M. Bangar, p. 235; Ramsay & Huber, 1983; Marland P. Billings, p. 340; Haakon Fossen, p. 272), the linear trace produced by the geometric intersection of <strong>bedding ($S_0$) and cleavage ($S_1$)</strong> is universally termed an <strong>Intersection lineation</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Lineation</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> When a secondary planar cleavage intersects a primary sedimentary bedding plane, their intersection creates a linear fabric visible on both surfaces as fine stripes, color bandings, or fine crinkles, termed an <strong>intersection lineation</strong>.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Boudin</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A boudin (sausage structure) is formed by the longitudinal tensile stretching and necking of a competent layer (such as quartzite or amphibolite) embedded in an incompetent ductile matrix (such as marble or shale), not by the simple geometric intersection of cleavage and bedding.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Mullion structure</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Mullion structures are large-scale cylindrical, fluted rock columns formed at the competency boundary between contrasting rock layers under ductile shortening, where cusps point toward the more competent rock. They are not produced by the intersection of bedding and cleavage.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Joint</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A joint is a brittle planar fracture across which negligible shear displacement has occurred. It is a planar surface, not a linear intersection fabric.
    </div>
  </div>
"""

q23_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Field Application: Structural Mapping using $S_0 \\times S_1$ Lineations</div>
    <div class="card-body">
      <p>The intersection lineation is one of the most powerful diagnostic tools in structural field mapping:</p>
      <ul>
        <li><strong>Parallelism to Regional Fold Axes ($B$-Lineation):</strong> In cylindrical folds, the intersection lineation ($L_{1/0}$) is strictly parallel to the major fold axis. Thus, by measuring the plunge and trend of intersection lineations in a single small hand specimen, a geologist immediately determines the orientation of a regional mountain-scale fold!</li>
        <li><strong>Pencil Cleavage:</strong> In mudstones and siltstones where bedding ($S_0$) and tectonic cleavage ($S_1$) intersect with equal fracture frequency, the rock breaks into elongated, slender polygonal rods termed "pencil structure" or pencil cleavage.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What is the difference between an "intersection lineation" and a "mineral stretching lineation"?
          <div class="pq-ans">✔ Correct Answer: An intersection lineation is a purely geometric intersection of two planes (parallel to fold axes, $B$-axis); a mineral stretching lineation reflects finite plastic extension of minerals parallel to tectonic transport ($X$-axis).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Intersection lineations generally form perpendicular to shortening ($B \perp \sigma_1$), whereas stretching lineations elongate parallel to the transport direction ($a$-lineation).
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What causes "pencil cleavage" in slightly deformed shales?
          <div class="pq-ans">✔ Correct Answer: The mutual intersection of bedding fissility ($S_0$) and incipient tectonic cleavage ($S_1$) breaking the rock into long pencil-like prismatic rods.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Characteristic of early-stage tectonic deformation in foreland fold-and-thrust belts (e.g., Appalachian Valley and Ridge).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is a "crenulation lineation"?
          <div class="pq-ans">✔ Correct Answer: Microscopic fold hinges formed when a second-generation cleavage ($S_2$) micro-folds an earlier foliation ($S_1$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Produces fine, corrugated crinkle lineations across schistosity planes in poly-deformed metamorphic schists.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In stereographic projection, how is an intersection lineation determined from the strikes and dips of bedding and cleavage?
          <div class="pq-ans">✔ Correct Answer: By finding the point of intersection between the two great circles representing $S_0$ and $S_1$; the plunge and trend of this point gives the lineation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The intersection of two planar great circles on a Wulff or Schmidt net is a point representing a line in space.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "rodded structure" (rodding)?
          <div class="pq-ans">✔ Correct Answer: Cylindrical rods of quartz formed by the folding, shearing, and isolation of quartz veins parallel to the fold hinge.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Competent quartz veins are severed and rolled into linear rods within weaker mica schist matrices.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the difference between an $S$-tectonite and an $L$-tectonite?
          <div class="pq-ans">✔ Correct Answer: An $S$-tectonite is dominated by planar foliation (flattening strain, $k < 1$); an $L$-tectonite is dominated by linear fabric (constrictional strain, $k > 1$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In Flinn's strain diagram, cigar-shaped constrictional strain ellipsoids produce pure $L$-tectonites devoid of planar foliation.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Can intersection lineation occur in undeformed horizontal sedimentary rocks?
          <div class="pq-ans">✔ Correct Answer: No; development of cleavage requires tectonic compressive strain exceeding the ductile yield strength of the rock.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Undeformed rocks only possess bedding ($S_0$). Cleavage ($S_1$) requires regional tectonic shortening.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does cleavage refraction occur when cleavage passes from a shale layer into a sandstone layer?
          <div class="pq-ans">✔ Correct Answer: Competency contrast causes the strain ellipse orientation to rotate, causing cleavage to steepen in competent sandstone and flatten in incompetent shale.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The refraction of cleavage creates differing intersection lineation characteristics across alternating beds.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=23,
    filename="Q023_Intersection_Bedding_Cleavage_Lineation_Complete_Guide.html",
    title="Q023: Structural Lineations, Bedding-Cleavage Intersections & Fabric Analysis",
    badge="GGM - 2/2019 • Structural Geology & Tectonic Fabrics",
    h1_title="Q023: Structural Mechanics of Lineations: Bedding-Cleavage Intersections & Tectonic Kinematics",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 23<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 235); John G. Ramsay & Martin I. Huber (<em>Techniques of Modern Structural Geology</em>, Vol. 2, 1983); Marland P. Billings (<em>Structural Geology</em>, pp. 340–345)",
    part1_html=q23_part1,
    part2_html=q23_part2,
    part3_html=q23_part3
)

# ==========================================
# QUESTION 24: HIGH ANGLE FAULTS - DIP GREATER THAN 45 DEGREES
# ==========================================
q24_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Geometric Classification of Faults: The 45-Degree Threshold</div>
    <div class="card-body">
      <p>In structural geology and fault mechanics (Billings, 1972; Bangar, p. 212; Davis & Reynolds, 1996; Fossen, 2016), faults are systematically classified based on the <strong>angle of inclination (dip, $\\delta$) of the fault plane</strong> relative to the horizontal datum:</p>
      <ul>
        <li><strong>High-Angle Faults:</strong> Faults whose fault planes dip at an angle <strong>greater than $45^\\circ$ ($\\text{Dip } > 45^\\circ$)</strong>.</li>
        <li><strong>Low-Angle Faults:</strong> Faults whose fault planes dip at an angle <strong>less than or equal to $45^\\circ$ ($\\text{Dip } \\le 45^\\circ$)</strong>.</li>
      </ul>

      <div class="quote-box bangar">
        "According to the angle of dip of the fault plane, faults are divided into high-angle faults and low-angle faults. Faults which dip at an angle greater than $45^\\circ$ are called <strong>high-angle faults</strong>. Faults which dip at an angle less than $45^\\circ$ are called low-angle faults (such as thrust faults). Most normal faults are high-angle faults, typically dipping at $60^\\circ$."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Chapter 7: Fault Classification, p. 212)</span>
      </div>

      <p>The selection of <strong>$45^\\circ$</strong> as the critical dividing threshold is rooted in the mathematical mechanics of displacement resolution:</p>

      <div class="formula-card">
        <div class="formula-title">Mathematical & Mechanical Significance of the 45-Degree Boundary</div>
        $$\\text{Throw } T = S_d \\cdot \\sin \\delta \\quad \\text{and} \\quad \\text{Heave } H = S_d \\cdot \\cos \\delta$$
        $$\\text{When } \\delta > 45^\\circ: \\sin \\delta > \\cos \\delta \\implies \\mathbf{\\text{Throw} > \\text{Heave}} \\quad (\\text{Vertical displacement dominates})$$
        $$\\text{When } \\delta < 45^\\circ: \\sin \\delta < \\cos \\delta \\implies \\mathbf{\\text{Heave} > \\text{Throw}} \\quad (\\text{Horizontal displacement dominates})$$
        $$\\text{At } \\delta = 45^\\circ: \\sin 45^\\circ = \\cos 45^\\circ = \\frac{1}{\\sqrt{2}} \\approx 0.7071 \\implies \\mathbf{\\text{Throw} = \\text{Heave}}$$
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q024/fossen_fig9_2_high_angle_vs_low_angle_faults.png" alt="Haakon Fossen High Angle vs Low Angle Fault Classification">
        <div class="tb-caption">
          <strong>Figure 24.1: Fault Classification by Dip Angle (Haakon Fossen, Fig. 9.2).</strong> Dip spectra showing high-angle faults ($\text{Dip} > 45^\circ$, typically Andersonian normal faults dipping at $\approx 60^\circ$) versus low-angle faults ($\text{Dip} \le 45^\circ$, typically thrust faults dipping at $\approx 30^\circ$ and detachment faults).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comprehensive Structural Fault Taxonomy by Dip Angle</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Dip Angle Class</th>
            <th>Dip Range ($\\delta$)</th>
            <th>Dominant Displacement Component</th>
            <th>Primary Fault Types Included</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>High-Angle Fault</strong></td>
            <td><strong>$> 45^\\circ$ (up to $90^\\circ$)</strong></td>
            <td><strong>Throw $>$ Heave (Vertical offset dominates)</strong></td>
            <td>Andersonian normal faults ($60^\\circ$), vertical strike-slip faults ($90^\\circ$), high-angle reverse faults</td>
          </tr>
          <tr>
            <td><strong>Low-Angle Fault</strong></td>
            <td><strong>$\\le 45^\\circ$ (down to $0^\\circ$)</strong></td>
            <td><strong>Heave $>$ Throw (Horizontal translation dominates)</strong></td>
            <td>Thrust faults ($30^\\circ$), overthrusts, detachment faults, lag faults</td>
          </tr>
          <tr>
            <td><strong>Subhorizontal / Flat Fault</strong></td>
            <td>$< 10^\\circ - 15^\\circ$</td>
            <td>Pure horizontal displacement</td>
            <td>Décollement, sole thrusts, basal detachment planes</td>
          </tr>
          <tr>
            <td><strong>Vertical Fault</strong></td>
            <td>$90^\\circ$ ($\\text{Hade} = 0^\\circ$)</td>
            <td>Pure strike-slip or pure vertical throw</td>
            <td>Transform faults, wrench faults, pure vertical dip-slip faults</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q24_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 24)</div>
    <div class="q-stmt">
      24. High angle faults are those that dip greater than :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) 60 degree</div>
      <div class="raw-opt">(B) 65 degree</div>
      <div class="raw-opt">(C) 40 degree</div>
      <div class="raw-opt correct">(D) 45 degree &nbsp;✔</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) 45 degree</div>
      <div class="sub">
        In standard structural geology (K.M. Bangar, p. 212; Marland P. Billings, p. 145; Davis & Reynolds, 1996; Haakon Fossen, p. 338), <strong>high-angle faults</strong> are defined as faults that dip <strong>greater than 45 degrees</strong> ($\text{Dip} > 45^\circ$).
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) 60 degree</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> While $60^\circ$ is the classic theoretical dip angle for Andersonian normal faults in pristine isotropic rock ($\theta = 45^\circ + \phi/2$), it is not the formal boundary defining high-angle faults. Any fault dipping at $50^\circ$ or $55^\circ$ is legally and structurally classified as a high-angle fault.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) 65 degree</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> $65^\circ$ is an arbitrary steep dip value without mathematical or taxonomic standing as a boundary criterion.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 40 degree</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A fault dipping at $40^\circ$ is a low-angle fault (such as a classic thrust fault dipping at $30^\circ - 40^\circ$).
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) 45 degree</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> The universal textbook standard divides faults into low-angle ($\le 45^\circ$) and high-angle ($> 45^\circ$). At $45^\circ$, throw exactly equals heave; above $45^\circ$, vertical displacement exceeds horizontal displacement, defining a <strong>high-angle fault</strong>.
    </div>
  </div>
"""

q24_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Anderson's Theoretical Conjugate Angles vs. High/Low Angle Classification</div>
    <div class="card-body">
      <p>Anderson's fault classification elegantly mirrors the $45^\circ$ threshold:</p>
      <ul>
        <li><strong>Normal Faults (Extensional):</strong> $\sigma_1$ vertical $\implies \text{Dip } \theta = 45^\circ + \phi/2 \approx 60^\circ > 45^\circ \implies$ <strong>High-Angle Faults</strong>.</li>
        <li><strong>Thrust Faults (Compressional):</strong> $\sigma_1$ horizontal $\implies \text{Dip } \theta = 45^\circ - \phi/2 \approx 30^\circ < 45^\circ \implies$ <strong>Low-Angle Faults</strong>.</li>
        <li><strong>Strike-Slip Faults:</strong> $\sigma_2$ vertical $\implies \text{Dip } \theta = 90^\circ > 45^\circ \implies$ <strong>Vertical / High-Angle Faults</strong>.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What is a "thrust fault", and what is its maximum allowable dip angle in standard structural classification?
          <div class="pq-ans">✔ Correct Answer: A reverse fault with a dip angle of less than or equal to $45^\circ$ (typically $\approx 30^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A reverse fault with dip $>45^\circ$ is termed a high-angle reverse fault; if dip $\le 45^\circ$, it is termed a thrust fault.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a "low-angle normal fault" (LANF), and why was its discovery controversial in Mohr-Coulomb mechanics?
          <div class="pq-ans">✔ Correct Answer: A normal fault dipping at $<30^\circ$; controversial because classic Andersonian mechanics predicts normal faults cannot initiate at dips $<45^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Slip on low-angle normal faults requires extreme fluid overpressure ($u \to \sigma_v$) or rolling-hinge rotation of initially steep faults.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> At what exact dip angle does the Throw of a fault equal its Heave?
          <div class="pq-ans">✔ Correct Answer: Exactly $45^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> $\tan \delta = \text{Throw} / \text{Heave}$. When $\delta = 45^\circ$, $\tan 45^\circ = 1.0 \implies \text{Throw} = \text{Heave}$.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is a "blind fault"?
          <div class="pq-ans">✔ Correct Answer: A fault that terminates upward within the crust and does not rupture the ground surface, often generating folding above its tip.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Blind thrust faults (e.g., 1994 Northridge earthquake) represent major seismic hazards because they lack surface fault scarps.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "transform fault", and what is its typical dip angle?
          <div class="pq-ans">✔ Correct Answer: A plate-boundary strike-slip fault connecting offset mid-ocean ridge segments, typically with a vertical dip ($\delta \approx 90^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> First defined by J. Tuzo Wilson (1965); displacement is horizontal and terminates abruptly at active ridge crests.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> In geological maps, what map pattern distinguishes a high-angle fault from a low-angle thrust fault crossing rugged topography?
          <div class="pq-ans">✔ Correct Answer: High-angle faults cut across topographic contours in straight lines (Rule of V's); low-angle faults trace highly sinuous paths parallel to topographic contour lines.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A vertical or near-vertical plane is unaffected by hills and valleys, cutting straight across the map.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is the "Byerlee's Law" friction coefficient for crustal rocks, and how does it determine fault dip?
          <div class="pq-ans">✔ Correct Answer: $\mu \approx 0.85$ (for $\sigma_n < 200\text{ MPa}$) and $\mu \approx 0.60$ (for higher stress), giving an internal friction angle $\phi \approx 30^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Setting $\phi = 30^\circ$ into $\theta = 45^\circ + \phi/2$ yields the canonical $60^\circ$ dip for normal faults and $30^\circ$ for thrust faults.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a "scissors fault"?
          <div class="pq-ans">✔ Correct Answer: A rotational fault where the hanging wall is upthrown at one end of the fault strike and downthrown at the opposite end.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Movement rotates around a central pivot point where throw is zero, reversing the apparent throw direction along strike.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=24,
    filename="Q024_High_Angle_Faults_Dip_Greater_45_Degrees_Complete_Guide.html",
    title="Q024: High-Angle vs. Low-Angle Faults, 45-Degree Boundary & Slip Mechanics",
    badge="GGM - 2/2019 • Structural Geology & Fault Mechanics",
    h1_title="Q024: Classification of Faults by Dip Angle: The 45-Degree Threshold & Mechanics",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 24<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 212); Marland P. Billings (<em>Structural Geology</em>, pp. 145–148); Haakon Fossen (<em>Structural Geology</em>, Ch. 9)",
    part1_html=q24_part1,
    part2_html=q24_part2,
    part3_html=q24_part3
)

print("Batch 2 (Q018 - Q024) generated successfully.")
