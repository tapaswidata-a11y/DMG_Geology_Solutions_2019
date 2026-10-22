#!/usr/bin/env python3
"""
Q110 Generator: Low-Grade Schists & Regional Metamorphism Conditions
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q110():
    title = r"Q110: Metamorphic Petrology: Low-Grade Schists & Regional Metamorphism | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Facies"
    h1_title = "Q110: Low-Grade Schists: Genesis under Low Temperature & Regional (Dynamothermal) Metamorphism"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 110<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 25: Metamorphic Facies / Greenschist Facies, pp. 485–505; Fig. 25.4); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 82–86, 182); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 128–132); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND METAMORPHIC CONDITIONS OF LOW-GRADE SCHISTS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Temperature-Pressure Window & Regional Tectonic Framework</div>
    <div class="card-body">
      <p>
        In metamorphic geology (Winter, 2014, pp. 485–505; Bangar, p. 82; Mahapatra, p. 128), a <strong>schist</strong> is defined as a medium- to coarse-grained foliated metamorphic rock characterized by <strong>schistosity</strong>—a pervasive planar fabric produced by the parallel crystallographic and dimensional alignment of platy sheet silicates (micas, chlorite, talc) or needle-like prismatic minerals (actinolite, tremolite) large enough to be clearly discerned with the unaided eye.
      </p>
      <p>
        A <strong>low-grade schist</strong> (exemplified by chlorite-schist, talc-schist, actinolite-schist, and sericite-schist) forms under a precise combination of thermodynamic and geotectonic conditions:
      </p>
      <ol>
        <li><strong>Low Temperature ($T \approx 300^\circ\text{C}$ to $450^\circ\text{C}$):</strong> Corresponds to the classic <strong>Greenschist Facies</strong> of metamorphic petrology. At these moderate-to-low temperatures, hydrous phyllosilicate minerals remain stable and do not dehydrate into anhydrous medium- or high-grade minerals (such as staurolite, kyanite, or sillimanite).</li>
        <li><strong>Regional (Dynamothermal) Metamorphism:</strong> Operates across gigantic spatial scales (hundreds to thousands of kilometers) in convergent tectonic regimes (orogenic mountain belts, subduction accretionary prisms). Crucially, regional metamorphism supplies the <strong>pervasive, directed differential tectonic stress ($\sigma_1 > \sigma_3$)</strong> required to force growing mineral plates into parallel alignment, generating true macroscopic schistosity.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q110/winter_p490_greenschist_low_temp_regional.png" alt="Greenschist Facies P-T Domain from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 110.1 — Greenschist Facies P-T Field and Mineral Stability:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 490). Highlights the greenschist facies domain under low temperatures ($300\text{--}450^\circ\text{C}$) and moderate-to-high regional pressures, characterizing low-grade schistose terranes.
        </div>
      </div>

      <h4>Why "Local Metamorphism" Cannot Form Low-Grade Schists</h4>
      <p>
        <strong>Local metamorphism</strong> (predominantly thermal or contact metamorphism occurring in narrow aureoles adjacent to igneous intrusions) operates under <strong>hydrostatic (isotropic, non-directed) stress</strong>:
      </p>
      <ul>
        <li>Without regional directed compressive stress ($\sigma_1 \gg \sigma_3$), platy minerals nucleate and grow with random, unoriented crystallographic axes.</li>
        <li>This yields non-foliated, dense, interlocking rocks termed <strong>hornfelses</strong> (or granofelses), which completely lack schistosity.</li>
        <li>Therefore, schistosity is structurally impossible under purely local/contact metamorphic regimes.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: MINERALOGY & GEOCHEMICAL REACTIONS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Mineralogical Paragenesis of Low-Grade Schists in the Greenschist Facies</div>
    <div class="card-body">
      <h4>Diagnostic Mineral Assemblages across Protoliths</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Protolith Chemistry</th>
            <th>Low-Grade Schist Variety</th>
            <th>Diagnostic Greenschist Mineral Assemblage</th>
            <th>Equilibrium P-T Range</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Basic / Mafic (Basalt / Dolerite)</strong></td>
            <td><strong>Greenschist / Chlorite-Schist</strong></td>
            <td>Chlorite + Actinolite + Epidote + Albite ($\text{An}_{0\text{--}7}$) $\pm$ Quartz $\pm$ Calcite</td>
            <td>$300\text{--}450^\circ\text{C}$, $2\text{--}7\text{ kbar}$</td>
          </tr>
          <tr>
            <td><strong>Pelitic (Shale / Mudstone)</strong></td>
            <td><strong>Chlorite-Muscovite Schist</strong></td>
            <td>Chlorite + Muscovite (phengite) + Quartz + Albite $\pm$ Paragonite</td>
            <td>$300\text{--}400^\circ\text{C}$, $2\text{--}6\text{ kbar}$</td>
          </tr>
          <tr>
            <td><strong>Ultramafic (Peridotite / Serpentinite)</strong></td>
            <td><strong>Talc-Schist / Tremolite-Schist</strong></td>
            <td>Talc + Magnesite + Tremolite + Chlorite $\pm$ Antigorite</td>
            <td>$250\text{--}400^\circ\text{C}$, $2\text{--}5\text{ kbar}$</td>
          </tr>
        </tbody>
      </table>

      <h4>The Defining Basal Reaction: Prehnite-Pumpellyite to Greenschist Transition</h4>
      <p>
        The definitive entry into the low-grade greenschist facies in mafic rocks is marked by the breakdown of pumpellyite in the presence of quartz and chlorite to form actinolite and epidote:
      </p>
      $$\text{Pumpellyite} + \text{Chlorite} + \text{Quartz} \xrightarrow{\sim 300^\circ\text{C}} \text{Actinolite} + \text{Clinozoisite/Epidote} + \text{H}_2\text{O}$$
      <p>
        Plagioclase in this low-grade regime is strictly pure <strong>albite ($\text{An}_{< 7}$)</strong> because the calcic anorthite component cannot enter the feldspar lattice at low temperatures and is sequestered into epidote (the "peristerite solvus" gap).
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
        <strong>Question 110:</strong> Low grade schist is formed under which metamorphic conditions ?
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> High temperature and local metamorphism</div>
        <div class="option-item correct-option"><strong>(B)</strong> Low temperature and regional metamorphism</div>
        <div class="option-item"><strong>(C)</strong> Low temperature and local metamorphism</div>
        <div class="option-item"><strong>(D)</strong> All of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) Low temperature and regional metamorphism</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — High Temperature & Local Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> Both parameters in this option are incorrect:
          (1) "High temperature" produces high-grade rocks (amphibolite, granulite, or pyroxene-hornfels facies), not low-grade schists.
          (2) "Local metamorphism" (contact aureoles) operates under static, non-directed stress, producing unfoliated <strong>pyroxene-hornfels or sanidinite facies rocks</strong>, which are devoid of planar schistosity.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — Low Temperature & Regional Metamorphism</div>
        <p>
          <strong>Correct:</strong> By universal definition in metamorphic petrology (Winter, 2014, p. 485; Bangar, p. 82; Bucher & Grapes, 2011), <strong>low-grade schists</strong> (such as chlorite-schist, talc-schist, and actinolite-schist) develop under <strong>low temperatures ($300\text{--}450^\circ\text{C}$)</strong> characteristic of the greenschist facies, coupled with pervasive <strong>regional (dynamothermal) metamorphism</strong> across active orogenic belts, which provides the directed differential tectonic stress ($\sigma_1 > \sigma_3$) required to generate penetrative schistosity.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Low Temperature & Local Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> Low temperature occurring in a <em>local</em> setting (e.g., the outermost, low-temperature margin of a contact metamorphic aureole) produces non-foliated <strong>spotted slates or albite-epidote hornfelses</strong>. Because local metamorphism lacks the regional tectonic deviatoric stress field needed to rotate and align micas, it cannot produce a schist.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — All of These</div>
        <p>
          <strong>Incorrect:</strong> Because Options (A) and (C) contradict the fundamental physical and tectonic requirements for schistosity, Option (D) is entirely invalid. The verified, incontrovertible answer is <strong>(B)</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Matrix: Regional vs. Local Metamorphic Facies & Textural Expressions</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Facies</th>
            <th>Metamorphic Type</th>
            <th>Temperature Range</th>
            <th>Pressure / Stress State</th>
            <th>Characteristic Textures & Rocks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Greenschist Facies</strong></td>
            <td><strong>Regional (Dynamothermal)</strong></td>
            <td><strong>$300\text{ to } 450^\circ\text{C}$ (Low $T$)</strong></td>
            <td><strong>Directed Differential Stress ($\sigma_1 > \sigma_3$)</strong></td>
            <td><strong>Pervasive schistosity; Chlorite-schist, Talc-schist, Greenschist</strong></td>
          </tr>
          <tr>
            <td><strong>Amphibolite Facies</strong></td>
            <td>Regional (Dynamothermal)</td>
            <td>$450\text{ to } 650^\circ\text{C}$ (Medium to High $T$)</td>
            <td>Directed Differential Stress ($\sigma_1 > \sigma_3$)</td>
            <td>Coarse schistosity, gneissic banding; Garnet-mica schist, Amphibolite</td>
          </tr>
          <tr>
            <td><strong>Albite-Epidote Hornfels</strong></td>
            <td>Local (Contact / Thermal)</td>
            <td>$300\text{ to } 450^\circ\text{C}$ (Low $T$)</td>
            <td>Hydrostatic / Isotropic ($\sigma_1 \approx \sigma_2 \approx \sigma_3$)</td>
            <td>Non-foliated; fine granoblastic, decussate hornfels; Spotted slates</td>
          </tr>
          <tr>
            <td><strong>Hornblende Hornfels</strong></td>
            <td>Local (Contact / Thermal)</td>
            <td>$450\text{ to } 600^\circ\text{C}$ (Moderate $T$)</td>
            <td>Hydrostatic / Isotropic ($\sigma_1 \approx \sigma_2 \approx \sigma_3$)</td>
            <td>Tough, massive, unfoliated granoblastic hornfelses</td>
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
        <p>A regional metamorphic belt of mafic green rocks contains the equilibrium assemblage: Chlorite + Actinolite + Epidote + Albite + Quartz. Identify the metamorphic facies, deduce the temperature range, and explain why plagioclase in this assemblage contains zero anorthite component.</p>
        <p><strong>Solution:</strong>
          - <strong>Metamorphic Facies:</strong> <strong>Greenschist Facies</strong> (low-grade regional metamorphism).
          - <strong>Temperature Range:</strong> Approximately <strong>$300^\circ\text{C}$ to $450^\circ\text{C}$</strong>.
          - <strong>Albite Purity:</strong> At temperatures below $\sim 450^\circ\text{C}$, the wide miscibility gap between albite ($\text{NaAlSi}_3\text{O}_8$) and oligoclase/andesine (the <em>peristerite gap</em>) makes calcic plagioclase thermodynamically unstable. All available calcium ($\text{Ca}^{2+}$) is sequestered into the epidote-clinozoisite lattice ($\text{Ca}_2\text{Al}_3\text{Si}_3\text{O}_{12}(\text{OH})$), leaving plagioclase as pure, stoichiometric albite ($\text{An}_{0\text{--}5}$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Why does a rock with the exact same chemical composition as a chlorite-schist crystallize as an unfoliated hornfels when subjected to the same temperature in a contact aureole?</p>
        <p><strong>Solution:</strong>
          Mineral alignment (schistosity) is not governed by chemical composition or temperature alone; it requires a <strong>deviatoric (non-hydrostatic) stress field</strong>. In regional metamorphism, tectonic plate collision imposes strong directed compressive stress ($\sigma_1 \gg \sigma_3$), forcing growing phyllosilicate flakes into parallel planes. In a contact metamorphic aureole, the stress field is <strong>hydrostatic (isotropic, $\sigma_1 = \sigma_2 = \sigma_3$)</strong>; without directed stress, chlorite crystals nucleate and grow with random, interlocking, decussate orientations, producing a massive, non-foliated hornfels.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>In a low-grade actinolite-schist, how is actinolite distinguished optically from hornblende under a polarizing petrographic microscope?</p>
        <p><strong>Solution:</strong>
          - <strong>Actinolite (Low-Grade Greenschist):</strong> Monoclinic inosilicate; pale green to yellow-green pleochroism, prismatic or acicular/fibrous habit, moderate extinction angle ($Z \wedge c = 11\text{--}15^\circ$), and relatively low birefringence.
          - <strong>Hornblende (Medium-Grade Amphibolite):</strong> Strongly pleochroic in vivid deep greens, bluish-greens, or brownish-greens, stout prismatic crystals, higher extinction angle ($Z \wedge c = 15\text{--}25^\circ$), reflecting substantial octahedral $\text{Al}^{3+}$ and tetrahedral $\text{Al/Si}$ substitution occurring only at $T > 450\text{--}500^\circ\text{C}$.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Write the chemical reaction that converts a low-grade ultramafic serpentinite into a talc-schist in the presence of hydrothermal $\text{CO}_2$ fluids.</p>
        <p><strong>Solution:</strong>
          The carbonation reaction of serpentine (antigorite/lizardite) at $T \approx 300\text{--}350^\circ\text{C}$ is:
          $$2\text{Mg}_3\text{Si}_2\text{O}_5(\text{OH})_4\text{ (serpentine)} + 3\text{CO}_2 \rightarrow \text{Mg}_3\text{Si}_4\text{O}_{10}(\text{OH})_2\text{ (talc)} + 3\text{MgCO}_3\text{ (magnesite)} + 3\text{H}_2\text{O}$$
          Under regional tectonic shear, the newly crystallized talc flakes align into dense, slippery foliation planes, forming a <strong>talc-carbonate schist (soapstone)</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>What is the "pumpellyite-actinolite facies" and where does it plot relative to the greenschist and blueschist facies in $P\text{-}T$ space?</p>
        <p><strong>Solution:</strong>
          The <strong>pumpellyite-actinolite facies</strong> (Hashimoto, 1966) occupies a transitional $P\text{-}T$ field ($T \approx 250\text{--}350^\circ\text{C}$, $P \approx 3\text{--}7\text{ kbar}$) representing a <strong>medium-to-high pressure / low-temperature</strong> regime intermediate between the low-pressure greenschist facies and the ultra-high-pressure blueschist facies, typical of subduction accretionary prisms.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Why do greenstone belts in Archean cratons (e.g., the Dharwar Craton in India) consist predominantly of low-grade schists?</p>
        <p><strong>Solution:</strong>
          Archean greenstone belts represent volcano-sedimentary sequences (komatiites, tholeiitic basalts, banded iron formations, turbidites) deposited in ancient oceanic/back-arc basins that were subsequently caught between coalescing granitic-gneissic micro-continents. During regional orogenic shortening and thermal equilibration, the volcano-sedimentary rocks were metamorphosed under <strong>greenschist facies conditions (low temperature $300\text{--}450^\circ\text{C}$, regional stress)</strong>, preserving their hydrated hydrous minerals (chlorite, actinolite, epidote) as pervasive greenstone schists.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is "retrograde metamorphism" and how can it convert a high-grade amphibolite into a low-grade chlorite-schist?</p>
        <p><strong>Solution:</strong>
          <strong>Retrograde metamorphism</strong> is the mineralogical re-equilibration of a high-grade metamorphic rock as it cools and decompresses during exhumation. If abundant aqueous fluids ($\text{H}_2\text{O}$) infiltrate the cooling rock along ductile shear zones at $T \approx 300\text{--}400^\circ\text{C}$, high-temperature hornblende and plagioclase hydrate and decompose back to low-grade chlorite, actinolite, albite, and epidote, transforming an amphibolite into a retrograde <strong>chlorite-schist mylonite</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Explain how the Point Load Strength Index ($I_s$) of a chlorite-schist varies when load is applied perpendicular vs. parallel to schistosity planes.</p>
        <p><strong>Solution:</strong>
          Because of the near-perfect parallel alignment of ultra-weak, basal-cleaved chlorite flakes, a chlorite-schist exhibits <strong>extreme strength anisotropy ($I_a > 3.0\text{ to } 5.0$)</strong>:
          - Loaded <strong>perpendicular to schistosity ($\perp$)</strong>: Grain contacts are compressed together, yielding a high point load index ($I_s \approx 3\text{--}5\text{ MPa}$).
          - Loaded <strong>parallel to schistosity ($\parallel$)</strong>: Tensile splitting initiates along the low-friction basal cleavage planes, causing splitting failure at exceptionally low values ($I_s \approx 0.5\text{--}1.0\text{ MPa}$), presenting severe slope stability risks.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=110,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q110_Greenschist_Low_Temperature_Regional_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q110: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q110()
