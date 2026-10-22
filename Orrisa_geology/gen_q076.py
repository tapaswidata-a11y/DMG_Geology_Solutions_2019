#!/usr/bin/env python3
"""
Q076 Generator: Primary Magma Generation Controls & Mantle Melting
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q076():
    title = r"Q076: Igneous Petrology: Controls on Primary Magma Generation & Mantle Melting | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Magma Genesis"
    h1_title = "Q076: Parameters Controlling the Composition of Primary Magma"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 76<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 10: Mantle Melting and Generation of Basaltic Magma, pp. 191–214); Anthony Hall, <em>Igneous Petrology</em> (Longman, Ch. 8); Myron G. Best, <em>Igneous and Metamorphic Petrology</em> (2nd Ed., Blackwell, Ch. 12); G.B. Mahapatra, <em>A Text-Book of Geology</em>."""

    part1 = r"""
  <!-- CARD 1: FUNDAMENTAL CONTROLS ON PRIMARY MAGMA COMPOSITION -->
  <div class="card">
    <div class="card-header bg-blue">1. Thermodynamics & Parameters of Primary Magma Generation</div>
    <div class="card-body">
      <p>
        A <strong>primary magma</strong> is defined as a pristine melt generated directly by the partial melting of a deep mantle or crustal source rock, which has reached the surface or emplaced in the crust without having undergone subsequent fractional crystallization, crustal assimilation, or magma mixing.
      </p>
      <p>
        The definitive thermodynamic and geochemical composition of any primary magma is rigorously governed by <strong>four interdependent physicochemical variables</strong> (Winter, 2014, p. 205):
      </p>

      <div class="figure-box">
        <img src="../../figures_Q76/winter_p205_primary_magma_melting.png" alt="Primary Magma Generation Controls and Mantle Melting Phase Relations from Winter">
        <div class="figure-caption">
          <strong>Figure 76.1 — Mantle Melting Geotherms, Phase Equilibria, and Primary Basaltic Magmas:</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 10). Demonstrating how variations in source composition, volatile fugacity ($H_2O, CO_2$), pressure ($P$), and degree of partial melting ($F$) dictate the primary magma composition.
        </div>
      </div>

      <h4>The Four Master Parameters Governing Primary Melt Chemistry</h4>
      <ol>
        <li><strong>(i) Composition of the Source Material:</strong>
          The bulk chemical and mineralogical composition of the mantle or crustal protolith sets the elemental and isotopic baseline. For instance, melting of fertile <em>lherzolite</em> ($Ol + Opx + Cpx + \text{Al-phase}$) yields basaltic liquids, whereas melting of depleted <em>harzburgite</em> ($Ol + Opx$) produces silica-rich, refractory boninites. Metasomatized mantle enriched in incompatible elements generates alkaline suites.
        </li>
        <li><strong>(ii) Relative Concentrations of Volatiles ($H_2O$, $CO_2$):</strong>
          Dissolved volatiles fundamentally alter liquidus/solidus phase boundaries and silica activity:
          <ul>
            <li><strong>Water ($H_2O$):</strong> Expands the stability field of olivine relative to orthopyroxene via incongruent melting ($\text{Enstatite} + \text{Liquid} \rightleftharpoons \text{Forsterite} + \text{Liquid}$), shifting primary melts toward <strong>silica-saturation and oversaturation</strong> (quartz-normative tholeiites and calc-alkaline andesites).</li>
            <li><strong>Carbon Dioxide ($CO_2$):</strong> Depresses silica activity by stabilizing orthopyroxene over olivine and promotes carbonate complexing ($\text{CO}_3^{2-}$), shifting cotectics toward extreme <strong>silica-undersaturation</strong>, generating primary nephelinites, melilitites, basanites, and carbonatites.</li>
          </ul>
        </li>
        <li><strong>(iii) Confining Pressure ($P$ / Depth of Melting):</strong>
          With increasing confining pressure, the eutectic/cotectic minima in basaltic systems shift systematically toward the nepheline/olivine-rich apex:
          <ul>
            <li><em>Shallow Depths ($P < 1.0\text{ GPa}, < 30\text{ km}$):</em> High silica activity, yielding primary quartz-normative tholeiitic basalts.</li>
            <li><em>Intermediate Depths ($1.0\text{--}2.5\text{ GPa}, 30\text{--}75\text{ km}$):</em> Transitional to olivine-tholeiitic and alkali olivine basalts.</li>
            <li><em>Deep Mantle ($P > 2.5\text{--}3.0\text{ GPa}, > 80\text{--}100\text{ km}$):</em> Extremely silica-undersaturated liquids (basanites, melilitites, kimberlitic melts).</li>
          </ul>
        </li>
        <li><strong>(iv) Degree of Partial Melting ($F$):</strong>
          The mass fraction of melt generated ($F$) strictly governs major and trace element concentrations according to the batch melting equation. Incompatible elements ($D \ll 1$) and volatile-loving alkalis are concentrated at low degrees of melting ($F < 5\%$, generating alkali basalts and nephelinites), whereas high degrees of melting ($F = 15\text{--}25\%$) dilute incompatible elements to generate Mid-Ocean Ridge Basalts (N-MORB). Ultra-high degrees of melting ($F > 30\text{--}40\%$) dissolve refractory olivine and enstatite, yielding Archean <strong>komatiites</strong> ($MgO > 18\text{--}30\text{ wt}\%$).
        </li>
      </ol>
    </div>
  </div>

  <!-- CARD 2: BATCH AND FRACTIONAL MELTING MATHEMATICS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Quantitative Melting Models: Batch vs. Fractional Melting</div>
    <div class="card-body">
      <p>
        The geochemical evolution of a primary magma as a function of the degree of partial melting ($F$) is mathematically described by two end-member models established by D.M. Shaw (1970):
      </p>

      <div class="formula-box">
        <strong>1. Equilibrium (Batch) Melting Equation:</strong><br>
        $$\frac{C_L}{C_0} = \frac{1}{D_0 + F(1 - D_0)}$$<br>
        where $C_L$ is trace element concentration in the primary melt, $C_0$ is source concentration, $F$ is melt fraction ($0 \le F \le 1$), and $D_0$ is bulk distribution coefficient ($\sum X_i K_{d,i}$).
      </div>

      <div class="formula-box">
        <strong>2. Fractional (Rayleigh) Melting Equation:</strong><br>
        $$\frac{C_L}{C_0} = \frac{1}{D_0} (1 - F)^{\frac{1}{D_0} - 1}$$
      </div>

      <h4>Behavior of Highly Incompatible Elements ($D_0 \to 0$)</h4>
      <p>
        For elements such as $Rb, Ba, Th, U, Nb$, where $D_0 \approx 0$, the batch melting equation simplifies directly to:
      </p>
      $$\frac{C_L}{C_0} \approx \frac{1}{F}$$
      <p>
        This fundamental inverse relationship demonstrates that at $F = 2\%$ ($0.02$), incompatible elements are enriched <strong>50-fold</strong> in the primary magma relative to the mantle source. At $F = 20\%$ ($0.20$), the enrichment factor drops to only <strong>5-fold</strong>.
      </p>
    </div>
  </div>

  <!-- CARD 3: PETROLOGIC DISCRIMINATION OF PRIMARY VS. DERIVATIVE MAGMAS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Petrologic Diagnostic Criteria for True Primary Mantle Magmas</div>
    <div class="card-body">
      <p>
        Because magmas inevitably cool and differentiate during ascent through the lithosphere, true primary magmas are rare in the geological record. Igneous petrologists apply strict geochemical filters to verify primary status:
      </p>
      <ul>
        <li><strong>Mg-Number ($Mg\#$):</strong> Defined as $\text{Mg}\# = \frac{\text{Mg}^{2+}}{\text{Mg}^{2+} + \text{Fe}^{2+}} \times 100$ (in molar units). Melts in thermodynamic equilibrium with mantle peridotitic olivine ($\text{Fo}_{89\text{--}92}$) using Roeder & Emslie's (1970) exchange partition coefficient $K_{D(\text{Fe-Mg})}^{\text{ol-liq}} = 0.30 \pm 0.03$ must possess:
          $$\mathbf{Mg\# = 68\text{ to } 75}$$
        </li>
        <li><strong>High Compatible Transition Elements:</strong> High concentrations of elements compatible in mantle olivine and chromite:
          $$\mathbf{Ni > 400\text{--}500\text{ ppm}} \quad \text{and} \quad \mathbf{Cr > 1000\text{ ppm}}$$
        </li>
        <li><strong>Mantle Xenoliths:</strong> The presence of dense, angular mantle peridotite (spinel/garnet lherzolite) xenoliths proves rapid ascent from the mantle without intermediate crustal magma chamber staging.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 76</div>
        <div class="q-text">The composition of a primary magma depends on the following parameters : (i) Composition of the source material being partially melted, (ii) Relative concentrations of volatiles, (iii) Confining pressure, (iv) Degree of partial melting. Choose the correct set of answer from the following options :</div>
        <div class="q-options">
          <div class="opt-node">(A) (i), (ii), (iii)</div>
          <div class="opt-node">(B) (ii), (iii), (iv)</div>
          <div class="opt-node">(C) (i), (iii), (iv)</div>
          <div class="opt-node correct">(D) (i), (ii), (iii), (iv)</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (D)</div>
        <div><strong>(i), (ii), (iii), (iv):</strong> All four parameters strictly control the chemical, mineralogical, and normative composition of a primary magma during partial melting of the mantle or crust.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) (i), (ii), (iii) — INCORRECT</div>
        <p>
          This option arbitrarily omits parameter <strong>(iv) Degree of partial melting ($F$)</strong>. Melt fraction ($F$) is one of the most critical variables in igneous petrogenesis: small degrees of partial melting ($F = 1\text{--}5\%$) generate alkali-rich, silica-undersaturated melts (basanites, nephelinites), whereas large degrees ($F = 20\text{--}30\%$) produce tholeiitic and picritic liquids. Omitting (iv) violates elementary chemical thermodynamics.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) (ii), (iii), (iv) — INCORRECT</div>
        <p>
          This option erroneously excludes parameter <strong>(i) Composition of the source material</strong>. The primary magma composition is fundamentally constrained by mass balance of the source protolith; a depleted peridotite source cannot generate an alkaline basalt rich in incompatible trace elements, nor can a pelitic crustal source generate an ultramafic picrite.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) (i), (iii), (iv) — INCORRECT</div>
        <p>
          This option incorrectly omits parameter <strong>(ii) Relative concentrations of volatiles</strong>. Volatile fugacity ($f_{H_2O}, f_{CO_2}$) completely reconfigures mantle phase equilibria: $H_2O$ shifts melts toward quartz-normative silica-oversaturation (tholeiites and andesites), while $CO_2$ induces silica-undersaturation, generating carbonatites and melilitites.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(D) (i), (ii), (iii), (iv) — CORRECT</div>
        <p>
          All four variables—<strong>source composition, volatile concentrations, confining pressure, and melt fraction ($F$)</strong>—are universally recognized in modern igneous petrology (Winter, 2014, p. 205; Best, 2003) as the comprehensive, governing set of parameters controlling primary magma chemistry.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Synthesis: Impact of Governing Parameters on Primary Basaltic Magma Suites</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Primary Magma Suite</th>
            <th>Primary Tectonic Setting</th>
            <th>Mantle Source Composition</th>
            <th>Melt Fraction ($F$)</th>
            <th>Depth / Pressure ($P$)</th>
            <th>Volatiles Present</th>
            <th>Normative Character</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Tholeiitic Basalt (N-MORB)</strong></td>
            <td>Mid-Ocean Ridges (divergent)</td>
            <td>Depleted Lherzolite / Harzburgite</td>
            <td>Moderate to High ($F = 15\text{--}25\%$)</td>
            <td>Shallow ($P < 1.0\text{--}1.5\text{ GPa}$)</td>
            <td>Essentially anhydrous ($H_2O < 0.2\%$)</td>
            <td>Hypersthene + Quartz-normative</td>
          </tr>
          <tr>
            <td><strong>Alkali Olivine Basalt / Basanite</strong></td>
            <td>Oceanic Islands (OIB), Continental Rifts</td>
            <td>Enriched (Metasomatized) Lherzolite</td>
            <td>Low to Moderate ($F = 3\text{--}10\%$)</td>
            <td>Deep ($P = 1.5\text{--}3.0\text{ GPa}$)</td>
            <td>Minor $H_2O + CO_2$</td>
            <td>Nepheline + Olivine-normative</td>
          </tr>
          <tr>
            <td><strong>Nephelinite / Melilitite</strong></td>
            <td>Intracontinental Rifts (e.g., East Africa)</td>
            <td>Highly Enriched Carbonated Mantle</td>
            <td>Very Low ($F < 2\text{--}5\%$)</td>
            <td>Very Deep ($P > 2.5\text{--}3.5\text{ GPa}$)</td>
            <td>High $CO_2$ ($CO_2 \gg H_2O$)</td>
            <td>Strongly Nepheline-normative</td>
          </tr>
          <tr>
            <td><strong>Calc-Alkaline Basalt / Basaltic Andesite</strong></td>
            <td>Subduction Zones (Island Arcs)</td>
            <td>Hydrated Wedge (Slab Metasomatism)</td>
            <td>Moderate ($F = 10\text{--}20\%$)</td>
            <td>Intermediate ($P = 1.0\text{--}2.0\text{ GPa}$)</td>
            <td>High $H_2O$ ($2\text{--}6\text{ wt}\%$)</td>
            <td>Hypersthene + Quartz-normative</td>
          </tr>
          <tr>
            <td><strong>Komatiite</strong></td>
            <td>Archean Greenstone Belts</td>
            <td>Primitive / Fertile Lower Mantle</td>
            <td>Ultra-High ($F > 30\text{--}50\%$)</td>
            <td>High to Extreme ($P > 3\text{--}7\text{ GPa}$)</td>
            <td>Anhydrous ($T_{\text{melt}} > 1600^\circ\text{C}$)</td>
            <td>Forsterite + Enstatite-normative ($MgO > 18\%$)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- WORKED PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Analytical & Quantitative Practice Problems</div>
    <div class="card-body">

      <!-- Problem 1 -->
      <div class="p-card">
        <div class="p-header">Problem 1: Equilibrium Batch Melting Quantitative Calculation</div>
        <p>
          A mantle peridotite source has an initial concentration of lanthanum ($C_0 = 0.65\text{ ppm}$). The bulk distribution coefficient for lanthanum during melting is $D_0 = 0.015$. Calculate the concentration of lanthanum in the primary melt ($C_L$) generated at: (a) $F = 2\%$ ($0.02$) partial melting (alkali basalt); and (b) $F = 20\%$ ($0.20$) partial melting (tholeiite).
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Batch Melting Derivation:</strong><br>
          Using Shaw's equilibrium batch melting formula:
          $$C_L = \frac{C_0}{D_0 + F(1 - D_0)}$$<br>
          <strong>(a) For $F = 0.02$:</strong><br>
          $$\text{Denominator} = 0.015 + 0.02(1 - 0.015) = 0.015 + 0.02(0.985) = 0.015 + 0.0197 = 0.0347$$<br>
          $$C_{L,2\%} = \frac{0.65}{0.0347} \approx \mathbf{18.73\text{ ppm}}$$ (Enrichment factor $\approx 28.8\times$)<br>
          <strong>(b) For $F = 0.20$:</strong><br>
          $$\text{Denominator} = 0.015 + 0.20(0.985) = 0.015 + 0.1970 = 0.2120$$<br>
          $$C_{L,20\%} = \frac{0.65}{0.2120} \approx \mathbf{3.07\text{ ppm}}$$ (Enrichment factor $\approx 4.7\times$)<br>
          <strong>Conclusion:</strong> Low-degree partial melts are enriched in incompatible elements by a factor of more than 6 relative to high-degree tholeiitic melts.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Primary Melt Mg# Equilibrium with Mantle Olivine</div>
        <p>
          Calculate the equilibrium molar $Mg\#$ of a primary basaltic liquid in equilibrium with residual mantle olivine of composition $\text{Fo}_{90}$ ($\text{Mg}\#_{\text{ol}} = 0.90$), given Roeder and Emslie's distribution coefficient $K_D = \frac{(\text{Fe}^{2+}/\text{Mg})_{\text{ol}}}{(\text{Fe}^{2+}/\text{Mg})_{\text{liq}}} = 0.30$.
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Exchange Derivation:</strong><br>
          1. For olivine of $\text{Fo}_{90}$:
          $$\left(\frac{\text{Fe}^{2+}}{\text{Mg}}\right)_{\text{ol}} = \frac{1 - 0.90}{0.90} = \frac{0.10}{0.90} = 0.1111$$<br>
          2. Calculate liquid ratio:
          $$\left(\frac{\text{Fe}^{2+}}{\text{Mg}}\right)_{\text{liq}} = \frac{(\text{Fe}^{2+}/\text{Mg})_{\text{ol}}}{K_D} = \frac{0.1111}{0.30} \approx 0.3704$$<br>
          3. Calculate liquid $Mg\#$:
          $$\text{Mg}\#_{\text{liq}} = \frac{1}{1 + (\text{Fe}^{2+}/\text{Mg})_{\text{liq}}} = \frac{1}{1 + 0.3704} = \frac{1}{1.3704} \approx 0.7297 \implies \mathbf{73.0\%}$$<br>
          <strong>Rule of Thumb:</strong> A primary mantle melt in equilibrium with $\text{Fo}_{90}$ must have an $\mathbf{Mg\# \approx 70\text{--}73\%}$. Basalts with $Mg\# < 65\%$ have experienced fractional crystallization of olivine.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Incongruent Melting of Enstatite and the Effect of Water</div>
        <p>
          At 1 atmosphere under anhydrous conditions, enstatite melts incongruently:
          $$\text{Enstatite (Opx)} \rightleftharpoons \text{Forsterite (Ol)} + \text{Silica-rich Liquid}$$
          Explain how dissolved water ($H_2O$) influences this reaction at elevated mantle pressures and why subduction-related magmas tend toward silica oversaturation.
        </p>
        <div class="p-ans">
          <strong>Phase Equilibrium Mechanism:</strong><br>
          - <strong>Anhydrous vs. Hydrous Liquidus Fields:</strong> In anhydrous mantle systems at high pressure ($P > 0.5\text{ GPa}$), enstatite melts congruently, and the olivine primary phase field contracts.<br>
          - <strong>Role of $H_2O$:</strong> Water dissolved as hydroxyl ions ($\text{OH}^-$) depolymerizes silica tetrahedra in the silicate melt ($Si\text{--}O\text{--}Si + H_2O \rightleftharpoons 2 Si\text{--}OH$), selectively depressing the liquidus of silicates. Crucially, water expands the liquidus stability field of olivine at the expense of orthopyroxene. Consequently, partial melting of hydrous mantle peridotite drives eutectic compositions toward the enstatite-quartz side of the ternary, generating primary <strong>quartz-normative, silica-saturated to oversaturated magmas (boninites and high-Mg andesites)</strong>.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Carbon Dioxide and the Genesis of Carbonatitic Liquids</div>
        <p>
          Explain the thermodynamic mechanism by which $CO_2$ causes extreme silica undersaturation in deep mantle partial melts, leading to primary nephelinites, melilitites, and carbonatites.
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Reaction:</strong><br>
          In the deep mantle ($P > 2.0\text{--}2.5\text{ GPa}$, depths $> 70\text{ km}$), $CO_2$ dissolves not as molecular gas but by reacting with network-modifying cations to form carbonate complexes ($\text{CO}_3^{2-}$). This stabilizes the carbonation reaction:
          $$\text{Enstatite} + \text{Dolomite} \rightleftharpoons \text{Forsterite} + \text{Diopside} + \text{CO}_2$$<br>
          The carbonate complexing drastically reduces silica activity in the melt ($a_{\text{SiO}_2} \ll 1$), shifting cotectic crystallization paths away from silica-saturated minerals and producing highly silica-undersaturated, alkali-rich primary liquids that can unmix via liquid immiscibility into silicate and carbonatite melts.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Archean Komatiite Petrogenesis & Mantle Potential Temperature ($T_p$)</div>
        <p>
          Archean komatiite lavas possess $MgO = 28\text{ wt}\%$ and spinifex textures requiring extrusion temperatures of $T = 1580^\circ\text{C}$. Calculate the degree of partial melting ($F$) and mantle potential temperature ($T_p$), explaining why komatiites ceased forming after the Proterozoic.
        </p>
        <div class="p-ans">
          <strong>Thermal and Petrological Evaluation:</strong><br>
          1. <strong>Melt Fraction ($F$):</strong> Generating a liquid with $28\text{ wt}\% MgO$ from a pyrolite mantle ($MgO \approx 38\text{ wt}\%$) requires melting nearly all pyroxene and garnet, leaving only refractory olivine ($\text{Fo}_{94}$), which corresponds to an ultra-high melt fraction of <strong>$F \approx 40\text{--}50\%$</strong>.<br>
          2. <strong>Mantle Potential Temperature ($T_p$):</strong> An extrusion temperature of $1580^\circ\text{C}$ corresponds to an adiabatic mantle potential temperature of $T_p \approx 1850\text{--}1900^\circ\text{C}$ (approximately $300\text{--}400^\circ\text{C}$ hotter than the modern convecting asthenosphere, $T_p \approx 1350\text{--}1400^\circ\text{C}$).<br>
          3. <strong>Post-Archean Cessation:</strong> Radioactive secular cooling of Earth's interior reduced mantle temperatures, making large-scale $F > 40\%$ mantle melting impossible in the Phanerozoic.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Adiabatic Decompression vs. Thermal Influx Melting</div>
        <p>
          Compare the physical mechanism of magma generation at mid-ocean ridges (adiabatic decompression) with subduction zone island arcs (flux melting). Draw schematic $P\text{-}T$ trajectories relative to the mantle solidus.
        </p>
        <div class="p-ans">
          <strong>Geodynamic Melting Mechanisms:</strong><br>
          1. <strong>Mid-Ocean Ridges (Decompression Melting):</strong> Solid asthenospheric peridotite rises buoyantly beneath spreading centers. Because rocks have very low thermal diffusivity ($\kappa \approx 10^{-6}\text{ m}^2/\text{s}$), the ascent is virtually adiabatic ($dT/dP \approx 10\text{--}15^\circ\text{C/GPa}$). The adiabatic path crosses the dry peridotite solidus at $\sim 60\text{ km}$ ($P \approx 2\text{ GPa}$), generating MORB tholeiitic magma without adding external heat.<br>
          2. <strong>Subduction Zones (Flux Melting):</strong> The subducting oceanic lithosphere dewaters, releasing hydrous fluids ($H_2O + \text{solutes}$) into the overlying mantle wedge. Water depresses the peridotite solidus by $200\text{--}400^\circ\text{C}$, causing the lowered wet solidus to cross the ambient mantle geotherm, triggering melting at constant or decreasing temperature.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Residual Mantle Mineralogy and Rare Earth Element (REE) Fractionation</div>
        <p>
          Explain why Ocean Island Basalts (OIB) display steep, highly fractionated chondrite-normalized REE patterns with high $(\text{La/Yb})_N$ ratios ($> 15$), whereas Normal Mid-Ocean Ridge Basalts (N-MORB) display flat or depleted Heavy REE (HREE) slopes ($(\text{La/Yb})_N \approx 0.8\text{--}1.2$).
        </p>
        <div class="p-ans">
          <strong>Mineralogical Partitioning Explanation:</strong><br>
          - <strong>Garnet Compatibility:</strong> Garnet is the only common mantle mineral that strongly partitions Heavy Rare Earth Elements (HREE, e.g., $Lu, Yb$) over Light Rare Earth Elements (LREE, e.g., $La, Ce$), with $K_{d,\text{Yb}}^{\text{garnet-liq}} \approx 4\text{--}10 \gg 1$.<br>
          - <strong>OIB Genesis (Garnet Lherzolite Facies):</strong> OIB magmas originate from deep mantle plumes at depths $> 80\text{--}100\text{ km}$ ($P > 2.8\text{ GPa}$), where garnet is stable in the residual mantle. Garnet retains HREE in the residue, leaving the primary melt strongly depleted in HREE and resulting in steep $(\text{La/Yb})_N$ slopes.<br>
          - <strong>MORB Genesis (Spinel Lherzolite Facies):</strong> MORB melting occurs at shallower depths ($< 60\text{ km}$, $P < 2\text{ GPa}$), where spinel replaces garnet. Spinel does not fractionate HREE from LREE, producing flat HREE patterns.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Critical Melt Fraction ($F_c$) and Melt Extraction Permeability</div>
        <p>
          In a partially melting porous mantle peridotite, define the critical melt fraction ($F_c$, or compaction threshold) and calculate whether melt can segregate when the wetting angle is $\theta = 48^\circ$ versus $\theta = 68^\circ$.
        </p>
        <div class="p-ans">
          <strong>Fluid Dynamics of Melt Segregation:</strong><br>
          - <strong>Dihedral (Wetting) Angle ($\theta$):</strong> Controls the geometry of melt droplets along solid grain edges.
          $$\text{If } \theta < 60^\circ: \text{Melt forms an interconnected, continuous network along 3-grain junctions}$$
          $$\text{If } \theta > 60^\circ: \text{Melt remains trapped as isolated, non-connecting pockets at 4-grain intersections}$$<br>
          - <strong>Evaluation:</strong><br>
            At $\theta = 48^\circ$ ($< 60^\circ$), basaltic melt forms an interconnected permeable network at extremely low porosities ($F < 0.1\text{--}1.0\%$), allowing efficient porous flow and matrix compaction to extract primary magma.<br>
            At $\theta = 68^\circ$ ($> 60^\circ$), melt cannot segregate until a high critical threshold ($F_c \approx 5\text{--}10\%$) is reached where isolated pockets coalesce.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 76, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q076_Primary_Magma_Generation_Controls_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q076: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q076()
