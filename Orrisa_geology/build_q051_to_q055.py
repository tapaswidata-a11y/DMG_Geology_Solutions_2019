#!/usr/bin/env python3
"""
Masterclass Builder for Batch 5A: Indian Stratigraphy, Petroleum & Geological Principles (Q051 - Q055)
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q051: Gondwana Stratigraphy: Barren Measures Formation
# ==============================================================================
def generate_q051():
    title = r"Q051: Lower Gondwana Stratigraphy: The Barren Measures Formation | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Gondwana Coal Geology"
    h1_title = "Q051: Lower Gondwana: The Barren Measures Formation"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 51<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 318–322); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 13: Stratigraphy of India, pp. 336–339, p. 176); Ramakrishnan & Vaidyanadhan, <em>Geology of India</em> (Vol. 2, Ch. 18: Gondwana Supergroup, pp. 612–626); M.S. Krishnan, <em>Geology of India and Burma</em> (Ch. 10)."""

    part1 = r"""
  <!-- CARD 1: STRATIGRAPHIC SUCCESSION OF THE DAMUDA GROUP -->
  <div class="card">
    <div class="card-header bg-blue">1. The Damuda Group: The Permian Coal Measures of Peninsular India</div>
    <div class="card-body">
      <p>The <strong>Damuda Group</strong> (Permian) of the Lower Gondwana Supergroup contains the world-famous commercial bituminous coal measures of Peninsular India. Across the Damodar, Son-Mahanadi, and Pranhita-Godavari valleys, the Damuda succession is classically subdivided into three distinct lithostratigraphic formations in ascending order:</p>

      <ul>
        <li><strong>1. Barakar Formation (Early Permian / Artinskian-Kungurian):</strong> The primary lower coal-bearing formation ($250-700\text{ m}$ thick). Characterized by fining-upward channel cycles of coarse, white feldspathic (arkosic) sandstones, grey shales, fireclays, and multiple thick, workable bituminous coal seams (e.g., Seams I through XVI in Jharia and Raniganj).</li>
        <li><strong>2. Barren Measures Formation (Middle Permian / Roadian-Wordian):</strong> The non-coaliferous stratigraphic interval sandwiched conformably between the two major coal-bearing units. It attains a thickness of $300-600\text{ m}$ in the Jharia and Bokaro coalfields. In the Raniganj Coalfield, this identical lithostratigraphic horizon is historically termed the <strong>Ironstone Shale Formation</strong> due to the abundant siderite and limonite nodules embedded in its dark carbonaceous shales.</li>
        <li><strong>3. Raniganj Formation (Late Permian / Capitanian-Changhsingian):</strong> The upper coal-bearing formation ($500-1000\text{ m}$ thick). Dominated by fine to medium-grained calcareous and feldspathic sandstones, siltstones, and numerous high-volatile, long-flame superior coal seams accompanied by an advanced <em>Glossopteris</em> flora.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q51/mahapatra_p168_barren_measures_damuda_succession.png" alt="Barren Measures in Damuda Succession">
        <div class="tb-caption">
          <strong>Figure 51.1 (G.B. Mahapatra, p. 168):</strong> Lithostratigraphic column of the Damuda Group illustrating the Barren Measures (Ironstone Shales) sandwiched conformably between the Barakar and Raniganj coal measures.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: PALEOENVIRONMENT OF THE BARREN MEASURES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Depositional Mechanics and Climatic Hiatus of Coalification</div>
    <div class="card-body">
      <p>The total absence of workable coal in the Barren Measures reflects a profound paleoclimatic and paleoenvironmental shift across eastern Gondwanaland during the Mid-Permian:</p>

      <div class="formula-card">
        <div class="formula-title">The Classic Tripartite Damuda Chronostratigraphic Sandwich</div>
        $$\mathbf{Barakar \text{ Formation}} \quad \longrightarrow \quad \mathbf{Barren \text{ Measures (Ironstone Shales)}} \quad \longrightarrow \quad \mathbf{Raniganj \text{ Formation}}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Warm Humid Peat Swamps $\to$ Warm Semi-Arid Stagnant Lakes $\to$ Restored Humid River-Floodplain Peat Swamps.</p>
      </div>

      <ul>
        <li><strong>Semi-Arid Climatic Pulsing:</strong> During the Middle Permian, an interval of seasonal aridity and intense seasonal drying curtailed the continuous, lush growth of swamp vegetation required for thick peat accumulation.</li>
        <li><strong>Stagnant Lacustrine Ironstone Deposition:</strong> Sedimentation shifted from high-energy braided fluvial channels to extensive, shallow, stratified lacustrine bodies. High dissolved ferrous iron in anoxic, acidic bottom waters reacted with bicarbonate to precipitate bedded and nodular <strong>siderite ($\text{FeCO}_3$)</strong>, which weathered subaerially to limonite and goethite ironstones.</li>
        <li><strong>Basin Equivalents:</strong> In the Godavari and Satpura basins, coeval non-coal strata are termed the <strong>Motur Formation</strong> and Lower Kamthi beds.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q51/bangar_p176_lower_gondwana_coalfields.png" alt="Lower Gondwana Coalfields from Bangar">
        <div class="tb-caption">
          <strong>Figure 51.2 (K.M. Bangar, p. 176):</strong> Stratigraphic classification of Lower Gondwana formations across the Jharia, Raniganj, and Central Indian coalfields.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF LOWER GONDWANA UNITS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Stratigraphic Subdivisions of the Damuda Group</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Stratigraphic Unit</th>
            <th>Stage / Epoch</th>
            <th>Dominant Lithofacies</th>
            <th>Workable Coal Seams</th>
            <th>Primary Flora</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Raniganj Formation</strong></td>
            <td>Late Permian (Lopingian)</td>
            <td>Fine-grained sandstones, carbonaceous shales.</td>
            <td><strong>Abundant</strong> (High-volatile bituminous coal; Raniganj Seams).</td>
            <td><em>Glossopteris retifera, Vertebraria indica, Schizoneura</em>.</td>
          </tr>
          <tr>
            <td><strong>Barren Measures Formation</strong> (Ironstone Shales)</td>
            <td><strong>Middle Permian (Guadalupian)</strong></td>
            <td><strong>Carbonaceous black shales, siderite ironstone bands, micaceous siltstones.</strong></td>
            <td><strong>Completely Barren of Workable Coal (Zero Coal)</strong></td>
            <td>Sparse, stunted <em>Glossopteris conspicua, Cyclodendron</em>.</td>
          </tr>
          <tr>
            <td><strong>Barakar Formation</strong></td>
            <td>Early Permian (Cisuralian)</td>
            <td>Coarse arkosic sandstones, fireclays, grey shales.</td>
            <td><strong>Prolific</strong> (Prime coking coal seams of India; Seams I to XVI).</td>
            <td><em>Glossopteris communis, Gangamopteris cyclopteroides</em>.</td>
          </tr>
          <tr>
            <td><strong>Karharbari Formation</strong></td>
            <td>Basal Cisuralian (Sakmarian)</td>
            <td>Sub-arkosic sandstones, grits, conglomerate.</td>
            <td>High-grade low-ash coking coal (Giridih Seams).</td>
            <td><em>Gondwanidium validum, Buriadia sewardana</em>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 51</div>
        <div class="q-text">The Mid-Permian non-coaliferous lithounit sandwitched between two major coal-bearing formations in the Indian Lower Gondwana succession is known as.________ Formation.</div>
        <div class="q-options">
          <div class="opt-node">(A) Barakar</div>
          <div class="opt-node">(B) Lower Kamthi</div>
          <div class="opt-node correct">(C) Barren Measures</div>
          <div class="opt-node">(D) Raniganj</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(C) Barren Measures</strong> [The Barren Measures Formation (known as Ironstone Shales in Raniganj) is the non-coal-bearing Mid-Permian unit sandwiched between the coal-bearing Barakar and Raniganj Formations.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (C) Barren Measures</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>Within the Permian Damuda Group of the Indian Gondwana Supergroup, coal deposition was famously punctuated during the Middle Permian by an interval devoid of economic coal seams.</li>
        <li>This non-coal-bearing formation is formally designated the <strong>Barren Measures Formation</strong> (so named by Fox in 1931 because it is completely barren of workable coal seams). In the Raniganj basin, it is known as the Ironstone Shale Formation.</li>
        <li>It lies directly and conformably above the richly coal-bearing <strong>Barakar Formation</strong> and directly below the major coal-bearing <strong>Raniganj Formation</strong>.</li>
        <li>Therefore, the unit sandwiched between the two major coal-bearing formations is unequivocally the <strong>Barren Measures Formation</strong>.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Barakar</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Barakar Formation</strong> is the premier <em>coal-bearing</em> formation of India, hosting the thickest and most valuable coking coal seams in the Damodar, Mahanadi, and Son basins.</li>
        <li>It represents the underlying coaliferous member, not the non-coaliferous unit sandwiched in the middle.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) Raniganj</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Raniganj Formation</strong> is the upper major <em>coal-bearing</em> formation of the Damuda Group, celebrated for superior non-coking and long-flame thermal coals.</li>
        <li>It overlies the Barren Measures; it is not the sandwiched non-coal unit.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Lower Kamthi</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Kamthi Formation</strong> is a lithostratigraphic unit of the Pranhita-Godavari and Wardha-Nagpur valleys, extending from the Late Permian into the Early Triassic.</li>
        <li>In standard Pan-Indian Gondwana nomenclature, the canonical Damuda sandwich sequence is Barakar $\to$ <strong>Barren Measures</strong> $\to$ Raniganj. Lower Kamthi is a lateral provincial correlate in central India, not the standard textbook sandwich unit.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Coal-Bearing vs. Barren Formations of Gondwana</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Gondwana Basin</th>
            <th>Lower Coal-Bearing Formation</th>
            <th>Middle Barren / Non-Coal Formation</th>
            <th>Upper Coal-Bearing Formation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Jharia / Bokaro / Karanpura</strong></td>
            <td>Barakar Formation (Seams I to XVI)</td>
            <td><strong>Barren Measures Formation</strong> (Carbonaceous shales)</td>
            <td>Raniganj Formation (Mahuda Group)</td>
          </tr>
          <tr>
            <td><strong>Raniganj Coalfield</strong></td>
            <td>Barakar Formation</td>
            <td><strong>Ironstone Shale Formation</strong> (Sideritic shales)</td>
            <td>Raniganj Formation</td>
          </tr>
          <tr>
            <td><strong>Satpura Basin</strong></td>
            <td>Barakar Formation</td>
            <td><strong>Motur Formation</strong> (Red & green mottled clays)</td>
            <td>Bijori Formation</td>
          </tr>
          <tr>
            <td><strong>Pranhita-Godavari Basin</strong></td>
            <td>Barakar Formation</td>
            <td><strong>Barren Measures / Kothagudem Barren beds</strong></td>
            <td>Lower Kamthi / Somagudem beds</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Gondwana Stratigraphy & Coal Petrology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Siderite to Limonite Diagenetic Oxidation</div>
        <p>In the Ironstone Shales of Raniganj, bedded siderite ($\text{FeCO}_3$, density $\rho = 3.96\text{ g/cm}^3$) oxidizes upon exposure to goethite ($\text{FeO(OH)}$, density $\rho = 4.28\text{ g/cm}^3$). Write the balanced geochemical oxidation-hydration reaction.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In the presence of atmospheric oxygen and surface groundwater:</p>
        $$4\text{FeCO}_3 + \text{O}_2 + 2\text{H}_2\text{O} \longrightarrow 4\text{FeO(OH)} + 4\text{CO}_2 \uparrow$$
        <p>This reaction dissolves soluble bicarbonate, precipitating insoluble hydrous iron oxyhydroxides (limonite and goethite) that cement the shales into dense, reddish-brown ironstone bands historically smelted at Kulti (Bengal Iron Works).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Coal Seam Peat Compaction Ratio</div>
        <p>If the peat-to-bituminous coal compaction ratio in the Barakar Formation is $10:1$, calculate the original peat swamp thickness required to generate a $12\text{ m}$ thick coal seam.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$T_{\text{peat}} = 10 \times T_{\text{coal}} = 10 \times 12\text{ m} = 120\text{ m}$$
        <p><strong>Final Answer:</strong> A massive $120\text{ m}$ of waterlogged peat was accumulated to yield a $12\text{ m}$ thick bituminous coal seam.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Vitrinite Reflectance and Coal Rank</div>
        <p>Barakar coking coals typically exhibit mean random vitrinite reflectance $R_o = 1.15\%-1.35\%$, whereas Raniganj non-coking coals have $R_o = 0.70\%-0.85\%$. Explain the geological reason for this rank disparity.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Barakar Formation was buried beneath more than $2000-3000\text{ m}$ of overlying Barren Measures, Raniganj, and Panchet strata. Due to deeper burial depth ($z$) and higher paleo-temperatures ($T \propto z \cdot dT/dz$), the Barakar coals underwent more intense thermal catagenesis, aromatization, and volatile loss, advancing to high-rank medium-volatile coking coal.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Botanical Identity of Vertebraria</div>
        <p>What anatomical part of the Gondwana seed-fern plant does the common fossil <em>Vertebraria</em> represent?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Vertebraria indica</em> represents the specialized <strong>root system (rhizome)</strong> of the <em>Glossopteris</em> tree. Its unique transverse rectangular partitions (resembling vertebrae) provided internal air cavities (aerenchyma) allowing the plant to breathe in waterlogged, anoxic peat bogs.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Proximate Analysis Calculation</div>
        <p>A coal sample from the Barakar Formation yields: Moisture $M = 2.0\%$, Ash $A = 18.0\%$, Volatile Matter $VM = 26.0\%$. Calculate the Fixed Carbon ($FC$) content on an air-dried basis.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$FC = 100\% - (M + A + VM)$$
        $$FC = 100 - (2.0 + 18.0 + 26.0) = 100 - 46.0 = 54.0\%$$
        <p><strong>Final Answer:</strong> Fixed Carbon is $54.0\%$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Differentiation of Gondwanidium vs. Glossopteris</div>
        <p>How does the basal Gondwana index plant fossil <em>Gondwanidium</em> differ from <em>Glossopteris</em>?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong><em>Gondwanidium validum</em>:</strong> Possesses pinnate, lobed fronds with neuropteroid venation without a true midrib or reticulate anastomosing mesh. Diagnostic index fossil of the early Sakmarian Karharbari Formation.</li>
          <li><strong><em>Glossopteris</em>:</strong> Possesses simple, tongue-shaped (lingulate) leaves with a distinct prominent central midrib and complex polygonal reticulate anastomosing secondary veins.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Palynological Biozone of the Barren Measures</div>
        <p>Which miospore assemblage characterizes the Barren Measures Formation in Indian palynostratigraphy?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Barren Measures is defined by the <strong><em>Densipollenites indicus</em> Assemblage Zone</strong> (monosaccate envelope pollen), with sub-dominant <em>Striatopodocarpites</em> and <em>Faunipollenites</em>, reflecting drought-tolerant gymnosperm floral elements surrounding shrinking lakes.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Coalfield Boundary Fault Reactivation</div>
        <p>Why are Indian Gondwana coalfields characterized by half-graben geometry with a single master boundary fault on the southern margin?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Extensional intraplate stress during the Permo-Triassic reactivated pre-existing Proterozoic basement faults as asymmetric listric normal faults. Continued fault displacement rotated the sedimentary floor into a hanging-wall syncline, tilting strata southward towards the master normal boundary fault where maximum sediment thickness is preserved.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 51, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q051_Barren_Measures_Gondwana_Succession_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q051: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q052: Digboi Oilfield of Assam: Tipam Group Anticline
# ==============================================================================
def generate_q052():
    title = r"Q052: Petroleum Geology: Digboi Oilfield of Assam & Tipam Group Anticlinal Trap | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Petroleum Geology & Assam-Arakan Basin"
    h1_title = "Q052: Digboi Oilfield of Assam: Tipam Group Structural Trap"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 52<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 9: Structural Geology, pp. 248–254, Fig. 9.17); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 338–342); P.K. Bhowmick et al., <em>Hydrocarbon Prospects of Assam-Arakan Basin</em> (ONGC Special Publication); Richard C. Selley, <em>Elements of Petroleum Geology</em> (3rd Ed., Academic Press, Ch. 7)."""

    part1 = r"""
  <!-- CARD 1: THE HISTORIC DIGBOI OILFIELD -->
  <div class="card">
    <div class="card-header bg-blue">1. The Historic Digboi Oilfield: Birthplace of the Indian Petroleum Industry</div>
    <div class="card-body">
      <p>The <strong>Digboi Oilfield</strong> in the Tinsukia district of Upper Assam is the oldest operating oil field in India and Asia, discovered in 1889 following the drilling of Well No. 1 by the Assam Railways and Trading Company (later Assam Oil Company):</p>

      <ul>
        <li><strong>Structural Geology of the Trap:</strong> The oilfield is situated on a prominent, narrow, sharply folded, asymmetric anticlinal structure termed the <strong>Digboi Anticline</strong>:
          <ul>
            <li><strong>Trend and Symmetry:</strong> Trends approximately ENE–WSW ($060^\circ-240^\circ$) for over $14\text{ km}$, plunging towards the west-southwest. Its northern flank is extremely steep ($70^\circ-80^\circ$ to near vertical) and truncated by a regional low-angle reverse fault known as the <strong>Naga Thrust</strong>. The southern flank dips much more gently ($30^\circ-40^\circ$).</li>
            <li><strong>Trap Type:</strong> A classic <strong>faulted asymmetric anticlinal trap</strong> (combination structural trap).</li>
          </ul>
        </li>
        <li><strong>Reservoir Lithology:</strong> The commercial hydrocarbon reservoirs occur in multi-layered, porous, deltaic-to-fluvial sandstone beds belonging to the <strong>Tipam Group</strong> (specifically the Middle Miocene <strong>Tipam Sandstone Formation</strong>).</li>
        <li><strong>Petroleum System:</strong>
          <ul>
            <li><strong>Source Rock:</strong> Deeply buried carbonaceous shales and coals of the Oligocene <strong>Barail Group</strong> (Tikak Parbat Formation) that reached thermal maturity in the adjacent foreland trough.</li>
            <li><strong>Reservoir Rock:</strong> Porous, permeable sandstones of the Miocene <strong>Tipam Group</strong> (Bappapung Sandstone / Digboi Oil Sands).</li>
            <li><strong>Cap Rock (Seal):</strong> Overlying impermeable silts and shales of the <strong>Girujan Clay Formation</strong> (upper Tipam Group).</li>
          </ul>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q52/mahapatra_p178_assam_tipam_digboi_stratigraphy.png" alt="Assam Tipam Digboi Stratigraphy">
        <div class="tb-caption">
          <strong>Figure 52.1 (G.B. Mahapatra, p. 178):</strong> Tertiary stratigraphic succession of the Assam-Arakan Basin showing the Tipam Sandstone reservoir sealed by Girujan clays within the faulted Digboi anticline.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: ANTICLINAL TRAP MECHANICS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Structural Geology of Anticlinal Petroleum Traps</div>
    <div class="card-body">
      <p>The anticlinal theory of petroleum accumulation, first formulated by T. Sterry Hunt and I.C. White, is classically exemplified by the Digboi structure:</p>

      <div class="formula-card">
        <div class="formula-title">Hydrocarbon Buoyancy Secondary Migration in an Anticline</div>
        $$F_{\text{buoyancy}} = (\rho_{\text{water}} - \rho_{\text{oil}}) g \cdot V > P_{\text{capillary entry}} = \frac{2\gamma \cos\theta}{r_{\text{pore}}}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Because oil ($\rho \sim 850\text{ kg/m}^3$) and gas ($\rho \sim 150\text{ kg/m}^3$) are lighter than formation connate brine ($\rho \sim 1050\text{ kg/m}^3$), buoyancy drives hydrocarbons upward into the anticlinal crest until trapped beneath the impermeable Girujan Clay roof.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q52/bangar_fig9_17_anticlinal_oil_trap.png" alt="Anticlinal Oil Trap from Bangar">
        <div class="tb-caption">
          <strong>Figure 52.2 (K.M. Bangar, Fig. 9.17):</strong> Cross-section of an anticlinal oil trap demonstrating gravitational segregation: Gas at crest, Oil in intermediate flanks, and Formation Water at the base.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: TERTIARY STRATIGRAPHY OF UPPER ASSAM -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Tertiary Stratigraphy of the Upper Assam Shelf</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Group</th>
            <th>Primary Formations</th>
            <th>Epoch / Age</th>
            <th>Petroleum System Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dihing Group</strong></td>
            <td>Dihing Formation (Pebble beds, sands)</td>
            <td>Pliocene to Pleistocene</td>
            <td>Overburden; post-orogenic molasse fill.</td>
          </tr>
          <tr>
            <td><strong>Dupitila Group</strong></td>
            <td>Upper & Lower Dupitila Sandstones</td>
            <td>Late Miocene to Pliocene</td>
            <td>Regional overburden.</td>
          </tr>
          <tr>
            <td><strong>Tipam Group</strong></td>
            <td><strong>Girujan Clay Formation</strong> (Upper)<br><strong>Tipam Sandstone Formation</strong> (Lower)</td>
            <td><strong>Middle to Late Miocene</strong></td>
            <td><strong>Principal Reservoir (Tipam Sandstone)</strong> sealed by <strong>Girujan Clay</strong> in the Digboi oilfield!</td>
          </tr>
          <tr>
            <td><strong>Surma Group</strong></td>
            <td>Bokabil Formation<br>Bhuban Formation</td>
            <td>Early to Middle Miocene</td>
            <td>Secondary gas and oil reservoirs in Surma Valley.</td>
          </tr>
          <tr>
            <td><strong>Barail Group</strong></td>
            <td>Tikak Parbat Formation<br>Baragolai Formation<br>Naogaon Formation</td>
            <td>Oligocene</td>
            <td><strong>Primary Source Rock</strong> (Coal-shale sequence); also major reservoir in Nahorkatiya.</td>
          </tr>
          <tr>
            <td><strong>Jaintia Group</strong></td>
            <td>Kopili Shale<br>Sylhet Limestone</td>
            <td>Eocene</td>
            <td>Regional seal (Kopili) and carbonate reservoir (Sylhet).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 52</div>
        <div class="q-text">The Digboi oil field of Assam is on a faulted elongate anticline in rocks of the.</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Tipam Group</div>
          <div class="opt-node">(B) Barail Group</div>
          <div class="opt-node">(C) Jaintia Group</div>
          <div class="opt-node">(D) All of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Tipam Group</strong> [The producing structural trap of the Digboi oilfield is developed in porous sandstones of the Miocene Tipam Group within the faulted Digboi anticline.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Tipam Group</div>
    <div class="card-body">
      <p><strong>Detailed Petroleum Geological Forensic Analysis:</strong></p>
      <ul>
        <li>The <strong>Digboi oilfield</strong> (Upper Assam) is developed along an elongated, sharply folded, asymmetric anticlinal structure whose northern flank is truncated by the regional Naga Thrust.</li>
        <li>The hydrocarbon reservoirs at Digboi are hosted in the porous and permeable deltaic sandstones of the <strong>Tipam Group</strong> (specifically the Middle Miocene Tipam Sandstone Formation, comprising the Bappapung and Digboi oil sands), capped by the impervious Girujan Clays.</li>
        <li>Over 24 distinct oil-bearing sand horizons are recognized within the Tipam Group in the Digboi field.</li>
        <li>Therefore, Option <strong>(A) Tipam Group</strong> is the precise and correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Barail Group</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Barail Group</strong> (Oligocene) is famous as the principal <em>source rock</em> for the entire Assam-Arakan petroleum province (via the coal-shale beds of the Tikak Parbat Formation) and serves as the main reservoir in deeper plains fields such as <strong>Nahorkatiya, Moran, and Rudrasagar</strong>.</li>
        <li>However, at the Digboi field itself, commercial production has historically been won from the shallower Miocene <strong>Tipam Group</strong> sandstones.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Jaintia Group</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Jaintia Group</strong> (Eocene) comprises the Sylhet Limestone and Kopili Formation. It forms the deep carbonate reservoir sequence in the Borholla-Champang fields and south of the Shillong Plateau.</li>
        <li>It is buried thousands of meters beneath the Digboi anticline and does not constitute the producing reservoir formation of the Digboi oilfield.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) All of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because the specific faulted anticlinal reservoir of the Digboi field is specifically and classically defined in the <strong>Tipam Group</strong>, selecting "All of these" is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Major Oilfields of the Assam Shelf</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Oilfield</th>
            <th>Discovery Year</th>
            <th>Primary Producing Reservoir</th>
            <th>Trap Style</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Digboi</strong></td>
            <td>1889 (Oldest)</td>
            <td><strong>Tipam Group (Tipam Sandstone)</strong></td>
            <td><strong>Faulted asymmetric anticline (Naga Thrust front).</strong></td>
          </tr>
          <tr>
            <td><strong>Nahorkatiya</strong></td>
            <td>1953</td>
            <td>Barail Group (Barail Main Sand)</td>
            <td>Gently folded gentle anticline with fault closures.</td>
          </tr>
          <tr>
            <td><strong>Moran</strong></td>
            <td>1956</td>
            <td>Barail Group (Oligocene)</td>
            <td>Faulted anticlinal dome in the Brahmaputra alluvium.</td>
          </tr>
          <tr>
            <td><strong>Rudrasagar</strong></td>
            <td>1960</td>
            <td>Barail & Tipam Groups</td>
            <td>Gentle broad anticlinal dome.</td>
          </tr>
          <tr>
            <td><strong>Borholla-Champang</strong></td>
            <td>1973</td>
            <td>Sylhet Limestone (Jaintia Group) & Basement</td>
            <td>Fractured granitic basement and Eocene carbonates.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Petroleum Systems & Basin Analysis</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Oil-Water Contact and Capillary Entry Pressure</div>
        <p>In an anticlinal reservoir, the water density is $\rho_w = 1050\text{ kg/m}^3$ and oil density is $\rho_o = 850\text{ kg/m}^3$. Calculate the buoyancy overpressure gradient ($\Delta \nabla P$) in $\text{kPa/m}$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\Delta \nabla P = (\rho_w - \rho_o) g = (1050 - 850)\text{ kg/m}^3 \times 9.81\text{ m/s}^2 = 200 \times 9.81 = 1962\text{ Pa/m} = 1.962\text{ kPa/m}$$
        <p><strong>Final Answer:</strong> The buoyancy drive is $1.96\text{ kPa}$ per meter of oil column height.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: API Gravity Calculation for Digboi Crude</div>
        <p>Digboi crude oil has a measured specific gravity $SG = 0.840$ at $60^\circ\text{F}$. Calculate its API Gravity ($^\circ\text{API}$) and classify its crude weight.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$^\circ\text{API} = \frac{141.5}{SG} - 131.5 = \frac{141.5}{0.840} - 131.5 = 168.45 - 131.5 = 36.95^\circ\text{API}$$
        <p><strong>Final Answer:</strong> The crude oil has an API gravity of $37.0^\circ\text{API}$, classifying it as high-value <strong>light sweet crude</strong> (rich in paraffin and lubricating oils).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Hydrocarbon Column Capacity of an Anticlinal Spill Point</div>
        <p>The crest of the Tipam reservoir in an anticline is at a subsea depth of $-1200\text{ m}$ and the structural spill point is at $-1350\text{ m}$. Calculate the maximum vertical column height of oil ($h_{\max}$) that this structure can retain before spilling.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$h_{\max} = \text{Depth}_{\text{spill}} - \text{Depth}_{\text{crest}} = 1350\text{ m} - 1200\text{ m} = 150\text{ m}$$
        <p><strong>Final Answer:</strong> The maximum structural oil column height is $150\text{ m}$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Role of the Naga Thrust in Digboi Trapping</div>
        <p>Explain how the regional Naga Thrust functions both as a trapping fault and as a potential leakage hazard at Digboi.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Naga Thrust juxtaposes impermeable clayey Tipam and Barail rocks across fault planes, providing a lateral structural barrier (fault seal) that traps oil in the northern limb. However, where the fault breaches the surface, active seepage of oil occurs (the famous Digboi oil seepages discovered by elephants in 1867), demonstrating that the fault also acts as a dynamic migration conduit.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Kerogen Type in the Barail Group</div>
        <p>Which type of kerogen dominates the coal-shale sequences of the Oligocene Tikak Parbat Formation (Barail Group)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>It is dominated by <strong>Type-III Kerogen</strong> (derived from terrestrial higher plants, rich in vitrinite) with subordinate <strong>Type-II Kerogen</strong> (resinite, cutinite, and exinite). This unique hydrogen-rich coaly kerogen generates both waxy paraffinic crude oil and rich natural gas upon thermal maturation.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Porosity and Permeability of Tipam Sandstone</div>
        <p>A core plug of Tipam Sandstone has bulk volume $V_b = 50\text{ cm}^3$ and dry grain volume $V_g = 39\text{ cm}^3$. Calculate its effective porosity ($\phi$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\phi = \frac{V_b - V_g}{V_b} \times 100\% = \frac{50 - 39}{50} \times 100\% = \frac{11}{50} \times 100\% = 22.0\%$$
        <p><strong>Final Answer:</strong> The porosity is $22\%$, representing an excellent quality commercial petroleum reservoir.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Structural Belt of Schuppen</div>
        <p>In which regional tectonic zone of the Assam-Arakan Basin is the Digboi oilfield located?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Digboi is situated in the <strong>Belt of Schuppen</strong>—a narrow, $20-40\text{ km}$ wide imbricate thrust belt located along the southeastern margin of the Upper Assam Valley where multiple southeast-dipping reverse thrust faults (Naga, Disang, Haflong thrusts) telescope Tertiary strata over the Brahmaputra foreland.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Darcy's Law for Flow in a Tipam Reservoir Sand</div>
        <p>Oil of viscosity $\mu = 2.5\text{ cP}$ flows through a Tipam sand block of length $L = 100\text{ m}$, area $A = 20\text{ m}^2$, permeability $k = 150\text{ mD}$ under a pressure differential $\Delta P = 5.0\text{ atm}$. Calculate the flow rate $Q$ in $\text{cm}^3/\text{s}$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Using Darcy's Law in practical oilfield units ($Q = \frac{k A \Delta P}{\mu L}$ with $k$ in Darcies, $A$ in $\text{cm}^2$, $P$ in atm, $\mu$ in cP, $L$ in cm):</p>
        $$k = 0.150\text{ D}, \quad A = 20\text{ m}^2 = 2.0 \times 10^5\text{ cm}^2, \quad L = 100\text{ m} = 1.0 \times 10^4\text{ cm}$$
        $$Q = \frac{0.150 \times (2.0 \times 10^5) \times 5.0}{2.5 \times (1.0 \times 10^4)} = \frac{1.5 \times 10^5}{2.5 \times 10^4} = 6.0\text{ cm}^3/\text{s}$$
        <p><strong>Final Answer:</strong> The flow rate is $6.0\text{ cm}^3/\text{s}$.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 52, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q052_Digboi_Oilfield_Assam_Tipam_Group_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q052: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q053: Uniformitarianism: The Present is the Key to the Past
# ==============================================================================
def generate_q053():
    title = r"Q053: Fundamental Geological Principles: Uniformitarianism & 'The Present is the Key to the Past' | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Historical Geology & Principles of Stratigraphy"
    h1_title = "Q053: Uniformitarianism: 'The Present is the Key to the Past'"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 53<br>
<strong>Authoritative References:</strong> James Hutton, <em>Theory of the Earth</em> (Trans. Roy. Soc. Edinburgh, 1788); Charles Lyell, <em>Principles of Geology</em> (1830); Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Ch. 1, p. 15); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 1: Introduction, p. 1); Stephen Jay Gould, <em>Time's Arrow, Time's Cycle</em> (Harvard Univ. Press, 1987)."""

    part1 = r"""
  <!-- CARD 1: THE PRINCIPLE OF UNIFORMITARIANISM -->
  <div class="card">
    <div class="card-header bg-blue">1. The Philosophical Foundation of Modern Geological Science</div>
    <div class="card-body">
      <p>The doctrine of <strong>Uniformitarianism</strong> is the foundational philosophical axiom of historical geology, first articulated by Scottish physician and naturalist <strong>James Hutton</strong> in 1785 (published in 1788 and 1795) and later codified into a global scientific framework by <strong>Sir Charles Lyell</strong> in his monumental three-volume treatise <em>Principles of Geology</em> (1830–1833):</p>

      <ul>
        <li><strong>The Classical Maxim:</strong> The core premise of uniformitarianism is immortalized in the famous aphorism popularized by John Playfair (1802) and Charles Lyell:
          <div class="formula-card">
            <div class="formula-title">The Foundational Axiom of Geology</div>
            $$\mathbf{\text{“The Present is the Key to the Past”}}$$
            <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">The physical, chemical, and biological processes operating on the Earth's surface and in its interior today (weathering, river transport, volcanic eruptions, sedimentation, faulting) have operated throughout geological deep time with immutable physical laws.</p>
          </div>
        </li>
        <li><strong>The Historical Anti-Catastrophist Revolution:</strong> Prior to Hutton and Lyell, geology was dominated by <strong>Catastrophism</strong> (championed by Georges Cuvier), which posited that Earth's landscapes and fossil successions were shaped by sudden, violent, supernatural global catastrophes (e.g., Noah's Flood) occurring over a biblically brief chronology of 6,000 years.</li>
        <li><strong>Deep Time (Hutton's Vision):</strong> At Siccar Point in Scotland, Hutton discovered an angular unconformity where vertical Silurian greywackes were planed off and overlain by horizontal Devonian Old Red Sandstone. This revealed immense cycles of sedimentation, deformation, erosion, and re-deposition, prompting his timeless conclusion: <em>"We find no vestige of a beginning, no prospect of an end."</em></li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q53/boggs_p15_uniformitarianism_principle.png" alt="Boggs Uniformitarianism Principle">
        <div class="tb-caption">
          <strong>Figure 53.1 (Sam Boggs Jr., p. 15):</strong> Pedagogical overview of Uniformitarianism vs. Actualism, establishing the immutability of physical and chemical laws across geological time.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: BANGAR EXCERPT AND MODERN ACTUALISM -->
  <div class="card">
    <div class="card-header bg-indigo">2. Modern Refinement: Substantive Uniformitarianism vs. Methodological Actualism</div>
    <div class="card-body">
      <p>In modern geological science, philosophers and geologists (notably Stephen Jay Gould, 1965) distinguish two aspects of uniformitarianism:</p>

      <div class="formula-card">
        <div class="formula-title">Methodological Uniformitarianism (Actualism)</div>
        $$\text{Invariance of Natural Laws: } \quad \left[\frac{\partial (\text{Physical Laws})}{\partial t}\right] = 0$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Gravity ($G$), thermodynamics, Snell's law, and Navier-Stokes equations were identical $3\text{ Ga}$ as today. However, rates and process intensities (meteorite impacts, banded iron formation deposition, oxygen levels) varied dramatically!</p>
      </div>

      <ul>
        <li><strong>Substantive Uniformitarianism (Lyellian Strict Gradualism):</strong> Lyell incorrectly hypothesized that rates of geological processes were always constant and slow, rejecting sudden events. Modern geology rejects strict substantive uniformitarianism because giant bolide impacts (e.g., Chicxulub K-Pg impact) and flood basalt eruptions (Deccan Traps) represent real catastrophic punctuation events.</li>
        <li><strong>Methodological Actualism:</strong> The modern working principle: we use present-day observable processes and natural laws to interpret ancient rocks, recognizing that environmental boundary conditions (e.g., anoxic Archean oceans) were different.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q53/bangar_p1_uniformitarianism_geology.png" alt="Bangar Uniformitarianism">
        <div class="tb-caption">
          <strong>Figure 53.2 (K.M. Bangar, p. 1):</strong> Introductory chapter establishing Uniformitarianism and James Hutton's role as the Father of Modern Geology.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF HISTORICAL PARADIGMS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Comparison: Catastrophism vs. Uniformitarianism vs. Neocatastrophism</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Doctrine</th>
            <th>Primary Proponents</th>
            <th>Timescale</th>
            <th>Rate / Mode of Change</th>
            <th>Primary Geological Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Catastrophism</strong></td>
            <td>Georges Cuvier (1812), Abraham Werner</td>
            <td>Short timescale ($<10,000\text{ years}$).</td>
            <td>Sudden, violent, supernatural global convulsions.</td>
            <td>Worldwide deluges, abrupt faunal annihilations followed by special creations.</td>
          </tr>
          <tr>
            <td><strong>Uniformitarianism (Classical)</strong></td>
            <td><strong>James Hutton (1785), Charles Lyell (1830)</strong></td>
            <td><strong>Immense Deep Time (Billions of years).</strong></td>
            <td><strong>Uniform, gradual, continuous slow operations.</strong></td>
            <td><strong>"The present is the key to the past"</strong>: daily weathering, erosion, sedimentation.</td>
          </tr>
          <tr>
            <td><strong>Neocatastrophism (Modern Synthesis)</strong></td>
            <td>Derek Ager (1993), Stephen Jay Gould</td>
            <td>Deep Time ($4.54\text{ Ga}$).</td>
            <td>Gradual background processes punctuated by rare high-energy catastrophes.</td>
            <td>Long calm intervals interrupted by asteroid impacts, tsunamis, volcanic super-plumes.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 53</div>
        <div class="q-text">As per the concept of ‘uniformitarianism’, the Earth has always changed in uniform ways and that the ‘ :</div>
        <div class="q-options">
          <div class="opt-node">(A) past is the key to the present</div>
          <div class="opt-node">(B) isostatic equilibrium is a key item</div>
          <div class="opt-node correct">(C) present is the key to the past</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(C) present is the key to the past</strong> [The canonical definition of uniformitarianism formulated by James Hutton and Charles Lyell states that the 'present is the key to the past'.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (C) present is the key to the past</div>
    <div class="card-body">
      <p><strong>Detailed Geological Forensic Analysis:</strong></p>
      <ul>
        <li>The doctrine of <strong>Uniformitarianism</strong> (founded by James Hutton in 1785 and popularized by Charles Lyell in 1830) is universally defined by the classic geological dictum:
          $$\mathbf{\text{“The Present is the Key to the Past”}}$$
        </li>
        <li>This principle asserts that the same natural geological processes (such as erosion, weathering, volcanism, sedimentation, and compaction) operating under the immutable laws of physics and chemistry today have operated throughout the Earth's history to produce the rock record.</li>
        <li>By studying modern river deltas, glaciers, deserts, and volcanic flows, geologists can decipher and reconstruct ancient environments preserved in sedimentary rocks.</li>
        <li>Therefore, Option <strong>(C)</strong> is the universally accepted, authoritative correct phrase.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) past is the key to the present</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>This statement reverses the methodological direction of the principle.</li>
        <li>We observe and directly measure <em>present-day</em> processes (which are accessible to immediate scientific instrumentation and testing) in order to unlock and interpret the unobserved <em>past</em> rock record.</li>
        <li>Hence, saying "the past is the key to the present" is a semantic inversion and historically incorrect.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) isostatic equilibrium is a key item</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>While isostatic equilibrium is an important concept in geophysics and geodesy, it is <em>not</em> the defining slogan or conceptual definition of uniformitarianism.</li>
        <li>This is an irrelevant distractor attempting to confuse different geological terms.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (C) represents the exact verbatim formulation of uniformitarianism, Option (D) is false.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Foundational Stratigraphic & Geological Principles</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Stratigraphic Principle</th>
            <th>Pioneering Scientist</th>
            <th>Core Scientific Assertion</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Principle of Uniformitarianism</strong></td>
            <td><strong>James Hutton (1785), Charles Lyell (1830)</strong></td>
            <td><strong>"The present is the key to the past." Natural laws are invariant through time.</strong></td>
          </tr>
          <tr>
            <td><strong>Law of Superposition</strong></td>
            <td>Nicolas Steno (1669)</td>
            <td>In an undeformed sedimentary sequence, the oldest beds lie at the bottom and youngest at top.</td>
          </tr>
          <tr>
            <td><strong>Principle of Original Horizontality</strong></td>
            <td>Nicolas Steno (1669)</td>
            <td>Sedimentary strata are originally deposited as horizontal or nearly horizontal sheets under gravity.</td>
          </tr>
          <tr>
            <td><strong>Principle of Lateral Continuity</strong></td>
            <td>Nicolas Steno (1669)</td>
            <td>Layers of sediment extend laterally in all directions until they thin out or terminate at basin margins.</td>
          </tr>
          <tr>
            <td><strong>Principle of Cross-Cutting Relationships</strong></td>
            <td>James Hutton (1788), Charles Lyell</td>
            <td>An igneous intrusion or fault that cuts across a rock body is younger than the rock it cuts.</td>
          </tr>
          <tr>
            <td><strong>Principle of Inclusions</strong></td>
            <td>Charles Lyell (1830)</td>
            <td>Any rock fragments (xenoliths, clasts) included within another rock are older than the host rock.</td>
          </tr>
          <tr>
            <td><strong>Principle of Faunal Succession</strong></td>
            <td>William "Strata" Smith (1799)</td>
            <td>Fossil assemblages succeed each other vertically in a definite, non-repeating, predictable order.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Geochronology & Geological Principles</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Sedimentary Ripple Marks Interpretation</div>
        <p>A geologist discovers asymmetric ripple marks with a ripple index $RI = \text{wavelength}/\text{amplitude} = 12$ preserved in a Neoproterozoic sandstone. Using the principle of uniformitarianism, determine the depositional agent and paleocurrent direction.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In modern environments, wave oscillation produces symmetric ripples ($RI < 8-10$), whereas unidirectional aqueous or eolian currents produce asymmetric ripples with gentle stoss sides and steep lee sides ($RI \approx 8-15$ for water currents, $>15$ for eolian). Applying "the present is the key to the past", the ancient ripples were formed by <strong>unidirectional water currents</strong> flowing from the gentle stoss slope toward the steep lee slope (paleocurrent direction).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Angular Unconformity at Siccar Point</div>
        <p>Explain the historical significance of Hutton's Unconformity at Siccar Point in establishing uniformitarianism.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>At Siccar Point, steeply tilted Silurian greywackes are truncated by an erosional planar surface and overlain by gently dipping Devonian red sandstones. Hutton recognized that tilting horizontal marine muds vertically, uplifting them above sea level, eroding them subaerially, submerging them beneath a new sea, and depositing miles of new sandstone required <strong>unfathomable expanses of geological time ("Deep Time")</strong> operating through ordinary gradual processes rather than a single sudden cataclysm.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Radioactive Half-Life Invariance</div>
        <p>How does nuclear geochronology depend on methodological uniformitarianism?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Radiometric dating of rocks (e.g., U-Pb, K-Ar, Rb-Sr) is based on the radioactive decay law $N(t) = N_0 e^{-\lambda t}$. This calculation is valid if and only if the radioactive decay constant $\lambda$ (governed by the fundamental electroweak nuclear force) has remained perfectly constant over the entire $4.54\text{ billion year}$ history of the Earth, which is an application of methodological uniformitarianism.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Limitations of Strict Uniformitarianism in the Archean</div>
        <p>Why cannot modern environments be applied blindly to interpret Banded Iron Formations (BIFs) deposited in the Archean ($>2.5\text{ Ga}$)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Today's atmosphere contains $\sim 21\%$ free oxygen ($\text{O}_2$), meaning iron in surface waters oxidizes immediately to insoluble $\text{Fe}^{3+}$ (ferric iron), preventing large-scale oceanic iron transport. In the Archean, Earth had an anoxic atmosphere ($P_{\text{O}_2} < 10^{-5}\text{ PAL}$), allowing vast quantities of soluble $\text{Fe}^{2+}$ (ferrous iron) to dissolve in seawater and precipitate BIFs upon encountering localized cyanobacterial oxygen. This illustrates that while chemical laws are invariant, <strong>environmental boundary conditions evolved through time</strong>.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Cross-Cutting Relationships Age Deduction</div>
        <p>A granitic dike $D$ cuts through folded limestone $L$ and is unconformably overlain by sandstone $S$. Place these three geological units in chronological order from oldest to youngest.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol>
          <li>The folded limestone $L$ must exist prior to being folded and intruded (Oldest).</li>
          <li>The granitic dike $D$ cuts across limestone $L$; hence by the principle of cross-cutting relationships, $D$ is younger than $L$.</li>
          <li>The sandstone $S$ overlies the eroded top of both $L$ and $D$; hence by the law of superposition and unconformities, $S$ is younger than both $L$ and $D$.</li>
          <li>Chronological Order: $\mathbf{L \text{ (Oldest)}} \to \mathbf{D} \to \mathbf{S \text{ (Youngest)}}$.</li>
        </ol>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Uniformitarian Interpretation of Desiccation Mud Cracks</div>
        <p>Polygonal downward-tapering V-shaped cracks filled with silt are discovered in a shale bed. What paleoenvironmental interpretation does uniformitarianism provide?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Modern muddy floodplains and tidal flats shrink and crack into polygonal patterns during subaerial drying and solar desiccation. Applying uniformitarianism, the ancient rock was subjected to <strong>episodic subaerial exposure and drying</strong> in an intertidal, playa lake, or floodplain environment.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: William Smith's Strata Identified by Organized Fossils</div>
        <p>What fundamental empirical observation made William Smith the "Father of English Geology"?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>While surveying canal excavations across England, William Smith discovered that sedimentary strata always occurred in the same predictable sequence, and each distinct rock layer contained its own <strong>unique, diagnostic fossil assemblage ("organized fossils")</strong>, establishing the Principle of Faunal Succession which allowed correlation of strata across vast geographic distances.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Charles Lyell's Influence on Charles Darwin</div>
        <p>How did Lyell's *Principles of Geology* directly inspire Charles Darwin's theory of biological evolution by natural selection?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Darwin took Lyell's book on HMS Beagle. Lyell's uniformitarianism provided Darwin with two indispensable conceptual breakthroughs: (1) <strong>Immense geological Deep Time</strong>, providing the millions of years required for minute, gradual biological variations to accumulate into new species; and (2) The concept that <strong>ordinary, observable modern processes</strong> (such as selective breeding and competition) could explain complex historical changes without invoking supernatural creation.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 53, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q053_Uniformitarianism_Present_Key_To_Past_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q053: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q054: Spiti Valley: "The Museum of Indian Geology"
# ==============================================================================
def generate_q054():
    title = r"Q054: Tethyan Himalayan Stratigraphy: Spiti Valley as the 'Museum of Indian Geology' | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Tethyan Himalayan Geology"
    h1_title = "Q054: Spiti Valley: The 'Museum of Indian Geology'"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 54<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 328–332, p. 173); P.K. Mukherjee, <em>A Text Book of Geology</em> (World Press, Ch. 17, pp. 204–208); O.N. Bhargava & U.K. Bassi, <em>The Tethyan Himalayan Succession in Spiti</em> (Mem. GSI, Vol. 124, 1998); M.S. Krishnan, <em>Geology of India and Burma</em> (Ch. 11: The Spiti Succession)."""

    part1 = r"""
  <!-- CARD 1: WHY SPITI IS THE MUSEUM OF INDIAN GEOLOGY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Spiti Valley: The Living Laboratory of Indian Stratigraphy</div>
    <div class="card-body">
      <p>In Indian geology and global classical stratigraphy, the <strong>Spiti Valley</strong> (located in the Lahaul and Spiti district of Himachal Pradesh, northeastern Himalayas) is universally celebrated and formally designated as the <strong>“Museum of Indian Geology”</strong> (or the “Paradise of Stratigraphers”):</p>

      <ul>
        <li><strong>Continuous Marine Record:</strong> Spiti contains the most magnificent, nearly complete, uninterrupted, conformable, and richly fossiliferous marine sedimentary succession in the world, spanning over <strong>500 million years</strong> from the earliest <strong>Cambrian to the Late Cretaceous / Early Eocene</strong>.</li>
        <li><strong>Structural Preservation:</strong> Situated within the <strong>Tethyan (Tibetan) Himalayan Zone</strong> north of the Higher Himalayan Crystalline basement (Vaikrita Group), these strata were deposited along the shallow-to-deep shelf of the southern Tethys Ocean (the northern continental margin of Gondwanaland). Due to the cold, arid rain-shadow alpine climate and deep tectonic valley incision by the Spiti River, the entire sedimentary column is exposed in bare, vegetation-free rock cliffs with pristine tectonic exposure.</li>
        <li><strong>The Complete Phanerozoic Column:</strong> Unlike Peninsular India (where vast unconformities wipe out entire geological eras), Spiti displays every single geological system:
          $$\mathbf{Cambrian} \to \mathbf{Ordovician} \to \mathbf{Silurian} \to \mathbf{Devonian} \to \mathbf{Carboniferous} \to \mathbf{Permian} \to \mathbf{Triassic} \to \mathbf{Jurassic} \to \mathbf{Cretaceous}$$
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q54/mahapatra_p173_spiti_museum_of_geology.png" alt="Spiti Museum of Geology from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 54.1 (G.B. Mahapatra, p. 173):</strong> Classical textbook summary confirming the Spiti Valley as the "Museum of Indian Geology" with its complete Paleozoic-Mesozoic succession.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: SPITI STRATIGRAPHIC SUCCESSION -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Complete Stratigraphic Column of the Spiti Valley</div>
    <div class="card-body">
      <p>The standard stratigraphic succession of the Spiti Valley serves as the type reference for all Himalayan and Asian correlation:</p>

      <div class="tb-figure">
        <img src="../../figures_Q54/pkm_p205_spiti_palaeozoic_succession.png" alt="PKM Spiti Palaeozoic Succession">
        <div class="tb-caption">
          <strong>Figure 54.2 (P.K. Mukherjee, p. 205):</strong> Detailed lithostratigraphic succession of Spiti from the basal Haimanta Group to the Lilang, Kioto, and Spiti Shales.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: STRATIGRAPHIC INVENTORY OF SPITI -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Chronostratigraphic Matrix of the Spiti Valley</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Geological System</th>
            <th>Spiti Group / Formation</th>
            <th>Characteristic Lithologies</th>
            <th>Diagnostic Index Fossils</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Cretaceous</strong></td>
            <td><strong>Chikkim Formation</strong><br>Giumal Sandstone</td>
            <td>White pelagic limestones and shales; glauconitic sandstones.</td>
            <td><em>Globotruncana stuarti</em>, <em>Neohibolites</em>.</td>
          </tr>
          <tr>
            <td><strong>Jurassic</strong></td>
            <td><strong>Spiti Shales Formation</strong><br>Kioto Limestone (Lower)</td>
            <td>Black splintery ammonite-bearing nodules ("Saligram"); massive bioclastic limestones.</td>
            <td><em>Virgatosphinctes densiplicatus</em>, <em>Belemnopsis gerardi</em>, <em>Megalodon</em>.</td>
          </tr>
          <tr>
            <td><strong>Triassic</strong></td>
            <td><strong>Lilang Group</strong> (Otoceras, Meekoceras, Daonella, Tropites beds)</td>
            <td>Dark ammonoid-rich limestones and calcareous shales.</td>
            <td><em>Otoceras woodwardi</em> (GSSP marker!), <em>Meekoceras</em>, <em>Ceratites</em>.</td>
          </tr>
          <tr>
            <td><strong>Permian</strong></td>
            <td><strong>Kuling Group</strong> (Gungri & Gechang Formations)</td>
            <td>Black shales with phosphatic nodules; calcareous sandstones.</td>
            <td><em>Cyclolobus walkeri</em>, <em>Productus</em>, <em>Spiriferella rajah</em>.</td>
          </tr>
          <tr>
            <td><strong>Carboniferous</strong></td>
            <td><strong>Kanawar Group</strong> (Po & Lipak Formations)</td>
            <td>Fossiliferous dark limestones, quartzites, shales.</td>
            <td><em>Syringothyris cuspidata</em>, <em>Fenestella</em>, <em>Rhacopteris</em>.</td>
          </tr>
          <tr>
            <td><strong>Devonian</strong></td>
            <td><strong>Muth Quartzite</strong></td>
            <td>Snow-white super-mature orthoquartzites.</td>
            <td>Arthropod trace fossils: <em>Cruziana</em>, <em>Rusophycus</em>.</td>
          </tr>
          <tr>
            <td><strong>Silurian</strong></td>
            <td><strong>Takche Formation</strong> (Sanugba Group)</td>
            <td>Coralline limestones, calcareous mudstones.</td>
            <td>Tabulate corals: <em>Halysites catenularia</em>, <em>Favosites</em>.</td>
          </tr>
          <tr>
            <td><strong>Ordovician</strong></td>
            <td><strong>Shian Formation</strong></td>
            <td>Reddish-brown quartzites, conglomerates.</td>
            <td>Brachiopods: <em>Orthis</em>, solitary corals.</td>
          </tr>
          <tr>
            <td><strong>Cambrian</strong></td>
            <td><strong>Haimanta Group</strong> (Kunzum La Formation)</td>
            <td>Greenish slates, phyllites, dolomites.</td>
            <td>Trilobites: <em>Redlichia noetlingi</em>, <em>Ptychoparia</em>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 54</div>
        <div class="q-text">The ________ area is popularly known as “Museum of Indian Geology” while referring to the Geology of India.</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Spiti</div>
          <div class="opt-node">(B) Siwaliks of kashmir</div>
          <div class="opt-node">(C) Palaeozoic sucession of Kashmir</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Spiti</strong> [The Spiti Valley in Himachal Pradesh is popularly known as the 'Museum of Indian Geology' due to its continuous, richly fossiliferous marine sequence from Cambrian to Cretaceous.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Spiti</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>The <strong>Spiti Valley</strong> of Himachal Pradesh is universally referred to in Indian geological literature and standard university textbooks (Mahapatra, p. 173 & p. 330; Mukherjee, p. 205; Krishnan, Ch. 11; Wadia, Ch. 8) as the <strong>“Museum of Indian Geology”</strong>.</li>
        <li>This title is bestowed because Spiti preserves an unbroken, continuous, magnificently exposed, and richly fossiliferous marine sedimentary succession from the base of the Cambrian (Haimanta Group) all the way through the Ordovician, Silurian, Devonian, Carboniferous, Permian, Triassic, Jurassic, and Cretaceous.</li>
        <li>No other region on the Indian subcontinent displays such a complete, textbook-perfect stratigraphic record of the Tethyan realm.</li>
        <li>Therefore, Option <strong>(A) Spiti</strong> is the definitive correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Siwaliks of kashmir</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Siwalik Group</strong> represents a late Cenozoic (Middle Miocene to Early Pleistocene) terrestrial fluvial foreland basin succession, renowned for fossil mammals (e.g., <em>Sivapithecus</em>, elephants, equids).</li>
        <li>It represents only a small slice of recent geological time ($\sim 18\text{ Ma}$ to present) and is never called the "Museum of Indian Geology".</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Palaeozoic sucession of Kashmir</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>While Kashmir does have an important Paleozoic succession (including the Panjal Volcanics and Gangamopteris beds), it has massive volcanic unconformities and lacks the unbroken Mesozoic marine continuity of Spiti.</li>
        <li>The traditional textbook title "Museum of Indian Geology" belongs exclusively to Spiti.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (A) Spiti is the universally recognized canonical designation, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Classic Geographic Epithets in Indian Geology</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Geographic Region / Formation</th>
            <th>Popular Geoscientific Epithet</th>
            <th>Primary Geological Rationale</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Spiti Valley (Himachal Pradesh)</strong></td>
            <td><strong>“Museum of Indian Geology”</strong></td>
            <td>Unbroken, fully fossiliferous marine sequence from Cambrian to Cretaceous.</td>
          </tr>
          <tr>
            <td><strong>Dharwar Craton (Karnataka)</strong></td>
            <td><strong>“Cradle of Indian Precambrian Geology”</strong></td>
            <td>Ancient Archean greenstone-granite terrains, BIFs, and gold belts.</td>
          </tr>
          <tr>
            <td><strong>Siwalik Hills (Sub-Himalaya)</strong></td>
            <td><strong>“Storehouse of Cenozoic Mammalian Fossils”</strong></td>
            <td>World's most complete Neogene mammalian biostratigraphic record.</td>
          </tr>
          <tr>
            <td><strong>Deccan Traps (Western / Central India)</strong></td>
            <td><strong>“LIP of the Cretaceous-Paleogene Catastrophe”</strong></td>
            <td>Massive continental flood basalt province associated with dinosaur extinction.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Himalayan Stratigraphy & Tethyan Paleontology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Otoceras woodwardi Biozone Significance</div>
        <p>Why is the <em>Otoceras woodwardi</em> bed of the basal Lilang Group in Spiti internationally famous in global chronostratigraphy?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The ammonoid <em>Otoceras woodwardi</em> marks the earliest ammonite biozone of the Triassic Period (basal Induan Stage, Griesbachian sub-stage). In Spiti and the adjacent Guryul Ravine in Kashmir, the boundary clay underlying the <em>Otoceras</em> bed preserves the most complete marine record of the <strong>Permian-Triassic (P-Tr) mass extinction</strong> ($\sim 251.9\text{ Ma}$), recording the catastrophic wipeout of Paleozoic brachiopods and corals.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: The Sacred Saligram of the Spiti Shales</div>
        <p>What are the sacred Hindu stones known as <em>Saligrams</em> (Shaligrams) found in the Gandaki and Spiti valleys, and what fossil group do they contain?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Saligrams are rounded, black, calcareous-phosphatic concretionary nodules weathered out from the Upper Jurassic <strong>Spiti Shales Formation</strong>. When cracked open, they reveal beautifully preserved, pyritized or calcified internal molds of <strong>ammonites</strong> (specifically <em>Virgatosphinctes densiplicatus, Aulacosphinctoides, Blanfordiceras</em>) and belemnites, revered as aniconic representations of Lord Vishnu.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: The Fenestella Shales of the Kanawar Group</div>
        <p>In which Carboniferous formation of Spiti and Kashmir do we find rock beds packed with the bryozoan <em>Fenestella</em>, and what is its morphology?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In the <strong>Po Formation</strong> of Spiti (and the Fenestella Shale of Kashmir), Middle Carboniferous shales contain dense colonies of the reticulate marine bryozoan <strong><em>Fenestella plebeia</em></strong>, characterized by a delicate fan-shaped or net-like calcareous skeleton with rectangular mesh apertures bearing zooecial pores.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Kioto Limestone and Megalodon Bivalve</div>
        <p>What diagnostic thick-shelled bivalve characterizes the Late Triassic to Early Jurassic Kioto Limestone of Spiti?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The pachyodont bivalve <strong><em>Megalodon</em></strong> (accompanied by <em>Dicerocardium</em>). These massive, thick-walled heart-shaped bivalves formed extensive biostromal carbonate banks across the shallow Tethyan shelf.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Giumal Sandstone vs. Chikkim Formation</div>
        <p>Contrast the lithofacies and depositional depth of the Giumal Sandstone with the overlying Chikkim Formation in Spiti.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Giumal Sandstone (Early Cretaceous):</strong> Shallow-marine, high-energy, greenish-brown glauconitic sandstones and quartzites deposited on an inner shelf.</li>
          <li><strong>Chikkim Formation (Late Cretaceous):</strong> Deep-water, pelagic, white microcrystalline limestones and bluish calcareous shales containing planktonic foraminifera (<em>Globotruncana</em>), reflecting a major oceanic drowning transgression.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Structural Contact between Tethyan Spiti and Higher Himalaya</div>
        <p>What major extensional tectonic fault separates the Tethyan sedimentary succession of Spiti from the Higher Himalayan Crystalline basement?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>South Tibetan Detachment System (STDS)</strong>, also locally designated the Trans-Himadri Fault. This is a regional low-angle, north-dipping normal fault system along which unmetamorphosed Tethyan Paleozoic sediments slipped down to the north during Miocene gravitational collapse of the overthickened Himalayan orogen.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Kuling Group and the Permian Gondwana Cooling</div>
        <p>What brachiopod genus dominates the Permian Kuling Group in Spiti, and what paleolatitude does it indicate?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The spiriferid brachiopod <strong><em>Spiriferella rajah</em></strong> and productid <strong><em>Productus</em></strong>. These cold-water to temperate brachiopods reflect the peri-Gondwanan cold marine climate along the southern shore of the Neo-Tethys.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Earliest Trilobites of Spiti</div>
        <p>Which famous Lower Cambrian trilobite marks the Parahio River section of the Kunzum La Formation in Spiti?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The redlichiid trilobite <strong><em>Redlichia noetlingi</em></strong> (Order Redlichiida). It possesses a large semicircular cephalon, long genal spines, numerous thoracic segments with pleural spines, and a tiny pygidium, establishing early Cambrian correlation across Asia and Australia.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 54, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q054_Spiti_Valley_Museum_of_Indian_Geology_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q054: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q055: Vindhyan Supergroup: Semri, Kaimur, Rewa, and Bhander Group
# ==============================================================================
def generate_q055():
    title = r"Q055: Proterozoic Purana Basins: Vindhyan Supergroup Quadripartite Classification & Bhander Group | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Proterozoic Lithostratigraphy"
    h1_title = "Q055: Vindhyan Supergroup: Semri, Kaimur, Rewa, and Bhander"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 55<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 312–316, p. 165); P.K. Mukherjee, <em>A Text Book of Geology</em> (pp. 200–204); Ramakrishnan & Vaidyanadhan, <em>Geology of India</em> (Vol. 1, Ch. 12: Vindhyan Supergroup, pp. 315–342); M.S. Krishnan, <em>Geology of India and Burma</em> (Ch. 7)."""

    part1 = r"""
  <!-- CARD 1: VINDHYAN FOUR GROUPS -->
  <div class="card">
    <div class="card-header bg-blue">1. The Quadripartite Architecture of the Vindhyan Supergroup</div>
    <div class="card-body">
      <p>The <strong>Vindhyan Supergroup</strong> represents India's largest and most magnificent Mesoproterozoic to Neoproterozoic intracratonic sedimentary basin (spanning over $100,000\text{ km}^2$ across Central India). Established by J.B. Auden (1933) and reaffirmed by the Geological Survey of India, the Supergroup is universally divided into two primary sub-divisions and <strong>four canonical groups</strong> (in ascending chronological order):</p>

      <ul>
        <li><strong>Lower Vindhyan:</strong>
          <ul>
            <li><strong>1. Semri Group:</strong> Basal marine carbonate-volcaniclastic sequence ($\sim 1700-1600\text{ Ma}$). Comprises the Kajrahat Limestone, Porcellanite Formation (acid tuffs), Olive Shales, Fawn Limestone, and Rohtas Limestone. Rich in columnar stromatolites (<em>Collenia, Kussiella</em>) and microfossils.</li>
          </ul>
        </li>
        <li><strong>Upper Vindhyan:</strong> Dominated by mature clastics, separated from the Semri Group by a regional disconformity:
          <ul>
            <li><strong>2. Kaimur Group:</strong> Orthoquartzites, quartz arenites, and conglomerates (Dhandraul Quartzite, Scarp Sandstone, Bijaigarh Shale) recording high-energy littoral barrier regimes ($\sim 1150-1000\text{ Ma}$).</li>
            <li><strong>3. Rewa Group:</strong> Alternating shales and sandstones (Panna Shale, Asan Sandstone, Jhiri Shale, Govindgarh Sandstone). Famous for diamondiferous basal conglomerates derived from the Majhgawan pipe.</li>
            <li><strong>4. Bhander Group:</strong> The uppermost, thickest, and most widely exposed group ($\sim 900-550\text{ Ma}$). Marks the return of extensive marine carbonate and tidal flat-sabkha sedimentation.</li>
          </ul>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q55/mahapatra_p165_vindhyan_four_groups.png" alt="Vindhyan Four Groups from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 55.1 (G.B. Mahapatra, p. 165):</strong> Stratigraphic classification of the Vindhyan Supergroup showing the ascending sequence: Semri $\to$ Kaimur $\to$ Rewa $\to$ Bhander Group.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: BHANDER GROUP LITHOLOGY AND SEDIMENTOLOGY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Detailed Lithostratigraphy of the Uppermost Bhander Group</div>
    <div class="card-body">
      <p>The <strong>Bhander Group</strong> terminates the Proterozoic sedimentary history of the Great Vindhyan Basin. It is divided into four constituent formations (in ascending order):</p>

      <div class="formula-card">
        <div class="formula-title">The Ascending Formations of the Bhander Group</div>
        $$\mathbf{Ganurgarh \text{ Shale}} \longrightarrow \mathbf{Bhander \text{ Limestone}} \longrightarrow \mathbf{Sirbu \text{ Shale}} \longrightarrow \mathbf{Upper \text{ Bhander Sandstone}}$$
      </div>

      <ul>
        <li><strong>Ganurgarh Shale:</strong> Reddish-brown, thinly bedded calcareous shales with interbedded siltstones, desiccation cracks, and halite casts indicating tidal flat muds.</li>
        <li><strong>Bhander Limestone:</strong> High-grade calcitic to dolomitic limestone ($50-100\text{ m}$ thick) exhibiting spectacular domal and columnar stromatolites (<em>Baicalia, Maiharia</em>). Forms the premier raw material base for Central India's portland cement industry.</li>
        <li><strong>Sirbu Shale:</strong> Olive-green to purple gypsiferous shales and fine sandstones with abundant ripple marks, mudcracks, and hopper crystal pseudomorphs.</li>
        <li><strong>Upper Bhander Sandstone:</strong> Dark red to pinkish-buff, fine-to-medium grained quartz arenite displaying large-scale tabular cross-bedding and planar lamination, quarried across Rajasthan and MP for world-famous architectural monument stone.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q55/pkm_p202_vindhyan_supergroup_classification.png" alt="PKM Vindhyan Supergroup Classification">
        <div class="tb-caption">
          <strong>Figure 55.2 (P.K. Mukherjee, p. 202):</strong> Comprehensive table of the Vindhyan Supergroup detailing the Semri, Kaimur, Rewa, and Bhander Groups with their diagnostic sub-units.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF VINDHYAN GROUPS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Comparative Matrix of the Four Vindhyan Groups</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Group</th>
            <th>Primary Lithologies</th>
            <th>Depositional Environment</th>
            <th>Economic Mineral Products</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bhander Group</strong> (Uppermost)</td>
            <td>Red sandstones, stromatolitic limestones, shales, gypsum.</td>
            <td>Tidal flat, lagoon, supratidal sabkha.</td>
            <td><strong>Portland cement limestone, architectural building stones (Red Fort).</strong></td>
          </tr>
          <tr>
            <td><strong>Rewa Group</strong></td>
            <td>Shales, fine sandstones, conglomerates.</td>
            <td>Shallow shelf, deltaic distributaries.</td>
            <td><strong>Panna diamond conglomerates</strong>, building stones.</td>
          </tr>
          <tr>
            <td><strong>Kaimur Group</strong></td>
            <td>Orthoquartzites, quartz arenites, black shales.</td>
            <td>High-energy coastal barrier beaches, sand bars.</td>
            <td>Refractory silica stone, pyrite (Bijaigarh Shale).</td>
          </tr>
          <tr>
            <td><strong>Semri Group</strong> (Lowermost)</td>
            <td>Limestones, dolomites, bedded tuffs, glauconitic sandstones.</td>
            <td>Transgressive shallow marine carbonate platform.</td>
            <td>High-grade cement limestone (Rohtas, Kajrahat), porcellanite road ballast.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 55</div>
        <div class="q-text">The Vindhyan Supergroup is divisible into four groups viz., Semri Group, Kaimur Group, Rewa Group and</div>
        <div class="q-options">
          <div class="opt-node">(A) Bijawar group</div>
          <div class="opt-node correct">(B) Bhander group</div>
          <div class="opt-node">(C) Gwalior group</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) Bhander group</strong> [The four constituent groups of the Vindhyan Supergroup in ascending chronological order are Semri Group, Kaimur Group, Rewa Group, and Bhander Group.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) Bhander group</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>The <strong>Vindhyan Supergroup</strong> of Central India is universally subdivided across all Indian geological treatises (Auden 1933; Krishnan 1982; Ramakrishnan & Vaidyanadhan 2008; Mahapatra 2019; Mukherjee 2013) into exactly four major lithostratigraphic groups:
          <ol>
            <li><strong>Semri Group</strong> (Lower Vindhyan)</li>
            <li><strong>Kaimur Group</strong> (Upper Vindhyan)</li>
            <li><strong>Rewa Group</strong> (Upper Vindhyan)</li>
            <li><strong>Bhander Group</strong> (Upper Vindhyan)</li>
          </ol>
        </li>
        <li>The <strong>Bhander Group</strong> represents the fourth, uppermost, and youngest member of this classic quadripartite succession, celebrated for its high-grade cement limestones (Bhander Limestone) and building stones (Upper Bhander Sandstone).</li>
        <li>Thus, Option <strong>(B) Bhander group</strong> is the indisputably correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Bijawar group</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Bijawar Group</strong> is a deformed Paleoproterozoic sequence of quartzites, dolomites, ferruginous beds, and basic lavas that forms the unconformable floor (basement) beneath the Vindhyan Supergroup.</li>
        <li>The Semri Group rests with angular unconformity upon the Bijawar rocks; hence, Bijawar is an older basement unit, not a constituent of the Vindhyan Supergroup.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Gwalior group</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Gwalior Group</strong> (Par and Morar Formations) is another Paleoproterozoic sedimentary-volcanic succession exposed around Gwalior in northern Madhya Pradesh.</li>
        <li>It unconformably underlies the Kaimur Group of the Vindhyan Supergroup, making it an older basement series rather than a member of the Vindhyan Supergroup.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (B) Bhander group is the exact canonical fourth group, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Purana Basin Stratigraphic Equivalents</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Purana Basin</th>
            <th>Primary Groups / Formations</th>
            <th>Geochronological Span</th>
            <th>Key Diagnostic Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Vindhyan Supergroup</strong></td>
            <td><strong>Semri $\to$ Kaimur $\to$ Rewa $\to$ Bhander</strong></td>
            <td>$\sim 1700\text{ Ma}$ to $\sim 550\text{ Ma}$</td>
            <td>Diamondiferous conglomerates (Panna), cement limestones, Red Fort sandstones.</td>
          </tr>
          <tr>
            <td><strong>Cuddapah Supergroup</strong></td>
            <td>Papaghni $\to$ Chitravati $\to$ Nallamalai $\to$ Sanjamala</td>
            <td>$\sim 1900\text{ Ma}$ to $\sim 1000\text{ Ma}$</td>
            <td>Crescentic intracratonic basin with barites (Mangampeta) and chrysotile asbestos.</td>
          </tr>
          <tr>
            <td><strong>Kurnool Group</strong></td>
            <td>Banganapalle $\to$ Narji $\to$ Owk $\to$ Paniam $\to$ Koilkuntla $\to$ Nandyal</td>
            <td>$\sim 1000\text{ Ma}$ to $\sim 600\text{ Ma}$</td>
            <td>Unconformably overlies Cuddapah; diamond conglomerate and Narji limestone.</td>
          </tr>
          <tr>
            <td><strong>Kaladgi / Bhima Groups</strong></td>
            <td>Lokapur & Mudhol (Kaladgi); Rabanpalli & Shahabad (Bhima)</td>
            <td>Mesoproterozoic - Neoproterozoic</td>
            <td>Flaggy ornamental limestone (Shahabad Stone) and unconformity-type uranium.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Vindhyan Stratigraphy & Sedimentary Petrology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Stromatolite Biostratigraphy of Bhander Limestone</div>
        <p>Which branching columnar stromatolite taxon characterizes the Neoproterozoic Bhander Limestone and correlates it with the Riphean of Russia?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Bhander Limestone is characterized by the branching columnar stromatolite <strong><em>Baicalia baicalica</em></strong> and <strong><em>Maiharia maiharensis</em></strong>. In Riphean biostratigraphy, <em>Baicalia</em> is the diagnostic index form for the <strong>Middle to Upper Riphean</strong> ($\sim 1000-700\text{ Ma}$), establishing global biostratigraphic correlation for the Bhander Group.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Halite Pseudomorphs as Evaporite Indicators</div>
        <p>Explain the step-by-step mechanism of hopper-crystal halite pseudomorph formation in the Sirbu Shale.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol>
          <li>Under hyper-saline, arid conditions on supratidal sabkha mudflats, brine evaporates, precipitating skeletal cubic "hopper" crystals of halite ($\text{NaCl}$) within the soft mud.</li>
          <li>During episodic marine flooding or rainstorms, less saline water dissolves the soluble halite crystal, leaving a hollow cubic mold in the mud.</li>
          <li>Inflowing silt or mud deposits immediately fill the cavity, casting a perfect cubic pseudomorph preserved on shale bedding planes.</li>
        </ol>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Architectural Durability of the Upper Bhander Sandstone</div>
        <p>Why has the Upper Bhander Sandstone survived centuries of environmental exposure in Mughal monuments (e.g., Red Fort, Fatehpur Sikri) without crumbling?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Upper Bhander Sandstone is a super-mature <strong>quartz arenite</strong> consisting of $>95\%$ monocrystalline quartz grains bonded by syntaxial <strong>silica cement</strong> in optical continuity with the host grains (secondary quartz overgrowths), with a microscopic coating of hematite providing the warm red color. The absence of unstable feldspars and soluble carbonate cements renders it virtually impervious to chemical weathering and acid rain.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: The Great Eparchean Hiatus at the Base of the Semri</div>
        <p>The basal conglomerate of the Semri Group rests upon the Bundelkhand Granite ($\sim 2500\text{ Ma}$). What is the duration of the missing geological time interval represented by this unconformity if the Semri initiated at $\sim 1700\text{ Ma}$?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\text{Hiatus} = 2500\text{ Ma} - 1700\text{ Ma} = 800\text{ Ma}$$
        <p><strong>Final Answer:</strong> The basal nonconformity represents an enormous erosional hiatus of approximately $800\text{ million years}$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Carbon Isotope Excursion ($\delta^{13}\text{C}$) in the Bhander Limestone</div>
        <p>Modern chemostratigraphy shows that the Bhander Limestone exhibits strongly positive carbon isotope ratios ($\delta^{13}\text{C} \approx +4.0\text{ to } +6.0\text{ \textperthousand}$). What global biogeochemical condition does this indicate?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>High positive $\delta^{13}\text{C}_{\text{carb}}$ values indicate high global rates of organic carbon burial in anoxic sediments (preferentially sequestering light $^{12}\text{C}$ into buried biomass, leaving the ocean reservoir enriched in heavy $^{13}\text{C}$). This massive burial of organic carbon corresponds to the Neoproterozoic oxygenation event preceding the radiation of multicellular life.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Origin of Porcellanite in the Semri Group</div>
        <p>What is the petrogenetic origin of the banded "porcellanite" beds in the Semri Group?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Porcellanites are dense, chert-like, microcrystalline silicified rocks that formed by the devitrification and diagenetic alteration of airborne <strong>felsic volcanic ash and rhyolitic tuffs</strong> deposited in a shallow marine basin during syn-sedimentary Paleoproterozoic volcanism.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Great Boundary Fault Juxtaposition</div>
        <p>Along the northwestern margin of the Vindhyan basin in Rajasthan, which specific Vindhyan group is brought into direct thrust contact against pre-Vindhyan schists by the Great Boundary Fault?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>Bhander Group</strong> (specifically the Upper Bhander Sandstone and Sirbu Shale) is folded into steep marginal synclines and faulted directly against the Aravalli-Bhilwara metamorphic basement by the Great Boundary Fault.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Modern Terminal Age of the Vindhyans</div>
        <p>Recent discoveries of Ediacaran trace fossils and discs in the Bhander Group place the terminal sedimentation close to which global chronostratigraphic boundary?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The uppermost Bhander Group extends to approximately $540-550\text{ Ma}$, placing the cessation of Vindhyan sedimentation immediately at the <strong>Ediacaran-Cambrian boundary</strong> (the Precambrian-Cambrian transition).</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 55, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q055_Vindhyan_Supergroup_Bhander_Group_Classification_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q055: {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    generate_q051()
    generate_q052()
    generate_q053()
    generate_q054()
    generate_q055()
