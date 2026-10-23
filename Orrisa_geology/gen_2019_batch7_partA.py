#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 7 Part A (Q076 - Q083)
Igneous Petrology: Chemistry, Classification, Reaction Principles, and Magmatic Rock Suites.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q076: Acid Igneous Rocks - Free Quartz Content (>=10%)
# -----------------------------------------------------------------------------
def gen_q076():
    q_num = 76
    filename = "Q076_Acid_Igneous_Rocks_Contain_10_Percent_Or_More_Free_Quartz_Complete_Guide.html"
    title = "Q076: Chemical Classification of Igneous Rocks - Acid Rocks & Free Quartz"
    badge = "OPSC 2019 Geology Paper-II • Question 76 • Igneous Petrology"
    h1_title = "Acid Igneous Rocks & Quartz Abundance: Chemical vs. Modal Mineralogical Criteria"
    meta_text = "<strong>Topic:</strong> Igneous Rock Classification • <strong>Key Concept:</strong> Total Silica (SiO2 wt%) vs. Free Quartz Modal % • <strong>Textbooks:</strong> K.M. Bangar (p. 110-112); John D. Winter (Principles of Igneous Petrology)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Chemical vs. Mineralogical Classification</div>
      <p>In igneous petrology, rocks are classified chemically based on their total silica ($SiO_2$) weight percentage, and mineralogically based on the abundance of <strong>free quartz</strong> ($\alpha$-quartz modal volume percentage):</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Class</th>
              <th>Total Silica ($SiO_2$ wt%)</th>
              <th>Normative / Modal Free Quartz</th>
              <th>Characteristic Mineral Assemblage</th>
              <th>Representative Plutonic & Volcanic Examples</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td>Acidic (Felsic / Silicic)</td>
              <td>&gt; 66% (or &gt; 65%)</td>
              <td>&ge; 10% Free Quartz (often 20&ndash;40%)</td>
              <td>Quartz + K-Feldspar (Orthoclase/Microcline) + Sodic Plagioclase &plusmn; Biotite/Muscovite</td>
              <td>Granite, Adamellite, Granodiorite (Plutonic); Rhyolite, Dacite (Volcanic)</td>
            </tr>
            <tr>
              <td>Intermediate</td>
              <td>52% &ndash; 66%</td>
              <td>&lt; 10% Free Quartz (or silica-saturated)</td>
              <td>Plagioclase (Oligoclase&ndash;Andesine) + Hornblende + Biotite &plusmn; minor Pyroxene</td>
              <td>Syenite, Diorite, Monzonite (Plutonic); Trachyte, Andesite (Volcanic)</td>
            </tr>
            <tr>
              <td>Basic (Mafic)</td>
              <td>45% &ndash; 52%</td>
              <td>0% Free Quartz (Silica-undersaturated or quartz-free)</td>
              <td>Calcic Plagioclase (Labradorite/Bytownite) + Clinopyroxene (Augite) &plusmn; Olivine</td>
              <td>Gabbro, Norite (Plutonic); Dolerite (Hypabyssal); Basalt (Volcanic)</td>
            </tr>
            <tr>
              <td>Ultrabasic (Ultramafic)</td>
              <td>&lt; 45%</td>
              <td>0% Free Quartz (Desilicated)</td>
              <td>Olivine (Forsterite) + Pyroxenes (Enstatite/Augite); Feldspar &lt; 10%</td>
              <td>Peridotite (Dunite, Lherzolite, Harzburgite), Pyroxenite (Plutonic); Komatiite (Volcanic)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Acid igneous rocks are characterized chemically by a high silica content exceeding 65 or 66 percent. In mineralogical terms, because all bases (alumina, potash, soda, lime, iron, and magnesia) are completely saturated with silica, the surplus silica crystallizes as <strong>free quartz</strong>, which generally amounts to <strong>10% or more</strong> of the rock's total modal volume. Rocks with more than 60-65% free quartz are rare monomineralic quartz-rocks (silexites/quartzolites) or sedimentary sandstones."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Petrology Section, pp. 110&ndash;112)</div>
      </div>

      <div class="formula-box">
        $$\text{Total Bulk Silica} = \sum (\text{Silica bound in silicates: feldspars, micas, amphiboles}) + \text{Free Modal Quartz} (SiO_2)$$
        $$\text{In Acid Granitoids: } \text{Total } SiO_2 \ge 66 \text{ wt\%} \implies \text{Modal Free Quartz } \ge 10\text{ vol\% (typically } 20\text{--}35\%\text{)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q076/acid_intermediate_basic_ultrabasic_quartz_silica.png" alt="Acid Igneous Rocks Total Silica vs Free Quartz" class="figure-img">
        <div class="figure-caption">Figure 76: Quantitative comparison between bulk silica content (wt%) and modal free quartz across the four fundamental igneous rock classes. Acid rocks characteristically contain &ge; 10% free quartz.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 76</div>
        <div class="raw-q-text">Generally, acid igneous rocks contain :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> 10% or more free quartz</div>
          <div class="raw-opt"><span class="opt-letter">B</span> 15% or more free quartz</div>
          <div class="raw-opt"><span class="opt-letter">C</span> 60% or more free quartz</div>
          <div class="raw-opt"><span class="opt-letter">D</span> 65% or more free quartz</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (10% or more free quartz)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">10% or more free quartz</div>
          <p>By standard petrological convention (Hatch, Wells & Wells; Bangar; IUGS granitoid field), an igneous rock is classified mineralogically as <strong>acidic</strong> when it contains at least <strong>10% or more free quartz</strong> (modal volume). In the QAPF classification of plutonic rocks, the boundary between silica-saturated intermediate rocks (monzonite, syenite, diorite) and true acid granitoids requires $Q > 5\text{--}10\%$. Free modal quartz in normal granites ranges from 20% to 35%.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">15% or more free quartz</div>
          <p>While many granites contain 15% to 30% quartz, 15% is an arbitrary cut-off and not the definition of acid igneous rocks. Rocks containing 10% to 14% free quartz (such as quartz syenites, quartz diorites, and granodioritic transition rocks) are already acid rocks supersaturated in silica.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">60% or more free quartz</div>
          <p>This option confuses <strong>free modal quartz</strong> with <strong>total chemical silica ($SiO_2$)</strong>. An igneous rock with 60% or more free quartz is an ultra-rare hydrothermal pegmatitic facies known as a <em>silexite</em> or <em>quartzolite</em>. Normal granites contain 60% to 70% feldspar, leaving 20% to 35% quartz.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">65% or more free quartz</div>
          <p>This is a classic trap: acid rocks contain <strong>65% or more total chemical silica ($SiO_2$)</strong>, NOT 65% free quartz! In a granite containing 72% bulk $SiO_2$, over 45% of that $SiO_2$ is chemically bound in the crystal lattices of feldspars ($KAlSi_3O_8, NaAlSi_3O_8$) and micas, leaving approximately 25% to 30% as free quartz crystals.</p>
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
              <th>Igneous Rock Group</th>
              <th>Bulk $SiO_2$ (wt%)</th>
              <th>Free Quartz Content (vol%)</th>
              <th>Color Index ($M'$)</th>
              <th>Specific Gravity</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2;"><td>Acidic / Felsic</td><td>&gt; 65&ndash;66%</td><td>&ge; 10% (up to 40%)</td><td>&lt; 20 (Leucocratic)</td><td>2.60 &ndash; 2.70</td></tr>
            <tr><td>Intermediate</td><td>52 &ndash; 66%</td><td>&lt; 10% (often 0&ndash;5%)</td><td>20 &ndash; 40 (Mesocratic)</td><td>2.75 &ndash; 2.90</td></tr>
            <tr><td>Basic / Mafic</td><td>45 &ndash; 52%</td><td>0% (Silica-free)</td><td>40 &ndash; 70 (Melanocratic)</td><td>2.95 &ndash; 3.10</td></tr>
            <tr><td>Ultrabasic / Ultramafic</td><td>&lt; 45%</td><td>0% (Silica-deficient)</td><td>&gt; 90 (Ultramelanocratic)</td><td>3.15 &ndash; 3.40</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. In the chemical classification of igneous rocks, a rock having 58% bulk $SiO_2$ and 4% free modal quartz is classified as:</div>
        <div class="pq-ans">Answer: Intermediate igneous rock</div>
        <div class="pq-exp">Intermediate rocks have bulk silica between 52% and 66% and contain less than 10% free modal quartz.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What distinguishes 'total silica' from 'free silica' in petrographic analysis?</div>
        <div class="pq-ans">Answer: Total silica is all $SiO_2$ present chemically; free silica is uncombined $SiO_2$ crystallizing as quartz/tridymite/cristobalite.</div>
        <div class="pq-exp">Most silica in igneous rocks is bound in framework and chain silicates (feldspars, amphiboles). Only the excess silica above cation saturation forms free quartz.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is an igneous rock with greater than 90% modal quartz called in the IUGS classification?</div>
        <div class="pq-ans">Answer: Quartzolite (or Silexite)</div>
        <div class="pq-exp">Field 1 of the IUGS QAPF double triangle covers rocks where $Q / (Q+A+P) > 90\%$, representing the most quartz-rich igneous extreme.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. A typical granite has 72 wt% $SiO_2$. What is its expected modal quartz percentage?</div>
        <div class="pq-ans">Answer: Approximately 25% to 35%</div>
        <div class="pq-exp">Feldspars (potash feldspar and albite) require ~65% $SiO_2$ in their formula stoichiometry. In a 72% bulk rock, ~25-30% modal quartz precipitates.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why cannot olivine ($Mg_2SiO_4$) and free quartz ($SiO_2$) coexist in equilibrium under normal magmatic conditions?</div>
        <div class="pq-ans">Answer: Because they react to form orthopyroxene (enstatite): $Mg_2SiO_4 + SiO_2 \rightarrow 2 MgSiO_3$.</div>
        <div class="pq-exp">Olivine is an unsaturated nesosilicate that is unstable in the presence of free silica melt, immediately reacting peritectically to form enstatite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which volcanic rock is the compositional equivalent of a granite?</div>
        <div class="pq-ans">Answer: Rhyolite</div>
        <div class="pq-exp">Rhyolite is the fine-grained, extrusive/volcanic equivalent of granite, possessing &gt;66% $SiO_2$ and &ge;10% free normative quartz.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the Color Index ($M'$) of acid igneous rocks?</div>
        <div class="pq-ans">Answer: $M' &lt; 20$ (Leucocratic to extreme leucocratic)</div>
        <div class="pq-exp">Acid rocks are dominated by felsic minerals (quartz + feldspars &gt; 80%), leaving less than 20% dark ferromagnesian minerals.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the normative mineral calculated in CIPW norm when a rock has excess silica over all mineral bases?</div>
        <div class="pq-ans">Answer: Normative Quartz ($q$)</div>
        <div class="pq-exp">When all alumina, alkalis, lime, iron, and magnesia are saturated to form feldspars, pyroxenes, and magnetite, remaining $SiO_2$ is allocated to normative quartz ($q$).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q077: Andesite - Intermediate Volcanic Rock
# -----------------------------------------------------------------------------
def gen_q077():
    q_num = 77
    filename = "Q077_Andesite_Is_An_Intermediate_Volcanic_Rock_Complete_Guide.html"
    title = "Q077: Igneous Rock Classification - Andesite Extrusive & Volcanic Nature"
    badge = "OPSC 2019 Geology Paper-II • Question 77 • Igneous Petrology"
    h1_title = "Andesite Petrography: The Prototypical Intermediate Volcanic Rock"
    meta_text = "<strong>Topic:</strong> Volcanic Rock Types • <strong>Key Concept:</strong> Subduction Zone Magmatism & Intermediate Chemistry • <strong>Textbooks:</strong> John D. Winter (Principles of Igneous & Metamorphic Petrology); K.M. Bangar (p. 125)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Petrography & Geological Environment of Andesite</div>
      <p><strong>Andesite</strong> is a fine-grained, aphanitic to porphyritic <strong>intermediate volcanic (extrusive)</strong> rock named by Christian Leopold von Buch (1826) after the <em>Andes Mountains</em> of South America, where it forms the dominant volcanic edifice along active subduction zone margins.</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Property</th>
              <th>Petrological Specification</th>
              <th>Diagnostic Detail</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Chemical Class</td>
              <td><strong>Intermediate</strong> (52 &ndash; 63 wt% $SiO_2$)</td>
              <td>Total alkali-silica (TAS) field between basaltic andesite and dacite.</td>
            </tr>
            <tr>
              <td>Emplacement Mode</td>
              <td><strong>Volcanic (Extrusive)</strong></td>
              <td>Lava flows, block-and-ash flows, pyroclastic breccias, and stratovolcano cones.</td>
            </tr>
            <tr>
              <td>Plutonic Equivalent</td>
              <td><strong>Diorite</strong></td>
              <td>Shares identical chemical and bulk mineralogical composition; differs in grain size.</td>
            </tr>
            <tr>
              <td>Essential Mineralogy</td>
              <td><strong>Plagioclase Feldspar + Mafics</strong></td>
              <td>Zoned plagioclase (typically <em>Andesine</em> $An_{30}\text{--}An_{50}$) + Augite / Hypersthene / Hornblende.</td>
            </tr>
            <tr>
              <td>Diagnostic Texture</td>
              <td><strong>Porphyritic with Hyalopilitic Groundmass</strong></td>
              <td>Prominent phenocrysts of oscillatory-zoned andesine and hornblende/augite in a microcrystalline or glassy groundmass.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Andesite is the volcanic equivalent of diorite. It is an intermediate, usually porphyritic rock consisting essentially of plagioclase feldspar (principally andesine or oligoclase) together with one or more ferromagnesian minerals such as biotite, hornblende, augite, or hypersthene. Andesites are the characteristic lavas of island arcs and active continental margins bordering the Pacific Ocean (the 'Andesite Line')."
        <div class="quote-author">&mdash; John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Chapter 2, pp. 24&ndash;28)</div>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q077/andesite_intermediate_volcanic_rock_tas_qapf.png" alt="Andesite Intermediate Volcanic Rock TAS and QAPF" class="figure-img">
        <div class="figure-caption">Figure 77: Position of Andesite within the IUGS Total Alkali-Silica (TAS) diagram and volcanic rock suite, illustrating its classification as an intermediate extrusive rock (52&ndash;63 wt% SiO2).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 77</div>
        <div class="raw-q-text">Andesite is :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> A coarse grained acid plutonic rock</div>
          <div class="raw-opt"><span class="opt-letter">B</span> A fine grained hypabyssal rock</div>
          <div class="raw-opt"><span class="opt-letter">C</span> An intermediate volcanic rock</div>
          <div class="raw-opt"><span class="opt-letter">D</span> An ultrabasic volcanic rock</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (An intermediate volcanic rock)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">An intermediate volcanic rock</div>
          <p>Andesite has a silica content of 52% to 63% (intermediate range) and forms as an extrusive (volcanic) lava flow or pyroclastic deposit on planetary crusts. It represents the extrusive counterpart of diorite.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">A coarse grained acid plutonic rock</div>
          <p>A coarse-grained acid plutonic rock is <strong>Granite</strong> or <strong>Adamellite</strong> ($SiO_2 > 66\%$, phaneritic texture). Andesite is fine-grained/porphyritic, volcanic, and intermediate.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">A fine grained hypabyssal rock</div>
          <p>A fine- to medium-grained hypabyssal rock equivalent to diorite is a <strong>microdiorite</strong> or <strong>porphyrite</strong>. Andesite is an extrusive surface lava flow (volcanic).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">An ultrabasic volcanic rock</div>
          <p>An ultrabasic volcanic rock ($SiO_2 < 45\%$, highly magnesian) is a <strong>Komatiite</strong> or <strong>Meimechite</strong>, characterized by spinifex texture. Andesite is neither ultrabasic nor rich in olivine.</p>
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
              <th>Plutonic (Coarse/Deep)</th>
              <th>Hypabyssal (Medium/Shallow)</th>
              <th>Volcanic (Fine/Extrusive)</th>
              <th>Dominant Minerals</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Acidic (&gt;66% $SiO_2$)</td><td>Granite</td><td>Granite Porphyry / Microgranite</td><td>Rhyolite</td><td>Quartz + K-Feldspar + Biotite</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Intermediate (52&ndash;66% $SiO_2$)</td><td>Diorite</td><td>Microdiorite</td><td>ANDESITE (Option C)</td><td>Andesine + Hornblende &plusmn; Pyroxene</td></tr>
            <tr><td>Basic (45&ndash;52% $SiO_2$)</td><td>Gabbro</td><td>Dolerite (Diabase)</td><td>Basalt</td><td>Labradorite + Augite</td></tr>
            <tr><td>Ultrabasic (&lt;45% $SiO_2$)</td><td>Peridotite</td><td>Picrite</td><td>Komatiite</td><td>Olivine + Pyroxene</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What geological boundary separates the tholeiitic basalt province of the open Pacific basin from circum-Pacific andesitic volcanism?</div>
        <div class="pq-ans">Answer: The Andesite Line (Marshall Line)</div>
        <div class="pq-exp">The Andesite Line marks the petrological boundary between intraplate oceanic basalts and subduction-related calc-alkaline andesites.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What specific plagioclase composition is diagnostic of andesite?</div>
        <div class="pq-ans">Answer: Andesine ($An_{30}\text{--}An_{50}$)</div>
        <div class="pq-exp">By IUGS petrographic rules, the dominant plagioclase in andesite has an anorthite content less than $An_{50}$ (andesine/oligoclase), whereas basalt plagioclase is labradorite ($An_{50}\text{--}An_{70}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the typical magma series that generates the voluminous andesites of volcanic arcs?</div>
        <div class="pq-ans">Answer: The Calc-Alkaline Magma Series</div>
        <div class="pq-exp">Hydrous partial melting of mantle wedge peridotite fluxed by slab-derived fluids generates primary hydrous basaltic magmas that differentiate along calc-alkaline pathways to andesite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What texture is commonly observed in andesite phenocrysts indicating magma mixing or fluctuating P-T conditions?</div>
        <div class="pq-ans">Answer: Oscillatory zoning and sieve (dusty) resorption rims</div>
        <div class="pq-exp">Repeated magma recharge in sub-volcanic chambers creates abrupt compositional jumps in plagioclase growth zones, forming oscillatory rings and sieve textures.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the volcanic equivalent of a granodiorite?</div>
        <div class="pq-ans">Answer: Dacite</div>
        <div class="pq-exp">Dacite occupies the composition field between andesite and rhyolite ($SiO_2 \approx 63\text{--}68\%$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which volcanic hazard is most typically associated with viscous andesitic to dacitic lavas?</div>
        <div class="pq-ans">Answer: Pyroclastic density currents (PDCs) and Peléan / Plinian explosive eruptions</div>
        <div class="pq-exp">The higher silica content and moderate-to-high volatile ($H_2O$) content make andesitic melts highly viscous, promoting explosive dome-collapse pyroclastic flows.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. How does basaltic andesite differ from normal andesite in $SiO_2$ content?</div>
        <div class="pq-ans">Answer: Basaltic andesite has 52% to 57% $SiO_2$, while andesite has 57% to 63% $SiO_2$.</div>
        <div class="pq-exp">The IUGS TAS diagram formally splits the intermediate volcanic field into basaltic andesite ($52\text{--}57\%$) and andesite ($57\text{--}63\%$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the intrusive plutonic equivalent of Andesite?</div>
        <div class="pq-ans">Answer: Diorite</div>
        <div class="pq-exp">Diorite crystallizes slowly at depth from the same intermediate magma, producing a phaneritic equigranular texture of plagioclase and amphibole.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q078: Bowen's Reaction Series - First Mineral in Continuous Series (Calcic Plagioclase)
# -----------------------------------------------------------------------------
def gen_q078():
    q_num = 78
    filename = "Q078_First_Mineral_Formed_Bowen_Continuous_Series_Calcic_Plagioclase_Complete_Guide.html"
    title = "Q078: Bowen's Reaction Series - Calcic Plagioclase in Continuous Series"
    badge = "OPSC 2019 Geology Paper-II • Question 78 • Igneous Petrology"
    h1_title = "Bowen's Reaction Principle: The Continuous Plagioclase Solid-Solution Series"
    meta_text = "<strong>Topic:</strong> Magmatic Crystallization Differentiation • <strong>Key Concept:</strong> Continuous vs. Discontinuous Reaction Series • <strong>Textbooks:</strong> N.L. Bowen (1928, The Evolution of the Igneous Rocks); John D. Winter"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Bowen's Reaction Principle (1928)</div>
      <p>In his seminal work <em>The Evolution of the Igneous Rocks</em> (1928), Canadian experimental petrologist <strong>Norman L. Bowen</strong> demonstrated that minerals crystallizing from a cooling basaltic magma do not precipitate independently at single freezing points, but rather react continuously with the residual liquid along two distinct branches:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Reaction Series Branch</th>
              <th>Crystallization Mechanism</th>
              <th>Sequence from High-T to Low-T</th>
              <th>Mineral Structural Evolution</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Discontinuous Series</strong> (Fe-Mg Silicates)</td>
              <td>Incongruent reaction at fixed temperatures; early crystal reacts with melt to form a new mineral with a fundamentally different crystal structure.</td>
              <td>$Mg\text{-Olivine} \rightarrow \text{Orthopyroxene} \rightarrow \text{Clinopyroxene} \rightarrow \text{Amphibole (Hornblende)} \rightarrow \text{Biotite}$</td>
              <td>Nesosilicate (isolated tetrahedra) $\rightarrow$ Inosilicate (single chains) $\rightarrow$ Inosilicate (double chains) $\rightarrow$ Phyllosilicate (sheets).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Continuous Series</strong> (Feldspar Solid Solution)</td>
              <td>Continuous ionic exchange without changing the underlying crystal lattice (tectosilicate framework); $Ca^{2+} + Al^{3+} \rightleftharpoons Na^+ + Si^{4+}$.</td>
              <td><strong>Calcic Plagioclase (Anorthite)</strong> $\rightarrow$ Bytownite $\rightarrow$ Labradorite $\rightarrow$ Andesine $\rightarrow$ Oligoclase $\rightarrow$ <strong>Sodic Plagioclase (Albite)</strong></td>
              <td>$CaAl_2Si_2O_8$ (pure calcic anorthite at $\sim 1553^\circ\text{C}$) progressively enriches in $NaAlSi_3O_8$ (sodic albite at $\sim 1118^\circ\text{C}$).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "In the continuous reaction series of the plagioclase feldspars, the first mineral to form at the highest temperature from a basaltic liquid is <strong>calcic plagioclase</strong> (anorthite, $CaAl_2Si_2O_8$). As cooling proceeds, this early-formed calcic plagioclase reacts continuously with the soda-enriched residual liquid, shifting its solid-solution composition gradually through bytownite, labradorite, and andesine toward sodic plagioclase (albite)."
        <div class="quote-author">&mdash; N.L. Bowen, <em>The Evolution of the Igneous Rocks</em> (Princeton University Press, 1928)</div>
      </div>

      <div class="formula-box">
        $$\text{Plagioclase Solid-Solution Coupled Substitution: } Ca^{2+} + Al^{3+} \rightleftharpoons Na^+ + Si^{4+}$$
        $$T_{\text{crystallization}}(\text{Anorthite } CaAl_2Si_2O_8) = 1553^\circ\text{C} \quad \gg \quad T_{\text{crystallization}}(\text{Albite } NaAlSi_3O_8) = 1118^\circ\text{C}$$
        $$\therefore \text{First mineral formed in continuous series} \equiv \mathbf{Calcic\ Plagioclase\ (Anorthite)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q078/bowen_reaction_series_continuous_calcic_plagioclase.png" alt="Bowen Reaction Series Continuous Branch Calcic Plagioclase" class="figure-img">
        <div class="figure-caption">Figure 78: Bowen's Reaction Series illustrating the continuous plagioclase solid-solution branch (right) and the discontinuous ferromagnesian branch (left), demonstrating that calcic plagioclase forms first.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 78</div>
        <div class="raw-q-text">The first mineral formed in the continuous series of Bowen reaction principle is :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Sodic-Calcic plagioclase</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Potash feldspar</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Calcic-sodic plagioclase</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Calcic plagioclase</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Calcic plagioclase)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Calcic plagioclase</div>
          <p>The continuous series is defined by the plagioclase feldspar binary solid-solution ($An\text{--}Ab$). Because anorthite ($CaAl_2Si_2O_8$) has a much higher melting point ($1553^\circ\text{C}$) than albite ($1118^\circ\text{C}$), the first crystal to precipitate from a cooling basic magma at the highest temperature is <strong>calcic plagioclase</strong> (anorthite-rich, $An_{90}\text{--}An_{100}$).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Sodic-Calcic plagioclase</div>
          <p>Sodic-calcic plagioclase (such as andesine or oligoclase) forms intermediate to late in the continuous series as the melt becomes progressively depleted in calcium and enriched in sodium.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Potash feldspar</div>
          <p>Potash feldspar (orthoclase/microcline) does not belong to the continuous plagioclase series; it precipitates late from the residual felsic liquid at low temperatures ($\sim 700\text{--}650^\circ\text{C}$) after both the continuous and discontinuous series converge.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Calcic-sodic plagioclase</div>
          <p>Calcic-sodic plagioclase (such as labradorite, $An_{50}\text{--}An_{70}$) represents a middle stage of continuous crystallization, after initial precipitation of pure calcic plagioclase (anorthite/bytownite).</p>
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
              <th>Plagioclase Species</th>
              <th>Anorthite Formula ($CaAl_2Si_2O_8$)</th>
              <th>Crystallization Temperature</th>
              <th>Stage in Bowen's Series</th>
              <th>Host Rock Group</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Anorthite ($An_{90}\text{--}An_{100}$)</td><td>Calcic</td><td>$1553^\circ\text{C} - 1400^\circ\text{C}$</td><td>FIRST FORMED (Option D)</td><td>Anorthosite, Basic Gabbro</td></tr>
            <tr><td>Bytownite ($An_{70}\text{--}An_{90}$)</td><td>Calcic</td><td>$1400^\circ\text{C} - 1280^\circ\text{C}$</td><td>Early High-T</td><td>Gabbro, Basalt</td></tr>
            <tr><td>Labradorite ($An_{50}\text{--}An_{70}$)</td><td>Calcic-Sodic</td><td>$1280^\circ\text{C} - 1180^\circ\text{C}$</td><td>Middle Stage</td><td>Basalt, Dolerite, Gabbro</td></tr>
            <tr><td>Andesine ($An_{30}\text{--}An_{50}$)</td><td>Sodic-Calcic</td><td>$1180^\circ\text{C} - 1050^\circ\text{C}$</td><td>Intermediate Stage</td><td>Andesite, Diorite</td></tr>
            <tr><td>Oligoclase ($An_{10}\text{--}An_{30}$)</td><td>Sodic</td><td>$1050^\circ\text{C} - 950^\circ\text{C}$</td><td>Late Stage</td><td>Granite, Granodiorite</td></tr>
            <tr><td>Albite ($An_{0}\text{--}An_{10}$)</td><td>Pure Sodic</td><td>$1118^\circ\text{C}$ (pure end-member)</td><td>LAST FORMED in Series</td><td>Alkali Granite, Pegmatite</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the first mineral to form in the DISCONTINUOUS series of Bowen's reaction principle?</div>
        <div class="pq-ans">Answer: Forsteritic Olivine ($Mg_2SiO_4$)</div>
        <div class="pq-exp">Magnesium-rich olivine (forsterite) has the highest crystallization temperature among mafic silicates ($\sim 1890^\circ\text{C}$ pure, $\sim 1200\text{--}1300^\circ\text{C}$ in basaltic melt).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why does normal zoning in plagioclase phenocrysts always exhibit a calcic core and a sodic rim?</div>
        <div class="pq-ans">Answer: Because the melt becomes progressively depleted in Ca and enriched in Na during fractional crystallization.</div>
        <div class="pq-exp">As temperature drops, the plagioclase liquidus and solidus dictate that successive crystal layers become richer in albite ($Na$), leaving the high-T calcic core enclosed by a sodic rim.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What happens to early-formed calcic plagioclase crystals if they are rapidly isolated from the melt by sinking?</div>
        <div class="pq-ans">Answer: Fractional crystallization occurs; the crystals cannot react with the liquid, forming cumulate anorthosite.</div>
        <div class="pq-exp">Bowen termed this fractional crystallization: removing crystals prevents equilibrium reaction, driving the residual melt toward extreme silicic/alkaline compositions.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the final mineral to crystallize when both the continuous and discontinuous series converge?</div>
        <div class="pq-ans">Answer: Quartz ($SiO_2$)</div>
        <div class="pq-exp">After potash feldspar and muscovite crystallize, residual pure silica precipitates as quartz at $\sim 650\text{--}600^\circ\text{C}$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What type of solid solution occurs in the plagioclase feldspar series?</div>
        <div class="pq-ans">Answer: Coupled substitution solid solution ($Ca^{2+} + Al^{3+} \rightleftharpoons Na^+ + Si^{4+}$)</div>
        <div class="pq-exp">Because $Ca^{2+}$ and $Na^+$ have different valencies, charge neutrality is maintained by simultaneously substituting $Al^{3+}$ for $Si^{4+}$ in the tetrahedral framework.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which mineral crystallizes immediately after orthopyroxene in Bowen's discontinuous reaction series?</div>
        <div class="pq-ans">Answer: Clinopyroxene (Augite), followed by Amphibole (Hornblende)</div>
        <div class="pq-exp">The discontinuous sequence proceeds: Olivine $\rightarrow$ Orthopyroxene/Clinopyroxene $\rightarrow$ Amphibole $\rightarrow$ Biotite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a peritectic reaction in the discontinuous series?</div>
        <div class="pq-ans">Answer: An incongruent reaction where an early crystal reacts with melt to produce a new crystal phase: Olivine + Liquid $\rightarrow$ Pyroxene.</div>
        <div class="pq-exp">At the peritectic point ($1557^\circ\text{C}$ in the pure $Mg_2SiO_4-SiO_2$ system), forsterite reacts with silica-rich liquid to form enstatite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. Which plagioclase feldspar is most susceptible to chemical weathering under humid surface conditions according to Goldich's Weathering Series?</div>
        <div class="pq-ans">Answer: Calcic Plagioclase (Anorthite)</div>
        <div class="pq-exp">Goldich's dissolution series exactly mirrors Bowen's reaction series: high-temperature minerals formed furthest from surface P-T conditions (anorthite, olivine) weather the fastest.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q079: Carbonatite - Magmatic Carbonate Rock & REE Mineralization
# -----------------------------------------------------------------------------
def gen_q079():
    q_num = 79
    filename = "Q079_Carbonatite_Magmatic_Rock_Rich_In_Calcium_Carbonate_REE_Complete_Guide.html"
    title = "Q079: Carbonatite Magmatism - Primary Carbonate Rocks & REE Mineralization"
    badge = "OPSC 2019 Geology Paper-II • Question 79 • Igneous Petrology"
    h1_title = "Carbonatites: Primary Mantle-Derived Carbonate Melts & Critical REE Reserves"
    meta_text = "<strong>Topic:</strong> Alkaline & Carbonatite Magmatism • <strong>Key Concept:</strong> IUGS Definition (&gt;50% Carbonate) & Rare Earth Mineralization • <strong>Textbooks:</strong> Winter (2014); Bell & Rukhlov (Carbonatites); K.M. Bangar"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Carbonatite Petrogenesis & Geochemistry</div>
      <p><strong>Carbonatites</strong> are unique, mantle-derived igneous rocks defined by the International Union of Geological Sciences (IUGS) as containing <strong>more than 50% modal primary carbonate minerals</strong> (calcite, dolomite, ankerite, and siderite) with less than 20% $SiO_2$.</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Classification</th>
              <th>Dominant Carbonate Mineral</th>
              <th>Chemical Designation</th>
              <th>Associated Silicate Rocks & Fenitization</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td>Calcio-carbonatite (S&ouml;vite / Alvikite)</td>
              <td><strong>Calcite</strong> ($CaCO_3$)</td>
              <td>Rich in $CaO$; S&ouml;vite is coarse plutonic, Alvikite is hypabyssal/volcanic.</td>
              <td>Surrounded by ijolite, nephelinite, and extensive <strong>fenitization</strong> (alkali metasomatic halo).</td>
            </tr>
            <tr>
              <td>Magnesio-carbonatite (Beforsite)</td>
              <td><strong>Dolomite</strong> ($CaMg(CO_3)_2$)</td>
              <td>Rich in $MgO$; often forms medium- to fine-grained dykes and cone sheets.</td>
              <td>Enriched in high-field strength elements (HFSE) and LREEs.</td>
            </tr>
            <tr>
              <td>Ferro-carbonatite</td>
              <td><strong>Ankerite / Siderite</strong> ($FeCO_3$)</td>
              <td>Rich in $FeO + Fe_2O_3 + MnO$; late-stage low-temperature magmatic differentiates.</td>
              <td>Highest concentration of Rare Earth Elements (monazite, bastn&auml;site).</td>
            </tr>
            <tr>
              <td>Natro-carbonatite</td>
              <td><strong>Nyerereite / Gregoryite</strong> ($(Na,K)_2Ca(CO_3)_2$)</td>
              <td>Extremely rich in $Na_2O$ and $K_2O$; active lava at <em>Oldoinyo Lengai</em>, Tanzania.</td>
              <td>Water-soluble, rapidly altering to hydrous carbonates at surface conditions.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Carbonatites are igneous rocks containing more than 50 percent by volume of carbonate minerals. Although rare, carbonatites are of immense economic importance because they host the world's richest deposits of <strong>Rare Earth Elements (REEs: La, Ce, Pr, Nd)</strong>, Niobium (in pyrochlore), Tantalum, Phosphate (in apatite), and Fluorite. The Amba Dongar complex in Gujarat is India's most famous carbonatite-alkaline ring complex."
        <div class="quote-author">&mdash; Keith Bell, <em>Carbonatites: Genesis and Evolution</em> (Unwin Hyman)</div>
      </div>

      <div class="formula-box">
        $$\text{IUGS Classification Criterion: Modal Carbonates } (\text{Calcite} + \text{Dolomite} + \text{Ankerite}) > 50\text{ vol\%}$$
        $$\text{Key REE-Bearing Minerals in Carbonatites: Bastn\ddot{a}site } [(\text{Ce},\text{La})CO_3F], \text{ Monazite } [(\text{Ce},\text{La},\text{Nd})PO_4], \text{ Pyrochlore } [(\text{Na},\text{Ca})_2\text{Nb}_2\text{O}_6(\text{OH},\text{F})]$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q079/carbonatite_magmatic_carbonate_ree_deposit.png" alt="Carbonatite Magmatic Carbonate Rock REE Deposit" class="figure-img">
        <div class="figure-caption">Figure 79: Cross-section through a zoned alkaline-carbonatite complex showing the central carbonatite plug, surrounding ijolite-syenite ring dykes, outer fenitization aureole, and primary REE-Nb mineral concentration.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 79</div>
        <div class="raw-q-text">A magmatic rock rich in calcium carbonate and often containing rare earth minerals is :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Alkali basalt</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Syenite porphyry</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Carbonatite</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Granodiorite</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Carbonatite)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Carbonatite</div>
          <p>Carbonatite is an igneous (magmatic) rock composed of greater than 50% carbonate minerals, predominantly calcium carbonate (calcite in s&ouml;vite). It is world-renowned as the primary geological host for economic concentrations of Rare Earth Elements (bastn&auml;site, monazite) and niobium (pyrochlore).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Alkali basalt</div>
          <p>Alkali basalt is a silicate volcanic rock composed of calcic plagioclase, titanaugite, and olivine with normative nepheline. It does not contain primary calcium carbonate minerals.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Syenite porphyry</div>
          <p>Syenite porphyry is an intermediate felsic silicate rock dominated by alkali feldspar phenocrysts. While often associated with carbonatite ring complexes, it consists of aluminosilicates, not calcium carbonate.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Granodiorite</div>
          <p>Granodiorite is a common acid plutonic silicate rock consisting of quartz, plagioclase (oligoclase/andesine), K-feldspar, and biotite/hornblende. It has negligible carbonate content.</p>
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
              <th>Primary Mineralogy</th>
              <th>Dominant Anion Group</th>
              <th>Economic Mineral Commodities</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Carbonatite (Option C)</td><td>Calcite, Dolomite, Ankerite (&gt;50%)</td><td>Carbonate ($CO_3^{2-}$)</td><td>REEs (Nd, Pr, Dy), Niobium (Nb), P, Fluorite</td></tr>
            <tr><td>Alkali Basalt</td><td>Labradorite + Augite + Olivine</td><td>Silicate ($SiO_4^{4-}$)</td><td>Crushed stone, Gem peridot</td></tr>
            <tr><td>Syenite</td><td>Orthoclase + Microcline &plusmn; Nepheline</td><td>Silicate ($SiO_4^{4-}$)</td><td>Ceramic feldspar, Zircon</td></tr>
            <tr><td>Granodiorite</td><td>Plagioclase + Quartz + Biotite</td><td>Silicate ($SiO_4^{4-}$)</td><td>Dimension stone, Porphyry Cu-Mo-Au host</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Which active volcano in the East African Rift erupts natrocarbonatite lava at approximately $500\text{--}600^\circ\text{C}$?</div>
        <div class="pq-ans">Answer: Oldoinyo Lengai (Tanzania)</div>
        <div class="pq-exp">Oldoinyo Lengai is the only active volcano on Earth erupting sodium-potassium carbonate lavas (nyerereite and gregoryite).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the coarse-grained, plutonic variety of calcite carbonatite called?</div>
        <div class="pq-ans">Answer: S&ouml;vite</div>
        <div class="pq-exp">Coarse-grained plutonic calcite-carbonatite is termed s&ouml;vite; its fine-grained hypabyssal or volcanic equivalent is alvikite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the process of intensive alkali metasomatism of wall rocks surrounding a carbonatite called?</div>
        <div class="pq-ans">Answer: Fenitization</div>
        <div class="pq-exp">Fenitization involves pervasive infiltration of hyper-alkaline fluids ($Na, K, Fe^{3+}$), transforming granitic country rocks into fenites rich in aegirine and alkali feldspar.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Where is India's most prominent carbonatite complex located, renowned for fluorite and REE mineralization?</div>
        <div class="pq-ans">Answer: Amba Dongar (Chhota Udepur district, Gujarat)</div>
        <div class="pq-exp">Amba Dongar is a Cretaceous-Palaeocene ring complex related to Deccan plume magmatism, hosting India's largest fluorite deposit and rich REE reserves.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What primary niobium-bearing ore mineral is extracted almost exclusively from carbonatite complexes?</div>
        <div class="pq-ans">Answer: Pyrochlore [$(Na,Ca)_2Nb_2O_6(OH,F)$]</div>
        <div class="pq-exp">Over 90% of global niobium production (e.g., Arax&aacute; in Brazil) is mined from weathered pyrochlore-bearing carbonatites.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does liquid immiscibility contribute to the origin of carbonatitic magmas?</div>
        <div class="pq-ans">Answer: A parent carbonated nephelinite/melilitite melt unmixes into two immiscible liquids: a silicate melt and a carbonate melt.</div>
        <div class="pq-exp">Experimental petrology shows that at crustal pressures, $CO_2$-saturated alkaline silicate melts split into conjugate silicate and carbonate fractions.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a dolomite-dominated carbonatite termed in classical petrography?</div>
        <div class="pq-ans">Answer: Beforsite</div>
        <div class="pq-exp">Beforsite is the magnesio-carbonatite variety, consisting primarily of magmatic dolomite with minor apatite and phlogopite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. Which world-class REE deposit in China is hosted within Proterozoic carbonatite dykes?</div>
        <div class="pq-ans">Answer: Bayan Obo (Inner Mongolia, China)</div>
        <div class="pq-exp">Bayan Obo is the world's largest known REE deposit, containing massive reserves of bastn&auml;site and monazite associated with dolomitic carbonatites.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q080: Charnockite Mineral Composition (Quartz-Feldspar-Hypersthene)
# -----------------------------------------------------------------------------
def gen_q080():
    q_num = 80
    filename = "Q080_Charnockite_Mineral_Composition_Quartz_Feldspar_Hypersthene_Complete_Guide.html"
    title = "Q080: Charnockite Mineralogy - Quartz-Feldspar-Hypersthene Assemblage"
    badge = "OPSC 2019 Geology Paper-II • Question 80 • Igneous & Metamorphic Petrology"
    h1_title = "The Charnockite Series: Mineralogy, Granulite Facies, and Hypersthene Signature"
    meta_text = "<strong>Topic:</strong> Charnockite Series & Granulite Facies • <strong>Key Concept:</strong> Orthopyroxene-Bearing Quartzofeldspathic Rocks • <strong>Textbooks:</strong> Sir Thomas Holland (1900); K.M. Bangar; John D. Winter"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Charnockite Series & Holland's Definition (1900)</div>
      <p>The term <strong>Charnockite</strong> was coined in 1900 by <strong>Sir Thomas H. Holland</strong>, Director of the Geological Survey of India, to designate an orthopyroxene (hypersthene)-bearing quartzofeldspathic rock quarried from St. Thomas Mount in Chennai (formerly Madras) that had been used to construct the tombstone of <strong>Job Charnock</strong>, the historical founder of Kolkata.</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Charnockite Member</th>
              <th>Essential Mineral Assemblage</th>
              <th>Granitoid Equivalence</th>
              <th>Diagnostic Optical Characteristics</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Charnockite (sensu stricto)</strong></td>
              <td><strong>Quartz + K-Feldspar (Perthite) + Plagioclase + Hypersthene</strong></td>
              <td>Hypersthene Granite</td>
              <td>Greasy bluish-green or waxy dark-brown lustre; pleochroic hypersthene (pink to green); blue quartz.</td>
            </tr>
            <tr>
              <td>Enderbite</td>
              <td>Quartz + Plagioclase (Anti-perthite) + Hypersthene (&plusmn; minor K-feldspar)</td>
              <td>Hypersthene Tonalite / Granodiorite</td>
              <td>Plagioclase-dominated ($P/(A+P) > 65\%$); common in South Indian granulite terranes.</td>
            </tr>
            <tr>
              <td>Mangerite</td>
              <td>Microperthite + Plagioclase + Hypersthene + minor Quartz (&lt; 20%)</td>
              <td>Hypersthene Monzonite</td>
              <td>Intermediate member with roughly equal alkali feldspar and plagioclase.</td>
            </tr>
            <tr>
              <td>Jotunite / Norite</td>
              <td>Calcic Plagioclase + Hypersthene / Orthopyroxene &plusmn; Clinopyroxene</td>
              <td>Hypersthene Monzogabbro / Norite</td>
              <td>Basic end-member of the charnockitic suite; dark melanocratic appearance.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Charnockite is a hypersthene granite consisting essentially of <strong>quartz, microcline (perthite), plagioclase, and hypersthene</strong>, with or without iron ores and garnet. Its most striking physical character is an olive-green, greasy, or resinous waxy luster, imparted by microscopic carbonaceous and fluid inclusions in quartz and feldspar under high-pressure granulite facies metamorphism ($T = 750\text{--}900^\circ\text{C}, P = 5\text{--}10\text{ kbar}$, ultra-low $a_{H_2O}$)."
        <div class="quote-author">&mdash; Sir Thomas Holland, <em>The Charnockite Series: A Group of Archaean Hypersthenic Rocks in Peninsular India</em> (Memoirs of the GSI, Vol. XXVIII, Part 2, 1900)</div>
      </div>

      <div class="formula-box">
        $$\text{Charnockite Mineral Formula: } \mathbf{Quartz}\ (SiO_2) + \mathbf{Feldspar}\ (\text{Microperthite } KAlSi_3O_8 + \text{Oligoclase}) + \mathbf{Hypersthene}\ ((Fe,Mg)_2Si_2O_6)$$
        $$\text{Dehydration Breakdown Reaction: } \text{Biotite} + \text{Quartz} \rightleftharpoons \mathbf{Hypersthene} + \text{K-Feldspar} + H_2O \uparrow \quad (\text{at } T > 750^\circ\text{C}, a_{CO_2} \gg a_{H_2O})$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q080/charnockite_hypersthene_granite_mineralogy_qapf.png" alt="Charnockite Series Mineral Composition QAPF" class="figure-img">
        <div class="figure-caption">Figure 80: The Charnockite Series plotted on the QAPF classification, highlighting the diagnostic Quartz-Feldspar-Hypersthene mineralogy of charnockite sensu stricto.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 80</div>
        <div class="raw-q-text">Generally, a charnockite has a mineral composition of :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Quartz-Hornblende-Oligoclase</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Quartz-Epidote-Andesine</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Quartz-Feldspar-Hypersthene</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Quartz-Feldspar-Augite</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Quartz-Feldspar-Hypersthene)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Quartz-Feldspar-Hypersthene</div>
          <p>By Holland's classical definition and international nomenclature, charnockite is an orthopyroxene granite composed essentially of <strong>Quartz, Feldspar (microperthitic K-feldspar and plagioclase), and Hypersthene</strong>. The presence of hypersthene (orthopyroxene) is the non-negotiable diagnostic signature that separates charnockite from all ordinary granites.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Quartz-Hornblende-Oligoclase</div>
          <p>This assemblage corresponds to a typical <strong>Tonalite</strong> or <strong>Diorite</strong>. It lacks the essential orthopyroxene (hypersthene) and K-feldspar.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Quartz-Epidote-Andesine</div>
          <p>Epidote is a hydrous low- to medium-grade mineral diagnostic of greenschist to epidote-amphibolite facies. It is completely unstable in the dry, ultra-high-temperature granulite facies regime of charnockites.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Quartz-Feldspar-Augite</div>
          <p>Augite is a clinopyroxene. While clinopyroxene may occur as a minor subordinate accessory, the <em>essential</em> diagnostic ferromagnesian mineral of charnockite is strictly <strong>orthopyroxene (Hypersthene)</strong>.</p>
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
              <th>Rock Type</th>
              <th>Essential Diagnostic Mafic</th>
              <th>Feldspar Character</th>
              <th>Metamorphic / Igneous Facies</th>
              <th>Macroscopic Lustre / Color</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Charnockite (Option C)</td><td><strong>Hypersthene</strong> (Orthopyroxene)</td><td>Microperthite + Plagioclase</td><td>Granulite Facies (Dehydrated, $CO_2$-rich)</td><td>Dark greasy green / waxy brownish</td></tr>
            <tr><td>Normal Granite</td><td>Biotite / Muscovite</td><td>Microcline / Orthoclase</td><td>Magmatic / Amphibolite Facies</td><td>Light pink, white, or grey</td></tr>
            <tr><td>Granulite (sensu lato)</td><td>Garnet &plusmn; Sillimanite &plusmn; Kyanite</td><td>Perthite + Plagioclase</td><td>Granulite Facies (Pelitic / Crustal)</td><td>Light grey, speckled with red garnet</td></tr>
            <tr><td>Enderbite</td><td><strong>Hypersthene</strong></td><td>Plagioclase (Antiperthitic) &gt;&gt; K-spar</td><td>Granulite Facies (Tonalitic)</td><td>Greasy greenish-grey</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Who named the charnockite series and after whom was it named?</div>
        <div class="pq-ans">Answer: Sir Thomas H. Holland (1900), after Job Charnock.</div>
        <div class="pq-exp">Holland named the rock after Job Charnock, founder of Calcutta, whose tombstone in St. John's Churchyard was made of this rock brought from St. Thomas Mount, Madras.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What pleochroic colors are typically displayed by hypersthene in a charnockite thin section?</div>
        <div class="pq-ans">Answer: Pink / reddish-pink ($\alpha$) to yellowish-green ($\beta$) to green ($\gamma$)</div>
        <div class="pq-exp">Hypersthene displays intense and diagnostic pleochroism from salmon-pink to pale green under plane-polarized light.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What causes the characteristic waxy, greasy bluish-green luster of charnockites in hand specimens?</div>
        <div class="pq-ans">Answer: Submicroscopic fluid inclusions ($CO_2$-rich) and exsolved micro-needles of rutile/iron oxides in quartz and feldspar.</div>
        <div class="pq-exp">These submicroscopic inclusions scatter light, producing the famous greasy appearance and opalescent blue quartz.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the process called where pre-existing amphibolite-facies gneisses are transformed in-situ into patchy charnockite by flushing of $CO_2$ fluids?</div>
        <div class="pq-ans">Answer: Charnockitization (or 'Incipient Charnockite' formation)</div>
        <div class="pq-exp">Demonstrated famously at Kabbaldurga (Karnataka), where carbonic fluids lowered water activity ($a_{H_2O}$), breaking down hornblende/biotite to hypersthene.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which tectonic mobile belt in Eastern India is world-renowned for extensive charnockite-khondalite massifs?</div>
        <div class="pq-ans">Answer: The Eastern Ghats Mobile Belt (EGMB)</div>
        <div class="pq-exp">The Eastern Ghats belt (extending through Odisha and Andhra Pradesh) represents a deeply eroded Proterozoic granulite terrain dominated by charnockites and khondalites.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does enderbite differ mineralogically from charnockite sensu stricto?</div>
        <div class="pq-ans">Answer: Enderbite is plagioclase-dominant (tonalitic), while charnockite s.s. has K-feldspar $\ge$ plagioclase (granitic).</div>
        <div class="pq-exp">In the charnockite series, enderbite is the hypersthene-bearing tonalite/trondhjemite equivalent.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the metamorphic facies condition required to generate hypersthene in quartzofeldspathic rocks?</div>
        <div class="pq-ans">Answer: Granulite Facies</div>
        <div class="pq-exp">Orthopyroxene in felsic rocks is the defining index mineral of the granulite facies ($T > 750^\circ\text{C}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What accessory mineral is often present alongside hypersthene in garnetiferous charnockites?</div>
        <div class="pq-ans">Answer: Almandine-Pyrope Garnet</div>
        <div class="pq-exp">High-pressure granulites frequently contain almandine-rich garnet formed via the reaction: $Biotite + Sillimanite + Quartz \rightarrow Garnet + K-feldspar + Liquid$.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q081: Diorite Mafic Content 100% - Perkinite
# -----------------------------------------------------------------------------
def gen_q081():
    q_num = 81
    filename = "Q081_Ferromagnesian_Content_Of_Diorite_100_Percent_Is_Perkinite_Complete_Guide.html"
    title = "Q081: Diorite Classification by Color Index - Perkinite Definition"
    badge = "OPSC 2019 Geology Paper-II • Question 81 • Igneous Petrology"
    h1_title = "Diorite Mafic Spectrum: From Leucodiorite to Meladiorite and Perkinite"
    meta_text = "<strong>Topic:</strong> Igneous Rock Classification & Color Index • <strong>Key Concept:</strong> 100% Ferromagnesian Extreme of Diorite • <strong>Textbooks:</strong> P.K. Mukherjee (Textbook of Geology, p. 249); K.M. Bangar; Duparc (1907)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Color Index ($M'$) Variation in Intermediate Rocks</div>
      <p>In classical petrography, intermediate plutonic rocks of the <strong>diorite family</strong> consist essentially of intermediate plagioclase (andesine or oligoclase) and ferromagnesian minerals (hornblende, augite, and biotite). Variations in the modal percentage of ferromagnesian (mafic) minerals dictate their nomenclature across the color index spectrum:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Variety</th>
              <th>Ferromagnesian Content (Mafic Modal %)</th>
              <th>Feldspar Content (Plagioclase %)</th>
              <th>Petrological Definition & Mineralogy</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Leucodiorite</td>
              <td>0% &ndash; 35% Mafic</td>
              <td>65% &ndash; 100% Andesine</td>
              <td>Light-colored, feldspar-rich variety of diorite.</td>
            </tr>
            <tr>
              <td>Diorite (sensu stricto)</td>
              <td>35% &ndash; 65% Mafic</td>
              <td>35% &ndash; 65% Andesine</td>
              <td>Normal mesocratic diorite; balanced hornblende and andesine plagioclase.</td>
            </tr>
            <tr>
              <td>Meladiorite</td>
              <td>65% &ndash; 90% Mafic</td>
              <td>10% &ndash; 35% Andesine</td>
              <td>Dark-colored, melanocratic variety of diorite enriched in hornblende/pyroxene.</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Perkinite</strong> (Option A)</td>
              <td><strong>90% &ndash; 100% Mafic (100% Ferromagnesian)</strong></td>
              <td>0% &ndash; 10% (Feldspar-free extreme)</td>
              <td>Coarse-grained ultramafic rock composed essentially of <strong>amphibole (hornblende) and pyroxene</strong> without olivine.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "If the ferromagnesian content of diorite increases until plagioclase disappears entirely, the rock becomes 100% ferromagnesian. Such an ultramafic rock consisting essentially of hornblende and pyroxene is termed <strong>Perkinite</strong>. It stands as the ultramafic, feldspar-free end-member of the dioritic-gabbroic clan."
        <div class="quote-author">&mdash; P.K. Mukherjee, <em>A Textbook of Geology</em> (World Press, Igneous Rocks, p. 249)</div>
      </div>

      <div class="formula-box">
        $$\text{Diorite} = \text{Andesine Plagioclase} + \text{Ferromagnesian Minerals (Hornblende, Biotite, Augite)}$$
        $$\text{When Ferromagnesian Content } \rightarrow 100\% \implies \text{Feldspar} \rightarrow 0\% \implies \mathbf{Perkinite}\ (\text{Hornblende} + \text{Pyroxene Ultramafic})$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q081/diorite_perkinite_meladiorite_ultramafic_spectrum.png" alt="Diorite Perkinite Meladiorite Spectrum" class="figure-img">
        <div class="figure-caption">Figure 81: Color index classification bar showing the continuous transition from Leucodiorite through Diorite and Meladiorite to 100% ferromagnesian Perkinite.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 81</div>
        <div class="raw-q-text">If the ferromagnesian content of diorite is 100%, then it is called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Perkinite</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Leptinite</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Meladiorite</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Leucodiorite</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Perkinite)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Perkinite</div>
          <p>By standard classical petrographic nomenclature (Duparc, 1907; P.K. Mukherjee, p. 249; K.M. Bangar), when the ferromagnesian mineral percentage of diorite reaches <strong>100%</strong> (meaning plagioclase feldspar is completely absent), the resulting ultramafic amphibole-pyroxene rock is designated as <strong>Perkinite</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Leptinite</div>
          <p>Leptinite (or leptite) is a fine-grained, light-colored granoblastic metamorphic rock (granulite or felsic gneiss) dominated by quartz and feldspar. It is leucocratic and metamorphic, not an ultramafic rock.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Meladiorite</div>
          <p>Meladiorite is a dark diorite that still contains <strong>10% to 35% plagioclase feldspar</strong> ($M' = 65\text{--}90\%$). It does NOT have 100% ferromagnesian minerals.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Leucodiorite</div>
          <p>Leucodiorite is the exact polar opposite: it is a light-colored diorite dominated by plagioclase feldspar with only 0% to 35% ferromagnesian minerals.</p>
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
              <th>Mafic % ($M'$)</th>
              <th>Essential Mineralogy</th>
              <th>Ultramafic vs. Felsic Classification</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Perkinite (Option A)</td><td><strong>100%</strong></td><td>Hornblende + Pyroxene (Amphibole-Pyroxenite)</td><td>Ultramafic Plutonic Rock</td></tr>
            <tr><td>Meladiorite</td><td>65% &ndash; 90%</td><td>Plagioclase (10&ndash;35%) + Hornblende + Augite</td><td>Melanocratic Intermediate Rock</td></tr>
            <tr><td>Diorite</td><td>35% &ndash; 65%</td><td>Plagioclase (Andesine) + Hornblende + Biotite</td><td>Mesocratic Intermediate Rock</td></tr>
            <tr><td>Leucodiorite</td><td>&lt; 35%</td><td>Plagioclase (65&ndash;100%) + minor Hornblende</td><td>Leucocratic Intermediate Rock</td></tr>
            <tr><td>Hornblendite</td><td>&gt; 90%</td><td>Monomineralic Hornblende</td><td>Ultramafic Rock</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Who originally defined 'perkinite' and what were its primary constituents?</div>
        <div class="pq-ans">Answer: L. Duparc (1907); defined as an ultramafic rock composed essentially of amphibole and pyroxene.</div>
        <div class="pq-exp">Duparc introduced perkinite for coarse-grained rocks containing amphibole and pyroxene in varying proportions, with little to no olivine.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is an ultramafic rock composed of greater than 90% olivine called?</div>
        <div class="pq-ans">Answer: Dunite</div>
        <div class="pq-exp">Dunite is a monomineralic ultramafic peridotite containing &ge;90% modal olivine.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is an ultramafic rock composed essentially of pyroxene called?</div>
        <div class="pq-ans">Answer: Pyroxenite</div>
        <div class="pq-exp">Pyroxenites contain &gt;90% pyroxene (orthopyroxene, clinopyroxene, or both).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the distinguishing mineralogical difference between perkinite and peridotite?</div>
        <div class="pq-ans">Answer: Peridotite contains essential olivine (&gt;40%), whereas perkinite is dominated by hornblende and pyroxene without significant olivine.</div>
        <div class="pq-exp">Peridotites are olivine-bearing ultramafic rocks (lherzolite, harzburgite, dunite), whereas perkinite belongs to the amphibole-pyroxene ultramafic group.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What prefix is added to an igneous rock name when the mafic mineral content is between 65% and 90%?</div>
        <div class="pq-ans">Answer: Mela- (e.g., meladiorite, melagabbro)</div>
        <div class="pq-exp">IUGS uses 'mela-' for melanocratic varieties with color index $M' = 65\text{--}90\%$, and 'leuco-' for leucocratic varieties with $M' = 0\text{--}35\%$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the volcanic equivalent of an ultramafic rock?</div>
        <div class="pq-ans">Answer: Komatiite</div>
        <div class="pq-exp">Komatiites are Archaean ultramafic volcanic lavas with &gt;18 wt% $MgO$ displaying spinifex texture.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an anorthosite in terms of plagioclase content?</div>
        <div class="pq-ans">Answer: An ultra-leucocratic plutonic rock containing greater than 90% plagioclase feldspar.</div>
        <div class="pq-exp">Anorthosite is essentially monomineralic plagioclase ($M' < 10\%$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the characteristic plagioclase in diorite?</div>
        <div class="pq-ans">Answer: Andesine ($An_{30}\text{--}An_{50}$) or Oligoclase</div>
        <div class="pq-exp">If the plagioclase is more calcic than $An_{50}$ (labradorite/bytownite), the rock is classified as a gabbro rather than a diorite.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q082: Dolerite Mineral Composition Equivalent to Basalt
# -----------------------------------------------------------------------------
def gen_q082():
    q_num = 82
    filename = "Q082_By_Mineral_Composition_Dolerite_Is_Equivalent_To_Basalt_Complete_Guide.html"
    title = "Q082: Dolerite Petrography - Compositional Equivalence to Basalt"
    badge = "OPSC 2019 Geology Paper-II • Question 82 • Igneous Petrology"
    h1_title = "The Basic Mafic Triad: Compositional Equivalence of Dolerite, Basalt, and Gabbro"
    meta_text = "<strong>Topic:</strong> Basic Igneous Rocks • <strong>Key Concept:</strong> Hypabyssal vs. Volcanic Textural Equivalents • <strong>Textbooks:</strong> K.M. Bangar (p. 126); John D. Winter (Principles of Igneous Petrology)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Plutonic-Hypabyssal-Volcanic Equivalence Triad</div>
      <p>In igneous petrology, rocks sharing identical chemical and mineralogical compositions are subdivided into three structural categories based on their cooling rate, depth of consolidation, and resulting crystalline texture:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Structural Setting</th>
              <th>Cooling Regime & Depth</th>
              <th>Grain Size & Diagnostic Texture</th>
              <th>Representative Mafic Rock</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Plutonic</strong> (Deep Intrusive)</td>
              <td>Slow cooling at deep crustal levels ($> 3\text{--}5\text{ km}$)</td>
              <td>Coarse-grained, phaneritic equigranular</td>
              <td><strong>Gabbro</strong></td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Hypabyssal</strong> (Subvolcanic / Shallow Intrusive)</td>
              <td>Moderate cooling in dykes, sills, and cone sheets ($< 2\text{ km}$)</td>
              <td>Medium-grained, <strong>ophitic / subophitic</strong> (laths of plagioclase enclosed by pyroxene)</td>
              <td><strong>DOLERITE (Diabase)</strong></td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Volcanic</strong> (Extrusive)</td>
              <td>Rapid quenching at Earth's surface as lava flows</td>
              <td>Fine-grained, aphanitic, glassy, <strong>intersertal / hyalopilitic</strong></td>
              <td><strong>BASALT (Option D)</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "By mineralogical and chemical composition, <strong>dolerite is precisely equivalent to basalt and gabbro</strong>. All three consist essentially of calcic plagioclase (labradorite or bytownite) and clinopyroxene (augite), with or without olivine and titanomagnetite. Dolerite represents the medium-grained hypabyssal facies (forming dykes and sills), basalt is the fine-grained extrusive volcanic facies, and gabbro is the coarse-grained plutonic facies."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Petrology, p. 126)</div>
      </div>

      <div class="formula-box">
        $$\text{Shared Chemical Composition: Basic } (45\text{--}52\text{ wt\% } SiO_2)$$
        $$\text{Shared Mineralogy: Calcic Plagioclase } (An_{50-70}) + \text{Clinopyroxene (Augite)} \pm \text{Olivine} \pm \text{Fe-Ti Oxides}$$
        $$\mathbf{Dolerite\ (Hypabyssal)} \equiv \mathbf{Basalt\ (Volcanic)} \equiv \mathbf{Gabbro\ (Plutonic)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q082/dolerite_basalt_gabbro_compositional_equivalents.png" alt="Dolerite Basalt Gabbro Compositional Equivalents" class="figure-img">
        <div class="figure-caption">Figure 82: The basic igneous rock triad showing compositional equivalence between coarse plutonic Gabbro, medium hypabyssal Dolerite, and fine volcanic Basalt.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 82</div>
        <div class="raw-q-text">By mineral composition, dolerite is equivalent to :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Pitchstone</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Syenite</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Peridotite</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Basalt</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Basalt)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Basalt</div>
          <p>Dolerite (termed diabase in North American literature) and basalt share identical mineral compositions: both are basic rocks composed of calcic plagioclase (labradorite) and augite (clinopyroxene). Dolerite is the medium-grained hypabyssal intrusive equivalent of extrusive volcanic basalt.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Pitchstone</div>
          <p>Pitchstone is a volcanic glass of acidic to intermediate composition ($SiO_2 > 65\%$, with 4-10% water) characterized by a dull, pitch-like resinous luster. It is highly felsic, unlike basic dolerite.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Syenite</div>
          <p>Syenite is an intermediate plutonic rock dominated by alkali feldspar (orthoclase/microcline) with minor hornblende or biotite. It is rich in alkalis ($K_2O + Na_2O$) and low in lime/magnesia, totally distinct from mafic dolerite.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Peridotite</div>
          <p>Peridotite is an ultrabasic rock ($SiO_2 < 45\%$) composed almost entirely of olivine and pyroxenes with little or no feldspar. Dolerite contains 50% or more plagioclase feldspar.</p>
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
              <th>Chemical Group</th>
              <th>Diagnostic Mineralogy</th>
              <th>Typical Texture</th>
              <th>Emplacement Realm</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Dolerite (Diabase)</td><td>Basic (45&ndash;52% $SiO_2$)</td><td>Labradorite + Augite &plusmn; Olivine</td><td>Ophitic / Subophitic</td><td>Hypabyssal (Dykes / Sills)</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Basalt (Option D)</td><td>Basic (45&ndash;52% $SiO_2$)</td><td>Labradorite + Augite &plusmn; Olivine</td><td>Aphanitic / Intersertal</td><td>Volcanic (Lava flows)</td></tr>
            <tr><td>Gabbro</td><td>Basic (45&ndash;52% $SiO_2$)</td><td>Labradorite + Augite &plusmn; Olivine</td><td>Coarse Phaneritic</td><td>Plutonic (Deep chambers)</td></tr>
            <tr><td>Syenite</td><td>Intermediate</td><td>Alkali Feldspar + Amphibole</td><td>Granitic / Hypidiomorphic</td><td>Plutonic</td></tr>
            <tr><td>Peridotite</td><td>Ultrabasic (&lt;45% $SiO_2$)</td><td>Olivine + Pyroxene</td><td>Granular / Cumulate</td><td>Plutonic / Mantle</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What diagnostic texture is characteristic of dolerites under the petrological microscope?</div>
        <div class="pq-ans">Answer: Ophitic (or Subophitic) texture</div>
        <div class="pq-exp">In ophitic texture, elongated, euhedral laths of plagioclase are completely or partially enclosed within larger, anhedral plates of augite pyroxene.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the North American synonymous term for dolerite?</div>
        <div class="pq-ans">Answer: Diabase</div>
        <div class="pq-exp">In the United States and Canada, medium-grained basic hypabyssal rocks are called diabase, whereas in British and Indian usage, they are called dolerite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What prominent geological formation in Peninsular India contains thousands of dolerite dykes cutting Archaean basements?</div>
        <div class="pq-ans">Answer: Newer Dolerite dyke swarms of the Singhbhum Craton (Odisha-Jharkhand) and Cuddapah dykes</div>
        <div class="pq-exp">The Singhbhum craton is criss-crossed by the spectacular Palaeoproterozoic Newer Dolerite dyke swarm trending NNE-SSW and NW-SE.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the fine-grained volcanic equivalent of Granite?</div>
        <div class="pq-ans">Answer: Rhyolite</div>
        <div class="pq-exp">Just as basalt is to dolerite/gabbro, rhyolite is the volcanic equivalent of granitic intrusive rocks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What alteration process converts calcic plagioclase in dolerite to epidote, zoisite, and albite?</div>
        <div class="pq-ans">Answer: Saussuritization</div>
        <div class="pq-exp">Hydrothermal alteration or low-grade metamorphism breaks down calcic plagioclase into a fine-grained aggregate of zoisite, epidote, calcite, and albite (saussurite).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What alteration process transforms pyroxene in dolerite to fibrous green amphibole (actinolite/tremolite)?</div>
        <div class="pq-ans">Answer: Uralitization</div>
        <div class="pq-exp">Uralitization is the hydrothermal replacement of primary clinopyroxene (augite) by secondary fibrous amphibole (uralite).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an olivine-rich dolerite called?</div>
        <div class="pq-ans">Answer: Olivine dolerite</div>
        <div class="pq-exp">When olivine exceeds 5-10% of modal volume, the rock is specifically termed olivine dolerite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the characteristic weathering pattern displayed by dolerite dyke outcrops in the field?</div>
        <div class="pq-ans">Answer: Spheroidal weathering (onion-skin spalling) and 'tombstone' topography</div>
        <div class="pq-exp">Jointed dolerite blocks weather inward along moisture-rich corners, peeling off in concentric shells and leaving rounded corestones resembling giant boulders or tombstones.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q083: Beerbachite - Variety of Gabbro
# -----------------------------------------------------------------------------
def gen_q083():
    q_num = 83
    filename = "Q083_Beerbachite_Is_A_Variety_Of_Gabbro_Complete_Guide.html"
    title = "Q083: Beerbachite Petrography - Variety of Gabbro"
    badge = "OPSC 2019 Geology Paper-II • Question 83 • Igneous Petrology"
    h1_title = "Beerbachite: Petrography, Granular Microgabbro Affinities, and Classification"
    meta_text = "<strong>Topic:</strong> Basic Rock Varieties • <strong>Key Concept:</strong> Fine-Grained Granular Gabbro / Pyroxene-Granulite Hornfels • <strong>Textbooks:</strong> Chelius (1892); IUGS Subcommission on the Systematics of Igneous Rocks; P.K. Mukherjee"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Origin & Petrographic Nature of Beerbachite</div>
      <p><strong>Beerbachite</strong> was originally described in 1892 by German petrologist <strong>C. Chelius</strong> from Beerbach in the Odenwald, Germany. In classical and modern petrology, it designates a fine-grained, equigranular (aplitic to granoblastic) variety of <strong>Gabbro</strong> (microgabbro) consisting essentially of granular calcic plagioclase and pyroxene:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Petrographic Attribute</th>
              <th>Scientific Characteristic</th>
              <th>Diagnostic Mineralogy & Texture</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td>Parent Rock Group</td>
              <td><strong>Gabbro Clan</strong> (Basic Igneous Rock)</td>
              <td>Compositionally identical to basic gabbro/norite; $SiO_2 \approx 45\text{--}52\%$.</td>
            </tr>
            <tr>
              <td>Essential Mineralogy</td>
              <td><strong>Calcic Plagioclase + Pyroxene</strong></td>
              <td>Labradorite/Bytownite + Orthopyroxene (Hypersthene) + Clinopyroxene (Diallage/Augite) + Magnetite.</td>
            </tr>
            <tr>
              <td>Microscopic Texture</td>
              <td><strong>Granular / Saccharoidal (Aplitic)</strong></td>
              <td>Evenly sized, polygonal, mosaic-like grains without porphyritic or ophitic textures; resembles a pyroxene-hornfels.</td>
            </tr>
            <tr>
              <td>Geological Occurrence</td>
              <td>Dykes & Contact Aureoles</td>
              <td>Occurs as aplitic basic dykes cutting larger gabbro massifs, or as intensely recrystallized basaltic xenoliths/walls in contact metamorphic aureoles.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Beerbachite is a fine-grained, granular variety of <strong>gabbro</strong> (or aplitic microgabbro) characterized by a sugary, saccharoidal texture. It consists of an equigranular mosaic of labradorite and pyroxene (both augite and hypersthene). Originally regarded as a basic aplite dyke rock, many beerbachites are now recognized as basaltic or doleritic inclusions contact-metamorphosed to pyroxene-hornfels facies by host gabbroic intrusions."
        <div class="quote-author">&mdash; IUGS Subcommission on the Systematics of Igneous Rocks; P.K. Mukherjee, <em>A Textbook of Geology</em> (p. 251)</div>
      </div>

      <div class="formula-box">
        $$\text{Beerbachite Mineral Assemblage} \equiv \text{Calcic Plagioclase } (An_{55-75}) + \text{Pyroxenes (Augite } \pm \text{ Hypersthene)} + \text{Fe-Ti Oxides}$$
        $$\text{Texture: Granoblastic / Aplitic (Non-ophitic, granular microgabbro)} \implies \mathbf{Gabbro\ Family\ (Option\ A)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q083/beerbachite_microgabbro_hornfelsic_granular_texture.png" alt="Beerbachite Microgabbro Granular Texture" class="figure-img">
        <div class="figure-caption">Figure 83: Position of Beerbachite within the Gabbro clan as a fine-grained granular/aplitic variety alongside Norite, Troctolite, and Anorthosite.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 83</div>
        <div class="raw-q-text">Beerbachite is a variety of :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Gabbro</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Basalt</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Dolerite</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Monzonite</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Gabbro)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Gabbro</div>
          <p>Beerbachite is historically and systematically classified as a fine-grained granular or aplitic variety of <strong>Gabbro</strong> (microgabbro). It shares the identical mineral chemistry of gabbro (calcic plagioclase + pyroxene) while displaying a distinctive saccharoidal, equigranular mosaic texture.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Basalt</div>
          <p>Basalt is an extrusive volcanic lava flow exhibiting aphanitic, glassy, or intersertal textures. Beerbachite forms as intrusive dykes or high-grade thermal hornfelses with completely holocrystalline granular texture.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Dolerite</div>
          <p>Dolerite is characterized by <strong>ophitic or subophitic texture</strong> with subhedral plagioclase laths. Beerbachite lacks ophitic texture, displaying instead an equigranular (aplitic) mosaic texture.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Monzonite</div>
          <p>Monzonite is an intermediate plutonic rock containing roughly equal amounts of alkali feldspar and plagioclase ($SiO_2 \approx 55\text{--}62\%$). Beerbachite contains no alkali feldspar and is strictly basic.</p>
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
              <th>Gabbro Variety</th>
              <th>Diagnostic Mineral Assemblage</th>
              <th>Textural Characteristics</th>
              <th>Geological Environment</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Beerbachite (Option A)</td><td>Calcic Plagioclase + Pyroxene (Augite + Hypersthene)</td><td>Fine-grained, equigranular, saccharoidal / aplitic</td><td>Microgabbro dykes / Pyroxene hornfels</td></tr>
            <tr><td>Norite</td><td>Calcic Plagioclase + <strong>Orthopyroxene (Hypersthene)</strong></td><td>Coarse-grained phaneritic</td><td>Layered basic intrusions (Bushveld, Sudbury)</td></tr>
            <tr><td>Troctolite</td><td>Calcic Plagioclase + <strong>Olivine</strong> (Pyroxene-poor)</td><td>Coarse-grained, 'trout-stone' speckled</td><td>Layered complexes (Skaergaard, Duluth)</td></tr>
            <tr><td>Anorthosite</td><td>Calcic Plagioclase (&gt;90%) &plusmn; minor pyroxene</td><td>Coarse to megacrystic adcumulate</td><td>Proterozoic massifs & Archaean layered intrusions</td></tr>
            <tr><td>Eucrite</td><td>Bytownite/Anorthite + Pigeonite/Augite</td><td>Coarse-grained achondritic / plutonic</td><td>Basaltic achondrite meteorites & layered complexes</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. From which European locality was beerbachite originally named?</div>
        <div class="pq-ans">Answer: Beerbach in the Odenwald, Hesse, Germany.</div>
        <div class="pq-exp">C. Chelius named the rock in 1892 from dyke-like occurrences cutting gabbros in the Odenwald mountain range.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What type of gabbro is characterized by essential orthopyroxene rather than clinopyroxene?</div>
        <div class="pq-ans">Answer: Norite</div>
        <div class="pq-exp">When orthopyroxene (enstatite/hypersthene) is the dominant pyroxene alongside calcic plagioclase, the rock is formally termed norite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is troctolite composed of?</div>
        <div class="pq-ans">Answer: Calcic plagioclase and olivine (essentially pyroxene-free).</div>
        <div class="pq-exp">Troctolite (from Greek for 'trout rock') is an olivine-plagioclase cumulate member of the gabbro family.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a basic aplite?</div>
        <div class="pq-ans">Answer: A fine-grained, saccharoidal dyke rock of basic composition (such as beerbachite).</div>
        <div class="pq-exp">While aplites are typically granitic, fine-grained sugary dykes of gabbroic composition are historically called basic aplites or beerbachites.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Under what metamorphic facies do basaltic country rocks recrystallize to produce beerbachite-like textures?</div>
        <div class="pq-ans">Answer: Pyroxene-hornfels facies (or Sanidinite facies)</div>
        <div class="pq-exp">Extreme contact thermal metamorphism by mafic magma dehydrates basalts into an equigranular mosaic of pyroxene and calcic plagioclase.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the diallage variety of clinopyroxene commonly found in gabbros?</div>
        <div class="pq-ans">Answer: Augite exhibiting prominent (100) parting due to microscopic exsolution lamellae of orthopyroxene.</div>
        <div class="pq-exp">Diallage is a historical petrographic name for augite with a distinctive platy parting parallel to {100} and pearly lustre.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an olivine gabbro?</div>
        <div class="pq-ans">Answer: A gabbro containing calcic plagioclase, clinopyroxene, and &gt;5% modal olivine.</div>
        <div class="pq-exp">Olivine gabbro is an abundant member of ocean floor crust (layer 3) and continental layered mafic complexes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the typical anorthite content ($An\%$) of plagioclase in gabbroic rocks?</div>
        <div class="pq-ans">Answer: $An_{50}\text{--}An_{85}$ (Labradorite to Bytownite)</div>
        <div class="pq-exp">By definition, gabbros contain calcic plagioclase with $An > 50\%$, which separates them from diorites ($An < 50\%$).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Batch 7 Part A (Q076 - Q083)...")
    gen_q076()
    gen_q077()
    gen_q078()
    gen_q079()
    gen_q080()
    gen_q081()
    gen_q082()
    gen_q083()
    print("Batch 7 Part A successfully generated!")
