#!/usr/bin/env python3
"""
Q098 Generator: Diagenesis & Physical-Chemical Sediment Transformation
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q098():
    title = r"Q098: Sedimentary Petrology: Diagenesis & Physical-Chemical Sediment Transformation | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Diagenesis"
    h1_title = "Q098: Diagenesis: Post-Depositional Physical, Chemical & Biological Transformations of Sediments"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 98<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 5: Sandstones / Diagenesis, pp. 175–190; Fig. 5.25); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 68–72, 170); Maurice E. Tucker, <em>Sedimentary Petrology: An Introduction to the Origin of Sedimentary Rocks</em>; F.J. Pettijohn, P.E. Potter, and R. Siever, <em>Sand and Sandstone</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PETROLOGIC FRAMEWORK OF DIAGENESIS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Temperature-Pressure Boundaries & Framework of Diagenesis</div>
    <div class="card-body">
      <p>
        In sedimentary geology and petroleum geoscience (Boggs, 2014, pp. 175–190; Tucker, 2001; Pettijohn et al., 1987), <strong>diagenesis</strong> is formally defined as the <strong>sum total of all physical, chemical, and biological changes and transformations</strong> that a sediment or soil undergoes after its initial deposition, during and after its burial, up to the lowest-grade boundary of metamorphism.
      </p>
      <p>
        The term was introduced into geological science in 1888 by the Austrian geologist Carl Wilhelm von Gümbel. The pressure-temperature window of diagenesis encompasses surface conditions up to temperatures of approximately <strong>$200^\circ\text{C}$ to $250^\circ\text{C}$</strong> and lithostatic burial pressures of approximately <strong>$1\text{ to } 2\text{ kbar}$</strong> (depths of $\sim 5\text{ to } 7\text{ km}$), beyond which processes enter the realm of very low-grade metamorphism (anchizone / sub-greenschist facies).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q98/boggs_p180_diagenesis_stages.png" alt="Stages and Regimes of Diagenesis from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 98.1 — Chronological and Depth Stages of Sedimentary Diagenesis:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 180). Shows the tripartite diagenetic framework: Eodiagenesis (surface/shallow burial), Mesodiagenesis (deep burial compaction and thermal maturation), and Telodiagenesis (uplift and meteoric weathering).
        </div>
      </div>

      <h4>The Tripartite Stages of Diagenesis</h4>
      <p>
        According to the widely accepted classification of Choquette and Pray (1970) and Schmidt and McDonald (1979), diagenesis is subdivided into three distinct chronological and depth regimes:
      </p>
      <ol>
        <li><strong>Eodiagenesis (Early Diagenesis):</strong> Operates at or immediately beneath the depositional surface (depths from $0\text{ to a few hundred meters}$). Governed by pore fluids chemically linked to the surface environment (marine, lacustrine, meteoric), active bioturbation by benthic organisms, microbial decomposition of organic matter (aerobic respiration, sulfate reduction, methanogenesis), and early cementation (e.g., micritic calcite crusts, siderite concretions).</li>
        <li><strong>Mesodiagenesis (Burial Diagenesis):</strong> Occurs during progressive deep basin burial (depths of $1\text{ to } 5+\text{ km}$, temperatures $50\text{--}200^\circ\text{C}$). Driven by increasing overburden stress and geothermal heat:
          <ul>
            <li><strong>Mechanical Compaction:</strong> Reorientation and ductile degranulation of clasts, repacking grains from loose cubic to tight rhombohedral packing, causing drastic porosity reduction.</li>
            <li><strong>Chemical Compaction (Pressure Solution):</strong> Intergranular dissolution at grain contact points under high differential stress, developing concavo-convex contacts, sutured contacts, and macroscopic stylolites.</li>
            <li><strong>Authigenesis & Cementation:</strong> Precipitation of syntaxial quartz overgrowths, poikilotopic carbonate cements, and authigenic clay minerals (kaolinite, illite).</li>
            <li><strong>Smectite-to-Illite Transition:</strong> Thermally driven clay dehydration releasing bound interlayer water into pore networks: $\text{Smectite} + \text{K}^+ \xrightarrow{60\text{--}120^\circ\text{C}} \text{Illite} + \text{Quartz} + \text{Water}$.</li>
            <li><strong>Dissolution & Secondary Porosity:</strong> Leaching of unstable feldspars and carbonates by acidic pore waters generated from kerogen decarboxylation.</li>
          </ul>
        </li>
        <li><strong>Telodiagenesis (Uplift Diagenesis / Retrograde Diagenesis):</strong> Occurs when deeply buried sedimentary rocks are tectonically uplifted and brought back into contact with oxidizing, cool meteoric groundwaters, driving dissolution of carbonate cements, oxidation of pyrite to iron oxides/hydroxides, and kaolinitization of remaining feldspars.</li>
      </ol>
    </div>
  </div>

  <!-- CARD 2: DIAGENESIS VS. LITHIFICATION -->
  <div class="card">
    <div class="card-header bg-emerald">2. Critical Distinction: Diagenesis vs. Lithification & Petrogenesis</div>
    <div class="card-body">
      <h4>Why Lithification is Only a Subset of Diagenesis</h4>
      <p>
        A frequent point of confusion among geology students is equating <em>diagenesis</em> with <em>lithification</em>. They are fundamentally distinct in scope:
      </p>
      <ul>
        <li><strong>Lithification (Consolidation):</strong> The specific process of turning loose, unconsolidated sediment into solid rock through mechanical compaction and intergranular mineral cementation.</li>
        <li><strong>Diagenesis (The Overarching Domain):</strong> Encompasses lithification, but also includes processes that operate in the <em>opposite</em> direction—such as <strong>leaching, dissolution, and secondary porosity creation</strong>, where solid rock is partially dissolved by acidic fluids, increasing void space and weakening rock competence. Diagenesis also includes recrystallization, mineral polymorphism, and isotopic re-equilibration.</li>
      </ul>

      <h4>Refutation of Distractor Terms</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Geological Term</th>
            <th>Rigorous Scientific Definition</th>
            <th>Scope & Typical Usage</th>
            <th>Governing Geological Regime</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Diagenesis</strong></td>
            <td>All post-depositional physical, chemical, and biological transformations of sediments and soils prior to metamorphism</td>
            <td>Comprehensive sedimentary petrology, soil genesis, and petroleum reservoir evolution</td>
            <td>Sedimentary domain ($T < 200\text{--}250^\circ\text{C}$, $P < 2\text{ kbar}$)</td>
          </tr>
          <tr>
            <td><strong>Petrogenesis</strong></td>
            <td>The origin, evolution, and formation history of rocks in general</td>
            <td>Predominantly utilized in igneous petrology (magmatic differentiation, partial melting) and metamorphic petrology</td>
            <td>All geological domains (igneous, metamorphic, sedimentary)</td>
          </tr>
          <tr>
            <td><strong>Lithification</strong></td>
            <td>The physical consolidation of loose sediment into coherent rock via compaction and cementation</td>
            <td>Sub-process of diagenesis; excludes dissolution and secondary porosity generation</td>
            <td>Sedimentary diagenetic sub-process</td>
          </tr>
          <tr>
            <td><strong>Crustification</strong></td>
            <td>Concentric or crust-like banding of mineral crystals lining hydrothermal veins or cavities</td>
            <td>Ore geology and hydrothermal mineral deposit textures</td>
            <td>Hydrothermal / Epithermal vein filling</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 98:</strong> The physical or chemical transformation of sediments or soil by geological processes is termed as :
      </div>
      <div class="options-grid">
        <div class="option-item correct-option"><strong>(A)</strong> Diagenesis</div>
        <div class="option-item"><strong>(B)</strong> Petrogenesis</div>
        <div class="option-item"><strong>(C)</strong> Lithification</div>
        <div class="option-item"><strong>(D)</strong> Crustificaton</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(A) Diagenesis</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-correct">
        <div class="option-badge opt-a">Option (A) Confirmed — Diagenesis</div>
        <p>
          <strong>Correct:</strong> By universal scientific definition in geology (Boggs, 2014, p. 175; Bangar, p. 68; Pettijohn et al., 1987), <strong>diagenesis</strong> is the exact term designating the entire spectrum of physical, chemical, and biological transformations that alter sediments or soils after deposition, throughout burial and compaction, up to the threshold of regional metamorphism. The question's formulation ("physical or chemical transformation of sediments or soil by geological processes") matches this textbook definition word for word.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Petrogenesis</div>
        <p>
          <strong>Incorrect:</strong> <strong>Petrogenesis</strong> (from Greek <em>petra</em> = rock + <em>genesis</em> = origin) is the broad branch of petrology that deals with the origin, historical evolution, and chemical genesis of rocks in general. It is most commonly applied to igneous rocks (e.g., magma generation, partial melting, fractional crystallization) and metamorphic rocks (anatexis, metamorphic reactions). It does not specifically refer to the post-depositional transformation of sediments or soils.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Lithification</div>
        <p>
          <strong>Incorrect:</strong> <strong>Lithification</strong> refers strictly and narrowly to the process of converting loose, soft sediment into solid, cohesive rock (primarily via mechanical compaction and cement precipitation). It is merely <strong>one individual sub-stage</strong> within the much broader domain of diagenesis. Diagenesis includes many major chemical transformations that do not consolidate rock—such as the creation of secondary dissolution porosity, dolomitization, neoformation of clay minerals, and telodiagenetic weathering.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Crustification</div>
        <p>
          <strong>Incorrect:</strong> In economic geology and mineral deposit petrography, <strong>crustification</strong> refers to a distinct texture in epigenetic hydrothermal mineral veins, where successive crusts or crystalline layers of different minerals (e.g., quartz, sphalerite, galena, calcite) are deposited on the walls of an open fracture or cavity. It has no relevance to the post-depositional alteration of sedimentary beds or soils.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Breakdown of Major Diagenetic Processes in Sedimentary Basins</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Diagenetic Process</th>
            <th>Type of Transformation</th>
            <th>Driving Mechanism / Physical Conditions</th>
            <th>Impact on Porosity & Permeability</th>
            <th>Typical Petrographic Features</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mechanical Compaction</strong></td>
            <td>Physical transformation</td>
            <td>Increasing vertical effective overburden stress ($\sigma'_v$)</td>
            <td>Severe porosity destruction (porosity drops from $40\text{--}50\%$ to $15\text{--}25\%$)</td>
            <td>Grain reorientation, bending of ductile mica flakes, fracture of brittle grains</td>
          </tr>
          <tr>
            <td><strong>Pressure Solution (Stylolitization)</strong></td>
            <td>Chemical transformation</td>
            <td>High differential stress at grain contact points</td>
            <td>Porosity reduction; source of dissolved silica/calcite for cements</td>
            <td>Sutured grain contacts, serrated zig-zag stylolitic seams with clay residue</td>
          </tr>
          <tr>
            <td><strong>Authigenic Cementation</strong></td>
            <td>Chemical precipitation</td>
            <td>Supersaturation of pore fluids with respect to mineral phases</td>
            <td>Destruction of intergranular void space and pore throats</td>
            <td>Syntaxial quartz overgrowths, poikilotopic calcite crystals, pore-filling kaolinite</td>
          </tr>
          <tr>
            <td><strong>Dissolution (Leaching)</strong></td>
            <td>Chemical transformation</td>
            <td>Undersaturated acidic pore fluids (carbonic/organic acids from kerogen maturation)</td>
            <td><strong>Enhancement</strong> of porosity (secondary porosity creation: $+5\text{ to } 15\%$)</td>
            <td>Skeletal feldspar remnants, oversized pores, biomoldic/vuggy pores</td>
          </tr>
          <tr>
            <td><strong>Dolomitization</strong></td>
            <td>Chemical replacement</td>
            <td>Circulation of warm, Mg-rich brines: $2\text{CaCO}_3 + \text{Mg}^{2+} \rightarrow \text{CaMg(CO}_3)_2 + \text{Ca}^{2+}$</td>
            <td>Theoretical $13\%$ increase in intercrystalline pore space</td>
            <td>Idiotopic to xenotopic mosaics of rhombohedral dolomite crystals</td>
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
        <p>A quartz sandstone at $3000\text{ m}$ burial depth in a sedimentary basin exhibits intergranular porosity of $18\%$. Petrographic examination shows that $8\%$ of this porosity consists of oversized pores containing corroded, skeletal remnants of K-feldspar. Classify this porosity and explain the diagenetic reaction responsible.</p>
        <p><strong>Solution:</strong>
          The $8\%$ porosity represents <strong>secondary dissolution porosity</strong> generated during <strong>mesodiagenesis</strong>. The reaction is driven by acidic pore fluids generated during the thermal maturation of organic matter (kerogen), which releases carbon dioxide and organic carboxylic acids at temperatures of $80\text{--}120^\circ\text{C}$. The acidic fluids aggressively leach unstable detrital K-feldspar:
          $$2\text{KAlSi}_3\text{O}_8 + 2\text{H}^+ + 9\text{H}_2\text{O} \rightarrow \text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4\text{ (kaolinite)} + 4\text{H}_4\text{SiO}_4 + 2\text{K}^+$$
          dissolving the feldspar interior and leaving behind empty oversized dissolution moldic pores.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain how pressure solution (chemical compaction) in sandstones acts as an internal source of silica for syntaxial quartz overgrowth cements.</p>
        <p><strong>Solution:</strong>
          Under high vertical lithostatic stress, the stress concentrated at grain-to-grain contact points exceeds the hydrostatic pore-fluid pressure. According to the <strong>Riecke Principle</strong>, mineral solubility increases with directed compressive stress. Consequently, quartz selectively dissolves at grain contact points. The dissolved aqueous silica ($\text{H}_4\text{SiO}_4$) diffuses outward into adjacent low-stress, open pore spaces where fluid is supersaturated relative to hydrostatic stress, precipitating onto detrital quartz grains as syntaxial quartz overgrowths.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is a "stylolite" in sedimentary petrology, and in which rocks are stylolites most prominently developed?</p>
        <p><strong>Solution:</strong>
          A <strong>stylolite</strong> is an irregular, serrated, suture-like planar or undulating seam formed by localized, intense chemical compaction (pressure solution). Along the stylolite, substantial thicknesses of the host rock have been completely dissolved away, leaving behind a thin insoluble residue of clay minerals, iron oxides, organic carbon, and heavy minerals. Stylolites are most prominently developed in <strong>carbonates (limestones and dolomites)</strong> and well-sorted quartzose sandstones.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Explain the smectite-to-illite transformation during burial diagenesis and state its significance as a geothermometer in petroleum exploration.</p>
        <p><strong>Solution:</strong>
          With increasing burial depth and temperature, expandable smectite reacts with available potassium (from dissolving K-feldspar) to form non-expandable illite through a series of mixed-layer illite/smectite (I/S) intermediates:
          $$\text{Smectite} + \text{K}^+ + \text{Al}^{3+} \xrightarrow{60\text{--}140^\circ\text{C}} \text{Illite} + \text{Quartz} + \text{H}_2\text{O}$$
          The percentage of illite layers in mixed-layer I/S clays increases progressively with temperature (e.g., $80\%$ illite layers corresponds to $\sim 100\text{--}120^\circ\text{C}$). This transformation serves as an invaluable <strong>inorganic geothermometer</strong> to map peak paleotemperatures and assess whether organic source rocks have entered the "oil generation window" ($60\text{--}120^\circ\text{C}$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Why does the Athy (1930) porosity-depth relationship show an exponential decline in mudrocks with depth: $\phi(z) = \phi_0 e^{-cz}$?</p>
        <p><strong>Solution:</strong>
          L.F. Athy established that mechanical compaction of fine-grained mudrocks is governed by the progressive expulsion of interstitial pore water under increasing effective overburden stress ($\sigma'_v = \sigma_v - P_p$). At shallow depths, high-porosity card-house clay fabrics collapse easily under small stress increments. As depth increases, grains become closely packed and interlocked, drastically increasing skeletal bulk stiffness; hence, progressively larger overburden increments are required to achieve further volumetric strain, producing an exponential decay curve.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Contrast "eodiagenesis", "mesodiagenesis", and "telodiagenesis" in terms of their fluid chemistry and temperature conditions.</p>
        <p><strong>Solution:</strong>
          - <strong>Eodiagenesis:</strong> Low temperature ($< 50^\circ\text{C}$); fluids are depositional surface waters (marine or meteoric); active microbial and biological control.
          - <strong>Mesodiagenesis:</strong> Elevated temperatures ($50\text{--}200^\circ\text{C}$); fluids are evolved, highly saline basinal formation brines; thermochemical reactions, hydrocarbon maturation, and burial pressure dominate.
          - <strong>Telodiagenesis:</strong> Low temperature ($< 50^\circ\text{C}$); fluids are fresh, cold, oxidizing, carbonic-acid-charged meteoric waters introduced via tectonic uplift and erosional unconformities.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is "pseudomatrix" in a compacted sandstone and how does it originate diagenetically?</p>
        <p><strong>Solution:</strong>
          <strong>Pseudomatrix</strong> is an artificial, diagenetically generated interstitial matrix formed when ductile, mechanically weak framework grains (such as shale clasts, mudstone lithics, or deeply weathered volcanic fragments) are squashed, deformed, and squeezed into adjacent intergranular pore spaces between rigid quartz grains during mechanical compaction. Under the microscope, it mimics primary detrital clay matrix, but petrographic inspection reveals ghost outlines of compacted lithic grains.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>State the upper physical boundary that demarcates diagenesis from metamorphism in sedimentary basins.</p>
        <p><strong>Solution:</strong>
          The boundary between diagenesis and metamorphism is transitional but formally defined by:
          1. <strong>Temperature:</strong> Approximately <strong>$200^\circ\text{C}$ to $250^\circ\text{C}$</strong>.
          2. <strong>Vitrinite Reflectance ($R_o$):</strong> $R_o \approx 2.5\text{ to } 3.0\%$.
          3. <strong>Clay Mineralogy:</strong> The disappearance of smectite and mixed-layer clays, marked by the onset of well-crystallized illite (Kübler Index illite crystallinity $\approx 0.42^\circ\Delta 2\theta$, defining the <em>anchizone</em>) and the appearance of metamorphic pyrophyllite, chloritoid, or paragonite.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=98,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q098_Diagenesis_Sediment_Transformation_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q098: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q098()
