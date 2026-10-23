#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 11 to 17
Assam DGMS 2019 Masterclass Standard
"""

import os
from gen_2019_q001_to_q005 import CSS_STYLES, generate_page

# ==========================================
# QUESTION 11: SAND DUNE - BARCHAN (TRANSVERSE AXIS)
# ==========================================
q11_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Morphodynamic Classification of Aeolian Dunes & Wind Regimes</div>
    <div class="card-body">
      <p>In aeolian geomorphology, sand dunes are classified based on the geometric relationship between the <strong>crest-ridge orientation (long axis)</strong> of the dune and the <strong>prevailing effective wind direction</strong> (Bagnold, 1941; McKee, 1979). When the long axis or crest of a sand dune is oriented <strong>perpendicular (transverse, $90^\\circ$)</strong> to the prevailing sand-transporting wind, it belongs to the transverse dune family, of which the crescentic <strong>barchan</strong> is the classic, quintessential example.</p>

      <div class="quote-box bangar">
        "Dunes whose long axes are oriented across (transverse to) the direction of the prevailing wind are called transverse dunes. The most common and classic variety of transverse dune is the <strong>barchan</strong>, which is crescent-shaped in plan with its convex side facing upwind and its two horns or tips pointing downwind in the direction of the wind."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Geological Work of Wind: Sand Dunes, p. 23)</span>
      </div>

      <p>The two fundamental geometric classes of sand dunes are:</p>
      <ul>
        <li><strong>Transverse Dunes (Including Barchans):</strong> Formed where wind blows predominantly from a single unidirectional quadrant ($RDP/DP > 0.8$). The crest line and slip face are oriented at right angles (transverse) to the wind vector. When sand supply is abundant and continuous, transverse ridges form; when sand supply is limited on a hard desert floor, isolated crescent-shaped <strong>barchans</strong> develop with their long transverse axes and downwind-pointing horns.</li>
        <li><strong>Longitudinal Dunes (Seifs / Sand Ridges):</strong> Formed where wind blows from two converging directions or in bidirectional wind regimes. The long axis of the dune extends <strong>parallel</strong> to the resultant wind direction, forming straight or sinuous razor-backed sand ridges that can extend unbroken for tens of kilometers.</li>
      </ul>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q011/bangar_fig2_3_2_4_wind_transport.png" alt="K.M. Bangar Wind Transport and Sand Dunes">
        <div class="tb-caption">
          <strong>Figure 11.1: Mechanics of Barchan Dune Migration (K.M. Bangar, p. 23).</strong> Plan and cross-sectional views of a barchan dune illustrating the gentle windward stoss slope ($10^\\circ - 15^\\circ$), the steep lee slip-face ($32^\\circ - 34^\\circ$ angle of repose), and the two horns pointing downwind along the transverse crest axis.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q011/boggs_fig8_17_barchan_transverse_dunes.png" alt="Sam Boggs Jr Classification of Aeolian Dunes">
        <div class="tb-caption">
          <strong>Figure 11.2: Global Aeolian Dune Classification (Sam Boggs Jr., Fig. 8.17).</strong> Relationship between wind variability, sand supply, and dune morphology, contrasting transverse/barchan dunes (unidirectional wind) with longitudinal seif dunes and multi-directional star dunes.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Matrix: Dune Types vs. Wind Direction Orientation</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Dune Type</th>
            <th>Crest / Long Axis Orientation</th>
            <th>Planform Morphology</th>
            <th>Sand Supply & Wind Regime</th>
            <th>Slip Face Orientation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Barchan</strong></td>
            <td><strong>Transverse ($90^\\circ$ to wind)</strong></td>
            <td>Crescent-shaped; convex stoss, horns pointing downwind</td>
            <td>Limited sand supply; hard bedrock/gravel floor; unidirectional wind</td>
            <td>Downwind concave slip face ($32^\\circ - 34^\\circ$)</td>
          </tr>
          <tr>
            <td><strong>Transverse Ridge</strong></td>
            <td><strong>Transverse ($90^\\circ$ to wind)</strong></td>
            <td>Continuous linear or wavy asymmetric sand ridges</td>
            <td>Abundant, unlimited sand supply; unidirectional wind</td>
            <td>Single continuous downwind slip face</td>
          </tr>
          <tr>
            <td><strong>Longitudinal Dune (Seif)</strong></td>
            <td><strong>Parallel (Long axis parallel to wind)</strong></td>
            <td>Linear, sharp-crested sand ridges (sand ridges)</td>
            <td>Moderate sand supply; bidirectional converging winds</td>
            <td>Two alternating slip faces on opposing flanks</td>
          </tr>
          <tr>
            <td><strong>Parabolic Dune</strong></td>
            <td>Transverse (Curvilinear)</td>
            <td>U- or V-shaped; convex downwind, horns pointing upwind</td>
            <td>Partially vegetated; coastal or semi-arid deflation blowouts</td>
            <td>Downwind convex slip face; vegetated arms</td>
          </tr>
          <tr>
            <td><strong>Star Dune</strong></td>
            <td>Multi-directional (Radiating arms)</td>
            <td>Pyramidal peak with 3 or more radiating sinuous arms</td>
            <td>Abundant sand; multidirectional complex wind regimes</td>
            <td>Multiple steep slip faces facing diverse directions</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q11_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 11)</div>
    <div class="q-stmt">
      11. A sand dune with its long axis transverse to wind direction is called :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Longitudinal dune</div>
      <div class="raw-opt">(B) Sand ridge</div>
      <div class="raw-opt">(C) Parallel dune</div>
      <div class="raw-opt correct">(D) Barchan &nbsp;✔</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) Barchan</div>
      <div class="sub">
        In physical geology and aeolian geomorphology (K.M. Bangar, p. 23; Sam Boggs Jr., p. 270; McKee, 1979), a <strong>barchan</strong> is defined as a crescentic sand dune whose long ridge crest is oriented <strong>transverse (perpendicular) to the prevailing wind direction</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Longitudinal dune</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A longitudinal dune (seif) is defined by its long crest axis extending <em>parallel</em> to the resultant prevailing wind direction, not transverse to it. They develop under bidirectional wind systems and can extend linearly for scores of kilometers.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Sand ridge</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A sand ridge is a synonym for longitudinal or seif dunes (e.g., the vast sand ridges of the Simpson and Great Sandy Deserts in Australia), where continuous parallel ridges run parallel to the wind corridors.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Parallel dune</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> "Parallel dune" is another descriptive term for longitudinal dunes whose elongate axes run parallel to the prevailing wind streamlines, the exact antithesis of a transverse dune.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) Barchan</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Among the choices provided, the <strong>barchan</strong> is the only dune whose primary long crest axis is oriented <strong>transverse (perpendicular)</strong> to the wind direction. Wind blows against its convex back, saltating sand up to the crest, where it avalanches down the transverse lee slip face, while the lateral wings are dragged forward into downwind horns.
    </div>
  </div>
"""

q11_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Kinematics of Barchan Migration: Bagnold's Equation</div>
    <div class="card-body">
      <p>The forward migration velocity ($C$) of a barchan dune is inversely proportional to its height ($H$):</p>
      $$C = \\frac{q}{\\gamma_b \\cdot H}$$
      <p>where $q$ is the sand transport rate ($\\text{kg}/\\text{m}\\cdot\\text{s}$) and $\\gamma_b$ is the bulk unit weight of sand. Because the lateral flanks and horns of a barchan are much lower in height than the central dune crest ($H_{\\text{horns}} \\ll H_{\\text{center}}$), the horns migrate forward substantially faster than the thick central body. This differential migration velocity is what generates and maintains the classic crescent shape with horns pointing downwind.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A small desert barchan dune has a crest height $H = 4.0\\text{ m}$. In a given wind storm season, the measured volumetric sand flux across the crest is $Q_s = 24.0\\text{ m}^3/\\text{m}\\cdot\\text{year}$. Calculate the annual migration distance of the dune.
          <div class="pq-ans">✔ Worked Answer: Migration velocity $C = 6.0\\text{ meters/year}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Using Bagnold's kinematic dune migration formula:<br>
            $$C = \\frac{Q_s}{H} = \\frac{24.0\\text{ m}^3/\\text{m}\\cdot\\text{year}}{4.0\\text{ m}} = 6.0\\text{ m/year}$$<br>
            If the dune were $12.0\\text{ m}$ high, its migration rate would slow to $C = 24.0 / 12.0 = 2.0\\text{ m/year}$.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Why do the horns of a Barchan dune point in the direction of the wind, whereas the horns of a Parabolic dune point against the wind?
          <div class="pq-ans">✔ Correct Answer: In barchans, the lower horns migrate faster downwind than the high central crest; in parabolic dunes, vegetation anchors the horns while the blowout center migrates downwind.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Vegetation along coastal margins physically stabilizes the arms of parabolic dunes, allowing the unanchored central sand mass to be blown out downwind.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What internal sedimentary structure uniquely diagnoses ancient aeolian sandstones in the stratigraphic rock record?
          <div class="pq-ans">✔ Correct Answer: Giant, high-angle ($>25^\\circ - 34^\\circ$) tabular and wedge-planar cross-bedding sets with grainfall and grainflow laminae.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sand avalanching down dune slip faces forms cross-bed sets that can reach tens of meters in thickness (e.g., Navajo Sandstone), showing inverse grading within grainflow avalanches.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In what type of desert surface do isolated Barchans typically form?
          <div class="pq-ans">✔ Correct Answer: Over hard, rocky or gravelly desert floors (reg/serir) with limited sand availability and a constant unidirectional wind regime.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When sand is scarce, sand grains cannot cover the entire surface, forming discrete migrating crescent dunes over the hard bedrock/pavement floor.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "draa"?
          <div class="pq-ans">✔ Correct Answer: A mega-dune bedform with wavelengths exceeding $500\\text{ m}$ to several kilometers and heights up to hundreds of meters, upon which smaller dunes are superposed.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Wilson (1972) classified aeolian bedforms into a hierarchical spectrum: ripples (wavelength cm), dunes (wavelength meters to tens of meters), and draas (wavelength kilometers).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What wind condition produces "Star Dunes" with pyramidal summits?
          <div class="pq-ans">✔ Correct Answer: Complex, multidirectional wind regimes where winds blow from three or more distinct directions during different seasons.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Star dunes do not migrate laterally; instead, they grow vertically as sand is blown into the central summit from opposing directions, reaching heights over $300 - 400\\text{ m}$.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is the difference between "grainfall" and "grainflow" (sand avalanche) deposition on a dune slip face?
          <div class="pq-ans">✔ Correct Answer: Grainfall is the settling of saltating grains from suspension in the flow separation zone; grainflow is gravitational shearing and avalanching when oversteepened past the angle of repose.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Grainflow deposits display diagnostic inverse grading (coarse grains rise to the top of the shearing avalanche tongue due to kinetic sieving).
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a "barchanoid ridge"?
          <div class="pq-ans">✔ Correct Answer: A continuous wavy, sinuous transverse sand ridge formed by the lateral coalescence of multiple individual barchan dunes under increasing sand supply.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> As sand supply increases, isolated barchans merge side-by-side, forming a sinuous transverse ridge with alternating crests and troughs.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=11,
    filename="Q011_Sand_Dune_Barchan_Transverse_Axis_Complete_Guide.html",
    title="Q011: Sand Dune Morphology, Barchans & Transverse vs. Longitudinal Kinematics",
    badge="GGM - 2/2019 • Aeolian Geomorphology & Sedimentology",
    h1_title="Q011: Morphodynamic Classification of Sand Dunes: Barchans & Transverse Kinematics",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 11<br><strong>Authoritative References:</strong> Ralph A. Bagnold (<em>The Physics of Blown Sand</em>, 1941); K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 23); Edwin D. McKee (<em>Global Sand Seas</em>, USGS Prof. Paper 1052)",
    part1_html=q11_part1,
    part2_html=q11_part2,
    part3_html=q11_part3
)

# ==========================================
# QUESTION 12: ESKER - GLACIOFLUVIAL DEPOSIT
# ==========================================
q12_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Subglacial Hydrology & Morphogenesis of Eskers</div>
    <div class="card-body">
      <p>An <strong>esker</strong> (derived from the Irish word <em>eiscir</em>, meaning a ridge or elevation) is a long, narrow, winding, steep-sided ridge composed of stratified, cross-bedded sand and gravel deposited by a subglacial, englacial, or proglacial meltwater stream flowing under hydrostatic pressure through an ice-walled tunnel within or beneath a melting or stagnant glacier. Genetically and lithologically, an esker is a classic and definitive <strong>glaciofluvial (fluvioglacial) deposit</strong>.</p>

      <div class="quote-box bangar">
        "Eskers are long, narrow, sinuous ridges of stratified sands and gravels deposited by subglacial streams flowing in tunnels beneath the melting ice. When the surrounding glacier melts away, these stream-bed deposits are left behind on the ground surface as winding, snake-like ridges that often run for miles across the landscape. They represent important <strong>glaciofluvial deposits</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Glacial Landforms: Fluvioglacial Deposits, p. 32)</span>
      </div>

      <p>Eskers are distinguished by several extraordinary hydrological and morphological characteristics:</p>
      <ul>
        <li><strong>Subglacial Pressurized Pipe Flow (R-Channels):</strong> Subglacial meltwater streams flow through semicircular tunnels melted upward into the basal ice, termed <em>Röthlisberger channels (R-channels)</em>. Because water is confined under immense glaciostatic overburden pressure ($P_w \\approx \\rho_i g H$), it flows at high velocities ($>1 - 3\\text{ m/s}$) and can even flow <strong>uphill</strong> across bedrock ridges, driven by the hydraulic gradient of the overlying ice surface slope!</li>
        <li><strong>Stratification & Sorting:</strong> Unlike true glacial till (which is unsorted and unstratified), esker sediments are <strong>water-laid, stratified, and well-sorted</strong>. They exhibit prominent climbing ripples, planar and trough cross-bedding, and imbricated gravel clasts.</li>
        <li><strong>Post-Depositional Collapse Faulting:</strong> When the confining ice walls melt away, lateral lateral support is removed, causing the flanks of the esker ridge to slump downward along normal gravity faults to attain the natural subaerial angle of repose of sand and gravel ($30^\\circ - 35^\\circ$).</li>
        <li><strong>Scale & Continuity:</strong> Eskers range from a few meters to over $40 - 50\\text{ meters}$ in height, $50 - 200\\text{ meters}$ in width, and can extend as segmented beaded ridges for tens to hundreds of kilometers (e.g., the Munro Esker in Ontario, Canada, extends $>250\\text{ km}$).</li>
      </ul>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q012/bangar_p32_esker_glaciofluvial.png" alt="K.M. Bangar Eskers and Fluvioglacial Deposits">
        <div class="tb-caption">
          <strong>Figure 12.1: Esker Formation and Glaciofluvial Deposition (K.M. Bangar, p. 32).</strong> Block diagram illustrating a subglacial meltwater river flowing through an ice tunnel beneath stagnant ice, depositing stratified gravels that become a sinuous esker ridge upon ice retreat.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q012/boggs_fig8_32_esker_subglacial_tunnel.png" alt="Sam Boggs Jr Glaciofluvial Subglacial Depositional Systems">
        <div class="tb-caption">
          <strong>Figure 12.2: Glaciofluvial Landform Assemblage (Sam Boggs Jr., Fig. 8.32).</strong> Comparative spatial distribution of subglacial eskers, ice-marginal kames, proglacial outwash plains (sandurs), and kettle lakes.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Glacial Sedimentary Taxonomy: Till vs. Glaciofluvial vs. Glaciolacustrine</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Deposit Category</th>
            <th>Primary Depositional Medium</th>
            <th>Sedimentary Structure</th>
            <th>Grain Size & Sorting</th>
            <th>Diagnostic Landforms</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Glacial Till (Moraine)</strong></td>
            <td>Direct passive melting / lodgement from <strong>ice</strong></td>
            <td>Unstratified, structureless diamicton</td>
            <td>Extremely poorly sorted (Clay to giant erratic boulders)</td>
            <td>Terminal moraines, lateral moraines, drumlins</td>
          </tr>
          <tr>
            <td><strong>Glaciofluvial Drift</strong></td>
            <td>Glacial <strong>meltwater streams</strong></td>
            <td>Stratified, cross-bedded, imbricated</td>
            <td>Moderately to well-sorted gravel and sand</td>
            <td><strong>Eskers</strong>, kames, kame terraces, outwash plains (sandurs)</td>
          </tr>
          <tr>
            <td><strong>Glaciolacustrine Deposit</strong></td>
            <td>Standing <strong>glacial lake water</strong></td>
            <td>Rhythmically laminated varves</td>
            <td>Fine silt and clay couplets with dropstones</td>
            <td>Proglacial lake plains, deltas, varved clay beds</td>
          </tr>
          <tr>
            <td><strong>Glaciomarine Drift</strong></td>
            <td>Floating shelf ice / Icebergs in the <strong>sea</strong></td>
            <td>Massive mud with isolated dropstones</td>
            <td>Marine muds with ice-rafted debris (IRD)</td>
            <td>Submarine morainal banks, glaciomarine fan complexes</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q12_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 12)</div>
    <div class="q-stmt">
      12. Esker is a :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Thoroughly graded bed</div>
      <div class="raw-opt">(B) Deposit formed by wind action</div>
      <div class="raw-opt correct">(C) Glaciofluvial deposit &nbsp;✔</div>
      <div class="raw-opt">(D) Alluvial deposit rich in clay matter</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Glaciofluvial deposit</div>
      <div class="sub">
        In glacial sedimentology and geomorphology (K.M. Bangar, p. 32; Sam Boggs Jr., p. 280; Arthur L. Bloom, p. 396; Benn & Evans, 2010), an <strong>esker</strong> is universally classified as a stratified, meltwater-laid <strong>Glaciofluvial (fluvioglacial) deposit</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Thoroughly graded bed</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Graded beds (where grain size fines systematically upward from coarse sand to fine clay) are classic deposits of subaqueous turbidity currents (turbidites, Bouma sequence $T_a$ division) in deep marine or lacustrine basins. Eskers are characterized by cross-bedding and gravel lenses formed by pulsating meltwater streams, not thoroughly graded beds.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Deposit formed by wind action</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Deposits formed by wind action (aeolian deposits) include sand dunes, sand sheets, and loess blankets. Eskers are high-energy fluvial gravel and sand deposits formed beneath glacial ice sheets, having no connection to wind transport.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Glaciofluvial deposit</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> An esker is the definitive geological manifestation of a <strong>glaciofluvial deposit</strong>. It consists of sorted and stratified sand and gravel deposited by flowing meltwater streams confined within subglacial or englacial ice tunnels.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Alluvial deposit rich in clay matter</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Alluvial deposits rich in clay are floodplain overbank silts, oxbow lake plugs, or backswamp muds. Eskers are coarse, highly permeable bedload deposits dominated by gravel, pebbles, and coarse-to-medium sand; fine clay is washed away down-ice into proglacial lakes by vigorous meltwater flow.
    </div>
  </div>
"""

q12_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Engineering & Economic Significance of Glaciofluvial Eskers</div>
    <div class="card-body">
      <p>Eskers are of enormous economic and civil engineering importance in glaciated shield terrains (e.g., Canada, Scandinavia, northern USA):</p>
      <ul>
        <li><strong>Prime Aggregate Source:</strong> Esker sands and gravels are naturally washed, sorted, and free of deleterious organic clays, making them the premier source of coarse aggregate for concrete production, asphalt paving, and railway ballast.</li>
        <li><strong>Artesian Groundwater Aquifers:</strong> Due to extremely high hydraulic conductivity ($K > 10^{-3} - 10^{-2}\\text{ m/s}$), eskers buried beneath impermeable glacial clays form exceptionally prolific regional artesian aquifers.</li>
        <li><strong>Natural Highway & Railway Corridors:</strong> Because eskers are elevated, well-drained, porous ridges rising above wet, swampy muskeg and peat bogs in subarctic terrains, early pioneers and modern highway engineers utilize them as natural, elevated foundation routes for roads and railways.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What hydraulic condition allows subglacial meltwater streams to flow uphill over bedrock topographic divides, depositing eskers that cross mountain ridges?
          <div class="pq-ans">✔ Correct Answer: Pipe flow under hydrostatic pressure governed by the hydraulic gradient of the sloping upper surface of the ice sheet.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Water in subglacial R-channels is pressurized by the weight of the ice. The hydraulic potential $\\Phi = z + \\frac{P_w}{\\rho_w g}$ is determined by the ice surface slope (which is $\\approx 11\\times$ more influential than bedrock bed slope), forcing water to flow uphill over subglacial hills.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Distinguish between an "Esker" and a "Kame".
          <div class="pq-ans">✔ Correct Answer: An esker is a linear, sinuous ridge deposited in a subglacial channel; a kame is an isolated mound or conical hill deposited in an ice-surface crevasse or moulin delta.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Both are glaciofluvial, but eskers represent continuous stream-bed conduits, whereas kames represent localized pond or moulin delta accumulations.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What sedimentary structure is commonly observed on the flanking margins of an esker, and what causes it?
          <div class="pq-ans">✔ Correct Answer: Gravity-induced normal faults and slumping with dipping beds, caused by the melting of supporting lateral ice walls.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When the ice tunnel walls melt away, lateral confining stress is lost, causing the gravel layers along the sides to collapse downward to the natural angle of repose.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is a "beaded esker"?
          <div class="pq-ans">✔ Correct Answer: An esker consisting of a chain of periodic, bulbous mounds or beads connected by narrow ridges, reflecting annual pulses of sediment deposition at a retreating subglacial portal.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> De Geer (1897) demonstrated that each bead represents a summer meltwater fan deposited where the tunnel exited into a proglacial lake, recording annual ice-front retreat rates.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Why are eskers predominantly formed during periods of glacial stagnation or retreat rather than during active glacial advance?
          <div class="pq-ans">✔ Correct Answer: Active advancing ice shears, deforms, and destroys delicate subglacial sediment tunnels; preservation requires stagnant or retreating ice.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> If the glacier is actively flowing rapidly, basal shear stresses crush and disperse tunnel deposits into till. Eskers survive when ice becomes dynamically stagnant ($v \\approx 0$) during deglaciation.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What paleocurrent feature in an esker reveals the direction of subglacial meltwater flow?
          <div class="pq-ans">✔ Correct Answer: Cross-bedding foreset dip directions and upstream pebble imbrication ($a(p)b(i)$ fabrics).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Fluvial cross-bedding dips down-current, while flat pebbles imbricate dipping up-current into the meltwater flow.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In mineral exploration, how are eskers utilized in "drift prospecting" for diamondiferous kimberlites and gold deposits?
          <div class="pq-ans">✔ Correct Answer: Heavy mineral sampling of esker gravels reveals indicator minerals (pyrope garnet, chromite, gold grains) that can be traced upstream to source kimberlite pipes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Subglacial streams wash vast volumes of basal till, concentrating resistant heavy indicator minerals within the esker gravel matrix.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a "Sandur", and how does it relate genetically to an esker?
          <div class="pq-ans">✔ Correct Answer: A sandur is a broad proglacial outwash plain formed where meltwater streams emerging from subglacial tunnels (eskers) discharge and spread over open land.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Eskers represent the feeder channels within the ice; sandurs represent the unconfined braided alluvial fans deposited beyond the ice terminus.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=12,
    filename="Q012_Esker_Glaciofluvial_Deposit_Complete_Guide.html",
    title="Q012: Eskers, Glaciofluvial Sedimentary Architecture & Subglacial Hydrology",
    badge="GGM - 2/2019 • Glacial Geology & Fluvial Hydrology",
    h1_title="Q012: Morphogenesis of Eskers: Subglacial Pressurized Flow & Glaciofluvial Drift",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 12<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 32); Sam Boggs Jr. (<em>Sedimentology & Stratigraphy</em>, Ch. 8, pp. 280–285); Benn & Evans (<em>Glaciers and Glaciation</em>, 2010)",
    part1_html=q12_part1,
    part2_html=q12_part2,
    part3_html=q12_part3
)

# ==========================================
# QUESTION 13: STALACTITES & STALAGMITES - SOLUTION ACTIVITY
# ==========================================
q13_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Hydrochemical Genesis of Speleothems via Solution Activity</div>
    <div class="card-body">
      <p><strong>Stalactites</strong> and <strong>stalagmites</strong> are secondary cave mineral formations (collectively termed <strong>speleothems</strong>) that originate fundamentally from the <strong>solution activity</strong> of circulating groundwater in soluble carbonate rock formations (limestone and dolostone). Their formation represents a two-stage hydrochemical cycle: (1) subsurface chemical dissolution of calcium carbonate by aggressive carbonic acid, followed by (2) subterranean precipitation of crystalline calcite in aerated cave chambers due to carbon dioxide degassing.</p>

      <div class="quote-box bangar">
        "Groundwater charged with atmospheric and soil carbon dioxide acts as a weak acid ($\text{H}_2\text{CO}_3$) that dissolves limestone along joints, enlarging them into extensive subterranean caverns (solution activity). When this calcium bicarbonate-rich water trickles into cave chambers, carbon dioxide escapes into the cave atmosphere, causing calcium carbonate to precipitate. The icicle-like forms hanging from the cave ceiling are called <strong>stalactites</strong>, while the pillars growing upward from the floor are called <strong>stalagmites</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Work of Groundwater: Solution Activity, p. 38)</span>
      </div>

      <p>The reversible thermodynamic reaction governing speleothem development is:</p>

      <div class="formula-card">
        <div class="formula-title">Reversible Carbonate Dissolution-Precipitation Equilibrium</div>
        $$\\text{CaCO}_3\\text{ (calcite)} + \\text{CO}_2 + \\text{H}_2\\text{O} \\underset{\\text{Precipitation (Degassing)}}{\\overset{\\text{Dissolution (Solution)}}{\\rightleftharpoons}} \\text{Ca}^{2+} + 2\\text{HCO}_3^-$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;"><strong>Stage 1 (Dissolution / Solution Activity):</strong> In the soil zone, biogenic respiration drives soil $p\\text{CO}_2$ up to $10 - 100\\times$ atmospheric levels, shifting the reaction to the <strong>right</strong> and dissolving limestone.<br>
        <strong>Stage 2 (Precipitation / Speleothem Growth):</strong> Upon entering a ventilated cave with lower ambient $p\\text{CO}_2$ ($0.04 - 0.1\\%$), $\\text{CO}_2$ spontaneously degasses from the dripping water droplet into cave air, shifting the reaction to the <strong>left</strong> and depositing pure crystalline calcite ($\text{CaCO}_3$).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q013/bangar_p38_stalactite_stalagmite_solution.png" alt="K.M. Bangar Stalactites Stalagmites Solution Activity">
        <div class="tb-caption">
          <strong>Figure 13.1: Solution Activity & Speleothem Architecture (K.M. Bangar, p. 38).</strong> Cross-section of a karst cavern depicting joint enlargement by solution activity, dripping vadose water, hollow cylindrical stalactites hanging from the ceiling, solid massive stalagmites growing from the floor, and coalesced columns.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Morphological Comparison: Stalactite vs. Stalagmite vs. Column</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>Growth Direction</th>
            <th>Internal Structure</th>
            <th>Precipitation Dynamics</th>
            <th>Physical Morphology</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Stalactite</strong></td>
            <td><strong>Downward</strong> from cave ceiling</td>
            <td>Hollow central tube ("soda straw") with radial crystals</td>
            <td>Degassing from hanging water droplet before detachment</td>
            <td>Slender, tapering icicle-like cones; delicate straws</td>
          </tr>
          <tr>
            <td><strong>Stalagmite</strong></td>
            <td><strong>Upward</strong> from cave floor</td>
            <td>Solid, layered; completely lacks central canal</td>
            <td>Degassing and mechanical splashing of fallen droplets</td>
            <td>Broad-based, flat-topped or domed solid pillars</td>
          </tr>
          <tr>
            <td><strong>Pillar / Column</strong></td>
            <td>Continuous vertical column</td>
            <td>Merged concentric and radial crystalline fabric</td>
            <td>Full union of descending stalactite and ascending stalagmite</td>
            <td>Massive structural pillar connecting floor to ceiling</td>
          </tr>
          <tr>
            <td><strong>Helictite</strong></td>
            <td>Arbitrary / Gravity-defying</td>
            <td>Microscopic capillary canal ($<0.05\\text{ mm}$)</td>
            <td>Slow seepage dominated by crystal lattice growth and capillary forces</td>
            <td>Twisted, worm-like branching filaments</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q13_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 13)</div>
    <div class="q-stmt">
      13. Development of stalactite and stalagmite is associated with :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Abrasion of valley floor</div>
      <div class="raw-opt correct">(B) Solution activity &nbsp;✔</div>
      <div class="raw-opt">(C) Sorting process</div>
      <div class="raw-opt">(D) Organic activity in ocean beds</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Solution activity</div>
      <div class="sub">
        In hydrogeology and karst geomorphology (K.M. Bangar, p. 38; Arthur L. Bloom, p. 156; Derek Ford & Paul Williams, 2007), the development of stalactites and stalagmites is fundamentally driven by the <strong>solution activity</strong> (groundwater chemical dissolution and subsequent carbonate precipitation) in limestone caverns.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Abrasion of valley floor</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Abrasion of a valley floor is a mechanical fluvial process where stream bedload (sand, pebbles) scours and polishes bedrock, forming potholes, flutes, and longitudinal grooves. It has no connection to chemical cave precipitation.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Solution activity</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Stalactites and stalagmites are the direct chemical products of groundwater <strong>solution activity</strong>. Acidic groundwater charged with carbonic acid dissolves calcium carbonate along bedrock joints, and upon dripping into cave atmospheres, carbon dioxide degassing reprecipitates the dissolved mineral as speleothems.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Sorting process</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The sorting process is a physical, hydrodynamic mechanism where flowing water or wind separates clastic sediment grains based on size, density, and settling velocity (e.g., in beach sands or braided rivers). Speleothems grow through chemical solute precipitation, not physical grain sorting.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Organic activity in ocean beds</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Organic activity in ocean beds produces biogenic carbonate rocks such as coral reefs, foraminiferal oozes, and chalk. Stalactites and stalagmites develop subaerially in inland terrestrial caves via inorganic degassing of meteoric groundwater, not in ocean beds.
    </div>
  </div>
"""

q13_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Paleoclimate Proxy Records in Speleothem Growth Rings</div>
    <div class="card-body">
      <p>In modern paleoclimatology, stalagmites provide ultra-high-resolution terrestrial paleoclimate records spanning hundreds of thousands of years:</p>
      <ul>
        <li><strong>Uranium-Thorium ($^{238}\\text{U} - ^{234}\\text{U} - ^{230}\\text{Th}$) Geochronology:</strong> Because calcite incorporates trace soluble uranium ($U^{6+}$) upon precipitation while excluding insoluble thorium ($Th^{4+}$), decay of uranium to $^{230}\\text{Th}$ provides precise absolute radiometric dates with sub-centennial accuracy back to $500,000\\text{ years}$.</li>
        <li><strong>Stable Oxygen Isotopes ($\\delta^{18}\\text{O}$):</strong> Serves as an exquisite proxy for paleomonsoon intensity and rainfall amount (the "amount effect"). Depleted $\\delta^{18}\\text{O}$ values in stalagmite calcite bands reflect intense Indian Summer Monsoon (ISM) rainfall regimes.</li>
        <li><strong>Trace Element Ratios ($Mg/Ca, Sr/Ca$):</strong> High $Mg/Ca$ ratios indicate Prior Calcite Precipitation (PCP) during severe surface droughts, as calcite precipitates along fractures before reaching the cave chamber.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> Why does a "soda straw" stalactite possess a constant internal diameter of approximately $5\\text{ millimeters}$ regardless of its length?
          <div class="pq-ans">✔ Correct Answer: The diameter is physically dictated by the surface tension and capillary meniscus size of a hanging water droplet before detachment.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Water drips through the central lumen; as each drop hangs, degassing precipitates a microscopic ring of calcite around the droplet's circular contact meniscus ($\approx 5\text{ mm}$ for water).
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What geochemical mechanism drives the precipitation of calcite in a cave chamber: temperature change, evaporation, or $\text{CO}_2$ degassing?
          <div class="pq-ans">✔ Correct Answer: Carbon dioxide ($\text{CO}_2$) degassing is the primary thermodynamic driver; evaporation plays a minor secondary role.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Caves maintain high relative humidity ($\approx 95 - 100\%$), preventing significant evaporation. Calcite precipitates because cave air has lower $p\text{CO}_2$ than soil water, forcing $\text{CO}_2$ to escape the droplet into cave air.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What mineral polymorphic form of $\text{CaCO}_3$ occasionally precipitates in warm cave environments instead of calcite?
          <div class="pq-ans">✔ Correct Answer: Aragonite (orthorhombic $\text{CaCO}_3$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In the presence of elevated dissolved magnesium ($Mg^{2+}$) concentrations, the precipitation of calcite is kinetically poisoned, favoring metastable needle-like aragonite (anthodites/cave flowers).
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is "flowstone", and how does its growth differ from stalactites and stalagmites?
          <div class="pq-ans">✔ Correct Answer: Sheet-like or drapery-like calcite deposits formed by thin sheets of water flowing down cave walls or across cave floors.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Stalactites/stalagmites form from discrete drips; flowstone forms from continuous laminar sheetwash over rock surfaces, creating "frozen waterfalls".
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How do "cave pearls" form in karst pools?
          <div class="pq-ans">✔ Correct Answer: Concentric precipitation of calcite around a grain nucleus (sand or bone) agitated by dripping water in shallow splash cups.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Constant mechanical agitation by falling drips prevents the pearl from adhering to the pool floor, allowing symmetrical concentric spherical growth.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What gives stalactites and stalagmites red, amber, or brown coloration?
          <div class="pq-ans">✔ Correct Answer: Trace impurities of iron oxides (hematite, goethite) or soil humic and fulvic acids flushed from overlying organic soils.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Pure calcite speleothems are translucent white; soil weathering products impart reddish-brown banded colorations.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In paleoclimatology, why are stalagmites preferred over stalactites for proxy time-series reconstruction?
          <div class="pq-ans">✔ Correct Answer: Stalagmites grow continuously upward with simple, undisturbed layer-cake stratigraphy and lack an open central feeding tube prone to internal dissolution.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The flat, solid growth caps of stalagmites provide clean, chronological stratigraphic sequences for micro-drilling and radiometric dating.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why is touching a living stalactite or stalagmite strictly prohibited in speleological conservation?
          <div class="pq-ans">✔ Correct Answer: Human skin oils leave a hydrophobic greasy film that prevents aqueous droplets from adhering and halts calcite crystallization.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The thin lipid layer repels water, permanently terminating the natural growth of the speleothem at the touched spot.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=13,
    filename="Q013_Stalactite_Stalagmite_Solution_Activity_Complete_Guide.html",
    title="Q013: Speleothems, Stalactites, Stalagmites & Karst Solution Dynamics",
    badge="GGM - 2/2019 • Hydrogeology & Karst Geomorphology",
    h1_title="Q013: Chemical Genesis of Speleothems: Solution Activity & Calcite Precipitation",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 13<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 38); Derek Ford & Paul Williams (<em>Karst Hydrogeology and Geomorphology</em>, 2007); Arthur L. Bloom (<em>Geomorphology</em>, Ch. 7)",
    part1_html=q13_part1,
    part2_html=q13_part2,
    part3_html=q13_part3
)

# ==========================================
# QUESTION 14: MASS WASTING - FORCE OF GRAVITY
# ==========================================
q14_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Mechanics of Slope Stability & Gravitational Driving Forces</div>
    <div class="card-body">
      <p><strong>Mass wasting</strong> (or <strong>mass movement</strong>) is the comprehensive geological term defining the downslope movement of rock, regolith, soil, or debris under the <strong>direct driving influence of the force of gravity</strong>, without requiring the dynamic kinetic transport of a fluid medium (such as running water, glacial ice, or wind) to carry the particles in suspension or traction.</p>

      <div class="quote-box bangar">
        "Mass movement or mass wasting is the term applied to the movement of rock fragments and soil down a slope under the direct influence of <strong>gravity</strong>. It includes movements of all kinds—from the slow, imperceptible downhill creep of soil to catastrophic rockfalls and landslides. Gravity is the fundamental driving force behind all mass wasting."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Chapter 10: Mass Movements, p. 377)</span>
      </div>

      <p>The mechanics of slope stability under gravity are formalized via the <strong>Limit Equilibrium Principle</strong> and the <strong>Mohr-Coulomb Failure Criterion</strong>:</p>

      <div class="formula-card">
        <div class="formula-title">Gravitational Stress Resolution on an Inclined Slope (Terzaghi, 1943)</div>
        $$W = m \\cdot g = \\gamma \\cdot V \\quad (\\text{Total Weight of Sliding Mass})$$
        $$\\text{Driving Shear Force } T = W \\cdot \\sin \\alpha$$
        $$\\text{Normal Force } N = W \\cdot \\cos \\alpha$$
        $$\\text{Factor of Safety } FS = \\frac{\\text{Resisting Shear Strength } R}{\\text{Driving Shear Force } T} = \\frac{c' \\cdot A + (W \\cos \\alpha - u \\cdot A) \\tan \\phi'}{W \\sin \\alpha}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $\\alpha$ is slope inclination, $c'$ is effective cohesion, $\\phi'$ is effective internal friction angle, $u$ is pore water pressure, and $A$ is failure plane area. Slope failure occurs when gravity causes $FS < 1.0$.</p>
      </div>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q014/bangar_p378_mass_wasting_gravity.png" alt="K.M. Bangar Verbatim Definition of Mass Wasting and Landslides">
        <div class="tb-caption">
          <strong>Figure 14.1: Landslide and Mass Movement Dynamics (K.M. Bangar, p. 378).</strong> Photographic scan illustrating classical landslide shear failure, rotational slumping along curved shear planes, and rock block glides driven by gravitational shear stress.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q014/mass_wasting_gravity_shear_plane.png" alt="Gravitational Resolution of Forces on a Slope">
        <div class="tb-caption">
          <strong>Figure 14.2: Gravitational Force Vector Decomposition.</strong> Resolution of the vertical gravitational body weight vector ($W = mg$) into a downslope driving shear component ($T = W \\sin \\alpha$) and a perpendicular normal component ($N = W \\cos \\alpha$).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Spectrum of Mass Wasting Processes (Varnes, 1978; Cruden & Varnes, 1996)</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Type of Movement</th>
            <th>Kinematic Mechanism</th>
            <th>Primary Material</th>
            <th>Velocity Range</th>
            <th>Gravitational Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fall (Rockfall)</strong></td>
            <td>Free-fall, bouncing, rolling through air</td>
            <td>Bedrock blocks, boulders</td>
            <td>Catastrophic ($>30\\text{ m/s}$)</td>
            <td>Direct unhindered gravitational free-fall ($g = 9.81\\text{ m/s}^2$)</td>
          </tr>
          <tr>
            <td><strong>Topple</strong></td>
            <td>Forward rotation about a basal pivot</td>
            <td>Columnar basalt, vertical joint blocks</td>
            <td>Fast to slow</td>
            <td>Overturning gravitational moment</td>
          </tr>
          <tr>
            <td><strong>Slide (Rotational Slump)</strong></td>
            <td>Shear displacement along concave slip surface</td>
            <td>Homogeneous cohesive clay/shale</td>
            <td>Meters/day to meters/hour</td>
            <td>Driving shear torque along curved shear plane</td>
          </tr>
          <tr>
            <td><strong>Slide (Translational Glide)</strong></td>
            <td>Planar sliding along bedding/fault plane</td>
            <td>Layered sedimentary / foliated rocks</td>
            <td>Meters/second (Rapid)</td>
            <td>Driving force $T = W \\sin \\alpha$ exceeding shear strength</td>
          </tr>
          <tr>
            <td><strong>Flow (Debris / Mudflow)</strong></td>
            <td>Viscous fluid shearing throughout mass</td>
            <td>Water-saturated soil and debris</td>
            <td>$0.5\\text{ m/s}$ to $15\\text{ m/s}$</td>
            <td>Gravitational slurry flow down drainage channels</td>
          </tr>
          <tr>
            <td><strong>Creep (Soil Creep)</strong></td>
            <td>Extremely slow, continuous internal shear strain</td>
            <td>Topsoil, regolith, weathered mantle</td>
            <td>$<1 - 10\\text{ mm/year}$</td>
            <td>Cyclic expansion-contraction ratcheting downhill under gravity</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q14_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 14)</div>
    <div class="q-stmt">
      14. Mass wasting is primarily affected by :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Force of gravity &nbsp;✔</div>
      <div class="raw-opt">(B) Intensity of oxidation</div>
      <div class="raw-opt">(C) Intensity of carbonization</div>
      <div class="raw-opt">(D) Strength of streams</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Force of gravity</div>
      <div class="sub">
        In engineering geology and geomorphology (K.M. Bangar, p. 377; Arthur Holmes, p. 347; Varnes, 1978; Bloom, p. 165), <strong>mass wasting</strong> is explicitly and fundamentally defined as the downslope movement of slope-forming materials under the <strong>direct driving influence of the force of gravity</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Force of gravity</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> The force of gravity is the primary, indispensable physical engine driving all mass wasting. Gravitational acceleration ($g$) acts upon the mass of rock and soil, resolving into a downslope driving shear component ($W \\sin \\alpha$). Whenever this driving stress exceeds the resisting shear strength of the slope, mass wasting occurs.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Intensity of oxidation</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Oxidation is a chemical weathering reaction (e.g., $4\\text{Fe}^{2+} + 3\\text{O}_2 \\to 2\\text{Fe}_2\\text{O}_3$) that alters iron-bearing silicates into rust-colored oxides. While chemical weathering can gradually weaken rock strength over millenia, it does not provide the dynamic physical driving force for mass displacement.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Intensity of carbonization</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Carbonization (or coalification / carbonation) refers either to the geochemical concentration of carbon in organic matter forming coal, or the chemical reaction of dissolved carbon dioxide with minerals. It is not the driving physical agent of downslope mass movement.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Strength of streams</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The strength of streams governs <em>fluvial erosion and transport</em>, where sediment particles are entrained within moving water. Mass wasting is fundamentally demarcated from fluvial erosion precisely because mass wasting moves under direct gravitational body force without being entrained as sediment load in a river.
    </div>
  </div>
"""

q14_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Triggering Mechanisms vs. Primary Driving Force in Mass Wasting</div>
    <div class="card-body">
      <p>It is vital to distinguish between the <strong>singular driving force (Gravity)</strong> and the transient <strong>triggering mechanisms</strong> that precipitate failure:</p>
      <ul>
        <li><strong>Rainfall & Pore Water Pressure ($u$):</strong> Water acts by reducing effective normal stress ($\\sigma' = \\sigma - u$) and lubricating shear planes; it does not replace gravity as the driving force.</li>
        <li><strong>Seismic Ground Acceleration (Earthquakes):</strong> Dynamic seismic shear waves ($k_h W$) temporarily augment gravitational driving shear stress.</li>
        <li><strong>Toe Undercutting (River or Road Excavation):</strong> Removes kinematic support at the base of the slope, leaving the upper block unsupported against gravitational collapse.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A planar rock block weighing $W = 600\\text{ kN}$ rests on a joint plane inclined at $\\alpha = 35^\\circ$. The basal contact area is $A = 25\\text{ m}^2$. The joint plane has an effective cohesion $c' = 12\\text{ kPa}$ and an internal friction angle $\\phi' = 30^\\circ$. If water pressure is zero, calculate the Factor of Safety ($FS$) against sliding.
          <div class="pq-ans">✔ Worked Answer: $FS = 1.69$ (Stable Slope).</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Driving force $T = W \\sin \\alpha = 600 \\sin 35^\\circ = 600(0.5736) = 344.15\\text{ kN}$.<br>
            Normal force $N = W \\cos \\alpha = 600 \\cos 35^\\circ = 600(0.8192) = 491.49\\text{ kN}$.<br>
            Resisting shear force $R = c' A + N \\tan \\phi'$:<br>
            $$R = (12\\text{ kPa} \\times 25\\text{ m}^2) + 491.49 \\tan 30^\\circ = 300 + 491.49(0.5774) = 300 + 283.77 = 583.77\\text{ kN}$$<br>
            $$FS = \\frac{R}{T} = \\frac{583.77}{344.15} \\approx 1.696$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What happens to the Factor of Safety ($FS$) of the slope in Q1 if heavy monsoon rains generate a pore water pressure $u = 15\\text{ kPa}$ along the joint plane?
          <div class="pq-ans">✔ Worked Answer: $FS = 1.07$ (Marginal Stability / Imminent Failure).</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Total pore water force $U = u \\times A = 15\\text{ kPa} \\times 25\\text{ m}^2 = 375\\text{ kN}$.<br>
            Effective normal force $N' = N - U = 491.49 - 375 = 116.49\\text{ kN}$.<br>
            New resisting force $R' = 300 + 116.49(0.5774) = 300 + 67.26 = 367.26\\text{ kN}$.<br>
            $$FS = \\frac{367.26}{344.15} \\approx 1.067$$
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> For a completely dry, cohesionless sand slope ($c'=0, u=0$), what is the maximum stable slope angle?
          <div class="pq-ans">✔ Correct Answer: The angle of internal friction of the sand ($\alpha_{\text{max}} = \phi'$), termed the angle of repose.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When $c'=0$, $FS = \frac{W \cos \alpha \tan \phi'}{W \sin \alpha} = \frac{\tan \phi'}{\tan \alpha}$. For $FS \ge 1.0$, $\tan \alpha \le \tan \phi' \implies \alpha \le \phi'$.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In what type of mass movement does the displaced block rotate backward toward the head scarp?
          <div class="pq-ans">✔ Correct Answer: Rotational slide (Slump).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In a rotational slump, the failure surface is curved concave-upward (spoon-shaped). As the mass slides, the center of gravity rotates, tilting trees and bedding backward into the hill.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is "solifluction", and in what climatic zone is it the dominant mass wasting agent?
          <div class="pq-ans">✔ Correct Answer: The slow downslope flow of water-saturated soil over an impermeable permafrost layer, dominant in periglacial/subarctic regions.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> During summer, the active layer thaws into a saturated slurry that cannot drain downward through the frozen permafrost, flowing slowly downslope under gravity.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What field evidence diagnoses active "soil creep" on a hillside?
          <div class="pq-ans">✔ Correct Answer: J-shaped (pistol-butted) tree trunks, tilted utility poles, displaced fences, and terracettes.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because surface soil creeps faster than subsoil, tree roots move slower than trunks, forcing trees to curve vertically toward sunlight as they grow.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In the 1963 catastrophic Vajont Dam disaster in Italy, what form of mass wasting occurred?
          <div class="pq-ans">✔ Correct Answer: A catastrophic translational rock block slide along clay interbeds, mobilizing 270 million cubic meters of rock into the reservoir.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Reservoir filling raised pore water pressure along bedding planes that dipped directly toward the valley, triggering instantaneous planar failure under gravity.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is the most cost-effective engineering stabilization measure for preventing rain-induced mass wasting?
          <div class="pq-ans">✔ Correct Answer: Subsurface drainage (horizontal drain holes and French drains) to reduce pore water pressure ($u$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Dewatering restores effective normal stress ($\sigma' = \sigma - u$) and maximizes frictional shear resistance without expensive retaining walls.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=14,
    filename="Q014_Mass_Wasting_Force_of_Gravity_Complete_Guide.html",
    title="Q014: Mass Wasting, Gravitational Mechanics & Slope Stability Derivations",
    badge="GGM - 2/2019 • Engineering Geology & Geomorphology",
    h1_title="Q014: Mechanics of Mass Wasting: Gravitational Driving Forces & Limit Equilibrium",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 14<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, pp. 377–380); Karl Terzaghi (<em>Theoretical Soil Mechanics</em>, 1943); D.J. Varnes (1978, TRB Special Report 176)",
    part1_html=q14_part1,
    part2_html=q14_part2,
    part3_html=q14_part3
)

# ==========================================
# QUESTION 15: DENDRITIC DRAINAGE - LACKING STRUCTURAL CONTROL
# ==========================================
q15_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Geomorphological Mechanics of Dendritic Drainage Networks</div>
    <div class="card-body">
      <p>A <strong>dendritic drainage pattern</strong> (derived from the Greek <em>dendron</em>, meaning tree) is an irregular, branching, tree-like stream network where tributaries join larger channels at acute angles ($<90^\\circ$). It is universally recognized as the diagnostic geomorphic signature of a geological region that is completely <strong>lacking in structural control</strong>.</p>

      <div class="quote-box bangar">
        "A dendritic drainage pattern is characterized by irregular branching of tributaries in all directions, resembling the branches of an oak or apple tree. It develops in regions where the underlying rocks are completely homogeneous, flat-lying, or massive, and exert <strong>no structural control</strong> on the direction of stream erosion (such as horizontal sedimentary beds, thick plateau basalts, or massive granitic plutons)."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Drainage Patterns & Structural Geology, p. 27)</span>
      </div>

      <p>The development of a dendritic network is governed by three primary geological conditions:</p>
      <ul>
        <li><strong>Uniform Substrate Erodibility (Isotropy):</strong> The rock or sediment exhibits equal resistance to fluvial erosion in all spatial directions. There are no alternating belts of hard and soft rock, no dipping beds, and no pervasive oriented joint systems to steer channel paths.</li>
        <li><strong>Headward Tributary Bifurcation:</strong> Streams extend their drainage basins upstream by headward erosion along path lines of maximum local hydraulic gradient. Because the terrain is structurally isotropic, tributary branching occurs randomly and naturally at acute angles ($30^\\circ - 60^\\circ$), maximizing drainage efficiency.</li>
        <li><strong>Typical Geological Settings:</strong>
          <ul>
            <li>Horizontally bedded sedimentary rocks (e.g., flat-lying plateau sandstones, shales, and limestones).</li>
            <li>Massive, isotropic igneous plutons (e.g., unjointed granite batholiths).</li>
            <li>Uniform unconsolidated sediment sheets (e.g., thick glacial till plains, alluvial plains, coastal plains).</li>
            <li>Flood basalt plateaus with uniform horizontal layering (e.g., Deccan Traps).</li>
          </ul>
        </li>
      </ul>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q015/bangar_p27_dendritic_trellis_drainage.png" alt="K.M. Bangar Dendritic and Trellis Drainage Patterns">
        <div class="tb-caption">
          <strong>Figure 15.1: Contrast in Drainage Network Symmetry (K.M. Bangar, p. 27).</strong> (A) Dendritic drainage pattern characterized by tree-like branching on structurally isotropic flat-lying rocks, contrasted with (B) Trellis drainage developed along strike and dip on folded strata.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Drainage Patterns as Diagnostic Indicators of Bedrock Structure</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Drainage Pattern</th>
            <th>Diagnostic Geometry</th>
            <th>Structural & Lithologic Regime</th>
            <th>Degree of Structural Control</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dendritic</strong></td>
            <td>Irregular, tree-like branching; acute junctions ($<90^\\circ$)</td>
            <td>Horizontal sedimentary strata, massive granite, uniform till</td>
            <td><strong>Nil / Absent (Homogeneous substrate)</strong></td>
          </tr>
          <tr>
            <td><strong>Trellis</strong></td>
            <td>Subparallel strike streams with $90^\\circ$ dip tributaries</td>
            <td>Folded alternating hard/soft strata (anticlines/synclines)</td>
            <td><strong>Very High</strong> (Strike-dip lithologic control)</td>
          </tr>
          <tr>
            <td><strong>Rectangular</strong></td>
            <td>Sharp $90^\\circ$ grid bends in master and tributary streams</td>
            <td>Intersecting orthogonal joint sets, fault systems</td>
            <td><strong>Very High</strong> (Fracture/fault controlled)</td>
          </tr>
          <tr>
            <td><strong>Radial</strong></td>
            <td>Radiating outward from a central point like wheel spokes</td>
            <td>Conical volcanic peaks, structural domes, isolated peaks</td>
            <td><strong>High</strong> (Topographic / domal control)</td>
          </tr>
          <tr>
            <td><strong>Annular</strong></td>
            <td>Ring-like concentric circular subsequent channels</td>
            <td>Breached structural domes with alternating soft/hard beds</td>
            <td><strong>Very High</strong> (Concentric dip-strike control)</td>
          </tr>
          <tr>
            <td><strong>Parallel</strong></td>
            <td>Swift, uniformly straight parallel channels</td>
            <td>Steep, uniform regional slopes or parallel fault scarps</td>
            <td><strong>Moderate to High</strong> (Slope/scarp controlled)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q15_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 15)</div>
    <div class="q-stmt">
      15. If a region is lacking in structural control, then the drainage pattern in such regions will be :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Dendritic &nbsp;✔</div>
      <div class="raw-opt">(B) Trellis</div>
      <div class="raw-opt">(C) Rectangular</div>
      <div class="raw-opt">(D) Radial</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) Dendritic</div>
      <div class="sub">
        In photogeology, structural geomorphology, and remote sensing (K.M. Bangar, p. 27; Arthur L. Bloom, p. 272; Arthur N. Strahler, 1957; W.D. Thornbury, p. 120), a region that is <strong>lacking in structural control</strong> universally develops a <strong>Dendritic drainage pattern</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) Dendritic</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> A dendritic drainage pattern is the defining diagnostic hallmark of terrain lacking structural control. In isotropic, flat-lying, or massive rocks with uniform resistance to erosion, stream channels branch randomly and organically like tree limbs, joining at acute angles.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Trellis</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A trellis pattern exhibits extreme structural control, developing specifically in folded mountain belts with alternating resistant and non-resistant strata where streams follow parallel strike valleys and dip slopes at right angles.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Rectangular</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A rectangular pattern develops under intense structural control dictated by intersecting sets of orthogonal bedrock joints or fault systems, causing streams to make sharp $90^\\circ$ bends.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Radial</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A radial pattern reflects strong geomorphic and structural control dictated by an isolated volcanic cone or structural dome from which streams radiate outward in all directions.
    </div>
  </div>
"""

q15_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Topological Properties of Dendritic Networks: Shreve & Strahler Analysis</div>
    <div class="card-body">
      <p>In quantitative morphometry (Shreve, 1966; Strahler, 1957), topologically random channel networks (where channels develop without structural bias) inevitably produce dendritic topology:</p>
      <ul>
        <li><strong>Bifurcation Ratio ($R_b$):</strong> In true dendritic networks, Horton's bifurcation ratio ($R_b = N_u / N_{u+1}$) falls consistently within the narrow theoretical range of <strong>$3.0\\text{ to } 5.0$</strong>. Significant deviation ($R_b > 5$ or $<3$) indicates structural distortion (e.g., fault elongation).</li>
        <li><strong>Junction Angles:</strong> Tributaries join master channels at acute angles governed by the ratio of stream gradients (Howard, 1971): $\\cos \\theta = S_m / S_t$, where $S_m$ is the main stream slope and $S_t$ is the tributary slope.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What is a "pinnate" drainage pattern, and how does it relate to dendritic drainage?
          <div class="pq-ans">✔ Correct Answer: A fine-textured, feather-like modification of dendritic drainage where closely spaced parallel tributaries enter a main channel at acute angles, diagnostic of easily erodible, uniform loess or fine silt deposits.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In thick loess blankets (e.g., Loess Plateau in China), extreme rill erodibility in uniform sediment produces delicate feather-like (pinnate) dendritic networks.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What does an "angular" or "sub-dendritic" drainage pattern indicate on aerial photographs?
          <div class="pq-ans">✔ Correct Answer: Moderate structural control where a generally dendritic network is partially modified by secondary joint sets or gentle regional dips.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When a terrain has weak or widely spaced joints, the overall tree-like pattern persists, but individual tributary segments straighten along joint trends.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> In what rock formation of India is the classic dendritic drainage pattern most spectacularly developed?
          <div class="pq-ans">✔ Correct Answer: The horizontal basalt flows of the Deccan Traps (Maharashtra/Madhya Pradesh) and flat-lying Vindhyan sandstones.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The flat-lying, homogeneous basalt sheets offer uniform erodibility in all directions, developing perfect dendritic drainage across thousands of square kilometers.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Horton's morphometric laws, what does a constant Bifurcation Ratio ($R_b \\approx 3.5$) across all stream orders signify?
          <div class="pq-ans">✔ Correct Answer: Complete geological homogeneity and lack of structural control throughout the entire drainage basin.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> If a fault or fold belt intersected part of the basin, the bifurcation ratio for that specific order would jump anomalously. Constant $R_b$ proves isotropic dendritic development.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "centripetal" drainage pattern, and how does its symmetry contrast with radial drainage?
          <div class="pq-ans">✔ Correct Answer: Streams converge inward toward a central topographic depression (e.g., a volcanic caldera, desert playa, or sinkhole), the exact reverse of outward-radiating radial drainage.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Inward drainage terminating in an ephemeral lake or ponor characterizes closed structural or volcanic basins.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What happens to a dendritic drainage network if regional tectonic tilting occurs after its establishment?
          <div class="pq-ans">✔ Correct Answer: The network becomes asymmetric; tributaries on one side of the trunk stream elongate while tributaries on the opposite side are shortened and steepened.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Tectonic tilting modifies local hydraulic gradients, favoring preferential tributary growth down the tilt direction.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is a "deranged" (or contorted) drainage pattern, and what geologic process produces it?
          <div class="pq-ans">✔ Correct Answer: An unorganized, chaotic network of irregular lakes, swamps, and short meandering channels produced by recent continental glaciation (e.g., the Canadian Shield).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Glacial scour and moraine dumping completely obliterate pre-existing drainage systems, leaving a juvenile, disorganized landscape that has not had time to achieve equilibrium.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why do tributaries in a dendritic pattern typically join at acute angles ($<90^\\circ$) rather than right angles?
          <div class="pq-ans">✔ Correct Answer: Fluid energy minimization; acute junction angles minimize turbulence and energy loss at the confluence.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Streams naturally seek the path of least work (Playfair's Law and Leopold's minimum work hypothesis), aligning tributary junctions smoothly downstream.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=15,
    filename="Q015_Dendritic_Drainage_Pattern_No_Structural_Control_Complete_Guide.html",
    title="Q015: Dendritic Drainage Networks, Structural Isotropy & Morphometric Analysis",
    badge="GGM - 2/2019 • Fluvial Geomorphology & Structural Geology",
    h1_title="Q015: Dendritic Drainage Morphometry: Diagnostic Signatures of Uncontrolled Substrates",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 15<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 27); Arthur L. Bloom (<em>Geomorphology</em>, Ch. 11, pp. 272–276); Arthur N. Strahler (<em>GSA Bulletin</em>, 1957)",
    part1_html=q15_part1,
    part2_html=q15_part2,
    part3_html=q15_part3
)

# ==========================================
# QUESTION 16: CALDERA - A VERY LARGE CRATER
# ==========================================
q16_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Volcanological Architecture & Collapse Mechanics of Calderas</div>
    <div class="card-body">
      <p>In physical volcanology, a <strong>caldera</strong> (from the Spanish word for "cauldron") is a very large, basin-shaped or circular volcanic depression whose diameter is many times greater than that of an ordinary volcanic vent or crater. In international volcanological standards (Macdonald, 1972; Cas & Wright, 1987; Lipman, 1997), a caldera is defined as a volcanic depression typically exceeding <strong>$1 - 2\\text{ kilometers}$ in diameter</strong> (frequently reaching $10 - 50\\text{ km}$ across), formed primarily by the <strong>catastrophic roof collapse and subsidence</strong> of a volcanic structure into an underlying evacuated magma chamber.</p>

      <div class="quote-box bangar">
        "A crater is the normal funnel-shaped opening or depression at the summit of a volcano through which lava and gases erupt. When a volcanic explosion or summit collapse is on a gigantic scale, a very large, broad, cauldron-like volcanic depression is produced, which is called a <strong>caldera</strong>. A caldera is essentially a very large crater formed mostly by the collapse of the volcanic summit following the rapid evacuation of the underlying magma chamber (e.g., Crater Lake in Oregon, USA)."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Volcanoes & Volcanic Landforms, p. 15)</span>
      </div>

      <p>Calderas are genetically divided into two primary geodynamic classes:</p>
      <ul>
        <li><strong>Explosive Collapse Calderas (Krakatau / Crater Lake Type):</strong> Associated with silica-rich, highly viscous, gas-charged magmas (dacite, rhyolite). Eruption of colossal volumes ($>10 - 1000\\text{ km}^3$) of pyroclastic ignimbrites and pumice evacuates the shallow magma chamber, removing hydrostatic support. The unsupported volcanic edifice collapses downward along ring fractures, forming a vast, vertical-walled caldera basin that frequently fills with water to form a caldera lake.</li>
        <li><strong>Non-Explosive Subsidence Calderas (Hawaiian / Kilauea Type):</strong> Associated with low-viscosity basaltic shield volcanoes. Formed by the gentle, passive subsidence of the summit as basaltic magma drains laterally into subterranean rift zones or erupts from flank fissures.</li>
      </ul>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q016/bangar_p15_caldera_crater_volcano.png" alt="K.M. Bangar Volcanic Caldera and Crater">
        <div class="tb-caption">
          <strong>Figure 16.1: Evolution of a Collapse Caldera (K.M. Bangar, p. 15).</strong> Sequential cross-sections showing (A) Composite cone with shallow magma chamber, (B) Massive explosive pyroclastic eruption evacuating the magma chamber, (C) Catastrophic roof collapse along ring faults forming a vast caldera, and (D) Post-caldera resurgent dome and crater lake.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Volcanic Depressions: Crater vs. Caldera vs. Maar</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Volcanic Depression</th>
            <th>Typical Diameter</th>
            <th>Genetic Origin</th>
            <th>Explosive Energy & Magma Volume</th>
            <th>Type Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Volcanic Crater</strong></td>
            <td>$< 1\\text{ km}$ (typically tens to hundreds of meters)</td>
            <td>Explosive excavation and construction of tephra/scoria rim around central vent</td>
            <td>Localized eruptive activity; small magma volume</td>
            <td>Summit crater of Mt. Vesuvius, Barren Island crater</td>
          </tr>
          <tr>
            <td><strong>Caldera</strong></td>
            <td><strong>$> 1 - 2\\text{ km}$ (up to $50 - 100\\text{ km}$)</strong></td>
            <td><strong>Catastrophic roof collapse</strong> into an evacuated magma chamber along ring faults</td>
            <td>Super-eruptions ($VEI \\ge 6 - 8$); colossal magma volumes ($>100 - 1000\\text{ km}^3$)</td>
            <td>Crater Lake (Oregon), Toba Caldera (Sumatra), Yellowstone</td>
          </tr>
          <tr>
            <td><strong>Maar</strong></td>
            <td>$200\\text{ m} - 2\\text{ km}$</td>
            <td>Hydrovolcanic phreatomagmatic explosions where magma encounters groundwater</td>
            <td>Violent steam explosions; low tephra ring (tuff ring)</td>
            <td>Eifel maars (Germany), Lonar Crater (impact crater often compared)</td>
          </tr>
          <tr>
            <td><strong>Pit Crater</strong></td>
            <td>Tens to hundreds of meters</td>
            <td>Localized collapse caused by magma withdrawal without explosive eruption</td>
            <td>Basaltic shield subsidence along rift zones</td>
            <td>Halemaʻumaʻu (Kilauea, Hawaii)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q16_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 16)</div>
    <div class="q-stmt">
      16. A Caldera is :
    </div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) A very large crater &nbsp;✔</div>
      <div class="raw-opt">(B) A long mountain chain</div>
      <div class="raw-opt">(C) A gorge formed due to faulting</div>
      <div class="raw-opt">(D) A U-shaped valley</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (A) A very large crater</div>
      <div class="sub">
        In physical geology and volcanology (K.M. Bangar, p. 15; Arthur Holmes, p. 204; Macdonald, 1972; Cas & Wright, 1987), a <strong>caldera</strong> is defined as an exceptionally <strong>very large crater (or volcanic basin)</strong> formed by the collapse of a volcano's summit.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option correct">
    <div class="option-header">
      <span>(A) A very large crater</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard international definition, a caldera is a large, basin-shaped volcanic depression many times the diameter of the original volcanic vent. While normal craters are constructed by explosive ejection, calderas represent massive volcanic collapse structures on a scale of kilometers to tens of kilometers.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) A long mountain chain</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A long mountain chain represents an orogenic fold belt formed by continental collision (e.g., the Himalayas, Alps, Andes), an immense positive tectonic relief structure completely distinct from a circular volcanic caldera basin.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) A gorge formed due to faulting</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A gorge formed due to faulting is a structural graben, rift valley, or fault-line chasm. Calderas are circular volcanic collapse depressions formed by magma evacuation, not linear fault gorges.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) A U-shaped valley</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A U-shaped valley (glacial trough) is an erosional landform excavated by valley glaciers, featuring steep rock walls and flat floors, bearing no relation to volcanic caldera collapse.
    </div>
  </div>
"""

q16_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Super-Eruptions & The Volcano Explosivity Index (VEI)</div>
    <div class="card-body">
      <p>Caldera-forming eruptions are the most catastrophic natural explosive events on Earth, classified at the highest levels of the Volcanic Explosivity Index (Newhall & Self, 1982):</p>
      <ul>
        <li><strong>VEI 7 (Colossal, $>100\\text{ km}^3$ tephra):</strong> E.g., Santorini (1600 BC), Tambora (1815, "Year Without a Summer"), Crater Lake / Mt. Mazama ($5700\\text{ BC}$).</li>
        <li><strong>VEI 8 (Mega-Colossal / Super-volcano, $>1000\\text{ km}^3$ tephra):</strong> E.g., Toba Caldera ($74,000\\text{ BP}$, Sumatra: $2800\\text{ km}^3$ of magma evacuated, creating a $100 \\times 30\\text{ km}$ caldera and causing global volcanic winter), Yellowstone ($640,000\\text{ BP}$).</li>
        <li><strong>Resurgent Cauldrons (Smith & Bailey, 1968):</strong> Following collapse, magma pressure re-accumulates beneath the caldera floor, uplifting a central <em>resurgent dome</em> (e.g., Samosir Island in Lake Toba).</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A circular rhyolitic caldera has a diameter $D = 12.0\\text{ km}$. Structural field mapping reveals that the caldera floor subsided by an average vertical displacement $\\Delta z = 800\\text{ m}$ during the eruption. Calculate the total volume of collapsed rock in cubic kilometers ($\\text{km}^3$), which provides an estimate of the volume of magma evacuated from the chamber.
          <div class="pq-ans">✔ Worked Answer: Evacuated volume $V \\approx 90.5\\text{ km}^3$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Radius of caldera $R = D/2 = 6.0\\text{ km}$.<br>
            Surface area $A = \\pi R^2 = \\pi (6.0)^2 = 36\\pi \\approx 113.10\\text{ km}^2$.<br>
            Vertical collapse displacement $\\Delta z = 800\\text{ m} = 0.80\\text{ km}$.<br>
            $$V = A \\times \\Delta z = 113.10\\text{ km}^2 \\times 0.80\\text{ km} \\approx 90.48\\text{ km}^3$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the diagnostic structural fault type that accommodates the piston-like vertical collapse of a caldera roof?
          <div class="pq-ans">✔ Correct Answer: Ring faults (ring fracture systems) dipping steeply outward or near-vertically.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Ring faults encircle the magma chamber roof, permitting the central piston of country rock to drop downward as a cohesive block into the magma chamber.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What igneous rock body represents the crystallized root of a ring-fault system beneath an eroded ancient caldera?
          <div class="pq-ans">✔ Correct Answer: A ring dyke (vertical to outward-dipping) or cone sheet (inward-dipping).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Magma forced up into the bounding ring fractures during caldera collapse crystallizes as cylindrical or arcuate ring dykes (classic in the British Tertiary Igneous Province, e.g., Ardnamurchan).
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is the difference between a "Crater Lake-type" caldera and a "Hawaiian-type" caldera?
          <div class="pq-ans">✔ Correct Answer: Crater Lake-type forms by violent, explosive pyroclastic super-eruptions of felsic magma; Hawaiian-type forms by non-explosive, passive drainage of fluid basalt.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Crater Lake (Mt. Mazama) erupted $50\\text{ km}^3$ of pumice violently. Kilauea calderas subside gently when basalt drains into flank rift fissures.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "resurgent dome" within a caldera?
          <div class="pq-ans">✔ Correct Answer: A structural uplift of the caldera floor caused by the post-collapse recharge and repressurization of the underlying magma chamber.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In Smith & Bailey's caldera cycle (Stage 5), new magma enters the depleted chamber, arching the caldera floor upward into a prominent structural dome (e.g., Wizard Island in Crater Lake or Samosir in Lake Toba).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What volcanic deposits are found blanketing the surrounding landscape for tens of kilometers around an explosive caldera?
          <div class="pq-ans">✔ Correct Answer: Thick sheets of welded pyroclastic flow deposits (ignimbrites) and pumice-fall tephra.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Pyroclastic density currents (PDCs) boiling over from ring fissures discharge dense, hot ash and pumice flows that weld into solid rhyolitic tuff.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is the world's largest Quaternary caldera, and where is it located?
          <div class="pq-ans">✔ Correct Answer: Lake Toba Caldera in northern Sumatra, Indonesia ($100\\text{ km} \\times 30\\text{ km}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Formed $\\approx 74,000\\text{ years ago}$ by the eruption of $2800\\text{ km}^3$ of rhyolitic magma, creating a volcanic depression that now holds the largest volcanic lake on Earth.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why are ancient eroded calderas of prime importance in economic geology?
          <div class="pq-ans">✔ Correct Answer: Ring fracture systems focus post-magmatic hydrothermal fluid circulation, forming rich epithermal gold, silver, and polymetallic vein deposits.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The fractured caldera margin provides permeable conduits for boiling hydrothermal solutions, precipitating precious metals (e.g., the San Juan volcanic field, Colorado).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=16,
    filename="Q016_Caldera_Large_Volcanic_Crater_Complete_Guide.html",
    title="Q016: Calderas, Volcanic Collapse Mechanics & Super-Eruption Dynamics",
    badge="GGM - 2/2019 • Volcanology & Igneous Geodynamics",
    h1_title="Q016: Morphogenesis of Volcanic Calderas: Collapse Dynamics & Magma Chamber Drainage",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 16<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 15); Gordon A. Macdonald (<em>Volcanoes</em>, 1972); Peter W. Lipman (<em>Bulletin of Volcanology</em>, 1997)",
    part1_html=q16_part1,
    part2_html=q16_part2,
    part3_html=q16_part3
)

# ==========================================
# QUESTION 17: ROCK FLOUR & GOUGE - BRITTLE DEFORMATION
# ==========================================
q17_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Fault Rocks & The Brittle-Ductile Transition in Crustal Shear Zones</div>
    <div class="card-body">
      <p>In structural geology and fault mechanics, <strong>fault gouge</strong> (and finely pulverized <strong>rock flour</strong>) is an unhardened, non-cohesive or cohesive, fine-grained powder-like rock material produced by mechanical abrasion, frictional grinding, and cataclastic crushing of wall rocks along a fault zone during active fault displacement. Fault gouge and rock flour are definitively produced under <strong>brittle deformation</strong> regimes in the upper crust.</p>

      <div class="quote-box bangar">
        "During faulting under shallow crustal conditions, the rocks along the fault plane are crushed and pulverized due to intense friction. When the rock is reduced to a fine, clay-like flour or powder, it is called <strong>fault gouge</strong> or <strong>rock flour</strong>. When the crushed fragments are angular and larger, the rock is called fault breccia. These cataclastic rocks are the classic products of <strong>brittle deformation</strong> in the upper crust."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Faults: Fault Rocks & Breccias, p. 215)</span>
      </div>

      <p>The structural character of fault rocks changes systematically with crustal depth, governed by the <strong>Brittle-Ductile (Frictional-Viscous) Transition</strong> (Sibson, 1977; Scholz, 2002):</p>
      <ul>
        <li><strong>Upper Crust ($<10 - 15\\text{ km}$, $T < 300^\\circ\\text{C}$): Brittle Regime (Frictional Flow / Cataclasis):</strong> Deformation is dominated by microcracking, frictional sliding, grain rotation, and mechanical pulverization. Cohesion is lost during failure. This produces non-foliated cataclastic fault rocks:
          <ul>
            <li><strong>Fault Breccia:</strong> Visible angular clasts ($>2\\text{ mm}$) constituting $>30\\%$ of the rock, set in a crushed matrix.</li>
            <li><strong>Fault Gouge / Rock Flour:</strong> Ultrafine pulverized powder (clay-sized particles $<0.1\\text{ mm}$) constituting $>70\\%$ of the rock, often resembling soft, unlithified gouge clay.</li>
            <li><strong>Pseudotachylyte:</strong> Glassy, friction-melted rock formed during seismic slip.</li>
          </ul>
        </li>
        <li><strong>Middle to Lower Crust ($>10 - 15\\text{ km}$, $T > 300^\\circ\\text{C}$): Ductile Regime (Plastic Flow):</strong> Crystal-plasticity, dislocation creep, and dynamic recrystallization dominate without loss of macroscopic continuity. Rocks deform without brittle fracturing, forming strongly foliated and lineated <strong>mylonites</strong> and ultramylonites.</li>
      </ul>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q017/bangar_p115_fault_breccia_gouge_brittle.png" alt="K.M. Bangar Fault Rocks Gouge Breccia Brittle">
        <div class="tb-caption">
          <strong>Figure 17.1: Fault Rocks and Brittle Cataclasis (K.M. Bangar, p. 115).</strong> Thin-section and outcrop sketches illustrating the progressive mechanical pulverization of rock into angular fault breccia and ultrafine fault gouge (rock flour) along brittle slip surfaces.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Sibson's Fault Rock Classification Matrix (Sibson, 1977)</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Deformation Regime</th>
            <th>Primary Mechanism</th>
            <th>Foliation Status</th>
            <th>Cohesion during Slip</th>
            <th>Diagnostic Fault Rock Types</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Brittle (Elasto-Frictional)</strong><br>Depth: $0 - 5\\text{ km}$</td>
            <td>Cataclasis, frictional grinding, crushing</td>
            <td><strong>Random-fabric (Non-foliated)</strong></td>
            <td>Incohesive (Loose powder / gravel)</td>
            <td><strong>Fault Gouge (Rock Flour)</strong>, Fault Breccia</td>
          </tr>
          <tr>
            <td><strong>Brittle (Semi-Brittle)</strong><br>Depth: $5 - 10\\text{ km}$</td>
            <td>Pressure solution, microfracturing</td>
            <td>Random-fabric to weakly foliated</td>
            <td>Cohesive (Cemented cataclasite)</td>
            <td>Cataclasite, Ultracataclasite, Pseudotachylyte</td>
          </tr>
          <tr>
            <td><strong>Ductile (Quasi-Plastic)</strong><br>Depth: $10 - 20\\text{ km}$</td>
            <td>Dislocation creep, dynamic recrystallization</td>
            <td><strong>Strongly Foliated (Mylonitic)</strong></td>
            <td>Cohesive (Plastically deformed rock)</td>
            <td>Protomylonite, Mylonite, Ultramylonite</td>
          </tr>
          <tr>
            <td><strong>High-Grade Ductile</strong><br>Depth: $> 20\\text{ km}$</td>
            <td>Diffusional creep, high-T recrystallization</td>
            <td>Gneissic banding</td>
            <td>Cohesive metamorphic crystalline rock</td>
            <td>Blastomylonite, Gneissic shear zone rock</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q17_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 17)</div>
    <div class="q-stmt">
      17. Rock flour or gouge is closely linked to :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Ductile deformation</div>
      <div class="raw-opt correct">(B) Brittle deformation &nbsp;✔</div>
      <div class="raw-opt">(C) Flow of incompetent beds</div>
      <div class="raw-opt">(D) Collapse structures</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Brittle deformation</div>
      <div class="sub">
        In structural geology, fault mechanics, and rock physics (K.M. Bangar, p. 215; Marland P. Billings, p. 150; Richard H. Sibson, 1977; Davis & Reynolds, 1996), <strong>fault gouge</strong> and <strong>rock flour</strong> are fundamentally the mechanical products of <strong>Brittle deformation</strong> in the upper crust.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Ductile deformation</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Ductile deformation operates at deeper crustal levels ($T > 300^\\circ\\text{C}$) via crystal-plastic mechanisms (dislocation creep, grain-boundary sliding, dynamic recrystallization) without loss of material continuity. Ductile shear zones produce <strong>mylonites</strong> with ribbon quartz and porphyroclasts, never uncohesive crushed gouge or rock flour.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Brittle deformation</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Rock flour and fault gouge are diagnostic cataclastic products of <strong>brittle deformation</strong>. Under shallow, high-frictional stress conditions, rock undergoes mechanical microfracturing, grain comminution, and grinding along fault planes, pulverizing solid rock into a fine, unlithified powder.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Flow of incompetent beds</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The flow of incompetent beds (such as ductile squeezing of shale or salt between competent sandstone layers during folding) is a classic manifestation of ductile plastic flow, producing thickened fold hinges (similar folds) rather than brittle fault gouge.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Collapse structures</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Collapse structures refer to sinkholes, caldera drop blocks, or cave roof collapses. While localized impact breccia occurs, the term "fault gouge / rock flour" is specifically linked to tectonic brittle fault shear planes.
    </div>
  </div>
"""

q17_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Hydrogeological & Seismic Role of Fault Gouge</div>
    <div class="card-body">
      <p>Fault gouge plays a pivotal role in earthquake physics and petroleum reservoir compartmentalization:</p>
      <ul>
        <li><strong>Fault Zone Hydrogeology (Barrier vs. Conduit):</strong> Freshly crushed, clay-rich fault gouge experiences extreme grain-size reduction, causing its permeability to plummet by $4 - 6$ orders of magnitude ($K < 10^{-18} - 10^{-20}\\text{ m}^2$). Consequently, a gouge-lined fault core acts as an impermeable <strong>sealing barrier</strong> to fluid flow across the fault, trapping hydrocarbons or compartmentalizing groundwater aquifers, while the surrounding fractured damage zone acts as a high-permeability conduit parallel to the fault.</li>
        <li><strong>Frictional Stability (Rate-and-State Friction):</strong> The velocity-dependence of friction in fault gouge governs earthquake nucleation. Velocity-weakening gouge ($a - b < 0$) promotes unstable stick-slip seismic ruptures (earthquakes), whereas velocity-strengthening gouge ($a - b > 0$, e.g., montmorillonite/talc clays) promotes stable, aseismic fault creep.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What is "Pseudotachylyte", and under what specific deformation conditions does it form?
          <div class="pq-ans">✔ Correct Answer: A dark, glassy to microcrystalline rock formed by extreme frictional melting of rock along a fault plane during rapid seismic earthquake slip ($v \approx 1\text{ m/s}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Under seismic slip rates, frictional heat generation along brittle fault planes exceeds heat conduction, melting wall rocks at $T > 1000^\circ\text{C}$; rapid quenching produces glassy pseudotachylyte (the "fossil earthquake").
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Distinguish between "Cataclasite" and "Mylonite" in thin-section petrography.
          <div class="pq-ans">✔ Correct Answer: Cataclasites have non-foliated random fabrics formed by brittle microcracking and grain crushing; Mylonites have strong planar foliation formed by crystal-plastic flow and dynamic recrystallization.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Cataclasites show shattered, angular grains with microfractures; mylonites show ductile ribbon quartz, core-and-mantle structures, and subgrain rotation.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> At what approximate temperature and crustal depth does quartz transition from brittle cataclasis to ductile crystal-plastic deformation?
          <div class="pq-ans">✔ Correct Answer: Approximately $300^\circ\text{C}$ at a depth of $10\text{ to } 15\text{ kilometers}$ (in typical continental crust).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Below $300^\circ\text{C}$, quartz fractures brittly; above $300^\circ\text{C}$, dislocation glide and climb become active, allowing quartz to deform plastically. (Feldspar requires $T > 450^\circ - 500^\circ\text{C}$).
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is the "Shale Gouge Ratio" (SGR) used in the petroleum industry?
          <div class="pq-ans">✔ Correct Answer: The percentage of clay/shale smeared into the fault zone from sliced wall-rock stratigraphy, used to predict fault seal capacity against hydrocarbon leakage.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> An $SGR > 20 - 30\%$ typically indicates that the fault gouge will form a continuous, impermeable capillary membrane seal holding back substantial oil or gas columns.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What are "slickenlines" and "slickensides" on a fault surface?
          <div class="pq-ans">✔ Correct Answer: Slickensides are polished fault planes; slickenlines are linear grooves and striations carved on the fault surface indicating the direction of slip.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Asperity ploughing during brittle shear polishes the slip surface, and mineral fiber steps (calcite/quartz) provide the absolute sense of movement (hanging-wall direction).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> In glacial geology, what is "glacial rock flour", and how does it relate mechanically to fault gouge?
          <div class="pq-ans">✔ Correct Answer: Extremely fine silt- and clay-sized particles pulverized by the mechanical abrasion of bedrock beneath moving ice, identical in brittle cataclastic origin to fault rock flour.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Both form by mechanical grinding and crushing of rock fragments under high frictional normal stress, generating light-scattering rock flour that gives glacial meltwater lakes their turquoise/milky color.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In geotechnical tunneling, why does intersecting an active fault gouge zone present a catastrophic engineering hazard?
          <div class="pq-ans">✔ Correct Answer: Fault gouge has near-zero cohesion when wet, behaves as "running ground" or swelling clay, and can trigger massive water and mud inrushes into the tunnel.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Saturated gouge loses all shear strength under decompression, flowing like liquid mud into the tunnel excavation.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is "core-and-mantle structure" in shear zone petrography?
          <div class="pq-ans">✔ Correct Answer: A relict porphyroclast core surrounded by a mantle of dynamically recrystallized fine subgrains, diagnostic of transitional ductile shear.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Formed during subgrain rotation recrystallization (SGR) at the brittle-ductile transition zone.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=17,
    filename="Q017_Fault_Gouge_Rock_Flour_Brittle_Deformation_Complete_Guide.html",
    title="Q017: Fault Gouge, Rock Flour & Brittle Cataclasis Mechanics",
    badge="GGM - 2/2019 • Structural Geology & Fault Mechanics",
    h1_title="Q017: Mechanics of Fault Rocks: Rock Flour, Fault Gouge & Brittle Cataclasis",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 17<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 215); Marland P. Billings (<em>Structural Geology</em>, pp. 150–154); Richard H. Sibson (<em>Journal of the Geological Society</em>, 1977)",
    part1_html=q17_part1,
    part2_html=q17_part2,
    part3_html=q17_part3
)

print("Batch 2 (Q011 - Q017) generated successfully.")
