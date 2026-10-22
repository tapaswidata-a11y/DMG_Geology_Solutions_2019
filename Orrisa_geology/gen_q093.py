#!/usr/bin/env python3
"""
Q093 Generator: Clastic Sedimentary Rocks & Mechanical Breakdown
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q093():
    title = r"Q093: Sedimentary Petrology: Clastic Sedimentary Rocks & Mechanical Breakdown | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Classification"
    h1_title = "Q093: Clastic Sedimentary Rocks: Genesis by Mechanical Breakdown of Primary Rocks"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 93<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 5: Siliciclastic Sedimentary Rocks, pp. 125–135; Fig. 5.1); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 67–70, 169); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 142–148); Maurice E. Tucker, <em>Sedimentary Petrology: An Introduction to the Origin of Sedimentary Rocks</em>."""

    part1 = r"""
  <!-- CARD 1: GENETIC CLASSIFICATION OF SEDIMENTARY ROCKS -->
  <div class="card">
    <div class="card-header bg-blue">1. Fundamental Classification of Sedimentary Rocks: Clastic vs. Non-Clastic</div>
    <div class="card-body">
      <p>
        In classical geology and sedimentary petrology (Bangar, p. 67; Mahapatra, p. 142; Boggs, 2014, p. 126), sedimentary rocks are categorized fundamentally into two grand genetic subdivisions based on their mode of origin and source material:
      </p>
      <ol>
        <li><strong>Clastic (Detrital / Mechanically Formed) Rocks:</strong> Sedimentary rocks formed by the accumulation, compaction, and cementation of particulate solid mineral and rock fragments (<em>clasts</em> or <em>detritus</em>) produced by the <strong>mechanical breakdown and physical disintegration</strong> of pre-existing primary (igneous, metamorphic, or older sedimentary) rocks. The word <em>clastic</em> derives from the Greek <em>klastos</em> ($\kappa\lambda\alpha\sigma\tau\acute{o}\varsigma$), meaning "broken in pieces".</li>
        <li><strong>Non-Clastic (Chemical and Biochemical/Organic) Rocks:</strong> Sedimentary rocks formed either by direct chemical precipitation of dissolved mineral salts from aqueous solution (e.g., evaporites like rock salt and gypsum, travertine) or by organic accumulation of biochemical skeletal debris and plant matter (e.g., fossiliferous limestones, chalk, diatomite, coal).</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q93/boggs_p130_siliciclastic_classification.png" alt="Classification of Clastic Sedimentary Rocks from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 93.1 — Classification Scheme of Clastic Sedimentary Rocks:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 130). Illustrates the Udden-Wentworth grain-size scale and major clastic divisions: Rudaceous (conglomerate/breccia), Arenaceous (sandstone), and Argillaceous (mudrock/shale).
        </div>
      </div>

      <h4>Grain-Size Subdivisions of Clastic Sedimentary Rocks</h4>
      <p>
        Clastic sedimentary rocks are systematically classified on the basis of the physical grain size of their constituent detrital fragments according to the Wentworth size scale:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Descriptive Group</th>
            <th>Classical Greek / Latin Term</th>
            <th>Clast Size Range</th>
            <th>Loose Sediment</th>
            <th>Consolidated Clastic Rock</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Coarse-grained</strong></td>
            <td><strong>Rudaceous / Psephitic</strong></td>
            <td>$> 2.0\text{ mm}$ (up to $> 256\text{ mm}$)</td>
            <td>Gravel, pebbles, cobbles, boulders</td>
            <td><strong>Conglomerate</strong> (rounded clasts)<br><strong>Breccia</strong> (angular clasts)</td>
          </tr>
          <tr>
            <td><strong>Medium-grained</strong></td>
            <td><strong>Arenaceous / Psammitic</strong></td>
            <td>$0.0625\text{ mm to } 2.0\text{ mm}$ ($1/16\text{--}2\text{ mm}$)</td>
            <td>Sand (coarse, medium, fine)</td>
            <td><strong>Sandstone</strong> (quartz arenite, arkose, greywacke)</td>
          </tr>
          <tr>
            <td><strong>Fine-grained</strong></td>
            <td><strong>Argillaceous / Pelitic</strong></td>
            <td>$< 0.0625\text{ mm}$ ($< 1/16\text{ mm}$)</td>
            <td>Silt ($1/16\text{--}1/256\text{ mm}$)<br>Clay ($< 1/256\text{ mm}$)</td>
            <td><strong>Siltstone, Mudstone, Shale, Claystone</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: MECHANICAL BREAKDOWN MECHANISMS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Mechanical Weathering Processes & Detrital Disintegration</div>
    <div class="card-body">
      <h4>Physical Weathering Mechanisms Generating Clasts</h4>
      <p>
        The mechanical breakdown of primary igneous and metamorphic bedrocks into detrital clasts occurs through several distinct physical weathering mechanisms operating without significant initial chemical transformation:
      </p>
      <ul>
        <li><strong>Frost Wedging (Gelifraction):</strong> Liquid water infiltrates joints and microcracks. Upon freezing at $0^\circ\text{C}$, water expands by approximately $9\%$ in volume, exerting immense crystallization pressures up to $200\text{ MPa}$, shattering massive parent rocks into angular rubble and scree.</li>
        <li><strong>Unloading / Pressure Release (Exfoliation):</strong> Deep-seated plutonic rocks (e.g., granite) crystallized under high lithostatic pressure expand elastically when overlying rock is stripped by erosion. Release of confining stress produces sheeting joints parallel to the topographic surface, causing outer shells of rock to spall off.</li>
        <li><strong>Thermal Expansion and Contraction (Insolation):</strong> In diurnal desert environments, rapid surface heating and cooling induce differential thermal stresses between mineral grains with differing coefficients of thermal expansion (e.g., quartz vs. feldspar), initiating micro-fractures.</li>
        <li><strong>Salt Crystallization (Haloclasty):</strong> Saline groundwater in arid regions evaporates in porous rocks; growing halite or gypsum crystals wedge pore walls apart.</li>
        <li><strong>Hydraulic and Abrasion Drag:</strong> Torrential rivers, glacial ice, and breaking waves physically pound, grind, and dislodge fragments from bedrock channels.</li>
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
        <strong>Question 93:</strong> Sedimentary rocks formed due to the sediments formed from mechanical breakdown of primary rocks is called :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> siliclastic rocks</div>
        <div class="option-item correct-option"><strong>(B)</strong> clastic rocks</div>
        <div class="option-item"><strong>(C)</strong> semi-clastic rocks</div>
        <div class="option-item"><strong>(D)</strong> chemical sediments</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) clastic rocks</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Siliclastic Rocks</div>
        <p>
          <strong>Incorrect:</strong> While <em>siliciclastic rocks</em> (spelled siliciclastic) represent the most common subdivision of clastic rocks, the term is restricted specifically to rocks where the constituent clasts are composed exclusively of <strong>silicate minerals</strong> (quartz, feldspar, clay minerals, and silicate lithic fragments). The question asks for the fundamental, overarching class of sedimentary rocks formed from the mechanical breakdown of primary rocks. That universal, primary classification category in classical petrology (Bangar, p. 67; Mahapatra, p. 142) is <strong>clastic rocks</strong>. Furthermore, "clastic rocks" encompasses all fragmental rocks (including non-silicate clastic carbonates, evaporite-clastics, and pyroclastics), making (B) the broader and canonically correct answer.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — Clastic Rocks</div>
        <p>
          <strong>Correct:</strong> In all authoritative geological textbooks (Bangar, <em>Principles of Engineering Geology</em>, p. 67; Mahapatra, <em>A Text-Book of Geology</em>, p. 142; Boggs, <em>Principles of Sedimentology and Stratigraphy</em>, p. 126), sedimentary rocks formed by the accumulation of fragments and mineral particles derived from the <strong>mechanical breakdown (physical weathering and disintegration)</strong> of pre-existing primary rocks are explicitly designated as <strong>clastic rocks</strong> (or detrital rocks). Examples include conglomerates, breccias, sandstones, and shales.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Semi-Clastic Rocks</div>
        <p>
          <strong>Incorrect:</strong> "Semi-clastic" is not a formal or standard taxonomic class in sedimentary petrology. While informal descriptions might occasionally refer to rocks with mixed origins (such as volcaniclastic-tuffaceous sediments or marls), no major geological classification system defines the product of primary rock mechanical breakdown as "semi-clastic."
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Chemical Sediments</div>
        <p>
          <strong>Incorrect:</strong> <strong>Chemical sediments</strong> represent the exact <em>antithesis</em> of mechanically formed clastic rocks. Chemical sedimentary rocks (such as halite, gypsum, anhydrite, chert, and travertine) are formed by <strong>precipitation of dissolved ions directly from aqueous solution</strong> through inorganic chemical processes (evaporation, pH/Eh changes, supersaturation), without involving the physical accumulation of mechanically disintegrated rock fragments.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison of Major Sedimentary Rock Classes</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Class of Sedimentary Rock</th>
            <th>Primary Genetic Mechanism</th>
            <th>Source Material</th>
            <th>Primary Textural Characteristic</th>
            <th>Key Representative Rock Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Clastic (Detrital)</strong></td>
            <td>Mechanical breakdown, physical transport, and deposition</td>
            <td>Pre-existing primary rocks (igneous, metamorphic, sedimentary)</td>
            <td>Particulate (clastic) texture: framework grains, matrix, and authigenic cement</td>
            <td>Conglomerate, Breccia, Quartz Sandstone, Arkose, Greywacke, Shale</td>
          </tr>
          <tr>
            <td><strong>Chemical Sedimentary</strong></td>
            <td>Inorganic chemical precipitation from solution</td>
            <td>Dissolved ions ($\text{Na}^+, \text{Ca}^{2+}, \text{Cl}^-, \text{SO}_4^{2-}, \text{HCO}_3^-$) in surface/subsurface water</td>
            <td>Crystalline, interlocking mosaic texture (microcrystalline to coarse spar)</td>
            <td>Rock salt (halite), Gypsum, Anhydrite, Travertine, Oolitic limestone, Bedded chert</td>
          </tr>
          <tr>
            <td><strong>Biochemical / Organic</strong></td>
            <td>Biological metabolic extraction or organic carbon accumulation</td>
            <td>Skeletal hard parts of organisms (shells, tests) or terrestrial vegetative debris</td>
            <td>Bioclastic, fossiliferous, or amorphous organic maceral mass</td>
            <td>Coquina, Chalk, Diatomite, Radiolarian chert, Peat, Lignite, Bituminous coal</td>
          </tr>
          <tr>
            <td><strong>Residual (Chemo-residual)</strong></td>
            <td>In-situ deep chemical leaching and residual concentration</td>
            <td>Immobile insoluble oxides and hydroxides remaining after base leaching</td>
            <td>Pisolitic, nodular, earthy, cellular, or slag-like porous texture</td>
            <td>Laterite, Bauxite, Residual clays, Gossans</td>
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
        <p>A sedimentary rock contains $65\%$ angular gravel clasts larger than $2\text{ mm}$ cemented by iron oxide. Name this rock, state its broad class, and interpret the distance of sediment transport from the primary source area.</p>
        <p><strong>Solution:</strong> The rock is a <strong>sedimentary breccia</strong>. It belongs to the <strong>rudaceous (psephitic) division of clastic sedimentary rocks</strong>. Because the gravel clasts are sharply angular (exhibiting sharp edges and corners with no rounding), it indicates <strong>minimal to negligible physical transport</strong> from the source area (e.g., deposited at the base of a fault scarp or talus/scree slope directly adjacent to the weathering bedrock).</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain why mechanical breakdown alone cannot produce an orthoquartzite containing $99\%$ monocrystalline quartz from a parent granitic pluton.</p>
        <p><strong>Solution:</strong> A parent granite typically contains $25\text{--}35\%$ quartz, $50\text{--}65\%$ feldspars (orthoclase, plagioclase), and $5\text{--}15\%$ mafic silicates (biotite, hornblende). Pure mechanical breakdown shatters all minerals equally. To achieve $99\%$ quartz purity (high mineralogical maturity), mechanical breakdown must operate in conjunction with <strong>intense chemical weathering</strong> (hydrolysis) in a warm, humid climate, which chemically decomposes unstable feldspars to clay ($2\text{KAlSi}_3\text{O}_8 + 2\text{H}^+ + 9\text{H}_2\text{O} \rightarrow \text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4 + 4\text{H}_4\text{SiO}_4 + 2\text{K}^+$) and dissolves mafics, leaving behind chemically inert quartz.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is the difference between a "conglomerate" and a "breccia" in clastic petrology, and what hydrodynamic parameter does this difference reflect?</p>
        <p><strong>Solution:</strong> Both conglomerate and breccia are rudaceous clastic rocks containing $> 30\%$ gravel-sized clasts ($> 2\text{ mm}$). In a <strong>conglomerate</strong>, the clasts are <strong>rounded to sub-rounded</strong> due to sustained attrition, abrasion, and tumbling during prolonged aquatic transport (e.g., fluvial rivers or wave-swept beaches). In a <strong>breccia</strong>, the clasts are <strong>angular to sub-angular</strong>, reflecting rapid deposition without significant abrasion (e.g., scree slopes, alluvial fans, or landslide debris flows).</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Calculate the Wentworth phi ($\phi$) value corresponding to the boundary between arenaceous (sand) and argillaceous (silt/clay) clastic sediments.</p>
        <p><strong>Solution:</strong>
          The Wentworth phi scale is defined mathematically as:
          $$\phi = -\log_2(d)$$
          where $d$ is the grain diameter in millimeters. The boundary between sand and silt is $1/16\text{ mm} = 0.0625\text{ mm}$.
          $$\phi = -\log_2\left(\frac{1}{16}\right) = -\log_2(2^{-4}) = -(-4) = +4.0\phi$$
          Thus, the sand-silt boundary corresponds exactly to $+4.0\phi$. Particles coarser than $+4\phi$ are sand (arenaceous); finer than $+4\phi$ are silt/clay (argillaceous).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Classify a rock consisting of $70\%$ volcanic ash and pumice fragments ejected violently from a volcanic vent and subsequently deposited and lithified in a lacustrine basin. Is it an igneous rock, a clastic sedimentary rock, or a hybrid?</p>
        <p><strong>Solution:</strong> The rock is a <strong>pyroclastic rock (specifically a lithified volcanic tuff)</strong>. Petrologically, it occupies a hybrid boundary: its components are generated by igneous volcanic processes (explosive magmatic fragmentation), but its transport, sorting, settling, and depositional bedding are governed entirely by sedimentary fluid processes. In sedimentological nomenclature, it is classified as a <strong>volcaniclastic rock</strong>.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>In the Goldich Weathering Series, which common rock-forming primary silicate mineral is most susceptible to mechanical and chemical breakdown, and which is the most resilient?</p>
        <p><strong>Solution:</strong> According to S.S. Goldich (1938), the susceptibility of primary silicate minerals to weathering is the inverse of Bowen's Reaction Series. <strong>Olivine</strong> (specifically forsterite, crystallizing at the highest temperatures $\sim 1200^\circ\text{C}$ with isolated $\text{SiO}_4^{4-}$ tetrahedra) is the <strong>most susceptible</strong> and least stable at surface conditions. <strong>Quartz</strong> (crystallizing at lowest temperatures with a fully polymerized 3D framework of Si-O bonds) is the <strong>most resilient</strong> and chemically stable.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Explain the role of freeze-thaw cycles (frost wedging) in the mechanical breakdown of alpine primary bedrocks, including the thermodynamic volumetric expansion of water.</p>
        <p><strong>Solution:</strong> When liquid water transitions to hexagonal ice at $0^\circ\text{C}$, the open hydrogen-bonded crystal lattice forces a <strong>$9\%$ increase in specific volume</strong> (from $1.000\text{ cm}^3\text{/g}$ to $1.0905\text{ cm}^3\text{/g}$). When confined within tight rock fractures, this expansion generates hydrostatic crystallization pressures theoretically reaching up to $207\text{ MPa}$ at $-22^\circ\text{C}$, vastly exceeding the tensile strength of crystalline rocks ($5\text{--}25\text{ MPa}$) and driving rapid physical shattering into block fields (felsenmeer).</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Why are graywackes (lithic/feldspathic wackes) referred to as "texturally and mineralogically immature" clastic rocks?</p>
        <p><strong>Solution:</strong> Graywackes contain $> 15\%$ fine-grained argillaceous/chloritic matrix, poorly sorted, angular to sub-angular framework grains (indicating <strong>textural immaturity</strong>), and high proportions of chemically unstable rock fragments and labile feldspars alongside quartz (indicating <strong>mineralogical immaturity</strong>). This combination reflects rapid erosion, short transport distances, and rapid deposition in high-energy, tectonically active environments (e.g., deep-marine turbidity currents in forearc basins).</p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=93,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q093_Clastic_Sedimentary_Rocks_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q093: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q093()
