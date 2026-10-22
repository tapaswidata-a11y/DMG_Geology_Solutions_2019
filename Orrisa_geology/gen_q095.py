#!/usr/bin/env python3
"""
Q095 Generator: Karst Topography & Carbonate Bedrock Geomorphology
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q095():
    title = r"Q095: Geomorphology & Hydrogeology: Karst Topography in Carbonate Bedrock | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geomorphology & Carbonate Hydrogeology"
    h1_title = "Q095: Karst Topography: Evolution, Dissolution Kinetics & Landforms in Carbonate Bedrock"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 95<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Ch. 4: Geological Work of Underground Water, pp. 60–66; Fig. 4.10; p. 30); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 68–74); D.C. Ford and P.W. Williams, <em>Karst Hydrogeology and Geomorphology</em> (John Wiley & Sons); Arthur Holmes, <em>Principles of Physical Geology</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND DISSOLUTION KINETICS OF KARST -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Etymology & Chemical Dissolution Thermodynamics of Karst</div>
    <div class="card-body">
      <p>
        The term <strong>karst</strong> originates from the Slovene word <em>kras</em> (Germanized as <em>Karst</em>), referring to the barren, rocky limestone plateau region of Slovenia and northeastern Italy near Trieste.
      </p>
      <p>
        In geomorphology and hydrogeology (Ford & Williams, 2007; Bangar, pp. 60–66), <strong>karst topography</strong> is defined as a distinctive, highly irregular landscape shaped predominantly by the <strong>chemical dissolution (corrosion)</strong> of soluble bedrocks—most classically and extensively developed in <strong>carbonate bedrock (limestone, $\text{CaCO}_3$, and dolomite, $\text{CaMg(CO}_3)_2$)</strong>, and less commonly in evaporites (gypsum, anhydrite, halite).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q95/bangar_p64_karst_topography_limestone.png" alt="Karst Topography Features and Caves in Limestone from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 95.1 — Geomorphology of Karst Topography in Carbonate Bedrock:</strong> Authentic textbook diagram from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 64). Shows characteristic karst features: sinkholes (dolines), swallow holes (ponors), subterranean caverns, underground rivers, blind valleys, and speleothems (stalactites and stalagmites) formed by the dissolution of limestone.
        </div>
      </div>

      <h4>Thermodynamics of Carbonate Dissolution</h4>
      <p>
        Pure water dissolves calcium carbonate only negligibly (solubility of calcite in pure water at $25^\circ\text{C}$ is approximately $0.014\text{ g/L}$). However, natural meteoric precipitation absorbs carbon dioxide ($\text{CO}_2$) from the atmosphere and, much more intensely, from <strong>biologically active soil air</strong> (where soil respiration generates $\text{CO}_2$ partial pressures $10\text{ to } 100\text{ times}$ greater than atmospheric levels: $P_{\text{CO}_2} \approx 10^{-2}\text{ to } 10^{-1.5}\text{ atm}$).
      </p>
      <ol>
        <li>Dissolution of carbon dioxide in water generates weak, highly corrosive <strong>carbonic acid ($\text{H}_2\text{CO}_3$)</strong>:
          $$\text{H}_2\text{O} + \text{CO}_2(\text{aqueous}) \rightleftharpoons \text{H}_2\text{CO}_3 \rightleftharpoons \text{H}^+ + \text{HCO}_3^-$$
        </li>
        <li>The hydrogen ions ($\text{H}^+$) attack the solid calcite crystal lattice, converting insoluble calcium carbonate into highly soluble <strong>calcium bicarbonate ($\text{Ca(HCO}_3)_2$)</strong>:
          $$\text{CaCO}_3\text{ (solid)} + \text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{Ca}^{2+} + 2\text{HCO}_3^-$$
        </li>
        <li>The forward reaction dissolves the carbonate bedrock, widening microscopic joints and bedding planes into massive conduit networks, caverns, and sinkholes.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q95/bangar_p30_karst_topography_limestone.png" alt="Underground Water Action and Karst Forms from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 95.2 — Evolution of Underground Limestone Caverns:</strong> Authentic diagram from K.M. Bangar (p. 30), detailing vadose vertical shafts, phreatic horizontal galleries, and speleothem precipitation triggered by carbon dioxide degassing.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: LANDFORMS & ENGINEERING GEOLOGY HAZARDS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Morphological Spectrum of Karst Landforms & Civil Engineering Hazards</div>
    <div class="card-body">
      <h4>Surface and Subsurface Karst Landforms</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Karst Feature</th>
            <th>Type</th>
            <th>Morphology & Scale</th>
            <th>Genesis & Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Karren / Lapies</strong></td>
            <td>Surface</td>
            <td>Millimeter- to meter-scale grooves, flutes, and sharp ridges on bare limestone</td>
            <td>Subaerial dissolution by trickling or ponded acidic rainwater</td>
          </tr>
          <tr>
            <td><strong>Sinkhole (Doline)</strong></td>
            <td>Surface</td>
            <td>Funnel- or bowl-shaped depressions ($5\text{--}100\text{ m}$ diameter)</td>
            <td>Two types: <em>Solution sinkholes</em> (gradual surface dissolution) and <em>Collapse sinkholes</em> (sudden catastrophic roof collapse over an underlying cavern)</td>
          </tr>
          <tr>
            <td><strong>Uvala (Compound Sinkhole)</strong></td>
            <td>Surface</td>
            <td>Elongated, composite depressions ($100\text{ m to } 1\text{ km}$)</td>
            <td>Coalescence of several adjacent individual sinkholes as dissolution widens boundaries</td>
          </tr>
          <tr>
            <td><strong>Polje</strong></td>
            <td>Surface</td>
            <td>Massive flat-bottomed structural valley ($1\text{ to } 40\text{ km}$ wide) surrounded by steep cliffs</td>
            <td>Tectonic graben subsidence combined with lateral planation and solution by karst rivers</td>
          </tr>
          <tr>
            <td><strong>Ponor / Swallow Hole</strong></td>
            <td>Interface</td>
            <td>Vertical or plunging opening in a stream bed</td>
            <td>Surface stream plunges underground, becoming a "disappearing stream" in a blind valley</td>
          </tr>
          <tr>
            <td><strong>Caves and Caverns</strong></td>
            <td>Subsurface</td>
            <td>Horizontal galleries, vertical shafts, and vast subterranean chambers</td>
            <td>Enlargement of joints and bedding planes in the phreatic and vadose groundwater zones</td>
          </tr>
          <tr>
            <td><strong>Speleothems (Dripstone)</strong></td>
            <td>Subsurface</td>
            <td>Stalactites (ceiling), Stalagmites (floor), Pillars/Columns, Flowstone</td>
            <td>Degassing of $\text{CO}_2$ from mineralized groundwater entering well-ventilated cave air, precipitating calcite: $\text{Ca}^{2+} + 2\text{HCO}_3^- \rightarrow \text{CaCO}_3\downarrow + \text{H}_2\text{O} + \text{CO}_2\uparrow$</td>
          </tr>
        </tbody>
      </table>

      <h4>Civil Engineering Hazards in Carbonate Karst Terrains</h4>
      <ul>
        <li><strong>Catastrophic Ground Subsidence:</strong> Sudden collapse of overburden soil or cavern roofs into concealed subsurface voids poses extreme hazards to highways, railways, building foundations, and pipelines.</li>
        <li><strong>Dam Reservoir Leakage:</strong> Construction of dams in karst valleys frequently results in severe water loss through hidden conduit systems beneath the abutments or reservoir floor (e.g., the infamous Hales Bar Dam failure in the USA).</li>
        <li><strong>Contaminant Vulnerability:</strong> Karst aquifers exhibit turbulent, high-velocity conduit flow ($100\text{ to } 1000\text{ m/day}$) with virtually zero natural filtration, transmitting untreated surface pollutants directly to regional drinking water wells.</li>
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
        <strong>Question 95:</strong> Karst topography is a special type of landform characterized by sinkholes or caves, developed in :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Calcareous sandstone</div>
        <div class="option-item"><strong>(B)</strong> Shales</div>
        <div class="option-item correct-option"><strong>(C)</strong> Carbonate bedrock</div>
        <div class="option-item"><strong>(D)</strong> Basaltic beds</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(C) Carbonate bedrock</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Calcareous Sandstone</div>
        <p>
          <strong>Incorrect:</strong> While calcareous sandstone contains calcite cement that is vulnerable to dissolution, its primary framework consists of insoluble detrital quartz grains ($> 50\text{--}80\%$). When groundwater dissolves the calcite cement, the rock merely disaggregates into loose, porous quartz sand rather than developing open subterranean caverns, towering speleothems, or self-supporting collapse sinkholes. True karst landforms require a rock mass composed almost entirely of soluble minerals.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Shales</div>
        <p>
          <strong>Incorrect:</strong> Shales are composed of insoluble, highly impermeable hydrous aluminosilicate clay minerals (illite, kaolinite, smectite) and fine quartz silt. Shales act as regional <strong>aquitards or aquicludes</strong> that block groundwater movement rather than permitting conduit dissolution. Instead of karst, weathering of shale produces gentle, undulating clay-rich slopes, badland topography, or shallow planar landslides.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-c">Option (C) Confirmed — Carbonate Bedrock</div>
        <p>
          <strong>Correct:</strong> By fundamental definition in geomorphology, hydrogeology, and engineering geology (Bangar, p. 60; Mahapatra, p. 68; Ford & Williams, 2007), <strong>karst topography</strong> develops specifically and typically in thick, dense, jointed <strong>carbonate bedrock (limestones and dolomites)</strong>. The high solubility of calcium carbonate ($\text{CaCO}_3$) in carbonic-acid-charged groundwater allows the complete dissolution of the bedrock, creating the classic diagnostic karst suite: sinkholes (dolines), caves, underground streams, and blind valleys.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Basaltic Beds</div>
        <p>
          <strong>Incorrect:</strong> Basaltic beds are composed of mafic igneous silicates (calcic plagioclase, augite pyroxene, olivine) that weather by silicate hydrolysis and oxidation, generating red clay soils (laterite, lithomarge) and step-like volcanic plateau trappean topography (e.g., the Deccan Traps). Although flowing lava can form hollow "lava tubes," these are volcanic constructional/thermal drainage conduits, completely distinct in genesis, morphology, and chemistry from karst dissolution caves and sinkholes.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Analysis: Karst Landforms in Carbonate Bedrocks vs. Non-Karst Pseudokarst Terrains</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Terrain / Rock Type</th>
            <th>Dominant Lithology</th>
            <th>Dominant Geological Process</th>
            <th>Morphological Manifestation</th>
            <th>Classification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>True Karst</strong></td>
            <td>Carbonate bedrock (Limestone $\text{CaCO}_3$, Dolomite $\text{CaMg(CO}_3)_2$)</td>
            <td>Chemical dissolution by carbonic acid ($\text{CaCO}_3 + \text{H}_2\text{CO}_3 \rightarrow \text{Ca}^{2+} + 2\text{HCO}_3^-$)</td>
            <td>Sinkholes, uvalas, poljes, blind valleys, caves, stalactites/stalagmites</td>
            <td><strong>Holokarst / Merokarst</strong></td>
          </tr>
          <tr>
            <td><strong>Evaporite Karst</strong></td>
            <td>Gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$), Anhydrite ($\text{CaSO}_4$), Halite ($\text{NaCl}$)</td>
            <td>Direct congruent aqueous dissolution in water (extremely rapid kinetics)</td>
            <td>Rapid collapse sinkholes, breccia pipes, salt caves</td>
            <td><strong>Hyper-soluble Evaporite Karst</strong></td>
          </tr>
          <tr>
            <td><strong>Pseudokarst (Volcanic)</strong></td>
            <td>Basalt lava flows</td>
            <td>Thermal drainage of liquid molten interior beneath crusted exterior</td>
            <td>Lava tubes, hornitos, collapse trenches</td>
            <td><strong>Volcanic Pseudokarst</strong></td>
          </tr>
          <tr>
            <td><strong>Pseudokarst (Piping / Sapping)</strong></td>
            <td>Poorly consolidated sandstones, loess, or cohesive soils</td>
            <td>Subsurface mechanical erosion and particle entrainment by groundwater seepage</td>
            <td>Piping sinkholes, badland gullies, collapse chasms</td>
            <td><strong>Clastic Piping Pseudokarst</strong></td>
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
        <p>State the fundamental chemical reaction that governs the dissolution of limestone bedrock during the initiation of karst caverns, and identify the source of the acid involved.</p>
        <p><strong>Solution:</strong>
          The overall governing chemical reaction is:
          $$\text{CaCO}_3\text{ (calcite)} + \text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{Ca}^{2+} + 2\text{HCO}_3^-$$
          The primary source of the carbonic acid ($\text{H}_2\text{CO}_3$) is not atmospheric rain (which contains only $\sim 0.04\%\text{ CO}_2$), but rather the <strong>soil atmosphere</strong> beneath dense vegetation. Bacterial decomposition of organic humus and root respiration in soils generate partial pressures of $\text{CO}_2$ reaching $1\text{--}5\%$ ($P_{\text{CO}_2} = 10^{-2}\text{ to } 10^{-1.3}\text{ atm}$), producing acidic vadose percolation that vigorously dissolves the underlying carbonate bedrock.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Distinguish between a "solution sinkhole" and a "collapse sinkhole" in terms of geological evolution and civil engineering risk.</p>
        <p><strong>Solution:</strong>
          - <strong>Solution Sinkhole (Doline):</strong> Forms by gradual, slow, progressive dissolution of limestone bedrock downward from the surface along intersecting joints. The ground settles slowly over thousands of years with minimal immediate threat to human life.
          - <strong>Collapse Sinkhole:</strong> Forms when an underground cave chamber enlarges until its carbonate or soil roof can no longer support the overlying lithostatic load. The cavern roof experiences catastrophic shear failure and collapses instantaneously into the subterranean void, creating a steep-walled abyss. This presents severe, lethal engineering hazards for highways, railways, and buildings.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Why do caves rarely form in pure, unjointed, massive marble under metamorphic conditions, even though marble is chemically identical to limestone ($\text{CaCO}_3$)?</p>
        <p><strong>Solution:</strong>
          Karst development requires not only chemical solubility, but also <strong>secondary permeability (interconnected fractures and joints)</strong> to allow meteoric groundwater circulation. Deeply buried, unjointed crystalline marbles lack primary porosity and continuous fracture networks. Without open fractures to admit and circulate carbonic-acid-charged groundwater, dissolution cannot focus along discrete conduits, and cavern systems cannot initiate.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Explain why stalactites and stalagmites (speleothems) precipitate inside cave chambers rather than dissolving further.</p>
        <p><strong>Solution:</strong>
          Groundwater percolating through the soil and tight rock joints is in equilibrium with high $P_{\text{CO}_2}$ ($> 10^{-2}\text{ atm}$) and carries high concentrations of dissolved $\text{Ca}^{2+}$ and $\text{HCO}_3^-$. When this water drips into an open, ventilated cave chamber, the air in the cave has a much lower $P_{\text{CO}_2}$ ($\approx 4 \times 10^{-4}\text{ atm}$). Consequently, $\text{CO}_2$ gas spontaneously degasses from the water droplet into the cave atmosphere. By Le Chatelier's principle, the loss of $\text{CO}_2$ drives the reversible equilibrium to the left:
          $$\text{Ca}^{2+} + 2\text{HCO}_3^- \rightarrow \text{CaCO}_3\downarrow + \text{H}_2\text{O} + \text{CO}_2\uparrow$$
          forcing the immediate precipitation of solid crystalline calcite dripstone (stalactites hanging from the roof, stalagmites rising from the floor).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>A civil engineering team is tasked with constructing a major hydroelectric concrete gravity dam in a river valley underlain by folded limestone. What geological investigations are mandatory to avoid catastrophic reservoir failure?</p>
        <p><strong>Solution:</strong>
          Mandatory investigations include:
          1. <strong>Extensive Core Drilling & Water Pressure Testing (Lugeon Tests):</strong> To map subterranean solution cavities, caverns, and open joint networks.
          2. <strong>Electrical Resistivity Tomography (ERT) & Ground Penetrating Radar (GPR):</strong> To locate hidden air-filled or mud-filled karst voids beneath the dam axis.
          3. <strong>Hydrogeological Dye-Tracing Tests:</strong> Injecting fluorescent tracer dyes (uranine/rhodamine) into upstream swallow holes to determine conduit velocity and discharge resurgence points.
          4. <strong>Curtain Grouting Design:</strong> Installing deep, pressurized cement-bentonite grout curtains beneath the dam foundation and abutments to seal all dissolution channels.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is a "blind valley" in karst geomorphology?</p>
        <p><strong>Solution:</strong>
          A <strong>blind valley</strong> is a steep-sided river valley that terminates abruptly downstream against a solid limestone cliff or wall. The surface stream flowing through the valley cannot continue overland; instead, it plunges entirely underground through a <strong>swallow hole or ponor</strong> at the base of the cliff, entering a subterranean cave conduit system.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Contrast "Holokarst" with "Fluviokarst" in the geomorphic classification of karst terrains.</p>
        <p><strong>Solution:</strong>
          - <strong>Holokarst:</strong> "Pure" karst developed in very thick, uninterrupted carbonate successions under humid conditions. Surface drainage is completely absent; all drainage is subterranean, and the landscape is dominated entirely by sinkholes, dolines, poljes, and bare limestone pavements.
          - <strong>Fluviokarst:</strong> A hybrid landscape where both surface river drainage (fluvial valleys and gorges) and subterranean karst features (caves, sinkholes) coexist, typically occurring where carbonate beds are relatively thin, interbedded with shales/sandstones, or in dissected uplands.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Why do environmental protection agencies designate karst aquifers as the most vulnerable groundwater systems to pollution?</p>
        <p><strong>Solution:</strong>
          In granular sand or sandstone aquifers, pollutants are naturally filtered by physical straining, mechanical adsorption, and biological degradation as water moves slowly ($0.1\text{--}1\text{ m/day}$). In karst aquifers, surface runoff enters directly into open sinkholes and conduits without passing through soil. Flow through conduit pipes is <strong>turbulent and exceptionally rapid ($100\text{ to } 10,000\text{ m/day}$)</strong>, providing zero filtration or residence time for attenuation. Contaminants (sewage, chemicals, hydrocarbons) travel miles in hours, emerging directly at municipal drinking water springs.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=95,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q095_Karst_Topography_Carbonate_Bedrock_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q095: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q095()
