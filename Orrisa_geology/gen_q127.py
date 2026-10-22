#!/usr/bin/env python3
"""
Q127 Generator: Natural vs. Artificial Pozzolanic Materials & Fly Ash
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q127():
    title = r"Q127: Engineering Geology: Natural vs. Artificial Pozzolanic Materials | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Engineering Geology & Building Materials"
    h1_title = "Q127: Pozzolanic Materials: Natural Geological Deposits vs. Artificial Industrial By-Products"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 127<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 10: Building Stones & Engineering Materials, p. 188); ASTM C618 (<em>Standard Specification for Coal Fly Ash and Raw or Calcined Natural Pozzolan for Use in Concrete</em>); A.M. Neville, <em>Properties of Concrete</em> (5th Ed., Ch. 13: Pozzolans and Slag); P.K. Mehta and P.J.M. Monteiro, <em>Concrete: Microstructure, Properties, and Materials</em>; Bureau of Indian Standards (IS: 3812-2003)."""

    part1 = r"""
  <!-- CARD 1: DEFINITIONS AND POZZOLANIC CHEMISTRY -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Fundamental Chemistry & Physical Classification of Pozzolans</div>
    <div class="card-body">
      <p>
        In engineering geology, concrete technology, and construction materials science, a <strong>pozzolan</strong> is formally defined (ASTM C125 / ASTM C618; Neville, 2011; Bangar, p. 188) as:
      </p>
      <div class="quote-box">
        <em>"A siliceous or siliceous and aluminous material which, in itself, possesses little or no cementitious value, but will, in finely divided form and in the presence of moisture, chemically react with calcium hydroxide at ordinary temperatures to form compounds possessing cementitious properties."</em>
      </div>

      <div class="figure-box">
        <img src="../../figures_Q127/pozzolanic_materials_classification_flyash.png" alt="Classification of Pozzolanic Materials: Natural vs Artificial">
        <div class="figure-caption">
          <strong>Figure 127.1 — Classification Taxonomy of Pozzolanic Materials:</strong> Division into Natural Pozzolans (Class N: Volcanic Ash, Diatomite, Opaline Chert, Pumice) and Artificial / Industrial By-Product Pozzolans (Fly Ash, Silica Fume, GGBFS, Rice Husk Ash).
        </div>
      </div>

      <h4>The Fundamental Pozzolanic Chemical Reaction</h4>
      <p>
        When Ordinary Portland Cement (OPC) hydrates, tricalcium silicate ($\text{C}_3\text{S}$) and dicalcium silicate ($\text{C}_2\text{S}$) react with water to produce calcium silicate hydrate gel ($\text{C-S-H}$) and release substantial amounts of crystalline <strong>calcium hydroxide ($\text{Ca(OH)}_2$ or Portlandite / CH)</strong>:
      </p>
      <div class="math-block">
        $$\text{Cement Hydration: } 2\text{C}_3\text{S} + 6\text{H} \longrightarrow \text{C-S-H (Gel)} + 3\text{Ca(OH)}_2 \quad (\approx 20\text{--}25\% \text{ by weight})$$
      </div>
      <p>
        Portlandite ($\text{Ca(OH)}_2$) contributes zero shear strength to concrete, is highly soluble, and leaches out in groundwater, creating porous pathways that trigger efflorescence and sulfate attack. When a pozzolan containing reactive amorphous silica ($\text{SiO}_2$) is introduced, it consumes the weak Portlandite, converting it into additional strong, water-insoluble binding gel:
      </p>
      <div class="math-block">
        $$\text{Pozzolanic Reaction: } \text{Ca(OH)}_2 + \text{SiO}_2 \text{ (reactive amorphous)} + \text{H}_2\text{O} \longrightarrow \text{C-S-H Gel}$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q127/bangar_p188_pozzolanic_materials_flyash.png" alt="Pozzolanic Materials and Flyash from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 127.2 — Pozzolanic Materials in Engineering Geology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 188). Outlines the natural geological sources of pozzolans and identifies flyash as an artificial industrial combustion product.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: NATURAL VS ARTIFICIAL POZZOLANS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Comprehensive Distinction: Natural Pozzolans vs. Artificial By-Products</div>
    <div class="card-body">
      <h4>Natural Pozzolanic Materials (ASTM C618 Class N)</h4>
      <p>
        Natural pozzolans are naturally occurring rocks and geological deposits that derive their reactivity from amorphous glass phases or cryptocrystalline silica:
      </p>
      <ul>
        <li><strong>Volcanic Ash, Tuff, and Pumicite:</strong> Ejected during explosive volcanic eruptions and rapidly quenched by air. Quenching prevents ordered crystal lattice formation, leaving amorphous vitric aluminosilicate glass. Used by ancient Romans (pozzolana from the slopes of Mount Vesuvius at Pozzuoli) to build the Pantheon and Roman aqueducts.</li>
        <li><strong>Calcined Diatomaceous Earths:</strong> Sedimentary rock composed of the microscopic amorphous opaline silica ($\text{SiO}_2 \cdot n\text{H}_2\text{O}$) skeletons of diatoms. When calcined at $600\text{--}800^\circ\text{C}$, free moisture and organics are expelled, producing exceptionally reactive pozzolanic powder.</li>
        <li><strong>Opaline Cherts & Shales:</strong> Marine or lacustrine sedimentary rocks containing high concentrations of amorphous opal-A or opal-CT that react vigorously with free lime.</li>
        <li><strong>Calcined Clays (Metakaolin):</strong> Kaolinite clay dehydroxylated by controlled thermal processing at $650\text{--}800^\circ\text{C}$ to produce an amorphous aluminosilicate framework ($2\text{SiO}_2 \cdot \text{Al}_2\text{O}_3$).</li>
      </ul>

      <h4>Artificial / Industrial By-Product Pozzolans</h4>
      <p>
        These materials do not exist in natural geological strata; they are synthesized as industrial waste products:
      </p>
      <ul>
        <li><strong>Fly Ash (Pulverized Fuel Ash / PFA):</strong> The fine, spherical particulate residue captured by electrostatic precipitators from the flue gases of <strong>coal-fired thermal power stations</strong>. Governed by ASTM C618 as Class F (siliceous, low lime $< 10\%$, from anthracite/bituminous coal) or Class C (pozzolanic and self-cementitious, high lime $> 20\%$, from sub-bituminous/lignite coal).</li>
        <li><strong>Silica Fume (Condensed Silica Fume / Microsilica):</strong> Extremely fine sub-micron spherical particles of non-crystalline silica condensed from the vapor phase in electric arc furnaces during the production of silicon metal or ferrosilicon alloys.</li>
        <li><strong>Ground Granulated Blast Furnace Slag (GGBFS):</strong> Molten glassy by-product from iron smelting, water-quenched to produce vitreous granules.</li>
        <li><strong>Rice Husk Ash (RHA):</strong> Combustion ash of agricultural rice husks containing amorphous biogenic silica.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: ENGINEERING BENEFITS IN MASS CONCRETE -->
  <div class="card">
    <div class="card-header bg-indigo">3. Engineering Benefits of Pozzolan Blending in Civil Structures</div>
    <div class="card-body">
      <p>
        Replacing $15\text{ to } 35\%$ of Portland cement with pozzolans yields crucial engineering advantages:
      </p>
      <ul>
        <li><strong>Drastic Reduction in Heat of Hydration:</strong> Crucial for massive gravity dams (e.g., Hirakud, Bhakra, Hoover Dams) to prevent thermal cracking during mass curing.</li>
        <li><strong>Pore Refinement & Impermeability:</strong> Secondary $\text{C-S-H}$ gel precipitates within the capillary pore network, converting continuous capillary pores into isolated gel pores and lowering water permeability by orders of magnitude.</li>
        <li><strong>Alkali-Silica Reaction (ASR) Mitigation:</strong> Pozzolanic silica binds free alkalis ($\text{Na}^+, \text{K}^+$) and reduces pore-fluid $\text{pH}$, preventing expansive gel formation around reactive siliceous aggregates.</li>
        <li><strong>Sulfate & Acid Resistance:</strong> Consumption of $\text{Ca(OH)}_2$ deprives aggressive sulfate ions ($\text{SO}_4^{2-}$) of the calcium needed to form destructive gypsum and ettringite.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 127</div>
      <div class="question-text">
        Which of the following is not a Natural Pozzolanic Material ?
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Calcined diatomaceous earths</li>
        <li class="option-item"><strong>(B)</strong> Volcanic ash, tuffs and pumicites</li>
        <li class="option-item correct"><strong>(C)</strong> Flyash</li>
        <li class="option-item"><strong>(D)</strong> Opaline cherts</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (C) Flyash</strong> — Fly ash is an <strong>artificial, industrial combustion by-product</strong> captured from coal-fired thermal power stations (ASTM C618 Class F/C), unlike natural geological materials such as volcanic ash, diatomaceous earth, and opaline chert (Class N).
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Calcined diatomaceous earths — Natural Pozzolan (Hence Incorrect Choice)</div>
        <p>
          Diatomaceous earth (diatomite) is a natural biogenic sedimentary rock consisting of the microscopic amorphous hydrated silica ($\text{SiO}_2 \cdot n\text{H}_2\text{O}$) frustules of diatoms. When calcined to drive off structural moisture, it functions as a potent natural pozzolan (ASTM C618 Class N; Bangar, p. 188). Because it is derived directly from a natural geological deposit, it is a natural pozzolanic material.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Volcanic ash, tuffs and pumicites — Prototypical Natural Pozzolans (Hence Incorrect Choice)</div>
        <p>
          Volcanic ashes, vitric tuffs, and pumicites are natural igneous pyroclastic deposits. Their rapid quenching upon atmospheric ejection locks silica and alumina into an amorphous glass structure. These materials represent the classical natural pozzolans used since Roman antiquity (pozzolana from Pozzuoli). Being naturally occurring geological deposits, they are natural pozzolans.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (C): Flyash — Fully Verified & Correct Option (Artificial By-Product)</div>
        <p>
          Fly ash (pulverized fuel ash / PFA) is <strong>NOT a natural geological material</strong>. It is an artificial industrial by-product produced by burning finely ground coal in the boilers of modern thermal electricity generation plants. The non-combustible mineral impurities fuse into microscopic spherical glassy droplets in the furnace flue gases and are collected mechanically or electrostatically. In ASTM C618, it is classified under Class F or Class C (coal fly ash), distinct from Class N (Natural pozzolans). Thus, fly ash is the only non-natural material listed.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Opaline cherts — Natural Pozzolan (Hence Incorrect Choice)</div>
        <p>
          Opaline chert is a naturally occurring siliceous sedimentary rock containing high concentrations of amorphous opal-A or opal-CT. Because of its disordered amorphous silica structure, finely ground opaline chert readily reacts with calcium hydroxide at ambient temperatures. It is formally classified as a Class N raw natural pozzolan.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Taxonomy: Pozzolanic Materials and Supplementary Cementitious Materials</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Material</th>
            <th>Origin / Source</th>
            <th>Classification (ASTM C618)</th>
            <th>Reactive Phase</th>
            <th>Physical Morphology</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fly Ash (Class F)</strong></td>
            <td><strong>Artificial:</strong> Combustion of bituminous/anthracite coal in thermal power plants</td>
            <td>Class F</td>
            <td>Amorphous aluminosilicate glass ($< 10\%\text{ CaO}$)</td>
            <td>Solid microscopic spheres ($1 - 100\ \mu\text{m}$)</td>
          </tr>
          <tr>
            <td><strong>Fly Ash (Class C)</strong></td>
            <td><strong>Artificial:</strong> Combustion of lignite/sub-bituminous coal</td>
            <td>Class C</td>
            <td>Aluminosilicate glass with reactive crystalline phases ($> 20\%\text{ CaO}$)</td>
            <td>Solid microscopic spheres ($1 - 50\ \mu\text{m}$)</td>
          </tr>
          <tr>
            <td><strong>Volcanic Ash / Pumicite</strong></td>
            <td><strong>Natural:</strong> Pyroclastic eruptive deposits</td>
            <td>Class N (Natural)</td>
            <td>Amorphous vitric volcanic glass</td>
            <td>Angular, vesicular glass shards</td>
          </tr>
          <tr>
            <td><strong>Calcined Diatomite</strong></td>
            <td><strong>Natural:</strong> Biogenic siliceous lake/marine sediment</td>
            <td>Class N (Natural)</td>
            <td>Amorphous opaline silica ($\text{SiO}_2 \cdot n\text{H}_2\text{O}$)</td>
            <td>Porous, highly cellular diatom frustules</td>
          </tr>
          <tr>
            <td><strong>Opaline Chert</strong></td>
            <td><strong>Natural:</strong> Sedimentary silica precipitation</td>
            <td>Class N (Natural)</td>
            <td>Disordered opal-A / opal-CT</td>
            <td>Angular ground mineral powder</td>
          </tr>
          <tr>
            <td><strong>Silica Fume</strong></td>
            <td><strong>Artificial:</strong> Smelting vapor of silicon/ferrosilicon alloy</td>
            <td>ASTM C1240</td>
            <td>Ultra-pure amorphous $\text{SiO}_2$ ($> 85 - 95\%$)</td>
            <td>Sub-micron spheres ($0.1 - 0.2\ \mu\text{m}$)</td>
          </tr>
          <tr>
            <td><strong>Ground Granulated Blast Furnace Slag</strong></td>
            <td><strong>Artificial:</strong> Molten iron blast furnace slag, water-quenched</td>
            <td>ASTM C989</td>
            <td>Vitreous calcium aluminosilicate</td>
            <td>Angular, glassy crushed particles</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD: 8 PRACTICE PROBLEMS WITH FULL STEP-BY-STEP DERIVATIONS -->
  <div class="card">
    <div class="card-header bg-purple">8 Advanced Practice Problems & Fully Worked Solutions</div>
    <div class="card-body">
      <!-- PROBLEM 1 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 1: Chemical Composition Threshold for ASTM C618 Classification</strong><br>
        Chemical analysis of an industrial by-product powder yields the following oxide percentages:
        $\text{SiO}_2 = 54.0\%$, $\text{Al}_2\text{O}_3 = 26.5\%$, $\text{Fe}_2\text{O}_3 = 7.5\%$, $\text{CaO} = 4.0\%$, $\text{SO}_3 = 1.2\%$, and Loss on Ignition ($\text{LOI}$) = $2.5\%$.
        According to ASTM C618 requirements, determine whether this material satisfies the chemical criterion for Class F pozzolan.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Check the major oxide sum ($\text{SiO}_2 + \text{Al}_2\text{O}_3 + \text{Fe}_2\text{O}_3$):
          $$\sum (\text{S} + \text{A} + \text{F}) = 54.0\% + 26.5\% + 7.5\% = 88.0\%$$
          2. ASTM C618 criterion for Class F:
          $$\sum (\text{SiO}_2 + \text{Al}_2\text{O}_3 + \text{Fe}_2\text{O}_3) \ge 70.0\%$$
          $$\text{Since } 88.0\% \ge 70.0\%, \text{ this criterion is fully satisfied.}$$
          3. Check calcium oxide ($\text{CaO}$): $\text{CaO} = 4.0\% < 10.0\%$ (characteristic of low-calcium Class F fly ash).<br>
          4. Check $\text{SO}_3 \le 5.0\%$ ($1.2\% \le 5.0\%$) and $\text{LOI} \le 6.0\%$ ($2.5\% \le 6.0\%$).<br>
          The material qualifies as a standard <strong>Class F Fly Ash</strong>.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Strength Activity Index (SAI) Calculation</strong><br>
        In accordance with ASTM C618 / ASTM C311, mortar cubes are cast for two mixes:
        (1) Control mix (100% Portland cement): 28-day compressive strength = $42.0\text{ MPa}$;
        (2) Test mix (80% cement + 20% calcined diatomaceous earth): 28-day compressive strength = $36.5\text{ MPa}$.
        Calculate the Strength Activity Index (SAI) and determine if it meets the ASTM C618 minimum threshold of $75.0\%$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate Strength Activity Index (SAI):
          $$\text{SAI} = \left(\frac{\text{Compressive Strength of Test Mix}}{\text{Compressive Strength of Control Mix}}\right) \times 100\%$$
          $$\text{SAI} = \left(\frac{36.5\text{ MPa}}{42.0\text{ MPa}}\right) \times 100\% = 86.90\%$$
          2. Check against threshold:
          $$\text{Since } 86.90\% > 75.0\%, \text{ the calcined diatomite comfortably satisfies the ASTM C618 pozzolanic activity requirement.}$$
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Heat of Hydration Mitigation in Dam Gravity Section</strong><br>
        A mass concrete gravity dam requires $400,000\text{ m}^3$ of concrete with a cementitious material content of $250\text{ kg/m}^3$. Plain Portland cement generates a 7-day heat of hydration of $350\text{ kJ/kg}$. If $30\%$ of the cement is replaced by Class F fly ash (which generates only $120\text{ kJ/kg}$ in 7 days), calculate: (a) total heat released using 100% cement, and (b) total heat released using the fly ash blend, and (c) the percentage reduction in heat generation.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Total cementitious mass $M = 400,000\text{ m}^3 \times 250\text{ kg/m}^3 = 1.0 \times 10^8\text{ kg} = 100,000\text{ tonnes}$.<br>
          2. Total heat released with 100% OPC:
          $$Q_{\text{plain}} = 1.0 \times 10^8\text{ kg} \times 350\text{ kJ/kg} = 3.50 \times 10^{10}\text{ kJ}$$
          3. Total heat released with 30% fly ash blend ($70\text{ kg OPC} + 30\text{ kg FA}$ per $100\text{ kg}$):
          $$Q_{\text{blend}} = [0.70(350) + 0.30(120)] \text{ kJ/kg} = [245 + 36] = 281\text{ kJ/kg}$$
          $$Q_{\text{total}} = 1.0 \times 10^8\text{ kg} \times 281\text{ kJ/kg} = 2.81 \times 10^{10}\text{ kJ}$$
          4. Percentage reduction in heat:
          $$\Delta Q (\%) = \left(\frac{3.50 - 2.81}{3.50}\right) \times 100\% = \frac{0.69}{3.50} \times 100\% = 19.71\%$$
          This $19.7\%$ heat reduction prevents massive thermal differential stress and core cracking.
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Stoichiometry of Portlandite ($\text{Ca(OH)}_2$) Consumption</strong><br>
        Hydration of $100\text{ g}$ of pure alite ($\text{C}_3\text{S}$, molecular weight $228.3\text{ g/mol}$) releases $1.5\text{ moles}$ of $\text{Ca(OH)}_2$ ($\text{MW} = 74.1\text{ g/mol}$) per mole of alite hydrated:
        $$2\text{C}_3\text{S} + 6\text{H}_2\text{O} \longrightarrow \text{C}_3\text{S}_2\text{H}_3 + 3\text{Ca(OH)}_2$$
        Calculate the mass of crystalline $\text{Ca(OH)}_2$ liberated by the complete hydration of $100\text{ g}$ of $\text{C}_3\text{S}$, and determine the minimum mass of pure reactive amorphous silica ($\text{SiO}_2$, $\text{MW} = 60.1\text{ g/mol}$) required to completely convert all liberated lime into tobermorite gel ($\text{C-S-H}$ with $\text{Ca/Si} = 1.5$ according to $1.5\text{Ca(OH)}_2 + \text{SiO}_2 \longrightarrow 1.5\text{CaO}\cdot\text{SiO}_2\cdot\text{H}_2\text{O}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Moles of $\text{C}_3\text{S}$ in $100\text{ g}$:
          $$n(\text{C}_3\text{S}) = \frac{100\text{ g}}{228.3\text{ g/mol}} = 0.4380\text{ mol}$$
          2. Moles and mass of $\text{Ca(OH)}_2$ liberated:
          $$n(\text{Ca(OH)}_2) = 1.5 \times 0.4380\text{ mol} = 0.6570\text{ mol}$$
          $$m(\text{Ca(OH)}_2) = 0.6570\text{ mol} \times 74.1\text{ g/mol} = 48.69\text{ g}$$
          3. Moles and mass of reactive $\text{SiO}_2$ required:
          $$\text{Ratio } \text{Ca/Si} = 1.5 \implies n(\text{SiO}_2) = \frac{n(\text{Ca(OH)}_2)}{1.5} = \frac{0.6570}{1.5} = 0.4380\text{ mol}$$
          $$m(\text{SiO}_2) = 0.4380\text{ mol} \times 60.1\text{ g/mol} = 26.32\text{ g}$$
          $26.32\text{ g}$ of reactive pozzolanic silica is consumed to convert all liberated lime into cementitious $\text{C-S-H}$ gel.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Carbon Footprint (Embodied $CO_2$) Reduction</strong><br>
        The manufacture of Ordinary Portland Cement releases approximately $0.85\text{ tonnes of } CO_2$ per tonne of cement produced due to limestone calcination ($\text{CaCO}_3 \rightarrow \text{CaO} + CO_2$) and fossil fuel kiln combustion. Fly ash, as an industrial by-product, carries an embodied carbon allocation of only $0.02\text{ tonnes of } CO_2$ per tonne (associated solely with processing and haulage). For a major infrastructure project requiring $50,000\text{ tonnes}$ of binder, calculate the net reduction in $CO_2$ emissions achieved by replacing $25\%$ of the OPC with fly ash.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Emissions for 100% OPC mix ($50,000\text{ t}$):
          $$E_{\text{plain}} = 50,000\text{ t} \times 0.85\text{ t } CO_2/\text{t} = 42,500\text{ tonnes } CO_2$$
          2. Emissions for 25% Fly Ash blend ($37,500\text{ t OPC} + 12,500\text{ t FA}$):
          $$E_{\text{blend}} = (37,500 \times 0.85) + (12,500 \times 0.02) = 31,875 + 250 = 32,125\text{ tonnes } CO_2$$
          3. Net $CO_2$ emission savings:
          $$\Delta E = 42,500 - 32,125 = 10,375\text{ tonnes of } CO_2 \quad (\approx 24.41\% \text{ reduction})$$
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Morphological Influence: Spherical Fly Ash vs Angular Pumicite</strong><br>
        A concrete mix design requires maintaining a slump of $100\text{ mm}$ at a fixed water-cementitious ratio of $0.45$. When $20\%$ of cement is replaced by Class F fly ash (spherical cenospheres), water demand for equivalent workability drops by $7\%$. Conversely, when replaced by ground volcanic pumicite (angular, vesicular shards), water demand increases by $12\%$. Explain the rheological mechanisms governing this divergence.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. <strong>Ball-Bearing Effect of Fly Ash:</strong> Fly ash forms via rapid surface-tension cooling of molten droplets in flue gases, creating perfectly smooth, spherical particles. These spherical particles act as microscopic ball bearings between angular cement grains, reducing inter-particle friction and plastic viscosity, thus decreasing water demand.
          2. <strong>Internal Absorption of Pumicite:</strong> Volcanic pumicite contains high cellular vesicularity and jagged, broken glass shards. The high internal porosity physically absorbs mixing water through capillary action, and high specific surface area increases frictional interlock, requiring higher water contents to maintain equivalent workability.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Fineness and Specific Surface Area (Blaine Method)</strong><br>
        A laboratory evaluates two pozzolans using the Blaine air permeability apparatus (ASTM C204):
        (A) Raw volcanic ash: specific surface area $S_A = 320\text{ m}^2\text{/kg}$;
        (B) Silica fume: specific surface area $S_B = 20,000\text{ m}^2\text{/kg}$.
        (a) Compute the ratio $S_B / S_A$. (b) Explain why silica fume achieves rapid 1-day pozzolanic activity whereas volcanic ash requires several weeks.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Ratio:
          $$\frac{S_B}{S_A} = \frac{20,000\text{ m}^2\text{/kg}}{320\text{ m}^2\text{/kg}} = 62.5$$
          2. Explanation: Heterogeneous chemical reaction rates are directly proportional to the accessible reactive surface area per unit mass. With a specific surface area over $60\times$ greater and particle size in the sub-micron range ($0.1\ \mu\text{m}$ vs $20\ \mu\text{m}$), silica fume dissolves instantaneously into pore solution, reacting immediately with $\text{Ca}^{2+}$ ions, whereas coarser volcanic ash undergoes slow dissolution limited by diffusion across developing product rinds.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Alkali-Silica Reaction (ASR) Expansion Suppression</strong><br>
        Standard mortar bars (ASTM C1260 / ASTM C1567) made with reactive borosilicate glass aggregate and high-alkali cement undergo a 14-day expansion of $\varepsilon_{\text{control}} = 0.38\%$ in $1\text{ N NaOH}$ bath at $80^\circ\text{C}$ (failing the $< 0.10\%$ safety threshold). Incorporating $25\%$ Class F fly ash reduces the 14-day expansion to $\varepsilon_{\text{flyash}} = 0.045\%$. Calculate the percentage suppression of ASR expansion and explain how the fly ash chemically neutralizes alkali attack.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Percentage suppression:
          $$\Delta \varepsilon (\%) = \left(\frac{0.38\% - 0.045\%}{0.38\%}\right) \times 100\% = \frac{0.335}{0.38} \times 100\% = 88.16\%$$
          2. Chemical Mechanism:
          <ul>
            <li><strong>Alkali Entrapment:</strong> The pozzolanic reaction consumes $\text{Ca(OH)}_2$ to produce $\text{C-S-H}$ gel with a lower $\text{Ca/Si}$ ratio ($1.0 - 1.2$ vs $1.7 - 2.0$ in plain cement). Lower $\text{Ca/Si}$ hydrates possess a strong negative surface charge that preferentially adsorbs alkali metal cations ($\text{Na}^+, \text{K}^+$) from pore fluid.</li>
            <li><strong>Reduction in Hydroxyl Ion Concentration ($\text{pH}$):</strong> Entrapping alkalis lowers the pore-water $\text{OH}^-$ concentration, preventing alkaline dissolution of reactive silica in the rock aggregates.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=127,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q127_Natural_vs_Artificial_Pozzolans_Flyash_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q127: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q127()
