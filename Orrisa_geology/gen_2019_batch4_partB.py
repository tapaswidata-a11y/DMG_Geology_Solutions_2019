#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 41 to 45
Assam DGMS 2019 Masterclass Standard
"""

from masterclass_generator_core import generate_page

# ==========================================
# QUESTION 41: AVERAGE DEPTH OF THE OCEAN (3,729 METERS)
# ==========================================
q41_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Planetary Hypsometry: Bimodal Crustal Elevation & Mean Ocean Depth</div>
    <div class="card-body">
      <p>The first-order topography of the Earth is characterized by a fundamental <strong>bimodal distribution of surface elevations</strong>, vividly displayed on the global <strong>Hypsographic (Hypsometric) Curve</strong>. Unlike planets lacking plate tectonics and liquid water (such as the Moon or Venus, which exhibit unimodal Gaussian topographic distributions), Earth features two distinct dominant elevation levels reflecting its two distinct crustal regimes:</p>
      
      <ul>
        <li><strong>Continental Platform Peak:</strong> Centered at an average elevation of approximately <strong>$+840\\text{ meters}$</strong> above sea level, sustained by thick, low-density granitic-felsic continental crust ($\\approx 35-40\\text{ km}$ thick, density $\\rho_c \\approx 2.7\\text{ g/cm}^3$).</li>
        <li><strong>Oceanic Abyssal Floor Peak:</strong> Centered at an average depth of approximately <strong>$-3,729\\text{ meters}$</strong> (widely cited in classical oceanography and physical geology texts as $3,729\\text{ m}$, or approximately $3,700-3,800\\text{ m}$), governed by thin, dense basaltic oceanic crust ($\\approx 7\\text{ km}$ thick, density $\\rho_o \\approx 2.9-3.0\\text{ g/cm}^3$).</li>
      </ul>

      <p>The ocean basins cover approximately $361 \\times 10^6\\text{ km}^2$, representing <strong>$70.8\\%$ of the Earth's total surface area</strong> ($510 \\times 10^6\\text{ km}^2$). The total volume of seawater contained within global oceans is estimated at approximately $1.332 \\times 10^9\\text{ km}^3$. Dividing this total oceanic volume by total oceanic surface area yields the mean depth of the global ocean:</p>

      <div class="formula-card">
        <div class="formula-title">Global Ocean Hypsometric Formulation</div>
        $$\\bar{d}_{\\text{ocean}} = \\frac{V_{\\text{ocean}}}{A_{\\text{ocean}}} = \\frac{1.332 \\times 10^9\\text{ km}^3}{3.61 \\times 10^8\\text{ km}^2} \\approx \\mathbf{3,690 - 3,729\\text{ meters}}$$
        $$\\text{Standard Examination Benchmark: } \\quad \\mathbf{3,729\\text{ meters}} \\quad (\\text{Classical oceanographic datum})$$
        $$\\text{Maximum Oceanic Depth: } \\quad \\text{Challenger Deep (Mariana Trench)} \\approx 10,994 \\pm 40\\text{ meters}$$
        $$\\text{Mean Continental Elevation: } \\quad +840\\text{ meters} \\quad \\big| \\quad \\text{Maximum Continental Elevation: } \\text{Mt. Everest} = +8,848.86\\text{ meters}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">The depth of $3,729\\text{ m}$ represents the exact standard figure derived from early precision soundings by the Challenger Expedition and classical physical geography textbooks.</p>
      </div>

      <div class="quote-box bangar">
        "The oceans cover about 71 percent of the earth's surface. The floor of the ocean lies at an average depth of about <strong>3,729 meters (or about 3.8 kilometers)</strong> below sea level, in contrast to the continents which have an average elevation of about 840 meters above sea level. The deepest part of the ocean is the Mariana Trench in the western Pacific with a depth of about 11,000 meters."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (The Oceans: Physical Dimensions, p. 35) & Sverdrup et al., <em>The Oceans</em> (1942)</span>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q041/bangar_p35_ocean_depth_zones_shelf_abyssal.png" alt="K.M. Bangar Ocean Floor Depth Zones Shelf Slope Abyssal">
        <div class="tb-caption">
          <strong>Figure 41.1: Ocean Basin Depth Zones & Hypsometric Distribution (K.M. Bangar, p. 35).</strong> Hypsographic curve of the Earth illustrating the bimodal distribution of elevations: continental platform ($+840\text{ m}$) and oceanic abyssal realm (averaging $3,729\text{ m}$).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Physiographic Partitioning of the Global Ocean Floor</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Morpho-Bathymetric Province</th>
            <th>% of Total Ocean Floor</th>
            <th>Depth Range (m)</th>
            <th>Average Depth (m)</th>
            <th>Dominant Substrate / Geology</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Continental Shelf</strong></td>
            <td>$7.5\\%$</td>
            <td>$0 - 130\\text{ m}$</td>
            <td>$60\\text{ m}$</td>
            <td>Terrigenous sands, silts, carbonate reefs</td>
          </tr>
          <tr>
            <td><strong>Continental Slope</strong></td>
            <td>$8.5\\%$</td>
            <td>$130 - 3,000\\text{ m}$</td>
            <td>$1,500\\text{ m}$</td>
            <td>Hemipelagic muds, submarine canyon channels</td>
          </tr>
          <tr>
            <td><strong>Continental Rise</strong></td>
            <td>$5.0\\%$</td>
            <td>$3,000 - 4,000\\text{ m}$</td>
            <td>$3,500\\text{ m}$</td>
            <td>Coalescing deep-sea turbidite fan aprons</td>
          </tr>
          <tr>
            <td><strong>Abyssal Plains & Hills</strong></td>
            <td><strong>$50.0\\%$</strong></td>
            <td><strong>$3,000 - 6,000\\text{ m}$</strong></td>
            <td><strong>$4,000\\text{ m}$</strong></td>
            <td><strong>Pelagic red clays, siliceous & calcareous oozes</strong></td>
          </tr>
          <tr>
            <td><strong>Mid-Ocean Ridges</strong></td>
            <td>$28.0\\%$</td>
            <td>$2,000 - 3,000\\text{ m}$</td>
            <td>$2,500\\text{ m}$</td>
            <td>Fresh MORB basalt pillow lavas and sheeted dykes</td>
          </tr>
          <tr>
            <td><strong>Deep-Sea Trenches</strong></td>
            <td>$1.0\\%$</td>
            <td>$6,000 - 11,000\\text{ m}$</td>
            <td>$8,000\\text{ m}$</td>
            <td>Trench fill turbidites, pelagic clays, ophiolitic melange</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q41_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q041</div>
    <div class="q-stmt">The average depth of the ocean is:</div>
    <div class="raw-options">
      <div class="raw-opt">(A) 5,200 meters</div>
      <div class="raw-opt">(B) 4,630 meters</div>
      <div class="raw-opt correct">(C) 3,729 meters</div>
      <div class="raw-opt">(D) 3,062 meters</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (C) 3,729 meters</div>
      <div class="sub">Verified against Bangar (p. 35), Sverdrup et al. (The Oceans), and standard physical geography curricula. The precise classical benchmark for the average depth of the global ocean is 3,729 meters (in contrast to the mean continental elevation of 840 meters).</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) 5,200 meters</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> A depth of $5,200\text{ m}$ corresponds to the deepest sectors of abyssal plains and deep ocean basins (e.g., the Argentine Basin or Philippine Basin), not the global oceanic average. Elevating the mean to $5,200\text{ m}$ overlooks the elevated mid-ocean ridge systems ($2,500\text{ m}$) and broad continental shelves ($0-200\text{ m}$).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) 4,630 meters</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> $4,630\text{ m}$ is an arbitrary distractor value well below the global average depth.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) 3,729 meters</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The precise value of <strong>3,729 meters</strong> (or $\approx 3.73\text{ km} / 12,234\text{ feet}$) is the classic, definitive geodetic and oceanographic benchmark for the mean depth of the world's oceans. Calculated by dividing total ocean water volume ($1.332 \times 10^9\text{ km}^3$) by total oceanic surface area ($361 \times 10^6\text{ km}^2$), it forms the foundation of all global hypsometric and isostatic calculations in geosciences.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) 3,062 meters</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> $3,062\text{ m}$ significantly underestimates ocean depth; it is close to the average crest depth of mid-ocean ridges rather than the abyssal ocean floor.
    </div>
  </div>
"""

q41_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Global Physical Dimensions of the Earth's Principal Oceans</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Ocean Basin</th>
            <th>Surface Area ($10^6 km^2$)</th>
            <th>Volume ($10^6 km^3$)</th>
            <th>Average Depth (m)</th>
            <th>Deepest Point (m)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Pacific Ocean</strong></td>
            <td>$168.7$ ($46.6\\%$)</td>
            <td>$669.9$ ($50.1\\%$)</td>
            <td><strong>$3,970\\text{ m}$ (Deepest average)</strong></td>
            <td>Challenger Deep ($10,994\\text{ m}$)</td>
          </tr>
          <tr>
            <td><strong>Atlantic Ocean</strong></td>
            <td>$85.1$ ($23.5\\%$)</td>
            <td>$310.4$ ($23.3\\%$)</td>
            <td><strong>$3,646\\text{ m}$</strong></td>
            <td>Puerto Rico Trench ($8,376\\text{ m}$)</td>
          </tr>
          <tr>
            <td><strong>Indian Ocean</strong></td>
            <td>$70.6$ ($19.5\\%$)</td>
            <td>$264.4$ ($19.8\\%$)</td>
            <td><strong>$3,741\\text{ m}$</strong></td>
            <td>Java / Sunda Trench ($7,450\\text{ m}$)</td>
          </tr>
          <tr>
            <td><strong>Arctic Ocean</strong></td>
            <td>$15.6$ ($4.3\\%$)</td>
            <td>$18.8$ ($1.4\\%$)</td>
            <td><strong>$1,205\\text{ m}$ (Shallowest)</strong></td>
            <td>Molloy Deep ($5,550\\text{ m}$)</td>
          </tr>
          <tr>
            <td><strong>All Oceans Combined</strong></td>
            <td><strong>$361.9\\text{ M km}^2$</strong></td>
            <td><strong>$1,332.4\\text{ M km}^3$</strong></td>
            <td><strong>$3,729\\text{ meters}$</strong></td>
            <td><strong>Challenger Deep ($10,994\\text{ m}$)</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Ocean Dimensions & Hypsometry</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Hydrostatic Pressure at Average Ocean Depth</div>
        <div class="pq-ans">Hydrostatic Pressure $P = 37.64\\text{ MPa}$ ($371.5\\text{ atmospheres}$)</div>
        <div class="pq-exp">Calculate the hydrostatic pressure at the average ocean depth $d = 3,729\\text{ m}$, assuming mean seawater density $\\rho_w = 1030\\text{ kg/m}^3$ and $g = 9.81\\text{ m/s}^2$.<br>
        $$P = \\rho_w g d = 1030 \\cdot 9.81 \\cdot 3729 = 3.768 \\times 10^7\\text{ Pa} = 37.68\\text{ MPa} \\approx 372\\text{ atm}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Ratio of Ocean Volume to Continental Crust Volume Above Sea Level</div>
        <div class="pq-ans">Ocean water volume is $\\approx 10.7$ times greater than subaerial continental volume</div>
        <div class="pq-exp">Continental area is $149 \\times 10^6\\text{ km}^2$ with mean height $+840\\text{ m}$, giving a subaerial rock volume of $V_{\\text{cont}} = 149 \\times 0.84 = 125.16 \\times 10^6\\text{ km}^3$. The ocean water volume ($1,332 \\times 10^6\\text{ km}^3$) is $1332 / 125.16 \\approx 10.64$ times larger. If the Earth were leveled flat, water would cover the entire globe to a depth of $\\approx 2,600\\text{ m}$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Sonic Depth Finding (Echo Sounding) Calculation</div>
        <div class="pq-ans">Depth $d = 3,750\\text{ meters}$</div>
        <div class="pq-exp">An echo sounder emits an acoustic pulse that reflects off the abyssal plain and returns in two-way travel time $t = 5.0\\text{ seconds}$. Assuming average sound velocity in seawater $v_s = 1500\\text{ m/s}$, calculate ocean depth.<br>
        $$d = \\frac{v_s \\cdot t}{2} = \\frac{1500 \\cdot 5.0}{2} = 3,750\\text{ meters}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Calcite Compensation Depth (CCD) in Relation to Ocean Depth</div>
        <div class="pq-ans">CCD occurs at $4,000 - 4,500\\text{ m}$ depth</div>
        <div class="pq-exp">Because the average ocean depth ($3,729\\text{ m}$) is shallower than the global CCD ($4,000-4,500\\text{ m}$), vast mid-ocean ridge flanks are draped in calcareous foraminifera oozes, whereas deeper abyssal plains ($>4,500\\text{ m}$) dissolve calcite and deposit pelagic red clays.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Sea Level Drop during Last Glacial Maximum (LGM)</div>
        <div class="pq-ans">Eustatic sea level dropped by $\\approx 120-130\\text{ meters}$</div>
        <div class="pq-exp">During the LGM ($21,000\\text{ yr BP}$), continental ice sheets locked up $50 \\times 10^6\\text{ km}^3$ of water, exposing the entire continental shelf ($0-120\\text{ m}$) to subaerial erosion and river incision.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Origin of Bimodal Hypsometry</div>
        <div class="pq-ans">Differentiation of Earth into felsic continents and mafic ocean floors</div>
        <div class="pq-exp">The bimodal hypsographic curve is unique to Earth because plate tectonics continuously generates low-density, buoyant felsic crust through hydrous subduction magmatism, while generating dense, thin mafic crust at mid-ocean ridges.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Challenger Deep Discovery</div>
        <div class="pq-ans">HMS Challenger (1875) recorded 8,184 m; HMS Challenger II (1951) recorded 10,863 m</div>
        <div class="pq-exp">The deepest point on Earth was discovered during the 1872-1876 Challenger Expedition using weighted hemp soundings, and precisely surveyed by echo sounding in 1951.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Thermocline Depth in the Open Ocean</div>
        <div class="pq-ans">Permanent thermocline spans $200\\text{ m}$ to $1,000\\text{ m}$ depth</div>
        <div class="pq-exp">Below the warm mixed surface layer ($0-200\\text{ m}$), ocean temperature plunges through the permanent thermocline from $20^\\circ\\text{C}$ down to $4^\\circ\\text{C}$. Deep abyssal ocean water ($>1,000\\text{ m}$ to the bottom at $3,729\\text{ m}$) remains near-freezing at $1-3^\\circ\\text{C}$.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 42: PALAEOMAGNETIC DATA & POLE REVERSALS
# ==========================================
q42_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Paleomagnetism & Geotectonics: Geomagnetic Polarity Reversals & Seafloor Striping</div>
    <div class="card-body">
      <p><strong>Paleomagnetism</strong> is the study of the Earth's ancient magnetic field preserved in ferromagnetic minerals (chiefly titanomagnetite and hematite) within igneous, sedimentary, and metamorphic rocks. When basaltic lava cools below the <strong>Curie temperature of magnetite ($T_C \\approx 580^\\circ\\text{C}$)</strong>, its magnetic domains lock in the exact direction and intensity of the ambient geomagnetic field at that instant, acquiring <strong>Thermo-Remanent Magnetization (TRM)</strong>.</p>
      
      <ul>
        <li><strong>Discovery of Geomagnetic Field Reversals:</strong> In 1906, French physicist <strong>Bernard Brunhes</strong> discovered volcanic rocks whose magnetization pointed opposite to the present-day magnetic field. In 1929, Japanese geophysicist <strong>Motonori Matuyama</strong> confirmed that the Earth's magnetic dipole has spontaneously flipped its polarity countless times throughout geological history:
          <ul>
            <li><strong>Normal Polarity:</strong> Magnetic field vectors point north (as in the present day).</li>
            <li><strong>Reversed Polarity:</strong> Magnetic field vectors point south (a compass needle would point to the South Pole).</li>
          </ul>
        </li>
        <li><strong>Geomagnetic Polarity Timescale (GPTS):</strong> By radiometric K-Ar dating of terrestrial basalt lava flows, geophysicists established the standard polarity epochs (chrons):
          <ol>
            <li><strong>Brunhes Normal Chron:</strong> $0 - 0.78\\text{ Ma}$ (Present day).</li>
            <li><strong>Matuyama Reversed Chron:</strong> $0.78 - 2.58\\text{ Ma}$ (Includes the Jaramillo and Olduvai normal subchrons).</li>
            <li><strong>Gauss Normal Chron:</strong> $2.58 - 3.58\\text{ Ma}$.</li>
            <li><strong>Gilbert Reversed Chron:</strong> $3.58 - 5.33\\text{ Ma}$.</li>
          </ol>
        </li>
        <li><strong>The Vine-Matthews-Morley Hypothesis (1963):</strong> Fred Vine, Drummond Matthews, and Lawrence Morley combined geomagnetic pole reversals with Harry Hess's seafloor spreading concept. As new oceanic crust forms at mid-ocean ridges, it cools and records the prevailing magnetic polarity. Periodic pole reversals create <strong>symmetrical alternating positive and negative magnetic anomaly stripes</strong> parallel to ridge crests, providing undeniable, quantitative empirical proof of seafloor spreading and plate tectonics.</li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Palaeomagnetism</strong> is the study of the fossil magnetism retained by rocks. Rocks containing magnetic minerals record the direction of the earth's magnetic field at the time of their formation. Studies of magnetized basalt lavas revealed that the earth's magnetic field has reversed its polarity repeatedly in the past. Thus, <strong>palaeomagnetic data is primarily useful for understanding magnetic pole reversals and continental drift</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of Earth & Plate Tectonics, p. 28) & Van der Pluijm & Marshak, p. 445</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Paleomagnetic Dipole Formula & Seafloor Spreading Rate</div>
        $$\\tan I = 2 \\tan \\lambda \\quad (\\text{Geocentric Axial Dipole Equation: Magnetic Inclination } I \\text{ vs. Paleolatitude } \\lambda)$$
        $$v_{\\text{spreading}} = \\frac{\\Delta x}{\\Delta t} \\quad (\\text{Distance to magnetic stripe } \\Delta x \\text{ divided by reversal age } \\Delta t)$$
        $$B_{\\text{total}} = B_{\\text{core}} + B_{\\text{crustal anomaly}} \\implies \\Delta B = \\pm 200 - 1000\\text{ nT}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Positive anomalies occur where remnant crustal magnetization reinforces the present normal field; negative anomalies occur where reversed remnant magnetization cancels part of the present field.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q042/vdp_p445_paleomagnetic_pole_reversals_stripes.png" alt="Van der Pluijm & Marshak Paleomagnetic Reversals and Seafloor Magnetic Stripes">
        <div class="tb-caption">
          <strong>Figure 42.1: Geomagnetic Field Reversals & Seafloor Magnetic Anomalies (Van der Pluijm & Marshak, p. 445).</strong> Symmetrical marine magnetic stripes across mid-ocean ridges recording historical geomagnetic pole reversals (Brunhes, Matuyama, Gauss, Gilbert).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Applications of Paleomagnetic Data in the Earth Sciences</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Paleomagnetic Investigation</th>
            <th>Primary Geophysical Signal</th>
            <th>Major Scientific Breakthrough</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Geomagnetic Polarity Reversals</strong></td>
            <td><strong>$180^\\circ$ flip in declination and inclination signs</strong></td>
            <td><strong>Establishment of GPTS; proof of Vine-Matthews-Morley seafloor spreading</strong></td>
          </tr>
          <tr>
            <td><strong>Apparent Polar Wander Paths (APWP)</strong></td>
            <td>Systematic shift of paleomagnetic pole positions over time</td>
            <td>Quantitative proof of continental drift and supercontinent assemblies</td>
          </tr>
          <tr>
            <td><strong>Paleolatitude Determination</strong></td>
            <td>Magnetic inclination ($\\tan I = 2 \\tan \\lambda$)</td>
            <td>Tracking the rapid northward flight of India during the Cretaceous</td>
          </tr>
          <tr>
            <td><strong>Magnetostratigraphy</strong></td>
            <td>Correlation of normal/reversed chrons across sedimentary sections</td>
            <td>High-resolution global chronostratigraphic correlation across continents</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q42_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q042</div>
    <div class="q-stmt">Palaeomagnetic data is useful for understanding :</div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Pole reversals</div>
      <div class="raw-opt">(B) Composition of mantle</div>
      <div class="raw-opt">(C) Internal structure of the earth</div>
      <div class="raw-opt">(D) Origin of life on earth</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (A) Pole reversals</div>
      <div class="sub">Verified against Bangar (p. 28), Van der Pluijm & Marshak (Earth Structure, p. 445), and Fowler (The Solid Earth, p. 43). Paleomagnetic records locked in cooled volcanic rocks and marine sediments provide direct, definitive empirical evidence of Earth's geomagnetic pole reversals and seafloor spreading.</div>
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) Pole reversals</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The most revolutionary discovery produced by paleomagnetic data was the realization that Earth's magnetic field periodically undergoes complete <strong>geomagnetic polarity reversals (pole reversals)</strong>, switching between normal and reversed polarity states. When mapped over the oceanic floor, these reversals produce symmetrical zebra-like magnetic anomaly stripes that proved Harry Hess's seafloor spreading theory and formed the bedrock of modern Plate Tectonics.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Composition of mantle</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The composition of the mantle is determined through mantle xenolith petrology (peridotites in kimberlites and alkali basalts), ophiolite field complexes, high-pressure diamond anvil cell experiments, and cosmochemical meteorite comparisons (CI chondrites), not through paleomagnetism. Because the mantle is above the Curie point throughout most of its depth, it cannot retain permanent remanent paleomagnetism.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Internal structure of the earth</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The internal concentric shell structure of the Earth (crust, mantle, outer core, inner core) was resolved through <strong>observational earthquake seismology</strong> (body wave travel-time curves, shadow zones, and seismic tomography), not paleomagnetism.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Origin of life on earth</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The origin of life on Earth is investigated via organic geochemistry (carbon isotopic fractionation $\delta^{13}\text{C}$), paleobiology (Archean stromatolites and microfossils), prebiotic chemical synthesis experiments, and hydrothermal vent biochemistry, bearing zero connection to paleomagnetic measurements.
    </div>
  </div>
"""

q42_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: The Geocentric Axial Dipole (GAD) Field & Remanent Magnetization Types</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Remanent Magnetization Mode</th>
            <th>Acquisition Mechanism</th>
            <th>Host Lithology</th>
            <th>Geological Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Thermo-Remanent Magnetization (TRM)</strong></td>
            <td>Cooling below Curie temperature ($T_C = 580^\\circ\\text{C}$)</td>
            <td><strong>Basaltic lavas, gabbros, dolerite dykes</strong></td>
            <td><strong>Seafloor spreading stripes, pole reversal timescale</strong></td>
          </tr>
          <tr>
            <td><strong>Chemical Remanent Magnetization (CRM)</strong></td>
            <td>Precipitation / oxidation of magnetic grains through critical volume</td>
            <td>Sedimentary red beds, diagenetic hematite</td>
            <td>Dating diagenetic events, secondary overprints</td>
          </tr>
          <tr>
            <td><strong>Depositional Remanent Magnetization (DRM)</strong></td>
            <td>Mechanical alignment of settling magnetic particles in water column</td>
            <td>Deep-sea marine clays, lake varves</td>
            <td>High-resolution magnetostratigraphy</td>
          </tr>
          <tr>
            <td><strong>Viscous Remanent Magnetization (VRM)</strong></td>
            <td>Long-term exposure to ambient field at low temperature</td>
            <td>Any rock over geologic time</td>
            <td>Unwanted secondary noise removed by demagnetization</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Paleomagnetism & Geotectonics</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Paleolatitude from Magnetic Inclination</div>
        <div class="pq-ans">Paleolatitude $\\lambda = 30.0^\\circ\\text{N}$</div>
        <div class="pq-exp">A Cretaceous basalt flow in peninsular India has a measured magnetic inclination of $I = 49.1^\\circ$. Calculate the paleolatitude $\\lambda$ of India when this basalt solidified.<br>
        $$\\tan I = 2 \\tan \\lambda \\implies \\tan \\lambda = \\frac{\\tan(49.1^\\circ)}{2} = \\frac{1.1544}{2} = 0.5772$$
        $$\\lambda = \\arctan(0.5772) = 30.0^\\circ$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Seafloor Spreading Rate Calculation</div>
        <div class="pq-ans">Half spreading rate $v = 2.5\\text{ cm/year}$; full opening rate $= 5.0\\text{ cm/year}$</div>
        <div class="pq-exp">The Brunhes-Matuyama magnetic reversal boundary ($0.78\\text{ Ma}$) is identified at a distance of $\\Delta x = 19.5\\text{ km}$ from the crest of the Mid-Atlantic Ridge. Calculate the half spreading rate.<br>
        $$v = \\frac{\\Delta x}{\\Delta t} = \\frac{19.5\\text{ km}}{0.78\\text{ Ma}} = \\frac{19.5 \\times 10^5\\text{ cm}}{7.8 \\times 10^5\\text{ yr}} = 2.5\\text{ cm/year}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: The Cretaceous Long Normal Quiet Zone</div>
        <div class="pq-ans">37 million years without a single magnetic reversal ($121 - 84\\text{ Ma}$)</div>
        <div class="pq-exp">During the Cretaceous Long Normal Superchron (Chron C34n), Earth's magnetic field remained continuously in normal polarity without flipping for 37 million years, creating broad smooth oceanic zones devoid of magnetic stripe anomalies.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Curie Temperature of Common Magnetic Minerals</div>
        <div class="pq-ans">Magnetite ($580^\\circ\\text{C}$), Hematite ($675^\\circ\\text{C}$), Pyrrhotite ($320^\\circ\\text{C}$)</div>
        <div class="pq-exp">Above the Curie temperature, thermal kinetic vibrations overcome quantum exchange coupling, converting ferromagnetic minerals into paramagnetic materials incapable of retaining remanent magnetization.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Apparent Polar Wander Path (APWP) Intersection</div>
        <div class="pq-ans">Convergence of APWPs proves the assembly of supercontinents</div>
        <div class="pq-exp">When APWP curves from two distinct continents coincide, it demonstrates mathematically that the two landmasses were joined and drifted as a single unified tectonic plate (e.g., Laurasia during the Permian).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Magnetic Inclination at Equator vs. Magnetic Poles</div>
        <div class="pq-ans">Inclination $I = 0^\\circ$ at magnetic equator; $I = \\pm 90^\\circ$ at magnetic poles</div>
        <div class="pq-exp">Under the GAD equation ($\\tan I = 2 \\tan \\lambda$): at the equator ($\\lambda = 0$), $I = 0^\\circ$ (horizontal field lines); at the poles ($\\lambda = 90^\\circ$), $I = 90^\\circ$ (vertical field lines).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Duration of a Geomagnetic Reversal Event</div>
        <div class="pq-ans">Field flip transition takes approximately $2,000 - 7,000\\text{ years}$</div>
        <div class="pq-exp">High-resolution sedimentary core records demonstrate that while polarity chrons last hundreds of thousands of years, the actual polarity reversal transition occurs very rapidly over $2,000$ to $7,000$ years, accompanied by a $90\\%$ collapse in dipole field strength.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Thermal Demagnetization Procedure</div>
        <div class="pq-ans">Stepwise heating in zero-field oven to isolate primary Characteristic Remanent Magnetization (ChRM)</div>
        <div class="pq-exp">Paleomagnetic laboratories heat rock specimens incrementally (e.g., $100^\\circ, 200^\\circ, \\dots, 580^\\circ\\text{C}$) inside mu-metal magnetic shields to unblock low-coercivity secondary viscous overprints and isolate the pristine primary ChRM vector.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 43: GUYOT (FLAT TOPPED SEAMOUNT)
# ==========================================
q43_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Marine Geomorphology: Seamounts, Guyots & Thermal Subsidence</div>
    <div class="card-body">
      <p>The deep ocean basin floor is populated by thousands of isolated underwater volcanic edifices rising from the abyssal plains. While active or recently extinct submarine volcanoes retain their conical, pointed summit peaks (termed <strong>Seamounts</strong>), vast numbers of ancient underwater volcanic mountains possess remarkably <strong>flat, horizontal summit plateaus</strong>. These flat-topped submarine mountains are termed <strong>Guyots</strong> (or <strong>Tablemounts</strong>).</p>
      
      <ul>
        <li><strong>Discovery & Naming:</strong> During World War II, Princeton geologist and naval commander <strong>Harry H. Hess</strong> utilized newly invented echo sounders on the transport ship <em>USS Cape Johnson</em> to survey the Pacific basin. He discovered hundreds of truncated, flat-topped volcanic peaks lying submerged at depths of $1,000 - 2,000\\text{ meters}$ below sea level. Hess named them <strong>Guyots</strong> in honor of Arnold Henry Guyot, the 19th-century Swiss-American geographer and founding geology professor at Princeton University.</li>
        <li><strong>Evolutionary Genesis of a Guyot:</strong> The formation of a guyot follows a rigorous four-stage geodynamic cycle:
          <ol>
            <li><strong>Subaerial Volcanic Island Stage:</strong> Hotspot or mid-ocean ridge volcanism builds a massive basaltic volcano that rises above sea level to form a volcanic island (analogous to Hawaii or Tahiti).</li>
            <li><strong>Wave Planation at Sea Level:</strong> Once volcanic activity ceases, relentless ocean wave attack and surf abrasion bevel and plane the volcanic summit completely flat at the sea level interface, creating a truncated wave-cut platform. Shallow-water fringing coral reefs and rounded basalt beach pebbles accumulate on this platform.</li>
            <li><strong>Thermal Contraction & Subsidence:</strong> As plate motion carries the extinct volcano away from the warm, buoyant spreading ridge or mantle plume, the underlying oceanic lithosphere conductively cools, thickens, and increases in density ($d(t) \\propto \\sqrt{t}$). This causes the entire seafloor to undergo massive <strong>isostatic thermal subsidence</strong> ($1,000 - 2,500\\text{ m}$).</li>
            <li><strong>Submerged Guyot:</strong> The flat, wave-beveled summit sinks below the photic zone. Corals die (drowned reefs), and the flat platform is preserved in the cold, deep ocean abyssal realm as a permanent <strong>flat-topped seamount (guyot)</strong>.</li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Guyot:</strong> A flat-topped seamount is called a <strong>guyot</strong>. It was once a volcanic island whose top was leveled and cut flat by wave action when it was at sea level. With the cooling and subsidence of the ocean floor, the flat-topped volcanic mountain was drowned and submerged to great depths."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (The Oceans: Features of Ocean Floor, p. 36)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Thermal Subsidence Formulation of Guyots</div>
        $$d_{\\text{guyot}}(t) = d_0 + C_s \\sqrt{t} \\quad (\\text{Depth increases with square root of crustal age } t)$$
        $$\\Delta z_{\\text{subsidence}} = 350 \\sqrt{t_{\\text{Ma}}} \\text{ meters} \\quad (\\text{Typical thermal contraction of oceanic lithosphere})$$
        $$\\text{For an extinct volcano aged } t = 64\\text{ Ma:} \\quad \\Delta z = 350 \\times \\sqrt{64} = 350 \\times 8 = \\mathbf{2,800\\text{ meters}}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Drowned Cretaceous rudist bivalves and reef corals recovered from guyot tops at $1,500\text{ m}$ depth provide empirical verification that these summits were once at sea level.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q043/bangar_p36_seamounts_guyots_trenches.png" alt="K.M. Bangar Ocean Floor Features Guyots and Seamounts">
        <div class="tb-caption">
          <strong>Figure 43.1: Seamounts, Guyots & Ocean Basin Topography (K.M. Bangar, p. 36).</strong> Cross section illustrating conical seamounts and wave-beveled flat-topped guyots submerged beneath ocean water due to lithospheric thermal subsidence.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Classification: Submarine Volcanic Topography</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Submarine Feature</th>
            <th>Summit Morphology</th>
            <th>Relationship to Sea Level</th>
            <th>Primary Geomorphic Process</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Guyot (Tablemount)</strong></td>
            <td><strong>Broad, perfectly flat, horizontal plateau</strong></td>
            <td><strong>Submerged ($1,000 - 2,500\\text{ m}$ depth)</strong></td>
            <td><strong>Wave planation at sea level followed by thermal subsidence</strong></td>
          </tr>
          <tr>
            <td><strong>Seamount</strong></td>
            <td>Sharp, pointed, conical summit peak</td>
            <td>Submerged ($>1,000\\text{ m}$ relief above seafloor)</td>
            <td>Submarine volcanism without reaching surf zone</td>
          </tr>
          <tr>
            <td><strong>Abyssal Hill</strong></td>
            <td>Small, rounded or elongated dome ($<1,000\\text{ m}$)</td>
            <td>Submerged on abyssal floor ($3,000 - 5,000\\text{ m}$)</td>
            <td>Fault-block horsts and minor volcanism at spreading axes</td>
          </tr>
          <tr>
            <td><strong>Volcanic Island</strong></td>
            <td>Steep, subaerial conical peaks</td>
            <td>Subaerial (Projecting above sea level)</td>
            <td>Active hotspot / island arc volcanism</td>
          </tr>
          <tr>
            <td><strong>Atoll</strong></td>
            <td>Circular ring of coral reef enclosing a lagoon</td>
            <td>Sea level reef rim</td>
            <td>Coral growth matching rate of volcanic subsidence</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q43_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q043</div>
    <div class="q-stmt">Guyot is a :</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Ridge of a fold mountain</div>
      <div class="raw-opt">(B) Major depression in a continental area</div>
      <div class="raw-opt correct">(C) Flat topped seamount</div>
      <div class="raw-opt">(D) Flat topped hill on the surface</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (C) Flat topped seamount</div>
      <div class="sub">Verified against Bangar (p. 36), Harry Hess (1946), and Thurman & Trujillo (Essentials of Oceanography). A guyot (tablemount) is by definition a flat-topped submarine volcanic mountain (seamount) submerged beneath the sea.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Ridge of a fold mountain</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The ridge of a fold mountain is a linear subaerial or submarine tectonic crest produced by regional horizontal crustal compression (e.g., an anticlinorium crest or Appalachian hogback ridge), bearing zero relation to isolated volcanic guyots.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Major depression in a continental area</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Major continental depressions include rift valleys, grabens, or structural basins (e.g., the Dead Sea basin or Lake Baikal). A guyot is an elevated positive submarine mountain, not a depression.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Flat topped seamount</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> A <strong>guyot</strong> (tablemount) is an isolated volcanic seamount whose peak was planed perfectly flat by marine surf erosion when it stood at sea level as an island, and subsequently drowned to great depths ($1,000-2,500\text{ m}$) as the cooling oceanic lithosphere subsided isostatically. Harry Hess recognized hundreds of these flat-topped volcanic seamounts in the Pacific, providing a cornerstone proof of seafloor spreading and oceanic subsidence.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Flat topped hill on the surface</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> A flat-topped hill on the continental land surface is known as a <strong>mesa</strong> or <strong>butte</strong>, formed by subaerial fluvial and scarp-retreat erosion of horizontal sedimentary strata capped by a resistant caprock. Guyots are exclusively submarine features.
    </div>
  </div>
"""

q43_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Darwin's Coral Reef Subsidence Theory vs. Guyot Formation</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Evolutionary Stage</th>
            <th>Darwin's Coral Reef Theory (Warm Tropics)</th>
            <th>Guyot Formation (Cold / Rapid Subsidence)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Stage 1: Active Island</strong></td>
            <td>Volcanic island with fringing coral reef</td>
            <td>Subaerial volcanic island</td>
          </tr>
          <tr>
            <td><strong>Stage 2: Extinction & Erosion</strong></td>
            <td>Island erodes; reef grows upward to form <strong>Barrier Reef</strong></td>
            <td>Surf and wave action bevel summit into a flat wave-cut platform</td>
          </tr>
          <tr>
            <td><strong>Stage 3: Thermal Subsidence</strong></td>
            <td>Volcanic peak sinks entirely below sea; reef forms an <strong>Atoll</strong></td>
            <td>Subsidence rate exceeds coral growth rate (or cold water kills reef)</td>
          </tr>
          <tr>
            <td><strong>Stage 4: Deep Submergence</strong></td>
            <td>Thick carbonate cap ($>1,000\\text{ m}$) maintains atoll rim at sea level</td>
            <td><strong>Flat-topped volcanic platform drowns into deep water as a Guyot</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Marine Geology & Guyots</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Drowned Coral Reefs on Guyots</div>
        <div class="pq-ans">Dredged fossils confirm Cretaceous reef corals at $1,500\\text{ m}$ depth</div>
        <div class="pq-exp">Oceanographic dredging of Pacific guyot summits recovered shallow-water Cretaceous rudist bivalves and reef corals (*Actinastrea*). Because hermatypic corals cannot grow below $50\\text{ m}$ depth (photic zone limit), this proves guyot summits were once at sea level.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Emperor Seamount-Hawaiian Ridge Bend</div>
        <div class="pq-ans">Bend at $\\approx 47\\text{ Ma}$ represents change in Pacific Plate motion from NNW to WNW</div>
        <div class="pq-exp">The Hawaiian-Emperor chain consists of active islands (Hawaii), conical seamounts, and ancient drowned guyots (Detroit Guyot, Meiji Guyot near the Aleutians). The prominent $60^\\circ$ bend at $47\\text{ Ma}$ marks a major kinematic plate reorganization.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Minimum Relief Criterion for Seamounts</div>
        <div class="pq-ans">Seamount elevation must exceed $1,000\\text{ meters}$ above surrounding abyssal floor</div>
        <div class="pq-exp">By international hydrographic definition (IHO/IOC), an isolated submarine elevation is classified as a seamount (or guyot, if flat-topped) only if its vertical relief is $1,000\\text{ m}$ or greater. Features under $1,000\\text{ m}$ are termed abyssal hills or knolls.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Role of Harry Hess in Seafloor Spreading</div>
        <div class="pq-ans">Guyots proved that ocean crust moves laterally away from ridges while subsiding</div>
        <div class="pq-exp">Harry Hess reasoned in 1962 that if the ocean floor were static, guyots would remain at sea level. Their systematic increase in depth and age away from spreading ridges provided a fundamental pillar of his "History of Ocean Basins" paper proposing seafloor spreading.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Ferromanganese Crusts on Guyots</div>
        <div class="pq-ans">Cobalt-rich ferromanganese crusts precipitate from seawater on flat summits</div>
        <div class="pq-exp">Because strong deep-sea currents sweep guyot summits free of sediment, dissolved metals precipitate directly from seawater over millions of years, forming $5-15\\text{ cm}$ thick crusts highly enriched in cobalt, nickel, and tellurium.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Ocean Current Taylor Columns Over Guyots</div>
        <div class="pq-ans">Upwelling and closed anticyclonic circulation vortices over flat summits</div>
        <div class="pq-exp">When deep ocean currents encounter a steep guyot, Coriolis forces create a closed circulating vortex termed a *Taylor Column*, which traps nutrients, driving localized biological upwelling and rich pelagic fisheries.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Distinction Between Mesa and Guyot</div>
        <div class="pq-ans">Mesa is a subaerial sedimentary hill; Guyot is a submarine volcanic mountain</div>
        <div class="pq-exp">While both feature flat tops, a mesa forms on land by stream erosion cutting horizontal sedimentary strata, whereas a guyot is an isolated basaltic volcano planed by sea waves and drowned in the deep ocean.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Subduction of Guyots at Deep Sea Trenches</div>
        <div class="pq-ans">Causes tectonic erosion and seismic asperities in subduction zones</div>
        <div class="pq-exp">When plate motion carries a guyot into an oceanic trench (e.g., Daiichi-Kashima Guyot in the Japan Trench), the massive volcanic block acts as a giant asperic wedge that scours the overriding plate and triggers high-magnitude megathrust earthquakes.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 44: DEEP SEA TRENCHES & CIRCUM PACIFIC BELT
# ==========================================
q44_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Subduction Geodynamics: Deep-Sea Trenches & The Circum-Pacific Belt</div>
    <div class="card-body">
      <p><strong>Deep-Sea Trenches</strong> are long, narrow, arcuate topographic depressions of the ocean floor that represent the deepest regions on Earth ($6,000 - 11,000\\text{ meters}$ below sea level). Mechanically, oceanic trenches mark the surface expression of <strong>convergent plate boundaries (subduction zones)</strong>, where cold, dense oceanic lithospheric plates bend downward and plunge into the asthenospheric mantle beneath overriding plates.</p>
      
      <ul>
        <li><strong>Global Distribution:</strong> Deep-sea trenches are overwhelmingly concentrated along the <strong>Circum-Pacific Belt (the Pacific "Ring of Fire")</strong>. The Pacific Ocean basin is encircled almost entirely by subduction zones consuming oceanic lithosphere, hosting the vast majority of Earth's great trenches:
          <ul>
            <li><strong>Mariana Trench (Western Pacific):</strong> Contains the Challenger Deep, the deepest surveyed point on Earth at approximately $10,994 \\pm 40\\text{ m}$.</li>
            <li><strong>Tonga & Kermadec Trenches (Southwest Pacific):</strong> Reaching depths of $10,882\\text{ m}$ and $10,047\\text{ m}$.</li>
            <li><strong>Kuril-Kamchatka & Japan Trenches (Northwest Pacific):</strong> Reaching $10,542\\text{ m}$ and $9,000\\text{ m}$.</li>
            <li><strong>Aleutian Trench (Northern Pacific):</strong> Reaching $7,679\\text{ m}$.</li>
            <li><strong>Peru-Chile Trench (Eastern Pacific):</strong> Extending along South America for over $5,900\\text{ km}$, reaching $8,065\\text{ m}$.</li>
          </ul>
        </li>
        <li><strong>Structural Anatomy:</strong> A trench profile exhibits an asymmetric V-shaped cross section:
          <ul>
            <li><strong>Outer (Seaward) Trench Slope:</strong> Gently dipping ($2^\\circ - 5^\\circ$), characterized by extensional bending faulting (horsts and grabens) as the flexed plate bends into the trench.</li>
            <li><strong>Inner (Landward) Trench Slope:</strong> Steeper ($5^\\circ - 15^\\circ$), forming the leading edge of the overriding plate (often an accretionary wedge or subduction erosion scarp).</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Deep Ocean Trenches:</strong> Deep ocean trenches are narrow, elongate troughs that represent the deepest parts of the ocean floor, reaching depths of 8,000 to 11,000 meters. <strong>Deep sea trenches are generally associated with the Circum-Pacific Belt</strong>, where oceanic crustal plates are being subducted down into the mantle."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of Earth & Deep Sea Trenches, p. 36 & 50)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Elastic Plate Flexure & Trench Depth Formulation</div>
        $$D \\frac{d^4 w}{dx^4} + P \\frac{d^2 w}{dx^2} + (\\rho_m - \\rho_w) g w = 0 \\quad (\\text{Thin Elastic Plate Flexure Equation})$$
        $$w_0 \\approx 2 - 4\\text{ km} \\quad (\\text{Downward flexural deflection of oceanic plate into trench})$$
        $$\\text{Total Depth: } \\quad d_{\\text{trench}} = d_{\\text{abyssal}} + w_0 \\approx 5,000\\text{ m} + 3,000-6,000\\text{ m} = \\mathbf{8,000 - 11,000\\text{ meters}}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $D = E h_e^3 / [12(1-\\nu^2)]$ is the flexural rigidity of the plate, $h_e$ is elastic plate thickness ($20-40\text{ km}$), and $w(x)$ is vertical flexural deflection.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q044/global_circum_pacific_trenches_map.png" alt="Global Map of Deep Sea Trenches Circum Pacific Belt">
        <div class="tb-caption">
          <strong>Figure 44.1: Deep-Sea Trenches & Global Subduction Zones (Bangar, p. 50).</strong> Tectonic map highlighting the global concentration of deep-sea trenches around the perimeter of the Pacific Ocean basin (Circum-Pacific Belt).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Major Oceanic Trenches of the World and Their Depths</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Trench Name</th>
            <th>Tectonic Belt</th>
            <th>Maximum Depth (m)</th>
            <th>Subducting Plate</th>
            <th>Overriding Plate</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mariana Trench</strong></td>
            <td><strong>Circum-Pacific (West)</strong></td>
            <td><strong>$10,994\\text{ m}$ (Deepest)</strong></td>
            <td>Pacific Plate</td>
            <td>Mariana Microplate / Philippine Sea</td>
          </tr>
          <tr>
            <td><strong>Tonga Trench</strong></td>
            <td><strong>Circum-Pacific (SW)</strong></td>
            <td><strong>$10,882\\text{ m}$</strong></td>
            <td>Pacific Plate</td>
            <td>Indo-Australian Plate</td>
          </tr>
          <tr>
            <td><strong>Kuril-Kamchatka Trench</strong></td>
            <td><strong>Circum-Pacific (NW)</strong></td>
            <td><strong>$10,542\\text{ m}$</strong></td>
            <td>Pacific Plate</td>
            <td>Okhotsk Plate (North American)</td>
          </tr>
          <tr>
            <td><strong>Philippine Trench</strong></td>
            <td><strong>Circum-Pacific (West)</strong></td>
            <td><strong>$10,540\\text{ m}$</strong></td>
            <td>Philippine Sea Plate</td>
            <td>Sunda Plate (Eurasian)</td>
          </tr>
          <tr>
            <td><strong>Peru-Chile (Atacama) Trench</strong></td>
            <td><strong>Circum-Pacific (East)</strong></td>
            <td><strong>$8,065\\text{ m}$</strong></td>
            <td>Nazca Plate</td>
            <td>South American Plate</td>
          </tr>
          <tr>
            <td><strong>Puerto Rico Trench</strong></td>
            <td>Atlantic Ocean (Caribbean Arc)</td>
            <td>$8,376\\text{ m}$</td>
            <td>North American Plate</td>
            <td>Caribbean Plate</td>
          </tr>
          <tr>
            <td><strong>Java (Sunda) Trench</strong></td>
            <td>Indian Ocean (Indonesian Arc)</td>
            <td>$7,450\\text{ m}$</td>
            <td>Indo-Australian Plate</td>
            <td>Eurasian (Sunda) Plate</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q44_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q044</div>
    <div class="q-stmt">Deep sea trenches are generally associated with :</div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) Circum pacific belt</div>
      <div class="raw-opt">(B) Mid-oceanic ridges</div>
      <div class="raw-opt">(C) Island arcs</div>
      <div class="raw-opt">(D) Collisional areas</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (A) Circum pacific belt</div>
      <div class="sub">Verified against Bangar (p. 36 & p. 50), Fowler (The Solid Earth), and Tarbuck & Lutgens. Deep-sea trenches are fundamentally concentrated in the Circum-Pacific Belt ("Ring of Fire"), where oceanic plates are consumed along convergent subduction zones encircling the Pacific Ocean basin.</div>
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) Circum pacific belt</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Deep-sea trenches mark the sites of active oceanic subduction. Because the Pacific Ocean is an ancient, contracting ocean basin encircled almost entirely by convergent plate boundaries, over <strong>$80\\%$ of Earth's deep-sea trenches are situated within the Circum-Pacific Belt</strong> (including the Mariana, Tonga, Kermadec, Kuril-Kamchatka, Japan, Aleutian, and Peru-Chile trenches). Option (A) is the definitive geographic and geodynamic answer.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Mid-oceanic ridges</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Mid-oceanic ridges represent divergent plate boundaries where new crust is created, standing elevated at $2,000-3,000\text{ m}$ depth. While ridges feature central axial rift valleys ($1-2\text{ km}$ deep), they are the exact kinematic opposite of deep-sea subduction trenches ($8,000-11,000\text{ m}$).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Island arcs</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> While island arcs (e.g., the Aleutians, Marianas) are genetically linked to subduction, trenches also border active continental margins devoid of island arcs (e.g., the Peru-Chile Trench along South America and the Cascadia Trench along North America). The overarching geographic entity defined in global tectonic curricula that unites all these trenches is the <strong>Circum-Pacific Belt</strong>.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Collisional areas</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Continental collision zones (e.g., the Himalayas, Zagros) occur where ocean basins have completely closed, destroying pre-existing trenches and producing suture zones and high mountain ranges, rather than deep oceanic trenches.
    </div>
  </div>
"""

q44_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Geophysical Signatures Across Deep Sea Trenches</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Geophysical Parameter</th>
            <th>Outer Trench High</th>
            <th>Trench Axis</th>
            <th>Forearc Accretionary Wedge</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bathymetry</strong></td>
            <td>Subtle bulge ($+200 - 500\\text{ m}$)</td>
            <td><strong>Maximum depth ($8,000 - 11,000\\text{ m}$)</strong></td>
            <td>Sloping terrace ($2,000 - 4,000\\text{ m}$)</td>
          </tr>
          <tr>
            <td><strong>Gravity Anomaly</strong></td>
            <td>Small positive Free-Air</td>
            <td><strong>Massive negative Free-Air ($-200\\text{ to } -350\\text{ mGal}$)</strong></td>
            <td>Gradually positive</td>
          </tr>
          <tr>
            <td><strong>Heat Flow</strong></td>
            <td>Normal oceanic ($50\\text{ mW/m}^2$)</td>
            <td><strong>Extremely low ($20 - 35\\text{ mW/m}^2$)</strong></td>
            <td>Low to moderate</td>
          </tr>
          <tr>
            <td><strong>Seismic Activity</strong></td>
            <td>Shallow bending normal faults</td>
            <td>Shallow megathrust slip ($M_w 8.5 - 9.5$)</td>
            <td>Imbricate thrusting, accretionary wedge</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Trench Mechanics & Subduction Tectonics</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Origin of the Massive Negative Free-Air Anomaly</div>
        <div class="pq-ans">Dynamic slab pull holds low-density seawater deep in place against isostasy</div>
        <div class="pq-exp">Oceanic trenches exhibit the largest negative Free-Air gravity anomalies on Earth (down to $-380\\text{ mGal}$). This occurs because downward hydrodynamic suction from the sinking slab holds the trench down, maintaining a huge mass deficit of water where mantle should be.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Outer Trench Swell / Forebulge Height</div>
        <div class="pq-ans">Upward flexural arch $w_b \\approx 200 - 500\\text{ m}$ located $\\approx 100-150\\text{ km}$ seaward</div>
        <div class="pq-exp">Before the oceanic plate plunges into the trench, the elastic bending moment causes the plate to arch upward into an *outer trench swell*, inducing extensional normal faulting in the upper crust.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Accretionary Wedge vs. Non-Accretionary Trench</div>
        <div class="pq-ans">Thick trench sediment produces accretionary wedges; sediment-starved trenches produce subduction erosion</div>
        <div class="pq-exp">Where rivers dump thick sediment into trenches (e.g., Cascadia, Makran), sediment scrapes off into imbricate thrust wedges. In sediment-starved trenches (e.g., Mariana), the overriding plate undergoes tectonic erosion.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Wadati-Benioff Zone Seismicity</div>
        <div class="pq-ans">Dipping planar zone of earthquakes tracing the descending subducting slab</div>
        <div class="pq-exp">Earthquakes along the Circum-Pacific belt define planar Wadati-Benioff zones dipping from the trench down to $670\\text{ km}$ depth, mapping the subducting cold lithospheric slab inside the warmer mantle.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Extreme Hydrostatic Pressure in the Challenger Deep</div>
        <div class="pq-ans">Pressure $P = 110.8\\text{ MPa}$ ($1,093\\text{ atmospheres}$)</div>
        <div class="pq-exp">Calculate hydrostatic pressure at $d = 10,994\\text{ m}$, accounting for water compression (mean $\\rho_w = 1050\\text{ kg/m}^3, g = 9.81\\text{ m/s}^2$).<br>
        $$P = \\rho_w g d = 1050 \\cdot 9.81 \\cdot 10994 = 1.132 \\times 10^8\\text{ Pa} \\approx 113.2\\text{ MPa} \\approx 1,117\\text{ atm}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Serpentinization in the Outer Rise</div>
        <div class="pq-ans">Bending-induced normal faults channel seawater $15-20\\text{ km}$ into upper mantle</div>
        <div class="pq-exp">Extensional faults at the outer trench slope fracture the incoming oceanic plate, allowing seawater to infiltrate deep into peridotite mantle, serpentinizing it and carrying water deep into the subduction zone to trigger arc volcanism.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Trench Rollback & Back-Arc Basin Opening</div>
        <div class="pq-ans">Sinking slab falls steeper than forward motion, retreating trench seaward</div>
        <div class="pq-exp">When dense oceanic lithosphere sinks faster than convergence, the hinge of the subducting plate rolls backward (trench rollback), exerting extensional suction on the overriding plate that rips open back-arc basins (e.g., Sea of Japan, Mariana Trough).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: The 2004 Sumatra Megathrust Tsunami</div>
        <div class="pq-ans">$M_w 9.1 - 9.3$ rupture along the Sunda (Java) Trench</div>
        <div class="pq-exp">On December 26, 2004, a $1,300\\text{ km}$ long segment of the Sunda Trench ruptured with up to $20\\text{ m}$ of co-seismic slip, uplifting the ocean floor by several meters and generating the catastrophic Indian Ocean tsunami.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 45: TEMPERATURE REGIME IN UPPER LOWER CRUST (400-500°C)
# ==========================================
q45_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Crustal Geothermics: Temperature Regimes Across the Continental Crust</div>
    <div class="card-body">
      <p>The thermal regime of the continental crust is governed by the 1D conductive heat transfer equation, sustained by two primary sources: <strong>radiogenic heat production</strong> ($A_0$) from radioactive decay of $^{238}\\text{U}, ^{235}\\text{U}, ^{232}\\text{Th},$ and $^{40}\\text{K}$ concentrated within felsic upper crustal rocks, and <strong>mantle basal heat flux</strong> ($q_m$) conducted into the base of the crust from the underlying asthenosphere.</p>
      
      <ul>
        <li><strong>Crustal Geothermal Gradient:</strong> In stable continental shields and cratons, the geothermal gradient near the surface averages approximately <strong>$20^\\circ - 25^\\circ\\text{C / km}$</strong> (or $25^\\circ - 30^\\circ\\text{C / km}$ in younger tectonic provinces). Because radiogenic elements are strongly concentrated in the upper $10-15\\text{ km}$, the gradient curves and decreases with depth.</li>
        <li><strong>Depth of the Lower Crust:</strong>
          <ul>
            <li><strong>Upper Crust (Sial):</strong> Extends from surface to the <strong>Conrad Discontinuity</strong> at depths of approximately $15 - 20\\text{ km}$.</li>
            <li><strong>Lower Crust (Sima):</strong> Extends from the Conrad Discontinuity ($\approx 20\\text{ km}$) down to the <strong>Mohorovicic Discontinuity (Moho)</strong> at $\approx 35 - 40\\text{ km}$.</li>
          </ul>
        </li>
        <li><strong>Temperature at the Upper Part of the Lower Crust:</strong>
          <ul>
            <li>At the top of the lower crust (depth $z \\approx 20 - 22\\text{ km}$), conductive thermal integration yields:
              $$T(z) = T_0 + \\int_0^z \\left( \\frac{q_m + A(z')}{k} \\right) dz' \\approx \\mathbf{400^\\circ - 500^\\circ\\text{C}}$$
            </li>
            <li><strong>Rheological Significance:</strong> This $400^\\circ - 500^\\circ\\text{C}$ temperature regime marks the critical <strong>Brittle-to-Ductile Transition Zone</strong> for plagioclase feldspar. While quartz transitions from brittle to crystal-plastic dislocation creep at $\approx 300^\\circ\\text{C}$, plagioclase feldspars (the dominant framework mineral of the lower crust) become plastic only above $450^\\circ - 500^\\circ\\text{C}$. Thus, the upper part of the lower crust marks the threshold where the entire crust becomes fully ductile.</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "Temperature increases continuously with depth within the earth. In the continental crust, the average geothermal gradient is about 20° to 30°C per kilometer depth. At the upper boundary of the lower crust, at depths of about 20 km, <strong>the temperature regime reaches approximately 400° to 500°C</strong>. At the base of the crust (Moho), temperatures reach about 600° to 800°C."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Interior of the Earth: Temperature Regime, p. 22) & John D. Winter, Ch. 1, p. 5</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">1D Steady-State Continental Geotherm Equation</div>
        $$T(z) = T_0 + \\frac{q_0 z}{k} - \\frac{A_0 D^2}{k} \\left( 1 - e^{-z/D} \\right)$$
        $$\\text{At depth } z = 20\\text{ km:} \\quad T(20) \\approx 20^\\circ\\text{C} + (20\\text{ km} \\times 22^\\circ\\text{C/km}) \\approx \\mathbf{440^\\circ - 460^\\circ\\text{C}}$$
        $$\\text{Brittle-Ductile Transition: } \\quad T_{\\text{quartz plasticity}} \\approx 300^\\circ\\text{C} \\quad \\big| \\quad T_{\\text{feldspar plasticity}} \\approx 450^\\circ - 500^\\circ\\text{C}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $q_0$ is surface heat flow ($\approx 60\text{ mW/m}^2$), $k$ is thermal conductivity ($\approx 2.5-3.0\text{ W}/(\text{m}\cdot\text{K})$), $A_0$ is surface radiogenic heat production ($\approx 2\text{ }\mu\text{W/m}^3$), and $D$ is radiogenic scale depth ($\approx 10\text{ km}$).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q045/winter_continental_geotherm_crustal_temperatures.png" alt="Winter Fig 1 Continental Geothermal Gradient Lower Crust">
        <div class="tb-caption">
          <strong>Figure 45.1: Continental Geothermal Gradient & Crustal Temperatures (Winter, Ch. 1, p. 5).</strong> Temperature-depth profile through continental lithosphere showing temperatures reaching $400-500^\circ\text{C}$ in the upper lower crust at depths of $20-25\text{ km}$.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Crustal Stratification & Corresponding Temperature Regimes</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Crustal Layer</th>
            <th>Depth Range (km)</th>
            <th>Temperature Regime (°C)</th>
            <th>Dominant Mineralogy & Facies</th>
            <th>Rheological Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Near-Surface Crust</strong></td>
            <td>$0 - 5\\text{ km}$</td>
            <td>$20^\\circ - 150^\\circ\\text{C}$</td>
            <td>Sedimentary rocks, unmetamorphosed</td>
            <td>Brittle (Frictional Mohr-Coulomb faulting)</td>
          </tr>
          <tr>
            <td><strong>Mid-Upper Crust</strong></td>
            <td>$10 - 15\\text{ km}$</td>
            <td>$250^\\circ - 350^\\circ\\text{C}$</td>
            <td>Greenschist facies (Quartz + Chlorite)</td>
            <td>Quartz undergoes ductile crystal-plastic creep</td>
          </tr>
          <tr>
            <td><strong>Upper Part of Lower Crust</strong></td>
            <td><strong>$20 - 25\\text{ km}$</strong></td>
            <td><strong>$400^\\circ - 500^\\circ\\text{C}$</strong></td>
            <td><strong>Amphibolite to Granulite facies transition</strong></td>
            <td><strong>Feldspars become plastic; fully ductile flow</strong></td>
          </tr>
          <tr>
            <td><strong>Base of Lower Crust (Moho)</strong></td>
            <td>$35 - 40\\text{ km}$</td>
            <td>$650^\\circ - 800^\\circ\\text{C}$</td>
            <td>Mafic granulite (Plagioclase + Pyroxene + Garnet)</td>
            <td>High-temperature dislocation creep, partial melting</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q45_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q045</div>
    <div class="q-stmt">The temperature regime in the upper part of the lower crust is:</div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) 400-500°C</div>
      <div class="raw-opt">(B) 300-400°C</div>
      <div class="raw-opt">(C) 100-200°C</div>
      <div class="raw-opt">(D) 200-250°C</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (A) 400-500°C</div>
      <div class="sub">Verified against Bangar (p. 22), Winter (Principles of Igneous & Metamorphic Petrology, p. 5), and Fowler (The Solid Earth, p. 235). Under standard continental geothermal gradients ($20-25^\circ\text{C/km}$), temperatures at depths of $20-25\text{ km}$ (the upper lower crust) reach precisely 400° to 500°C.</div>
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) 400-500°C</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The lower continental crust begins at the Conrad discontinuity at a depth of approximately $20\text{ km}$. Multiplying this depth by standard continental geothermal gradients ($20^\circ-25^\circ\text{C/km}$) demonstrates that the temperature regime prevailing at the top of the lower crust is precisely <strong>$400^\circ - 500^\circ\text{C}$</strong>. This temperature matches the onset of crystal-plasticity in feldspars and corresponds to middle amphibolite facies metamorphic conditions.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) 300-400°C</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The $300^\circ - 400^\circ\text{C}$ temperature regime is characteristic of the <strong>middle to lower part of the UPPER crust</strong> (depths of $12 - 16\text{ km}$), where greenschist facies metamorphism occurs and quartz undergoes plastic deformation while feldspar remains brittle.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) 100-200°C</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> $100^\circ - 200^\circ\text{C}$ corresponds to the <strong>shallow upper crust</strong> at depths of only $4 - 8\text{ km}$, characteristic of sedimentary diagenesis and early zeolite facies burial metamorphism.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) 200-250°C</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Temperatures of $200^\circ - 250^\circ\text{C}$ prevail at depths of $8 - 10\text{ km}$ within the upper crust, where oil generation windows terminate and brittle micro-fracturing dominates.
    </div>
  </div>
"""

q45_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Metamorphic Facies & Mineral Assemblages Across Crustal Levels</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Crustal Domain</th>
            <th>Typical Depth</th>
            <th>Temperature Range</th>
            <th>Metamorphic Facies</th>
            <th>Diagnostic Mineral Assemblage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Shallow Crust</strong></td>
            <td>$0 - 8\\text{ km}$</td>
            <td>$20^\\circ - 200^\\circ\\text{C}$</td>
            <td>Zeolite Facies</td>
            <td>Zeolites (Laumontite, Heulandite), Smectite</td>
          </tr>
          <tr>
            <td><strong>Middle Upper Crust</strong></td>
            <td>$10 - 15\\text{ km}$</td>
            <td>$250^\\circ - 350^\\circ\\text{C}$</td>
            <td>Greenschist Facies</td>
            <td>Chlorite + Epidote + Albite + Actinolite</td>
          </tr>
          <tr>
            <td><strong>Upper Part of Lower Crust</strong></td>
            <td><strong>$20 - 25\\text{ km}$</strong></td>
            <td><strong>$400^\\circ - 500^\\circ\\text{C}$</strong></td>
            <td><strong>Amphibolite Facies</strong></td>
            <td><strong>Hornblende + Oligoclase/Andesine + Garnet</strong></td>
          </tr>
          <tr>
            <td><strong>Deepest Lower Crust</strong></td>
            <td>$30 - 40\\text{ km}$</td>
            <td>$700^\\circ - 850^\\circ\\text{C}$</td>
            <td>Granulite Facies</td>
            <td>Orthopyroxene (Hypersthene) + Clinopyroxene + Garnet</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Geothermics & Lower Crustal Petrology</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Temperature Calculation from Geothermal Gradient</div>
        <div class="pq-ans">Temperature $T = 460^\\circ\\text{C}$ at $z = 20\\text{ km}$</div>
        <div class="pq-exp">Assuming a mean surface temperature $T_0 = 20^\\circ\\text{C}$ and an average geothermal gradient $\\nabla T = 22^\\circ\\text{C/km}$ through the upper crust, calculate the temperature at depth $z = 20\\text{ km}$.<br>
        $$T(20) = T_0 + z \\cdot \\nabla T = 20 + 20 \\times 22 = 20 + 440 = 460^\\circ\\text{C}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Plagioclase Brittle-Ductile Transition Temperature</div>
        <div class="pq-ans">Plagioclase transitions to crystal-plasticity at $450^\\circ - 500^\\circ\\text{C}$</div>
        <div class="pq-exp">In quartz-feldspathic crustal rocks, quartz flows ductilely above $300^\\circ\\text{C}$, but the rock retains macroscopic strength until plagioclase feldspars soften at $450-500^\\circ\\text{C}$, enabling pervasive ductile shearing in the lower crust.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: The Conrad Discontinuity as a Petrological Boundary</div>
        <div class="pq-ans">Transition from granodioritic upper crust to mafic granulitic lower crust</div>
        <div class="pq-exp">V. Conrad (1925) identified a mid-crustal seismic velocity jump from $6.0$ to $6.8\\text{ km/s}$ at $15-20\\text{ km}$ depth, marking the compositional change from hydrous granitic rocks to dry, dense mafic granulites.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Heat Generation in the Lower Crust vs. Upper Crust</div>
        <div class="pq-ans">Lower crust is depleted in radioactive isotopes ($A_{\\text{lower}} \\approx 0.2 - 0.4\\text{ }\\mu\\text{W/m}^3$)</div>
        <div class="pq-exp">Large-ion lithophile elements (U, Th, K) are strongly incompatible in mantle melting and partition preferentially into upper crustal granites ($A_{\\text{upper}} \\approx 1.5 - 3.0\\text{ }\\mu\\text{W/m}^3$), leaving the lower crust chemically depleted in radiogenic heat production.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Maximum Depth of Continental Earthquakes</div>
        <div class="pq-ans">Restricted to upper $15 - 20\\text{ km}$ (the seismogenic zone)</div>
        <div class="pq-exp">Because rocks below $20\\text{ km}$ ($>400^\\circ\\text{C}$) deform by ductile plastic creep rather than brittle fracture, elastic strain cannot accumulate, confining continental earthquakes strictly to the brittle upper crust.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Dehydration Melting of Biotite in the Lower Crust</div>
        <div class="pq-ans">Biotite dehydration melting initiates at $\\approx 750^\\circ - 800^\\circ\\text{C}$</div>
        <div class="pq-exp">At depths approaching the Moho ($30-35\\text{ km}$), temperatures exceed $750^\\circ\\text{C}$, causing biotite and hornblende to break down via dehydration melting, generating granitic leucosomes (migmatites) and anhydrous granulite restites.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Underplating of Mafic Magma at the Moho</div>
        <div class="pq-ans">Ponding of dense mantle basalt at crust-mantle boundary due to neutral buoyancy</div>
        <div class="pq-exp">Ascending mantle basaltic melts ($\rho \approx 2.8\text{ g/cm}^3$) are more buoyant than mantle ($3.3\text{ g/cm}^3$) but denser than upper crust ($2.7\text{ g/cm}^3$), causing them to pond and crystallize at the Moho, underplating the lower crust with high-temperature gabbroic cumulates.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Electrical Conductivity of the Lower Crust</div>
        <div class="pq-ans">High conductivity layers caused by saline metamorphic fluids or graphite films</div>
        <div class="pq-exp">Magnetotelluric (MT) surveys worldwide reveal zones of anomalous high electrical conductivity at $20-30\text{ km}$ depth ($400-500^\circ\text{C}$), attributed to interconnected saline brines released by prograde metamorphic dehydration.</div>
      </div>
    </div>
  </div>
"""

# Generate all pages
generate_page(
    q_num=41,
    filename="Q041_Average_Depth_Ocean_3729_Meters_Complete_Guide.html",
    title="Q041: Marine Hypsometry: Average Depth of the Ocean (3,729 m)",
    badge="OPSC 2019 · Paper-II · Q041 · Oceanography & Marine Geology",
    h1_title="The Average Depth of the Global Ocean (3,729 Meters)",
    meta_text="Question ID: GEO-2019-Q041 | Topic: Marine Hypsometry & Physical Oceanography | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q41_part1,
    part2_html=q41_part2,
    part3_html=q41_part3
)

generate_page(
    q_num=42,
    filename="Q042_Palaeomagnetic_Data_Pole_Reversals_Complete_Guide.html",
    title="Q042: Paleomagnetism: Geomagnetic Pole Reversals & Seafloor Striping",
    badge="OPSC 2019 · Paper-II · Q042 · Paleomagnetism & Geotectonics",
    h1_title="Palaeomagnetic Data and Geomagnetic Pole Reversals",
    meta_text="Question ID: GEO-2019-Q042 | Topic: Paleomagnetism & Seafloor Spreading | Difficulty: Moderate | Target Time: 35 sec",
    part1_html=q42_part1,
    part2_html=q42_part2,
    part3_html=q42_part3
)

generate_page(
    q_num=43,
    filename="Q043_Guyot_Flat_Topped_Seamount_Complete_Guide.html",
    title="Q043: Marine Geomorphology: Guyot as a Flat-Topped Seamount",
    badge="OPSC 2019 · Paper-II · Q043 · Marine Geology & Geomorphology",
    h1_title="Guyots: Drowned Flat-Topped Volcanic Seamounts",
    meta_text="Question ID: GEO-2019-Q043 | Topic: Marine Geomorphology & Seamounts | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q43_part1,
    part2_html=q43_part2,
    part3_html=q43_part3
)

generate_page(
    q_num=44,
    filename="Q044_Deep_Sea_Trenches_Circum_Pacific_Belt_Complete_Guide.html",
    title="Q044: Subduction Geodynamics: Deep Sea Trenches in Circum-Pacific Belt",
    badge="OPSC 2019 · Paper-II · Q044 · Geotectonics & Subduction Zones",
    h1_title="Deep Sea Trenches and the Circum-Pacific Belt",
    meta_text="Question ID: GEO-2019-Q044 | Topic: Oceanic Trenches & Subduction Zones | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q44_part1,
    part2_html=q44_part2,
    part3_html=q44_part3
)

generate_page(
    q_num=45,
    filename="Q045_Temperature_Regime_Upper_Lower_Crust_400_500_Complete_Guide.html",
    title="Q045: Crustal Geothermics: Temperature in Upper Lower Crust (400-500°C)",
    badge="OPSC 2019 · Paper-II · Q045 · Geothermics & Solid Earth Geophysics",
    h1_title="Temperature Regime in the Upper Part of the Lower Crust (400-500°C)",
    meta_text="Question ID: GEO-2019-Q045 | Topic: Continental Geotherm & Crustal Physics | Difficulty: Moderate | Target Time: 35 sec",
    part1_html=q45_part1,
    part2_html=q45_part2,
    part3_html=q45_part3
)

print("Batch 4 Part B (Q041 - Q045) completed successfully!")
