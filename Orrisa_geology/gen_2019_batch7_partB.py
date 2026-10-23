#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 7 Part B (Q084 - Q090)
Igneous Petrology: Granitoids, Textures, Emplacement Mechanisms, Lamprophyres, and Magmatic Processes.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q084: Adamellite Mineral Composition (Equal Oligoclase & K-feldspar)
# -----------------------------------------------------------------------------
def gen_q084():
    q_num = 84
    filename = "Q084_Adamellite_Contains_Equal_Amounts_Oligoclase_And_K_Feldspar_Complete_Guide.html"
    title = "Q084: Granitoid Classification - Adamellite (Quartz Monzonite) Mineralogy"
    badge = "OPSC 2019 Geology Paper-II • Question 84 • Igneous Petrology"
    h1_title = "Adamellite (Quartz Monzonite): IUGS Granitoid QAPF Systematics and Feldspar Ratios"
    meta_text = "<strong>Topic:</strong> Granitic Rock Classification • <strong>Key Concept:</strong> Sub-equal Alkali Feldspar and Plagioclase • <strong>Textbooks:</strong> IUGS Systematics of Igneous Rocks (Le Maitre, 2002); K.M. Bangar (p. 123)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Adamellite in Granitoid Systematics</div>
      <p><strong>Adamellite</strong> was named in 1898 by A. Cathrein after Mount Adamello in the Italian Alps. In classical petrography and the standard IUGS classification, adamellite is synonymous with <strong>Quartz Monzonite</strong> (Field 3b of the QAPF classification), defined as a plutonic rock where quartz comprises 20% to 60% of the felsic minerals and the ratio of plagioclase to total feldspar is roughly equal ($35\% \le P/(A+P) \le 65\%$):</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Type</th>
              <th>IUGS QAPF Field</th>
              <th>Plagioclase : Alkali Feldspar Ratio</th>
              <th>Dominant Feldspar Species</th>
              <th>Characteristic Ferromagnesian Minerals</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Alkali-Feldspar Granite</td>
              <td>Field 2</td>
              <td>$P/(A+P) < 10\%$ (Alkali Feldspar dominant)</td>
              <td>Orthoclase, Microcline, Perthite &gt;&gt; Albite</td>
              <td>Biotite, Riebeckite, Aegirine</td>
            </tr>
            <tr>
              <td>Syenogranite</td>
              <td>Field 3a</td>
              <td>$10\% \le P/(A+P) < 35\%$</td>
              <td>K-Feldspar &gt; Plagioclase</td>
              <td>Biotite &plusmn; Muscovite</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>ADAMELLITE (Quartz Monzonite)</strong></td>
              <td><strong>Field 3b</strong></td>
              <td><strong>$35\% \le P/(A+P) \le 65\%$ (Roughly EQUAL)</strong></td>
              <td><strong>Roughly equal amounts of Oligoclase & K-feldspar</strong></td>
              <td>Biotite, Hornblende</td>
            </tr>
            <tr>
              <td>Granodiorite</td>
              <td>Field 4</td>
              <td>$65\% < P/(A+P) \le 90\%$ (Plagioclase dominant)</td>
              <td>Oligoclase/Andesine &gt; K-Feldspar</td>
              <td>Hornblende &gt; Biotite</td>
            </tr>
            <tr>
              <td>Tonalite (Trondhjemite)</td>
              <td>Field 5</td>
              <td>$P/(A+P) > 90\%$ (Extreme Plagioclase)</td>
              <td>Andesine/Oligoclase &gt;&gt; K-Feldspar</td>
              <td>Hornblende, Biotite</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Adamellite is a variety of granite containing <strong>roughly equal amounts of orthoclase (K-feldspar) and plagioclase (normally oligoclase)</strong>, with 20% to 60% quartz. In Br&oslash;gger's terminology and modern IUGS usage, it is referred to as quartz monzonite. When plagioclase exceeds two-thirds of total feldspar, the rock grades into granodiorite; when potash feldspar exceeds two-thirds, it becomes normal granite (syenogranite)."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Petrology Section, pp. 122&ndash;124)</div>
      </div>

      <div class="formula-box">
        $$\text{Feldspar Ratio in Adamellite: } \frac{\text{Plagioclase (Oligoclase)}}{\text{Alkali Feldspar (K-spar)} + \text{Plagioclase}} \approx 0.35 \text{ to } 0.65 \implies \mathbf{Plagioclase \approx K\text{-}feldspar}$$
        $$\text{Quartz Content: } 20\% \le Q \le 60\% \quad \text{of Total } (Q + A + P)$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q084/adamellite_quartz_monzonite_qapf_diagram.png" alt="Adamellite Quartz Monzonite QAPF Diagram" class="figure-img">
        <div class="figure-caption">Figure 84: IUGS QAPF classification of granitoids highlighting Field 3b (Adamellite / Quartz Monzonite) positioned at the balanced center where Oligoclase and K-feldspar are roughly equal.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 84</div>
        <div class="raw-q-text">Adamellite contains :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Roughly equal amounts of Oligoclase and K-feldspar</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Roughly equal amounts of Quartz and Oligoclase</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Roughly equal amounts of Quartz and K-feldspar</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Roughly equal amounts of Quartz and Albite</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Roughly equal amounts of Oligoclase and K-feldspar)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Roughly equal amounts of Oligoclase and K-feldspar</div>
          <p>By international and Indian petrological definition, <strong>adamellite</strong> (quartz monzonite) is specifically distinguished from granite sensu stricto and granodiorite by possessing <strong>roughly equal proportions of plagioclase (oligoclase) and potash feldspar (orthoclase/microcline)</strong> ($P/(A+P)$ ratio of approximately 1:1, or between 35:65 and 65:35).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Roughly equal amounts of Quartz and Oligoclase</div>
          <p>Granitoid classifications are fundamentally based on the ratio between the two feldspar phases ($A$ vs $P$), not the ratio between quartz and plagioclase. In adamellite, total feldspar comprises 50% to 70% of the rock, while quartz makes up only 20% to 35%.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Roughly equal amounts of Quartz and K-feldspar</div>
          <p>This is incorrect. Quartz and K-feldspar do not define adamellite; a rock with equal quartz and K-feldspar but little plagioclase is a syenogranite or alkali-feldspar granite.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Roughly equal amounts of Quartz and Albite</div>
          <p>Albite ($An_0\text{--}An_{10}$) is the sodic alkali feldspar characteristic of rare peralkaline granites. Adamellite typically contains calcic-sodic plagioclase in the range of <strong>oligoclase</strong> ($An_{10}\text{--}An_{30}$) alongside microcline/orthoclase.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Name</th>
              <th>Plagioclase Content</th>
              <th>K-Feldspar Content</th>
              <th>$P / (A + P)$ Ratio</th>
              <th>IUGS Formal Name</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Granite (sensu stricto)</td><td>Low to moderate (10&ndash;35%)</td><td>Dominant (65&ndash;90%)</td><td>$0.10 &ndash; 0.35$</td><td>Syenogranite</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Adamellite (Option A)</td><td><strong>Sub-equal (35&ndash;65%)</strong></td><td><strong>Sub-equal (35&ndash;65%)</strong></td><td><strong>$0.35 &ndash; 0.65$</strong></td><td><strong>Quartz Monzonite</strong></td></tr>
            <tr><td>Granodiorite</td><td>Dominant (65&ndash;90%)</td><td>Subordinate (10&ndash;35%)</td><td>$0.65 &ndash; 0.90$</td><td>Granodiorite</td></tr>
            <tr><td>Tonalite</td><td>Overwhelming (&gt;90%)</td><td>Trace (&lt;10%)</td><td>$&gt; 0.90$</td><td>Tonalite (Trondhjemite)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the volcanic extrusive equivalent of Adamellite (Quartz Monzonite)?</div>
        <div class="pq-ans">Answer: Quartz Latite (or Rhyodacite)</div>
        <div class="pq-exp">Quartz latite contains phenocrysts of both plagioclase and sanidine in roughly equal amounts within a fine-grained silicic groundmass.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Who introduced the term 'monzonite' and from which type area is it derived?</div>
        <div class="pq-ans">Answer: Albert de Lapparent (1864), from Mount Monzoni in the Italian Dolomites.</div>
        <div class="pq-exp">Monzoni in Northern Italy is the type locality for intermediate plutonic rocks having equal alkali feldspar and plagioclase.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between monzonite and quartz monzonite (adamellite)?</div>
        <div class="pq-ans">Answer: Monzonite has &lt;5% modal quartz; quartz monzonite (adamellite) has 5% to 20% (or 20-60% in QAPF) quartz.</div>
        <div class="pq-exp">Monzonite is silica-saturated/intermediate, while quartz monzonite is oversaturated and acidic.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the specific composition of oligoclase plagioclase found in adamellites?</div>
        <div class="pq-ans">Answer: $An_{10}$ to $An_{30}$ ($10\%\text{--}30\%$ anorthite, $70\%\text{--}90\%$ albite).</div>
        <div class="pq-exp">Oligoclase is the classic intermediate-sodic plagioclase of acid plutonic rocks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which batholith in North America contains enormous volumes of adamellite/quartz monzonite?</div>
        <div class="pq-ans">Answer: The Sierra Nevada Batholith and Idaho Batholith</div>
        <div class="pq-exp">Mesozoic subduction-related cordilleran batholiths are predominantly composed of granodiorite, adamellite, and tonalite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the characteristic dark mineral in adamellites?</div>
        <div class="pq-ans">Answer: Biotite mica &plusmn; common hornblende</div>
        <div class="pq-exp">Adamellites are calc-alkaline rocks typically carrying 10-15% mafics, dominated by brown biotite and dark green hornblende.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why did the IUGS Subcommission recommend replacing 'adamellite' with 'quartz monzonite'?</div>
        <div class="pq-ans">Answer: To create a consistent, systematic root-name hierarchy based on QAP modal parameters.</div>
        <div class="pq-exp">IUGS (1973, 2002) preferred 'quartz monzonite' for Field 3b, but recognized adamellite as an established historical synonym.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What texture is produced when plagioclase cores in adamellite are mantled by alkali feldspar?</div>
        <div class="pq-ans">Answer: Anti-rapakivi texture</div>
        <div class="pq-exp">Rapakivi texture is K-feldspar mantled by plagioclase; the reverse (plagioclase mantled by K-feldspar) is anti-rapakivi.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q085: Graphic Texture in Pegmatite
# -----------------------------------------------------------------------------
def gen_q085():
    q_num = 85
    filename = "Q085_Graphic_Texture_Normally_Exhibited_By_Pegmatite_Complete_Guide.html"
    title = "Q085: Igneous Textures - Graphic Texture in Pegmatites"
    badge = "OPSC 2019 Geology Paper-II • Question 85 • Igneous Petrology"
    h1_title = "Graphic (Runic) Texture: Eutectic Crystallization in Granitic Pegmatites"
    meta_text = "<strong>Topic:</strong> Igneous Textures & Pegmatites • <strong>Key Concept:</strong> Quartz-Feldspar Simultaneous Eutectic Intergrowth • <strong>Textbooks:</strong> K.M. Bangar (p. 115); John D. Winter (Principles of Igneous Petrology)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Origin & Morphology of Graphic Texture</div>
      <p><strong>Graphic texture</strong> (also termed <em>runic texture</em> or <em>micrographic texture</em>) is a distinctive magmatic intergrowth texture where angular, wedge-shaped, or hook-shaped rods of <strong>quartz</strong> are enclosed within a single optically continuous host crystal of <strong>alkali feldspar</strong> (microcline or orthoclase). In cross-section, the skeletal quartz crystals strikingly resemble ancient cuneiform, Arabic, or runic writing:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Petrological Characteristic</th>
              <th>Physicochemical Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td>Host Rock Type</td>
              <td><strong>Granitic Pegmatite</strong> (Option B)</td>
              <td>Exhibited magnificently in coarse pegmatite border and wall zones (often termed <em>graphic granite</em>).</td>
            </tr>
            <tr>
              <td>Host Mineral</td>
              <td><strong>Microcline / Orthoclase</strong> (Alkali Feldspar)</td>
              <td>Forms large, single-crystal optically continuous background plates (pink, buff, or white).</td>
            </tr>
            <tr>
              <td>Intersertal Mineral</td>
              <td><strong>Quartz</strong> (Ichthyoglypts / Skeletal Rods)</td>
              <td>Parallel three-dimensional rods of quartz that extinguish simultaneously under crossed polars.</td>
            </tr>
            <tr>
              <td>Petrogenetic Mechanism</td>
              <td><strong>Simultaneous Eutectic Crystallization</strong></td>
              <td>Precipitates at the granite eutectic minimum in volatile-rich, undercooled residual pegmatitic melts.</td>
            </tr>
            <tr>
              <td>Phase Ratio</td>
              <td><strong>$\sim 72\text{--}75\%$ Feldspar : $25\text{--}28\%$ Quartz</strong></td>
              <td>Matches precisely the eutectic proportions in the binary $SiO_2 - KAlSi_3O_8 - H_2O$ phase system at water-vapor pressures.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Graphic texture is an intimate intergrowth of quartz and alkali feldspar in which the quartz forms angular, skeletal grains resembling runic inscriptions or ancient cuneiform characters. It is the hallmark texture of <strong>pegmatites</strong> (graphic granite), resulting from the simultaneous, rapid, eutectic crystallization of quartz and feldspar from a volatile-rich, fluxed residual magmatic liquid."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Petrology Section, p. 115)</div>
      </div>

      <div class="formula-box">
        $$\text{Eutectic Crystallization: Liquid } (L) \xrightarrow{\Delta T} \text{Alkali Feldspar} + \text{Quartz simultaneously}$$
        $$\text{Eutectic Phase Ratio: } \approx 72\text{ wt\% Feldspar} : 28\text{ wt\% Quartz} \quad (\text{Constant across global graphic pegmatites})$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q085/graphic_texture_runic_pegmatite_eutectic.png" alt="Graphic Texture Runic Pegmatite" class="figure-img">
        <div class="figure-caption">Figure 85: Schematic thin-section view of graphic texture in granitic pegmatite, showing skeletal quartz rods mimicking runic writing embedded in a single microcline host crystal.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 85</div>
        <div class="raw-q-text">Graphic texture is normally exhibited by :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Komatiite</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Pegmatite</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Phonolite</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Anorthosite</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Pegmatite)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Pegmatite</div>
          <p>Graphic texture is the textbook diagnostic feature of <strong>granitic pegmatites</strong> (often known commercially as <em>graphic granite</em>). It forms by the simultaneous, eutectic precipitation of skeletal quartz rods within large plates of alkali feldspar from volatile-saturated, fluxed residual fluids.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Komatiite</div>
          <p>Komatiite is an Archaean ultramafic volcanic rock characterized by <strong>spinifex texture</strong> (skeletal, bladed, or platy crystals of olivine and pyroxene caused by rapid surface supercooling). It never contains graphic quartz-feldspar intergrowths.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Phonolite</div>
          <p>Phonolite is an undersaturated alkaline volcanic rock composed of nepheline, sanidine, and aegirine. Because phonolite is silica-undersaturated (foid-bearing), free quartz cannot form, making graphic texture chemically impossible.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Anorthosite</div>
          <p>Anorthosite is a coarse-grained monomineralic plutonic rock consisting of &gt;90% plagioclase feldspar displaying cumulate and adcumulate textures, not graphic intergrowths.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Igneous Texture</th>
              <th>Intergrowing Minerals</th>
              <th>Host Rock Type</th>
              <th>Genetic Mechanism</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Graphic / Runic</strong></td><td>Quartz in Alkali Feldspar (Microcline)</td><td><strong>Pegmatite (Option B)</strong></td><td>Eutectic simultaneous crystallization in volatile melts</td></tr>
            <tr><td>Myrmekitic</td><td>Worm-like Quartz in Plagioclase</td><td>Granite / Gneiss borders</td><td>Solid-state metasomatic replacement of K-spar by Na-Ca fluids</td></tr>
            <tr><td>Perthitic</td><td>Albite lamellae in K-Feldspar host</td><td>Granite / Syenite</td><td>Subsolidus exsolution upon cooling across the solvus</td></tr>
            <tr><td>Antiperthitic</td><td>K-spar blebs in Plagioclase host</td><td>Charnockite / Granulite</td><td>Exsolution of K-feldspar from high-T plagioclase</td></tr>
            <tr><td>Spinifex</td><td>Bladed Olivine / Pyroxene needles</td><td>Komatiite (Option A)</td><td>Rapid thermal quenching of high-Mg ultramafic lava</td></tr>
            <tr><td>Ophitic</td><td>Plagioclase laths inside Augite</td><td>Dolerite / Diabase</td><td>Post-crystallization poikilitic enclosure</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. How does micrographic texture differ from granophyric texture?</div>
        <div class="pq-ans">Answer: Granophyric texture exhibits a radiating, plumose, or spherulitic intergrowth of quartz and feldspar, often in subvolcanic felsic intrusions.</div>
        <div class="pq-exp">Granophyric texture occurs at shallower depths and higher undercooling than classic coarse graphic pegmatite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What optical proof confirms that all quartz rods in a graphic granite field belong to a single continuous crystal network?</div>
        <div class="pq-ans">Answer: They extinguish simultaneously under crossed nicols (birefringence extinction).</div>
        <div class="pq-exp">Even though cross-sections appear as disconnected angular rods, all quartz units share a single three-dimensional crystallographic orientation.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between graphic texture and myrmekitic texture?</div>
        <div class="pq-ans">Answer: Graphic texture is magmatic quartz in K-feldspar; myrmekite is vermicular quartz in sodic plagioclase replacing K-feldspar.</div>
        <div class="pq-exp">Myrmekite forms by subsolidus fluid-driven metasomatism: $KAlSi_3O_8 + Na^+/Ca^{2+} \rightarrow (Na,Ca)AlSi_3O_8 + SiO_2 (quartz) + K^+$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a complex pegmatite with distinct concentric zones called?</div>
        <div class="pq-ans">Answer: Zoned pegmatite (e.g., Border zone $\rightarrow$ Wall zone $\rightarrow$ Intermediate zone $\rightarrow$ Quartz core)</div>
        <div class="pq-exp">Cameron et al. (1949) demonstrated that graphic texture typically develops in the intermediate wall zone of zoned pegmatites.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What volatile components lower the crystallization temperature of pegmatite melts to $500\text{--}650^\circ\text{C}$?</div>
        <div class="pq-ans">Answer: Water ($H_2O$), Fluorine ($F$), Boron ($B$), and Lithium ($Li$)</div>
        <div class="pq-exp">These network-modifying fluxing components depolymerize the silicate melt, reducing viscosity and enabling giant crystal growth.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In which Indian state are the world-famous Bihar Mica Belt pegmatites located?</div>
        <div class="pq-ans">Answer: Jharkhand (Koderma, Giridih, Hazaribagh districts)</div>
        <div class="pq-exp">The Koderma pegmatite belt is renowned for giant muscovite 'books', beryl, and exquisite graphic granites.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an aplite in relation to a pegmatite?</div>
        <div class="pq-ans">Answer: Aplite is a fine-grained, sugary (saccharoidal) felsic dyke rock of identical granitic composition to pegmatite.</div>
        <div class="pq-exp">Aplites crystallize rapidly due to sudden pressure-release quenching (loss of volatiles), whereas pegmatites crystallize slowly from volatile-rich fluids.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the term for the skeletal fish-hook shaped quartz grains in graphic texture?</div>
        <div class="pq-ans">Answer: Ichthyoglypts</div>
        <div class="pq-exp">Classical petrographers termed the hieroglyphic, hook-shaped quartz rods in graphic granite 'ichthyoglypts' (fish carvings).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q086: Laccolith - Domed Up Strata
# -----------------------------------------------------------------------------
def gen_q086():
    q_num = 86
    filename = "Q086_Igneous_Body_Domed_Up_Strata_Is_Laccolith_Complete_Guide.html"
    title = "Q086: Igneous Intrusions - Laccolith Domed Morphology"
    badge = "OPSC 2019 Geology Paper-II • Question 86 • Igneous Petrology"
    h1_title = "Pluton Morphology: Laccolith Mechanics and Concordant Intrusive Geometry"
    meta_text = "<strong>Topic:</strong> Forms of Igneous Rocks • <strong>Key Concept:</strong> Mushroom-Shaped Pluton with Domed Roof & Flat Floor • <strong>Textbooks:</strong> G.K. Gilbert (1877); K.M. Bangar (p. 118); G.B. Mahapatra"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Morphology & Mechanics of Concordant Intrusions</div>
      <p>In structural and igneous geology, intrusive bodies are classified as <strong>concordant</strong> when their contacts are parallel to the bedding or foliation planes of the country rock, and <strong>discordant</strong> when they cross-cut pre-existing planar structures. The classic concordant forms are defined by their geometric cross-sections:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Intrusive Form</th>
              <th>Roof Geometry</th>
              <th>Floor Geometry</th>
              <th>Structural Effect on Host Strata</th>
              <th>Magmatic Viscosity & Examples</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>LACCOLITH</strong> (Option D)</td>
              <td><strong>Arched / Convex Upward (Domed)</strong></td>
              <td><strong>Flat / Planar Horizontal</strong></td>
              <td><strong>Forces overlying sedimentary beds upward into a gentle to steep structural dome</strong>.</td>
              <td>High-viscosity felsic/intermediate melts (Henry Mountains, Utah; G.K. Gilbert, 1877).</td>
            </tr>
            <tr>
              <td><strong>Lopolith</strong></td>
              <td>Concave Upward (Depressed)</td>
              <td>Concave Upward (Saucer-shaped)</td>
              <td>Weight of intrusion sags underlying strata into a central structural basin.</td>
              <td>Huge basic to ultrabasic layered intrusions (Bushveld, South Africa; Duluth, USA).</td>
            </tr>
            <tr>
              <td><strong>Bysmalith</strong></td>
              <td>Steeply Domed / Plug-shaped</td>
              <td>Flat Floor bounded by faults</td>
              <td>Overlying strata lifted vertically like a cylindrical plug along circumscribing piston faults.</td>
              <td>Extremely viscous silicic magmas (Mt. Holmes, Yellowstone; Iddings, 1898).</td>
            </tr>
            <tr>
              <td><strong>Phacolith</strong></td>
              <td>Crescentic / Lens-shaped</td>
              <td>Concordant with fold limbs</td>
              <td>Passive filling of low-pressure crests of anticlines or troughs of synclines.</td>
              <td>Folded mountain belts (Harker, 1909).</td>
            </tr>
            <tr>
              <td><strong>Sill</strong></td>
              <td>Tabular Planar Parallel</td>
              <td>Tabular Planar Parallel</td>
              <td>Injected horizontally along bedding without doming; uniform thickness.</td>
              <td>Low-viscosity basic basaltic melts (Great Whin Sill, UK; Karoo, S. Africa).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "A <strong>laccolith</strong> is a concordant, mushroom-shaped or blister-like igneous intrusion that has an approximately flat floor and an arched or domed roof. When viscous magma is injected along bedding planes, instead of spreading laterally as a thin sill, it accumulates locally and pushes up the overlying strata into a magnificent dome or anticline."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Forms of Igneous Bodies, p. 118)</div>
      </div>

      <div class="formula-box">
        $$\text{Laccolith Mechanics: Magma Overpressure } (P_{\text{magma}}) > \text{Lithostatic Overburden Load } (\rho_{\text{rock}} g z) + \text{Bending Rigidity } (D \nabla^4 w)$$
        $$\text{Result: Overlying strata flexed into a dome } \implies \mathbf{Concordant\ Domed\ Pluton \equiv Laccolith}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q086/laccolith_vs_lopolith_bysmalith_pluton_morphology.png" alt="Laccolith vs Lopolith vs Bysmalith" class="figure-img">
        <div class="figure-caption">Figure 86: Cross-sectional comparisons of concordant igneous intrusions highlighting the domed-up roof and planar floor of a Laccolith compared to a saucer-shaped Lopolith and faulted Bysmalith.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 86</div>
        <div class="raw-q-text">An igneous body that has doomed up the strata into which it has been inserted is known as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Lopolith</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Dyke</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Bysmalith</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Laccolith</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Laccolith)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Laccolith</div>
          <p>By standard definition (G.K. Gilbert, 1877; Bangar; Mahapatra), a <strong>laccolith</strong> (from Greek <em>lakkos</em> = reservoir/cistern, and <em>lithos</em> = stone) is a concordant igneous intrusion characterized by a flat floor and a convex-upward roof that has physically arched or <strong>domed up the overlying strata</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Lopolith</div>
          <p>A lopolith is a saucer-shaped intrusion where the floor and roof are <strong>concave upward</strong> (sagged downward into a basin under magmatic weight), the exact opposite of an upward-domed laccolith.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Dyke</div>
          <p>A dyke is a <strong>discordant tabular</strong> body that cuts perpendicularly or obliquely across bedding planes. It does not dome up strata.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Bysmalith</div>
          <p>While a bysmalith is an extreme cylindrical plug-shaped offshoot of a laccolith, its roof is lifted vertically along steep <strong>bounding peripheral faults</strong> like a piston, rather than gently doming continuous flexible strata.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Form Name</th>
              <th>Concordant / Discordant</th>
              <th>Geometric Cross-Section</th>
              <th>Deformation of Country Rock</th>
              <th>Prototypical Global Locality</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Laccolith (Option D)</td><td>Concordant</td><td>Plano-convex (Flat floor, arched roof)</td><td>Domes overlying strata upward</td><td>Henry Mountains, Utah (USA)</td></tr>
            <tr><td>Lopolith</td><td>Concordant</td><td>Saucer-shaped (Centrally depressed)</td><td>Downwarps strata into syncline/basin</td><td>Bushveld Complex (South Africa)</td></tr>
            <tr><td>Phacolith</td><td>Concordant</td><td>Crescentic / Sickle-shaped</td><td>Conforms passively to fold hinges</td><td>Corndon Hill, Shropshire (UK)</td></tr>
            <tr><td>Bysmalith</td><td>Concordant / Fault-bounded</td><td>Cylindrical / Piston plug</td><td>Faults roof upward vertically</td><td>Mount Holmes, Yellowstone (USA)</td></tr>
            <tr><td>Batholith</td><td>Discordant</td><td>Huge irregular mass (&gt;100 $km^2$)</td><td>Thermal stoping & shouldering</td><td>Singhbhum Granite (India); Coast Range</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Who first described and named laccoliths in classical geological literature?</div>
        <div class="pq-ans">Answer: Grove Karl Gilbert (1877), in his classic report on the Henry Mountains of Utah.</div>
        <div class="pq-exp">G.K. Gilbert established the fundamental principles of laccolithic intrusion, hydraulic lift, and structural doming.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why do basic (basaltic) magmas typically form sills rather than laccoliths?</div>
        <div class="pq-ans">Answer: Low viscosity allows basic magma to spread laterally for long distances; viscous felsic magma pools locally, pushing up the roof.</div>
        <div class="pq-exp">Magma viscosity governs morphology: low-viscosity basalt spreads into thin extensive sills, while high-viscosity dacite/rhyolite bulges into laccoliths.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is a concordant intrusion located along the crest of an anticline or trough of a syncline called?</div>
        <div class="pq-ans">Answer: Phacolith</div>
        <div class="pq-exp">Alfred Harker (1909) coined 'phacolith' for lens-shaped intrusions that occupy fold crests or troughs where mechanical pressure is lowest.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a lopolith, and what famous igneous complex represents the world's greatest example?</div>
        <div class="pq-ans">Answer: A huge saucer-shaped intrusion with sagging floor; the Bushveld Igneous Complex of South Africa.</div>
        <div class="pq-exp">The Bushveld lopolith covers over $65,000\text{ km}^2$ and holds world-class platinum group elements (Merensky Reef) and chromite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the surface area requirement for an igneous pluton to be classified as a batholith?</div>
        <div class="pq-ans">Answer: Greater than 100 square kilometers ($> 100\text{ km}^2$)</div>
        <div class="pq-exp">By definition, discordant plutons with exposed areas $< 100\text{ km}^2$ are termed stocks or bosses; those $> 100\text{ km}^2$ are batholiths.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is a ring-dyke versus a cone-sheet?</div>
        <div class="pq-ans">Answer: Ring-dykes dip steeply outward/vertically; cone-sheets dip inward toward a common magmatic focus.</div>
        <div class="pq-exp">Cone-sheets form during upward magmatic pressure; ring-dykes form by cauldron subsidence when the magma chamber roof drops.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. How can a sill be distinguished in the field from a buried lava flow?</div>
        <div class="pq-ans">Answer: A sill produces thermal metamorphism (baking) on BOTH its top and bottom contacts and has no vesicular top; a flow only bakes its floor.</div>
        <div class="pq-exp">Sills bake both upper and lower country rocks and may contain xenoliths from both; lava flows display ropy/vesicular tops and only bake the base.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a bysmalith?</div>
        <div class="pq-ans">Answer: A plugged laccolith whose roof has been vertically uplifted along circular fault boundaries.</div>
        <div class="pq-exp">J.P. Iddings (1898) defined a bysmalith as a cylindrical plug-shaped intrusion where uplift exceeded bending limits, shearing the bounding walls.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q087: Magmatic Stoping (R.A. Daly)
# -----------------------------------------------------------------------------
def gen_q087():
    q_num = 87
    filename = "Q087_Magma_Works_Way_Into_Crust_Is_Magmatic_Stoping_Complete_Guide.html"
    title = "Q087: Pluton Emplacement - Magmatic Stoping Mechanism"
    badge = "OPSC 2019 Geology Paper-II • Question 87 • Igneous Petrology"
    h1_title = "Pluton Emplacement Mechanics: R.A. Daly's Theory of Magmatic Stoping"
    meta_text = "<strong>Topic:</strong> Magma Ascent & Emplacement Mechanisms • <strong>Key Concept:</strong> Overhead Stoping & Thermal Shattering • <strong>Textbooks:</strong> Reginald A. Daly (1903, 1914); K.M. Bangar (p. 119); John D. Winter"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Room Problem & Magmatic Stoping</div>
      <p>One of the classic conundrums in igneous geology is the <strong>'room problem'</strong>: how do huge granitic batholiths comprising thousands of cubic kilometers of magma make space for themselves as they ascend through the brittle, solid continental crust? In 1903, Harvard geologist <strong>Reginald Aldworth Daly</strong> formulated the definitive mechanical theory of <strong>Magmatic Stoping</strong> (overhead or piecemeal stoping):</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Stage</th>
              <th>Physical / Thermal Process</th>
              <th>Mechanical Consequence</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1. Thermal Shattering</td>
              <td>Extreme heat from ascending magma ($800\text{--}1100^\circ\text{C}$) establishes steep thermal gradients across the roof rock.</td>
              <td>Thermal expansion and hydraulic fracturing generate intense jointing and brecciation in country rock walls.</td>
            </tr>
            <tr>
              <td>2. Magmatic Wedging</td>
              <td>Low-viscosity volatile fluids and magma under high pressure inject into open joints and bedding planes.</td>
              <td>Disarticulates large angular blocks of country rock from the roof (overhead quarrying).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>3. Gravitational Sinking (Stoping)</strong></td>
              <td>Solid country rock blocks ($\rho \approx 2.7\text{--}2.9\text{ g/cm}^3$) are denser than the hydrous granitic melt ($\rho \approx 2.3\text{--}2.5\text{ g/cm}^3$).</td>
              <td><strong>Blocks (xenoliths) sink downward through the magma chamber, clearing space for the magma to work its way upward</strong>.</td>
            </tr>
            <tr>
              <td>4. Abyssal Assimilation</td>
              <td>Sunken xenoliths reach the hotter, deeper base of the chamber where they undergo partial melting and hybrid assimilation.</td>
              <td>Contaminates magma chemistry (crustal assimilation) leaving restite residues at depth.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "The process whereby magma works its way up into the crust of the earth by mechanically shattering, detaching, and engulfing blocks of the roof and wall rocks—which then sink through the lighter molten magma—is known as <strong>Magmatic Stoping</strong> (or overhead stoping). Proposed by R.A. Daly in 1903, it explains how batholiths cut cleanly across country rock structures without pushing them aside."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Forms of Igneous Bodies, p. 119)</div>
      </div>

      <div class="formula-box">
        $$\text{Gravitational Sinking Condition: } \rho_{\text{country rock block (xenolith)}} > \rho_{\text{magma liquid}}$$
        $$\Delta \rho = \rho_{\text{solid}} - \rho_{\text{melt}} \approx 2.75 - 2.40 = +0.35\text{ g/cm}^3 \implies \text{Downward Stokes Sinking}$$
        $$\mathbf{Upward\ Magma\ Ascent\ via\ Xenolith\ Engulfment \equiv Magmatic\ Stoping\ (Option\ C)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q087/magmatic_stoping_piecemeal_roof_shattering.png" alt="Magmatic Stoping Piecemeal Roof Shattering" class="figure-img">
        <div class="figure-caption">Figure 87: Cross-section of a magmatic chamber demonstrating overhead stoping: thermal fracturing of roof rocks, detachment and gravitational sinking of xenoliths, and upward migration of the intrusion.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 87</div>
        <div class="raw-q-text">A process whereby magma works its way up into the crust of the earth is known as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Magmatic injection</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Magmatic thrusting</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Magmatic stoping</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Magmatic intrusion</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Magmatic stoping)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Magmatic stoping</div>
          <p>By standard textbook terminology (R.A. Daly, 1903; Bangar, p. 119; Mahapatra), the classic mechanism whereby magma works its way upward through the crust by fracturing and engulfing roof blocks (which sink under gravity) is formally defined as <strong>magmatic stoping</strong> (or overhead/piecemeal stoping).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Magmatic injection</div>
          <p>Magmatic injection refers simply to the passive or forceful squirt of molten rock into pre-existing fractures or fissures (such as forming dykes and sills), not the continuous crustal penetration process described by Daly.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Magmatic thrusting</div>
          <p>Magmatic thrusting is an informal or non-standard term; forceful shouldering aside of country rock is called diapirism or forceful shouldering, not 'thrusting'.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Magmatic intrusion</div>
          <p>'Magmatic intrusion' is an umbrella general term denoting any underground entry of magma, whereas the specific process of magma working its way through roof-shattering and block sinking is specifically termed <strong>magmatic stoping</strong>.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Emplacement Mechanism</th>
              <th>Primary Physical Process</th>
              <th>Depth Domain</th>
              <th>Deformation of Country Rock</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Magmatic Stoping</strong> (Option C)</td><td>Thermal fracturing; sinking of roof blocks (xenoliths)</td><td>Brittle upper crust (&lt; 10 km)</td><td>Cross-cutting; discordant clean contacts</td></tr>
            <tr><td>Diapirism</td><td>Buoyant ductile upwelling like salt domes</td><td>Ductile middle to lower crust (&gt; 15 km)</td><td>Concordant ductile foliation and shouldering</td></tr>
            <tr><td>Cauldron Subsidence</td><td>Piston-like collapse of a central crustal cylinder</td><td>Subvolcanic to shallow crust (&lt; 5 km)</td><td>Bounded by ring-dykes and ring-faults</td></tr>
            <tr><td>Ductile Shouldering</td><td>Lateral displacement and pushing aside of wall rocks</td><td>Ductile metamorphic regimes</td><td>Intense local folding and shearing</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Who proposed the theory of magmatic stoping and in which year?</div>
        <div class="pq-ans">Answer: Reginald Aldworth Daly (1903)</div>
        <div class="pq-exp">Daly published 'The Mechanics of Igneous Intrusion' in the American Journal of Science (1903), detailing overhead stoping.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What field evidence directly supports the occurrence of magmatic stoping along pluton roofs?</div>
        <div class="pq-ans">Answer: Abundant angular xenoliths of country rock frozen in the margins and roof of the intrusion.</div>
        <div class="pq-exp">Xenolith-rich 'intrusion breccias' at contacts capture roof blocks caught in the act of detaching and sinking.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the fundamental physical requirement for stoped blocks to sink through the magma?</div>
        <div class="pq-ans">Answer: The density of the solid country rock must exceed the density of the magma melt.</div>
        <div class="pq-exp">Silicic melts have densities around $2.3\text{--}2.4\text{ g/cm}^3$, whereas solid country rocks (schists, gneisses, basalts) have densities of $2.6\text{--}3.0\text{ g/cm}^3$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is piecemeal stoping vs. cauldron stoping?</div>
        <div class="pq-ans">Answer: Piecemeal stoping involves small individual blocks; cauldron stoping involves a single giant cylindrical block sinking along ring faults.</div>
        <div class="pq-exp">Cauldron subsidence (Clough, Maufe, & Bailey, 1909) is the large-scale caldera equivalent of overhead stoping.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What chemical process occurs when stoped xenoliths dissolve and react with the surrounding magma?</div>
        <div class="pq-ans">Answer: Magmatic Assimilation (Contamination)</div>
        <div class="pq-exp">Assimilation modifies the chemical composition of the melt, often enriching it in silica, alumina, and incompatible trace elements.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the term for a fragment of foreign country rock completely enclosed within an igneous pluton?</div>
        <div class="pq-ans">Answer: Xenolith (or Accidental inclusion)</div>
        <div class="pq-exp">Xenolith (from Greek *xenos* = foreign, *lithos* = stone) is a detached piece of wall or roof rock enclosed within an igneous body.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why is magmatic stoping less effective in deep, ductile crustal environments?</div>
        <div class="pq-ans">Answer: Rocks at high temperature and confining pressure deform ductily rather than fracturing into brittle blocks.</div>
        <div class="pq-exp">In the lower crust, ductile flow promotes diapirism and ballooning rather than brittle thermal fracturing.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is 'underhand stoping' in mining, and how does it relate to Daly's geological term?</div>
        <div class="pq-ans">Answer: Daly borrowed the term 'stoping' from mining underground excavations where miners break down rock overhead or underfoot.</div>
        <div class="pq-exp">Daly adopted 'stoping' as a metaphor for nature's overhead excavation of country rock by magma.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q088: Minette is a type of Lamprophyre
# -----------------------------------------------------------------------------
def gen_q088():
    q_num = 88
    filename = "Q088_Minette_Is_A_Type_Of_Lamprophyre_Complete_Guide.html"
    title = "Q088: Lamprophyre Petrography - Minette Classification"
    badge = "OPSC 2019 Geology Paper-II • Question 88 • Igneous Petrology"
    h1_title = "Lamprophyres: Minette Petrography, Mineralogy, and Dyke-Rock Systematics"
    meta_text = "<strong>Topic:</strong> Alkaline Dyke Rocks & Lamprophyres • <strong>Key Concept:</strong> Biotite-Orthoclase Calc-Alkaline Lamprophyre • <strong>Textbooks:</strong> N.M.S. Rock (1991, Lamprophyres); K.M. Bangar (p. 128); John D. Winter"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Lamprophyre Clan & Minette Systematics</div>
      <p><strong>Lamprophyres</strong> (from Greek <em>lampros</em> = bright/glistening, and <em>phyro</em> = mixed/porphyritic; von G&uuml;mbel, 1874) are a distinctive group of melanocratic, volatile-rich ($H_2O, CO_2, F$) hypabyssal dyke rocks characterized by <strong>panidiomorphic texture</strong>, in which euhedral phenocrysts of ferromagnesian minerals (biotite/phlogopite, amphibole, or pyroxene) are set in a fine-grained groundmass of feldspars &plusmn; feldspathoids. Critically, <strong>felsic minerals NEVER form phenocrysts</strong> in true lamprophyres.</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Lamprophyre Group</th>
              <th>Dominant Mafic Phenocryst</th>
              <th>Dominant Groundmass Feldspar</th>
              <th>Lamprophyre Rock Name</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td rowspan="2"><strong>Calc-Alkaline Lamprophyres</strong> (Shoshonitic)</td>
              <td><strong>Biotite / Phlogopite</strong></td>
              <td><strong>Alkali Feldspar (Orthoclase / Sanidine)</strong></td>
              <td><strong>★ MINETTE ★ (Option D)</strong></td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Biotite / Phlogopite</strong></td>
              <td>Plagioclase Feldspar (Oligoclase/Andesine)</td>
              <td><strong>Kersantite</strong></td>
            </tr>
            <tr>
              <td rowspan="2">Amphibole / Pyroxene-Dominated</td>
              <td>Hornblende &plusmn; Diopside/Augite</td>
              <td>Alkali Feldspar (Orthoclase)</td>
              <td><strong>Vogesite</strong></td>
            </tr>
            <tr>
              <td>Hornblende &plusmn; Diopside/Augite</td>
              <td>Plagioclase Feldspar</td>
              <td><strong>Spessartite</strong></td>
            </tr>
            <tr>
              <td>Alkaline Lamprophyres</td>
              <td>Titanaugite, Kaersutite, Biotite</td>
              <td>Feldspathoids (Nepheline, Analcime) &plusmn; Plagioclase</td>
              <td>Camptonite, Monchiquite, Sannaite</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Minette is a variety of <strong>lamprophyre</strong> characterized by an abundance of glistening bronze-colored flakes of biotite (or phlogopite) set in a fine-grained groundmass consisting predominantly of orthoclase feldspar. First named from the Vosges Mountains in France, minette forms narrow dykes and sills associated with granitic plutons and continental rift zones."
        <div class="quote-author">&mdash; N.M.S. Rock, <em>Lamprophyres</em> (Blackie and Son, Glasgow, 1991)</div>
      </div>

      <div class="formula-box">
        $$\text{Calc-Alkaline Lamprophyre Diagnostic Rule:}$$
        $$\mathbf{Minette} \equiv \text{Phenocrysts: } \mathbf{Biotite / Phlogopite} + \text{Groundmass: } \mathbf{Orthoclase\ (K\text{-}Feldspar)}$$
        $$\text{Family Affiliation: } \mathbf{Lamprophyre\ (Option\ D)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q088/lamprophyre_classification_minette_vogesite_kersantite.png" alt="Lamprophyre Classification Minette Vogesite Kersantite" class="figure-img">
        <div class="figure-caption">Figure 88: Standard 2x2 classification matrix of calc-alkaline lamprophyres, showing the exact position of Minette (Biotite + Orthoclase) alongside Kersantite, Vogesite, and Spessartite.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 88</div>
        <div class="raw-q-text">Minette is a type of :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Diorite</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Tonalite</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Aplite</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Lamprophyre</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Lamprophyre)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Lamprophyre</div>
          <p>By international IUGS classification (Rock, 1991; Le Maitre, 2002; Bangar), <strong>minette</strong> is the classic type of calc-alkaline <strong>lamprophyre</strong> containing essential phenocrystic biotite/phlogopite and groundmass alkali feldspar (orthoclase).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Diorite</div>
          <p>Diorite is a coarse-grained plutonic intermediate rock composed of andesine plagioclase and hornblende. It lacks the distinctive porphyritic-panidiomorphic texture and alkali-rich lamprophyric chemistry of minette.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Tonalite</div>
          <p>Tonalite is a quartz-rich, plagioclase-dominated plutonic rock ($Q > 20\%$, $P/(A+P) > 90\%$). Minette is a melanocratic dyke rock dominated by K-feldspar and mica, not a quartz-plagioclase pluton.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Aplite</div>
          <p>Aplite is a leucocratic (light-colored), fine-grained, equigranular (saccharoidal) dyke rock dominated by quartz and feldspars ($M' < 5\%$). Minette is melanocratic ($M' > 35\text{--}50\%$), dark, and intensely porphyritic.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Class</th>
              <th>Color Index ($M'$)</th>
              <th>Texture</th>
              <th>Phenocryst Phase</th>
              <th>Groundmass Mineralogy</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Minette (Lamprophyre)</td><td>Melanocratic (35&ndash;60%)</td><td>Panidiomorphic porphyritic</td><td>Biotite / Phlogopite</td><td>Orthoclase &plusmn; Apatite, Carbonate</td></tr>
            <tr><td>Kersantite (Lamprophyre)</td><td>Melanocratic (35&ndash;60%)</td><td>Panidiomorphic porphyritic</td><td>Biotite / Phlogopite</td><td>Plagioclase (Oligoclase/Andesine)</td></tr>
            <tr><td>Aplite (Option C)</td><td>Leucocratic (&lt;5%)</td><td>Saccharoidal equigranular</td><td>None (Aphyric)</td><td>Quartz + Alkali Feldspar</td></tr>
            <tr><td>Diorite (Option A)</td><td>Mesocratic (35&ndash;65%)</td><td>Phaneritic granular</td><td>None (Equigranular)</td><td>Andesine + Hornblende</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental textural rule that distinguishes lamprophyres from all ordinary porphyries?</div>
        <div class="pq-ans">Answer: In lamprophyres, only mafic minerals form phenocrysts; felsic minerals (quartz and feldspar) are restricted to the groundmass.</div>
        <div class="pq-exp">In normal porphyries (like granite porphyry), feldspar or quartz form the phenocrysts, whereas lamprophyres exhibit strictly mafic phenocrysts.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which lamprophyre has biotite phenocrysts with PLAGIOCLASE in the groundmass?</div>
        <div class="pq-ans">Answer: Kersantite</div>
        <div class="pq-exp">Kersantite is the plagioclase-bearing counterpart of orthoclase-bearing minette.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Which lamprophyre has HORNBLENDE phenocrysts with ORTHOCLASE in the groundmass?</div>
        <div class="pq-ans">Answer: Vogesite</div>
        <div class="pq-exp">Vogesite is characterized by amphibole/clinopyroxene phenocrysts and alkali feldspar groundmass.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is panidiomorphic texture?</div>
        <div class="pq-ans">Answer: A texture in which almost all constituent mineral grains possess well-developed crystal faces (euhedral/idiomorphic).</div>
        <div class="pq-exp">Lamprophyres are renowned for panidiomorphic texture, especially prominently zoned euhedral phlogopite and hornblende.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What volatile components are unusually enriched in lamprophyre magmas?</div>
        <div class="pq-ans">Answer: $H_2O, CO_2, F, Cl, P_2O_5$, and $SO_3$</div>
        <div class="pq-exp">Abundant primary carbonates, apatite, and hydrous micas reflect deep mantle derivation with metasomatic volatile enrichment.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which Indian coalfield is famous for lamprophyre (mica-peridotite) dykes that have heat-altered coal beds into 'jhama' (natural coke)?</div>
        <div class="pq-ans">Answer: The Jharia and Raniganj Coalfields (Damodar Valley Basin)</div>
        <div class="pq-exp">Cretaceous lamprophyre dykes intruded Permian Gondwana coal seams in Jharia, pyrolyzing valuable coal into natural coke (jhama).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an ocellus (plural: ocelli) in a lamprophyre?</div>
        <div class="pq-ans">Answer: A small, spherical or rounded leucocratic globule consisting of carbonates, quartz, or feldspar formed by liquid immiscibility or late-stage gas-bubble segregation.</div>
        <div class="pq-exp">Ocelli are classic diagnostic features of lamprophyric melts, representing separated silicate or carbonate liquid droplets.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a kimberlite or lamproite in relation to lamprophyres?</div>
        <div class="pq-ans">Answer: Kimberlites and lamproites are ultra-deep potassic/ultramafic mantle rocks closely related to the lamprophyre clan that host diamonds.</div>
        <div class="pq-exp">Lamproites and kimberlites share deep volatile-rich mantle genesis and phlogopite-rich mineralogy with lamprophyres.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q089: Palingenesis - Magmatic Melting of Rocks
# -----------------------------------------------------------------------------
def gen_q089():
    q_num = 89
    filename = "Q089_Process_Of_Complete_Or_Partial_Melting_Of_Rock_Is_Palingenesis_Complete_Guide.html"
    title = "Q089: Magmatic Petrogenesis - Palingenesis & Crustal Melting"
    badge = "OPSC 2019 Geology Paper-II • Question 89 • Igneous & Metamorphic Petrology"
    h1_title = "Palingenesis & Anatexis: Complete and Partial Melting of Pre-Existing Rocks"
    meta_text = "<strong>Topic:</strong> Magma Generation & Petrogenesis • <strong>Key Concept:</strong> Rebirth of Magma from Pre-Existing Crustal Rocks • <strong>Textbooks:</strong> J.J. Sederholm (1907); P.K. Mukherjee (p. 238); K.M. Bangar; Winter"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Origin & Meaning of Palingenesis</div>
      <p>The term <strong>Palingenesis</strong> was coined in 1907 by the renowned Finnish petrologist <strong>Johannes Jakob Sederholm</strong> from the Greek roots <em>palin</em> (meaning 'again') and <em>genesis</em> (meaning 'birth' or 'creation')—literally translating to the <strong>'rebirth of magma'</strong>. In petrology, it designates the geological process of the <strong>complete or partial melting (remelting)</strong> of pre-existing crustal rocks to generate new magmatic melts:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Magmatic Process</th>
              <th>Scientific Definition</th>
              <th>Physical Mechanism & P-T Conditions</th>
              <th>Resulting Rock / Product</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>PALINGENESIS</strong> (Option D)</td>
              <td><strong>Complete or partial melting / regeneration of pre-existing rocks</strong> to yield new magma.</td>
              <td>Deep continental subduction, collisional thickening, or mantle plume underplating ($T > 650\text{--}850^\circ\text{C}$).</td>
              <td>Regenerated S-type granites, batholiths, and mobilised felsic magmas.</td>
            </tr>
            <tr>
              <td><strong>Anatexis</strong></td>
              <td>The ultra-high temperature partial melting of metamorphic rocks in-situ.</td>
              <td>Water-saturated or dehydration melting of pelites/gneisses across the wet granite solidus.</td>
              <td>Migmatites (forming <em>leucosome</em> melt and refractory <em>melanosome</em> restite).</td>
            </tr>
            <tr>
              <td><strong>Migmatization</strong></td>
              <td>The transformation of rocks into composite hybrid rocks containing metamorphic and igneous parts.</td>
              <td>Infiltration of granitic fluids or local in-situ anatectic segregation.</td>
              <td>Migmatites (banded gneisses with neosome and paleosome).</td>
            </tr>
            <tr>
              <td><strong>Assimilation</strong></td>
              <td>The incorporation, reaction, and dissolution of foreign country rocks into a pre-existing magma.</td>
              <td>Thermal melting and chemical digestion of stoped xenoliths by hotter surrounding melt.</td>
              <td>Contaminated hybrid magmas (e.g., crustally contaminated basalts).</td>
            </tr>
            <tr>
              <td><strong>Juvenile Magmatism</strong></td>
              <td>Magma derived directly from the Earth's primordial interior (mantle or core).</td>
              <td>Direct primary melting of pristine, uncontaminated peridotitic mantle.</td>
              <td>Mid-Ocean Ridge Basalts (MORB), primary picrites.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "The process of complete or partial melting of pre-existing rocks to form new magma is called <strong>palingenesis</strong> (literally, magma rebirth). Introduced by Sederholm, it describes the recycling of continental crustal sediments and metamorphic rocks into granitic batholiths during intense orogenic cycles."
        <div class="quote-author">&mdash; P.K. Mukherjee, <em>A Textbook of Geology</em> (Petrogenesis Section, p. 238)</div>
      </div>

      <div class="formula-box">
        $$\text{Palingenesis: Pre-existing Crustal Rock } \xrightarrow[\text{Collisional Orogeny}]{T \ge 700^\circ\text{C},\ P \ge 5\text{ kbar}} \text{Partial / Complete Melt} \rightarrow \mathbf{New\ Magma\ (S\text{-}type\ Granite)}$$
        $$\text{Etymology: Greek } \pi\acute{\alpha}\lambda\iota\nu\ (\text{again}) + \gamma\acute{\epsilon}\nu\epsilon\sigma\iota\varsigma\ (\text{birth}) \equiv \mathbf{'Rebirth\ of\ Magma' \equiv Palingenesis\ (Option\ D)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q089/palingenesis_crustal_melting_anatexis_cycle.png" alt="Palingenesis Crustal Melting Anatexis Cycle" class="figure-img">
        <div class="figure-caption">Figure 89: The crustal palingenesis cycle: burial of sediment $\rightarrow$ prograde metamorphism $\rightarrow$ anatexis (partial melting) $\rightarrow$ palingenetic magma coalescence and plutonic intrusion.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 89</div>
        <div class="raw-q-text">The process of complete or partial melting of a rock is known as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Migmatization</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Assimilation</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Juvenile magmatism</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Palingenesis</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Palingenesis)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Palingenesis</div>
          <p>By standard petrological definitions (J.J. Sederholm, 1907; P.K. Mukherjee, p. 238; Bangar), <strong>palingenesis</strong> is the specific geological term for the <strong>complete or partial melting</strong> of pre-existing continental crustal rocks to generate new magma.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Migmatization</div>
          <p>Migmatization is the process of generating a <em>migmatite</em>—a composite rock retaining both unmelted metamorphic paleosome and newly melted or injected granitic neosome. It does not mean the wholesale or partial melting process that produces mobile magma.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Assimilation</div>
          <p>Assimilation is the chemical dissolution and digestion of foreign country rock into an already existing, pre-formed magma. It requires a pre-existing magma host, rather than generating a brand new magma from solid rock.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Juvenile magmatism</div>
          <p>Juvenile magmatism refers to virgin magma derived directly from the Earth's deep pristine mantle that has never previously been part of the crustal rock cycle. Palingenesis is recycled crustal melting.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Petrogenetic Process</th>
              <th>Source Material</th>
              <th>Driving Heat Source</th>
              <th>Resulting Igneous / Metamorphic Product</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Palingenesis</strong> (Option D)</td><td>Pre-existing crustal rocks (pelites, gneisses)</td><td>Orogenic crustal thickening & radioactive decay</td><td>Regenerated S-type Granites & Batholiths</td></tr>
            <tr><td>Anatexis</td><td>Deep metamorphic rock</td><td>Regional thermal metamorphism</td><td>Migmatitic leucosome veins</td></tr>
            <tr><td>Assimilation (Option B)</td><td>Wall-rock / stoped xenoliths</td><td>Thermal heat from pre-existing magma</td><td>Contaminated hybrid melts</td></tr>
            <tr><td>Juvenile Magmatism (Option C)</td><td>Primordial upper mantle peridotite</td><td>Mantle convection & decompression</td><td>Primary MORB & OIB Basalts</td></tr>
            <tr><td>Metasomatism</td><td>Solid rocks exposed to fluids</td><td>Hydrothermal / pneumatolytic fluid flow</td><td>Skarns, Fenites, Greisens</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Who introduced the term 'palingenesis' to geology?</div>
        <div class="pq-ans">Answer: Johannes Jakob Sederholm (1907)</div>
        <div class="pq-exp">Sederholm coined both 'migmatite' and 'palingenesis' during his pioneering studies of the Precambrian Fennoscandian Shield of Finland.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What granite classification corresponds directly to magmas derived by the palingenesis of sedimentary source rocks?</div>
        <div class="pq-ans">Answer: S-type Granites (Chappell & White, 1974)</div>
        <div class="pq-exp">S-type (sedimentary source) granites are peraluminous, contain cordierite/garnet/muscovite, and have high initial $^{87}Sr/^{86}Sr$ ratios ($> 0.708$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between anatexis and palingenesis?</div>
        <div class="pq-ans">Answer: Anatexis is the initial physical process of partial melting in-situ; palingenesis is the complete or partial melting viewed as the rebirth of a mobile magma body.</div>
        <div class="pq-exp">Anatexis describes the melting mechanism; palingenesis emphasizes the regeneration and creation of a new magma from old rock.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the unmelted, refractory residue remaining after anatectic melting of a crustal rock called?</div>
        <div class="pq-ans">Answer: Restite (or Melanosome)</div>
        <div class="pq-exp">The low-melting quartzofeldspathic fraction forms the leucosome (melt), leaving the dark, refractory ferromagnesian residue as restite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. At what approximate temperature does water-saturated melting of granitic crust begin?</div>
        <div class="pq-ans">Answer: Around $650^\circ\text{C}$ to $680^\circ\text{C}$ at crustal pressures ($P \approx 5\text{ kbar}$).</div>
        <div class="pq-exp">The 'wet granite solidus' marks the minimum temperature required for crustal anatexis in the presence of free $H_2O$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is dehydration melting in metamorphic rocks?</div>
        <div class="pq-ans">Answer: Melting triggered by the breakdown of hydrous minerals (muscovite, biotite) without requiring an external water fluid.</div>
        <div class="pq-exp">Reactions like $Muscovite + Quartz \rightarrow K-feldspar + Sillimanite + Liquid$ release water directly into the melt phase.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is juvenile water vs. palingenetic (resurgent) water?</div>
        <div class="pq-ans">Answer: Juvenile water is virgin water from the deep mantle; palingenetic water is recycled water released from melted crustal rocks.</div>
        <div class="pq-exp">Juvenile volatiles originate from Earth's deep interior, while palingenetic volatiles were previously locked in sedimentary or hydrous crustal minerals.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the Critical Melt Fraction (CMF) or Rheological Transition Threshold in migmatites?</div>
        <div class="pq-ans">Answer: Around 25% to 40% melt fraction.</div>
        <div class="pq-exp">When melt exceeds ~30%, the solid crystal framework breaks down and the migmatite behaves as a fluid suspension capable of ascending as a magmatic diapir.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q090: Liquid Immiscibility (Unmixing of Two Liquids of Different Composition)
# -----------------------------------------------------------------------------
def gen_q090():
    q_num = 90
    filename = "Q090_Liquid_Immiscibility_Results_From_Unmixing_Two_Liquids_Different_Composition_Complete_Guide.html"
    title = "Q090: Magmatic Differentiation - Liquid Immiscibility Solvus Mechanism"
    badge = "OPSC 2019 Geology Paper-II • Question 90 • Igneous Petrology"
    h1_title = "Liquid Immiscibility: Solvus Physics, Liquid-Liquid Unmixing, and Ore Petrogenesis"
    meta_text = "<strong>Topic:</strong> Magmatic Differentiation Mechanisms • <strong>Key Concept:</strong> Two-Liquid Solvus & Unmixing of Melts • <strong>Textbooks:</strong> John D. Winter (Principles of Igneous Petrology); K.M. Bangar (p. 116); Roedder (1979)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Physicochemical Basis of Liquid Immiscibility</div>
      <p>In chemical thermodynamics and igneous petrology, <strong>liquid immiscibility</strong> refers to the thermodynamic phenomenon where a single, homogeneous silicate melt cools until it encounters a two-phase liquid boundary (the <strong>solvus</strong>), causing it to split or <strong>unmix into two coexisting, distinct liquids of different composition</strong> that cannot dissolve in one another:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Magmatic System</th>
              <th>Parent Homogeneous Melt</th>
              <th>Separated Immiscible Liquid 1</th>
              <th>Separated Immiscible Liquid 2</th>
              <th>Geological / Ore Deposit Consequence</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Silicate-Sulfide System</strong></td>
              <td>Sulfur-saturated basic magma</td>
              <td><strong>Silicate Melt</strong> ($SiO_2$-rich, Fe-poor)</td>
              <td><strong>Dense Sulfide Melt</strong> ($Fe\text{-}Ni\text{-}Cu\text{-}PGE$ liquid)</td>
              <td>World-class magmatic sulfide deposits (Sudbury, Canada; Norilsk, Russia; Kambalda).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Silicate-Carbonate System</strong></td>
              <td>$CO_2$-rich alkaline silicate melt</td>
              <td><strong>Alkaline Silicate Melt</strong> (Nephelinite / Ijolite)</td>
              <td><strong>Carbonate Melt</strong> ($Ca\text{-}Mg\text{-}Na$ rich, $SiO_2$-poor)</td>
              <td>Origin of Carbonatites and associated alkaline ring complexes (Oldoinyo Lengai, Amba Dongar).</td>
            </tr>
            <tr>
              <td><strong>Silicate-Iron Oxide System</strong></td>
              <td>Extreme Fe-rich tholeiitic differentiate</td>
              <td><strong>Silica-rich Felsic Melt</strong> (Granitic / Rhyolitic)</td>
              <td><strong>Iron-rich Mafic Melt</strong> (Magnetite-Apatite liquid)</td>
              <td>Kiruna-type magnetite-apatite deposits; Skaergaard intrusion late-stage splits.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Liquid immiscibility is the process by which a single homogeneous liquid phase splits upon cooling into <strong>two distinct liquid phases of different compositions</strong> that are mutually insoluble, just like oil and water. In silicate systems, this solvus unmixing produces conjugate liquids such as an iron-rich basic melt and a silica-rich felsic melt, or a silicate melt and a sulfide ore melt."
        <div class="quote-author">&mdash; Edwin Roedder, <em>Silicate Liquid Immiscibility in Magmas</em> (Evolution of the Igneous Rocks, 1979)</div>
      </div>

      <div class="formula-box">
        $$\text{Thermodynamic Solvus Condition: } \Delta G_{\text{mixing}} = \Delta H_{\text{mixing}} - T \Delta S_{\text{mixing}} > 0 \quad (\text{at } T < T_{\text{solvus}})$$
        $$\mathbf{Homogeneous\ Single\ Melt\ (L_0)} \xrightarrow{T \le T_{\text{solvus}}} \mathbf{Liquid\ 1\ (L_1)} + \mathbf{Liquid\ 2\ (L_2)} \quad (\text{Distinct Compositions})$$
        $$\therefore \text{Liquid immiscibility results from: } \mathbf{Unmixing\ of\ two\ liquids\ of\ different\ composition\ (Option\ C)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q090/liquid_immiscibility_silicate_melt_phase_diagram.png" alt="Liquid Immiscibility Solvus Phase Diagram" class="figure-img">
        <div class="figure-caption">Figure 90: Binary phase diagram illustrating the liquid immiscibility dome (solvus), showing a homogeneous single melt separating into two coexisting immiscible liquids of different composition upon cooling.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 90</div>
        <div class="raw-q-text">Liquid imissibility generally results from :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Mixing of two liquids of two different composition</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Mixing of two liquids of same composition</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Unmixing of two liquids of different composition</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Unmixing of two liquids of same composition</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Unmixing of two liquids of different composition)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Unmixing of two liquids of different composition</div>
          <p>By definition in physical chemistry and petrology, <strong>liquid immiscibility</strong> is the <strong>unmixing</strong> (separation or exsolution) of a parent homogeneous liquid into <strong>two coexisting liquids having different chemical compositions</strong> (e.g., a sulfide liquid vs. a silicate liquid, or a carbonate liquid vs. a silicate liquid) because they are mutually insoluble below their solvus temperature.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Mixing of two liquids of two different composition</div>
          <p>This defines <strong>magma mixing</strong> or hybridization, which is the exact opposite of immiscibility. Mixing combines two melts into one; immiscibility unmixes one melt into two.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Mixing of two liquids of same composition</div>
          <p>Mixing identical liquids produces the same liquid without any change, neither creating immiscibility nor generating differentiated phases.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Unmixing of two liquids of same composition</div>
          <p>Physically impossible. A liquid cannot 'unmix' into two phases of identical composition; if the compositions were identical, there would be no chemical boundary or interface between them.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Magmatic Process</th>
              <th>Physical / Chemical Action</th>
              <th>Direction of Evolution</th>
              <th>Typical Geological Phenomenon</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Liquid Immiscibility</strong> (Option C)</td><td><strong>Unmixing</strong> of a single melt into two liquids of different composition</td><td>Homogeneous $\rightarrow$ 2 Heterogeneous Liquids</td><td>Sulfide droplets settling; Carbonatite separation</td></tr>
            <tr><td>Magma Mixing (Option A)</td><td><strong>Mixing</strong> of two distinct magmas into a hybrid melt</td><td>2 Heterogeneous Liquids $\rightarrow$ 1 Hybrid Melt</td><td>Reverse zoning; mingled mafic enclaves in granite</td></tr>
            <tr><td>Fractional Crystallization</td><td>Separation of solid crystals from residual liquid</td><td>Liquid $\rightarrow$ Crystal + Residual Liquid</td><td>Bowen's reaction series; layered cumulates</td></tr>
            <tr><td>Subsolidus Exsolution</td><td>Unmixing of a solid-solution crystal into two solids</td><td>Single Solid Phase $\rightarrow$ 2 Intergrown Solids</td><td>Perthite (K-spar + Albite); Pyroxene lamellae</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What economic ore deposits owe their origin fundamentally to sulfide liquid immiscibility?</div>
        <div class="pq-ans">Answer: Magmatic Nickel-Copper-PGE Sulfide Deposits (e.g., Sudbury, Norilsk-Talnakh, Bushveld, Kambalda)</div>
        <div class="pq-exp">When mafic magma becomes sulfur-saturated, an immiscible sulfide liquid droplets exsolve, scavenge chalcophile metals (Ni, Cu, Pt, Pd), and sink to form massive basal ore pools.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What phase boundary in a temperature-composition phase diagram bounds the region of two immiscible liquids?</div>
        <div class="pq-ans">Answer: The Solvus (Two-Liquid Dome)</div>
        <div class="pq-exp">Above the solvus, the liquid is completely miscible and homogeneous; below the solvus, it unmixes into conjugate liquids.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What petrographic evidence was found in Apollo lunar basalts proving silicate liquid immiscibility?</div>
        <div class="pq-ans">Answer: High-silica (potassic granite) and high-iron (pyroxferroite) glassy globules in late-stage mesostasis.</div>
        <div class="pq-exp">Edwin Roedder and Paul Weiblen (1970) proved immiscibility in lunar samples where residual melt split into immiscible felsic and mafic glasses.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. How does sulfur saturation occur in a basic magma leading to sulfide liquid unmixing?</div>
        <div class="pq-ans">Answer: By crustal sulfur assimilation, cooling, silica contamination, or fractional crystallization.</div>
        <div class="pq-exp">Adding crustal sulfur or adding silica drastically lowers sulfide solubility, triggering immediate immiscible sulfide droplet exsolution.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the Partition Coefficient ($D$) of Platinum Group Elements (PGEs) between immiscible sulfide melt and silicate melt?</div>
        <div class="pq-ans">Answer: Extremely high ($D_{PGE} \approx 10^3\text{ to } 10^5$)</div>
        <div class="pq-exp">PGEs strongly partition into the sulfide melt phase, concentrating platinum and palladium by thousands of times relative to silicate magma.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What famous layered mafic intrusion in Greenland exhibits late-stage Fe-rich vs. Si-rich liquid immiscibility?</div>
        <div class="pq-ans">Answer: The Skaergaard Intrusion</div>
        <div class="pq-exp">Extreme fractional crystallization in the Skaergaard closed magma chamber drove the final melt into the two-liquid immiscibility field.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the difference between solid solution exsolution and liquid immiscibility?</div>
        <div class="pq-ans">Answer: Exsolution occurs in the solid state below the solidus; liquid immiscibility occurs entirely within the liquid melt state above the solidus.</div>
        <div class="pq-exp">Perthite forms by solid-state exsolution; sulfide dropplets and carbonatite melts unmix as distinct liquids above the solidus.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What texture is formed when immiscible droplets of sulfide or carbonate are trapped in rapidly solidified volcanic rocks?</div>
        <div class="pq-ans">Answer: Variolitic, globular, or ocellar texture</div>
        <div class="pq-exp">Immiscible liquid droplets form spherical globules (ocelli or varioles) preserving the liquid-liquid emulsion texture.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Batch 7 Part B (Q084 - Q090)...")
    gen_q084()
    gen_q085()
    gen_q086()
    gen_q087()
    gen_q088()
    gen_q089()
    gen_q090()
    print("Batch 7 Part B successfully generated!")
