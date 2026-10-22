#!/usr/bin/env python3
"""
Q088 Generator: Quartz Monzonite in IUGS QAPF Classification
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q088():
    title = r"Q088: Igneous Petrology: IUGS QAPF Classification of Quartz Monzonite | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & IUGS Classification"
    h1_title = "Q088: Quartz Monzonite: IUGS QAPF Field 8* Definition & Petrography"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 88<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 2: Classification of Igneous Rocks, pp. 27–31, Fig. 2-2); A. Streckeisen (1976, <em>Earth-Science Reviews</em>, "Classification and nomenclature of igneous rocks"); R.W. Le Maitre, <em>Igneous Rocks: A Classification and Glossary of Terms (IUGS)</em>; K.M. Bangar, <em>Principles of Engineering Geology</em> (p. 165)."""

    part1 = r"""
  <!-- CARD 1: IUGS QAPF CLASSIFICATION AND FIELD 8* DEFINITION -->
  <div class="card">
    <div class="card-header bg-blue">1. The IUGS QAPF Plutonic Classification & Field 8* (Quartz Monzonite)</div>
    <div class="card-body">
      <p>
        The standardized international system for classifying plutonic igneous rocks containing less than $90\%$ mafic minerals ($M' < 90\%$) was established by the <strong>IUGS Subcommission on the Systematics of Igneous Rocks</strong> (Streckeisen, 1976; Le Maitre, 2002).
      </p>
      <p>
        Classification is performed on the basis of the modal proportions of three light-colored felsic mineral groups, normalized to $100\%$:
      </p>
      <ul>
        <li><strong>Q:</strong> Quartz ($\text{SiO}_2$) and its polymorphs (tridymite, cristobalite).</li>
        <li><strong>A:</strong> Alkali Feldspar (potassium feldspar: orthoclase, microcline, sanidine, perthite; and sodic plagioclase albite with $\text{An}_{00\text{--}05}$).</li>
        <li><strong>P:</strong> Plagioclase Feldspar (all plagioclase with compositions from oligoclase to anorthite, $\text{An}_{05\text{--}100}$).</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q88/winter_p28_quartz_monzonite_qapf.png" alt="IUGS QAPF Plutonic Classification Diagram from Winter">
        <div class="figure-caption">
          <strong>Figure 88.1 — IUGS QAPF Plutonic Diagram & Position of Field 8* (Quartz Monzonite):</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 2). Highlighting Field 8*, defined by $Q = 5\text{--}20\%$ and roughly equal proportions of alkali feldspar and plagioclase ($P/(A+P) = 35\text{--}65\%$).
        </div>
      </div>

      <h4>Strict Mathematical Definition of Field 8* (Quartz Monzonite)</h4>
      <div class="formula-box">
        <strong>IUGS Criteria for Quartz Monzonite (Field 8*):</strong><br>
        $$\mathbf{\text{Quartz Parameter:}} \quad \mathbf{5\% \le \frac{Q}{Q + A + P} \le 20\%}$$<br>
        $$\mathbf{\text{Plagioclase Ratio:}} \quad \mathbf{35\% \le \frac{P}{A + P} \le 65\%} \quad (\mathbf{\text{Approximately equal amounts of A and P!}})$$
      </div>
      <p>
        If quartz exceeds $20\%$ ($Q > 20\%$), the rock enters the true granite realm (Field 3b: <strong>Monzogranite</strong>). If quartz falls below $5\%$ ($Q < 5\%$), it is a true <strong>Monzonite</strong> (Field 8).
      </p>
    </div>
  </div>

  <!-- CARD 2: ADAMELLITE SYNONYMY AND PETROGRAPHIC CHARACTERISTICS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Historical Terminology: The Adamellite Problem & Petrography</div>
    <div class="card-body">
      <p>
        In classical 19th- and 20th-century petrology, this rock was widely designated as <strong>Adamellite</strong> (named by A. Cathrein in 1890 from Mount Adamello in the Italian Alps).
      </p>
      <ul>
        <li><strong>The British Tradition:</strong> British and Commonwealth geologists historically used "adamellite" for any granitic rock containing approximately equal proportions of plagioclase and orthoclase with significant quartz ($>10\%$).</li>
        <li><strong>The IUGS Recommendation:</strong> Because the term "adamellite" had been applied ambiguously to both quartz monzonites ($Q = 5\text{--}20\%$) and monzogranites ($Q = 20\text{--}60\%$), the IUGS officially discarded the name <em>adamellite</em>, replacing it with the unambiguous, systematic term <strong>Quartz Monzonite</strong>.</li>
      </ul>

      <h4>Essential Mineralogy and Microscopic Fabric</h4>
      <ul>
        <li><strong>Alkali Feldspar ($35\text{--}65\%$ of total feldspar):</strong> Typically pink to buff perthitic orthoclase or microcline displaying Carlsbad or tartan twinning.</li>
        <li><strong>Plagioclase ($35\text{--}65\%$ of total feldspar):</strong> Sodic plagioclase (oligoclase to andesine, $\text{An}_{20\text{--}40}$), frequently showing well-developed polysynthetic albite twinning and normal compositional zoning.</li>
        <li><strong>Quartz ($5\text{--}20\%$ of felsics):</strong> Anhedral, clear grains occupying interstitial spaces between earlier-crystallized subhedral feldspar crystals.</li>
        <li><strong>Mafic Minerals ($M' = 10\text{--}25\%$):</strong> Biotite mica and calcic amphibole (hornblende), with accessory titanite (sphene), apatite, zircon, and magnetite.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: BOUNDARY DIFFERENTIATION FROM ADJACENT QAPF FIELDS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Diagnostic Demarcation from Adjacent QAPF Plutonic Fields</div>
    <div class="card-body">
      <p>
        Understanding the boundary coordinates of Field 8* is critical for solving classification questions:
      </p>
      <ul>
        <li><strong>Field 8* vs. Field 3b (Monzogranite):</strong> Both have co-equal alkali feldspar and plagioclase ($P/(A+P) = 35\text{--}65\%$), but Monzogranite contains <strong>$> 20\%$ quartz ($Q = 20\text{--}60\%$)</strong>, making it a true granite.</li>
        <li><strong>Field 8* vs. Field 9* (Quartz Monzodiorite / Quartz Monzogabbro):</strong> In Field 9*, plagioclase clearly dominates over alkali feldspar ($P/(A+P) = 65\text{--}90\%$). If plagioclase is sodic ($\text{An} < 50$), it is Quartz Monzodiorite; if calcic ($\text{An} > 50$), it is Quartz Monzogabbro.</li>
        <li><strong>Field 8* vs. Field 10* (Quartz Norite / Quartz Gabbro):</strong> In Field 10*, plagioclase comprises $>90\%$ of total feldspar ($P/(A+P) > 90\%$). A <em>Quartz Norite</em> is a gabbroic rock where orthopyroxene (hypersthene) is the dominant mafic phase, and alkali feldspar is virtually absent ($< 10\%$).</li>
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
        <div class="q-num">Question 88</div>
        <div class="q-text">A plutonic rock consisting of approximately equal amounts of alkali feldspar and plagioclase and with essential quartz (5%-20% of felsic minerals) but not enough to make the rock a granite is termed as :</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Quartz Monzonite</div>
          <div class="opt-node">(B) Quartz Monzodiorite</div>
          <div class="opt-node">(C) Quartz Norite</div>
          <div class="opt-node">(D) Quartz Monzogabbro</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (A)</div>
        <div><strong>Quartz Monzonite:</strong> Occupies Field 8* of the IUGS QAPF classification, characterized by roughly equal proportions of alkali feldspar and plagioclase ($P/(A+P) = 35\text{--}65\%$) and 5% to 20% modal quartz.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option correct">
        <div class="opt-title">(A) Quartz Monzonite — CORRECT</div>
        <p>
          <em>Quartz Monzonite</em> is the exact, canonical definition established by the IUGS Subcommission (Streckeisen, 1976; Le Maitre, 2002; Winter, 2014, p. 28) for a plutonic rock containing <strong>approximately equal amounts of alkali feldspar and plagioclase ($P/(A+P) = 35\text{--}65\%$) and essential quartz between 5% and 20% of total felsic minerals</strong>. Because quartz is $<20\%$, it lacks sufficient silica to be classified as a true granite.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Quartz Monzodiorite — INCORRECT</div>
        <p>
          In <em>Quartz Monzodiorite</em> (Field 9*), plagioclase is heavily dominant over alkali feldspar, accounting for <strong>65% to 90% of total feldspars</strong> ($P/(A+P) = 65\text{--}90\%$). The feldspars are NOT in approximately equal amounts.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Quartz Norite — INCORRECT</div>
        <p>
          A <em>Quartz Norite</em> plots in Field 10* of the QAPF diagram where plagioclase constitutes <strong>greater than 90% of all feldspars</strong> ($P/(A+P) > 90\%$), and alkali feldspar is virtually absent ($<10\%$). Furthermore, it is a basic rock dominated by calcic plagioclase ($\text{An} > 50$) and orthopyroxene (hypersthene).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Quartz Monzogabbro — INCORRECT</div>
        <p>
          Like Quartz Monzodiorite, <em>Quartz Monzogabbro</em> occupies Field 9* with plagioclase comprising <strong>65% to 90% of total feldspars</strong>, with the specific distinction that the plagioclase is calcic ($\text{An} > 50$). It does not possess equal amounts of alkali feldspar and plagioclase.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">IUGS QAPF Classification Matrix: Intermediate to Felsic Plutonic Rocks</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>IUGS Field</th>
            <th>Plutonic Rock Name</th>
            <th>Quartz Content ($Q\%$)</th>
            <th>Plagioclase Ratio $\frac{P}{A+P} \times 100\%$</th>
            <th>Typical Plagioclase Composition</th>
            <th>Dominant Mafic Minerals</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Field 3b</strong></td>
            <td><strong>Monzogranite (True Granite)</strong></td>
            <td>$20\text{--}60\%$ (High Quartz!)</td>
            <td>$35\text{--}65\%$ (Co-equal Feldspars)</td>
            <td>Oligoclase ($\text{An}_{15\text{--}30}$)</td>
            <td>Biotite $\pm$ Muscovite</td>
          </tr>
          <tr>
            <td><strong>Field 8*</strong></td>
            <td><strong>QUARTZ MONZONITE</strong></td>
            <td><strong>$5\text{--}20\%$ (Essential Quartz)</strong></td>
            <td><strong>$35\text{--}65\%$ (Approximately Equal!)</strong></td>
            <td><strong>Oligoclase / Andesine ($\text{An}_{20\text{--}40}$)</strong></td>
            <td><strong>Hornblende + Biotite</strong></td>
          </tr>
          <tr>
            <td><strong>Field 8</strong></td>
            <td><strong>Monzonite (sensu stricto)</strong></td>
            <td>$0\text{--}5\%$ (Quartz-poor)</td>
            <td>$35\text{--}65\%$ (Co-equal Feldspars)</td>
            <td>Andesine ($\text{An}_{30\text{--}45}$)</td>
            <td>Augite + Hornblende + Biotite</td>
          </tr>
          <tr>
            <td><strong>Field 9*</strong></td>
            <td><strong>Quartz Monzodiorite</strong></td>
            <td>$5\text{--}20\%$</td>
            <td>$65\text{--}90\%$ (Plagioclase dominant)</td>
            <td>Oligoclase / Andesine ($\text{An} < 50$)</td>
            <td>Hornblende + Biotite</td>
          </tr>
          <tr>
            <td><strong>Field 9*</strong></td>
            <td><strong>Quartz Monzogabbro</strong></td>
            <td>$5\text{--}20\%$</td>
            <td>$65\text{--}90\%$ (Plagioclase dominant)</td>
            <td>Labradorite ($\text{An} > 50$)</td>
            <td>Clinopyroxene (Augite)</td>
          </tr>
          <tr>
            <td><strong>Field 10*</strong></td>
            <td><strong>Quartz Norite / Quartz Gabbro</strong></td>
            <td>$5\text{--}20\%$</td>
            <td>$> 90\%$ (Plagioclase only; $A < 10\%$)</td>
            <td>Labradorite / Bytownite ($\text{An} > 50$)</td>
            <td><strong>Orthopyroxene (Norite)</strong> / Cpx (Gabbro)</td>
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
        <div class="p-header">Problem 1: Step-by-Step QAPF Modal Normalization Calculation</div>
        <p>
          A point-count modal analysis of an unknown plutonic rock yields the following raw volume percentages:
          $$\text{Quartz} = 12.0\%, \quad \text{Microcline} = 34.0\%, \quad \text{Plagioclase (An}_{30}) = 36.0\%, \quad \text{Biotite} = 12.0\%, \quad \text{Hornblende} = 4.0\%, \quad \text{Apatite+Magnetite} = 2.0\%$$
          Normalize the felsic minerals to $100\%$ ($Q + A + P$) and determine the exact IUGS classification field.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Normalization:</strong><br>
          1. <strong>Sum of Felsic Minerals ($Q + A + P$):</strong>
          $$\sum_{\text{felsic}} = 12.0 + 34.0 + 36.0 = 82.0\%$$<br>
          2. <strong>Calculate Normalized Felsic Percentages:</strong>
          $$Q' = \frac{12.0}{82.0} \times 100\% = \mathbf{14.63\%}$$<br>
          $$A' = \frac{34.0}{82.0} \times 100\% = \mathbf{41.46\%}$$<br>
          $$P' = \frac{36.0}{82.0} \times 100\% = \mathbf{43.90\%}$$<br>
          Verification: $14.63 + 41.46 + 43.90 = 99.99\% \approx 100\%$.<br><br>
          3. <strong>Calculate Plagioclase Ratio ($P^*$):</strong>
          $$P^* = \frac{P'}{A' + P'} \times 100\% = \frac{43.90}{41.46 + 43.90} \times 100\% = \frac{43.90}{85.36} \times 100\% \approx \mathbf{51.43\%}$$<br>
          4. <strong>Evaluate Against IUGS Criteria:</strong><br>
          - Quartz $Q' = 14.63\%$, which falls strictly within $5\% \le Q \le 20\%$.<br>
          - Plagioclase ratio $P^* = 51.43\%$, which falls strictly within $35\% \le P^* \le 65\%$.<br>
          <strong>Conclusion:</strong> The rock plots squarely in <strong>Field 8*</strong> and is definitively classified as a <strong>Quartz Monzonite</strong>.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: The Critical Granite Boundary at 20% Quartz</div>
        <p>
          Explain why the IUGS established the boundary between quartz-bearing intermediate rocks (Field 8* Quartz Monzonite) and true granites (Field 3b Monzogranite) at exactly $20\%$ modal quartz, rather than at $10\%$ or $30\%$.
        </p>
        <div class="p-ans">
          <strong>Eutectic Phase Equilibrium Justification:</strong><br>
          In experimental petrology of the "granite system" ($SiO_2\text{--}NaAlSi_3O_8\text{--}KAlSi_3O_8\text{--}H_2O$ at $P_{H_2O} = 1\text{ to } 5\text{ kbar}$, Tuttle & Bowen, 1958), the ternary eutectic / minimum melt composition contains between <strong>$25\text{ wt}\%$ and $35\text{ wt}\%$ quartz</strong>.<br>
          - True granites ($Q > 20\%$) represent near-eutectic liquids produced by advanced crustal melting or extensive fractional crystallization.<br>
          - Rocks containing $5\text{--}20\%$ quartz are transitional sub-eutectic rocks whose parental melts were not saturated with quartz until very late in their crystallization history. Setting the master boundary at $Q = 20\%$ cleanly separates true eutectic granites from quartz-bearing intermediate plutons.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Distinguishing Quartz Monzodiorite vs. Quartz Monzogabbro</div>
        <p>
          A plutonic rock has $Q = 10\%$, $P = 75\%$, and $A = 15\%$, placing it in Field 9*. State the specific mineralogical test required to determine whether it should be named Quartz Monzodiorite or Quartz Monzogabbro.
        </p>
        <div class="p-ans">
          <strong>Plagioclase Composition Rule ($\text{An}_{50}$):</strong><br>
          According to IUGS rules (Le Maitre, 2002, p. 25):<br>
          - Measure the average anorthite content ($\text{An}\%$) of the plagioclase feldspar using optical extinction methods (Michel-Lévy method) or electron microprobe.<br>
          - If the plagioclase is <strong>sodic ($\text{An} < 50$, oligoclase or andesine)</strong>, the rock is named <strong>Quartz Monzodiorite</strong>.<br>
          - If the plagioclase is <strong>calcic ($\text{An} > 50$, labradorite or bytownite)</strong>, the rock is named <strong>Quartz Monzogabbro</strong>.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Volcanic Equivalent of Quartz Monzonite</div>
        <p>
          Name the volcanic (extrusive) equivalent of a Quartz Monzonite in the IUGS volcanic classification system, and state its position on the Total Alkali-Silica (TAS) diagram.
        </p>
        <div class="p-ans">
          <strong>Extrusive Equivalent:</strong><br>
          - The volcanic equivalent of Quartz Monzonite is <strong>Quartz Latite</strong> (or <strong>Trachyandesite / Trachydacite</strong> on the TAS diagram).<br>
          - On the TAS diagram ($\text{Na}_2\text{O} + \text{K}_2\text{O}$ vs $\text{SiO}_2$), it plots in the intermediate-to-high alkali sector at $\text{SiO}_2 \approx 57\text{--}63\text{ wt}\%$ and total alkalis between $7\%$ and $10\%$.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Tectonic Setting of Quartz Monzonite Plutonism</div>
        <p>
          In what plate tectonic settings do quartz monzonites typically form, and how does their geochemistry differ from island arc tonalites?
        </p>
        <div class="p-ans">
          <strong>Tectonic & Geochemical Environment:</strong><br>
          - <strong>Tectonic Setting:</strong> Quartz monzonites are typical of <strong>mature continental magmatic arcs</strong> (e.g., Sierra Nevada Batholith, USA; Gangdese Arc, Tibet) and <strong>post-collisional extensional collapse regimes</strong>.<br>
          - <strong>Geochemical Contrast:</strong> Primitive island arc magmas (tonalites) are depleted in potassium and enriched in sodium and calcium ($P \gg A, Na_2O \gg K_2O$). In contrast, quartz monzonites involve thick continental crust where assimilation and partial melting of ancient K-rich crustal gneisses enriches the magma in potassium, producing co-equal alkali feldspar and plagioclase ($K_2O \approx Na_2O$).
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: CIPW Normative Calculation of Quartz Monzonite</div>
        <p>
          A rock analysis yields CIPW normative minerals: $\text{Q} = 8.5\%, \text{Or} = 26.0\%, \text{Ab} = 28.5\%, \text{An} = 22.0\%, \text{Di} = 8.0\%, \text{Hy} = 5.0\%$. Calculate its normative QAP coordinates and verify its classification.
        </p>
        <div class="p-ans">
          <strong>Normative Calculation:</strong><br>
          1. $Q = 8.5\%$.<br>
          2. $A = \text{Or} = 26.0\%$.<br>
          3. $P = \text{Ab} + \text{An} = 28.5 + 22.0 = 50.5\%$.<br>
          4. Total Felsic Norm: $\sum = 8.5 + 26.0 + 50.5 = 85.0\%$.<br>
          5. Normalized Quartz: $Q' = \frac{8.5}{85.0} \times 100\% = \mathbf{10.0\%}$ (within $5\text{--}20\%$).<br>
          6. Plagioclase Ratio: $P^* = \frac{50.5}{26.0 + 50.5} \times 100\% = \frac{50.5}{76.5} \times 100\% \approx \mathbf{66.0\%}$ (at the Field 8*/9* boundary).<br>
          This confirms the rock is a transitional <strong>Quartz Monzonite to Quartz Monzodiorite</strong>.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Distinction from Norite and Gabbro</div>
        <p>
          Why is "Quartz Norite" (Option C) completely incompatible with the description "approximately equal amounts of alkali feldspar and plagioclase"?
        </p>
        <div class="p-ans">
          <strong>Fundamental Mineralogical Contradiction:</strong><br>
          - In the IUGS system, any rock bearing the root name <strong>Gabbro, Norite, or Anorthosite</strong> must plot in <strong>Field 10</strong>, which requires that plagioclase constitutes <strong>at least $90\%$ of total feldspar ($P/(A+P) \ge 90\%$)</strong>.<br>
          - Alkali feldspar can never exceed $10\%$. Therefore, a norite can NEVER have "approximately equal amounts of alkali feldspar and plagioclase" ($35\text{--}65\%$).
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Optical Identification of Quartz Monzonite in Hand Specimen</div>
        <p>
          How can a geologist distinguish a Quartz Monzonite from a Granite in a field hand specimen without a microscope?
        </p>
        <div class="p-ans">
          <strong>Field Megascopic Diagnostic Criteria:</strong><br>
          1. <strong>Feldspar Color Contrast:</strong> In hand specimen, two distinctly different feldspars are visible in roughly co-equal quantities: pink/salmon-colored potassium feldspar (orthoclase) and white/grey plagioclase displaying visible striations (twinning) on cleavage faces.<br>
          2. <strong>Quartz Abundance:</strong> Quartz is present as vitreous, smoky grey grains, but comprises only about 1 out of every 10 crystals ($10\text{--}15\%$), appearing distinctly subordinate to the overwhelming mass of interlocking feldspars—unlike true granite where vitreous quartz forms prominent, abundant puddles comprising $25\text{--}35\%$ of the rock surface.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 88, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q088_Quartz_Monzonite_IUGS_QAPF_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q088: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q088()
