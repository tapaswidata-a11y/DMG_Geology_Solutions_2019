#!/usr/bin/env python3
"""
Masterclass Builder for Q002 and Q003
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q002: Sinuosity Index of Meandering River
# ==============================================================================
def generate_q002():
    title = "Q002: Fluvial Channel Sinuosity Index & Leopold-Wolman Meandering Thresholds | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geomorphology & Fluvial Dynamics"
    h1_title = "Q002: Fluvial Channel Sinuosity Index & Leopold-Wolman Meandering Thresholds"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 2<br>
<strong>Authoritative References:</strong> Leopold & Wolman (1957, USGS Prof. Paper 282-B, pp. 39–85); Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Ch. 8, pp. 248–255); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 2, pp. 45–52)."""

    part1 = r"""
  <!-- CARD 1: MATHEMATICAL DERIVATION & DEFINITIONS -->
  <div class="card">
    <div class="card-header bg-blue">1. Mathematical Definition of Channel Sinuosity & Planform Continuum</div>
    <div class="card-body">
      <p>In fluvial geomorphology and sedimentology, the planform geometry of an alluvial river is quantitatively characterized by its <strong>Sinuosity Index ($S$)</strong>. Sinuosity is dimensionless and expresses the degree of channel wandering relative to the general down-valley slope.</p>
      
      <div class="formula-card">
        <div class="formula-title">Fundamental Sinuosity Formula (Leopold, Wolman & Miller, 1964)</div>
        $$S = \frac{L_{\text{channel}}}{L_{\text{valley}}} = \frac{\text{Actual Thalweg Length between two points}}{\text{Straight-line down-valley distance between those points}}$$
      </div>

      <p>Because the shortest geometric distance between two points is a straight line, the minimum theoretical value of $S$ is <strong>1.0</strong> (an absolute straight channel). In nature, true straight channels with $S = 1.0$ virtually never exist over long reaches due to secondary helical circulation cells, turbulent flow instabilities, and alternating bar formation.</p>

      <div class="quote-box">
        "Channel sinuosity is the ratio of channel length to downvalley distance. Most natural streams are sinuous, and a value of 1.5 is traditionally taken as the dividing line between sinuous and meandering reaches."
        <span class="quote-ref">— Luna B. Leopold and M. Gordon Wolman, <em>River Channel Patterns: Braided, Meandering and Straight</em> (USGS Professional Paper 282-B, 1957, p. 60)</span>
      </div>

      <p>In 1968, J.E. Mueller refined this concept by recognizing that total stream sinuosity ($CI$, Channel Index) is partitioned into two distinct components: <em>Hydraulic Sinuosity ($HSI$)</em>, caused by fluid-dynamic bar growth and cross-current deflection, and <em>Topographic Sinuosity ($TSI$)</em>, caused by regional structural barriers, bedrock lithologies, or valley walls.</p>
    </div>
  </div>

  <!-- CARD 2: LEOPOLD-WOLMAN CRITICAL THRESHOLDS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Leopold-Wolman (1957) Thresholds & Slope-Discharge Continuum</div>
    <div class="card-body">
      <p>The standard quantitative geomorphic classification established by Leopold & Wolman (1957) and adopted universally by modern textbooks (Boggs, 2011; Ritter et al., 2011; Nichols, 2009) categorizes single-thread alluvial channels into three definitive planform domains:</p>
      
      <table>
        <thead>
          <tr>
            <th>Sinuosity Range ($S$)</th>
            <th>Morphological Planform</th>
            <th>Hydraulic & Sedimentological Characteristics</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>$S < 1.05$</td>
            <td><strong>Straight Channel</strong></td>
            <td>Extremely rare in alluvial plains; typically bedrock-confined, structurally controlled along faults/joints, or canalized.</td>
          </tr>
          <tr>
            <td>$1.05 \le S < 1.50$</td>
            <td><strong>Sinuous Channel</strong></td>
            <td>Transitional regime; alternating submerged side-bars (riffles) present, thalweg sinuous but channel banks remain relatively straight.</td>
          </tr>
          <tr>
            <td>$S \ge 1.50$</td>
            <td><strong>Meandering Channel</strong></td>
            <td><strong>Universally accepted threshold for true meandering rivers</strong>; continuous, self-propagating loop sequences, helicoidal secondary flow, lateral point-bar accretion, and neck/chute cutoffs.</td>
          </tr>
        </tbody>
      </table>

      <p>Furthermore, Leopold and Wolman (1957) established that the boundary separating meandering streams from multi-thread braided streams is governed by the <strong>critical channel slope ($S_{\text{crit}}$)</strong> relative to bankfull discharge ($Q_{bf}$):</p>
      
      <div class="formula-card">
        <div class="formula-title">Braided-Meandering Threshold Equation</div>
        $$S_{\text{crit}} = 0.06 \cdot Q^{-0.44} \quad \text{(in metric units: } S_{\text{crit}} = 0.012 \cdot Q^{-0.44}\text{)}$$
      </div>
      <p>Rivers plotting <em>below</em> this critical threshold line maintain a single meandering channel with $S \ge 1.5$; rivers plotting <em>above</em> the line develop steep gradients, bedload overload, and multi-thread braided planforms.</p>

      <div class="tb-figure">
        <img src="../../figures_Q02/sinuosity_threshold_spectrum.png" alt="Channel Sinuosity Threshold Spectrum">
        <div class="tb-caption">
          <strong>Figure 2.1: The Channel Sinuosity Spectrum.</strong> Diagrammatic illustration of stream planforms from straight ($S < 1.05$) to sinuous ($1.05 \le S < 1.50$) and meandering ($S \ge 1.50$), showing the definitive 1.5 quantitative threshold established by Leopold & Wolman (1957).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: HELICAL FLOW & MEANDER MORPHODYNAMICS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Helical Cross-Flow, Point Bar Accretion & Epsilon Cross-Bedding</div>
    <div class="card-body">
      <p>Why do alluvial streams develop sinuosity $\ge 1.5$? The initiation and maintenance of meander bends is driven by <strong>three-dimensional helical secondary circulation</strong>:</p>
      <ul>
        <li><strong>Outer Cut-Bank Shear Stress:</strong> Centrifugal acceleration forces high-velocity surface water toward the outer concave bank, producing water-surface super-elevation. A downward hydrostatic pressure gradient drives water down the outer cut-bank face, maximizing basal boundary shear stress ($\tau_0 = \gamma R S$) and causing rapid hydraulic undercutting and bank collapse.</li>
        <li><strong>Inner Convex Point-Bar Accretion:</strong> The outward-directed surface flow is balanced by an inward-directed, slow bottom return current. This basal current carries sand and gravel up the inner convex bank, depositing a curved <strong>point bar</strong>.</li>
        <li><strong>Lateral Accretion Deposits (Epsilon Cross-Bedding):</strong> As the bend migrates outward and down-valley, point bars aggrade laterally, producing low-angle ($< 15^\circ$) dipping surfaces known in sedimentary petrology as <em>lateral accretion surfaces</em> or <em>epsilon cross-stratification</em> (Allen, 1965).</li>
        <li><strong>Cutoff Mechanics & Oxbow Lakes:</strong> When meander amplitude increases to the point where the narrow neck separating two loops is breached during bankfull floods, a <em>neck cutoff</em> occurs, instantly shortening the river reach and abandoning the loop as an crescent-shaped <strong>oxbow lake</strong> (mortlake).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q02/boggs_fig8_9_meandering_morphology.png" alt="Meandering Channel Morphology from Sam Boggs Jr.">
        <div class="tb-caption">
          <strong>Figure 2.2 (Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em>, 5th Ed., Fig. 8.9):</strong> Dynamic architecture of a high-sinuosity ($S \ge 1.5$) meandering river. Illustrates helicoidal cross-flow, point-bar lateral accretion, cut-bank erosion, chute cutoffs, and abandoned oxbow lake clay plugs.
        </div>
      </div>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 2)</div>
    <div class="q-stmt">
      Q2. Sinuosity Index of a meandering river is greater than the threshold value of :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) 1.4</div>
      <div class="raw-opt correct">(B) 1.5 &nbsp;✔</div>
      <div class="raw-opt">(C) 1.6</div>
      <div class="raw-opt">(D) 1.2</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) 1.5</div>
      <div class="sub">
        In international fluvial geomorphology (Leopold & Wolman 1957; Schumm 1963; Sam Boggs Jr., 5th Ed., p. 248), a stream reach is formally classified as a <strong>meandering river</strong> when its Sinuosity Index satisfies the quantitative criterion <strong>$S \ge 1.5$</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) 1.4</span>
      <span class="tag wrong">Incorrect (Transitional Sinuous Domain)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A river reach with a sinuosity of 1.4 possesses significant curvature and alternating riffle-pool bars, but in quantitative geomorphology it remains classified as <em>sinuous</em> or <em>transitional</em> ($1.05 \le S < 1.50$). It has not crossed the empirical morphological threshold of 1.5 required to develop fully self-sustaining meander loops, neck cutoffs, and oxbow lakes.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) 1.5</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> The value of <strong>1.5</strong> was quantitatively established by Luna B. Leopold and M. Gordon Wolman in their seminal 1957 United States Geological Survey (USGS) paper. They observed that when the ratio of actual channel distance to downvalley distance exceeds 1.5, single-thread alluvial rivers display mature meander loop dynamics, steady helical secondary flow, and characteristic lateral migration. All major university sedimentology and geomorphology textbooks recognize 1.5 as the universal benchmark.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 1.6</span>
      <span class="tag wrong">Incorrect (Exceeds Lower Threshold)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> While mature, highly tortuous meandering rivers frequently achieve sinuosities of 1.6, 2.0, or even 3.0 (e.g., lower Mississippi, meandering reaches of the Brahmaputra and Ganga), 1.6 is an arbitrary intermediate point, not the recognized lower boundary threshold.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) 1.2</span>
      <span class="tag wrong">Incorrect (Low-Sinuosity Channel)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A sinuosity of 1.2 indicates a low-sinuosity channel with minor wandering. Under S.A. Schumm's (1963) classification, channels with $S < 1.3$ are classified as low-sinuosity bedload streams dominated by coarse sand and gravel, with high width-to-depth ratios ($W/D > 40$).
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Classification Matrix: Alluvial Channel Planforms</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Channel Planform</th>
            <th>Sinuosity ($S$)</th>
            <th>Sediment Load Type</th>
            <th>Width-Depth Ratio ($W/D$)</th>
            <th>Primary Depositional Architectural Element</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Straight</strong></td>
            <td>$< 1.05$</td>
            <td>Mixed to Bedload</td>
            <td>Moderate ($15 - 30$)</td>
            <td>Alternating submerged side bars, longitudinal bars</td>
          </tr>
          <tr>
            <td><strong>Sinuous</strong></td>
            <td>$1.05 - 1.49$</td>
            <td>Mixed Load</td>
            <td>Moderate ($20 - 35$)</td>
            <td>Incipient point bars, transverse riffle-pool sequences</td>
          </tr>
          <tr>
            <td><strong>Meandering</strong></td>
            <td><strong>$\ge 1.50$</strong></td>
            <td>Suspended / Fine Mixed Load</td>
            <td>Low to Moderate ($< 20$)</td>
            <td>Lateral accretion point bars, oxbow lake clay plugs, natural levees</td>
          </tr>
          <tr>
            <td><strong>Braided</strong></td>
            <td>Low ($< 1.3$)</td>
            <td>Dominantly Bedload (Gravel/Sand)</td>
            <td>Very High ($> 40$)</td>
            <td>Mid-channel longitudinal bars, transverse bars, multiple active thalwegs</td>
          </tr>
          <tr>
            <td><strong>Anastomosing</strong></td>
            <td>Variable (often $> 1.5$)</td>
            <td>Suspended Fine Silt & Clay</td>
            <td>Very Low ($< 10$)</td>
            <td>Stable avulsion channels separated by vegetated floodplain wetlands</td>
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
          <strong>Practice Q1 (Numerical):</strong> A river reach flowing across an alluvial foreland plain has an actual thalweg channel length of $57.6\text{ km}$ measured along its course between two gauging stations. The straight-line down-valley distance between these two stations is $36.0\text{ km}$. Calculate the Sinuosity Index ($S$) and classify the channel planform according to Leopold & Wolman (1957).
          <div class="pq-ans">✔ Worked Answer: $S = 1.60$; Classified as a Meandering Channel.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$S = \frac{L_{\text{channel}}}{L_{\text{valley}}} = \frac{57.6\text{ km}}{36.0\text{ km}} = 1.60$$
            Since $S = 1.60 \ge 1.50$, the reach exceeds the threshold value of 1.5 and is definitively classified as a <strong>Meandering channel</strong>.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> In a meandering river bend, what is the direction of the secondary helical flow near the channel bed?
          <div class="pq-ans">✔ Correct Answer: Directed inward toward the convex inner bank (point bar).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Water surface super-elevation at the outer concave bank creates a cross-channel pressure gradient. At the bed, where friction retards centrifugal velocity, this pressure gradient forces fluid and bottom bedload to migrate inward toward the convex bank, constructing the point bar.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> According to Hickin and Nanson (1984), at what ratio of meander radius of curvature to channel width ($r_c / w$) does the rate of outer-bank meander migration reach its maximum?
          <div class="pq-ans">✔ Correct Answer: At $r_c / w \approx 2.0 \text{ to } 3.0$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When $r_c / w < 2.0$, severe flow separation occurs along the inner bank, causing energy dissipation that slows outer-bank erosion. When $r_c / w > 3.0$, centrifugal acceleration is weak. Maximum shear stress and migration rate universally peak at $r_c / w \approx 2.5 - 3.0$.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is the diagnostic sedimentary structure that identifies ancient meandering river point bars in the rock record?
          <div class="pq-ans">✔ Correct Answer: Epsilon cross-stratification (low-angle lateral accretion surfaces dipping $< 15^\circ$) showing a fining-upward grain size profile.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> First described by J.R.L. Allen (1965), epsilon cross-bedding forms as the point bar accreted laterally into the migrating channel. The resulting vertical sequence fines upward from basal lag gravels through cross-bedded sand to ripple cross-laminated silts capped by floodplain muds.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How does S.A. Schumm's sediment parameter $M$ (percentage of silt and clay in channel perimeter) relate to sinuosity and channel shape?
          <div class="pq-ans">✔ Correct Answer: Higher $M$ values produce high sinuosity ($S \ge 1.5$), cohesive banks, and narrow, deep channels (low width-to-depth ratio).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Cohesive bank sediments rich in clay/silt resist erosion, forcing the stream to dissipate its energy by increasing path length (meandering) rather than widening. Schumm established that $S = 0.94 M^{0.25}$.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is the critical hydraulic difference between a neck cutoff and a chute cutoff in a meandering river?
          <div class="pq-ans">✔ Correct Answer: Neck cutoff breaches the narrow septum of an exaggerated loop creating an oxbow lake; chute cutoff carves a new channel across the swale of the point bar during overbank flooding.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Neck cutoffs are rapid, avulsive cutoffs occurring at the narrowest point of a meander neck when sinuosity is extremely high, immediately isolating the loop. Chute cutoffs occur during flood stages when water takes a shorter path through swales on the inner point bar without requiring neck closure.
          </div>
        </li>

        <li>
          <strong>Practice Q7 (Numerical):</strong> Calculate the critical channel slope ($S_{\text{crit}}$) required to maintain a meandering channel if the bankfull discharge is $Q = 1000\text{ m}^3/\text{s}$, using the Leopold-Wolman metric relationship $S_{\text{crit}} = 0.012 \cdot Q^{-0.44}$.
          <div class="pq-ans">✔ Worked Answer: $S_{\text{crit}} \approx 0.000574$ (or $0.574\text{ m/km}$).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$Q^{0.44} = (1000)^{0.44} = (10^3)^{0.44} = 10^{1.32} \approx 20.89$$<br>
            $$S_{\text{crit}} = \frac{0.012}{20.89} \approx 0.000574$$
            If the actual valley slope is less than $0.000574$, the river will meander ($S \ge 1.5$). If the slope is steeper, braided channels develop.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Mueller's Hydraulic Sinuosity Index ($HSI$) is calculated as $HSI = \frac{\% \text{Hydraulic Sinuosity}}{\text{Total Sinuosity} - 1}$. If a river has a channel index $CI = 1.80$ and hydraulic sinuosity contributes $0.60$ to the excess sinuosity, what is the $HSI$?
          <div class="pq-ans">✔ Worked Answer: $HSI = 75\%$ (0.75).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            Total excess sinuosity $= CI - 1 = 1.80 - 1.0 = 0.80$.<br>
            $$HSI = \frac{0.60}{0.80} \times 100\% = 75\%$$
            This indicates that $75\%$ of the river's tortuosity is controlled by hydraulic fluid dynamics (meandering bar development) and only $25\%$ by topographic/structural valley guidance.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 2, part1, part2, part3)


# ==============================================================================
# Q003: Aeolian Activity Controls Triad
# ==============================================================================
def generate_q003():
    title = "Q003: Aeolian Dynamic System Controls: Transport Capacity, Supply & Availability | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geomorphology & Aeolian Dynamics"
    h1_title = "Q003: Aeolian Dynamic System Controls: Transport Capacity, Supply & Availability"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 3<br>
<strong>Authoritative References:</strong> Kocurek & Lancaster (1999, <em>Sedimentology</em>, 46, pp. 505–515); Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Ch. 8, pp. 280–288); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 2, pp. 28–33); Bagnold, R.A. (1941, <em>The Physics of Blown Sand and Desert Dunes</em>)."""

    part1 = r"""
  <!-- CARD 1: THE AEOLIAN DYNAMIC TRIAD -->
  <div class="card">
    <div class="card-header bg-blue">1. The Aeolian Dynamic System Triad (Kocurek & Lancaster, 1999)</div>
    <div class="card-body">
      <p>Modern process sedimentology and aeolian geomorphology abandon simplistic climatic assumptions that sand seas (ergs) require "hot desert" climates. Instead, comprehensive physical models (Kocurek & Lancaster 1999; Pye & Tsoar 2009; Boggs 2011) demonstrate that all aeolian accumulation, dune construction, and sand transport are strictly governed by a <strong>Dynamic Triad of Interacting Parameters</strong>:</p>
      
      <ul>
        <li><strong>(i) Transport Capacity ($C$):</strong> The potential maximum kinetic mass of sediment that wind can move per unit time through a specified cross-section. Transport capacity is a direct physical function of aerodynamic shear velocity ($u_*$) and wind power, governed by Bagnold's (1941) cubic sand-flux equation.</li>
        <li><strong>(ii) Sediment Supply ($G$):</strong> The total volume, bulk inventory, and grain-size distribution of sand-sized material ($0.063 - 2.0\text{ mm}$) provided to the basin by primary external source engines—such as braided glacial outwash plains, dry ephemeral wadis, paleolacustrine strandlines, or deeply weathered crystalline granites.</li>
        <li><strong>(iv) Sediment Availability ($A$):</strong> The fraction or proportion of existing sediment supply that is physically, aerodynamically, and mechanically <em>free to be entrained</em> by the wind. Availability is restricted by extrinsic moisture content, evaporite salt crusts, biogenic soil crusts, vegetation cover, groundwater table capillary fringe, and coarse gravel lag armoring.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q03/aeolian_control_triad.png" alt="Aeolian Dynamic Triad Control Model">
        <div class="tb-caption">
          <strong>Figure 3.1: The Aeolian Dynamic Control Triad (Kocurek & Lancaster, 1999).</strong> Conceptual phase diagram showing the three fundamental controls: Transport Capacity, Sediment Supply, and Sediment Availability, which determine whether an aeolian system is in a state of accumulation, equilibrium bypass, or deflation.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: BAGNOLD'S AERODYNAMIC MECHANICS & TRANSPORT MODES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Bagnold's Aerodynamic Physics: Fluid vs. Impact Thresholds</div>
    <div class="card-body">
      <p>Brigadier Ralph Alger Bagnold (1941) laid the empirical and theoretical foundations for particle transport by wind in <em>The Physics of Blown Sand and Desert Dunes</em>. The boundary shear stress ($\tau_0 = \rho_a u_*^2$) exerted by wind on the ground drives three distinct transport modes:</p>

      <ul>
        <li><strong>Saltation (70–80% of total load):</strong> Sand grains ($0.1 - 0.5\text{ mm}$) leap into the air in asymmetric trajectories, rising steeply at $50^\circ$ and descending at shallow angles ($10^\circ - 15^\circ$), imparting kinetic energy upon impact.</li>
        <li><strong>Surface Creep / Reptation (20–25% of total load):</strong> Coarser sand grains and granules ($0.5 - 2.0\text{ mm}$) pushed, rolled, and nudged forward by the ballistic impacts of returning saltating grains.</li>
        <li><strong>Suspension (< 5% of total load):</strong> Fine silts and dust ($< 0.063\text{ mm}$) lifted high into the planetary boundary layer by turbulent eddies, traveling hundreds to thousands of kilometers as dust storms (loess deposits).</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Bagnold's Fluid Threshold Friction Velocity ($u_{*t}$)</div>
        $$u_{*t} = A \sqrt{\frac{\rho_s - \rho_a}{\rho_a} g d}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $A \approx 0.1$ for fluid threshold, $\rho_s$ is quartz density ($2650\text{ kg/m}^3$), $\rho_a$ is air density ($1.22\text{ kg/m}^3$), $g$ is gravity, and $d$ is grain diameter. For $0.25\text{ mm}$ sand, minimum entrainment threshold occurs around $u_* \approx 0.2\text{ m/s}$.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q03/boggs_fig2_4_transport_modes.png" alt="Aeolian Transport Modes from Sam Boggs Jr.">
        <div class="tb-caption">
          <strong>Figure 3.2 (Sam Boggs Jr., 5th Ed., Fig. 2.4):</strong> Mechanics of sediment transport by fluid flow. Illustrates the tripartite division of bedload into traction (rolling/creep), saltation, and suspended load.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: TEXTBOOK EXCERPTS & REFUTATION OF HOT DESERTS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Textbooks on Wind Action & Scientific Refutation of "Hot Deserts"</div>
    <div class="card-body">
      <p>Why is condition <strong>(iii) Hot desertic conditions</strong> categorically excluded from the primary physical controls? Because <em>temperature is not an aerodynamic parameter</em>. Aeolian processes are exceptionally active in hyper-arid <strong>cold polar and sub-polar deserts</strong>:</p>

      <ul>
        <li><strong>Periglacial & Polar Ergs:</strong> Massive active dune fields occur in the McMurdo Dry Valleys of Antarctica ($-30^\circ\text{C}$ to $-50^\circ\text{C}$), the Kobuk Valley of sub-arctic Alaska, and the periglacial outwash sandurs of Iceland and Greenland.</li>
        <li><strong>Extraterrestrial Aeolian Systems:</strong> Gigantic active dune systems cover extensive regions of Mars (where mean surface temperatures are $-60^\circ\text{C}$) and Saturn's moon Titan ($-179^\circ\text{C}$ with methane/ethane winds).</li>
      </ul>

      <div class="quote-box bangar">
        "Wind is an active agent of erosion, transportation and deposition only in arid and semi-arid regions where rainfall is scanty, vegetation is scarce or absent, and loose dry materials are easily picked up... Temperature extremes assist mechanical disintegration, but the movement of material is purely a mechanical operation of wind velocity and sediment supply."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 2: Geological Work of Wind, pp. 28–29)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q03/bangar_fig2_3_2_4_wind_transport.png" alt="Wind Transportation Modes from Bangar">
        <div class="tb-caption">
          <strong>Figure 3.3 (K.M. Bangar, Fig. 2.3 & 2.4):</strong> Geological work of wind. Shows particle movement via saltation and suspension, demonstrating that aerodynamic shear stress and particle size dictate movement regardless of ambient temperature.
        </div>
      </div>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 3)</div>
    <div class="q-stmt">
      Q3. Aeolian activity is primarily controlled by: (i) Transport capacity, (ii) Sediment supply, (iii) Hot desertic conditions, (iv) Sediment availability. Choose the correct set of answer from the following options :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) (i), (ii), (iii)</div>
      <div class="raw-opt correct">(B) (i), (ii), (iv) &nbsp;✔</div>
      <div class="raw-opt">(C) (i), (iii), (iv)</div>
      <div class="raw-opt">(D) (i), (ii), (iii), (iv)</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) (i), (ii), (iv)</div>
      <div class="sub">
        In modern aeolian process sedimentology (Kocurek & Lancaster 1999; Boggs 2011), the primary controls on aeolian system dynamics form a fundamental triad: <strong>(i) Transport capacity</strong>, <strong>(ii) Sediment supply</strong>, and <strong>(iv) Sediment availability</strong>. "Hot desertic conditions" is a classic distractor because aeolian transport operates identically in frigid polar, sub-arctic, and extraterrestrial environments.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) (i), (ii), (iii)</span>
      <span class="tag wrong">Incorrect (Omits Availability & Includes Climatological Distractor)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option omits <em>Sediment availability</em>—a disastrous oversight because an abundant sediment supply cannot be transported if it is locked beneath a high water table, salt crust, or lag armor. Furthermore, it erroneously includes "hot desertic conditions", which is scientifically invalid.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) (i), (ii), (iv)</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Statements (i), (ii), and (iv) comprise the universally acknowledged <strong>Aeolian Dynamic Triad</strong> established by Kocurek & Lancaster (1999). <em>Transport capacity</em> dictates the kinetic wind energy; <em>sediment supply</em> dictates the total reservoir of sand produced by weathering/fluvial systems; and <em>sediment availability</em> dictates how much of that reservoir can actually be lifted into the air stream without being anchored by moisture or surface crusts.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) (i), (iii), (iv)</span>
      <span class="tag wrong">Incorrect (Omits Fundamental Sediment Supply)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option fails to include <em>Sediment supply</em>. Without a primary source supplying sand-sized siliciclastic grains into a sedimentary basin, strong winds can only generate bare bedrock deflation surfaces (hamadas) or gravel lag pavements, completely preventing dune formation.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) (i), (ii), (iii), (iv)</span>
      <span class="tag wrong">Incorrect (Popular Superficially All-Inclusive Trap)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This is the universal "all-of-the-above" trap designed to lure candidates who conflate casual layperson associations (linking sand dunes strictly to hot Sahara-like deserts) with rigorous physics. Because high-latitude cold dunes (e.g., Great Kobuk, Alaska; Lake Athabasca, Canada; Victoria Valley, Antarctica) and Martian ergs experience intense aeolian activity under freezing conditions, thermal heat is definitively not a primary control.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Diagnostic Matrix: States of the Aeolian System (Kocurek & Lancaster Model)</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Aeolian Regime State</th>
            <th>Governing Control Relationship</th>
            <th>Morphodynamic Process</th>
            <th>Resulting Sedimentary & Landscape Product</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Supply-Limited (Starved)</strong></td>
            <td>$\text{Transport Capacity } (C) \gg \text{Sediment Supply } (G)$</td>
            <td>Maximum deflation, wind scour, grain export</td>
            <td>Deflation hollows, yardangs, reg/serir desert pavement, ventifacts</td>
          </tr>
          <tr>
            <td><strong>Availability-Limited</strong></td>
            <td>$G \text{ high, but Availability } (A) \ll C$</td>
            <td>Moisture / crust stabilization, capillary locking</td>
            <td>Interdune sabkhas, salt encrustations, anchored shadow dunes</td>
          </tr>
          <tr>
            <td><strong>Capacity-Limited (Accumulating)</strong></td>
            <td>$\text{Transport Capacity } (C) < \text{Sediment Supply } (G \cdot A)$</td>
            <td>Deceleration, aerodynamic stalling, net aggradation</td>
            <td>Massive compound ergs, transverse/barchan dune fields, draa complexes</td>
          </tr>
          <tr>
            <td><strong>Dynamic Equilibrium (Bypass)</strong></td>
            <td>$C \approx G \cdot A$</td>
            <td>Sediment throughput without net erosion or deposition</td>
            <td>Migrating sand sheets, mobile barchan corridors over planar substrate</td>
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
          <strong>Practice Q1 (Numerical Flux):</strong> According to Bagnold's sand flux formulation, mass transport rate per unit width of channel ($q$) varies with the cube of shear velocity ($q = C \cdot \frac{\rho_a}{g} u_*^3$). If a desert gale increases the aerodynamic friction velocity ($u_*$) from $0.30\text{ m/s}$ to $0.60\text{ m/s}$ (a 2-fold increase), by what factor does the sand transport rate increase?
          <div class="pq-ans">✔ Worked Answer: Increases by a factor of $8$ ($2^3 = 8$, an $800\%$ increase).</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            $$\frac{q_2}{q_1} = \left(\frac{u_{*2}}{u_{*1}}\right)^3 = \left(\frac{0.60}{0.30}\right)^3 = 2^3 = 8$$
            This cubic dependency demonstrates why high-magnitude, low-frequency storm events perform the vast majority of geological work in aeolian environments.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the difference between Bagnold's <em>fluid threshold</em> and <em>impact threshold</em>?
          <div class="pq-ans">✔ Correct Answer: Fluid threshold is the wind velocity required to initiate grain motion purely by fluid drag; impact threshold is the lower velocity required to sustain movement once saltating grains begin impacting the bed.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the kinetic energy transferred by returning saltating grains dislodges stationary bed particles mechanically, the impact threshold friction velocity ($u_{*ti}$) is approximately $80\%$ of the initial fluid threshold velocity ($u_{*t}$).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> Why does the threshold friction velocity curve for entrainment of dry sediment display a minimum around grain sizes of $0.08 - 0.10\text{ mm}$ (fine sand), increasing for both coarser gravel AND ultra-fine clays/silts?
          <div class="pq-ans">✔ Correct Answer: Coarse grains require more wind power due to gravitational mass; ultra-fine clay/silt particles are held by strong inter-particle electrostatic (van der Waals) cohesion and hide within the laminar sublayer.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Particles smaller than $0.05\text{ mm}$ do not protrude into the turbulent boundary layer and are bound tightly by cohesive surface forces, making pure clay beds extremely resistant to wind erosion unless impacted by saltating sand grains.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In an aeolian system, how does a rising regional groundwater table influence sand accumulation?
          <div class="pq-ans">✔ Correct Answer: It acts as an absolute baseline of deflation (Stokes surface) by drastically reducing sediment availability through capillary moisture.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Wet sand cannot be entrained because surface tension of capillary water creates meniscus bonding forces hundreds of times greater than aerodynamic lift. The water table thus acts as an accumulation baseline, preserving underlying aeolian strata in the rock record.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Desert pavement (known as <em>reg</em> in the western Sahara or <em>serir</em> in the eastern Sahara) is primarily formed by which physical process?
          <div class="pq-ans">✔ Correct Answer: Deflation (removal of fine sand and dust) leaving behind a concentrated armor of interlocking coarse gravel and pebbles, augmented by dust infiltration beneath the stones.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Winnowing of sand-sized grains exposes coarse clasts. Modern research shows that once formed, the pebble mosaic traps windblown dust, which washes beneath the stones, progressively lifting the pavement upward on a layer of fine vesicular silt.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What dune morphology develops under a strictly <em>unidirectional</em> wind regime in an area with a <em>limited sediment supply</em> moving across a hard, non-erodible substrate?
          <div class="pq-ans">✔ Correct Answer: Barchan dunes (crescentic dunes with horns pointing downwind).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Barchans are classic indicators of supply-limited conditions under a persistent one-directional wind. If sediment supply increases dramatically, individual barchans coalesce laterally into transverse dune ridges.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Star dunes (radially symmetrical pyramidal sand mounds with multiple slip faces) require which specific meteorological wind regime?
          <div class="pq-ans">✔ Correct Answer: A complex, multi-directional or multidirectional seasonal wind regime with high wind variability.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because winds blow from three or more distinct directions throughout the year, sand is not transported across large regional distances; instead, it accumulates vertically in place, creating the highest dunes on Earth (up to $300 - 500\text{ m}$ tall in the Namib and Badain Jaran deserts).
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is the aerodynamic roughness length ($z_0$) over a flat desert sand sheet, and how does it relate to the logarithmic wind profile equation $u_z = \frac{u_*}{\kappa} \ln\left(\frac{z}{z_0}\right)$?
          <div class="pq-ans">✔ Correct Answer: $z_0 \approx d / 30$ (approximately $1/30$th of the mean grain diameter $d$), representing the theoretical height above the bed where velocity extrapolates to zero.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In von Kármán's logarithmic law of the wall, $\kappa \approx 0.40$ is the von Kármán constant. When saltation begins, moving grains extract momentum from the air, causing the effective aerodynamic roughness length ($z_0'$) to increase significantly to several grain diameters.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 3, part1, part2, part3)


if __name__ == "__main__":
    out_q2 = os.path.join(SOLUTIONS_DIR, "Q002_Sinuosity_Index_Meandering_River_Complete_Guide.html")
    with open(out_q2, "w", encoding="utf-8") as f:
        f.write(generate_q002())
    print(f"Generated Q002: {out_q2} ({os.path.getsize(out_q2)} bytes)")

    out_q3 = os.path.join(SOLUTIONS_DIR, "Q003_Aeolian_Activity_Transport_Sediment_Supply_Complete_Guide.html")
    with open(out_q3, "w", encoding="utf-8") as f:
        f.write(generate_q003())
    print(f"Generated Q003: {out_q3} ({os.path.getsize(out_q3)} bytes)")
