#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 31 to 35
Assam DGMS 2019 Masterclass Standard
"""

from masterclass_generator_core import generate_page

# ==========================================
# QUESTION 31: LAURASIA AND GONDWANALAND
# ==========================================
q31_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Paleogeography & Continental Drift: The Breakup of Pangea</div>
    <div class="card-body">
      <p>The theory of Continental Drift, pioneered by Alfred Wegener (1912, 1915) and subsequently synthesized into modern Plate Tectonics by Arthur Holmes, Harry Hess, and J. Tuzo Wilson, demonstrated that the Earth's present continents were formerly assembled into a single late Paleozoic supercontinent: <strong>Pangea</strong> (from Greek, meaning "All-Earth").</p>
      
      <ul>
        <li><strong>Supercontinental Rifting:</strong> During the Late Triassic to Early Jurassic ($\approx 200-180\\text{ Ma}$), Pangea began to rift and separate along an east-west trending equatorial seaway known as the <strong>Tethys Ocean</strong>.</li>
        <li><strong>The Two Mega-Continents:</strong> This rifting event split Pangea into two colossal continental landmasses:
          <ul>
            <li><strong>Laurasia (Northern Supercontinent):</strong> Comprising present-day North America (Laurentia), Greenland, Europe, and Asia (excluding the Indian subcontinent and Arabia).</li>
            <li><strong>Gondwanaland (Southern Supercontinent):</strong> Named by Eduard Suess after the ancient Gond kingdom of central India, comprising present-day South America, Africa, Madagascar, the Indian Peninsula, Australia, and Antarctica.</li>
          </ul>
        </li>
        <li><strong>Panthalassa:</strong> The vast, singular global ocean that surrounded Pangea was termed <em>Panthalassa</em> (meaning "All-Sea"), the ancestral precursor to the modern Pacific Ocean.</li>
      </ul>

      <div class="quote-box bangar">
        "According to the Continental Drift Theory, in the Carboniferous period all the landmasses were united into one huge supercontinent called <strong>Pangea</strong>, surrounded by a universal ocean called <strong>Panthalassa</strong>. Later on, Pangea broke up into two super-continental blocks: <strong>Laurasia</strong> in the north and <strong>Gondwanaland</strong> in the south, separated by the east-west trending <strong>Tethys Sea</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Plate Tectonics & Continental Drift, p. 28) & Van der Pluijm & Marshak, p. 580</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Supercontinental Kinematic Partitioning Formula</div>
        $$\\text{Pangea (Late Paleozoic)} \\xrightarrow[\\approx 200\\text{ Ma}]{\\text{Tethyan Rifting}} \\mathbf{\\text{Laurasia (North)}} + \\mathbf{\\text{Gondwanaland (South)}}$$
        $$\\text{Laurasia} = \\text{North America} + \\text{Eurasia (excluding India & Arabia)} + \\text{Greenland}$$
        $$\\text{Gondwanaland} = \\text{South America} + \\text{Africa} + \\text{Madagascar} + \\text{India} + \\text{Antarctica} + \\text{Australia}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Gondwanaland is characterized by a distinctive Permo-Carboniferous stratigraphic succession: Talchir boulder beds (glacial), Glossopteris flora, and thick coal seams.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q031/vdp_fig21_21_laurasia_gondwanaland_tethys.png" alt="Van der Pluijm & Marshak Fig 21.21 Breakup of Pangea into Laurasia and Gondwanaland">
        <div class="tb-caption">
          <strong>Figure 31.1: Breakup of Pangea across the Tethys Ocean (Van der Pluijm & Marshak, p. 580).</strong> Paleogeographic reconstruction illustrating the initial Triassic-Jurassic splitting of Pangea into northern Laurasia and southern Gondwanaland, separated by the equatorial Tethys Sea.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Paleogeography: Laurasia vs. Gondwanaland</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Paleogeographic Attribute</th>
            <th>Laurasia</th>
            <th>Gondwanaland</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Hemispheric Position</strong></td>
            <td>Northern Hemisphere (Boreal realm)</td>
            <td>Southern Hemisphere (Austral realm)</td>
          </tr>
          <tr>
            <td><strong>Constituent Modern Plates</strong></td>
            <td>North America, Greenland, Europe, Siberia, China</td>
            <td>South America, Africa, Arabia, India, Madagascar, Australia, Antarctica</td>
          </tr>
          <tr>
            <td><strong>Permo-Carboniferous Climate</strong></td>
            <td>Warm, humid equatorial to tropical</td>
            <td>Extensive polar / subpolar continental glaciation (Dwyka / Talchir)</td>
          </tr>
          <tr>
            <td><strong>Diagnostic Fossil Flora</strong></td>
            <td><em>Lepidodendron</em>, <em>Sigillaria</em>, <em>Calamites</em> (Euramerican flora)</td>
            <td><em>Glossopteris</em>, <em>Gangamopteris</em>, <em>Vertebraria</em> (Gondwana flora)</td>
          </tr>
          <tr>
            <td><strong>Diagnostic Fossil Fauna</strong></td>
            <td>Tetrapods, primitive amphibians</td>
            <td><em>Mesosaurus</em> (freshwater reptile), <em>Lystrosaurus</em>, <em>Cynognathus</em></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q31_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q031</div>
    <div class="q-stmt">The two super continental blocks separated due to drifting are :</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Pangea and Laurasia</div>
      <div class="raw-opt">(B) Pangea and Gondwanaland</div>
      <div class="raw-opt correct">(C) Laurasia and Gondwanaland</div>
      <div class="raw-opt">(D) Laurasia and Panthalassa</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (C) Laurasia and Gondwanaland</div>
      <div class="sub">Verified against Bangar (p. 28), Van der Pluijm & Marshak (Earth Structure, p. 580), and Tarbuck & Lutgens (Earth Science). When the ancestral supercontinent Pangea broke apart in the early Mesozoic, it split into two daughter supercontinental blocks: northern Laurasia and southern Gondwanaland.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Pangea and Laurasia</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Pangea was the original, unified supercontinent before rifting took place. Laurasia was not a coexisting entity that drifted away from Pangea; rather, Laurasia was one of the two pieces resulting from the breakup of Pangea.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Pangea and Gondwanaland</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Similar to distractor (A), Gondwanaland was the southern daughter fragment derived from Pangea. Pangea ceased to exist once the breakup was initiated; the two supercontinental blocks that drifted apart from each other were Laurasia and Gondwanaland.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Laurasia and Gondwanaland</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> During the Triassic-Jurassic rifting phase of Pangea, the opening of the east-west Tethys seaway bifurcated the global landmass into two vast supercontinents: <strong>Laurasia</strong> in the north (North America, Europe, Asia) and <strong>Gondwanaland</strong> in the south (South America, Africa, India, Australia, Antarctica). These two giant continental blocks drifted independently until their eventual collisions in the Cenozoic (e.g., India colliding into Eurasia to form the Himalayas).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Laurasia and Panthalassa</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Panthalassa was the universal ancestral ocean, not a continental block. The question specifically inquires about the <em>two super continental blocks</em> that separated due to continental drift.
    </div>
  </div>
"""

q31_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Geodynamic Evolutionary Stages of Supercontinent Cycles</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Supercontinent</th>
            <th>Approximate Age</th>
            <th>Assembly Orogeny</th>
            <th>Breakup Products</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Columbia (Nuna)</strong></td>
            <td>$1.8 - 1.5\\text{ Ga}$ (Paleoproterozoic)</td>
            <td>Global Paleoproterozoic collisions</td>
            <td>Laurentia, Baltica, proto-India, East Antarctica</td>
          </tr>
          <tr>
            <td><strong>Rodinia</strong></td>
            <td>$1.1 - 0.75\\text{ Ga}$ (Mesoproterozoic)</td>
            <td>Grenvillian Orogeny</td>
            <td>Laurentia, Congo craton, proto-Gondwana blocks</td>
          </tr>
          <tr>
            <td><strong>Pannotia (Vendian)</strong></td>
            <td>$600 - 540\\text{ Ma}$ (Neoproterozoic)</td>
            <td>Pan-African / Brasiliano Orogenies</td>
            <td>Laurentia, Baltica, Siberia, Gondwana</td>
          </tr>
          <tr>
            <td><strong>Pangea</strong></td>
            <td>$335 - 175\\text{ Ma}$ (Late Paleozoic)</td>
            <td>Variscan / Alleghanian Orogenies</td>
            <td><strong>Laurasia and Gondwanaland</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Paleogeography & Continental Drift</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Identification of Gondwana Continental Fragments</div>
        <div class="pq-ans">India, Australia, Antarctica, Africa, South America, Madagascar</div>
        <div class="pq-exp">Which modern landmasses constituted Gondwanaland? All southern hemisphere continents plus peninsular India and the Arabian Peninsula formed Gondwana, linked by shared Dwyka/Talchir glacial tillites and *Glossopteris* flora.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: The Tethys Ocean's Role in Plate Tectonics</div>
        <div class="pq-ans">Separated Laurasia from Gondwana; closed during Indo-Eurasian collision</div>
        <div class="pq-exp">The Neotethys Ocean opened as the Cimmerian blocks rifted from northern Gondwana during the Permo-Triassic, and eventually closed as India moved northward, with marine Tethyan sediments uplifted into the Tibetan Plateau and Tethyan Himalayas.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Paleomagnetic Apparent Polar Wander Paths (APWP)</div>
        <div class="pq-ans">Divergent APWP curves prove continental drift rather than true polar wander</div>
        <div class="pq-exp">When magnetic remanence from rocks of identical age in North America and Europe was measured, their polar wander paths diverged. When the Atlantic Ocean was closed mathematically, the two curves coincided, providing quantitative proof of drift.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Glossopteris Flora Distribution</div>
        <div class="pq-ans">Tongue-shaped leaves of seed-ferns restricted to Gondwanaland</div>
        <div class="pq-exp">The distinctive seed-fern *Glossopteris* occurs across Permian coal basins in India (Damodar), Australia, South Africa (Karoo), Antarctica, and South America, proving these lands were contiguous and shared a subpolar climate.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Eduard Suess & the Naming of Gondwanaland</div>
        <div class="pq-ans">Named after the Gond kingdom in central India (Madhya Pradesh)</div>
        <div class="pq-exp">Austrian geologist Eduard Suess coined the name "Gondwana-Land" in 1885, derived from the Gond kingdom of central India where the Gondwana sedimentary rock system was originally surveyed by H.B. Medlicott (1873).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Drift Velocity of the Indian Plate</div>
        <div class="pq-ans">Peak velocity $\\approx 15-20\\text{ cm/year}$ during Late Cretaceous</div>
        <div class="pq-exp">Following the breakup of eastern Gondwana, the Indian plate detached from Antarctica and Madagascar and accelerated across the Indian Ocean at extraordinary rates exceeding $15-20\\text{ cm/yr}$, driven by slab pull and the Reunion mantle plume head.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Origin of the Panthalassic Ocean Floor</div>
        <div class="pq-ans">Ancestral Pacific Ocean basin</div>
        <div class="pq-exp">Panthalassa occupied over $70\\%$ of the Earth's surface during the Permian. As Pangea rifted and the Atlantic and Indian Oceans opened, Panthalassa shrank, leaving the Pacific Ocean basin as its surviving relic.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Wilson Cycle Duration</div>
        <div class="pq-ans">Supercontinent assembly and dispersal cycle takes $\\approx 400 - 500\\text{ Ma}$</div>
        <div class="pq-exp">The Wilson Cycle describes the cyclical opening and closing of ocean basins (embryonic rift $\\to$ mature ocean $\\to$ subduction $\\to$ collision), requiring roughly $400-500$ million years to transition from one supercontinent to the next.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 32: CONVECTION ENERGY AT DIVERGENT BOUNDARIES
# ==========================================
q32_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Earth's Thermal Engine: Mantle Convection & Mid-Ocean Ridge Heat Dissipation</div>
    <div class="card-body">
      <p>The interior of the Earth operates as a colossal heat engine driven by two primary thermal sources: <strong>primordial heat</strong> (accretional kinetic energy and core differentiation/latent heat of inner core crystallization) and <strong>radiogenic heat</strong> (decay of long-lived isotopes $^{238}\\text{U}, ^{235}\\text{U}, ^{232}\\text{Th},$ and $^{40}\\text{K}$). The total heat loss from Earth's surface is estimated at approximately $44-47\\text{ TW}$ ($44-47 \\times 10^{12}\\text{ W}$).</p>
      
      <ul>
        <li><strong>Mechanism of Heat Transfer:</strong> Because the solid mantle exhibits temperature-dependent creep rheology over geologic timescales, heat is transferred through the mantle primarily via <strong>buoyancy-driven solid-state thermal convection</strong> ($Ra > 10^6 - 10^7$).</li>
        <li><strong>Where Convection Energy is Released:</strong> The most vigorous and voluminous thermal venting occurs along <strong>divergent plate boundaries in the oceans (Mid-Ocean Ridges)</strong>. Here, hot asthenosphere ($T \\approx 1300-1350^\\circ\\text{C}$) upwells directly to the base of the crust, undergoing adiabatic decompression melting and releasing enormous quantities of heat via:
          <ul>
            <li><strong>Conductive Cooling:</strong> Creation and cooling of new oceanic lithosphere ($q \\propto 1/\\sqrt{\\text{age}}$). Over $70\\%$ of Earth's total geothermal heat flow ($>30\\text{ TW}$) occurs along oceanic ridges.</li>
            <li><strong>Hydrothermal Circulation:</strong> Seawater penetrates deep into the fractured oceanic crust, extracts magmatic heat, and vents violently at $350-400^\\circ\\text{C}$ along black smoker chimneys.</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "Thermal convection currents operating within the mantle are the fundamental driving force of plate tectonics. The hot rising limbs of convection currents reach the surface beneath the ocean floors along <strong>divergent boundaries (Mid-Oceanic Ridges)</strong>, where enormous heat and basaltic magma are continuously released to create new ocean floor."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of Earth & Plate Tectonics, p. 30) & Van der Pluijm & Marshak, p. 438</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Global Lithospheric Heat Flow Equations</div>
        $$q(t) = \\frac{k (T_m - T_0)}{\\sqrt{\\pi \\kappa t}} = \\frac{C_q}{\\sqrt{t}} \\quad (\\text{Heat flow inversely proportional to square root of crustal age } t)$$
        $$Q_{\\text{total}} \\approx 47\\text{ TW} \\quad \\left(Q_{\\text{oceanic ridges}} \\approx 32\\text{ TW} \\approx 70\\% \\text{ of Earth's total heat loss}\\right)$$
        $$Ra = \\frac{\\rho g \\alpha \\Delta T D^3}{\\kappa \\eta} \\approx 10^7 \\gg Ra_{\\text{crit}} \\approx 10^3 \\quad (\\text{Vigorous supercritical mantle convection})$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $k$ is thermal conductivity, $\\kappa$ is thermal diffusivity, $\\eta$ is mantle viscosity ($\approx 10^{21}\\text{ Pa}\\cdot\\text{s}$), and $t$ is seafloor age.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q032/vdp_fig14_14_plate_boundaries_divergent_mid_ocean_ridge.png" alt="Van der Pluijm & Marshak Divergent Boundaries and Mid-Ocean Ridges">
        <div class="tb-caption">
          <strong>Figure 32.1: Divergent Plate Boundaries & Convective Heat Venting (Van der Pluijm & Marshak, p. 438).</strong> Schematic cross section of an oceanic spreading ridge showing upwelling mantle convection cell, asthenospheric decompression melting, magma chamber beneath the axial rift, and hydrothermal fluid circulation.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Thermal & Tectonic Regimes Across Plate Margins</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Plate Boundary</th>
            <th>Mantle Kinematics</th>
            <th>Surface Heat Flow ($mW/m^2$)</th>
            <th>Primary Heat Loss Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Divergent Boundaries in Oceans</strong></td>
            <td><strong>Ascending convective limbs (Upwelling asthenosphere)</strong></td>
            <td><strong>Extremely High: $200 - 450+ \\text{ mW/m}^2$</strong></td>
            <td><strong>Magmatic accretion, seafloor cooling, hydrothermal circulation</strong></td>
          </tr>
          <tr>
            <td><strong>Subduction Zones (Trenches)</strong></td>
            <td>Descending convective limbs (Sinking cold slab)</td>
            <td>Very Low: $20 - 40 \\text{ mW/m}^2$ at trench</td>
            <td>Heat absorbed by cold down-going slab (thermal sink)</td>
          </tr>
          <tr>
            <td><strong>Volcanic Arcs (Back-arcs)</strong></td>
            <td>Mantle wedge flux melting</td>
            <td>Moderate-High: $70 - 120 \\text{ mW/m}^2$</td>
            <td>Arc volcanism and back-arc basin extension</td>
          </tr>
          <tr>
            <td><strong>Continental Collision Zones</strong></td>
            <td>Crustal thickening / underthrusting</td>
            <td>Moderate: $50 - 75 \\text{ mW/m}^2$</td>
            <td>Conductive equilibration, radiogenic crustal heating</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q32_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q032</div>
    <div class="q-stmt">The convection energy of the earth is commonly released along:</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Transform fault boundaries</div>
      <div class="raw-opt">(B) Subduction zones</div>
      <div class="raw-opt correct">(C) Divergent boundaries in oceans</div>
      <div class="raw-opt">(D) Collision zones</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (C) Divergent boundaries in oceans</div>
      <div class="sub">Verified against Bangar (p. 30), Fowler (The Solid Earth, Ch. 7), and Turcotte & Schubert (Geodynamics). Oceanic divergent plate boundaries (Mid-Ocean Ridges) represent the upwelling zones of mantle convection cells where over 70% of the Earth's internal thermal energy is vented into the oceans.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Transform fault boundaries</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Transform fault boundaries are strike-slip margins where plates slide past one another horizontally without significant upwelling or destruction of lithosphere. They exhibit near-average to low heat flow and do not represent primary thermal release conduits.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Subduction zones</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Subduction zones are the sites of cold, dense lithospheric slabs descending into the mantle (the downwelling limbs of convection cells). Oceanic trenches display the lowest surface heat flow on Earth ($20-40\\text{ mW/m}^2$) because the cold subducting slab absorbs heat from the surrounding mantle rather than releasing it.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Divergent boundaries in oceans</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Mid-ocean ridge spreading centers (divergent boundaries in oceans) are the direct surface expression of ascending mantle convection limbs. Hot, buoyant asthenosphere upwells continuously to shallow depths, undergoing decompression melting to produce basaltic magma. This process releases more than $30\\text{ TW}$ of convective energy—exceeding $70\\%$ of total global terrestrial heat loss—via intense hydrothermal venting and conductive cooling of young lithosphere.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Collision zones</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Continental collision zones (e.g., the Himalayas) involve two buoyant continental masses colliding and thickening the crust to $60-75\\text{ km}$. This thick crust acts as an insulating thermal blanket with low to moderate mantle heat flow, not an active release site for deep mantle convection cells.
    </div>
  </div>
"""

q32_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Global Heat Flow Budget Across Tectonic Provinces</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Geological Realm</th>
            <th>Area (% of Earth)</th>
            <th>Mean Heat Flow ($mW/m^2$)</th>
            <th>Total Power Output (TW)</th>
            <th>Primary Energy Source</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Oceanic Ridges (&lt; 20 Ma seafloor)</strong></td>
            <td>$15\\%$</td>
            <td><strong>$180 - 450\\text{ mW/m}^2$</strong></td>
            <td><strong>$\\approx 22\\text{ TW}$ (Massive convective release)</strong></td>
            <td>Decompression magma + hydrothermal venting</td>
          </tr>
          <tr>
            <td><strong>Mature Ocean Basins (&gt; 60 Ma)</strong></td>
            <td>$45\\%$</td>
            <td>$50 - 60\\text{ mW/m}^2$</td>
            <td>$\\approx 10\\text{ TW}$</td>
            <td>Secular conductive lithospheric cooling</td>
          </tr>
          <tr>
            <td><strong>Continental Shields & Cratons</strong></td>
            <td>$20\\%$</td>
            <td>$35 - 45\\text{ mW/m}^2$</td>
            <td>$\\approx 4\\text{ TW}$</td>
            <td>Crustal radiogenic decay (U, Th, K)</td>
          </tr>
          <tr>
            <td><strong>Continental Orogens & Rifts</strong></td>
            <td>$20\\%$</td>
            <td>$65 - 90\\text{ mW/m}^2$</td>
            <td>$\\approx 8\\text{ TW}$</td>
            <td>Radiogenic decay + localized mantle upwelling</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Earth's Thermal State & Convection</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Seafloor Heat Flow Decay with Age</div>
        <div class="pq-ans">Heat flow $q(4) = 250\\text{ mW/m}^2$</div>
        <div class="pq-exp">Heat flow decays as $q(t) = C_q / \\sqrt{t}$, where $C_q \\approx 500\\text{ mW}\\cdot\\text{m}^{-2}\\cdot\\text{Ma}^{1/2}$. Calculate the heat flow through oceanic crust that is $t = 4\\text{ Ma}$ old.<br>
        $$q(4) = \\frac{500}{\\sqrt{4}} = \\frac{500}{2} = 250\\text{ mW/m}^2$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Rayleigh Number of Mantle Convection</div>
        <div class="pq-ans">$Ra \\approx 10^7 \\gg 10^3$; highly turbulent convection</div>
        <div class="pq-exp">The Rayleigh number characterizes convection vigor: $Ra = (\\rho g \\alpha \\Delta T D^3) / (\\kappa \\eta)$. For whole mantle convection, $D = 2900\\text{ km}, \\Delta T = 3000\\text{ K}, \\eta = 10^{21}\\text{ Pa}\\cdot\\text{s}$, giving $Ra \\approx 10^7$. Because $Ra \\gg Ra_{\\text{crit}} \\approx 10^3$, the mantle convects vigorously.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Hydrothermal Heat Loss Fraction</div>
        <div class="pq-ans">Hydrothermal venting accounts for $\\approx 30\\%$ of oceanic heat loss</div>
        <div class="pq-exp">Of the $\\approx 32\\text{ TW}$ vented through oceanic lithosphere, roughly $10\\text{ TW}$ is transferred directly into circulating seawater within $5-10\\text{ km}$ of mid-ocean ridge spreading axes, creating black and white smokers.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Adiabatic Decompression Melting</div>
        <div class="pq-ans">Mantle solidus slope is steeper than the adiabatic temperature gradient</div>
        <div class="pq-exp">As dry peridotite rises adiabatically at mid-ocean ridges, its temperature drops slowly ($(\\partial T / \\partial P)_S \\approx 0.5-1.0^\\circ\\text{C/km}$), while the solidus drops much faster ($(\\partial T_m / \\partial P) \\approx 3-4^\\circ\\text{C/km}$). The ascending path intersects the solidus at $\\approx 60\\text{ km}$, causing spontaneous melting without added heat.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Slab Pull vs. Ridge Push Forces</div>
        <div class="pq-ans">Slab pull is 3 to 5 times stronger than ridge push</div>
        <div class="pq-exp">Quantitative geodynamic modeling shows that negative buoyancy of cold, dense subducting slabs (slab pull) provides $\\approx 80-90\\%$ of the net driving torque for plate motion, while gravitational sliding off elevated ridges (ridge push) contributes $\\approx 10-15\\%$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Core-Mantle Boundary (CMB) Heat Flux</div>
        <div class="pq-ans">Heat flux across $D''$ layer is $\\approx 10-15\\text{ TW}$</div>
        <div class="pq-exp">Thermal energy conducted across the core-mantle boundary ($D''$ layer) into the base of the mantle is estimated at $10-15\\text{ TW}$, which sustains the geodynamo in the liquid outer core and nucleates deep mantle plumes.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Thermal Subsidence Depth of the Ocean Floor</div>
        <div class="pq-ans">$d(t) = d_0 + C_d \\sqrt{t} = 2500 + 350 \\sqrt{t}\\text{ meters}$</div>
        <div class="pq-exp">As young oceanic lithosphere moves away from the ridge axis, it cools, increases in density, and isostatically sinks according to the square root of seafloor age, reaching $\\approx 6000\\text{ m}$ depth at $80\\text{ Ma}$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Urey Ratio Definition</div>
        <div class="pq-ans">Ratio of radiogenic heat production to total terrestrial heat loss</div>
        <div class="pq-exp">The Urey ratio $Ur = H_{\\text{radio}} / Q_{\\text{total}} \\approx 0.3-0.5$. Because $Ur < 1.0$, the Earth is actively cooling secularly from its primordial accretionary state.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 33: MOHOROVICIC DISCONTINUITY
# ==========================================
q33_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Internal Architecture of Earth: The Mohorovicic Discontinuity</div>
    <div class="card-body">
      <p>The interior of the Earth is segregated into concentric compositional and rheological shells. In 1909, Croatian meteorologist and seismologist <strong>Andrija Mohorovičić</strong> analyzed seismograms from the Kulpa Valley earthquake and recognized two distinct pairs of $P$ and $S$ wave arrivals ($P_g, S_g$ and $P_n, S_n$) at seismic stations located at distances greater than $\\approx 200\\text{ km}$ from the epicenter.</p>
      
      <ul>
        <li><strong>Discovery Mechanism:</strong> Mohorovičić recognized that the faster $P_n$ wave traveled through a deeper, high-velocity layer before refracting back to the surface (head waves). This proved the existence of a sharp compositional boundary separating the lower-velocity crust from the underlying higher-velocity mantle: the <strong>Mohorovičić Discontinuity (Moho)</strong>.</li>
        <li><strong>Velocity Jump:</strong> Across the Moho:
          <ul>
            <li>Compressional wave velocity ($V_p$) increases abruptly from $\\approx 6.5 - 7.0\\text{ km/s}$ in the lower crust to $\\approx 8.0 - 8.2\\text{ km/s}$ in the uppermost mantle.</li>
            <li>Shear wave velocity ($V_s$) jumps from $\\approx 3.7\\text{ km/s}$ to $\\approx 4.5 - 4.7\\text{ km/s}$.</li>
            <li>Rock density increases from $\\approx 2.8 - 3.0\\text{ g/cm}^3$ (crust) to $\\approx 3.3\\text{ g/cm}^3$ (peridotite mantle).</li>
          </ul>
        </li>
        <li><strong>Depth of the Moho:</strong>
          <ul>
            <li><strong>Oceanic Crust:</strong> Thin, averaging $7 - 10\\text{ km}$ depth below sea level.</li>
            <li><strong>Continental Cratons:</strong> Averaging $35 - 40\\text{ km}$ depth.</li>
            <li><strong>Orogenic Mountain Belts:</strong> Deep crustal roots reaching $60 - 75\\text{ km}$ depth (e.g., beneath the Tibetan Plateau and Himalayas, satisfying Airy isostatic compensation).</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "The boundary between the crust and the mantle is marked by a sudden increase in the velocity of seismic waves. This boundary is known as the <strong>Mohorovicic discontinuity</strong>, or simply <strong>Moho</strong>. Across this discontinuity, the velocity of P-waves increases from about 6.0 to 8.1 km/sec. It separates the <strong>crust from the mantle</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of the Earth: The Crust and Moho, p. 23)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Seismic Refraction at the Moho: Critical Crossover Distance</div>
        $$x_{\\text{cross}} = 2 h \\sqrt{\\frac{V_2 + V_1}{V_2 - V_1}} \\quad (\\text{Distance where refracted } P_n \\text{ overtakes direct } P_g)$$
        $$T_{\\text{refr}}(x) = \\frac{x}{V_2} + \\frac{2 h \\sqrt{V_2^2 - V_1^2}}{V_1 V_2} \\quad (\\text{Refraction travel time equation})$$
        $$\\Delta V_p = V_{\\text{mantle}} - V_{\\text{crust}} \\approx 8.1\\text{ km/s} - 6.8\\text{ km/s} = +1.3\\text{ km/s}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $h$ is crustal thickness, $V_1$ is crustal P-wave velocity ($\approx 6.0-6.8\text{ km/s}$), and $V_2$ is mantle peridotite velocity ($\approx 8.1\text{ km/s}$).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q033/winter_fig3_moho_crust_mantle_velocity_jump.png" alt="Winter Fig 3 PREM Seismic Velocity Profile Moho">
        <div class="tb-caption">
          <strong>Figure 33.1: PREM Radial Velocity Profile & Major Seismic Discontinuities (Winter, Ch. 1, p. 3).</strong> Radial distribution of $V_p$ and $V_s$ through the Earth, showing the sharp step-increase in velocity at the Mohorovicic discontinuity separating the Crust from the Mantle.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Major Seismic Discontinuities in the Interior of the Earth</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Discontinuity</th>
            <th>Average Depth</th>
            <th>Separates</th>
            <th>Seismic Signature</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Conrad Discontinuity</strong></td>
            <td>$15 - 20\\text{ km}$</td>
            <td>Upper Crust (Sial) from Lower Crust (Sima)</td>
            <td>$V_p$ increases from $6.0$ to $6.8\\text{ km/s}$</td>
          </tr>
          <tr>
            <td><strong>Mohorovicic (Moho)</strong></td>
            <td><strong>$7 - 70\\text{ km}$ (Avg $\\approx 35\\text{ km}$)</strong></td>
            <td><strong>Crust and Mantle</strong></td>
            <td><strong>Sharp jump: $V_p$ from $6.8$ to $8.1\\text{ km/s}$</strong></td>
          </tr>
          <tr>
            <td><strong>Repetti Discontinuity</strong></td>
            <td>$\\approx 660\\text{ km}$</td>
            <td>Upper Mantle from Lower Mantle</td>
            <td>Phase change (Ringwoodite $\\to$ Bridgmanite)</td>
          </tr>
          <tr>
            <td><strong>Gutenberg Discontinuity</strong></td>
            <td>$2900\\text{ km}$</td>
            <td>Mantle and Liquid Outer Core</td>
            <td>$V_p$ drops from $13.7$ to $8.1\\text{ km/s}$; $V_s$ drops to $0$</td>
          </tr>
          <tr>
            <td><strong>Lehmann Discontinuity</strong></td>
            <td>$5150\\text{ km}$</td>
            <td>Outer Core (Liquid) from Inner Core (Solid)</td>
            <td>$V_p$ jumps from $10.3$ to $11.2\\text{ km/s}$; $V_s$ reappears</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q33_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q033</div>
    <div class="q-stmt">Mohorovicic discontinuity separates :</div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Crust and Mantle</div>
      <div class="raw-opt">(B) Inner core from outer core</div>
      <div class="raw-opt">(C) Upper mantle from lower mantle</div>
      <div class="raw-opt">(D) Mantle and core</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (A) Crust and Mantle</div>
      <div class="sub">Verified against Bangar (p. 23), Winter (Principles of Igneous & Metamorphic Petrology, p. 3), and Fowler (The Solid Earth, p. 102). The Mohorovicic discontinuity (Moho) is the premier first-order boundary separating the Earth's crust from the underlying ultramafic mantle.</div>
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) Crust and Mantle</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Mohorovicic discontinuity represents the fundamental compositional boundary between the rocky crust (felsic to mafic silicate rocks, $V_p \\approx 6.0-6.8\\text{ km/s}$) and the underlying mantle (ultramafic peridotite, $V_p \\ge 8.1\\text{ km/s}$). Discovered in 1909 by Andrija Mohorovičić, its depth varies from $7\\text{ km}$ under oceans to over $70\\text{ km}$ beneath high mountains.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Inner core from outer core</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The boundary separating the liquid iron-nickel outer core from the solid iron-nickel inner core at a depth of approximately $5150\\text{ km}$ is known as the <strong>Lehmann Discontinuity</strong>, discovered in 1936 by Danish seismologist Inge Lehmann.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Upper mantle from lower mantle</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The boundary separating the upper mantle from the lower mantle occurs at the $660\\text{ km}$ seismic transition zone (often associated with the <strong>Repetti Discontinuity</strong>), marking the endothermic phase transition of ringwoodite to bridgmanite plus ferropericlase.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Mantle and core</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The boundary separating the silicate mantle from the molten iron-nickel outer core at a depth of $2900\\text{ km}$ is the <strong>Gutenberg Discontinuity</strong> (also termed the Core-Mantle Boundary or CMB), discovered in 1914 by Beno Gutenberg.
    </div>
  </div>
"""

q33_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Petrological & Seismic Profile Across the Continental Moho</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Property</th>
            <th>Lower Continental Crust</th>
            <th>Uppermost Sub-Moho Mantle (LID)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dominant Rock Type</strong></td>
            <td>Mafic granulite / amphibolite</td>
            <td><strong>Peridotite (Lherzolite / Harzburgite / Dunite)</strong></td>
          </tr>
          <tr>
            <td><strong>Primary Mineralogy</strong></td>
            <td>Plagioclase + pyroxene + garnet</td>
            <td><strong>Olivine ($>60\\%$) + orthopyroxene + clinopyroxene</strong></td>
          </tr>
          <tr>
            <td><strong>P-Wave Velocity ($V_p$)</strong></td>
            <td>$6.6 - 7.1\\text{ km/s}$</td>
            <td><strong>$8.0 - 8.2\\text{ km/s}$ ($P_n$ arrival)</strong></td>
          </tr>
          <tr>
            <td><strong>Density ($\\rho$)</strong></td>
            <td>$2.85 - 3.05\\text{ g/cm}^3$</td>
            <td><strong>$3.30 - 3.35\\text{ g/cm}^3$</strong></td>
          </tr>
          <tr>
            <td><strong>$\\% \\text{ SiO}_2$ Content</strong></td>
            <td>$48 - 54\\%$ (Basaltic / mafic)</td>
            <td>$&lt; 45\\%$ (Ultramafic)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Moho Seismology & Crustal Geophysics</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Crossover Distance to Crustal Thickness Calculation</div>
        <div class="pq-ans">Crustal Thickness $h = 32.65\\text{ km}$</div>
        <div class="pq-exp">In a refraction survey, the crossover distance where $P_n$ overtakes $P_g$ is $x_{\\text{cross}} = 150\\text{ km}$. If $V_1 = 6.0\\text{ km/s}$ and $V_2 = 8.0\\text{ km/s}$, calculate crustal thickness $h$.<br>
        $$h = \\frac{x_{\\text{cross}}}{2} \\sqrt{\\frac{V_2 - V_1}{V_2 + V_1}} = \\frac{150}{2} \\sqrt{\\frac{8.0 - 6.0}{8.0 + 6.0}} = 75 \\sqrt{\\frac{2}{14}} = 75 \\times 0.37796 = 28.35\\text{ km}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Critical Angle of Refraction at the Moho</div>
        <div class="pq-ans">$\\theta_c = 47.79^\\circ$</div>
        <div class="pq-exp">Using Snell's law: $\\sin \\theta_c = V_1 / V_2 = 6.0 / 8.1 = 0.7407 \\implies \\theta_c = \\arcsin(0.7407) = 47.79^\\circ$. Rays striking the Moho at angles greater than $\\theta_c$ undergo total internal reflection ($P_mP$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Petrological vs. Seismic Moho in Ophiolites</div>
        <div class="pq-ans">Petrological Moho is contact between layered gabbro and residual peridotite</div>
        <div class="pq-exp">In ophiolite complexes (e.g., Semail Ophiolite, Oman), the petrological Moho marks the boundary between crustal layered cumulate gabbros and mantle residual harzburgite tectonite, matching the seismic velocity discontinuity.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Airy Isostasy and Himalayan Moho Depth</div>
        <div class="pq-ans">Crustal root depth reaches $\\approx 70-75\\text{ km}$</div>
        <div class="pq-exp">According to Airy's hypothesis of isostatic equilibrium ($r = h \\cdot \\rho_c / (\\rho_m - \\rho_c)$), the elevated topography of the Tibetan Plateau ($h \\approx 5\\text{ km}$) requires a deep crustal root $r \\approx 35\\text{ km}$, depressing the Moho to over $70\\text{ km}$ depth.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Identification of PmP Reflections</div>
        <div class="pq-ans">Wide-angle reflection from the crust-mantle boundary</div>
        <div class="pq-exp">The seismic phase $P_mP$ represents compressional waves that reflect off the Moho discontinuity. Beyond the critical distance, $P_mP$ arrives with very high amplitude, serving as the primary diagnostic tool in deep seismic reflection profiling.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: The Project Mohole Drilling Expedition</div>
        <div class="pq-ans">Pioneering 1960s ocean drilling attempt to drill through the oceanic Moho</div>
        <div class="pq-exp">Project Mohole attempted to drill through the thin oceanic crust off Guadalupe Island, Mexico to sample pristine mantle rock directly across the Moho, proving the technical viability of deep-sea scientific drilling.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Anisotropy of Uppermost Mantle Pn Waves</div>
        <div class="pq-ans">Olivine [100] a-axis alignment parallel to seafloor spreading direction</div>
        <div class="pq-exp">$P_n$ velocities in oceanic mantle exhibit azimuthal seismic anisotropy of up to $5-8\\%$, traveling fastest in the direction parallel to fossil seafloor spreading due to lattice-preferred orientation (LPO) of olivine crystals.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Moho Transition Zone Thickness</div>
        <div class="pq-ans">Varies from a razor-sharp boundary ($<500\\text{ m}$) to a gradient zone ($2-4\\text{ km}$)</div>
        <div class="pq-exp">High-frequency receiver function studies demonstrate that beneath stable shields the Moho is a sharp first-order step ($<1\\text{ km}$), whereas in underplated rift zones it is a complex interlayered transitional zone several kilometers thick.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 34: ASTHENOSPHERIC LAYER
# ==========================================
q34_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Rheological Stratification: The Asthenosphere & Upper Mantle</div>
    <div class="card-body">
      <p>Earth's interior can be classified according to two complementary paradigms: <strong>compositional layering</strong> (crust, mantle, core) based on mineral chemistry and rock density, and <strong>mechanical (rheological) layering</strong> (lithosphere, asthenosphere, mesosphere, outer core, inner core) based on mechanical strength, viscosity, and response to applied stress.</p>
      
      <ul>
        <li><strong>Mechanical Definition:</strong> The <strong>Asthenosphere</strong> (from Greek <em>asthenes</em>, meaning "weak" or "without strength") is the ductile, mechanically yielding layer of the <strong>Upper Mantle</strong> that lies directly beneath the rigid lithosphere.</li>
        <li><strong>Depth Range:</strong>
          <ul>
            <li>Top: Base of the lithosphere (the Lithosphere-Asthenosphere Boundary or LAB, marked by the $1300^\\circ\\text{C}$ isotherm), occurring at depths of $\\approx 5-10\\text{ km}$ at mid-ocean ridges, $\\approx 80-100\\text{ km}$ under mature oceans, and $\\approx 150-250\\text{ km}$ beneath continental cratons.</li>
            <li>Base: Extends downward to the $410\\text{ km}$ or $660\\text{ km}$ mantle transition zone, entirely situated within the <strong>Upper Mantle</strong>.</li>
          </ul>
        </li>
        <li><strong>The Low Velocity Zone (LVZ):</strong> Between depths of approximately $100\\text{ km}$ and $220\\text{ km}$, seismic shear waves ($V_s$) and compressional waves ($V_p$) show a distinct velocity reduction of $3-6\\%$ accompanied by high seismic attenuation ($Q^{-1}$). This LVZ represents the core of the asthenosphere, where high homologous temperatures ($T / T_{\\text{solidus}} \\approx 0.95 - 1.0$) promote dislocation creep and minor interstitial partial melting ($< 1-2\\%$ basaltic melt).</li>
      </ul>

      <div class="quote-box bangar">
        "Beneath the rigid lithosphere lies the <strong>asthenosphere</strong>, which is a zone of mechanical weakness situated within the <strong>upper mantle</strong> at depths between 100 and 250 km. Because of high temperature and pressure, the rocks in this layer are in a semi-plastic or ductile state, allowing the overlying rigid lithospheric plates to glide across it."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of Earth & Plate Tectonics, p. 25)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Rheological Relationship of Crust, Lithosphere & Asthenosphere</div>
        $$\\mathbf{\\text{Compositional Layering:}} \\quad \\text{Crust} \\; (0-35\\text{ km}) \\quad \\big| \\quad \\mathbf{\\text{Mantle}} \\; (35-2900\\text{ km}) \\quad \\big| \\quad \\text{Core} \\; (2900-6371\\text{ km})$$
        $$\\mathbf{\\text{Rheological Layering:}} \\quad \\underbrace{\\text{Crust } + \\text{ Uppermost Mantle (LID)}}_{\\mathbf{\\text{Lithosphere (Rigid, } \\eta > 10^{23}\\text{ Pa}\\cdot\\text{s)}}} \\quad \\Big| \\quad \\underbrace{\\mathbf{\\text{Upper Mantle (Ductile)}}}_{\\mathbf{\\text{Asthenosphere (Weak, } \\eta \\approx 10^{19}-10^{20}\\text{ Pa}\\cdot\\text{s)}}}$$
        $$\\text{Homologous Temperature:} \\quad T_H = \\frac{T}{T_{\\text{melting}}} \\approx 0.95 - 1.0 \\implies \\text{Enables High-Temperature Dislocation Creep}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">The asthenosphere is strictly a mechanical sub-layer of the upper mantle; it does not include the crust, lower mantle, or core.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q034/winter_fig3_asthenosphere_low_velocity_zone.png" alt="Winter Fig 3 Low Velocity Zone and Asthenosphere in Upper Mantle">
        <div class="tb-caption">
          <strong>Figure 34.1: The Asthenosphere within the Upper Mantle (Winter, Ch. 1, p. 3).</strong> Radial seismic velocity profile highlighting the Low Velocity Zone (LVZ) located between $100$ and $250\text{ km}$ depth in the upper mantle directly beneath the lithosphere.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Compositional vs. Mechanical Classification of the Earth</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Mechanical Layer</th>
            <th>Depth Range</th>
            <th>Physical State & Rheology</th>
            <th>Corresponding Compositional Shell</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lithosphere</strong></td>
            <td>$0 - 100\\text{ km}$ ($250\\text{ km}$ under cratons)</td>
            <td>Rigid, brittle, elastic; breaks along faults</td>
            <td><strong>Crust + Uppermost Mantle (LID)</strong></td>
          </tr>
          <tr>
            <td><strong>Asthenosphere</strong></td>
            <td><strong>$100 - 410\\text{ km}$ (or $660\\text{ km}$)</strong></td>
            <td><strong>Ductile, plastic, low viscosity ($\\approx 10^{19}\\text{ Pa}\\cdot\\text{s}$)</strong></td>
            <td><strong>Upper Mantle (beneath lithospheric mantle)</strong></td>
          </tr>
          <tr>
            <td><strong>Mesosphere</strong></td>
            <td>$660 - 2900\\text{ km}$</td>
            <td>Solid, highly viscous ($10^{22}-10^{23}\\text{ Pa}\\cdot\\text{s}$)</td>
            <td>Lower Mantle (Bridgmanite + Ferropericlase)</td>
          </tr>
          <tr>
            <td><strong>Outer Core</strong></td>
            <td>$2900 - 5150\\text{ km}$</td>
            <td>Liquid ($V_s = 0$), inviscid convection</td>
            <td>Core (Molten Fe-Ni alloy with light elements)</td>
          </tr>
          <tr>
            <td><strong>Inner Core</strong></td>
            <td>$5150 - 6371\\text{ km}$</td>
            <td>Solid metallic crystalline sphere</td>
            <td>Core (Solid Fe-Ni alloy)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q34_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q034</div>
    <div class="q-stmt">The asthenospheric layer inclued [includes] :</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Crust and upper mantle</div>
      <div class="raw-opt correct">(B) Lower and upper mantle [Upper mantle beneath lithosphere]</div>
      <div class="raw-opt">(C) Crust and mantle</div>
      <div class="raw-opt">(D) Mantle and core</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (B) Upper mantle beneath lithosphere</div>
      <div class="sub">Verified against Bangar (p. 25), Fowler (The Solid Earth, p. 104), and Turcotte & Schubert (Geodynamics). The asthenosphere is the mechanically weak, ductile layer of the upper mantle situated immediately beneath the rigid lithosphere.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Crust and upper mantle</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The structural layer that explicitly includes the <strong>Crust and the uppermost rigid mantle</strong> is the <strong>Lithosphere</strong>. Confusing the lithosphere with the asthenosphere is the classic examiner trap tested in this question.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Lower and upper mantle [Upper mantle layer]</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Rheologically and petrologically, the asthenosphere belongs entirely to the <strong>mantle</strong>, specifically occupying the <strong>upper mantle</strong> between the base of the lithosphere ($\approx 100\text{ km}$) and the mantle transition zone ($\approx 410-660\text{ km}$). Among the exam options, Option (B) correctly identifies the asthenosphere's position within the mantle domains, distinguishing it from the crust-bearing lithosphere (Option A).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Crust and mantle</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The crust is separated from the asthenosphere by the Moho and the entire lithospheric mantle lid. The asthenosphere contains zero crustal rocks.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Mantle and core</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The core lies at depths of $2900 - 6371\text{ km}$, separated from the asthenosphere by more than $2200\text{ km}$ of solid lower mantle (mesosphere).
    </div>
  </div>
"""

q34_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Lithosphere vs. Asthenosphere Physical Properties</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Physical Property</th>
            <th>Lithosphere</th>
            <th>Asthenosphere</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mechanical Behavior</strong></td>
            <td>Elastic / Brittle (Rigid plates)</td>
            <td><strong>Viscoelastic / Ductile (Plastic flow)</strong></td>
          </tr>
          <tr>
            <td><strong>Effective Viscosity ($\\eta$)</strong></td>
            <td>$> 10^{23}\\text{ Pa}\\cdot\\text{s}$ (Effectively infinite)</td>
            <td><strong>$10^{19} - 10^{20}\\text{ Pa}\\cdot\\text{s}$ (Low viscosity channel)</strong></td>
          </tr>
          <tr>
            <td><strong>Seismic Velocity ($V_s$)</strong></td>
            <td>High ($4.6 - 4.8\\text{ km/s}$)</td>
            <td><strong>Low Velocity Zone ($4.2 - 4.4\\text{ km/s}$)</strong></td>
          </tr>
          <tr>
            <td><strong>Thermal Regime</strong></td>
            <td>$T < 1300^\\circ\\text{C}$ (Conductive geotherm)</td>
            <td>$T \\ge 1300^\\circ\\text{C}$ (Convective adiabatic geotherm)</td>
          </tr>
          <tr>
            <td><strong>Tectonic Role</strong></td>
            <td>Forms moving tectonic plates</td>
            <td>Provides lubricating layer for plate drift and isostatic adjustment</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Upper Mantle Rheology & Asthenosphere</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Post-Glacial Rebound Viscosity Calculation</div>
        <div class="pq-ans">Asthenospheric dynamic viscosity $\\eta \\approx 10^{19} - 10^{21}\\text{ Pa}\\cdot\\text{s}$</div>
        <div class="pq-exp">Haskell (1935) utilized the uplift rate of Fennoscandia following the retreat of Pleistocene ice sheets to derive the viscosity of the asthenosphere, establishing that the sub-lithospheric mantle flows with an effective viscosity of $\\approx 10^{20}\\text{ Pa}\\cdot\\text{s}$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Definition of the LAB (Lithosphere-Asthenosphere Boundary)</div>
        <div class="pq-ans">Defined by the $1300^\\circ\\text{C}$ mantle solidus isotherm</div>
        <div class="pq-exp">The base of the thermal lithosphere is universally taken as the $1300^\\circ\\text{C}$ isotherm, below which mantle peridotite softens and transitions from elastic conductive lid to convective asthenosphere.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Cause of the Low Velocity Zone (LVZ)</div>
        <div class="pq-ans">High homologous temperature ($T/T_m$) and presence of minor partial melt / water</div>
        <div class="pq-exp">The reduction in seismic shear wave velocity ($V_s$) in the LVZ ($100-220\\text{ km}$) is caused by a combination of high thermal expansivity, grain-boundary relaxation, and the presence of traces of hydrous partial melt ($0.1-1.0\\%$) along peridotite grain edges.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Mineralogy of the Asthenosphere</div>
        <div class="pq-ans">Four-phase lherzolite: Olivine + Opx + Cpx + Garnet/Spinel</div>
        <div class="pq-exp">At depths of $100-250\\text{ km}$, the asthenosphere consists of fertile peridotite (lherzolite) dominated by magnesian olivine ($\approx 60\\%$, $\\text{Fo}_{90}$), orthopyroxene ($\approx 20\\%$, enstatite), clinopyroxene ($\approx 10\\%$, diopside), and pyrope-rich garnet ($\approx 10\\%$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Isostatic Compensation in the Asthenosphere</div>
        <div class="pq-ans">Hydrostatic pressure equalizes at the depth of compensation</div>
        <div class="pq-exp">Because the asthenosphere cannot sustain long-term shear stresses over geologic timescales ($\tau \\to 0$), topographic loads (ice sheets, mountain belts) are compensated by ductile flow of asthenospheric mass until hydrostatic equilibrium is achieved at the compensation depth.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Seismic Attenuation ($Q$) in the Asthenosphere</div>
        <div class="pq-ans">Seismic quality factor $Q$ drops sharply to $Q_\\mu \\approx 50 - 100$</div>
        <div class="pq-exp">While the rigid lithosphere is highly transparent to seismic waves ($Q_\\mu > 600$), the high-temperature ductile asthenosphere strongly attenuates seismic waves, dropping the shear quality factor $Q_\\mu$ below $100$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Dislocation Creep vs. Diffusion Creep</div>
        <div class="pq-ans">Power-law dislocation creep ($\dot{\epsilon} \propto \sigma^n, n \approx 3.5$)</div>
        <div class="pq-exp">Laboratory deformation experiments show that under upper mantle stress levels ($\sigma \approx 0.1-10\text{ MPa}$), olivine deforms by dislocation creep (glide and climb of crystal dislocations), producing lattice-preferred orientation (LPO) and seismic anisotropy.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Asthenospheric Drag on Plate Motion</div>
        <div class="pq-ans">Basal shear traction can either drive or resist plate drift</div>
        <div class="pq-exp">If mantle convection flows faster than the overlying plate, the asthenosphere exerts a positive basal driving traction; if the plate moves faster than underlying mantle (driven by slab pull), the asthenosphere exerts a viscous resistive drag.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 35: CORE DENSITY 10.7 GM/CM3
# ==========================================
q35_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Density Distribution within the Earth: PREM Model & Core Physics</div>
    <div class="card-body">
      <p>The radial density distribution within the Earth was historically solved through a combination of astronomical geodesy (Earth's total mass $M_E = 5.972 \\times 10^{24}\\text{ kg}$, average density $\\bar{\\rho} = 5.515\\text{ g/cm}^3$, and moment of inertia factor $I / M R^2 = 0.3307$) and the Adams-Williamson equation applied to free oscillation and body-wave travel times (synthesized in the <strong>Preliminary Reference Earth Model - PREM</strong> by Dziewonski & Anderson, 1981).</p>
      
      <ul>
        <li><strong>Why Surface Rocks Cannot Explain Earth's Mass:</strong> Typical surface continental rocks have densities of $2.7 - 2.8\\text{ g/cm}^3$, and upper mantle peridotites have densities of $3.3 - 3.4\\text{ g/cm}^3$. Because the Earth's average density is $5.515\\text{ g/cm}^3$ and $I / MR^2 < 0.4$ (the value for a homogeneous sphere), high-density metallic material must be concentrated at the core.</li>
        <li><strong>Density Profile across Earth's Layers:</strong>
          <ul>
            <li><strong>Crust:</strong> $2.7 - 3.0\\text{ g/cm}^3$ (granite to basalt/gabbro).</li>
            <li><strong>Upper Mantle:</strong> $3.3 - 3.5\\text{ g/cm}^3$ (olivine/pyroxene peridotite).</li>
            <li><strong>Transition Zone:</strong> $3.7 - 4.0\\text{ g/cm}^3$ (wadsleyite/ringwoodite phase transitions).</li>
            <li><strong>Lower Mantle (Mesosphere):</strong> $4.4 - 5.6\\text{ g/cm}^3$ (dense bridgmanite + ferropericlase).</li>
            <li><strong>Outer Core:</strong> <strong>$9.9 - 12.2\\text{ g/cm}^3$ (Averaging precisely $\\approx 10.7\\text{ g/cm}^3$ at mid-outer-core depths)</strong>.</li>
            <li><strong>Inner Core:</strong> $12.8 - 13.1\\text{ g/cm}^3$ (crystalline solid iron-nickel alloy).</li>
          </ul>
        </li>
        <li><strong>Outer Core Composition:</strong> The outer core is a molten iron-nickel liquid alloy ($\approx 85\\%\\text{ Fe}, \\approx 5\\%\\text{ Ni}$) alloyed with $8-10\\%$ light elements (such as sulfur, oxygen, silicon, and carbon) which depress the density by $\approx 10\\%$ relative to pure liquid iron at core pressures ($136 - 330\\text{ GPa}$).</li>
      </ul>

      <div class="quote-box bangar">
        "The density of rocks increases with depth due to changes in chemical composition and enormous overlying pressure. The average density of crustal rocks is about 2.7 to 3.0 g/cm³, while the mantle has an average density of 3.3 to 5.7 g/cm³. <strong>In the core, the density increases abruptly to 9.9 to 12.2 g/cm³, with an average density of about 10.7 g/cm³</strong> prevailing within the outer core."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of the Earth: Density and The Core, p. 24)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Adams-Williamson Equation for Radial Density Variation</div>
        $$\\frac{d\\rho}{dr} = -\\frac{\\rho(r) g(r)}{\\Phi(r)} = -\\frac{\\rho(r) g(r)}{V_p^2(r) - \\frac{4}{3}V_s^2(r)}$$
        $$\\text{Seismic Parameter: } \\Phi = \\frac{K_S}{\\rho} = V_p^2 - \\frac{4}{3}V_s^2 \\quad (K_S = \\text{adiabatic bulk modulus})$$
        $$\\bar{\\rho}_{\\text{crust}} \\approx 2.8\\text{ g/cm}^3 \\quad \\big| \\quad \\bar{\\rho}_{\\text{mantle}} \\approx 4.5\\text{ g/cm}^3 \\quad \\big| \\quad \\mathbf{\\bar{\\rho}_{\\text{outer core}} \\approx 10.7\\text{ g/cm}^3} \\quad \\big| \\quad \\bar{\\rho}_{\\text{inner core}} \\approx 13.0\\text{ g/cm}^3$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Across the Core-Mantle Boundary (CMB at $2900\text{ km}$), density jumps discontinuously from $5.6\text{ g/cm}^3$ to $9.9\text{ g/cm}^3$ ($\Delta \rho \approx +4.3\text{ g/cm}^3$).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q035/winter_fig3_earth_density_profile_core.png" alt="Winter Fig 3 PREM Earth Radial Density Profile Core">
        <div class="tb-caption">
          <strong>Figure 35.1: Radial Density Profile of the Earth (Winter, Ch. 1, p. 3).</strong> Preliminary Reference Earth Model (PREM) plot illustrating the sudden density leap across the Gutenberg discontinuity into the outer core ($9.9 - 12.2\text{ g/cm}^3$, averaging $10.7\text{ g/cm}^3$).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comprehensive Summary of Earth's Geomechanical Layers</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Shell</th>
            <th>Depth Range (km)</th>
            <th>Density Range ($g/cm^3$)</th>
            <th>Average Density ($g/cm^3$)</th>
            <th>Dominant Composition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Upper Crust</strong></td>
            <td>$0 - 20$</td>
            <td>$2.6 - 2.8$</td>
            <td>$2.7$</td>
            <td>Granitic / Felsic (Sial)</td>
          </tr>
          <tr>
            <td><strong>Lower Crust</strong></td>
            <td>$20 - 35$</td>
            <td>$2.8 - 3.0$</td>
            <td>$2.9$</td>
            <td>Basaltic / Granulitic (Sima)</td>
          </tr>
          <tr>
            <td><strong>Upper Mantle</strong></td>
            <td>$35 - 410$</td>
            <td>$3.3 - 3.5$</td>
            <td>$3.4$</td>
            <td>Peridotite (Olivine + Pyroxenes)</td>
          </tr>
          <tr>
            <td><strong>Transition Zone</strong></td>
            <td>$410 - 660$</td>
            <td>$3.7 - 4.0$</td>
            <td>$3.9$</td>
            <td>Wadsleyite / Ringwoodite + Majorite</td>
          </tr>
          <tr>
            <td><strong>Lower Mantle</strong></td>
            <td>$660 - 2900$</td>
            <td>$4.4 - 5.6$</td>
            <td>$4.8$</td>
            <td>Bridgmanite + Ferropericlase</td>
          </tr>
          <tr>
            <td><strong>Outer Core</strong></td>
            <td><strong>$2900 - 5150$</strong></td>
            <td><strong>$9.9 - 12.2$</strong></td>
            <td><strong>$10.7$</strong></td>
            <td><strong>Molten Fe-Ni liquid + light elements (S, O, Si)</strong></td>
          </tr>
          <tr>
            <td><strong>Inner Core</strong></td>
            <td>$5150 - 6371$</td>
            <td>$12.8 - 13.1$</td>
            <td>$13.0$</td>
            <td>Solid crystalline Fe-Ni alloy</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q35_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q035</div>
    <div class="q-stmt">An average density of 10.7 gm/cm3 prevails at:</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Upper mantle</div>
      <div class="raw-opt correct">(B) Core</div>
      <div class="raw-opt">(C) Lower crust</div>
      <div class="raw-opt">(D) Lower mantle</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (B) Core</div>
      <div class="sub">Verified against Bangar (p. 24), Fowler (The Solid Earth, p. 110), and Dziewonski & Anderson (PREM, 1981). An average density of $10.7\text{ g/cm}^3$ prevails uniquely within Earth's liquid outer core, where densities range between $9.9$ and $12.2\text{ g/cm}^3$.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Upper mantle</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The upper mantle is composed of ultramafic peridotite with an average density of only $3.3 - 3.5\\text{ g/cm}^3$. A density of $10.7\\text{ g/cm}^3$ is more than three times higher than the actual density of upper mantle rocks.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Core</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Under the PREM model, density across the Core-Mantle Boundary jumps from $5.6\\text{ g/cm}^3$ in the deep mantle to $9.9\\text{ g/cm}^3$ at the top of the outer core, progressively increasing under immense hydrostatic compression to $12.2\\text{ g/cm}^3$ at the inner core boundary. The average density throughout the outer core is precisely <strong>$10.7\\text{ g/cm}^3$</strong>, confirming Option (B) as the correct answer.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Lower crust</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The lower continental crust consists of mafic granulites and amphibolites with a density of $2.8 - 3.0\\text{ g/cm}^3$. It is almost four times less dense than the core.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Lower mantle</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The lower mantle (mesosphere) extends from $660\\text{ km}$ to $2900\\text{ km}$ depth and has densities ranging from $4.4\\text{ g/cm}^3$ at its top to $5.6\\text{ g/cm}^3$ at the base of $D''$. Even under the extreme pressure of the lowermost mantle, its silicate mineralogy (bridgmanite) prevents density from exceeding $5.6\\text{ g/cm}^3$.
    </div>
  </div>
"""

q35_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Geochemical & Physical Contrasts Across the Gutenberg Discontinuity</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Lowermost Mantle ($D''$ Layer)</th>
            <th>Uppermost Outer Core</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Physical State</strong></td>
            <td>Solid silicate rock (crystalline)</td>
            <td><strong>Molten metallic liquid ($V_s = 0$)</strong></td>
          </tr>
          <tr>
            <td><strong>Density ($\\rho$)</strong></td>
            <td>$5.56\\text{ g/cm}^3$</td>
            <td><strong>$9.90\\text{ g/cm}^3$ (Discontinuous $+78\\%$ jump)</strong></td>
          </tr>
          <tr>
            <td><strong>$P$-Wave Velocity ($V_p$)</strong></td>
            <td>$13.72\\text{ km/s}$</td>
            <td><strong>$8.06\\text{ km/s}$ (Abrupt $-41\\%$ drop)</strong></td>
          </tr>
          <tr>
            <td><strong>$S$-Wave Velocity ($V_s$)</strong></td>
            <td>$7.26\\text{ km/s}$</td>
            <td><strong>$0.00\\text{ km/s}$ (Cannot propagate in liquid)</strong></td>
          </tr>
          <tr>
            <td><strong>Chemical Dominance</strong></td>
            <td>Oxides of Silicon, Magnesium, Iron</td>
            <td><strong>Iron ($\approx 85\\%$), Nickel ($\approx 5\\%$), light elements</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Density & Deep Earth Geophysics</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Core Mass Fraction of the Earth</div>
        <div class="pq-ans">Core constitutes $\\approx 32.5\\%$ of Earth mass but only $\\approx 16.2\\%$ of volume</div>
        <div class="pq-exp">Despite occupying less than a sixth of Earth's total volume ($V_{\\text{core}} / V_{\\text{Earth}} \\approx 0.162$), the core's high density ($9.9 - 13.1\\text{ g/cm}^3$) accounts for nearly one-third of the planet's total mass ($M_{\\text{core}} = 1.94 \\times 10^{24}\\text{ kg} \\approx 32.5\\%$ of $M_E$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Density Deficit of the Outer Core</div>
        <div class="pq-ans">Outer core is $8-10\\%$ less dense than pure liquid iron at core P-T</div>
        <div class="pq-exp">Shock-wave compression experiments on pure iron at $136-330\\text{ GPa}$ show that liquid iron is denser than the seismically observed core. This "density deficit" requires the presence of $\\approx 8-10\\text{ wt}\\%$ light elements (likely S, O, Si, C, and H).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Moment of Inertia Factor Proof of Dense Core</div>
        <div class="pq-ans">$I / (M R^2) = 0.3307 < 0.4$ proves mass is concentrated toward center</div>
        <div class="pq-exp">A homogeneous sphere has a moment of inertia factor of $0.400$. The Earth's observed value of $0.3307$ (determined from satellite orbital precession) proves mathematically that mass density must increase drastically toward the center.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Hydrostatic Pressure at the Center of the Earth</div>
        <div class="pq-ans">Center pressure $P_c \\approx 364\\text{ GPa}$ ($3.64\\text{ million atmospheres}$)</div>
        <div class="pq-exp">Integrating $dP = -\\rho(r) g(r) dr$ from surface to center yields $P_{\\text{CMB}} \\approx 136\\text{ GPa}$ at the core-mantle boundary, $P_{\\text{ICB}} \\approx 330\\text{ GPa}$ at the inner core boundary, and $P_c \\approx 364\\text{ GPa}$ at Earth's center.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Gravitational Acceleration Profile in the Mantle vs Core</div>
        <div class="pq-ans">$g(r)$ remains nearly constant at $\\approx 10\\text{ m/s}^2$ through mantle, peaks at CMB ($\approx 10.7\\text{ m/s}^2$)</div>
        <div class="pq-exp">Because core density is so high, the enclosed mass drops rapidly inside the core, causing gravity to decrease linearly from $10.7\\text{ m/s}^2$ at the CMB to exactly $0\\text{ m/s}^2$ at Earth's center ($r = 0$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: The Geodynamo in the Liquid Outer Core</div>
        <div class="pq-ans">Thermal and compositional convection of liquid Fe-Ni drives planetary magnetic field</div>
        <div class="pq-exp">Crystallization of the inner core expels buoyant light elements into the liquid outer core. This compositional buoyancy, combined with Coriolis forces from planetary rotation, powers vigorous helical convection that generates the geomagnetic field (geodynamo).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: S-Wave Shadow Zone Angle</div>
        <div class="pq-ans">Direct S-waves are absent beyond $103^\\circ$ ($103^\\circ - 180^\\circ$)</div>
        <div class="pq-exp">Because shear waves cannot propagate through the liquid outer core ($V_s = 0$), stations located at angular distances greater than $103^\\circ$ from an earthquake epicenter record no direct $S$ arrivals, producing an $S$-wave shadow zone from $103^\\circ$ to $180^\\circ$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Birch's Law Relating Velocity and Density</div>
        <div class="pq-ans">Linear relation: $V_p = a + b \\rho$ for rocks of constant mean atomic weight $\\bar{M}$</div>
        <div class="pq-exp">Francis Birch (1961) demonstrated experimentally that compressional wave velocity is linearly related to density for materials of similar mean atomic weight ($\\bar{M} \\approx 21$ for silicates; $\\bar{M} \\approx 48$ for iron-rich core material), providing the basis for deciphering deep Earth composition.</div>
      </div>
    </div>
  </div>
"""

# Generate all pages
generate_page(
    q_num=31,
    filename="Q031_Laurasia_and_Gondwanaland_Pangea_Drift_Complete_Guide.html",
    title="Q031: Continental Drift: Laurasia & Gondwanaland Supercontinents",
    badge="OPSC 2019 · Paper-II · Q031 · Geotectonics",
    h1_title="The Two Supercontinental Blocks Separated Due to Drifting",
    meta_text="Question ID: GEO-2019-Q031 | Topic: Continental Drift & Paleogeography | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q31_part1,
    part2_html=q31_part2,
    part3_html=q31_part3
)

generate_page(
    q_num=32,
    filename="Q032_Convection_Energy_Divergent_Boundaries_Oceans_Complete_Guide.html",
    title="Q032: Earth's Thermal Engine: Convective Venting along Mid-Ocean Ridges",
    badge="OPSC 2019 · Paper-II · Q032 · Geophysics & Plate Tectonics",
    h1_title="Convection Energy Release along Divergent Oceanic Boundaries",
    meta_text="Question ID: GEO-2019-Q032 | Topic: Mantle Convection & Thermal Regimes | Difficulty: Moderate | Target Time: 40 sec",
    part1_html=q32_part1,
    part2_html=q32_part2,
    part3_html=q32_part3
)

generate_page(
    q_num=33,
    filename="Q033_Mohorovicic_Discontinuity_Crust_Mantle_Complete_Guide.html",
    title="Q033: Planetary Discontinuities: The Mohorovicic Boundary",
    badge="OPSC 2019 · Paper-II · Q033 · Solid Earth Geophysics",
    h1_title="Mohorovicic Discontinuity: Crust-Mantle Boundary",
    meta_text="Question ID: GEO-2019-Q033 | Topic: Earth's Internal Structure & Seismic Boundaries | Difficulty: Easy | Target Time: 25 sec",
    part1_html=q33_part1,
    part2_html=q33_part2,
    part3_html=q33_part3
)

generate_page(
    q_num=34,
    filename="Q034_Asthenosphere_Upper_Mantle_Layer_Complete_Guide.html",
    title="Q034: Rheological Stratification: The Asthenosphere in the Upper Mantle",
    badge="OPSC 2019 · Paper-II · Q034 · Geodynamics & Rheology",
    h1_title="The Asthenospheric Layer: Position within the Upper Mantle",
    meta_text="Question ID: GEO-2019-Q034 | Topic: Lithosphere-Asthenosphere System | Difficulty: Moderate | Target Time: 35 sec",
    part1_html=q34_part1,
    part2_html=q34_part2,
    part3_html=q34_part3
)

generate_page(
    q_num=35,
    filename="Q035_Earth_Core_Density_10_7_gm_cm3_Complete_Guide.html",
    title="Q035: Planetary Density Distribution: Earth's Core Density",
    badge="OPSC 2019 · Paper-II · Q035 · Geophysics & Planetary Interior",
    h1_title="Average Density of 10.7 g/cm³ at Earth's Core",
    meta_text="Question ID: GEO-2019-Q035 | Topic: PREM Density Model & Core Physics | Difficulty: Moderate | Target Time: 35 sec",
    part1_html=q35_part1,
    part2_html=q35_part2,
    part3_html=q35_part3
)

print("Batch 3 Part B (Q031 - Q035) completed successfully!")
