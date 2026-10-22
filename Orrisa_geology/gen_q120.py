#!/usr/bin/env python3
"""
Q120 Generator: Skarns, Carbonate Contact Metasomatism & Calc-Silicate Petrology
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q120():
    title = r"Q120: Metamorphic Petrology: Skarn Contact Metasomatism in Carbonate Bedrock | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Skarns"
    h1_title = "Q120: Skarn Genesis: Contact Metasomatic Calc-Silicate Zones around Carbonate Intrusions"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 120<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 29: Metasomatism and Skarns, pp. 635–648; Fig. 29.4); Lawrence D. Meinert, G.M. Dipple, and S. Nicolescu (2005), <em>World Skarn Deposits</em> (Economic Geology 100th Anniversary Volume, pp. 299–336); K.M. Bangar, <em>Principles of Engineering Geology</em> (pp. 81–84, 180); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND ETYMOLOGY OF SKARNS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Etymology & Petrogenetic Architecture of Skarns</div>
    <div class="card-body">
      <p>
        The term <strong>skarn</strong> is an old Swedish mining term originally applied by miners in the Bergslagen ore district of central Sweden to designate the tough, coarse-grained, calc-silicate gangue rocks enclosing iron-ore and sulfide deposits. In American geological literature, it is often termed <strong>tactite</strong>.
      </p>
      <p>
        In modern metamorphic petrology and economic geology (Meinert et al., 2005; Winter, 2014, pp. 635–648; Bangar, p. 81), a <strong>skarn</strong> is formally defined as a coarse-grained, calc-silicate metamorphic rock or reaction zone developed in the <strong>contact area where an igneous intrusion invades carbonate sedimentary rocks (limestone, $\text{CaCO}_3$, or dolomite, $\text{CaMg(CO}_3)_2$)</strong>.
      </p>
      <p>
        Skarn formation is driven by high-temperature <strong>contact metasomatism</strong>: hot, silica- and iron-bearing hydrothermal fluids exsolved from the cooling magma react aggressively with the calcium- and magnesium-rich carbonate wall rocks, replacing calcite and dolomite with a complex suite of calc-silicate minerals.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q120/winter_p494_skarn_carbonate_contact_metasomatism.png" alt="Skarn Zonation and Contact Metasomatism from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 120.1 — Contact Metasomatic Zonation and Skarn Evolution:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 494). Illustrates the spatial development of Endoskarn (within the intrusive pluton margin) and Exoskarn (within the invaded carbonate bedrock), with concentric calc-silicate reaction zones (Garnet $\rightarrow$ Pyroxene $\rightarrow$ Wollastonite $\rightarrow$ Marble).
        </div>
      </div>

      <h4>Spatial Anatomy: Exoskarn vs. Endoskarn</h4>
      <ul>
        <li><strong>Exoskarn:</strong> Metasomatic replacement that develops <strong>outside the intrusion within the carbonate sedimentary host rock</strong>. Exoskarns typically comprise the vast majority of the skarn volume and host major metallic ore deposits.</li>
        <li><strong>Endoskarn:</strong> Metasomatic replacement that develops <strong>within the margin of the igneous intrusion itself</strong>. Inward diffusion of calcium ($\text{Ca}^{2+}$) from dissolving limestone alters the granitic magma/rock, converting primary quartz and K-feldspar into secondary plagioclase, diopsidic pyroxene, epidote, and scapolite.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: MINERALOGY & EVOLUTIONARY STAGES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Mineralogical Paragenesis & Evolutionary Stages of Skarn Systems</div>
    <div class="card-body">
      <h4>Diagnostic Calc-Silicate Mineral Suites</h4>
      <p>
        Depending on whether the invaded carbonate protolith is a pure limestone or a magnesian dolomite, two major geochemical skarn suites develop:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Carbonate Host Rock</th>
            <th>Skarn Class</th>
            <th>Diagnostic Anhydrous Prograde Minerals</th>
            <th>Diagnostic Hydrous Retrograde Minerals</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Limestone ($\text{CaCO}_3$)</strong></td>
            <td><strong>Calcic Skarn</strong></td>
            <td>Grandite Garnet (Grossular-Andradite), Clinopyroxene (Diopside-Hedenbergite), Wollastonite ($\text{CaSiO}_3$)</td>
            <td>Epidote / Clinozoisite, Calcic Amphibole (Actinolite/Hornblende), Calcite, Quartz</td>
          </tr>
          <tr>
            <td><strong>Dolomite ($\text{CaMg(CO}_3)_2$)</strong></td>
            <td><strong>Magnesian Skarn</strong></td>
            <td>Diopside, Forsterite ($\text{Mg}_2\text{SiO}_4$), Spinel ($\text{MgAl}_2\text{O}_4$), Humite/Chondrodite</td>
            <td>Serpentine (antigorite/lizardite), Talc, Tremolite, Phlogopite, Brucite, Magnetite</td>
          </tr>
        </tbody>
      </table>

      <h4>The Four Sequential Stages of Skarn Evolution</h4>
      <ol>
        <li><strong>Stage 1: Isochemical Contact Metamorphism (Early Thermal):</strong> Conductive heating of carbonate beds before significant fluid release. Produces fine-grained, barren <em>calc-silicate hornfelses</em> and crystalline marble.</li>
        <li><strong>Stage 2: Prograde Metasomatism (High-Temperature Magmatic Fluids, $T \approx 500\text{--}700^\circ\text{C}$):</strong> Exsolution of saline, supercritical magmatic-hydrothermal fluids carrying $\text{Si, Fe, Al, Mg}$. Massive fluid infiltration drives decarbonation, crystallizing coarse-grained anhydrous garnet, pyroxene, and wollastonite.</li>
        <li><strong>Stage 3: Retrograde Alteration & Ore Deposition ($T \approx 300\text{--}450^\circ\text{C}$):</strong> As the pluton cools, meteoric groundwaters collapse inward, mixing with hydrothermal brines. Early anhydrous silicates are hydrously altered (garnet $\rightarrow$ epidote; pyroxene $\rightarrow$ actinolite/tremolite). This cooling and pH-drop triggers the <strong>massive precipitation of economic metal sulfides and oxides</strong>.</li>
        <li><strong>Stage 4: Post-Metasomatic Carbonatization ($T < 300^\circ\text{C}$):</strong> Final deposition of low-temperature calcite, quartz, and fluorite veins in open fractures.</li>
      </ol>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 120:</strong> Metamorphic zone developed in the contact area around igneous rock intrusions when carbonate sedimentary rocks are invaded called :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Carbonatites</div>
        <div class="option-item"><strong>(B)</strong> Metamorphites</div>
        <div class="option-item correct-option"><strong>(C)</strong> Skarn</div>
        <div class="option-item"><strong>(D)</strong> Hornblendite</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(C) Skarn</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Carbonatites</div>
        <p>
          <strong>Incorrect:</strong> <strong>Carbonatites</strong> are rare <strong>igneous rocks</strong> of mantle origin composed of greater than $50\%$ primary carbonate minerals (calcite, dolomite, ankerite). They crystallize directly from mantle-derived carbonatite magmas associated with continental rifts and alkaline complexes (e.g., Oldoinyo Lengai in Tanzania, Amba Dongar in Gujarat). They are not contact metamorphic reaction zones formed around invaded carbonate sediments.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Metamorphites</div>
        <p>
          <strong>Incorrect:</strong> "Metamorphites" is an obsolete, non-specific general German term (<em>Metamorphite</em>) loosely referring to any metamorphic rock in the broadest sense. It does not designate the specific contact metasomatic zone developed between igneous intrusions and invaded carbonate sedimentary rocks.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-c">Option (C) Confirmed — Skarn</div>
        <p>
          <strong>Correct:</strong> By universal definition in metamorphic petrology and economic mineralogy (Meinert et al., 2005; Winter, 2014, p. 635; Bangar, p. 81), <strong>skarn</strong> (or tactite) is the definitive geological term for the contact metasomatic zone and calc-silicate rock body developed when an igneous intrusion invades carbonate sedimentary rocks (limestone or dolomite).
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Hornblendite</div>
        <p>
          <strong>Incorrect:</strong> <strong>Hornblendite</strong> is a coarse-grained <strong>ultramafic igneous plutonic rock</strong> composed of $> 90\%$ hornblende amphibole. It is neither a contact metamorphic zone nor derived from invaded carbonate rocks.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Classification of Economic Skarn Deposit Types</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Economic Skarn Type</th>
            <th>Associated Intrusive Magma</th>
            <th>Diagnostic Ore Minerals</th>
            <th>Primary Calc-Silicate Gangue Assemblage</th>
            <th>Tectonic Setting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Tungsten (W) Skarn</strong></td>
            <td>Coarse-grained, porphyritic, peraluminous to metaluminous granites / granodiorites</td>
            <td><strong>Scheelite ($\text{CaWO}_4$)</strong>, Molybdenite, Chalcopyrite</td>
            <td>Andradite-rich Garnet, Hedenbergite-rich Pyroxene, Vesuvianite</td>
            <td>Continental collision orogens / continental magmatic arcs</td>
          </tr>
          <tr>
            <td><strong>Copper (Cu) Skarn</strong></td>
            <td>Porphyritic quartz monzonite / granodiorite stocks (porphyry Cu systems)</td>
            <td><strong>Chalcopyrite ($\text{CuFeS}_2$)</strong>, Bornite, Magnetite</td>
            <td>Andradite Garnet, Diopsidic Augite, Wollastonite, Actinolite</td>
            <td>Andean-type continental volcanic arcs</td>
          </tr>
          <tr>
            <td><strong>Iron (Fe) Skarn</strong></td>
            <td>Primitive island-arc diorite, gabbro, or quartz diorite plutons</td>
            <td><strong>Magnetite ($\text{Fe}_3\text{O}_4$)</strong>, specular Hematite $\pm$ Pyrite</td>
            <td>Epidote, Grossular Garnet, Ferrosalite Pyroxene, Scapolite</td>
            <td>Oceanic island arcs, accretionary subduction complexes</td>
          </tr>
          <tr>
            <td><strong>Zinc-Lead (Zn-Pb) Skarn</strong></td>
            <td>Distal granitic dikes, sills, or buried blind stocks</td>
            <td><strong>Sphalerite ($\text{ZnS}$)</strong>, Galena ($\text{PbS}$), Chalcopyrite</td>
            <td>Mn-rich Pyroxene (Johannsenite), Mn-rich Garnet (Spessartine), Bustamite</td>
            <td>Continental rifts, back-arc basins (distal carbonate replacement)</td>
          </tr>
          <tr>
            <td><strong>Gold (Au) Skarn</strong></td>
            <td>Reduced dioritic to granodioritic plutons with low $\text{Fe}_2\text{O}_3/\text{FeO}$</td>
            <td>Native Gold, Bismuth tellurides, Arsenopyrite, Pyrrhotite</td>
            <td>Ferrous pyroxene (Hedenbergite $> 70\%$), K-feldspar, Actinolite</td>
            <td>Accretionary volcanic arcs, back-arc extensional margins</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Practice Problems & Analytical Derivations</div>
    <div class="card-body">
      <div class="problem-box">
        <h4>Practice Problem 1</h4>
        <p>A granitic pluton intrudes a sequence of pure limestone ($\text{CaCO}_3$). At the contact, a prominent white bladed calc-silicate mineral forms according to the reaction $\text{CaCO}_3 + \text{SiO}_2 \rightarrow \text{Mineral X} + \text{CO}_2\uparrow$. Identify Mineral X, name the reaction type, and calculate its equilibrium condition.</p>
        <p><strong>Solution:</strong>
          - <strong>Mineral X:</strong> <strong>Wollastonite ($\text{CaSiO}_3$)</strong>, a triclinic single-chain inosilicate.
          - <strong>Reaction Type:</strong> Decarbonation contact metasomatic reaction.
          - <strong>Equilibrium Condition:</strong> In the presence of silica-rich magmatic fluids, calcite reacts with dissolved silica:
          $$\text{CaCO}_3\text{ (calcite)} + \text{SiO}_2\text{ (quartz/fluid silica)} \rightleftharpoons \text{CaSiO}_3\text{ (wollastonite)} + \text{CO}_2\uparrow$$
          At a shallow contact pressure of $P = 1.0\text{ kbar}$, this reaction proceeds to the right at temperatures of <strong>$550^\circ\text{C}$ to $650^\circ\text{C}$</strong> (depending on $X_{\text{CO}_2}$), defining the innermost wollastonite zone of calcic exoskarns.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain why garnets in calcic skarns belong to the "Grandite" series rather than the "Pyralspite" series.</p>
        <p><strong>Solution:</strong>
          Garnet group minerals are divided into two solid-solution series based on chemistry:
          - <strong>Pyralspite (Pyrope-Almandine-Spessartine):</strong> Calcium-poor, aluminous garnets characteristic of pelitic schists and mantle peridotites.
          - <strong>Ugrandite / Grandite (Grossular-Andradite):</strong> Calcium-rich garnets ($\text{Ca}_3\text{(Al,Fe}^{3+})_2\text{Si}_3\text{O}_{12}$).
          Because the host rock of a skarn is limestone ($\text{CaCO}_3$), the system is flooded with calcium ($\text{Ca}^{2+}$). Concurrently, magmatic hydrothermal fluids introduce $\text{Fe}^{3+}$ and $\text{Al}^{3+}$. Consequently, skarn garnets crystallize exclusively as <strong>Grossular ($\text{Ca}_3\text{Al}_2\text{Si}_3\text{O}_{12}$) - Andradite ($\text{Ca}_3\text{Fe}_2\text{Si}_3\text{O}_{12}$)</strong> solid solutions (Grandites), frequently displaying spectacular oscillatory optical zoning and anomalous birefringence under crossed polars.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is an "endoskarn" and what mineralogical transformation occurs within the margin of an invaded granodiorite pluton?</p>
        <p><strong>Solution:</strong>
          An <strong>endoskarn</strong> is the metasomatically altered zone developed <strong>within the intrusive igneous rock itself</strong> bordering the carbonate contact. Diffusive mass transfer forces calcium ($\text{Ca}^{2+}$) from the dissolving limestone inward into the igneous margin, while silica ($\text{SiO}_2$) and alkalis diffuse outward. This calcium enrichment destroys primary igneous biotite, hornblende, and quartz, converting the granodiorite margin into an endoskarn assemblage of <strong>calcic plagioclase, diopsidic pyroxene, epidote, and scapolite</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Distinguish between a "calcic skarn" and a "magnesian skarn" in terms of carbonate protolith and characteristic pyroxene/olivine mineralogy.</p>
        <p><strong>Solution:</strong>
          - <strong>Calcic Skarn:</strong> Formed in <strong>pure limestone ($\text{CaCO}_3$)</strong>; pyroxenes belong to the diopside-hedenbergite series ($\text{Ca(Mg,Fe)Si}_2\text{O}_6$); olivine is absent; dominant garnet is andradite/grossular.
          - <strong>Magnesian Skarn:</strong> Formed in <strong>dolomite ($\text{CaMg(CO}_3)_2$)</strong>; dominated by magnesium-rich phases: <strong>forsterite olivine ($\text{Mg}_2\text{SiO}_4$)</strong>, pure diopside, spinel ($\text{MgAl}_2\text{O}_4$), humite group minerals, and serpentine/talc retrograde pseudomorphs.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Why does economic sulfide ore mineralization (e.g., chalcopyrite, sphalerite, galena) precipitate predominantly during the retrograde stage of skarn evolution rather than during prograde metasomatism?</p>
        <p><strong>Solution:</strong>
          During early prograde metasomatism ($550\text{--}700^\circ\text{C}$), fluids are ultra-hot, highly saline, oxidized, and slightly acidic, keeping metals in soluble chloride complexes ($\text{CuCl}_2^-, \text{ZnCl}_4^{2-}$). During the retrograde stage ($300\text{--}450^\circ\text{C}$):
          1. Fluid temperatures drop drastically.
          2. Meteoric water incursion dilutes salinity and neutralizes acidity via extensive reaction with surrounding marble.
          3. Sulfur activity rises as hydrous silicates form.
          This cooling and pH neutralization destabilizes metal chloride complexes, driving the <strong>spontaneous, massive precipitation of metal sulfides (chalcopyrite, sphalerite, galena)</strong> replacing earlier anhydrous garnets and pyroxenes.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is a "stratiform skarn" (or mantos) and what geological control dictates its geometry?</p>
        <p><strong>Solution:</strong>
          A <strong>stratiform skarn (manto skarn)</strong> is a tabular, bedding-parallel skarn body that extends horizontally away from a central feeder dike or fault for hundreds of meters along a specific, highly receptive sedimentary carbonate bed. Its geometry is controlled by <strong>lithological permeability and chemical reactivity</strong>: hydrothermal fluids preferentially infiltrate a porous, reactive limestone bed sandwiched between impermeable shale or sandstone aquitards.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>In exploration geochemistry, what diagnostic heavy mineral found in panned stream concentrates serves as a pathfinder for tungsten skarns?</p>
        <p><strong>Solution:</strong>
          The primary pathfinder mineral is <strong>Scheelite ($\text{CaWO}_4$)</strong>. Scheelite is heavy (specific gravity $5.9\text{--}6.1\text{ g/cm}^3$) and highly resistant to mechanical abrasion, concentrating in stream sediments. Crucially, scheelite exhibits brilliant <strong>bright sky-blue to creamy-yellow fluorescence under shortwave ultraviolet (UV) light ($254\text{ nm}$)</strong>, allowing field geologists to detect trace grains in night pan-sampling.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>How does the formation of a skarn zone impact geotechnical tunneling and foundation engineering in carbonate terrains?</p>
        <p><strong>Solution:</strong>
          Skarns introduce <strong>extreme, erratic mechanical heterogeneity</strong> into a rock mass:
          1. <strong>Abrasiveness:</strong> Prograde skarn zones containing grandite garnet and pyroxene have exceptionally high unconfined compressive strength ($\sigma_c > 200\text{--}300\text{ MPa}$) and high Cerchar abrasiveness, causing severe wear on Tunnel Boring Machine (TBM) cutter discs.
          2. <strong>Water Inrush Hazards:</strong> Retrograde skarn zones and marble contact interfaces frequently harbor cavernous dissolution voids, open vugs, and intense jointing that channel high-pressure groundwater inrushes into excavations.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=120,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q120_Skarn_Carbonate_Contact_Metasomatism_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q120: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q120()
