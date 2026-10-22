#!/usr/bin/env python3
"""
Q072 Generator: Brachiopods Dominance in Paleozoic Ecosystems
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q072():
    title = r"Q072: Brachiopoda: Paleozoic Ecosystem Dominance & Evolutionary Turnovers | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Invertebrate Paleontology & Paleoecology"
    h1_title = "Q072: Brachiopoda vs. Bivalvia: Paleozoic Ecosystem Hegemony"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 72<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (Ch. 9: Paleontology / Brachiopoda, pp. 180–186, 348); P.K. Mukherjee, <em>A Text Book of Geology</em> (Ch. 13: Paleontology, pp. 171–174); J. John Sepkoski Jr. (1981, <em>Paleobiology</em>, "A factor analytic description of the Phanerozoic marine fossil record"); E.N.K. Clarkson, <em>Invertebrate Palaeontology and Evolution</em> (Ch. 6: Brachiopods, pp. 139–178)."""

    part1 = r"""
  <!-- CARD 1: SEPKOSKI'S EVOLUTIONARY FAUNAS AND PALEOZOIC HEGEMONY -->
  <div class="card">
    <div class="card-header bg-blue">1. Sepkoski's Evolutionary Faunas & the Paleozoic Hegemony of Brachiopoda</div>
    <div class="card-body">
      <p>
        In macroevolutionary paleontology, the Phanerozoic marine biosphere is classified into <strong>Three Great Evolutionary Faunas</strong> (Sepkoski, 1981): the <em>Cambrian Fauna</em>, the <em>Paleozoic Fauna</em>, and the <em>Modern Fauna</em>. The <strong>Phylum Brachiopoda</strong>—specifically the articulate class <strong>Rhynchonelliformea</strong>—served as the crowning, dominant metazoan component of the <strong>Paleozoic Evolutionary Fauna</strong>.
      </p>
      <p>
        Following the <em>Great Ordovician Biodiversification Event (GOBE)</em>, articulate brachiopods radiated explosively, establishing undisputed numerical, ecological, and taxonomic supremacy across shallow-shelf, epicontinental, and slope benthic habitats worldwide. They formed extensive shell beds (coquinas and lumachelles) and served as the primary filter-feeding tier on Paleozoic seafloors, vastly outnumbering and out-diversifying molluscan bivalves throughout the Ordovician, Silurian, Devonian, and Carboniferous periods.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q72/mahapatra_p182_brachiopoda_paleozoic_dominance.png" alt="Brachiopoda Paleozoic Dominance and Stratigraphic Distribution from Mahapatra">
        <div class="figure-caption">
          <strong>Figure 72.1 — Stratigraphic Diversification and Paleozoic Hegemony of Brachiopods:</strong> Authentic textbook scan from G.B. Mahapatra (<em>A Text-Book of Geology</em>, p. 182). Illustrating the extraordinary radiation, morphological variety, and geological dominance of articulate brachiopod orders throughout the Paleozoic Era.
        </div>
      </div>

      <h4>Quantitative Macroevolutionary Comparison</h4>
      <ul>
        <li><strong>Paleozoic Era (Ordovician to Permian):</strong> Brachiopods comprised over <strong>4,500 fossil genera</strong> and tens of thousands of described species. In typical level-bottom benthic fossil assemblages, brachiopod shells outnumber bivalve shells by ratios often exceeding $20:1$ to $100:1$.</li>
        <li><strong>Mesozoic to Cenozoic Era:</strong> At the catastrophic <em>End-Permian Mass Extinction (251.9 Ma)</em>, articulate brachiopods suffered a catastrophic $>95\%$ species loss. Following this bottleneck, the <strong>Modern Fauna</strong> (spearheaded by Bivalvia and Gastropoda) radiated explosively during the Mesozoic Marine Revolution (MMR), while surviving brachiopod clades (Terebratulida and Rhynchonellida) were permanently marginalized into cryptic, bathyal, and polar marine refugia.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: COMPARATIVE FUNCTIONAL ANATOMY: BRACHIOPODA VS. BIVALVIA -->
  <div class="card">
    <div class="card-header bg-indigo">2. Comparative Functional Morphology: Brachiopoda vs. Bivalvia</div>
    <div class="card-body">
      <p>
        Although brachiopods and bivalves represent convergent solutions to the lifestyle of a bivalved, suspension-feeding benthic marine organism, their underlying body plans, symmetry axes, and feeding organs belong to entirely distinct bilaterian phyla (Lophotrochozoa / Lophophorata vs. Mollusca).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q72/mahapatra_fig91_1_brachiopoda_morphology.png" alt="Morphological Architecture of Brachiopod Valves and Symmetry from Mahapatra">
        <div class="figure-caption">
          <strong>Figure 72.2 — Morphological Anatomy and Symmetry Planes of Brachiopoda:</strong> Authentic textbook diagram from G.B. Mahapatra (<em>A Text-Book of Geology</em>, Fig. 9.1). Demonstrating the median symmetry plane bisecting both valves, the differentiation between Pedicle and Brachial valves, the hinge-line dentition, and the internal brachidium.
        </div>
      </div>

      <h4>The Fundamental Symmetry Criterion</h4>
      <div class="formula-box">
        <strong>Plane of Bilateral Symmetry:</strong><br>
        $$\text{Brachiopoda: } \text{Plane bisects each valve perpendicularly down the midline} \implies \mathbf{Inequivalve, Equilateral}$$<br>
        $$\text{Bivalvia: } \text{Plane passes between the two valves along the commissure} \implies \mathbf{Equivalve, Inequilateral}$$
      </div>

      <h4>Detailed Structural Contrast</h4>
      <ul>
        <li><strong>Feeding Mechanism:</strong>
          <ul>
            <li><em>Brachiopoda:</em> Filter feed using a specialized, ciliated, loop- or spiral-shaped organ called a <strong>lophophore</strong>, supported internally by a calcified skeletal ribbon termed the <strong>brachidium</strong>. Cilia generate an inhalant lateral water current and an exhalant median current.</li>
            <li><em>Bivalvia:</em> Filter feed using enlarged, folded respiratory gills termed <strong>ctenidia</strong> (lamellibranch gills), which capture organic particles and convey them via ciliated food grooves to labial palps.</li>
          </ul>
        </li>
        <li><strong>Valvular Nomenclature:</strong>
          <ul>
            <li><em>Brachiopoda:</em> Dorso-ventrally oriented. The larger ventral valve is the <strong>Pedicle Valve</strong> (giving exit to the fleshy attaching pedicle through a delthyrium or foramen); the smaller dorsal valve is the <strong>Brachial Valve</strong> (supporting the lophophore).</li>
            <li><em>Bivalvia:</em> Laterally oriented. Composed of a <strong>Right Valve</strong> and a <strong>Left Valve</strong> hinged dorsally by an elastic organic ligament and closing ventrally.</li>
          </ul>
        </li>
        <li><strong>Muscular System & Valve Operation:</strong>
          <ul>
            <li><em>Brachiopoda:</em> Closed actively by <strong>adductor muscles</strong>; opened actively by antagonistic <strong>diductor muscles</strong> pulling on the cardinal process posterior to the hinge axis. No elastic opening ligament exists.</li>
            <li><em>Bivalvia:</em> Closed actively by adductor muscles; opened <em>passively</em> by the mechanical elasticity and compression of the dorsal organic <strong>ligament</strong>.</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: ENERGETICS, PALEOECOLOGY & THE MESOZOIC TURNOVER -->
  <div class="card">
    <div class="card-header bg-emerald">3. Metabolic Energetics, Paleoecology & the Post-Paleozoic Displacement</div>
    <div class="card-body">
      <p>
        The dramatic replacement of brachiopods by bivalves across the Paleozoic-Mesozoic transition represents one of the classic debates in macroevolution: Was it direct ecological competition, or the result of differential survival and opportunistic radiation following a mass extinction filter?
      </p>

      <h4>Physiological Energetics and Metabolic Rates</h4>
      <p>
        Modern physiological studies (e.g., Rhodes & Thompson, 1993; Peck, 1996) demonstrate that brachiopods possess an exceptionally <strong>low metabolic rate</strong>—their oxygen consumption ($V_{O_2}$) is typically $2\text{ to }10\text{ times lower}$ than that of bivalves of equivalent biomass:
      </p>
      <ul>
        <li><strong>The Low-Energy Brachiopod Strategy:</strong> In the nutrient-limited, calm epicontinental seas of the Paleozoic, articulate brachiopods functioned as highly efficient, low-energy "energy misers". Their tissue content is exceptionally small relative to shell mass (often $>95\%$ shell by weight), enabling them to thrive in oligotrophic waters with minimal caloric intake.</li>
        <li><strong>The High-Energy Bivalve Engine:</strong> Bivalves possess dense, protein-rich muscular tissue, a muscular foot for active locomotion, and active ctenidial pumps. When primary productivity surged during the Mesozoic with the radiation of calcareous nannoplankton and dinoflagellates, bivalves utilized their superior filtration rates to out-grow and out-reproduce brachiopods.</li>
      </ul>

      <h4>The Mesozoic Marine Revolution (MMR) & Infaunal Escape</h4>
      <p>
        Articulate brachiopods are strictly <strong>epifaunal sessile organisms</strong>—they lack a muscular foot and cannot burrow into sediment once dislodged. During the Jurassic and Cretaceous periods, the radiation of shell-crushing predators (durophagous teleost fish, crustaceans, and marine reptiles) created intense predation pressure. Bivalves possessed the evolutionary flexibility to evolve deep infaunal siphonate burrowing (Mactracea, Tellinacea, Myacea), escaping benthic predation beneath the sediment-water interface, whereas brachiopods were vulnerable targets on the seafloor.
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 72</div>
        <div class="q-text">Brachiopods are considered more important than bivalves in , —________. due to their greater global diversity and greater abundance in many fossil assemblages.</div>
        <div class="q-options">
          <div class="opt-node">(A) Mesozoic ecosystems</div>
          <div class="opt-node">(B) Cenozoic ecosystems</div>
          <div class="opt-node correct">(C) Paleozoic ecosystems</div>
          <div class="opt-node">(D) Paleocene ecosystems</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (C)</div>
        <div><strong>Paleozoic ecosystems:</strong> Brachiopods reached their evolutionary zenith in the Paleozoic Era (Ordovician to Permian), dominating marine benthic diversity, biomass, and fossil assemblages prior to their catastrophic decimation at the End-Permian extinction.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Mesozoic ecosystems — INCORRECT</div>
        <p>
          Following the End-Permian extinction (251.9 Ma), the Phylum Brachiopoda never regained its former diversity or ecological dominance. In Mesozoic marine ecosystems (Triassic, Jurassic, Cretaceous), molluscan bivalves (such as inoceramids, oysters, rudists, and trigonians) radiated explosively to occupy primary benthic suspension-feeding niches, rendering brachiopods a subordinate faunal element.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Cenozoic ecosystems — INCORRECT</div>
        <p>
          In Cenozoic and modern oceans, bivalves are overwhelmingly dominant, comprising over 9,200 living species and dominating shallow coastal, intertidal, deep-sea, and freshwater realms. Brachiopods in the Cenozoic are rare, relict taxa (fewer than 400 living species) largely restricted to cold, deep, or cryptic marine environments (e.g., fiords, submarine caves, bathyal slopes).
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(C) Paleozoic ecosystems — CORRECT</div>
        <p>
          The <strong>Paleozoic Era</strong> represents the golden age of brachiopods. As members of Sepkoski's diagnostic <em>Paleozoic Evolutionary Fauna</em>, articulate brachiopods (Orders Orthida, Strophomenida, Pentamerida, Rhynchonellida, Spiriferida, and Productida) exhibited extraordinary morphological diversity, overwhelming numerical abundance, and pivotal reef-building and level-bottom community roles from the Early Ordovician through the Late Permian.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Paleocene ecosystems — INCORRECT</div>
        <p>
          The Paleocene is the earliest epoch of the Cenozoic Era (66.0 to 56.0 Ma). Paleocene benthic marine communities were completely dominated by modern molluscan bivalves following the End-Cretaceous (K-Pg) extinction event.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Systematic Comparison: Phylum Brachiopoda vs. Class Bivalvia (Mollusca)</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Diagnostic Parameter</th>
            <th>Phylum Brachiopoda</th>
            <th>Class Bivalvia (Phylum Mollusca)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Symmetry Plane</strong></td>
            <td><strong>Bilateral plane cuts down midline of both valves</strong>; Inequivalve, Equilateral</td>
            <td><strong>Bilateral plane lies between the two valves</strong>; Equivalve, Inequilateral</td>
          </tr>
          <tr>
            <td><strong>Valve Designation</strong></td>
            <td><strong>Pedicle Valve</strong> (Ventral) and <strong>Brachial Valve</strong> (Dorsal)</td>
            <td><strong>Right Valve</strong> and <strong>Left Valve</strong> (Lateral)</td>
          </tr>
          <tr>
            <td><strong>Feeding Organ</strong></td>
            <td>Ciliated <strong>Lophophore</strong> supported by calcified brachidium</td>
            <td>Enlarged ciliated gills (<strong>Ctenidia</strong>) with labial palps</td>
          </tr>
          <tr>
            <td><strong>Valve Opening Mechanism</strong></td>
            <td>Active contraction of <strong>diductor muscles</strong> on cardinal process</td>
            <td>Passive elastic expansion of compressed organic <strong>ligament</strong></td>
          </tr>
          <tr>
            <td><strong>Locomotion & Substrate Habit</strong></td>
            <td>Exclusively <strong>epifaunal sessile</strong>; anchored by fleshy pedicle or spines; no foot</td>
            <td><strong>Infaunal burrowers</strong> (muscular foot & siphons), epifaunal byssal clingers, cementing, or free-swimming</td>
          </tr>
          <tr>
            <td><strong>Metabolic Energetics ($V_{O_2}$)</strong></td>
            <td>Exceptionally low; low organic tissue/shell ratio; oligotrophic specialists</td>
            <td>High; active muscular pumping; thrives in nutrient-rich eutrophic waters</td>
          </tr>
          <tr>
            <td><strong>Peak Diversity & Dominance</strong></td>
            <td><strong>Paleozoic Era</strong> (Ordovician – Permian; >4,500 fossil genera)</td>
            <td><strong>Mesozoic – Cenozoic</strong> (Triassic – Recent; >9,200 living species)</td>
          </tr>
          <tr>
            <td><strong>Shell Mineralogy</strong></td>
            <td>Low-Mg calcite (Articulata) or organo-phosphatic chitin (Inarticulata)</td>
            <td>Aragonite, low-Mg calcite, or mixed bimineralic layers</td>
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
        <div class="p-header">Problem 1: Valve Symmetry and Axis Identification in Deformed Coquinas</div>
        <p>
          A field geologist collects a fossilized shell from a deformed Paleozoic limestone. The shell shows unequal valves where one valve has an apical perforation (foramen). When a plane is drawn perpendicular to the hinge line passing through the beak, the left and right halves of each valve are perfect mirror images. Classify this fossil into its phylum and distinguish its valves.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Morphological Deduction:</strong><br>
          1. <strong>Symmetry Analysis:</strong> The plane of bilateral symmetry bisects each valve down the midline, producing equilateral halves ($L_{\text{half}} = R_{\text{half}}$). This is the absolute hallmark of the <strong>Phylum Brachiopoda</strong> (in contrast to Bivalvia, where each single valve is inequilateral and asymmetrical).<br>
          2. <strong>Valvular Identification:</strong> Because the two valves are unequal (inequivalve), the larger valve with the apical foramen is the <strong>Pedicle Valve (Ventral Valve)</strong>, through which the fleshy pedicle emerged in life. The opposing smaller valve lacking the foramen is the <strong>Brachial Valve (Dorsal Valve)</strong>.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Diductor and Adductor Biomechanics in Articulate Brachiopods</div>
        <p>
          Derive the mechanical leverage governing valve opening in an articulate brachiopod. Let $F_{\text{did}}$ be the tension exerted by the diductor muscles attached to the cardinal process at distance $r_{\text{cp}} = 3\text{ mm}$ behind the hinge fulcrum, and let $F_{\text{res}} = 0.15\text{ N}$ be the hydrodynamic water resistance acting at the center of pressure $r_{\text{cpres}} = 15\text{ mm}$ anterior to the fulcrum. Calculate the minimum diductor force required to initiate valve gape.
        </p>
        <div class="p-ans">
          <strong>Torque Equilibrium Derivation:</strong><br>
          The hinge dentition (teeth and sockets) acts as a rigid class-1 lever fulcrum ($O$).<br>
          For rotational equilibrium about the hinge axis:<br>
          $$\sum \tau = 0 \implies \tau_{\text{diductor}} - \tau_{\text{resistance}} = 0$$<br>
          $$\tau_{\text{diductor}} = F_{\text{did}} \times r_{\text{cp}}$$<br>
          $$\tau_{\text{resistance}} = F_{\text{res}} \times r_{\text{cpres}}$$<br>
          Substituting values:<br>
          $$F_{\text{did}} \times 3\text{ mm} = 0.15\text{ N} \times 15\text{ mm}$$<br>
          $$F_{\text{did}} = \frac{0.15 \times 15}{3} = 0.15 \times 5 = 0.75\text{ N}$$<br>
          <strong>Conclusion:</strong> The diductor muscles must exert at least <strong>0.75 N</strong> of tensile force to crack open the valves against seawater resistance.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Shell Microstructure Classification: Impunctate, Punctate, Pseudopunctate</div>
        <p>
          Under petrographic thin-section microscopy, articulate brachiopod shells exhibit three distinct histological wall structures. Define impunctate, punctate, and pseudopunctate microstructures and cite one classic Paleozoic order representative of each.
        </p>
        <div class="p-ans">
          <strong>Histological Wall Microstructures:</strong><br>
          1. <strong>Impunctate:</strong> The solid calcitic secondary fibrous layer is continuous and completely devoid of perforations or internal rods (e.g., Order <em>Orthida</em>, <em>Rhynchonellida</em>).<br>
          2. <strong>Punctate:</strong> The calcitic shell is densely perforated by microscopic cylindrical tubules (caeca) extending from the mantle epithelium to near the outer surface, serving for respiration, nutrient storage, or chemical defense (e.g., Order <em>Terebratulida</em>).<br>
          3. <strong>Pseudopunctate:</strong> Lacks true open pores; instead, the fibrous layer contains microscopic sub-cylindrical rods of non-lamellar sparry calcite termed <em>taleolae</em>, which deflect surrounding growth lamellae into conical flexures (e.g., Order <em>Strophomenida</em>, <em>Productida</em>).
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Sepkoski's Factor Analysis & Mathematical Turnover Dynamics</div>
        <p>
          In Sepkoski's (1981) factor analytic model, three principal factors ($Q$-mode varimax factors) describe Phanerozoic family diversity. Factor 2 peaks strongly in the Middle Paleozoic ($F_2 > 0.85$) and plummets across the P-Tr boundary ($F_2 < 0.10$). Identify the faunal constituents of Factor 2 and explain why its diversity collapsed so abruptly compared to Factor 3 (Modern Fauna).
        </p>
        <div class="p-ans">
          <strong>Macroevolutionary Analysis:</strong><br>
          - <strong>Factor 2 Identity:</strong> Represents the <strong>Paleozoic Evolutionary Fauna</strong>, comprising Articulate Brachiopoda, Crinoidea, Anthozoa (Rugosa and Tabulata), Stenolaemate Bryozoa (Trepostomata, Cryptostomata), and Nautiloidea.<br>
          - <strong>Extinction Vulnerability:</strong> The End-Permian catastrophic volcanism caused widespread ocean anoxia, hypercapnia, and elevated sea surface temperatures ($>40^\circ\text{C}$). Members of the Paleozoic Fauna possessed heavy calcification, unbuffered internal coelomic fluids, and low physiological ventilation rates, making them exceptionally vulnerable to physiological acidosis. Conversely, the Modern Fauna (Factor 3: Bivalves, Gastropods, Malacostracans) possessed active respiratory circulation, muscular gills, and infaunal mobility, facilitating superior post-extinction recovery.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Metabolic Scaling & Energetic Advantage in Oligotrophic Waters</div>
        <p>
          A benthic ecologist measures the mass-specific oxygen consumption rate of a living articulate brachiopod (<em>Liothyrella</em>) at $0.012\text{ mg } O_2 \cdot \text{g}^{-1} \cdot \text{hr}^{-1}$ and that of an equivalent-sized bivalve (<em>Mytilus</em>) at $0.084\text{ mg } O_2 \cdot \text{g}^{-1} \cdot \text{hr}^{-1}$ under identical polar temperature ($0^\circ\text{C}$). Calculate the metabolic ratio and explain the evolutionary implication for Paleozoic epicontinental seas.
        </p>
        <div class="p-ans">
          <strong>Quantitative Evaluation:</strong><br>
          $$\text{Metabolic Ratio} = \frac{V_{O_2,\text{bivalve}}}{V_{O_2,\text{brachiopod}}} = \frac{0.084}{0.012} = 7.0$$<br>
          The bivalve consumes <strong>7 times more oxygen</strong> per unit tissue mass per hour than the brachiopod.<br>
          <strong>Ecological Significance:</strong> In the vast, stagnant, clear-water epicontinental epeiric seas of the Paleozoic (where terrestrial nutrient runoff was modest prior to the Devonian spread of deep-rooted land forests), nutrient flux was low. Brachiopods, requiring minimal metabolic maintenance, were energetic champions that easily outcompeted high-energy mollusks in oligotrophic level-bottom ecosystems.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Morphological Evolution of the Spiriferida Brachidium</div>
        <p>
          The Paleozoic brachiopod order <em>Spiriferida</em> is famous for its extended, wing-like cardinal extremities (strophic hinge line) and elaborate internal brachidium. Describe the geometrical structure of the spiriferid brachidium and explain its hydrodynamic function in suspension feeding.
        </p>
        <div class="p-ans">
          <strong>Structural & Functional Explanation:</strong><br>
          1. <strong>Spiralia Architecture:</strong> The brachidium of Spiriferida consists of two large, laterally directed calcareous spirals (<strong>spiralia</strong>) that occupy the wide transverse lateral wings of the shell.<br>
          2. <strong>Hydrodynamic Function:</strong> The spiral ribbons supported the long, ciliated lophophore. The coiled configuration drastically maximized the surface area of the ciliated feeding epithelium (often increasing filtration area by $>400\%$) without increasing body volume. Inhalant water currents were drawn in from both lateral margins and expelled as a unified, powerful exhalant jet along the median sulcus/fold, preventing the recycling of filtered, waste-laden seawater.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Brachiopod Spines in Productida: Paleoecological Anchoring</div>
        <p>
          Members of the Late Paleozoic Order <em>Productida</em> (e.g., <em>Productus</em>, <em>Gigantoproductus</em>) lacked a functional pedicle opening (delthyrium sealed) yet attained immense sizes on muddy Carboniferous seafloors. How did productids anchor themselves, and what role did hollow tubular spines play?
        </p>
        <div class="p-ans">
          <strong>Paleoecological Adaptation:</strong><br>
          1. <strong>Loss of Pedicle:</strong> Adult productids lost the functional fleshy pedicle entirely. The pedicle valve became highly convex and cup-shaped, while the brachial valve became flat or concave (concavo-convex shell).<br>
          2. <strong>Tubular Spines as Outriggers:</strong> The outer surface of the large pedicle valve secreted dozens of long, hollow, curved cylindrical calcitic <strong>spines</strong>. These spines acted as stabilizing snowshoes and outriggers, spreading the heavy shell's weight across unconsolidated, soft carbonate muds and preventing the coral/brachiopod from being smothered or flipped by bottom currents.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Taphonomy and Articulation State in Hydrodynamic Regimes</div>
        <p>
          In a sedimentary basin analysis, a shale bed yields articulate brachiopods preserved almost entirely with both valves tightly closed, whereas an overlying cross-bedded sandstone bed yields disarticulated, broken valves. Contrast the taphonomic and energy regimes of these two beds, citing the anatomical strength of the articulate hinge.
        </p>
        <div class="p-ans">
          <strong>Taphonomic & Anatomical Interpretation:</strong><br>
          - <strong>Articulate Hinge Mechanics:</strong> In articulate brachiopods (Rhynchonelliformea), interlocking calcified cyrtomatodont teeth in the pedicle valve fit deeply into sockets in the brachial valve, forming a mechanical joint that cannot be separated without fracturing the shell teeth.<br>
          - <strong>Shale Bed (Low-Energy / Rapid Burial):</strong> Closed, articulated valves indicate quiet, sub-wave-base deposition or rapid episodic smothering (obrution / tempestite mud blanket) where organisms were buried in life position without post-mortem transport.<br>
          - <strong>Sandstone Bed (High-Energy / Wave Reworking):</strong> Cross-bedded sandstone represents an energetic shoreface or channel environment where oscillatory wave shear stresses exceeded the shear strength of the calcified teeth, causing mechanical fragmentation, disarticulation, and sorting of skeletal bioclasts.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 72, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q072_Brachiopods_Dominance_Paleozoic_Ecosystems_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q072: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q072()
