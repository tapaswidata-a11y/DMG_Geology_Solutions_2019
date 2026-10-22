#!/usr/bin/env python3
"""
Q074 Generator: Dinoflagellate Biostratigraphy & Early Cretaceous Transgression in KG Basin
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q074():
    title = r"Q074: Dinoflagellate Biostratigraphy: Early Cretaceous Transgression in KG Basin | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Palynology & Basin Stratigraphy"
    h1_title = "Q074: Dinoflagellates: Early Cretaceous Marine Transgression in Krishna-Godavari Basin"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 74<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Ch. 15, pp. 510–514); Directorate General of Hydrocarbons (DGH), <em>Krishna-Godavari Basin Hydrocarbon Potential & Stratigraphic Atlas</em>; R. Garg, Khowaja-Ateequzzaman & K.P. Jain, "Early Cretaceous dinoflagellate cysts from Raghavapuram Mudstone, KG Basin" (<em>J. Palaeontol. Soc. India</em>); A. Kumar, "Palynostratigraphy of Upper Gondwana of East Coast basins" (<em>Geol. Surv. India Spec. Publ.</em>)."""

    part1 = r"""
  <!-- CARD 1: TECTONOSTRATIGRAPHY OF THE KRISHNA-GODAVARI (KG) BASIN -->
  <div class="card">
    <div class="card-header bg-blue">1. Tectonostratigraphy of the Krishna-Godavari (KG) Basin & the Mesozoic Transgression</div>
    <div class="card-body">
      <p>
        The <strong>Krishna-Godavari (KG) Basin</strong>, located along the eastern passive continental margin of peninsular India (Andhra Pradesh), is a polyhistory pericratonic rift and drift basin. It initiated during the <strong>Late Jurassic to Early Cretaceous breakup of Eastern Gondwana</strong>, when the Indian continental plate rifted and separated from East Antarctica and Australia (~135–120 Ma).
      </p>
      <p>
        During the early evolution of this passive margin, a series of NE–SW trending extensional horsts and grabens (e.g., Mandapeta Graben, Chintalapudi Sub-basin, Gudivada Graben) developed. As continental separation accelerated, marine waters from the nascent Indian Ocean flooded the subsiding rift valleys, culminating in a major, regionally extensive <strong>marine transgressive event during the Early Cretaceous (Aptian–Albian stages)</strong>.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q74/kg_basin_early_cretaceous_dinoflagellate_assemblage.png" alt="KG Basin Early Cretaceous Dinoflagellate Assemblage">
        <div class="figure-caption">
          <strong>Figure 74.1 — Early Cretaceous Dinoflagellate Cyst Assemblage and Stratigraphy in the KG Basin:</strong> Microphotographs and stratigraphic distribution of diagnostic marker dinocysts (including <em>Cassiculosphaeridia magna</em> and <em>Hystrichodinium voigtii</em>) establishing the marine flooding of the Raghavapuram Mudstone in the Krishna-Godavari Basin.
        </div>
      </div>

      <h4>The Mesozoic Lithostratigraphic Triad of the KG Basin</h4>
      <p>
        The classic Mesozoic sequence exposed in the Krishna-Godavari Basin comprises three conformable to paraconformable lithostratigraphic units:
      </p>
      <ul>
        <li><strong>Gollapalli Sandstone (Late Jurassic – Early Cretaceous / Neocomian):</strong> Basal syn-rift continental to deltaic sandstones, conglomerates, and minor clays deposited in fluvial channel and lacustrine systems. Dominated by terrestrial plant fossils and coniferous spore-pollen.</li>
        <li><strong>Raghavapuram Mudstone (Early Cretaceous / Aptian – Albian):</strong> The paramount marine transgressive shale unit! Consists of dark grey to carbonaceous, fissile marine shales, silty mudstones, and minor calcareous bands. It preserves a prolific assemblage of marine dinoflagellate cysts, ammonites, and marine bivalves, representing the prime syn-rift source rock of the basin.</li>
        <li><strong>Tirupati Sandstone (Late Cretaceous / Cenomanian – Campanian):</strong> Regressive, littoral to fluvio-deltaic ferruginous sandstones, grit, and conglomerates representing shoreface progradation over the drowning mudstone.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: DINOFLAGELLATE CYSTS AS CHRONOSTRATIGRAPHIC PROXIES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Dinoflagellate Cyst Biostratigraphy: Diagnostic Early Cretaceous Markers</div>
    <div class="card-body">
      <p>
        <strong>Dinoflagellates</strong> are unicellular, biflagellated eukaryotic protists (Phylum Dinoflagellata). During their sexual life cycle, many planktic marine species form a dormant, benthic resting cyst (<strong>dinocyst</strong>) composed of <em>dinosporin</em>—a complex, highly resistant, lipoidal biomacromolecule functionally analogous to sporopollenin.
      </p>
      <p>
        Because dinocysts resist non-oxidizing acids ($HCl$, $HF$), they survive severe diagenetic leaching that completely dissolves calcareous microfossils (foraminifera, nannoplankton). In the dark, dysoxic shales of the Raghavapuram Mudstone, dinoflagellate cysts provide absolute biostratigraphic resolution:
      </p>

      <h4>Diagnostic Early Cretaceous Marker Taxa</h4>
      <ul>
        <li><strong><em>Cassiculosphaeridia magna</em> Dave & Kumar (often cited as <em>magma</em> in exam papers):</strong> A proximate, spheroidal to subspheroidal dinocyst displaying an irregular reticulate/reticulocavate surface network and an apical archaeopyle. Strictly diagnostic of Aptian–Albian marine transgressive strata along the East Coast of India.</li>
        <li><strong><em>Hystrichodinium voigtii</em> (Alberti) Davey:</strong> A classic chorate (spinose) dinocyst bearing long, slender, distally pointed hollow processes radiating from a fibro-reticulate central body. A cosmopolitan Early Cretaceous marker characteristic of open-marine shelf waters from the Valanginian through Albian.</li>
        <li><strong>Associated Index Taxa:</strong> <em>Dingodinium cerviculum</em>, <em>Canningia colliveri</em>, <em>Circulodinium hirtellum</em>, <em>Odontochitina operculata</em>, <em>Cribroperidinium orthoceras</em>, and <em>Muderongia</em> spp.</li>
      </ul>

      <div class="formula-box">
        <strong>Transgressive Index Criterion:</strong><br>
        $$\text{Raghavapuram Transgressive Event} \iff \text{Dinocyst Acme } (C.\text{ magna} + H.\text{ voigtii}) + \text{D/S Ratio} > 0.65$$<br>
        $$\text{Chronostratigraphic Age} = \mathbf{Early\ Cretaceous\ (Aptian\ to\ Albian,\ \sim 125\text{--}100\ Ma)}$$
      </div>
    </div>
  </div>

  <!-- CARD 3: PALYNOFACIES & SEQUENCE STRATIGRAPHIC FLOODING SURFACES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Palynofacies, Maximum Flooding Surfaces & Hydrocarbon Source Potential</div>
    <div class="card-body">
      <p>
        In petroleum sequence stratigraphy, dinoflagellate cysts are the definitive tool for delineating <strong>Transgressive Systems Tracts (TST)</strong> and identifying <strong>Maximum Flooding Surfaces (MFS)</strong>:
      </p>
      <ul>
        <li><strong>The Dinocyst-to-Spore Ratio ($\text{D/S}$ Ratio):</strong> As the marine shoreline migrates landward during transgression, the relative abundance of terrestrial spore-pollen (derived from land plants) plummets, while marine dinocysts increase exponentially. The maximum peak in the $\text{D/S}$ ratio precisely identifies the condensed section and Maximum Flooding Surface within the Raghavapuram Mudstone.</li>
        <li><strong>Source Rock Kinetics:</strong> The transgressive marine shales of the Raghavapuram Formation contain high concentrations of hydrogen-rich <strong>Type II amorphous organic matter (AOM)</strong> derived from marine phytoplankton (dinoflagellates and prasinophytes). With Total Organic Carbon ($TOC$) values reaching $2.0\text{--}6.5\text{ wt}\%$ and Hydrogen Indices ($HI > 350\text{ mg HC/g TOC}$), this Early Cretaceous transgressive event generated the primary petroleum source beds charged into the Mandapeta and Ravva reservoirs.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 74</div>
        <div class="q-text">Dinoflagellate cysts like Cassiculosphaeridia magma, Hystrichodinium voigti etc. are important in establishing which age of transgressive event in the Krishna-Godavari Basin, India ?</div>
        <div class="q-options">
          <div class="opt-node">(A) Palaeocene</div>
          <div class="opt-node">(B) Jurassic</div>
          <div class="opt-node correct">(C) Early Cretaceous</div>
          <div class="opt-node">(D) Late Palaeocene</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (C)</div>
        <div><strong>Early Cretaceous:</strong> The dinocyst assemblage comprising <em>Cassiculosphaeridia magna</em> and <em>Hystrichodinium voigtii</em> is the diagnostic biostratigraphic marker for the Aptian–Albian (Early Cretaceous) marine transgression that deposited the Raghavapuram Mudstone in the Krishna-Godavari Basin.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Palaeocene — INCORRECT</div>
        <p>
          The Paleocene transgressive succession in the KG Basin is represented by the Palakollu Shale and basal Pasarlapudi Formation, deposited following Deccan volcanism. Its microplankton assemblage is characterized by typical Cenozoic marker dinocysts such as <em>Damassadinium californicum</em>, <em>Carpatella cornuta</em>, and <em>Senegalinium</em>, completely lacking the Mesozoic species <em>Cassiculosphaeridia magna</em> and <em>Hystrichodinium voigtii</em>.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Jurassic — INCORRECT</div>
        <p>
          In the KG Basin, Jurassic strata (represented by the lower Gollapalli Sandstone and subsurface Mandapeta Red Beds) are strictly non-marine, syn-rift continental deposits formed in fluvial-lacustrine settings. They contain terrestrial spore-pollen (e.g., <em>Classopollis</em>, <em>Callialasporites</em>, <em>Araucariacites</em>) but are devoid of marine dinoflagellate cysts, as marine waters had not yet breached the rift valley.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(C) Early Cretaceous — CORRECT</div>
        <p>
          The regional marine transgressive event that drowned the early rift system along the eastern coast of India occurred in the <strong>Early Cretaceous (Aptian to Albian stages, ~125–100 Ma)</strong>, depositing the hydrocarbon-prolific <strong>Raghavapuram Mudstone</strong>. Palynological investigations by Garg et al., Kumar, and ONGC/DGH firmly established that the acme of <em>Cassiculosphaeridia magna</em>, <em>Hystrichodinium voigtii</em>, <em>Dingodinium cerviculum</em>, and <em>Canningia</em> establishes this Early Cretaceous transgressive datum.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Late Palaeocene — INCORRECT</div>
        <p>
          The Late Paleocene (Thanetian stage) in the Tethyan and Indo-Pacific realms coincides with the Paleocene-Eocene Thermal Maximum (PETM). Its diagnostic palynological signature is an extraordinary global acme of the peridinioid genus <em>Apectodinium</em> (e.g., <em>Apectodinium augustum</em>, <em>A. homomorphum</em>), not Cretaceous gonyaulacoids.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Mesozoic–Cenozoic Stratigraphic & Palynological Framework of the Krishna-Godavari Basin</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Formation Name</th>
            <th>Geological Age</th>
            <th>Depositional Environment</th>
            <th>Diagnostic Palynomorph Assemblage</th>
            <th>Petroleum System Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Gollapalli Sandstone</strong></td>
            <td>Late Jurassic – Early Cretaceous (Neocomian)</td>
            <td>Fluvial, alluvial fan & lacustrine rift valleys</td>
            <td>Terrestrial spore-pollen: <em>Classopollis</em>, <em>Callialasporites</em>, <em>Microcachryidites</em>; no marine dinocysts</td>
            <td>Syn-rift Reservoir Rock</td>
          </tr>
          <tr>
            <td><strong>Raghavapuram Mudstone</strong></td>
            <td><strong>Early Cretaceous (Aptian – Albian)</strong></td>
            <td><strong>Shallow marine, prodelta to shelf (Major Transgression)</strong></td>
            <td><strong>Dinocysts:</strong> <em>Cassiculosphaeridia magna</em>, <em>Hystrichodinium voigtii</em>, <em>Dingodinium cerviculum</em></td>
            <td><strong>Primary Regional Source Rock & Top Seal</strong></td>
          </tr>
          <tr>
            <td><strong>Tirupati Sandstone</strong></td>
            <td>Late Cretaceous (Cenomanian – Campanian)</td>
            <td>Littoral, estuarine to shallow marine (Regression)</td>
            <td>Mixed terrestrial pollen and marginal-marine cysts: <em>Palaeoperidinium</em>, <em>Odontochitina costata</em></td>
            <td>Regional Reservoir Sandstone</td>
          </tr>
          <tr>
            <td><strong>Razole Volcanics</strong></td>
            <td>Late Cretaceous – Early Paleocene (66 Ma)</td>
            <td>Subaerial to shallow subaqueous basaltic lava flows</td>
            <td>Intertrappean fresh-to-brackish algae: <em>Botryococcus</em>, <em>Azolla</em></td>
            <td>Volcanic marker / tight unit</td>
          </tr>
          <tr>
            <td><strong>Palakollu Shale</strong></td>
            <td>Paleocene (Danian – Thanetian)</td>
            <td>Outer shelf to bathyal marine</td>
            <td>Cenozoic dinocysts: <em>Damassadinium</em>, <em>Glaphyrocysta</em>, <em>Apectodinium</em></td>
            <td>Post-rift Source Rock / Regional Seal</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- WORKED PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Analytical & Quantitative Practice Problems</div>
    <div class="card-body">

      <!-- Problem 1 -->
      <div class="p-card">
        <div class="p-header">Problem 1: Sequence Stratigraphic Maximum Flooding Surface (MFS) Quantitative Calculation</div>
        <p>
          In a deep exploration well in the KG Basin, palynological counts of 300 specimens per sample across a continuous core yielded the following terrestrial spore-pollen ($S$) and marine dinoflagellate cyst ($D$) counts:<br>
          - Depth 2,800 m: $S = 270, D = 30$<br>
          - Depth 2,850 m: $S = 180, D = 120$<br>
          - Depth 2,900 m: $S = 45, D = 255$<br>
          - Depth 2,950 m: $S = 150, D = 150$<br>
          - Depth 3,000 m: $S = 285, D = 15$<br>
          Calculate the Marine Inundation Index ($\text{MII} = \frac{D}{D+S} \times 100\%$) for each depth and identify the exact position of the Maximum Flooding Surface (MFS).
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Calculation:</strong><br>
          $$\text{MII} = \frac{D}{D+S} \times 100\%$$<br>
          - Depth 2,800 m: $\text{MII} = \frac{30}{300} \times 100\% = 10.0\%$ (Regressive / Highstand Systems Tract)<br>
          - Depth 2,850 m: $\text{MII} = \frac{120}{300} \times 100\% = 40.0\%$<br>
          - Depth 2,900 m: $\text{MII} = \frac{255}{300} \times 100\% = \mathbf{85.0\%}$ (Maximum Peak!)<br>
          - Depth 2,950 m: $\text{MII} = \frac{150}{300} \times 100\% = 50.0\%$ (Transgressive Systems Tract)<br>
          - Depth 3,000 m: $\text{MII} = \frac{15}{300} \times 100\% = 5.0\%$ (Lowstand / Fluvial Sandstone)<br>
          <strong>Conclusion:</strong> The <strong>Maximum Flooding Surface (MFS)</strong> is located precisely at <strong>2,900 meters</strong>, marked by an $85\%$ marine dinocyst peak reflecting maximum water depth and minimum clastic terrestrial dilution.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Morphogroup Classification: Chorate vs. Proximate Cysts</div>
        <p>
          Classify <em>Cassiculosphaeridia magna</em> and <em>Hystrichodinium voigtii</em> into their respective dinoflagellate cyst morphological archetypes (proximate, cavate, or chorate) and explain their paleoenvironmental implications regarding distance from shoreline.
        </p>
        <div class="p-ans">
          <strong>Morphological & Environmental Classification:</strong><br>
          1. <em>Cassiculosphaeridia magna:</em> A <strong>proximate cyst</strong>, formed in close contact with the original thecal wall, bearing low-relief reticulate ridges. Proximate cysts are typically dominant in inner neritic, protected shelf, or prodeltaic marine environments near the coast.<br>
          2. <em>Hystrichodinium voigtii:</em> A classic <strong>chorate cyst</strong>, characterized by a small central body ($25\text{--}35\ \mu\text{m}$) bearing long, radiating, spine-like processes ($15\text{--}25\ \mu\text{m}$) that held the cyst within the motile theca. Chorate cysts are buoyant adaptations for flotation in high-energy, open-marine outer neritic and pelagic shelf waters.<br>
          <strong>Environmental Synthesis:</strong> The co-occurrence of both morphogroups indicates an open-marine shelf inundation directly receiving marine microplankton while remaining within reach of fine terrigenous sediment influx.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: East Coast Geodynamics: Kinematics of Greater India Breakup</div>
        <p>
          Relate the Early Cretaceous Raghavapuram transgressive event in the KG Basin to the plate tectonic geodynamics of the Eastern Gondwana margin. What magnetic anomaly in the Bay of Bengal dates the onset of seafloor spreading?
        </p>
        <div class="p-ans">
          <strong>Plate Tectonic Derivation:</strong><br>
          1. <strong>Rifting Phase:</strong> During the Late Jurassic (Kimmeridgian–Tithonian, ~150 Ma), lithospheric extension between Greater India and East Antarctica (Enderby Land) created the Krishna-Godavari and Cauvery rift basins along ancient Eastern Ghats structural trends.<br>
          2. <strong>Breakup & Sea-Floor Spreading:</strong> Active seafloor spreading began in the Early Cretaceous, confirmed by seafloor magnetic anomaly <strong>$M_0$ (Early Aptian, ~125–120 Ma)</strong> and $M_2$–$M_4$ in the southern Bay of Bengal.<br>
          3. <strong>Thermal Subsidence & Transgression:</strong> The transition from active crustal necking to post-rift lithospheric thermal cooling induced rapid tectonic subsidence of the margin ($dZ_{\text{thermal}} \propto \sqrt{t}$), causing the Indian Ocean to drown the coastal grabens and depositing the marine Raghavapuram Mudstone.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Taphonomic Preservation: Why Dinocysts Outlast Foraminifera in Dysoxic Shales</div>
        <p>
          In organic-rich black shales of the Raghavapuram Formation, calcareous foraminifera are virtually absent, whereas dinoflagellate cysts are preserved in millions of specimens per gram. Provide the biogeochemical explanation for this selective preservation.
        </p>
        <div class="p-ans">
          <strong>Biogeochemical Explanation:</strong><br>
          1. <strong>Calcareous Vulnerability:</strong> In stagnant, restricted transgressive basins with high organic matter deposition, bacterial sulfate reduction ($2\text{CH}_2\text{O} + \text{SO}_4^{2-} \to \text{H}_2\text{S} + 2\text{HCO}_3^-$) and subsequent post-oxic organic decomposition produce high concentrations of carbonic and organic acids. Low porewater pH ($< 6.8$) dissolved the thin, metastable calcitic tests of planktic foraminifera.<br>
          2. <strong>Dinosporin Invariance:</strong> Dinoflagellate cysts are composed of <strong>dinosporin</strong>, an ultra-resistant, highly cross-linked, complex macromolecular network of aliphatic polycarbonates and aromatic ether bridges. Dinosporin is impervious to low pH, high $p\text{CO}_2$, and severe diagenetic leaching, allowing immaculate morphological preservation in black shales.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Palynofacies Analysis and Kerogen Type in the Raghavapuram Mudstone</div>
        <p>
          A transmitted-light palynofacies analysis of the Raghavapuram Mudstone yields $75\%$ fluffy, orange Amorphous Organic Matter (AOM), $20\%$ marine dinocysts, and $5\%$ inert black woody phytoclasts. Determine the Kerogen Type and evaluate its petroleum yield potential.
        </p>
        <div class="p-ans">
          <strong>Palynofacies Evaluation:</strong><br>
          - <strong>AOM and Dinocyst Dominance:</strong> High concentrations of marine phytoplankton-derived amorphous organic matter ($>70\%$) combined with dinoflagellate cysts and minimal terrestrial phytoclasts ($<10\%$) is the definitive petrographic signature of <strong>Type II Marine Sapropelic Kerogen</strong>.<br>
          - <strong>Petroleum Potential:</strong> Type II kerogen has an initial Hydrogen Index ($HI$) of $400\text{--}600\text{ mg HC/g TOC}$. Upon thermal maturation in the catagenetic zone ($T = 100\text{--}130^\circ\text{C}$), it possesses world-class generative potential for <strong>light paraffinic and naphthenic crude oil</strong> and associated rich gas.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Well-Log Correlation of the Raghavapuram Transgression</div>
        <p>
          On wireline logging suites, how is the Early Cretaceous Raghavapuram transgressive shale interval differentiated from the underlying Gollapalli Sandstone and overlying Tirupati Sandstone?
        </p>
        <div class="p-ans">
          <strong>Petrophysical Log Response:</strong><br>
          1. <strong>Gamma Ray (GR):</strong> Gollapalli and Tirupati sandstones display low gamma ray readings ($20\text{--}45\text{ API}$). In contrast, the Raghavapuram Mudstone displays a sharp, sustained "hot shale" gamma ray deflection ($90\text{--}180\text{ API}$) due to the concentration of uranium ($U$) adsorbed onto marine organic matter and thorium-potassium ($Th, K$) in detrital illite clays.<br>
          2. <strong>Resistivity ($R_t$):</strong> Low baseline in water-wet shales ($1\text{--}3\ \Omega\cdot\text{m}$), with elevated resistivity ($8\text{--}25\ \Omega\cdot\text{m}$) where mature hydrocarbons are actively generating within the shale matrix.<br>
          3. <strong>Sonic Transit Time ($\Delta t$):</strong> High acoustic slowness ($90\text{--}120\ \mu\text{s/ft}$) characteristic of undercompacted, high-porosity fissile marine shale.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Paleobathymetric Zonation using Dinocyst Associations</div>
        <p>
          How do micropaleontologists use the peridinioid-to-gonyaulacoid ratio ($P/G$ ratio) in Cretaceous dinocysts to track transgressive-regressive cycles?
        </p>
        <div class="p-ans">
          <strong>Paleoecological Principles:</strong><br>
          - <strong>Peridinioid Dinocysts ($P$):</strong> Predominantly heterotrophic microzooplankton that feed on marine diatoms. They proliferate in nutrient-rich, high-turbidity, upwelling or estuarine/inner neritic coastal waters.<br>
          - <strong>Gonyaulacoid Dinocysts ($G$, e.g., <em>Hystrichodinium</em>):</strong> Primarily autotrophic phototrophic algae that dominate clear, oligotrophic, open-ocean neritic and oceanic waters.<br>
          - <strong>Tracking Transgressions:</strong> During a marine transgressive phase, the $P/G$ ratio decreases as clear, open-shelf marine waters flood the basin. During regressive highstands and deltaic progradation, terrestrial nutrient runoff spikes, driving a sharp increase in the $P/G$ ratio.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Thermal Alteration Index (TAI) of Dinocyst Palynomorphs</div>
        <p>
          Palynological slides from an exploration well show <em>Cassiculosphaeridia</em> specimens with a dark golden-brown coloration (TAI 2.8). Correlate this value with the oil generation window and vitrinite reflectance.
        </p>
        <div class="p-ans">
          <strong>Thermal Calibration:</strong><br>
          - <strong>TAI 2.8:</strong> On Staplin's (1969) Thermal Alteration Index scale, a TAI of $2.6\text{--}3.0$ corresponds to a golden-brown to cinnamon-brown coloration of sporopollenin and dinosporin.<br>
          - <strong>Vitrinite Reflectance ($R_o$):</strong> Corresponds precisely to $R_o \approx 0.80\text{--}0.95\%$.<br>
          - <strong>Hydrocarbon Generation Window:</strong> Represents the <strong>Peak Oil Generation Window</strong>, confirming that the Raghavapuram source beds at this well location have undergone optimal thermal maturation and actively expelled liquid petroleum into adjoining sandstone reservoirs.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 74, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q074_Dinoflagellates_Early_Cretaceous_Transgression_KG_Basin_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q074: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q074()
