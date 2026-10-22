#!/usr/bin/env python3
"""
Q078 Generator: Ultra-Alkalic Rock Ijolite & Foidolite Petrography
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q078():
    title = r"Q078: Alkaline Igneous Rocks: Ijolite as an Ultra-Alkalic Plutonic Rock | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Alkaline Magmatism"
    h1_title = "Q078: Ultra-Alkalic Rocks: Ijolite Petrography & Foidolite Magmatism"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 78<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 2: Classification of Igneous Rocks / Foidolites, p. 28; Ch. 19: Alkaline Igneous Rocks); Anthony Hall, <em>Igneous Petrology</em> (Longman, Ch. 11: Alkaline Rocks); Daniel S. Barker, <em>Igneous Rocks</em> (Prentice-Hall); R.W. Le Maitre, <em>Igneous Rocks: A Classification and Glossary of Terms (IUGS)</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION OF ULTRA-ALKALIC ROCKS AND FOIDOLITES -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition of Ultra-Alkalic Rocks & the IUGS Foidolite Suite</div>
    <div class="card-body">
      <p>
        In igneous petrology, <strong>alkaline rocks</strong> are defined as magmas whose molecular alkali-to-alumina ratio $\frac{\text{Na}_2\text{O} + \text{K}_2\text{O}}{\text{Al}_2\text{O}_3}$ or alkali-to-silica ratio is unusually high, such that minerals deficient in silica—most notably <strong>feldspathoids (foids: nepheline, leucite, kalsilite, sodalite)</strong>—appear in the norm or mode.
      </p>
      <p>
        The designation <strong>ultra-alkalic</strong> (or hyper-alkaline) is reserved for extraordinary plutonic rocks where silica deficiency is so profound that <strong>true feldspars (plagioclase and alkali feldspar) are completely excluded</strong> from the mineral assemblage. In the standard IUGS QAPF classification (Le Maitre, 2002; Winter, 2014, p. 28), these rocks plot in <strong>Field 15 (Foidolites)</strong>, where feldspathoids comprise greater than $60\%$ (and frequently $100\%$) of the light felsic minerals.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q78/winter_p28_iugs_plutonic_ijolite.png" alt="IUGS QAPF Plutonic Classification and Foidolite Field from Winter">
        <div class="figure-caption">
          <strong>Figure 78.1 — IUGS QAPF Classification & Field 15 (Foidolites):</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 2). Highlighting the ultra-alkalic, feldspar-free Foidolite field containing the Urtite-Ijolite-Melteigite series.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE URTITE-IJOLITE-MELTEIGITE CLAN -->
  <div class="card">
    <div class="card-header bg-indigo">2. Petrography of the Urtite-Ijolite-Melteigite Series</div>
    <div class="card-body">
      <p>
        The classic plutonic suite of feldspar-free, nepheline-clinopyroxene rocks is known as the <strong>Ijolite Series</strong> (named after the type locality at Iivaara / Ijola, Kuusamo, Finland). The rocks are classified strictly on the basis of their <strong>Color Index ($M'$)</strong>, representing the modal percentage of dark mafic minerals:
      </p>

      <h4>The Three Members of the Ijolite Series</h4>
      <ul>
        <li><strong>Urtite ($M' = 0\text{--}30\%$):</strong> Leucocratic end-member, consisting predominantly of <strong>nepheline ($>70\text{--}90\%$)</strong> with minor green aegirine-augite. (Named from Lujaur-Urt, Kola Peninsula).</li>
        <li><strong>Ijolite ($M' = 30\text{--}70\%$):</strong> The quintessential mesocratic ultra-alkalic rock, consisting of approximately equal proportions of <strong>nepheline ($30\text{--}70\%$) and sodic clinopyroxene (aegirine or aegirine-augite, $30\text{--}70\%$)</strong>. Feldspars are completely absent! Common accessory minerals include titanium-rich black andradite garnet (<strong>melanite</strong>), fluorapatite, titanite (sphene), perovskite, and primary magmatic calcite.</li>
        <li><strong>Melteigite ($M' = 70\text{--}90\%$):</strong> Melanocratic end-member, dominated by <strong>aegirine-augite ($>70\%$)</strong> with subordinate interstitial nepheline ($10\text{--}30\%$). (Named from Melteig, Fen complex, Norway).</li>
      </ul>
      <div class="formula-box">
        <strong>Mineralogical Archetype of Ijolite:</strong><br>
        $$\mathbf{\text{Ijolite}} = \mathbf{\text{Nepheline (30--70\%)}} + \mathbf{\text{Aegirine-Augite (30--70\%)}} + \text{Melanite Garnet} + \text{Apatite} \quad [\mathbf{\text{Feldspar = 0\%}}]$$
      </div>
    </div>
  </div>

  <!-- CARD 3: PETROGENESIS AND CARBONATITE-FENITE COMPLEXES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Geodynamic Setting, Carbonatite Association & Fenitization</div>
    <div class="card-body">
      <p>
        Ijolites never occur as isolated regional batholiths; instead, they are diagnostic components of <strong>alkaline-carbonatite ring complexes</strong> emplaced within intra-continental rift valleys (e.g., East African Rift, Kola Alkaline Province in Russia, Fen Complex in Norway, and the <strong>Amba Dongar complex in Gujarat, India</strong>).
      </p>

      <h4>Petrogenesis and Liquid Immiscibility</h4>
      <ul>
        <li><strong>Primary Carbonated Mantle Melting:</strong> Primary carbonated nephelinite magmas are generated by extremely low degrees of partial melting ($F < 2\text{--}5\%$) of deep, volatile-metasomatized sub-continental lithospheric mantle (SCLM) at depths $> 100\text{ km}$ ($P > 3.0\text{ GPa}$) in the presence of high $CO_2$ and $H_2O$.</li>
        <li><strong>Silicate-Carbonatite Unmixing:</strong> As the primary nephelinitic melt ascends and decompresses into crustal chambers, it intersects a two-liquid miscibility gap, unmixing into an ultra-alkaline silicate melt (crystallizing as <strong>ijolite</strong>) and a conjugate carbonate-rich liquid (crystallizing as <strong>carbonatite</strong>: sovite/alvikite).</li>
        <li><strong>Fenitization (Alkali Metasomatism):</strong> The extreme alkali enrichment of ijolitic and carbonatitic intrusions generates intense hydrothermal exsolution of sodium-potassium-rich fluids. These reactive fluids invade surrounding granitic and gneissic country rocks, leaching silica and quartz while metasomatically replacing host minerals with aegirine, sodic amphibole (riebeckite/arfvedsonite), and alkali feldspar—a process termed <strong>fenitization</strong>.</li>
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
        <div class="q-num">Question 78</div>
        <div class="q-text">Which of the following is an ultra-alkalic rock ?</div>
        <div class="q-options">
          <div class="opt-node">(A) Adamellite</div>
          <div class="opt-node">(B) Rhyodacite</div>
          <div class="opt-node">(C) Trondhjemite</div>
          <div class="opt-node correct">(D) Ijolite</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (D)</div>
        <div><strong>Ijolite:</strong> An ultra-alkalic, feldspar-free plutonic rock composed essentially of nepheline (30–70%) and sodic pyroxene (aegirine-augite), plotting in the Foidolite field of the IUGS QAPF classification.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Adamellite — INCORRECT</div>
        <p>
          <em>Adamellite</em> is the classic European petrographic synonym for <strong>Quartz Monzonite</strong> (IUGS Field 8). It is a subalkaline, quartz-bearing granitoid consisting of roughly equal proportions of alkali feldspar and plagioclase with 5–20% quartz. It is completely subalkaline to calc-alkaline and contains abundant silica, making it the diametric opposite of an ultra-alkalic rock.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Rhyodacite — INCORRECT</div>
        <p>
          <em>Rhyodacite</em> is a subalkaline, volcanic intermediate-to-felsic rock compositional equivalent to granodiorite. It is characterized by phenocrysts of plagioclase, quartz, and biotite/hornblende in a fine-grained, silica-oversaturated groundmass ($SiO_2 \approx 66\text{--}72\%$). It belongs to typical calc-alkaline subduction arc suites.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Trondhjemite — INCORRECT</div>
        <p>
          <em>Trondhjemite</em> is a leucocratic variety of tonalite belonging to the famous Archean <strong>TTG suite (Tonalite-Trondhjemite-Granodiorite)</strong>. It consists almost entirely of sodic plagioclase (oligoclase) and quartz, with $<10\%$ K-feldspar and minor biotite. It is strongly subalkaline, metaluminous to peraluminous, and completely devoid of feldspathoids.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(D) Ijolite — CORRECT</div>
        <p>
          <em>Ijolite</em> is the classic, textbook archetype of an <strong>ultra-alkalic plutonic rock</strong> (Winter, 2014, p. 28, 412). It is a foidolite composed exclusively of <strong>nepheline and aegirine-augite</strong> with total exclusion of feldspars. Its agpaitic index, extreme silica-undersaturation, and association with carbonatites firmly establish it as ultra-alkalic.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Petrographic Comparison of Alkaline and Subalkaline Rock Suites</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Rock Name</th>
            <th>Magma Series</th>
            <th>IUGS QAPF Field</th>
            <th>Essential Mineralogy</th>
            <th>Feldspar Content</th>
            <th>Silica Saturation State</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Ijolite</strong></td>
            <td><strong>Ultra-Alkalic (Foidolitic)</strong></td>
            <td><strong>Field 15 (Foidolite)</strong></td>
            <td><strong>Nepheline (30–70%) + Aegirine-augite (30–70%)</strong></td>
            <td><strong>$0\%$ (Feldspar-free!)</strong></td>
            <td><strong>Strongly Silica-Undersaturated</strong> ($Ne$-normative)</td>
          </tr>
          <tr>
            <td><strong>Adamellite</strong></td>
            <td>Calc-Alkaline / Subalkaline</td>
            <td>Field 8 (Quartz Monzonite)</td>
            <td>Plagioclase (Oligoclase) + K-Feldspar + Quartz (5–20%)</td>
            <td>$70\text{--}85\%$ of total rock</td>
            <td>Silica-Saturated to Oversaturated ($Q$-normative)</td>
          </tr>
          <tr>
            <td><strong>Trondhjemite</strong></td>
            <td>Subalkaline (TTG Suite)</td>
            <td>Field 5 (Tonalite / Leucotonalite)</td>
            <td>Oligoclase/Andesine + Quartz ($>20\%$) + minor Biotite</td>
            <td>$50\text{--}65\%$ Plagioclase ($Kfs < 5\%$)</td>
            <td>Strongly Silica-Oversaturated ($Q > 25\%$)</td>
          </tr>
          <tr>
            <td><strong>Rhyodacite</strong></td>
            <td>Calc-Alkaline (Volcanic)</td>
            <td>Field 3b/4 (Rhyodacite / Dacite)</td>
            <td>Plagioclase + Quartz + Sanidine + Biotite phenocrysts</td>
            <td>$45\text{--}60\%$ (Phenocrysts + Glass)</td>
            <td>Strongly Silica-Oversaturated ($SiO_2 > 68\%$)</td>
          </tr>
          <tr>
            <td><strong>Nepheline Syenite</strong></td>
            <td>Alkaline</td>
            <td>Field 11 (Foid Syenite)</td>
            <td>Alkali Feldspar (Microperthite) + Nepheline ($10\text{--}60\%$)</td>
            <td>Abundant Alkali Feldspar ($>40\%$)</td>
            <td>Silica-Undersaturated</td>
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
        <div class="p-header">Problem 1: Agpaitic Index ($AI$) and Peralkalinity Quantitative Calculation</div>
        <p>
          A geochemical analysis of an ultra-alkalic plutonic rock yields the following molar concentrations: $\text{Na}_2\text{O} = 0.142\text{ mol}$, $\text{K}_2\text{O} = 0.038\text{ mol}$, and $\text{Al}_2\text{O}_3 = 0.125\text{ mol}$. Calculate the Agpaitic Index ($AI$) and classify the rock as peralkaline, metaluminous, or peraluminous.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Calculation:</strong><br>
          The Agpaitic Index ($AI$, or Peralkalinity Index) is defined as the molar ratio of total alkalis to alumina:
          $$AI = \frac{\text{Molar }(\text{Na}_2\text{O} + \text{K}_2\text{O})}{\text{Molar }\text{Al}_2\text{O}_3}$$<br>
          Substituting the molar values:
          $$AI = \frac{0.142 + 0.038}{0.125} = \frac{0.180}{0.125} = \mathbf{1.44}$$<br>
          <strong>Classification:</strong><br>
          - Since $\mathbf{AI = 1.44 > 1.0}$, the rock is strictly <strong>Peralkaline (Agpaitic)</strong>.<br>
          - Surplus sodium beyond that needed to form feldspars and feldspathoids ($(\text{Na}+\text{K}) > \text{Al}$) forces the crystallization of sodic mafic minerals, namely <strong>aegirine ($\text{NaFe}^{3+}\text{Si}_2\text{O}_6$) and arfvedsonite</strong>, characteristic of ijolites.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Color Index ($M'$) Classification in the Ijolite Series</div>
        <p>
          Point-counting modal analysis of three foidolitic plutonic thin sections from a carbonatite complex yielded the following modal percentages:<br>
          - Sample A: $82\%$ Nepheline, $14\%$ Aegirine-augite, $4\%$ Melanite garnet.<br>
          - Sample B: $48\%$ Nepheline, $42\%$ Aegirine-augite, $6\%$ Melanite, $4\%$ Apatite.<br>
          - Sample C: $18\%$ Nepheline, $74\%$ Aegirine-augite, $8\%$ Titanite + Magnetite.<br>
          Classify Samples A, B, and C into their specific members of the Ijolite Series.
        </p>
        <div class="p-ans">
          <strong>Color Index ($M'$) Derivation:</strong><br>
          $M'$ is the sum of all dark, mafic, and accessory minerals ($100 - \text{Felsic Foids}$):<br>
          - <strong>Sample A:</strong> $M' = 14\% + 4\% = 18\%$. Since $M' < 30\%$, it is classified as <strong>Urtite</strong> (leucocratic foidolite).<br>
          - <strong>Sample B:</strong> $M' = 42\% + 6\% + 4\% = 52\%$. Since $M'$ is between $30\%$ and $70\%$, it is classified as <strong>Ijolite sensu stricto</strong>.<br>
          - <strong>Sample C:</strong> $M' = 74\% + 8\% = 82\%$. Since $M' > 70\%$, it is classified as <strong>Melteigite</strong> (melanocratic foidolite).
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Liquid Immiscibility: Silicate-Carbonatite Unmixing</div>
        <p>
          Explain why ijolite and carbonatite rocks are intimately associated in space and time within alkaline complexes, citing experimental phase equilibria in the system $\text{Na}_2\text{O}\text{--}\text{CaO}\text{--}\text{Al}_2\text{O}_3\text{--}\text{SiO}_2\text{--}\text{CO}_2$.
        </p>
        <div class="p-ans">
          <strong>Experimental Petrologic Mechanism:</strong><br>
          1. <strong>Miscibility Gap:</strong> Freestone & Hamilton (1980) and Kjarsgaard & Hamilton (1988) demonstrated that at crustal pressures ($0.2\text{--}0.5\text{ GPa}$) and temperatures of $850\text{--}1050^\circ\text{C}$, a primary $CO_2$-saturated nephelinitic melt enters a wide <strong>two-liquid immiscibility field</strong>.<br>
          2. <strong>Phase Separation:</strong> The homogeneous melt splits into two conjugate, immiscible liquids:
             - An <em>alkali-aluminosilicate liquid</em> enriched in $SiO_2, Al_2O_3, Na_2O$, which crystallizes as <strong>ijolite</strong>.<br>
             - A conjugate <em>alkaline-carbonatitic liquid</em> enriched in $CaO, CO_2, P_2O_5$, and LREE, which crystallizes as <strong>carbonatite (calciocarbonatite/sovite)</strong>.<br>
          3. This explains why ijolites form concentric ring dikes and plugs directly enclosing central carbonatite cores.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Chemical Impossibility of Quartz and Nepheline Coexistence</div>
        <p>
          Demonstrate thermodynamically why quartz and nepheline can never coexist in thermodynamic equilibrium in any primary igneous rock.
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Reaction:</strong><br>
          Nepheline is a silica-undersaturated feldspathoid. In the presence of free silica (quartz), it undergoes instantaneous, spontaneous reaction to form albite feldspar:
          $$\text{NaAlSiO}_4\ (\text{Nepheline}) + \text{SiO}_2\ (\text{Quartz}) \rightleftharpoons \text{NaAlSi}_3\text{O}_8\ (\text{Albite})$$<br>
          The standard Gibbs free energy of this reaction is strongly negative ($\Delta G^\circ_{298} \approx -26.5\text{ kJ/mol}$) across all magmatic temperatures and pressures. Therefore, free quartz consumes nepheline to form albite until one of the reactants is completely exhausted. Rocks containing nepheline (like ijolite) have zero modal or normative quartz.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Fenitization Halo Metasomatic Mass Balance</div>
        <p>
          Describe the mineralogical transformations that occur when a granitic country rock containing quartz ($30\%$), microcline ($40\%$), and oligoclase ($30\%$) undergoes intense fenitization by fluids exsolved from an ijolitic intrusion.
        </p>
        <div class="p-ans">
          <strong>Metasomatic Progression:</strong><br>
          1. <strong>Desilication:</strong> High-pH alkaline hydrothermal fluids dissolve quartz entirely:
             $$\text{SiO}_{2\text{ (solid)}} + 2\text{OH}^- \longrightarrow \text{H}_2\text{SiO}_4^{2-\text{ (aqueous)}}$$<br>
          2. <strong>Aegirine Formation:</strong> Sodium and ferric iron metasomatically replace host mafic minerals and quartz:
             $$\text{Fe}^{3+} + \text{Na}^+ + 2\text{SiO}_2 \longrightarrow \text{NaFe}^{3+}\text{Si}_2\text{O}_6\ (\text{Aegirine})$$<br>
          3. <strong>Alkali Feldspar Recrystallization:</strong> Oligoclase is albitized, and potassium feldspar recrystallizes into perthitic orthoclase/microcline. The resulting rock is a <strong>fenite</strong>: a quartz-free rock composed of perthite, albite, and radiating needles of aegirine.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Melanite Garnet: The Diagnostic Accessory Phase of Ijolite</div>
        <p>
          In thin section, ijolite typically contains dark brown to opaque dodecahedral garnet crystals. Identify this garnet variety, write its chemical formula, and explain why titanium enters its crystal lattice.
        </p>
        <div class="p-ans">
          <strong>Mineralogical Characterization:</strong><br>
          - <strong>Mineral Variety:</strong> <strong>Melanite</strong> (or <strong>Schorlomite</strong> when $TiO_2 > 10\text{ wt}\%$), a titanium-rich variety of the ugrandite garnet <strong>Andradite</strong>.<br>
          - <strong>Chemical Formula:</strong> $\text{Ca}_3(\text{Fe}^{3+}, \text{Ti})_2(\text{SiO}_4, \text{Fe}^{3+}\text{O}_4)_3$, ideally $\text{Ca}_3\text{Fe}_2^{3+}\text{Si}_3\text{O}_{12}$ with up to $5\text{--}15\text{ wt}\% TiO_2$.<br>
          - <strong>Titanium Incorporation:</strong> In silica-undersaturated, alkaline ijolitic magmas, the low activity of silica ($a_{\text{SiO}_2}$) impedes the formation of sphene/titanite or ilmenite. Instead, $Ti^{4+}$ substitutes into the octahedral $Y$-site and tetrahedral $Z$-site of andradite via coupled substitutions ($\text{Ti}^{4+} + \text{Fe}^{3+} \rightleftharpoons \text{Si}^{4+} + \text{Al}^{3+}$), yielding the deep black/brown melanite garnet.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Amba Dongar Alkaline-Carbonatite Complex, Gujarat</div>
        <p>
          The Amba Dongar complex in the Chhota Udaipur alkaline sub-province of Gujarat represents India's most famous carbonatite-alkaline ring complex. Identify the spatial distribution of ijolites and carbonatites within this ring structure and its relation to Deccan volcanism.
        </p>
        <div class="p-ans">
          <strong>Indian Regional Geology:</strong><br>
          - <strong>Tectonic & Temporal Context:</strong> Emplaced at $\sim 65\text{ Ma}$, Amba Dongar is intimately associated with the terminal rifting stage of the <strong>Deccan Traps flood basalt province</strong> (Reunion hotspot interaction with the Narmada-Tapi rift zone).<br>
          - <strong>Ring Architecture:</strong> The complex forms a prominent ring dike system cutting Cretaceous Bagh Sandstones. The central volcanic diatreme depression consists of carbonatite breccia and large ring dikes of <strong>calciocarbonatite (sovite) and ankeritic carbonatite</strong>.<br>
          - <strong>Ijolite Occurrence:</strong> Ijolitic and nephelinitic plutonic bodies occur as peripheral intrusions and ring segments intimately associated with extensive fenitization of the surrounding Bagh Sandstones. It hosts world-class hydrothermal fluorite mineralization.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: CIPW Norm Calculation: Differentiating Silica Saturation</div>
        <p>
          Given the following CIPW normative mineral percentages for two igneous rocks, determine which one is an ultra-alkalic rock and explain why:<br>
          - Rock X: $Q = 14.5\%, Or = 28.0\%, Ab = 32.5\%, An = 15.0\%, Hy = 6.0\%, Mt = 2.5\%$.<br>
          - Rock Y: $Ne = 42.0\%, Di = 44.0\%, Ol = 8.0\%, Ap = 3.5\%, Mt = 2.5\%$.
        </p>
        <div class="p-ans">
          <strong>Normative Analysis:</strong><br>
          - <strong>Rock X:</strong> Contains $14.5\%$ normative Quartz ($Q$) and abundant normative feldspars ($Or + Ab + An = 75.5\%$). It is a <strong>silica-oversaturated, calc-alkaline rock (Quartz Monzonite / Adamellite)</strong>.<br>
          - <strong>Rock Y:</strong> Contains $42.0\%$ normative Nepheline ($Ne$) and zero normative quartz or feldspars ($Or = Ab = An = 0\%$). The entire felsic norm is nepheline, accompanied by dominant normative Diopside ($Di = 44\%$). This normative composition corresponds precisely to an <strong>ultra-alkalic foidolite (Ijolite)</strong>.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 78, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q078_Ultra_Alkalic_Rock_Ijolite_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q078: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q078()
