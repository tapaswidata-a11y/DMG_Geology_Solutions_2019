#!/usr/bin/env python3
"""
Q082 Generator: Autometamorphic / Deuteric Alteration Processes
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q082():
    title = r"Q082: Igneous Petrology: Autometamorphism & Deuteric Alteration Processes | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Late-Stage Alteration"
    h1_title = "Q082: Autometamorphic (Deuteric) Processes in Cooling Igneous Plutons"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 82<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 3: Textures of Igneous Rocks / Deuteric Alteration, pp. 48–50); Anthony Hall, <em>Igneous Petrology</em>; G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 122–124); F.J. Turner & J. Verhoogen, <em>Igneous and Metamorphic Petrology</em>; H.G.F. Winkler, <em>Petrogenesis of Metamorphic Rocks</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND NATURE OF AUTOMETAMORPHISM -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Kinetics & Mechanism of Autometamorphism (Deuteric Alteration)</div>
    <div class="card-body">
      <p>
        <strong>Autometamorphism</strong> (universally known in igneous petrography as <strong>deuteric alteration</strong> or late-magmatic alteration, from the Greek <em>deuteros</em> = second) refers to the internal mineralogical and chemical transformations that occur within an igneous rock <strong>as it cools down immediately following its own crystallization</strong>.
      </p>
      <p>
        These secondary mineral reactions are driven by <strong>hot, volatile-rich aqueous fluids and gases exsolved directly from the residual magmatic liquid</strong> (second boiling / resurgent boiling), or by heated juvenile/connate fluids circulating in the thermal aureole of the cooling pluton.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q82/winter_p48_deuteric_autometamorphic.png" alt="Deuteric Alteration and Autometamorphic Textures from Winter">
        <div class="figure-caption">
          <strong>Figure 82.1 — Deuteric Replacement & Late-Magmatic Alteration Textures:</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 3). Illustrating the progressive replacement of high-temperature anhydrous igneous minerals (plagioclase, pyroxene, biotite) by hydrous secondary phases (sericite, epidote, uralitic actinolite, chlorite) during post-magmatic cooling.
        </div>
      </div>

      <h4>Fundamental Characteristics of Autometamorphic Processes</h4>
      <ul>
        <li><strong>Continuous Thermal Continuity:</strong> Autometamorphic reactions occur as part of a <strong>continuous cooling trajectory</strong> of the single parent igneous event. They are <em>not</em> the products of an independent, later, separate regional or contact metamorphic event.</li>
        <li><strong>Plutonic Dominance:</strong> Because deep plutonic environments (batholiths, lopoliths, stocks, thick sills) retain their exsolved magmatic volatiles under confining pressure and cool very slowly over millions of years, <strong>autometamorphic processes are far more widespread and intense in plutonic rocks than in volcanic rocks</strong>, where volatiles escape instantaneously into the atmosphere.</li>
        <li><strong>Fluid-Driven Reactions at Moderate Temperatures:</strong> Most reactions occur between $500^\circ\text{C}$ and $200^\circ\text{C}$, involving the interaction of water, carbon dioxide, fluorine, and boron with anhydrous silicate minerals.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: COMMON AUTOMETAMORPHIC / DEUTERIC PHENOMENA -->
  <div class="card">
    <div class="card-header bg-indigo">2. Common Autometamorphic Reactions in Igneous Petrography</div>
    <div class="card-body">
      <p>
        Petrologists routinely encounter specific diagnostic mineral replacements produced by autometamorphic fluid circulation:
      </p>
      <ul>
        <li><strong>Uralitization:</strong> The secondary alteration of high-temperature pyroxenes (augite, pigeonite, enstatite) into fibrous, acicular pale-green amphibole (<strong>actinolite, tremolite, or hornblende</strong>), typically observed in gabbros and dolerites.</li>
        <li><strong>Saussuritization:</strong> The hydrothermal breakdown of calcium-rich plagioclase (labradorite/bytownite) into a dense, fine-grained, microcrystalline aggregate of <strong>zoisite, clinozoisite, epidote, albite, calcite, and quartz</strong>.</li>
        <li><strong>Sericitization:</strong> The hydrolytic alteration of feldspars (both plagioclase and alkali feldspar) by acidic hydrothermal fluids, converting them into microscopic flakes of fine-grained white mica (<strong>sericite / muscovite</strong>) with the liberation of quartz and alkalis.</li>
        <li><strong>Serpentinization:</strong> The hydration of magnesium-rich olivine and orthopyroxene in peridotites and ultramafic cumulates by aqueous fluids ($T < 450^\circ\text{C}$), producing <strong>serpentine group minerals (lizardite, chrysotile, antigorite) and magnetite</strong>:
          $$2\text{Mg}_2\text{SiO}_4\ (\text{Forsterite}) + 3\text{H}_2\text{O} \longrightarrow \text{Mg}_3\text{Si}_2\text{O}_5(\text{OH})_4\ (\text{Serpentine}) + \text{Mg(OH)}_2\ (\text{Brucite})$$
        </li>
        <li><strong>Chloritization:</strong> The replacement of biotite mica or hornblende by green <strong>chlorite</strong>, often accompanied by the exsolution of needle-like rutile inclusions forming sagenitic webs.</li>
        <li><strong>Greisenization:</strong> Autometasomatic alteration of granitic cupolas by late-stage fluorine- and boron-rich magmatic fluids, transforming feldspars into an aggregate of <strong>quartz, lithian muscovite (zinnwaldite), topaz, fluorite, and cassiterite</strong>.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: THE FUNDAMENTAL BOUNDARY: WEATHERING AND DIAGENESIS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Why Weathering and Diagenesis are Strictly Excluded from Autometamorphism</div>
    <div class="card-body">
      <p>
        It is a gross petrological error to conflate autometamorphism with weathering or diagenesis:
      </p>
      <ul>
        <li><strong>Weathering:</strong> An <strong>exogenic, surface process</strong> occurring at atmospheric pressure ($P = 1\text{ atm}$) and ambient Earth-surface temperatures (typically $-10^\circ\text{C}$ to $+40^\circ\text{C}$). It is driven exclusively by the interaction of rocks with the atmosphere, biosphere, and meteoric precipitation ($O_2, CO_2, H_2O$), producing soils, saprolites, and clays (kaolinite, smectite). It has zero connection to magmatic heat or residual magmatic fluids.</li>
        <li><strong>Diagenesis:</strong> Refers strictly to <strong>post-depositional physical and chemical changes in sedimentary rocks</strong> at near-surface to shallow burial depths ($T < 150\text{--}200^\circ\text{C}$, $P < 1\text{--}2\text{ kbar}$), encompassing sediment compaction, cementation, dissolution, and authigenesis. It does not apply to igneous crystallization.</li>
      </ul>
      <div class="formula-box">
        <strong>The Petrogenetic Boundary:</strong><br>
        $$\text{Autometamorphism (Deuteric)} \implies \mathbf{Endogenic,\ High\ to\ Moderate\ Temp\ (500\text{--}200^\circ C),\ Magmatic\ Fluids}$$<br>
        $$\text{Weathering / Diagenesis} \implies \mathbf{Exogenic\ /\ Sedimentary,\ Low\ Temp\ (<150^\circ C),\ Meteoric\ /\ Pore\ Waters}$$
      </div>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 82</div>
        <div class="q-text">Which of the following statements w. r. t. Autometamorphic processes is not correct ?</div>
        <div class="q-options">
          <div class="opt-node">(A) These secondary mineral reactions occur in igneous rocks as they cool, and are not products of a distinct later metamorphic event.</div>
          <div class="opt-node">(B) These processes are more common in plutonic rocks than in volcanics.</div>
          <div class="opt-node correct">(C) Diagenetic and weathering processes are also considered to be Autometamorphic.</div>
          <div class="opt-node">(D) Most reactions involve minerals at moderate temperatures in an environment in which H2O is either liberated from residual melt or externally introduced.</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (C)</div>
        <div><strong>"Diagenetic and weathering processes are also considered to be Autometamorphic":</strong> This statement is completely false. Weathering is an exogenic, low-temperature surface process, and diagenesis is a sedimentary process; neither is ever classified as autometamorphic.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) These secondary mineral reactions occur in igneous rocks as they cool, and are not products of a distinct later metamorphic event. — ACCURATE STATEMENT</div>
        <p>
          This is the fundamental defining criterion of autometamorphism (deuteric alteration). Unlike regional or contact metamorphism, which requires an independent tectonothermal event millions of years later, autometamorphism occurs during the continuous cooling of the single host igneous intrusion itself.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) These processes are more common in plutonic rocks than in volcanics. — ACCURATE STATEMENT</div>
        <p>
          This statement is entirely true. Plutonic rocks crystallize slowly at depth under lithostatic confining pressure, allowing residual volatile-rich aqueous fluids to remain trapped and react with earlier crystals. In volcanic lavas, gases escape rapidly into the air, and lavas freeze before deuteric reactions can proceed.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(C) Diagenetic and weathering processes are also considered to be Autometamorphic. — NOT CORRECT (IDENTIFIED FLAW)</div>
        <p>
          This statement is <strong>completely incorrect and petrologically false</strong>. Weathering is an exogenic surface process driven by the atmosphere and meteoric water at ambient surface conditions ($T < 30^\circ\text{C}$). Diagenesis refers to post-depositional lithification processes in sedimentary basins. Neither has any relation to late-magmatic cooling or igneous autometamorphism (Winter, 2014, p. 48).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Most reactions involve minerals at moderate temperatures in an environment in which H2O is either liberated from residual melt or externally introduced. — ACCURATE STATEMENT</div>
        <p>
          This is a precise summary of deuteric thermodynamics: reactions proceed at moderate subsolidus temperatures ($200\text{--}500^\circ\text{C}$) in the presence of $H_2O$ and other volatiles exsolved by second boiling or drawn into the pluton via convective meteoric-hydrothermal cells.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison: Autometamorphism vs. Weathering, Diagenesis & Metamorphism</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Geological Process</th>
            <th>Primary Temperature Range</th>
            <th>Pressure Regime</th>
            <th>Fluid Source & Composition</th>
            <th>Host Rock Type</th>
            <th>Diagnostic Products</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Autometamorphism (Deuteric)</strong></td>
            <td><strong>Moderate ($200\text{--}500^\circ\text{C}$)</strong></td>
            <td>Subvolcanic to Plutonic ($0.5\text{--}5\text{ kbar}$)</td>
            <td><strong>Juvenile magmatic volatiles</strong> exsolved from residual melt (second boiling)</td>
            <td>Igneous Rocks (Plutonic & Hypabyssal)</td>
            <td><strong>Uralite, Saussurite, Sericite, Serpentine, Chlorite, Greisen</strong></td>
          </tr>
          <tr>
            <td><strong>Weathering</strong></td>
            <td>Surface ambient ($-10\text{ to }+40^\circ\text{C}$)</td>
            <td>Atmospheric ($1\text{ atm} \approx 0.001\text{ kbar}$)</td>
            <td>Meteoric water, atmospheric $O_2$ and $CO_2$</td>
            <td>Any exposed surface rock</td>
            <td>Kaolinite, Smectite, Goethite, Gibbsite, Saprolite</td>
          </tr>
          <tr>
            <td><strong>Diagenesis</strong></td>
            <td>Low ($20\text{--}150^\circ\text{C}$)</td>
            <td>Sedimentary burial ($< 1\text{--}2\text{ kbar}$)</td>
            <td>Connate porewater, modified basin brines</td>
            <td>Sedimentary Rocks</td>
            <td>Calcite/quartz cement, smectite-to-illite, dolomite</td>
          </tr>
          <tr>
            <td><strong>Regional Metamorphism</strong></td>
            <td>High ($300\text{--}900^\circ\text{C}$)</td>
            <td>Deep crustal ($3\text{--}12\text{ kbar}$)</td>
            <td>Metamorphic dehydration fluids derived from subducted slabs/crust</td>
            <td>Any pre-existing rock</td>
            <td>Foliated Schists, Gneisses, Granulites</td>
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
        <div class="p-header">Problem 1: Second Boiling (Resurgent Boiling) Thermodynamics</div>
        <p>
          During the isobaric crystallization of a hydrous granitic magma containing $4\text{ wt}\% H_2O$ at $P = 2\text{ kbar}$ ($200\text{ MPa}$), explain the physical mechanism of "second boiling" (resurgent boiling) and calculate whether the reaction involves a net positive or negative volume change ($\Delta V_{\text{rxn}}$).
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Derivation:</strong><br>
          1. <strong>Mechanistic Definition:</strong> Primary boiling occurs when magma decompresses during ascent. <em>Second boiling</em> occurs during cooling and isobaric crystallization: as anhydrous minerals (quartz and feldspars) crystallize from the melt, water is rejected into the shrinking volume of residual melt. When water concentration exceeds the solubility limit ($\sim 6\text{ wt}\%$ at 2 kbar), an aqueous supercritical fluid phase ($H_2O\text{-rich vapor}$) exsolves spontaneously.<br>
          2. <strong>Volume Change:</strong>
          $$\text{Melt} \longrightarrow \text{Crystals} + \text{Aqueous Vapor}$$
          $$\Delta V_{\text{rxn}} = V_{\text{crystals}} + V_{\text{vapor}} - V_{\text{melt}}$$<br>
          Because the specific volume of the low-density aqueous vapor ($V_{\text{vapor}}$) is exceedingly large compared to silicate melt at crustal pressures ($V_{\text{vapor}} \approx 1.5\text{ to } 3.0\text{ cm}^3/\text{g}$ vs $V_{\text{melt}} \approx 0.4\text{ cm}^3/\text{g}$), <strong>$\Delta V_{\text{rxn}}$ is strongly positive</strong>.<br>
          <strong>Consequence:</strong> This large volumetric expansion induces hydraulic fracturing of the pluton roof, creating stockworks and driving extensive deuteric autometamorphism.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Balanced Chemical Stoichiometry of Saussuritization</div>
        <p>
          Write the balanced chemical reaction for the complete saussuritization of anorthite plagioclase in the presence of water, producing zoisite, aluminum hydroxide, and quartz.
        </p>
        <div class="p-ans">
          <strong>Stoichiometric Reaction:</strong><br>
          $$\mathbf{4\text{CaAl}_2\text{Si}_2\text{O}_8\ (\text{Anorthite})} + \mathbf{2\text{H}_2\text{O}} \longrightarrow \mathbf{2\text{Ca}_2\text{Al}_3\text{Si}_3\text{O}_{12}(\text{OH})\ (\text{Zoisite})} + \mathbf{\text{Al}_2\text{O}_3\cdot\text{H}_2\text{O}} + \mathbf{2\text{SiO}_2\ (\text{Quartz})}$$<br>
          When sodium is available in solid solution (labradorite $\text{An}_{60}\text{Ab}_{40}$), the calcium is consumed by zoisite/epidote while the sodium recrystallizes into fine-grained secondary albite, producing the classic dull-green, turbid "saussurite" pseudomorph under the microscope.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Serpentinization Mass Balance & Density Reduction</div>
        <p>
          A pure dunite consisting of forsterite olivine ($\rho = 3.30\text{ g/cm}^3$) undergoes complete serpentinization to chrysotile serpentine ($\rho = 2.55\text{ g/cm}^3$) without loss of magnesium or silica according to:
          $$2\text{Mg}_2\text{SiO}_4 + 3\text{H}_2\text{O} \longrightarrow \text{Mg}_3\text{Si}_2\text{O}_5(\text{OH})_4 + \text{Mg(OH)}_2$$
          Calculate the percentage volume expansion ($\Delta V/V_0 \times 100\%$) of the rock during this autometamorphic hydration.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Calculation:</strong><br>
          1. <strong>Molar Masses:</strong>
          - Forsterite ($\text{Mg}_2\text{SiO}_4$): $M = 140.7\text{ g/mol}$. For 2 moles: Mass = $281.4\text{ g}$.<br>
          - Initial volume: $V_0 = \frac{281.4\text{ g}}{3.30\text{ g/cm}^3} \approx \mathbf{85.27\text{ cm}^3}$.<br>
          2. <strong>Product Masses:</strong>
          - Chrysotile ($\text{Mg}_3\text{Si}_2\text{O}_5(\text{OH})_4$): $M = 277.1\text{ g/mol}$. Volume = $\frac{277.1}{2.55} \approx 108.67\text{ cm}^3$.<br>
          - Brucite ($\text{Mg(OH)}_2$): $M = 58.3\text{ g/mol}$, $\rho = 2.39\text{ g/cm}^3$. Volume = $\frac{58.3}{2.39} \approx 24.39\text{ cm}^3$.<br>
          - Total final volume: $V_{\text{final}} = 108.67 + 24.39 = \mathbf{133.06\text{ cm}^3}$.<br>
          3. <strong>Volume Expansion:</strong>
          $$\frac{\Delta V}{V_0} \times 100\% = \frac{133.06 - 85.27}{85.27} \times 100\% = \frac{47.79}{85.27} \times 100\% \approx \mathbf{+56.0\%}$$<br>
          <strong>Geological Significance:</strong> The massive $\sim 56\%$ volume expansion during serpentinization generates immense internal stresses, producing networks of micro-fractures and slickensided shear surfaces in ophiolites.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Sericitization and Hydrogen-Ion Metasomatism</div>
        <p>
          Write the hydrolytic reaction governing the sericitization of potassium feldspar by acidic hydrothermal fluids ($H^+$), explaining why the fluid becomes enriched in potassium.
        </p>
        <div class="p-ans">
          <strong>Reaction Equation:</strong><br>
          $$\mathbf{3\text{KAlSi}_3\text{O}_8\ (\text{Microcline})} + \mathbf{2\text{H}^+} \longrightarrow \mathbf{\text{KAl}_3\text{Si}_3\text{O}_{10}(\text{OH})_2\ (\text{Sericite})} + \mathbf{6\text{SiO}_2\ (\text{Quartz})} + \mathbf{2\text{K}^+}$$<br>
          <strong>Hydrochemical Mechanism:</strong> Acidic deuteric fluids supply $H^+$ ions that exchange with $K^+$ in the feldspar lattice. The displaced potassium is leached into the aqueous fluid phase, leaving behind fine-grained white mica (sericite) and silica. This neutralizes the fluid, shifting it toward alkaline compositions in outer alteration zones.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Greisenization Reactions in Granitic Tin-Tungsten Systems</div>
        <p>
          Define greisenization and write the chemical transformation converting alkali feldspar into quartz and muscovite in the presence of fluorine-bearing magmatic fluids.
        </p>
        <div class="p-ans">
          <strong>Greisenization Definition & Reaction:</strong><br>
          - <strong>Greisen:</strong> A pneumatolytic/deuteric rock consisting essentially of quartz and white mica (muscovite, lepidolite, zinnwaldite), with accessory topaz, fluorite, tourmaline, cassiterite ($\text{SnO}_2$), and wolframite ($(\text{Fe,Mn})\text{WO}_4$).<br>
          - <strong>Chemical Transformation:</strong>
          $$\text{KAlSi}_3\text{O}_8\ (\text{K-feldspar}) + \text{HF} + \text{H}_2\text{O} \longrightarrow \text{KAl}_3\text{Si}_3\text{O}_{10}(\text{OH,F})_2\ (\text{Muscovite}) + \text{SiO}_2\ (\text{Quartz}) + \text{Topaz} + \text{K}^+$$<br>
          Occurs in the apical roofs (cupolas) of highly differentiated, peraluminous S-type granites.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Sagenitic Rutile Webs in Chloritized Biotite</div>
        <p>
          Under the microscope, altered biotite often exhibits a dense, triangular, or hexagonal grid of microscopic needle-like crystals of rutile (sagenite). Explain the crystallographic and geochemical origin of this deuteric texture.
        </p>
        <div class="p-ans">
          <strong>Mineralogical Origin:</strong><br>
          1. <strong>Titanium in Primary Biotite:</strong> High-temperature magmatic biotite can accommodate significant titanium ($2\text{ to } 5\text{ wt}\% TiO_2$) in its octahedral layer.<br>
          2. <strong>Exsolution during Chloritization:</strong> When deuteric fluids alter biotite to chlorite, titanium cannot fit into the chlorite crystal lattice ($TiO_2 \ll 0.1\text{ wt}\%$).<br>
          3. <strong>Epitaxial Sagenite Web:</strong> The excess titanium is rejected and exsolves as microscopic needles of <strong>rutile ($\text{TiO}_2$)</strong> oriented strictly parallel to the $\{110\}$ and $\{010\}$ directions of the host biotite cleavage plane, intersecting at $60^\circ/120^\circ$ angles to form a delicate geometric lattice termed a <strong>sagenite web</strong>.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Fluid Inclusion Microthermometry of Deuteric Quartz</div>
        <p>
          Microthermometric heating-freezing analysis of primary fluid inclusions trapped in deuteric quartz veins yields a homogenization temperature $T_h = 280^\circ\text{C}$ and a freezing point depression $\Delta T_f = -4.2^\circ\text{C}$. Calculate the fluid salinity in equivalent wt% NaCl using Potter's formula ($\text{Salinity} = 1.769|\Delta T_f| - 0.0423|\Delta T_f|^2 + 0.000527|\Delta T_f|^3$).
        </p>
        <div class="p-ans">
          <strong>Fluid Salinity Calculation:</strong><br>
          Given $|\Delta T_f| = 4.2^\circ\text{C}$:<br>
          $$\text{Term 1} = 1.769 \times 4.2 = 7.4298$$<br>
          $$\text{Term 2} = -0.0423 \times (4.2)^2 = -0.0423 \times 17.64 \approx -0.7462$$<br>
          $$\text{Term 3} = 0.000527 \times (4.2)^3 = 0.000527 \times 74.088 \approx +0.0390$$<br>
          $$\text{Salinity} = 7.4298 - 0.7462 + 0.0390 = \mathbf{6.72\text{ eq. wt}\% NaCl}$$<br>
          <strong>Interpretation:</strong> The deuteric fluid was a moderate-salinity hydrothermal brine ($6.7\text{ wt}\% NaCl$) actively circulating at $T > 280^\circ\text{C}$ during late-magmatic cooling.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Taphonomic & Structural Distinction: Deuteric vs Regional Metamorphism</div>
        <p>
          How can a field geologist definitively distinguish between an igneous pluton that has undergone deuteric autometamorphism versus one that has experienced subsequent regional dynamo-thermal metamorphism?
        </p>
        <div class="p-ans">
          <strong>Field and Microscopic Diagnostic Criteria:</strong><br>
          - <strong>Autometamorphism (Deuteric):</strong> Mineral alteration is <strong>pseudomorphic and non-foliated</strong> (e.g., uralite preserves the exact rectangular shape of original pyroxene crystals; plagioclase retains original igneous zoning despite being saussuritized). There is NO tectonic foliation, lineation, or dynamic recrystallization.<br>
          - <strong>Regional Metamorphism:</strong> Accompanied by directed tectonic differential stress, producing <strong>pervasive metamorphic foliation, schistosity, or gneissic banding</strong>. Primary igneous zoning is destroyed; minerals display undulose extinction, subgrain formation, dynamic recrystallization (core-and-mantle structures), and orientation of newly formed phyllosilicates.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 82, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q082_Autometamorphic_Deuteric_Alteration_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q082: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q082()
