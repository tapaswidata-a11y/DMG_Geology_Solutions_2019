#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 6 to 10
Assam DGMS 2019 Masterclass Standard
"""

import os
from gen_2019_q001_to_q005 import CSS_STYLES, generate_page

# ==========================================
# QUESTION 6: FIORDS - GLACIAL ACTIVITY
# ==========================================
q6_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Geomorphology & Overdeepening Dynamics of Glacial Fiords</div>
    <div class="card-body">
      <p>A <strong>fiord</strong> (or <strong>fjord</strong>, from Old Norse <em>fjörðr</em>) is a long, narrow, steep-sided, deep marine coastal inlet or drowned valley produced by the glacial carving of a U-shaped trough below sea level, followed by post-glacial marine inundation. Fiords represent the most dramatic coastal erosional landforms created by <strong>glacial activity</strong>.</p>

      <div class="quote-box bangar">
        "When a valley glacier terminates at the sea coast, it excavates a deep, steep-sided U-shaped valley whose floor is overdeepened far below the current sea level. With the retreat of the glacier and post-glacial rise in sea level, the ocean waters drown these deep glacial troughs. Such drowned, steep-walled, deep marine glacial valleys are called <strong>fiords</strong> (characteristic of Norway, Greenland, Alaska, and New Zealand)."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Glacial Landforms & Marine Inundation, p. 31)</span>
      </div>

      <p>The morphology and oceanographic hydrodynamics of a fiord are governed by several diagnostic characteristics:</p>
      <ul>
        <li><strong>Glacial Overdeepening Below Sea Level:</strong> Unlike subaerial rivers, which cannot erode below sea-level base level, a valley glacier is a solid viscoelastic mass driven by upstream ice surface slopes and immense head pressure. An advancing glacier continues to scour, abrade, and pluck its bedrock bed until the ice floats in seawater (the flotation criterion: water depth $D_w = H_{\\text{ice}} \\times \\frac{\\rho_{\\text{ice}}}{\\rho_{\\text{water}}} \\approx 0.895 H_{\\text{ice}}$). Consequently, fiord floors frequently extend to extreme depths (e.g., Sognefjord in Norway is $1308\\text{ m}$ deep, while the surrounding peaks rise over $1000\\text{ m}$ above sea level).</li>
        <li><strong>Shallow Seaward Threshold (Sill / Rock Bar):</strong> At the mouth of the fiord where it enters the open ocean, the water depth abruptly shoals to a shallow bedrock ridge or terminal moraine deposit. This <em>sill</em> forms where the glacier's buoyancy reduced effective basal stress, halting bedrock erosion, and dumping terminal moraine debris.</li>
        <li><strong>Hanging Valleys & Waterfalls:</strong> Flanking tributary glaciers, possessing far less ice volume than the trunk glacier, eroded their tributary valleys less deeply. Following ice melt, these tributary valleys hang perched hundreds of meters above the fiord water surface, discharging dramatic hanging waterfalls.</li>
        <li><strong>U-Shaped Parabolic Cross-Section:</strong> Glacial erosion transforms narrow, pre-glacial fluvial V-shaped canyons into broad, steep-walled, flat-bottomed U-shaped troughs with flat valley floors.</li>
      </ul>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q006/bangar_p31_glacial_fiords_u_valleys.png" alt="K.M. Bangar Glacial Erosion U-Shaped Valleys and Fiords">
        <div class="tb-caption">
          <strong>Figure 6.1: Evolution of Glacial Troughs and Fiords (K.M. Bangar, p. 31).</strong> Progressive stages depicting (A) Pre-glacial fluvial V-shaped valley, (B) Maximum glaciation with deep ice scour and overdeepening below sea level, and (C) Post-glacial drowned fiord with hanging valleys, steep rock cliffs, and a shallow seaward bedrock sill.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Coastal Inlets Comparison: Fiord vs. Ria vs. Estuary</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Coastal Inlet Type</th>
            <th>Primary Originating Agent</th>
            <th>Cross-Profile Geometry</th>
            <th>Longitudinal Bed Profile</th>
            <th>Seaward Mouth Sill</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fiord (Fjord)</strong></td>
            <td><strong>Glacial activity</strong> (Drowned glacial trough)</td>
            <td>U-shaped; steep to vertical cliffs ($>500 - 1000\\text{ m}$)</td>
            <td>Overdeepened rock basin (hundreds of meters below sea level)</td>
            <td><strong>Present</strong> (Shallow bedrock sill or moraine ridge)</td>
          </tr>
          <tr>
            <td><strong>Ria</strong></td>
            <td><strong>Fluvial activity</strong> (Drowned river valley)</td>
            <td>V-shaped; sloping, dendritic valley sides</td>
            <td>Deepens gradually and continuously seaward</td>
            <td><strong>Absent</strong> (No bedrock sill)</td>
          </tr>
          <tr>
            <td><strong>Estuary</strong></td>
            <td>Tidal & Fluvial mixing</td>
            <td>Funnel-shaped; low relief alluvial banks</td>
            <td>Shallow; sandbars and mudflats</td>
            <td>Variable (Tidal sand shoals)</td>
          </tr>
          <tr>
            <td><strong>Fjard</strong></td>
            <td>Glacial erosion of low-relief crystalline plains</td>
            <td>Lower relief, undulating, branched glacial inlet</td>
            <td>Moderately shallow; many small rocky islets (skerry guard)</td>
            <td>Present (Irregular shallow sills)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q6_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 6)</div>
    <div class="q-stmt">
      6. Fiords are formed due to :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Lacustrine process</div>
      <div class="raw-opt">(B) Wind action</div>
      <div class="raw-opt correct">(C) Glacial activity &nbsp;✔</div>
      <div class="raw-opt">(D) Alluvial activity</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Glacial activity</div>
      <div class="sub">
        In physical geology and coastal geomorphology (K.M. Bangar, p. 31; Arthur L. Bloom, p. 378; Arthur Holmes, p. 556), <strong>fiords</strong> are universally defined as drowned, overdeepened U-shaped troughs created by <strong>glacial activity</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Lacustrine process</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Lacustrine processes pertain to inland freshwater or saline lakes (such as lake-bed varve deposition, delta sedimentation, and shoreline wave cut). While glacial lakes (tarns, paternoster lakes, ribbon lakes) form in glaciated valleys, marine-drowned coastal fiords are connected to the open ocean and carved by valley glaciers, not formed by lake processes.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Wind action</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Wind action (aeolian geomorphology) is restricted to sand dune construction, deflation hollows, yardangs, and loess deposition in arid terrains. Air lacks the physical density and abrasive energy required to excavate massive, kilometer-deep bedrock trenches into coastal mountain ranges.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Glacial activity</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> A fiord is unequivocally the geomorphic product of <strong>glacial activity</strong>. Massive valley glaciers (ice streams) scour and overdeepen bedrock troughs below sea level; following deglaciation and eustatic sea-level rise, ocean water drowns the U-shaped trough, creating a classic fiord with sheer rock walls, hanging tributary valleys, and a shallow seaward sill.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Alluvial activity</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Alluvial activity refers to stream erosion and deposition. When a river valley is submerged by sea-level rise, it produces a <strong>ria</strong> (a V-shaped, branching dendritic inlet that deepens continuously seaward without an overdeepened basin or bedrock sill). True fiords require glacial ice erosion.
    </div>
  </div>
"""

q6_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Oceanographic & Stratigraphic Signatures of Glacial Fiords</div>
    <div class="card-body">
      <p>Because the seaward threshold (sill) severely restricts deep-water exchange with the open ocean, the hydrodynamics of fiords lead to distinct environmental and sedimentological signatures:</p>
      <ul>
        <li><strong>Anoxic Bottom Water & Sapropelic Muds:</strong> The shallow sill prevents incoming dense ocean currents from easily flushing the deep basin floor. In poorly ventilated fiords, organic matter sinking from surface waters consumes all dissolved oxygen, producing stagnant, anoxic bottom conditions ($H_2S$ generation) that preserve unbioturbated, finely laminated organic-rich black muds (sapropels).</li>
        <li><strong>Varved Glaciomarine Sediments:</strong> Proglacial meltwater streams discharge rock flour (silt and clay) forming seasonal glaciomarine couplets (varves) that provide ultra-high-resolution paleoclimatic records.</li>
        <li><strong>Iceberg Dropstones:</strong> Calving tidewater glaciers release icebergs carrying erratic pebbles and boulders, which melt and drop into the finely laminated basin sediments, creating piercing dropstone deformation structures.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A valley glacier with an ice thickness $H_{\\text{ice}} = 900\\text{ m}$ and average density $\\rho_{\\text{ice}} = 900\\text{ kg/m}^3$ advances into the sea (seawater density $\\rho_{\\text{sw}} = 1025\\text{ kg/m}^3$). According to Archimedes' flotation principle, calculate the maximum water depth at which the glacier maintains contact with the bedrock floor before it floats, thereby setting the maximum theoretical limit of glacial bedrock overdeepening.
          <div class="pq-ans">✔ Worked Answer: Water depth $D_w \\approx 790.2\\text{ meters}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Flotation occurs when the weight of displaced seawater equals the total weight of the ice column:<br>
            $$\\rho_{\\text{sw}} \\cdot g \\cdot D_w = \\rho_{\\text{ice}} \\cdot g \\cdot H_{\\text{ice}}$$
            $$D_w = H_{\\text{ice}} \\times \\frac{\\rho_{\\text{ice}}}{\\rho_{\\text{sw}}} = 900\\text{ m} \\times \\frac{900}{1025} \\approx 790.24\\text{ m}$$<br>
            Therefore, as long as water depth is less than $790.2\\text{ m}$, the glacier remains grounded, continuing to erode and overdeepen its bedrock bed.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the name of the shallow bedrock or moraine barrier located at the seaward mouth of a fiord, and what is its hydrodynamic consequence?
          <div class="pq-ans">✔ Correct Answer: The "Sill" (or threshold); it restricts oceanic deep-water exchange, often resulting in stagnant, anoxic basin bottom waters.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The sill acts as a submarine dam separating the open ocean from the overdeepened inner fiord basin, trapping dense bottom water and preventing vertical tidal mixing.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the morphological difference between a "Fiord" and a "Ria"?
          <div class="pq-ans">✔ Correct Answer: A fiord is a drowned glacial U-shaped valley with a steep cross-section, overdeepened floor, and shallow sill; a ria is a drowned fluvial V-shaped valley deepening continuously seaward without a sill.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Rias (common in Galicia, Spain and southwest Ireland) are dendritic river systems submerged by post-glacial sea-level rise, whereas fiords are glaciated chasms.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Why do hanging valleys frequently flank the walls of glacial fiords?
          <div class="pq-ans">✔ Correct Answer: Because smaller tributary glaciers had much less ice discharge and erosive power, carving their valleys to a much shallower depth than the massive trunk glacier.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Glacial downcutting scales with ice discharge and basal shear stress. The trunk glacier excavated hundreds of meters deeper than the tributary glaciers, leaving the tributary mouths perched high above the main valley floor.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the world's deepest known fiord, and what is its maximum water depth?
          <div class="pq-ans">✔ Correct Answer: Skelton Inlet in Antarctica ($>1900\\text{ m}$ deep) or Sognefjord in Norway ($1308\\text{ m}$ water depth).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sognefjord in western Norway penetrates $205\\text{ km}$ inland with sheer rock cliffs rising over $1000\\text{ m}$ above the water surface and a water depth of $1308\\text{ m}$ at its central basin.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "skerry guard" (skjærgård) associated with fiord coastlines?
          <div class="pq-ans">✔ Correct Answer: An archipelago of thousands of low, rounded glaciated rocky islands, reefs, and skerries flanking the seaward entrance to fiords.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Formed where continental ice sheets smoothed and grooved low crystalline bedrock plains before reaching the open sea (classic in Norway and Sweden).
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> In glaciomarine sedimentary cores, how is a sudden iceberg calving event identified?
          <div class="pq-ans">✔ Correct Answer: By a layer of Ice-Rafted Debris (IRD) containing coarse, angular gravel dropstones embedded in fine-grained marine muds (e.g., Heinrich events).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Large icebergs floating over fiords and oceans drop frozen debris as they melt, punching through underlying laminated sediments.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why are modern fiords vulnerable to catastrophic tsunamis triggered by subaerial rockslides?
          <div class="pq-ans">✔ Correct Answer: Because the near-vertical, glacially oversteepened rock walls are prone to debuttressing failure, and the narrow confined water body amplifies wave runup to extreme heights.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Glacial retreat removes lateral support (debuttressing). When rock masses collapse into the narrow, deep fiord chasm, water is displaced into mega-tsunamis (e.g., 1958 Lituya Bay megatsunami, Alaska: $524\\text{ m}$ wave runup).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=6,
    filename="Q006_Fiords_Glacial_Trough_Drowned_Valley_Complete_Guide.html",
    title="Q006: Glacial Fiords, Overdeepened Troughs & Marine Inundation Mechanics",
    badge="GGM - 2/2019 • Glacial Geomorphology & Marine Geology",
    h1_title="Q006: Morphogenesis of Glacial Fiords: Overdeepening, Sills & Flotation Dynamics",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 6<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 31); Arthur L. Bloom (<em>Geomorphology</em>, Ch. 15, pp. 378–384); Arthur Holmes (<em>Principles of Physical Geology</em>, Ch. 18)",
    part1_html=q6_part1,
    part2_html=q6_part2,
    part3_html=q6_part3
)

# ==========================================
# QUESTION 7: AEOLIAN DEPOSITS - SAND
# ==========================================
q7_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Physics of Aeolian Grain Transport & Granulometric Sorting</div>
    <div class="card-body">
      <p>In physical geology and sedimentology, <strong>aeolian deposits</strong> (wind-blown sediments) exhibit the most exquisite and precise grain-size sorting observed anywhere in the natural geological world. The physical reason why well-sorted aeolian accumulations (dunes, ergs, and sand sheets) are overwhelmingly composed of <strong>sand</strong> (specifically medium-to-fine quartz sand, $0.125 - 0.50\\text{ mm}$) is governed by the fundamental fluid mechanics of wind transport formalized by Brigadier <strong>Ralph A. Bagnold</strong> (1941, <em>The Physics of Blown Sand and Desert Dunes</em>).</p>

      <div class="quote-box bangar">
        "Wind is a remarkably efficient sorting agent. Because air has a very low density compared to water, it cannot transport coarse pebbles and gravels except by rolling them along the ground, while fine dust and silt are carried far away in turbulent suspension to form loess. The intermediate size fraction—consisting of medium to fine sand—moves by hopping and bouncing (saltation) and accumulates into dunes. Therefore, well-sorted aeolian deposits are chiefly composed of <strong>sand</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Geological Work of Wind, p. 23)</span>
      </div>

      <p>Wind moves sediment via three sharply distinct physical transport modes, dictated by grain diameter ($D$):</p>
      <ul>
        <li><strong>Surface Creep / Traction ($D > 0.5 - 2.0\\text{ mm}$, Coarse Sand & Granules):</strong> Particles too heavy to be lifted into the air. They are pushed and rolled along the surface by the kinetic impacts of landing saltating grains ($20 - 25\\%$ of total aeolian bedload).</li>
        <li><strong>Saltation ($D \\approx 0.125 - 0.50\\text{ mm}$, Medium to Fine Sand):</strong> Grains are lifted by fluid aerodynamic drag and Bernoulli lift, ascending into parabolic trajectories before crashing back to the surface at shallow angles ($10^\\circ - 16^\\circ$). This impact dislodges and ejects new grains into saltation. Saltation accounts for <strong>$75 - 80\\%$ of all aeolian sand transport</strong> and produces near-perfectly sorted quartz sand deposits ($\\sigma_\\phi < 0.35 - 0.50$).</li>
        <li><strong>Suspension ($D < 0.05\\text{ mm}$, Silt and Clay Dust):</strong> Particles small enough that turbulent upward eddies in the wind exceed their gravitational terminal settling velocity ($w_s$). Silt and clay are carried thousands of kilometers downwind in high-altitude dust storms, bypassing dune fields entirely and settling across distant humid margins as unstratified <strong>loess</strong> blankets.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Bagnold's Fluid Threshold Shear Velocity for Grain Entrainment (Bagnold, 1941)</div>
        $$u_{*t} = A \\cdot \\sqrt{\\frac{\\rho_s - \\rho}{\\rho} \\cdot g \\cdot D}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $u_{*t}$ is the critical fluid threshold shear velocity, $A \\approx 0.1$ is an empirical constant, $\\rho_s \\approx 2650\\text{ kg/m}^3$ is quartz grain density, $\\rho \\approx 1.225\\text{ kg/m}^3$ is air density, $g = 9.81\\text{ m/s}^2$, and $D$ is grain diameter. Crucially, as $D$ decreases below $0.08\\text{ mm}$ (silt and clay), cohesive electrostatic forces and the smooth viscous sublayer cause $u_{*t}$ to sharply <em>increase</em>, making fine sand ($0.1 - 0.25\\text{ mm}$) by far the most easily entrained grain size on Earth!</p>
      </div>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q007/bangar_p23_wind_transport_sand_dunes.png" alt="K.M. Bangar Wind Transport Saltation Sand Dunes">
        <div class="tb-caption">
          <strong>Figure 7.1: Aeolian Transport Dynamics & Sand Dunes (K.M. Bangar, p. 23).</strong> Mechanics of wind transportation showing surface creep, saltation of medium sand, and suspension of dust, along with the morphology of transverse and barchan sand dunes.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q007/boggs_fig8_17_eolian_dune_types.png" alt="Sam Boggs Jr Eolian Dune Types and Sorting">
        <div class="tb-caption">
          <strong>Figure 7.2: Classification of Aeolian Dunes & Granulometric Sorting (Sam Boggs Jr., Fig. 8.17).</strong> Relationship between wind regime, sand supply, and dune morphology (Barchan, Transverse, Longitudinal/Seif, Parabolic, and Star dunes).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Granulometric & Textural Maturity of Aeolian Dune Sands</div>
    <div class="card-body">
      <p>Under petrographic and Scanning Electron Microscope (SEM) analysis, well-sorted aeolian dune sands display unmatched textural and mineralogical maturity:</p>
      <table>
        <thead>
          <tr>
            <th>Diagnostic Textural Property</th>
            <th>Observed Aeolian Characteristic</th>
            <th>Underlying Physical / Mechanical Cause</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Grain-Size Sorting ($\\sigma_\\phi$)</strong></td>
            <td>Very Well Sorted ($\\sigma_\\phi < 0.35$)</td>
            <td>Air density window preferentially traps grains moving by saltation ($0.125 - 0.5\\text{ mm}$)</td>
          </tr>
          <tr>
            <td><strong>Mineralogical Composition</strong></td>
            <td>Supermature Quartzarenite ($>95 - 99\\% \\text{ SiO}_2$)</td>
            <td>High-energy grain collisions in air shatter and destroy fragile feldspars and lithic fragments</td>
          </tr>
          <tr>
            <td><strong>Roundness & Sphericity</strong></td>
            <td>Exceptionally well-rounded, high sphericity</td>
            <td>Particle impact kinetic energy in air is $\\approx 800\\times$ greater than in water due to lack of buoyancy</td>
          </tr>
          <tr>
            <td><strong>Surface Microtexture (SEM)</strong></td>
            <td>"Frosted" / Ground-glass appearance; upturned cleavage plates</td>
            <td>Direct grain-to-grain ballistic impacts produce microscopic percussion pits</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q7_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 7)</div>
    <div class="q-stmt">
      7. Well sorted aeolian deposits are chiefly composed of :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Clay</div>
      <div class="raw-opt correct">(B) Sand &nbsp;✔</div>
      <div class="raw-opt">(C) Sand and Silt</div>
      <div class="raw-opt">(D) Silt and Clay</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Sand</div>
      <div class="sub">
        In standard university sedimentology (Bagnold, 1941; K.M. Bangar, p. 23; Sam Boggs Jr., p. 268; Folk, 1974), well-sorted aeolian accumulations (dunes, ergs, sand sheets) are fundamentally and chiefly composed of <strong>Sand</strong> (medium-to-fine quartz sand).
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Clay</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Clay particles ($<0.002\\text{ mm}$) possess strong electrostatic surface charges (cohesion) and lie within the laminar viscous sublayer, making them nearly impossible for wind to entrain directly from dry mudflats. Once entrained, clay remains in high turbulent suspension over thousands of kilometers and never accumulates as local, well-sorted bedforms.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Sand</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Because air has very low viscosity and low density, wind acts as a hyper-selective sorting filter. Grains of medium-to-fine sand ($0.125 - 0.50\\text{ mm}$) move predominantly by <strong>saltation</strong>, accumulating in vast dune fields and ergs as exceptionally well-sorted, clean sand deposits, while finer silt and clay are winnowed away into suspension.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Sand and Silt</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> While poorly sorted desert wadi wash may contain sand and silt, <em>well-sorted</em> aeolian deposits are remarkably devoid of silt. Silt particles are winnowed out by continuous aeolian saltation bombardment and lifted into atmospheric suspension.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Silt and Clay</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Silt and clay mixtures constitute aeolian <strong>loess</strong> and atmospheric dust deposits. Loess is typically a massive, unstratified, moderately sorted silt deposit ($0.02 - 0.05\\text{ mm}$) rather than the quintessential "well-sorted aeolian deposit" represented by dune sands.
    </div>
  </div>
"""

q7_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comparison: Aeolian Sand Dunes vs. Aeolian Loess</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Sedimentary Attribute</th>
            <th>Aeolian Dune Deposits (Sand)</th>
            <th>Aeolian Loess Deposits (Dust)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dominant Grain Size</strong></td>
            <td>Medium to fine sand ($0.125 - 0.50\\text{ mm}$)</td>
            <td>Fine silt ($0.02 - 0.05\\text{ mm}$) with minor clay</td>
          </tr>
          <tr>
            <td><strong>Transport Mode</strong></td>
            <td>Saltation and surface creep</td>
            <td>Turbulent atmospheric suspension</td>
          </tr>
          <tr>
            <td><strong>Degree of Sorting</strong></td>
            <td><strong>Very well sorted</strong> ($\\sigma_\\phi < 0.35 - 0.50$)</td>
            <td>Moderately to poorly sorted ($\\sigma_\\phi > 1.0$)</td>
          </tr>
          <tr>
            <td><strong>Sedimentary Bedforms</strong></td>
            <td>Spectacular, large-scale cross-bedding (tabular/trough)</td>
            <td>Massive, unstratified blankets with vertical jointing</td>
          </tr>
          <tr>
            <td><strong>Mineralogy</strong></td>
            <td>Quartzarenite ($>95\\%$ quartz; highly mature)</td>
            <td>Quartz, feldspar, mica, calcite, clay minerals (chemically fresh)</td>
          </tr>
          <tr>
            <td><strong>Depositional Setting</strong></td>
            <td>Deserts (Ergs), coastal foredunes, proglacial sand plains</td>
            <td>Periglacial plains, semi-arid margins (e.g., Loess Plateau, China)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A granulometric sieving analysis of an aeolian dune sand yields the following cumulative percentiles on the Wentworth phi scale: $\\phi_{16} = 2.10$, $\\phi_{84} = 2.70$, $\\phi_5 = 1.80$, $\\phi_{95} = 3.00$. Calculate the Folk and Ward Graphic Standard Deviation (sorting coefficient, $\\sigma_I$) and classify its sorting quality.
          <div class="pq-ans">✔ Worked Answer: $\\sigma_I = 0.332$ (Very Well Sorted).</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Using the Folk and Ward (1957) Inclusive Graphic Standard Deviation formula:<br>
            $$\\sigma_I = \\frac{\\phi_{84} - \\phi_{16}}{4} + \\frac{\\phi_{95} - \\phi_5}{6.6}$$
            $$\\sigma_I = \\frac{2.70 - 2.10}{4} + \\frac{3.00 - 1.80}{6.6} = \\frac{0.60}{4} + \\frac{1.20}{6.6} = 0.150 + 0.1818 = 0.3318$$<br>
            Since $\\sigma_I < 0.35$, the sediment is classified as <strong>Very Well Sorted</strong>, a hallmark of aeolian dune sands.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Why does the threshold shear velocity curve ($u_{*t}$) reach an absolute minimum for grains of size $0.10 - 0.15\\text{ mm}$ (fine sand) and increase sharply for smaller silt and clay particles?
          <div class="pq-ans">✔ Correct Answer: Because cohesive electrostatic forces (van der Waals attraction) bind fine clay/silt particles together, and their small diameter hides them beneath the laminar viscous sublayer.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> To lift a clay particle, wind must overcome not just gravity, but powerful inter-particle cohesion. For sand grains ($>0.1\\text{ mm}$), cohesion is negligible and grains protrude into turbulent air flow, making fine sand the easiest grain size to transport.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is the classic angle of repose for dry quartz sand forming the slip-face (lee slope) of an aeolian sand dune?
          <div class="pq-ans">✔ Correct Answer: Approximately $30^\\circ \\text{ to } 34^\\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Sand saltating up the gentle windward stoss slope ($10^\\circ - 15^\\circ$) reaches the dune crest and avalanches down the lee side under gravity, maintaining the natural angle of internal friction of dry cohesionless sand ($32^\\circ - 34^\\circ$).
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> Distinguish between a Barchan dune and a Parabolic dune based on horn orientation and environmental setting.
          <div class="pq-ans">✔ Correct Answer: Barchan horns point downwind in arid, vegetation-free environments; Parabolic horns point upwind, anchored by coastal or semi-arid vegetation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In barchans, the central dune body moves slower than the thin flanking horns. In parabolic dunes, coastal shrubs pin the horns while the blowout center migrates downwind.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What microscopic surface texture under SEM distinguishes aeolian sand grains from subaqueous fluvial sand grains?
          <div class="pq-ans">✔ Correct Answer: A frosted, pitted surface with dense crescentic percussion pits and upturned cleavage plates caused by violent grain-to-grain impacts in air.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The absence of a buoyant, cushioning water film allows unbuffered grain collisions in air, chipping microscopic pits that give grains a frosted appearance.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "Yardang", and how does it form?
          <div class="pq-ans">✔ Correct Answer: A streamlined, sharp-crested, keel-shaped bedrock ridge aligned parallel to the prevailing wind, carved by wind abrasion and deflation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Wind armed with saltating sand scours softer strata, leaving streamlined, aerodynamic ridges that minimize drag.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> Why do ancient aeolian sandstones (e.g., the Jurassic Navajo Sandstone in the USA or Permian Rotliegend in Europe) constitute superior hydrocarbon and groundwater aquifers?
          <div class="pq-ans">✔ Correct Answer: Superb sorting, high roundness, lack of fine clay/silt matrix, and well-connected pore networks give them exceptionally high porosity ($20 - 30\\%$) and permeability ($>1000\\text{ mD}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Aeolian winnowing strips away impermeable clay minerals, creating uniform pore throats.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is "desert pavement" (or reg/serir), and how does it develop?
          <div class="pq-ans">✔ Correct Answer: A closely packed, armor-like surface layer of coarse pebbles and rock fragments left behind after wind deflation has winnowed away all sand and silt.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Once the pavement forms, it protects the underlying fine material from further wind deflation, establishing a geomorphic steady state.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=7,
    filename="Q007_Aeolian_Sand_Sorting_Bagnold_Physics_Complete_Guide.html",
    title="Q007: Aeolian Granulometry, Bagnold Transport Physics & Sand Dune Sorting",
    badge="GGM - 2/2019 • Sedimentology & Aeolian Geomorphology",
    h1_title="Q007: Physics of Aeolian Grain Transport: Saltation, Sorting & Dune Petrography",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 7<br><strong>Authoritative References:</strong> Ralph A. Bagnold (<em>The Physics of Blown Sand</em>, 1941); K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 23); Sam Boggs Jr. (<em>Sedimentology & Stratigraphy</em>, Ch. 8, pp. 268–274)",
    part1_html=q7_part1,
    part2_html=q7_part2,
    part3_html=q7_part3
)

# ==========================================
# QUESTION 8: DRAINAGE DENSITY - TOTAL LENGTH / AREA
# ==========================================
q8_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Mathematical Formulation of Drainage Density & Horton's Laws</div>
    <div class="card-body">
      <p>In quantitative fluvial morphometry and hydrology, <strong>drainage density ($D_d$)</strong> is a fundamental linear-areal dimensionless-scale parameter introduced by the distinguished American hydrologist and engineer <strong>Robert E. Horton</strong> in his seminal 1945 paper (<em>Erosional development of streams and their drainage basins; hydrophysical approach to quantitative morphology</em>, GSA Bulletin). Horton mathematically defined drainage density as the <strong>total length of streams of all orders within a drainage basin divided by the total area of the basin</strong>.</p>

      <div class="quote-box bangar">
        "Drainage density ($D_d$) is defined as the ratio of the total length of all stream channels in a drainage basin to the total area of the basin. It is expressed as:
        $$D_d = \\frac{\\sum L}{A}$$
        where $\\sum L$ is the total length of streams of all orders and $A$ is the total basin area. It reflects the closeness of spacing of channels and provides a quantitative measure of the dissected nature of the terrain."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Drainage Basins & Morphometric Analysis, p. 27)</span>
      </div>

      <p>Drainage density possesses dimensions of $[L]/[L^2] = [L^{-1}]$, typically expressed in units of <strong>$\\text{km}/\\text{km}^2 = \\text{km}^{-1}$</strong> (or $\\text{mi}/\\text{mi}^2$). It serves as the primary quantitative bridge connecting watershed geology, climate, vegetative cover, and surface runoff dynamics.</p>

      <div class="formula-card">
        <div class="formula-title">Horton's Core Morphometric Basin Equations (Horton, 1945; Schumm, 1956)</div>
        $$D_d = \\frac{\\sum_{u=1}^k \\sum_{i=1}^{N_u} L_{u,i}}{A} \\quad [\\text{km}^{-1}]$$
        $$C = \\frac{1}{D_d} = \\frac{A}{\\sum L} \\quad [\\text{km}^2/\\text{km}] \\quad (\\text{Constant of Channel Maintenance})$$
        $$L_g = \\frac{1}{2 D_d} \\quad [\\text{km}] \\quad (\\text{Mean Length of Overland Flow})$$
        $$F_s = \\frac{\\sum N}{A} \\quad [\\text{km}^{-2}] \\quad (\\text{Stream Frequency})$$
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q008/bangar_p27_drainage_density_basin_morphometry.png" alt="K.M. Bangar Drainage Density Basin Morphometry">
        <div class="tb-caption">
          <strong>Figure 8.1: Basin Morphometry & Horton Stream Ordering (K.M. Bangar, p. 27).</strong> Quantitative stream network delineation illustrating Strahler/Horton stream ordering, drainage basin boundary ($A$), and cumulative channel length calculation ($\\sum L$) for determining drainage density.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Geological & Hydrological Controls on Drainage Density</div>
    <div class="card-body">
      <p>Drainage density varies across three orders of magnitude (from $<1.0\\text{ km}^{-1}$ in dense forests on sandstone/limestone to $>500\\text{ km}^{-1}$ in arid badlands on impermeable shales). Its magnitude is dictated by the fundamental balance between <strong>erosive driving forces</strong> (surface runoff) and <strong>surface resistance forces</strong> (infiltration capacity and vegetation):</p>
      <table>
        <thead>
          <tr>
            <th>Drainage Density Category</th>
            <th>Value Range ($D_d$)</th>
            <th>Dominant Bedrock Lithology & Soil</th>
            <th>Infiltration & Runoff Dynamics</th>
            <th>Hydrograph Flashiness</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Extremely Low ($D_d < 2\\text{ km}^{-1}$)</strong></td>
            <td>$< 2\\text{ km/km}^2$</td>
            <td>Highly permeable sands, gravels, karstic limestone, thick gravelly regolith</td>
            <td>Very high infiltration; minimal overland flow; sustained groundwater baseflow</td>
            <td>Subdued, broad hydrographs; minimal flood risk</td>
          </tr>
          <tr>
            <td><strong>Moderate ($D_d = 5 - 15\\text{ km}^{-1}$)</strong></td>
            <td>$5 - 15\\text{ km/km}^2$</td>
            <td>Jointed granite, sandstones with moderate soil cover, humid temperate forests</td>
            <td>Moderate infiltration capacity; balanced surface runoff and throughflow</td>
            <td>Standard hydrograph response</td>
          </tr>
          <tr>
            <td><strong>High ($D_d = 15 - 50\\text{ km}^{-1}$)</strong></td>
            <td>$15 - 50\\text{ km/km}^2$</td>
            <td>Impermeable crystalline schist, weathered basalt, sparse vegetation</td>
            <td>Low infiltration; rapid overland flow concentration</td>
            <td>Sharp, rapid flood peaks</td>
          </tr>
          <tr>
            <td><strong>Extremely High / Badlands ($D_d > 100 - 500\\text{ km}^{-1}$)</strong></td>
            <td>$> 100\\text{ km/km}^2$</td>
            <td>Unconsolidated, impermeable montmorillonite clays, mudstones, devoid of vegetation</td>
            <td>Near-zero infiltration; massive sheetwash and rapid rill incision</td>
            <td>Extreme flash-flood catastrophe risk</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q8_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 8)</div>
    <div class="q-stmt">
      8. Drainage density of a basin is a measure of :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Total number of the highest order streams divided by the total number of the next lower order streams</div>
      <div class="raw-opt">(B) Length of the largest stream divided by the total area of the basin</div>
      <div class="raw-opt correct">(C) Total length of streams of all orders divided by the total area of the basin &nbsp;✔</div>
      <div class="raw-opt">(D) Total number of streams of all orders</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Total length of streams of all orders divided by the total area of the basin</div>
      <div class="sub">
        In quantitative geomorphology and basin hydrology (Robert E. Horton, 1945; Arthur N. Strahler, 1957; K.M. Bangar, p. 27), <strong>Drainage Density ($D_d$)</strong> is mathematically defined as the <strong>total length of streams of all orders divided by the total area of the drainage basin</strong> ($D_d = \\sum L / A$).
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Total number of the highest order streams divided by...</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The ratio of the number of streams of a given order ($N_u$) to the number of streams of the next higher order ($N_{u+1}$) defines Horton's <strong>Bifurcation Ratio ($R_b = N_u / N_{u+1}$)</strong>, which describes the branching geometry of a network, not its drainage density.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Length of the largest stream divided by the total area...</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Dividing only the length of the trunk/largest stream by total basin area is an arbitrary ratio that neglects the entire tributary network. Drainage density strictly requires the summation of stream lengths across <em>all stream orders</em> from 1st-order headwater rills to the highest-order trunk channel.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Total length of streams of all orders divided by the total area of the basin</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> This is the universal, standardized textbook definition established by Robert E. Horton (1945): $D_d = \\frac{\\sum L}{A}$, measuring the density of channel incision in units of $\\text{km}^{-1}$.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Total number of streams of all orders</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> The total number of streams of all orders is simply the basin's total channel count ($\sum N$). When divided by basin area ($A$), it yields <strong>Stream Frequency ($F_s = \\sum N / A$)</strong>, which has units of $\\text{km}^{-2}$, whereas drainage density measures cumulative <em>stream length</em> per unit area.
    </div>
  </div>
"""

q8_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Horton's Morphometric Parameters</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Morphometric Parameter</th>
            <th>Mathematical Formula</th>
            <th>Physical Dimension / Units</th>
            <th>Geomorphological & Hydrological Meaning</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Drainage Density ($D_d$)</strong></td>
            <td>$$D_d = \\frac{\\sum L}{A}$$</td>
            <td>$[L^{-1}] \\quad (\\text{km}^{-1})$</td>
            <td>Closeness of channel spacing; landscape dissection intensity; runoff speed</td>
          </tr>
          <tr>
            <td><strong>Constant of Channel Maintenance ($C$)</strong></td>
            <td>$$C = \\frac{1}{D_d} = \\frac{A}{\\sum L}$$</td>
            <td>$[L] \\quad (\\text{km}^2/\\text{km})$</td>
            <td>Minimum surface drainage area required to sustain 1 kilometer of channel</td>
          </tr>
          <tr>
            <td><strong>Length of Overland Flow ($L_g$)</strong></td>
            <td>$$L_g = \\frac{1}{2 D_d}$$</td>
            <td>$[L] \\quad (\\text{km} \\text{ or } \\text{m})$</td>
            <td>Average distance rainwater travels overland before entering a stream channel</td>
          </tr>
          <tr>
            <td><strong>Stream Frequency ($F_s$)</strong></td>
            <td>$$F_s = \\frac{\\sum N}{A}$$</td>
            <td>$[L^{-2}] \\quad (\\text{km}^{-2})$</td>
            <td>Total number of discrete channel segments per unit basin area</td>
          </tr>
          <tr>
            <td><strong>Bifurcation Ratio ($R_b$)</strong></td>
            <td>$$R_b = \\frac{N_u}{N_{u+1}}$$</td>
            <td>Dimensionless</td>
            <td>Index of tributary branching; controls synchronization of flood peaks</td>
          </tr>
          <tr>
            <td><strong>Ruggedness Number ($R_n$)</strong></td>
            <td>$$R_n = D_d \\cdot H$$</td>
            <td>Dimensionless</td>
            <td>Combines relief ($H$) and drainage density; indicates flash flood hazard</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A watershed basin has a total surface area $A = 160.0\\text{ km}^2$. The total lengths of stream channels by order are: 1st order $= 120.0\\text{ km}$, 2nd order $= 60.0\\text{ km}$, 3rd order $= 36.0\\text{ km}$, and 4th order $= 24.0\\text{ km}$. Calculate: (a) the Drainage Density ($D_d$), (b) the Constant of Channel Maintenance ($C$), and (c) the Mean Length of Overland Flow ($L_g$).
          <div class="pq-ans">✔ Worked Answer: (a) $D_d = 1.50\\text{ km}^{-1}$; (b) $C = 0.667\\text{ km}^2/\\text{km}$; (c) $L_g = 0.333\\text{ km} = 333.3\\text{ m}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Total cumulative stream length $\\sum L = 120.0 + 60.0 + 36.0 + 24.0 = 240.0\\text{ km}$.<br>
            (a) Drainage Density:<br>
            $$D_d = \\frac{\\sum L}{A} = \\frac{240.0\\text{ km}}{160.0\\text{ km}^2} = 1.50\\text{ km}^{-1}$$<br>
            (b) Constant of Channel Maintenance:<br>
            $$C = \\frac{1}{D_d} = \\frac{1}{1.50} \\approx 0.667\\text{ km}^2/\\text{km}$$<br>
            (c) Mean Length of Overland Flow:<br>
            $$L_g = \\frac{1}{2 D_d} = \\frac{1}{2 \\times 1.50} = \\frac{1}{3.00} \\approx 0.3333\\text{ km} = 333.3\\text{ meters}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> How does bedrock permeability directly control drainage density?
          <div class="pq-ans">✔ Correct Answer: High permeability produces low drainage density; low permeability produces high drainage density.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In permeable rock (e.g., porous sandstone or karstified limestone), rainfall infiltrates into the subsurface, leaving little surface runoff to carve stream channels. In impermeable rocks (e.g., clay/shale), all rainfall is forced into overland flow, gouging dense channel networks.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> State Horton's Law of Stream Numbers.
          <div class="pq-ans">✔ Correct Answer: The number of streams of different orders in a given basin tends to form a geometric progression starting with the highest-order stream: $N_u = R_b^{k-u}$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Plotting the logarithm of the number of streams against stream order yields a straight line with slope equal to $-\\log(R_b)$.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Strahler's stream ordering system, what happens when a 1st-order stream joins a 2nd-order stream?
          <div class="pq-ans">✔ Correct Answer: The downstream channel remains a 2nd-order stream.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In Strahler's system, a channel order increases if and only if two streams of the <em>same order</em> join (e.g., $1 + 1 \\to 2$, $2 + 2 \\to 3$). The junction of a lower-order stream with a higher-order stream leaves the higher order unchanged ($1 + 2 \\to 2$).
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What does an exceptionally high Ruggedness Number ($R_n = D_d \\times H$) indicate about a watershed?
          <div class="pq-ans">✔ Correct Answer: It indicates extreme structural dissection, steep slopes, and catastrophic flash-flood vulnerability.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> High relief ($H$) provides gravitational potential energy while high drainage density ($D_d$) rapidly concentrates runoff into trunk streams, producing extreme flood peaks with minimal lag time.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> Why does deforestation or overgrazing trigger an immediate increase in drainage density?
          <div class="pq-ans">✔ Correct Answer: Loss of canopy and root cover reduces infiltration capacity and soil shear strength, allowing sheetwash to rapidly incise new rills and gullies.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Vegetation increases infiltration and physically anchors topsoil. Removing vegetation lowers the critical shear stress required for channel initiation, causing extensive gully incision.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is the difference between Horton's Stream Frequency ($F_s$) and Drainage Density ($D_d$)?
          <div class="pq-ans">✔ Correct Answer: $F_s$ measures the number of stream segments per unit area ($\\text{km}^{-2}$), whereas $D_d$ measures total channel length per unit area ($\\text{km}^{-1}$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Two basins can have identical stream frequencies ($F_s$) but vastly different drainage densities if one basin has much longer stream channels.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> In hydrogeology, how does drainage density correlate with groundwater recharge potential?
          <div class="pq-ans">✔ Correct Answer: Inversely; areas with low drainage density generally possess high infiltration capacity and superior groundwater recharge potential.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When drainage density is low, precipitation spends more time as overland flow and percolates into aquifers rather than being swiftly evacuated by stream channels.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=8,
    filename="Q008_Drainage_Density_Horton_Basin_Morphometry_Complete_Guide.html",
    title="Q008: Drainage Density, Horton's Basin Morphometry & Fluvial Hydrology",
    badge="GGM - 2/2019 • Fluvial Geomorphology & Hydrology",
    h1_title="Q008: Mathematical Physics of Drainage Density: Horton's Laws & Basin Morphometry",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 8<br><strong>Authoritative References:</strong> Robert E. Horton (<em>GSA Bulletin</em>, 1945); Arthur N. Strahler (<em>GSA Bulletin</em>, 1957); K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 27)",
    part1_html=q8_part1,
    part2_html=q8_part2,
    part3_html=q8_part3
)

# ==========================================
# QUESTION 9: MORAINES - GLACIAL ENVIRONMENT
# ==========================================
q9_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Glacial Deposition Dynamics & Moraine Architecture</div>
    <div class="card-body">
      <p>A <strong>moraine</strong> is a distinctive landform constructed of <strong>till</strong> (or unstratified <strong>diamicton</strong>)—an unsorted, unstratified, polymictic accumulation of subangular to faceted rock debris ranging in size from microscopic pulverized rock flour to house-sized erratic boulders—deposited directly by the movement, melting, or standstill of a glacier. Moraines are diagnostic and exclusive landforms of the <strong>glacial environment</strong>.</p>

      <div class="quote-box bangar">
        "The loose rock waste, boulders, and pulverized clay transported and dumped directly by moving or melting glaciers is known as glacial till or boulder clay. The linear ridges and mounds formed by the accumulation of such unsorted glacial debris are called <strong>moraines</strong>. Depending upon their position relative to the glacier, they are classified as lateral, medial, terminal (end), recessional, and ground moraines."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Glacial Landforms & Moraines, p. 32)</span>
      </div>

      <p>Morphogenetically, moraines are classified into distinct structural categories based on their position relative to the ice body:</p>
      <ul>
        <li><strong>Lateral Moraines:</strong> Prominent ridge-like embankments of debris deposited along the lateral margins of a valley glacier, supplied by freeze-thaw frost wedging and mass wasting of the flanking valley rock walls.</li>
        <li><strong>Medial Moraines:</strong> A dark stripe or ridge of debris running down the center of a glacier trunk, formed where two lateral moraines coalesce at the confluence of two merging tributary valley glaciers.</li>
        <li><strong>Terminal / End Moraines:</strong> A prominent, arcuate, transverse crescentic ridge dumped at the snout (terminus) of an advancing glacier, marking the maximum forward position attained by the ice front during a steady state (where rate of forward ice movement equals rate of ablation).</li>
        <li><strong>Recessional Moraines:</strong> Transverse ridges deposited behind the terminal moraine during temporary standstills or minor readvances during overall glacial retreat.</li>
        <li><strong>Ground Moraines (Till Plains):</strong> A widespread, blanket-like undulating sheet of subglacial lodgement till smeared across the bedrock floor beneath the melting glacier.</li>
        <li><strong>Push Moraines:</strong> Subaerial ridges formed by the mechanical bulldozing and buckling of proglacial sediment sheets by a surging or readvancing ice lobe.</li>
      </ul>

      <!-- TEXTBOOK IMAGE 1 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q009/bangar_p32_glacial_moraines_till.png" alt="K.M. Bangar Types of Glacial Moraines">
        <div class="tb-caption">
          <strong>Figure 9.1: Morphogenetic Classification of Glacial Moraines (K.M. Bangar, p. 32).</strong> Perspective view of an alpine valley glacier showing lateral moraines along valley sides, a medial moraine at glacial junction, and terminal/end moraines dumped at the melting snout.
        </div>
      </div>

      <!-- TEXTBOOK IMAGE 2 -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q009/boggs_fig8_32_glacial_moraine_deposits.png" alt="Sam Boggs Jr Glacial Depositional Systems and Moraines">
        <div class="tb-caption">
          <strong>Figure 9.2: Glacial Depositional Environments & Sedimentary Architecture (Sam Boggs Jr., Fig. 8.32).</strong> Cross-sectional model illustrating lodgement till, ablation till, moraine ridges, outwash plains (sandurs), and kettle lakes.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Sedimentological Properties of Glacial Till vs. Fluvioglacial Drift</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Property</th>
            <th>Glacial Till (Moraine)</th>
            <th>Fluvioglacial Drift (Outwash / Esker)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Depositional Agent</strong></td>
            <td>Direct passive melting or lodgement from <strong>ice</strong></td>
            <td>Transport and deposition by <strong>glacial meltwater streams</strong></td>
          </tr>
          <tr>
            <td><strong>Grain-Size Sorting</strong></td>
            <td>Extremely poorly sorted (Bimodal/Polymodal diamicton)</td>
            <td>Moderately to well sorted (Gravels and sands)</td>
          </tr>
          <tr>
            <td><strong>Stratification / Bedding</strong></td>
            <td>Completely unstratified and structureless</td>
            <td>Prominently cross-bedded, planar-bedded, laminated</td>
          </tr>
          <tr>
            <td><strong>Clast Morphology & Striations</strong></td>
            <td>Subangular, bullet-shaped, faceted, polished, striated clasts</td>
            <td>Rounded to subrounded; striations erased by fluvial abrasion</td>
          </tr>
          <tr>
            <td><strong>Clast Fabric / Imbrication</strong></td>
            <td>Long axes ($a$-axis) aligned parallel to glacier flow direction</td>
            <td>Upstream imbrication dipping against meltwater flow direction</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q9_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 9)</div>
    <div class="q-stmt">
      9. Moraines are formed in :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Lacustrine Environment</div>
      <div class="raw-opt correct">(B) Glacial Environment &nbsp;✔</div>
      <div class="raw-opt">(C) Alluvial Environment</div>
      <div class="raw-opt">(D) Marine Environment</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Glacial Environment</div>
      <div class="sub">
        In physical geology, sedimentology, and geomorphology (K.M. Bangar, p. 32; Sam Boggs Jr., p. 275; Arthur Holmes, p. 542), <strong>moraines</strong> are universally recognized as primary diagnostic depositional landforms of the <strong>Glacial Environment</strong>.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Lacustrine Environment</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A lacustrine environment represents a standing lake basin dominated by low-energy suspension settling of fine clay, horizontally laminated silt, varves, and small deltaic sand bodies. Moraine ridges composed of unstratified boulder till cannot form in lacustrine environments.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Glacial Environment</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Moraines are constructed directly by glacial ice dumping, pushing, or plastering unsorted rock debris (till/diamicton) at the margins, snout, and bed of active or retreating glaciers. They are the quintessential depositional landform of glaciated terrains.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Alluvial Environment</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Alluvial environments are governed by running river water, characterized by sorted and stratified gravels, sands, point bars, natural levees, and floodplain silts. Running water sorts particles by hydraulic equivalence, preventing the formation of unsorted morainic till.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Marine Environment</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Marine environments produce fossiliferous, horizontally bedded sands, muds, and carbonates across shelf, slope, and abyssal plain settings. While floating icebergs can drop dropstones into glaciomarine muds, terrestrial moraine ridge complexes do not develop in marine environments.
    </div>
  </div>
"""

q9_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Glacial Depositional Landform Assemblage</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Glacial Landform</th>
            <th>Primary Material</th>
            <th>Depositional Sub-environment</th>
            <th>Morphological Diagnostic Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Terminal Moraine</strong></td>
            <td>Unsorted Till (Diamicton)</td>
            <td>Ice-contact / Glacial terminus</td>
            <td>Crescentic transverse ridge marking maximum ice advance</td>
          </tr>
          <tr>
            <td><strong>Drumlin</strong></td>
            <td>Compacted Lodgement Till</td>
            <td>Subglacial</td>
            <td>Streamlined, teardrop-shaped hill with steep stoss and gentle lee</td>
          </tr>
          <tr>
            <td><strong>Esker</strong></td>
            <td>Stratified Sand and Gravel</td>
            <td>Subglacial meltwater tunnel</td>
            <td>Sinuous, snake-like winding ridge</td>
          </tr>
          <tr>
            <td><strong>Kame & Kame Terrace</strong></td>
            <td>Stratified Sand and Gravel</td>
            <td>Ice-marginal meltwater delta/pond</td>
            <td>Flat-topped mound or terrace flanking valley walls</td>
          </tr>
          <tr>
            <td><strong>Outwash Plain (Sandur)</strong></td>
            <td>Braided stream gravels and sands</td>
            <td>Proglacial fluvioglacial zone</td>
            <td>Broad, gently sloping stratified alluvial braidplain</td>
          </tr>
          <tr>
            <td><strong>Kettle Hole / Lake</strong></td>
            <td>Glaciolacustrine silt & peat</td>
            <td>Moraine or outwash plain</td>
            <td>Circular collapse depression formed by melting of buried stagnant ice</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1:</strong> What is the fundamental sedimentological and mechanical difference between "Lodgement Till" and "Ablation Till"?
          <div class="pq-ans">✔ Correct Answer: Lodgement till is deposited subglacially under extreme ice overburden pressure (highly compacted, overconsolidated, fissile); ablation till is let down loosely during melting (uncompacted, washed).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Lodgement till is plastered onto bedrock beneath moving ice, resulting in very high dry density and preferential clast orientation parallel to ice flow. Ablation till is released supraglacially as ice melts, lacking overconsolidation.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> How does a Drumlin differ from a Roche Moutonnée in both origin and slope orientation?
          <div class="pq-ans">✔ Correct Answer: A drumlin is a depositional till mound (steep stoss facing up-ice, gentle lee pointing down-ice); a roche moutonnée is an erosional bedrock knob (gentle abraded stoss facing up-ice, steep plucked lee pointing down-ice).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Drumlins streamline with their tails pointing down-glacier. Roches moutonnées have a gentle, striated stoss side polished by abrasion, and a jagged, steep lee side plucked by freeze-thaw quarrying.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What are "striations" and "chattermarks", and what vital paleogeographic information do they provide?
          <div class="pq-ans">✔ Correct Answer: Linear scratches and crescentic gouges carved into bedrock by rock fragments dragged by glacier ice; they record the exact direction of ancient ice movement.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The orientation of parallel striations gives the ice-flow axis, while crescentic fractures (chattermarks) convex down-ice reveal the absolute flow direction.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Quaternary stratigraphy, how are Terminal Moraines used to reconstruct ancient Pleistocene ice sheet margins?
          <div class="pq-ans">✔ Correct Answer: They delineate the maximum extent of continental ice sheets during major glacial stadials (e.g., the Last Glacial Maximum).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Long, continuous terminal moraine ridges across North America and Europe mark the equilibrium limit of the Laurentide and Fennoscandian ice sheets during the Wisconsinan/Würm glaciation.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is a "glacial erratic"?
          <div class="pq-ans">✔ Correct Answer: A boulder or rock fragment transported by a glacier and deposited on bedrock of completely different lithological composition.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Erratics can be traced back to their source pluton or outcrop (provenance studies), allowing geologists to map regional ice transport trajectories.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> In geotechnical engineering, why does lodgement till make an exceptionally stable foundation for heavy structures, whereas ablation till presents settlement hazards?
          <div class="pq-ans">✔ Correct Answer: Lodgement till has been heavily preconsolidated under thousands of meters of ice overburden pressure, yielding high shear strength and low compressibility.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Glacial loading acted as a massive natural pre-loading mechanism, giving lodgement till high bearing capacity ($>400 - 800\\text{ kPa}$).
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is an "Esker", and how is it recognized in the field?
          <div class="pq-ans">✔ Correct Answer: A long, narrow, sinuous, steep-sided ridge composed of stratified sand and gravel deposited by a subglacial meltwater river tunnel.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When the surrounding ice melts away, the gravel and sand deposited in the ice tunnel are left standing as a snake-like ridge, often running for tens of kilometers across the landscape.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> What is a "push moraine", and what glaciological condition does it diagnose?
          <div class="pq-ans">✔ Correct Answer: A ridge produced by tectonic-like thrusting and folding of proglacial sediment by a surging or readvancing glacier snout.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Readvancing glaciers act as bulldozers, compressively deforming and stacking un-thawed proglacial sediments into imbricate thrust sheets.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=9,
    filename="Q009_Glacial_Moraines_Till_Diamicton_Complete_Guide.html",
    title="Q009: Glacial Moraines, Till Dynamics & Glacial Depositional Environments",
    badge="GGM - 2/2019 • Glacial Geology & Sedimentology",
    h1_title="Q009: Genesis and Architecture of Glacial Moraines: Till Dynamics & Landforms",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 9<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 32); Sam Boggs Jr. (<em>Sedimentology & Stratigraphy</em>, Ch. 8, pp. 275–282); Arthur Holmes (<em>Principles of Physical Geology</em>, Ch. 18)",
    part1_html=q9_part1,
    part2_html=q9_part2,
    part3_html=q9_part3
)

# ==========================================
# QUESTION 10: KARST TOPOGRAPHY - LIMESTONE
# ==========================================
q1_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Chemical Dissolution Thermodynamics of Karst Landscapes</div>
    <div class="card-body">
      <p><strong>Karst topography</strong> is a distinctive landscape produced primarily by the chemical dissolution of soluble carbonate bedrock, overwhelmingly <strong>limestone</strong> (calcium carbonate, $\\text{CaCO}_3$) and dolostone (calcium-magnesium carbonate, $\\text{CaMg(CO}_3)_2$). Karst terrains are characterized by subterranean drainage networks, sinking streams, sinkholes (dolines), caves, dry valleys, and residual towers, named after the classic Kras (Karst) plateau of Slovenia and Italy.</p>

      <div class="quote-box bangar">
        "Karst topography refers to a distinctive type of landscape formed by the solvent action of groundwater on soluble carbonate rocks, particularly <strong>limestone</strong>. The landscape is characterized by an abundance of sinkholes, swallow holes, caverns, underground rivers, and the conspicuous absence of normal surface streams. Limestone bearing areas provide the ideal environment for the development of karst features."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Geological Work of Groundwater: Karst Topography, p. 38)</span>
      </div>

      <p>The chemical dissolution of limestone is governed by the reversible <strong>carbonic acid equilibrium</strong>:</p>

      <div class="formula-card">
        <div class="formula-title">Thermodynamic Carbonic Acid Dissolution of Calcite (Ford & Williams, 2007)</div>
        $$\\text{CO}_2\\text{ (gas)} + \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}_2\\text{CO}_3\\text{ (aqueous carbonic acid)}$$
        $$\\text{CaCO}_3\\text{ (calcite)} + \\text{H}_2\\text{CO}_3 \\rightleftharpoons \\text{Ca}^{2+} + 2\\text{HCO}_3^-\\text{ (calcium & bicarbonate in solution)}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">As rainwater percolates through biogenic soil layers, microbial respiration enriches soil air $p\\text{CO}_2$ up to $10 - 100\\times$ atmospheric levels ($0.03\\% \\to 1 - 3\\% \\text{ CO}_2$). The highly aggressive acidic groundwater dissolves calcite along joint and bedding planes, widening them into cavernous subterranean conduits.</p>
      </div>

      <p>Four primary lithological and structural prerequisites govern the development of mature karst topography:</p>
      <ol>
        <li><strong>High-Purity Carbonate Bedrock:</strong> Thick-bedded, dense limestone containing $>80 - 90\\% \\text{ CaCO}_3$. Insoluble clastic impurities (clay, silica) retard dissolution.</li>
        <li><strong>Dense Secondary Permeability (Joints & Fractures):</strong> Pure limestone has low primary intergranular porosity ($<1 - 5\\%$); groundwater circulation requires well-developed orthogonal joint sets and bedding plane partings to initiate solution channels.</li>
        <li><strong>Entrenched Master Drainage & Hydraulic Gradient:</strong> Deeply incised master river valleys flanking the limestone plateau to maintain a low subterranean water table and drive vigorous groundwater flow.</li>
        <li><strong>Abundant Rainfall:</strong> Sufficient precipitation to replenish aggressive, unsaturated solvent water through the unsaturated vadose zone.</li>
      </ol>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q010/bangar_p38_karst_topography_limestone.png" alt="K.M. Bangar Karst Topography Limestone Caves">
        <div class="tb-caption">
          <strong>Figure 10.1: Anatomy of Karst Topography in Limestone (K.M. Bangar, p. 38).</strong> Schematic cross-section showing surface sinkholes (dolines), swallow holes (ponors), blind valleys, solution caverns, stalactites, stalagmites, columns, and emerging resurgences.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Morphological Zonation: Surface vs. Subterranean Karst Landforms</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Karst Landform</th>
            <th>Realm</th>
            <th>Primary Genetic Mechanism</th>
            <th>Diagnostic Field Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lapies / Karren</strong></td>
            <td>Surface</td>
            <td>Subaerial dissolution along bare limestone joints</td>
            <td>Etched, fluted grooves, solution rills, and sharp limestone ribs</td>
          </tr>
          <tr>
            <td><strong>Doline / Sinkhole</strong></td>
            <td>Surface</td>
            <td>Solution subsidence or catastrophic roof collapse</td>
            <td>Funnel-shaped circular depressions ($2\\text{ m} - 500\\text{ m}$ diameter)</td>
          </tr>
          <tr>
            <td><strong>Polje</strong></td>
            <td>Surface</td>
            <td>Massive structural tectonic depression enlarged by dissolution</td>
            <td>Vast, flat-bottomed karst plain enclosed by steep limestone walls</td>
          </tr>
          <tr>
            <td><strong>Swallow Hole (Ponor)</strong></td>
            <td>Transition</td>
            <td>Disappearance of surface stream underground</td>
            <td>Chasm or funnel where an active river plunges into a subterranean conduit</td>
          </tr>
          <tr>
            <td><strong>Cave / Cavern</strong></td>
            <td>Subterranean</td>
            <td>Phreatic & vadose groundwater dissolution along joints</td>
            <td>Interconnected underground chambers and solution galleries</td>
          </tr>
          <tr>
            <td><strong>Speleothems</strong></td>
            <td>Subterranean</td>
            <td>Degassing of $\\text{CO}_2$ causing calcite reprecipitation</td>
            <td>Stalactites (ceiling-down), stalagmites (floor-up), columns, flowstone</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q10_part2 = """
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC Assistant Geologist 2019 Paper-II (Question 10)</div>
    <div class="q-stmt">
      10. Karst topography is most commonly developed in :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Shale bearing areas</div>
      <div class="raw-opt">(B) Sandstone bearing areas</div>
      <div class="raw-opt">(C) Laterite bearing areas</div>
      <div class="raw-opt correct">(D) Limestone bearing areas &nbsp;✔</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (D) Limestone bearing areas</div>
      <div class="sub">
        In physical geology, hydrogeology, and geomorphology (K.M. Bangar, p. 38; Arthur L. Bloom, p. 156; Ford & Williams, 2007; W.D. Thornbury, p. 317), <strong>karst topography</strong> is universally and fundamentally developed in <strong>Limestone bearing areas</strong> due to the high chemical solubility of calcium carbonate in carbonic acid.
      </div>
    </div>
  </div>

  <!-- OPTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Shale bearing areas</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Shale is an argillaceous sedimentary rock composed of insoluble clay minerals (illite, smectite, kaolinite) and silt. Because shale is virtually impermeable and chemically insoluble in carbonic acid, it does not dissolve to form subterranean drainage or caves. Instead, shale weathers mechanically into badlands, rolling plains, or impermeable aquitards.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Sandstone bearing areas</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Sandstone consists primarily of quartz ($\\text{SiO}_2$), which is exceptionally insoluble in natural surface waters at normal environmental pH ($<9$). While rare "pseudokarst" features can develop in tropical quartzite through grain-boundary leaching over millions of years, true karst topography requires carbonate solubility.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Laterite bearing areas</span>
      <span class="tag wrong">Incorrect Distractor</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Laterite is a highly weathered, residual tropical regolith enriched in insoluble iron oxides (goethite, hematite) and aluminum hydroxides (gibbsite, bauxite) formed by the leaching of silica. It forms hard, porous duricrusts (ferricrete) that weather into plateaus and mesas, lacking karst dissolution systems.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) Limestone bearing areas</span>
      <span class="tag correct">Correct Verified Option</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Limestone (composed of calcite, $\\text{CaCO}_3$) is readily soluble in natural meteoric water charged with dissolved carbon dioxide (forming weak carbonic acid, $\\text{H}_2\\text{CO}_3$). This chemical dissolution dissolves joint systems, excavates subterranean caverns, causes surface collapse into sinkholes, and diverts entire surface river networks underground, creating the classic <strong>karst topography</strong>.
    </div>
  </div>
"""

q10_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Speleothem Morphology & Precipitation Physics</div>
    <div class="card-body">
      <p>Speleothems (cave mineral formations) develop in the vadose (unsaturated) zone of limestone caves when dripping groundwater degasses carbon dioxide into the cave air:</p>
      $$\\text{Ca}^{2+} + 2\\text{HCO}_3^- \\xrightarrow{\\text{degassing of } \\text{CO}_2} \\text{CaCO}_3\\downarrow \\text{ (solid calcite)} + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}$$
      <ul>
        <li><strong>Stalactite (Ceiling-Down):</strong> Icicle-like speleothem hanging from the cave ceiling. Originates as a thin-walled, hollow tubular "soda straw" through whose central canal water drips, depositing calcite rings along its lip.</li>
        <li><strong>Stalagmite (Floor-Up):</strong> Solid, rounded, inverted-cone speleothem growing upward from the cave floor. Formed by calcite precipitation from water droplets splashing down from the ceiling; lacks a central hollow canal.</li>
        <li><strong>Column / Pillar:</strong> Formed when a descending stalactite and an ascending stalagmite meet and merge into a single continuous vertical column.</li>
        <li><strong>Helictites:</strong> Curved, contorted, gravity-defying speleothems whose growth direction is governed by capillary forces and crystal lattice orientation rather than gravity.</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Questions & Worked Derivations (8 Problems)</div>
    <div class="card-body">
      <ul class="pq-list">
        <li>
          <strong>Practice Q1 (Numerical):</strong> A limestone drainage basin covers an area $A = 80.0\\text{ km}^2$ with an annual runoff of $Q = 0.50\\text{ m/yr}$. Chemical analysis of the emerging spring water shows a dissolved calcium ion concentration $[\\text{Ca}^{2+}] = 48.0\\text{ mg/L}$. Assuming all dissolved calcium originates from pure limestone ($\\text{CaCO}_3$, density $\\rho = 2650\\text{ kg/m}^3$), calculate the total mass of limestone removed annually in metric tons and the basin-wide chemical denudation rate in millimeters per thousand years ($\\text{mm/ka}$, Bubnoff units).
          <div class="pq-ans">✔ Worked Answer: Total mass removed $= 4,800\\text{ metric tons/yr}$; Denudation rate $\\approx 22.6\\text{ mm/ka}$.</div>
          <div class="pq-exp">
            <strong>Derivation:</strong><br>
            Annual water discharge volume $V = A \\times Q = 80.0 \\times 10^6\\text{ m}^2 \\times 0.50\\text{ m} = 40.0 \\times 10^6\\text{ m}^3 = 40.0 \\times 10^9\\text{ Liters}$.<br>
            Molar mass of $\\text{Ca}^{2+} = 40.08\\text{ g/mol}$; Molar mass of $\\text{CaCO}_3 = 100.09\\text{ g/mol}$.<br>
            Mass conversion factor: $\\frac{100.09}{40.08} \\approx 2.50$.<br>
            $$\\text{Concentration of CaCO}_3 = 48.0\\text{ mg/L} \\times 2.50 = 120.0\\text{ mg/L} = 0.120\\text{ kg/m}^3$$<br>
            Total annual mass removed:<br>
            $$M = 40.0 \\times 10^6\\text{ m}^3 \\times 0.120\\text{ kg/m}^3 = 4,800,000\\text{ kg} = 4,800\\text{ metric tons/yr}$$<br>
            Volume of solid limestone removed:<br>
            $$V_{\\text{rock}} = \\frac{4,800,000\\text{ kg}}{2650\\text{ kg/m}^3} \\approx 1811.32\\text{ m}^3$$<br>
            Surface lowering rate:<br>
            $$\\text{Rate} = \\frac{V_{\\text{rock}}}{A} = \\frac{1811.32\\text{ m}^3}{80.0 \\times 10^6\\text{ m}^2} = 2.264 \\times 10^{-5}\\text{ m/yr} = 0.02264\\text{ mm/yr} \\approx 22.64\\text{ mm/ka}$$
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is the phenomenon of "Mixing Corrosion" (Mischungskorrosion / Bögli effect) in karst hydrology?
          <div class="pq-ans">✔ Correct Answer: When two distinct saturated groundwater masses with different carbon dioxide concentrations mix, the resulting mixture becomes chemically undersaturated and capable of aggressively dissolving more limestone.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the equilibrium saturation curve for calcite is non-linear (concave upward with respect to $p\\text{CO}_2$), mixing two saturated waters produces a combined solution that is undersaturated, driving rapid cavern excavation deep below the water table.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> Distinguish between a "Solution Sinkhole" and a "Collapse Sinkhole".
          <div class="pq-ans">✔ Correct Answer: A solution sinkhole forms by gradual downward dissolution along joints; a collapse sinkhole forms by catastrophic structural failure of an underlying cavern roof.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Solution sinkholes develop slowly and gently. Collapse sinkholes occur suddenly when the void beneath becomes too large to support the weight of the overlying rock ceiling, creating vertical-walled craters.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> What is "Tower Karst" (Mogotes / Kegelkarst), and in what climatic zone does it achieve its most spectacular development?
          <div class="pq-ans">✔ Correct Answer: Residual steep-sided limestone towers rising vertically from flat alluvial plains, developed in humid tropical and subtropical climates (e.g., Guilin in China, Krabi/Phang Nga in Thailand).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Abundant tropical heat and intense monsoonal rains accelerate biochemical weathering, while lateral planation by surface rivers erodes tower bases.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> Why does a stalactite possess a central hollow feeding canal (soda straw), whereas a stalagmite is solid?
          <div class="pq-ans">✔ Correct Answer: A stalactite grows as water flows through its central tube, depositing calcite rings along its rim; a stalagmite grows from splashing water droplets hitting the floor, depositing solid layers.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Droplets hang from the ceiling, releasing $\\text{CO}_2$ and depositing a microscopic ring around the droplet margin. On the floor, the kinetic impact of falling drops splashes water radially, building a solid mound.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What is a "Blind Valley" in karst geomorphology?
          <div class="pq-ans">✔ Correct Answer: A valley carved by a surface stream that ends abruptly at a cliff or sinkhole (ponor) where the stream sinks completely underground.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Typically occurs where an impermeable rock formation meets a soluble limestone block; the surface stream cannot flow past the contact, plunging into subterranean caverns.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> What is a "Polje", and why is it of critical importance in karst landscapes?
          <div class="pq-ans">✔ Correct Answer: A massive, flat-bottomed, fault-bounded structural karst depression (often tens of kilometers wide), drained by ponors and subject to seasonal inundation.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Poljes are the largest individual karst features on Earth, providing fertile agricultural soils on their flat, terra-rossa covered floors in otherwise barren limestone plateaus.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> In engineering geology, what are the primary foundation hazards when building dams or reservoirs in limestone karst terrain?
          <div class="pq-ans">✔ Correct Answer: Severe water leakage through undiscovered subterranean cavern conduits and catastrophic reservoir sinkhole collapse.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Impounding water increases hydraulic head, forcing water through hidden karst solution cavities, which can wash out clay fillings and completely drain the reservoir (e.g., the Lar Dam in Iran).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""

generate_page(
    q_num=10,
    filename="Q010_Karst_Topography_Limestone_Dissolution_Complete_Guide.html",
    title="Q010: Karst Topography, Carbonate Dissolution & Speleothem Morphogenesis",
    badge="GGM - 2/2019 • Hydrogeology & Karst Geomorphology",
    h1_title="Q010: Chemical Dynamics of Karst Topography: Limestone Dissolution & Cavern Evolution",
    meta_text="<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2019), Question 10<br><strong>Authoritative References:</strong> K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 38); Derek Ford & Paul Williams (<em>Karst Hydrogeology and Geomorphology</em>, 2007); Arthur L. Bloom (<em>Geomorphology</em>, Ch. 7)",
    part1_html=q1_part1,
    part2_html=q10_part2,
    part3_html=q10_part3
)

print("Batch 1 (Q006 - Q010) generated successfully.")
