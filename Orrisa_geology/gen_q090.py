#!/usr/bin/env python3
"""
Q090 Generator: Andesite Intermediate Volcanic Petrography & Oscillatory Zoning
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q090():
    title = r"Q090: Intermediate Volcanic Petrology: Andesite Mineralogy & Oscillatory Zoning | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Volcanic Suites"
    h1_title = "Q090: Andesite: Intermediate Volcanic Rock & Oscillatory Plagioclase Zoning"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 90<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Ch. 5: Petrology / Volcanic Rocks, pp. 80, 182); John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 2: Classification of Igneous Rocks, pp. 27–31; Ch. 16: Island Arc Magmatism); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 118–122); R.W. Le Maitre, <em>Igneous Rocks: A Classification and Glossary of Terms (IUGS)</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND ETYMOLOGY OF ANDESITE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, History & Petrographic Framework of Andesite</div>
    <div class="card-body">
      <p>
        The term <strong>andesite</strong> was introduced into petrology in 1826 by Christian Leopold von Buch, derived directly from the <strong>Andes mountain range of South America</strong>, where this intermediate volcanic rock forms towering stratovolcanoes along the active continental margin.
      </p>
      <p>
        In modern igneous classification (IUGS / Le Maitre, 2002; Winter, 2014, p. 27), <strong>andesite</strong> is formally defined as an <strong>intermediate volcanic rock ($SiO_2 = 52\text{ to } 63\text{ wt}\%$)</strong>—the fine-grained extrusive equivalent of plutonic <strong>diorite</strong>.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q90/bangar_p182_andesite_petrology.png" alt="Petrology and Thin Section of Andesite from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 90.1 — Petrographic Thin Section of Porphyritic Andesite:</strong> Authentic textbook diagram from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 182). Conspicuous phenocrysts of zoned plagioclase feldspar, euhedral hornblende, and augite pyroxene set in a fine-grained pilotaxitic/hyalopilitic groundmass.
        </div>
      </div>

      <h4>Mineralogical Composition of Andesite</h4>
      <ul>
        <li><strong>Plagioclase Feldspar:</strong> The dominant mineral phase, occurring as both large phenocrysts and tiny groundmass laths. Phenocrysts characteristically exhibit <strong>compositional oscillatory normal zoning</strong>, ranging from calcic cores (<strong>labradorite / bytownite, $\text{An}_{60\text{--}75}$</strong>) to sodic rims (<strong>andesine / oligoclase, $\text{An}_{25\text{--}45}$</strong>).</li>
        <li><strong>Mafic Phenocrysts:</strong> Ferromagnesian minerals constitute $15\text{--}35\%$ of the rock, consisting of:
          <ul>
            <li><strong>Clinopyroxene:</strong> Pale green augite or diopside.</li>
            <li><strong>Orthopyroxene:</strong> Pleochroic hypersthene (defining <em>hypersthene andesite</em>).</li>
            <li><strong>Amphibole:</strong> Brown-to-green calcic hornblende or oxyhornblende, frequently displaying dark opacite reaction rims.</li>
            <li><strong>Biotite Mica:</strong> Dark brown flakes occurring in more felsic varieties.</li>
          </ul>
        </li>
        <li><strong>Groundmass:</strong> Plagioclase microlites, pyroxene granules, iron-titanium oxides (magnetite, ilmenite), and interstitial cryptocrystalline silica or glass.</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q90/bangar_p80_andesite_petrology.png" alt="Volcanic Textures in Andesite from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 90.2 — Microscopic Volcanic Groundmass Textures:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 80). Illustrating pilotaxitic (felted microlites) and hyalopilitic (microlites in glass) textures typical of andesitic lavas.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: OSCILLATORY ZONING AND MAGMATIC KINETICS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Crystallization Dynamics: The Origin of Oscillatory Plagioclase Zoning</div>
    <div class="card-body">
      <p>
        The striking <strong>oscillatory zoning</strong> in andesitic plagioclase—where the anorthite content fluctuates periodically by $5\text{--}15\text{ mol}\% \text{An}$ across dozens of concentric growth shells—is a premier natural archive of open-system crustal magma chamber dynamics:
      </p>

      <h4>Petrogenetic Mechanisms Driving Zoning</h4>
      <ol>
        <li><strong>Diffusion-Controlled Interface Kinetics:</strong> During rapid crystal growth in a cooling melt, calcium and aluminium are depleted immediately adjacent to the growing crystal face faster than they can diffuse through the viscous melt. The crystal is forced to precipitate a more sodic, albite-rich layer. Once growth slows, diffusion replenishes $Ca^{2+}$ and $Al^{3+}$, allowing another calcic layer to form.</li>
        <li><strong>Magma Chamber Convective Cycling:</strong> As plagioclase crystals circulate through thermal and pressure gradients within a convective magma chamber ($P\text{-}T$ cycling), changes in water solubility ($a_{H_2O}$) alter liquidus phase equilibria: high $P_{H_2O}$ stabilizes calcic anorthite, while degassing during ascent stabilizes sodic albite.</li>
        <li><strong>Magma Recharge & Magma Mixing:</strong> In sub-volcanic arc reservoirs (MASH zones), episodic injections of hot, primitive basaltic magma reheat the resident dacitic/andesitic magma, partially resorbing existing plagioclase rims (forming a ragged "sieve texture") followed by crystallization of a high-temperature calcic spike.</li>
      </ol>
    </div>
  </div>

  <!-- CARD 3: SUBDUCTION TECTONICS AND THE ANDESITE LINE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Geodynamic Setting: The "Andesite Line" & Continental Crust Generation</div>
    <div class="card-body">
      <p>
        Andesite is the undisputed geochemical emblem of <strong>convergent plate boundary subduction zones</strong> (island arcs and active continental margins):
      </p>
      <ul>
        <li><strong>The "Andesite Line" (Marshall, 1912):</strong> A famous global geographic and petrologic petrographic boundary circumscribing the entire Pacific Ocean basin ("Ring of Fire"). Rocks oceanward of the Andesite Line are intraplate oceanic tholeiites and alkali basalts (e.g., Hawaii, Samoa); rocks landward of the line are subduction-derived orogenic <strong>calc-alkaline andesites, dacites, and rhyolites</strong>.</li>
        <li><strong>The Continental Crust Paradox (The "Andesite Model"):</strong> The bulk continental crust has an intermediate composition equivalent to <strong>andesite ($\text{SiO}_2 \approx 60\text{ wt}\%$, $\text{Mg}\# \approx 55$)</strong> (Taylor & McLennan, 1985). Because primary mantle melts are basaltic, the continental crust must have grown through the secondary accretion and distillation of andesitic volcanic arcs throughout Earth history.</li>
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
        <div class="q-num">Question 90</div>
        <div class="q-text">An intermediate volcanic rock, usually porphyritic, consisting of plagioclase (frequently zoned from labradorite to oligoclase), pyroxene, hornblende and/or biotite is termed as :</div>
        <div class="q-options">
          <div class="opt-node">(A) Anorthosite</div>
          <div class="opt-node correct">(B) Andesite</div>
          <div class="opt-node">(C) Andesitoid</div>
          <div class="opt-node">(D) Andesinite</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (B)</div>
        <div><strong>Andesite:</strong> The premier intermediate volcanic rock, characterized by porphyritic texture with phenocrysts of zoned plagioclase (labradorite to oligoclase), pyroxene, hornblende, and biotite.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Anorthosite — INCORRECT</div>
        <p>
          <em>Anorthosite</em> is a coarse-grained <strong>plutonic monomineralic rock</strong> composed of $>90\%$ plagioclase feldspar. It is completely non-volcanic and contains $<10\%$ mafic minerals, making it diametrically opposed to an intermediate porphyritic volcanic rock containing pyroxene, hornblende, and biotite.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(B) Andesite — CORRECT</div>
        <p>
          <em>Andesite</em> is the exact, canonical definition of an <strong>intermediate volcanic rock, usually porphyritic, consisting of plagioclase (frequently zoned from labradorite to oligoclase), pyroxene, hornblende and/or biotite</strong> (Bangar, p. 182; Winter, 2014, p. 27; Mahapatra, p. 118). It is the volcanic equivalent of diorite.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Andesitoid — INCORRECT</div>
        <p>
          <em>Andesitoid</em> is an informal, provisional IUGS term proposed for rocks believed to be andesite in the field where exact chemical analysis or mineral modal counts have not yet been verified. It is not the definitive rock name.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Andesinite — INCORRECT</div>
        <p>
          <em>Andesinite</em> is an obsolete historical term occasionally applied to an anorthosite composed almost exclusively of andesine plagioclase. It is a plutonic rock, not an intermediate volcanic rock.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Systematic Igneous Classification: Volcanic vs. Plutonic Equivalents</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Chemical Category</th>
            <th>Silica Content ($\text{SiO}_2$)</th>
            <th>Plutonic Equivalent (Coarse Phaneritic)</th>
            <th>Volcanic Equivalent (Fine / Porphyritic)</th>
            <th>Essential Mineral Assemblage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Acidic (Felsic)</strong></td>
            <td>$> 66\text{ wt}\%$</td>
            <td><strong>Granite / Granodiorite</strong></td>
            <td><strong>Rhyolite / Dacite</strong></td>
            <td>Quartz ($>20\%$) + K-Feldspar + Sodic Plagioclase + Biotite</td>
          </tr>
          <tr>
            <td><strong>Intermediate</strong></td>
            <td><strong>$52\text{--}66\text{ wt}\%$</strong></td>
            <td><strong>Diorite</strong></td>
            <td><strong>ANDESITE</strong></td>
            <td><strong>Zoned Plagioclase (Labradorite to Oligoclase) + Hornblende + Augite $\pm$ Biotite</strong></td>
          </tr>
          <tr>
            <td><strong>Basic (Mafic)</strong></td>
            <td>$45\text{--}52\text{ wt}\%$</td>
            <td><strong>Gabbro</strong> (Hypabyssal: Dolerite)</td>
            <td><strong>Basalt</strong></td>
            <td>Calcic Plagioclase (Labradorite) + Clinopyroxene (Augite) $\pm$ Olivine</td>
          </tr>
          <tr>
            <td><strong>Ultrabasic</strong></td>
            <td>$< 45\text{ wt}\%$</td>
            <td><strong>Peridotite (Dunite / Harzburgite)</strong></td>
            <td><strong>Komatiite</strong> (Archean) / Picrite</td>
            <td>Olivine ($>40\%$) + Orthopyroxene + Clinopyroxene (Feldspar $<10\%$)</td>
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
        <div class="p-header">Problem 1: Optical Determination of Plagioclase Composition via the Michel-Lévy Method</div>
        <p>
          In an andesite thin section, a plagioclase phenocryst cut perpendicular to the $\{010\}$ plane displays sharp albite twin lamellae. The maximum symmetrical extinction angle measured on the core is $\theta_{\text{core}} = 33^\circ$, while the rim displays a maximum symmetrical extinction angle of $\theta_{\text{rim}} = 20^\circ$. Determine the anorthite content ($\text{An}\%$) of the core and rim using the standard Michel-Lévy determinative curve and classify the zoning.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Michel-Lévy Determination:</strong><br>
          1. <strong>Core Composition:</strong>
          - A maximum symmetrical extinction angle of $\theta = 33^\circ$ corresponds on the Michel-Lévy curve for plutonic/volcanic plagioclase to $\mathbf{An_{58}\text{ to } An_{60}}$ (<strong>Labradorite</strong>).<br>
          2. <strong>Rim Composition:</strong>
          - An extinction angle of $\theta = 20^\circ$ corresponds to $\mathbf{An_{37}\text{ to } An_{39}}$ (<strong>Andesine</strong>).<br>
          3. <strong>Classification of Zoning:</strong>
          - Because the core is more calcic ($\text{An}_{60}$) and the rim is more sodic ($\text{An}_{38}$), this represents classic <strong>normal compositional zoning</strong>, reflecting fractional crystallization as the magma cooled along the plagioclase liquidus-solidus loop.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Total Alkali-Silica (TAS) Coordinates for Andesite</div>
        <p>
          State the exact mathematical boundaries defining the Andesite field on the IUGS Total Alkali-Silica (TAS) volcanic classification diagram (Le Bas et al., 1986).
        </p>
        <div class="p-ans">
          <strong>TAS Diagram Coordinates:</strong><br>
          - <strong>Silica Range ($X$-axis):</strong>
          $$\mathbf{57.0\text{ wt}\% \le SiO_2 \le 63.0\text{ wt}\%}$$<br>
          (Below $57\%$, from $52\text{ to } 57\% \text{ SiO}_2$, is <em>Basaltic Andesite</em>; above $63\%$, from $63\text{ to } 68\% \text{ SiO}_2$, is <em>Dacite</em>).<br>
          - <strong>Total Alkalis Range ($Y$-axis, $\text{Na}_2\text{O} + \text{K}_2\text{O}$):</strong>
          $$\mathbf{Total\ Alkalis} < 5.9\text{ wt}\% \quad (\text{Subalkaline / Calc-Alkaline Sector})$$<br>
          If total alkalis exceed $5.9\%$, the rock enters the alkaline fields of <em>Trachyandesite</em> or <em>Shoshonite</em>.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Opacite (Black Reaction Rims) on Hornblende Phenocrysts</div>
        <p>
          Under the microscope, hornblende phenocrysts in subaerial andesitic lava flows frequently exhibit thick, opaque, black peripheral reaction rims ("opacite rims") composed of fine-grained magnetite, pyroxene, and plagioclase. Explain the physical cause of this rim during volcanic eruption.
        </p>
        <div class="p-ans">
          <strong>Decompression Degassing Mechanism:</strong><br>
          1. <strong>Magmatic Storage:</strong> Calcic amphibole (hornblende) requires high dissolved water pressure ($P_{H_2O} > 1.5\text{--}2.0\text{ kbar}$, depth $> 5\text{ km}$) to remain stable in an andesitic magma.<br>
          2. <strong>Decompression during Eruption:</strong> As the magma ascends rapidly toward the volcanic vent, confining pressure plummets, causing water to violently exsolve from the melt ($H_2O\text{ degassing}$).<br>
          3. <strong>Dehydration Breakdown:</strong> Without confining water pressure, hornblende is thrown outside its stability field and breaks down spontaneously:
          $$\text{Hornblende} \longrightarrow \text{Augite} + \text{Hypersthene} + \text{Plagioclase} + \mathbf{\text{Magnetite (Opaque / Black)}} + \text{H}_2\text{O}\uparrow$$<br>
          The microscopic magnetite grains impart a solid black "opacite" border.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Pilotaxitic vs. Hyalopilitic Groundmass Textures</div>
        <p>
          Compare the microstructures of pilotaxitic and hyalopilitic groundmasses in andesitic rocks.
        </p>
        <div class="p-ans">
          <strong>Textural Comparison:</strong><br>
          - <strong>Pilotaxitic Texture (Trachytic-like):</strong> The groundmass consists of a dense, felted, interlocking network of microcrystalline, subparallel tabular plagioclase microlites with <strong>zero or negligible interstitial glass</strong>. Microscopic pyroxene and magnetite granules fill the tiny gaps.<br>
          - <strong>Hyalopilitic Texture:</strong> The plagioclase microlites are embedded in an abundant base of <strong>dark brown, amorphous, isotropic volcanic glass</strong>. It indicates more rapid cooling and quenching near flow surfaces or margins.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Calc-Alkaline Iron Depletion Trend (Miyashiro's Ratio)</div>
        <p>
          Explain why the calc-alkaline magma series (characteristic of andesites) displays continuous iron depletion ($FeO^*/MgO$ remains low as $SiO_2$ increases) on an AFM diagram, whereas the tholeiitic series displays pronounced early iron enrichment.
        </p>
        <div class="p-ans">
          <strong>Oxygen Fugacity and Magnetite Crystallization:</strong><br>
          - <strong>Calc-Alkaline Series (Andesites):</strong> Generated in subduction zones where slab-derived hydrous fluids impart a <strong>high oxygen fugacity ($f_{O_2} \ge \text{NNO}$)</strong>. High $f_{O_2}$ stabilizes early crystallization of <strong>titanomagnetite ($\text{Fe}_3\text{O}_4$)</strong> on the liquidus. Early extraction of magnetite strips iron out of the melt, preventing iron enrichment and driving differentiation directly toward silica-rich, iron-depleted andesites and dacites.<br>
          - <strong>Tholeiitic Series:</strong> Anhydrous, low $f_{O_2}$ conditions delay magnetite precipitation, concentrating iron into the residual liquid until late stages (Fenner / Skaergaard trend).
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: The "Andesite Model" for the Growth of Continental Crust</div>
        <p>
          According to S.R. Taylor & S.M. McLennan (1985), the bulk chemical composition of Earth's continental crust is identical to that of an orogenic andesite. Why does this create a mass-balance problem, and how is it resolved?
        </p>
        <div class="p-ans">
          <strong>The "Andesite Paradox" and Crustal Distillation:</strong><br>
          1. <strong>The Mass Balance Problem:</strong> Primary partial melting of the peridotitic mantle yields <em>basaltic</em> liquids ($SiO_2 \approx 48\text{--}50\%$), not andesite ($SiO_2 \approx 60\%$). If continental crust was generated directly from the mantle, why is it andesitic rather than basaltic?<br>
          2. <strong>Resolution (Lower Crustal Delamination):</strong> Primary basaltic magmas underplate the base of volcanic arcs. Differentiation produces upper crustal andesites/dacites and dense ultramafic/mafic cumulates (garnet pyroxenites / eclogitic restites, $\rho > 3.4\text{ g/cm}^3$) in the deep crust. Being denser than the underlying asthenosphere, the lower mafic cumulates founder and sink (delaminate) back into the mantle, leaving behind the buoyant, preserved <strong>andesitic continental crust</strong>.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Viscosity and Explosive Volcanism of Andesite Magma</div>
        <p>
          Why do andesitic volcanoes (e.g., Krakatoa, Mount St. Helens, Merapi) exhibit catastrophic explosive Plinian eruptions, whereas basaltic volcanoes (e.g., Kilauea, Mauna Loa) produce gentle effusive lava fountains?
        </p>
        <div class="p-ans">
          <strong>Viscosity and Gas Overpressure:</strong><br>
          1. <strong>Viscosity:</strong> Andesitic magma has a much higher silica content ($SiO_2 \approx 58\text{--}62\%$) and lower temperature ($T \approx 900\text{--}1050^\circ\text{C}$), giving it a viscosity ($10^4\text{--}10^6\text{ Pa}\cdot\text{s}$) that is <strong>10,000 times higher</strong> than fluid basalt ($10\text{--}100\text{ Pa}\cdot\text{s}$).<br>
          2. <strong>Volatile Content:</strong> Subduction-related andesites contain $3\text{--}6\text{ wt}\% H_2O$. As magma ascends, exsolving gas bubbles cannot escape through the viscous, sticky liquid.<br>
          3. <strong>Catastrophic Fragmentation:</strong> Trapped gas overpressure builds until the bubble walls exceed their tensile strength, resulting in violent explosive fragmentation of the magma column into pyroclastic flows and ash clouds.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Sieve Texture (Fritted Plagioclase) as a Magma Mixing Proxy</div>
        <p>
          In an andesite thin section, several plagioclase phenocrysts contain a spongy, cellular zone filled with glassy inclusions ("sieve texture") sandwiched between a clear core and a clear overgrowth rim. Explain the magmatic history recorded by this texture.
        </p>
        <div class="p-ans">
          <strong>Magma Mixing and Thermal Dissolution History:</strong><br>
          1. <strong>Early Stage:</strong> Plagioclase grew slowly in an evolved, cooler dacitic/andesitic magma chamber, developing a clear sodic core ($\text{An}_{35}$).<br>
          2. <strong>Thermal/Chemical Shock:</strong> An injection of hot, primitive basaltic magma intruded the chamber. The sudden increase in temperature ($+100^\circ\text{C}$) superheated the crystal beyond its solidus, causing partial melting and skeletal dissolution along internal cleavages, forming a spongy, perforated sieve zone.<br>
          3. <strong>Hybrid Overgrowth:</strong> After thermal equilibration and magma mixing, a new calcic plagioclase rim ($\text{An}_{60}$) precipitated smoothly over the resorbed sponge, preserving an undeniable petrographic record of <strong>magma recharge and mixing</strong>.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 90, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q090_Andesite_Intermediate_Volcanic_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q090: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q090()
