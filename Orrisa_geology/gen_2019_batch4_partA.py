#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 36 to 40
Assam DGMS 2019 Masterclass Standard
"""

from masterclass_generator_core import generate_page

# ==========================================
# QUESTION 36: EXFOLIATING WEATHERING IN MASSIVE ROCKS
# ==========================================
q36_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Mechanical Weathering: Exfoliation, Spheroidal Spalling & Rock Fabric</div>
    <div class="card-body">
      <p>Weathering processes break down bedrock through physical disintegration and chemical decomposition. Among physical weathering phenomena, <strong>exfoliation</strong> (also termed <em>onion-skin weathering</em> or <em>flaking</em>) is the process whereby curved, concentric outer shells or sheets of rock spall and peel away from the core of a rock mass.</p>
      
      <ul>
        <li><strong>Structural Requirement:</strong> Exfoliation operates with maximum efficiency in <strong>massive, unstratified, isotropic rocks</strong> (such as massive granites, granodiorites, gabbros, and thick homogeneous sandstones). Because massive rocks lack pre-existing planar weaknesses (bedding planes, cleavage, or schistosity), internal thermal and mechanical stresses cannot be dissipated along planar fractures. Instead, stresses accumulate isotropically until concentric curvilinear failure surfaces develop parallel to the external rock surface.</li>
        <li><strong>Ineffectiveness in Layered / Foliated / Jointed Rocks:</strong>
          <ul>
            <li>In <em>layered</em> (stratified) or <em>foliated</em> (schists, slates, gneisses) rocks, weathering is guided almost entirely along pre-existing laminae and foliation planes, causing splitting into flat slabs (slabbing/fissility) rather than curved concentric exfoliation shells.</li>
            <li>In heavily <em>jointed rocks</em>, block disintegration along intersecting joint planes isolates angular boulders without producing the massive, curved exfoliated domes characteristic of massive plutons.</li>
          </ul>
        </li>
        <li><strong>Driving Mechanisms:</strong> Exfoliation in massive rocks is driven by two synergistic processes:
          <ol>
            <li><strong>Thermal Insolation & Diurnal Fluctuations:</strong> Rock is an exceptionally poor conductor of heat. Intense solar radiation rapidly expands the outer few centimeters of a rock surface, while the interior remains cold and unexpanded. Differential expansion creates severe shear stresses parallel to the surface, causing curved flakes to spall off.</li>
            <li><strong>Chemical Spheroidal Weathering:</strong> Water penetrates micro-fissures, hydrolyzing feldspars into clay minerals (kaolinite). The formation of clay increases volume by $10-20\\%$, exerting outward expansive pressure that pops off concentric shells around a core-stone.</li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Exfoliation:</strong> The peeling off of curved concentric shells or layers from the surface of a rock mass is called exfoliation. It is particularly effective in <strong>massive rocks</strong> like granites and massive sandstones. In massive rocks devoid of bedding planes or joints, daily temperature variations produce differential expansion between outer and inner layers, causing the rock to peel like the coats of an onion."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Weathering of Rocks: Exfoliation & Spheroidal Weathering, p. 20)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Thermal Stress & Volumetric Expansion in Massive Rocks</div>
        $$\\sigma_{\\text{thermal}} = \\frac{E \\cdot \\alpha_T \\cdot \\Delta T}{1 - \\nu} \\quad (\\text{Biaxial Thermal Stress at Rock Surface})$$
        $$\\Delta V_{\\text{hydration}} = \\frac{V_{\\text{clay}} - V_{\\text{feldspar}}}{V_{\\text{feldspar}}} \\times 100\\% \\approx +15\\% \\text{ to } +25\\%$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $E$ is Young's modulus ($\approx 50\\text{ GPa}$ for granite), $\\alpha_T$ is thermal expansion coefficient ($\approx 8 \\times 10^{-6}\\text{ K}^{-1}$), $\\Delta T$ is diurnal temperature swing ($30-40^\\circ\\text{C}$ in arid regions), and $\\nu$ is Poisson's ratio ($0.25$). Thermal stresses can exceed $60-80\\text{ MPa}$, easily surpassing the tensile strength of granite ($5-10\\text{ MPa}$).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q036/bangar_p20_exfoliation_weathering_massive_rocks.png" alt="K.M. Bangar Spheroidal Weathering and Exfoliation in Massive Rocks">
        <div class="tb-caption">
          <strong>Figure 36.1: Exfoliation & Spheroidal Spalling in Massive Rocks (K.M. Bangar, p. 20).</strong> Concentric curved shells peeling away from core-stones in massive granite due to combined diurnal thermal stresses and chemical hydration expansion.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Weathering Modes Governed by Rock Fabric & Internal Discontinuities</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Rock Fabric / Type</th>
            <th>Internal Structural Discontinuities</th>
            <th>Dominant Physical Weathering Mode</th>
            <th>Resulting Landform / Product</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Massive Rocks</strong></td>
            <td><strong>None (Homogeneous, unstratified, isotropic)</strong></td>
            <td><strong>Exfoliation (Spalling of concentric shells)</strong></td>
            <td><strong>Exfoliation domes, bornhardts, rounded tors, core-stones</strong></td>
          </tr>
          <tr>
            <td><strong>Layered Rocks</strong></td>
            <td>Bedding planes ($S_0$), laminations</td>
            <td>Planar bedding parting, sheeting along strata</td>
            <td>Flagstones, cuestas, step-like ledges, mesas</td>
          </tr>
          <tr>
            <td><strong>Foliated Rocks</strong></td>
            <td>Continuous slaty cleavage, schistosity ($S_1$)</td>
            <td>Fissile cleavage splitting (Delamination)</td>
            <td>Slaty chips, needle-like scree, jagged arêtes</td>
          </tr>
          <tr>
            <td><strong>Jointed Rocks</strong></td>
            <td>Intersecting orthogonal joint sets</td>
            <td>Block disintegration / wedging</td>
            <td>Talus slopes, felsenmeer (block fields), scree aprons</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q36_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q036</div>
    <div class="q-stmt">The process of weathering by exfoliating activity is very effective in:</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Layered rocks</div>
      <div class="raw-opt correct">(B) Massive rocks</div>
      <div class="raw-opt">(C) Jointed rocks</div>
      <div class="raw-opt">(D) Foliated rocks</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (B) Massive rocks</div>
      <div class="sub">Verified against Bangar (p. 20), Mahapatra (Textbook of Geology, p. 45), and Mukherjee (p. 28). Exfoliation is uniquely effective in massive, isotropic rocks (e.g., granites and massive sandstones) because the absence of bedding or foliation allows thermal and hydration stresses to spall off concentric curved shells.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Layered rocks</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> In layered (sedimentary) rocks, weathering stresses are immediately accommodated along pre-existing bedding planes. As water freezes or salts crystallize, the rock separates into flat, tabular slabs parallel to the strata, precluding the formation of curved concentric exfoliation shells.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Massive rocks</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Massive rocks lack continuous planes of weakness such as bedding, cleavage, or dense joints. Consequently, thermal gradients (insolation) and chemical hydration volume changes cannot dissipate along planes; instead, they generate uniform, curved tensile stresses parallel to the external rock surface. This causes outer curved slabs to detach sequentially, producing the classic exfoliation domes, tors, and core-stones seen across massive granite plutons globally.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Jointed rocks</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> In heavily jointed rocks, weathering proceeds predominantly via <em>block disintegration</em>. Freeze-thaw cycles (frost wedging) and plant roots wedge apart discrete, angular blocks bounded by joint sets, yielding angular scree and talus rather than continuous peeling of curved shells.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Foliated rocks</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Foliated metamorphic rocks (schists, slates, phyllites) possess high directional anisotropy due to parallel-aligned platy phyllosilicate minerals (micas, chlorite). Weathering stresses exploit these planes of minimum tensile strength, producing fissility and jagged platy flakes, completely inhibiting concentric curved exfoliation.
    </div>
  </div>
"""

q36_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Mechanical Breakdown Mechanisms Across Rock Fabrics</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Weathering Type</th>
            <th>Primary Trigger</th>
            <th>Fabric Control</th>
            <th>Characteristic Morphology</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Exfoliation</strong></td>
            <td>Thermal insolation / pressure release</td>
            <td><strong>Massive, isotropic crystalline rocks</strong></td>
            <td>Curved concentric shells, bornhardt domes</td>
          </tr>
          <tr>
            <td><strong>Spheroidal Weathering</strong></td>
            <td>Chemical hydration along joints</td>
            <td>Massive blocks bounded by wide joints</td>
            <td>Concentric weathered rinds around core-stones</td>
          </tr>
          <tr>
            <td><strong>Frost Wedging (Gelifraction)</strong></td>
            <td>$9\\%$ volumetric expansion of ice in fissures</td>
            <td>Any jointed or fractured rock</td>
            <td>Angular felsenmeer, scree talus slopes</td>
          </tr>
          <tr>
            <td><strong>Salt Haloclasty</strong></td>
            <td>Crystallization pressure of salts in pores</td>
            <td>Porous sandstones and volcanic tuffs</td>
            <td>Tafoni, alveolar weathering, honeycomb cavities</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Weathering Mechanics & Rock Fabrics</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Calculation of Ice Crystallization Pressure in Joints</div>
        <div class="pq-ans">Maximum theoretical frost wedging pressure $P \\approx 200\\text{ MPa}$ at $-22^\\circ\\text{C}$</div>
        <div class="pq-exp">When confined water freezes, it expands by $9\\%$. At $-22^\\circ\\text{C}$, the ice-water phase equilibrium pressure reaches $\\approx 210\\text{ MPa}$, far exceeding the compressive strength of any known rock ($100-200\\text{ MPa}$), violently forcing joint blocks apart.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Role of Chemical Alteration in Spheroidal Weathering</div>
        <div class="pq-ans">Hydrolysis of plagioclase into smectite/kaolinite creates expansive lattice stress</div>
        <div class="pq-exp">Chemical weathering attacks the edges and corners of joint blocks faster than flat faces ($3\\times$ faster at corners due to high surface-area-to-volume ratio), rounding angular blocks into spheroids while clay expansion pops off concentric outer layers.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Thermal Conductivity of Granite</div>
        <div class="pq-ans">Low conductivity ($k \\approx 2.5 - 3.0\\text{ W}/(\\text{m}\\cdot\\text{K})$) concentrates thermal stress at surface</div>
        <div class="pq-exp">Because granite conducts heat poorly, diurnal solar heating penetrates less than $5-10\\text{ cm}$. The exterior shell heats to $50^\\circ\\text{C}$ while the interior remains at $20^\\circ\\text{C}$, inducing severe thermal shear stresses that detach surface flakes.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Identification of Bornhardts in Peninsular India</div>
        <div class="pq-ans">Massive Archean granitic domes shaped by sheet exfoliation</div>
        <div class="pq-exp">The bornhardts and whalebacks of Hyderabad, Hampi, and Ramanagara (Karnataka) are massive crystalline inselbergs developed in Archean Closepet and Peninsular Granites via deep chemical weathering followed by stripping and sheet exfoliation.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Goldich Dissolution Series & Mineral Resistance</div>
        <div class="pq-ans">Olivine weathers fastest; Quartz weathers slowest</div>
        <div class="pq-exp">S.S. Goldich (1938) established that mineral susceptibility to chemical weathering is the inverse of Bowen's reaction series: Olivine $\\to$ Augite $\\to$ Hornblende $\\to$ Biotite $\\to$ K-feldspar $\\to$ Muscovite $\\to$ Quartz.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Exfoliation vs. Sheeting Terminology</div>
        <div class="pq-ans">Exfoliation is small-to-medium scale (thermal/chemical); sheeting is large-scale (lithostatic unloading)</div>
        <div class="pq-exp">While both involve spalling of curved slabs parallel to topography, sheeting refers to deep-seated stress relief fractures ($1-10\\text{ m}$ thick) across whole mountains, whereas exfoliation encompasses thin surface peeling ($1-10\\text{ cm}$) driven by insolation and hydration.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Weathering in Foliated Metamorphic Schists</div>
        <div class="pq-ans">Mechanical splitting along schistosity planes (fissility)</div>
        <div class="pq-exp">In mica schists, the continuous orientation of biotite and muscovite creates planes of zero cohesion. Moisture and oxidation attack these cleavage sheets, causing the rock to crumble into thin, pencil-like or platy shards rather than peeling concentrically.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Tafoni and Cavernous Weathering</div>
        <div class="pq-ans">Sub-surface granular disintegration beneath a case-hardened crust</div>
        <div class="pq-exp">In arid and coastal environments, salt crystallization and moisture evaporation hollow out rounded cavities (tafoni) beneath a sun-hardened iron/silica-rich exterior rind, particularly on massive sandstone and granite cliffs.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 37: PELEAN TYPE VOLCANO
# ==========================================
q37_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Volcanological Dynamics: The Pelean Eruption Mechanism & Catastrophic Pyroclastics</div>
    <div class="card-body">
      <p>Volcanic eruptions are categorized globally according to the viscosity of their magmas, gas content (volatiles), eruption column height, and explosivity index. The <strong>Pelean Type</strong> of eruption—named after the catastrophic 1902 eruption of <strong>Mount Pelée</strong> on the Caribbean island of Martinique—represents one of the <strong>most violent, destructive volcanic phenomena on Earth</strong>.</p>
      
      <ul>
        <li><strong>Magma Viscosity & Composition:</strong> Pelean eruptions involve highly polymerized, silica-rich <strong>andesitic, dacitic, or rhyolitic magmas</strong> ($>65\\%\\text{ SiO}_2$) with high dissolved volatile contents ($H_2O, CO_2, SO_2$). Because the viscosity is extraordinarily high, gases cannot exsolve smoothly.</li>
        <li><strong>Lava Domes & Solid Spines:</strong> The magma is so viscous that it often solidifies directly within the volcanic conduit, forming a rigid plug or ascending into a monumental solid lava needle (the famous <em>Spine of Mount Pelée</em> grew to over $300\\text{ m}$ height before collapsing).</li>
        <li><strong>Nuées Ardentes (Pyroclastic Density Currents):</strong> When the gas pressure beneath the solid dome exceeds the tensile strength of the plug, or when the gravitational oversteepened dome collapses, the volcano detonates in a <strong>catastrophic lateral blast</strong>. This generates incandescent, high-speed pyroclastic avalanches of incandescent ash, pumice, and toxic gas termed <strong>nuées ardentes</strong> (glowing avalanches) that race down slopes at speeds exceeding $100-300\\text{ km/h}$ at temperatures $>700-1000^\\circ\\text{C}$ (destroying the city of Saint-Pierre in 1902 within 2 minutes).</li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Pelean Type:</strong> In this type of eruption, the most viscous lava is forced out of the volcanic vent. The lava is so stiff that it solidifies into a huge spine or needle over the vent. The gases trapped beneath escape with <strong>tremendous explosions, producing glowing clouds of incandescent ash and gas called 'nuée ardente'</strong>. It represents the <strong>most violent volcanic activity</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Volcanoes: Types of Volcanic Eruption, p. 49)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Volcanic Explosivity Index (VEI) & Fluid Dynamics of Nuées Ardentes</div>
        $$\\text{Dynamic Pressure of Pyroclastic Surge: } \\quad P_{\\text{dyn}} = \\frac{1}{2} \\rho_{\\text{surge}} v^2 \\approx 10 - 50\\text{ kPa} \\quad (\\text{Sufficient to level concrete buildings})$$
        $$\\text{Volcanic Explosivity Index (VEI): } \\quad \\text{VEI} = 4 - 6 \\quad (\\text{Ejecta volume } 0.1 - 10+\\text{ km}^3, \\text{ Plinian/Pelean class})$$
        $$\\eta_{\\text{dacite}} \\approx 10^7 - 10^9\\text{ Pa}\\cdot\\text{s} \\gg \\eta_{\\text{basalt}} \\approx 10^1 - 10^2\\text{ Pa}\\cdot\\text{s} \\quad (10^7 \\times \\text{ higher viscosity than basalt})$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">High silica polymerization ($[\\text{SiO}_4]^{4-}$ tetrahedral networks) traps expanding gas bubbles, raising overpressure $\\Delta P$ until catastrophic brittle explosive fragmentation occurs.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q037/bangar_p49_pelean_volcano_types.png" alt="K.M. Bangar Pelean Volcano and Nuée Ardente">
        <div class="tb-caption">
          <strong>Figure 37.1: Pelean Type Volcano & Catastrophic Nuée Ardente (K.M. Bangar, p. 49).</strong> Explosive lateral blast blowing out the flank of a volcanic dome, generating a glowing incandescent cloud (nuée ardente) and extruded solid spine.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Classification of Volcanic Eruption Styles</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Eruption Type</th>
            <th>Magma Type</th>
            <th>Viscosity</th>
            <th>Explosivity / Dynamics</th>
            <th>Diagnostic Products</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Hawaiian</strong></td>
            <td>Basaltic ($45-52\\%\\text{ SiO}_2$)</td>
            <td>Very Low ($10^1-10^2\\text{ Pa}\\cdot\\text{s}$)</td>
            <td>Quiet, effusive, non-explosive</td>
            <td>Pahoehoe & Aa flows, lava fountains, shield volcanoes</td>
          </tr>
          <tr>
            <td><strong>Strombolian</strong></td>
            <td>Basaltic to Andesitic</td>
            <td>Low-Moderate</td>
            <td>Rhythmic, mild bursts</td>
            <td>Glowing scoria cinders, bombs, lapilli cones</td>
          </tr>
          <tr>
            <td><strong>Vulcanian</strong></td>
            <td>Andesitic to Dacitic</td>
            <td>Moderate-High</td>
            <td>Violent periodic explosions clearing plugs</td>
            <td>Dense cauliflower ash clouds, breadcrust bombs</td>
          </tr>
          <tr>
            <td><strong>Pelean</strong></td>
            <td><strong>Dacitic to Rhyolitic</strong></td>
            <td><strong>Extremely High ($10^7-10^9\\text{ Pa}\\cdot\\text{s}$)</strong></td>
            <td><strong>Most violent activity; lateral blasts</strong></td>
            <td><strong>Lava domes, spines, nuées ardentes (pyroclastic flows)</strong></td>
          </tr>
          <tr>
            <td><strong>Plinian (Krakatoan)</strong></td>
            <td>Rhyolitic / Pumiceous</td>
            <td>Maximum ($>10^9\\text{ Pa}\\cdot\\text{s}$)</td>
            <td>Cataclysmic vertical gas columns ($>30\\text{ km}$)</td>
            <td>Extensive pumice falls, calderas, global climatic impact</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q37_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q037</div>
    <div class="q-stmt">Pelean type of volcano is known for:</div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Most violent activity</div>
      <div class="raw-opt">(B) Quiet flow</div>
      <div class="raw-opt">(C) Submarine flow</div>
      <div class="raw-opt">(D) Ropy type flow</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (A) Most violent activity</div>
      <div class="sub">Verified against Bangar (p. 49), Mahapatra (p. 55), and Cas & Wright (Volcanic Successions). Pelean eruptions involve extremely viscous, gas-charged dacitic lava that solidifies in the vent and detonates in violent lateral blasts and lethal incandescent nuées ardentes, representing the most violent volcanic activity.</div>
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) Most violent activity</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Pelean-type volcanism is universally recognized by geologists for its <strong>extreme, catastrophic explosivity</strong>. The lava is so stiff that it cannot flow; it forms towering spines and domes that trap subterranean gases at immense overpressures. When failure occurs, explosive disintegration triggers lateral blasts and incandescent pyroclastic surges (nuées ardentes) that completely obliterate everything in their paths, as demonstrated by the lethal eruption of Mt. Pelée in 1902.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Quiet flow</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Quiet, non-explosive effusive flows are characteristic of <strong>Hawaiian-type eruptions</strong> and continental flood basalt fissures (e.g., Deccan Traps). Low-viscosity, gas-poor basaltic lavas flow quietly for tens of kilometers without explosive disintegration.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Submarine flow</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Submarine flows occur at mid-ocean ridges and submarine seamounts, typically producing <strong>pillow basalts</strong> and hyaloclastites due to rapid quenching by sea water. Pelean eruptions are subaerial dome-building and dome-collapse phenomena.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Ropy type flow</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Ropy lava is the diagnostic surface texture of <strong>pahoehoe basalt</strong>, formed when a thin, fluid crust is wrinkled into coiled, rope-like folds by the continuous flow of molten basalt underneath. Pelean lavas are felsic, blocky, and completely devoid of pahoehoe textures.
    </div>
  </div>
"""

q37_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Diagnostic Volcanological Signatures Across Eruption Scales</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Eruption Style</th>
            <th>Type Locality</th>
            <th>Column Height (km)</th>
            <th>Discharge Rate ($m^3/s$)</th>
            <th>Primary Hazard</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Hawaiian</strong></td>
            <td>Kilauea / Mauna Loa, Hawaii</td>
            <td>$&lt; 0.5$</td>
            <td>$10^1 - 10^3$</td>
            <td>Lava flow inundation</td>
          </tr>
          <tr>
            <td><strong>Strombolian</strong></td>
            <td>Stromboli, Aeolian Islands, Italy</td>
            <td>$0.5 - 2.0$</td>
            <td>$10^1 - 10^2$</td>
            <td>Ballistic projectiles, scoria fall</td>
          </tr>
          <tr>
            <td><strong>Vulcanian</strong></td>
            <td>Vulcano, Italy</td>
            <td>$3 - 15$</td>
            <td>$10^3 - 10^5$</td>
            <td>Breadcrust bombs, widespread tephra fall</td>
          </tr>
          <tr>
            <td><strong>Pelean</strong></td>
            <td><strong>Mount Pelée, Martinique (1902)</strong></td>
            <td><strong>$5 - 20$ (Lateral Blasts)</strong></td>
            <td><strong>$10^4 - 10^6$</strong></td>
            <td><strong>Lethal nuées ardentes (pyroclastic density currents)</strong></td>
          </tr>
          <tr>
            <td><strong>Plinian</strong></td>
            <td>Vesuvius (79 AD) / Pinatubo (1991)</td>
            <td>$20 - 50+$</td>
            <td>$10^6 - 10^9$</td>
            <td>Global aerosol cooling, pumice fall, caldera collapse</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Volcanology & Pelean Eruptions</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Calculation of Pyroclastic Density Current Velocity</div>
        <div class="pq-ans">PDC speed $v = \\sqrt{2 g \\Delta \\rho / \\rho \\cdot h} \\approx 45\\text{ m/s} = 162\\text{ km/h}$</div>
        <div class="pq-exp">A nuée ardente generated by dome collapse on a $h = 500\\text{ m}$ high flank converts potential energy into kinetic energy with minimal basal friction due to gas fluidization, easily exceeding $150\\text{ km/h}$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Origin of the Spine of Mount Pelée</div>
        <div class="pq-ans">Extruded monolith of solid, coherent dacitic magma</div>
        <div class="pq-exp">Following the 1902 eruption, a monolithic needle of crystalline dacite was forced up like toothpaste from the vent, reaching a height of $310\\text{ m}$ and a diameter of $100\\text{ m}$ before crumbling under its own weight.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Fragmentation Threshold of Volcanic Melts</div>
        <div class="pq-ans">Strain rate exceeds viscoelastic relaxation time: $\\dot{\\gamma} \\cdot \\tau > 1$</div>
        <div class="pq-exp">Magma fragments explosively when the rate of decompression exceeds the melt's ability to flow viscously, causing the liquid-gas foam to shatter brittlely into ash and pumice shards.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: The 1980 Mount St. Helens Lateral Blast</div>
        <div class="pq-ans">Pelean-style cryptodome collapse and lateral explosion</div>
        <div class="pq-exp">Mount St. Helens (1980) represents a modern analog of the Pelean mechanism: a dacite cryptodome oversteepened the north flank, triggering a massive landslide that abruptly depressurized the hydrothermal/magmatic system, unleashing a supersonic lateral blast.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Identification of Ignimbrite Deposits</div>
        <div class="pq-ans">Welded tuffs deposited by high-temperature pyroclastic flows</div>
        <div class="pq-exp">When nuées ardentes come to rest while particles are still above their glass transition temperature ($>600^\\circ\\text{C}$), pumice fragments collapse into flattened glassy lenses (fiamme), forming welded ignimbrites.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Water Solubility in Rhyolitic/Dacitic Magmas</div>
        <div class="pq-ans">Solubility scales with square root of pressure: $C_w = s \\sqrt{P}$</div>
        <div class="pq-exp">At $100\\text{ MPa}$ ($3.5\\text{ km}$ depth), felsic melt can dissolve $>5-6\\text{ wt}\\%$ water. Rapid ascent drops pressure to atmospheric levels ($0.1\\text{ MPa}$), converting dissolved water into thousands of liters of expanding steam.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Base Surge vs. Pyroclastic Flow</div>
        <div class="pq-ans">Base surge is dilute, turbulent, and gas-supported; flow is dense and concentrated</div>
        <div class="pq-exp">Pelean blasts produce both a basal high-density pyroclastic flow that hugs valleys and a superheated, low-density turbulent base surge that surges over ridges and topography.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Volcanic Gas Hazard in Nuées Ardentes</div>
        <div class="pq-ans">Asphyxiation by superheated steam, CO2, SO2, and thermal lung searing</div>
        <div class="pq-exp">Autopsies of the 28,000 victims of the 1902 Saint-Pierre catastrophe revealed that death was instantaneous due to thermal searing of the respiratory tract by inhaling superheated steam ($>800^\\circ\\text{C}$) loaded with microscopic vitreous ash particles.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 38: COMPOSITE CONES / STRATOVOLCANOES
# ==========================================
q38_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Volcanic Geomorphology: Stratovolcanoes & Composite Cone Architecture</div>
    <div class="card-body">
      <p>Volcanic landforms constructed around central vents display distinct topographic profiles governed by the rheology of their erupted products. When a volcano erupts alternately between explosive pyroclastic fragmentation and effusive lava flows, it constructs a monumental edifice known as a <strong>Composite Cone</strong> (or <strong>Stratovolcano</strong>).</p>
      
      <ul>
        <li><strong>Internal Stratification:</strong> A composite cone is constructed from <strong>alternating layers (strata) of pyroclastic tephra (ash, cinders, bombs, lapilli) and solidified lava flows</strong>. This interstratified architecture is the explicit source of the term <em>stratovolcano</em>.</li>
        <li><strong>Topographic Profile:</strong> Stratovolcanoes exhibit a classic, majestic <strong>concave-upward conical profile</strong>:
          <ul>
            <li><strong>Summit slopes:</strong> Very steep ($30^\\circ - 35^\\circ$), supported by the angle of repose of coarse pyroclastic debris and viscous lava spines.</li>
            <li><strong>Basal flanks:</strong> Flatter and gentler ($5^\\circ - 10^\\circ$), built by far-reaching viscous lava flows, lahars (volcanic mudflows), and ash falls.</li>
          </ul>
        </li>
        <li><strong>Magmatic Composition:</strong> Primarily <strong>intermediate to felsic</strong> magmas (andesite, dacite, and minor rhyolite). The viscous andesitic lava acts as a natural mortar, cementing the loose pyroclastic layers and granting the cone exceptional structural elevation (frequently reaching $3000-6000\\text{ m}$ height).</li>
        <li><strong>Global Setting:</strong> Stratovolcanoes dominate convergent plate boundaries (subduction zones) around the Pacific <strong>Circum-Pacific Belt (Ring of Fire)</strong>. Renowned global examples include Mount Fuji (Japan), Mount Mayon (Philippines), Mount Rainier (USA), Mount Vesuvius (Italy), and Mount Cotopaxi (Ecuador).</li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Composite Cones:</strong> These cones are composed of <strong>alternate layers of pyroclastic material and solidified lava flows</strong>. Composite cones with marked stratification are called <strong>stratovolcanoes</strong>. They are the most picturesque and large-sized volcanoes. Examples include Mt. Vesuvius, Mt. Fuji, and Mt. Mayon."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Volcanoes: Volcanic Cones, p. 48)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Slope Equilibrium & Volume of a Symmetrical Stratovolcano</div>
        $$\\text{Summit Slope: } \\theta_{\\text{summit}} \\approx 30^\\circ - 35^\\circ \\approx \\phi_{\\text{repose of cinders}}$$
        $$\\text{Basal Slope: } \\theta_{\\text{base}} \\approx 5^\\circ - 10^\\circ$$
        $$V_{\\text{cone}} = \\frac{1}{3} \\pi R^2 H \\quad (\\text{Geometric volume of conical edifice})$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $R$ is basal radius ($10-20\\text{ km}$) and $H$ is elevation above baseline ($2-4\\text{ km}$). The alternating competent lava sheets prevent catastrophic structural collapse of loose pyroclastic beds.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q038/bangar_p48_composite_stratovolcano.png" alt="K.M. Bangar Composite Cone Stratovolcano Cross Section">
        <div class="tb-caption">
          <strong>Figure 38.1: Internal Architecture of a Composite Cone / Stratovolcano (K.M. Bangar, p. 48).</strong> Cross-sectional anatomy showing alternating strata of pyroclastic cinders/ash and solidified lava flows fed by a central conduit and radiating feeder dykes.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Anatomy of the Four Primary Volcanic Edifices</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Volcanic Edifice</th>
            <th>Primary Composition</th>
            <th>Internal Architecture</th>
            <th>Slope Profile</th>
            <th>Type Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Strato Volcano (Composite Cone)</strong></td>
            <td><strong>Andesite, Dacite (Intermediate)</strong></td>
            <td><strong>Alternating layers of pyroclastic debris and lava flows</strong></td>
            <td><strong>Concave steep cone ($30^\\circ$ summit, $10^\\circ$ base)</strong></td>
            <td><strong>Mt. Fuji, Mt. Mayon, Mt. Vesuvius, Mt. Rainier</strong></td>
          </tr>
          <tr>
            <td><strong>Shield Volcano</strong></td>
            <td>Basalt (Low-viscosity mafic)</td>
            <td>Successive sheets of fluid basaltic lava flows</td>
            <td>Broad, convex, very gentle slopes ($2^\\circ - 8^\\circ$)</td>
            <td>Mauna Loa, Kilauea, Erta Ale</td>
          </tr>
          <tr>
            <td><strong>Cinder Cone (Scoria Cone)</strong></td>
            <td>Basaltic to Andesitic tephra</td>
            <td>Uncemented, loose pyroclastic scoria cinders</td>
            <td>Straight, steep uniform slopes ($30^\\circ - 33^\\circ$)</td>
            <td>Parícutin (Mexico), Sunset Crater (USA)</td>
          </tr>
          <tr>
            <td><strong>Lava Dome (Tholoid)</strong></td>
            <td>Rhyolite, Dacite (Extremely viscous)</td>
            <td>Concentric bulbous mound of solid degassed lava</td>
            <td>Steep-sided, dome-like, rubbly flanks</td>
            <td>Mt. St. Helens dome, Chaitén (Chile)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q38_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q038</div>
    <div class="q-stmt">Composite cones are the characteristics of :</div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Strato volcanoes</div>
      <div class="raw-opt">(B) Cinder cone volcanoes</div>
      <div class="raw-opt">(C) Shield volcano</div>
      <div class="raw-opt">(D) Lava domes</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (A) Strato volcanoes</div>
      <div class="sub">Verified against Bangar (p. 48), Tarbuck & Lutgens (Earth Science), and Philpotts & Ague (Principles of Igneous Petrology). Composite cones are by definition the physical volcanic edifices termed stratovolcanoes, characterized by alternating strata of pyroclastic debris and solidified lava.</div>
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) Strato volcanoes</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The term <strong>stratovolcano</strong> is directly derived from its stratified internal architecture: alternating strata (composite layers) of pyroclastic tephra (ash, lapilli, cinders) and viscous lava flows. These composite layers build steep, symmetrical, monumental mountains with concave slopes, forming the classic composite cones recognized worldwide (such as Mount Fuji and Mount Mayon).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Cinder cone volcanoes</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Cinder cones (scoria cones) are constructed <strong>purely from loose pyroclastic debris</strong> (cinders and lapilli) ejected into the air that rain down around the vent at their natural angle of repose ($\approx 30-33^\circ$). They are small (rarely exceeding $300-400\text{ m}$ height), monogenetic, and lack the alternating lava sheets that define composite cones.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Shield volcano</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Shield volcanoes (e.g., Mauna Loa in Hawaii) are built almost <strong>exclusively by successive flows of fluid basaltic lava</strong> with very little to no pyroclastic material. Because fluid basalt spreads thin over immense distances, shield volcanoes develop extremely broad, low-angle convex slopes ($2^\circ-8^\circ$) resembling a warrior's shield, rather than steep composite cones.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Lava domes</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Lava domes (tholoids) form when degassed, highly viscous rhyolitic or dacitic lava is squeezed out of a vent without explosive dispersal, piling up into a steep-sided bulbous dome. They lack conical symmetry and do not display alternating pyroclastic and lava layering.
    </div>
  </div>
"""

q38_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Morphometric & Rheological Parameters of Volcanic Cones</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Parameter</th>
            <th>Stratovolcano (Composite)</th>
            <th>Shield Volcano</th>
            <th>Cinder Cone</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Height ($H$)</strong></td>
            <td>$1000 - 4000+\\text{ m}$</td>
            <td>Up to $9000\\text{ m}$ (from ocean base)</td>
            <td>$50 - 400\\text{ m}$</td>
          </tr>
          <tr>
            <td><strong>Basal Diameter ($D$)</strong></td>
            <td>$10 - 30\\text{ km}$</td>
            <td>$100 - 200\\text{ km}$</td>
            <td>$0.5 - 2.0\\text{ km}$</td>
          </tr>
          <tr>
            <td><strong>Height/Diameter Ratio ($H/D$)</strong></td>
            <td>$0.1 - 0.2$ (Prominent peak)</td>
            <td>$0.05$ (Very broad)</td>
            <td>$0.2$ (Steep pimple)</td>
          </tr>
          <tr>
            <td><strong>Eruption Recurrence</strong></td>
            <td>Polygenetic (Erupts over $10^5 - 10^6\\text{ yr}$)</td>
            <td>Polygenetic (Continuous over $10^6\\text{ yr}$)</td>
            <td>Monogenetic (Single eruption lasting weeks/years)</td>
          </tr>
          <tr>
            <td><strong>Sector Collapse Hazard</strong></td>
            <td>Very High (Debris avalanches / lahars)</td>
            <td>Low (Slow rift slumping)</td>
            <td>Negligible</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Volcanic Geomorphology & Stratocones</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Volume Calculation of a Symmetrical Stratocone</div>
        <div class="pq-ans">Edifice Volume $V = 314.16\\text{ km}^3$</div>
        <div class="pq-exp">A symmetrical stratovolcano has a basal diameter of $D = 20\\text{ km}$ (radius $R = 10\\text{ km}$) and rises to an elevation of $H = 3.0\\text{ km}$. Approximate its volume using a cone formula.<br>
        $$V = \\frac{1}{3} \\pi R^2 H = \\frac{1}{3} \\pi (10)^2 (3.0) = 100 \\pi = 314.16\\text{ km}^3$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Angle of Repose of Volcanic Cinders</div>
        <div class="pq-ans">Angle of repose is $\\approx 33^\\circ$</div>
        <div class="pq-exp">Loose scoria and volcanic cinders have internal friction angles between $32^\\circ$ and $36^\\circ$. Gravity forces dry granular debris to slide until it stabilizes at its angle of repose ($\approx 33^\\circ$), establishing the summit slope of stratovolcanoes and cinder cones.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Hydrothermal Alteration & Edifice Instability</div>
        <div class="pq-ans">Acid sulfate fluids alter competent volcanic rock into weak smectite clays</div>
        <div class="pq-exp">Circulating hydrothermal fluids within stratovolcanoes convert resistant lavas into water-saturated clays, causing major internal weakening that predisposes the volcanic cone to catastrophic sector collapse and gigantic debris avalanches.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Lahars (Volcanic Mudflows) on Stratovolcanoes</div>
        <div class="pq-ans">Mobilization of loose summit tephra by melting snow/ice or heavy rainfall</div>
        <div class="pq-exp">Stratovolcanoes generate deadly lahars because loose, fine-grained pyroclastic ash on steep slopes easily mixes with water (from crater lake breaches, rain, or glacial melt), creating slurries with the density of wet concrete that travel at $>50\\text{ km/h}$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Barren Island Volcano, India</div>
        <div class="pq-ans">Only active stratovolcano in the Indian subcontinent</div>
        <div class="pq-exp">Barren Island in the Andaman Sea is an active composite stratovolcano situated along the volcanic arc produced by the subduction of the Indian Plate beneath the Burma Microplate.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Parasitic Cones on Flanks</div>
        <div class="pq-ans">Adventive cones fed by radial dykes branching off the central conduit</div>
        <div class="pq-exp">When the main conduit of a high stratovolcano becomes clogged by solidified magma plugs, lateral magma pressure fractures the cone flanks via radial dykes, erupting on the mountain sides to form parasitic cinder cones.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Magmatic Evolution of Stratovolcanoes</div>
        <div class="pq-ans">Fractional crystallization and crustal assimilation produce calc-alkaline suites</div>
        <div class="pq-exp">Subduction-derived hydrous basaltic parental magmas undergo extensive fractionation and assimilation of continental crust within crustal magma chambers, evolving from basaltic andesite to andesite, dacite, and rhyolite (the classic calc-alkaline series).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Somma Volcano Morphology</div>
        <div class="pq-ans">A new stratocone growing within the collapsed caldera of an older volcano</div>
        <div class="pq-exp">A somma volcano (named after Monte Somma, Italy) occurs when a younger stratovolcano cone (Vesuvius) builds inside the caldera rim of a partially destroyed ancient composite cone.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 39: AIRY'S THEORY OF ISOSTASY
# ==========================================
q39_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Planetary Geodynamics: Theories of Isostasy (Airy vs. Pratt)</div>
    <div class="card-body">
      <p><strong>Isostasy</strong> (coined by C.E. Dutton in 1889, from Greek <em>isostasios</em>, meaning "equal standing") describes the condition of gravitational hydrostatic equilibrium between Earth's rigid lithospheric crust and the denser, ductile underlying mantle asthenosphere. The concept originated during the Great Trigonometrical Survey of India (1854) under Sir George Everest, when gravitational deflection of the plumb-line near the Himalayas yielded significantly less gravitational pull than predicted by the visible mass of the mountains.</p>
      
      <ul>
        <li><strong>Airy's Hypothesis (1855):</strong> Proposed by English Astronomer Royal <strong>Sir George Biddell Airy</strong>. Airy postulated that:
          <ul>
            <li>Earth's crust has a <strong>constant, uniform density ($\\rho_c \\approx 2.7 - 2.8\\text{ g/cm}^3$)</strong> throughout all continents and mountains.</li>
            <li>This lighter crust <strong>floats upon a denser, ductile substratum (the mantle, $\\rho_m \\approx 3.3\\text{ g/cm}^3$)</strong>, exactly like <strong>icebergs floating in water</strong>.</li>
            <li>High mountains are mechanically supported not by high density, but by <strong>deep crustal roots</strong> plunging downward into the denser mantle substratum. The taller the mountain, the deeper its root:
              $$r = h \\cdot \\frac{\\rho_c}{\\rho_m - \\rho_c}$$
            </li>
          </ul>
        </li>
        <li><strong>Pratt's Hypothesis (1859):</strong> Proposed by Archdeacon John Henry Pratt. In Pratt's model, the crust has a <strong>uniform depth of compensation</strong> ($D$), but mountains have <strong>variable, lower densities</strong> (the higher the peak, the lighter the rock: $\\rho \\cdot H = \\text{constant}$).</li>
        <li><strong>Seismic Validation:</strong> Modern deep seismic reflection and refraction profiling (e.g., receiver functions) confirms that continental mountain belts like the Himalayas and Alps indeed possess deep crustal roots extending down to $60-75\\text{ km}$ into the denser mantle, proving that <strong>Airy's model is the fundamentally correct mechanism for mountain belts</strong>.</li>
      </ul>

      <div class="quote-box bangar">
        "According to <strong>Airy's theory of isostasy</strong>, the earth's crust is made of lighter material of uniform density ($\\rho_c$) which is <strong>floating on a denser substratum</strong> ($\\rho_m$). Just as an iceberg floats in water with a large part submerged beneath the water, the mountains have deep roots projecting down into the denser substratum. The higher the mountain, the deeper is its root."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of the Earth: Isostasy, p. 32)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Airy's Isostatic Equilibrium Formulation</div>
        $$\\text{Mass Conservation at Compensation Depth: } \\quad \\rho_c (h + T_0 + r) = \\rho_c T_0 + \\rho_m r$$
        $$\\rho_c h + \\rho_c r = \\rho_m r \\implies \\mathbf{r = h \\left( \\frac{\\rho_c}{\\rho_m - \\rho_c} \\right)}$$
        $$\\text{Total Crustal Thickness beneath Mountain: } \\quad T = T_0 + h + r = T_0 + h \\left( 1 + \\frac{\\rho_c}{\\rho_m - \\rho_c} \\right)$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">For crustal density $\\rho_c = 2.8\\text{ g/cm}^3$ and mantle density $\\rho_m = 3.3\\text{ g/cm}^3$, the root ratio is $r / h = 2.8 / 0.5 = 5.6$. Every $1\\text{ km}$ of topography requires $\\approx 5.6\\text{ km}$ of crustal root beneath it!</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q039/bangar_fig1_7_airy_isostasy_crustal_roots.png" alt="K.M. Bangar Fig 1.7 Airy's Theory of Isostasy Roots">
        <div class="tb-caption">
          <strong>Figure 39.1: Airy's Model of Isostasy (K.M. Bangar, p. 32).</strong> Light crustal blocks of uniform density ($\rho_c$) floating in a denser substratum ($\rho_m$). Mountain peaks are balanced by deep crustal roots projecting into the denser mantle, analogous to floating icebergs.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Airy vs. Pratt Models of Isostatic Compensation</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Parameter</th>
            <th>Airy's Model (1855)</th>
            <th>Pratt's Model (1859)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Crustal Density ($\\rho_c$)</strong></td>
            <td><strong>Constant / Uniform ($\\approx 2.7-2.8\\text{ g/cm}^3$)</strong></td>
            <td><strong>Variable (Lower density under high peaks)</strong></td>
          </tr>
          <tr>
            <td><strong>Base of Crust (Roots)</strong></td>
            <td><strong>Variable depth (Deep roots under mountains)</strong></td>
            <td><strong>Uniform, flat depth of compensation ($D$)</strong></td>
          </tr>
          <tr>
            <td><strong>Physical Analogy</strong></td>
            <td><strong>Icebergs floating in water / wooden blocks of unequal length</strong></td>
            <td>Blocks of different metals (lead, iron, zinc) floating in mercury</td>
          </tr>
          <tr>
            <td><strong>Geological Reality</strong></td>
            <td><strong>Validated for continental mountain belts (Himalayas, Andes)</strong></td>
            <td>Applies partially to mid-ocean ridge thermal buoyancy</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q39_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q039</div>
    <div class="q-stmt">According to Airy’s theory of isostasy :</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Lighter mountains are floating on the lighter substratum</div>
      <div class="raw-opt correct">(B) Lighter mountains are floating on the denser substratum</div>
      <div class="raw-opt">(C) Denser mountains are floating on denser substratum</div>
      <div class="raw-opt">(D) Denser mountains are floating on the lighter substratum</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (B) Lighter mountains are floating on the denser substratum</div>
      <div class="sub">Verified against Bangar (p. 32), Fowler (The Solid Earth, p. 195), and Turcotte & Schubert (Geodynamics). Sir George Airy established that the Earth's crust is composed of lighter rocks ($\rho_c \approx 2.7\text{ g/cm}^3$) floating in hydrostatic equilibrium upon a denser mantle substratum ($\rho_m \approx 3.3\text{ g/cm}^3$), supported by deep crustal roots.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Lighter mountains are floating on the lighter substratum</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Under Archimedes' principle, a body cannot float in a fluid of equal or lesser density; it would sink immediately. For isostatic flotation to occur, the substratum must be mechanically denser than the floating mountain mass.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Lighter mountains are floating on the denser substratum</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Airy's fundamental thesis is that continental mountains consist of relatively light granitic/silicate crustal rocks ($\\rho_c \\approx 2.7\\text{ g/cm}^3$) that <strong>float upon a significantly denser, ductile ultramafic mantle substratum</strong> ($\\rho_m \\approx 3.3\\text{ g/cm}^3$). Just as an iceberg floats in seawater with the majority of its bulk submerged as a root, tall mountains are held in gravitational equilibrium by deep crustal roots displacing the denser mantle substratum below.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Denser mountains are floating on denser substratum</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Mountains are not denser than the substratum; they are composed of felsic and intermediate silicate rocks ($2.7\\text{ g/cm}^3$), whereas the underlying asthenospheric mantle is composed of dense ultramafic peridotite ($3.3\\text{ g/cm}^3$).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Denser mountains are floating on the lighter substratum</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> If mountains were denser than the substratum, hydrostatic equilibrium would be physically impossible, and gravitational instability would cause the mountains to sink to the core.
    </div>
  </div>
"""

q39_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Isostatic Anomalies & Geodynamic Implications</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Isostatic Anomaly State</th>
            <th>Observed vs. Calculated Gravity</th>
            <th>Physical Crustal Condition</th>
            <th>Geodynamic Response</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Zero Isostatic Anomaly</strong></td>
            <td>$g_{\\text{obs}} = g_{\\text{isostasy}}$</td>
            <td><strong>Perfect hydrostatic equilibrium</strong></td>
            <td>Tectonic stability; no vertical crustal movement</td>
          </tr>
          <tr>
            <td><strong>Positive Isostatic Anomaly</strong></td>
            <td>$g_{\\text{obs}} > g_{\\text{isostasy}}$ (Excess mass)</td>
            <td>Under-compensated crust (Deficit of root)</td>
            <td>Crust will undergo isostatic subsidence / downwarping</td>
          </tr>
          <tr>
            <td><strong>Negative Isostatic Anomaly</strong></td>
            <td>$g_{\\text{obs}} < g_{\\text{isostasy}}$ (Mass deficit)</td>
            <td>Over-compensated crust (Root too deep for topography)</td>
            <td>Crust will undergo <strong>isostatic uplift / rebound</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Isostatic Balancing & Root Calculations</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Himalayan Crustal Root Calculation</div>
        <div class="pq-ans">Crustal root $r = 28.0\\text{ km}$; total thickness $T = 68.0\\text{ km}$</div>
        <div class="pq-exp">The Tibetan plateau stands at an average elevation of $h = 5.0\\text{ km}$. Standard crustal thickness is $T_0 = 35.0\\text{ km}$. Assuming $\\rho_c = 2.8\\text{ g/cm}^3$ and $\\rho_m = 3.3\\text{ g/cm}^3$, calculate the root depth $r$ and total crustal thickness $T$.<br>
        $$r = h \\left( \\frac{\\rho_c}{\\rho_m - \\rho_c} \\right) = 5.0 \\left( \\frac{2.8}{3.3 - 2.8} \\right) = 5.0 \\times 5.6 = 28.0\\text{ km}$$
        $$T = T_0 + h + r = 35.0 + 5.0 + 28.0 = 68.0\\text{ km}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Isostatic Uplift during Mountain Erosion</div>
        <div class="pq-ans">For $1000\\text{ m}$ of erosion, isostatic rebound restores $\\approx 848\\text{ m}$</div>
        <div class="pq-exp">When erosion strips thickness $\\Delta h$ of rock, the crust unburdens and rebounds by $\\Delta z = \\Delta h (\\rho_c / \\rho_m) = 1000 \\times (2.8 / 3.3) = 848.5\\text{ m}$. Thus, net lowering of the mountain summit is only $151.5\\text{ m}$, prolonging mountain lifespans.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Anti-Roots beneath Ocean Basins</div>
        <div class="pq-ans">Mantle bulges upward beneath thin oceanic crust</div>
        <div class="pq-exp">Because ocean water has low density ($\\rho_w = 1.03\\text{ g/cm}^3$), oceanic crust is thin ($7\\text{ km}$). The compensation depth is maintained by dense mantle ($3.3\\text{ g/cm}^3$) rising to shallow depths of only $10\\text{ km}$ below sea level (an isostatic anti-root).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Post-Glacial Rebound of Scandinavia</div>
        <div class="pq-ans">Negative isostatic anomaly recovering at $\\approx 1\\text{ cm/year}$</div>
        <div class="pq-exp">The melting of the $3\\text{ km}$ thick Weichselian ice sheet removed immense mass. The depressed lithosphere is currently rebounding upward toward isostatic equilibrium as mantle asthenosphere flows back underneath.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Free-Air vs. Bouguer Anomalies over Mountain Chains</div>
        <div class="pq-ans">Free-Air anomaly is near zero; Bouguer anomaly is strongly negative</div>
        <div class="pq-exp">If a mountain chain is in isostatic equilibrium, its total mass is compensated at depth, making the Free-Air anomaly $\\approx 0$. However, the Bouguer reduction removes the mountain mass without adding the low-density root, producing a large negative Bouguer anomaly (e.g., $-450\\text{ mGal}$ over Tibet).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Flexural Isostasy (Vening Meinesz Model)</div>
        <div class="pq-ans">Lithosphere acts as an elastic plate with finite flexural rigidity ($D$)</div>
        <div class="pq-exp">Airy assumes localized hydrostatic pistons with zero lateral shear strength. Vening Meinesz (1931) introduced flexural isostasy, where regional elastic bending distributes loads over a broader flexural wavelength ($\lambda = 2\pi (D / \rho_m g)^{1/4}$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Great Trigonometrical Survey Discrepancy</div>
        <div class="pq-ans">5.236 seconds of arc plumb-line deflection deficit</div>
        <div class="pq-exp">In 1854, J.H. Pratt found the gravitational attraction of the Himalayas on a plumb-line at Kaliana was $5.236''$ less than expected from surface mass, directly proving the presence of an underlying low-density crustal root.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Isostatic Response to Reservoir Filling</div>
        <div class="pq-ans">Crustal flexural sag beneath deep reservoirs (e.g., Lake Mead, Kariba)</div>
        <div class="pq-exp">Filling colossal reservoirs places hundreds of billions of kilograms of water over small areas, causing immediate elastic deflection ($\approx 10-20\text{ cm}$) followed by viscous isostatic subsidence.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 40: ATLANTIC MARGIN PASSIVE CONTINENTAL MARGIN
# ==========================================
q40_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Continental Margin Architecture: Atlantic Passive vs. Pacific Active Margins</div>
    <div class="card-body">
      <p>Continental margins represent the transitional boundary zones connecting thick continental crust with thin oceanic crust. Based on their relationship to tectonic plate boundaries, global continental margins are fundamentally categorized into <strong>Active Margins</strong> and <strong>Passive Margins</strong>.</p>
      
      <ul>
        <li><strong>Passive Continental Margin (Atlantic-Type Margin):</strong> The eastern continental margin of North America is the quintessential global prototype of a <strong>Passive Margin</strong>.
          <ul>
            <li><strong>Intraplate Setting:</strong> It is located within the stable interior of the North American Plate, far removed from any active plate boundary (the nearest boundary is the Mid-Atlantic Ridge thousands of kilometers to the east).</li>
            <li><strong>Tectonic Quiescence:</strong> Devoid of active subduction, oceanic trenches, volcanic arc systems, or major Wadati-Benioff seismic zones.</li>
            <li><strong>Origin by Continental Rifting:</strong> Formed during the Late Triassic to Early Jurassic rifting and continental separation of Pangea (opening of the Central Atlantic Ocean $\approx 180\\text{ Ma}$).</li>
          </ul>
        </li>
        <li><strong>Morpho-Sedimentary Architecture:</strong> A passive continental margin comprises three distinct, gently sloping physiographic provinces:
          <ol>
            <li><strong>Continental Shelf:</strong> Broad, shallow ($0-200\\text{ m}$ depth), gently dipping ($< 0.1^\\circ$) platform underlain by thick post-rift sedimentary prisms.</li>
            <li><strong>Continental Slope:</strong> Steeper zone ($3^\\circ - 5^\\circ$) marking the true structural boundary where continental crust thins abruptly toward oceanic crust, dissected by submarine canyons.</li>
            <li><strong>Continental Rise:</strong> Thick wedge of coalescing deep-sea submarine fans and turbidite deposits ($2000 - 4000\\text{ m}$ depth) merging seamlessly into the abyssal plain.</li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "Continental margins are of two types: active and passive. The <strong>Atlantic continental margin of North America is a passive margin</strong>. It is not a plate boundary. It consists of a broad continental shelf, continental slope, and continental rise. It is characterized by absence of trenches, low seismicity, and lack of volcanic activity."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of Earth & Continental Margins, p. 34) & Van der Pluijm & Marshak, p. 437</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Sedimentary Prism Thickness on Passive Margins</div>
        $$S_{\\text{total}} = S_{\\text{syn-rift}} + S_{\\text{thermal}} + S_{\\text{flexural loading}} > 10 - 15\\text{ km}$$
        $$\\text{Thermal Subsidence Rate: } \\quad y(t) = \\frac{4 L \\rho_m \\alpha_T T_m}{\\pi^2 (\\rho_m - \\rho_w)} \\left( 1 - e^{-t / \\tau} \\right)$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $t$ is post-rift age, $\\tau \\approx 62.8\\text{ Ma}$ is the thermal decay constant of the lithosphere, $\\rho_m$ is mantle density, and $\\rho_w$ is water density. The massive accommodation space traps major petroleum reservoirs.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q040/vdp_p437_atlantic_passive_continental_margin.png" alt="Van der Pluijm & Marshak Passive Continental Margin Profile">
        <div class="tb-caption">
          <strong>Figure 40.1: Architecture of the Atlantic Passive Continental Margin (Van der Pluijm & Marshak, p. 437).</strong> Cross-sectional profile from continental shelf across continental slope and rise to the abyssal plain, showing thick Mesozoic-Cenozoic post-rift sedimentary wedges over stretched crust.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Geodynamic Contrast: Passive (Atlantic) vs. Active (Pacific) Continental Margins</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Feature</th>
            <th>Passive Margin (Atlantic-Type)</th>
            <th>Active Margin (Pacific-Type)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Tectonic Status</strong></td>
            <td><strong>Intraplate (Not a plate boundary)</strong></td>
            <td><strong>Convergent plate boundary (Subduction zone)</strong></td>
          </tr>
          <tr>
            <td><strong>Continental Shelf</strong></td>
            <td><strong>Broad and wide ($100 - 300+\\text{ km}$)</strong></td>
            <td>Narrow or absent ($10 - 30\\text{ km}$)</td>
          </tr>
          <tr>
            <td><strong>Deep-Sea Trench</strong></td>
            <td><strong>Absent (Replaced by Continental Rise)</strong></td>
            <td><strong>Present (Deep oceanic trench, $>6000-11000\\text{ m}$)</strong></td>
          </tr>
          <tr>
            <td><strong>Volcanic Activity</strong></td>
            <td><strong>None (Aseismic / Non-volcanic)</strong></td>
            <td>Vigorous (Andesitic volcanic arc / island arc)</td>
          </tr>
          <tr>
            <td><strong>Earthquake Seismicity</strong></td>
            <td>Very low to negligible; shallow intraplate</td>
            <td>Intense, deep Wadati-Benioff zone megathrusts</td>
          </tr>
          <tr>
            <td><strong>Global Example</strong></td>
            <td><strong>Eastern North America, Brazil, West Africa, East Coast of India</strong></td>
            <td>Western South America (Andes), Cascadia, Japan</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q40_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q040</div>
    <div class="q-stmt">The Atlantic continental margin of North America is known to be :</div>
    <div class="raw-options">
      <div class="raw-opt">(A) An active margin</div>
      <div class="raw-opt correct">(B) Passive margin</div>
      <div class="raw-opt">(C) Suture zone</div>
      <div class="raw-opt">(D) Collision zone</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (B) Passive margin</div>
      <div class="sub">Verified against Bangar (p. 34), Van der Pluijm & Marshak (p. 437), and Boggs (Sedimentology & Stratigraphy, p. 434). The Atlantic margin of North America is the classic global type example of a passive (trailing) continental margin, situated within a single tectonic plate without active subduction or volcanism.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) An active margin</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Active continental margins coincide with plate boundaries, such as the Pacific margin of South America (subduction of the Nazca plate beneath the South American plate). Active margins feature narrow shelves, deep oceanic trenches, active stratovolcanoes, and high-magnitude earthquakes, none of which exist on the North American Atlantic coast.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Passive margin</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Atlantic continental margin of North America is the classic type example of a <strong>passive continental margin</strong>. Formed during the Mesozoic rifting of Pangea, the transition from continental crust to oceanic crust is welded together within the interior of the North American Plate. It is characterized by wide continental shelves (e.g., Georges Bank), thick sedimentary wedges, a prominent continental rise, and an absence of volcanic and subduction trench activity.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Suture zone</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> A suture zone is the linear collision boundary where two formerly separate continents have collided and joined along a consumed ocean basin, typically marked by ophiolites, blueschists, and intense mylonitization (e.g., the Indus-Tsangpo Suture Zone in the Himalayas).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Collision zone</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> A collision zone represents active continental collision between two continental landmasses driven by convergence (such as India colliding into Eurasia). The Atlantic margin is currently in the mature drifting phase of the Wilson Cycle, moving passively away from the Mid-Atlantic Ridge spreading axis.
    </div>
  </div>
"""

q40_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: The Wilson Cycle Stages of Continental Margin Evolution</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Wilson Cycle Stage</th>
            <th>Tectonic Regime</th>
            <th>Margin Configuration</th>
            <th>Global Modern Prototype</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Embryonic Rift</strong></td>
            <td>Continental crustal extension</td>
            <td>Rift valleys, grabens, alkaline volcanism</td>
            <td>East African Rift System</td>
          </tr>
          <tr>
            <td><strong>2. Juvenile Ocean</strong></td>
            <td>Early seafloor spreading</td>
            <td>Narrow ocean basin, evaporites, early shelves</td>
            <td>Red Sea, Gulf of California</td>
          </tr>
          <tr>
            <td><strong>3. Mature Ocean</strong></td>
            <td>Broad seafloor spreading</td>
            <td><strong>Wide passive continental margins with shelf/slope/rise</strong></td>
            <td><strong>Atlantic Ocean (North America & Africa)</strong></td>
          </tr>
          <tr>
            <td><strong>4. Declining Ocean</strong></td>
            <td>Subduction initiation</td>
            <td>Active continental margins, trenches, volcanic arcs</td>
            <td>Pacific Ocean basin</td>
          </tr>
          <tr>
            <td><strong>5. Terminal Collision</strong></td>
            <td>Continental collision</td>
            <td>Suture zones, fold-and-thrust mountain belts</td>
            <td>Himalayas (Indo-Eurasian collision)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Continental Margins & Basin Dynamics</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Width of the Atlantic vs. Pacific Continental Shelves</div>
        <div class="pq-ans">Atlantic shelf averages $100-300\\text{ km}$; Pacific shelf averages $<30\\text{ km}$</div>
        <div class="pq-exp">Because passive margins experience prolonged thermal subsidence and sediment loading without tectonic truncation by subduction trenches, the Atlantic continental shelf is extraordinarily wide compared to the narrow, trench-bounded Pacific active margin.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Role of Turbidity Currents on Continental Rises</div>
        <div class="pq-ans">Deposition of deep-sea fans through submarine canyon conduits</div>
        <div class="pq-exp">Submarine canyons cutting the continental slope act as funnels for density-driven turbidity currents, which decelerate at the slope base to deposit overlapping deep-sea fans that coalesce into the broad, gently dipping continental rise.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: East Coast of India as a Passive Margin</div>
        <div class="pq-ans">Formed by Cretaceous rifting of India from Antarctica-Australia</div>
        <div class="pq-exp">The eastern continental margin of India (Krishna-Godavari, Cauvery, Mahanadi basins) is a classic passive margin formed during the Early Cretaceous breakup of eastern Gondwanaland ($\approx 130\\text{ Ma}$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Hydrocarbon Trapping in Passive Margins</div>
        <div class="pq-ans">Salt diapirs, rollover anticlines, and deep-water turbidite channel sands</div>
        <div class="pq-exp">Passive margins host world-class petroleum systems because syn-rift restricted basins deposit rich lacustrine/marine source rocks, post-rift halite forms salt domes, and prograding shelf-delta sands provide thick reservoirs.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Subduction Initiation along Passive Margins</div>
        <div class="pq-ans">Old oceanic lithosphere becomes negatively buoyant after $\approx 30-50\\text{ Ma}$</div>
        <div class="pq-exp">As oceanic lithosphere cools, its density exceeds the underlying asthenosphere ($\rho_{\text{lith}} > \rho_{\text{asthen}}$). Eventually, gravitational instability may cause old Atlantic oceanic crust to fracture and subduct beneath the continental margin, converting it to an active margin.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: The Fall Line of Eastern North America</div>
        <div class="pq-ans">Geomorphic boundary between crystalline Piedmont and soft Coastal Plain sediments</div>
        <div class="pq-exp">The Fall Line represents the inland limit of the Atlantic passive margin sediment wedge, where rivers cascade over resistant Appalachian basement rocks onto soft Mesozoic-Cenozoic coastal plain sands, creating waterfalls that determined historic city locations.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Thermal Subsidence Time Constant</div>
        <div class="pq-ans">Exponential cooling decay with half-life $\tau \approx 62.8\\text{ Ma}$</div>
        <div class="pq-exp">Thermal contraction of stretched lithosphere follows the 1D heat diffusion equation: $S(t) \propto (1 - e^{-t/\tau})$, leading to rapid subsidence during the first $50\\text{ Ma}$ that gradually slows over hundreds of millions of years.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Seismic Stratigraphy of Passive Margins</div>
        <div class="pq-ans">Three-tier sequence: Pre-rift basement, Syn-rift grabens, Post-rift drift wedge</div>
        <div class="pq-exp">Seismic reflection profiles across passive margins reveal: (1) undeformed crystalline basement, (2) wedge-shaped syn-rift fault blocks bounded by normal faults, and (3) an overlying, undeformed post-rift "steer's head" thermal sag sequence prograding seaward.</div>
      </div>
    </div>
  </div>
"""

# Generate all pages
generate_page(
    q_num=36,
    filename="Q036_Weathering_Exfoliating_Activity_Massive_Rocks_Complete_Guide.html",
    title="Q036: Mechanical Weathering: Exfoliation in Massive Rocks",
    badge="OPSC 2019 · Paper-II · Q036 · Geomorphology & Weathering",
    h1_title="Exfoliating Weathering Activity in Massive Rocks",
    meta_text="Question ID: GEO-2019-Q036 | Topic: Physical Weathering & Rock Fabric | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q36_part1,
    part2_html=q36_part2,
    part3_html=q36_part3
)

generate_page(
    q_num=37,
    filename="Q037_Pelean_Volcano_Most_Violent_Activity_Complete_Guide.html",
    title="Q037: Volcanic Dynamics: Pelean Eruptions & Most Violent Activity",
    badge="OPSC 2019 · Paper-II · Q037 · Volcanology & Igneous Petrology",
    h1_title="Pelean Type Volcanoes: Most Violent Eruptive Activity",
    meta_text="Question ID: GEO-2019-Q037 | Topic: Volcanology & Pyroclastic Surges | Difficulty: Moderate | Target Time: 35 sec",
    part1_html=q37_part1,
    part2_html=q37_part2,
    part3_html=q37_part3
)

generate_page(
    q_num=38,
    filename="Q038_Composite_Cones_Stratovolcanoes_Characteristics_Complete_Guide.html",
    title="Q038: Volcanic Architecture: Composite Cones of Stratovolcanoes",
    badge="OPSC 2019 · Paper-II · Q038 · Volcanology & Geomorphology",
    h1_title="Composite Cones as Defining Characteristics of Stratovolcanoes",
    meta_text="Question ID: GEO-2019-Q038 | Topic: Volcanic Cones & Morphology | Difficulty: Easy | Target Time: 25 sec",
    part1_html=q38_part1,
    part2_html=q38_part2,
    part3_html=q38_part3
)

generate_page(
    q_num=39,
    filename="Q039_Airy_Theory_Isostasy_Mountains_Floating_Denser_Substratum_Complete_Guide.html",
    title="Q039: Planetary Geodynamics: Airy's Theory of Isostasy",
    badge="OPSC 2019 · Paper-II · Q039 · Geophysics & Geodynamics",
    h1_title="Airy's Theory of Isostasy: Lighter Mountains Floating on Denser Substratum",
    meta_text="Question ID: GEO-2019-Q039 | Topic: Isostasy & Crustal Roots | Difficulty: Moderate | Target Time: 35 sec",
    part1_html=q39_part1,
    part2_html=q39_part2,
    part3_html=q39_part3
)

generate_page(
    q_num=40,
    filename="Q040_Atlantic_Margin_North_America_Passive_Margin_Complete_Guide.html",
    title="Q040: Continental Margins: Atlantic Passive Margin of North America",
    badge="OPSC 2019 · Paper-II · Q040 · Geotectonics & Marine Geology",
    h1_title="Atlantic Continental Margin of North America as a Passive Margin",
    meta_text="Question ID: GEO-2019-Q040 | Topic: Continental Margins & Plate Boundaries | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q40_part1,
    part2_html=q40_part2,
    part3_html=q40_part3
)

print("Batch 4 Part A (Q036 - Q040) completed successfully!")
