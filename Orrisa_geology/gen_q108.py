#!/usr/bin/env python3
"""
Q108 Generator: Metamorphic Foliation Genesis & Thermodynamic Metamorphism
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q108():
    title = r"Q108: Metamorphic Petrology: Foliation Genesis & Thermodynamic Metamorphism | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Textures"
    h1_title = "Q108: Metamorphic Foliation: Preferred Mineral Alignment & Thermodynamic (Dynamothermal) Metamorphism"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 108<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 22: Metamorphic Textures & Deformation, pp. 450–465; Fig. 22.3); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 82–85, 181); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 128–132); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PETROLOGICAL ORIGIN OF FOLIATION -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Architecture & Thermodynamic Coupling of Metamorphic Foliation</div>
    <div class="card-body">
      <p>
        In structural geology and metamorphic petrology (Winter, 2014, pp. 450–465; Bangar, p. 82; Mahapatra, p. 128), <strong>foliation</strong> (derived from the Latin <em>folium</em>, meaning "leaf") is defined as any repetitive, penetrative planar fabric in a metamorphic rock resulting from:
      </p>
      <ol>
        <li>The preferred crystallographic or dimensional parallel alignment of inequant mineral grains—predominantly platy phyllosilicates (micas, chlorite, talc) and prismatic inosilicates (amphiboles).</li>
        <li>Alternating compositional or textural mineral bands (e.g., alternating light quartz-feldspar and dark biotite-amphibole layers in gneisses).</li>
        <li>Flattened, ductilely deformed mineral aggregates, pebbles, or ooids.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q108/winter_p455_foliation_thermodynamic_deformation.png" alt="Mechanisms of Foliation Development from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 108.1 — Thermodynamic and Mechanical Genesis of Metamorphic Foliation:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 455). Illustrates foliation development via the simultaneous coupling of directed tectonic differential stress ($\sigma_1 > \sigma_3$) and elevated temperature (thermal activation), driving crystal rotation, pressure solution, and oriented neocrystallization.
        </div>
      </div>

      <h4>Why Foliation is Inherently a "Thermodynamic" Process</h4>
      <p>
        The formation of true penetrative metamorphic foliation requires the simultaneous, coupled operation of two distinct geological driving forces—formally termed <strong>thermodynamic (or dynamothermal / regional) metamorphism</strong>:
      </p>
      <ul>
        <li><strong>Thermal Component (Heat, $\Delta T$):</strong> Thermal energy provides the vital activation energy necessary for chemical bonds to break and reform, driving <strong>solid-state neocrystallization, ionic diffusion, and grain-boundary migration</strong>. Without heat, minerals cannot grow or chemically reorganize.</li>
        <li><strong>Dynamic Component (Directed Tectonic Stress, $\sigma_1 > \sigma_3$):</strong> Non-hydrostatic differential stress creates a directional strain field. According to thermodynamics, crystal growth is energetically favored in orientations of lowest strain energy. Platy phyllosilicates (micas) grow spontaneously with their basal $\{001\}$ planes oriented <strong>perpendicular to the maximum principal compressive stress ($\sigma_1$)</strong> and parallel to the extension direction ($\sigma_3$).</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: MECHANICAL MECHANISMS & CONTRAST WITH OTHER REGIMES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Microstructural Mechanisms of Foliation & Contrast with Other Metamorphic Regimes</div>
    <div class="card-body">
      <h4>The Four Microscopic Mechanisms Generating Foliation</h4>
      <ol>
        <li><strong>Rotation of Pre-Existing Inequant Grains:</strong> Mechanical rotation of rigid mineral flakes through a ductilely deforming matrix toward the kinematic flattening plane.</li>
        <li><strong>Dynamic Recrystallization and Pressure Solution:</strong> Under directed stress, high-stress grain boundaries dissolve preferentially into interstitial fluids; the dissolved ions diffuse and precipitate onto low-stress grain faces parallel to $\sigma_3$ (Riecke's Principle), flattening grains.</li>
        <li><strong>Directed Neocrystallization (Oriented Nucleation and Growth):</strong> New metamorphic minerals (e.g., biotite, muscovite, hornblende) nucleate and crystallize with their fastest-growing crystallographic axes aligned in the low-stress plane of flattening.</li>
        <li><strong>Intracrystalline Plastic Slip (Dislocation Creep):</strong> High temperatures activate crystallographic slip systems within quartz and calcite, causing grains to stretch ductilely into elongated ribbons.</li>
      </ol>

      <h4>Comparison of Metamorphic Regimes</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Type</th>
            <th>Governing Geological Agent</th>
            <th>Stress State</th>
            <th>Resulting Fabric / Texture</th>
            <th>Representative Rock Suite</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Thermal (Contact)</strong></td>
            <td>Heat ($\Delta T$) from igneous intrusion</td>
            <td>Hydrostatic / Isotropic ($\sigma_1 = \sigma_2 = \sigma_3$)</td>
            <td><strong>Non-foliated</strong>; random interlocking granoblastic / hornfelsic texture</td>
            <td>Hornfels, Marble, Quartzite</td>
          </tr>
          <tr>
            <td><strong>Dynamic (Cataclastic)</strong></td>
            <td>Directed shear stress ($\tau$) along faults at low $T$</td>
            <td>Intense non-hydrostatic shear</td>
            <td>Mechanical fracturing, crushing; non-foliated or localized shear ribbons</td>
            <td>Fault breccia, Cataclasite, Mylonite</td>
          </tr>
          <tr>
            <td><strong>Thermodynamic (Dynamothermal / Regional)</strong></td>
            <td><strong>Coupled Heat ($\Delta T$) + Directed Stress ($\sigma_1 > \sigma_3$)</strong></td>
            <td><strong>Triaxial differential tectonic compression</strong></td>
            <td><strong>Pervasive, penetrative foliation</strong> (slaty cleavage, schistosity, gneissic banding)</td>
            <td><strong>Slate, Phyllite, Schist, Gneiss</strong></td>
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
        <strong>Question 108:</strong> Foliation in metamorphic rocks developed due to which metamorphic process ?
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Thermal</div>
        <div class="option-item"><strong>(B)</strong> Dynamic</div>
        <div class="option-item correct-option"><strong>(C)</strong> Thermodynamic</div>
        <div class="option-item"><strong>(D)</strong> All of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(C) Thermodynamic</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Thermal Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> <strong>Thermal (contact) metamorphism</strong> operates under high temperatures adjacent to igneous plutons where the stress field is essentially <strong>hydrostatic (isotropic, $\sigma_1 = \sigma_2 = \sigma_3$)</strong>. Without directed differential stress to guide crystal orientation, minerals grow in completely random, unoriented directions, producing classic <strong>non-foliated rocks</strong> with granoblastic or decussate hornfelsic textures (e.g., hornfels, marble, quartzite). Thermal metamorphism does not produce foliation.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Dynamic Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> Pure <strong>dynamic (cataclastic) metamorphism</strong> operates under directed shear stress in shallow fault zones at low temperatures. Because thermal energy is lacking, the process is dominated by brittle mechanical crushing, granulation, and micro-shattering without significant solid-state metamorphic recrystallization, producing unfoliated fault breccias and cataclasites. It is insufficient on its own to generate regional penetrative crystalline foliation.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-c">Option (C) Confirmed — Thermodynamic Metamorphism</div>
        <p>
          <strong>Correct:</strong> In classical petrology and standard Indian geological curricula (Bangar, p. 82; Mahapatra, p. 128; Winter, 2014), the process that combines <strong>elevated thermal energy (thermo)</strong> and <strong>directed tectonic differential stress (dynamic)</strong> is formally designated as <strong>thermodynamic (or dynamothermal) metamorphism</strong>. Heat enables atomic diffusion and prograde recrystallization, while directed stress simultaneously controls the parallel alignment of growing inequant minerals, directly producing penetrative <strong>foliation</strong> (slaty cleavage, schistosity, and gneissic banding).
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — All of These</div>
        <p>
          <strong>Incorrect:</strong> Because thermal metamorphism produces non-foliated hornfelses and dynamic metamorphism produces cataclasites, asserting that "all of these" produce foliation is scientifically fallacious. Foliation is the diagnostic hallmark exclusively of <strong>(C) Thermodynamic</strong> metamorphism.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Spectrum of Metamorphic Foliation Types</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Foliation Type</th>
            <th>Defining Petrographic Characteristics</th>
            <th>Primary Aligned Minerals</th>
            <th>Metamorphic Grade</th>
            <th>Exemplary Rock Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Slaty Cleavage</strong></td>
            <td>Pervasive, planar, perfectly parallel fissility along sub-microscopic surfaces</td>
            <td>Sub-microscopic sericite (white mica), chlorite, quartz</td>
            <td>Very Low Grade ($200\text{--}300^\circ\text{C}$)</td>
            <td><strong>Slate</strong></td>
          </tr>
          <tr>
            <td><strong>Phyllitic Cleavage</strong></td>
            <td>Pervasive, wavy, micro-crenulated foliation with a silky lustrous sheen</td>
            <td>Microscopic muscovite, chlorite, quartz</td>
            <td>Low Grade ($300\text{--}450^\circ\text{C}$)</td>
            <td><strong>Phyllite</strong></td>
          </tr>
          <tr>
            <td><strong>Schistosity</strong></td>
            <td>Coarse-grained, visible crystalline foliation; sparkling glittering flakes</td>
            <td>Visible megascopic flakes ($> 0.1\text{ mm}$) of biotite, muscovite, talc, chlorite</td>
            <td>Medium Grade ($450\text{--}650^\circ\text{C}$)</td>
            <td><strong>Schist</strong> (e.g., Mica schist, Garnet schist)</td>
          </tr>
          <tr>
            <td><strong>Gneissic Banding</strong></td>
            <td>Segregated alternating macroscopic layers of light felsic and dark mafic minerals</td>
            <td>Felsic bands (quartz, feldspar) alternating with mafic bands (biotite, hornblende)</td>
            <td>High Grade ($650\text{--}800^\circ\text{C}$)</td>
            <td><strong>Gneiss</strong></td>
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
        <p>A shale formation is intruded by a hot granite batholith ($T \approx 800^\circ\text{C}$) at a shallow crustal depth ($2\text{ km}$, hydrostatic lithostatic load). Will the metamorphosed contact aureole exhibit foliation? Justify your answer based on stress states.</p>
        <p><strong>Solution:</strong>
          <strong>No, the rock will not exhibit foliation.</strong> At a shallow crustal depth under static magmatic intrusion, the rock mass experiences purely <strong>hydrostatic (isotropic) stress</strong>, where compressive stresses are equal in all directions ($\sigma_1 = \sigma_2 = \sigma_3$). In the absence of a directed tectonic differential stress ($\sigma_1 > \sigma_3$), growing metamorphic minerals (cordierite, andalusite, biotite) nucleate and grow with random, unoriented crystallographic orientations, producing a dense, tough, <strong>non-foliated hornfels</strong> with granoblastic/decussate texture.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain the thermodynamic mechanism of "pressure solution" (Riecke's Principle) during the development of slaty cleavage under tectonic differential stress.</p>
        <p><strong>Solution:</strong>
          According to the Riecke Principle, chemical chemical potential and solubility of a mineral crystal increase under directed compressive stress. When a rock experiences non-hydrostatic stress ($\sigma_1 \gg \sigma_3$):
          - Mineral surfaces oriented perpendicular to $\sigma_1$ experience maximum compressive stress, driving <strong>selective dissolution</strong> into interstitial pore fluids.
          - The dissolved solutes diffuse through pore fluids away from high-stress faces and reprecipitate in low-stress zones (parallel to $\sigma_3$), where solubility is lower.
          This thermodynamic mass transfer continuously shortens the rock along $\sigma_1$ and extends it along $\sigma_3$, generating thin planar seams of insoluble mica/clay residue that form <strong>slaty cleavage foliation</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Distinguish between "foliation" and "lineation" in a deformed metamorphic rock.</p>
        <p><strong>Solution:</strong>
          - <strong>Foliation:</strong> A penetrative, two-dimensional <strong>planar</strong> structural fabric produced by the parallel alignment of platy sheet silicates (micas) or alternating compositional bands.
          - <strong>Lineation:</strong> A penetrative, one-dimensional <strong>linear</strong> structural fabric produced by the preferred parallel alignment of elongated, needle-shaped prismatic minerals (e.g., prismatic hornblende, tourmaline needles, or stretched quartz rods) parallel to the tectonic transport/stretching axis ($X$-axis of the strain ellipsoid).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What is "metamorphic differentiation" and how does it generate gneissic banding during high-grade thermodynamic metamorphism?</p>
        <p><strong>Solution:</strong>
          <strong>Metamorphic differentiation</strong> is the thermodynamic and chemical segregation of originally homogeneous rock into distinct, alternating mineralogical layers during high-grade metamorphism. Driven by chemical potential gradients under differential stress:
          - Quartz and feldspars selectively migrate via stress-induced diffusion or incipient partial melting into low-stress zones, forming light-colored <strong>felsic bands</strong>.
          - Mafic ferromagnesian minerals (biotite, hornblende, garnet) concentrate along high-stress domains, forming dark <strong>mafic bands</strong>, producing macroscopic gneissic foliation.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Why do pure monomineralic rocks (such as pure quartz sandstone or pure calcite limestone) rarely develop well-defined foliation, even under intense thermodynamic regional metamorphism?</p>
        <p><strong>Solution:</strong>
          Foliation fundamentally requires minerals that possess an <strong>inequant, highly anisotropic crystal habit</strong> (such as platy micas or prismatic amphiboles) that can align in parallel sheets. Pure quartz and calcite crystallize with equant, roughly spherical, isotropic crystal lattices. Under thermodynamic metamorphism, they recrystallize into an interlocking, polygonal equigranular mosaic (granoblastic texture) producing <strong>quartzite</strong> and <strong>marble</strong>, which lack dimensional foliation planes unless deformed into severe quartz ribbon mylonites.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is a "crenulation cleavage" and what tectonic history does it indicate?</p>
        <p><strong>Solution:</strong>
          <strong>Crenulation cleavage</strong> is a secondary tectonic foliation formed when an <strong>earlier, pre-existing foliation ($S_1$)</strong> is micro-folded or wrinkled into millimeter-scale chevron micro-folds during a subsequent, distinct phase of tectonic compression ($D_2$). The parallel alignment of the new micro-fold limbs and axial planes defines the new foliation ($S_2$), proving a complex, <strong>polyphase deformation history</strong> in an orogenic belt.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Explain the geometrical relationship between the orientation of metamorphic foliation planes and the three principal axes of the finite strain ellipsoid ($X \ge Y \ge Z$).</p>
        <p><strong>Solution:</strong>
          In structural geology and strain analysis, metamorphic foliation planes develop parallel to the <strong>$XY$-plane of the finite strain ellipsoid</strong> (the plane of maximum tectonic flattening and extension). The normal (pole) to the foliation plane corresponds exactly to the <strong>$Z$-axis</strong>, representing the direction of maximum finite shortening (perpendicular to maximum compressive stress $\sigma_1$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>How does the presence of pervasive metamorphic foliation affect the engineering stability of high-cut rock slopes in civil engineering?</p>
        <p><strong>Solution:</strong>
          Pervasive foliation introduces <strong>severe mechanical weakness and directional anisotropy</strong> into the rock mass. Shear strength parallel to foliation planes ($\tau_{\parallel}$) is dramatically lower than perpendicular to foliation ($\tau_{\perp}$). If the foliation planes dip toward the excavated slope face at an angle gentler than the cut slope but steeper than the internal friction angle ($\phi < \theta_{bed} < \theta_{slope}$, "daylighting foliation"), it creates an extreme hazard of catastrophic <strong>planar rockslide failure</strong>, requiring heavy prestressed rock anchoring and drainage.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=108,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q108_Foliation_Thermodynamic_Metamorphism_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q108: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q108()
