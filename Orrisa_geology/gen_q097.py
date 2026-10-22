#!/usr/bin/env python3
"""
Q097 Generator: Chemical Sedimentary Rocks & Gypsum Evaporite Petrography
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q097():
    title = r"Q097: Sedimentary Petrology: Chemical Sedimentary Rocks & Gypsum Evaporites | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Evaporites"
    h1_title = "Q097: Chemical Sedimentary Rocks: Genesis, Usiglio's Evaporation Sequence & Gypsum"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 97<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 7: Chemical and Biochemical Sedimentary Rocks / Evaporites, pp. 195–210; Table 7.1); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 75–78, 175); Maurice E. Tucker, <em>Sedimentary Petrology: An Introduction to the Origin of Sedimentary Rocks</em>; G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 148–152)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND CLASSIFICATION OF CHEMICAL SEDIMENTARY ROCKS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Classification & Evaporation Dynamics of Chemical Sediments</div>
    <div class="card-body">
      <p>
        In sedimentary petrology (Boggs, 2014, pp. 195–210; Bangar, p. 75; Tucker, 2001), <strong>chemical sedimentary rocks</strong> are defined as rocks formed primarily by the <strong>direct inorganic chemical precipitation of dissolved mineral solutes</strong> from surface or subsurface aqueous solutions (marine seawater, saline lake brines, or mineral springs) driven by changes in chemical equilibrium, evaporation, temperature, pH, or redox potential ($Eh$).
      </p>
      <p>
        Among the options provided, <strong>gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$)</strong> represents the definitive, classic prototype of a <strong>marine and non-marine evaporite</strong>—a premier chemical sedimentary rock.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q97/boggs_table7_1_chemical_evaporite_gypsum.png" alt="Chemical Sedimentary Rocks and Evaporite Mineralogy from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 97.1 — Chemical Classification of Evaporites and Sedimentary Precipitates:</strong> Authentic textbook table from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, Table 7.1). Systematically categorizes evaporites, marine sulfate precipitates (gypsum, anhydrite), halides (halite, sylvite), and borates formed by chemical precipitation from supersaturated brines.
        </div>
      </div>

      <h4>Usiglio's (1849) Experimental Evaporation Sequence of Seawater</h4>
      <p>
        In a landmark experimental study, J. Usiglio evaporated normal seawater (salinity $\approx 35\text{ g/L}$ or $3.5\%$) and documented the exact sequence and volumetric brine concentration stages at which chemical minerals precipitate:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Precipitation Stage</th>
            <th>Mineral Phase Precipitated</th>
            <th>Chemical Formula</th>
            <th>Brine Volume Remaining (% of Original)</th>
            <th>Brine Salinity Range</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Stage I (Carbonate)</strong></td>
            <td>Calcite / Aragonite</td>
            <td>$\text{CaCO}_3$</td>
            <td>$50\%$ to $20\%$</td>
            <td>$70\text{--}140\text{ g/L}$</td>
          </tr>
          <tr>
            <td><strong>Stage II (Sulfate)</strong></td>
            <td><strong>Gypsum</strong></td>
            <td>$\text{CaSO}_4\cdot 2\text{H}_2\text{O}$</td>
            <td><strong>$19\%$ to $10\%$</strong></td>
            <td><strong>$140\text{--}350\text{ g/L}$</strong></td>
          </tr>
          <tr>
            <td><strong>Stage III (Halide)</strong></td>
            <td>Halite (Rock Salt)</td>
            <td>$\text{NaCl}$</td>
            <td>$9.5\%$ to $4.0\%$</td>
            <td>$350\text{--}450\text{ g/L}$</td>
          </tr>
          <tr>
            <td><strong>Stage IV (Bitterns)</strong></td>
            <td>Sylvite, Carnallite, Kieserite</td>
            <td>$\text{KCl}, \text{KMgCl}_3\cdot 6\text{H}_2\text{O}, \text{MgSO}_4\cdot\text{H}_2\text{O}$</td>
            <td>$< 4.0\%$ (Extreme desiccation)</td>
            <td>$> 450\text{ g/L}$</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: GYPSUM PETROLOGY & ANHYDRITE TRANSFORMATION -->
  <div class="card">
    <div class="card-header bg-emerald">2. Gypsum Crystal Chemistry, Diagenetic Dehydration & Industrial Applications</div>
    <div class="card-body">
      <h4>Crystal Structure and Mineralogical Varieties</h4>
      <p>
        Gypsum crystallizes in the <strong>monoclinic crystal system ($2/m$)</strong> with a distinctive layered sheet structure: layers of $\text{Ca}^{2+}$ and $\text{SO}_4^{2-}$ ions are bonded by weak hydrogen bonds via neutral interlayer $\text{H}_2\text{O}$ molecules. This molecular structure gives rise to its perfect $\{010\}$ cleavage, very low Mohs hardness of $2.0$, and multiple macroscopic varieties:
      </p>
      <ul>
        <li><strong>Selenite:</strong> Transparent, colorless, flawless cleavage sheets with pearly to vitreous luster.</li>
        <li><strong>Satin Spar:</strong> Silky, fibrous variety exhibiting a chatoyant fibrous sheen.</li>
        <li><strong>Alabaster:</strong> Fine-grained, massive, snow-white or translucent variety prized for ornamental carving.</li>
      </ul>

      <h4>Diagenetic Gypsum-Anhydrite Reversible Transition</h4>
      <p>
        Under burial diagenesis, gypsum dehydrates into <strong>anhydrite ($\text{CaSO}_4$)</strong> as temperature and pressure increase:
        $$\text{CaSO}_4\cdot 2\text{H}_2\text{O}\text{ (gypsum)} \xrightarrow{\Delta, P} \text{CaSO}_4\text{ (anhydrite)} + 2\text{H}_2\text{O}$$
        This dehydration reaction occurs typically at burial depths between $600\text{ and } 1000\text{ m}$ (temperatures $\sim 42\text{--}60^\circ\text{C}$ depending on pore-water salinity). Dehydration causes a <strong>$38\%$ volume loss</strong> of solid mineral phase, releasing free water that may trigger anomalous overpressure. Conversely, when uplift brings anhydrite back near the surface, contact with meteoric groundwater rehydrates it back to gypsum, causing a <strong>$60\%$ volumetric expansion</strong> that shatters overlying rock strata.
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 97:</strong> ——— is an example of Chemical Sedimentary Rock.
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Breccia</div>
        <div class="option-item"><strong>(B)</strong> Laterite</div>
        <div class="option-item"><strong>(C)</strong> Bauxite</div>
        <div class="option-item correct-option"><strong>(D)</strong> Gypsum</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(D) Gypsum</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Breccia</div>
        <p>
          <strong>Incorrect:</strong> <strong>Breccia</strong> is a classic <strong>clastic (detrital/mechanically formed)</strong> sedimentary rock consisting of angular to sub-angular fragments larger than $2\text{ mm}$ (gravel, pebble, or cobble size) held together by a finer mineral matrix and cement. It is formed by the mechanical fracturing, transport, and deposition of pre-existing rocks (e.g., fault breccia, talus/scree breccia, volcanic breccia), with no involvement of direct inorganic chemical precipitation from solution.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Laterite</div>
        <p>
          <strong>Incorrect:</strong> <strong>Laterite</strong> is a <strong>residual rock or soil</strong> (regolith / paleosol) produced by extreme, intensive subaerial sub-tropical to tropical chemical weathering (pedogenesis). Under high rainfall and warm temperatures, intense leaching removes mobile alkalis ($\text{Na}^+, \text{K}^+$), alkaline earths ($\text{Ca}^{2+}, \text{Mg}^{2+}$), and silica ($\text{SiO}_2$), leaving an insoluble residual accumulation of hydrated iron oxides (goethite, hematite) and clay minerals. It is classified as a residual weathering product, not a chemical sedimentary rock precipitated from a water body.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Bauxite</div>
        <p>
          <strong>Incorrect:</strong> Like laterite, <strong>bauxite</strong> is an in-situ <strong>residual deposit</strong> formed by prolonged tropical leaching of aluminous silicate rocks (nepheline syenite, basalt, clay-bearing limestone). The leaching of silica leaves a concentration of insoluble aluminum hydroxides—principally gibbsite ($\text{Al(OH)}_3$), boehmite ($\gamma\text{-AlO(OH)}$), and diaspore ($\alpha\text{-AlO(OH)}$). In sedimentary taxonomy, bauxites are designated as residual chemorelicts or paleosols rather than primary chemical sedimentary precipitates.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-d">Option (D) Confirmed — Gypsum</div>
        <p>
          <strong>Correct:</strong> By universal scientific and textbook consensus (Boggs, 2014, p. 195; Bangar, p. 75; Tucker, 2001), <strong>gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$)</strong> is the classic exemplar of a <strong>chemical sedimentary rock</strong>. It forms by inorganic crystallization directly from evaporating saline brines when seawater is concentrated to roughly five times its normal salinity ($\sim 19\%$ of original volume remaining), forming thick bedded evaporite deposits.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparative Matrix: Sedimentary Genetic Categories</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Candidate Rock</th>
            <th>Genetic Sedimentary Classification</th>
            <th>Primary Formation Mechanism</th>
            <th>Chemical / Mineralogical Composition</th>
            <th>Typical Depositional / Genesis Setting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Gypsum</strong></td>
            <td><strong>Chemical Sedimentary (Evaporite)</strong></td>
            <td>Inorganic solar evaporation and supersaturation from brine</td>
            <td>Hydrous calcium sulfate ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$)</td>
            <td>Restricted marine basins, coastal sabkhas, playa lakes</td>
          </tr>
          <tr>
            <td><strong>Breccia</strong></td>
            <td><strong>Clastic / Detrital Sedimentary</strong></td>
            <td>Mechanical fragmentation and short-distance physical transport</td>
            <td>Heterogeneous angular rock clasts ($> 2\text{ mm}$) + matrix</td>
            <td>Scree/talus slopes, alluvial fan heads, tectonic fault scarps</td>
          </tr>
          <tr>
            <td><strong>Laterite</strong></td>
            <td><strong>Residual Weathering Product (Paleosol)</strong></td>
            <td>In-situ tropical leaching of silica and alkalis</td>
            <td>Hydrated ferric iron oxides ($\text{Fe}_2\text{O}_3\cdot n\text{H}_2\text{O}$, goethite)</td>
            <td>Subaerial tropical weathering plateaus and peneplains</td>
          </tr>
          <tr>
            <td><strong>Bauxite</strong></td>
            <td><strong>Residual Weathering Product (Ore)</strong></td>
            <td>Intense desilication of aluminous bedrock in wet tropics</td>
            <td>Hydrated aluminum oxides ($\text{Al(OH)}_3$, gibbsite, boehmite)</td>
            <td>Tropical karst depressions (karst bauxite) or weathered peneplains</td>
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
        <p>In Usiglio's seawater evaporation experiment, calculate the volume of original normal seawater ($1000\text{ liters}$) that must evaporate before the first crystal of gypsum begins to precipitate.</p>
        <p><strong>Solution:</strong>
          According to Usiglio's empirical measurements, gypsum begins to precipitate when seawater is concentrated to approximately <strong>$19\%$ of its original volume</strong>.
          $$\text{Volume Remaining} = 1000\text{ L} \times 0.19 = 190\text{ liters}$$
          Therefore, the volume of water that must evaporate before gypsum precipitation begins is:
          $$\text{Volume Evaporated} = 1000\text{ L} - 190\text{ L} = 810\text{ liters (or } 81\%\text{ evaporated)}.$$
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain the mineralogical and volumetric transformation that occurs when deep-seated anhydrite ($\text{CaSO}_4$) is brought into the near-surface weathering zone by tectonic uplift and erosion.</p>
        <p><strong>Solution:</strong>
          In the near-surface zone, anhydrite reacts with meteoric groundwater and rehydrates to form gypsum:
          $$\text{CaSO}_4\text{ (anhydrite)} + 2\text{H}_2\text{O} \rightarrow \text{CaSO}_4\cdot 2\text{H}_2\text{O}\text{ (gypsum)}$$
          The molar volume of anhydrite is $46.0\text{ cm}^3\text{/mol}$, while the molar volume of gypsum is $74.7\text{ cm}^3\text{/mol}$. This represents an immense <strong>volumetric solid expansion of approximately $+62.4\%$</strong>. In the field, this massive expansion generates intense swelling pressures that buckle, heave, and shatter overlying rock strata, creating folded "enterolithic structures."
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>State two common varieties of gypsum and provide their diagnostic physical properties.</p>
        <p><strong>Solution:</strong>
          1. <strong>Selenite:</strong> Transparent, colorless crystal plates with perfect micaceous cleavage $\{010\}$, vitreous to pearly luster, and flexibility in thin sheets.
          2. <strong>Satin Spar:</strong> Fibrous, silky aggregate of parallel needle-like crystals displaying prominent light reflection (chatoyancy or "cat's-eye" effect).
          3. <strong>Alabaster:</strong> Dense, fine-grained, snow-white to lightly tinted massive variety with Mohs hardness $2.0$, easily carved with a fingernail.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What is a "sabkha" in sedimentology, and what evaporite mineral assemblage characteristically precipitates there?</p>
        <p><strong>Solution:</strong>
          A <strong>sabkha</strong> (Arabic for salt flat) is a broad, supratidal mudflat or coastal plain bordering an arid, hypersaline sea (e.g., the Trucial Coast of the Persian Gulf). Intense solar evaporation draws pore fluids upward via evaporative pumping, driving the precipitation of <strong>nodular anhydrite ("chicken-wire" texture), gypsum crystals (desert roses), and secondary dolomite</strong> within the intertidal sediment matrix.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Why does calcite precipitate from evaporating seawater well before gypsum begins to crystallize?</p>
        <p><strong>Solution:</strong>
          The precipitation order is controlled strictly by the <strong>solubility product ($K_{sp}$)</strong> of the respective minerals:
          - For Calcite ($\text{CaCO}_3$): $K_{sp} \approx 3.3 \times 10^{-9}\text{ at } 25^\circ\text{C}$.
          - For Gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$): $K_{sp} \approx 3.1 \times 10^{-5}\text{ at } 25^\circ\text{C}$.
          Because calcite is roughly four orders of magnitude less soluble than gypsum, the ion activity product $[\text{Ca}^{2+}][\text{CO}_3^{2-}]$ exceeds $K_{sp}$ as soon as seawater concentrates by a factor of 2 ($50\%$ volume remaining), whereas $[\text{Ca}^{2+}][\text{SO}_4^{2-}]$ does not exceed the solubility product of gypsum until seawater is concentrated by a factor of 5 ($19\%$ volume remaining).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is "Plaster of Paris" chemically, and how is it manufactured from naturally occurring sedimentary gypsum?</p>
        <p><strong>Solution:</strong>
          Plaster of Paris is calcium sulfate hemihydrate ($\text{CaSO}_4\cdot 0.5\text{H}_2\text{O}$ or $2\text{CaSO}_4\cdot\text{H}_2\text{O}$). It is manufactured by heating natural sedimentary gypsum to approximately $150^\circ\text{C}\text{ to } 160^\circ\text{C}$ in a kiln (calcination):
          $$\text{CaSO}_4\cdot 2\text{H}_2\text{O} \xrightarrow{150^\circ\text{C}} \text{CaSO}_4\cdot 0.5\text{H}_2\text{O} + 1.5\text{H}_2\text{O}\uparrow$$
          When mixed with water, it rehydrates back to gypsum, setting into an interlocking, rigid crystalline mass with a slight expansion ($0.5\%$), which ensures sharp casting of molds.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Distinguish between a primary evaporite and a diagenetic replacement evaporite in sedimentary petrography.</p>
        <p><strong>Solution:</strong>
          - <strong>Primary Evaporite:</strong> Precipitates directly from the free water column of a brine body, exhibiting depositional bedded features such as bottom-grown chevron or swallowtail gypsum crystal palisades, subaqueous laminations, and ripple marks.
          - <strong>Diagenetic Evaporite:</strong> Grows displacively or replacively within host sediment pore spaces post-depositionally from interstitial brines, forming nodular anhydrite ("chicken-wire" or enterolithic structures), poikilotopic cements, or pseudomorphic crystal casts replacing precursor carbonates.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Why are evaporite formations (such as bedded gypsum and halite) of paramount importance in petroleum exploration?</p>
        <p><strong>Solution:</strong>
          Evaporites serve as the <strong>world's most effective petroleum seal rocks (cap rocks)</strong>. Because evaporite minerals undergo ductile plastic flow under lithostatic burial pressure, they exhibit zero effective permeability ($k \approx 0$), have virtually infinite capillary entry pressures, and spontaneously self-heal micro-fractures, preventing oil and natural gas from escaping from underlying porous reservoir rocks (e.g., the Arab Formation cap rocks in the Middle East).
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=97,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q097_Chemical_Sedimentary_Rock_Gypsum_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q097: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q097()
