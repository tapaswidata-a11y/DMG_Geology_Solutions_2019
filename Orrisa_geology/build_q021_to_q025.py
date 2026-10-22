#!/usr/bin/env python3
"""
Masterclass Builder for Batch 3: Structural Geology (Q021 - Q025)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q021: Thrust Fault Dip Angle Threshold
# ==============================================================================
def generate_q021():
    title = "Q021: Mechanics of Contractional Faulting: Thrust vs. Reverse Fault Dip Angles | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Fault Mechanics"
    h1_title = "Q021: Mechanics of Contractional Faulting: Thrust vs. Reverse Fault Dip Angles"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 21<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 9: Contractional Regimes, pp. 195–215); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds & Faults, pp. 200–205); E.M. Anderson, <em>The Dynamics of Faulting</em> (1951, Oliver & Boyd); Davis, Reynolds & Kluth, <em>Structural Geology of Rocks and Regions</em> (3rd Ed., Wiley)."""

    part1 = r"""
  <!-- CARD 1: ANDERSONIAN DYNAMICS & COULOMB CRITERIA -->
  <div class="card">
    <div class="card-header bg-blue">1. Andersonian Fault Mechanics & Theoretical Dip Angle</div>
    <div class="card-body">
      <p>In structural geology and geodynamics, <strong>thrust faults</strong> and <strong>reverse faults</strong> are contractional dip-slip fault systems in which the hanging wall moves upward relative to the footwall, accommodating horizontal crustal shortening ($\Delta L < 0$) and vertical thickening. The orientation and dip angle ($\theta$) of these faults are governed by E.M. Anderson's (1905, 1951) dynamic theory of faulting and the Mohr-Coulomb failure criterion:</p>

      <ul>
        <li><strong>Principal Stress Orientation:</strong> In a contractional tectonic regime (such as collisional orogenic belts like the Himalayas or Appalachian foreland), the maximum compressive principal stress ($\sigma_1$) is horizontal, intermediate stress ($\sigma_2$) is horizontal and parallel to fault strike, and the minimum principal stress ($\sigma_3$) is vertical (overburden weight).</li>
        <li><strong>Theoretical Andersonian Failure Angle:</strong> According to Coulomb fracture mechanics, shear rupture planes form at an angle $\theta$ relative to $\sigma_1$:
        $$\theta = 45^\circ - \frac{\phi}{2}$$
        Where $\phi$ is the angle of internal friction of typical crustal rocks ($\phi \approx 30^\circ$). Because $\sigma_1$ is horizontal, the theoretical dip of a newly initiated thrust fault is:
        $$\theta = 45^\circ - \frac{30^\circ}{2} = 45^\circ - 15^\circ = 30^\circ$$
        Thus, Andersonian mechanics predicts that contractional shear planes naturally initiate with gentle dips around $30^\circ$, universally satisfying the criterion <strong>$< 45^\circ$</strong>.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q21/fossen_fig9_2_three_fault_regimes.png" alt="Anderson's Three Fault Regimes from Haakon Fossen">
        <div class="tb-caption">
          <strong>Figure 21.1 (Haakon Fossen, <em>Structural Geology</em>, 2nd Ed., Fig. 9.2):</strong> Anderson's three tectonic fault regimes. In the contractional thrust regime, $\sigma_1$ is horizontal and $\sigma_3$ is vertical, generating shallow-dipping conjugate shear fractures dipping at $\approx 30^\circ$ ($< 45^\circ$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: STRUCTURAL CLASSIFICATION: THRUST VS REVERSE -->
  <div class="card">
    <div class="card-header bg-indigo">2. Geometric Demarcation: Thrust Fault ($< 45^\circ$) vs. Reverse Fault ($> 45^\circ$)</div>
    <div class="card-body">
      <p>In both classical and modern structural geology syllabi (Bangar, p. 202; Billings, 1972; Fossen, 2016), the dip angle of $45^\circ$ represents the formal dividing boundary between contractional fault species:</p>

      <table>
        <thead>
          <tr>
            <th>Contractional Fault Type</th>
            <th>Dip Angle Range ($\theta$)</th>
            <th>Tectonic Architecture & Kinematics</th>
            <th>Classic Geological Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Thrust Fault (Sensu Stricto)</strong></td>
            <td><strong>$< 45^\circ$</strong> (typically $10^\circ - 35^\circ$)</td>
            <td>Low-angle contraction; large horizontal transport ($> 10 - 100\text{ km}$); forms nappes, klippes, and tectonic windows (fensters)</td>
            <td>Main Boundary Thrust (MBT), Main Central Thrust (MCT) in Himalayas; Moine Thrust (Scotland)</td>
          </tr>
          <tr>
            <td><strong>Low-Angle Overthrust / Decollement</strong></td>
            <td>$< 10^\circ - 15^\circ$ (sub-horizontal)</td>
            <td>Basal detachment gliding along weak evaporite/shale horizons (thin-skinned fold-and-thrust belts)</td>
            <td>Main Frontal Thrust (MFT) / Siwalik detachment</td>
          </tr>
          <tr>
            <td><strong>High-Angle Reverse Fault</strong></td>
            <td>$> 45^\circ$ (typically $55^\circ - 75^\circ$)</td>
            <td>Steep contractional slip; dominantly vertical stratigraphic offset; often reactivated steep normal faults (tectonic inversion)</td>
            <td>Laramide basement-cored uplifts (Rocky Mountains, USA)</td>
          </tr>
        </tbody>
      </table>

      <div class="quote-box bangar">
        "Thrust Fault: A reverse fault in which the fault plane dips at an angle less than 45° (usually between 10° and 30°) is termed a thrust fault or overthrust. In such faults, older rocks are pushed horizontally over younger rocks across large distances."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds and Faults, p. 202)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q21/fossen_fig9_2c_reverse_thrust_fault.png" alt="Reverse vs Thrust Fault Geometry from Fossen">
        <div class="tb-caption">
          <strong>Figure 21.2 (Haakon Fossen, Fig. 9.2c):</strong> Cross-sectional geometry of contractional faults. Shows low-angle thrust faults ($\theta < 45^\circ$) with extensive horizontal displacement placing older strata over younger strata.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: TECTONIC FEATURES: NAPPES, KLIPPES AND FENSTERS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Regional Tectonic Manifestations: Nappes, Klippen & Fensters</div>
    <div class="card-body">
      <p>Because thrust faults dip at shallow angles ($< 45^\circ$), prolonged erosion of the displaced thrust sheet (allochthon) uncovers complex geometric outcrop patterns:</p>
      <ul>
        <li><strong>Nappe:</strong> A colossal, sheet-like allochthonous rock mass displaced horizontally tens to hundreds of kilometers along a low-angle thrust surface.</li>
        <li><strong>Klippe (Plural: Klippen):</strong> An isolated, erosional remnant of the thrust sheet stranded atop younger autochthonous footwall rocks.</li>
        <li><strong>Fenster (Tectonic Window):</strong> An erosional hole or window gouged through the hanging wall sheet exposing the underlying younger autochthonous rocks beneath.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 21)</div>
    <div class="q-stmt">
      Q21. Thrust faults are reverse faults that dip at :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) > 45°</div>
      <div class="raw-opt correct">(B) < 45° &nbsp;✔</div>
      <div class="raw-opt">(C) 45°</div>
      <div class="raw-opt">(D) 90°</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) < 45°</div>
      <div class="sub">
        In standard structural geology (Bangar, p. 202; Billings; Fossen), a contractional fault where the hanging wall moves upward is formally classified as a <strong>thrust fault</strong> when the fault plane dips at an inclination <strong>less than 45° ($\theta < 45^\circ$)</strong>. Contractional faults dipping $> 45^\circ$ are termed reverse faults.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) > 45°</span>
      <span class="tag wrong">Incorrect (Defines High-Angle Reverse Faults)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Contractional faults dipping at angles greater than 45° ($\theta > 45^\circ$) are specifically designated as <em>high-angle reverse faults</em>. They are typically produced by tectonic inversion of older steep normal faults or deep basement upthrusts, producing high vertical throw with minimal horizontal displacement.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) < 45°</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> The universal geometric criterion that separates a thrust fault from a generic reverse fault is a dip angle <strong>$< 45^\circ$</strong>. In nature and Andersonian failure models ($\theta = 45^\circ - \phi/2 \approx 30^\circ$), most thrusts initiate at $25^\circ - 35^\circ$ and often flatten into bedding-parallel decollements dipping $< 15^\circ$.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 45°</span>
      <span class="tag wrong">Incorrect (Arbitrary Division Boundary, Not a Range)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> 45° is the geometric boundary dividing low-angle thrusts ($< 45^\circ$) from high-angle reverse faults ($> 45^\circ$). A thrust fault does not dip exclusively at exactly 45°.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) 90°</span>
      <span class="tag wrong">Incorrect (Vertical Fault / Strike-Slip Fault)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A dip of 90° represents a vertical fault. In Andersonian mechanics, vertical faults with horizontal displacement are strike-slip (wrench) faults ($\sigma_2$ vertical).
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Fault Classification Matrix (Andersonian Mechanics)</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Fault Class</th>
            <th>Kinematic Slip Type</th>
            <th>Dip Angle ($\theta$)</th>
            <th>Stress Regime ($\sigma_1, \sigma_2, \sigma_3$)</th>
            <th>Tectonic Shortening / Extension</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Thrust Fault</strong></td>
            <td>Hanging wall moves UP</td>
            <td><strong>$< 45^\circ$ (typically $\sim 30^\circ$)</strong></td>
            <td>$\sigma_1$ horizontal, $\sigma_2$ horizontal, $\sigma_3$ vertical</td>
            <td><strong>Horizontal Shortening</strong> ($\Delta L < 0$)</td>
          </tr>
          <tr>
            <td><strong>High-Angle Reverse Fault</strong></td>
            <td>Hanging wall moves UP</td>
            <td>$> 45^\circ$ (typically $60^\circ - 70^\circ$)</td>
            <td>Contractional inversion / basement uplifts</td>
            <td>Horizontal Shortening ($\Delta L < 0$)</td>
          </tr>
          <tr>
            <td><strong>Normal Fault</strong></td>
            <td>Hanging wall moves DOWN</td>
            <td>$\sim 60^\circ$ (Andersonian: $45^\circ + \phi/2$)</td>
            <td>$\sigma_1$ vertical, $\sigma_2$ horizontal, $\sigma_3$ horizontal</td>
            <td><strong>Horizontal Extension</strong> ($\Delta L > 0$)</td>
          </tr>
          <tr>
            <td><strong>Strike-Slip Fault</strong></td>
            <td>Horizontal lateral shear</td>
            <td>$\approx 90^\circ$ (Near-vertical)</td>
            <td>$\sigma_1$ horizontal, $\sigma_2$ vertical, $\sigma_3$ horizontal</td>
            <td>Conservative (no net extension or shortening)</td>
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
          <strong>Practice Q1 (Numerical):</strong> A thrust fault dips at an angle $\theta = 30^\circ$ into a collisional mountain belt. Geodetic and seismic measurements indicate a net dip-slip displacement (slip) of $S = 5.0\text{ km}$. Calculate the horizontal crustal shortening ($\Delta L$) and vertical tectonic throw ($h$) produced by this fault.
          <div class="pq-ans">✔ Worked Answer: Horizontal Shortening $\Delta L = 4.33\text{ km}$; Vertical Throw $h = 2.50\text{ km}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\text{Shortening } \Delta L = S \cdot \cos\theta = 5.0 \cdot \cos 30^\circ = 5.0 \times 0.8660 = 4.33\text{ km}$$<br>
            $$\text{Vertical Throw } h = S \cdot \sin\theta = 5.0 \cdot \sin 30^\circ = 5.0 \times 0.5000 = 2.50\text{ km}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>blind thrust fault</em>, and why does it represent a grave seismic hazard in urban foreland regions?
          <div class="pq-ans">✔ Correct Answer: A thrust fault that terminates underground without breaking the surface, creating an anticline fold (fault-propagation fold) above it.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the fault plane does not rupture the surface, it lacks a recognizable surface fault scarp, obscuring active seismic accumulation until a catastrophic earthquake occurs (e.g., 1994 Northridge, California earthquake).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What stratigraphic diagnostic rule is universally violated when a borehole penetrates an active thrust fault?
          <div class="pq-ans">✔ Correct Answer: Steno's Law of Superposition; the borehole encounters older rocks overlying younger rocks, and repeats stratigraphic sections.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Low-angle thrusting transports deeply buried older strata up and over younger rocks in the footwall, causing vertical repetition of layers.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Himalayan tectonics, name the major regional low-angle thrust fault separating the Lesser Himalayan sedimentary sequence from the Higher Himalayan Crystallines.
          <div class="pq-ans">✔ Correct Answer: The Main Central Thrust (MCT).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The MCT is an iconic ductile shear zone and low-angle thrust dipping gently to the north, along which high-grade metamorphic rocks were thrust over low-grade Lesser Himalayan rocks.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a <em>duplex</em> in thrust belt kinematics?
          <div class="pq-ans">✔ Correct Answer: A stack of imbricate thrust slices (horses) bounded below by a floor thrust (sole thrust) and above by a roof thrust.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Duplexes accommodate massive crustal shortening by packing multiple lenticular thrust sheets into an overlapping shingles-like structural stack.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the difference between a <em>ramp</em> and a <em>flat</em> in thin-skinned fold-and-thrust belts?
          <div class="pq-ans">✔ Correct Answer: A flat is a bedding-parallel thrust segment in weak shale/salt; a ramp is a steeper segment cutting obliquely across competent sandstone/limestone.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Faults propagate easily along weak bedding planes (flats, $\theta \approx 0^\circ - 5^\circ$) and step upward through strong layers along ramps ($\theta \approx 30^\circ$), generating fault-bend folds.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How does high pore fluid pressure ($u$) facilitate low-angle thrusting under Hubbert and Rubey's (1959) overthrust mechanism?
          <div class="pq-ans">✔ Correct Answer: Pore fluid pressure reduces effective normal stress ($\sigma_n' = \sigma_n - u$), reducing frictional resistance along the fault plane to near zero.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Trapped high fluid pressures float the thrust sheet, allowing colossal nappes to glide horizontally across hundreds of kilometers without shattering.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> A tectonic window (fenster) is an erosional hole that exposes:
          <div class="pq-ans">✔ Correct Answer: Autochthonous (younger) footwall rocks surrounded by allochthonous (older) hanging wall rocks.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Deep stream incision cuts through the allochthonous thrust sheet, opening a window to view the younger, overridden rocks underneath.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 21, part1, part2, part3)


# ==============================================================================
# Q022: Plunge of Linear Feature
# ==============================================================================
def generate_q022():
    title = "Q022: Orientation of Linear Structural Features: Plunge vs. Rake / Pitch | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Lineations"
    h1_title = "Q022: Orientation of Linear Structural Features: Plunge vs. Rake / Pitch"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 22<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 2: Structural Orientation, pp. 24–35); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Dip, Strike & Plunge, pp. 191–194, Fig. 7.5); Davis, Reynolds & Kluth (3rd Ed., pp. 12–18)."""

    part1 = r"""
  <!-- CARD 1: LINEAR STRUCTURAL ORIENTATION -->
  <div class="card">
    <div class="card-header bg-blue">1. Geometric Definitions: Plunge & Trend of Linear Elements</div>
    <div class="card-body">
      <p>In structural geology, geological structures are geometric entities classified as either <strong>planar features</strong> (e.g., bedding planes, fault planes, foliation surfaces, joint sets) or <strong>linear features</strong> (e.g., fold hinge lines, stretching lineations, intersection lineations, slickenlines, elongate mineral needles). While planar features are completely defined by <em>Strike and Dip</em>, linear features are completely defined in space by <strong>Plunge and Trend</strong>:</p>

      <ul>
        <li><strong>Plunge ($\beta$):</strong> The <strong>vertical angle</strong> between the horizontal plane and the inclined linear feature, measured downward in a vertical plane from the horizontal to the line ($0^\circ \le \beta \le 90^\circ$). If a line lies horizontally, its plunge is $0^\circ$; if it is vertical, its plunge is $90^\circ$.</li>
        <li><strong>Trend ($\alpha$):</strong> The geographic azimuth (compass bearing, $000^\circ - 360^\circ$) of the vertical plane containing the linear feature, pointing in the direction of downward plunge.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Structural Notation for Linear Orientation</div>
        $$\text{Notation: } \beta \to \alpha \quad \text{(e.g., } 35^\circ \to 140^\circ\text{)}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Read as: "Plunging 35 degrees toward an azimuth of 140 degrees (South-East)". The plunge angle is always written first as a two-digit number, followed by the trend as a three-digit azimuth.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q22/linear_feature_plunge_trend_block.png" alt="Linear Feature Plunge and Trend 3D Block Diagram">
        <div class="tb-caption">
          <strong>Figure 22.1: 3D Geometry of a Linear Structural Feature.</strong> Showing the Plunge angle ($\beta$) measured strictly in the vertical plane, the Trend azimuth ($\alpha$), and the Rake / Pitch angle ($\phi$) measured within an inclined plane.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: CRITICAL DISCRIMINATION: PLUNGE VS RAKE / PITCH -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Crucial Distinction: Plunge vs. Rake (Pitch)</div>
    <div class="card-body">
      <p>Candidates must strictly master the geometric difference between <strong>Plunge</strong> and <strong>Rake (Pitch)</strong>:</p>

      <ul>
        <li><strong>Plunge:</strong> Measured strictly within a <strong>true vertical plane</strong> intersecting the line. It requires no reference to an inclined plane ($0^\circ \le \text{Plunge} \le 90^\circ$).</li>
        <li><strong>Rake (or Pitch):</strong> The acute angle measured <strong>within an inclined structural plane</strong> between the linear feature and the horizontal strike line of that plane ($0^\circ \le \text{Rake} \le 90^\circ$). For example, slickenlines (fault scratch marks) on a fault plane dipping $60^\circ$ are measured directly on the rock face as a rake angle relative to the fault's strike line.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Mathematical Relation Connecting Plunge, Dip, and Rake</div>
        $$\sin(\text{Plunge}) = \sin(\text{Dip}) \cdot \sin(\text{Rake})$$
        $$\tan(\text{Apparent Dip}) = \tan(\text{True Dip}) \cdot \cos(\text{Angle to Strike})$$
      </div>

      <div class="quote-box bangar">
        "Plunge: The angle of inclination of the fold axis (or any linear feature) with the horizontal, measured in a vertical plane, is called the plunge of the fold. When the axis is horizontal, the plunge is zero."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds, pp. 192–193, Fig. 7.5)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q22/bangar_fig7_5_7_8_plunge_fold_axis.png" alt="Plunge of Fold Axis from Bangar">
        <div class="tb-caption">
          <strong>Figure 22.2 (K.M. Bangar, Fig. 7.5 & 7.8):</strong> Plunging fold geometry, illustrating the vertical inclination angle between the horizontal plane and the fold axis (plunge).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Strike and Dip (Planar Parameters)</div>
    <div class="card-body">
      <p>Understanding geometric dimensionality eliminates distractors:</p>
      <ul>
        <li><strong>Strike:</strong> The compass bearing of a horizontal line formed by the intersection of an inclined <em>geological plane</em> with the horizontal plane. It applies to planes, not lines.</li>
        <li><strong>Dip:</strong> The maximum vertical inclination angle of an inclined <em>geological plane</em> relative to the horizontal. Dip is measured perpendicular to the strike line of a plane.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 22)</div>
    <div class="q-stmt">
      Q22. The vertical angle between the horizontal plane and the axis or line of maximum elongation of a... (linear feature) is known as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) strike</div>
      <div class="raw-opt">(B) dip</div>
      <div class="raw-opt">(C) rake</div>
      <div class="raw-opt correct">(D) plunge &nbsp;✔</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) plunge</div>
      <div class="sub">
        The vertical angle measured in a vertical plane between the horizontal plane and an inclined linear feature (such as a fold axis, line of maximum elongation, or mineral lineation) is universally defined as the <strong>plunge</strong> of that line (Bangar, p. 192; Fossen, p. 25).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) strike</span>
      <span class="tag wrong">Incorrect (Compass Azimuth of a Planar Feature)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Strike is the horizontal compass direction of a planar surface (bedding, joint, fault). It is a horizontal azimuth, not a vertical angle of inclination, and applies exclusively to planes, not linear axes.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) dip</span>
      <span class="tag wrong">Incorrect (Vertical Angle of an Inclined Plane)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Dip is the angle of inclination of a <em>planar surface</em> measured perpendicular to strike. While both dip and plunge are vertical angles, "dip" is reserved strictly for planar surfaces, whereas "plunge" is the precise scientific term for linear features.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) rake</span>
      <span class="tag wrong">Incorrect (Angle Measured in an Inclined Plane, Not Vertical Plane)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Rake (also termed pitch) is the angle between a linear feature and the strike line measured <em>within an inclined plane</em>. Plunge is measured strictly in a <em>true vertical plane</em>.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) plunge</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard definition in structural geology, the vertical angle between the horizontal reference plane and an inclined line (fold axis, mineral stretching lineation, or line of maximum elongation) is the <strong>plunge</strong>. It ranges from $0^\circ$ (horizontal line) to $90^\circ$ (vertical line).
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Structural Attitude Measurements: Planar vs. Linear</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Structural Measurement</th>
            <th>Applies To</th>
            <th>Plane of Measurement</th>
            <th>Angular Range</th>
            <th>Standard Structural Notation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Plunge</strong></td>
            <td><strong>Linear Feature</strong></td>
            <td><strong>True Vertical Plane</strong></td>
            <td><strong>$0^\circ \text{ to } 90^\circ$</strong></td>
            <td>$\beta \to \alpha$ (e.g., $30^\circ \to 045^\circ$)</td>
          </tr>
          <tr>
            <td><strong>Trend</strong></td>
            <td>Linear Feature</td>
            <td>Horizontal Plane (Azimuth)</td>
            <td>$000^\circ \text{ to } 360^\circ$</td>
            <td>Compass bearing of plunge direction</td>
          </tr>
          <tr>
            <td><strong>Rake / Pitch</strong></td>
            <td>Linear Feature on a Plane</td>
            <td><strong>Inclined Structural Plane</strong></td>
            <td>$0^\circ \text{ to } 90^\circ$</td>
            <td>e.g., $45^\circ\text{NE on plane } 120/40^\circ\text{SW}$</td>
          </tr>
          <tr>
            <td><strong>Dip</strong></td>
            <td><strong>Planar Feature</strong></td>
            <td>True Vertical Plane $\perp$ Strike</td>
            <td>$0^\circ \text{ to } 90^\circ$</td>
            <td>Strike/Dip (e.g., $045^\circ/30^\circ\text{SE}$)</td>
          </tr>
          <tr>
            <td><strong>Strike</strong></td>
            <td>Planar Feature</td>
            <td>Horizontal Plane (Intersection)</td>
            <td>$000^\circ \text{ to } 360^\circ$</td>
            <td>Compass azimuth of horizontal line</td>
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
          <strong>Practice Q1 (Numerical Trigonometry):</strong> Slickenlines on a fault plane dipping $60^\circ$ display a rake of $30^\circ$. Calculate the true plunge of the slickenlines.
          <div class="pq-ans">✔ Worked Answer: $\text{Plunge } \beta \approx 25.66^\circ$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            Using the fundamental geometric formula:
            $$\sin(\text{Plunge}) = \sin(\text{Dip}) \cdot \sin(\text{Rake}) = \sin(60^\circ) \cdot \sin(30^\circ) = (0.8660) \times (0.5000) = 0.4330$$<br>
            $$\text{Plunge } \beta = \arcsin(0.4330) \approx 25.66^\circ$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> If a mineral lineation lies directly along the true dip direction of an inclined foliation plane, what is the mathematical relationship between its plunge and the plane's dip?
          <div class="pq-ans">✔ Correct Answer: Plunge equals True Dip ($\beta = \text{Dip}$); Rake is $90^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the line points down the steepest path of the plane, $\sin\beta = \sin(\text{Dip}) \sin(90^\circ) = \sin(\text{Dip})$, meaning plunge is identical to the plane's dip angle.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> If a linear feature lies parallel to the strike line of an inclined plane, what are its plunge and rake?
          <div class="pq-ans">✔ Correct Answer: Plunge is $0^\circ$ (horizontal line); Rake is $0^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Any line parallel to the strike is horizontal by definition, hence its vertical plunge angle is zero.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What type of lineation is formed by the intersection of sedimentary bedding ($S_0$) with tectonic cleavage foliation ($S_1$)?
          <div class="pq-ans">✔ Correct Answer: An intersection lineation ($L_{0-1}$), which is parallel to the fold hinge line.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In cylindrical folds, axial planar cleavage intersects bedding along lines parallel to the regional fold axis, allowing fold plunge to be determined from hand samples.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> On a geological map, how is a plunging anticline recognized from the outcrop pattern of its beds?
          <div class="pq-ans">✔ Correct Answer: The outcrop pattern forms a V-shaped or U-shaped nose that points (closes) in the direction of plunge.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> For an anticline, the outcrop closes in the direction of plunge, with older rocks inside the V; for a syncline, the outcrop opens in the direction of plunge (closes away from plunge).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a <em>stretching lineation</em>, and what does its plunge and trend indicate in ductile shear zones?
          <div class="pq-ans">✔ Correct Answer: Elongate mineral aggregates (stretched pebbles, quartz ribbons) parallel to the maximum finite elongation direction ($\lambda_1$ or $X$-axis of the strain ellipsoid).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Stretching lineations record the flow trajectory of ductile tectonic transport within mylonites and orogenic shear belts.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> On an equal-area stereonet (Schmidt net), how is a linear structural feature represented?
          <div class="pq-ans">✔ Correct Answer: As a single point (pole), plotted at an angular distance from the primitive circle equal to $90^\circ - \text{plunge}$ along its trend radius.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Planes plot as great circle arcs; lines plot as unique discrete points on the lower hemisphere projection.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> If a fold has an axis that is horizontal, what is its plunge, and what is the term for such a fold?
          <div class="pq-ans">✔ Correct Answer: Plunge is $0^\circ$; termed a Non-Plunging (or Horizontal) Fold.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A horizontal fold produces perfectly parallel ribbon-like outcrop stripes on a planar horizontal geologic map that never close into V-shaped noses.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 22, part1, part2, part3)


# ==============================================================================
# Q023: Hooke's Law
# ==============================================================================
def generate_q023():
    title = "Q023: Rheology of Geomaterials: Hooke's Law of Linear Elasticity | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Rock Mechanics & Geomechanics"
    h1_title = "Q023: Rheology of Geomaterials: Hooke's Law of Linear Elasticity"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 23<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 6: Stress & Elasticity, pp. 115–128); Jaeger, Cook & Zimmerman, <em>Fundamentals of Rock Mechanics</em> (4th Ed., Wiley-Blackwell); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 10: Rock Mechanics, pp. 360–368)."""

    part1 = r"""
  <!-- CARD 1: HOOKE'S LAW & LINEAR ELASTICITY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Principle of Linear Elasticity: Hooke's Law (1678)</div>
    <div class="card-body">
      <p>In continuum mechanics, rock mechanics, and geodynamics, the mechanical response of solid Earth materials to applied tectonic stresses is governed by <strong>rheology</strong>. When a solid geomaterial is subjected to differential stress below its elastic yield limit ($\sigma < \sigma_y$), it deforms through <strong>recoverable elastic deformation</strong>:</p>

      <ul>
        <li><strong>Hooke's Law Formulation:</strong> First formulated anagrammatically in 1676 and published in 1678 by the English polymath Robert Hooke as <em>Ut tensio, sic vis</em> ("As the extension, so the force"), Hooke's Law states that <strong>strain ($\epsilon$) is directly proportional to applied stress ($\sigma$)</strong>:
        $$\sigma = E \cdot \epsilon$$
        Where $\sigma$ is normal stress ($\text{Pa}$ or $\text{MPa}$), $\epsilon = \Delta L / L_0$ is dimensionless axial strain, and $E$ is the material proportionality constant known as <strong>Young's Modulus</strong> (Modulus of Elasticity).</li>
        <li><strong>Instantaneous & Recoverable:</strong> Elastic strain occurs instantaneously upon stress application and is completely recovered (reverses to zero strain) when the stress is removed, storing energy as strain potential energy ($U = \frac{1}{2} \sigma \epsilon$).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">The Four Fundamental Elastic Constants for Isotropic Rocks</div>
        $$E = \frac{\sigma}{\epsilon} \quad \text{(Young's Modulus)} \qquad \nu = -\frac{\epsilon_{\text{lateral}}}{\epsilon_{\text{axial}}} \quad \text{(Poisson's Ratio)}$$
        $$G = \frac{\tau}{\gamma} = \frac{E}{2(1 + \nu)} \quad \text{(Shear Modulus)} \qquad K = \frac{\Delta P}{\Delta V / V} = \frac{E}{3(1 - 2\nu)} \quad \text{(Bulk Modulus)}$$
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q23/fossen_fig6_3_hookes_law_elasticity.png" alt="Hooke's Law Linear Elasticity from Haakon Fossen">
        <div class="tb-caption">
          <strong>Figure 23.1 (Haakon Fossen, <em>Structural Geology</em>, Fig. 6.3):</strong> Linear elastic stress-strain behavior governed by Hooke's Law ($\sigma = E\epsilon$). Illustrates the linear elastic slope ($E$), elastic limit, yield point, and post-yield failure regimes.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE COMPLETE STRESS-STRAIN SPECTRUM OF ROCKS -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Complete Rock Deformation Spectrum: Elastic, Plastic & Brittle</div>
    <div class="card-body">
      <p>Under laboratory triaxial testing, crystalline rocks pass through three distinct deformation regimes as differential stress ($\sigma_1 - \sigma_3$) increases:</p>

      <ul>
        <li><strong>1. Linear Elastic Region (Hookean):</strong> The initial straight-line portion where strain is proportional to stress. The slope of this line equals Young's Modulus ($E$). Rocks like quartzite and granite have high $E \approx 60 - 80\text{ GPa}$; soft shales have $E \approx 10 - 20\text{ GPa}$.</li>
        <li><strong>2. Elastic Limit / Yield Strength ($\sigma_y$):</strong> The critical threshold beyond which deformation ceases to be linear and permanent irreversible strain begins.</li>
        <li><strong>3. Ductile / Plastic Deformation:</strong> Permanent strain accumulated without loss of macroscopic cohesion (governed by power-law dislocation creep $\dot{\epsilon} = A \sigma^n \exp(-Q/RT)$). Strain is NOT proportional to stress.</li>
        <li><strong>4. Brittle Rupture / Failure:</strong> Catastrophic loss of cohesion along shear fracture planes governed by Mohr-Coulomb and Griffith's failure criteria.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q23/rock_mechanics_hookes_law_stress_strain.png" alt="Rock Mechanics Stress Strain Curve">
        <div class="tb-caption">
          <strong>Figure 23.2: Complete Triaxial Stress-Strain Curve of Rock.</strong> Showing the Hookean linear elastic regime, yield point, plastic flow plateau, and brittle ultimate failure strength.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Mohr, Griffith, and Plasticity Distractors</div>
    <div class="card-body">
      <p>Candidates must clearly differentiate Hooke's Law from failure and non-elastic rheologies:</p>
      <ul>
        <li><strong>(A) Mohr’s Circle:</strong> A two-dimensional graphical representation of the coordinate transformation equations for normal ($\sigma$) and shear ($\tau$) stress acting on planes of varying orientation. It is a mathematical stress transformation tool, not a physical law of proportionality.</li>
        <li><strong>(B) Plastic Deformation:</strong> Irreversible permanent strain occurring beyond the yield strength without cohesion loss. In plasticity, strain continues to increase under constant yield stress (perfect plasticity), violating proportionality.</li>
        <li><strong>(D) Griffith’s Theory:</strong> A brittle fracture mechanics theory (A.A. Griffith, 1921) explaining rock failure via stress concentration at the tips of microscopic pre-existing elliptical micro-cracks ($K_{IC} = \sigma \sqrt{\pi a}$). It governs tensile and shear rupture, not linear elastic proportionality.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 23)</div>
    <div class="q-stmt">
      Q23. In elastic deformation, when strain is proportional to stress is known as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Mohr’s circle</div>
      <div class="raw-opt">(B) Plastic deformation</div>
      <div class="raw-opt correct">(C) Hooke’s law &nbsp;✔</div>
      <div class="raw-opt">(D) Griffith’s theory</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Hooke’s law</div>
      <div class="sub">
        In solid mechanics and rock physics, the fundamental relationship stating that <strong>strain is directly proportional to applied stress ($\sigma = E\epsilon$)</strong> during recoverable elastic deformation is known universally as <strong>Hooke’s law</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Mohr’s circle</span>
      <span class="tag wrong">Incorrect (Stress Transformation Graphical Circle)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Mohr's circle is a geometric graphical construct (developed by Christian Otto Mohr in 1882) used to calculate normal and shear stresses acting on arbitrarily oriented planes from known principal stresses ($\sigma_1, \sigma_3$). It does not define stress-strain proportionality.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Plastic deformation</span>
      <span class="tag wrong">Incorrect (Non-Linear, Irreversible Permanent Flow)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Plastic deformation occurs only after the elastic limit has been exceeded. It represents permanent, non-recoverable change in shape where strain is highly non-linear and not proportional to stress.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Hooke’s law</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Formulated by Robert Hooke in 1678, Hooke's Law represents the foundational constitutive equation of linear elasticity: $\sigma = E\epsilon$. It states that within the elastic limit, strain is directly proportional to the applied stress, and the material returns to its original dimensions when the stress is released.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Griffith’s theory</span>
      <span class="tag wrong">Incorrect (Microcrack Brittle Fracture Mechanics)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A.A. Griffith's (1921) theory is a brittle failure criterion based on the thermodynamic balance between surface energy and elastic strain energy around micro-cracks. It explains why rocks fracture at stresses far below their theoretical atomic bond strengths, but does not describe linear elasticity.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Rheological & Failure Models in Rock Mechanics</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Constitutive / Mechanical Law</th>
            <th>Primary Mathematical Formulation</th>
            <th>Rheological Behavior</th>
            <th>Geological Process & Environment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Hooke’s Law (Elasticity)</strong></td>
            <td><strong>$\sigma = E \cdot \epsilon$</strong></td>
            <td><strong>Instantaneous, recoverable, linear strain proportional to stress</strong></td>
            <td>Seismic wave propagation; crustal tidal flexure; coseismic elastic rebound</td>
          </tr>
          <tr>
            <td><strong>Newtonian Viscosity</strong></td>
            <td>$\sigma = \eta \cdot \dot{\epsilon}$</td>
            <td>Linear viscous fluid flow; strain rate proportional to stress</td>
            <td>Magma chamber convection; asthenospheric mantle flow</td>
          </tr>
          <tr>
            <td><strong>Saint-Venant Plasticity</strong></td>
            <td>$\sigma = \sigma_y$ (for $\dot{\epsilon} > 0$)</td>
            <td>Rigid-perfectly plastic; zero strain until yield stress $\sigma_y$ is reached</td>
            <td>Glacial basal sliding; cohesive mudflow initiation</td>
          </tr>
          <tr>
            <td><strong>Power-Law Creep (Dislocation)</strong></td>
            <td>$\dot{\epsilon} = A \sigma^n \exp(-Q/RT)$</td>
            <td>Non-linear ductile flow ($n \approx 3 - 4$)</td>
            <td>Mid-to-lower crustal ductile shear zones; mylonite formation</td>
          </tr>
          <tr>
            <td><strong>Mohr-Coulomb Failure</strong></td>
            <td>$\tau_f = c + \sigma_n \tan\phi$</td>
            <td>Brittle shear fracture envelope</td>
            <td>Upper crustal faulting; landslide shear plane failure</td>
          </tr>
          <tr>
            <td><strong>Griffith Failure Criterion</strong></td>
            <td>$(\sigma_1 - \sigma_3)^2 = 8 T_0 (\sigma_1 + \sigma_3)$</td>
            <td>Tensile and shear fracture from elliptical microcracks</td>
            <td>Hydraulic fracturing; joint initiation; volcanic dyke propagation</td>
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
          <strong>Practice Q1 (Numerical):</strong> A core of Charnockite with an original length $L_0 = 100.0\text{ mm}$ and cross-sectional area $A = 2000\text{ mm}^2$ is compressed in a uniaxial press. The applied axial load is $F = 160\text{ kN}$. If the rock's Young's Modulus is $E = 80\text{ GPa}$, calculate the resulting axial stress ($\sigma$), axial strain ($\epsilon$), and total length reduction ($\Delta L$).
          <div class="pq-ans">✔ Worked Answer: $\sigma = 80\text{ MPa}$; $\epsilon = 0.0010$ ($0.10\%$); $\Delta L = 0.10\text{ mm}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\sigma = \frac{F}{A} = \frac{160,000\text{ N}}{2 \times 10^{-3}\text{ m}^2} = 80 \times 10^6\text{ Pa} = 80\text{ MPa}$$<br>
            By Hooke's Law ($\epsilon = \sigma / E$):
            $$\epsilon = \frac{80 \times 10^6\text{ Pa}}{80 \times 10^9\text{ Pa}} = 1.0 \times 10^{-3} = 0.0010$$<br>
            $$\Delta L = \epsilon \cdot L_0 = 0.0010 \times 100.0\text{ mm} = 0.10\text{ mm}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> In elasticity, what is <em>Poisson’s Ratio ($\nu$)</em>, and what is its typical value for crystalline rocks?
          <div class="pq-ans">✔ Correct Answer: The ratio of lateral transverse strain to axial longitudinal strain ($\nu = -\epsilon_{\text{lat}} / \epsilon_{\text{ax}}$); typically $\nu \approx 0.20 - 0.30$ (Poisson solid: $\nu = 0.25$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Under uniaxial compression, rocks expand laterally as they shorten longitudinally. An incompressible material has $\nu = 0.50$.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What geophysical theory, proposed by H.F. Reid following the 1906 San Francisco earthquake, directly relies on Hooke's Law of elasticity?
          <div class="pq-ans">✔ Correct Answer: The Elastic Rebound Theory.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Tectonic plate motions slowly bend crustal rocks elastically (storing Hookean strain energy) until shear stress overcomes fault friction, causing rapid elastic rebound that releases seismic waves.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What are the two <em>Lamé parameters</em> ($\lambda$ and $\mu$) used to describe linear isotropic elasticity in seismology?
          <div class="pq-ans">✔ Correct Answer: $\mu$ is the Shear Modulus (modulus of rigidity $G$), and $\lambda$ is Lamé's first parameter ($\lambda = K - \frac{2}{3}\mu$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In a Poisson solid ($\lambda = \mu$), the seismic compressional wave velocity relates to shear velocity as $V_p = \sqrt{3} V_s \approx 1.732 V_s$.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How is seismic P-wave velocity ($V_p$) expressed in terms of Bulk Modulus ($K$), Shear Modulus ($G$), and rock density ($\rho$)?
          <div class="pq-ans">✔ Correct Answer: $V_p = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> P-wave speed is controlled by the elastic resistance of the rock lattice to volumetric compression ($K$) and shear deformation ($G$).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What mechanical model represents a <em>Maxwell viscoelastic</em> body, and how does it respond to an instantaneous stress step?
          <div class="pq-ans">✔ Correct Answer: A Hookean spring connected in series with a Newtonian viscous dashpot; responds with instantaneous elastic strain followed by steady viscous creep.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The Maxwell model explains post-glacial isostatic rebound and post-seismic relaxation in the upper mantle.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is <em>elastic hysteresis</em> in rock mechanics?
          <div class="pq-ans">✔ Correct Answer: The loop-like divergence between the loading and unloading stress-strain curves caused by micro-scale frictional sliding along internal microcracks.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The area enclosed by the hysteresis loop represents energy permanently dissipated as heat (internal friction damping) during cyclic loading.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does Bulk Modulus ($K$) describe the elastic behavior of fluids (water, magma), whereas Shear Modulus ($G$) is zero?
          <div class="pq-ans">✔ Correct Answer: Fluids resist volumetric compression ($K > 0$) but possess zero resistance to shear deformation ($G = 0$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because $G = 0$ in liquids, shear waves cannot propagate ($V_s = \sqrt{G/\rho} = 0$), explaining why S-waves are blocked by Earth's liquid outer core.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 23, part1, part2, part3)


# ==============================================================================
# Q024: Fold Hinge Line Maximum Curvature
# ==============================================================================
def generate_q024():
    title = "Q024: Fold Anatomy: Hinge Zone, Maximum Curvature & Inflection Points | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Fold Mechanics"
    h1_title = "Q024: Fold Anatomy: Hinge Zone, Maximum Curvature & Inflection Points"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 24<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 11 & 12: Folds, pp. 240–265); J.G. Ramsay, <em>Folding and Fracturing of Rocks</em> (McGraw-Hill, 1967); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds, pp. 191–195); van der Pluijm & Marshak, <em>Earth Structure</em> (2nd Ed., Norton)."""

    part1 = r"""
  <!-- CARD 1: FOLD ANATOMY & GEOMETRIC DEFINITIONS -->
  <div class="card">
    <div class="card-header bg-blue">1. Fold Anatomy & Mathematical Curvature Analysis</div>
    <div class="card-body">
      <p>In structural geology and differential geometry (Ramsay, 1967; Fossen, 2016), a <strong>fold</strong> is defined as a curved or deformed planar surface that was originally flat. Across any folded layer, structural geologists analyze the mathematical rate of change of layer dip relative to arc length ($\kappa = d\theta / ds$, where $\kappa$ is local curvature):</p>

      <ul>
        <li><strong>Hinge Point:</strong> The point of <strong>maximum curvature</strong> ($\kappa = \kappa_{\text{max}}$) on a two-dimensional cross-sectional fold profile.</li>
        <li><strong>Hinge Line (Hinge):</strong> The continuous three-dimensional line or locus formed by connecting all points of maximum curvature across a folded geological surface. The hinge line represents the physical line of maximum bend of the fold.</li>
        <li><strong>Hinge Zone:</strong> The curved region of high curvature immediately surrounding the hinge line, separating the two limbs.</li>
        <li><strong>Inflection Point:</strong> The point on the fold limb where curvature is zero ($\kappa = 0$) and where the sense of curvature changes from convex (anticlinal) to concave (synclinal).</li>
        <li><strong>Fold Limb:</strong> The relatively straight or low-curvature section of the fold located between the hinge zone and the inflection point.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q24/fossen_fig12_1_fold_hinge_anatomy.png" alt="Fold Anatomy Hinge Line Inflection Point from Haakon Fossen">
        <div class="tb-caption">
          <strong>Figure 24.1 (Haakon Fossen, <em>Structural Geology</em>, Fig. 12.1):</strong> Anatomical elements of a fold profile. Shows the hinge point as the locus of maximum curvature ($\kappa_{\text{max}}$), the inflection point of zero curvature, and the axial trace connecting hinge lines.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: HINGE LINE VS FOLD AXIS (CRUCIAL DISCRIMINATION) -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Vital Distinction: Hinge Line vs. Fold Axis vs. Axial Surface</div>
    <div class="card-body">
      <p>Candidates frequently confuse three distinct structural terms:</p>

      <ul>
        <li><strong>1. Hinge Line (Physical Entity):</strong> A physical, real line on a specific folded surface where curvature is maximum. If the fold is non-cylindrical (e.g., dome or basin), the hinge line is curved.</li>
        <li><strong>2. Fold Axis (Geometric Kinematic Generator):</strong> An imaginary straight line that, when moved parallel to itself in space, sweeps out and generates the fold surface. A fold axis can only exist for <em>cylindrical folds</em>.</li>
        <li><strong>3. Axial Surface (Axial Plane):</strong> The surface (planar or curved) formed by connecting the hinge lines of all successive layered beds stacked through the fold profile.</li>
      </ul>

      <div class="quote-box">
        "The hinge of a fold is the line of maximum curvature. It connects points of maximum curvature on a folded surface. The limbs are the parts of the fold that have lower curvature and lie between adjacent hinges."
        <span class="quote-ref">— Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, 2016, p. 242)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q24/vdpm_hinge_line_curvature.png" alt="Hinge Line and Curvature Profile from van der Pluijm and Marshak">
        <div class="tb-caption">
          <strong>Figure 24.2 (van der Pluijm & Marshak, <em>Earth Structure</em>):</strong> Curvature distribution across a profile of a folded layer, proving mathematically that the hinge coincides strictly with the curvature maximum ($d\theta/ds = \text{max}$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Axial Plane, Limb, and Axis</div>
    <div class="card-body">
      <p>Understanding geometric definitions eliminates the distractors:</p>
      <ul>
        <li><strong>(A) Axial plane:</strong> A surface (planar or curved) connecting the hinge lines of multiple stacked layers. It is an extensive 2D surface, not the 1D line of maximum curvature within a bed.</li>
        <li><strong>(B) Fold limb:</strong> The straight or gently dipping segment of the fold displaying minimum curvature ($\kappa \to 0$).</li>
        <li><strong>(C) Axis:</strong> An imaginary geometric generator line. A fold axis has a fixed orientation in space but no fixed position on the rock; the hinge is the actual physical line of maximum bend on the rock.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 24)</div>
    <div class="q-stmt">
      Q24. The line of maximum curvature in a fold is known as —________.
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) axial plane</div>
      <div class="raw-opt">(B) fold limb</div>
      <div class="raw-opt">(C) axis</div>
      <div class="raw-opt correct">(D) hinge &nbsp;✔</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) hinge</div>
      <div class="sub">
        In structural geology, the line connecting all points of maximum curvature across a folded surface is formally designated as the <strong>hinge</strong> (or <strong>hinge line</strong>).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) axial plane</span>
      <span class="tag wrong">Incorrect (Surface Connecting Successive Hinge Lines)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The axial plane (axial surface) is a two-dimensional surface that connects the hinge lines of successive folded layers throughout the rock volume. It is not the 1D line of maximum curvature on a single folded layer.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) fold limb</span>
      <span class="tag wrong">Incorrect (Zone of Minimum Curvature)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The fold limbs are the side flanks of the fold located between adjacent hinges. Mechanically and mathematically, the limbs are zones of low or zero curvature ($\kappa \approx 0$), the exact opposite of maximum curvature.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) axis</span>
      <span class="tag wrong">Incorrect (Imaginary Geometric Generator Line)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The fold axis is an abstract mathematical line that, when moved parallel to itself, generates the cylindrical fold surface. It has orientation but no specific physical location on the rock. The hinge is the actual physical line of maximum curvature on the layer.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) hinge</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard international definition (Ramsay 1967; Fossen 2016; Bangar p. 192), the locus of points where the rate of change of layer dip is maximum ($\kappa = d\theta/ds = \text{max}$) is the <strong>hinge</strong> (or hinge line).
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Structural Anatomy of Fold Elements</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Fold Anatomical Element</th>
            <th>Geometric Nature</th>
            <th>Mathematical Definition</th>
            <th>Field Identification Criteria</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Hinge Line (Hinge)</strong></td>
            <td><strong>1D Physical Line</strong></td>
            <td><strong>Locus of Maximum Curvature ($\kappa = \text{max}$)</strong></td>
            <td><strong>Sharpest bend on folded bedding plane; high strain concentration</strong></td>
          </tr>
          <tr>
            <td><strong>Inflection Line</strong></td>
            <td>1D Line</td>
            <td>Locus of Zero Curvature ($\kappa = 0$)</td>
            <td>Point of inflection where limb changes curvature sense</td>
          </tr>
          <tr>
            <td><strong>Axial Surface (Plane)</strong></td>
            <td>2D Surface (Planar or Curved)</td>
            <td>Surface connecting hinge lines of successive layers</td>
            <td>Bisects the interlimb angle in symmetrical folds; parallel to cleavage</td>
          </tr>
          <tr>
            <td><strong>Fold Axis</strong></td>
            <td>1D Imaginary Line</td>
            <td>Direction vector generating cylindrical fold</td>
            <td>Parallel to hinge line in cylindrical folds; non-existent in non-cylindrical</td>
          </tr>
          <tr>
            <td><strong>Crest Line</strong></td>
            <td>1D Topographic Line</td>
            <td>Line connecting highest topographic points of layer</td>
            <td>Coincides with hinge line only in upright, symmetrical folds</td>
          </tr>
          <tr>
            <td><strong>Trough Line</strong></td>
            <td>1D Topographic Line</td>
            <td>Line connecting lowest topographic points of layer</td>
            <td>Coincides with synclinal hinge line only in upright folds</td>
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
          <strong>Practice Q1:</strong> Under what geometric condition does the <em>Crest Line</em> of an anticline fail to coincide with its <em>Hinge Line</em>?
          <div class="pq-ans">✔ Correct Answer: Whenever the fold is inclined, overturned, or plunging (asymmetrical fold).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The hinge line is purely geometric (maximum curvature); the crest line is purely gravitational/topographic (highest elevation). In an inclined fold, the highest point occurs on one of the limbs away from the hinge line.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>cylindrical fold</em>, and how do its hinge lines relate to its fold axis?
          <div class="pq-ans">✔ Correct Answer: A fold that can be generated by translating a straight line parallel to itself; all hinge lines are straight and mutually parallel to the fold axis.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> On a stereonet, bedding poles of a cylindrical fold plot along a single great circle ($\pi$-circle) whose pole ($\beta$-axis) defines the fold axis.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is a <em>non-cylindrical fold</em>, and give two common geological examples?
          <div class="pq-ans">✔ Correct Answer: A fold whose hinge line is curved in three dimensions; examples include structural domes and structural basins (doubly-plunging folds).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In non-cylindrical folds (sheath folds, culminations, depressions), no single straight generator axis exists, and the hinge line curves continuously through space.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Ramsay's fold classification, what parameter is defined by the angle between the two tangents drawn at the inflection points on adjacent limbs?
          <div class="pq-ans">✔ Correct Answer: The Interlimb Angle ($2\alpha$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Interlimb angle classifies fold tightness: Gentle ($180^\circ - 120^\circ$), Open ($120^\circ - 70^\circ$), Close ($70^\circ - 30^\circ$), Tight ($30^\circ - 0^\circ$), and Isoclinal ($0^\circ$, parallel limbs).
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> In an active folding regime via tangential longitudinal strain (buckling), what is the state of strain at the outer arc versus the inner arc of the hinge zone?
          <div class="pq-ans">✔ Correct Answer: Outer arc experiences layer-parallel extension (tension gashes); inner arc experiences layer-parallel contraction (buckle thrusts and cleavage).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Separating the outer extensional arc from the inner contractional arc is a central <em>neutral surface</em> of zero strain within the hinge zone.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What structural feature typically forms in the hinge zone of folded competent sandstone layers due to low pressure during buckling?
          <div class="pq-ans">✔ Correct Answer: Saddle reefs (gold-bearing quartz vein dilation zones).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Bedding separation at the hinge during flexural slip creates dilation voids where hydrothermal fluids precipitate thick saddle-reef quartz veins (e.g., Bendigo goldfield, Australia).
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How is an <em>isoclinal fold</em> defined in terms of its limbs and axial plane?
          <div class="pq-ans">✔ Correct Answer: A fold with an interlimb angle of $0^\circ$, where both limbs are parallel to each other and parallel to the axial plane.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Extreme tectonic shortening compresses both limbs into complete parallelism, making hinge zones the only place where bedding can be seen cutting across cleavage.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a <em>sheath fold</em>, and in what structural tectonic environment does it form?
          <div class="pq-ans">✔ Correct Answer: A tubular, eye-shaped, or condom-shaped fold with a severely curved hinge line formed in high-strain ductile shear zones.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> High-strain simple shear rotates the fold hinge into near-perfect parallelism with the stretching lineation ($X$-direction), forming closed elliptical cross-sections.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 24, part1, part2, part3)


# ==============================================================================
# Q025: Parallel Concentric Fold Curvature With Depth
# ==============================================================================
def generate_q025():
    title = "Q025: Ramsay's Fold Classes: Parallel (Concentric) Fold Curvature With Depth | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Fold Classification"
    h1_title = "Q025: Ramsay's Fold Classes: Parallel (Concentric) Fold Curvature With Depth"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 25<br>
<strong>Authoritative References:</strong> John G. Ramsay, <em>Folding and Fracturing of Rocks</em> (McGraw-Hill, 1967, Ch. 7, pp. 359–372); Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 12: Fold Classification, pp. 248–254); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds, pp. 193–194, Fig. 7.11); Ramsay & Huber, <em>The Techniques of Modern Structural Geology</em> (Vol. 2, Academic Press)."""

    part1 = r"""
  <!-- CARD 1: RAMSAY'S FOLD CLASSIFICATION & CLASS 1B -->
  <div class="card">
    <div class="card-header bg-blue">1. Ramsay's Dip Isogon Classification & Parallel (Concentric) Folds</div>
    <div class="card-body">
      <p>In 1967, John G. Ramsay revolutionized structural geology by establishing a rigorous mathematical classification of folds based on <strong>dip isogons</strong> (lines connecting points of equal dip on adjacent surfaces of a folded layer) and the variation of <strong>orthogonal layer thickness ($t_\alpha$)</strong> relative to limb dip ($\alpha$):</p>

      <ul>
        <li><strong>Class 1:</strong> Dip isogons converge toward the fold core. Orthogonal thickness $t_\alpha$ is either greater on limbs than at the hinge (Class 1A), constant everywhere (Class 1B), or thinner on limbs (Class 1C).</li>
        <li><strong>Class 1B — The Parallel (Concentric) Fold:</strong> A fold where the orthogonal layer thickness remains <strong>strictly constant throughout the fold</strong>:
        $$t_\alpha = t_0 = \text{constant}$$
        Where $t_0$ is orthogonal thickness at the hinge. In profile, individual bedding surfaces form concentric circular arcs sharing a common center of curvature.</li>
        <li><strong>Class 2 — Similar Folds:</strong> Dip isogons are strictly parallel. Axial planar thickness $T_\alpha = T_0 = \text{constant}$; orthogonal thickness thins on limbs ($t_\alpha = t_0 \cos\alpha$). Fold shape is identical on all layers with depth.</li>
        <li><strong>Class 3:</strong> Dip isogons diverge toward the core; extreme thinning on limbs.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q25/fossen_fig12_10_ramsay_fold_classes.png" alt="Ramsay Fold Classes and Dip Isogons from Haakon Fossen">
        <div class="tb-caption">
          <strong>Figure 25.1 (Haakon Fossen, <em>Structural Geology</em>, Fig. 12.10):</strong> Ramsay's dip isogon classification. Class 1B defines Parallel (Concentric) folds where orthogonal layer thickness ($t$) is invariant across the entire profile.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE SPACE PROBLEM AT THE CORE -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Space Problem: Why Anticlines Sharpen & Synclines Broaden Downward</div>
    <div class="card-body">
      <p>Because concentric folded beds maintain constant orthogonal thickness ($t_0$) like layers of cardboard or thick plywood bent together, circular arc geometry imposes a severe geometric constraint with depth:</p>

      <ul>
        <li><strong>Radius of Curvature with Depth ($R$):</strong> For an anticline, the center of curvature lies <em>below</em> the fold. As one moves downward into the core of the anticline, the radius of curvature decreases by the layer thickness on each successive layer ($R_{n} = R_0 - n \cdot t_0$).</li>
        <li><strong>Anticlines Sharpen Downward:</strong> Because radius of curvature $R \to 0$ downward, the anticline becomes progressively tighter, narrower, and sharper at depth until the layers can no longer fit into the core (the <em>cusp singularity</em>).</li>
        <li><strong>Synclines Broaden Downward:</strong> Conversely, for a syncline, the center of curvature lies <em>above</em> the ground surface. Moving downward away from the center of curvature increases the radius ($R_{n} = R_0 + n \cdot t_0$), causing the syncline to become <strong>progressively broader and more open with depth</strong>.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Concentric Fold Curvature Relationship with Depth</div>
        $$\kappa_{\text{anticline}}(z) = \frac{1}{R_0 - z} \to \infty \quad \text{(Curvature sharpens as depth } z \to R_0\text{)}$$
        $$\kappa_{\text{syncline}}(z) = \frac{1}{R_0 + z} \to 0 \quad \text{(Curvature broadens/flattens downward)}$$
      </div>

      <div class="quote-box bangar">
        "Parallel or Concentric Folds: These are folds in which the thickness of the beds remains uniform throughout. As a consequence of uniform thickness, the anticlines become sharper (tighter) downward while the synclines become broader with depth. Ultimately, a depth is reached where the anticline cannot continue downward without fracturing or crumpling. This is known as the space problem in parallel folds."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds, pp. 193–194, Fig. 7.11)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q25/bangar_fig7_11_parallel_folds.png" alt="Parallel Folds Cross Section from Bangar">
        <div class="tb-caption">
          <strong>Figure 25.2 (K.M. Bangar, Fig. 7.11):</strong> Cross-section of Parallel (Concentric) folds illustrating the geometric consequence of constant thickness: anticlines sharpen and pinch out downward while synclines broaden downward, generating the core space problem.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Similar, Supratenuous, and Chevron Folds</div>
    <div class="card-body">
      <p>Candidates must clearly discriminate alternative fold morphologies:</p>
      <ul>
        <li><strong>(B) Similar fold:</strong> Layers have variable orthogonal thickness (thick at hinges, thin on limbs) such that curvature is identical on all layers with depth. Anticlines and synclines never sharpen or broaden downward in a similar fold.</li>
        <li><strong>(C) Supratenuous fold:</strong> Non-tectonic compaction folds formed over buried hills or reefs, where beds are thinner over the anticlinal crest and thicker in adjacent basins due to differential sedimentary compaction.</li>
        <li><strong>(D) Chevron fold:</strong> Folds characterized by straight planar limbs and sharp, angular, knife-edge hinges (accordion folds).</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 25)</div>
    <div class="q-stmt">
      Q25. A fold in which the anticlines become sharper and synclines become broader with depth is known as :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Parallel fold &nbsp;✔</div>
      <div class="raw-opt">(B) Similar fold</div>
      <div class="raw-opt">(C) Supratenuous fold</div>
      <div class="raw-opt">(D) Chevron fold</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Parallel fold</div>
      <div class="sub">
        A <strong>Parallel fold</strong> (Class 1B Concentric Fold) maintains constant orthogonal layer thickness ($t_\alpha = t_0$) throughout. As an inescapable geometric consequence of concentric arc curvature, <strong>anticlines become sharper and synclines become broader with depth</strong> (Bangar, p. 193; Ramsay, 1967).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Parallel fold</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> In a parallel (concentric) fold, every bed maintains identical orthogonal thickness everywhere. Because concentric circular arcs have a common center of curvature, the radius of curvature of anticlinal beds decreases downward toward the center of curvature, forcing anticlines to become progressively tighter and sharper at depth. Conversely, synclines move away from their center of curvature and broaden downward.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Similar fold</span>
      <span class="tag wrong">Incorrect (Curvature Invariant with Depth)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> In a similar fold (Ramsay Class 2), beds thin on the limbs ($t_\alpha = t_0 \cos\alpha$) and thicken at the hinge, maintaining an identical cross-sectional shape and identical curvature on every layer with depth. Anticlines and synclines in similar folds never change curvature with depth.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Supratenuous fold</span>
      <span class="tag wrong">Incorrect (Sedimentary Differential Compaction Fold)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A supratenuous fold is formed by syn-depositional differential compaction over an unyielding buried topographic ridge (such as a granite tor or fossil reef). Beds thin over the anticlinal crest and thicken into flanking troughs; it does not display concentric curvature deepening.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Chevron fold</span>
      <span class="tag wrong">Incorrect (Straight-Limbed Angular Folds)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Chevron folds (accordion folds) possess straight, planar limbs meeting at narrow, acute, angular hinges. While they may belong to Class 1B, their defining criterion is angularity, not the systematic downward broadening of synclines.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison: Ramsay's Fundamental Fold Classes</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Fold Class (Ramsay, 1967)</th>
            <th>Common Name</th>
            <th>Orthogonal Thickness ($t_\alpha$)</th>
            <th>Dip Isogons Pattern</th>
            <th>Curvature Variation with Depth</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Class 1A</strong></td>
            <td>Thick-Limbed Fold</td>
            <td>$t_\alpha > t_0$ (thicker on limbs)</td>
            <td>Strongly Convergent</td>
            <td>Anticlines broaden downward</td>
          </tr>
          <tr>
            <td><strong>Class 1B</strong></td>
            <td><strong>Parallel / Concentric Fold</strong></td>
            <td><strong>$t_\alpha = t_0 = \text{constant}$</strong></td>
            <td><strong>Moderately Convergent (perpendicular to bedding)</strong></td>
            <td><strong>Anticlines sharpen downward; Synclines broaden downward</strong></td>
          </tr>
          <tr>
            <td><strong>Class 1C</strong></td>
            <td>Modified Concentric Fold</td>
            <td>$t_0 \cos\alpha < t_\alpha < t_0$</td>
            <td>Weakly Convergent</td>
            <td>Weak sharpening downward; common buckling mode</td>
          </tr>
          <tr>
            <td><strong>Class 2</strong></td>
            <td><strong>Similar Fold</strong></td>
            <td><strong>$t_\alpha = t_0 \cos\alpha$ (thick hinge, thin limbs)</strong></td>
            <td><strong>Strictly Parallel</strong></td>
            <td><strong>Invariant with depth</strong> (identical profile on all layers)</td>
          </tr>
          <tr>
            <td><strong>Class 3</strong></td>
            <td>Thinned-Limb Fold</td>
            <td>$t_\alpha < t_0 \cos\alpha$ (extreme limb thinning)</td>
            <td>Divergent toward core</td>
            <td>Synclines sharpen downward; Anticlines broaden downward</td>
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
          <strong>Practice Q1:</strong> How do rocks in the core of a parallel anticline resolve the "space problem" when the radius of curvature approaches zero ($R \to 0$)?
          <div class="pq-ans">✔ Correct Answer: Through ductile flow of incompetent layers, disharmonic folding, decollement detachment, or core thrust faulting (out-of-the-syncline thrusts).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because rigid beds cannot occupy zero volume, the concentric fold cannot continue downward indefinitely; a basal detachment (decollement) separates the folded competent layers from undeformed basement below.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What primary deformation mechanism produces Class 1B parallel folds in competent sedimentary sequences?
          <div class="pq-ans">✔ Correct Answer: Flexural Slip (slip along bedding planes like bending a deck of cards).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In flexural slip folding, individual layers slide past one another along pre-existing weak bedding planes without altering internal orthogonal thickness ($t_\alpha = \text{const}$).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> Where does the amount of flexural slip between adjacent beds reach a maximum in a parallel fold?
          <div class="pq-ans">✔ Correct Answer: At the inflection points on the limbs (where layer dip is steepest). Slip is zero at the hinge line.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Relative displacement between beds ($S = t \cdot \alpha$) is proportional to limb dip ($\alpha$). At the hinge ($\alpha = 0$), shear slip is zero.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In a Similar Fold (Class 2), what remains constant across the entire profile of a folded layer?
          <div class="pq-ans">✔ Correct Answer: Thickness measured parallel to the axial plane ($T_\alpha = \text{constant}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Similar folds form by heterogeneous simple shear or passive flow parallel to the axial plane, resulting in uniform axial planar thickness everywhere.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What metamorphic and structural environment favors the development of Similar Folds (Class 2) over Parallel Folds (Class 1B)?
          <div class="pq-ans">✔ Correct Answer: High-grade regional metamorphism and ductile shearing in the middle to lower crust (incompetent rocks under high temperature).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> High temperature lowers rock viscosity, promoting passive ductile flow and axial planar cleavage rather than bedding-plane slip.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a <em>disharmonic fold</em>, and why is it intimately associated with parallel folds?
          <div class="pq-ans">✔ Correct Answer: A fold where soft, incompetent layers (shale, halite) deform into complex, irregular wrinkles between uniformly curved competent layers.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Incompetent beds squeeze out of high-pressure anticlinal hinges and flow into low-pressure voids to resolve the space problem.
          </div>
        </li>

        <li>
          <strong>Practice Q7 (Numerical):</strong> A competent limestone bed of thickness $t_0 = 10\text{ m}$ is folded into a concentric anticline whose outer surface has a radius of curvature $R_{\text{outer}} = 50\text{ m}$. After how many successive $10\text{ m}$ beds will the anticlinal core encounter the geometric cusp singularity ($R = 0$)?
          <div class="pq-ans">✔ Worked Answer: Exactly 5 beds ($50\text{ m} / 10\text{ m} = 5$).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$R_n = R_{\text{outer}} - n \cdot t_0 = 50 - n(10) = 0 \implies n = 5$$
            Below the 5th layer, concentric folding is mathematically impossible without core disruption.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a <em>ptygmatic fold</em>, and what Ramsay class does it belong to?
          <div class="pq-ans">✔ Correct Answer: A tortuously contorted, pucker-folded granitic or quartzose vein enclosed in a ductile metamorphic schist/gneiss; Class 1B to Class 1C.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Buckling of a high-viscosity competent vein embedded in a low-viscosity incompetent host matrix produces ptygmatic meanders.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 25, part1, part2, part3)


if __name__ == "__main__":
    for q_fn, q_name in [
        (generate_q021, "Q021_Thrust_Fault_Reverse_Dip_Angle_Threshold_Complete_Guide.html"),
        (generate_q022, "Q022_Plunge_Linear_Feature_Inclination_Complete_Guide.html"),
        (generate_q023, "Q023_Hookes_Law_Elastic_Stress_Strain_Proportionality_Complete_Guide.html"),
        (generate_q024, "Q024_Fold_Hinge_Line_Maximum_Curvature_Complete_Guide.html"),
        (generate_q025, "Q025_Parallel_Concentric_Fold_Curvature_With_Depth_Complete_Guide.html"),
    ]:
        out_path = os.path.join(SOLUTIONS_DIR, q_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(q_fn())
        print(f"Generated {q_name}: {out_path} ({os.path.getsize(out_path)} bytes)")
