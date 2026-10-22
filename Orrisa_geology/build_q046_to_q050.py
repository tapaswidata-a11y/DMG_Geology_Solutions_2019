#!/usr/bin/env python3
"""
Masterclass Builder for Batch 4C: Indian Stratigraphy & Paleontology (Q046 - Q050)
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q046: South Indian Cretaceous: Trichinopoly Basin Tripartite Succession
# ==============================================================================
def generate_q046():
    title = r"Q046: South Indian Marine Cretaceous Stratigraphy: Uttatur, Trichinopoly & Ariyalur Groups | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Mesozoic Biostratigraphy"
    h1_title = "Q046: South Indian Cretaceous: Trichinopoly Tripartite Succession"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 46<br>
<strong>Authoritative References:</strong> M.S. Krishnan, <em>Geology of India and Burma</em> (6th Ed., CBS Publishers, Ch. 15: The Cretaceous System, pp. 402–424); Ramakrishnan & Vaidyanadhan, <em>Geology of India</em> (Geol. Soc. India, Vol. 2, Ch. 24: Cretaceous of South India, pp. 815–842); H.F. Blanford, <em>On the Cretaceous and other rocks of South Arcot and Trichinopoly districts</em> (Mem. Geol. Surv. India, Vol. 4, 1862); Ravindran et al., <em>Cauvery Basin Biostratigraphy</em> (ONGC Bulletin)."""

    part1 = r"""
  <!-- CARD 1: GEOLOGICAL FRAMEWORK OF CAUVERY BASIN CRETACEOUS -->
  <div class="card">
    <div class="card-header bg-blue">1. Stratigraphic Architecture of the Cretaceous Cauvery Basin</div>
    <div class="card-body">
      <p>The marine Cretaceous rocks of the <strong>Tiruchirappalli (Trichinopoly) District</strong> in the Cauvery Basin of Tamil Nadu represent one of the classic, most complete, and richly fossiliferous marine Cretaceous successions in the world. Deposited in a pericratonic rift basin initiated during the breakup of eastern Gondwanaland (separation of India from Antarctica and Australia), the succession rests unconformably upon Archean granitic gneisses or Upper Gondwana plant beds:</p>

      <ul>
        <li><strong>Historical Classification (H.F. Blanford, 1862):</strong> Henry F. Blanford established the foundational tripartite classification of the Trichinopoly Cretaceous succession in ascending chronostratigraphic order:
          <ol>
            <li><strong>Uttatur (Ootatoor) Group (Albian to Cenomanian):</strong> Basal marine transgressive facies resting directly on Archean basement. Characterized by basal coral reef limestones, gypsiferous clays, phosphatic nodules, and abundant ammonites (<em>Schloenbachia, Acanthoceras, Turrilites</em>).</li>
            <li><strong>Trichinopoly Group (Turonian to Coniacian):</strong> Separated from the underlying Uttatur Group by an erosional disconformity marked by a basal conglomerate. Composed of shallow-water marine sandstones, shell limestones, and silts containing fossil wood (silicified tree trunks up to 25 m long) and gastropods/bivalves (<em>Inoceramus, Protocardia</em>).</li>
            <li><strong>Ariyalur Group (Santonian to Maastrichtian):</strong> The thickest, most extensive group, conformably to disconformably overlying the Trichinopoly beds. Dominated by calcareous sandstones, marls, and richly fossiliferous arenites with abundant ammonites (<em>Pachydiscus, Baculites, Sphenodiscus</em>), echinoids (<em>Stigmatopygus</em>), and dinosaurian bone remains (Titanosaurids).</li>
            <li><strong>Niniyur Formation (Danian / Early Paleocene):</strong> Overlies the Ariyalur Group, marking the post-ammonite Tertiary transition characterized by the nautiloid <em>Hercoglossa danica</em>.</li>
          </ol>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q46/cauvery_basin_trichinopoly_cretaceous_stratigraphy.png" alt="Cauvery Basin Trichinopoly Cretaceous Stratigraphy">
        <div class="tb-caption">
          <strong>Figure 46.1:</strong> Chronostratigraphic litho-column of the marine Cretaceous succession in Tiruchirappalli (Cauvery Basin), detailing the sequence: Archean Basement $\to$ Uttatur Group $\to$ Trichinopoly Group $\to$ Ariyalur Group $\to$ Niniyur Formation.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MAHAPATRA EXCERPT AND BIOZONATION -->
  <div class="card">
    <div class="card-header bg-indigo">2. Biostratigraphic Biozones and Transgressive-Regressive Cycles</div>
    <div class="card-body">
      <p>The Trichinopoly Cretaceous sequence records major global sea-level fluctuations (eustatic transgressions) coupled with thermal rift basin subsidence:</p>

      <div class="formula-card">
        <div class="formula-title">Chronostratigraphic Sequence of the Trichinopoly Cretaceous</div>
        $$\text{Basement Gneiss} \xrightarrow{\text{Unconformity}} \mathbf{Uttatur} \xrightarrow{\text{Disconformity}} \mathbf{Trichinopoly} \xrightarrow{\text{Transition}} \mathbf{Ariyalur} \xrightarrow{\text{K-Pg Boundary}} \mathbf{Niniyur}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Ages: Uttatur (Albian-Cenomanian) $\to$ Trichinopoly (Turonian-Coniacian) $\to$ Ariyalur (Santonian-Maastrichtian) $\to$ Niniyur (Danian Paleocene).</p>
      </div>

      <ul>
        <li><strong>Phosphatic Nodules of Uttatur:</strong> The Uttatur clays contain commercially exploited phosphatic nodules ($\sim 20-25\% \text{ P}_2\text{O}_5$) formed under warm, upwelling coastal shelf conditions.</li>
        <li><strong>Fossil Silicified Wood:</strong> The Trichinopoly Group is globally renowned for its giant silicified coniferous tree trunks (e.g., National Fossil Wood Park at Sathanur) swept into shallow marine bays by rivers during regression.</li>
        <li><strong>Global Correlation:</strong> The rich ammonite fauna allows precise high-resolution correlation with the European stage stratotypes (Albian, Cenomanian, Turonian, Senonian, Maastrichtian).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q46/mahapatra_p173_trichinopoly_cretaceous.png" alt="Mahapatra Trichinopoly Cretaceous">
        <div class="tb-caption">
          <strong>Figure 46.2 (G.B. Mahapatra, p. 173):</strong> Textbook stratigraphic classification of the Trichinopoly Cretaceous rocks illustrating the three canonical groups: Uttatur, Trichinopoly, and Ariyalur.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARATIVE STRATIGRAPHIC MATRIX -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Stratigraphic Subdivisions of South Indian Cretaceous</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Group / Formation</th>
            <th>Standard Global Age</th>
            <th>Dominant Lithologies</th>
            <th>Diagnostic Index Fossils</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Niniyur Formation</strong></td>
            <td>Danian (Early Paleocene)</td>
            <td>White limestones, marls, calcareous sands.</td>
            <td><em>Hercoglossa danica</em>, <em>Cardita jaquinoti</em> (Ammonites extinct!).</td>
          </tr>
          <tr>
            <td><strong>Ariyalur Group</strong></td>
            <td>Santonian to Maastrichtian</td>
            <td>Fossiliferous arenites, sandy clays, calcareous sandstone.</td>
            <td><em>Pachydiscus otacodensis</em>, <em>Baculites</em>, <em>Stigmatopygus elatus</em>, Titanosaur bones.</td>
          </tr>
          <tr>
            <td><strong>Trichinopoly Group</strong></td>
            <td>Turonian to Coniacian</td>
            <td>Coarse sandstones, shell limestones, conglomerates.</td>
            <td><em>Inoceramus concentricus</em>, <em>Protocardia hillana</em>, silicified wood (Sathanur).</td>
          </tr>
          <tr>
            <td><strong>Uttatur Group</strong></td>
            <td>Late Albian to Cenomanian</td>
            <td>Basal coral limestone, yellow clays, gypsum, phosphate.</td>
            <td><em>Schloenbachia inflata</em>, <em>Acanthoceras rhotomagense</em>, <em>Turrilites costatus</em>.</td>
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
        <div class="q-num">Question 46</div>
        <div class="q-text">The Upper Cretaceous rocks of the Tiruchchirappalli area has been classified into three Formations viz., Uttatur, Trichinapoli and _____.</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Ariyalur Formation</div>
          <div class="opt-node">(B) Haimanta Formation</div>
          <div class="opt-node">(C) Lilang Formation</div>
          <div class="opt-node">(D) Chikkim Formation</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Ariyalur Formation</strong> [The classic tripartite South Indian Cretaceous sequence of Blanford (1862) comprises the Uttatur, Trichinopoly, and Ariyalur Groups, followed by the Danian Niniyur Formation.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Ariyalur Formation</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>The marine Cretaceous succession of the Cauvery Basin in the Tiruchirappalli (Trichinopoly) district of Tamil Nadu was classically subdivided by Henry F. Blanford (1862) into three principal units (in ascending stratigraphic order):
          <ol>
            <li><strong>Uttatur Formation (Group)</strong> — Albian to Cenomanian</li>
            <li><strong>Trichinopoly Formation (Group)</strong> — Turonian to Coniacian</li>
            <li><strong>Ariyalur Formation (Group)</strong> — Santonian to Maastrichtian</li>
          </ol>
        </li>
        <li>The <strong>Ariyalur Formation</strong> forms the youngest and most aerially extensive Cretaceous unit of this tripartite sequence, beautifully exposed around the town of Ariyalur and overlain by the Paleocene Niniyur beds.</li>
        <li>Therefore, the missing third member in the official sequence is unequivocally the <strong>Ariyalur Formation</strong>.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Haimanta Formation</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Haimanta Group (Formation)</strong> is a famous lithostratigraphic unit belonging to the <strong>Cambrian System of the Tethyan Himalayan succession</strong> in Spiti, Himachal Pradesh (named by C.L. Griesbach in 1891).</li>
        <li>It represents early Paleozoic slates, phyllites, and quartzites containing trilobites (<em>Redlichia</em>), bearing zero geological, geographic, or chronostratigraphic connection to the Cretaceous of Tamil Nadu.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Lilang Formation</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Lilang Group (System)</strong> is the classical <strong>Triassic marine succession of Spiti</strong> (Himalayas), comprising richly fossiliferous limestones and shales containing ammonoids such as <em>Otoceras, Meekoceras, Ceratites</em>, and <em>Daonella</em>.</li>
        <li>It has nothing to do with the South Indian Cretaceous Cauvery Basin.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) Chikkim Formation</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Although the <strong>Chikkim Formation</strong> is indeed of Cretaceous age, it is located entirely in the <strong>Tethyan Himalayan basin of Spiti</strong> (Himachal Pradesh), consisting of white pelagic limestones and shales containing planktonic foraminifera (<em>Globotruncana</em>).</li>
        <li>It is not part of the Peninsular Tiruchirappalli (Cauvery Basin) succession.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Indian Cretaceous Marine Basins</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Geographic Basin</th>
            <th>Primary Lithostratigraphic Succession</th>
            <th>Tectonic Setting</th>
            <th>Key Index Fossils / Biota</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Trichinopoly (Cauvery Basin, Tamil Nadu)</strong></td>
            <td><strong>Uttatur $\to$ Trichinopoly $\to$ Ariyalur $\to$ Niniyur</strong></td>
            <td>East coast passive margin pericratonic rift (Gondwana breakup).</td>
            <td><em>Acanthoceras</em>, <em>Inoceramus</em>, <em>Pachydiscus</em>, <em>Hercoglossa danica</em>.</td>
          </tr>
          <tr>
            <td><strong>Narmada Basin (Bagh Beds, MP/Gujarat)</strong></td>
            <td>Nimar Sandstone $\to$ Nodular Limestone $\to$ Deola-Chirakhan Marl $\to$ Coralline Limestone</td>
            <td>SONATA intraplate marine transgressive arm from western Tethys.</td>
            <td>Echinoids (<em>Hemiaster</em>), ammonites (<em>Placenticeras</em>), bivalves (<em>Inoceramus</em>).</td>
          </tr>
          <tr>
            <td><strong>Spiti (Tethyan Himalayas)</strong></td>
            <td>Giumal Sandstone $\to$ <strong>Chikkim Formation</strong> (Limestone & Shale)</td>
            <td>Tethyan deep-marine continental shelf and slope.</td>
            <td>Planktonic foraminifera (<em>Globotruncana stuarti</em>), belemnites (<em>Neohibolites</em>).</td>
          </tr>
          <tr>
            <td><strong>Jaisalmer / Kutch Basin</strong></td>
            <td>Ukra Member $\to$ Bhuj Formation (Kutch); Pariwar $\to$ Habur (Jaisalmer)</td>
            <td>Western continental passive margin rift basins.</td>
            <td>Ammonites (<em>Australiceras, Tropaeum</em>), plant fossils (<em>Ptilophyllum</em>).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Indian Stratigraphy & Biostratigraphy</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Identification of the K-Pg Boundary in South India</div>
        <p>In which specific lithostratigraphic contact in the Cauvery Basin is the Cretaceous-Paleogene (K-Pg) boundary located, and what biostratigraphic event marks it?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The K-Pg boundary occurs at the contact between the uppermost <strong>Ariyalur Group (Kallankurichchi / Ottakoil / Kallamedu Formations, late Maastrichtian)</strong> and the overlying <strong>Niniyur Formation (Danian, early Paleocene)</strong>. The boundary is marked by the catastrophic mass extinction of ammonites (e.g., <em>Pachydiscus</em>, <em>Sphenodiscus</em>), belemnites, and dinosaurs, and the sudden emergence of the Danian nautiloid <em>Hercoglossa danica</em> and globigerinid planktonic foraminifera.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Phosphorite Genesis in the Uttatur Clays</div>
        <p>Explain the geochemical depositional environment responsible for the accumulation of phosphatic nodules in the Uttatur Formation.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>During the early Cretaceous (Albian-Cenomanian) marine transgression, strong coastal upwelling carried cold, nutrient-rich deep ocean waters onto the warm shallow shelf of the Cauvery Basin. Intense biological productivity of phytoplankton led to high organic matter burial in anoxic bottom muds. Anaerobic decay released high concentrations of dissolved phosphate, precipitating cryptocrystalline carbonate-fluorapatite (francolite) nodules within the gypsiferous Uttatur clays.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Distinguishing Himalayan Cretaceous from Peninsular Cretaceous</div>
        <p>Match the following Cretaceous formations with their correct basin: (1) Chikkim, (2) Bagh, (3) Ariyalur, (4) Habur.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li>(1) <strong>Chikkim Formation:</strong> Spiti Basin, Tethyan Himalayas.</li>
          <li>(2) <strong>Bagh Beds:</strong> Narmada Rift Valley, Madhya Pradesh.</li>
          <li>(3) <strong>Ariyalur Formation:</strong> Cauvery Basin, Tiruchirappalli, Tamil Nadu.</li>
          <li>(4) <strong>Habur Formation:</strong> Jaisalmer Basin, Rajasthan.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Chronostratigraphic Age Estimation from Transgression</div>
        <p>The basal Uttatur coral reef limestones rest directly upon Archean charnockitic gneisses. What is the geological name for such an unconformity, and what is the magnitude of the missing time gap?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Because marine sedimentary strata rest directly upon crystalline igneous/high-grade metamorphic basement, the contact is a <strong>Nonconformity</strong>. The charnockites are Archean/Paleoproterozoic ($\sim 2500\text{ Ma}$), while the basal Uttatur limestones are Albian ($\sim 105\text{ Ma}$). The missing chronological record represents an enormous hiatus of approximately $2.4\text{ billion years}$!</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Inoceramid Bivalve Environmental Significance</div>
        <p>The Trichinopoly Group is rich in large bivalves of the genus <em>Inoceramus</em>. What paleoenvironmental conditions are indicated by broad-shelled inoceramids?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Inoceramus</em> species were specialized benthic epifaunal bivalves capable of inhabiting low-oxygen (dysaerobic) muddy seafloors. Their broad, thin, flattened prismatic shells spread their weight over soft substrate (snowshoe effect) and harbored chemosymbiotic sulfur-oxidizing bacteria in their gills, indicating warm shelf waters with periodic oxygen restriction.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Origin of Sathanur Fossil Wood Park</div>
        <p>How were the massive conifer logs in the Trichinopoly Group fossilized?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>During the Turonian, dense gymnosperm forests fringed the adjacent crystalline highland. Catastrophic river floods uprooted trees and transported them into coastal estuaries and shallow marine lagoons. Rapid burial under fine silts prevented aerobic bacterial decay. Percolating silica-rich groundwater gradually replaced cellulose cellular structures with microcrystalline silica/quartz (petrifaction / silicification), preserving delicate growth rings in solid stone.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Subdivisions of the Ariyalur Group</div>
        <p>Name the four constituent formations comprising the Ariyalur Group in modern lithostratigraphic usage.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In modern lithostratigraphic nomenclature (Sastry et al., ONGC), the Ariyalur Group is subdivided into four formations (in ascending order):</p>
        <ol>
          <li><strong>Sillakkudi Formation:</strong> Campanian arenites and clays.</li>
          <li><strong>Kallankurichchi Formation:</strong> Late Campanian-Early Maastrichtian bioclastic gryphean limestone.</li>
          <li><strong>Ottakoil Formation:</strong> Late Maastrichtian calcareous sandstone.</li>
          <li><strong>Kallamedu Formation:</strong> Terminal Maastrichtian terrestrial/estuarine sands with dinosaur bones.</li>
        </ol>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Cephalopod Suture Transition across the Niniyur Boundary</div>
        <p>How do the sutures of cephalopods change from the Ariyalur Group to the Niniyur Formation?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Ariyalur cephalopods are dominated by true ammonites (e.g., <em>Pachydiscus</em>) possessing extremely complex <strong>ammonitic sutures</strong> (intricately fluted lobes and saddles). Across the K-Pg boundary into the Niniyur Formation, all ammonites are completely extinct; the surviving cephalopods are nautiloids (e.g., <em>Hercoglossa danica</em>) possessing smooth, simple undulating <strong>nautilitic sutures</strong>.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 46, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q046_Trichinopoly_Cretaceous_Uttatur_Trichinopoly_Ariyalur_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q046: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q047: Purana Basins: Vindhyan Supergroup Lithostratigraphy
# ==============================================================================
def generate_q047():
    title = r"Q047: Proterozoic Purana Basins: Vindhyan Supergroup Lithostratigraphy (Semri, Kaimur, Rewa, Bhander) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Proterozoic Purana Basins"
    h1_title = "Q047: Vindhyan Supergroup: Semri, Kaimur, Rewa, and Bhander Groups"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 47<br>
<strong>Authoritative References:</strong> J.B. Auden, <em>Vindhyan Sedimentation in the Son Valley, Mirzapur District</em> (Mem. Geol. Surv. India, Vol. 62, 1933); Ramakrishnan & Vaidyanadhan, <em>Geology of India</em> (Vol. 1, Ch. 12: Purana Basins — Vindhyan Supergroup, pp. 315–354); M.S. Krishnan, <em>Geology of India and Burma</em> (Ch. 7: The Vindhyan System); G.B. Mahapatra, <em>Textbook of Physical Geology & Indian Stratigraphy</em> (pp. 164–167)."""

    part1 = r"""
  <!-- CARD 1: VINDHYAN SUPERGROUP STRATIGRAPHIC ARCHITECTURE -->
  <div class="card">
    <div class="card-header bg-blue">1. The Vindhyan Supergroup: Architecture of India's Premier Purana Basin</div>
    <div class="card-body">
      <p>The <strong>Vindhyan Supergroup</strong> occupies a vast, crescent-shaped intracratonic sag basin (the Great Vindhyan Basin) covering over $104,000\text{ km}^2$ across Madhya Pradesh, Uttar Pradesh, Rajasthan, and Bihar. Resting unconformably over Archean granitic basement (Bundelkhand Gneiss) and Paleoproterozoic folded metasediments (Bijawar and Gwalior Groups), it represents an undeformed to gently warped Proterozoic shallow marine-to-continental sedimentary pile up to $4,500\text{ m}$ thick:</p>

      <ul>
        <li><strong>Classical Subdivisions:</strong> Stratigraphically, the Vindhyan Supergroup is divided into two primary divisions and <strong>four canonical groups</strong> (in ascending stratigraphic order):
          <ol>
            <li><strong>Lower Vindhyan:</strong>
              <ul>
                <li><strong>Semri Group:</strong> Dominated by marine carbonate-clastic cycles (basal conglomerate, Kajrahat Limestone, Porcellanite Formation, Olive Shales, Fawn Limestone, and Rohtas Limestone). Contains diverse stromatolites, microfossils, and volcaniclastic tuffs dated between $\sim 1700\text{ Ma}$ and $1600\text{ Ma}$.</li>
              </ul>
            </li>
            <li><strong>Upper Vindhyan:</strong> Separated from the Semri Group by a regional erosional unconformity marked by the disappearance of extensive marine carbonates and the onset of mature clastic sedimentation:
              <ul>
                <li><strong>Kaimur Group:</strong> Dominated by quartzose sandstones, conglomerates, and orthoquartzites (Dhandraul Quartzite) recording high-energy fluvial to coastal barrier regimes ($\sim 1150-1000\text{ Ma}$).</li>
                <li><strong>Rewa Group:</strong> Rhythmic alternation of shales and sandstones (Panna Shale, Asan Sandstone, Jhiri Shale, Govindgarh Sandstone). Famous for diamondiferous conglomerates at Panna.</li>
                <li><strong>Bhander Group:</strong> The uppermost group, marking the return of marine tidal carbonate-evaporite sedimentation (Ganurgarh Shale, Bhander Limestone, Sirbu Shale, Upper Bhander Sandstone) terminating around $\sim 650-550\text{ Ma}$ (Ediacaran).</li>
              </ul>
            </li>
          </ol>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q47/vindhyan_supergroup_four_groups_stratigraphy.png" alt="Vindhyan Supergroup Stratigraphy">
        <div class="tb-caption">
          <strong>Figure 47.1:</strong> Complete stratigraphic column of the Vindhyan Supergroup showing the ascending sequence of the four constituent groups: Semri $\to$ Kaimur $\to$ Rewa $\to$ Bhander Group.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MAHAPATRA EXCERPT AND ECONOMIC POTENTIAL -->
  <div class="card">
    <div class="card-header bg-indigo">2. Lithological Characteristics and Economic Minerals</div>
    <div class="card-body">
      <p>Each of the four Vindhyan groups hosts diagnostic lithologies and critical industrial minerals:</p>

      <div class="formula-card">
        <div class="formula-title">The Ascending Quadripartite Vindhyan Succession</div>
        $$\text{Archean Basement} \xrightarrow{\text{Great Eparchean Interval}} \mathbf{Semri} \xrightarrow{\text{Unconformity}} \mathbf{Kaimur} \xrightarrow{\text{Conformity}} \mathbf{Rewa} \xrightarrow{\text{Conformity}} \mathbf{Bhander}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Rule: Semri (Carbonates + Volcanics) $\to$ Kaimur (Arenaceous) $\to$ Rewa (Argillaceous + Arenaceous) $\to$ Bhander (Calcareous + Arenaceous).</p>
      </div>

      <ul>
        <li><strong>Diamondiferous Conglomerates:</strong> The famous <strong>Panna diamond mines</strong> of Madhya Pradesh occur in conglomerates at the base of the Rewa Group (Panna Diamond Belt) and the base of the Bhander Group, derived from Kimberlite/Lamproite pipes (e.g., Majhgawan pipe, dated $\sim 1070\text{ Ma}$).</li>
        <li><strong>Portland Cement Raw Material:</strong> High-grade calcitic limestones of the Semri (Rohtas Limestone, Kajrahat Limestone) and Bhander (Bhander Limestone) support India's largest cement manufacturing clusters.</li>
        <li><strong>Architectural Building Stones:</strong> The durable, uniformly grained red and buff sandstones of the Kaimur and Bhander groups provided the construction stones for India's historic monuments, including the Red Fort of Delhi, the Sanchi Stupa, and the Rashtrapati Bhavan.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q47/mahapatra_p165_vindhyan_four_groups.png" alt="Mahapatra Vindhyan Stratigraphy">
        <div class="tb-caption">
          <strong>Figure 47.2 (G.B. Mahapatra, p. 165):</strong> Textbook litho-stratigraphic chart of the Vindhyan Supergroup highlighting the division into Semri, Kaimur, Rewa, and Bhander Groups.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPLETE STRATIGRAPHIC BREAKDOWN -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Stratigraphic Subdivisions of the Vindhyan Supergroup</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Group</th>
            <th>Primary Subformations</th>
            <th>Dominant Lithologies</th>
            <th>Depositional Environment & Economic Minerals</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bhander Group</strong> (Uppermost)</td>
            <td>Upper Bhander Sandstone, Sirbu Shale, Bhander Limestone, Ganurgarh Shale.</td>
            <td>Red sandstones, stromatolitic limestones, shales, gypsum casts.</td>
            <td>Tidal flat, sabkha, lagoonal. High-grade cement limestone and building flagstones.</td>
          </tr>
          <tr>
            <td><strong>Rewa Group</strong></td>
            <td>Govindgarh Sandstone, Jhiri Shale, Asan Sandstone, Panna Shale.</td>
            <td>Shales, fine sandstones, basal conglomerates.</td>
            <td>Shallow marine shelf to deltaic. <strong>Diamond-bearing conglomerates (Panna)</strong>.</td>
          </tr>
          <tr>
            <td><strong>Kaimur Group</strong></td>
            <td>Dhandraul Quartzite, Scarp Sandstone, Bijaigarh Shale, Ghaghar Sandstone.</td>
            <td>Orthoquartzites, quartz arenites, black carbonaceous shales.</td>
            <td>High-energy coastal barrier beaches and fluvial bars. Pyrite in Bijaigarh Shale.</td>
          </tr>
          <tr>
            <td><strong>Semri Group</strong> (Lowermost)</td>
            <td>Rohtas Limestone, Glauconitic Sandstone, Fawn Limestone, Porcellanite, Kajrahat Limestone.</td>
            <td>Limestones, dolomites, tuffs, porcellanites, glauconitic sandstones.</td>
            <td>Transgressive shallow marine carbonate platform. Sub-volcanic tuffs and cement limestone.</td>
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
        <div class="q-num">Question 47</div>
        <div class="q-text">The Vindhyan Supergroup is divisible into four groups viz., Semri Group, Kaimur Group, Rewa Group and _____.</div>
        <div class="q-options">
          <div class="opt-node">(A) Bijawar Group</div>
          <div class="opt-node correct">(B) Bhander Group</div>
          <div class="opt-node">(C) Gwalior Group</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) Bhander Group</strong> [The four groups of the Vindhyan Supergroup in ascending order are the Semri Group, Kaimur Group, Rewa Group, and Bhander Group.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) Bhander Group</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>The <strong>Vindhyan Supergroup</strong> is universally recognized across all Indian geological surveys and textbooks (Auden 1933; Krishnan 1982; Ramakrishnan & Vaidyanadhan 2008; Mahapatra 2019) as comprising exactly <strong>four constituent groups</strong> in ascending chronological order:
          <ol>
            <li><strong>Semri Group</strong> (Lower Vindhyan)</li>
            <li><strong>Kaimur Group</strong> (Upper Vindhyan)</li>
            <li><strong>Rewa Group</strong> (Upper Vindhyan)</li>
            <li><strong>Bhander Group</strong> (Upper Vindhyan)</li>
          </ol>
        </li>
        <li>The <strong>Bhander Group</strong> is the fourth and uppermost group of the Vindhyan Supergroup, composed of the Ganurgarh Shale, Bhander Limestone, Sirbu Shale, and Upper Bhander Sandstone.</li>
        <li>Therefore, the missing fourth group is indisputably the <strong>Bhander Group</strong>.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Bijawar Group</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Bijawar Group</strong> is a Paleoproterozoic metasedimentary sequence (quartzites, dolomites, ferruginous beds, and basaltic traps) that forms the <em>folded structural basement</em> underlying the Vindhyan Supergroup in central India.</li>
        <li>The Vindhyan Semri Group rests unconformably upon the deformed Bijawar Group with an intervening angular unconformity. Thus, Bijawar is not a constituent group of the Vindhyan Supergroup.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Gwalior Group</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Gwalior Group</strong> (comprising the Par Formation and Morar Formation with banded iron formations and volcanic sills) is another Paleoproterozoic sedimentary-volcanic succession in northern Madhya Pradesh.</li>
        <li>Like the Bijawar, the Gwalior Group unconformably underlies the Kaimur Group of the Vindhyan Supergroup. It is an older basement succession, not a division of the Vindhyan Supergroup.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (B) Bhander Group is the exact, canonical fourth member of the Vindhyan Supergroup, selecting "None of these" is factually incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: The Major Proterozoic Purana Basins of India</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Purana Supergroup / Basin</th>
            <th>Primary Groups / Formations</th>
            <th>Cratonic Setting</th>
            <th>Key Economic Minerals</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Vindhyan Supergroup</strong></td>
            <td><strong>Semri $\to$ Kaimur $\to$ Rewa $\to$ Bhander</strong></td>
            <td>Bundelkhand / Central Indian Craton.</td>
            <td>Diamonds (Panna), Cement Limestone, Building Sandstones, Pyrite.</td>
          </tr>
          <tr>
            <td><strong>Cuddapah Supergroup</strong></td>
            <td>Papaghni $\to$ Chitravati $\to$ Nallamalai $\to$ Sanjamala</td>
            <td>Dharwar Craton (Eastern margin).</td>
            <td>Barite (Mangampeta), Chrysotile Asbestos, Lead-Zinc, Limestone.</td>
          </tr>
          <tr>
            <td><strong>Kurnool Group</strong></td>
            <td>Banganapalle $\to$ Narji $\to$ Owk $\to$ Paniam $\to$ Koilkuntla $\to$ Nandyal</td>
            <td>Unconformable basin overlying Cuddapah Supergroup.</td>
            <td>Diamonds (Banganapalle conglomerate), High-grade Cement Limestone (Narji).</td>
          </tr>
          <tr>
            <td><strong>Bhima Group</strong></td>
            <td>Rabanpalli $\to$ Shahabad $\to$ Sogur $\to$ Halkal $\to$ Katamadevarahalli</td>
            <td>Dharwar Craton (Karnataka).</td>
            <td>High-grade Flaggy Limestone (Shahabad Stone), Uranium mineralization (Gogi).</td>
          </tr>
          <tr>
            <td><strong>Chhattisgarh Supergroup</strong></td>
            <td>Singhora $\to$ Chandarpur $\to$ Raipur Groups</td>
            <td>Bastar Craton.</td>
            <td>Limestone, Dolomite, Quartzite, Building Stone.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Purana Stratigraphy & Sedimentary Basins</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Geochronological Dating of the Semri Porcellanite</div>
        <p>High-precision U-Pb zircon SHRIMP dating of felsic volcanic tuffs in the Porcellanite Formation of the Semri Group yields an age of $1630 \pm 5\text{ Ma}$. What does this establish regarding the age of the base of the Vindhyan Supergroup?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Historically, the Vindhyan Supergroup was considered Neoproterozoic to early Cambrian. The $1630\text{ Ma}$ U-Pb zircon age from the Porcellanite Formation (located in the lower-middle Semri Group) conclusively proved that the base of the Vindhyan Supergroup initiated in the <strong>Paleoproterozoic (Statherian Period)</strong>, extending the duration of Vindhyan sedimentation across nearly $1\text{ billion years}$ of Earth history.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: The Great Boundary Fault (GBF) of Rajasthan</div>
        <p>What major structural tectonic dislocation bounds the Vindhyan Basin along its northwestern margin in Rajasthan?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The northwestern margin of the Vindhyan Basin is truncated by the <strong>Great Boundary Fault (GBF) of Rajasthan</strong>. This is a regional, northeast-trending, post-Vindhyan reverse fault/thrust exceeding $800\text{ km}$ in length that brings deformed pre-Vindhyan rocks (Aravalli/Delhi/Bhilwara metamorphic belts) into juxtaposition against undeformed Upper Vindhyan strata (Bhander and Kaimur groups).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Glauconite Mineralogy in the Semri Group</div>
        <p>Glauconitic sandstones occur prominently in the Semri and Kaimur groups. What does the presence of authigenic glauconite indicate about the paleoenvironment?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Authigenic glauconite is a potassium iron phyllosilicate mineral that precipitates exclusively in <strong>marine shelf environments</strong> with slow, starved sedimentation rates (condensed sections), mild reducing (suboxic) conditions, and normal marine salinities at water depths typically between $50\text{ m}$ and $300\text{ m}$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Diamond Source in the Panna Diamond Belt</div>
        <p>In which igneous rock body did the diamonds found in the Rewa Group conglomerates originate, and what is its age?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The primary source of the diamonds is the <strong>Majhgawan and Hinota Kimberlite/Lamproite pipes</strong> intruded into the Paleoproterozoic basement. Radiometric dating (Rb-Sr and Ar-Ar) dates the Majhgawan intrusion at $\sim 1070\text{ Ma}$. Weathering and fluvial erosion of these pipes during Rewa Group sedimentation concentrated diamonds into basal fluvial gravels, forming the diamondiferous conglomerates.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Ediacaran Trace Fossil Debate in the Vindhyans</div>
        <p>What controversy arose regarding the discovery of trace fossils and carbonaceous discs (<em>Chuaria circularis</em>) in the Rohtas and Bhander shales?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The discovery of circular carbonaceous compressions (<em>Chuaria, Tawuia</em>) and putative trace fossils in the Rohtas Formation (Semri) and Bhander Group led some workers to propose a late Neoproterozoic/Cambrian age for the whole sequence. However, <em>Chuaria</em> is now recognized as a long-ranging megascopic eukaryotic alga that extends back to the Mesoproterozoic ($\sim 1400\text{ Ma}$), fully compatible with modern radiometric age constraints.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Sedimentological Maturity of the Dhandraul Quartzite</div>
        <p>The Dhandraul Quartzite of the Kaimur Group exhibits quartz arenite composition ($>98\% \text{ quartz}$) and well-rounded grains. What does this signify about the depositional and tectonic regime?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Extreme compositional and textural maturity (quartz arenites with well-rounded, well-sorted monocrystalline quartz) indicates intense chemical weathering of the source area, prolonged polycyclic sediment recycling, and deposition on a stable, slowly subsiding cratonic shelf under high-energy wave and tidal action.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Distinction Between Purana Basins and Gondwana Basins</div>
        <p>Contrast the tectonic basins of the Proterozoic Purana Supergroups (Vindhyan, Cuddapah) with the Phanerozoic Gondwana Basins.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Purana Basins:</strong> Broad intracratonic sag/flexural basins; Proterozoic in age; dominated by marine carbonates, mature orthoquartzites, and shales; devoid of coal.</li>
          <li><strong>Gondwana Basins:</strong> Linear fault-bounded grabens and half-grabens; Permian to Early Cretaceous in age; dominated by continental fluvial, lacustrine, and glacial clastics; host to India's major bituminous coal seams.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Identification of Evaporite Facies in the Sirbu Shale</div>
        <p>What sedimentary structures in the Sirbu Shale and Bhander Limestone demonstrate arid sabkha depositional conditions?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The occurrence of <strong>halite pseudomorphs (hopper crystal casts)</strong>, gypsum discoidal casts, desiccation mud cracks, and flat-pebble intraformational conglomerates in the Sirbu Shale and Upper Bhander strata proves episodic subaerial exposure and intense evaporation on supratidal sabkha mudflats.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 47, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q047_Vindhyan_Supergroup_Semri_Kaimur_Rewa_Bhander_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q047: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q048: Peninsular Gondwana Basins: Talchir Formation Glaciation
# ==============================================================================
def generate_q048():
    title = r"Q048: Basal Gondwana Stratigraphy: Talchir Boulder Bed & Permo-Carboniferous Glaciation | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Gondwana Coal Basins"
    h1_title = "Q048: Basal Gondwana Stratigraphy: Talchir Boulder Bed & Glaciation"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 48<br>
<strong>Authoritative References:</strong> W.T. Blanford, H.F. Blanford & W. Theobald, <em>On the Geological Structure and Relations of the Talcheer Coal Field</em> (Mem. Geol. Surv. India, Vol. 1, 1856, pp. 33–88); Ramakrishnan & Vaidyanadhan, <em>Geology of India</em> (Vol. 2, Ch. 18: Gondwana Supergroup, pp. 605–648); M.S. Krishnan, <em>Geology of India and Burma</em> (Ch. 10: The Gondwana System); G.B. Mahapatra, <em>Textbook of Indian Stratigraphy</em> (pp. 167–170)."""

    part1 = r"""
  <!-- CARD 1: THE TALCHIR FORMATION AND GONDWANA GLACIATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Talchir Formation: Basal Hallmark of the Gondwana Supergroup</div>
    <div class="card-body">
      <p>The <strong>Gondwana Supergroup</strong> of Peninsular India represents a massive continental sedimentary sequence ranging in age from the Late Carboniferous (Asselian) to Early Cretaceous. In all Indian Gondwana basins—and specifically in its type locality, the <strong>Talcher Coalfield</strong> of the Mahanadi-Brahmani Valley in Odisha—the base of the Gondwana succession is invariably marked by the <strong>Talchir Formation</strong>:</p>

      <ul>
        <li><strong>Discovery in Odisha (Blanford Brothers, 1856):</strong> The formation takes its name from the former princely state of <strong>Talcher (now Angul district, Odisha)</strong>, where W.T. Blanford, H.F. Blanford, and William Theobald first recognized that the basal boulder-bearing beds were deposited under ancient glacial conditions.</li>
        <li><strong>The Basal Talchir Boulder Bed (Glacial Tillite / Diamictite):</strong> The lowermost member is an unsorted, unstratified, polymictic diamictite (tillite) resting with profound unconformity upon striated and polished Precambrian basement gneisses:
          <ul>
            <li><strong>Clast Characteristics:</strong> Contains angular to subrounded pebbles, cobbles, and giant boulders (up to several meters across) embedded in a matrix of fine-grained greenish-grey rock flour (silt-clay matrix).</li>
            <li><strong>Glacial Signatures:</strong> Many clasts exhibit characteristic <strong>faceted surfaces, flat soles, chatter marks, and glacial striations</strong>. Dropstones punctuate thinly laminated glacio-lacustrine shales.</li>
          </ul>
        </li>
        <li><strong>Periglacial & Glacio-Lacustrine Facies:</strong> Overlying the basal tillite are periglacial rhythmically laminated greenish silts known as <strong>needle shales</strong> (which weather into delicate pencil-like fragments), turbidite sandstones, and varved glacio-lacustrine clays.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q48/talchir_boulder_bed_gondwana_glaciation.png" alt="Talchir Boulder Bed Glaciation">
        <div class="tb-caption">
          <strong>Figure 48.1:</strong> Outcrop model of the basal Gondwana Talchir Boulder Bed resting on polished, striated basement pavement, showing glacial dropstones embedded in periglacial rhythmite shales.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MAHAPATRA EXCERPT AND CLIMATIC REVERSAL -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Permo-Carboniferous Gondwana Ice Age</div>
    <div class="card-body">
      <p>The Talchir deposits document the climax and retreat of the great Late Paleozoic Ice Age across the supercontinent Gondwanaland:</p>

      <div class="formula-card">
        <div class="formula-title">Stratigraphic Triad of the Basal Gondwana Succession</div>
        $$\text{Striated Precambrian Basement} \xrightarrow{\text{Glacial Abrasion}} \mathbf{Tillite \text{ (Boulder Bed)}} \xrightarrow{\text{Meltwater}} \mathbf{Needle \text{ Shales}} \xrightarrow{\text{Post-Glacial Warmth}} \mathbf{Coal \text{ Measures (Barakar)}}$$
      </div>

      <ul>
        <li><strong>Paleogeographic Location:</strong> During the Late Carboniferous ($\sim 300\text{ Ma}$), Greater India was located at high southern latitudes ($60^\circ-75^\circ\text{S}$) near the South Pole as part of Gondwanaland. Vast continental ice sheets covered the craton, radiating glacial debris into proto-rift grabens.</li>
        <li><strong>Climatic Amelioration:</strong> As Gondwanaland drifted equatorward during the Early Permian, the ice sheets melted rapidly. Meltwater rivers flooded the rift valleys, depositing thick braided-stream sandstones and extensive peat swamps that gave rise to the overlying coal-bearing <strong>Barakar Formation</strong> and rich <em>Glossopteris</em> flora.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q48/mahapatra_p168_talchir_boulder_bed.png" alt="Mahapatra Talchir Boulder Bed">
        <div class="tb-caption">
          <strong>Figure 48.2 (G.B. Mahapatra, p. 168):</strong> Textbook description of the Talchir Boulder Bed and its diagnostic periglacial needle shales marking the base of Gondwana sedimentation in Talcher.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF BASAL GONDWANA UNITS ACROSS CRATONS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Pan-Gondwanan Correlation of the Basal Glacial Horizon</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Gondwana Continent / Basin</th>
            <th>Basal Glacial / Periglacial Formation</th>
            <th>Dominant Glacial Lithofacies</th>
            <th>Diagnostic Glacial Evidence</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>India (Talcher / Damodar)</strong></td>
            <td><strong>Talchir Formation (Talchir Boulder Bed)</strong></td>
            <td>Polymictic tillite, needle shales, turbidite sands.</td>
            <td>Striated basement pavements (Irai, Maharashtra), faceted dropstones.</td>
          </tr>
          <tr>
            <td><strong>South Africa (Karoo Basin)</strong></td>
            <td><strong>Dwyka Group</strong></td>
            <td>Massive diamictites, varvites, glaciomarine dropstones.</td>
            <td>Glacially polished rock surfaces, grooved pavements.</td>
          </tr>
          <tr>
            <td><strong>South America (Paraná Basin)</strong></td>
            <td><strong>Itararé Group</strong></td>
            <td>Tillites, rhythmite shales, dropstones.</td>
            <td>Striated clasts, subglacial tunnel-valley fills.</td>
          </tr>
          <tr>
            <td><strong>Australia (Bowen / Sydney Basins)</strong></td>
            <td><strong>Bacchus Marsh / Wynyard Formations</strong></td>
            <td>Diamictites, varved mudstones.</td>
            <td>Glacial erratic pavements, cold-water marine fauna (<em>Eurydesma</em>).</td>
          </tr>
          <tr>
            <td><strong>Antarctica (Transantarctic Mts.)</strong></td>
            <td><strong>Pagoda Formation</strong></td>
            <td>Massive subglacial tillites, striated pavements.</td>
            <td>Direct polar ice-sheet striations on crystalline basement.</td>
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
        <div class="q-num">Question 48</div>
        <div class="q-text">The base of Gondwana sediments in Talcher coalfield, is marked by a pile of :</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Glacial and Periglacial deposits</div>
          <div class="opt-node">(B) Fossiliferous shale</div>
          <div class="opt-node">(C) Glossopteris flora</div>
          <div class="opt-node">(D) Talcher sandstone</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Glacial and Periglacial deposits</strong> [The basal Gondwana sequence in Talcher is universally characterized by the Talchir Boulder Bed (tillite) and associated glacio-lacustrine needle shales reflecting the Permo-Carboniferous Gondwana glaciation.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Glacial and Periglacial deposits</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>In all Indian Gondwana basins—and precisely in the <strong>Talcher Coalfield</strong> of Odisha (the global type area established by W.T. Blanford in 1856)—the absolute base of the Gondwana Supergroup is represented by the <strong>Talchir Formation</strong>.</li>
        <li>The defining, unmistakable lithological feature of the basal Talchir Formation is a massive pile of <strong>glacial and periglacial deposits</strong>:
          <ol>
            <li>The <strong>Talchir Boulder Bed</strong>: A true subglacial tillite (diamictite) containing faceted, polished, and striated boulders embedded in a fine rock-flour matrix resting directly upon polished Precambrian basement.</li>
            <li><strong>Periglacial rhythmite shales</strong> ("needle shales") and varved clays carrying ice-rafted dropstones deposited in proglacial lakes.</li>
          </ol>
        </li>
        <li>These deposits serve as the prime stratigraphic marker of the widespread Late Carboniferous to Early Permian glaciation of Gondwanaland. Thus, <strong>(A)</strong> is the definitive correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Fossiliferous shale</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The basal Talchir glacial tillites are almost entirely devoid of macrofossils due to the hostile polar/glacial environment, containing only rare reworked cold-climate monosaccate miospores (e.g., <em>Plicatipollenites</em>).</li>
        <li>Abundant fossiliferous shales (carbonaceous and coaly shales) only appear higher up in the succession within the overlying Barakar and Raniganj formations.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Glossopteris flora</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The characteristic <em>Glossopteris</em> seed-fern flora (comprising <em>Glossopteris, Gangamopteris</em>) flourished during the post-glacial warm, humid climate of the Artinskian-Kungurian stages.</li>
        <li>It reaches its peak abundance in the coal-bearing <strong>Barakar and Raniganj Formations</strong>. While very rare, primitive <em>Gangamopteris</em> appears in the uppermost transitional Talchir beds, the <em>base</em> of the Talchir sediments is physically marked by sterile glacial diamictite, not by plant flora.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) Talcher sandstone</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Sandstones occur as subordinate beds within the middle-to-upper Talchir Formation, but they do not form the basal marker.</li>
        <li>The base of the Gondwana sequence is physically and genetically defined by the <strong>Talchir Boulder Bed (glacial tillite)</strong>, not sandstone.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Stratigraphy of the Talcher Coalfield (Odisha)</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Stratigraphic Formation</th>
            <th>Thickness</th>
            <th>Primary Lithological Characteristics</th>
            <th>Paleoclimate & Economic Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mahadeva / Kamthi Formation</strong> (Triassic)</td>
            <td>$200-300\text{ m}$</td>
            <td>Ferruginous red sandstones, quartz pebble conglomerates.</td>
            <td>Warm semi-arid climate. Barren of coal.</td>
          </tr>
          <tr>
            <td><strong>Raniganj Formation</strong> (Late Permian)</td>
            <td>$150-250\text{ m}$</td>
            <td>Fine sandstones, carbonaceous shales, thin coal seams.</td>
            <td>Humid temperate. Subsidiary coal seams.</td>
          </tr>
          <tr>
            <td><strong>Ironstone Shale / Barren Measures</strong></td>
            <td>$100-200\text{ m}$</td>
            <td>Dark carbonaceous shales with siderite (ironstone) nodules.</td>
            <td>Stagnant lacustrine conditions. Devoid of workable coal.</td>
          </tr>
          <tr>
            <td><strong>Barakar Formation</strong> (Early Permian)</td>
            <td>$300-500\text{ m}$</td>
            <td>Coarse feldspathic sandstones, grey shales, thick coal seams (Seams I to VIII).</td>
            <td>Warm, humid, high-rainfall post-glacial swamps. <strong>Prime thermal coal repository of Odisha</strong>.</td>
          </tr>
          <tr>
            <td><strong>Talchir Formation</strong> (Late Carboniferous - Basal Permian)</td>
            <td>$50-150\text{ m}$</td>
            <td><strong>Basal Boulder Bed (tillite), greenish needle shales, varvites.</strong></td>
            <td><strong>Severe Polar Glacial to Periglacial climate.</strong> Base of Gondwana.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Gondwana Stratigraphy & Glaciology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Identification of Glacial Pavement Striations</div>
        <p>In 1872, Thomas Oldham discovered the famous Irai striated pavement on the banks of the Penganga River in Maharashtra. What does the orientation of glacial striae on the underlying Precambrian limestone pavement reveal?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The fine parallel scratches, grooves, and chattermarks etched onto the hard Neoproterozoic limestone pavement were carved by angular quartz pebbles dragged beneath the sliding basal sole of a grounded continental ice sheet. The azimuthal orientation of the striae ($010^\circ-190^\circ$, nearly NNE-SSW) demonstrates the exact <strong>paleo-ice flow direction</strong> of the Gondwana ice sheet moving north-northeastward across Peninsular India.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Clast-to-Matrix Ratio in Subglacial Tillites</div>
        <p>A core from the basal Talchir Boulder Bed reveals an unsorted diamictite where pebble and boulder clasts occupy $25\%$ of the total volume and do not touch each other. What sedimentological term describes this fabric, and what is its genetic origin?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>This is a <strong>matrix-supported diamictite (paraconglomerate)</strong>. In subglacial lodgement till and glaciomarine dropstone muds, sediment is transported en masse by ice without fluid sorting, depositing clasts suspended directly within an abundant, fine-grained rock-flour matrix without grain-to-grain contact.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Glaciomarine Marine Transgression in the Talchir</div>
        <p>Name the famous cold-water marine bivalve and gastropod fauna discovered within the upper Talchir beds in the Umaria and Manendragarh marine beds of central India.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong><em>Eurydesma</em> fauna</strong> (dominated by thick-shelled marine bivalves <em>Eurydesma mytiloides</em>, <em>Eurydesma hobartense</em>, and gastropod <em>Peruvispira</em>). This diagnostic fauna proves that during the melting of the ice sheet in the earliest Permian (Asselian), a brief marine transgression penetrated deep into the interior of the Indian craton via the Narmada and Damodar rift corridors.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Mechanical Origin of "Needle Shales"</div>
        <p>Why do the green silty shales of the Talchir Formation weather characteristically into slender, pencil-like prismatic needles?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Talchir needle shales possess extremely delicate, rhythmic, paper-thin primary horizontal laminations intersected at right angles by two closely spaced, mutually perpendicular conjugate sets of micro-tectonic joints. Upon subaerial desiccation and weathering, the rock fractures simultaneously along the horizontal bedding and vertical joint planes, disaggregating into characteristic polygonal needles.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Palynological Dating of the Talchir Formation</div>
        <p>Which distinctive fossil pollen group dominates the palynological assemblage of the Talchir Formation?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The assemblage is dominated by <strong>monosaccate pollen grains</strong> (e.g., <em>Plicatipollenites, Parasaccites, Potonieisporites</em>). These saccate pollen grains were produced by primitive gymnosperms (cordaitaleans and primitive conifers) adapted to survive cold, arid periglacial tundra winds.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Coalification Lag Following Glaciation</div>
        <p>Why are economic coal seams completely absent in the Talchir Formation, only appearing in the overlying Barakar Formation?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Coal formation requires luxuriant, high-density terrestrial forest growth and rapid biomass accumulation in subsiding anoxic wetlands. The polar, permafrost climate of the Talchir stage was too frigid to support dense arboreal forests. Only when the climate shifted to warm, humid temperate conditions during Barakar times could vast swamp forests of <em>Glossopteris</em> trees flourish and generate thick peat seams.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Dropstone Impact Deformation in Varves</div>
        <p>How does a sedimentologist conclusively distinguish an ice-rafted glacial dropstone from a normal river gravel pebble in a finely laminated mudstone?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>A true glacial dropstone displays distinct <strong>penetration and drape structures</strong>: as the rock falls from melting floating icebergs or lake ice, its kinetic impact violently pierces and downwarps the underlying soft laminations beneath it, while subsequent sediment laminations continuously drape over the top of the protruding boulder.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Tectonic Mechanism of Gondwana Basin Formation</div>
        <p>Explain the structural graben geometry that preserved the Talchir and overlying Gondwana sediments from subsequent erosion.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Gondwana sediments were deposited in actively subsiding, linear, fault-bounded <strong>half-grabens and grabens</strong> (e.g., Damodar, Son-Mahanadi, and Pranhita-Godavari troughs) controlled by intraplate extensional rifting along Precambrian sutures. Downfaulting continuously lowered the sedimentary pile below the regional base level, shielding the soft coal measures and basal Talchir tillites from Post-Mesozoic subaerial erosion.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 48, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q048_Talchir_Boulder_Bed_Basal_Gondwana_Glaciation_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q048: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q049: Tethyan Himalayan Muth Quartzite: Devonian Arthropod Trace Fossils
# ==============================================================================
def generate_q049():
    title = r"Q049: Tethyan Himalayan Stratigraphy: Muth Quartzite Devonian Arthropod Trace Fossils (Cruziana) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Paleozoic Ichnology"
    h1_title = "Q049: Muth Quartzite: Devonian Arthropod Trace Fossils (Cruziana)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 49<br>
<strong>Authoritative References:</strong> O.N. Bhargava & U.K. Bassi, <em>The Tethyan Himalayan Succession in Spiti</em> (Mem. Geol. Surv. India, Vol. 124, 1998, pp. 112–128); Adolf Seilacher, <em>Trace Fossil Analysis</em> (Springer-Verlag, 2007, Ch. 2: Cruziana Stratigraphy); S.V. Srikantia, <em>The Muth Quartzite: A Reappraisal of its Stratigraphic Position</em> (Jour. Geol. Soc. India, 1981); G.B. Mahapatra, <em>Textbook of Indian Stratigraphy</em> (pp. 172–175)."""

    part1 = r"""
  <!-- CARD 1: MUTH QUARTZITE GEOLOGY AND ENVIRONMENT -->
  <div class="card">
    <div class="card-header bg-blue">1. The Muth Quartzite: Regional Stratigraphic Marker of the Tethyan Himalayas</div>
    <div class="card-body">
      <p>The <strong>Muth Quartzite</strong> (named after the village of Muth in the Pin Valley of Spiti, Himachal Pradesh, by Ferdinand Stoliczka in 1865) represents the most conspicuous, widely traceable, and visually spectacular lithostratigraphic marker bed across the entire <strong>Tethyan Himalayan Paleozoic succession</strong> from Kashmir, Spiti, Kinnaur, and Garhwal to Nepal and Bhutan:</p>

      <ul>
        <li><strong>Lithological Characteristics:</strong> A remarkably uniform, massive, snow-white to light-grey, cliff-forming <strong>super-mature quartz arenite / orthoquartzite</strong> ($150-300\text{ m}$ thick). Composed of $>98\%$ monocrystalline quartz grains that are extremely well-rounded, well-sorted, and cemented by syntaxial siliceous quartz overgrowths, with secondary dolomitic and calcareous patches near the top.</li>
        <li><strong>Stratigraphic Position & Age:</strong> Overlies the Silurian Sanugba Group (Takche Formation coral limestones) and underlies the Lower Carboniferous Lipak Formation (fossiliferous crinoidal limestone). Its chronostratigraphic age is established as <strong>Early to Middle Devonian</strong>.</li>
        <li><strong>Depositional Setting:</strong> Represents high-energy coastal barrier-beach complexes, tidal shoals, and shallow subtidal-to-intertidal sand sheets deposited along the northern passive continental margin of eastern Gondwanaland facing the Paleo-Tethys Ocean.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q49/spiti_muth_quartzite_devonian_paleoenvironmental.png" alt="Spiti Muth Quartzite Paleogeography">
        <div class="tb-caption">
          <strong>Figure 49.1:</strong> Stratigraphic section and paleoenvironmental reconstruction of the Devonian Muth Quartzite in the Spiti Valley, showing the transition from Silurian shelf carbonates to pure quartz arenite tidal barrier complexes.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MAHAPATRA EXCERPT AND ARTHROPOD ICHNOLOGY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Arthropod Trace Fossils (Ichnofossils) in the Muth Quartzite</div>
    <div class="card-body">
      <p>Because intense wave agitation in high-energy quartz beach regimes destroyed delicate body fossils (shells and carapaces), the Muth Quartzite is almost devoid of macro-invertebrate body fossils. However, it preserves an outstanding and biostratigraphically diagnostic suite of <strong>arthropod trace fossils</strong>:</p>

      <div class="formula-card">
        <div class="formula-title">Diagnostic Arthropod Ichnofacies of the Muth Quartzite</div>
        $$\mathbf{Cruziana} \text{ (Locomotion/Feeding Burrow)} \quad \longleftrightarrow \quad \mathbf{Rusophycus} \text{ (Resting Excavation Nest)}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Constructed by benthic marine arthropods (trilobites, aglaspidids, or eurypterids) dragging paired appendages across shallow-water sand beds.</p>
      </div>

      <ul>
        <li><strong><em>Cruziana</em> (Ribbon-like Crawling Traces):</strong> Bilobed, furrowed crawling and feeding trails (pascichnia) showing distinctive chevron-patterned scratch marks made by the rhythmic digging of arthropod endopodites as they ploughed through the sand in search of detritus.</li>
        <li><strong><em>Rusophycus</em> (Resting Traces):</strong> Bilobed, coffee-bean shaped excavations (cubichnia) formed when the arthropod settled onto the sand bed and excavated a temporary resting burrow.</li>
        <li><strong><em>Diplichnites</em> & <em>Dimorphichnus</em>:</strong> Trackways composed of two parallel rows of individual walking dot/dash footprints produced during rapid locomotion.</li>
        <li><strong>Authoritative Classification:</strong> All these diagnostic trace fossils are created exclusively by the phylum <strong>Arthropoda</strong> (primarily Trilobita and primitive marine chelicerates).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q49/mahapatra_p173_spiti_muth_quartzite.png" alt="Mahapatra Muth Quartzite">
        <div class="tb-caption">
          <strong>Figure 49.2 (G.B. Mahapatra, p. 173):</strong> Textbook summary of the Muth Quartzite in Spiti, confirming its Devonian age and the classic occurrence of arthropod trace fossils.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF FOSSIL TYPES IN SPITI PALEOZOIC -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Paleozoic Fossil Succession of Spiti</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Formation</th>
            <th>Geological System / Age</th>
            <th>Dominant Rock Type</th>
            <th>Primary Fossil Content & Category</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lipak Formation</strong></td>
            <td>Early Carboniferous (Tournaisian-Visean)</td>
            <td>Crinoidal limestones and dolomites.</td>
            <td>Brachiopods (<em>Syringothyris cuspidata</em>), crinoids, rugose corals.</td>
          </tr>
          <tr>
            <td><strong>Muth Quartzite</strong></td>
            <td><strong>Early to Middle Devonian</strong></td>
            <td><strong>Snow-white, pure orthoquartzite.</strong></td>
            <td><strong>Arthropod Trace Fossils (<em>Cruziana, Rusophycus, Diplichnites</em>).</strong></td>
          </tr>
          <tr>
            <td><strong>Takche Formation</strong></td>
            <td>Silurian (Llandovery-Ludlow)</td>
            <td>Coralline limestones, calcareous mudstones.</td>
            <td>Tabulate corals (<em>Favosites, Halysites</em>), brachiopods (<em>Pentamerus</em>).</td>
          </tr>
          <tr>
            <td><strong>Shian Formation</strong></td>
            <td>Late Ordovician</td>
            <td>Reddish-brown quartzites and conglomerates.</td>
            <td>Brachiopods (<em>Orthis</em>), solitary corals.</td>
          </tr>
          <tr>
            <td><strong>Kunzum La Formation</strong></td>
            <td>Cambrian</td>
            <td>Greenish shales, siltstones, quartzites.</td>
            <td>Trilobite body fossils (<em>Redlichia noetlingi, Ptychoparia</em>).</td>
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
        <div class="q-num">Question 49</div>
        <div class="q-text">Which trace fossils are described from the Lower Devonian Muth Quartzite in Spiti, India ?</div>
        <div class="q-options">
          <div class="opt-node">(A) Nautilus</div>
          <div class="opt-node">(B) Unio</div>
          <div class="opt-node">(C) Pelecypod</div>
          <div class="opt-node correct">(D) Arthropod</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(D) Arthropod</strong> [The Muth Quartzite preserves diagnostic arthropod (trilobite/eurypterid) locomotion and resting trace fossils, specifically bilobed Cruziana and Rusophycus.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (D) Arthropod</div>
    <div class="card-body">
      <p><strong>Detailed Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>The <strong>Muth Quartzite</strong> of the Spiti Valley (Himachal Pradesh) is composed of mature, high-energy marine quartz arenite. Due to intense wave churning, calcareous shells of marine organisms were completely ground to sand; however, bedding surfaces preserve magnificent <strong>ichnofossils (trace fossils)</strong>.</li>
        <li>The dominant, world-renowned trace fossils documented from the Muth Quartzite are <em>Cruziana</em>, <em>Rusophycus</em>, and <em>Diplichnites</em> (Bhargava & Bassi 1998; Bagati & Thakur 1993; Seilacher 2007).</li>
        <li>In biological taxonomy, <em>Cruziana</em> (furrowed crawling/scratch trails) and <em>Rusophycus</em> (bilobed resting excavation nests) were produced by benthic <strong>Arthropods</strong> (specifically marine trilobites, eurypterids, or phyllocarid crustaceans) raking their paired walking appendages through the sand.</li>
        <li>Therefore, Option <strong>(D) Arthropod</strong> is the scientifically precise, definitive correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Nautilus</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><em>Nautilus</em> is a modern genus of coiled cephalopod molluscs (Class Cephalopoda). It represents a <strong>body fossil</strong> (calcareous shell), not a trace fossil.</li>
        <li>Furthermore, true <em>Nautilus</em> did not exist in the Devonian, and cephalopods do not make bilobed crawling trace burrows in sandstones.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Unio</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><em>Unio</em> is a genus of freshwater unionid bivalve molluscs that evolved much later in the Mesozoic and Cenozoic. It is a body fossil organism living in continental rivers and lakes, not a Paleozoic marine trace fossil.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Pelecypod</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Pelecypoda (Bivalvia) is a taxonomic class of molluscs having bivalved shells. While bivalves can produce resting traces (e.g., <em>Lockeia</em>), the primary diagnostic ichnogenus documented and classically celebrated from the Muth Quartzite is <strong><em>Cruziana</em></strong>, which is exclusively formed by <strong>arthropods</strong>, not pelecypods.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Ethological Classification of Trace Fossils (Ichnofossils)</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Ethological Category</th>
            <th>Biological Behavior</th>
            <th>Characteristic Ichnogenera</th>
            <th>Typical Producing Organism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Cubichnia</strong></td>
            <td>Resting traces made while stationary.</td>
            <td><strong><em>Rusophycus</em></strong>, <em>Lockeia</em>, <em>Asteriacites</em>.</td>
            <td><strong>Arthropods (Trilobites)</strong>, Bivalves, Ophiuroids (Brittle stars).</td>
          </tr>
          <tr>
            <td><strong>Pascichnia</strong></td>
            <td>Locomotion combined with active deposit-feeding.</td>
            <td><strong><em>Cruziana</em></strong>, <em>Helminthopsis</em>, <em>Phycosiphon</em>.</td>
            <td><strong>Arthropods</strong>, Deposit-feeding marine worms.</td>
          </tr>
          <tr>
            <td><strong>Repichnia</strong></td>
            <td>Pure directed crawling / walking locomotion traces.</td>
            <td><strong><em>Diplichnites</em></strong>, <em>Dimorphichnus</em>, <em>Cruziana</em>.</td>
            <td><strong>Arthropods</strong>, Gastropods, Vertebrates.</td>
          </tr>
          <tr>
            <td><strong>Fodinichnia</strong></td>
            <td>Subsurface semi-permanent feeding burrows.</td>
            <td><em>Thalassinoides</em>, <em>Planolites</em>, <em>Ophiomorpha</em>.</td>
            <td>Decapod crustaceans, polychaete annelids.</td>
          </tr>
          <tr>
            <td><strong>Domichnia</strong></td>
            <td>Permanent dwelling cylindrical tubes / borings.</td>
            <td><em>Skolithos</em>, <em>Arenicolites</em>, <em>Trypanites</em>.</td>
            <td>Suspension feeders, phoronids, tube-dwelling worms.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Ichnology & Tethyan Stratigraphy</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Distinguishing Cruziana from Rusophycus</div>
        <p>Explain the morphological and behavioral distinction between <em>Cruziana</em> and <em>Rusophycus</em> on a sandstone bedding plane.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong><em>Cruziana</em> (Pascichnia / Repichnia):</strong> Elongate, continuous, ribbon-like bilobed trail exhibiting a central longitudinal groove flanked by two lateral lobes covered in chevron-like scratch marks. Formed by an arthropod <em>actively crawling and ploughing forward</em> through sediment.</li>
          <li><strong><em>Rusophycus</em> (Cubichnia):</strong> Isolated, ovate to coffee-bean shaped, bilobed excavation nest reflecting the exact dimensions of the stationary organism. Formed when the arthropod <em>halted and dug itself into the substrate</em> for concealment or resting.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Seilacherian Ichnofacies of the Muth Quartzite</div>
        <p>Which standard Seilacherian marine ichnofacies is represented by the <em>Cruziana-Skolithos</em> assemblage in the Muth Quartzite, and what bathymetric zone does it define?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>It represents the <strong><em>Cruziana</em> Ichnofacies</strong> grading shoreward into the <strong><em>Skolithos</em> Ichnofacies</strong>. The <em>Cruziana</em> ichnofacies characterizes shallow subtidal continental shelf regimes situated between the daily fair-weather wave base and the storm wave base (water depths typically $5-50\text{ m}$), with moderate wave energy, fine-to-medium sand substrates, and abundant benthic nutrients.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Super-Maturity of Quartz Arenites</div>
        <p>The Muth Quartzite has a quartz index $>98\%$ and a rounded grain roundness index $>0.6$. What chemical and mechanical processes produce such super-mature quartz arenites?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Such extreme quartz purity requires: (1) Intensely warm, humid, tropical chemical weathering of the crystalline source landmass (destroying all unstable feldspars, micas, and ferromagnesians); (2) Prolonged eolian or polycyclic abrasion rounding the resistant quartz grains; and (3) Extensive marine beach and shoreface wave winnowing that completely strips out fine clay matrix.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Biostratigraphic Range of Cruziana</div>
        <p>Why can <em>Cruziana</em> serve as an effective biostratigraphic tool ("Cruziana Stratigraphy" of Adolf Seilacher) in Lower Paleozoic rocks devoid of body fossils?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Because the paired walking appendages (endopodites and exopodites) of trilobites underwent rapid morphological evolution throughout the Cambrian, Ordovician, Silurian, and Devonian, the precise angle, spacing, bundling, and symmetry of the claw scratches on the lobes of <em>Cruziana</em> change systematically through geological time, allowing species-level ichnostratigraphic biozonation.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Identification of the Type Locality of Muth Quartzite</div>
        <p>Where is the historical type section of the Muth Quartzite located, and who first designated it?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The type locality is situated near the village of <strong>Muth (Mudh)</strong> along the Pin River in the Spiti Valley, Lahaul & Spiti District of Himachal Pradesh. It was first named and described by the pioneering Austro-Czech paleontologist <strong>Ferdinand Stoliczka in 1865</strong>.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Overlying Carboniferous Formations in Spiti</div>
        <p>What formation directly overlies the Muth Quartzite in the Spiti Valley, and what major fossil group marks its base?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Muth Quartzite is conformably overlain by the <strong>Lipak Formation (Kanawar Group)</strong> of Early Carboniferous (Tournaisian-Visean) age. Its base is composed of dark, bituminous, fossiliferous limestones packed with the diagnostic spiriferid brachiopod <strong><em>Syringothyris cuspidata</em></strong> and crinoid columnals.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Preservation Potential of Trace Fossils vs. Body Fossils</div>
        <p>Why are trace fossils preserved in high-energy quartz arenites where body fossils are absent?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Body fossils are composed of soluble mineral phases (aragonite, calcite, chitin) that are easily dissolved by acidic pore waters or mechanically pulverized by surf waves in porous sands. In contrast, trace fossils are <strong>sedimentary structures</strong> (topographic reliefs in the rock fabric itself) cast by sand and cemented during diagenetic quartz syntaxial overgrowth, making them immune to post-depositional carbonate dissolution.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Tectonic Significance of the Muth Quartzite in Himalayan Geology</div>
        <p>In which structural-tectonic zone of the Himalayas does the Muth Quartzite occur: Sub-Himalaya, Lesser Himalaya, Higher Himalaya, or Tethyan Himalaya?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>It occurs exclusively within the <strong>Tethyan (Tibetan) Himalayan Zone</strong>, situated north of the Main Central Thrust (MCT) and Higher Himalayan Crystalline basement, bounded to the north by the Indus-Tsangpo Suture Zone (ITSZ).</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 49, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q049_Muth_Quartzite_Spiti_Devonian_Arthropod_Trace_Fossils_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q049: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q050: Jurassic Biostratigraphy: Ammonites as Index Fossils
# ==============================================================================
def generate_q050():
    title = r"Q050: Jurassic Biostratigraphy: Ammonites as Master Index (Zone) Fossils | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Invertebrate Paleontology & Biostratigraphy"
    h1_title = "Q050: Jurassic Biostratigraphy: Ammonites as Master Index Fossils"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 50<br>
<strong>Authoritative References:</strong> W.J. Arkell, <em>Jurassic Geology of the World</em> (Oliver & Boyd, Edinburgh, 1956); Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Pearson, Ch. 15: Biostratigraphy, pp. 520–535); Clarkson, <em>Invertebrate Palaeontology and Evolution</em> (4th Ed., Blackwell, Ch. 8: Cephalopods, pp. 240–265); G.B. Mahapatra, <em>Textbook of Physical Geology & Paleontology</em> (pp. 90–95, Fig. 91.4)."""

    part1 = r"""
  <!-- CARD 1: THE CONCEPT OF AN INDEX FOSSIL -->
  <div class="card">
    <div class="card-header bg-blue">1. Theoretical Criteria for an Ideal Index (Guide / Zone) Fossil</div>
    <div class="card-body">
      <p>In chronostratigraphy and biostratigraphy, an <strong>index fossil</strong> (or guide fossil / zone fossil) is a preserved organism used to define and identify specific geological periods and high-resolution biozones. To serve as an ideal index fossil, a biological taxon must rigorously fulfill five fundamental criteria:</p>

      <ul>
        <li><strong>1. Rapid Morphological Evolution:</strong> The lineage must undergo rapid speciation and morphological change over short geological intervals, resulting in <strong>extremely short vertical stratigraphic ranges (biochrons $<1-2\text{ Ma}$)</strong>.</li>
        <li><strong>2. Wide Cosmopolitan Geographic Distribution:</strong> The organism must have inhabited diverse marine provinces globally, independent of local bottom sediment facies (nektonic or planktonic pelagic mode of life).</li>
        <li><strong>3. Abundant Fossilization Potential:</strong> Possesses hard, durable mineralized shells (aragonite / calcite) produced in vast numbers that resist mechanical and chemical destruction.</li>
        <li><strong>4. Distinct Morphological Recognizability:</strong> Easily diagnosable morphologic features (e.g., shell coiling, ribbing, whorl cross-section, complex suture patterns) enabling unequivocal identification by field stratigraphers.</li>
        <li><strong>5. Facies Independence:</strong> Pelagic organisms float or swim in the water column and sink upon death into diverse substrates (muds, silts, carbonates), bridging correlations across differing sedimentary environments.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q50/jurassic_ammonite_biostratigraphy_zones.png" alt="Jurassic Ammonite Biostratigraphy">
        <div class="tb-caption">
          <strong>Figure 50.1:</strong> Ammonite biozonation chart of the Jurassic System illustrating rapid succession of ammonite species establishing ultra-high resolution biozones across Hettangian to Tithonian stages.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: AMMONITES IN THE JURASSIC -->
  <div class="card">
    <div class="card-header bg-indigo">2. Why Ammonites Are the Master Index Fossils of the Jurassic</div>
    <div class="card-body">
      <p>Ammonoids (Subclass Ammonoidea, Class Cephalopoda) represent the gold standard of index fossils for the entire Mesozoic, reaching their evolutionary zenith during the <strong>Jurassic Period</strong>:</p>

      <div class="formula-card">
        <div class="formula-title">The Arkellian Biostratigraphic Resolution</div>
        $$\text{Jurassic Duration } \approx 55\text{ Ma} \quad \div \quad \sim 60 \text{ Standard Ammonite Biozones} \implies \text{Resolution } \le 0.9\text{ Ma per Zone!}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">William Joscelyn Arkell (1956) established that ammonite biozones provide time resolution exceeding standard radiometric dating for Jurassic marine strata.</p>
      </div>

      <ul>
        <li><strong>Evolution of Complex Suture Lines:</strong> As ammonites evolved from simple nautilitic sutures (Paleozoic) to goniatitic, ceratitic (Triassic), and finally <strong>ammonitic sutures</strong> (Jurassic-Cretaceous), the septal margins became extraordinarily complex with intricately frilled, dendritic lobes and saddles. Each species possessed a distinct, immutable suture "fingerprint."</li>
        <li><strong>Nektonic Pelagic Buoyancy:</strong> Chambered phragmocones with siphuncular gas regulation enabled ammonites to swim freely across ocean basins, achieving global dispersal within months. Post-mortem shell drift further distributed shells across all oceanic facies.</li>
        <li><strong>The Kutch Jurassic Succession:</strong> In India, the famous Jurassic marine succession of <strong>Kutch (Patcham, Chari, Katrol, and Umia Formations)</strong> is correlated stage-by-stage (Bathonian to Tithonian) with the global standard using ammonite index genera (<em>Macrocephalites, Reineckeia, Gregoryceras, Virgatosphinctes</em>).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q50/mahapatra_fig91_4_ammonitic_sutures.png" alt="Ammonitic Sutures from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 50.2 (G.B. Mahapatra, Fig. 91.4):</strong> Evolution of cephalopod suture lines showing Nautilitic (smooth), Goniatitic (angular), Ceratitic (crenulated lobes), and Ammonitic (intricately frilled lobes and saddles) diagnostic of Jurassic ammonites.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARATIVE FOSSIL TYPES TABLE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Index Fossils vs. Other Fossil Categories</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Fossil Category</th>
            <th>Scientific Definition</th>
            <th>Stratigraphic / Paleoenvironmental Role</th>
            <th>Representative Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Index (Zone / Guide) Fossil</strong></td>
            <td>Short vertical geological range, wide geographic distribution, abundant, distinct.</td>
            <td><strong>Pinpoints exact chronostratigraphic age and defines biozones.</strong></td>
            <td><strong>Ammonites (Jurassic)</strong>, Graptolites (Ordovician-Silurian), Trilobites (Cambrian), Forams (Cenozoic).</td>
          </tr>
          <tr>
            <td><strong>Facies Fossil</strong></td>
            <td>Long geological range restricted to a very specific depositional environment.</td>
            <td>Indicates paleoenvironmental conditions (depth, salinity, energy) rather than age.</td>
            <td>Reef-building Corals (warm, shallow marine), Lingula (intertidal muds).</td>
          </tr>
          <tr>
            <td><strong>Trace Fossil (Ichnofossil)</strong></td>
            <td>Preserved tracks, trails, burrows, or borings reflecting organism behavior.</td>
            <td>Indicates ethology, sediment substrate coherence, and paleobathymetry.</td>
            <td><em>Cruziana, Rusophycus, Skolithos, Chondrites</em>.</td>
          </tr>
          <tr>
            <td><strong>Leaked Fossil (Infiltration)</strong></td>
            <td>Younger fossil washed down into cavities/fractures of older subterranean strata.</td>
            <td>Stratigraphic contamination that must be recognized to prevent false dating.</td>
            <td>Microfossils infiltrating paleokarst fissures or boreholes.</td>
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
        <div class="q-num">Question 50</div>
        <div class="q-text">Jurassic stratigraphy is primarily based on the use of ammonites as :</div>
        <div class="q-options">
          <div class="opt-node">(A) leaked fossil</div>
          <div class="opt-node correct">(B) index fossil</div>
          <div class="opt-node">(C) trace fossil</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) index fossil</strong> [Ammonites are the premier index (guide/zone) fossils of the Jurassic Period due to their rapid suture evolution, short stratigraphic ranges, cosmopolitan pelagic dispersal, and high preservation potential.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) index fossil</div>
    <div class="card-body">
      <p><strong>Detailed Biostratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>In historical geology and biostratigraphy (Arkell 1956; Boggs 2012; Mahapatra 2019), an <strong>index fossil</strong> (also termed guide fossil or zone fossil) is a fossil used to date and correlate the strata in which it is found.</li>
        <li>The ammonites (Subclass Ammonoidea) represent the ultimate index fossils for the Jurassic System because they exhibit:
          <ol>
            <li><strong>Exceptionally rapid morphological evolution</strong>, especially in their intricate ammonitic suture lines, shell ribbing, and whorl shapes.</li>
            <li><strong>Short vertical stratigraphic durations</strong> (individual species lived for only a few hundred thousand years).</li>
            <li><strong>Cosmopolitan, worldwide pelagic marine distribution</strong> as free-swimming nekton.</li>
          </ol>
        </li>
        <li>The standard global Jurassic chronostratigraphic timescale is subdivided into approximately 60 standard ammonite zones. Therefore, ammonites are used primarily and universally as <strong>index fossils</strong>.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) leaked fossil</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>A <strong>leaked fossil</strong> (or infiltration fossil) is a younger fossil that has percolated downward through subterranean fractures, solution cavities, or drillholes into older rock formations, representing an anomaly or stratigraphic contamination.</li>
        <li>Ammonites are authentic, primary, in-situ macrofossils of the Jurassic seas, not secondary leaked contaminants.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) trace fossil</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>A <strong>trace fossil</strong> (ichnofossil) represents indirect sedimentary evidence of biological activity—such as foot prints, crawling trails, resting excavations, or dwelling burrows (e.g., <em>Cruziana, Skolithos</em>).</li>
        <li>Ammonite fossils consist of the preserved physical shell, chambered septa, and siphuncle; they are bona fide <strong>body fossils</strong>, not trace fossils.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (B) index fossil is the universally established, textbook-verified role of ammonites in Jurassic stratigraphy, Option (D) is completely incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Classic Indian Mesozoic Index Fossils</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Geological System</th>
            <th>Premier Index Fossil Group</th>
            <th>Key Diagnostic Morphological Feature</th>
            <th>Classic Indian Stratigraphic Horizons</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Triassic</strong></td>
            <td><strong>Ceratitic Ammonoids</strong> & Conodonts</td>
            <td><strong>Ceratitic sutures</strong> (smooth rounded saddles, serrated denticulate lobes).</td>
            <td>Lilang Group (Spiti): <em>Otoceras woodwardi</em>, <em>Meekoceras</em>, <em>Ceratites</em>.</td>
          </tr>
          <tr>
            <td><strong>Jurassic</strong></td>
            <td><strong>Ammonitic Ammonoids</strong></td>
            <td><strong>Ammonitic sutures</strong> (both lobes and saddles are intricately frilled/dendritic).</td>
            <td>Kutch Succession: <em>Macrocephalites macrocephalus</em> (Chari), <em>Virgatosphinctes</em> (Katrol/Umia).</td>
          </tr>
          <tr>
            <td><strong>Cretaceous</strong></td>
            <td><strong>Ammonites</strong> & Planktonic Foraminifera</td>
            <td>Heteromorph ammonite coiling; globotruncanid chambers.</td>
            <td>Uttatur & Ariyalur (Cauvery): <em>Acanthoceras</em>, <em>Pachydiscus</em>, <em>Globotruncana</em>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Cephalopod Paleontology & Biozonation</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Suture Line Evolution Stages</div>
        <p>Outline the sequential evolutionary development of cephalopod suture lines from the Cambrian to the Cretaceous.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol>
          <li><strong>Nautilitic Suture (Cambrian - Present):</strong> Simple, smooth, straight or gently undulating line without fluting (e.g., <em>Nautilus</em>).</li>
          <li><strong>Goniatitic Suture (Devonian - Permian):</strong> Smooth, undivided angular lobes (pointing backward toward apex) and rounded saddles (pointing forward).</li>
          <li><strong>Ceratitic Suture (Triassic):</strong> Saddles are smooth and rounded, while lobes are denticulate, serrated, or saw-toothed (e.g., <em>Ceratites</em>).</li>
          <li><strong>Ammonitic Suture (Jurassic - Cretaceous):</strong> Maximum mechanical complexity; both lobes and saddles are deeply subdivided into intricate leaf-like or dendritic foliations (e.g., <em>Ammonites, Pachydiscus</em>).</li>
        </ol>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Functional Significance of Complex Ammonitic Sutures</div>
        <p>What mechanical advantage did the intricate fluting of ammonitic septal margins provide to the Jurassic ammonite shell?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The fluted septa met the outer shell wall at numerous corrugated contact lines, functioning like internal structural buttresses or corrugated bulkheads. This distributed hydrostatic crushing pressure evenly across the thin aragonitic shell wall, allowing the shell to remain extremely light and buoyant while resisting implosion at significant ocean depths.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: The Golden Spike (GSSP) of the Jurassic System</div>
        <p>Which ammonite species defines the Global Boundary Stratotype Section and Point (GSSP) for the base of the Jurassic System (Hettangian Stage)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The base of the Jurassic System is formally defined at Kuhjoch in the Karwendel Mountains of Austria by the first appearance datum (FAD) of the smooth-ribbed ammonite <strong><em>Psiloceras spelae tirolicum</em></strong>, marking the rapid post-extinction recovery of ammonites following the end-Triassic catastrophe.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Oppel's Concept of Biozones</div>
        <p>How did Albert Oppel (1856) use ammonites to invent modern biostratigraphy?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Albert Oppel carefully mapped the vertical ranges of ammonites across Western Europe and demonstrated that the Jurassic System could be subdivided into 33 discrete, universally reproducible time-stratigraphic intervals, which he named <strong>zones (Biozones)</strong>, each characterized by a distinct assemblage of co-occurring index ammonite species.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Macrocephalites in the Kutch Jurassic Succession</div>
        <p>In which formation of the Kutch Jurassic succession does the famous index ammonite <em>Macrocephalites macrocephalus</em> occur, and what European stage does it denote?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Macrocephalites macrocephalus</em> occurs at the base of the <strong>Chari Formation (Macrocephalus Beds)</strong> in Kutch, Gujarat. It marks the base of the <strong>Callovian Stage</strong> (Middle Jurassic), correlating the Kutch sequence with the standard European Callovian stratotype.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Siphuncle Position in Ammonoids vs. Nautiloids</div>
        <p>How does the position of the siphuncle allow a paleontologist to immediately distinguish an ammonite shell from a nautiloid shell?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Ammonoids:</strong> The siphuncle is strictly <strong>marginal and external (ventral)</strong>, running directly beneath the outer perimeter wall of the whorl (except in Clymeniida where it is dorsal).</li>
          <li><strong>Nautiloids:</strong> The siphuncle is <strong>central or sub-central</strong>, passing through the middle of each septum.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Heteromorph Ammonites in the Late Mesozoic</div>
        <p>What are <em>heteromorph ammonites</em>, and what evolutionary trend do they represent?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Heteromorph ammonites are ammonoids whose adult shells deviate from normal planispiral coiling—exhibiting open coils, helical spires, straight shafts, or hooked U-tubes (e.g., <em>Baculites, Scaphites, Hamites, Nipponites</em>). They represent specialized evolutionary radiations adapting to diverse nekto-planktonic and demersal marine ecological niches during the Late Jurassic and Cretaceous.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Taphonomy and Post-Mortem Ammonite Shell Drift</div>
        <p>Why can necroplanktic post-mortem shell drift cause minor taphonomic anomalies in ammonite biostratigraphy?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>When an ammonite dies, the decomposition of soft body tissues generates gas inside the chambered phragmocone. The empty shell can float on the surface of the ocean for weeks to months (necroplankton) and be carried hundreds of kilometers by surface wind and ocean currents before waterlogging and sinking. This enables exceptional cosmopolitan dispersal across ocean basins, but can occasionally transport shells into foreign depositional realms.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 50, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q050_Ammonites_Index_Fossils_Jurassic_Biostratigraphy_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q050: {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    generate_q046()
    generate_q047()
    generate_q048()
    generate_q049()
    generate_q050()
