#!/usr/bin/env python3
"""
Q087 Generator: Fergusite Pseudoleucite-Pyroxene Alkaline Plutonic Rock
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q087():
    title = r"Q087: Alkaline Petrology: Fergusite & Pseudoleucite Foidolite Petrography | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Potassic Alkaline Rocks"
    h1_title = "Q087: Fergusite: Pseudoleucite-Pyroxene Potassic Foidolite"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 87<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 2: Classification of Igneous Rocks / Foidolites, p. 28; Ch. 19: Potassic Alkaline Rocks); L.V. Pirsson (1905, <em>USGS Bulletin</em> 237, "Petrography and Geology of the Igneous Rocks of the Highwood Mountains, Montana"); R.W. Le Maitre, <em>Igneous Rocks: A Classification and Glossary of Terms (IUGS)</em>; Anthony Hall, <em>Igneous Petrology</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND DISCOVERY OF FERGUSITE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, History & Petrographic Identity of Fergusite</div>
    <div class="card-body">
      <p>
        The rock name <strong>fergusite</strong> was introduced in 1905 by the eminent petrologist <strong>Louis Valentine Pirsson</strong> (U.S. Geological Survey Bulletin 237) from its type locality in Upper Fergus County, Highwood Mountains, Montana, USA.
      </p>
      <p>
        According to the <em>IUGS Subcommission on the Systematics of Igneous Rocks</em> (Le Maitre, 2002; Winter, 2014, p. 28), <strong>fergusite</strong> is formally defined as:
      </p>
      <div class="formula-box">
        <strong>IUGS Definition of Fergusite:</strong><br>
        $$\mathbf{\text{Fergusite}} = \text{A potassic foidolitic plutonic rock composed of roughly } \mathbf{70\%\ \text{Pseudoleucite}} \text{ and } \mathbf{30\%\ \text{Clinopyroxene (Aegirine-Augite / Diopside)}}$$
      </div>
      <p>
        It occupies <strong>Field 15 (Foidolites)</strong> of the IUGS QAPF classification, representing the coarse-grained plutonic equivalent of a leucite nephelinite or leucitite, closely affiliated with the potassic shonkinite-missourite intrusive series.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q87/winter_p28_fergusite_iugs_classification.png" alt="IUGS QAPF Plutonic Classification and Fergusite Position from Winter">
        <div class="figure-caption">
          <strong>Figure 87.1 — IUGS QAPF Plutonic Classification & Field 15 (Foidolites):</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 2, p. 28). Highlighting the ultra-alkaline Foidolite field where nepheline, kalsilite, and pseudoleucite rocks (such as Fergusite and Ijolite) plot.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: NATURE AND GENESIS OF PSEUDOLEUCITE -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Nature of Pseudoleucite: Subsolidus Trapezohedral Breakdown</div>
    <div class="card-body">
      <p>
        <strong>Leucite ($\text{KAlSi}_2\text{O}_6$)</strong> is an ultra-potassic, silica-deficient feldspathoid. While stable at high temperatures ($>1000^\circ\text{C}$) in subvolcanic lavas, primary sodic leucite solid solution becomes thermodynamically unstable at lower subsolidus temperatures during slow plutonic cooling, or under elevated water vapor pressures.
      </p>

      <h4>The Pseudoleucite Intergrowth Reaction</h4>
      <p>
        Under plutonic cooling, primary leucite unmixes and reacts with residual interstitial melt, decomposing into a fine-grained, multiphase microcrystalline aggregate termed <strong>pseudoleucite</strong>:
      </p>
      <div class="formula-box">
        <strong>Subsolidus Breakdown of Leucite Solid Solution:</strong><br>
        $$\mathbf{2\text{KAlSi}_2\text{O}_6\ (\text{Leucite})} \longrightarrow \mathbf{\text{KAlSi}_3\text{O}_8\ (\text{Potassium Feldspar})} + \mathbf{\text{KAlSiO}_4\ (\text{Kalsilite})}$$<br>
        $$\text{When sodium is present: } \text{Leucite}_{\text{ss}} \longrightarrow \mathbf{\text{Orthoclase}} + \mathbf{\text{Nepheline}} + \mathbf{\text{Analcime}}$$
      </div>
      <p>
        Crucially, this replacement occurs <strong>pseudomorphically</strong>: the resulting intergrowth of alkali feldspar, nepheline, kalsilite, and minor analcime faithfully preserves the iconic <strong>trapezohedral (icositetrahedral, $\{211\}$) crystal geometry</strong> of the original high-temperature leucite crystals.
      </p>
    </div>
  </div>

  <!-- CARD 3: PETROGRAPHIC CONTRAST WITH FENITE, FELSITE, AND FERRILITE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Petrographic Demarcation: Fergusite vs. Fenite, Felsite & Ferrilite</div>
    <div class="card-body">
      <p>
        The multiple-choice options present phonetically similar petrological terms that represent entirely different geological processes:
      </p>
      <ul>
        <li><strong>Fergusite:</strong> A primary, potassic ultra-alkalic <em>plutonic igneous rock</em> containing $70\%$ pseudoleucite and $30\%$ pyroxene.</li>
        <li><strong>Fenite:</strong> A <em>metasomatic contact-metamorphic rock</em> produced by the high-temperature alkaline fluid alteration (fenitization) of granitic country rocks bordering carbonatite and alkaline ring complexes, dominated by secondary aegirine, sodic amphibole, and albite/microperthite.</li>
        <li><strong>Felsite:</strong> A generic field term for any <em>very fine-grained, light-colored volcanic or hypabyssal rock</em> (e.g., devitrified rhyolite or microgranite) composed of a microcrystalline groundmass of quartz and feldspar, having an acidic silica content ($SiO_2 > 70\%$).</li>
        <li><strong>Ferrilite:</strong> A non-standard, obsolete historical term occasionally applied to iron-rich sedimentary sandstones or ironstone-cemented rocks, completely devoid of feldspathoids.</li>
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
        <div class="q-num">Question 87</div>
        <div class="q-text">The plutonic rock consisting of roughly 70% pseudoleucite (alkali feldspar, nepheline, kalsilite and minor analcime) and 30% pyroxene is termed as :</div>
        <div class="q-options">
          <div class="opt-node">(A) Ferrilite</div>
          <div class="opt-node">(B) Fenite</div>
          <div class="opt-node correct">(C) Fergusite</div>
          <div class="opt-node">(D) Felsite</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (C)</div>
        <div><strong>Fergusite:</strong> The definitive potassic foidolitic plutonic rock composed of approximately 70% pseudoleucite and 30% clinopyroxene, named from Fergus County, Montana.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Ferrilite — INCORRECT</div>
        <p>
          <em>Ferrilite</em> is an obsolete or informal term for iron-rich sedimentary lithologies or ferriferous rocks. It is completely unrelated to potassic alkaline foidolitic plutonism.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Fenite — INCORRECT</div>
        <p>
          <em>Fenite</em> is a metasomatically altered rock formed in the contact aureole surrounding carbonatite-ijolite complexes via alkali metasomatism (fenitization). It consists of desilicated quartz-free country rocks enriched in aegirine and alkali feldspar, but does not constitute the primary 70% pseudoleucite plutonic rock described in the question.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(C) Fergusite — CORRECT</div>
        <p>
          <em>Fergusite</em> (Pirsson, 1905; Le Maitre, 2002, p. 80) is the exact, standard international petrographic term for a plutonic rock consisting of <strong>roughly 70% pseudoleucite (intergrowth of alkali feldspar, nepheline, kalsilite, and minor analcime) and 30% pyroxene (aegirine-augite)</strong>. It is the textbook archetype of a potassic foidolite (Winter, 2014, p. 28).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Felsite — INCORRECT</div>
        <p>
          <em>Felsite</em> is a broad field term for light-colored, microcrystalline or cryptocrystalline felsic volcanic/hypabyssal rocks (such as rhyolite or dacite) consisting of quartz and feldspar, entirely lacking the potassic feldspathoids and coarse pseudoleucite crystals characteristic of fergusite.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Petrography of Potassic and Alkaline Plutonic Suites</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Rock Type</th>
            <th>Primary Felsic / Foid Phase</th>
            <th>Dominant Mafic Phase</th>
            <th>Color Index ($M'$)</th>
            <th>IUGS Classification Field</th>
            <th>Type Locality & Setting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fergusite</strong></td>
            <td><strong>Pseudoleucite (~70%)</strong> (Kfs + Nepheline + Kalsilite)</td>
            <td><strong>Aegirine-augite / Diopside (~30%)</strong></td>
            <td>$M' \approx 30\%$ (Mesocratic)</td>
            <td><strong>Field 15 (Potassic Foidolite)</strong></td>
            <td><strong>Fergus County, Highwood Mountains (Montana, USA)</strong></td>
          </tr>
          <tr>
            <td><strong>Shonkinite</strong></td>
            <td>Potassium Feldspar (Orthoclase) $\pm$ minor Nepheline/Leucite</td>
            <td>Augite (Diopside) + Biotite</td>
            <td>$M' = 60\text{--}80\%$ (Melanocratic)</td>
            <td>Field 7/8 (Melano-Syenite / Monzonite)</td>
            <td>Shonkin Sag Laccolith (Montana, USA)</td>
          </tr>
          <tr>
            <td><strong>Missourite</strong></td>
            <td>Leucite / Pseudoleucite ($10\text{--}30\%$)</td>
            <td>Clinopyroxene ($> 70\%$) + minor Olivine</td>
            <td>$M' > 70\%$ (Melanocratic Foidolite)</td>
            <td>Field 15 (Melanocratic Leucitolite)</td>
            <td>Missouri River Basin, Highwood Mountains (USA)</td>
          </tr>
          <tr>
            <td><strong>Italite</strong></td>
            <td>Leucite ($> 90\%$, virtually pure leucite rock!)</td>
            <td>Minor Pyroxene / Melanite ($< 10\%$)</td>
            <td>$M' < 10\%$ (Leucocratic Foidolite)</td>
            <td>Field 15 (Leucitolite)</td>
            <td>Alban Hills, Rome (Italy)</td>
          </tr>
          <tr>
            <td><strong>Ijolite</strong></td>
            <td>Nepheline ($30\text{--}70\%$) [Sodium-dominant!]</td>
            <td>Aegirine-augite ($30\text{--}70\%$)</td>
            <td>$M' = 30\text{--}70\%$ (Sodic Foidolite)</td>
            <td>Field 15 (Sodic Foidolite)</td>
            <td>Iivaara (Finland); Amba Dongar (India)</td>
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
        <div class="p-header">Problem 1: Leucite Solid Solution Subsolidus Decomposition Reaction</div>
        <p>
          Write the balanced chemical reaction demonstrating how a sodium-bearing leucite solid solution of composition $\text{K}_{0.5}\text{Na}_{0.5}\text{AlSi}_2\text{O}_6$ unmixes into potassium feldspar and nepheline to form pseudoleucite.
        </p>
        <div class="p-ans">
          <strong>Stoichiometric Reaction:</strong><br>
          $$\mathbf{2\text{K}_{0.5}\text{Na}_{0.5}\text{AlSi}_2\text{O}_6\ (\text{Na-Leucite Solid Solution})} \longrightarrow \mathbf{\text{KAlSi}_3\text{O}_8\ (\text{K-Feldspar})} + \mathbf{\text{NaAlSiO}_4\ (\text{Nepheline})}$$<br>
          <strong>Mass Balance Verification:</strong><br>
          - Reactants: $1\text{ K} + 1\text{ Na} + 2\text{ Al} + 4\text{ Si} + 12\text{ O}$.<br>
          - Products: ($1\text{ K} + 1\text{ Al} + 3\text{ Si} + 8\text{ O}$) + ($1\text{ Na} + 1\text{ Al} + 1\text{ Si} + 4\text{ O}$) = $1\text{ K} + 1\text{ Na} + 2\text{ Al} + 4\text{ Si} + 12\text{ O}$.<br>
          The stoichiometry balances perfectly, proving that sodic leucite decomposes into equimolar orthoclase and nepheline within pseudoleucite grains.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Potassium/Sodium Molecular Ratio in Fergusite Petrogenesis</div>
        <p>
          A bulk geochemical analysis of fergusite yields: $\text{K}_2\text{O} = 9.8\text{ wt}\%$ (molecular weight = $94.20\text{ g/mol}$) and $\text{Na}_2\text{O} = 2.4\text{ wt}\%$ (molecular weight = $61.98\text{ g/mol}$). Calculate the molecular $\text{K}_2\text{O}/\text{Na}_2\text{O}$ ratio and state whether the rock belongs to the potassic or sodic alkaline series.
        </p>
        <div class="p-ans">
          <strong>Molar Ratio Calculation:</strong><br>
          1. Moles of $\text{K}_2\text{O}$:
          $$n(\text{K}_2\text{O}) = \frac{9.8}{94.20} \approx \mathbf{0.1040\text{ mol}}$$<br>
          2. Moles of $\text{Na}_2\text{O}$:
          $$n(\text{Na}_2\text{O}) = \frac{2.4}{61.98} \approx \mathbf{0.0387\text{ mol}}$$<br>
          3. Molecular Ratio:
          $$\frac{\text{Molar }\text{K}_2\text{O}}{\text{Molar }\text{Na}_2\text{O}} = \frac{0.1040}{0.0387} \approx \mathbf{2.69}$$<br>
          <strong>Classification:</strong> Since the molecular ratio $\mathbf{K_2O/Na_2O = 2.69 \gg 1.0}$, the rock is classified as <strong>Ultra-Potassic</strong>, in sharp contrast to sodic foidolites like ijolite where $Na_2O/K_2O \gg 1.0$.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: High-Pressure Instability of Leucite</div>
        <p>
          In experimental petrology, leucite is never found in deep mantle xenoliths or high-pressure metamorphic rocks. Using the reaction $\text{KAlSi}_2\text{O}_6\ (\text{Leucite}) \rightleftharpoons \text{KAlSi}_3\text{O}_8\ (\text{Sanidine}) + \text{KAlSiO}_4\ (\text{Kalsilite})$, explain the pressure limit on leucite stability.
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Pressure Limit:</strong><br>
          - Leucite has an exceptionally open, framework crystal structure with high molar volume ($V_m = 88.4\text{ cm}^3/\text{mol}$).<br>
          - Under elevated pressure ($P > 0.5\text{--}0.8\text{ GPa}$, depths $> 15\text{--}25\text{ km}$ in the presence of water), Leucite breaks down into a higher-density assemblage of <strong>Sanidine + Kalsilite</strong>, or reacts with water to form <strong>Analcime</strong>.<br>
          - Consequently, leucite can only precipitate in <strong>shallow crustal magma chambers or subaerial volcanic lavas</strong> ($P < 0.5\text{ GPa}$).
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Microscopic Identification of Trapezohedral Pseudoleucite</div>
        <p>
          Describe the optical petrographic appearance of a pseudoleucite phenocryst under plane-polarized light (PPL) and cross-polarized light (XPL).
        </p>
        <div class="p-ans">
          <strong>Petrographic Description:</strong><br>
          - <strong>Plane-Polarized Light (PPL):</strong> The grain displays a sharp, eight-sided or rounded polygonal outline representing the external crystal faces of a <strong>trapezohedron (icositetrahedron)</strong>. Internally, the grain is turbid, cloudy, and filled with tiny microscopic fluid inclusions and dust-like particles.<br>
          - <strong>Cross-Polarized Light (XPL):</strong> The original isotropic character of cubic leucite is completely gone! Instead, the crystal exhibits a fine, mottled, intergrown mosaic of low-birefringence orthoclase and nepheline displaying first-order grey interference colors, forming delicate sub-radial or vermicular micro-patches within the trapezohedral boundary.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Geotectonic Setting of the Montana Alkaline Province</div>
        <p>
          Where and in what tectonic setting did the type fergusite of the Highwood Mountains (Montana) form?
        </p>
        <div class="p-ans">
          <strong>Regional Tectonics:</strong><br>
          - <strong>Geotectonic Setting:</strong> The Central Montana Alkalic Province represents an <strong>Eocene back-arc / intraplate extensional magmatic province</strong> situated in the foreland of the North American Cordillera (~50–45 Ma).<br>
          - <strong>Petrogenesis:</strong> Magmas were generated by low-degree partial melting of ancient Archean sub-continental lithospheric mantle (SCLM) that had been heavily metasomatized by potassic fluids during earlier Proterozoic subduction events.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Fenite vs. Fergusite Diagnostic Criteria</div>
        <p>
          State three definitive field and petrographic criteria that enable an exploration geologist to distinguish a fergusite from a fenite.
        </p>
        <div class="p-ans">
          <strong>Threefold Distinction:</strong><br>
          1. <strong>Rock Origin:</strong> Fergusite is a <em>primary igneous pluton</em>; Fenite is an <em>in-situ metasomatic replacement rock</em> formed around intrusive margins.<br>
          2. <strong>Diagnostic Texture:</strong> Fergusite exhibits <em>panidiomorphic or hypidiomorphic igneous texture with trapezohedral pseudoleucite phenocrysts</em>; Fenite exhibits <em>relict gneissic/granitic foliation</em> overprinted by radiating fibrous sheaves of aegirine and riebeckite.<br>
          3. <strong>Mineral Composition:</strong> Fergusite contains up to $70\%$ pseudoleucite (nepheline + kalsilite); Fenite is dominated by secondary albite, perthitic microcline, and aegirine, with quartz leached away but feldspathoids rarely reaching $70\%$.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Agpaitic vs. Miaskitic Nature of Potassic Rocks</div>
        <p>
          Calculate the peralkalinity index of a fergusite containing molecular $\text{Al}_2\text{O}_3 = 0.110\text{ mol}$, $\text{K}_2\text{O} = 0.085\text{ mol}$, and $\text{Na}_2\text{O} = 0.020\text{ mol}$, and determine whether it is agpaitic or miaskitic.
        </p>
        <div class="p-ans">
          <strong>Calculation:</strong><br>
          $$\text{Alkali Sum} = \text{K}_2\text{O} + \text{Na}_2\text{O} = 0.085 + 0.020 = 0.105\text{ mol}$$<br>
          $$\text{Agpaitic Index } (AI) = \frac{\text{K}_2\text{O} + \text{Na}_2\text{O}}{\text{Al}_2\text{O}_3} = \frac{0.105}{0.110} \approx \mathbf{0.955}$$<br>
          <strong>Classification:</strong> Since $\mathbf{AI = 0.955 < 1.0}$, total alkalis do not exceed alumina; hence the rock is classified as <strong>Miaskitic (subaluminous to metaluminous alkaline)</strong>, where all alkalis are consumed in forming feldspars and feldspathoids, and excess alumina is bound in pyroxene/amphibole.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Origin of Ultra-Potassic Primary Magmas via Phlogopite Melting</div>
        <p>
          Explain why melting of a phlogopite-bearing mantle peridotite at depths $> 100\text{ km}$ generates potassic magmas (like the parent of fergusite), whereas melting of amphibole-bearing mantle generates sodic magmas.
        </p>
        <div class="p-ans">
          <strong>Mantle Mineral Partitioning:</strong><br>
          - <strong>Phlogopite ($\text{KMg}_3\text{AlSi}_3\text{O}_{10}(\text{OH})_2$):</strong> The premier potassic hydrous phase in the deep sub-continental lithospheric mantle ($P > 3\text{ GPa}$, depths $> 100\text{ km}$). When phlogopite melts incongruently, it releases massive concentrations of potassium ($K_2O$), rubidium, and barium into the melt, yielding ultra-potassic liquids ($K_2O \gg Na_2O$) that crystallize as fergusite, leucitite, or lamproite.<br>
          - <strong>Pargasitic Amphibole:</strong> Sodic hydrous phase stable only at shallower mantle depths ($P < 2.5\text{ GPa}$, depths $< 75\text{ km}$). Melting of pargasite releases sodium ($Na_2O$), generating sodic alkali basalts, basanites, and nephelinites.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 87, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q087_Fergusite_Pseudoleucite_Alkaline_Rock_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q087: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q087()
