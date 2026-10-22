#!/usr/bin/env python3
"""
Masterclass Builder for Q008, Q009, and Q010
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q008: Trellis Drainage Pattern
# ==============================================================================
def generate_q008():
    title = "Q008: Trellis Drainage Pattern & Strike-Dip Structural Control | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geomorphology & Structural Drainage"
    h1_title = "Q008: Trellis Drainage Pattern & Strike-Dip Structural Control"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 8<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 2: Work of Rivers, pp. 60–63, Fig. 2.15); Zernitz, E.R. (1932, <em>Drainage Patterns and Their Significance</em>, Jour. Geology, 40, pp. 498–521); Howard, A.D. (1967, <em>AAPG Bulletin</em>, 51, pp. 2246–2259); Thornbury, W.D. (1969, <em>Principles of Geomorphology</em>)."""

    part1 = r"""
  <!-- CARD 1: GENETIC STREAM TYPES & STRUCTURAL CONTROL -->
  <div class="card">
    <div class="card-header bg-blue">1. Genetic Stream Systematics & Structural Guidance</div>
    <div class="card-body">
      <p>The geometric layout of a river network—its <strong>drainage pattern</strong>—is primarily governed by regional rock structure, varying lithological hardness, joint/fault fracture networks, and tectonic slope. In genetic fluvial geomorphology (W.M. Davis, 1899; Zernitz, 1932), streams within a drainage basin are genetically categorized relative to structural strike and dip:</p>

      <ul>
        <li><strong>Consequent Streams:</strong> Initial streams whose flow course is directly determined by the original slope or tilt of a newly uplifted land surface.</li>
        <li><strong>Subsequent Streams:</strong> Streams that develop along lines of structural weakness, specifically excavating linear master strike valleys into belts of easily erodible, soft sedimentary formations (such as shale, slate, or soft marl) parallel to structural strike.</li>
        <li><strong>Resequent Streams:</strong> Tributary streams that flow down the regional structural dip slope in the same direction as original consequent streams, joining master subsequent streams at right angles ($90^\circ$).</li>
        <li><strong>Obsequent Streams:</strong> Short, steep tributary streams flowing down the escarpment (scarp slope) in the direction opposite to the regional structural dip, emptying orthogonally into subsequent strike streams.</li>
      </ul>

      <div class="quote-box bangar">
        "Trellis Pattern: In this type of drainage pattern, the master streams and their tributaries follow a system of mutually perpendicular or nearly right-angled courses. The master streams flow parallel to the regional strike of the beds (in soft rock belts), while short tributaries flow down the dip and anti-dip slopes, joining the main stream at right angles. It resembles a vine on a garden trellis and is typical of folded sedimentary belts."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 2: Geological Work of Rivers, pp. 61–62, Fig. 2.15)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q08/bangar_fig2_15_trellis_drainage.png" alt="Trellis Drainage from Bangar">
        <div class="tb-caption">
          <strong>Figure 8.1 (K.M. Bangar, Fig. 2.15):</strong> Authentic textbook illustration of a Trellis Drainage Pattern developed across tilted and folded sedimentary strata, showing subsequent master streams along strike vales fed orthogonally by dip and scarp tributaries.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MORPHOLOGY OF THE TRELLIS PATTERN -->
  <div class="card">
    <div class="card-header bg-indigo">2. Geometric Architecture: Strike Valleys and Orthogonal Intersections</div>
    <div class="card-body">
      <p>When alternating resistant formations (quartzite, sandstone, limestone) and incompetent formations (shale, mudstone) are folded into synclines and anticlines or tilted into homoclinal ridges, differential erosion carves a series of parallel ridges and valleys:</p>

      <ul>
        <li><strong>Master Strike Streams:</strong> Long, prominent subsequent rivers occupy the soft-rock strike vales, running strictly parallel to one another along the regional strike line of the formations.</li>
        <li><strong>Orthogonal Dip & Scarp Tributaries:</strong> Short, parallel tributaries flow down the resistant dip slopes (resequent streams) and steep scarp faces (obsequent streams), intersecting the master strike streams at near-perfect <strong>right angles ($90^\circ$)</strong>.</li>
        <li><strong>Water Gaps & Wind Gaps:</strong> Where transverse master rivers carve narrow gorges directly across resistant quartzite strike ridges, they form <em>water gaps</em>. If headward erosion and stream piracy divert the river into an adjacent strike valley, the dry, abandoned notch through the ridge is termed a <em>wind gap</em>.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q08/trellis_drainage_pattern.png" alt="Trellis Drainage Pattern 3D Schematic">
        <div class="tb-caption">
          <strong>Figure 8.2: 3D Geologic Block Diagram of Trellis Drainage.</strong> Illustrates alternating resistant sandstone ridges and weak shale vales controlling subsequent strike drainage with orthogonal dip-fed tributaries.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: DISCRIMINATION FROM OTHER PATTERNS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Diagnostic Discrimination: Trellis vs. Rectangular vs. Parallel vs. Dendritic</div>
    <div class="card-body">
      <p>Candidates must clearly differentiate trellis drainage from other geometric network patterns:</p>

      <ul>
        <li><strong>Rectangular Pattern:</strong> Characterized by sharp $90^\circ$ bends and right-angled junctions, but <em>controlled by intersecting joint systems and faults</em> in homogeneous crystalline rocks (e.g., jointed granites, basalts) or flat-lying sedimentary beds. It lacks parallel strike ridges and soft-rock vales.</li>
        <li><strong>Parallel Pattern:</strong> Characterized by straight, parallel streams running down uniform, steep regional slopes (e.g., young volcanic slopes, tilted coastal plains, or steep fault scarps). It lacks right-angled orthogonal tributaries.</li>
        <li><strong>Dendritic Pattern:</strong> Irregular, treelike branching with tributaries joining at acute angles ($< 90^\circ$), characteristic of structurally isotropic, homogeneous rocks or horizontally undeformed strata lacking directional control.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 8)</div>
    <div class="q-stmt">
      Q8. If a network of parallel streams is developed along strike and dip of the formations, the drainage pattern is referred to as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Parallel</div>
      <div class="raw-opt">(B) Rectangular</div>
      <div class="raw-opt correct">(C) Trellis &nbsp;✔</div>
      <div class="raw-opt">(D) Dendritic</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Trellis</div>
      <div class="sub">
        A drainage pattern wherein master subsequent streams flow parallel to one another along the <strong>strike</strong> of incompetent beds and are joined orthogonally by short tributaries flowing down the <strong>dip</strong> and scarp slopes is universally designated a <strong>Trellis Drainage Pattern</strong> (Bangar, p. 61; Zernitz, 1932).
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Parallel</span>
      <span class="tag wrong">Incorrect (Steep Slope Controlled, Lacks Strike-Dip Orthogonality)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A parallel drainage pattern develops on steep, elongated, uniformly dipping regional slopes or coastal plains. All streams flow in the same direction down the regional gradient without developing an orthogonal strike-and-dip tributary network.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Rectangular</span>
      <span class="tag wrong">Incorrect (Controlled by Joint/Fault Networks, Not Strike-Dip Formations)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> While rectangular drainage also exhibits right-angled bends and tributary junctions, it is structurally controlled by intersecting orthogonal joint sets, cleavage fractures, or fault lines in homogeneous crystalline rocks (granites, basalts) or horizontal strata. It lacks parallel strike vales and dipping homoclinal ridges.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Trellis</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By standard geological definition, the trellis pattern is defined specifically by parallel master streams aligned along the strike of soft formations, intersected at right angles by short tributaries flowing down the structural dip and anti-dip slopes of resistant homoclinal ridges. It is the diagnostic fingerprint of folded sedimentary terranes (e.g., the Appalachian Valley and Ridge, Cuddapah Basin).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Dendritic</span>
      <span class="tag wrong">Incorrect (Irregular Insequent Branching in Isotropic Rocks)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Dendritic drainage resembles the branching veins of a leaf or tree roots, with tributaries joining at acute angles ($< 90^\circ$). It develops in structurally isotropic, homogeneous rocks or flat horizontal beds where geology exerts no directional control over stream orientation.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Classification Matrix: Geologic Drainage Patterns</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Drainage Pattern</th>
            <th>Geometric Geometry</th>
            <th>Structural & Lithological Control</th>
            <th>Type Indian / Global Field Terrane</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Trellis</strong></td>
            <td>Parallel master streams along strike with orthogonal ($90^\circ$) dip/scarp tributaries</td>
            <td>Folded or tilted sedimentary beds with alternating resistant/soft layers</td>
            <td>Appalachian Valley & Ridge (USA); Cuddapah Basin (Andhra Pradesh)</td>
          </tr>
          <tr>
            <td><strong>Rectangular</strong></td>
            <td>Right-angled junctions and sharp bends without long parallel strike ridges</td>
            <td>Intersecting orthogonal joint systems or fault lines in massive rocks</td>
            <td>Jointed Bundelkhand Granite (MP/UP); Norwegian fjord bedrock valleys</td>
          </tr>
          <tr>
            <td><strong>Parallel</strong></td>
            <td>Elongated, uniformly spaced parallel channels running down-slope</td>
            <td>Steep, uniform regional slopes or narrow coastal ramps</td>
            <td>Western Ghats coastal plain (Konkan); young strato-volcano flanks</td>
          </tr>
          <tr>
            <td><strong>Dendritic</strong></td>
            <td>Tree-like branching with tributaries joining master streams at acute angles</td>
            <td>Massive homogeneous crystalline rocks or horizontal sedimentary strata</td>
            <td>Deccan Volcanic Province (Maharashtra); Indo-Gangetic Alluvial Plain</td>
          </tr>
          <tr>
            <td><strong>Radial</strong></td>
            <td>Streams radiating outward like spokes of a wheel from a central elevated apex</td>
            <td>Volcanic cones, structural domes, isolated mountain massifs</td>
            <td>Mount Girnar (Gujarat); Dalma Volcanics (Jharkhand)</td>
          </tr>
          <tr>
            <td><strong>Centripetal</strong></td>
            <td>Streams flowing inward from all directions toward a central depression</td>
            <td>Inland drainage basins, sinkholes (dolines), calderas, structural basins</td>
            <td>Lonar Crater (Maharashtra); Tibetan endorheic lake basins</td>
          </tr>
          <tr>
            <td><strong>Annular</strong></td>
            <td>Concentric circular paths tracing ring-like soft rock belts</td>
            <td>Breached structural domes with alternating resistant and weak concentric rings</td>
            <td>Black Hills dome (South Dakota, USA); Ramgarh Crater dome (Rajasthan)</td>
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
          <strong>Practice Q1:</strong> What is the genetic classification of a tributary that flows down the steep escarpment face in a direction directly opposite to the regional structural dip?
          <div class="pq-ans">✔ Correct Answer: Obsequent stream.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Consequent and resequent streams flow in the direction of structural dip; obsequent streams flow down the scarp face opposite to dip, discharging into the subsequent strike stream.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> Describe the mechanism of <em>stream piracy (river capture)</em> in a trellis drainage network.
          <div class="pq-ans">✔ Correct Answer: A vigorous subsequent strike stream working headward in soft shale breaches a drainage divide and diverts a transverse consequent stream.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Rapid headward erosion along soft shale belts allows subsequent streams to intersect and capture transverse streams that are slowed down by cutting across hard quartzite ridges.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What field diagnostic distinguishes an active <em>water gap</em> from an abandoned <em>wind gap</em> in folded mountain belts?
          <div class="pq-ans">✔ Correct Answer: A water gap carries an active transverse river; a wind gap is a dry, elevated notch through a ridge containing river gravels but no running stream.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Wind gaps are former water gaps abandoned after stream piracy diverted the river upstream, leaving rounded fluvial gravels stranded high above the valley floor.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Horton-Strahler stream ordering, what is the typical <em>Bifurcation Ratio ($R_b = N_u / N_{u+1}$)</em> for a dendritic network versus a trellis network?
          <div class="pq-ans">✔ Correct Answer: Dendritic basins typically yield $R_b \approx 3.0 - 5.0$; elongated trellis basins in folded belts often show anomalously high $R_b > 5.0 - 10.0$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Trellis networks restrict lateral expansion, forcing dozens of short first-order streams to feed directly into a long master subsequent channel, inflating $R_b$.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How does an <em>antecedent stream</em> maintain its course across a newly rising anticlinal ridge in a trellis belt?
          <div class="pq-ans">✔ Correct Answer: The river's downcutting rate equals or exceeds the rate of tectonic fold uplift, incising a narrow transverse antecedent gorge.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Antecedent streams predate the folding and maintain their original transverse path across the rising ridges (e.g., Indus, Brahmaputra, and Sutlej cutting across the rising Himalayas).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What drainage pattern develops on a deeply eroded circular structural salt dome or breached granite dome?
          <div class="pq-ans">✔ Correct Answer: Annular drainage pattern.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Circular upturned sedimentary layers create concentric rings of hard and soft rock; subsequent streams trace circular concentric rings joined radially by short tributaries.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> A <em>superimposed stream</em> is defined as:
          <div class="pq-ans">✔ Correct Answer: A stream whose drainage course was established on an overlying unconformable cover, which then incised vertically into older discordant structural rocks below.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Superimposition explains why rivers sometimes cut bizarre transverse gorges through buried folded mountain ranges without structural regard to the buried folds (e.g., Subarnarekha River in the Singhbhum shear zone).
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> A <em>deranged</em> or disordered drainage pattern with erratic wandering channels and abundant lakes/swamps is diagnostic of which geologic history?
          <div class="pq-ans">✔ Correct Answer: Recently glaciated continental shield terranes (Pleistocene ice sheet ablation).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Glacial erosion and morainic dumping completely disrupt pre-existing fluvial systems, creating irregular lakes, swamps, and aimlessly wandering streams (e.g., Canadian Shield and Finland).
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 8, part1, part2, part3)


# ==============================================================================
# Q009: Fanglomerate Lithification
# ==============================================================================
def generate_q009():
    title = "Q009: Fanglomerate: Alluvial Fan Petrography & Lawson's Lithification Paradigm | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Conglomerates"
    h1_title = "Q009: Fanglomerate: Alluvial Fan Petrography & Lawson's Lithification Paradigm"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 9<br>
<strong>Authoritative References:</strong> Andrew C. Lawson (1913, <em>The Petrographic Designation of Alluvial Fan Deposits</em>, Univ. Calif. Publ. Bull. Dept. Geol., 7, pp. 325–334); Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Ch. 5, pp. 138–142 & Ch. 8, pp. 243–248); F.J. Pettijohn, <em>Sedimentary Rocks</em> (3rd Ed., pp. 165–172); K.M. Bangar, <em>Principles of Engineering Geology</em> (pp. 48–51, 142–144)."""

    part1 = r"""
  <!-- CARD 1: LAWSON'S 1913 PETROGRAPHIC DESIGNATION -->
  <div class="card">
    <div class="card-header bg-blue">1. Historical Petrogenesis: Lawson's (1913) Coining of "Fanglomerate"</div>
    <div class="card-body">
      <p>In 1913, the renowned Scottish-American geologist Andrew Cowper Lawson published a landmark paper in the <em>University of California Publications Bulletin of the Department of Geology</em> entitled <strong>"The Petrographic Designation of Alluvial Fan Deposits"</strong>. Lawson recognized that while unconsolidated alluvial fan gravels are common in arid and semi-arid intramontane basins (such as the Great Basin of Nevada and California), sedimentary petrology lacked a dedicated lithologic rock name for their indurated, lithified ancient equivalents:</p>

      <div class="quote-box">
        "For the consolidated deposits of alluvial fans... the term 'fanglomerate' is here proposed. The rock is a distinct petrographic species, possessing characteristics which separate it from ordinary water-worn conglomerates on the one hand and from volcanic or fault breccias on the other."
        <span class="quote-ref">— Andrew C. Lawson, <em>The Petrographic Designation of Alluvial Fan Deposits</em> (Univ. Calif. Publ. Bull. Dept. Geol., 1913, Vol. 7, No. 15, p. 329)</span>
      </div>

      <p>Lawson defined <strong>Fanglomerate</strong> as the sedimentary rock formed by the lithification and induration of coarse, poorly sorted, angular to subrounded gravels, boulders, and sand-matrix debris flows deposited upon an <strong>alluvial fan</strong>.</p>

      <div class="tb-figure">
        <img src="../../figures_Q09/boggs_fig8_4_fanglomerate_model.png" alt="Fanglomerate Sedimentary Model from Sam Boggs Jr.">
        <div class="tb-caption">
          <strong>Figure 9.1 (Sam Boggs Jr., 5th Ed., Fig. 8.4):</strong> Depositional architecture and facies spectrum of an alluvial fan yielding consolidated fanglomerates. Shows proximal debris-flow diamictites grading into medial braided sheetflood sandstones and distal playa silts.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: PETROLOGICAL CHARACTERISTICS OF FANGLOMERATES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Petrology: Paraconglomerates, Textural Immaturity & Diagenesis</div>
    <div class="card-body">
      <p>Petrologically, fanglomerates are characterized by extreme textural and mineralogical immaturity reflecting rapid deposition adjacent to mountainous fault scarps:</p>

      <ul>
        <li><strong>Matrix-Supported Diamictites (Paraconglomerates):</strong> In proximal and medial fan facies, episodic cohesive debris flows deposit unstratified, chaotic beds where coarse boulders ($> 1\text{ meter}$) float in a muddy, sandy matrix ($> 15 - 50\%$ matrix), forming authentic <em>paraconglomerates</em>.</li>
        <li><strong>Clast-Supported Orthoconglomerates:</strong> Medial and distal braided channel and sheetflood facies deposit clast-supported gravel sheets ($< 15\%$ matrix) with distinct $a(\text{p})b(\text{i})$ pebble imbrication dipping up-fan toward the mountain source.</li>
        <li><strong>Polymictic / Petromict Lithologies:</strong> Fanglomerates contain heterogeneous assortments of unstable sedimentary, metamorphic, and igneous rock fragments reflecting the unroofing history of the adjacent mountain block.</li>
        <li><strong>Diagenetic Cementation:</strong> In arid and semi-arid basins, early diagenesis is driven by evaporative pore fluids depositing calcium carbonate (caliche / calcrete) or amorphous silica (silcrete) cements, rapidly converting loose gravels into indurated rock.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q09/alluvial_fan_fanglomerate_facies.png" alt="Alluvial Fan Fanglomerate Facies Architecture">
        <div class="tb-caption">
          <strong>Figure 9.2: Alluvial Fan Facies & Fanglomerate Lithification.</strong> Conceptual model showing debris-flow paraconglomerate beds interbedded with sheetflood sandstone lenses.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: FORENSIC DISCRIMINATION FROM DISTRACTORS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Forensic Dissection: Why Bajada, Agglomerate & Orthoconglomerate Fail</div>
    <div class="card-body">
      <p>To master this question, candidates must clearly separate geomorphic landform terms from igneous and textural classifications:</p>

      <ul>
        <li><strong>Bajada (Geomorphic Landform):</strong> A continuous, undulating piedmont alluvial plain produced by the lateral coalescence and overlapping of multiple adjacent alluvial fans along a mountain front. A bajada is a <strong>topographic landform</strong>, not a lithified petrographic rock name.</li>
        <li><strong>Agglomerate (Pyroclastic Igneous Rock):</strong> A coarse-grained, chaotic volcanic rock composed predominantly of consolidated, rounded to subangular volcanic bombs ($> 64\text{ mm}$) ejected during explosive volcanic eruptions. It has zero relation to alluvial fans.</li>
        <li><strong>Orthoconglomerate (Broad Textural Class):</strong> A purely textural classification term for any conglomerate containing less than $15\%$ matrix (grain-supported). While some fluvial stream gravels are orthoconglomerates, many alluvial fan beds are matrix-rich paraconglomerates; hence, orthoconglomerate is not specific to alluvial fans.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 9)</div>
    <div class="q-stmt">
      Q9. The lithified portions of alluvial fans are termed as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Bajada</div>
      <div class="raw-opt">(B) Agglomerate</div>
      <div class="raw-opt correct">(C) Fanglomerate &nbsp;✔</div>
      <div class="raw-opt">(D) Orthoconglomerate</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (C) Fanglomerate</div>
      <div class="sub">
        The consolidated, indurated petrographic equivalent of an alluvial fan deposit is specifically termed a <strong>Fanglomerate</strong>, coined by Andrew C. Lawson in 1913. A bajada is an unconsolidated geomorphic landform; an agglomerate is a pyroclastic volcanic rock; and an orthoconglomerate is a generic textural category.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Bajada</span>
      <span class="tag wrong">Incorrect (Geomorphological Landform, Not a Lithified Rock)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A bajada (or piedmont apron) is a <em>geomorphological landscape feature</em> formed when neighboring alluvial fans coalesce along a mountain piedmont. It describes modern unconsolidated topography, not a lithified rock unit.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Agglomerate</span>
      <span class="tag wrong">Incorrect (Coarse Pyroclastic Volcanic Rock)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Agglomerate is an igneous pyroclastic rock consisting of consolidated volcanic bombs and coarse ejected pyroclasts ($> 64\text{ mm}$) shaped in the air during volcanic eruptions. It is entirely unrelated to sedimentary alluvial fans.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Fanglomerate</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> Coined specifically by A.C. Lawson (1913) for the consolidated, lithified rock equivalents of alluvial fan deposits, <strong>fanglomerate</strong> is the exact, standard petrological term recognized in all international dictionaries of geology and standard sedimentology treatises (Boggs, Pettijohn, Bangar).
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Orthoconglomerate</span>
      <span class="tag wrong">Incorrect (Generic Textural Clast-Supported Category)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> Orthoconglomerate refers strictly to any conglomerate with a clast-supported framework ($< 15\%$ matrix), such as beach gravels or braided river channel gravels. Alluvial fans contain substantial matrix-supported debris-flow deposits (paraconglomerates); hence, orthoconglomerate is neither diagnostic of nor synonymous with alluvial fan rocks.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Diagnostic Matrix: Rudaceous Rocks & Alluvial Terms</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Geological Term</th>
            <th>Scientific Nature</th>
            <th>Genetic Environment</th>
            <th>Essential Composition & Texture</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fanglomerate</strong></td>
            <td><strong>Sedimentary Rock</strong></td>
            <td><strong>Lithified Alluvial Fan</strong> (coined by A.C. Lawson, 1913)</td>
            <td>Poorly sorted, subangular to rounded boulders/gravels; petromict; calcrete-cemented</td>
          </tr>
          <tr>
            <td><strong>Bajada</strong></td>
            <td><strong>Geomorphic Landform</strong></td>
            <td>Piedmont alluvial coalescence along mountain front</td>
            <td>Unconsolidated, apron-like coalescing alluvial fan surfaces</td>
          </tr>
          <tr>
            <td><strong>Agglomerate</strong></td>
            <td><strong>Pyroclastic Igneous Rock</strong></td>
            <td>Explosive volcanic vent / crater facies</td>
            <td>Consolidated volcanic bombs ($> 64\text{ mm}$); basaltic, andesitic, or rhyolitic scoria</td>
          </tr>
          <tr>
            <td><strong>Orthoconglomerate</strong></td>
            <td>Textural Rock Class</td>
            <td>High-energy fluvial channels, wave-dominated marine beaches</td>
            <td>Clast-supported ($< 15\%$ matrix); clast-to-clast framework contact</td>
          </tr>
          <tr>
            <td><strong>Paraconglomerate (Diamictite)</strong></td>
            <td>Textural Rock Class</td>
            <td>Subaerial debris flows, subaqueous slumps, glacial tillites</td>
            <td>Matrix-supported ($> 15 - 50\%$ matrix); clasts floating chaotically</td>
          </tr>
          <tr>
            <td><strong>Tillite</strong></td>
            <td>Sedimentary Rock</td>
            <td>Lithified glacial till (morainic deposit)</td>
            <td>Unsorted, unstratified diamictite with striated, polished, faceted clasts</td>
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
          <strong>Practice Q1:</strong> In which classic American geological province did Andrew C. Lawson first define and name fanglomerates in 1913?
          <div class="pq-ans">✔ Correct Answer: The Basin and Range Province (specifically the arid intermontane basins of California and Nevada).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Lawson investigated fault-bounded grabens bordered by steep fault-line scarps where alluvial fans aggraded rapidly under arid conditions, preserving thick fanglomerate sequences.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>sieve deposit</em> on an alluvial fan, and what rock type does it form upon lithification?
          <div class="pq-ans">✔ Correct Answer: Highly permeable gravel sheets devoid of mud formed when water infiltrates instantly through coarse debris, forming clean orthoconglomerates.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Where source rocks produce coarse, mud-free rock debris (e.g., quartzites), flood waters sink rapidly through the permeable gravels, stranding clean, open-framework gravel sheets known as sieve lobes.
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What clast fabric (imbrication) is characteristic of water-laid sheetflood conglomerates in contrast to debris-flow deposits?
          <div class="pq-ans">✔ Correct Answer: $a(\text{p})b(\text{i})$ imbrication, where flatter $ab$ planes dip upstream (up-fan) against the flow.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Water currents orient discoid pebbles with their longest axes transverse to flow ($b$-axis) and flat planes dipping into the current ($a$-plane). Cohesive debris flows lack organized imbrication, exhibiting random or vertical clast orientations.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In Indian stratigraphy, the famous Neogene-Quaternary Upper Siwalik <em>Boulder Conglomerate Formation</em> is a lithified archetype of which depositional system?
          <div class="pq-ans">✔ Correct Answer: Giant coalescing alluvial fan and fanglomerate aprons shed from the rising Main Boundary Thrust (MBT) of the Himalayas.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The Upper Siwalik Boulder Conglomerates represent coarse orogenic fanglomerates prograding southwards into the foreland basin during Pleistocene Himalayan orogenic pulses.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> What is the diagnostic petrographic difference between an <em>oligomictic</em> conglomerate and a <em>petromict (polymictic)</em> fanglomerate?
          <div class="pq-ans">✔ Correct Answer: Oligomictic conglomerates contain clasts of a single resistant rock type (e.g., $> 90\%$ vein quartz or chert); petromict fanglomerates contain unstable, multi-lithology rock fragments (granites, basalts, schists, shales).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because alluvial fans form adjacent to unroofed mountain scarps without long-distance transport, unstable rock clasts are preserved without chemical weathering.
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What pedogenic cement is most commonly responsible for the early induration and lithification of Quaternary arid alluvial fans into fanglomerates?
          <div class="pq-ans">✔ Correct Answer: Calcrete (caliche / pedogenic calcium carbonate $\text{CaCO}_3$).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> In arid and semi-arid climates, intense seasonal evaporation of groundwater draws bicarbonate-rich water toward the surface, precipitating micritic and sparry calcite that welds loose gravels into hard rock.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> How do tectonic normal faults along a rift basin margin control the vertical stratigraphic stacking of fanglomerates?
          <div class="pq-ans">✔ Correct Answer: Repeated fault slip creates recurring accommodation space, generating stacked, multistory coarsening-upward fanglomerate wedges.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Each episodic faulting event rejuvenates relief, dumping coarse proximal debris directly over finer distal fan or lacustrine facies.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> Why is an <em>intraformational conglomerate</em> distinct from a fanglomerate?
          <div class="pq-ans">✔ Correct Answer: Intraformational conglomerates contain clasts derived from within the same depositional basin (e.g., ripped-up shale rip-up clasts); fanglomerates contain extraformational clasts eroded from an external mountainous source.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Intraformational clasts are penecontemporaneous mud-flakes eroded by energetic currents within the basin, whereas fanglomerates are classic extraformational rudites.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 9, part1, part2, part3)


# ==============================================================================
# Q010: Hogback vs Cuesta
# ==============================================================================
def generate_q010():
    title = "Q010: Structural Landforms: Hogback vs. Cuesta & Dip Slope Symmetries | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geomorphology & Ridge Forms"
    h1_title = "Q010: Structural Landforms: Hogback vs. Cuesta & Dip Slope Symmetries"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 10<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Structural Geology, pp. 195–198, Fig. 7.51); Thornbury, W.D. (1969, <em>Principles of Geomorphology</em>, Ch. 6, pp. 132–136); Bloom, A.L. (1998, <em>Geomorphology: A Systematic Analysis</em>); Ritter, Kochel & Miller (2011, <em>Process Geomorphology</em>)."""

    part1 = r"""
  <!-- CARD 1: THE HOMOCLINAL RIDGE CONTINUUM -->
  <div class="card">
    <div class="card-header bg-blue">1. The Homoclinal Ridge Continuum: Dip Angle ($\theta$) Control</div>
    <div class="card-body">
      <p>In structural geomorphology, when alternating resistant rock layers (such as quartzitic sandstone, well-cemented conglomerate, or basalt sills) and non-resistant layers (shale, slate, or marl) are tilted by tectonic deformation, differential weathering and stream erosion produce distinct linear structural ridges known as <strong>Homoclinal Ridges</strong>. The morphology, cross-sectional symmetry, and flank inclinations of these ridges are strictly governed by the <strong>angle of true dip ($\theta$)</strong> of the resistant rock strata:</p>

      <ul>
        <li><strong>Cuesta ($\theta < 15^\circ - 20^\circ$):</strong> Highly asymmetrical ridge with a long, gentle dip slope matching bed dip and an abrupt, steep scarp slope.</li>
        <li><strong>Hogback ($\theta > 30^\circ - 45^\circ$):</strong> Narrow, symmetrical knife-edge ridge where both flanks (dip slope and scarp slope) exhibit <strong>steep slopes of nearly equal inclination</strong>.</li>
        <li><strong>Mesa & Butte ($\theta \approx 0^\circ$):</strong> Flat-topped horizontal plateaus bounded on all sides by steep escarpments.</li>
      </ul>

      <div class="quote-box bangar">
        "Cuesta and Hogback: Where gently dipping strata of alternating hard and soft rocks are subjected to erosion, an asymmetrical ridge called a cuesta is formed. It has a gentle slope on one side (dip slope) and a steep slope on the other (scarp slope). If the dip of the beds is very steep (greater than 30° to 45°), the two slopes become nearly equal in inclination. Such a sharp, symmetrical ridge is called a Hogback."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Structural Geology, pp. 196–197, Fig. 7.51)</span>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q10/bangar_fig7_51_cuesta_hogback.png" alt="Cuesta and Hogback Cross Section from Bangar">
        <div class="tb-caption">
          <strong>Figure 10.1 (K.M. Bangar, Fig. 7.51):</strong> Classical cross-sectional profiles of (A) Cuesta with gentle dip slope and steep scarp, and (B) Hogback with steeply dipping beds producing near-equal slope angles on both flanks.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MORPHODYNAMICS OF THE HOGBACK RIDGE -->
  <div class="card">
    <div class="card-header bg-indigo">2. Morphodynamics: Why Flank Slopes Become Equal in a Hogback</div>
    <div class="card-body">
      <p>Why do the slopes on both flanks of a <strong>Hogback</strong> approach near-equal inclination when bed dip exceeds $30^\circ - 45^\circ$? The answer lies in the interaction between structural dip and the geotechnical <strong>angle of repose of scree/talus ($\phi \approx 32^\circ - 38^\circ$)</strong>:</p>

      <ul>
        <li><strong>Dip Slope Angle:</strong> On the dip side of the ridge, erosion strips the overlying soft rock down to the resistant structural bedding plane. When bed dip $\theta > 35^\circ - 45^\circ$, the dip slope itself is inherently steep ($35^\circ - 60^\circ$).</li>
        <li><strong>Scarp (Anti-Dip) Slope Angle:</strong> On the opposite scarp side, mechanical undercutting of the underlying soft shale causes rockfalls and toppling of the resistant cap, forming a gravity-controlled scree slope that naturally stabilizes at its angle of repose ($\sim 35^\circ - 40^\circ$).</li>
        <li><strong>Symmetrical Equilibrium:</strong> Because both the structural dip slope ($35^\circ - 50^\circ$) and the erosional scarp slope ($35^\circ - 45^\circ$) have comparable steepness, the ridge assumes an exceptionally sharp, symmetrical triangular cross-section with a narrow crest resembling the arched spine of a razorback hog (hence the name <em>hogback</em>).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q10/hogback_vs_cuesta_morphology.png" alt="Hogback vs Cuesta Morphology Comparison">
        <div class="tb-caption">
          <strong>Figure 10.2: Morphometric Comparison: Mesa vs. Cuesta vs. Hogback.</strong> Demonstrates the geometric transition from horizontal beds ($0^\circ$) to gentle dip cuestas ($< 15^\circ$) and steep, symmetrical hogbacks ($> 45^\circ$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: MESAS, BUTTES AND FLATIRONS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Associated Structural Landforms: Mesas, Buttes & Flatirons</div>
    <div class="card-body">
      <p>Candidates must understand the full structural geomorphology family:</p>

      <ul>
        <li><strong>Cuesta (Spanish for "slope" or "hill"):</strong> Forms when strata dip gently ($< 15^\circ - 20^\circ$). The dip slope is a long, gentle ramp, while the scarp slope is a sheer, abrupt cliff. The two flanks are dramatically asymmetrical.</li>
        <li><strong>Mesa (Spanish for "table"):</strong> A broad, flat-topped tableland capped by a horizontal resistant caprock ($\theta \approx 0^\circ$). By morphological definition, a mesa's top surface width is <em>greater than its vertical height</em>.</li>
        <li><strong>Butte (French for "knoll"):</strong> An isolated, steep-sided pillar or pinnacle resulting from the advanced dissection and retreat of a mesa. A butte's vertical height is <em>greater than its surface width</em>.</li>
        <li><strong>Flatirons:</strong> Triangular-shaped erosion remnants of steeply dipping resistant beds adhering to the flanks of a hogback, resembling giant upright clothes irons.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <div class="question-box">
    <div class="q-num">Official Question Statement — OPSC 2021 Geology Paper-II (Question 10)</div>
    <div class="q-stmt">
      Q10. A long, narrow ridge or a series of hills with a narrow crest and steep slopes of nearly equal inclination on both flanks created by the differential erosion of outcropping sedimentary strata is termed as :
    </div>
    <div class="raw-options">
      <div class="raw-opt">(A) Cuesta</div>
      <div class="raw-opt correct">(B) Hogback &nbsp;✔</div>
      <div class="raw-opt">(C) Mesa</div>
      <div class="raw-opt">(D) Butte</div>
    </div>
  </div>

  <!-- ANSWER BANNER -->
  <div class="answer-banner">
    <div class="tick">✔</div>
    <div>
      <div class="text">Correct Answer: (B) Hogback</div>
      <div class="sub">
        A homoclinal ridge formed by steeply dipping sedimentary beds ($> 30^\circ - 45^\circ$) resulting in a sharp, narrow crest with <strong>steep slopes of nearly equal inclination on both flanks</strong> is formally termed a <strong>Hogback</strong> (Bangar, p. 196; Thornbury, p. 133). Cuestas are strongly asymmetrical.
      </div>
    </div>
  </div>

  <!-- OPTION DISSECTION CARDS -->
  <div class="option wrong">
    <div class="option-header">
      <span>(A) Cuesta</span>
      <span class="tag wrong">Incorrect (Dramatically Asymmetrical Flanks)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A cuesta develops on gently dipping strata ($< 15^\circ - 20^\circ$). It possesses an extremely <em>asymmetrical</em> cross-section consisting of a long, gentle dip slope on one side and a steep, abrupt escarpment on the other. Its flank slopes are never of equal inclination.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Hogback</span>
      <span class="tag correct">Correct Verified Answer</span>
    </div>
    <div class="option-body">
      <strong>Why this option is correct:</strong> By universal geomorphological definition, a <strong>hogback</strong> is a narrow, sharp-crested ridge formed by differential erosion of steeply dipping beds ($> 30^\circ - 45^\circ$). Because the structural dip is steep, the dip slope inclination approaches the scarp slope angle, producing nearly equal, symmetrical slopes on both flanks.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Mesa</span>
      <span class="tag wrong">Incorrect (Broad, Flat-Topped Tableland in Horizontal Strata)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A mesa is a wide, flat-topped horizontal plateau capped by undeformed resistant strata ($\text{dip} \approx 0^\circ$). It is not a narrow ridge or a series of hills with a sharp crest.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Butte</span>
      <span class="tag wrong">Incorrect (Isolated Erosional Pillar in Flat Strata)</span>
    </div>
    <div class="option-body">
      <strong>Why this distractor is incorrect:</strong> A butte is an isolated, small, steep-sided pillar or column formed by extreme dissection of horizontal strata. It lacks the continuous, elongate linear narrow crest of a homoclinal ridge.
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Structural Landform Continuum: Bed Dip vs. Morphology</div>
    <div class="card-body" style="padding:0; overflow-x:auto;">
      <table>
        <thead>
          <tr>
            <th>Structural Landform</th>
            <th>Stratal Dip Angle ($\theta$)</th>
            <th>Cross-Sectional Symmetry</th>
            <th>Flank Slope Relationships</th>
            <th>Crest & Topographic Morphology</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mesa</strong></td>
            <td>Horizontal: $\theta \approx 0^\circ$</td>
            <td>Symmetrical flat plateau</td>
            <td>Steep cliffs on all sides descending to pediments</td>
            <td>Broad, expansive horizontal flat tableland ($Width > Height$)</td>
          </tr>
          <tr>
            <td><strong>Butte</strong></td>
            <td>Horizontal: $\theta \approx 0^\circ$</td>
            <td>Symmetrical pillar</td>
            <td>Sheer vertical cliffs on all sides</td>
            <td>Isolated, small flat cap ($Height > Width$)</td>
          </tr>
          <tr>
            <td><strong>Cuesta</strong></td>
            <td>Gentle Dip: <strong>$\theta < 15^\circ - 20^\circ$</strong></td>
            <td><strong>Highly Asymmetrical</strong></td>
            <td>Gentle dip slope ($\theta$) vs. steep abrupt scarp ($> 40^\circ$)</td>
            <td>Broad, rolling dip plain terminating at a cliff scarp</td>
          </tr>
          <tr>
            <td><strong>Hogback</strong></td>
            <td>Steep Dip: <strong>$\theta > 30^\circ - 45^\circ$</strong></td>
            <td><strong>Nearly Symmetrical</strong></td>
            <td><strong>Steep slopes of nearly equal inclination on both flanks</strong></td>
            <td>Sharp, linear, knife-edge narrow crest (spine)</td>
          </tr>
          <tr>
            <td><strong>Flatiron</strong></td>
            <td>Steep Dip: $\theta > 45^\circ - 60^\circ$</td>
            <td>Triangular facet</td>
            <td>Steep dip facet stripped along bedding plane</td>
            <td>Triangular flatiron remnant on hogback flanks</td>
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
          <strong>Practice Q1:</strong> At what quantitative threshold of structural stratal dip ($\theta$) does a homoclinal ridge transition morphologically from a cuesta into a hogback?
          <div class="pq-ans">✔ Correct Answer: Approximately $\theta \ge 30^\circ \text{ to } 45^\circ$.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Below $20^\circ$, asymmetry between the gentle dip slope and steep scarp is pronounced (cuesta). As dip exceeds $30^\circ - 45^\circ$, the dip slope steepness matches the natural talus angle of the scarp, producing a symmetrical hogback.
          </div>
        </li>

        <li>
          <strong>Practice Q2:</strong> What is a <em>Flatiron</em>, and along which structural landform does it typically develop?
          <div class="pq-ans">✔ Correct Answer: A triangular, steeply inclined erosional facet formed by chevron dissection of a hogback dip slope.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> V-shaped tributary gullies dissecting the steep dip slope of a hogback leave behind prominent triangular plates of resistant rock that resemble antique clothing flatirons (e.g., the famous Flatirons of Boulder, Colorado).
          </div>
        </li>

        <li>
          <strong>Practice Q3:</strong> What is <em>homoclinal shifting</em> (or uniclinal shifting) of a river system?
          <div class="pq-ans">✔ Correct Answer: The continuous lateral migration of a subsequent strike stream down the gentle dip slope of a cuesta as it downcuts into soft shale.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Because the underlying resistant bed acts as a structural slip surface, subsequent streams cut downward and laterally down-dip, undermining the scarp face of the adjacent cuesta.
          </div>
        </li>

        <li>
          <strong>Practice Q4:</strong> In geomorphology, what is the geometric distinction between a <em>Mesa</em> and a <em>Butte</em>?
          <div class="pq-ans">✔ Correct Answer: For a mesa, top surface diameter/width exceeds vertical cliff height; for a butte, vertical height exceeds surface diameter.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Buttes are the erosional remnants of mesas that have been reduced by scarp retreat until their horizontal summit area is smaller than their relief.
          </div>
        </li>

        <li>
          <strong>Practice Q5:</strong> How does an <em>inverted relief</em> synclinal ridge form in folded sedimentary rocks?
          <div class="pq-ans">✔ Correct Answer: Tension fractures along anticlinal crests accelerate erosion into anticlinal valleys, while compressed, joint-free synclinal troughs resist erosion, standing as elevated ridges.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> Tectonic anticlines are initially ridges, but crestal dilation joints promote rapid weathering. Over geologic time, the topography inverts, leaving synclines as high mountain ridges (synclinal mountains).
          </div>
        </li>

        <li>
          <strong>Practice Q6:</strong> What geomorphic model, proposed by Lester C. King, explains the persistence of steep escarpments during the erosion of tabular mesas and cuestas?
          <div class="pq-ans">✔ Correct Answer: Parallel scarp retreat (Pediplanation model).</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> King demonstrated that in semi-arid and arid landscapes, scarps retreat parallel to themselves without losing steepness, leaving behind gently sloping pediments at their base.
          </div>
        </li>

        <li>
          <strong>Practice Q7:</strong> From an engineering geology perspective, why do road cuts excavated into the dip slope of a cuesta present high landslide hazards compared to cuts into a hogback?
          <div class="pq-ans">✔ Correct Answer: Bedding planes dip gently into the road cut ("daylighting"), enabling catastrophic translational planar sliding along weak shale interbeds.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> When cut slope inclination exceeds stratal dip ($\beta_{\text{cut}} > \theta$), unsupported bedding planes daylight into the excavation, triggering planar block slides if water lubricates the shale.
          </div>
        </li>

        <li>
          <strong>Practice Q8:</strong> The Dakota Hogback along the eastern front of the Rocky Mountains in Colorado is composed of which resistant rock formation?
          <div class="pq-ans">✔ Correct Answer: The Cretaceous Dakota Sandstone.</div>
          <div class="pq-exp">
            <strong>Explanation:</strong> The Dakota Sandstone dips steeply at $45^\circ - 60^\circ$ eastward away from the Precambrian Front Range granites, creating the archetypal textbook hogback of North America.
          </div>
        </li>
      </ul>
    </div>
  </div>
"""
    return wrap_html(title, badge, h1_title, meta_text, 10, part1, part2, part3)


if __name__ == "__main__":
    out_q8 = os.path.join(SOLUTIONS_DIR, "Q008_Trellis_Drainage_Pattern_Strike_Dip_Complete_Guide.html")
    with open(out_q8, "w", encoding="utf-8") as f:
        f.write(generate_q008())
    print(f"Generated Q008: {out_q8} ({os.path.getsize(out_q8)} bytes)")

    out_q9 = os.path.join(SOLUTIONS_DIR, "Q009_Fanglomerate_Alluvial_Fan_Lithification_Complete_Guide.html")
    with open(out_q9, "w", encoding="utf-8") as f:
        f.write(generate_q009())
    print(f"Generated Q009: {out_q9} ({os.path.getsize(out_q9)} bytes)")

    out_q10 = os.path.join(SOLUTIONS_DIR, "Q010_Hogback_vs_Cuesta_Steep_Dip_Complete_Guide.html")
    with open(out_q10, "w", encoding="utf-8") as f:
        f.write(generate_q010())
    print(f"Generated Q010: {out_q10} ({os.path.getsize(out_q10)} bytes)")
