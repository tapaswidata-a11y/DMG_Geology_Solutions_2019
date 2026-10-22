#!/usr/bin/env python3
"""
Masterclass Builder for Batch 5C: Vertebrate Paleontology & Chordate Evolution (Q061 - Q065)
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q061: Ordovician Vertebrate Fossils: Dermal Bone Structure & Aspidin
# ==============================================================================
def generate_q061():
    title = r"Q061: Early Vertebrate Evolution: Ordovician Ostracoderm Bone Structure (Aspidin) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Vertebrate Paleontology & Early Life"
    h1_title = "Q061: Early Vertebrates: Ordovician Bone Structure & Dermal Armor"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 61<br>
<strong>Authoritative References:</strong> Michael J. Benton, <em>Vertebrate Palaeontology</em> (4th Ed., Wiley-Blackwell, Ch. 2: Early Palaeozoic Fishes, pp. 28–45); Alfred S. Romer & Thomas S. Parsons, <em>The Vertebrate Body</em> (6th Ed., Saunders, Ch. 6: The Skeleton); Tor Ørvig, <em>Histologic Studies of Placoderms and Fossil Bone</em> (Arkiv för Zoologi, 1951); G.B. Mahapatra, <em>A Text-Book of Geology</em> (p. 360)."""

    part1 = r"""
  <!-- CARD 1: EARLIEST VERTEBRATE SKELETAL HISTOLOGY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Histological Recognition of Ordovician Vertebrates</div>
    <div class="card-body">
      <p>The dawn of the subphylum Vertebrata in the fossil record is heralded not by articulated skeletons, but by microscopic fragments of mineralized dermal armor. In early Paleozoic strata (specifically the Middle to Late Ordovician, $\sim 470-450\text{ Ma}$, such as the Harding Sandstone of Colorado and the Stairway Sandstone of Australia), jawless stem-vertebrates (ostracoderms like <em>Astraspis, Arandaspis</em>, and <em>Eriptychius</em>) are diagnosed with absolute certainty based on three convergent anatomical lines of evidence:</p>

      <ul>
        <li><strong>Brain Impressions & Cranial Cartilage:</strong> Internal natural casts and impressions of a distinct tripartite brain (forebrain, midbrain, hindbrain) preserved on the visceral surfaces of head shields.</li>
        <li><strong>Paired Sensory Capsules:</strong> Clear skeletal accommodation and impressions for paired visual orbits (eyes) and otic capsules (inner ears containing two semicircular canals).</li>
        <li><strong>Microscopic Bone Structure (Aspidin & Dentine):</strong> The definitive diagnostic hallmark is true <strong>bone structure</strong> (specifically acellular dermal bone known as <strong>aspidin</strong>, dentine tubercles, and basal lamellar bone), proving unequivocally that these organisms had evolved a biologically regulated calcium phosphate (hydroxyapatite) skeletal system.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q61/benton_fig2_ordovician_ostracoderm_bone_histology.png" alt="Ordovician Ostracoderm Bone Histology">
        <div class="tb-caption">
          <strong>Figure 61.1 (Michael J. Benton, Fig. 2.4):</strong> Histological cross-section of an Ordovician ostracoderm (<em>Astraspis</em>) dermal plate, showing the three classic layers: outer enameloid/dentine caps, middle vascular spongy aspidin bone, and basal compact lamellar bone.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: BONE TISSUE ARCHITECTURE -->
  <div class="card">
    <div class="card-header bg-indigo">2. Tripartite Architecture of Early Dermal Bone</div>
    <div class="card-body">
      <p>The dermal armor plates of Ordovician ostracoderms display an invariant three-layered microstructural organization:</p>

      <div class="formula-card">
        <div class="formula-title">The Classical Three-Layered Ostracoderm Exoskeleton</div>
        $$\mathbf{\text{Superficial Layer}} \text{ (Dentine/Enameloid Tubercles)} \quad \longleftrightarrow \quad \mathbf{\text{Middle Layer}} \text{ (Spongy Vascular Aspidin)} \quad \longleftrightarrow \quad \mathbf{\text{Basal Layer}} \text{ (Lamellar Isopedine)}$$
      </div>

      <ul>
        <li><strong>1. Superficial Layer:</strong> Capped by pointed, stellate tubercles composed of <strong>mesodentine</strong> or orthodentine, capped by a hypermineralized enameloid glaze.</li>
        <li><strong>2. Middle Vascular Layer:</strong> Highly porous cancellous bone riddled with interconnected vascular canals that housed cutaneous blood vessels and lateral line neuromast sensory canals. Composed of <strong>aspidin</strong>—a dense, unmineralized or acellular calcified collagenous matrix without osteocyte lacunae.</li>
        <li><strong>3. Basal Layer:</strong> Dense, horizontally stratified compact bone (isopedine) formed of stacked lamellae of collagen fibers impregnated with microcrystalline hydroxyapatite $\text{Ca}_5(\text{PO}_4)_3(\text{OH})$.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF EARLY CHORDATE TISSUES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Early Skeletal Tissues in Chordate Evolution</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Tissue Type</th>
            <th>Mineralogical Composition</th>
            <th>Cellular Structure</th>
            <th>Taxonomic Group Where First Evolved</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Aspidin (Acellular Bone)</strong></td>
            <td>Carbonated Hydroxyapatite ($65\%$) + Collagen ($35\%$)</td>
            <td>Devoid of cell bodies (osteocytes); canaliculi for Sharpey's fibers.</td>
            <td><strong>Ordovician Ostracoderms (<em>Astraspis, Arandaspis</em>).</strong></td>
          </tr>
          <tr>
            <td><strong>Cellular Bone</strong></td>
            <td>Hydroxyapatite + Collagen</td>
            <td>Contains osteocyte lacunae connected by dendritic canaliculi.</td>
            <td>Osteostracans (Silurian) and Gnathostomes.</td>
          </tr>
          <tr>
            <td><strong>Dentine</strong></td>
            <td>Hydroxyapatite ($70\%$) + Organic Matrix ($30\%$)</td>
            <td>Odontoblast tubules radiating from central pulp cavities.</td>
            <td>Ordovician dermal tubercles and conodont elements.</td>
          </tr>
          <tr>
            <td><strong>Cartilage</strong></td>
            <td>Unmineralized (Chondroitin sulfate + Collagen)</td>
            <td>Chondrocytes embedded in flexible avascular matrix.</td>
            <td>Basal chordates (lancelets, hagfishes, lampreys).</td>
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
        <div class="q-num">Question 61</div>
        <div class="q-text">It is possible to recognize vertebrate fossils as early as Ordovician on the basis of evidences of brain, paired sensory organs and_____.</div>
        <div class="q-options">
          <div class="opt-node">(A) anatomy</div>
          <div class="opt-node">(B) bodyparts</div>
          <div class="opt-node">(C) carbon dating</div>
          <div class="opt-node correct">(D) bone structure</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(D) bone structure</strong> [Ordovician vertebrates are formally recognized by the microscopic histology of their dermal armor plates, which display true bone structure (aspidin and dentine) surrounding the brain and sensory capsules.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (D) bone structure</div>
    <div class="card-body">
      <p><strong>Detailed Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In vertebrate paleontology (Benton 2014, Ch. 2; Romer & Parsons 1986; Janvier 1996), the earliest definitive diagnostic physical remains of vertebrates from the Ordovician period consist of bony dermal armor fragments.</li>
        <li>These fossils are identified as vertebrates through three correlated anatomical features:
          <ol>
            <li>Endocranial impressions of a differentiated <strong>brain</strong>.</li>
            <li>Skeletal capsules for <strong>paired sensory organs</strong> (eyes and inner ear otic capsules).</li>
            <li>Diagnostic microscopic <strong>bone structure</strong> (specifically cellular/acellular bone called aspidin with dentine tubercles and vascular canals).</li>
          </ol>
        </li>
        <li>Bone is a unique, exclusive biological tissue synthesized only by vertebrates; its presence in Ordovician rocks definitively identifies the specimen as a vertebrate.</li>
        <li>Therefore, Option <strong>(D) bone structure</strong> is the scientifically exact correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) anatomy</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>"Anatomy" is an overarching general term describing the bodily structure of all living things, from bacteria and corals to humans. It does not name a specific physical fossil tissue or skeletal material.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) bodyparts</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>"Bodyparts" is an informal, non-scientific vernacular term. Vertebrate identification requires precise cellular histological markers, not vague references to body parts.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) carbon dating</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Radiocarbon dating ($^{14}\text{C}$) has a half-life of only $5,730\text{ years}$ and is completely useless for rocks older than $\sim 50,000\text{ years}$.</li>
        <li>Applying carbon dating to Ordovician rocks ($\sim 450\text{ million years old}$) is physically impossible by four orders of magnitude.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Landmark Ordovician Vertebrate Localities</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Geographic Locality / Formation</th>
            <th>Geological Age</th>
            <th>Primary Ostracoderm Taxa</th>
            <th>Preserved Skeletal Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Harding Sandstone (Colorado, USA)</strong></td>
            <td>Late Ordovician (Caradoc / Sandbian)</td>
            <td><em>Astraspis desiderata</em>, <em>Eriptychius</em></td>
            <td>Tessellated polygonal bone plates, sensory grooves, braincase impressions.</td>
          </tr>
          <tr>
            <td><strong>Stairway Sandstone (Amadeus Basin, Australia)</strong></td>
            <td>Middle Ordovician (Darriwilian)</td>
            <td><em>Arandaspis prionotolepis</em></td>
            <td>Articulated dorsal and ventral dermal carapaces, branchial gill openings.</td>
          </tr>
          <tr>
            <td><strong>Tiñu Formation (Oaxaca, Mexico)</strong></td>
            <td>Early Ordovician (Tremadocian)</td>
            <td>Proto-conodont and ostracoderm dermal fragments</td>
            <td>Isolated dentine-tipped tubercles, early aspidin plates.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Early Vertebrate Evolution & Bone Histology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Hydroxyapatite vs. Calcium Carbonate in Shells</div>
        <p>Why did early vertebrates evolve a calcium phosphate (hydroxyapatite) skeleton rather than the calcium carbonate ($\text{CaCO}_3$) used by invertebrates (molluscs, brachiopods)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Vertebrates are active, high-metabolic animals that generate large amounts of lactic acid during anaerobic muscular exertion. Calcium carbonate ($\text{CaCO}_3$) readily dissolves under acidic conditions ($\text{pH} < 7$), which would cause skeletal dissolution. In contrast, <strong>calcium phosphate / hydroxyapatite [$\text{Ca}_5(\text{PO}_4)_3(\text{OH})$]</strong> is chemically stable at lower pH, resists lactic acidosis, and serves as an indispensable physiological metabolic buffer and phosphate reservoir.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Sharpey's Fibers in Ostracoderm Bone</div>
        <p>What are Sharpey's fibers and how do they appear in thin sections of fossil ostracoderm plates?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Sharpey's fibers are bundles of collagenous connective tissue that anchor the external dermal armor to the underlying subdermal muscles and connective tissue. In petrographic thin sections, they appear as microscopic unmineralized or mineralized radial tubules crossing the basal compact lamellae at right angles.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Conodont Elements Composition</div>
        <p>What are conodont elements, and why were they classified as vertebrates?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Conodonts are microscopic tooth-like feeding apparatuses ($0.1-2\text{ mm}$) composed of calcium phosphate (dahllite / fluorapatite). Histological studies revealed that conodont elements possess true cellular bone-like lamellar tissue and enameloid caps, while soft-bodied fossils from Granton (Scotland) revealed an eel-like animal with a notochord, chevron-shaped myomeres, and large paired eyes, proving conodonts are primitive jawless vertebrates.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Semicircular Canals in Ostracoderms</div>
        <p>How many semicircular canals did Ordovician ostracoderms possess in their inner ear, compared to modern jawed vertebrates?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Hagfishes:</strong> 1 semicircular canal.</li>
          <li><strong>Lampreys and Ostracoderms (Agnatha):</strong> <strong>2 semicircular canals</strong> (anterior and posterior), providing pitch and roll balance.</li>
          <li><strong>Gnathostomes (Jawed Vertebrates):</strong> <strong>3 semicircular canals</strong> (anterior, posterior, and horizontal), enabling full 3D spatial equilibrium.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Aspidin vs. Osteocyte Lacunae</div>
        <p>How does aspidin differ from normal haversian bone under high-magnification polarized light?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Aspidin is <strong>acellular bone</strong>. It contains criss-crossing collagen fiber bundles and vascular spaces, but is completely devoid of spider-like osteocyte cell bodies (lacunae) and their canaliculi. Normal Haversian bone contains concentric osteons centered around Haversian canals containing living osteocytes trapped within lacunae.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Origin of Jaws from Branchial Arches</div>
        <p>Which visceral branchial gill arch was modified during the transition from jawless ostracoderms to jawed gnathostomes to form the upper and lower jaws?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>first mandibular arch</strong> was modified: its dorsal element (epibranchial) evolved into the upper jaw (<strong>palatoquadrate cartilage</strong>), and its ventral element (ceratobranchial) evolved into the lower jaw (<strong>Meckel's cartilage</strong>). The second arch became the hyoid arch supporting the jaws.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Sensory Lateral Line Canal System</div>
        <p>What hydrodynamic function did the porous sensory grooves on <em>Astraspis</em> dermal plates perform?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The grooves housed the <strong>lateral line sensory system</strong>. Neuromast hair cells inside the canals detected micro-vibrations, water currents, and low-frequency pressure waves in the surrounding water, allowing the jawless fish to navigate in murky water and evade predatory giant eurypterids.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Harding Sandstone Depositional Realm</div>
        <p>In what depositional environment was the fossiliferous Harding Sandstone deposited?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Sedimentological structures (herringbone cross-bedding, tidal bundles, wave ripples) indicate an <strong>estuarine, intertidal to shallow nearshore marine environment</strong>, supporting the hypothesis that early vertebrate biomineralization originated in shallow coastal marine waters rather than fresh water.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 61, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q061_Ordovician_Vertebrates_Bone_Structure_Dermal_Armor_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q061: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q062: Chordate Morphology: Amphioxus Notochord Anterior Extension
# ==============================================================================
def generate_q062():
    title = r"Q062: Chordate Morphology: Amphioxus Cephalochordate Notochord Anterior Extension | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Comparative Chordate Anatomy & Evolution"
    h1_title = "Q062: Amphioxus: Cephalochordate Notochord Anterior Extension"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 62<br>
<strong>Authoritative References:</strong> Michael J. Benton, <em>Vertebrate Palaeontology</em> (4th Ed., Ch. 1: The Origin of Vertebrates, pp. 1–15); Alfred S. Romer & Thomas S. Parsons, <em>The Vertebrate Body</em> (Ch. 2: The Chordate Background); K.V. Kardong, <em>Vertebrates: Comparative Anatomy, Function, Evolution</em> (7th Ed., McGraw-Hill, Ch. 2); G.B. Mahapatra, <em>A Text-Book of Geology</em>."""

    part1 = r"""
  <!-- CARD 1: CEPHALOCHORDATE NOTOCHORD ANATOMY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Notochord of Amphioxus (Branchiostoma)</div>
    <div class="card-body">
      <p>The lancelet, popularly known as <strong>Amphioxus</strong> (genus <em>Branchiostoma</em>, Subphylum <strong>Cephalochordata</strong>), represents the classical archetype of the primitive chordate body plan. While sharing all five fundamental diagnostic chordate characteristics (notochord, dorsal hollow nerve cord, pharyngeal gill slits, endostyle, and post-anal tail), its notochord exhibits a unique and profound anatomical distinction from all true vertebrates:</p>

      <ul>
        <li><strong>Etymology and Definition:</strong> The subphylum name <strong>Cephalochordata</strong> is derived directly from Greek <em>kephale</em> (meaning "head") + <em>chorde</em> (meaning "string" or "cord"), which literally translates as <strong>“head-chordates”</strong>.</li>
        <li><strong>Anterior Extension Past the Brain:</strong> In <em>Amphioxus</em>, the notochord does not terminate beneath the brain as in vertebrates. Instead, it extends along the entire length of the animal to the <strong>extreme anterior end (tip of the snout / rostrum)</strong>, extending well beyond the anterior-most cerebral vesicle of the neural tube.</li>
        <li><strong>Hydrodynamic Burrowing Function:</strong> This extreme anterior extension serves a vital mechanical adaptation: when <em>Amphioxus</em> burrows forward into marine coarse sand, the stiff, hydrostatic notochord acts as a rigid pointed hydraulic battering ram, protecting the delicate front end of the nerve cord from compression injury.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q62/amphioxus_sagittal_notochord_anterior_rostrum.png" alt="Amphioxus Notochord Anatomy">
        <div class="tb-caption">
          <strong>Figure 62.1:</strong> Sagittal anatomical section of <em>Amphioxus</em> (Cephalochordata), showing the continuous hydrostatic notochord extending to the extreme anterior tip of the rostrum beyond the brain vesicle.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: CEPHALOCHORDATES VS CRANIATES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Anatomical Comparison: Cephalochordates vs. Vertebrates (Craniates)</div>
    <div class="card-body">
      <p>The anterior termination of the notochord marks the fundamental evolutionary divergence between invertebrates and craniate vertebrates:</p>

      <div class="formula-card">
        <div class="formula-title">The Rostral Notochord Boundary Condition</div>
        $$\text{Cephalochordates (Amphioxus): } \quad x_{\text{notochord}} \ge x_{\text{rostrum}} \quad (\text{Notochord extends past brain to extreme anterior})$$
        $$\text{Vertebrates (Craniata): } \quad x_{\text{notochord}} \le x_{\text{midbrain}} \quad (\text{Notochord stops at pituitary infundibulum / basicranium})$$
      </div>

      <ul>
        <li><strong>In True Vertebrates (Craniata):</strong> The notochord terminates anteriorly beneath the posterior part of the diencephalon / midbrain, directly behind the hypophysis (pituitary gland). The anterior cranium (ethmoid and orbital cartilage) develops independently from neural crest cells.</li>
        <li><strong>Muscularized Notochord in Amphioxus:</strong> Unlike the gelatinous, fluid-vacuolated notochord of vertebrate embryos, the notochord of <em>Amphioxus</em> is unique in consisting of disk-shaped, transversely stacked <strong>paramyosin muscle plates</strong> that can contract to adjust the stiffness of the rod during swimming!</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON TABLE OF CHORDATE SUBPHYLA -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: The Three Chordate Subphyla</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Subphylum</th>
            <th>Notochord Anterior Limit</th>
            <th>Persistence in Adult</th>
            <th>Cranium / Braincase</th>
            <th>Representative Genera</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Cephalochordata</strong> (Target)</td>
            <td><strong>Extends to extreme anterior tip of snout (rostrum).</strong></td>
            <td><strong>Persistent throughout life</strong> as primary axial support.</td>
            <td><strong>Absent</strong> (No cranium or tripartite brain).</td>
            <td><em>Branchiostoma</em> (Amphioxus), <em>Epigonichthys</em>.</td>
          </tr>
          <tr>
            <td><strong>Urochordata (Tunicata)</strong></td>
            <td>Confined exclusively to the larval tail; absent in trunk.</td>
            <td>Lost completely during metamorphosis into sessile adult.</td>
            <td><strong>Absent</strong>.</td>
            <td><em>Ascidia, Ciona, Salpa</em>.</td>
          </tr>
          <tr>
            <td><strong>Vertebrata (Craniata)</strong></td>
            <td>Terminates beneath midbrain/hindbrain behind pituitary.</td>
            <td>Replaced by cartilaginous or bony vertebral column (remnants as nucleus pulposus).</td>
            <td><strong>Present</strong> (True cartilaginous or bony skull).</td>
            <td>Hagfish, lampreys, fishes, amphibians, reptiles, mammals.</td>
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
        <div class="q-num">Question 62</div>
        <div class="q-text">The notochord of amphioxus differs from that of vertebrates by extending to the extreme _______ end of the body.</div>
        <div class="q-options">
          <div class="opt-node">(A) posterior</div>
          <div class="opt-node correct">(B) anterior</div>
          <div class="opt-node">(C) open</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) anterior</strong> [In Amphioxus (Cephalochordata), the notochord extends to the extreme anterior end of the body (tip of the snout), whereas in vertebrates it terminates behind the brain.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) anterior</div>
    <div class="card-body">
      <p><strong>Detailed Anatomical Forensic Analysis:</strong></p>
      <ul>
        <li>In comparative chordate anatomy (Benton 2014; Romer & Parsons 1986; Kardong 2015), the defining morphological characteristic of <em>Amphioxus</em> (Subphylum <strong>Cephalochordata</strong>) is that its notochord extends to the <strong>extreme anterior end</strong> of the body, protruding beyond the anterior tip of the nerve cord into the pointed rostrum.</li>
        <li>In contrast, in all true vertebrates (Craniata), the notochord terminates anteriorly beneath the midbrain/hindbrain, never reaching the front of the head.</li>
        <li>This anterior extension gives the cephalochordates their name (<em>cephalo-</em> = head) and provides structural rigidity for forward sand-burrowing.</li>
        <li>Therefore, Option <strong>(B) anterior</strong> is the definitive correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) posterior</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The notochord extends into the posterior tail in *both* vertebrates (embryos) and amphioxus.</li>
        <li>Extending to the posterior tail does not differentiate amphioxus from vertebrates; it is the unique extension to the extreme <strong>anterior</strong> rostrum that distinguishes it.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) open</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>"Open" is a nonsensical anatomical descriptor for the terminus of a skeletal rod. The notochord is enclosed within a continuous collagenous sheath.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (B) anterior is the precise textbook anatomical term, Option (D) is false.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Anatomical Distinctions Between Amphioxus and Vertebrates</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Anatomical Feature</th>
            <th><em>Amphioxus</em> (Cephalochordata)</th>
            <th>Vertebrata (Craniata)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Notochord Extent</strong></td>
            <td><strong>Extends to extreme anterior tip (rostrum).</strong></td>
            <td>Terminates beneath midbrain/pituitary.</td>
          </tr>
          <tr>
            <td><strong>Brain Differentiation</strong></td>
            <td>Simple anterior cerebral vesicle; unsegmented.</td>
            <td>Tripartite brain (Prosencephalon, Mesencephalon, Rhombencephalon).</td>
          </tr>
          <tr>
            <td><strong>Heart & Circulatory System</strong></td>
            <td>No single heart; contractile sinus venosus and pulsating bulbils.</td>
            <td>Multi-chambered muscular heart (atrium + ventricle).</td>
          </tr>
          <tr>
            <td><strong>Respiratory Organ</strong></td>
            <td>Pharyngeal slits used primarily for filter-feeding; skin respires.</td>
            <td>Gills or lungs dedicated to gas exchange with specialized capillary beds.</td>
          </tr>
          <tr>
            <td><strong>Excretory System</strong></td>
            <td>Segmental protonephridia with solenocytes (ciliated flame cells).</td>
            <td>Mesodermal kidneys (pronephros, mesonephros, or metanephros) with glomeruli.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Chordate Evolution & Comparative Anatomy</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Cambrian Chordate Ancestry (*Pikaia*)</div>
        <p>What Burgess Shale fossil from the Middle Cambrian of Canada is recognized as the earliest known stem-cephalochordate closely related to <em>Amphioxus</em>?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong><em>Pikaia gracilens</em></strong>. This ribbon-shaped, laterally compressed organism ($\sim 5\text{ cm}$ long) possesses a distinct dorsal notochord, a dorsal nerve cord, and over 100 zigzag chevron-shaped myomeres, demonstrating that cephalochordate-like ancestors had already radiated in the early Cambrian seas ($508\text{ Ma}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: The Endostyle and Thyroid Homology</div>
        <p>What homologous organ in adult vertebrates evolves from the ciliated mucus-secreting endostyle found in <em>Amphioxus</em> and larval lampreys?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>thyroid gland</strong>. In <em>Amphioxus</em>, the endostyle is a ventral pharyngeal groove that binds environmental iodine into iodinated tyrosine compounds to trap food. During vertebrate development, this iodine-binding epithelium invaginates to form the endocrine thyroid gland producing thyroxine ($\text{T}_4$) and triiodothyronine ($\text{T}_3$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Hydrostatic Stiffness of the Notochord</div>
        <p>Explain the physical mechanism that provides flexural stiffness to the chordate notochord without bone or cartilage.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The notochord consists of a core of tightly packed, fluid-engorged vacuolated cells surrounded by an outer acellular sheath of densely woven, helically wound <strong>collagen fibers</strong>. The osmotic absorption of water creates high internal hydrostatic turgor pressure. Because water is incompressible, the rod resists longitudinal shortening under muscle contraction while allowing lateral sinusoidal bending for undulatory swimming.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Neural Crest Cells and the "New Head" Hypothesis</div>
        <p>What embryological tissue, completely absent in <em>Amphioxus</em>, is responsible for forming the vertebrate skull, sensory capsules, and jaws (Gans & Northcutt "New Head" hypothesis)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong>Neural Crest Cells</strong>. In vertebrate embryos, neural crest cells migrate from the margins of the folding neural tube throughout the body to generate the cartilaginous cranium, jaw skeleton, sensory ganglia, melanocytes, and tooth dentine. The evolutionary emergence of neural crest cells transformed passive filter-feeders like amphioxus into active, predatory craniate vertebrates.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Nucleus Pulposus in Human Anatomy</div>
        <p>What anatomical structure in the adult human body represents the direct embryonic remnant of the notochord?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>nucleus pulposus</strong>—the gelatinous, shock-absorbing central core of each intervertebral disc in the human spine. Herniation of an intervertebral disc ("slipped disc") involves the rupture of the outer annulus fibrosus and extrusion of this ancient notochordal remnant.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Solenocytes vs. Glomerular Kidneys</div>
        <p>Why is the excretory system of <em>Amphioxus</em> considered non-vertebrate?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Amphioxus</em> excretes waste via ectodermally derived <strong>protonephridia with solenocytes</strong> (flagellated cells identical to the flame cells of flatworms and polychaetes) that discharge directly into the atrium. Vertebrates possess mesodermally derived nephric tubules with blood-filtering glomeruli, a completely independent evolutionary innovation.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: *Haikouichthys* and the Origin of Craniates</div>
        <p>How does the Early Cambrian fossil <em>Haikouichthys</em> from the Chengjiang Biota of China advance beyond the <em>Amphioxus</em> grade?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Unlike <em>Amphioxus</em>, <em>Haikouichthys</em> ($\sim 518\text{ Ma}$) exhibits a distinct <strong>cartilaginous head skeleton (cranium)</strong>, paired eyes, otic capsules, branchial arches supporting true gills, a dorsal fin with fin rays, and vertebral arcualia, establishing it as the world's oldest known craniate vertebrate.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Myomere Folding Geometry</div>
        <p>Contrast the shape of the myomeres (muscle blocks) in <em>Amphioxus</em> with those in teleost fishes.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In <em>Amphioxus</em>, the myomeres are simple V-shaped chevrons pointing anteriorly. In jawed fishes (teleosts and sharks), myomeres evolve into complex <strong>W-shaped 3D folded cones</strong> intersected by a horizontal connective tissue septum (dividing epaxial and hypaxial muscles), enabling powerful three-dimensional undulatory thrust.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 62, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q062_Amphioxus_Cephalochordata_Notochord_Anterior_Extension_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q062: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q063: Triadobatrachus: The Transitional Link to Modern Anura (Frogs)
# ==============================================================================
def generate_q063():
    title = r"Q063: Amphibian Evolution: Triadobatrachus as the Transitional Link to Modern Anura | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Vertebrate Paleontology & Amphibian Evolution"
    h1_title = "Q063: Triadobatrachus: The Transitional Link to Modern Anura"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 63<br>
<strong>Authoritative References:</strong> Michael J. Benton, <em>Vertebrate Palaeontology</em> (4th Ed., Ch. 4: Early Amphibians and Lissamphibians, pp. 100–106); Robert L. Carroll, <em>Vertebrate Paleontology and Evolution</em> (W.H. Freeman, Ch. 9); Jean Piveteau, <em>Une forme ancestrale des amphibiens anoures: Triadobatrachus massinoti</em> (Ann. Paleontol., 1937); G.B. Mahapatra, <em>A Text-Book of Geology</em>."""

    part1 = r"""
  <!-- CARD 1: THE DISCOVERY OF TRIADOBATRACHUS -->
  <div class="card">
    <div class="card-header bg-blue">1. Triadobatrachus: The "Protothecal" Bridge to Modern Frogs</div>
    <div class="card-body">
      <p>Among all three living orders of modern amphibians (Order <strong>Anura</strong> [frogs and toads], Order <strong>Urodela / Caudata</strong> [salamanders], and Order <strong>Gymnophiona / Apoda</strong> [caecilians]), the evolutionary transition from Paleozoic labyrinthodont/temnospondyl ancestors is notoriously obscured by the "lissamphibian gap". In global vertebrate paleontology, <strong>the only fossil that provides a direct morphological link between modern orders and Paleozoic amphibians</strong> is <strong><em>Triadobatrachus massinoti</em></strong>:</p>

      <ul>
        <li><strong>Discovery & Provenance:</strong> Discovered in 1936 by French paleontologist Jean Piveteau in the Early Triassic (Induan stage, $\sim 250\text{ Ma}$) marine Sakamena Group of northern Madagascar.</li>
        <li><strong>Transitional Evolutionary Significance:</strong> <em>Triadobatrachus</em> (literally "Triassic Frog") displays an exquisite intermediate mosaic anatomy, bridging primitive Paleozoic dissorophoid temnospondyls (e.g., <em>Doleserpeton</em> or <em>Gerobatrachus</em>) with advanced hopping anurans (modern frogs):
          <ul>
            <li><strong>Frog-Like (Derived) Characters:</strong> Broad, skull with large orbits, frontoparietals fused, T-shaped squamosal, edentulous lower jaw, toothless premaxilla, and an <strong>elongated forward-directed ilium</strong> attached to the sacrum.</li>
            <li><strong>Primitive (Paleozoic Temnospondyl) Characters:</strong> Retains a <strong>short tail composed of 6 distinct caudal vertebrae</strong> (modern frogs have zero tail vertebrae, fused into an internal rod called the <strong>urostyle</strong>); retains 14 presacral vertebrae (reduced to 8 or 9 in modern frogs); radius and ulna are separate (fused into a single radioulna in frogs); tibia and fibula are separate (fused into tibiofibula in frogs); hindlimbs are only moderately elongated, indicating it could not yet perform saltatorial (jumping) leaps.</li>
          </ul>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q63/triadobatrachus_fossil_and_skeletal_reconstruction.png" alt="Triadobatrachus Fossil and Skeleton">
        <div class="tb-caption">
          <strong>Figure 63.1 (Carroll 1988 / Piveteau 1937):</strong> Fossil mold and anatomical skeletal reconstruction of <em>Triadobatrachus massinoti</em>, illustrating the ancestral tail vertebrae, elongate ilium, and broad anuran skull.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MORPHOLOGICAL MOSAIC ANALYSIS -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Biomechanical Transition to Saltation (Jumping)</div>
    <div class="card-body">
      <p>Modern anurans are biomechanical specialists designed for explosive jumping and shock-absorbing landings. <em>Triadobatrachus</em> illustrates the step-by-step assembly of this body plan:</p>

      <div class="formula-card">
        <div class="formula-title">The Anuran Skeletal Transformation Cascade</div>
        $$\mathbf{\text{Paleozoic Temnospondyl}} \longrightarrow \mathbf{Triadobatrachus} \text{ (Tail + Elongate Ilium)} \longrightarrow \mathbf{\text{Crown Anura (Vieraella / Prosalirus)}} \text{ (Urostyle + Saltation)}$$
      </div>

      <ul>
        <li><strong>The Origin of the Urostyle:</strong> In modern frogs, the caudal vertebrae fuse into a long, rigid post-sacral rod called the <strong>urostyle (coccyx)</strong>, which braces the pelvis against the shock of landing. In <em>Triadobatrachus</em>, the tail vertebrae are shortened and reduced to six, but have not yet fused into a urostyle!</li>
        <li><strong>Pelvic Lengthening:</strong> The anteriorly directed elongation of the iliac blades represents the primary skeletal adaptation shifting thrust from lateral undulation to bilateral leg kicking.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON TABLE OF ANURAN EVOLUTION -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Temnospondyl vs. Triadobatrachus vs. Modern Frog</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Anatomical Feature</th>
            <th>Paleozoic Temnospondyl (e.g., <em>Doleserpeton</em>)</th>
            <th>Transitional <em>Triadobatrachus</em> (Early Triassic)</th>
            <th>Modern Anura (Frog / Toad)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Tail Skeleton</strong></td>
            <td>Long tail with $20-30+$ caudal vertebrae.</td>
            <td><strong>Short tail with 6 caudal vertebrae.</strong></td>
            <td><strong>Tail absent; vertebrae fused into a rigid Urostyle.</strong></td>
          </tr>
          <tr>
            <td><strong>Presacral Vertebrae Count</strong></td>
            <td>$20$ to $25$ vertebrae.</td>
            <td><strong>$14$ vertebrae.</strong></td>
            <td><strong>Drastically reduced to $8$ (or $9$) vertebrae.</strong></td>
          </tr>
          <tr>
            <td><strong>Ilium Orientation</strong></td>
            <td>Short vertical or posterodorsal blade.</td>
            <td><strong>Elongated forward parallel to vertebral column.</strong></td>
            <td>Extreme anterior elongation acting as pelvic shock-absorber.</td>
          </tr>
          <tr>
            <td><strong>Forearm (Radius & Ulna)</strong></td>
            <td>Two separate, distinct bones.</td>
            <td><strong>Separate radius and ulna.</strong></td>
            <td><strong>Fused into a single stout Radioulna.</strong></td>
          </tr>
          <tr>
            <td><strong>Shank (Tibia & Fibula)</strong></td>
            <td>Two separate, distinct bones.</td>
            <td><strong>Separate tibia and fibula.</strong></td>
            <td><strong>Fused into a single elongate Tibiofibula.</strong></td>
          </tr>
          <tr>
            <td><strong>Ankle Bones (Astragalus & Calcaneum)</strong></td>
            <td>Small polygonal tarsals.</td>
            <td>Slightly elongated.</td>
            <td><strong>Extremely elongated into extra leg levers (Tibiale & Fibulare).</strong></td>
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
        <div class="q-num">Question 63</div>
        <div class="q-text">The only fossil that provides a link beween any of the modern orders and Paleozoic amphibians is</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Triadobatrachus</div>
          <div class="opt-node">(B) Salamander hynobius</div>
          <div class="opt-node">(C) Rhipidistrian fish</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Triadobatrachus</strong> [Triadobatrachus massinoti from the Early Triassic of Madagascar is universally recognized as the sole fossil transitional link between modern anuran frogs and Paleozoic amphibians.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Triadobatrachus</div>
    <div class="card-body">
      <p><strong>Detailed Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In vertebrate paleontology (Benton 2014, Ch. 4, p. 102; Carroll 1988, p. 182; Colbert 2001), <strong><em>Triadobatrachus massinoti</em></strong> (from the Early Triassic of Madagascar) is classically celebrated as the <strong>only fossil providing a direct morphological link</strong> between any modern living amphibian order (Order Anura) and Paleozoic labyrinthodont/temnospondyl amphibians.</li>
        <li>It represents a stem-anuran (Salientia) that retains ancestral Paleozoic traits (a short tail of 6 vertebrae, 14 presacral vertebrae, unfused limb bones) while displaying derived modern frog traits (broad skull with large orbits, frontoparietals, and an elongated forward-directed ilium).</li>
        <li>Therefore, Option <strong>(A) Triadobatrachus</strong> is the singular correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Salamander hynobius</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><em>Hynobius</em> is an extant (living) genus of primitive Asiatic salamanders (Family Hynobiidae).</li>
        <li>It is a living modern animal, not a fossil transitional link between modern orders and Paleozoic amphibians.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Rhipidistrian fish</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Rhipidistians (e.g., <em>Eusthenopteron, Tiktaalik</em>) are lobe-finned sarcopterygian <em>fishes</em> that link fishes to the earliest tetrapods (such as <em>Acanthostega</em> and <em>Ichthyostega</em>) in the Devonian.</li>
        <li>They do not link modern amphibian orders (frogs/salamanders) to Paleozoic amphibians.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (A) is the famous, universally verified textbook answer, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Iconic Transitional Fossils in Vertebrate Evolution</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Transitional Fossil Genus</th>
            <th>Geological Age & Locality</th>
            <th>Ancestral Group</th>
            <th>Derived Modern Group</th>
            <th>Key Transitional Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong><em>Triadobatrachus</em></strong></td>
            <td><strong>Early Triassic (Madagascar)</strong></td>
            <td><strong>Paleozoic Temnospondyls</strong></td>
            <td><strong>Modern Anurans (Frogs)</strong></td>
            <td><strong>Frog-like skull and elongate ilium, but retains a short tail of 6 vertebrae.</strong></td>
          </tr>
          <tr>
            <td><strong><em>Tiktaalik roseae</em></strong></td>
            <td>Late Devonian (Canada)</td>
            <td>Sarcopterygian Fishes</td>
            <td>Early Tetrapods</td>
            <td>Fish scales and fin rays, but has a movable neck, wrist joints, and ribs.</td>
          </tr>
          <tr>
            <td><strong><em>Archaeopteryx lithographica</em></strong></td>
            <td>Late Jurassic (Solnhofen, Germany)</td>
            <td>Theropod Dinosaurs</td>
            <td>Modern Birds (Aves)</td>
            <td>Feathered wings, but retains teeth, clawed fingers, and a long bony tail.</td>
          </tr>
          <tr>
            <td><strong><em>Morganucodon</em></strong></td>
            <td>Late Triassic (Wales / China)</td>
            <td>Cynodont Therapsids</td>
            <td>Crown Mammals</td>
            <td>Double jaw joint (articular-quadrate and dentary-squamosal), diphyodont teeth.</td>
          </tr>
          <tr>
            <td><strong><em>Pakicetus</em> / <em>Ambulocetus</em></strong></td>
            <td>Early Eocene (Pakistan)</td>
            <td>Artiodactyl Ungulates</td>
            <td>Cetaceans (Whales)</td>
            <td>Four-legged terrestrial runner with pachyosteosclerotic whale-like ear bulla.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Amphibian Paleontology & Skeletal Specialization</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Pedicellate Teeth as a Lissamphibian Synapomorphy</div>
        <p>What unique tooth structure unites all modern amphibians (frogs, salamanders, caecilians) as a monophyletic clade (Lissamphibia)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong>Pedicellate bicuspid teeth</strong>. The tooth consists of a crown and a basal pedicel made of dentine, separated by an uncalcified fibrous ring of connective tissue. This allows the tooth crown to bend inward during prey ingestion while preventing prey escape.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: The Earliest True Jumping Frog</div>
        <p>What is the earliest known fossil frog that had fully evolved saltatorial jumping mechanics and a complete urostyle, and what is its age?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong><em>Prosalirus bitis</em></strong> from the Early Jurassic (Kayenta Formation of Arizona, $\sim 190\text{ Ma}$) and <strong><em>Vieraella herbsti</em></strong> from the Early Jurassic of Patagonia, Argentina. They possessed a fused urostyle, elongate hindlimbs, and fused radioulna and tibiofibula capable of modern jumping.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Fusion of Distal Limb Bones</div>
        <p>Why did frogs evolve fused bones in the forearm (radioulna) and lower leg (tibiofibula)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Jumping generates massive shear forces during takeoff, and landing subjects limbs to violent compressive shock. Fusing the radius with the ulna, and tibia with fibula, eliminates twisting and rotation between adjacent long bones, creating high-strength structural struts that prevent bone dislocation and fracture during impact.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Indian Fossil Frog Indobatrachus</div>
        <p>What famous fossil frog occurs abundantly in the Intertrappean beds of Malabar Hill and Worli in Mumbai, and what is its age?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong><em>Indobatrachus pusillus</em></strong> (Family Pelobatidae / Myobatrachidae). It occurs in millions of exquisitely preserved articulated skeletons within the dark, bituminous lacustrine Intertrappean shales of Mumbai, dated to the <strong>Early Eocene ($\sim 55\text{ Ma}$)</strong>.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Middle Ear Columella (Stapes) Evolution</div>
        <p>From which skeletal bone of rhipidistian fish did the amphibian middle ear bone (columella / stapes) evolve?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>hyomandibula</strong>. In lobe-finned fishes, the massive hyomandibula braced the jaw against the braincase. In land-dwelling amphibians, as the spiracle evolved into the tympanic middle ear cavity, the hyomandibula shrank into a slender, delicate rod (the stapes/columella) transmitting aerial sound vibrations from the tympanum to the inner ear.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Gerobatrachus hottoni ("The Frogmander")</div>
        <p>What is the phylogenetic significance of the Permian fossil <em>Gerobatrachus hottoni</em> discovered in Texas?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Nicknamed the "Frogmander" (Early Permian, $\sim 290\text{ Ma}$), <em>Gerobatrachus</em> displays a mosaic mixture of frog-like features (broad skull, large tympanic ear space) and salamander-like features (two fused ankle bones, long body), providing strong evidence that both frogs (Anura) and salamanders (Caudata) share a common ancestor among dissorophoid temnospondyls.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Absence of Ribs in Modern Anurans</div>
        <p>Why are thoracic ribs drastically reduced or absent in modern frogs?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Frogs ventilate their lungs via <strong>buccal-pump positive-pressure breathing</strong> (gulping air using the floor of the mouth) rather than rib-cage aspiration. Rigid ribs would add unnecessary weight and interfere with the shock-absorbing pelvic rotation during jumping and landing.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Urodela (Caudata) Fossil Record</div>
        <p>What is the oldest known crown-group salamander fossil, and does it retain a tail?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong><em>Karaurus sharovi</em></strong> from the Late Jurassic of Kazakhstan ($\sim 150\text{ Ma}$). Unlike anurans, all salamanders (extinct and living) retain a fully developed, long caudal vertebral column used for aquatic undulatory propulsion.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 63, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q063_Triadobatrachus_Transitional_Amphibian_Anura_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q063: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q064: Early Diapsid Reptiles: Petrolacosaurus and Araeoscelis
# ==============================================================================
def generate_q064():
    title = r"Q064: Early Reptile Evolution: Petrolacosaurus & Araeoscelis (Basal Diapsida) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Vertebrate Paleontology & Early Amniote Phylogeny"
    h1_title = "Q064: Early Diapsids: Petrolacosaurus & Araeoscelis Phylogeny"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 64<br>
<strong>Authoritative References:</strong> Michael J. Benton, <em>Vertebrate Palaeontology</em> (4th Ed., Ch. 5: Early Amniotes and Diapsids, pp. 118–124); Robert L. Carroll, <em>The Ancestry of Reptiles</em> (Phil. Trans. R. Soc. Lond. B, 1982); Robert R. Reisz, <em>Araeoscelidia and the Early Radiation of Diapsids</em> (Jour. Paleontol., 1981); G.B. Mahapatra, <em>A Text-Book of Geology</em>."""

    part1 = r"""
  <!-- CARD 1: THE BASAL DIAPSID RADIATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Origin of Diapsid Reptiles: The Araeoscelidia Clade</div>
    <div class="card-body">
      <p>The amniote class Reptilia is divided into major evolutionary lineages based on the architecture of the temporal region of the skull. The clade <strong>Diapsida</strong>—which gave rise to lizards, snakes, sphenodontians, crocodilians, pterosaurs, dinosaurs, and birds—is defined by the presence of <strong>two temporal openings (fenestrae)</strong> on each side of the skull behind the orbit (a superior/upper temporal fenestra and an inferior/lower temporal fenestra):</p>

      <ul>
        <li><strong><em>Petrolacosaurus kansensis</em> (Oldest Known Diapsid):</strong> Discovered in the Late Carboniferous (Pennsylvanian, Gzhelian, $\sim 305\text{ Ma}$) Garnett quarry of Kansas, USA, by H.H. Lane (described in detail by Robert R. Reisz in 1981). It is an agile, lizard-like carnivore ($\sim 40\text{ cm}$ long) with large eyes, slender gracile limbs, an elongated neck, and unequivocal upper and lower temporal fenestrae.</li>
        <li><strong>The Sister Genus <em>Araeoscelis</em>:</strong> The closest known relative of <em>Petrolacosaurus</em> in global paleontology is <strong><em>Araeoscelis</em></strong> (from the Early Permian Red Beds of Texas, described by S.W. Williston in 1910).</li>
        <li><strong>The Order Araeoscelidia:</strong> Together, <em>Petrolacosaurus</em> and <em>Araeoscelis</em> constitute the stem group <strong>Araeoscelidia</strong> (or Araeoscelida)—the most primitive, basal sister clade to all other diapsids (Eosuchia / Neodiapsida).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q64/petrolacosaurus_araeoscelis_diapsid_skeletons.png" alt="Petrolacosaurus and Araeoscelis Skeletons">
        <div class="tb-caption">
          <strong>Figure 64.1 (Reisz 1981 / Benton 2014):</strong> Comparative skeletal anatomy of basal diapsids: <em>Petrolacosaurus</em> (Late Carboniferous) and its closest relative <em>Araeoscelis</em> (Early Permian), illustrating the elongate cervical vertebrae and gracile limbs.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: SKULL FENESTRATION AND ANATOMY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Comparative Anatomy: Petrolacosaurus vs. Araeoscelis</div>
    <div class="card-body">
      <p>While sharing a close phylogenetic sister-group relationship, <em>Araeoscelis</em> displays specialized dietary adaptations compared to the generalized insectivorous <em>Petrolacosaurus</em>:</p>

      <div class="formula-card">
        <div class="formula-title">The Basal Diapsid Sister Relationship</div>
        $$\mathbf{\text{Clade Araeoscelidia:}} \quad \mathbf{Petrolacosaurus} \text{ (Carboniferous)} \quad \longleftrightarrow \quad \mathbf{Araeoscelis} \text{ (Permian)}$$
      </div>

      <ul>
        <li><strong>Skull Fenestration Evolution:</strong> <em>Petrolacosaurus</em> preserves the primitive complete diapsid condition with both upper and lower temporal openings wide open. In <em>Araeoscelis</em>, while the upper temporal fenestra remains open, the lower temporal opening has closed secondarily by expansion of the squamosal and jugal bones (euryapsid-like condition) to accommodate massive jaw-closing adductor musculature.</li>
        <li><strong>Dentition:</strong> <em>Petrolacosaurus</em> has slender, pointed teeth and two caniniform fangs for capturing active insects. <em>Araeoscelis</em> has broad, blunt, bulbous crushing teeth adapted for hard-shelled invertebrates (durophagy).</li>
        <li><strong>Postcranial Skeleton:</strong> Both genera possess uniquely <strong>elongated cervical vertebrae</strong> (neck vertebrae longer than dorsal vertebrae), slender humeri, and elongated tarsals.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF EARLY AMNIOTE GROUPS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Early Amniote Skull Architectures</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Amniote Skull Pattern</th>
            <th>Number of Temporal Fenestrae</th>
            <th>Bones Bounding the Openings</th>
            <th>Representative Genera & Lineages</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Anapsid</strong></td>
            <td><strong>Zero (0)</strong>; solid bony roof behind orbit.</td>
            <td>Postorbital, squamosal, jugal (unperforated).</td>
            <td><em>Hylonomus, Paleothyris</em> (Captorhinids, Pareiasaurs).</td>
          </tr>
          <tr>
            <td><strong>Synapsid</strong></td>
            <td><strong>One (1)</strong> lower temporal opening.</td>
            <td>Bounded above by Postorbital-Squamosal bar.</td>
            <td>Pelycosaurs (<em>Dimetrodon</em>), Therapsids $\to$ <strong>Mammals</strong>.</td>
          </tr>
          <tr>
            <td><strong>Diapsid</strong> (Target)</td>
            <td><strong>Two (2)</strong>; upper and lower openings.</td>
            <td>Upper (parietal-postorbital); Lower (postorbital-jugal-squamosal).</td>
            <td><strong><em>Petrolacosaurus, Araeoscelis</em></strong>, Lizards, Dinosaurs, Birds.</td>
          </tr>
          <tr>
            <td><strong>Euryapsid</strong></td>
            <td><strong>One (1)</strong> upper temporal opening (derived).</td>
            <td>Bounded below by Postorbital-Squamosal bar.</td>
            <td>Marine reptiles (Ichthyosaurs, Plesiosaurs).</td>
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
        <div class="q-num">Question 64</div>
        <div class="q-text">The closest known relative of Petrolacosaurus is —__.</div>
        <div class="q-options">
          <div class="opt-node">(A) Sphenodon</div>
          <div class="opt-node correct">(B) Araeoscelis</div>
          <div class="opt-node">(C) Hylonomous</div>
          <div class="opt-node">(D) Askeptosaurus</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) Araeoscelis</strong> [The Early Permian genus Araeoscelis is the closest known sister taxon to the Late Carboniferous Petrolacosaurus, uniting within the basal diapsid clade Araeoscelidia.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) Araeoscelis</div>
    <div class="card-body">
      <p><strong>Detailed Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In vertebrate paleontology and amniote systematics (Benton 2014, Ch. 5, p. 120; Carroll 1988; Reisz 1981), <strong><em>Petrolacosaurus</em></strong> is universally classified in the Order <strong>Araeoscelidia</strong>.</li>
        <li>The nominal genus and undisputed closest phylogenetic relative of <em>Petrolacosaurus</em> is <strong><em>Araeoscelis</em></strong> from the Early Permian of Texas.</li>
        <li>Both genera share unique synapomorphies: distinct cervical vertebral elongation, gracile limb ratios, specialized astragalus-calcaneum contacts, and primitive diapsid cranial construction.</li>
        <li>Therefore, Option <strong>(B) Araeoscelis</strong> is the precise, authoritative correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Sphenodon</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><em>Sphenodon</em> (the modern Tuatara of New Zealand) is a living rhynchocephalian diapsid belonging to the highly advanced crown-diapsid clade Lepidosauromorpha.</li>
        <li>While it retains a complete primitive diapsid skull, it is separated from <em>Petrolacosaurus</em> by hundreds of millions of years of evolution and belongs to a completely different sub-clade.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Hylonomous</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><em>Hylonomus lyelli</em> (Late Carboniferous of Joggins, Nova Scotia) is famously the oldest known stem-reptile, but it is an <strong>anapsid</strong> (with a completely solid temporal skull roof lacking fenestrae).</li>
        <li>It is not the closest relative of the diapsid <em>Petrolacosaurus</em>.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) Askeptosaurus</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><em>Askeptosaurus</em> is an aquatic marine reptile belonging to the Order Thalattosauria (Triassic), specialized for marine swimming with an elongate snout and paddle limbs. It is entirely unrelated to <em>Petrolacosaurus</em>.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Evolutionary Lineages Derived from Diapsida</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Diapsid Sub-Clade</th>
            <th>Diagnostic Skull / Anatomic Feature</th>
            <th>Major Living & Extinct Groups</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Araeoscelidia</strong> (Basal Diapsids)</td>
            <td>Elongate cervicals, primitive upper & lower fenestrae.</td>
            <td><strong><em>Petrolacosaurus</em>, <em>Araeoscelis</em></strong> (Carboniferous-Permian).</td>
          </tr>
          <tr>
            <td><strong>Lepidosauromorpha</strong></td>
            <td>Modified temporal bars (loss of lower bar in squamates).</td>
            <td>Lizards, Snakes, Amphisbaenians, Tuatara (<em>Sphenodon</em>).</td>
          </tr>
          <tr>
            <td><strong>Archosauromorpha</strong></td>
            <td>Antorbital fenestra and mandibular fenestra.</td>
            <td>Crocodilians, Pterosaurs, Dinosaurs, <strong>Birds (Aves)</strong>.</td>
          </tr>
          <tr>
            <td><strong>Sauropterygia / Ichthyopterygia</strong></td>
            <td>Modified secondarily into euryapsid marine skulls.</td>
            <td>Plesiosaurs, Pliosaurs, Ichthyosaurs.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Amniote Phylogeny & Reptilian Skull Architecture</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Functional Advantage of Temporal Fenestrae</div>
        <p>What physiological and mechanical advantage did the evolution of temporal fenestrae provide to early reptiles over solid-skulled anapsids?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol>
          <li>Provided open window space for the bulky <strong>adductor mandibulae (jaw-closing) muscles</strong> to bulge outwards during contraction, enabling stronger, faster biting.</li>
          <li>Provided secure, thickened bony margins (crests and arches) for muscle attachment with minimum skull weight.</li>
          <li>Reduced unnecessary bone mass, creating a light, agile skull suitable for rapid predation.</li>
        </ol>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: The Amniotic Egg Adaptations</div>
        <p>Name the four extraembryonic membranes of the amniotic egg that allowed early reptiles like <em>Petrolacosaurus</em> to conquer dry terrestrial environments.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Amnion:</strong> Encloses the embryo in a fluid-filled aquatic cushion, preventing desiccation.</li>
          <li><strong>Yolk Sac:</strong> Provides nutrient reserves for embryonic growth.</li>
          <li><strong>Allantois:</strong> Stores nitrogenous metabolic waste (uric acid) and acts as a respiratory organ.</li>
          <li><strong>Chorion:</strong> Outer membrane facilitating gas exchange ($\text{O}_2$ and $\text{CO}_2$) across the porous shell.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Loss of the Lower Temporal Bar in Squamates</div>
        <p>How did modern lizards modify the ancestral diapsid skull of <em>Petrolacosaurus</em> to achieve cranial kinesis?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Lizards lost the <strong>lower temporal bar (quadratojugal bone)</strong>, liberating the quadrate bone to swing freely (streptostyly). This enables cranial kinesis, allowing the jaws to open extraordinarily wide and align upper and lower teeth to grasp struggling prey.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Geological Formation of Petrolacosaurus</div>
        <p>In which rock unit was <em>Petrolacosaurus</em> discovered, and what unusual taphonomic setting preserved its delicate skeleton?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Preserved in the <strong>Rock Lake Shale Member (Stanton Formation)</strong> near Garnett, Kansas. The depositional environment was a stagnant, anoxic coastal lagoon or estuarine channel where fine muds buried complete skeletons away from scavengers and storm currents.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Secondary Euryapsid Condition in Araeoscelis</div>
        <p>Why did earlier paleontologists mistakenly classify <em>Araeoscelis</em> as a "protorosaur" or euryapsid rather than a diapsid?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Because the lower temporal fenestra in <em>Araeoscelis</em> was secondarily closed by the widening of the squamosal and jugal bones, leaving only the upper temporal opening visible. Detailed preparation by Reisz (1981) proved that its postcranial skeleton and upper fenestra are identical to <em>Petrolacosaurus</em>, establishing it as a secondarily modified diapsid.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Synapsid vs. Diapsid Competition in the Permian</div>
        <p>During the Late Carboniferous and Early Permian, which amniote lineage was the ecologically dominant terrestrial carnivore group: Diapsida or Synapsida?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong>Synapsida</strong> (the mammal-like reptiles / pelycosaurs such as <em>Dimetrodon, Sphenacodon, Edaphosaurus</em>) dominated terrestrial megafaunal niches ($>80\%$ of biomass). Early diapsids like <em>Petrolacosaurus</em> were minor, small-bodied, agile insectivorous components of the undergrowth, only achieving ecological dominance after the end-Permian extinction during the Triassic.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Distinction Between Captorhinids and Diapsids</div>
        <p>How does the skull of a captorhinid stem-reptile (e.g., <em>Captorhinus</em>) differ from <em>Petrolacosaurus</em>?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Captorhinus</em> possesses a heavy, completely unperforated <strong>anapsid</strong> skull without temporal openings, multiple rows of blunt crushing teeth on the jaw margins, and short, stocky, sprawling limbs, in contrast to the light, diapsid-fenestrated skull and gracile limbs of <em>Petrolacosaurus</em>.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Youngina and the Rise of Neodiapsids</div>
        <p>What is the phylogenetic position of the Late Permian fossil <em>Youngina capensis</em> relative to Araeoscelidia?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Youngina</em> (from the Karoo Basin of South Africa) is a primitive member of <strong>Neodiapsida</strong>. It represents the crownward evolutionary stage beyond the primitive Araeoscelidia, possessing the modernized skull structure that directly gave rise to archosaurs and lepidosaurs.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 64, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q064_Petrolacosaurus_Araeoscelis_Basal_Diapsids_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q064: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q065: Placoderms: Armored Jawed Fishes
# ==============================================================================
def generate_q065():
    title = r"Q065: Paleozoic Fish Evolution: Placoderms as Armored Jawed Fishes | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Vertebrate Paleontology & Paleozoic Icthyology"
    h1_title = "Q065: Placoderms: Armored Jawed Fishes of the Paleozoic"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 65<br>
<strong>Authoritative References:</strong> Michael J. Benton, <em>Vertebrate Palaeontology</em> (4th Ed., Ch. 3: Early Gnathostomes and Placoderms, pp. 50–65); John A. Long, <em>The Rise of Fishes: 500 Million Years of Evolution</em> (Johns Hopkins Univ. Press, Ch. 5); Alfred S. Romer, <em>Vertebrate Paleontology</em> (3rd Ed., Ch. 3); G.B. Mahapatra, <em>A Text-Book of Geology</em>."""

    part1 = r"""
  <!-- CARD 1: PLACODERM ANATOMY AND CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Placodermi: The Armored Kings of the Devonian Seas</div>
    <div class="card-body">
      <p>The class <strong>Placodermi</strong> (derived from Greek <em>plax</em> [genitive <em>plakos</em>], meaning "flat plate" or "tablet" + <em>derma</em>, meaning "skin") represents an extinct, highly diverse, and evolutionary pivotal group of <strong>armored jawed fishes</strong> that dominated global marine, estuarine, and freshwater ecosystems during the Silurian and Devonian periods ($\sim 440-359\text{ Ma}$):</p>

      <ul>
        <li><strong>Diagnostic Anatomical Hallmark:</strong> Placoderms are uniquely characterized by an extensive, heavily ossified <strong>dermal bony armor</strong> divided into two interlocking units:
          <ol>
            <li><strong>Head Shield (Cranial Carapace):</strong> Tightly sutured bony dermal plates enclosing the brain, sensory capsules, and jaws.</li>
            <li><strong>Thoracic Shield (Shoulder Carapace):</strong> A bony ring of dermal plates girdling the anterior trunk and enclosing the heart, gills, and pectoral fin bases.</li>
          </ol>
        </li>
        <li><strong>The Unique Cranio-Thoracic Neck Joint:</strong> Connecting the head shield to the thoracic shield is a unique, specialized ball-and-socket hinge joint (the <strong>cranio-thoracic articulation</strong>) formed by the paranuchal plate of the head and the anterior dorsolateral plate of the body. This permitted the head to tilt upward while the lower jaw dropped, creating a massive, terrifying gape.</li>
        <li><strong>True Jaws (Gnathostomata):</strong> Placoderms were among the earliest true <strong>gnathostomes (jawed vertebrates)</strong>, possessing formidable jaw arches equipped with self-sharpening, serrated dermal gnathal plates (shearing bone blades) that functioned like guillotine shears.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q65/placoderm_dunkleosteus_armored_jawed_fish.png" alt="Placoderm Dunkleosteus Skeleton">
        <div class="tb-caption">
          <strong>Figure 65.1 (John A. Long / Benton 2014):</strong> Complete skeletal anatomy of the apex arthrodire placoderm <em>Dunkleosteus terrelli</em> (Late Devonian), showing the heavy head and thoracic armor plates and the unique cranio-thoracic ball-and-socket neck joint.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: BITE FORCE AND DUNKLEOSTEUS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Biomechanics: The Apex Predator Dunkleosteus</div>
    <div class="card-body">
      <p>The ecological climax of placoderm evolution was reached in the Late Devonian (Famennian) with the giant arthrodire <strong><em>Dunkleosteus terrelli</em></strong> (Cleveland Shale of Ohio, USA):</p>

      <div class="formula-card">
        <div class="formula-title">Biomechanics of the Placoderm Four-Bar Linkage Jaw Mechanism</div>
        $$F_{\text{bite}} \approx 4,400\text{ N} \text{ (at tooth tip)} \quad \text{to} \quad >7,400\text{ N} \text{ (at rear blade)} \quad [P_{\text{pressure}} > 150\text{ MPa!}]$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">A four-bar linkage mechanism enabled <em>Dunkleosteus</em> to snap its jaws shut in just $20\text{ milliseconds}$ with a bite force rivaling <em>Tyrannosaurus rex</em> and large crocodilians, shearing through armored ammonites and sharks.</p>
      </div>

      <ul>
        <li><strong>Internal Fertilization & Viviparity:</strong> Spectacular fossil placoderms from the Gogo Formation of Western Australia (e.g., <em>Materpiscis attenboroughi</em>, "Attenborough's Mother Fish") preserve mineralized embryos inside the female body cavity attached by an umbilical cord, proving that placoderms invented <strong>internal fertilization and live birth (viviparity)</strong> $380\text{ million years ago}$!</li>
        <li><strong>Total Extinction:</strong> Placoderms suffered a complete, catastrophic mass extinction at the end-Devonian <strong>Hangenberg event ($\sim 359\text{ Ma}$)</strong>, leaving zero post-Devonian survivors.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON TABLE OF EARLY FISH CLASSES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: The Four Major Classes of Paleozoic Fishes</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Fish Class</th>
            <th>Jaw Status</th>
            <th>Exoskeleton / Armor Characteristics</th>
            <th>Primary Geologic Span</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Placodermi</strong> (Target)</td>
            <td><strong>Jawed (Gnathostomes)</strong>; shearing dermal gnathal plates.</td>
            <td><strong>Heavily armored head & thoracic shields with ball-and-socket neck joint.</strong></td>
            <td>Silurian to <strong>Late Devonian Extinction</strong>.</td>
          </tr>
          <tr>
            <td><strong>Agnatha (Ostracoderms)</strong></td>
            <td><strong>Jawless (Agnathans)</strong>; round sucker or filter mouth.</td>
            <td>Complete head shield of aspidin bone; no neck joint.</td>
            <td>Ordovician to Late Devonian.</td>
          </tr>
          <tr>
            <td><strong>Acanthodii ("Spiny Sharks")</strong></td>
            <td>Jawed; equipped with small teeth.</td>
            <td>Tiny diamond-shaped scales; stout spine in front of all fins.</td>
            <td>Silurian to Early Permian.</td>
          </tr>
          <tr>
            <td><strong>Chondrichthyes (Sharks & Rays)</strong></td>
            <td>Jawed; replaceable rows of enameloid teeth.</td>
            <td>Cartilaginous endoskeleton; skin covered in placoid denticles.</td>
            <td>Devonian to <strong>Present</strong>.</td>
          </tr>
          <tr>
            <td><strong>Osteichthyes (Bony Fishes)</strong></td>
            <td>Jawed; marginal tooth-bearing bones (maxilla, dentary).</td>
            <td>Opercular bone covering gills; ganoid/cycloid/ctenoid scales.</td>
            <td>Silurian to <strong>Present</strong> (dominant modern vertebrates).</td>
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
        <div class="q-num">Question 65</div>
        <div class="q-text">Placoderms are a particular assemblage of heavily __.</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Armord jawed fish</div>
          <div class="opt-node">(B) Benthonic fish</div>
          <div class="opt-node">(C) Plankton</div>
          <div class="opt-node">(D) Nekton</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Armord jawed fish</strong> [Placoderms are universally defined in vertebrate paleontology as an extinct group of heavily armored jawed fishes that flourished during the Silurian and Devonian.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Armord jawed fish</div>
    <div class="card-body">
      <p><strong>Detailed Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In vertebrate paleontology (Benton 2014, Ch. 3; Long 2011; Romer 1966), the Class <strong>Placodermi</strong> is universally defined as an assemblage of <strong>heavily armored jawed fishes</strong> (gnathostomes).</li>
        <li>The name *Placodermi* explicitly refers to the heavy armor plates (Greek *plakos* = flat plate, *derma* = skin) enclosing their head and thorax.</li>
        <li>Unlike the earlier ostracoderms (which were armored but *jawless*), placoderms possessed true functional jaws equipped with self-sharpening gnathal cutting plates.</li>
        <li>Therefore, Option <strong>(A) Armord jawed fish</strong> (spelled verbatim as in the official exam key) is the exact, definitive correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Benthonic fish</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>While some placoderm groups (like the antiarchs, e.g., <em>Bothriolepis</em>) lived on benthic substrates, many others (such as the giant arthrodire <em>Dunkleosteus</em>) were active pelagic apex predators swimming freely in the water column (nekton).</li>
        <li>More importantly, "benthonic" is an ecological lifestyle, not the fundamental defining taxonomic characteristic of the class Placodermi.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Plankton</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Plankton consists of passively drifting microscopic organisms (e.g., diatoms, radiolarians, foraminifera, larvae) unable to swim against ocean currents.</li>
        <li>Placoderms were massive, powerfully muscled predatory vertebrates reaching up to $8-10\text{ meters}$ in length; calling them plankton is biologically absurd.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) Nekton</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Although many placoderms were nektonic (active swimmers), the word "nekton" merely denotes swimming behavior and fails to identify them as fish, jawed vertebrates, or armored animals.</li>
        <li>Option (A) is vastly more precise and forms the standard textbook definition.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Major Orders of the Class Placodermi</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Placoderm Order</th>
            <th>Armor & Body Specialization</th>
            <th>Ecological Niche</th>
            <th>Representative Genera</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Arthrodira</strong> ("Jointed Neck")</td>
            <td>Ball-and-socket cranio-thoracic neck joint; scissor-like cutting gnathal blades.</td>
            <td>Active nektonic apex predators.</td>
            <td><strong><em>Dunkleosteus</em>, <em>Coccosteus</em></strong>.</td>
          </tr>
          <tr>
            <td><strong>Antiarchi</strong> ("Opposite Anus")</td>
            <td>Box-like thoracic carapace; pectoral fins encased in jointed crab-like armor tubes.</td>
            <td>Benthic bottom-feeders / sediment sifters in freshwater rivers and estuaries.</td>
            <td><strong><em>Bothriolepis</em>, <em>Asterolepis</em></strong>.</td>
          </tr>
          <tr>
            <td><strong>Ptyctodontida</strong></td>
            <td>Armor reduced; large eyes; crushing tooth plates; claspers in males.</td>
            <td>Mollusc crushers (durophagy); living birth documented (Gogo Formation).</td>
            <td><strong><em>Materpiscis</em>, <em>Austroptyctodus</em></strong>.</td>
          </tr>
          <tr>
            <td><strong>Rhenanida</strong></td>
            <td>Flattened body resembling modern stingrays; mosaic of small polygonal tubercles.</td>
            <td>Benthic ambush predators camouflaged on sandy sea beds.</td>
            <td><strong><em>Gemuendina</em></strong>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Paleozoic Icthyology & Evolutionary Innovations</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Absence of True Replacement Teeth</div>
        <p>How did the biting plates of placoderms differ from the teeth of modern sharks and bony fishes?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Placoderms lacked true polyphyodont replacement teeth anchored in dental laminae (like shark conveyor-belt teeth). Instead, their jaws were lined with <strong>dermal gnathal plates</strong> (supragnathals and infragnathals) made of dense, compact bone and dentine that grew by basal accretion. As the jaws opened and closed, the plates rubbed against each other, continuously self-sharpening their cutting edges like industrial shears.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Gogo Formation 3D Acid Preparation</div>
        <p>Why does the Late Devonian Gogo Formation of Western Australia preserve the world's most spectacular placoderm fossils?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Placoderms were buried in deep, anoxic inter-reef basins within calcareous concretions. The limestone nodules prevented mechanical flattening by compaction. When paleontologists dissolve the limestone matrix using dilute ($10\%$) acetic acid, the uncrushed, 3-dimensional calcium phosphate bones are revealed in pristine anatomical perfection, preserving delicate braincases, muscle tissues, nerve canals, and embryos.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Discovery of Pelvic Claspers</div>
        <p>What reproductive organ discovered in male ptyctodontid and arthrodire placoderms demonstrated copulatory behavior in the Paleozoic?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Male placoderms possessed paired, cartilaginous and dermal-bone-covered <strong>pelvic claspers</strong> extending backward from the pelvic girdle. These functioned as intromittent organs to transfer sperm into the female reproductive tract, proving internal fertilization evolved over $380\text{ Ma}$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: *Bothriolepis* Worldwide Biostratigraphy</div>
        <p>Why is the antiarch placoderm <em>Bothriolepis</em> used as an index fossil for Upper Devonian continental rocks globally?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Bothriolepis</em> was a hardy, euryhaline fish capable of migrating through coastal marine seaways into freshwater river basins across all Gondwanan and Euramerican continents. Over 60 distinct species evolved rapidly during the Frasnian-Famennian stages, making their robust, easily fossilized box-like carapaces ideal index fossils.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: End-Devonian Hangenberg Extinction Event</div>
        <p>What catastrophic global event caused the complete annihilation of the Placodermi at the end of the Devonian ($\sim 359\text{ Ma}$)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>Hangenberg Event</strong> (at the Devonian-Carboniferous boundary). It was triggered by intense global cooling, southern hemisphere continental glaciation, rapid sea-level regression, and severe marine anoxia (widespread deposition of black Hangenberg shales). Specialized, heavy placoderms were completely wiped out, clearing ecological niches for the post-Devonian radiation of actinopterygians (ray-finned fishes) and chondrichthyans (sharks).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Endoskeleton vs. Exoskeleton Mineralization</div>
        <p>Was the internal endoskeleton (vertebrae and braincase) of placoderms heavily ossified like their dermal armor?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>No. While their dermal exoskeleton was composed of thick, dense, heavily mineralized bone plates, their internal endoskeleton (axial column and braincase) remained largely <strong>cartilaginous or perichondrally calcified</strong>. The vertebral column consisted of a persistent unrestricted notochord flanked by cartilaginous neural and hemal arches.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: *Entelognathus* and the Origin of Modern Fish Jaws</div>
        <p>How did the 2013 discovery of *Entelognathus primordialis* in China revolutionize our understanding of placoderms and modern bony fishes?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Entelognathus</em> (Silurian, $\sim 419\text{ Ma}$) possesses a typical placoderm body armor, but its face displays the marginal jaw bones of <strong>osteichthyans (premaxilla, maxilla, and dentary)</strong>! This proved that placoderms are not an aberrant dead-end side branch, but are paraphyletic stem-gnathostomes from which all bony fishes (and land vertebrates) directly inherited their facial and jaw bones.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Dermal Bone Puncture Resistance</div>
        <p>How did the sandwich microstructure of placoderm dermal plates provide high fracture toughness against predator bites?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The plate consists of dense compact outer and inner bone lamellae sandwiching a middle layer of porous, vascular spongy bone. This engineered <strong>sandwich-panel structure</strong> absorbs and dissipates mechanical energy through micro-yielding in the porous middle core, stopping propagating cracks and preventing catastrophic puncture by large predators.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 65, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q065_Placoderms_Armored_Jawed_Fishes_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q065: {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    generate_q061()
    generate_q062()
    generate_q063()
    generate_q064()
    generate_q065()
