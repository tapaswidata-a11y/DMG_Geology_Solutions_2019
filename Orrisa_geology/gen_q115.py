#!/usr/bin/env python3
"""
Q115 Generator: Blueschist Facies & Subduction at Continental Margins
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q115():
    title = r"Q115: Metamorphic Petrology: Blueschist Facies & Subduction Zones | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Geodynamics"
    h1_title = "Q115: Blueschist Facies Metamorphism: High-Pressure / Low-Temperature Subduction along Continental Margins"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 115<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 25: Metamorphic Facies / Blueschist Facies, pp. 485–492; Fig. 25.3); Akiho Miyashiro (1961, 1994), <em>Evolution of Metamorphic Belts</em> & <em>Metamorphism and Metamorphic Belts</em>; Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer); W.G. Ernst (1971, 1988), <em>Do Blueschists Really Signify Former Subduction Zones?</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND GEODYNAMIC LOCALIZATION OF BLUESCHISTS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Geodynamic Framework & The Subduction Locale of Blueschists</div>
    <div class="card-body">
      <p>
        In global geodynamics and metamorphic petrology (Winter, 2014, pp. 485–492; Ernst, 1988; Miyashiro, 1994), the <strong>blueschist (glaucophane-schist) facies</strong> represents the quintessential signature of <strong>High-Pressure / Low-Temperature ($HP/LT$) metamorphism</strong>.
      </p>
      <p>
        The characteristic, canonical locale for blueschist metamorphism is along an <strong>active convergent continental margin (or island-arc trench)</strong> where a cold, dense, hydrous oceanic lithospheric plate is actively <strong>underthrust (subducted)</strong> beneath the overriding continental crust:
      </p>

      <div class="figure-box">
        <img src="../../figures_Q115/winter_p489_blueschist_subduction_continental_margin.png" alt="Blueschist Metamorphism at Convergent Continental Margins from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 115.1 — Geodynamic Locale of Blueschist Metamorphism in a Subduction Zone:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 489). Illustrates rapid underthrusting of oceanic crust along a continental margin, depressing isotherms downward and generating an anomalously low geothermal gradient ($< 10\text{--}15^\circ\text{C/km}$) that stabilizes glaucophane, lawsonite, and jadeite.
        </div>
      </div>

      <h4>Thermodynamic Mechanism: Why Temperatures Remain Unusually Low</h4>
      <p>
        Normal continental geotherms exhibit gradients of $25\text{ to } 35^\circ\text{C/km}$, which would heat rocks at $30\text{ km}$ depth to $> 750^\circ\text{C}$ (granulite facies). Blueschists require temperatures of only <strong>$200^\circ\text{C}$ to $400^\circ\text{C}$</strong> at depths of <strong>$20\text{ to } 45\text{ km}$ ($P \approx 6\text{ to } 14\text{ kbar}$)</strong>. This anomalous $HP/LT$ regime is generated exclusively by subduction kinematics:
      </p>
      <ul>
        <li><strong>Rapid Advective Down-Carrying:</strong> The cold oceanic slab is subducted at tectonic velocities ($3\text{ to } 10\text{ cm/year}$) vastly faster than the rate at which heat can conduct inward from the surrounding hot mantle wedge ($thermal\text{ diffusivity } \kappa \approx 10^{-6}\text{ m}^2\text{/s}$).</li>
        <li><strong>Depressed Isotherms:</strong> This thermal lag severely bends regional isotherms downward into the subduction trench, maintaining frigid conditions ($200\text{--}350^\circ\text{C}$) while lithostatic pressure climbs steeply to over $10\text{ kbar}$, directly accessing the blueschist stability field.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: DIAGNOSTIC MINERALOGY & PAIRED BELTS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Diagnostic Mineralogy, Decompression Preservation & Paired Belts</div>
    <div class="card-body">
      <h4>Pathognomonic Minerals of the Blueschist Facies</h4>
      <p>
        When basaltic oceanic crust (MORB) undergoes blueschist metamorphism, it develops a striking blue-to-lavender coloration defined by specific high-pressure minerals:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Diagnostic Mineral</th>
            <th>Chemical Formula</th>
            <th>Thermodynamic Significance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Glaucophane</strong></td>
            <td>$\text{Na}_2(\text{Mg}_3\text{Al}_2)\text{Si}_8\text{O}_{22}(\text{OH})_2$</td>
            <td>Sodic amphibole imparting the diagnostic blue color; requires high confining pressure to stabilize $\text{Na}$ in the $M4$ site.</td>
          </tr>
          <tr>
            <td><strong>Lawsonite</strong></td>
            <td>$\text{CaAl}_2\text{Si}_2\text{O}_7(\text{OH})_2\cdot\text{H}_2\text{O}$</td>
            <td>Hydrous calcium aluminosilicate; diagnostic of cold subduction geotherms ($T < 350\text{--}400^\circ\text{C}$).</td>
          </tr>
          <tr>
            <td><strong>Jadeite + Quartz</strong></td>
            <td>$\text{NaAlSi}_2\text{O}_6 + \text{SiO}_2$</td>
            <td>Formed by the high-pressure breakdown of albite: $\text{Albite} \rightleftharpoons \text{Jadeite} + \text{Quartz}$ ($P > 10\text{ kbar}$).</td>
          </tr>
          <tr>
            <td><strong>Aragonite</strong></td>
            <td>$\text{CaCO}_3$ (orthorhombic)</td>
            <td>Dense high-pressure polymorph of calcite ($P > 6\text{--}8\text{ kbar}$ at $250^\circ\text{C}$).</td>
          </tr>
        </tbody>
      </table>

      <h4>Miyashiro's (1961) Paired Metamorphic Belts</h4>
      <p>
        In convergent continental margins (e.g., Japan, California Franciscan/Sierra Nevada), Akiho Miyashiro demonstrated that blueschist belts always occur as part of a <strong>paired metamorphic belt</strong>:
      </p>
      <ul>
        <li><strong>Outer Belt (Trench / Accretionary Prism, Oceanward):</strong> $HP/LT$ Blueschist belt formed in the cold subduction channel along the continental margin.</li>
        <li><strong>Inner Belt (Volcanic Arc / Back-Arc, Continentward):</strong> $LP/HT$ Ryoke-type metamorphic belt formed by magmatic advection beneath continental arc volcanoes.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 115:</strong> The characteristic locale for blueschist type of metamorphism appears to be along a ________ being underthrust by an oceanic plate.
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> mid-oceanic ridge</div>
        <div class="option-item correct-option"><strong>(B)</strong> continental margin</div>
        <div class="option-item"><strong>(C)</strong> transform boundary</div>
        <div class="option-item"><strong>(D)</strong> Both (A) and (C) are correct</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) continental margin</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Mid-Oceanic Ridge</div>
        <p>
          <strong>Incorrect:</strong> <strong>Mid-oceanic ridges</strong> are divergent extensional plate boundaries characterized by upwelling mantle asthenosphere, extreme geothermal heat flow ($> 100\text{--}200^\circ\text{C/km}$), and zero lithostatic burial pressure. Metamorphism at ridges is <strong>low-pressure hydrothermal metamorphism (ocean-floor metamorphism)</strong> producing spilites, greenschists, and serpentinites, never high-pressure blueschists.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — Continental Margin</div>
        <p>
          <strong>Correct:</strong> By universal consensus in plate tectonics and metamorphic petrology (Winter, 2014, p. 489; Ernst, 1988; Miyashiro, 1994), <strong>blueschist metamorphism occurs along convergent active continental margins</strong> (e.g., the Franciscan Complex along the western margin of North America) where an oceanic lithospheric plate is subducted (underthrust) beneath the continental edge. This unique tectonic mechanism drags cold rocks rapidly to high pressures while suppressing temperature, generating the pathognomonic blueschist facies.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Transform Boundary</div>
        <p>
          <strong>Incorrect:</strong> A <strong>transform boundary</strong> (e.g., the San Andreas Fault) is a strike-slip boundary where plates slide past one another horizontally without significant vertical descent or subduction. It generates localized cataclasites and mylonites via dynamic metamorphism, not regional $HP/LT$ blueschists.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Both (A) and (C) are Correct</div>
        <p>
          <strong>Incorrect:</strong> Because neither mid-oceanic ridges nor transform boundaries involve plate underthrusting or $HP/LT$ thermal lag, Option (D) is completely invalid. The sole correct geodynamic locale is <strong>(B) continental margin</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Geodynamic Settings of Metamorphic Facies Series</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Facies Series</th>
            <th>$P/T$ Regime</th>
            <th>Geothermal Gradient</th>
            <th>Diagnostic Plate Tectonic Locale</th>
            <th>Classic Type Locality</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Blueschist - Eclogite Series</strong></td>
            <td><strong>High $P$ / Low $T$ ($HP/LT$)</strong></td>
            <td><strong>$< 10\text{--}15^\circ\text{C/km}$ (Frigid Geotherm)</strong></td>
            <td><strong>Subduction Trench along Active Continental Margin</strong></td>
            <td><strong>Franciscan Complex (California), Sanbagawa Belt (Japan)</strong></td>
          </tr>
          <tr>
            <td><strong>Barrovian Series</strong></td>
            <td>Medium $P$ / Medium $T$ ($MP/MT$)</td>
            <td>$20\text{--}30^\circ\text{C/km}$ (Standard Orogenic)</td>
            <td>Continent-Continent Collision Orogens</td>
            <td>Scottish Highlands (Grampian Orogen), Himalayas</td>
          </tr>
          <tr>
            <td><strong>Buchan / Ryoke Series</strong></td>
            <td>Low $P$ / High $T$ ($LP/HT$)</td>
            <td>$> 40\text{--}70^\circ\text{C/km}$ (High Heat Flow)</td>
            <td>Volcanic Magmatic Arc & Back-Arc Basins</td>
            <td>Ryoke Belt (Japan), Sierra Nevada Batholith aureoles</td>
          </tr>
          <tr>
            <td><strong>Ocean-Floor Hydrothermal</strong></td>
            <td>Low $P$ / Moderate-High $T$</td>
            <td>Extremely high ($> 100^\circ\text{C/km}$)</td>
            <td>Mid-Oceanic Ridge Spreading Centers</td>
            <td>Mid-Atlantic Ridge, Oman Ophiolite upper crust</td>
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
        <p>Write the chemical reaction for the high-pressure breakdown of albite plagioclase into jadeitic pyroxene and quartz, and calculate why this reaction is favored at high pressures based on molar volumes: $V^\circ_{\text{albite}} = 100.1\text{ cm}^3\text{/mol}$, $V^\circ_{\text{jadeite}} = 60.4\text{ cm}^3\text{/mol}$, $V^\circ_{\text{quartz}} = 22.7\text{ cm}^3\text{/mol}$.</p>
        <p><strong>Solution:</strong>
          The reaction is:
          $$\text{NaAlSi}_3\text{O}_8\text{ (Albite)} \rightleftharpoons \text{NaAlSi}_2\text{O}_6\text{ (Jadeite)} + \text{SiO}_2\text{ (Quartz)}$$
          Calculate $\Delta V^\circ$:
          $$\Delta V^\circ = V^\circ_{\text{jadeite}} + V^\circ_{\text{quartz}} - V^\circ_{\text{albite}} = 60.4 + 22.7 - 100.1 = 83.1 - 100.1 = \mathbf{-17.0\text{ cm}^3\text{/mol}}$$
          Because the product assemblage occupies $17\%$ less volume than albite ($\Delta V \ll 0$), high lithostatic pressure drives the equilibrium strongly to the right, making the appearance of <strong>jadeite + quartz</strong> the premier geobarometric indicator of blueschist/eclogite facies metamorphism ($P > 10\text{--}12\text{ kbar}$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Why are blueschists virtually absent from the Archean and early Paleoproterozoic geological record prior to $\sim 1.0\text{ Ga}$?</p>
        <p><strong>Solution:</strong>
          Blueschist metamorphism requires an anomalously <strong>cold geothermal gradient ($< 10\text{--}15^\circ\text{C/km}$)</strong>. During the Archean and Paleoproterozoic, the Earth's mantle was significantly hotter due to higher radiogenic heat production and residual accretionary heat. Even in subduction zones, warm mantle temperatures heated the descending slab rapidly ($LP/HT$ or $MP/MT$), preventing the cold thermal lag required for blueschists. The appearance of blueschists in the Neoproterozoic marks the secular cooling of the Earth and the onset of modern "cold, deep" subduction tectonics.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>How does rapid tectonic exhumation preserve delicate blueschist minerals from retrograde transformation into greenschist facies during their return to the surface?</p>
        <p><strong>Solution:</strong>
          If a subducted slab exhumes slowly along a normal geothermal path, conduction from surrounding hot mantle heats the rock while it decompresses, entering the greenschist field where glaucophane and lawsonite react with fluids to form chlorite, albite, and actinolite (complete retrograde destruction). Preservation of blueschists requires <strong>rapid tectonic exhumation</strong> (driven by buoyant extrusion, channel flow, or tectonic unroofing in accretionary wedges) accompanied by <strong>structural desiccation (fluid loss)</strong>, preventing retrograde hydration and "freezing" the high-pressure glaucophane assemblage metastably.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What is the significance of the "calcite-to-aragonite" phase transition in subduction zone blueschists?</p>
        <p><strong>Solution:</strong>
          Aragonite is the dense orthorhombic high-pressure polymorph of calcium carbonate ($\text{CaCO}_3$, $\rho \approx 2.93\text{ g/cm}^3$ vs. calcite $\rho \approx 2.71\text{ g/cm}^3$). The transition boundary requires a minimum pressure of <strong>$P \approx 6.5\text{ kbar}$ at $200^\circ\text{C}$ ($z \approx 22\text{ km}$)</strong>. The discovery of metamorphic aragonite veins in the Franciscan Complex proved conclusively that these sedimentary rocks were carried to depths exceeding $20\text{--}30\text{ km}$ and exhumed rapidly before aragonite could invert back to calcite.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>In a paired metamorphic belt, what accounts for the dramatic contrast in geothermal gradient between the oceanward blueschist belt and the continentward volcanic arc belt?</p>
        <p><strong>Solution:</strong>
          The contrast is driven by <strong>asymmetric heat advection</strong>:
          - <strong>Oceanward (Trench):</strong> Dominated by the subduction of a massive, cold, hydrated oceanic lithospheric slab, which acts as a gigantic regional heat sink, dragging isotherms down and producing a <strong>frigid geotherm ($< 10^\circ\text{C/km}$, Blueschist belt)</strong>.
          - <strong>Continentward (Arc):</strong> Dominated by the ascent of hot, mantle-derived magmas generated by fluxed melting above the dehydrating slab. Magmatic advection pumps enormous heat into the overriding crust, producing an <strong>extremely hot geotherm ($> 40\text{--}60^\circ\text{C/km}$, Ryoke-type belt)</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What rock type forms when a blueschist metabasite is subjected to further increase in pressure and temperature beyond $P > 15\text{ kbar}$ and $T > 500^\circ\text{C}$?</p>
        <p><strong>Solution:</strong>
          At depths exceeding $\sim 45\text{--}50\text{ km}$ ($P > 15\text{ kbar}$), hydrous glaucophane and lawsonite break down via terminal dehydration, recrystallizing into anhydrous <strong>omphacite clinopyroxene and pyrope-almandine garnet</strong>. The rock transforms into an <strong>Eclogite</strong>, the densest crustal rock on Earth ($\rho \approx 3.4\text{--}3.6\text{ g/cm}^3$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Under a polarizing microscope, how can a geologist definitively identify glaucophane?</p>
        <p><strong>Solution:</strong>
          Glaucophane is an inosilicate amphibole exhibiting diagnostic optical properties:
          1. <strong>Strong Distinctive Pleochroism:</strong> $X = \text{colorless to pale yellow}$, $Y = \text{violet / lavender-blue}$, $Z = \text{vivid Prussian blue / sky blue}$.
          2. <strong>Low Extinction Angle:</strong> Small extinction angle $Z \wedge c = 4^\circ\text{ to } 8^\circ$.
          3. <strong>Amphibole Cleavage:</strong> Intersecting $\{110\}$ cleavage planes at $56^\circ / 124^\circ$.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Why do serpentine mud volcanoes on the Mariana forearc seafloor exhume blueschist-facies mineral clasts?</p>
        <p><strong>Solution:</strong>
          In the Mariana subduction forearc, dehydration fluids rising from the subducting slab hydrate the overlying mantle wedge peridotite into low-density, buoyant <strong>serpentine diapirs ($\rho \approx 2.5\text{ g/cm}^3$)</strong>. As the ductile serpentine rises buoyantly through faults to erupt on the ocean floor as mud volcanoes, it physically plucks and entrains rock fragments (xenoliths) of subducted blueschists from $15\text{--}25\text{ km}$ depth, providing real-time exhumation of active subduction zone metamorphism.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=115,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q115_Blueschist_Subduction_Continental_Margin_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q115: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q115()
