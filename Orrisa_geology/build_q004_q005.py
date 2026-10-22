#!/usr/bin/env python3
"""
Masterclass Builder for Q004 and Q005
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q004: Tectonic Activity Indices (Morphotectonics)
# ==============================================================================
def generate_q004():
    title = "Q004: Tectonic Activity Indices in Morphotectonic Basin Analysis | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Tectonic Geomorphology & Morphotectonics"
    h1_title = "Q004: Tectonic Activity Indices in Morphotectonic Basin Analysis"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 4<br>
<strong>Authoritative References:</strong> Edward A. Keller & Nicholas Pinter, <em>Active Tectonics: Earthquakes, Uplift, and Landscape</em> (2nd Ed., Ch. 5, pp. 120–150); Bull & McFadden (1977); Hack, J.T. (1973, USGS Jour. Research, 1, pp. 421–429); Burbank & Anderson (2011, <em>Tectonic Geomorphology</em>)."""

    part1 = r"""
  <!-- CARD 1: THE MORPHOTECTONIC FRAMEWORK -->
  <div class="card">
    <div class="card-header bg-blue">1. The Quantitative Morphotectonic Framework (Keller & Pinter, 2002)</div>
    <div class="card-body">
      <p>In regions subject to active crustal deformation, earthquakes, and fault propagation, landscape evolution is driven by the dynamic competition between <strong>tectonic rock uplift</strong> and <strong>fluvial/hillslope incision</strong>. Because tectonic processes operate over timescales of $10^3 - 10^6\text{ years}$—far exceeding instrumental seismic records—geomorphologists rely on <strong>Tectonic Activity Indices</strong> derived from digital elevation models (DEMs) and drainage basin metrics to identify, quantify, and map differential uplift and seismic hazard.</p>

      <div class="quote-box">
        "Tectonic geomorphology evaluates the interplay between tectonic and surface processes that shape the landscape in regions of active crustal deformation. Quantitative morphotectonic indices provide a rapid and powerful reconnaissance tool for evaluating relative tectonic activity across drainage basins."
        <span class="quote-ref">— Edward A. Keller and Nicholas Pinter, <em>Active Tectonics: Earthquakes, Uplift, and Landscape</em> (Prentice Hall, 2002, p. 121)</span>
      </div>

      <p>The internationally standardized morphotectonic suite formalized by Keller & Pinter (2002) includes four primary morphometric indices: <strong>Drainage Basin Asymmetry ($AF$)</strong>, <strong>Stream Length-Gradient Index ($SL$)</strong>, <strong>Mountain-Front Sinuosity ($S_{mf}$)</strong>, and the <strong>Valley Floor Width-to-Valley Height Ratio ($V_f$)</strong>.</p>
    </div>
  </div>

  <!-- CARD 2: MATHEMATICAL FORMULATIONS OF THE 4 INDICES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Mathematical Derivations & Geodynamic Sensitivity of the Four Indices</div>
    <div class="card-body">
      <p>Each index diagnoses a specific structural and erosional manifestation of active deformation:</p>

      <div class="formula-card">
        <div class="formula-title">1. Asymmetry Factor ($AF$) — Hare & Gardner (1985)</div>
        $$AF = 100 \times \left(\frac{A_r}{A_t}\right)$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $A_r$ is the basin area on the downstream right of the trunk stream, and $A_t$ is total basin area. Under tectonic stability, $AF \approx 50\%$. Significant deviations ($AF > 50\%$ or $AF < 50\%$) indicate lateral tectonic tilting orthogonal to stream flow.</p>
      </div>

      <div class="formula-card">
        <div class="formula-title">2. Stream Length-Gradient Index ($SL$) — Hack (1973)</div>
        $$SL = \left(\frac{\Delta H}{\Delta L}\right) \cdot L$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $\Delta H / \Delta L$ is the reach channel gradient, and $L$ is total channel length from the drainage divide to the midpoint of the reach. Exceptionally high $SL$ anomalies highlight active fault crossings, localized surface uplift, or tectonic knickpoints.</p>
      </div>

      <div class="formula-card">
        <div class="formula-title">3. Mountain-Front Sinuosity ($S_{mf}$) — Bull & McFadden (1977)</div>
        $$S_{mf} = \frac{L_{mf}}{L_s}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $L_{mf}$ is actual length of the mountain front along the foot of the range, and $L_s$ is straight-line length. Active range-bounding normal/thrust faults produce straight fronts with $S_{mf} \approx 1.0 - 1.5$ (Class 1); inactive embayed fronts have $S_{mf} > 2.5$ (Class 3).</p>
      </div>

      <div class="formula-card">
        <div class="formula-title">4. Valley Floor Width-to-Valley Height Ratio ($V_f$) — Bull (1977)</div>
        $$V_f = \frac{2 V_{fw}}{(E_{ld} - E_{sc}) + (E_{rd} - E_{sc})}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $V_{fw}$ is valley floor width, $E_{ld}$ and $E_{rd}$ are divide elevations on left/right, and $E_{sc}$ is valley floor elevation. Low $V_f (< 1.0)$ indicates deep, narrow V-shaped gorges undergoing rapid tectonic incision; high $V_f (\gg 1.0)$ indicates broad, flat valleys dominated by lateral planation.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q04/morphotectonic_indices_suite.png" alt="Morphotectonic Indices Suite Diagram">
        <div class="tb-caption">
          <strong>Figure 4.1: The Four Classic Morphotectonic Indices (Keller & Pinter, 2002).</strong> Schematic representation of (A) Drainage basin asymmetry ($AF$), (B) Stream length-gradient index ($SL$), (C) Mountain-front sinuosity ($S_{mf}$), and (D) Valley width-to-height ratio ($V_f$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: INDEX OF RELATIVE TECTONIC ACTIVITY -->
  <div class="card">
    <div class="card-header bg-emerald">3. Index of Relative Tectonic Activity (IRAT) & Synthesis</div>
    <div class="card-body">
      <p>Because individual indices may be influenced by local lithological contrasts or structural anisotropies, modern active tectonics investigations combine these metrics into an integrated <strong>Index of Relative Tectonic Activity (IRAT)</strong>:</p>
      $$IRAT = \frac{S_{mf} + V_f + AF + SL + Hypsometric\ Integral}{N}$$
      <p>This multi-parameter index classifies mountainous terrains and drainage basins into three distinct tectonic activity regimes:</p>
      <ul>
        <li><strong>Class 1 (High Tectonic Activity):</strong> Ongoing rapid uplift ($> 1\text{ mm/yr}$), high seismicity, straight mountain fronts ($S_{mf} < 1.4$), deeply incised V-shaped canyons ($V_f < 0.5$), and pronounced $SL$ knickpoint anomalies.</li>
        <li><strong>Class 2 (Moderate Tectonic Activity):</strong> Intermediate uplift rates ($0.1 - 0.5\text{ mm/yr}$), partially embayed fronts ($1.4 \le S_{mf} \le 2.5$), and moderately incised valleys ($0.5 \le V_f \le 1.5$).</li>
        <li><strong>Class 3 (Low / Inactive Tectonic Regime):</strong> Tectonic quiescence, extensive lateral erosion, sinuous mountain fronts ($S_{mf} > 2.5$), wide U-shaped alluvial plains ($V_f > 1.5$), and symmetrical basins ($AF \approx 50\%$).</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 4)</div>
    <div class="q-stmt">
      Q4. Which of the following indices belong to 'Tectonic Activity Indices' used for morphotectonic analysis of a drainage basin? (i) Drainage basin asymmetry, (ii) Stream Length-Gradient Index (SL Index), (iii) Mountain-front sinuosity, (iv) Ratio of valley floor width to valley height. Choose the correct set of answer from the following options :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) (i), (ii) and (iv)</div>
      <div class="raw-opt">(B) (ii) and (iv)</div>
      <div class="raw-opt correct">(C) (i), (ii), (iii) and (iv) &nbsp;✔</div>
      <div class="raw-opt">(D) (ii), (iii) and (iv)</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) (i), (ii), (iii) and (iv)</div>
      <div class="sub">
        All four parameters—<strong>(i) Drainage basin asymmetry ($AF$)</strong>, <strong>(ii) Stream Length-Gradient Index ($SL$)</strong>, <strong>(iii) Mountain-front sinuosity ($S_{mf}$)</strong>, and <strong>(iv) Ratio of valley floor width to valley height ($V_f$)</strong>—constitute the canonical suite of morphotectonic indices established by Bull & McFadden (1977) and Keller & Pinter (2002).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) (i), (ii) and (iv)</span>
      <span class="tag wrong">Incorrect (Omits Mountain-Front Sinuosity)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option omits parameter (iii) <em>Mountain-front sinuosity ($S_{mf}$)</em>. $S_{mf}$ is one of the oldest and most fundamental tectonic indices in geomorphology (Bull & McFadden, 1977), directly quantifying the activity of range-bounding piedmont fault scarps.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) (ii) and (iv)</span>
      <span class="tag wrong">Incorrect (Severely Incomplete Subset)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> While $SL$ and $V_f$ are valid indices, this option completely ignores drainage basin asymmetry ($AF$) and mountain-front sinuosity ($S_{mf}$), excluding half of the standard analytical suite.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) (i), (ii), (iii) and (iv)</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Every single listed metric belongs to the primary suite of quantitative indices used in modern tectonic geomorphology. In Chapter 5 of <em>Active Tectonics</em>, Keller & Pinter explicitly group these exact four parameters together as the indispensable toolkit for morphotectonic basin analysis.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) (ii), (iii) and (iv)</span>
      <span class="tag wrong">Incorrect (Omits Drainage Basin Asymmetry)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option omits parameter (i) <em>Drainage basin asymmetry ($AF$)</em>. $AF$ is essential for detecting broad tectonic ground tilting and differential block rotation perpendicular to the master drainage channel.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Quantitative Classification Thresholds: Tectonic Activity Classes (Keller & Pinter Suite)</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Morphotectonic Index</th>
            <th>Symbol & Formula</th>
            <th>Class 1 (High Activity)</th>
            <th>Class 2 (Moderate Activity)</th>
            <th>Class 3 (Low / Inactive)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mountain-Front Sinuosity</strong></td>
            <td>$S_{mf} = L_{mf} / L_s$</td>
            <td><strong>$1.0 \le S_{mf} < 1.4$</strong> (Straight)</td>
            <td>$1.4 \le S_{mf} \le 2.5$</td>
            <td>$S_{mf} > 2.5$ (Deeply embayed)</td>
          </tr>
          <tr>
            <td><strong>Valley Floor Width / Height</strong></td>
            <td>$V_f = \frac{2 V_{fw}}{(E_{ld}-E_{sc}) + (E_{rd}-E_{sc})}$</td>
            <td><strong>$V_f < 0.5$</strong> (Deep V-gorge)</td>
            <td>$0.5 \le V_f \le 1.5$</td>
            <td>$V_f > 1.5$ (Broad flat valley)</td>
          </tr>
          <tr>
            <td><strong>Basin Asymmetry Factor</strong></td>
            <td>$AF = 100(A_r / A_t)$</td>
            <td><strong>$|AF - 50| \ge 15$</strong> (Strong tilt)</td>
            <td>$7 \le |AF - 50| < 15$</td>
            <td>$|AF - 50| < 7$ (Symmetrical)</td>
          </tr>
          <tr>
            <td><strong>Stream Length-Gradient</strong></td>
            <td>$SL = (\Delta H / \Delta L) \cdot L$</td>
            <td><strong>$SL > 500$</strong> (Severe knickpoints)</td>
            <td>$200 \le SL \le 500$</td>
            <td>$SL < 200$ (Graded equilibrium profile)</td>
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
          <strong>Practice Q1 (Numerical $AF$ Calculation):</strong> A drainage basin has a total catchment area $A_t = 600\text{ km}^2$. The catchment area lying to the right of the master trunk stream (looking downstream) is measured as $A_r = 432\text{ km}^2$. Calculate the Asymmetry Factor ($AF$) and infer the tectonic deformation of the basin.
          <div class="pq-ans">✔ Worked Answer: $AF = 72\%$; Indicates strong lateral tectonic tilting down toward the right bank.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$AF = 100 \times \left(\frac{A_r}{A_t}\right) = 100 \times \left(\frac{432}{600}\right) = 72\%$$
            The deviation $|AF - 50| = |72 - 50| = 22\% > 15\%$, placing the basin into <strong>Class 1 (High Tectonic Activity)</strong>. The stream has migrated toward the left due to ground tilting downward to the right.
          </div>
        </li>

        <li>
          <strong>Practice Q2 (Numerical $SL$ Calculation):</strong> Along a mountain stream reach, the channel drops in elevation by $\Delta H = 50\text{ m}$ over a reach length $\Delta L = 400\text{ m}$. The total length from the drainage headwaters divide to the reach midpoint is $L = 6000\text{ m}$. Calculate the Hack Stream Length-Gradient Index ($SL$).
          <div class="pq-ans">✔ Worked Answer: $SL = 750\text{ m}$.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            Reach gradient $S = \frac{\Delta H}{\Delta L} = \frac{50\text{ m}}{400\text{ m}} = 0.125$.<br>
            $$SL = \left(\frac{\Delta H}{\Delta L}\right) \cdot L = 0.125 \times 6000\text{ m} = 750\text{ m}$$
            Because $SL = 750\text{ m} > 500\text{ m}$, this reach represents an anomalously steep tectonic knickpoint, likely indicating an active fault crossing or localized surface uplift.
          </div>
        </li>

        <li>
          <strong>Practice Q3 (Numerical $S_{mf}$ Classification):</strong> A mountain range front has a straight-line end-to-end distance $L_s = 15.0\text{ km}$. The surveyed actual mountain-piedmont junction length is $L_{mf} = 18.3\text{ km}$. Calculate $S_{mf}$ and assign the tectonic activity class under the Bull & McFadden (1977) scheme.
          <div class="pq-ans">✔ Worked Answer: $S_{mf} = 1.22$; Assigned to Class 1 (Tectonically Active Mountain Front).</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            $$S_{mf} = \frac{L_{mf}}{L_s} = \frac{18.3\text{ km}}{15.0\text{ km}} = 1.22$$
            Because $S_{mf} < 1.40$, tectonic uplift along the range-bounding fault outpaces stream incision and pediment embayment, maintaining a nearly straight fault-line scarp.
          </div>
        </li>

        <li>
          <strong>Practice Q4 (Numerical $V_f$ Valley Inversion):</strong> Cross-sectional profiling across a valley yields: valley floor width $V_{fw} = 30\text{ m}$, left divide elevation $E_{ld} = 850\text{ m}$, right divide elevation $E_{rd} = 810\text{ m}$, and valley floor elevation $E_{sc} = 550\text{ m}$. Calculate the $V_f$ ratio and interpret the geomorphic state.
          <div class="pq-ans">✔ Worked Answer: $V_f = 0.107$; Indicates intense, rapid vertical channel incision driven by active tectonic uplift.</div>
          <div class="pq-exp">
            <strong>Calculation:</strong><br>
            Left relief $= 850 - 550 = 300\text{ m}$; Right relief $= 810 - 550 = 260\text{ m}$.<br>
            $$V_f = \frac{2 V_{fw}}{(E_{ld} - E_{sc}) + (E_{rd} - E_{sc})} = \frac{2(30)}{300 + 260} = \frac{60}{560} \approx 0.107$$
            Since $V_f \ll 0.5$, the cross-section is an acute V-shaped canyon characteristic of rapid tectonic incisive response to crustal uplift.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How is Hack's Law expressed mathematically, and what does it relate in drainage basin morphometry?
          <div class="pq-ans">✔ Correct Answer: $L = C \cdot A^h$ (where $L$ is mainstream length, $A$ is basin area, $C \approx 1.4$, and $h \approx 0.55 - 0.60$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Hack's Law proves that drainage basins become increasingly elongated rather than geometrically circular as they grow in size, because the exponent $h > 0.5$.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What does a high Hypsometric Integral ($HI > 0.60$) indicate regarding Strahler's cycle of landscape erosion?
          <div class="pq-ans">✔ Correct Answer: Indicates a "youthful" landscape experiencing active tectonic uplift where most rock mass has not yet been eroded.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The hypsometric integral represents the volume of unconsumed bedrock remaining beneath the hypsometric curve. $HI > 0.60$ is diagnostic of young, actively uplifting mountain ranges; mature landscapes have $0.35 \le HI \le 0.60$; and old peneplains have $HI < 0.35$.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How can a tectonic knickpoint be distinguished from a lithologic knickpoint along a longitudinal stream profile?
          <div class="pq-ans">✔ Correct Answer: Tectonic knickpoints migrate upstream across varying rock types at similar elevations across adjacent parallel valleys; lithologic knickpoints are stationary and coincide strictly with resistant bedrock contacts.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> A transient knickpoint generated by a pulse of fault uplift propagates upstream into the landscape independently of underlying rock hardness, appearing as a coherent elevation step across neighboring catchments.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why do paired fluvial terraces signify active tectonic uplift or base-level fall, whereas unpaired terraces typically indicate lateral channel meandering?
          <div class="pq-ans">✔ Correct Answer: Paired terraces occur at identical elevations on opposite sides of a valley, proving rapid, symmetrical downcutting too fast for lateral erosion; unpaired terraces form when a meandering river cuts down slowly while simultaneously shifting laterally.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Tectonic pulses accelerate stream incision rates, stranding former floodplains synchronously on both banks at matching elevations (paired terraces).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 4, part1, part2, part3)


# ==============================================================================
# Q005: Pedestal and Mushroom Rocks
# ==============================================================================
def generate_q005():
    title = "Q005: Morphogenesis of Pedestal & Mushroom Rocks vs. Balanced Rocks | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geomorphology & Arid Landforms"
    h1_title = "Q005: Morphogenesis of Pedestal & Mushroom Rocks vs. Balanced Rocks"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 5<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 2: Work of Wind, pp. 29–31, Fig. 2.2); Arthur Holmes, <em>Principles of Physical Geology</em> (Ch. 21); Thornbury, W.D. (1969, <em>Principles of Geomorphology</em>, Ch. 12); Ritter, Kochel & Miller (2011, <em>Process Geomorphology</em>)."""

    part1 = r"""
  <!-- CARD 1: WIND ABRASION AND VERTICAL SANDBLAST GRADIENT -->
  <div class="card">
    <div class="card-header bg-blue">1. Aerodynamic Sandblast Mechanics & the Vertical Abrasion Profile</div>
    <div class="card-body">
      <p>Wind erosion of consolidated rock masses operates through two distinct physical mechanisms: <strong>deflation</strong> (aerodynamic lifting and winnowing of loose particles) and <strong>abrasion / corrasion</strong> (the kinetic sandblast impact of wind-driven quartz particles against rock obstacles). In desert environments, wind abrasion is severely concentrated in the immediate vicinity of the ground surface due to the physical limits of saltation:</p>

      <ul>
        <li><strong>Saltation Height Boundary:</strong> More than $90 - 95\%$ of all windblown sand grains ($0.1 - 0.5\text{ mm}$) leap through saltation trajectories that rarely exceed <strong>$0.5\text{ to } 1.5\text{ meters}$</strong> above the desert floor.</li>
        <li><strong>Kinetic Energy Profile:</strong> Particle kinetic energy ($KE = \frac{1}{2} m v^2$) peaks at approximately $0.2 - 0.7\text{ meters}$ height, where grain mass (sand rather than dust) and wind velocity are optimally balanced.</li>
        <li><strong>Basal Undercutting:</strong> As a consequence, protruding rock masses experience intense, focused sandblast grinding at their base, while their upper crowns (above $1.5 - 2\text{ meters}$) remain completely unattacked by sand-sized abrasive tools.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Kinetic Energy of Saltating Abrasive Grain</div>
        $$KE = \frac{1}{2} m v^2 = \frac{1}{2} \left(\frac{4}{3} \pi r^3 \rho_s\right) v_{\text{impact}}^2$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Because mass $m \propto r^3$, coarse sand grains carry thousands of times more abrasive kinetic energy than suspended dust particles, but gravity confines their bounce height strictly to the lowest 1 meter.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q05/mushroom_rock_abrasion_genesis.png" alt="Mushroom Rock Abrasion Genesis Model">
        <div class="tb-caption">
          <strong>Figure 5.1: Morphogenesis of Pedestal / Mushroom Rocks.</strong> Illustrates the vertical sandblast concentration zone ($< 1.5\text{ m}$) producing extreme basal undercutting of a rock tower supporting a broad, un-eroded capstone.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MORPHOLOGICAL TERMINOLOGY: PEDESTAL VS MUSHROOM ROCKS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Geological Nomenclature: Pedestal Rocks, Mushroom Rocks & Pilzfelsen</div>
    <div class="card-body">
      <p>In standard geomorphology and engineering geology syllabi, an isolated erosional rock mass comprising a slender stem, neck, or column supporting an umbrella-like wider cap is described by two universally interchangeable geological terms:</p>

      <ul>
        <li><strong>Pedestal Rock:</strong> The descriptive morphometric term emphasizing the narrow pedestal or columnar stalk supporting the elevated rock mass.</li>
        <li><strong>Mushroom Rock (German: <em>Pilzfelsen</em>):</strong> The visual analog term denoting the characteristic mushroom or toadstool morphology.</li>
      </ul>

      <div class="quote-box bangar">
        "Pedestal or Mushroom Rocks: In desert areas, the wind-blown sand acts like a natural sand-blast. Because the abrasive sand grains are carried close to the ground (seldom exceeding 1 to 2 metres), the lower parts of standing rock masses are eroded much more rapidly than their upper portions. In the course of time, isolated rock masses with narrow slender necks or stems and broad overarching caps are developed. These are termed Pedestal rocks or Mushroom rocks."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 2: Work of Wind, pp. 29–30, Fig. 2.2)</span>
      </div>

      <p>Differential lithology often accelerates this morphodynamic development: when a resistant horizontal caprock (e.g., quartzitic sandstone or basalt) overlies easily abraded, softer rocks (e.g., shale, marl, or friable sandstone), undercutting proceeds with exceptional rapidity.</p>

      <div class="tb-figure">
        <img src="../../figures_Q05/bangar_fig2_2_pedestal_rock.png" alt="Pedestal Rock from Bangar">
        <div class="tb-caption">
          <strong>Figure 5.2 (K.M. Bangar, Fig. 2.2):</strong> Authentic textbook depiction of a Pedestal / Mushroom Rock developed by differential aeolian undercutting of a standing rock column.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: BALANCED ROCKS VS PERCHED BLOCKS (DISTRACTORS) -->
  <div class="card">
    <div class="card-header bg-emerald">3. Petrological Discrimination: Balanced Rocks (Corestones) vs. Perched Blocks (Erratics)</div>
    <div class="card-body">
      <p>To avoid frequent exam confusion, candidates must distinguish aeolian pedestal/mushroom rocks from unrelated weathering and glacial landforms:</p>

      <ul>
        <li><strong>Balanced Rocks (Weathering Tors / Corestones):</strong> Massive, rounded boulders precariously balanced upon underlying bedrock (e.g., the famous "Krishna's Butterball" in Mahabalipuram, or granite tors of Hyderabad and Jabalpur). These are <strong>not aeolian columns</strong>; they are produced by <em>deep subsurface chemical spheroidal weathering</em> along intersecting orthogonal joint sets, followed by stripping of the saprolite mantle (etchplanation).</li>
        <li><strong>Perched Blocks (Glacial Erratics):</strong> Large boulders transported over tens to hundreds of kilometers by moving glaciers and deposited high on cliffs, ridges, or bedrock pedestals as the ice sheet melts. Their mineralogy and petrology are exotic to the local bedrock.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 5)</div>
    <div class="q-stmt">
      Q5. An isolated erosional rock mass comprising a slender stem, neck or column supporting a wider cap is known as: (i) Pedestal rocks, (ii) Mushroom rocks, (iii) Balanced rocks, (iv) Perched blocks. Choose the correct set of answer from the following options :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) (i)</div>
      <div class="raw-opt correct">(B) (i) and (ii) &nbsp;✔</div>
      <div class="raw-opt">(C) (i), (ii) and (iii)</div>
      <div class="raw-opt">(D) (i), (ii), (iii) and (iv)</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) (i) and (ii)</div>
      <div class="sub">
        An isolated erosional pillar with a slender, wind-abraded stem supporting an expansive cap is interchangeably termed a <strong>(i) Pedestal rock</strong> or a <strong>(ii) Mushroom rock</strong> (Bangar, p. 29). Balanced rocks (weathering corestones) and perched blocks (glacial erratics) are genetically distinct landforms that lack a slender erosional columnar neck.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) (i)</span>
      <span class="tag wrong">Incorrect (Incomplete Synonym Set)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> While "Pedestal rock" is correct, this option fails to include "Mushroom rock". In geological literature, "Pedestal rock" and "Mushroom rock" are synonymous terms used interchangeably for this exact landform.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) (i) and (ii)</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Both <strong>(i) Pedestal rocks</strong> and <strong>(ii) Mushroom rocks</strong> (Pilzfelsen) are the precise, universally recognized geomorphic designations for isolated rock masses with slender, undercut necks supporting a wider cap formed by basal sandblast abrasion.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) (i), (ii) and (iii)</span>
      <span class="tag wrong">Incorrect (Includes Chemically Weathered Balanced Rocks)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option wrongly includes <em>(iii) Balanced rocks</em>. A balanced rock is a boulder resting in precarious equilibrium atop a rock base, typically formed by spheroidal weathering of jointed granitic corestones (tors). It does not consist of a single erosional mass with a slender carved neck or column.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) (i), (ii), (iii) and (iv)</span>
      <span class="tag wrong">Incorrect (All-Inclusive Trap Conflating Glacial and Weathering Features)</span>
    </div>
    <div class="option-body">
      <strong>Why this option is incorrect:</strong> This option lumps together four genetically disparate landforms. <em>(iv) Perched blocks</em> are glacially transported erratics deposited by melting ice sheets, possessing no morphological stem or neck.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Genetic Discrimination: Erosional Columns, Tors & Boulders</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Landform Term</th>
            <th>Primary Genetic Mechanism</th>
            <th>Morphological Architecture</th>
            <th>Diagnostic Field Identification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Pedestal Rock / Mushroom Rock</strong></td>
            <td>Aeolian sandblast abrasion concentrated in lowest $1.5\text{ m}$</td>
            <td>Single rock mass with slender neck/stem supporting wide cap</td>
            <td>Polished, fluted, and grooved neck; common in arid desert basins</td>
          </tr>
          <tr>
            <td><strong>Balanced Rock (Tor / Corestone)</strong></td>
            <td>Subsurface chemical spheroidal weathering of orthogonal joint blocks</td>
            <td>Rounded spheroid boulder perched precariously on flat bedrock</td>
            <td>Exfoliation shells, grus apron, granitic plutonic composition</td>
          </tr>
          <tr>
            <td><strong>Perched Block (Glacial Erratic)</strong></td>
            <td>Glacial entrainment, supraglacial transport, and ice-melt ablation</td>
            <td>Angular to sub-rounded massive boulder resting on aliens</td>
            <td>Glacial striations, polished facets, exotic lithology alien to local bedrock</td>
          </tr>
          <tr>
            <td><strong>Yardang</strong></td>
            <td>Unidirectional wind deflation and abrasion in cohesive silt/clay</td>
            <td>Aerodynamically streamlined, keel-shaped parallel ridges</td>
            <td>Steep blunt prow facing upwind, tapered tail pointing downwind</td>
          </tr>
          <tr>
            <td><strong>Zeugen (Singular: Zeuge)</strong></td>
            <td>Differential weathering and wind scour along orthogonal joint fissures</td>
            <td>Tabular, flat-topped ridge capped by resistant hard rock over soft shale</td>
            <td>Trench-and-ridge topography; undercutting along horizontal strata</td>
          </tr>
          <tr>
            <td><strong>Ventifact (Dreikanter)</strong></td>
            <td>Aeolian sandblast grinding of stationary ground pebbles</td>
            <td>Pebble with flat, polished, wind-beveled planar facets and sharp keels</td>
            <td>Two (Zweikanter) or three (Dreikanter) intersecting polished faces</td>
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
          <strong>Practice Q1:</strong> Why is aeolian corrasion (sandblasting) virtually ineffective above a height of $2.0\text{ meters}$ on a desert rock face?
          <div class="pq-ans">✔ Correct Answer: Because saltating quartz sand grains ($0.1 - 0.5\text{ mm}$) cannot bounce higher than $1.5\text{ meters}$ under normal atmospheric wind shear velocities.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Particles traveling above $2\text{ m}$ are exclusively clay and fine silt in suspension ($< 0.05\text{ mm}$), which have negligible kinetic mass and are deflected around rock obstacles by air streamlines without causing impact chipping.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the German geomorphic term widely used internationally for mushroom rocks?
          <div class="pq-ans">✔ Correct Answer: <em>Pilzfelsen</em> (literally "mushroom-rock").</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> First popularized by German geomorphologists describing arid landforms in North Africa and the Middle East, <em>Pilzfelsen</em> appears frequently in classical literature as an exact synonym for pedestal rock.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the essential structural difference between a <em>Zeuge</em> and a <em>Yardang</em>?
          <div class="pq-ans">✔ Correct Answer: A Zeuge is formed in horizontally bedded strata with a hard caprock over soft layers; a Yardang is carved into vertically tilted or homogeneous cohesive fine-grained sediments aligned parallel to wind direction.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Zeugen (mushroom-like tabular ridges) require horizontal structural layering, whereas yardangs are aerodynamic inverted-boat-hull ridges sculpted parallel to the dominant unidirectional wind regime.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> A faceted pebble displaying three polished, wind-beveled faces meeting at sharp ridges is called a:
          <div class="pq-ans">✔ Correct Answer: Dreikanter (a classic three-faceted ventifact).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Ventifacts develop when stationary pebbles on desert pavements are abraded by windblown sand. If wind direction shifts or the stone rolls due to undermining, multiple intersecting facets develop (one facet = Einkanter; two = Zweikanter; three = Dreikanter).
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What role does haloclasty (salt weathering) play in the development of pedestal rocks in hyper-arid playa basins?
          <div class="pq-ans">✔ Correct Answer: Evaporative crystallization of capillary salts near the ground surface disintegrates the rock grain-by-grain, weakening the base for wind scour.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Capillary rise of groundwater draws saline water into the lower 1 meter of the rock. Daily cycles of thermal crystallization and hydration generate internal expansion stresses up to $100\text{ MPa}$, shattering rock minerals into loose sand readily stripped by wind.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> The famous "Krishna's Butterball" in Mahabalipuram, Tamil Nadu, is a classic example of:
          <div class="pq-ans">✔ Correct Answer: A Balanced Rock (Corestone/Tor) formed by sub-surface spheroidal weathering of charnockite/granite.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> It is not an aeolian pedestal rock. It was rounded in situ beneath the regolith by chemical weathering along joints, followed by erosional stripping of the surrounding weathered saprolite.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In a desert basin, an isolated steep-sided erosional bedrock residual mountain rising abruptly from a flat pediment is termed an:
          <div class="pq-ans">✔ Correct Answer: Inselberg (or Bornhardt).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Inselbergs (German for "island mountain") are landscape-scale relict hills (such as Ayers Rock/Uluru) produced by long-term pediplanation, deep weathering, and scarp retreat, distinct from small localized pedestal rocks.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why does differential wind erosion produce hollows, pits, and fretted honeycombs on desert sandstone cliffs (tafoni)?
          <div class="pq-ans">✔ Correct Answer: Due to the synergistic combination of salt weathering, case-hardening of rock surfaces, and wind evacuation of loosened grains from the soft interior.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Once the outer case-hardened crust is breached, cavernous weathering (tafoni) hollows out the interior through salt crystallization and micro-scale moisture cycles.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 5, part1, part2, part3)


if __name__ == "__main__":
    out_q4 = os.path.join(SOLUTIONS_DIR, "Q004_Tectonic_Activity_Indices_Drainage_Basin_Complete_Guide.html")
    with open(out_q4, "w", encoding="utf-8") as f:
        f.write(generate_q004())
    print(f"Generated Q004: {out_q4} ({os.path.getsize(out_q4)} bytes)")

    out_q5 = os.path.join(SOLUTIONS_DIR, "Q005_Pedestal_Mushroom_Rocks_Wind_Abrasion_Complete_Guide.html")
    with open(out_q5, "w", encoding="utf-8") as f:
        f.write(generate_q005())
    print(f"Generated Q005: {out_q5} ({os.path.getsize(out_q5)} bytes)")
