#!/usr/bin/env python3
"""
Q109 Generator: Barrovian Metamorphic Grades & Garnet-Schist Petrology
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q109():
    title = r"Q109: Metamorphic Petrology: Barrovian Metamorphic Zones & Garnet-Schist Grade | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Barrovian Zones"
    h1_title = "Q109: Barrovian Metamorphic Grades: Relative Thermodynamic Stability & Garnet-Schist"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 109<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 21: Metamorphic Pelites / Barrovian Zones, pp. 425–435; Fig. 21.2); George Barrow (1893, 1912), <em>On the Geology of Lower Deeside and the Southern Highland Border</em>; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 85–90, 184); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: BARROVIAN ZONES AND THE METAMORPHIC GRADE HIERARCHY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Barrovian Metamorphic Hierarchy & George Barrow's Index Minerals</div>
    <div class="card-body">
      <p>
        In metamorphic geology (Winter, 2014, pp. 425–435; Bucher & Grapes, 2011; Bangar, p. 85), the systematic progressive increase in temperature and pressure across an orogenic belt is measured through the classical concept of <strong>metamorphic grade</strong> and <strong>isograds</strong>.
      </p>
      <p>
        In his pioneering studies in the Scottish Highlands (1893, 1912), George Barrow established the world-standard <strong>Barrovian Prograde Metamorphic Sequence</strong> for pelitic (aluminous) rocks, defined by the sequential first appearance (entry isograd) of specific index minerals:
      </p>
      $$\text{Chlorite} \xrightarrow{300^\circ\text{C}} \text{Biotite} \xrightarrow{400^\circ\text{C}} \mathbf{\text{Garnet}} \xrightarrow{500^\circ\text{C}} \text{Staurolite} \xrightarrow{570^\circ\text{C}} \text{Kyanite} \xrightarrow{620^\circ\text{C}} \text{Sillimanite} \xrightarrow{> 680^\circ\text{C}} \text{Anatexis}$$

      <div class="figure-box">
        <img src="../../figures_Q109/winter_p430_barrovian_zones_garnet_schist_grade.png" alt="Barrovian Metamorphic Zones and Garnet Stability from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 109.1 — Barrovian Metamorphic Zones and P-T Trajectories:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 430). Illustrates the progressive entry of Barrovian index minerals, showing the garnet-in isograd marking the critical boundary transition into the amphibolite facies ($T \approx 450\text{--}550^\circ\text{C}$).
        </div>
      </div>

      <h4>Comparison of the Four Candidate Schist Types</h4>
      <p>
        To determine which rock represents the highest metamorphic grade among the options, we evaluate their respective equilibrium crystallization temperatures and metamorphic facies:
      </p>
      <ul>
        <li><strong>Talc-Schist:</strong> Formed by low-temperature hydrothermal alteration or low-grade metamorphism of ultramafic rocks (peridotites/serpentinites) in the presence of $\text{CO}_2$-bearing fluids ($\text{Serpentine} + \text{CO}_2 \rightarrow \text{Talc} + \text{Magnesite} + \text{H}_2\text{O}$). Typically crystallizes under <strong>sub-greenschist to lower-greenschist facies ($T \approx 250\text{--}350^\circ\text{C}$)</strong>.</li>
        <li><strong>Chlorite-Schist:</strong> Represents the <strong>lowest grade</strong> of the Barrovian pelitic/mafic sequence (Chlorite zone, <strong>lower greenschist facies, $T \approx 300\text{--}350^\circ\text{C}$</strong>). Characterized by fine-grained green chlorite flakes, albite, and quartz.</li>
        <li><strong>Mica-Schist (Biotite-Muscovite Schist):</strong> Represents the <strong>intermediate-low grade</strong> (Biotite zone, <strong>middle greenschist facies, $T \approx 350\text{--}420^\circ\text{C}$</strong>), where biotite nucleates via the reaction: $\text{Chlorite} + \text{K-feldspar/Phengite} \rightarrow \text{Biotite} + \text{Muscovite} + \text{Quartz} + \text{H}_2\text{O}$.</li>
        <li><strong>Garnet-Schist:</strong> Represents the <strong>highest grade</strong> among the group, marking the <strong>Garnet Zone</strong>. The crystallization of almandine-rich garnet porphyroblasts ($T \approx 450\text{--}550^\circ\text{C}$) marks the entry into the <strong>amphibolite facies (medium to upper grade)</strong>.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: GARNET ISOGRAD & CRYSTAL CHEMISTRY -->
  <div class="card">
    <div class="card-header bg-emerald">2. The Garnet-In Reaction Kinetics & Porphyroblast Crystallography</div>
    <div class="card-body">
      <h4>Thermodynamic Reaction Governing the Garnet Isograd</h4>
      <p>
        In pelitic rocks, almandine-rich garnet ($\text{Fe}_3\text{Al}_2\text{Si}_3\text{O}_{12}$) forms via prograde dehydration reactions that consume lower-grade chlorite and quartz (Winter, 2014, p. 427):
      </p>
      $$\text{Fe-Chlorite} + \text{Muscovite} + \text{Quartz} \xrightarrow{\sim 450\text{--}500^\circ\text{C}} \mathbf{\text{Almandine Garnet}} + \text{Biotite} + \text{H}_2\text{O}$$
      <p>
        Because this reaction releases bound crystalline water ($\Delta S_{rxn} > 0$), it is driven strongly to the right by increasing temperature, permanently consuming chlorite and crystallizing conspicuous dodecahedral or trapezohedral garnet porphyroblasts.
      </p>

      <h4>Metamorphic Grade Comparison Matrix</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Schist Variety</th>
            <th>Index Mineral</th>
            <th>Equilibrium Temperature ($T$)</th>
            <th>Metamorphic Facies</th>
            <th>Relative Metamorphic Grade</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Talc-Schist</strong></td>
            <td>Talc ($\text{Mg}_3\text{Si}_4\text{O}_{10}(\text{OH})_2$)</td>
            <td>$250\text{ to } 350^\circ\text{C}$</td>
            <td>Sub-greenschist to Lower Greenschist</td>
            <td>Low Grade</td>
          </tr>
          <tr>
            <td><strong>Chlorite-Schist</strong></td>
            <td>Chlorite</td>
            <td>$300\text{ to } 350^\circ\text{C}$</td>
            <td>Lower Greenschist Facies</td>
            <td>Low Grade</td>
          </tr>
          <tr>
            <td><strong>Mica-Schist</strong></td>
            <td>Biotite + Muscovite</td>
            <td>$350\text{ to } 420^\circ\text{C}$</td>
            <td>Middle to Upper Greenschist Facies</td>
            <td>Low-Medium Grade</td>
          </tr>
          <tr>
            <td><strong>Garnet-Schist</strong></td>
            <td><strong>Almandine Garnet</strong></td>
            <td><strong>$450\text{ to } 550^\circ\text{C}$</strong></td>
            <td><strong>Epidote-Amphibolite to Amphibolite</strong></td>
            <td><strong>Highest Grade (Medium-High)</strong></td>
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
        <strong>Question 109:</strong> Amongst the following which is the highest grade of metamorphic rock ?
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Talc-schist</div>
        <div class="option-item correct-option"><strong>(B)</strong> Garnet-schist</div>
        <div class="option-item"><strong>(C)</strong> Mica-schist</div>
        <div class="option-item"><strong>(D)</strong> Chlorite-schist</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) Garnet-schist</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Talc-Schist</div>
        <p>
          <strong>Incorrect:</strong> <strong>Talc-schist</strong> is a hydrous magnesium silicate rock ($\text{Mg}_3\text{Si}_4\text{O}_{10}(\text{OH})_2$) formed primarily by the low-temperature hydrothermal alteration or low-grade metamorphism of ultramafic serpentinites under temperatures of only $250\text{--}350^\circ\text{C}$ (sub-greenschist to lower greenschist facies). Under higher metamorphic temperatures ($> 500^\circ\text{C}$), talc breaks down and is replaced by anthophyllite or enstatite. It is therefore a low-grade rock.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — Garnet-Schist</div>
        <p>
          <strong>Correct:</strong> In the classic Barrovian progressive metamorphic sequence (Winter, 2014, p. 425; Bangar, p. 85), the appearance of almandine garnet porphyroblasts defines the <strong>Garnet Zone</strong>, which requires temperatures of <strong>$450\text{--}550^\circ\text{C}$</strong> and pressures of $4\text{--}7\text{ kbar}$, marking the transitional boundary into the <strong>Amphibolite facies</strong>. Because this temperature significantly exceeds that required for chlorite-schist ($300^\circ\text{C}$), talc-schist ($300^\circ\text{C}$), and biotite mica-schist ($400^\circ\text{C}$), <strong>Garnet-schist is unequivocally the highest grade of metamorphic rock</strong> among the choices.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Mica-Schist</div>
        <p>
          <strong>Incorrect:</strong> A standard <strong>mica-schist</strong> (composed of biotite, muscovite, and quartz without garnet) crystallizes in the <strong>Biotite Zone</strong> of the middle-to-upper greenschist facies at temperatures around $350\text{--}420^\circ\text{C}$. This is lower in thermal grade than the garnet-in isograd ($450\text{--}550^\circ\text{C}$); when the metamorphic grade increases beyond $450^\circ\text{C}$, the mica-schist transforms into a garnet-mica schist.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Chlorite-Schist</div>
        <p>
          <strong>Incorrect:</strong> <strong>Chlorite-schist</strong> represents the <strong>lowest grade</strong> of regional metamorphism among schists (Chlorite Zone, lower greenschist facies, $T \approx 300\text{--}350^\circ\text{C}$). Chlorite is chemically destroyed by dehydration reactions as temperatures rise toward the garnet isograd.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Ranking of Barrovian Metamorphic Zones & Mineral Stability</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Barrovian Zone</th>
            <th>Primary Index Mineral</th>
            <th>Metamorphic Facies</th>
            <th>Typical Temperature ($T$)</th>
            <th>Typical Pressure ($P$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Chlorite Zone</strong></td>
            <td>Chlorite (in Chlorite-schist)</td>
            <td>Lower Greenschist</td>
            <td>$300\text{ to } 350^\circ\text{C}$</td>
            <td>$2\text{ to } 4\text{ kbar}$</td>
          </tr>
          <tr>
            <td><strong>Biotite Zone</strong></td>
            <td>Biotite (in Mica-schist)</td>
            <td>Middle Greenschist</td>
            <td>$350\text{ to } 420^\circ\text{C}$</td>
            <td>$3\text{ to } 5\text{ kbar}$</td>
          </tr>
          <tr>
            <td><strong>Garnet Zone</strong></td>
            <td><strong>Almandine Garnet (in Garnet-schist)</strong></td>
            <td><strong>Epidote-Amphibolite / Lower Amphibolite</strong></td>
            <td><strong>$450\text{ to } 550^\circ\text{C}$</strong></td>
            <td><strong>$4\text{ to } 7\text{ kbar}$</strong></td>
          </tr>
          <tr>
            <td><strong>Staurolite Zone</strong></td>
            <td>Staurolite</td>
            <td>Middle Amphibolite</td>
            <td>$550\text{ to } 600^\circ\text{C}$</td>
            <td>$5\text{ to } 8\text{ kbar}$</td>
          </tr>
          <tr>
            <td><strong>Kyanite Zone</strong></td>
            <td>Kyanite</td>
            <td>Upper Amphibolite</td>
            <td>$600\text{ to } 650^\circ\text{C}$</td>
            <td>$6\text{ to } 9\text{ kbar}$</td>
          </tr>
          <tr>
            <td><strong>Sillimanite Zone</strong></td>
            <td>Sillimanite</td>
            <td>Upper Amphibolite to Granulite</td>
            <td>$650\text{ to } 750+^\circ\text{C}$</td>
            <td>$5\text{ to } 10\text{ kbar}$</td>
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
        <p>In a prograde Barrovian metamorphic terrane, a field geologist traverses from a zone of chlorite-muscovite schist to a zone containing porphyroblasts of almandine garnet. Write the generalized chemical dehydration reaction that marks this isograd and explain why it is endothermic.</p>
        <p><strong>Solution:</strong>
          The generalized garnet-in reaction is:
          $$\text{Chlorite} + \text{Muscovite} + \text{Quartz} \rightarrow \text{Almandine Garnet} + \text{Biotite} + \text{H}_2\text{O}$$
          This reaction is <strong>endothermic ($\Delta H > 0$)</strong> because breaking the strong chemical bonds holding hydrous sheet silicates together requires the absorption of thermal energy. Furthermore, the generation of a free, high-entropy fluid phase ($\text{H}_2\text{O}$) causes a large positive entropy change ($\Delta S > 0$). According to $\Delta G = \Delta H - T\Delta S$, the Gibbs free energy becomes increasingly negative ($G < 0$) as temperature $T$ rises, driving the spontaneous crystallization of garnet at $T \approx 450\text{--}500^\circ\text{C}$.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Under an electron microprobe (EPMA), a prograde garnet porphyroblast from a garnet-schist exhibits compositional chemical zoning. How do the concentrations of manganese (spessartine, $\text{Mn}$) and iron/magnesium (almandine/pyrope, $\text{Fe/Mg}$) vary from the core to the rim of the crystal?</p>
        <p><strong>Solution:</strong>
          Prograde Barrovian garnets exhibit characteristic <strong>Rayleigh fractionation bell-shaped growth zoning</strong>:
          - <strong>Core:</strong> Strongly enriched in <strong>Manganese ($\text{MnO}$, Spessartine component)</strong> and Calcium (Grossular). Because garnet preferentially fractionates $\text{Mn}^{2+}$ into its dodecahedral site over $\text{Fe}^{2+}$/$\text{Mg}^{2+}$ at low temperatures, the early-nucleated core absorbs virtually all available manganese from the rock matrix.
          - <strong>Rim:</strong> Strongly depleted in Manganese ($\text{Mn} \rightarrow 0$) and progressively enriched in <strong>Iron ($\text{FeO}$, Almandine) and Magnesium ($\text{MgO}$, Pyrope)</strong> as metamorphic temperature ascends toward peak conditions.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Why is talc-schist extraordinarily soft (Mohs hardness = 1.0) and slippery, and what engineering hazard does it pose when encountered in underground tunneling?</p>
        <p><strong>Solution:</strong>
          Talc ($\text{Mg}_3\text{Si}_4\text{O}_{10}(\text{OH})_2$) is a trioctahedral phyllosilicate whose composite sheets are completely neutral with zero interlayer cations. The adjacent composite layers are held together solely by <strong>exceptionally weak van der Waals forces</strong>, allowing planes to shear across each other effortlessly, giving talc a Mohs hardness of $1.0$ and a greasy feel. When encountered in a tunnel excavation, talc-schist behaves as an ultra-weak, low-friction shear zone ($\phi' < 15^\circ$) that deforms via rapid squeezing and plastic creep, generating enormous, uniform rock pressures that crush standard tunnel steel ribs.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Explain the structural significance of "snowball" (rotated) garnet porphyroblasts with sigmoidal quartz inclusion trails ($\text{S}_i$) in a garnet-schist.</p>
        <p><strong>Solution:</strong>
          "Snowball garnets" are syn-kinematic porphyroblasts that grew <strong>contemporaneously with non-coaxial ductile shear strain</strong>. As the garnet crystal grew, it enveloped microscopic external matrix grains (quartz, graphite) along the foliation plane ($\text{S}_e$). Simultaneous tectonic shearing rotated the rigid garnet crystal like a ball bearing, twisting the internal inclusion trails into a continuous, elegant <strong>sigmoidal or spiral geometry ($\text{S}_i$)</strong>, providing a quantitative record of rotational shear sense and total shear strain ($\gamma$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>What is the difference between a "Barrovian" metamorphic facies series and a "Buchan" (Abukuma) facies series?</p>
        <p><strong>Solution:</strong>
          - <strong>Barrovian Facies Series:</strong> Represents a <strong>medium-pressure (moderate geothermal gradient, $\sim 20\text{--}30^\circ\text{C/km}$)</strong> metamorphic regime characteristic of continent-continent collision belts; characterized by the index sequence: Chlorite $\rightarrow$ Biotite $\rightarrow$ Garnet $\rightarrow$ Staurolite $\rightarrow$ <strong>Kyanite</strong> $\rightarrow$ Sillimanite.
          - <strong>Buchan / Abukuma Series:</strong> Represents a <strong>low-pressure / high-temperature (elevated geothermal gradient, $> 40\text{--}60^\circ\text{C/km}$)</strong> regime associated with magmatic arcs; characterized by low-pressure minerals like <strong>Andalusite and Cordierite</strong> rather than staurolite and kyanite.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Calculate the depth of burial corresponding to the garnet-in isograd assuming a lithostatic pressure of $5.5\text{ kbar}$ and an average continental crustal density of $2750\text{ kg/m}^3$.</p>
        <p><strong>Solution:</strong>
          The lithostatic pressure formula is:
          $$P = \rho g z \implies z = \frac{P}{\rho g}$$
          Given:
          - $P = 5.5\text{ kbar} = 5.5 \times 10^8\text{ Pa}$
          - $\rho = 2750\text{ kg/m}^3$
          - $g = 9.81\text{ m/s}^2$
          $$z = \frac{5.5 \times 10^8\text{ N/m}^2}{2750\text{ kg/m}^3 \times 9.81\text{ m/s}^2} = \frac{5.5 \times 10^8}{26977.5} \approx 20,387\text{ meters} \approx \mathbf{20.4\text{ km}}$$
          The garnet-in isograd was achieved at approximately $20.4\text{ km}$ depth in the orogenic crust.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Why does chlorite disappear in pelitic schists once metamorphic temperatures exceed $550^\circ\text{C}$?</p>
        <p><strong>Solution:</strong>
          Chlorite is a hydrous mineral containing approximately $12\text{ to } 14\text{ wt}\%\text{ H}_2\text{O}$ bound in its octahedral brucite-like interlayers. At temperatures above $\sim 500\text{--}550^\circ\text{C}$, the crystal lattice cannot thermodynamically retain its structural hydroxyl $(\text{OH}^-)$ groups. Chlorite undergoes continuous and terminal dehydration breakdown reactions with quartz and muscovite to form anhydrous garnet, staurolite, and biotite, completely exhausting chlorite in pelites.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>How does the Garnet-Biotite (GARB) geothermometer calculate peak metamorphic temperatures in a garnet-mica schist?</p>
        <p><strong>Solution:</strong>
          The GARB geothermometer (Ferry & Spear, 1978) utilizes the temperature-dependent exchange of $\text{Fe}^{2+}$ and $\text{Mg}^{2+}$ between coexisting garnet and biotite:
          $$\text{Almandine (Garnet)} + \text{Phlogopite (Biotite)} \rightleftharpoons \text{Pyrope (Garnet)} + \text{Annite (Biotite)}$$
          The distribution coefficient $K_D = \frac{(\text{Mg}/\text{Fe})_{\text{garnet}}}{(\text{Mg}/\text{Fe})_{\text{biotite}}}$ is calibrated as a function of temperature via:
          $$\ln K_D = -\frac{\Delta H^\circ}{RT} + \frac{\Delta S^\circ}{R}$$
          Measuring the $\text{Fe/Mg}$ ratios of adjacent garnet rim and biotite touching edges via electron microprobe allows the precise calculation of peak metamorphic equilibration temperatures ($T \pm 25^\circ\text{C}$).
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=109,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q109_Barrovian_Metamorphic_Grades_Garnet_Schist_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q109: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q109()
