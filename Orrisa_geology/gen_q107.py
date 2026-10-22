#!/usr/bin/env python3
"""
Q107 Generator: Slate Metamorphic Protolith & Pelitic Evolution
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q107():
    title = r"Q107: Metamorphic Petrology: Slate Protolith & Pelitic Metamorphic Evolution | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Protoliths"
    h1_title = "Q107: Metamorphic Protoliths: Slate Genesis from Parental Shale & The Pelitic Metamorphic Suite"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 107<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 21: Metamorphism of Pelitic Sediments, pp. 420–435; Fig. 21.1); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 82–86, 183); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 132–136); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PARENTAL PROTOLITH OF SLATE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Petrogenesis & Protolith Relationship of Slate</div>
    <div class="card-body">
      <p>
        In metamorphic geology (Winter, 2014, pp. 420–435; Bangar, p. 82; Mahapatra, p. 132), the term <strong>protolith</strong> designates the original, precursor unmetamorphosed parent rock from which a metamorphic rock was derived through thermal, dynamic, or regional metamorphic processes.
      </p>
      <p>
        <strong>Slate</strong> is universally recognized as the lowest-grade foliated metamorphic rock in the <strong>pelitic (aluminous) metamorphic suite</strong>, formed explicitly by the low-temperature, directed-stress regional metamorphism of a <strong>shale</strong> (or argillaceous mudstone) parental rock:
      </p>
      $$\mathbf{\text{Shale (Protolith)}} \xrightarrow[\Delta T \sim 200\text{--}300^\circ\text{C}]{\text{Directed Tectonic Stress } (\sigma_1)} \mathbf{\text{Slate}}$$

      <div class="figure-box">
        <img src="../../figures_Q107/winter_p420_slate_parental_shale_protolith.png" alt="Progressive Metamorphism of Pelitic Rocks from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 107.1 — Progressive Metamorphic Evolution of Pelitic Rocks:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 420). Traces the continuous prograde transformation from parent Shale $\rightarrow$ Slate $\rightarrow$ Phyllite $\rightarrow$ Schist $\rightarrow$ Gneiss $\rightarrow$ Migmatite under escalating temperature and pressure.
        </div>
      </div>

      <h4>Mineralogical and Textural Transformation: Shale to Slate</h4>
      <p>
        The conversion of a sedimentary shale into a metamorphic slate involves profound micro-structural and mineralogical re-equilibration:
      </p>
      <ul>
        <li><strong>Parental Shale Composition:</strong> Sub-microscopic, randomly to sub-parallel oriented detrital clay minerals (kaolinite, smectite, illite), fine quartz silt, and organic matter deposited in quiet aquatic environments.</li>
        <li><strong>Recrystallization into Slate:</strong> Under very low-grade conditions ($T \approx 200\text{--}300^\circ\text{C}$, $P \approx 2\text{--}4\text{ kbar}$):
          <ul>
            <li>Smectite and kaolinite become chemically unstable and react with available potassium to synthesize sub-microscopic flakes of <strong>sericite (fine-grained white mica / muscovite)</strong> and <strong>chlorite</strong>.</li>
            <li>Organic matter is pyrolyzed into microscopic graphite specks, imparting the characteristic dark grey, bluish-black, or charcoal color to slate.</li>
            <li>Under tectonic compression ($\sigma_1$), the growing sheet silicates re-crystallize in strict parallel alignment perpendicular to maximum compressive stress, developing pervasive <strong>slaty cleavage</strong>.</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: PROGRADE PELITIC PROGRESSION & PROTOLITH MATRIX -->
  <div class="card">
    <div class="card-header bg-emerald">2. The Classical Pelitic Prograde Sequence & Comparative Protolith Lineages</div>
    <div class="card-body">
      <h4>The Classical Barrovian Pelitic Prograde Lineage</h4>
      <p>
        When an original aluminous shale is subjected to progressively increasing regional metamorphism, it ascends through a continuous textural and mineralogical sequence:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Stage</th>
            <th>Metamorphic Grade</th>
            <th>Diagnostic Fabric / Cleavage</th>
            <th>Grain Size & Lustre</th>
            <th>Characteristic Mineral Assemblage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Shale (Parent Rock)</strong></td>
            <td>Sedimentary (Unmetamorphosed)</td>
            <td>Bedding fissility, lamination</td>
            <td>Sub-microscopic; dull earthy</td>
            <td>Detrital illite, smectite, kaolinite, quartz, organic carbon</td>
          </tr>
          <tr>
            <td><strong>Slate</strong></td>
            <td>Very Low Grade ($200\text{--}300^\circ\text{C}$)</td>
            <td><strong>Slaty cleavage</strong> (planar, smooth)</td>
            <td>Sub-microscopic ($< 10\mu\text{m}$); dull sheen</td>
            <td>Sericite, chlorite, microcrystalline quartz, graphite, albite</td>
          </tr>
          <tr>
            <td><strong>Phyllite</strong></td>
            <td>Low Grade ($300\text{--}450^\circ\text{C}$)</td>
            <td>Phyllitic cleavage (crenulated, wavy)</td>
            <td>Microscopic ($10\text{--}50\mu\text{m}$); <strong>silky lustrous sheen</strong></td>
            <td>Muscovite, chlorite, quartz, albite</td>
          </tr>
          <tr>
            <td><strong>Schist</strong></td>
            <td>Medium Grade ($450\text{--}650^\circ\text{C}$)</td>
            <td><strong>Schistosity</strong> (pervasive foliation)</td>
            <td>Megascopic ($> 0.1\text{ mm}$); glittering flakes</td>
            <td>Biotite, muscovite, almandine garnet, staurolite, kyanite</td>
          </tr>
          <tr>
            <td><strong>Gneiss</strong></td>
            <td>High Grade ($650\text{--}800^\circ\text{C}$)</td>
            <td><strong>Gneissose banding</strong> (segregated layers)</td>
            <td>Coarse-grained ($1\text{--}5\text{ mm}$); banded</td>
            <td>Quartz, K-feldspar, plagioclase, sillimanite, garnet</td>
          </tr>
        </tbody>
      </table>

      <h4>Protolith-Product Relationships of Other Rock Types</h4>
      <ul>
        <li><strong>Sandstone (Quartzose):</strong> Metamorphoses into <strong>Quartzite</strong> (non-foliated granoblastic mosaic of interlocking quartz grains).</li>
        <li><strong>Limestone / Dolostone:</strong> Metamorphoses into <strong>Marble</strong> (crystalline calcite/dolomite mosaic).</li>
        <li><strong>Basalt / Dolerite (Mafic):</strong> Metamorphoses into <strong>Greenschist $\rightarrow$ Amphibolite $\rightarrow$ Eclogite</strong>.</li>
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
        <strong>Question 107:</strong> Which will be the parental rock for Slate ?
      </div>
      <div class="options-grid">
        <div class="option-item correct-option"><strong>(A)</strong> Shale</div>
        <div class="option-item"><strong>(B)</strong> Sandstone</div>
        <div class="option-item"><strong>(C)</strong> Limestone</div>
        <div class="option-item"><strong>(D)</strong> All of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(A) Shale</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-correct">
        <div class="option-badge opt-a">Option (A) Confirmed — Shale Protolith</div>
        <p>
          <strong>Correct:</strong> By universal scientific consensus in geology and petrology (Winter, 2014, p. 420; Bangar, p. 82; Mahapatra, p. 132), <strong>shale</strong> is the definitive sedimentary parental rock (protolith) for <strong>slate</strong>. When a clay-rich shale is subjected to regional compressive stress and low-grade temperatures ($200\text{--}300^\circ\text{C}$), its clay minerals dynamically recrystallize into microscopic parallel plates of sericite and chlorite, forming slate with pervasive slaty cleavage.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Sandstone Protolith</div>
        <p>
          <strong>Incorrect:</strong> The metamorphism of quartz sandstone produces <strong>quartzite</strong>, a dense, non-foliated granoblastic metamorphic rock composed of recrystallized, interlocking quartz crystals. Sandstone contains $> 80\text{--}95\%$ quartz and lacks the abundant aluminum and potassium necessary to crystallize the aligned phyllosilicates (micas) that generate slaty cleavage in slate.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Limestone Protolith</div>
        <p>
          <strong>Incorrect:</strong> The metamorphism of carbonate limestone or dolostone produces <strong>marble</strong>, characterized by interlocking granoblastic rhombohedral crystals of calcite ($\text{CaCO}_3$) or dolomite. Limestone cannot form slate because it is chemically dominated by calcium and carbonate ions, completely lacking the hydrous aluminum silicates required for slate genesis.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — All of These</div>
        <p>
          <strong>Incorrect:</strong> Because sandstone produces quartzite and limestone produces marble, neither of these rocks can serve as the parental rock for slate. The protolith is exclusively <strong>(A) Shale</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Protolith vs. Metamorphic Product Correlation Matrix</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Original Parental Rock (Protolith)</th>
            <th>Chemical Category</th>
            <th>Low-Grade Product</th>
            <th>Medium-Grade Product</th>
            <th>High-Grade Product</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Shale / Mudstone</strong></td>
            <td><strong>Pelitic (Aluminous)</strong></td>
            <td><strong>Slate $\rightarrow$ Phyllite</strong></td>
            <td>Garnet-Mica Schist</td>
            <td>Sillimanite-K-feldspar Gneiss / Migmatite</td>
          </tr>
          <tr>
            <td><strong>Quartz Sandstone</strong></td>
            <td>Psammitic (Siliceous)</td>
            <td>Proto-quartzite</td>
            <td>Orthoquartzite</td>
            <td>Granoblastic Quartzite</td>
          </tr>
          <tr>
            <td><strong>Limestone / Dolomite</strong></td>
            <td>Calcareous (Carbonate)</td>
            <td>Fine-grained Marble</td>
            <td>Crystalline Marble</td>
            <td>Coarse-grained Calcite-Wollastonite Marble</td>
          </tr>
          <tr>
            <td><strong>Basalt / Dolerite</strong></td>
            <td>Basic / Mafic</td>
            <td>Greenschist (chlorite-actinolite)</td>
            <td>Amphibolite (hornblende-plagioclase)</td>
            <td>Pyroxene Granulite / Eclogite</td>
          </tr>
          <tr>
            <td><strong>Granite / Rhyolite</strong></td>
            <td>Felsic / Quartzo-feldspathic</td>
            <td>Meta-granite / Mylonite</td>
            <td>Granitic Gneiss</td>
            <td>Orthogneiss / Charnockite</td>
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
        <p>Explain the structural and mechanical difference between "bedding fissility" in a parent shale and "slaty cleavage" in the resulting slate.</p>
        <p><strong>Solution:</strong>
          - <strong>Bedding Fissility (Shale):</strong> A primary sedimentary fabric oriented strictly parallel to the original depositional stratification surfaces ($S_0$), formed by gravity compaction and settling of clay flakes in quiet water.
          - <strong>Slaty Cleavage (Slate):</strong> A secondary, tectonic, metamorphic planar fabric ($S_1$) formed by dynamic recrystallization of sericite and chlorite. Slaty cleavage forms <strong>perpendicular to the maximum regional tectonic compressive stress ($\sigma_1$)</strong>, oriented parallel to the axial plane of folds, typically intersecting and cutting across original bedding planes at steep angles.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Under what specific $P\text{-}T$ conditions does the metamorphism of shale transition into slate, and what is the characteristic metamorphic facies?</p>
        <p><strong>Solution:</strong>
          The transition from shale to slate occurs in the <strong>anchizone / sub-greenschist to lowest greenschist facies</strong> at temperatures of <strong>$200^\circ\text{C}$ to $300^\circ\text{C}$</strong> and confining pressures of approximately <strong>$2\text{ to } 4\text{ kbar}$</strong> (equivalent to burial depths of $\sim 6\text{ to } 12\text{ km}$) accompanied by intense directed tectonic differential stress ($\sigma_1 > \sigma_3$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Why is roofing slate impermeable to water and highly resistant to frost weathering compared to its parent shale?</p>
        <p><strong>Solution:</strong>
          Parent shale contains open capillary pores ($5\text{--}15\%$ porosity) and expandable clay minerals that absorb water and slake rapidly. In slate, metamorphic recrystallization and ductile compaction squeeze out virtually all pore space (porosity $< 0.5\%$), and expandable smectites are transformed into dense, non-expandable muscovite/chlorite lattices with tightly interlocked grain boundaries, rendering high-quality slate completely impermeable and frost-resistant.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What causes the distinctive silvery, lustrous sheen that distinguishes a phyllite from a dull matte slate?</p>
        <p><strong>Solution:</strong>
          In <strong>slate</strong>, the recrystallized sericite and chlorite flakes are sub-microscopic ($< 10\mu\text{m}$ in diameter), too small to reflect visible light coherently, giving slate a dull, matte appearance. In <strong>phyllite</strong> (formed at slightly higher temperatures, $300\text{--}450^\circ\text{C}$), progressive crystal growth enlarges the mica flakes to microscopic dimensions ($10\text{--}50\mu\text{m}$). These aligned, parallel mica crystals act as tiny microscopic mirrors, reflecting incident light simultaneously to produce the diagnostic <strong>silky, lustrous sheen (phyllitic sheen)</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Identify the chemical cause for red, green, and black coloration in slates.</p>
        <p><strong>Solution:</strong>
          - <strong>Black / Dark Grey Slate:</strong> Caused by finely disseminated, microscopic amorphous <strong>carbonaceous organic matter / graphite</strong> inherited from anoxic parent black shales.
          - <strong>Green Slate:</strong> Caused by the dominance of ferrous iron-bearing <strong>chlorite</strong> ($\text{Fe}^{2+}$-rich chlorite) formed under reducing or low-oxygen conditions.
          - <strong>Red / Purple Slate:</strong> Caused by finely dispersed, microcrystalline ferric iron oxide (<strong>hematite, $\text{Fe}_2\text{O}_3$</strong>) inherited from oxidized red-bed shale protoliths.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is a "spotted slate" and under what geological metamorphic regime does it form?</p>
        <p><strong>Solution:</strong>
          A <strong>spotted slate</strong> forms by <strong>contact (thermal) metamorphism</strong> where an igneous pluton intrudes a shale or slate formation under static, non-directed stress conditions. Heat from the magma initiates localized nucleation and growth of new, poikiloblastic minerals—typically cordierite, andalusite (chiastolite), or biotite—which appear as conspicuous dark ovoid "spots" ($1\text{--}5\text{ mm}$) scattered across the slaty matrix.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>In structural geology, explain the concept of "cleavage-bedding intersection lineation" in a slate outcrop.</p>
        <p><strong>Solution:</strong>
          When a sedimentary shale is folded during orogenesis, original bedding planes ($S_0$) are cut by tectonic slaty cleavage planes ($S_1$). The intersection of these two non-parallel planes creates a linear structural fabric called the <strong>cleavage-bedding intersection lineation ($L_{0-1}$)</strong>. Geometrically, this lineation is strictly parallel to the <strong>fold axis ($B$-axis)</strong> of the regional folds, allowing field geologists to determine the plunge and trend of regional fold axes from small slate hand specimens.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Why does slate exhibit exceptional splitting properties (cleavability) that make it an outstanding architectural material?</p>
        <p><strong>Solution:</strong>
          Slate's cleavability is governed by the <strong>near-perfect crystallographic parallelism</strong> of millions of microscopic platy phyllosilicate flakes (sericite and chlorite). Because these sheet silicates share identical basal pinacoid $\{001\}$ cleavage oriented in a single plane, mechanical tensile strength across the cleavage plane is very low, allowing the rock to be split cleanly and effortlessly into razor-thin, structurally sound planar sheets of uniform thickness without breaking.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=107,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q107_Slate_Parental_Rock_Shale_Protolith_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q107: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q107()
