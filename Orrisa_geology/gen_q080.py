#!/usr/bin/env python3
"""
Q080 Generator: Charnockite Composition, Petrography & Granulite Genesis
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q080():
    title = r"Q080: Petrology: Charnockite Mineral Composition & Hypersthene Granulite Genesis | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic & Igneous Petrology"
    h1_title = "Q080: Charnockite Composition: Hypersthene Granulite & Holland's Series"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 80<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (Ch. 8: Petrology / Metamorphic Rocks, pp. 140–142); John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 21: Granulite Facies, pp. 468–475); Sir Thomas H. Holland (1900, <em>Memoirs of the Geological Survey of India</em>, Vol. 28, Pt. 2: "The Charnockite Series"); B.L. Sreenivas & R. Srinivasan, <em>Precambrian Geology of South India</em>."""

    part1 = r"""
  <!-- CARD 1: HISTORICAL ORIGIN AND ESSENTIAL MINERALOGY -->
  <div class="card">
    <div class="card-header bg-blue">1. Historical Discovery & Mineralogical Definition of Charnockite</div>
    <div class="card-body">
      <p>
        The rock name <strong>Charnockite</strong> holds a historic and honored position in Indian and international petrology. It was introduced in 1893 and comprehensively established in 1900 by <strong>Sir Thomas H. Holland</strong>, Director of the Geological Survey of India (GSI).
      </p>
      <p>
        Holland named the rock in memory of <strong>Job Charnock</strong>, the founder of modern Kolkata (Calcutta). In 1892, Holland discovered that Job Charnock's monumental tombstone in St. John's Churchyard, Kolkata (erected in 1695), was carved from a distinctive, dark, greasy, hypersthene-bearing granitic rock that had been quarried and transported from <strong>St. Thomas Mount at Pallavaram, near Chennai (Madras), Tamil Nadu</strong>.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q80/mahapatra_p140_charnockite_hypersthene.png" alt="Charnockite Mineral Composition and Hand Specimen from G.B. Mahapatra">
        <div class="figure-caption">
          <strong>Figure 80.1 — Essential Mineralogy & Granulitic Fabric of Charnockite:</strong> Authentic textbook scan from G.B. Mahapatra (<em>A Text-Book of Geology</em>, p. 140). Showing the essential granoblastic mineral assemblage of hypersthene orthopyroxene, perthitic potassium feldspar, and quartz, along with its characteristic greasy, waxy dark luster.
        </div>
      </div>

      <h4>Mineralogical Definition of Charnockite (sensu stricto)</h4>
      <p>
        According to both Holland's classical definition and the modern <em>IUGS Subcommission on the Systematics of Metamorphic/Igneous Rocks</em>:
      </p>
      <div class="formula-box">
        <strong>Charnockite (sensu stricto) = Hypersthene Granite</strong><br>
        $$\mathbf{\text{Essential Minerals}} = \mathbf{\text{Hypersthene (Orthopyroxene)}} + \mathbf{\text{Potassium Feldspar (Microperthite)}} + \mathbf{\text{Quartz}} \pm \text{Oligoclase/Andesine}$$
      </div>

      <h4>Megascopic Diagnostic Features</h4>
      <ul>
        <li><strong>Color & Luster:</strong> Despite containing over $70\text{ wt}\% \text{SiO}_2$ (an acidic, felsic chemistry), charnockite displays an anomalously <strong>dark greenish-grey, bluish-grey, or greasy dark brown to black coloration</strong> with a diagnostic <strong>greasy, waxy, or vitreous luster</strong>.</li>
        <li><strong>Cause of Dark Coloration:</strong> Under high-resolution transmission electron microscopy, this greasy dark appearance is produced by dense networks of submicroscopic exsolution lamellae, micro-fracture fillings of carbonic and ferruginous fluids, and submicron-scale acicular inclusions of rutile and ilmenite inside quartz and feldspar crystals.</li>
        <li><strong>Fabric:</strong> Typically exhibits a medium-to-coarse <strong>granoblastic equigranular</strong> (granulitic) texture, frequently displaying coarse metamorphic gneissose foliation.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: HOLLAND'S CHARNOCKITE SERIES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Holland's Charnockite Series & Petrographic Classification</div>
    <div class="card-body">
      <p>
        Sir Thomas Holland recognized that charnockites do not occur in isolation but form a complete, cogenetic consanguineous differentiation suite spanning from acid to ultrabasic compositions, all unified by the constant presence of <strong>orthopyroxene (hypersthene)</strong>:
      </p>

      <h4>The Four Divisions of the Charnockite Series (Holland, 1900)</h4>
      <ol>
        <li><strong>Acid Division (Charnockite sensu stricto):</strong> The hypersthene granite ($SiO_2 > 70\%$). Dominated by <strong>quartz, microcline/orthoclase microperthite, and pleochroic hypersthene</strong>, with subordinate oligoclase.</li>
        <li><strong>Intermediate Division (Enderbite / Mangerite):</strong> Quartz diorite or monzonite equivalents ($SiO_2 \approx 60\text{--}70\%$). In <strong>Enderbite</strong> (Tilley, 1936), plagioclase (antiperthitic andesine/oligoclase) vastly exceeds K-feldspar ($Plag \gg Kfs$).</li>
        <li><strong>Basic Division (Norite / 2-Pyroxene Granulite):</strong> Basaltic/gabbroic equivalent ($SiO_2 \approx 48\text{--}55\%$). Composed of <strong>calcic plagioclase (labradorite), hypersthene, and clinopyroxene (augite/diopside)</strong>, with or without garnet; quartz and K-feldspar are absent.</li>
        <li><strong>Ultrabasic Division (Pyroxenite / Bahite):</strong> Ultramafic end-member ($SiO_2 < 45\%$). Composed entirely of <strong>hypersthene, diopside, hornblende, and magnetite</strong>, with zero feldspar.</li>
      </ol>
    </div>
  </div>

  <!-- CARD 3: METAMORPHIC GENESIS AND CARBONIC FLUID FLUSHING -->
  <div class="card">
    <div class="card-header bg-emerald">3. Metamorphic Petrogenesis: Granulite Facies & Carbonic Fluid Influx</div>
    <div class="card-body">
      <p>
        While Holland originally interpreted charnockites as an igneous plutonic suite, modern petrology conclusively proves that they are <strong>high-grade regional metamorphic rocks formed under Granulite Facies conditions</strong> ($T \approx 750\text{--}900^\circ\text{C}$, $P \approx 6\text{--}10\text{ kbar}$, depths of $20\text{--}35\text{ km}$ in the lower continental crust).
      </p>

      <h4>Dehydration Breakdown of Hydrous Minerals</h4>
      <p>
        At granulite facies temperatures, hydrous phyllosilicates (biotite and hornblende) become thermodynamically unstable in the presence of quartz and undergo vapor-absent dehydration melting or breakdown, forming anhydrous orthopyroxene:
      </p>
      <div class="formula-box">
        <strong>Biotite Dehydration Reaction:</strong><br>
        $$\text{K}(\text{Mg,Fe})_3\text{AlSi}_3\text{O}_{10}(\text{OH})_2\ (\text{Biotite}) + 3\text{SiO}_2\ (\text{Quartz}) \rightleftharpoons 3(\text{Mg,Fe})\text{SiO}_3\ (\mathbf{\text{Hypersthene}}) + \text{KAlSi}_3\text{O}_8\ (\mathbf{\text{K-feldspar}}) + \text{H}_2\text{O}$$
      </div>

      <h4>The "Incipient Charnockite" Phenomenon at Kabbaldurga (Karnataka)</h4>
      <p>
        In a landmark paper, Janardhan, Newton & Smith (1979) documented the genesis of <strong>"incipient charnockite"</strong> at Kabbaldurga quarry in the Dharwar Craton. Foliated, grey amphibolite-facies Peninsular Gneiss containing biotite and hornblende is transformed along fracture-controlled patches and veins into coarse, unfoliated, greasy dark charnockite.
      </p>
      <p>
        Fluid inclusion studies confirmed that this dehydration was driven by an active influx of <strong>mantle-derived, juvenile, high-density $CO_2$-rich fluids</strong>. The massive influx of $CO_2$ flushed out water, reducing the water activity ($a_{H_2O} < 0.35$). Because $a_{H_2O}$ was depressed, the biotite dehydration curve was drawn down to lower temperatures, precipitating hypersthene + K-feldspar + quartz in situ.
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
        <div class="q-num">Question 80</div>
        <div class="q-text">What is the composition of Charnockite ?</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Hypersthene + K-feldspar + Quartz</div>
          <div class="opt-node">(B) Hornblende + K-feldspar + Quartz</div>
          <div class="opt-node">(C) Sillimanite + K-feldspar + Quartz</div>
          <div class="opt-node">(D) Epidote + Plagioclase + Quartz</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (A)</div>
        <div><strong>Hypersthene + K-feldspar + Quartz:</strong> Charnockite (sensu stricto) is canonically defined as a hypersthene granite, characterized by the essential anhydrous mineral assemblage of orthopyroxene (hypersthene), potassium feldspar (perthitic microcline), and quartz.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option correct">
        <div class="opt-title">(A) Hypersthene + K-feldspar + Quartz — CORRECT</div>
        <p>
          This is the exact, canonical definition established by Sir Thomas Holland (1900) and maintained in all international metamorphic and igneous classifications (Winter, 2014, p. 468; Mahapatra, p. 140). The defining diagnostic mineral that separates charnockite from all ordinary granites is the orthopyroxene <strong>hypersthene</strong>, coexisting with <strong>potassium feldspar (perthite)</strong> and <strong>quartz</strong> under high-grade granulite facies conditions.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Hornblende + K-feldspar + Quartz — INCORRECT</div>
        <p>
          An assemblage of hornblende + K-feldspar + quartz represents an ordinary <strong>hornblende granite</strong> or <strong>amphibolite-facies granitic gneiss</strong>. It lacks the defining orthopyroxene (hypersthene). In fact, charnockite forms when hornblende breaks down and dehydrates into hypersthene.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Sillimanite + K-feldspar + Quartz — INCORRECT</div>
        <p>
          This aluminous, pelitic granulite assemblage is diagnostic of <strong>Khondalite</strong> (a quartz-manganese-garnet-sillimanite schist/gneiss named after the Khond tribes of Odisha and Eastern Ghats), or a metapelitic restite. It represents a metamorphosed aluminous clay/shale, not the quartzofeldspathic hypersthene rock charnockite.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Epidote + Plagioclase + Quartz — INCORRECT</div>
        <p>
          This hydrous, low-to-medium grade assemblage is characteristic of <strong>greenschist or epidote-amphibolite facies</strong> metabasites and epidote tonalites. Epidote is completely unstable at granulite facies temperatures and pressures, breaking down at $T > 550\text{--}650^\circ\text{C}$ long before charnockite forms.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">The Complete Charnockite Series (Holland, 1900) & Granulite Suites</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Division / Rock Name</th>
            <th>Igneous Equivalent</th>
            <th>$\text{SiO}_2\text{ (wt\%)}$</th>
            <th>Essential Mineral Assemblage</th>
            <th>Diagnostic Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Acid: Charnockite (sensu stricto)</strong></td>
            <td><strong>Hypersthene Granite</strong></td>
            <td>$> 70\%$</td>
            <td><strong>Hypersthene + K-Feldspar (Perthite) + Quartz</strong> $\pm$ Oligoclase</td>
            <td>Greasy dark brownish-green luster; high silica; granoblastic</td>
          </tr>
          <tr>
            <td><strong>Acid-Intermediate: Enderbite</strong></td>
            <td>Hypersthene Tonalite</td>
            <td>$65\text{--}70\%$</td>
            <td>Hypersthene + <strong>Plagioclase (Antiperthite)</strong> + Quartz ($Plag \gg Kfs$)</td>
            <td>Sodic, plagioclase-dominated; low K-feldspar</td>
          </tr>
          <tr>
            <td><strong>Intermediate: Mangerite / Jotunite</strong></td>
            <td>Hypersthene Monzonite / Monzodiorite</td>
            <td>$55\text{--}65\%$</td>
            <td>Hypersthene + Plagioclase + K-Feldspar + Clinopyroxene $\pm$ Quartz</td>
            <td>Mesocratic; roughly equal plagioclase and alkali feldspar</td>
          </tr>
          <tr>
            <td><strong>Basic: Basic Charnockite (Norite)</strong></td>
            <td>Hypersthene Gabbro (Two-Pyroxene Granulite)</td>
            <td>$48\text{--}55\%$</td>
            <td>Hypersthene + Clinopyroxene (Augite) + Calcic Plagioclase $\pm$ Garnet</td>
            <td>Melanocratic; dark grey-black; anhydrous mafic granulite</td>
          </tr>
          <tr>
            <td><strong>Ultrabasic: Bahite (Pyroxenite)</strong></td>
            <td>Orthopyroxenite</td>
            <td>$< 45\%$</td>
            <td>Hypersthene + Diopside + Hornblende + Magnetite (Feldspar-free)</td>
            <td>Ultramafic; dense; dark green-black</td>
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
        <div class="p-header">Problem 1: Stoichiometric Biotite Dehydration Reaction & Gibbs Free Energy</div>
        <p>
          Write the balanced chemical reaction for the breakdown of pure phlogopite biotite in the presence of quartz to form enstatite and K-feldspar. Given standard free energies of formation ($\Delta G^\circ_f$): Phlogopite = $-5,835\text{ kJ/mol}$, Quartz = $-856.3\text{ kJ/mol}$, Enstatite = $-1,460.8\text{ kJ/mol}$, K-feldspar = $-3,742.9\text{ kJ/mol}$, and $H_2O\text{ (steam)} = -228.6\text{ kJ/mol}$. Calculate the standard Gibbs free energy of the reaction ($\Delta G^\circ_{\text{rxn}}$) at 298.15 K.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Thermodynamic Derivation:</strong><br>
          The balanced dehydration reaction is:
          $$\text{KMg}_3\text{AlSi}_3\text{O}_{10}(\text{OH})_2\ (\text{Phl}) + 3\text{SiO}_2\ (\text{Qtz}) \longrightarrow 3\text{MgSiO}_3\ (\text{En}) + \text{KAlSi}_3\text{O}_8\ (\text{Kfs}) + \text{H}_2\text{O}$$<br>
          1. Calculate $\sum \Delta G^\circ_f(\text{Reactants})$:
          $$\sum \Delta G^\circ_f(\text{reactants}) = -5,835 + 3(-856.3) = -5,835 - 2,568.9 = -8,403.9\text{ kJ}$$<br>
          2. Calculate $\sum \Delta G^\circ_f(\text{Products})$:
          $$\sum \Delta G^\circ_f(\text{products}) = 3(-1,460.8) + (-3,742.9) + (-228.6) = -4,382.4 - 3,742.9 - 228.6 = -8,353.9\text{ kJ}$$<br>
          3. Calculate $\Delta G^\circ_{\text{rxn}}$:
          $$\Delta G^\circ_{\text{rxn}} = \sum \Delta G^\circ_f(\text{products}) - \sum \Delta G^\circ_f(\text{reactants}) = -8,353.9 - (-8,403.9) = \mathbf{+50.0\text{ kJ/mol}}$$
          <strong>Physical Interpretation:</strong> At 298 K, $\Delta G^\circ > 0$, meaning hydrous biotite + quartz is stable at surface conditions. Because the reaction produces steam ($\Delta S_{\text{rxn}} \gg 0$), the $-T\Delta S$ term dominates at high temperature ($T > 750^\circ\text{C}$), driving $\Delta G_{\text{rxn}}$ negative and precipitating hypersthene charnockite.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Thermodynamic Effect of Water Activity ($a_{H_2O}$) on Charnockitization</div>
        <p>
          The equilibrium constant for the biotite dehydration reaction is given by $\ln K = -\frac{\Delta G^\circ}{RT}$. If the solid phases are pure minerals ($a_{\text{solids}} = 1$), express the equilibrium temperature ($T_{\text{eq}}$) as a function of water activity ($a_{H_2O}$). Explain why $CO_2$ flushing induces "incipient charnockite" formation at Kabbaldurga.
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Fluid Activity Derivation:</strong><br>
          The equilibrium constant expression is:
          $$K = \frac{a_{\text{En}}^3 \cdot a_{\text{Kfs}} \cdot a_{H_2O}}{a_{\text{Phl}} \cdot a_{\text{Qtz}}^3} = a_{H_2O}$$<br>
          $$\Delta G^\circ(T) = -R T \ln(a_{H_2O}) \implies \Delta H^\circ - T\Delta S^\circ = -R T \ln(a_{H_2O})$$<br>
          Solving for equilibrium temperature $T$:
          $$T = \frac{\Delta H^\circ}{\Delta S^\circ - R \ln(a_{H_2O})}$$<br>
          <strong>Kabbaldurga Mechanism:</strong> Influx of juvenile, mantle-derived $CO_2$ dilutes intergranular metamorphic pore fluids, drastically lowering water activity from $a_{H_2O} \approx 1.0$ down to $a_{H_2O} \approx 0.2\text{--}0.3$. Because $\ln(a_{H_2O})$ becomes a large negative number, the denominator increases, <strong>lowering the equilibrium dehydration temperature by $100\text{--}150^\circ\text{C}$</strong>. Consequently, ambient amphibolite-facies gneisses at $\sim 700^\circ\text{C}$ are instantly dehydrated into hypersthene charnockite without requiring any addition of heat!
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Optical Mineralogy: Hypersthene Pleochroic Formula</div>
        <p>
          State the diagnostic optical properties of hypersthene under the petrographic microscope, including its axial character, extinction angle, and characteristic pleochroic colors along its three vibration axes ($\alpha$, $\beta$, $\gamma$).
        </p>
        <div class="p-ans">
          <strong>Optical Properties of Hypersthene (Ferroan Enstatite):</strong><br>
          - <strong>Crystal System:</strong> Orthorhombic ($P_{bca}$).<br>
          - <strong>Extinction:</strong> Parallel (straight) extinction ($0^\circ$) to prismatic $\{110\}$ cleavage in longitudinal sections.<br>
          - <strong>Cleavage:</strong> Two sets of distinct prismatic cleavages intersecting at approximately $87^\circ$ and $93^\circ$ in basal cross-sections.<br>
          - <strong>Optic Sign:</strong> Biaxial Negative ($2V \approx 50\text{--}80^\circ$).<br>
          - <strong>Diagnostic Pleochroism:</strong> The most famous pleochroism in petrology:<br>
            - $\alpha\ (X) = \mathbf{\text{Pink to brownish-red / salmon pink}}$<br>
            - $\beta\ (Y) = \mathbf{\text{Pale yellow to greenish-yellow}}$<br>
            - $\gamma\ (Z) = \mathbf{\text{Pale green to emerald green}}$
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Petrographic Discrimination: Charnockite vs. Enderbite</div>
        <p>
          A granulite facies rock contains $25\%$ quartz, $15\%$ hypersthene, $55\%$ antiperthitic plagioclase ($\text{An}_{32}$), and only $5\%$ microcline. Classify this rock into Holland's terminology and modern IUGS nomenclature.
        </p>
        <div class="p-ans">
          <strong>Classification Derivation:</strong><br>
          - <strong>Felsic Ratio:</strong> Quartz ($Q = 25\%$), Plagioclase ($P = 55\%$), Alkali Feldspar ($A = 5\%$).<br>
          - In the QAP classification, $P / (P + A) = \frac{55}{55 + 5} = \frac{55}{60} = \mathbf{91.7\%}$. This plots directly in Field 5 (Tonalite / Quartz Diorite).<br>
          - <strong>Taxonomic Designation:</strong> Because plagioclase vastly predominates over K-feldspar ($P \gg A$) and the mafic mineral is hypersthene, the rock is an <strong>Enderbite</strong> (Tilley, 1936), the plagioclase-dominant member of the Charnockitic suite, distinct from Charnockite sensu stricto where $A \ge P$.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Physical Cause of the Greasy Luster and Dark Color</div>
        <p>
          Why do acid charnockites ($SiO_2 > 70\%$) appear dark olive-green or greasy dark brown in hand specimen, whereas common calc-alkaline granites of identical silica content appear light pink, white, or light grey?
        </p>
        <div class="p-ans">
          <strong>Solid-State Physics and Optical Scattering:</strong><br>
          1. <strong>Submicroscopic Inclusions:</strong> Charnockites formed at deep lower crustal levels under high confining pressures ($>7\text{ kbar}$). Slow cooling under anhydrous conditions caused $Fe$ and $Ti$ dissolved in the feldspar and quartz lattices at high temperature to precipitate as billions of submicron-scale needles of <strong>ilmenite ($\text{FeTiO}_3$) and rutile ($\text{TiO}_2$)</strong>.<br>
          2. <strong>Micro-Fracture Hydrocarbon/Fluid Films:</strong> Intergranular grain boundaries and micro-cracks host high-density carbonic fluid inclusions and thin films of graphite/chlorite/iron-oxides.<br>
          3. <strong>Rayleigh & Mie Scattering:</strong> These submicroscopic inclusions scatter and absorb light across all visible wavelengths, completely destroying the normal white specular reflection of feldspars and imparting a dark, greasy, waxy appearance.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: The Charnockite-Khondalite Terrain of the Eastern Ghats (EGMB)</div>
        <p>
          In the Eastern Ghats Mobile Belt (EGMB) of Odisha and Andhra Pradesh, charnockites are intimately intercalated with khondalites. Contrast the protoliths and metamorphic environments of these two iconic Indian rock types.
        </p>
        <div class="p-ans">
          <strong>Regional Tectonometamorphic Contrast:</strong><br>
          - <strong>Khondalite (Metasedimentary Protolith):</strong> Formed by ultra-high temperature granulite metamorphism of highly weathered, kaolinite-rich aluminous pelitic sediments (lithomargic clays and bauxitic soils) deposited in passive margins. Mineralogy: Garnet (almandine-pyrope) + Sillimanite + Quartz + K-feldspar $\pm$ Graphite.<br>
          - <strong>Charnockite (Meta-igneous / Ortho-gneiss Protolith):</strong> Formed by deep crustal granulite metamorphism and dehydration of calc-alkaline igneous granitoids, tonalites, and diorites under high-density $CO_2$ conditions. Mineralogy: Hypersthene + K-feldspar + Quartz $\pm$ Plagioclase.<br>
          - <strong>Geodynamic Setting:</strong> Both were fused and metamorphosed together during Proterozoic collisional orogenies (Grenvillian / Kuunga orogenies, ~1000–900 Ma) when India docked against East Antarctica.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Geothermobarometry of the Garnet-Orthopyroxene Pair</div>
        <p>
          In garnet-bearing charnockites, the exchange of iron and magnesium between garnet and hypersthene:
          $$\frac{1}{3}\text{Mg}_3\text{Al}_2\text{Si}_3\text{O}_{12}\ (\text{Pyrope}) + \text{FeSiO}_3\ (\text{Ferrosilite}) \rightleftharpoons \frac{1}{3}\text{Fe}_3\text{Al}_2\text{Si}_3\text{O}_{12}\ (\text{Almandine}) + \text{MgSiO}_3\ (\text{Enstatite})$$
          is used as a geothermometer (Harley, 1984). If the distribution coefficient is $K_D = \frac{(Fe/Mg)_{\text{grt}}}{(Fe/Mg)_{\text{opx}}} = 3.25$, explain how $K_D$ responds to increasing metamorphic temperature.
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Response:</strong><br>
          - The exchange reaction is endothermic in the forward direction. Consequently, as metamorphic temperature ($T$) increases, thermal agitation overcomes the energy barrier that selectively partitions $Fe^{2+}$ into the smaller 8-coordinated garnet dodecahedral site.<br>
          - Therefore, with <strong>increasing temperature, $K_D$ decreases systematically toward unity ($K_D \to 1.0$)</strong>.<br>
          - A high $K_D$ value ($3.25$) reflects retrograde cooling or lower granulite facies ($T \approx 700\text{--}750^\circ\text{C}$), whereas peak ultra-high temperature (UHT) granulites ($T > 950^\circ\text{C}$) yield lower $K_D$ values ($K_D \approx 1.8\text{--}2.2$).
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Retrograde Metamorphism: Uralitization of Hypersthene</div>
        <p>
          During exhumation and hydration of a charnockite terrain, hypersthene is often partially replaced along cracks and margins by green amphibole (hornblende) and secondary biotite. Name this texture and write the general hydration reaction.
        </p>
        <div class="p-ans">
          <strong>Retrograde Reaction & Nomenclature:</strong><br>
          - <strong>Textural Name:</strong> <strong>Uralitization</strong> (when pyroxene is replaced by fibrous amphibole) or <strong>kelyphitic / corona rim</strong>.<br>
          - <strong>Hydration Reaction:</strong> Influx of aqueous fluids ($H_2O$) during cooling and crustal uplift reverses the prograde dehydration:
          $$\text{Hypersthene} + \text{Plagioclase} + \text{K-feldspar} + \text{H}_2\text{O} \longrightarrow \text{Hornblende} + \text{Biotite} + \text{Quartz}$$<br>
          - <strong>Significance:</strong> Identifies retrograde amphibolite-facies overprinting of pristine anhydrous granulite facies charnockites.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 80, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q080_Charnockite_Composition_Hypersthene_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q080: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q080()
