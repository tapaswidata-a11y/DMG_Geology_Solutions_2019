#!/usr/bin/env python3
"""
Masterclass Builder for Batch 3: Structural Geology (Q026 - Q030)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q026: Graben and Horst
# ==============================================================================
def generate_q026():
    title = "Q026: Extensional Tectonics: Graben, Horst & Continental Rift Valleys | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Extensional Tectonics"
    h1_title = "Q026: Extensional Tectonics: Graben, Horst & Continental Rift Valleys"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 26<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 17: Extensional Regimes, pp. 360–378); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Faults, pp. 203–204, Fig. 7.30 & 7.31); Davis, Reynolds & Kluth (3rd Ed., pp. 315–330)."""

    part1 = r"""
  <!-- CARD 1: EXTENSIONAL FAULT BLOCK SYSTEMATICS -->
  <div class="card">
    <div class="card-header bg-blue">1. Extensional Tectonic Mechanics & Graben-Horst Geometry</div>
    <div class="card-body">
      <p>In continental rift systems and regions undergoing horizontal crustal extension ($\Delta L > 0$), the maximum principal stress is vertical ($\sigma_1 = \text{overburden weight}$), while minimum principal stress is horizontal ($\sigma_3 = \text{extensional axis}$). Under this stress regime, conjugate normal faults dipping at $\approx 60^\circ$ toward each other partition the brittle upper crust into alternating elevated and depressed fault blocks:</p>

      <ul>
        <li><strong>Graben (German for "trench" or "ditch"):</strong> A downthrown, depressed structural block bounded on both sides by conjugate normal faults dipping toward each other. A graben forms an elongated, fault-bounded structural depression or <strong>rift valley</strong>.</li>
        <li><strong>Horst (German for "eyrie" or "nest"):</strong> An upthrown, elevated crustal block bounded on both sides by conjugate normal faults dipping away from each other. Horsts form linear mountain ranges or plateaus flanking rift basins.</li>
        <li><strong>Half-Graben:</strong> An asymmetrical extensional basin bounded by a major master normal fault (border fault) on one side and a gentle roll-over flexure on the other, characteristic of modern continental rifts.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q26/fossen_fig9_5_horst_graben.png" alt="Horst and Graben System from Haakon Fossen">
        <div class="tb-caption">
          <strong>Figure 26.1 (Haakon Fossen, <em>Structural Geology</em>, Fig. 9.5):</strong> Extensional tectonic block diagram showing a central downthrown Graben bounded by conjugate normal faults, flanked by elevated Horsts.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: TEXTBOOK EXCERPTS & GEOLOGICAL EXAMPLES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Global & Indian Archetypes: Rhine Graben, East African Rift & Narmada</div>
    <div class="card-body">
      <p>Grabens and rift valleys host some of Earth's most spectacular geological and physiographic features:</p>

      <ul>
        <li><strong>The Rhine Graben (Western Europe):</strong> The classic European type-locality, where a $300\text{ km}$ long, $35\text{ km}$ wide graben floor (the Rhine Valley) dropped down between the elevated Vosges Mountains horst in France and the Black Forest (Schwarzwald) horst in Germany.</li>
        <li><strong>The East African Rift System (EARS):</strong> A grand active continental divergent boundary where Africa is splitting into the Nubian and Somalian plates, forming giant grabens occupied by deep rift lakes (Lake Tanganyika, Lake Malawi).</li>
        <li><strong>The Narmada-Son Graben (Central India):</strong> A major fault-bounded rift basin where the Narmada River flows westward within a depressed crustal graben bounded by the elevated Vindhyan Range horst to the north and the Satpura Range horst to the south.</li>
      </ul>

      <div class="quote-box bangar">
        "Graben and Horst: A Graben or Rift Valley is formed when a central block is displaced downward between two parallel normal faults that dip towards each other... A Horst or Block Mountain is formed when the central block remains elevated while the bordering blocks are downthrown, or when the central block is pushed upward between faults that dip away from each other."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds and Faults, p. 204, Fig. 7.30)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q26/bangar_fig7_30_31_graben_horst.png" alt="Graben and Horst from Bangar">
        <div class="tb-caption">
          <strong>Figure 26.2 (K.M. Bangar, Fig. 7.30 & 7.31):</strong> Classical cross-sectional diagrams of a Graben (rift valley) and Horst (block mountain) with relative fault displacements.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Horst, Strike Valley, and Dip Valley</div>
    <div class="card-body">
      <p>Understanding geomorphic vs. structural terms eliminates distractors:</p>
      <ul>
        <li><strong>Horst (Option A):</strong> An elevated, upthrown crustal block (block mountain), the polar opposite of a depressed valley.</li>
        <li><strong>Strike Valley (Option B):</strong> An erosional valley carved by a river flowing parallel to the strike of soft sedimentary formations (subsequent stream), not a fault-bounded structural downthrow.</li>
        <li><strong>Dip Valley (Option D):</strong> An erosional valley carved down the dip slope of inclined strata by a consequent or resequent stream.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 26)</div>
    <div class="q-stmt">
      Q26. A valley formed by the downward displacement of a fault bounded block is known as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Horst</div>
      <div class="raw-opt">(B) Strike valley</div>
      <div class="raw-opt correct">(C) Graben &nbsp;✔</div>
      <div class="raw-opt">(D) Dip valley</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Graben</div>
      <div class="sub">
        An elongate, fault-bounded structural valley or trench formed by the <strong>downward displacement of a crustal block</strong> between conjugate normal faults is formally designated as a <strong>Graben</strong> (or <strong>Rift Valley</strong>).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Horst</span>
      <span class="tag wrong">Incorrect (Upthrown Elevated Block Mountain)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A horst is an upthrown, elevated crustal block standing prominent between down-dropped blocks. It forms a block mountain or plateau (such as the Vosges, Black Forest, or Satpura range), the exact morphological opposite of a downthrown valley.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Strike valley</span>
      <span class="tag wrong">Incorrect (Fluvial Erosional Feature Along Strike)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A strike valley is an erosional landscape feature excavated by a subsequent stream eroding soft rock beds parallel to regional strike. It is produced by fluvial differential erosion, not tectonic block faulting.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Graben</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Derived from the German word for trench, a <strong>graben</strong> is the standard geological term for an elongate crustal valley produced by the downward displacement of a rock block bounded by parallel normal faults dipping toward each other. When developed on a continental scale, it forms a rift valley.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Dip valley</span>
      <span class="tag wrong">Incorrect (Erosional Valley Down Structural Dip)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A dip valley is carved by a river flowing in the direction of stratal dip across a homoclinal ridge or cuesta. It is an erosional fluvial feature, not a fault-bounded downthrown block.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Structural vs. Erosional Valley Taxonomy</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Valley / Block Term</th>
            <th>Primary Origin</th>
            <th>Structural Architecture</th>
            <th>Famous Global & Indian Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Graben / Rift Valley</strong></td>
            <td><strong>Tectonic Downthrow (Extension)</strong></td>
            <td><strong>Crustal block downthrown between conjugate normal faults</strong></td>
            <td><strong>Rhine Graben; East African Rift; Narmada Valley</strong></td>
          </tr>
          <tr>
            <td><strong>Horst / Block Mountain</strong></td>
            <td>Tectonic Upthrow (Extension)</td>
            <td>Crustal block standing elevated between downthrown blocks</td>
            <td>Vosges Mountains (France); Black Forest (Germany); Satpuras</td>
          </tr>
          <tr>
            <td><strong>Strike Valley</strong></td>
            <td>Fluvial Differential Erosion</td>
            <td>River excavating weak shale parallel to rock strike</td>
            <td>Appalachian shale vales; Cuddapah Basin strike valleys</td>
          </tr>
          <tr>
            <td><strong>Dip Valley</strong></td>
            <td>Fluvial Incision</td>
            <td>River flowing down the dip slope of a cuesta/hogback</td>
            <td>Consequent valleys in homoclinal terrains</td>
          </tr>
          <tr>
            <td><strong>Fault-Line Scarp Valley</strong></td>
            <td>Erosion along Fault Trace</td>
            <td>Differential erosion along crushed fault breccia zone</td>
            <td>San Andreas fault-line valleys (California)</td>
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
          <strong>Practice Q1:</strong> What is a <em>half-graben</em>, and what structural feature separates it from a full graben?
          <div class="pq-ans">✔ Correct Answer: An asymmetrical rift basin bounded by a major planar or listric normal fault on only ONE side, with a flexural rollover on the other.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Most continental rifts are composed of chains of linked half-grabens with alternating polarity, rather than perfectly symmetrical grabens bounded by two opposing faults.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>listric normal fault</em>, and what happens to the hanging wall block as it slips downward?
          <div class="pq-ans">✔ Correct Answer: A normal fault with a curved, concave-upward fault plane that flattens with depth; hanging wall block rotates backward creating a rollover anticline.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Slip along a curved fault surface creates extension and rollover, forming crestal collapse grabens that trap petroleum in extensional basins.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> In the Basin and Range Province of western North America, what landforms represent the horsts and grabens?
          <div class="pq-ans">✔ Correct Answer: The linear mountain ranges are horsts; the intervening flat desert basins (playas) are grabens and half-grabens.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Crustal extension across Nevada and Utah over the past 20 million years has doubled the width of the crust, creating alternating horst ranges and graben basins.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Indian tectonics, the Narmada and Tapti river valleys flow westward across peninsular India through which structural feature?
          <div class="pq-ans">✔ Correct Answer: The Narmada-Son-Damodar Graben System (SONATA Zone).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> While most peninsular rivers flow eastward to the Bay of Bengal, the Narmada and Tapti are structurally confined within ancient, reactivated Proterozoic-Cretaceous grabens.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is an <em>accommodation zone</em> in a continental rift system?
          <div class="pq-ans">✔ Correct Answer: A complex structural transfer zone connecting two half-grabens that have opposing fault dip polarities.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Accommodation zones transfer extensional strain between overlapping normal fault segments via oblique faults and strike-slip tear faults.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What sedimentary rock deposit is characteristically deposited along the border fault of an active graben?
          <div class="pq-ans">✔ Correct Answer: Coarse alluvial fan fanglomerates and talus breccias.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Rapid uplift of the horst footwall generates steep fault scarps that shed coarse, poorly sorted fanglomerates directly into the graben basin.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is a <em>pull-apart basin</em>, and how does it relate to strike-slip faulting?
          <div class="pq-ans">✔ Correct Answer: A rhomboidal graben-like extensional basin formed at a releasing bend or en echelon stepover along a strike-slip fault.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Left-stepping dextral faults or right-stepping sinistral faults pull crust apart, creating deep rhombic basins (e.g., the Dead Sea basin).
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why do continental rifts and grabens exhibit positive Bouguer gravity anomalies despite being filled with low-density sediments?
          <div class="pq-ans">✔ Correct Answer: Due to crustal thinning and passive upwelling of high-density asthenospheric mantle beneath the rift axis.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Lithospheric necking pulls the dense mantle closer to the surface, generating an overriding positive regional Bouguer gravity signature.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 26, part1, part2, part3)


# ==============================================================================
# Q027: Plunge of Linear Feature (Second Occurrence in Syllabus)
# ==============================================================================
def generate_q027():
    title = "Q027: Kinematics of Linear Structural Features: Plunge, Trend & Finite Strain | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Kinematic Analysis"
    h1_title = "Q027: Kinematics of Linear Structural Features: Plunge, Trend & Finite Strain"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 27<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 2 & 13: Lineations, pp. 270–288); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7, pp. 191–194); Ramsay & Lisle, <em>Techniques of Modern Structural Geology</em> (Vol. 3)."""

    part1 = r"""
  <!-- CARD 1: LINEAR ATTITUDES & MAXIMUM ELONGATION -->
  <div class="card">
    <div class="card-header bg-blue">1. Geometric Foundations: Plunge as the Vertical Inclination of Lineations</div>
    <div class="card-body">
      <p>In structural geology and finite strain analysis, linear geological features—including the <strong>axis of a fold</strong>, mineral lineations, stretched pebble axes, and the <strong>line of maximum elongation ($X$-axis of the strain ellipsoid)</strong>—require exact spatial orientation in three dimensions. The primary quantitative measure of a line's inclination is its <strong>Plunge</strong>:</p>

      <ul>
        <li><strong>Plunge ($\beta$):</strong> The <strong>vertical angle</strong> between the horizontal plane and the inclined linear feature, measured strictly downward in a vertical plane ($0^\circ \le \beta \le 90^\circ$).</li>
        <li><strong>Line of Maximum Elongation:</strong> During finite strain, deformed spherical markers (oolites, pebbles, reduction spots) are transformed into triaxial ellipsoids with principal axes $X \ge Y \ge Z$. The long axis ($X$) represents the line of maximum elongation, and its vertical angle of inclination to the horizontal plane is its plunge.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q27/plunge_and_rake_pitch_kinematics.png" alt="Plunge and Rake Pitch Kinematics Diagram">
        <div class="tb-caption">
          <strong>Figure 27.1: Spatial Kinematics of Plunge vs. Rake.</strong> Illustrating the measurement of Plunge ($\beta$) strictly within a vertical plane, contrasting with Rake ($\phi$) measured within an inclined planar surface.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: PITCH (RAKE) ON INCLINED PLANES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Geometric Interrelationships: Plunge, Trend, and Rake</div>
    <div class="card-body">
      <p>When a lineation lies upon an inclined geological plane (e.g., mineral alignment on foliation, or slickenside striae on a fault surface), structural geologists relate its true vertical plunge to its rake within the plane:</p>

      <div class="formula-card">
        <div class="formula-title">Spherical Trigonometry of Lineations on Planes</div>
        $$\sin(\text{Plunge}) = \sin(\text{Dip of Plane}) \cdot \sin(\text{Rake})$$
        $$\cos(\text{Rake}) = \cos(\text{Plunge}) \cdot \cos(\alpha - \text{Strike})$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $\alpha$ is the trend of the lineation. If the plane is vertical ($\text{Dip} = 90^\circ$), Plunge equals Rake. If the plane is horizontal ($\text{Dip} = 0^\circ$), Plunge is identically zero.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q27/fossen_rake_pitch_diagram.png" alt="Fossen Rake and Pitch Geometric Diagram">
        <div class="tb-caption">
          <strong>Figure 27.2 (Haakon Fossen, <em>Structural Geology</em>):</strong> Detailed geometric block diagram distinguishing Plunge (angle in vertical plane $V$) from Rake/Pitch (angle on the dipping plane $S$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Strike, Dip, and Rake</div>
    <div class="card-body">
      <p>Re-affirming fundamental structural taxonomy:</p>
      <ul>
        <li><strong>Strike:</strong> Azimuth of a horizontal line within an inclined plane; has zero vertical angle.</li>
        <li><strong>Dip:</strong> Vertical angle of an inclined <em>plane</em>, not an individual linear axis.</li>
        <li><strong>Rake:</strong> Angle measured <em>in an inclined plane</em>, not relative to the horizontal plane.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 27)</div>
    <div class="q-stmt">
      Q27. The vertical angle between the horizontal plane and the axis or line of maximum elongation of a... (linear feature) is known as :
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
        The vertical angle measured in a vertical plane between the horizontal plane and any linear structural feature (such as a fold axis, line of maximum elongation, or lineation) is universally defined as the <strong>plunge</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) strike</span>
      <span class="tag wrong">Incorrect (Horizontal Azimuth of a Planar Feature)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Strike is the horizontal compass direction of a planar surface (bedding, fault, or joint). It is not a vertical angle and does not apply to lines.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) dip</span>
      <span class="tag wrong">Incorrect (Vertical Inclination of a Plane)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Dip is the maximum vertical angle of an inclined <em>geological plane</em>. While both dip and plunge are vertical angles, dip is strictly planar, whereas plunge is the universal term for linear features.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) rake</span>
      <span class="tag wrong">Incorrect (Angle Measured Inside an Inclined Plane)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Rake is measured within the dipping surface itself relative to its strike line, not in the true vertical plane.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) plunge</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard international definition in structural geology (Bangar, p. 192; Fossen, p. 25), the acute vertical angle between an inclined linear feature and the horizontal reference plane is its <strong>plunge</strong>.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Structural Attitude Measurements</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Measurement Term</th>
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
            <td>Bearing of vertical plane containing line</td>
          </tr>
          <tr>
            <td><strong>Rake / Pitch</strong></td>
            <td>Line on a Plane</td>
            <td>Inclined Plane</td>
            <td>$0^\circ \text{ to } 90^\circ$</td>
            <td>Angle from strike line on rock face</td>
          </tr>
          <tr>
            <td><strong>Dip</strong></td>
            <td>Planar Feature</td>
            <td>Vertical Plane $\perp$ Strike</td>
            <td>$0^\circ \text{ to } 90^\circ$</td>
            <td>Strike/Dip (e.g., $045/30^\circ\text{SE}$)</td>
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
          <strong>Practice Q1:</strong> If a fault plane dips at $45^\circ$ and slickenlines display a rake of $90^\circ$ (pointing directly down-dip), what is the plunge of the slickenlines?
          <div class="pq-ans">✔ Worked Answer: Plunge is exactly $45^\circ$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\sin(\text{Plunge}) = \sin(45^\circ) \cdot \sin(90^\circ) = \sin(45^\circ) \times 1 = \sin(45^\circ) \implies \text{Plunge} = 45^\circ$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What geological instrument is used in the field to measure both the plunge and trend of a lineation?
          <div class="pq-ans">✔ Correct Answer: A geological compass-clinometer (Brunton compass or Freiberg compass).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Aligning the compass edge along the line and leveling the clinometer bubble measures plunge; setting the compass horizontal along the vertical sighting line measures trend.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is a <em>mullion structure</em>, and what is its orientation relative to regional fold plunge?
          <div class="pq-ans">✔ Correct Answer: Linear fluted columns formed along competent/incompetent rock interfaces; parallel to fold hinges and regional plunge.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Mullions develop by cuspate buckling along interfaces with high viscosity contrast (e.g., sandstone-shale), running parallel to the fold axis.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In a shear zone, if mineral lineations plunge at $0^\circ$ (horizontal) on a vertical fault plane, what is the kinematic sense of the fault?
          <div class="pq-ans">✔ Correct Answer: Pure strike-slip faulting.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Horizontal slip lines on a vertical plane indicate lateral displacement with zero dip-slip component.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How do pencil structures (pencil cleavage) form, and what does their plunge indicate?
          <div class="pq-ans">✔ Correct Answer: Formed by the intersection of flat bedding ($S_0$) with weakly developed tectonic cleavage ($S_1$) in shales; plunge indicates the fold axis plunge.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Weathering causes the rock to splinter into elongated pencil-like polygonal rods parallel to the intersection lineation.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the difference between a <em>stretching lineation</em> and an <em>intersection lineation</em>?
          <div class="pq-ans">✔ Correct Answer: Stretching lineations are physical markers of maximum finite strain ($X$ direction); intersection lineations are geometric intersections of two planar fabrics.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Stretching lineations record ductile flow; intersection lineations are non-kinematic intersection traces.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> On an equal-area stereonet, what geometric feature represents the locus of all possible linear features that can lie within a single plane?
          <div class="pq-ans">✔ Correct Answer: The great circle arc representing that plane.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Any line lying on a plane must plot as a point along the plane's great circle trace.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> If an anticline plunges at $80^\circ$, what term is used to describe such an extreme orientation?
          <div class="pq-ans">✔ Correct Answer: A steeply plunging fold (or vertically plunging fold if plunge $> 80^\circ$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Plunge classification: Horizontal ($0^\circ - 10^\circ$), Gently plunging ($10^\circ - 30^\circ$), Moderately plunging ($30^\circ - 60^\circ$), Steeply plunging ($60^\circ - 80^\circ$), and Vertical ($80^\circ - 90^\circ$).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 27, part1, part2, part3)


# ==============================================================================
# Q028: Dip-Slip Fault
# ==============================================================================
def generate_q028():
    title = "Q028: Kinematic Fault Classification: Dip-Slip, Strike-Slip & Oblique-Slip | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Fault Kinematics"
    h1_title = "Q028: Kinematic Fault Classification: Dip-Slip, Strike-Slip & Oblique-Slip"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 28<br>
<strong>Authoritative References:</strong> Haakon Fossen, <em>Structural Geology</em> (2nd Ed., Cambridge Univ. Press, Ch. 8 & 9, pp. 165–185); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Faults, pp. 200–205, Fig. 7.24); Marland P. Billings, <em>Structural Geology</em> (3rd Ed., Prentice Hall)."""

    part1 = r"""
  <!-- CARD 1: KINEMATIC FAULT CLASSIFICATION BY NET SLIP -->
  <div class="card">
    <div class="card-header bg-blue">1. Kinematic Classification of Faults by Net Slip Direction</div>
    <div class="card-body">
      <p>In structural geology (Billings, 1972; Fossen, 2016; Bangar, p. 201), faults are classified kinematically according to the orientation of the <strong>net-slip vector</strong> (the actual vector displacement connecting two formerly contiguous points on opposite sides of the fault plane):</p>

      <ul>
        <li><strong>Dip-Slip Fault:</strong> A fault in which the relative movement of the blocks is <strong>parallel to the dip direction of the fault plane</strong> (the net slip vector lies parallel to the true dip line, meaning rake of slickenlines is $\approx 90^\circ$). Dip-slip faults are subdivided based on the sense of displacement:
          <ul>
            <li><strong>Normal Fault:</strong> Hanging wall moves downward relative to footwall (extensional regime).</li>
            <li><strong>Reverse / Thrust Fault:</strong> Hanging wall moves upward relative to footwall (contractional regime).</li>
          </ul>
        </li>
        <li><strong>Strike-Slip Fault (Wrench / Transcurrent Fault):</strong> A fault in which movement is strictly parallel to the strike line of the fault plane (horizontal displacement, rake $\approx 0^\circ$). Subdivided into <em>Dextral</em> (right-lateral) and <em>Sinistral</em> (left-lateral).</li>
        <li><strong>Oblique-Slip Fault:</strong> A fault combining significant components of both strike-slip and dip-slip motion ($0^\circ < \text{rake} < 90^\circ$, typically $15^\circ < \text{rake} < 75^\circ$).</li>
        <li><strong>Hinge Fault (Pivotal / Rotational Fault):</strong> A fault where displacement increases progressively away from a stationary pivot point.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q28/dip_slip_normal_reverse_mechanics.png" alt="Dip-Slip Fault Mechanics Normal and Reverse">
        <div class="tb-caption">
          <strong>Figure 28.1: Kinematic Architecture of Dip-Slip Faults.</strong> Illustrating pure dip-parallel slip ($90^\circ$ rake) in (A) Normal fault (hanging wall moves down) and (B) Reverse fault (hanging wall moves up).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: DIP-SLIP DISPLACEMENT COMPONENTS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Geometric Anatomy: Throw, Heave, and Net Slip</div>
    <div class="card-body">
      <p>On a dip-slip fault dipping at angle $\theta$, the net dip slip ($S$) is geometrically resolved into two orthogonal components:</p>

      <div class="formula-card">
        <div class="formula-title">Mathematical Resolution of Dip Slip</div>
        $$\text{Vertical Throw } (h) = S \cdot \sin\theta$$
        $$\text{Horizontal Heave } (l) = S \cdot \cos\theta$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $S$ is dip slip, $h$ is throw (vertical stratigraphic displacement), and $l$ is heave (horizontal separation). For normal faults, heave represents crustal extension; for reverse faults, heave represents crustal shortening.</p>
      </div>

      <div class="quote-box bangar">
        "Classification of Faults Based on Direction of Slip: 1. Dip-slip fault: In this type, the relative movement of the blocks is essentially parallel to the dip of the fault plane. It includes normal faults and reverse faults. 2. Strike-slip fault: Movement is parallel to the strike. 3. Oblique-slip fault: Movement is oblique to both dip and strike."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Folds and Faults, p. 201, Fig. 7.24)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q28/bangar_fig7_24_normal_reverse_faults.png" alt="Normal and Reverse Dip-Slip Faults from Bangar">
        <div class="tb-caption">
          <strong>Figure 28.2 (K.M. Bangar, Fig. 7.24):</strong> Dip-slip fault mechanics, illustrating displacement strictly parallel to the fault plane's dip inclination.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Strike-Slip, Oblique-Slip, and Hinge Faults</div>
    <div class="card-body">
      <p>Candidates must clearly differentiate alternative slip geometries:</p>
      <ul>
        <li><strong>(A) Strike-slip fault:</strong> Movement is parallel to the <em>strike</em> (horizontal line), not the dip.</li>
        <li><strong>(C) Oblique-slip fault:</strong> Movement is at an oblique angle, possessing both strike and dip components simultaneously.</li>
        <li><strong>(D) Hinge fault:</strong> Movement involves rotation around an axis perpendicular to the fault plane, where slip is not uniform or purely parallel to dip.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 28)</div>
    <div class="q-stmt">
      Q28. A fault in which the movement is parallel to the dip of the fault is called :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Strike-slip fault</div>
      <div class="raw-opt correct">(B) Dip-slip fault &nbsp;✔</div>
      <div class="raw-opt">(C) Oblique-slip fault</div>
      <div class="raw-opt">(D) Hinge fault</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Dip-slip fault</div>
      <div class="sub">
        A fault in which the relative movement of the displaced blocks is strictly <strong>parallel to the dip of the fault plane</strong> is universally defined as a <strong>Dip-slip fault</strong> (Bangar, p. 201; Fossen, p. 166).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Strike-slip fault</span>
      <span class="tag wrong">Incorrect (Displacement Parallel to Strike)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> In a strike-slip fault (transcurrent/wrench fault), the displacement vector is horizontal and parallel to the strike line of the fault plane (e.g., San Andreas Fault). It has zero dip-slip component.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Dip-slip fault</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard international definition, a <strong>dip-slip fault</strong> is one in which the net slip is oriented parallel to the fault dip. It encompasses normal faults (hanging wall down) and reverse/thrust faults (hanging wall up).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Oblique-slip fault</span>
      <span class="tag wrong">Incorrect (Combines Strike and Dip Slip Simultaneously)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> In an oblique-slip fault, the net displacement vector is neither parallel to strike nor parallel to dip, but cuts diagonally across the fault plane ($0^\circ < \text{rake} < 90^\circ$).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Hinge fault</span>
      <span class="tag wrong">Incorrect (Rotational Displacement around a Pivot)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A hinge (pivotal) fault involves rotational displacement around an axis perpendicular to the fault, such that displacement varies from zero at the pivot to a maximum at the opposite end.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Kinematic Fault Classification Matrix</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Kinematic Fault Type</th>
            <th>Net Slip Orientation Relative to Fault Geometry</th>
            <th>Rake / Pitch of Slickenlines</th>
            <th>Primary Subtypes / Manifestations</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dip-Slip Fault</strong></td>
            <td><strong>Strictly parallel to true dip direction</strong></td>
            <td><strong>$80^\circ - 90^\circ$ (Near-perpendicular to strike)</strong></td>
            <td><strong>Normal faults</strong> (extensional) and <strong>Reverse / Thrust faults</strong> (contractional)</td>
          </tr>
          <tr>
            <td><strong>Strike-Slip Fault</strong></td>
            <td>Strictly parallel to fault strike line (horizontal)</td>
            <td>$0^\circ - 10^\circ$ (Near-parallel to strike)</td>
            <td>Dextral (Right-lateral) and Sinistral (Left-lateral) wrench faults</td>
          </tr>
          <tr>
            <td><strong>Oblique-Slip Fault</strong></td>
            <td>Oblique / diagonal across fault plane</td>
            <td>$15^\circ - 75^\circ$ (Diagonal)</td>
            <td>Transtensional (normal + strike-slip) and Transpressional (reverse + strike-slip)</td>
          </tr>
          <tr>
            <td><strong>Hinge (Pivotal) Fault</strong></td>
            <td>Rotational shear around a fixed pivot point</td>
            <td>Variable along strike</td>
            <td>Scissors faults, trapdoor caldera collapse faults</td>
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
          <strong>Practice Q1 (Numerical):</strong> A normal dip-slip fault dips at an angle $\theta = 60^\circ$. Geological mapping shows a total net dip-slip $S = 200\text{ m}$. Calculate the vertical throw ($h$) and horizontal heave ($l$) of the fault.
          <div class="pq-ans">✔ Worked Answer: Throw $h = 173.2\text{ m}$; Heave $l = 100.0\text{ m}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\text{Throw } h = S \cdot \sin(60^\circ) = 200 \times 0.8660 = 173.2\text{ m}$$<br>
            $$\text{Heave } l = S \cdot \cos(60^\circ) = 200 \times 0.5000 = 100.0\text{ m}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> On a vertical fault plane ($\text{dip} = 90^\circ$), if the hanging wall moves purely vertically downward, is the fault classified as a dip-slip fault?
          <div class="pq-ans">✔ Correct Answer: Yes; movement is strictly parallel to the vertical dip line.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the slip vector is aligned with the vertical dip vector, it is kinematically a dip-slip fault with $90^\circ$ throw and zero heave.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What field diagnostic feature on a fault surface directly proves that slip was purely dip-slip rather than strike-slip?
          <div class="pq-ans">✔ Correct Answer: Slickenlines (striations) and mineral step fibres that plunge down the steepest line of dip with a rake of $90^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Slickenlines record the instantaneous velocity vector of fault movement; a rake of $90^\circ$ demonstrates pure dip-slip kinematics.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In oil exploration, what is the geometric difference between <em>stratigraphic throw</em> and <em>vertical throw</em> across a dip-slip fault?
          <div class="pq-ans">✔ Correct Answer: Vertical throw is measured vertically; stratigraphic throw is measured perpendicular to bedding planes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Stratigraphic throw ($\text{ST} = \text{Throw} \cdot \cos\delta \pm \text{Heave} \cdot \sin\delta$) directly determines the thickness of missing or repeated strata in a well.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How does an oblique-slip fault differ from a pure dip-slip fault in terms of net slip formulation?
          <div class="pq-ans">✔ Correct Answer: Net slip requires vector summation of both dip-slip ($S_d$) and strike-slip ($S_s$) components: $S_{\text{net}} = \sqrt{S_d^2 + S_s^2}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> For pure dip-slip faults, $S_s = 0$, so $S_{\text{net}} = S_d$.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What term describes a strike-slip fault that terminates into a series of imbricate contractional thrust faults at its end?
          <div class="pq-ans">✔ Correct Answer: A horse-tailing termination or transpressional flower structure (positive flower structure).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Lateral strike-slip motion decelerates by transferring displacement into contractional thrust splays.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is a <em>growth fault</em>, and what kinematic class does it belong to?
          <div class="pq-ans">✔ Correct Answer: A syn-sedimentary normal dip-slip fault where sediment thickness increases abruptly across the fault into the downthrown hanging wall.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Growth faults slip continuously during deltaic sedimentation (e.g., Gulf of Mexico and Niger Delta), trapping thick hydrocarbon reservoirs.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does drilling through a normal dip-slip fault result in a "missing section" of strata in a vertical wellbore?
          <div class="pq-ans">✔ Correct Answer: Because horizontal crustal extension (heave) pulls the stratigraphic layers apart, creating a horizontal gap.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Normal fault heave separates strata laterally; a vertical wellbore passing through the fault plane passes from hanging wall into footwall, missing the intervening stratigraphic section.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 28, part1, part2, part3)


# ==============================================================================
# Q029: Disconformity
# ==============================================================================
def generate_q029():
    title = "Q029: Stratigraphic Unconformities: Disconformity vs. Paraconformity | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Stratigraphy & Unconformity Analysis"
    h1_title = "Q029: Stratigraphic Unconformities: Disconformity vs. Paraconformity"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 29<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Ch. 12: Stratigraphic Principles, pp. 385–390); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Unconformities, pp. 206–210); Dunbar & Rodgers, <em>Principles of Stratigraphy</em> (Wiley, 1957); Gary, McAfee & Wolf, <em>Glossary of Geology</em> (AGI)."""

    part1 = r"""
  <!-- CARD 1: THE FOUR UNCONFORMITIES -->
  <div class="card">
    <div class="card-header bg-blue">1. The Four Fundamental Types of Unconformities</div>
    <div class="card-body">
      <p>An <strong>unconformity</strong> is a substantial break, gap, or hiatus in the geological rock record representing a significant interval of non-deposition, subaerial weathering, and erosion. In classical stratigraphy (Dunbar & Rodgers, 1957; Boggs, 2011; Bangar, p. 207), unconformities are classified into four distinct types based on the geometric relationship between the older underlying rocks and younger overlying rocks:</p>

      <ul>
        <li><strong>1. Disconformity:</strong> An unconformity between <strong>parallel sedimentary strata</strong> where the contact is marked by an obvious, irregular, undulating <strong>erosional surface</strong> (paleotopography, ancient river channels, fossil soil horizons / paleosols, or basal conglomerate lag beds). Beds above and below the surface are structurally parallel (same strike and dip).</li>
        <li><strong>2. Paraconformity:</strong> An unconformity between parallel sedimentary strata where the contact is a completely planar, simple bedding surface displaying <strong>no visible erosional relief</strong>. It resembles a normal conformable bedding plane and can only be identified by a major biostratigraphic gap (faunal hiatus/missing fossil zones).</li>
        <li><strong>3. Angular Unconformity:</strong> An unconformity in which older strata dip at a different angle than younger overlying strata (structural angular discordance produced by tectonic folding/tilting prior to erosion).</li>
        <li><strong>4. Nonconformity:</strong> An unconformity where layered sedimentary strata are deposited directly on an eroded surface of crystalline igneous plutonic rocks (granite) or metamorphic rocks (gneiss, schist).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q29/boggs_fig12_5_four_unconformities.png" alt="Four Types of Unconformities from Sam Boggs Jr.">
        <div class="tb-caption">
          <strong>Figure 29.1 (Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em>, 5th Ed., Fig. 12.5):</strong> Block diagrams illustrating the four major types of unconformities: (A) Angular unconformity, (B) Disconformity, (C) Paraconformity, and (D) Nonconformity.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MORPHOLOGY OF A DISCONFORMITY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Physical Manifestations of a Disconformity in the Field</div>
    <div class="card-body">
      <p>In field geology, a <strong>disconformity</strong> is diagnosed by unmistakable physical evidence of subaerial exposure and erosion, despite perfect structural parallelism of the strata:</p>

      <ul>
        <li><strong>Incised Paleochannels & Paleotopography:</strong> Ancient river valleys carved into the underlying rock and backfilled with coarse channel sandstones and conglomerates.</li>
        <li><strong>Basal Conglomerates:</strong> Layers of rounded pebbles derived from the underlying eroded formation concentrated along the contact surface.</li>
        <li><strong>Paleosols (Fossil Soils) & Weathering Crusts:</strong> Ancient soil horizons containing calcrete nodules, rootlet bioturbation, or lateritic/bauxitic crusts developed during prolonged subaerial exposure.</li>
        <li><strong>Karst Dissolution Cavities:</strong> In limestone terrains, disconformities are characterized by paleokarst sinkholes, caves, and collapsed breccias.</li>
      </ul>

      <div class="quote-box bangar">
        "Disconformity: It is a type of unconformity in which the beds above and below the erosion surface are parallel to each other. The erosion surface is usually irregular and undulating, marked by the presence of a basal conglomerate containing pebbles of the underlying rocks."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Unconformities, pp. 207–208)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q29/unconformity_four_types_cross_section.png" alt="Unconformity Four Types Cross Section Diagram">
        <div class="tb-caption">
          <strong>Figure 29.2: Cross-Sectional Comparison of Unconformities.</strong> Demonstrating that both Disconformities and Paraconformities maintain parallel strata, but Disconformities exhibit irregular erosional scour.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: WHY OTHER OPTIONS FAIL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Refutation of Nonconformity, Paraconformity, and Angular Unconformity</div>
    <div class="card-body">
      <p>Candidates must clearly differentiate these terms in multiple-choice exams:</p>
      <ul>
        <li><strong>(A) Nonconformity:</strong> Separates sedimentary rocks from underlying <em>crystalline igneous/metamorphic rocks</em>. The underlying rocks are not stratified sedimentary beds.</li>
        <li><strong>(B) Paraconformity:</strong> A special subtype where beds are parallel, but the contact is completely <em>planar with zero erosional relief</em>. In standard university curricula (Bangar, p. 207), <strong>Disconformity</strong> is the primary standard umbrella term for parallel sedimentary unconformities.</li>
        <li><strong>(C) Angular unconformity:</strong> The beds above and below are non-parallel (angular discordance).</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 29)</div>
    <div class="q-stmt">
      Q29. A type of unconformity in which the beds above and below are parallel is termed as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Nonconformity</div>
      <div class="raw-opt">(B) Paraconformity</div>
      <div class="raw-opt">(C) Angular unconformity</div>
      <div class="raw-opt correct">(D) Disconformity &nbsp;✔</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) Disconformity</div>
      <div class="sub">
        An unconformity in which the sedimentary beds above and below the erosional break are <strong>parallel to each other</strong> is universally defined as a <strong>Disconformity</strong> (Bangar, p. 207; Boggs, p. 386).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Nonconformity</span>
      <span class="tag wrong">Incorrect (Sediments Overlying Unstratified Crystalline Rocks)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A nonconformity separates layered sedimentary strata from underlying non-sedimentary crystalline basement rocks (plutonic granite or metamorphic gneiss). The rocks below are not "beds" and cannot be parallel.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Paraconformity</span>
      <span class="tag wrong">Incorrect (Obscure Niche Subtype Lacking Physical Erosional Features)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A paraconformity is a specialized, obscure subtype of parallel unconformity that lacks any physical erosional surface or basal conglomerate, detectable exclusively via microfossil biozones. In standard Indian geology curricula and classical textbooks, <strong>Disconformity</strong> is the standard established designation.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Angular unconformity</span>
      <span class="tag wrong">Incorrect (Strata Above and Below Are Non-Parallel)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> In an angular unconformity, older strata were tilted, folded, or faulted prior to erosion, creating an obvious geometric angular discordance between the underlying inclined beds and overlying horizontal beds.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) Disconformity</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard international definition, a <strong>disconformity</strong> is an unconformity where the strata above and below the erosion surface are mutually parallel. It records an eustatic sea-level drop or broad epeirogenic regional uplift that exposed the terrain to subaerial weathering and channel incision without tectonic tilting.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Classification Matrix: The Four Unconformity Types</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Unconformity Type</th>
            <th>Geometric Relationship of Strata</th>
            <th>Nature of Contact Surface</th>
            <th>Primary Geologic Cause</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Disconformity</strong></td>
            <td><strong>Parallel sedimentary strata above and below</strong></td>
            <td><strong>Irregular, undulating erosional scour; paleosols; basal conglomerate</strong></td>
            <td><strong>Eustatic base-level drop; broad epeirogenic uplift without tilting</strong></td>
          </tr>
          <tr>
            <td><strong>Paraconformity</strong></td>
            <td>Parallel sedimentary strata above and below</td>
            <td>Planar, knife-sharp bedding contact (no visible erosional relief)</td>
            <td>Non-deposition in deep marine or starved basin; biostratigraphic gap</td>
          </tr>
          <tr>
            <td><strong>Angular Unconformity</strong></td>
            <td><strong>Non-parallel; angular discordance between beds</strong></td>
            <td>Truncation surface cutting across inclined older strata</td>
            <td>Orogenic tectonic compression, folding, uplift, and deep erosion (Hutton's Siccar Point)</td>
          </tr>
          <tr>
            <td><strong>Nonconformity</strong></td>
            <td>Layered sedimentary strata over crystalline rock</td>
            <td>Eroded plutonic or high-grade metamorphic basement</td>
            <td>Deep crustal exhumation of granite batholiths followed by marine transgression</td>
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
          <strong>Practice Q1:</strong> What world-famous outcrop in Berwickshire, Scotland, discovered by James Hutton in 1788, serves as the historic archetype of an angular unconformity?
          <div class="pq-ans">✔ Correct Answer: Hutton's Unconformity at Siccar Point.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Near-vertical Silurian greywacke strata are truncated and overlain by gently dipping Devonian Old Red Sandstone, proving the vast expanse of geological "deep time".
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> In the Grand Canyon of Arizona, what type of unconformity separates the Vishnu Schist and Zoroaster Granite from the overlying Bass Limestone?
          <div class="pq-ans">✔ Correct Answer: A Nonconformity (the "Great Unconformity").</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Stratified sedimentary beds rest directly on crystalline metamorphic schist and plutonic granite, representing over one billion years of missing geological history.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What field feature distinguishes an intrusive igneous contact (e.g., a granite sill) from an erosional nonconformity?
          <div class="pq-ans">✔ Correct Answer: Contact metamorphism (baking effect/chilled margins) on both upper and lower contacts indicates an intrusion; nonconformities show baking only below and basal conglomerates above.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sills bake sedimentary strata both above and below them; lava flows or eroded batholiths bake only the underlying rocks and provide pebbles to overlying beds.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In sequence stratigraphy, what is a <em>sequence boundary</em>?
          <div class="pq-ans">✔ Correct Answer: A regionally correlative subaerial unconformity (disconformity) and its correlative conformities formed during a sea-level fall.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sequence boundaries are created by forced regressions that incise river valleys into the shelf, forming extensive disconformities.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a <em>hiatus</em> in stratigraphy?
          <div class="pq-ans">✔ Correct Answer: The total geological duration of time missing at an unconformity.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A hiatus represents the sum of the time interval of non-deposition (vacuity) plus the time represented by strata eroded away.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> In Indian stratigraphy, the Eparchaean Unconformity in Tirumala, Andhra Pradesh, is a prime textbook example of which unconformity type?
          <div class="pq-ans">✔ Correct Answer: A Nonconformity.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The Proterozoic Nagari Quartzite of the Cuddapah Supergroup rests directly on eroded Archean granitic gneiss, forming a National Geological Monument.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How is a paraconformity proven in the rock record if physical erosional relief is absent?
          <div class="pq-ans">✔ Correct Answer: High-resolution biostratigraphy proving the absence of multiple index fossil biozones (a faunal gap).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Missing biozones (e.g., missing ammonite or conodont zones) prove that millions of years of time elapsed without physical erosion carving valleys.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a <em>buttress unconformity (onlap unconformity)</em>?
          <div class="pq-ans">✔ Correct Answer: An unconformity where younger sedimentary beds terminate (onlap) against steep, pre-existing paleotopographic bedrock slopes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Marine transgression submerges ancient island hills, depositing horizontal strata that terminate abruptly against steep ancient cliffs.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 29, part1, part2, part3)


# ==============================================================================
# Q030: Map Scale Calculation
# ==============================================================================
def generate_q030():
    title = "Q030: Geological Cartography: Map Scale, Representative Fraction (RF) & Distance | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geological Cartography & Topographic Analysis"
    h1_title = "Q030: Geological Cartography: Map Scale, Representative Fraction (RF) & Distance"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 30<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 12: Geological Maps & Scales, pp. 385–392, Fig. 12.1); Paul R. Wolf & Charles D. Ghilani, <em>Elementary Surveying: An Introduction to Geomatics</em> (14th Ed., Pearson); Survey of India, <em>Topographical Mapping Manual</em>."""

    part1 = r"""
  <!-- CARD 1: CARTOGRAPHIC SCALE FUNDAMENTALS -->
  <div class="card">
    <div class="card-header bg-blue">1. Cartographic Scale & The Representative Fraction (RF)</div>
    <div class="card-body">
      <p>In geological cartography, civil engineering, and surveying, the <strong>Map Scale</strong> is defined as the fixed ratio between the distance measured between any two points on a map ($D_{\text{map}}$) and the corresponding true horizontal distance between those same two points on the ground ($D_{\text{ground}}$):</p>

      <div class="formula-card">
        <div class="formula-title">Fundamental Map Scale Equation</div>
        $$\text{Map Scale} = \frac{\text{Distance on Map } (D_{\text{map}})}{\text{True Distance on Ground } (D_{\text{ground}})}$$
      </div>

      <p>Scale is expressed in three standard formats:</p>
      <ul>
        <li><strong>1. Representative Fraction (RF):</strong> A unitless ratio where the numerator is always unity ($1$). In a $1 : 25,000$ map, $1\text{ unit on the map}$ represents $25,000\text{ identical units on the ground}$ (e.g., $1\text{ cm} = 25,000\text{ cm}$, or $1\text{ inch} = 25,000\text{ inches}$).</li>
        <li><strong>2. Verbal Scale:</strong> An engineering statement equating map units to convenient ground units (e.g., "$1\text{ cm to } 250\text{ meters}$").</li>
        <li><strong>3. Graphical (Bar) Scale:</strong> A subdivided ruler printed on the map margin that remains mathematically accurate even if the map is photographically enlarged or reduced.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q30/map_scale_rf_ground_distance_triangle.png" alt="Map Scale RF Ground Distance Formula Triangle">
        <div class="tb-caption">
          <strong>Figure 30.1: Cartographic Scale Formula Triangle.</strong> Showing the direct mathematical relationships between Map Distance ($D_{\text{map}}$), Representative Fraction ($RF$), and True Ground Distance ($D_{\text{ground}}$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: STEP-BY-STEP CALCULATION -->
  <div class="card">
    <div class="card-header bg-indigo">2. Step-by-Step Derivation for 1:25,000 Scale</div>
    <div class="card-body">
      <p>Applying the Representative Fraction $1 : 25,000$ to a measured map distance of $1.5\text{ cm}$:</p>

      <div class="formula-card">
        <div class="formula-title">Analytical Ground Distance Calculation</div>
        $$D_{\text{ground}} = D_{\text{map}} \times \text{Scale Factor} = 1.5\text{ cm} \times 25,000 = 37,500\text{ cm}$$
        <p style="margin-top:6px; font-size:13.5px; color:#38bdf8;">Converting centimeters to standard metric meters ($1\text{ m} = 100\text{ cm}$):</p>
        $$D_{\text{ground}} = \frac{37,500\text{ cm}}{100\text{ cm/m}} = \mathbf{375\text{ meters}}$$
      </div>

      <div class="quote-box bangar">
        "Scale of Maps: The scale is the ratio between a distance measured on the map and the corresponding distance on the ground. When expressed as a fraction, such as 1:25,000 or 1:50,000, it is called the Representative Fraction (R.F.). On a 1:25,000 map, 1 centimetre represents 25,000 centimetres, which equals 250 metres on the ground."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 12: Geological Maps, p. 386)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q30/bangar_fig12_1_geological_map_scale.png" alt="Geological Map Scale from Bangar">
        <div class="tb-caption">
          <strong>Figure 30.2 (K.M. Bangar, Fig. 12.1):</strong> Graphical scale representation and conversion factors for topographical and geological mapping.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: SURVEY OF INDIA TOPOSHEET HIERARCHY -->
  <div class="card">
    <div class="card-header bg-emerald">3. Survey of India (SOI) Topographic Map Scale Hierarchies</div>
    <div class="card-body">
      <p>In Indian geology and mining, the Survey of India (SOI) toposheet series follows strict geometric numbering hierarchies:</p>
      <ul>
        <li><strong>Million Sheet Series ($1 : 1,000,000$):</strong> Covers $4^\circ \times 4^\circ$ quadrants (e.g., Sheet No. 73 covers Odisha/Jharkhand).</li>
        <li><strong>Degree Sheet Series ($1 : 250,000$):</strong> Covers $1^\circ \times 1^\circ$ quadrangles (designated by letters A to P, e.g., 73H). Scale: $1\text{ cm} = 2.5\text{ km}$.</li>
        <li><strong>Quadrant Sheet Series ($1 : 50,000$):</strong> Covers $15' \times 15'$ quadrangles (numbered 1 to 16, e.g., 73H/15). Scale: $1\text{ cm} = 500\text{ meters}$.</li>
        <li><strong>Special Planning Series ($1 : 25,000$):</strong> Covers $7.5' \times 7.5'$ quadrangles (designated NW, NE, SW, SE). Scale: <strong>$1\text{ cm} = 250\text{ meters}$</strong>.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 30)</div>
    <div class="q-stmt">
      Q30. The distance between two points on a 1: 25,000 map is 1.5 cm than the true distance between them is:
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) 375 m &nbsp;✔</div>
      <div class="raw-opt">(B) 37.5 m</div>
      <div class="raw-opt">(C) 3750 m</div>
      <div class="raw-opt">(D) 3.75 m</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) 375 m</div>
      <div class="sub">
        At a Representative Fraction of $1 : 25,000$, $1\text{ cm}$ on the map equals $25,000\text{ cm} = 250\text{ m}$ on the ground. A measured map distance of $1.5\text{ cm}$ corresponds to $1.5 \times 250\text{ m} = \mathbf{375\text{ meters}}$.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) 375 m</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By direct metric conversion:
      $$D_{\text{ground}} = 1.5\text{ cm} \times 25,000 = 37,500\text{ cm}$$
      Since $1\text{ meter} = 100\text{ centimeters}$:
      $$D_{\text{ground}} = \frac{37,500}{100} = \mathbf{375\text{ meters}}$$
      Thus, option (A) is mathematically exact.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) 37.5 m</span>
      <span class="tag wrong">Incorrect (Factor of 10 Decimal Error)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> $37.5\text{ m}$ results from an arithmetic error dividing by 1000 instead of 100 ($37,500 / 1000 = 37.5\text{ m}$). It corresponds to a scale of $1 : 2,500$, not $1 : 25,000$.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 3750 m</span>
      <span class="tag wrong">Incorrect (Factor of 10 Overestimation)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> $3,750\text{ meters}$ ($3.75\text{ km}$) corresponds to a map scale of $1 : 250,000$ (an SOI degree sheet), where $1.5\text{ cm} \times 250,000 = 375,000\text{ cm} = 3750\text{ m}$.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) 3.75 m</span>
      <span class="tag wrong">Incorrect (Factor of 100 Error)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> $3.75\text{ meters}$ corresponds to an engineering architectural drafting scale of $1 : 250$.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Map Scale & Representative Fraction (RF) Matrix</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Representative Fraction (RF)</th>
            <th>Ground Distance per 1 cm on Map</th>
            <th>Ground Distance for 1.5 cm</th>
            <th>Standard Topographic / Geological Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1 : 1,000</strong></td>
            <td>$10\text{ meters}$</td>
            <td>$15\text{ meters}$</td>
            <td>Mine pit engineering; dam site foundation plans</td>
          </tr>
          <tr>
            <td><strong>1 : 10,000</strong></td>
            <td>$100\text{ meters}$</td>
            <td>$150\text{ meters}$</td>
            <td>Detailed mineral block exploration; urban cadastral mapping</td>
          </tr>
          <tr>
            <td><strong>1 : 25,000</strong></td>
            <td><strong>$250\text{ meters}$</strong></td>
            <td><strong>$\mathbf{375\text{ meters}}$</strong></td>
            <td><strong>SOI 7.5' special topographic sheets; district watershed planning</strong></td>
          </tr>
          <tr>
            <td><strong>1 : 50,000</strong></td>
            <td>$500\text{ meters}$ ($0.5\text{ km}$)</td>
            <td>$750\text{ meters}$</td>
            <td>Standard Survey of India 15' toposheet; regional geological quadrangle maps</td>
          </tr>
          <tr>
            <td><strong>1 : 250,000</strong></td>
            <td>$2,500\text{ meters}$ ($2.5\text{ km}$)</td>
            <td>$3,750\text{ meters}$ ($3.75\text{ km}$)</td>
            <td>SOI $1^\circ \times 1^\circ$ degree sheets; state geological overview maps</td>
          </tr>
          <tr>
            <td><strong>1 : 1,000,000</strong></td>
            <td>$10,000\text{ meters}$ ($10.0\text{ km}$)</td>
            <td>$15,000\text{ meters}$ ($15.0\text{ km}$)</td>
            <td>Million sheet series; National Atlas of India; Geological Map of India</td>
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
          <strong>Practice Q1 (Numerical):</strong> On a $1 : 50,000$ Survey of India geological map, an iron ore body has an outcrop strike length of $4.8\text{ cm}$. Calculate the actual ground strike length of the ore body in kilometers.
          <div class="pq-ans">✔ Worked Answer: $2.40\text{ km}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$D_{\text{ground}} = 4.8\text{ cm} \times 50,000 = 240,000\text{ cm} = 2,400\text{ m} = 2.40\text{ km}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the difference between a <em>large-scale map</em> and a <em>small-scale map</em>?
          <div class="pq-ans">✔ Correct Answer: Large-scale maps have larger numerical RF fractions ($> 1 : 25,000$) showing small areas in great detail; small-scale maps have small fractions ($< 1 : 500,000$) covering vast regional areas with low detail.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because $1/25,000 = 0.00004$ is mathematically larger than $1/250,000 = 0.000004$, a $1 : 25,000$ map is a large-scale map.
          </div>
        </li>

        <li>
          <strong>Practice Q3 (Area Scale Conversion):</strong> A mining lease covers a rectangular area measuring $4.0\text{ cm} \times 5.0\text{ cm}$ on a $1 : 25,000$ toposheet. Calculate the true ground area of the lease in square kilometers ($\text{km}^2$) and hectares ($1\text{ ha} = 10,000\text{ m}^2$).
          <div class="pq-ans">✔ Worked Answer: $\text{Area} = 1.25\text{ km}^2 = 125\text{ hectares}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\text{Ground Width } W = 4.0\text{ cm} \times 250\text{ m/cm} = 1000\text{ m} = 1.0\text{ km}$$<br>
            $$\text{Ground Length } L = 5.0\text{ cm} \times 250\text{ m/cm} = 1250\text{ m} = 1.25\text{ km}$$<br>
            $$\text{Ground Area } A = 1.0\text{ km} \times 1.25\text{ km} = 1.25\text{ km}^2 = 1,250,000\text{ m}^2 = 125\text{ hectares}$$
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> If a map with a scale of $1 : 50,000$ is photocopied and enlarged by $200\%$ ($2\times$ linear enlargement), what is the new scale of the enlarged copy?
          <div class="pq-ans">✔ Correct Answer: $1 : 25,000$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Linear features are twice as long on the copy ($2\text{ cm}$ represents what $1\text{ cm}$ previously represented). The new scale is $2 / 50,000 = 1 / 25,000$.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Why does a graphical bar scale remain accurate after photographic map resizing, whereas a written Representative Fraction (e.g., $1 : 50,000$) becomes false?
          <div class="pq-ans">✔ Correct Answer: The bar scale enlarges or shrinks in exact proportion with the map graphics.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Resizing alters physical distances on paper; the printed RF numbers do not change, but the graphical bar expands/contracts synchronously with the image.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the standard contour interval on Survey of India $1 : 50,000$ toposheets in plains vs. mountainous terrain?
          <div class="pq-ans">✔ Correct Answer: Typically $20\text{ meters}$ (or $10\text{ meters}$ on $1 : 25,000$ sheets).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A $20\text{ m}$ contour interval provides clear topographic visualization without overcrowding steep slopes with contour lines.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> On an aerial photograph of an unmapped region, a runway known to be $1800\text{ meters}$ long measures $7.2\text{ cm}$ on the print. What is the approximate photo scale?
          <div class="pq-ans">✔ Worked Answer: $1 : 25,000$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$\text{Scale} = \frac{D_{\text{photo}}}{D_{\text{ground}}} = \frac{7.2\text{ cm}}{1800\text{ m}} = \frac{7.2\text{ cm}}{180,000\text{ cm}} = \frac{1}{25,000}$$
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is the geographic coverage area in latitude and longitude of a standard Survey of India $1 : 50,000$ quadrangle sheet (e.g., 73H/15)?
          <div class="pq-ans">✔ Correct Answer: $15\text{ minutes of latitude} \times 15\text{ minutes of longitude}$ ($15' \times 15'$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A degree sheet ($1^\circ \times 1^\circ$) is divided into 16 quadrants, each measuring $15' \times 15'$ (approximately $28\text{ km} \times 28\text{ km} \approx 780\text{ km}^2$).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 30, part1, part2, part3)


if __name__ == "__main__":
    for q_fn, q_name in [
        (generate_q026, "Q026_Graben_Horst_Rift_Valley_Fault_Block_Complete_Guide.html"),
        (generate_q027, "Q027_Plunge_Linear_Structural_Feature_Complete_Guide.html"),
        (generate_q028, "Q028_Dip_Slip_Fault_Parallel_Movement_Complete_Guide.html"),
        (generate_q029, "Q029_Disconformity_Parallel_Strata_Erosional_Break_Complete_Guide.html"),
        (generate_q030, "Q030_Map_Scale_RF_1_25000_Distance_Calculation_Complete_Guide.html"),
    ]:
        out_path = os.path.join(SOLUTIONS_DIR, q_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(q_fn())
        print(f"Generated {q_name}: {out_path} ({os.path.getsize(out_path)} bytes)")
