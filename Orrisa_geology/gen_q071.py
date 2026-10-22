#!/usr/bin/env python3
"""
Q071 Generator: Rugose Corals (Tetracoralla) Horn Coral Morphology & Septal Insertion
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q071():
    title = r"Q071: Anthozoa: Rugosa (Tetracoralla) Horn Corals Morphology & Septal Insertion | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Invertebrate Paleontology & Anthozoa"
    h1_title = "Q071: Rugose Corals (Tetracoralla): Horn Coral Morphology & Septal Insertion"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 71<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (Ch. 9: Paleontology / Anthozoa, pp. 186–188, 358); P.K. Mukherjee, <em>A Text Book of Geology</em> (Ch. 13: Paleontology, p. 170); E.N.K. Clarkson, <em>Invertebrate Palaeontology and Evolution</em> (4th Ed., Ch. 5: Corals, pp. 109–137); Moore, Lalicker & Fischer, <em>Invertebrate Fossils</em> (McGraw-Hill, Ch. 4: Coelenterata)."""

    part1 = r"""
  <!-- CARD 1: SYSTEMATIC PALEONTOLOGY AND MORPHOLOGY -->
  <div class="card">
    <div class="card-header bg-blue">1. Systematic Paleontology & Anatomy of Order Rugosa (Tetracoralla)</div>
    <div class="card-body">
      <p>
        The <strong>Order Rugosa</strong> (Milne-Edwards & Haime, 1850), universally referred to in classical invertebrate paleontology as <strong>Tetracoralla</strong> (Haeckel, 1866), constitutes an extinct, major group of solitary and colonial anthozoan cnidarians that flourished throughout the Paleozoic marine realm. The name <em>Rugosa</em> derives from the Latin <em>ruga</em> (wrinkle), referring directly to the prominent concentric growth ridges and coarse wrinkles that ornament the outer skeletal wall (<strong>epitheca</strong>).
      </p>
      <p>
        The classic morphological archetype of the solitary rugosan is a curved, conical or ceratoid skeletal cup, popularly designated as the <strong>"horn coral"</strong> due to its uncanny resemblance to a bovine or ram horn. The animal inhabited the concave upper depression of this skeleton, termed the <strong>calice</strong>, while secreting a continuous basal and peripheral framework of calcium carbonate.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q71/mahapatra_p187_rugosa_tetracoralla_horn_corals.png" alt="Morphology of Rugose Horn Corals from Mahapatra">
        <div class="figure-caption">
          <strong>Figure 71.1 — Morphological Architecture of Solitary Rugose Corals (Horn Corals):</strong> Authentic textbook scan from G.B. Mahapatra (<em>A Text-Book of Geology</em>, p. 187). Illustrating the curved conical corallite, wrinkled outer epitheca, deep terminal calice, prominent radial septa, tabulae, and the cardinal fossula.
        </div>
      </div>

      <h4>Fundamental Anatomical Components of the Rugose Corallite</h4>
      <ul>
        <li><strong>Epitheca:</strong> The thin, outer cuticular calcitic sheath secreted by the basal ectoderm of the polyp, displaying pronounced horizontal growth rugae (annulations) and longitudinal septal grooves.</li>
        <li><strong>Calice (Calyx):</strong> The cup-like terminal depression at the broad anterior end of the corallite where the living anthozoan polyp sat.</li>
        <li><strong>Septa:</strong> Radial vertical calcitic plates that project inwards from the peripheral wall into the central lumen, providing mechanical support to the soft mesenteries of the polyp.</li>
        <li><strong>Tabulae:</strong> Horizontal or gently arched, convex/concave transverse partitions that floor the lower, abandoned portions of the visceral cavity as the polyp grew upward.</li>
        <li><strong>Dissepiments:</strong> Small, curved, blister-like vesicular plates lining the peripheral zone (the <em>dissepimentarium</em>), providing lateral reinforcement between septa.</li>
        <li><strong>Columella / Axial Structure:</strong> A solid central rod or complex meshwork of twisted septal lamellae (axial vortex) along the central axis of the corallite.</li>
        <li><strong>Cardinal Fossula:</strong> A prominent depression or gap within the septal array, formed by the abortion, abbreviation, or depression of the <em>cardinal septum</em>, reflecting the location of the siphonoglyph in the living polyp.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: SEPTAL INSERTION DYNAMICS AND TETRAMERAL SYMMETRY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Septal Insertion Dynamics and Bilateral Quadrant Symmetry</div>
    <div class="card-body">
      <p>
        The defining taxonomic criterion separating <strong>Tetracoralla (Rugosa)</strong> from <strong>Hexacorallia (Scleractinia)</strong> lies in the ontogenetic sequence of septal insertion. While modern scleractinians insert septa in radial cycles of six ($6 \to 12 \to 24 \dots$), rugose corals insert their adult septa (<strong>metasepta</strong>) in strictly <strong>four quadrants</strong>, imparting a conspicuous <strong>bilateral symmetry</strong> to the adult corallum.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q71/pkm_p170_anthozoa_tetracorals_septal_arrangement.png" alt="Septal Arrangement and Insertion in Tetracoralla from P.K. Mukherjee">
        <div class="figure-caption">
          <strong>Figure 71.2 — Septal Insertion and Tetrameral Quadrant Architecture:</strong> Authentic textbook scan from P.K. Mukherjee (<em>A Text Book of Geology</em>, p. 170). Depicting the initial insertion of the cardinal ($C$), counter ($K$), and two alar ($A$) protosepta, followed by the serial addition of metasepta within four distinct growth sectors.
        </div>
      </div>

      <h4>Ontogenetic Sequence of Septal Development (Kunth's Law)</h4>
      <p>
        The classical insertion sequence established by A. Kunth (1869) proceeds as follows:
      </p>
      <ol>
        <li><strong>Protoseptal Stage:</strong> The very first septum formed is an axial plate running across the entire calice floor. It subsequently divides into two opposing primary septa: the <strong>Cardinal Septum ($C$)</strong> and the <strong>Counter Septum ($K$)</strong>. Shortly thereafter, two lateral protosepta arise, termed the <strong>Alar Septa ($A$)</strong>, followed by two <strong>Counter-Lateral Septa ($KL$)</strong>. These primary plates divide the calice into four primary growth sectors or quadrants.</li>
        <li><strong>Metaseptal Insertion (Tetrameral Growth):</strong> Subsequent major septa (metasepta) are inserted <em>only at four specific loci</em> directly adjacent to the protosepta:
          <ul>
            <li>In the two cardinal quadrants, metasepta are added on both sides of the <strong>cardinal septum</strong>, leaning pinnately against the alar septa (feather-like arrangement).</li>
            <li>In the two counter quadrants, metasepta are added on the cardinal side of the <strong>alar septa</strong>, leaning towards the counter septum.</li>
          </ul>
        </li>
        <li><strong>Bilateral Symmetry Plane:</strong> Because new septa are never added adjacent to the counter septum or counter-lateral septa, the corallite displays an unmistakable bilateral symmetry plane passing directly through the cardinal and counter septa.</li>
      </ol>
      <div class="formula-box">
        <strong>Kunth's Quadrant Insertion Rule:</strong><br>
        $$\text{Total Metasepta added per cycle} = 4 \quad (\text{One per quadrant})$$<br>
        $$\text{Quadrants} = 2 \times \text{Cardinal Quadrants} + 2 \times \text{Counter-Alar Quadrants}$$
      </div>
    </div>
  </div>

  <!-- CARD 3: GEOCHEMICAL MINERALOGY AND EXTINCTION DYNAMICS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Skeletal Mineralogy, Paleoecology & the Permian-Triassic Extinction</div>
    <div class="card-body">
      <p>
        Rugose corals were exclusively marine, benthic, suspension-feeding organisms that flourished on shallow Paleozoic carbonate platforms, patch reefs, and level-bottom muddy/silty substrates from the Middle Ordovician (Darriwilian) to the Late Permian (Changhsingian).
      </p>
      <h4>Skeletal Mineralogy: Calcite vs. Aragonite</h4>
      <p>
        A fundamental distinction between Paleozoic Rugosa and post-Paleozoic Scleractinia is their primary skeletal mineralogy:
      </p>
      <ul>
        <li><strong>Rugosa:</strong> Primarily secreted skeletons of stable <strong>high-magnesium calcite</strong> ($MgCO_3 \approx 5\text{--}15\text{ mol}\%$). Consequently, fossil rugose corallites retain exquisite original microstructural detail (fibro-normal and lamellar calcitic trabeculae) in Paleozoic limestones without undergoing gross dissolution or neomorphic destruction.</li>
        <li><strong>Scleractinia:</strong> Primarily secrete skeletons of metastable <strong>aragonite</strong> ($\text{orthorhombic } CaCO_3$). In the fossil record, scleractinian skeletons are frequently dissolved to form hollow molds or are recrystallized into coarse, blocky sparry calcite mosaics.</li>
      </ul>

      <h4>The Permian-Triassic (P-Tr) Mass Extinction Catastrophe</h4>
      <p>
        At the end of the Permian Period (~251.9 Ma), the massive flood basalt eruptions of the Siberian Traps induced severe ocean acidification, hypercapnia, marine anoxia, and global warming. Because rugose corals possessed thick calcitic skeletons, lacked high physiological buffering against elevated oceanic $p\text{CO}_2$, and relied on vulnerable benthic carbonate ecosystems, the entire order <strong>Rugosa was completely annihilated</strong>. Not a single species of Rugosa survived into the Triassic Period. The scleractinian corals that appeared in the Middle Triassic (Anisian) evolved independently from non-skeletal actiniarian sea anemone ancestors, exhibiting a 14-million-year "reef gap" in the Early Triassic.
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
        <div class="q-num">Question 71</div>
        <div class="q-text">The Rugose corals have unique horn-shaped chamber with a wrinkled or rugose wall are called ___.</div>
        <div class="q-options">
          <div class="opt-node">(A) Scleractinia or Hexacorallia</div>
          <div class="opt-node correct">(B) Tetracoralla or Horn corals</div>
          <div class="opt-node">(C) Octocoralla</div>
          <div class="opt-node">(D) All of these</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (B)</div>
        <div><strong>Tetracoralla or Horn corals:</strong> The Order Rugosa is universally defined by its solitary horn-shaped corallites with wrinkled (rugose) epithecal walls and a characteristic four-quadrant (tetrameral) septal insertion pattern.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Scleractinia or Hexacorallia — INCORRECT</div>
        <p>
          <em>Scleractinia</em> (also designated as <em>Hexacorallia</em>) are the modern stony reef-building corals that first appeared in the Middle Triassic (~240 Ma) and persist to the present day. They possess an aragonitic skeleton with septa inserted in cycles of <strong>six</strong> (hexameral radial symmetry), completely lacking the distinctive four-fold septal insertion, cardinal fossula, and coarse wrinkled epithecal horn morphology characteristic of Paleozoic Rugosa.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(B) Tetracoralla or Horn corals — CORRECT</div>
        <p>
          <em>Tetracoralla</em> is the classic paleontological synonym for the Order <em>Rugosa</em> (Milne-Edwards & Haime, 1850). The term refers directly to the four cardinal quadrants within which all adult metasepta are inserted. The solitary representatives possess a diagnostic curved, conical morphology resembling a horn (hence the universal vernacular name <strong>"horn corals"</strong>) enclosed by a wrinkled outer wall (epitheca). This is the exact textbook definition provided by G.B. Mahapatra (p. 187, 358) and P.K. Mukherjee (p. 170).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Octocoralla — INCORRECT</div>
        <p>
          <em>Octocoralla</em> (Alcyonaria) constitutes an entirely separate anthozoan subclass characterized by polyps possessing exactly <strong>eight pinnate (feather-like) tentacles</strong> and eight complete mesenteries. Octocorals include sea pens (Pennatulacea), sea fans (Gorgonacea), and soft corals (Alcyonacea). With rare exceptions (e.g., the organ-pipe coral <em>Tubipora</em>), they secrete microscopic internal calcitic spicules (sclerites) or gorgonin axes rather than solitary conical horn-shaped skeletons with rugose walls.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) All of these — INCORRECT</div>
        <p>
          This choice is biologically and stratigraphically impossible. <em>Hexacorallia</em> (6-fold), <em>Tetracoralla</em> (4-fold), and <em>Octocoralla</em> (8-fold) are distinct, mutually exclusive taxonomic divisions defined by entirely different symmetries, skeletal mineralogies, and geological distributions.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Taxonomic Synthesis of Anthozoan Corals</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Taxonomic Group</th>
            <th>Septal Symmetry & Insertion</th>
            <th>Skeletal Mineralogy</th>
            <th>Internal Structures</th>
            <th>Growth Habit</th>
            <th>Stratigraphic Range</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Rugosa (Tetracoralla)</strong></td>
            <td><strong>Tetrameral (4 quadrants)</strong>; bilateral symmetry; metasepta added at 4 loci</td>
            <td><strong>Calcite</strong> (high-Mg, stable)</td>
            <td>Tabulae, dissepiments, columella, <strong>cardinal fossula</strong></td>
            <td>Solitary ("horn corals") and Compound/Colonial</td>
            <td>Middle Ordovician – Late Permian (Extinct at P-Tr)</td>
          </tr>
          <tr>
            <td><strong>Scleractinia (Hexacorallia)</strong></td>
            <td><strong>Hexameral (cycles of 6)</strong>; radial symmetry; septa inserted in concentric cycles</td>
            <td><strong>Aragonite</strong> (metastable)</td>
            <td>Dissepiments, columella, synapticulae; fossula absent</td>
            <td>Predominantly colonial (reef-builders) & solitary</td>
            <td>Middle Triassic – Recent (Dominant today)</td>
          </tr>
          <tr>
            <td><strong>Tabulata</strong></td>
            <td>Radial; septa poorly developed (spines, ridges) or absent; 12-fold when present</td>
            <td><strong>Calcite</strong> (low- to high-Mg)</td>
            <td><strong>Prominent horizontal tabulae</strong>; mural pores; no dissepiments</td>
            <td>Exclusively <strong>colonial</strong> (honeycomb, chain, tube colonies)</td>
            <td>Early Ordovician – Late Permian (Extinct at P-Tr)</td>
          </tr>
          <tr>
            <td><strong>Octocoralla (Alcyonaria)</strong></td>
            <td>Eight-fold (octameral); septa absent or represented by 8 internal ridges</td>
            <td>Organic gorgonin and/or isolated calcitic sclerites</td>
            <td>Spicular meshwork or horny central axis</td>
            <td>Colonial (soft corals, sea fans, sea pens)</td>
            <td>Ordovician – Recent</td>
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
        <div class="p-header">Problem 1: Septal Quadrant Calculation and Kunth's Insertion Formula</div>
        <p>
          A transverse thin section of a solitary Carboniferous rugose coral displays a total of 42 major septa (metasepta + protosepta). If the cardinal septum and counter septum are uniquely identified along the bilateral plane, and 10 metasepta are counted in each of the two cardinal quadrants, calculate the number of metasepta present in each of the two counter quadrants.
        </p>
        <div class="p-ans">
          <strong>Step 1: Identify the primary protosepta:</strong><br>
          The primary protosepta establishing the four quadrants consist of four key plates: Cardinal ($C$), Counter ($K$), Left Alar ($A_L$), and Right Alar ($A_R$). Thus, $N_{\text{proto}} = 4$.<br>
          <strong>Step 2: Calculate total metasepta:</strong><br>
          $$\text{Total Metasepta} = N_{\text{total}} - N_{\text{proto}} = 42 - 4 = 38$$<br>
          <strong>Step 3: Distribute metasepta across symmetrical quadrants:</strong><br>
          Rugose corals display bilateral symmetry across the cardinal-counter axis. The two cardinal quadrants contain $10 \times 2 = 20$ metasepta.<br>
          Therefore, the two counter quadrants contain:<br>
          $$38 - 20 = 18 \text{ metasepta}$$<br>
          $$\text{Metasepta per counter quadrant} = \frac{18}{2} = 9$$<br>
          <strong>Conclusion:</strong> Each counter quadrant contains exactly <strong>9 metasepta</strong>.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Skeletal Mineralogy & Taphonomic Preservation Bias</div>
        <p>
          Explain why solitary rugose corals from the Devonian Hamilton Group commonly preserve fibrous crystalline trabecular microstructures, whereas Middle Triassic scleractinian corals from equivalent shallow marine limestones are frequently preserved as sparry calcite-filled molds.
        </p>
        <div class="p-ans">
          <strong>Geochemical and Diagenetic Derivation:</strong><br>
          1. <strong>Primary Mineralogy:</strong> Rugosa secreted a primary skeleton of <strong>high-magnesium calcite</strong> ($MgCO_3 \approx 8\text{--}12\text{ mol}\%$). Calcite is the thermodynamically stable polymorph of calcium carbonate at near-surface sedimentary temperatures and pressures ($G^\circ_{\text{calcite}} < G^\circ_{\text{aragonite}}$ by $\sim 1.0\text{ kJ/mol}$). During diagenesis, high-Mg calcite undergoes incongruent dissolution and loss of $Mg^{2+}$ to form low-Mg calcite via a microscopic, film-controlled dissolution-reprecipitation process that preserves original skeletal lamellae and trabeculae.<br>
          2. <strong>Metastable Aragonite in Scleractinia:</strong> Scleractinians secrete <strong>aragonite</strong>. In meteoric or mixed diagenetic porewaters undersaturated with respect to aragonite, the aragonitic corallite dissolves completely, creating a moldic void ($CaCO_{3(\text{aragonite})} \to Ca^{2+} + CO_3^{2-}$). Subsequent cementation by coarse sparry low-Mg calcite fills the void, obliterating all original septal microstructure.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Morphological Differentiation in Transverse Section</div>
        <p>
          Under petrographic inspection of an unknown Paleozoic coral thin section, a student observes: (a) radial septa displaying a feather-like pinnate convergence toward an open slot; (b) a gap devoid of septa on one side of the lumen; and (c) absence of cyclical insertion in multiples of six. Identify the structure and determine the coral order.
        </p>
        <div class="p-ans">
          <strong>Diagnostic Identification:</strong><br>
          - <strong>Structure:</strong> The open gap represents the <strong>cardinal fossula</strong>, formed by the shortening or abortion of the cardinal septum ($C$). The pinnate arrangement represents metasepta leaning toward the alar septa ($A$) according to Kunth's Law.<br>
          - <strong>Taxonomic Classification:</strong> The specimen belongs to the <strong>Order Rugosa (Tetracoralla)</strong>.<br>
          - <strong>Differentiation:</strong> Scleractinia never exhibit a cardinal fossula or pinnate metaseptal insertion; their septa are radially arranged in multiples of six ($6, 12, 24, 48$).
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Wells' Devonian Paleochronometry (Coral Growth Clocks)</div>
        <p>
          In a famous 1963 study, John Wells counted the microscopic epithecal daily growth ridges between major annual growth annulations on Middle Devonian horn corals (e.g., <em>Heliophyllum halli</em>), obtaining an average of 400 daily bands per annual cycle. Calculate the length of a Devonian solar day in hours, assuming Earth's orbital period (year length) has remained constant at $3.156 \times 10^7\text{ seconds}$ (365.25 modern days).
        </p>
        <div class="p-ans">
          <strong>Mathematical Derivation:</strong><br>
          $$\text{Total annual seconds} = 365.25 \times 24 \times 3600 = 31,557,600\text{ s}$$<br>
          $$\text{Devonian solar days per year} = 400\text{ days}$$<br>
          $$\text{Length of Devonian solar day} = \frac{31,557,600\text{ s}}{400} = 78,894\text{ seconds}$$<br>
          $$\text{Length of day in hours} = \frac{78,894}{3600} \approx 21.92\text{ hours} \approx 21\text{ hours } 55\text{ minutes}$$<br>
          <strong>Geophysical Significance:</strong> Tidal friction caused by the Moon dissipates Earth's rotational kinetic energy, steadily decelerating planetary rotation and lengthening the day at $\sim 2\text{ milliseconds per century}$ ($5.3 \times 10^{-22}\text{ rad/s}^2$).
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Functional Morphology of Operculate Corals: Calceola sandalina</div>
        <p>
          The Devonian fossil <em>Calceola sandalina</em> is a specialized rugose coral possessing a flat semicircular side, a pointed apex, and a hinged lid (operculum). Describe its life mode and explain how its morphology adapted it to high-energy muddy benthic substrates.
        </p>
        <div class="p-ans">
          <strong>Functional Morphological Analysis:</strong><br>
          1. <strong>Slipper-like Morphology:</strong> Unlike typical upright conical horn corals, <em>Calceola</em> rested horizontally on its flat, semicircular cardinal side, which acted as a snowshoe or barge preventing the coral from sinking into soft, unconsolidated Devonian carbonate muds.<br>
          2. <strong>Operculum Function:</strong> The calcareous lid (composed of a single large semicircular plate) could be clamped tightly shut by retractor muscles during heavy sedimentation, storm turbulence, or predatory browsing, sealing the delicate polyp within a protected chamber. When conditions cleared, the lid swung open to allow lophophoric/tentacular suspension feeding.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Structural Architecture: Solitary vs. Compound Rugosa</div>
        <p>
          Compare the colonial architecture of the Carboniferous compound rugosan <em>Lithostrotion</em> with a solitary horn coral like <em>Zaphrentis</em>. Specify the terms for colonial corals where corallites are: (a) separated by distinct cylindrical walls; (b) polygonal and in contact; and (c) confluent with confluent septa.
        </p>
        <div class="p-ans">
          <strong>Architectural Terminology:</strong><br>
          - <em>Zaphrentis:</em> Solitary, horn-shaped, unattached or anchored by an apical rootlet, possessing a deep calice with a cardinal fossula.<br>
          - <em>Lithostrotion:</em> Compound (colonial), forming massive reef-framework or bushy dendroid thickets.<br>
          - <strong>Classification of Colonial Coralla:</strong><br>
            (a) <strong>Fasciculate (Dendroid / Phaceloid):</strong> Corallites are cylindrical, separate, and branch upward without touching (e.g., <em>Lithostrotion junceum</em>).<br>
            (b) <strong>Cerioid:</strong> Corallites are pressed tightly together, sharing distinct polygonal epithecal walls (e.g., <em>Lithostrotion basaltiforme</em>).<br>
            (c) <strong>Astraeoid / Aphroid:</strong> Outer corallite walls are absent, and septa of neighboring corallites become confluent or merge into a common dissepimental tissue (e.g., <em>Orionastraea</em>, <em>Phillipsastraea</em>).
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Longitudinal Section Anatomy: Dissepimentarium vs. Tabularium</div>
        <p>
          In a longitudinal thin section cut parallel to the growth axis of a rugose coral, two distinct structural zones are observed: an outer peripheral zone and an inner axial zone. Define these zones and explain their respective structural functions.
        </p>
        <div class="p-ans">
          <strong>Zonal Anatomy:</strong><br>
          1. <strong>Peripheral Zone (Dissepimentarium):</strong> Occupied by numerous small, vesicular, convex-outward calcitic plates termed <strong>dissepiments</strong>. Function: Provides rigid structural buttressing to the outer corallite wall against crushing waves and anchors the radial septa.<br>
          2. <strong>Axial Zone (Tabularium):</strong> The central core floored by broad, flat, arched, or sagging transverse partitions termed <strong>tabulae</strong>. Function: Elevates the living polyp as the corallite extends vertically, sealing off abandoned lower chambers to maintain visceral volume without metabolic over-expenditure.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: The "Reef Gap" and Evolutionary Origins of Scleractinia</div>
        <p>
          Following the total extinction of Rugosa and Tabulata at the Permian-Triassic boundary (251.9 Ma), no biogenic coral reefs are found in the fossil record during the Griesbachian, Dienerian, Smithian, and Spathian stages of the Early Triassic (~5 million years). Explain why scleractinians did not immediately take over rugose reef niches in the Early Triassic.
        </p>
        <div class="p-ans">
          <strong>Evolutionary & Environmental Synthesis:</strong><br>
          1. <strong>Lack of Direct Ancestry (Polyphyly):</strong> Scleractinians are <em>not</em> direct descendants of Rugosa. Molecular phylogenetic clocks and skeletal microstructure prove Scleractinia evolved independently from soft-bodied actiniarian-like anthozoans (sea anemones) that acquired aragonitic skeletal biomineralization during the Middle Triassic.<br>
          2. <strong>Post-Extinction Environmental Stress:</strong> The Early Triassic ocean suffered prolonged super-greenhouse temperatures (equatorial sea surface temperatures exceeding $40^\circ\text{C}$), widespread deep-sea and shelf anoxia, and severe ocean acidification from continued Siberian Traps sill intrusions. These lethal conditions suppressed calcifying metazoans, producing the famous <strong>Early Triassic Reef Gap</strong>. Biogenic skeletal reef building did not resume until the Anisian stage (~247 Ma).
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 71, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q071_Rugose_Corals_Tetracoralla_Horn_Corals_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q071: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q071()
