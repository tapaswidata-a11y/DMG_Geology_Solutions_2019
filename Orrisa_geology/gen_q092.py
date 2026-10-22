#!/usr/bin/env python3
"""
Q092 Generator: Shale Petrography, Laminar Structure & Fissility
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q092():
    title = r"Q092: Sedimentary Petrology: Shale Laminar Structure & Fissility | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Mudrocks"
    h1_title = "Q092: Shale Characterization: Laminar Structure, Fissility & Clay Fabric"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 92<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 6: Mudrocks, pp. 150–165; Fig. 6.4); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 73–75, 173); P.E. Potter, J.B. Maynard, and P.J. Depetris, <em>Mud and Mudstones: Introduction and Overview</em> (Springer); Maurice E. Tucker, <em>Sedimentary Petrology: An Introduction to the Origin of Sedimentary Rocks</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PETROLOGY OF SHALES -->
  <div class="card">
    <div class="card-header bg-blue">1. Mudrock Petrography: Definition of Shale, Laminar Structure & Fissility</div>
    <div class="card-body">
      <p>
        Mudrocks (siliciclastic sedimentary rocks composed predominantly of particles smaller than $0.0625\text{ mm}$ or $62.5\mu\text{m}$, representing silt and clay) constitute over <strong>$50\text{ to } 65\%$ of the entire sedimentary rock record</strong> on Earth.
      </p>
      <p>
        Within this clan, <strong>shale</strong> is rigorously defined in sedimentary petrology (Boggs, 2014, p. 152; Potter et al., 2005) as a fine-grained, siliciclastic sedimentary rock characterized essentially by two distinct attributes:
      </p>
      <ol>
        <li><strong>Fine Laminar Structure (Primary Micro-bedding):</strong> Individual sedimentary layers or laminae are thin, typically measuring <strong>less than $10\text{ mm}$ ($1\text{ cm}$) thick</strong> (often sub-millimeter scale, $0.05\text{--}1.0\text{ mm}$). These reflect subtle rhythmic fluctuations in hydrodynamic deposition, sediment influx, or seasonal organic blooms.</li>
        <li><strong>Fissility:</strong> The physical tendency of the rock to split smoothly and cleanly along closely spaced, parallel bedding planes into thin, planar sheets or flakes under mechanical stress or gentle weathering.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q92/boggs_p155_shale_laminar_structure_fissility.png" alt="Shale Laminar Structure and Fissility Fabric from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 92.1 — Petrographic Architecture and Fissility of Shale:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 155). Illustrates the parallel orientation of phyllosilicate clay platelets under overburden burial compaction and primary depositional micro-lamination, creating the characteristic fissile fabric.
        </div>
      </div>

      <h4>Mudstone vs. Shale: The Fissility Distinction</h4>
      <p>
        In modern sedimentary petrographic nomenclature (e.g., Folk, 1980; Lundegard and Samuels, 1980; Boggs, 2014), fine-grained siliciclastic rocks are divided according to grain size and presence of fissility:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Grain-Size Category</th>
            <th>Non-Fissile / Massive Equivalent</th>
            <th>Fissile / Laminated Equivalent (Shale)</th>
            <th>Grain-Size Range</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Silt-dominated ($> 66\%$ Silt)</strong></td>
            <td>Siltstone (massive, blocky)</td>
            <td><strong>Silt-shale</strong> (laminated, fissile)</td>
            <td>$0.0625\text{ to } 0.0039\text{ mm}$ ($4\phi\text{ to } 8\phi$)</td>
          </tr>
          <tr>
            <td><strong>Mud-mixture (Clay + Silt)</strong></td>
            <td>Mudstone (subconchoidal, blocky)</td>
            <td><strong>Mud-shale</strong> (fissile, paper shale)</td>
            <td>Subequal mixtures of silt and clay</td>
          </tr>
          <tr>
            <td><strong>Clay-dominated ($> 66\%$ Clay)</strong></td>
            <td>Claystone (massive, plastic when wet)</td>
            <td><strong>Clay-shale</strong> (highly fissile, flaky)</td>
            <td>$< 0.0039\text{ mm}$ ($> 8\phi$)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: ORIGIN OF LAMINATION AND PETROPHYSICAL ANISOTROPY -->
  <div class="card">
    <div class="card-header bg-emerald">2. Genesis of Lamination: Compaction Fabric, Anoxia & Engineering Implications</div>
    <div class="card-body">
      <h4>Microstructural Origin of Fissility</h4>
      <p>
        The formation of fissile, laminar shale requires a precise combination of depositional and diagenetic factors:
      </p>
      <ul>
        <li><strong>Parallel Phyllosilicate Reorientation:</strong> During initial deposition in flocculated clay suspensions, clay platelets form random, edge-to-face "card-house" flocculation structures with porosities up to $70\text{--}80\%$. As sediment is buried under progressive overburden load ($P_{overburden} > 10\text{--}50\text{ MPa}$), gravitational compaction collapses the card-house structure, forcing platy sheet silicates (illite, smectite, kaolinite, chlorite) to rotate into a dense, parallel face-to-face orientation perpendicular to maximum principal stress ($\sigma_1$ vertical).</li>
        <li><strong>Micro-lamination Preservation via Anoxia:</strong> In oxygenated aquatic settings, benthic burrowing organisms (worms, bivalves, crustaceans) continuously churn and homogenize muddy sediments (bioturbation), obliterating primary layering and producing massive, unlaminated mudstones. Preservation of delicate millimetric laminae requires <em>anoxic or euxinic bottom waters</em> where infauna cannot survive.</li>
        <li><strong>Compositional Segregation:</strong> Alternations between organic-rich or clay-rich laminae and silt-rich laminae (e.g., seasonal storm pulses, riverine spring freshets, or phytoplankton blooms) generate planes of mechanical weakness.</li>
      </ul>

      <h4>Engineering Hazards and Anisotropy</h4>
      <ul>
        <li><strong>Extreme Mechanical Anisotropy:</strong> Unconfined compressive strength ($\sigma_c$) measured parallel to lamination ($\sigma_{c\parallel}$) is often $40\text{--}70\%$ lower than that measured perpendicular to lamination ($\sigma_{c\perp}$), creating high risk of planar sliding along daylighting beds in road cuttings and open-pit mines.</li>
        <li><strong>Slaking and Swelling:</strong> When de-stressed and exposed to atmospheric moisture or cyclical wetting/drying, smectite-bearing shales undergo osmotic swelling and spontaneous slaking disintegration.</li>
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
        <strong>Question 92:</strong> Shales are generally characterized with distinct :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> cleavage</div>
        <div class="option-item correct-option"><strong>(B)</strong> laminar structure</div>
        <div class="option-item"><strong>(C)</strong> joints</div>
        <div class="option-item"><strong>(D)</strong> parting</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) laminar structure</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Cleavage</div>
        <p>
          <strong>Incorrect:</strong> In geological terminology, <strong>cleavage</strong> has two distinct meanings, neither of which is the primary diagnostic characteristic of unmetamorphosed shale:
          (1) In mineralogy, cleavage refers to the crystallographic splitting along planes of atomic weakness in single crystals (e.g., basal cleavage in mica, rhombohedral cleavage in calcite).
          (2) In structural geology, <em>slaty cleavage</em> or <em>schistosity</em> is a <strong>secondary, tectonic, metamorphic fabric</strong> produced by ductile strain, recrystallization, and pressure solution during regional orogenesis, forming perpendicular to maximum tectonic shortening ($\sigma_1$), typically cutting across primary bedding planes at an angle. Unmetamorphosed shale exhibits sedimentary lamination and fissility, not tectonic cleavage.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — Laminar Structure</div>
        <p>
          <strong>Correct:</strong> By definition in sedimentary petrology (Boggs, 2014; Bangar, p. 73), <strong>shales</strong> are universally distinguished from massive mudrocks by their <strong>distinct laminar structure</strong> (fine sub-millimeter to millimetric layering, $< 10\text{ mm}$ thick) and associated <strong>fissility</strong>. This laminar fabric results from depositional grain-size/organic sorting and the preferred face-to-face parallel orientation of microscopic clay mineral flakes under overburden burial compaction.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Joints</div>
        <p>
          <strong>Incorrect:</strong> <strong>Joints</strong> are brittle fracture surfaces in rock masses along which there has been no perceptible displacement parallel to the plane. Joints occur ubiquitously in all types of rocks (igneous granites and basalts, metamorphic gneisses, and sedimentary limestones and sandstones) due to regional tectonic stress fields, fluid overpressure, or cooling/unloading contraction. Joints are secondary structural discontinuities, not the intrinsic petrographic defining feature of shale.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Parting</div>
        <p>
          <strong>Incorrect:</strong> While the term "parting" refers broadly to a separation or thin non-coal interbed in coal seams, or false cleavage in certain minerals (e.g., corundum twinning planes), it does not constitute the comprehensive primary petrological and structural characterization of shale. The definitive textbook property that defines and characterises shale in sedimentary geology is its <strong>laminar structure</strong> and primary bedding fissility.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Analysis: Sedimentary Bedding Fabrics vs. Tectonic & Brittle Structures</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Geological Feature</th>
            <th>Genetic Origin</th>
            <th>Scale & Geometry</th>
            <th>Primary Controls</th>
            <th>Typical Host Rocks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Laminar Structure (Shale)</strong></td>
            <td>Sedimentary deposition & burial compaction</td>
            <td>Planar, parallel sheets; thickness $< 10\text{ mm}$ (often $< 1\text{ mm}$)</td>
            <td>Cyclic sedimentation, quiet water, anoxia, preferred face-to-face clay alignment</td>
            <td>Shale (mud-shale, clay-shale, silt-shale, oil shale)</td>
          </tr>
          <tr>
            <td><strong>Slaty Cleavage</strong></td>
            <td>Tectonic metamorphism (low-grade regional)</td>
            <td>Closely spaced pervasive foliation ($< 0.1\text{ mm}$)</td>
            <td>Tectonic shortening ($\sigma_1$), dynamic recrystallization, pressure solution</td>
            <td>Slate, phyllite (metamorphosed pelites)</td>
          </tr>
          <tr>
            <td><strong>Joints</strong></td>
            <td>Brittle mechanical fracturing</td>
            <td>Discontinuous fractures; centimeters to tens of meters; open or mineral-filled</td>
            <td>Tensile or shear tectonic stresses, hydraulic fracturing, thermal contraction, erosional unloading</td>
            <td>All rock types (sandstone, basalt, granite, limestone)</td>
          </tr>
          <tr>
            <td><strong>Bedding Parting</strong></td>
            <td>Sedimentary bedding boundary separation</td>
            <td>Discrete macroscopic separation plane between thicker beds ($> 1\text{ cm}$)</td>
            <td>Abrupt lithological or environmental hiatus during sedimentation</td>
            <td>Sandstones, limestones, thick-bedded siltstones</td>
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
        <p>Distinguish between a mudstone and a shale based on textural and physical criteria defined by Sam Boggs Jr. and K.M. Bangar.</p>
        <p><strong>Solution:</strong> Both mudstone and shale are fine-grained siliciclastic rocks composed predominantly of silt and clay particles ($< 0.0625\text{ mm}$). The defining distinction is that <strong>shale</strong> possesses a distinct <strong>laminar structure</strong> ($< 10\text{ mm}$ thick) and <strong>fissility</strong> (readily splitting along parallel planes), whereas <strong>mudstone</strong> is massive, blocky, and breaks with a subconchoidal or irregular fracture without splitting into thin sheets.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Why do highly fossiliferous marine shelf mudrocks frequently lack laminar structure, whereas black basinal mudrocks display pristine sub-millimeter lamination?</p>
        <p><strong>Solution:</strong> Well-oxygenated marine shelf environments support rich communities of benthic macroinfauna (annelids, echinoderms, burrowing bivalves) that thoroughly churn the upper $5\text{--}20\text{ cm}$ of sediment through <strong>bioturbation</strong>, completely destroying depositional laminae. In contrast, restricted basinal environments with anoxic bottom water preclude benthic animal life, allowing undisturbed deposition of organic-clay laminae and preserving pristine laminar shale fabric.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>A core sample of shale is subjected to point load testing. The Point Load Strength Index measured perpendicular to lamination ($I_{s(50)\perp}$) is $3.8\text{ MPa}$, while parallel to lamination ($I_{s(50)\parallel}$) it is $1.1\text{ MPa}$. Calculate the Strength Anisotropy Index ($I_a$) and classify its degree of anisotropy according to ISRM standards.</p>
        <p><strong>Solution:</strong>
          The Strength Anisotropy Index is given by:
          $$I_a = \frac{I_{s(50)\perp}}{I_{s(50)\parallel}} = \frac{3.8\text{ MPa}}{1.1\text{ MPa}} \approx 3.45$$
          According to the International Society for Rock Mechanics (ISRM), an anisotropy index between $2.0$ and $4.0$ is classified as <strong>High Anisotropy</strong> (values $> 4.0$ are Extreme Anisotropy). This severe anisotropy must be accounted for in slope and tunnel design.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Explain the microscopic structural change that occurs when a flocculated clay suspension is transformed into a compacted shale during progressive burial from $0\text{ m}$ to $2000\text{ m}$ depth.</p>
        <p><strong>Solution:</strong>
          At the sediment-water interface ($0\text{ m}$), clay particles interact via edge-to-face electrostatic charges forming an open, porous "card-house" flocculated structure with $70\text{--}80\%$ water content (porosity). Under burial compaction ($2000\text{ m}$, overburden pressure $\approx 45\text{--}50\text{ MPa}$), water is expelled, collapsing the card-house framework. Mechanical shear and vertical strain force the platy phyllosilicate crystals (illite, smectite) to rotate and align parallel to each other in dense face-to-face horizontal orientations, generating primary fissility and reducing porosity to $< 10\%$.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>How does a field geologist distinguish between sedimentary fissility in a carbonaceous shale and tectonic slaty cleavage in a low-grade slate?</p>
        <p><strong>Solution:</strong>
          In a field outcrop:
          1. <strong>Orientation Relative to Bedding:</strong> Sedimentary fissility in shale is strictly parallel to depositional bedding planes ($S_0$) and lithological contacts. Slaty cleavage ($S_1$) is a tectonic planar fabric oriented parallel to the axial plane of folds and cuts across bedding planes at varying angles.
          2. <strong>Mineral Recrystallization:</strong> Slate has undergone dynamic recrystallization producing microscopic white mica (sericite) with a silky macroscopic sheen, whereas shale has non-recrystallized detrital/authigenic clays with a dull, earthy luster.
          3. <strong>Water Immersion:</strong> Shale chips will generally soften or slake in water, whereas slate is metamorphically indurated and will not slake.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is an "oil shale" and how is it related to sedimentary lamination and kerogen preservation?</p>
        <p><strong>Solution:</strong>
          An oil shale is a fine-grained, laminated sedimentary rock containing substantial quantities of solid, insoluble organic matter called <strong>kerogen</strong> (typically Type I or Type II, $10\text{--}40\text{ wt}\%$) that yields liquid hydrocarbons upon destructive pyrolysis ($450\text{--}500^\circ\text{C}$). The fine laminar structure of oil shales represents seasonal alternations of lipid-rich algal blooms and fine clay deposition in quiet, stratified, anoxic lacustrine or marine waters (e.g., the Eocene Green River Formation).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Explain the slaking mechanism of shale in engineering geology and state the standard laboratory test used to quantify it.</p>
        <p><strong>Solution:</strong>
          Slaking is the spontaneous disintegration and crumbling of shale upon exposure to cyclical wetting and drying. The mechanism involves: (a) air entrapment and compression in micro-capillaries upon water immersion, (b) osmotic swelling of expandable smectite/illite interlayers, and (c) dissolution of soluble salt cements. Slaking susceptibility is standardized by the <strong>Slake Durability Test (ASTM D4644 / ISRM)</strong>, which measures the <strong>Slake Durability Index ($I_{d2}$)</strong> as the percentage dry weight retained after two cycles of rotating the sample in a water bath inside a wire mesh drum.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>In seismic exploration for shale gas, why is vertical transverse isotropy (VTI) a fundamental characteristic of shale formations?</p>
        <p><strong>Solution:</strong>
          Due to its pronounced <strong>laminar structure</strong> and the uniform horizontal alignment of anisotropic platy clay minerals, shale behaves as a transversely isotropic medium with a vertical axis of rotational symmetry (VTI). Compressional seismic waves ($P$-waves) travel faster along the horizontal bedding planes ($V_{P\parallel} \approx 3800\text{--}4500\text{ m/s}$) than vertically across the laminae ($V_{P\perp} \approx 2800\text{--}3400\text{ m/s}$), governed by Thomsen's anisotropy parameters ($\epsilon$, $\gamma$, and $\delta$).
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=92,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q092_Shale_Laminar_Structure_Fissility_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q092: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q092()
