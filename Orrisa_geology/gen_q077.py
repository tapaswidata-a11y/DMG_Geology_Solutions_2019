#!/usr/bin/env python3
"""
Q077 Generator: Igneous Textures Matching & Petrographic Analysis
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q077():
    title = r"Q077: Igneous Petrology: Matching Diagnostic Textures & Rock Types | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Textural Analysis"
    h1_title = "Q077: Diagnostic Igneous Textures & Structures: Phaneritic, Ophitic, Holocrystalline, and Pillows"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 77<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Ch. 5: Petrology / Igneous Rocks, pp. 76–84, 164–170); John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (Ch. 3: Textures of Igneous Rocks, pp. 33–51); G.B. Mahapatra, <em>A Text-Book of Geology</em> (Ch. 8, pp. 115–128); Tyrrell, <em>The Principles of Petrology</em>."""

    part1 = r"""
  <!-- CARD 1: TEXTURAL CLASSIFICATION AND CRYSTALLIZATION KINETICS -->
  <div class="card">
    <div class="card-header bg-blue">1. Crystallization Kinetics & Textural Evolution of Magmas</div>
    <div class="card-body">
      <p>
        The texture of an igneous rock is the geometric arrangement, mutual spatial relationships, crystallinity, and grain size of its constituent mineral phases. Textural development is fundamentally controlled by the interplay of two kinetic parameters during magmatic cooling (Winter, 2014, p. 34):
      </p>
      <ul>
        <li><strong>Rate of Nucleation ($I$):</strong> The number of stable crystal nuclei formed per unit volume per unit time.</li>
        <li><strong>Rate of Crystal Growth ($Y$):</strong> The linear rate at which chemical components diffuse through the melt and attach to existing crystal faces ($m/\text{s}$).</li>
      </ul>
      <p>
        Both rates are functions of <strong>undercooling ($\Delta T = T_{\text{liquidus}} - T_{\text{actual}}$)</strong>:
      </p>
      <ul>
        <li><strong>Slow Cooling (Deep Plutonic Realm / Low $\Delta T$):</strong> Growth rate ($Y$) far exceeds nucleation rate ($I$). Very few nuclei form, but each grows to large macroscopic dimensions. This produces a <strong>phaneritic texture</strong> (crystals visible to the unaided eye, $>1\text{ mm}$), characteristic of deep-seated plutons such as <strong>Granite</strong> and <strong>Gabbro</strong>.</li>
        <li><strong>Rapid Cooling (Volcanic Realm / High $\Delta T$):</strong> Nucleation rate surges while diffusion slows, yielding microscopic crystals (<strong>aphanitic</strong>) or, under explosive quenching into air/water, freezing the liquid structure into volcanic glass (<strong>holohyaline</strong>).</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q77/bangar_p77_igneous_textures_ophitic.png" alt="Igneous Textures and Crystallinity from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 77.1 — Diagnostic Igneous Textures:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 77). Illustrating grain size categories, crystallinity divisions (holocrystalline vs. hypocrystalline), and specialized intergrowth textures.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: OPHITIC TEXTURE IN HYPABYSSAL DOLERITES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Ophitic & Subophitic Textures: Hallmarks of Hypabyssal Dolerite</div>
    <div class="card-body">
      <p>
        <strong>Ophitic texture</strong> (from the Greek <em>ophis</em> = serpent, referring to its mottled appearance) is the diagnostic petrographic signature of <strong>dolerite (diabase)</strong>, the medium-grained hypabyssal intrusive equivalent of basalt that forms extensive dikes and sills worldwide.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q77/bangar_p166_ophitic_texture_dolerite.png" alt="Ophitic Texture in Dolerite from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 77.2 — Petrographic Thin Section of Ophitic Texture in Dolerite:</strong> Authentic textbook diagram from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 166). Laths of euhedral-to-subhedral plagioclase feldspar (labradorite) are completely enclosed within large, optically continuous plates of clinopyroxene (augite).
        </div>
      </div>

      <h4>Crystallization Mechanics of the Ophitic Texture</h4>
      <p>
        The formation of ophitic texture reflects cotectic crystallization along the plagioclase-clinopyroxene liquidus:
      </p>
      <ol>
        <li><strong>Early Plagioclase Framework:</strong> In basaltic dikes, plagioclase begins crystallizing first or nucleates with high frequency, forming an open, interlocking network of slender, prismatic laths.</li>
        <li><strong>Late Poikilitic Pyroxene Overgrowth:</strong> Clinopyroxene (augite) has a relatively high nucleation barrier in dry basaltic melts. Once nucleated, pyroxene grows rapidly, wrapping around and completely enclosing the pre-existing plagioclase laths. Under polarized light, the enclosing pyroxene extinguishes simultaneously over several square millimeters.</li>
        <li><strong>Subophitic Transition:</strong> When the plagioclase laths are only <em>partially</em> enclosed by pyroxene grains, the texture is termed <strong>subophitic</strong>. When pyroxenes form small, granular grains clustered between plagioclase laths, it becomes <strong>intergranular</strong>.</li>
      </ol>
    </div>
  </div>

  <!-- CARD 3: HOLOCRYSTALLINITY & SUBAQUEOUS PILLOW SPILITES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Holocrystalline Plutonism (Gabbro) & Submarine Pillow Structures (Spillite)</div>
    <div class="card-body">
      <h4>Degree of Crystallinity: Holocrystalline Gabbro</h4>
      <p>
        Igneous rocks are divided based on the ratio of crystal to glass into:
      </p>
      <ul>
        <li><strong>Holocrystalline:</strong> Composed <strong>$100\%$ of crystalline mineral grains</strong> with zero interstitial amorphous glass. In the exam pairing, <strong>Gabbro</strong>—the coarse-grained mafic plutonic equivalent of basalt crystallized deep within oceanic crust (Layer 3) or continental layered intrusions—is the textbook archetype of a <strong>holocrystalline phaneritic rock</strong>.</li>
        <li><strong>Hypocrystalline (Merocrystalline):</strong> Composed of both crystals and interstitial glass (e.g., andesite, pitchstone).</li>
        <li><strong>Holohyaline:</strong> Composed entirely of amorphous volcanic glass ($>95\%$ glass, e.g., obsidian, tachylite).</li>
      </ul>

      <h4>Subaqueous Quenching & Pillow Structures in Spillites</h4>
      <p>
        <strong>Pillow structures</strong> are bulbous, rounded, or ellipsoidal sack-like masses (typically 0.2 to 2 m in diameter) formed when basaltic magma is extruded underwater into a marine or lacustrine basin:
      </p>
      <ul>
        <li><strong>Pillow Mechanics:</strong> Upon contact with cold seawater, a flexible, chilled glassy rind (tachylite) freezes instantly around the expanding lava lobe. Internal magmatic pressure inflates the lobe like a water balloon until it ruptures, budding into a daughter pillow. Gravity forces the lower surface to sag into underlying voids, creating a diagnostic <strong>convex upper surface and a downward-pointing V-shaped pedicle</strong> (a classic geopetal younging indicator!).</li>
        <li><strong>Spillite (Spilite):</strong> An altered, sodium-rich submarine basalt commonly exhibiting pillow structure. During extrusion on the seabed, low-temperature hydrothermal reaction with heated seawater induces <strong>spilitization</strong>, transforming calcic plagioclase into secondary <strong>albite</strong> while mafic phases alter to <strong>chlorite, actinolite, epidote, and calcite</strong>.</li>
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
        <div class="q-num">Question 77</div>
        <div class="q-text">Match the following in List — I and List — II and choose the correct answer :<br><br>
        <strong>List — I:</strong><br>
        (a) Phaneritic texture<br>
        (b) Ophitic texture<br>
        (c) Holocrystalline texture<br>
        (d) Pillow structure<br><br>
        <strong>List — II:</strong><br>
        (i) Dolerite<br>
        (ii) Gabbro<br>
        (iii) Spillite<br>
        (iv) Granite</div>
        <div class="q-options">
          <div class="opt-node">(A) (a) - (ii), (b) - (i), (c) - (iv), (d) - (iii)</div>
          <div class="opt-node correct">(B) (a) - (iv), (b) - (i), (c) - (ii), (d) - (iii)</div>
          <div class="opt-node">(C) (a) - (iv), (b) - (ii), (c) - (i), (d) - (iii)</div>
          <div class="opt-node">(D) (a) - (i), (b) - (ii), (c) - (iii), (d) - (iv)</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (B)</div>
        <div><strong>(a) - (iv), (b) - (i), (c) - (ii), (d) - (iii):</strong> Phaneritic texture corresponds to Granite (iv), Ophitic texture is diagnostic of Dolerite (i), Holocrystalline texture characterizes Gabbro (ii), and Pillow structure is the hallmark of submarine Spillite (iii).</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) (a) - (ii), (b) - (i), (c) - (iv), (d) - (iii) — INCORRECT</div>
        <p>
          Pairs (a) Phaneritic texture with (ii) Gabbro and (c) Holocrystalline with (iv) Granite. While both plutonic rocks are technically phaneritic and holocrystalline, standard Indian geological curricula (Bangar, p. 166; Mahapatra, p. 120) pair Granite canonically as the prime archetype of <em>phaneritic equigranular texture</em>, and Gabbro as the prime example of a <em>coarse holocrystalline basic pluton</em>.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(B) (a) - (iv), (b) - (i), (c) - (ii), (d) - (iii) — CORRECT</div>
        <p>
          This is the exact, canonical matching:
          <ul>
            <li><strong>(a) Phaneritic texture $\to$ (iv) Granite:</strong> The textbook definition of a coarse, plutonic felsic rock where individual mineral grains (quartz, K-feldspar, mica) are clearly visible to the naked eye.</li>
            <li><strong>(b) Ophitic texture $\to$ (i) Dolerite:</strong> The quintessential, universal petrographic hallmark of hypabyssal dolerite/diabase dikes and sills.</li>
            <li><strong>(c) Holocrystalline texture $\to$ (ii) Gabbro:</strong> The classic mafic plutonic rock completely composed of interlocking crystals of calcic plagioclase and pyroxene with zero glass.</li>
            <li><strong>(d) Pillow structure $\to$ (iii) Spillite:</strong> The definitive subaqueous volcanic cooling structure formed by quenched, spilitized submarine pillow basalts.</li>
          </ul>
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) (a) - (iv), (b) - (ii), (c) - (i), (d) - (iii) — INCORRECT</div>
        <p>
          Erroneously assigns (b) Ophitic texture to (ii) Gabbro and (c) Holocrystalline to (i) Dolerite. Gabbros exhibit granular or gabbroic texture, whereas ophitic texture is the distinct, defining characteristic of hypabyssal dolerite.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) (a) - (i), (b) - (ii), (c) - (iii), (d) - (iv) — INCORRECT</div>
        <p>
          Completely scrambled pairings; pairs pillow structure with granite (granites never form pillows) and phaneritic texture with dolerite.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Textural & Structural Framework of Igneous Rocks</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Texture / Structure</th>
            <th>Primary Petrographic Definition</th>
            <th>Cooling Regime & Environment</th>
            <th>Nucleation vs Growth Kinetics</th>
            <th>Canonical Rock Types</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Phaneritic Texture</strong></td>
            <td>Individual mineral grains macroscopic ($>1\text{ mm}$), clearly distinguishable with naked eye</td>
            <td>Plutonic (Abyssal, deep crustal batholiths & stocks)</td>
            <td>Low undercooling ($\Delta T$); Low nucleation ($I$), High growth rate ($Y$)</td>
            <td><strong>Granite</strong>, Diorite, Syenite</td>
          </tr>
          <tr>
            <td><strong>Ophitic Texture</strong></td>
            <td>Laths of plagioclase completely enclosed poikilitically in large single pyroxene plates</td>
            <td>Hypabyssal (Subvolcanic dikes, sills, minor intrusions)</td>
            <td>Cotectic crystallization; high plagioclase nucleation followed by rapid augite growth</td>
            <td><strong>Dolerite (Diabase)</strong></td>
          </tr>
          <tr>
            <td><strong>Holocrystalline Texture</strong></td>
            <td>$100\%$ crystalline mineral framework; entirely devoid of uncrystallized glassy base</td>
            <td>Plutonic to Hypabyssal (slow to moderate cooling)</td>
            <td>Complete crystallization achieved before temperature drops below glass transition ($T_g$)</td>
            <td><strong>Gabbro</strong>, Peridotite, Granodiorite</td>
          </tr>
          <tr>
            <td><strong>Pillow Structure</strong></td>
            <td>Interlocking, bulbous, convex-up sack-like lobes with chilled glassy rinds and radial fractures</td>
            <td>Extrusive (Subaqueous / Submarine seafloor volcanism)</td>
            <td>Instantaneous thermal quenching in water ($1200^\circ\text{C} \to 4^\circ\text{C}$); ductile crust budding</td>
            <td><strong>Spillite (Spilite)</strong>, Submarine Basalt</td>
          </tr>
          <tr>
            <td><strong>Porphyritic Texture</strong></td>
            <td>Large, conspicuous crystals (phenocrysts) embedded in a finer groundmass</td>
            <td>Two-stage cooling (slow plutonic incubation followed by rapid ascent/eruption)</td>
            <td>Early low $\Delta T$ phenocryst growth followed by sudden high $\Delta T$ groundmass nucleation</td>
            <td>Rhyolite, Andesite porphyry, Basalt</td>
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
        <div class="p-header">Problem 1: Crystal Size Distribution (CSD) Theory & Residence Time</div>
        <p>
          In a porphyritic granite pluton, Crystal Size Distribution (CSD) analysis of plagioclase phenocrysts yields a linear slope $s = -0.12\text{ mm}^{-1}$ in a plot of $\ln(n)$ versus crystal size $L$. If the linear crystal growth rate is experimentally determined as $G = 1.0 \times 10^{-10}\text{ mm/s}$, calculate the average magma residence time ($\tau$) in years ($1\text{ year} \approx 3.15 \times 10^7\text{ s}$).
        </p>
        <div class="p-ans">
          <strong>Step-by-Step CSD Derivation:</strong><br>
          In steady-state CSD theory (Marsh, 1988), the population density slope $s$ is related to growth rate $G$ and residence time $\tau$ by:
          $$s = -\frac{1}{G \cdot \tau}$$<br>
          Rearranging for residence time $\tau$:
          $$\tau = -\frac{1}{G \cdot s} = \frac{1}{(1.0 \times 10^{-10}\text{ mm/s}) \times (0.12\text{ mm}^{-1})} = \frac{1}{1.2 \times 10^{-11}\text{ s}^{-1}} \approx 8.33 \times 10^{10}\text{ seconds}$$<br>
          Converting seconds to years:
          $$\tau = \frac{8.33 \times 10^{10}\text{ s}}{3.1536 \times 10^7\text{ s/year}} \approx \mathbf{2,642\text{ years}}$$<br>
          <strong>Interpretation:</strong> The plagioclase phenocrysts resided in the cooling granitic magma chamber for approximately <strong>2,640 years</strong> prior to final consolidation.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Petrographic Discrimination of Basaltic Textures</div>
        <p>
          Compare and contrast the microscopic definitions and cooling regimes of: (a) Ophitic; (b) Subophitic; (c) Intergranular; and (d) Intersertal textures.
        </p>
        <div class="p-ans">
          <strong>Textural Continuum in Mafic Rocks:</strong><br>
          1. <strong>Ophitic:</strong> Plagioclase laths are <em>completely enclosed</em> poikilitically within large, optically continuous clinopyroxene plates. (Slowest cooling among hypabyssal dolerites; thick sill cores).<br>
          2. <strong>Subophitic:</strong> Plagioclase laths are only <em>partially enclosed</em> by pyroxene crystals, with parts of the laths projecting outside. (Moderate cooling rates; medium-width dikes).<br>
          3. <strong>Intergranular:</strong> Plagioclase laths form an interlocking lattice, and the angular interstitial spaces are completely filled by <em>small, polygonal, granular pyroxene and iron-oxide crystals</em> without any glass. (Rapid cooling; dike margins).<br>
          4. <strong>Intersertal:</strong> The angular wedges between plagioclase laths are occupied by <em>brown amorphous volcanic glass (tachylite) or cryptocrystalline devitrified material</em>. (Very rapid cooling / subaqueous flow tops).
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Chemical Stoichiometry of the Spilitization Reaction</div>
        <p>
          Submarine basalts undergo hydrothermal metasomatism (spilitization) on the ocean floor. Write the balanced chemical reaction representing the albitization of an anorthite plagioclase component in the presence of dissolved sodium and silica in seawater, producing secondary calcite.
        </p>
        <div class="p-ans">
          <strong>Stoichiometric Reaction:</strong><br>
          $$\text{CaAl}_2\text{Si}_2\text{O}_8\ (\text{Anorthite}) + 2\text{Na}^+ + 4\text{SiO}_{2\text{ (aq)}} + \text{CO}_3^{2-} \longrightarrow 2\text{NaAlSi}_3\text{O}_8\ (\text{Albite}) + \text{CaCO}_3\ (\text{Calcite})$$<br>
          <strong>Geochemical Significance:</strong> Calcic plagioclase ($\text{An}_{50\text{--}70}$) is unstable in the presence of heated, circulating seawater ($T \approx 200\text{--}350^\circ\text{C}$). Seawater donates $Na^+$ while leaching $Ca^{2+}$, transforming the basalt into a spilite dominated by albite, chlorite, epidote, and calcite amygdules.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Geopetal Younging Criteria in Submarine Pillow Basalts</div>
        <p>
          A structural geologist mapping an overturned Archean greenstone belt encounters deformed pillow lavas. Explain how the cross-sectional geometry of individual pillows indicates the original stratigraphic "way-up" (younging direction).
        </p>
        <div class="p-ans">
          <strong>Geopetal Criteria:</strong><br>
          1. <strong>Convex Upper Surface:</strong> As hot lava buds from a feeder tube, buoyancy and surface tension cause the top surface of the pillow to expand smoothly upward, forming a broad, convex-upward dome.<br>
          2. <strong>Cuspidate V-shaped Base (Pedicle):</strong> The soft, plastic bottom of the expanding pillow sags under gravity into the triangular cusp or indentation formed between the two underlying, pre-existing pillows, producing a downward-pointing tail or "keel" (V-shaped pedicle).<br>
          3. <strong>Vesicle Zonation:</strong> Gas vesicles are concentrated near the top margin of the pillow due to buoyant upward gas migration before quenching.<br>
          <strong>Deduction:</strong> The smooth rounded curve points to <strong>stratigraphic TOP (younger)</strong>; the pointed V-shaped cusp points to <strong>stratigraphic BASE (older)</strong>.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Thermal Profiling of a Dolerite Dike Chilled Margin</div>
        <p>
          A vertical dolerite dike of thickness $w = 10\text{ meters}$ intrudes cold country rock ($T_0 = 20^\circ\text{C}$). The magma enters at its liquidus temperature ($T_m = 1180^\circ\text{C}$). Using Jaeger's (1968) thermal contact solution, calculate the immediate contact temperature ($T_c$) at the dike wall and describe the resulting texture.
        </p>
        <div class="p-ans">
          <strong>Thermal Contact Derivation:</strong><br>
          Assuming equivalent thermal properties (heat capacity and thermal conductivity) for the magma and host rock, the initial contact temperature ($T_c$) immediately upon intrusion is:
          $$T_c = \frac{T_m + T_0}{2} = \frac{1180 + 20}{2} = \frac{1200}{2} = \mathbf{600^\circ\text{C}}$$<br>
          <strong>Textural Evolution Across the Dike:</strong><br>
          - <em>At the immediate wall ($x = 0$):</em> Quenched instantly from $1180^\circ\text{C}$ to $600^\circ\text{C}$ ($\Delta T = 580^\circ\text{C}$). Extreme undercooling produces an aphanitic to glassy chilled margin (tachylite).<br>
          - <em>At the dike interior ($x = 5\text{ m}$):</em> Cooling is slow, controlled by heat conduction through the country rock. Low undercooling allows complete crystal growth, developing classic coarse <strong>ophitic texture</strong>.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Poikilitic vs. Ophitic: Terminological Demarcation</div>
        <p>
          Both poikilitic and ophitic textures describe mineral grains enclosed within larger host crystals. Explain the precise mineralogical restriction that distinguishes an ophitic texture from general poikilitic texture.
        </p>
        <div class="p-ans">
          <strong>Taxonomic Distinction:</strong><br>
          - <strong>Poikilitic Texture (General Term):</strong> A generic petrographic texture where relatively small, randomly oriented crystals of <em>any mineral phase</em> (chadacrysts) are enclosed within a much larger host crystal of a different mineral (oikocryst). Examples: Olivine enclosed in hornblende, or quartz enclosed in biotite.<br>
          - <strong>Ophitic Texture (Specific Restrictive Variety):</strong> A specialized variety of poikilitic texture strictly restricted to mafic rocks where the enclosed chadacrysts are specifically <strong>prismatic laths of plagioclase feldspar</strong>, and the enclosing oikocryst is specifically <strong>clinopyroxene (augite)</strong>.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Grain Size Boundaries in Crystalline Rocks</div>
        <p>
          State the internationally accepted metric grain size thresholds defining: (a) Fine-grained (aphanitic); (b) Medium-grained; (c) Coarse-grained; and (d) Pegmatitic crystalline rocks according to the IUGS Subcommission on the Systematics of Igneous Rocks.
        </p>
        <div class="p-ans">
          <strong>IUGS Grain Size Scales:</strong><br>
          - <strong>Fine-grained (Aphanitic):</strong> Average grain diameter $< 1.0\text{ mm}$ (individual crystals cannot be distinguished with the naked eye; e.g., basalt, rhyolite).<br>
          - <strong>Medium-grained:</strong> Average grain diameter between $1.0\text{ mm}$ and $5.0\text{ mm}$ (typical of hypabyssal rocks; e.g., dolerite, microgranite).<br>
          - <strong>Coarse-grained (Phaneritic):</strong> Average grain diameter between $5.0\text{ mm}$ and $30.0\text{ mm}$ (typical of plutonic rocks; e.g., granite, gabbro).<br>
          - <strong>Very Coarse / Pegmatitic:</strong> Giant crystals exceeding $> 30.0\text{ mm}$ (often $> 5\text{--}10\text{ cm}$), crystallized from volatile-rich, water-saturated residual pegmatitic melts.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Glass Formation and the Glass Transition Temperature ($T_g$)</div>
        <p>
          Why do high-silica rhyolitic magmas readily form natural glass (obsidian) upon subaerial cooling, whereas low-silica basaltic magmas rarely form pure glass except when quenched underwater?
        </p>
        <div class="p-ans">
          <strong>Melt Polymerization and Rheology:</strong><br>
          1. <strong>Polymerization and Viscosity:</strong> Rhyolitic magma ($SiO_2 \approx 72\text{--}75\text{ wt}\%$) has a fully polymerized, three-dimensional network of bridging oxygens ($NBO/T \approx 0$), resulting in an astronomical viscosity ($\eta \approx 10^7\text{ to } 10^9\text{ Pa}\cdot\text{s}$). During subaerial cooling, high viscosity impedes the diffusion of ions to crystal growth sites, freezing the disordered liquid structure into glass even under moderate subaerial cooling rates.<br>
          2. <strong>Basaltic Depolymerization:</strong> Basaltic magma ($SiO_2 \approx 48\text{--}50\text{ wt}\%$) is rich in network-modifying cations ($Mg^{2+}, Fe^{2+}, Ca^{2+}$) with high non-bridging oxygens ($NBO/T \approx 0.6\text{--}0.8$), giving it an extremely low viscosity ($\eta \approx 10\text{--}100\text{ Pa}\cdot\text{s}$). Rapid ionic diffusion allows crystals to nucleate and grow rapidly; pure glass can only form when basalt is violently quenched in cold water ($dT/dt > 100^\circ\text{C/s}$).
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 77, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q077_Igneous_Textures_Matching_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q077: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q077()
